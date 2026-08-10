#!/usr/bin/env python
"""Schema resolution for taskmd — turn a config file into the rules the rest of the tool obeys.

The plugin's design rule is *store the forward edge, derive the rest*. This module applies the
same rule to the schema itself: the default schema is written **once**, in
`taskmd/defaults/config.md`, and loaded from there. There are no default values in this file to
disagree with it.

Resolution
----------
A project's `.taskmd/config.md` **replaces** the default; it is not merged with it. So the
config you are reading is your whole schema — the same single-source property the plugin is
built on. A config missing a key is an error naming the key, not a silent fallback.

Task front-matter, by contrast, is permissive: a field the schema does not name is carried and
displayed but never interpreted, so a project can adopt taskmd without rewriting its files.

Usage
-----
  python -m taskmd.schema [project_dir]     print the resolved schema and the task graph

Pure standard library. Console output is ASCII; task content is UTF-8.
"""

import os
import re
import shlex
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(HERE, "defaults", "config.md")
PROJECT_CONFIG = os.path.join(".taskmd", "config.md")

# Fixed vocabulary: each kind is a different traversal in code, so adding one means new code,
# not new config. Their field *names* are configurable; this set is not.
EDGE_KINDS = ("hierarchy", "dependency", "soft")

SCALAR_KEYS = ("id_field", "id_prefix", "id_width", "title_field", "tasks_dir", "status_field")
# Required to be present, permitted to be empty: `none` means the project does not track that
# fact. Absent is still an error — a config replaces the default, so a missing key is a schema
# nobody wrote.
NULLABLE_KEYS = ("deliverables_field", "blocked_status", "value_field", "effort_field",
                 "after_write")
LIST_KEYS = ("open_statuses", "context_fields", "index_columns")
CONFIG_KEYS = SCALAR_KEYS + NULLABLE_KEYS + LIST_KEYS

NULLS = ("", "null", "none", "~")

_BLOCK = re.compile(r"^([A-Za-z_]\w*):[ \t]*(?:#[^\n]*)?\n((?:[ \t]+-[^\n]*\n?)+)", re.M)
_ITEM = re.compile(r"^[ \t]+-[ \t]*(.*)$", re.M)
_SCALAR = re.compile(r"^([A-Za-z_]\w*):[ \t]*([^\n]*)$", re.M)
_COMMENT = re.compile(r"\s+#.*$")
_SEPARATOR = re.compile(r":?-{2,}:?")


class SchemaError(Exception):
    """A config that cannot be trusted. Always names the file and what is wrong with it."""


# --------------------------------------------------------------------- restricted parsing

def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _clean(value):
    return _COMMENT.sub("", value).strip()


def _split_items(raw):
    return [item.strip() for item in raw.split(",") if item.strip()]


def parse_fields(fm):
    """Front-matter text -> {key: str | list}. Block lists and `[a, b]` both give a list."""
    fields = {}
    for key, block in _BLOCK.findall(fm):
        fields[key] = [_clean(item) for item in _ITEM.findall(block) if _clean(item)]
    for key, raw in _SCALAR.findall(fm):
        if key in fields:
            continue  # already taken as a block list
        value = _clean(raw)
        if value.startswith("[") and value.endswith("]"):
            fields[key] = _split_items(value[1:-1])
        elif value.lower() in NULLS:
            fields[key] = ""
        else:
            fields[key] = value
    return fields


def split_front_matter(text):
    """(fields, body). A file with no `---` block yields ({}, whole text)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    rest = text[end + 4:]
    nl = rest.find("\n")
    return parse_fields(text[3:end]), (rest[nl + 1:] if nl != -1 else "")


def _cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def _section(body, heading):
    m = re.search(r"^##[ \t]+" + re.escape(heading) + r"[ \t]*$", body, re.M)
    if not m:
        return None
    tail = body[m.end():]
    nxt = re.search(r"^##[ \t]+", tail, re.M)
    return tail[:nxt.start()] if nxt else tail


def parse_table(body, heading, columns):
    """Rows of the table under `## <heading>` whose header matches `columns`, as dicts.

    A section may hold several tables — the default config explains the edge kinds in one table
    and declares the edges in another. Matching on the header picks the right one instead of
    assuming a position, and an unmatched header is an error rather than a silent empty result.
    """
    section = _section(body, heading)
    if section is None:
        return None  # section absent: legal, means "none declared"

    tables, current = [], []
    for ln in section.splitlines():
        if ln.strip().startswith("|"):
            current.append(ln)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)

    wanted = [c.lower() for c in columns]
    seen = []
    for rows in tables:
        header = _cells(rows[0])
        seen.append(" | ".join(header))
        if [h.lower() for h in header] != wanted:
            continue
        out = []
        for row in rows[1:]:
            cells = _cells(row)
            if all(_SEPARATOR.fullmatch(c) for c in cells if c):
                continue
            if len(cells) != len(columns):
                raise SchemaError("table under '## %s' has a row with %d cells, expected %d: %s"
                                  % (heading, len(cells), len(columns), row.strip()))
            out.append(dict(zip(columns, cells)))
        return out
    raise SchemaError("no table under '## %s' with header %s; found: %s"
                      % (heading, " | ".join(columns), "; ".join(seen) or "no tables"))


# ------------------------------------------------------------------------------ the schema

class Edge(object):
    def __init__(self, field, kind, derives):
        self.field = field
        self.kind = kind
        self.derives = derives  # "" for soft edges

    def __repr__(self):
        return "Edge(%s, %s -> %s)" % (self.field, self.kind, self.derives or "-")


class Schema(object):
    def __init__(self, source, fields, edges, vocabularies, hook=("", [])):
        self.source = source
        # What the project wrote, and the same thing ready to run. The declared string is what
        # any message quotes: it is the line the reader can go and edit, and the resolved one
        # holds an absolute path, which never belongs in output.
        self.after_write, self.after_write_argv = hook
        self.id_field = fields["id_field"]
        self.id_prefix = fields["id_prefix"]
        self.id_width = fields["id_width"]
        self.title_field = fields["title_field"]
        self.tasks_dir = fields["tasks_dir"]
        self.status_field = fields["status_field"]
        self.deliverables_field = fields["deliverables_field"]
        self.blocked_status = fields["blocked_status"]
        self.value_field = fields["value_field"]
        self.effort_field = fields["effort_field"]
        self.open_statuses = fields["open_statuses"]
        self.context_fields = fields["context_fields"]
        self.index_columns = fields["index_columns"]
        self.edges = edges                # {field: Edge}
        self.vocabularies = vocabularies  # {field: [values]}
        self._id_re = re.compile(r"^%s\d{%d}$" % (re.escape(self.id_prefix), self.id_width))
        self._loose_id_re = re.compile(r"^%s\d+$" % re.escape(self.id_prefix))

    @property
    def statuses(self):
        return self.vocabularies[self.status_field]

    @property
    def known_fields(self):
        """Fields this schema interprets. Everything else in a task file is pass-through."""
        named = [self.id_field, self.title_field]
        if self.deliverables_field:
            named.append(self.deliverables_field)
        return named + sorted(self.edges) + sorted(self.vocabularies)

    @property
    def derived_names(self):
        """Names under which computed edges are stored on a task.

        A `hierarchy` or `dependency` edge derives its inverse under a *different* name
        (`parent` -> `children`). A `soft` edge is **symmetric**: it derives under its own name, so
        a link written on one task is visible from the other without being written there too.
        """
        names = []
        for edge in self.edges.values():
            names.append(edge.derives if edge.derives else edge.field)
        return names

    def is_open(self, status):
        return status in self.open_statuses

    def rank(self, field, value):
        """Position of `value` in `field`'s vocabulary — lower is preferred.

        The vocabulary row *is* the ranking, best first; see `## Ordering` in the default config,
        which is the one place the ordering rule is written down. A value that is missing, or not
        in the vocabulary, ranks after every value that is — so an unestimated task still sorts
        and is still listed rather than disappearing from a view.
        """
        values = self.vocabularies.get(field) or []
        return values.index(value) if value in values else len(values)

    def is_id(self, value):
        """Prefix plus **exactly** `id_width` digits.

        The width is enforced here, when a file is read, and not only by `format_id` when a new id
        is composed — which is what the local-markdown binding's *enumerate* rule has always said
        and what the code used to leave unsaid (T-075). So a file whose id is the right shape and
        the wrong width is not quietly a task; `looks_like_id` is how a caller tells that case
        apart from an ordinary Markdown file, and reports it instead of ignoring it.
        """
        return bool(self._id_re.match(value or ""))

    def looks_like_id(self, value):
        """Prefix plus digits of any width — an id as somebody meant to write one.

        Its whole purpose is to make a near-miss reportable. Without it, a mistyped width is
        indistinguishable from a README, and the file leaves the project with no signal.
        """
        return bool(self._loose_id_re.match(value or ""))

    def format_id(self, number):
        return "%s%0*d" % (self.id_prefix, self.id_width, number)

    def number_of(self, task_id):
        return int(task_id[len(self.id_prefix):])


def _require(fields, source):
    unknown = sorted(k for k in fields if k not in CONFIG_KEYS)
    if unknown:
        raise SchemaError("%s: unknown config key(s): %s. Known keys: %s"
                          % (source, ", ".join(unknown), ", ".join(CONFIG_KEYS)))
    missing = [k for k in CONFIG_KEYS if k not in fields]
    if missing:
        raise SchemaError("%s: missing config key(s): %s. A project config replaces the default "
                          "rather than merging with it, so every key must be present."
                          % (source, ", ".join(missing)))
    for key in SCALAR_KEYS:
        if not isinstance(fields[key], str) or not fields[key]:
            raise SchemaError("%s: '%s' must be a non-empty scalar" % (source, key))
    for key in NULLABLE_KEYS:
        if not isinstance(fields[key], str):
            raise SchemaError("%s: '%s' must be a field name or 'none', not a list"
                              % (source, key))
    for key in LIST_KEYS:
        if not isinstance(fields[key], list):
            raise SchemaError("%s: '%s' must be a list" % (source, key))
    try:
        fields["id_width"] = int(fields["id_width"])
    except ValueError:
        raise SchemaError("%s: 'id_width' must be a whole number, got '%s'"
                          % (source, fields["id_width"]))
    if fields["id_width"] < 1:
        raise SchemaError("%s: 'id_width' must be at least 1" % source)


def _read_edges(body, source, fields):
    rows = parse_table(body, "Edges", ["Field", "Kind", "Derives"]) or []
    edges = {}
    reserved = {fields["id_field"], fields["title_field"]}
    for row in rows:
        field, kind, derives = row["Field"], row["Kind"], row["Derives"]
        if kind not in EDGE_KINDS:
            raise SchemaError("%s: edge '%s' has kind '%s'; taskmd implements only: %s"
                              % (source, field, kind, ", ".join(EDGE_KINDS)))
        if field in edges:
            raise SchemaError("%s: edge '%s' declared twice" % (source, field))
        if field in reserved:
            raise SchemaError("%s: edge '%s' collides with id_field/title_field" % (source, field))
        if derives in ("-", "") or derives.lower() in NULLS:
            derives = ""
        if kind == "soft" and derives:
            raise SchemaError("%s: soft edge '%s' cannot derive '%s' — a soft link is symmetric "
                              "and is derived under its own name, so there is nothing to name; "
                              "use '-'" % (source, field, derives))
        if kind != "soft" and not derives:
            raise SchemaError("%s: %s edge '%s' must name what it derives"
                              % (source, kind, field))
        edges[field] = Edge(field, kind, derives)

    derived = [e.derives for e in edges.values() if e.derives]
    for name in derived:
        if name in edges or name in reserved:
            raise SchemaError("%s: '%s' is derived and also stored — a derived name may not be "
                              "a field, or the computed value would overwrite a written one"
                              % (source, name))
    if len(set(derived)) != len(derived):
        raise SchemaError("%s: two edges derive the same name" % source)
    return edges


def _read_vocabularies(body, source, fields):
    rows = parse_table(body, "Vocabularies", ["Field", "Values"]) or []
    vocabularies = {}
    for row in rows:
        if row["Field"] in vocabularies:
            raise SchemaError("%s: vocabulary '%s' declared twice" % (source, row["Field"]))
        values = _split_items(row["Values"])
        if not values:
            raise SchemaError("%s: vocabulary '%s' lists no values" % (source, row["Field"]))
        vocabularies[row["Field"]] = values

    status_field = fields["status_field"]
    if status_field not in vocabularies:
        raise SchemaError("%s: status_field is '%s' but no vocabulary declares it. Add a row to "
                          "'## Vocabularies'." % (source, status_field))
    stray = [s for s in fields["open_statuses"] if s not in vocabularies[status_field]]
    if stray:
        raise SchemaError("%s: open_statuses has value(s) not in the '%s' vocabulary: %s"
                          % (source, status_field, ", ".join(stray)))
    blocked = fields["blocked_status"]
    if blocked and blocked not in vocabularies[status_field]:
        raise SchemaError("%s: blocked_status is '%s', which is not in the '%s' vocabulary: %s"
                          % (source, blocked, status_field,
                             ", ".join(vocabularies[status_field])))
    return vocabularies


def _check_deliverables_field(fields, edges, vocabularies, source):
    """The deliverables field holds paths, so it cannot also be an edge or an enumerated value.

    Naming it `parent` would ask one field to be a link and a file list at once; naming it `status`
    would ask `check` to validate a path against a vocabulary. Both are caught here, at config-read
    time, rather than inside whichever command trips over it first.
    """
    name = fields["deliverables_field"]
    if not name:
        return
    if name in edges:
        raise SchemaError("%s: deliverables_field is '%s', which is also declared as an edge — a "
                          "field holds links or paths, not both" % (source, name))
    derived = [e.derives for e in edges.values() if e.derives]
    if name in derived:
        raise SchemaError("%s: deliverables_field is '%s', which is derived from an edge — the "
                          "computed value would overwrite the declared paths" % (source, name))
    if name in vocabularies:
        raise SchemaError("%s: deliverables_field is '%s', which also has a vocabulary — paths are "
                          "not an enumerated value" % (source, name))
    if name in (fields["id_field"], fields["title_field"]):
        raise SchemaError("%s: deliverables_field is '%s', which collides with id_field/title_field"
                          % (source, name))


def _check_tasks_dir(root, fields, source, own_config):
    """The one config value that names a folder, checked here rather than on first use.

    Absent is an error however the value arrived. Tolerating it for the shipped default was the
    alternative — only a value someone wrote can be misspelled — and it was rejected because it
    leaves `check` exiting 0 on a project it never read, which is the failure this rule exists to
    remove. The cost is one `mkdir` for a project adopting taskmd; there is no command to do it,
    so the message says so.

    The message names the configured value, not the resolved absolute path: the value is the thing
    the user can act on, and printing the join would put a machine-specific path into output that
    has to be identical on every platform.
    """
    tasks_dir = fields["tasks_dir"]
    if os.path.isdir(os.path.join(root, tasks_dir)):
        return
    if own_config:
        hint = "Create it, or correct tasks_dir."
    else:
        hint = ("This project has no %s, so taskmd is using its shipped default; create the "
                "folder, or write a config naming a different one."
                % PROJECT_CONFIG.replace("\\", "/"))
    raise SchemaError("%s: tasks_dir is '%s', but the project root has no such folder. %s"
                      % (source, tasks_dir, hint))


def _resolve_hook(root, fields, source):
    """Resolve the one hook when the config is read, so reporting it early is structural rather
    than remembered.

    The declaration is **a program followed by its arguments**, and that shape is what makes the
    question answerable at all: taskmd can ask whether the program is there without running it. A
    free shell line was the alternative and is more convenient to write — it was rejected because
    "is this runnable?" then has no answer short of running it, which is the mid-command failure
    this ordering exists to prevent, and because the shell that would interpret it differs by
    platform, which output identical everywhere does not allow.

    A first token containing a slash is a path in the project; anything else is looked up on PATH.
    That is the whole rule, and it is what lets a hook be written in any language: name the
    interpreter, or name an executable file.

    Returns `(declared, argv)` — empty when the project declares no hook.
    """
    declared = fields["after_write"]
    if not declared:
        return "", []
    try:
        argv = shlex.split(declared)
    except ValueError as exc:
        raise SchemaError("%s: after_write is not a command line (%s): %s"
                          % (source, exc, declared))
    if not argv:
        raise SchemaError("%s: after_write is empty. Write a command, or 'none'." % source)

    program = argv[0]
    if "/" in program or "\\" in program:
        candidate = os.path.join(root, program.replace("/", os.sep).replace("\\", os.sep))
        if not os.path.isfile(candidate):
            raise SchemaError("%s: after_write names '%s', which is not a file in this project. "
                              "A hook is resolved when the config is read, so a project cannot "
                              "discover halfway through a command that it had none."
                              % (source, program))
        resolved = os.path.abspath(candidate)
    else:
        resolved = shutil.which(program)
        if not resolved:
            raise SchemaError("%s: after_write starts with '%s', which is not on PATH and is not "
                              "a path in this project. Name an executable that is installed, or a "
                              "file the project ships." % (source, program))
    return declared, [resolved] + argv[1:]


def _display(path, root):
    """A short, machine-independent name for a config file, for messages.

    Every `SchemaError` opens with this, and until the root was resolved rather than assumed it
    could stay as-written — the root was `.`, so the name already was relative. A resolved root is
    absolute, so without this every config error would print one machine's disk — which no output
    of this tool may do, on any path.
    """
    for base in (root, os.path.dirname(HERE)):
        try:
            name = os.path.relpath(path, base)
        except ValueError:  # a different drive on Windows: not relative to this base at all
            continue
        if not name.startswith(".."):
            return name.replace("\\", "/")
    return os.path.basename(path)


def drift_from_default(root, schema):
    """Vocabulary values the shipped default carries that this project's own config does not.

    What counts as drift, and why only this shape, is `## When this file moves ahead of yours` in
    the default config — the one description of it, not restated here.

    Returns `[(field, [missing values])]` and the number of rows compared, so the caller can report
    the reach of the comparison and not only its findings. A project with no config of its own is
    not examined and the count is zero: it is *using* the default, so there is nothing it can be
    behind — a vacuous case with a mechanical guarantee, rather than a walk that quietly read
    nothing.
    """
    if not os.path.exists(os.path.join(root, PROJECT_CONFIG)):
        return [], 0
    fields, body = split_front_matter(read(DEFAULT_CONFIG))
    shipped = _read_vocabularies(body, _display(DEFAULT_CONFIG, root), fields)
    compared = [f for f in sorted(shipped) if f in schema.vocabularies]
    drifted = []
    for field in compared:
        missing = [v for v in shipped[field] if v not in schema.vocabularies[field]]
        if missing:
            drifted.append((field, missing))
    return drifted, len(compared)


def templates(root, schema):
    """Every template under `tasks_dir`, and whether the create path can find each one.

    A template is a Markdown file carrying the id field with a **placeholder** in it — a value that
    is neither an id nor a near miss, which is exactly the test `load_tasks` applies when it
    declines to read `_task-template.md` as work. Name and location are deliberately not part of
    that test: they are what *reachability* is about, and keeping the two apart is what lets a
    project be told which of them it got wrong.

    Reachable means what the local-Markdown binding's *create* rule means by it: a `_`-prefixed
    file directly in `tasks_dir`. One level down, a template's relative links resolve differently
    from those of the task copied out of it (T-076), and the folder is skipped by the same rule
    that keeps templates out of the task set — so the listing comes back empty and *a project with
    no template is a normal project* is the documented reading of empty.

    Yields `(path, reachable)`, in a stable order.
    """
    base = os.path.join(root, schema.tasks_dir)
    for folder, subfolders, names in os.walk(base):
        subfolders[:] = sorted(d for d in subfolders if not d.startswith("."))
        here = os.path.relpath(folder, base)
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            path = os.path.join(folder, name)
            try:
                fields = split_front_matter(read(path))[0]
            except (OSError, ValueError, UnicodeDecodeError):
                continue
            value = fields.get(schema.id_field)
            if not value or schema.is_id(value) or schema.looks_like_id(value):
                continue
            yield path, here == os.curdir and name.startswith("_")


def load_schema(root="."):
    """Resolve the schema for a project: its own config if it has one, else the shipped default."""
    candidate = os.path.join(root, PROJECT_CONFIG)
    own_config = os.path.exists(candidate)
    path = candidate if own_config else DEFAULT_CONFIG
    source = _display(path, root)

    fields, body = split_front_matter(read(path))
    if not fields:
        raise SchemaError("%s: no front-matter block. The config opens with '---'." % source)
    _require(fields, source)
    edges = _read_edges(body, source, fields)
    vocabularies = _read_vocabularies(body, source, fields)
    _check_deliverables_field(fields, edges, vocabularies, source)
    hook = _resolve_hook(root, fields, source)
    # Last, deliberately: a config that is both malformed and points at a missing folder is
    # reported as malformed. The `SchemaError` suite builds a project from a config file alone,
    # with no tasks folder, and stays meaningful only while the earlier errors still win.
    _check_tasks_dir(root, fields, source, own_config)
    return Schema(source, fields, edges, vocabularies, hook)


# -------------------------------------------------------------------------------- the tasks

class Task(object):
    def __init__(self, path, schema, fields):
        self.path = path.replace("\\", "/")
        self.name = os.path.basename(self.path)
        self.schema = schema
        self.fields = fields
        self.id = fields.get(schema.id_field, "")
        self.title = fields.get(schema.title_field, "")
        self.status = fields.get(schema.status_field, "")

        self.edges = {}
        for field, edge in schema.edges.items():
            raw = fields.get(field, "")
            values = [raw] if isinstance(raw, str) else list(raw)
            values = [v for v in values if v and v.lower() not in NULLS]
            if edge.kind == "hierarchy" and len(values) > 1:
                values = values[:1]
            self.edges[field] = values

        # Every inverse edge starts empty and is filled by derive(). Never read from a file.
        self.derived = dict((name, []) for name in schema.derived_names)

    @property
    def deliverables(self):
        """Paths this task declares it produces, relative to the project root.

        Empty when the schema sets `deliverables_field: none` — the field name is never written
        here, so the CLI never learns it either.
        """
        if not self.schema.deliverables_field:
            return []
        raw = self.fields.get(self.schema.deliverables_field, "")
        values = [raw] if isinstance(raw, str) else list(raw)
        return [v for v in values if v and v.lower() not in NULLS]

    def links(self, name):
        """Every task linked under `name` — stored here, derived from elsewhere, or both.

        This is what a view should show: whichever end of a link a task is on, it sees the link.
        Writing a soft edge on both tasks is allowed and collapses to one entry here, so nobody has
        to know which side "owns" it.
        """
        out = [tid for tid in self.edges.get(name, []) if tid != self.id]
        for tid in self.derived.get(name, []):
            if tid not in out:
                out.append(tid)
        return sorted(out)

    @property
    def extra(self):
        """Front-matter this schema does not interpret: carried, never acted on.

        **Nothing in the four commands reads this**, and that is not an oversight. A project that
        wants to *see* an unnamed field names it in `context_fields` or `index_columns`, and those
        read `Task.fields` directly — so the display route needs no help from here. The only reader
        left is this module's own `main()`, which T-030 has decided to remove; when it goes, this
        accessor goes with it unless a binding implementation has found a use for it by then.
        """
        known = set(self.schema.known_fields)
        return dict((k, v) for k, v in self.fields.items() if k not in known)

    @property
    def is_open(self):
        return self.schema.is_open(self.status)

    def __repr__(self):
        return "Task(%s, %s)" % (self.id, self.status)


class TaskSet(dict):
    """The project's tasks, and what was **not** loaded as one.

    A `dict` subclass, so every caller that treats this as `{id: Task}` carries on unchanged. The
    anomalies ride along because they are facts about this set — which id was claimed twice, which
    file was rejected — and the alternative was threading a fifth argument through four commands
    to reach the two places that care.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.anomalies = []


DUPLICATE_ID = "duplicate-id"   # two files claim one id; the first in walk order is loaded
ID_WIDTH = "id-width"           # right prefix, wrong width: not a task, and said so


class Anomaly(object):
    """One reason a file under `tasks_dir` is not the task somebody thought it was."""

    def __init__(self, kind, task_id, paths):
        self.kind = kind
        self.task_id = task_id
        self.paths = paths

    def __repr__(self):
        return "Anomaly(%s, %s, %s)" % (self.kind, self.task_id, self.paths)


def load_tasks(root=".", schema=None):
    """Read every task file under the schema's tasks_dir and wire up the derived edges.

    Two things go wrong while reading a folder of files, and both used to be silent. Two files
    claiming one id: the second overwrote the first in a plain dict, so a task simply ceased to
    exist — gone from `list`, from the index, from `context` and from every derived edge on both
    ends, with nothing printed and exit 0 (T-062). And a file whose id carries the right prefix at
    the wrong width, accepted as though `id_width` were decoration (T-075).

    **Neither raises.** A defect in one task file is not a configuration problem, and a problem is
    never raised from inside a task the user is trying to finish — so the readable tasks are
    returned, and the anomalies travel with them on the result for `check` to report and every
    other command to warn about.
    """
    schema = schema or load_schema(root)
    claims, mismatched = {}, []
    base = os.path.join(root, schema.tasks_dir)
    for folder, dirs, files in os.walk(base):
        # Sorted, so which file wins a collision is reproducible instead of an artefact of the
        # filesystem's own ordering. It is still a collision, and it is still reported; this only
        # means the same project gives the same answer twice.
        dirs[:] = sorted(d for d in dirs if not d.startswith(("_", ".")))
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(folder, name)
            fields, _ = split_front_matter(read(path))
            task = Task(path, schema, fields)
            if schema.is_id(task.id):
                claims.setdefault(task.id, []).append(task)
            elif schema.looks_like_id(task.id):
                mismatched.append(task)

    tasks = TaskSet()
    for task_id in sorted(claims):
        claimed = claims[task_id]
        tasks[task_id] = claimed[0]
        if len(claimed) > 1:
            tasks.anomalies.append(Anomaly(DUPLICATE_ID, task_id, [t.path for t in claimed]))
    for task in sorted(mismatched, key=lambda t: t.path):
        tasks.anomalies.append(Anomaly(ID_WIDTH, task.id, [task.path]))
    return derive(tasks, schema)


def derive(tasks, schema):
    """Compute every inverse edge. This is the only place a `children`/`blocks` list exists.

    Named inverses (`parent` -> `children`, `blocked_by` -> `blocks`) land under the derived name.
    Soft edges are symmetric and land under their own name, so a task sees links written on the
    other task. A link written on both sides yields one entry, not two — see `Task.links`.
    """
    for task in tasks.values():
        for field, edge in schema.edges.items():
            name = edge.derives or field
            for target in task.edges[field]:
                if target == task.id or target not in tasks:
                    continue
                inverse = tasks[target].derived[name]
                if task.id not in inverse:
                    inverse.append(task.id)
    for task in tasks.values():
        for name in task.derived:
            task.derived[name].sort()
    return tasks


# -------------------------------------------------------------------------------------- main

def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = argv[0] if argv else "."
    try:
        schema = load_schema(root)
    except SchemaError as exc:
        print("SCHEMA ERROR: %s" % exc)
        return 1

    print("schema   %s" % schema.source)
    print("ids      %s (width %d), e.g. %s"
          % (schema.id_prefix, schema.id_width, schema.format_id(7)))
    print("tasks    %s/" % schema.tasks_dir)
    print("status   %s = %s" % (schema.status_field, ", ".join(schema.statuses)))
    print("open     %s" % ", ".join(schema.open_statuses))
    print("edges    " + "; ".join("%s (%s) -> %s" % (e.field, e.kind, e.derives or "-")
                                  for e in schema.edges.values()))
    print("vocab    " + "; ".join(sorted(schema.vocabularies)))

    # Every name a link can appear under, stored or derived — this is what a view shows.
    names = []
    for field, edge in schema.edges.items():
        for name in (field, edge.derives):
            if name and name not in names:
                names.append(name)

    tasks = load_tasks(root, schema)
    print("\n%d task(s) in %s/" % (len(tasks), schema.tasks_dir))
    for tid in sorted(tasks):
        t = tasks[tid]
        print("  %-12s %-11s %s" % (tid, t.status, t.title))
        shown = "; ".join("%s=%s" % (n, ",".join(t.links(n))) for n in names if t.links(n))
        if shown:
            print("      links    %s" % shown)
        if t.extra:
            print("      carried  %s" % ", ".join(sorted(t.extra)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
