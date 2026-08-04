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
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(HERE, "defaults", "config.md")
PROJECT_CONFIG = os.path.join(".taskmd", "config.md")

# Fixed vocabulary: each kind is a different traversal in code, so adding one means new code,
# not new config. Their field *names* are configurable; this set is not.
EDGE_KINDS = ("hierarchy", "dependency", "soft")

SCALAR_KEYS = ("id_field", "id_prefix", "id_width", "title_field", "tasks_dir", "status_field")
LIST_KEYS = ("open_statuses", "context_fields", "index_columns")
CONFIG_KEYS = SCALAR_KEYS + LIST_KEYS

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
    def __init__(self, source, fields, edges, vocabularies):
        self.source = source
        self.id_field = fields["id_field"]
        self.id_prefix = fields["id_prefix"]
        self.id_width = fields["id_width"]
        self.title_field = fields["title_field"]
        self.tasks_dir = fields["tasks_dir"]
        self.status_field = fields["status_field"]
        self.open_statuses = fields["open_statuses"]
        self.context_fields = fields["context_fields"]
        self.index_columns = fields["index_columns"]
        self.edges = edges                # {field: Edge}
        self.vocabularies = vocabularies  # {field: [values]}
        self._id_re = re.compile(r"^%s\d+$" % re.escape(self.id_prefix))

    @property
    def statuses(self):
        return self.vocabularies[self.status_field]

    @property
    def known_fields(self):
        """Fields this schema interprets. Everything else in a task file is pass-through."""
        return ([self.id_field, self.title_field] + sorted(self.edges) +
                sorted(self.vocabularies))

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

    def is_id(self, value):
        return bool(self._id_re.match(value or ""))

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
    return vocabularies


def load_schema(root="."):
    """Resolve the schema for a project: its own config if it has one, else the shipped default."""
    candidate = os.path.join(root, PROJECT_CONFIG)
    path = candidate if os.path.exists(candidate) else DEFAULT_CONFIG
    source = path.replace("\\", "/")

    fields, body = split_front_matter(read(path))
    if not fields:
        raise SchemaError("%s: no front-matter block. The config opens with '---'." % source)
    _require(fields, source)
    edges = _read_edges(body, source, fields)
    vocabularies = _read_vocabularies(body, source, fields)
    return Schema(source, fields, edges, vocabularies)


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
        """Front-matter this schema does not interpret: carried and displayable, never acted on."""
        known = set(self.schema.known_fields)
        return dict((k, v) for k, v in self.fields.items() if k not in known)

    @property
    def is_open(self):
        return self.schema.is_open(self.status)

    def __repr__(self):
        return "Task(%s, %s)" % (self.id, self.status)


def load_tasks(root=".", schema=None):
    """Read every task file under the schema's tasks_dir and wire up the derived edges."""
    schema = schema or load_schema(root)
    tasks = {}
    base = os.path.join(root, schema.tasks_dir)
    for folder, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith(("_", "."))]
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            fields, _ = split_front_matter(read(os.path.join(folder, name)))
            task = Task(os.path.join(folder, name), schema, fields)
            if schema.is_id(task.id):
                tasks[task.id] = task
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
