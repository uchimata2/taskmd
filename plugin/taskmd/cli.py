#!/usr/bin/env python
"""The four commands: `context`, `index`, `check`, `list`.

  python -m taskmd context T-002        [--root PATH]
  python -m taskmd index                [--root PATH]
  python -m taskmd check                [--root PATH]
  python -m taskmd list [--<field> V]   [--open|--closed] [--limit N] [--json] [--root PATH]

Four, and the fourth was argued for rather than added — `docs/SCOPE.md` non-goal 11 was amended on
2026-08-05 (T-022) after standing at three. Filtering is in; a query language is still out. The
reason it could not stay grep's job is that grep cannot see a derived edge at all: what a task
blocks, and the far end of a soft link, exist nowhere on disk. What the retired `deliverables`
command did that nothing else does still survives as a `check` class rather than as a command.

This module holds **no field name, status value or id format of its own**. Everything it knows
about a project's shape it asks `taskmd.schema` for, which reads it from the config. If you find a
literal like "blocked" or "status" below, that is a defect.

`--root` is an override, not a default: with no flag the project is found by walking up from where
the command was run, and the rule for that lives in `taskmd.discovery`.

Pure standard library. Files are written with an explicit newline so output is byte-identical on
every platform; console output is ASCII so a cp1252 terminal cannot mangle it.
"""

import os
import re
import subprocess
import sys

from . import discovery
from .schema import SchemaError, load_schema, load_tasks

BEGIN = "<!-- taskmd:index - generated, do not edit by hand -->"
END = "<!-- taskmd:end -->"

LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)\s]*)?\)")
SKIP_DIRS = (".git", "node_modules", "__pycache__", ".venv")

RULE = "=" * 72


# ------------------------------------------------------------------------------ plumbing

def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    """Always `newline="\\n"`: Python's default text mode rewrites every newline on Windows,
    which would make the same command produce different bytes on different machines."""
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def rel(root, *parts):
    """A repo-relative path with forward slashes, so printed output does not depend on the OS."""
    return os.path.normpath(os.path.join(*parts)).replace("\\", "/") if parts else root


def is_nested_project(schema, folder):
    """True if `folder` is a taskmd project in its own right.

    A project inside a project is validated on its own, not by its host — which is what lets this
    repository carry deliberately-broken fixture projects without reporting their defects as its
    own. What counts as a project is `taskmd.discovery`'s to say, since resolving the root asks
    the identical question one folder at a time; this passes the *resolved* tasks folder, so a
    project that renamed it still recognises its own nested projects.
    """
    return discovery.is_project(folder, schema.tasks_dir)


def markdown_files(root, schema):
    """Every .md in the project, including dot-directories, excluding nested projects.

    Walking rather than globbing is deliberate: `glob`'s `**` skips dot-directories, and a broken
    link in a dot-directory is exactly the one that stayed hidden long enough to matter.
    """
    for base, dirs, files in os.walk(root):
        keep = []
        for d in dirs:
            if d in SKIP_DIRS:
                continue
            if base != root and is_nested_project(schema, os.path.join(base, d)):
                continue
            keep.append(d)
        dirs[:] = sorted(keep)
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(base, name)


def link_names(schema):
    """Every name a link can appear under — stored fields and derived inverses, in config order."""
    names = []
    for field, edge in schema.edges.items():
        for name in (field, edge.derives):
            if name and name not in names:
                names.append(name)
    return names


def label(name):
    return name.replace("_", " ").upper()


def summarise(task):
    return "%-12s %-11s %s" % (task.id, task.status, task.title)


def load(root):
    """Resolve the schema and the tasks, or explain why not.

    R-17: a configuration problem is reported *here*, when the config is read, and the command
    never starts. It is never raised from inside a task the user is trying to finish.
    """
    schema = load_schema(root)
    return schema, load_tasks(root, schema)


# ------------------------------------------------------------------------------- context

def cmd_context(root, schema, tasks, args):
    if not args:
        print("usage: taskmd context <id>")
        return 1
    wanted = args[0]
    if wanted not in tasks:
        print("No such task: %s" % wanted)
        return 1
    task = tasks[wanted]

    out = [RULE, "%s  %s" % (task.id, task.title), RULE]
    shown = [(f, task.fields.get(f, "")) for f in schema.context_fields]
    out.append(" | ".join("%s %s" % (f, v or "-") for f, v in shown))
    out.append("file   %s" % rel(root, os.path.relpath(task.path, root)))

    open_blockers = []
    for name in link_names(schema):
        linked = [tasks[t] for t in task.links(name) if t in tasks]
        if not linked:
            continue
        out.append("")
        out.append(label(name))
        for other in linked:
            flag = ""
            if name in schema.edges and schema.edges[name].kind == "dependency" and other.is_open:
                flag = "  <-- still open"
                open_blockers.append(other)
            out.append("  " + summarise(other) + flag)

    if task.deliverables:
        out.append("")
        out.append("DECLARES")
        for path in task.deliverables:
            here = os.path.join(root, path.replace("/", os.sep))
            out.append("  [%s] %s" % ("x" if os.path.exists(here) else " ", path))

    # Facts, not an instruction. R-6: a next-step pointer is context, not authorization, so the
    # closing line reports state and stops. It carries only what is *derived* — open/closed, and
    # which blockers are still open — because the stored fields are already on the header line and
    # printing them twice would be two homes for one fact.
    out.append("")
    if open_blockers:
        out.append("STATE  open, waiting on %s"
                   % ", ".join(sorted(set(b.id for b in open_blockers))))
    elif task.is_open:
        out.append("STATE  open, no blocker outstanding")
    else:
        out.append("STATE  closed")
    print("\n".join(out))
    return 0


# --------------------------------------------------------------------------------- index

def table(header, rows):
    if not rows:
        return []
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join(":---" for _ in header) + " |"]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return out


def index_block(root, schema, tasks):
    """The generated region. Edge columns appear only when some task uses them.

    Omitting an unused edge is derived from the data rather than configured — a project with no
    hierarchy should not read a column of dashes, and one that starts using it should not have to
    remember to switch a column on.
    """
    names = [n for n in link_names(schema)
             if any(t.links(n) for t in tasks.values())]
    header = ["ID", "Title"] + [c.replace("_", " ").title() for c in schema.index_columns] + \
             [n.replace("_", " ").title() for n in names]

    def row(task):
        cells = ["[%s](%s)" % (task.id, os.path.basename(task.path)), task.title]
        cells += ["`%s`" % task.fields.get(c, "-") if task.fields.get(c) else "-"
                  for c in schema.index_columns]
        cells += [", ".join(task.links(n)) or "-" for n in names]
        return cells

    ordered = [tasks[t] for t in sorted(tasks)]
    active = [t for t in ordered if t.is_open]
    closed = [t for t in ordered if not t.is_open]

    out = [BEGIN, ""]
    out.append("## Active")
    out.append("")
    out += table(header, [row(t) for t in active]) or ["None."]
    out.append("")
    out.append("## Closed")
    out.append("")
    out += table(header, [row(t) for t in closed]) or ["None."]
    out.append("")
    out.append(END)
    return "\n".join(out)


def run_after_write(root, schema):
    """Run the project's declared command, and let its failure fail the command that wrote.

    One invocation point, and it is *after* the write: the file is on disk before the hook sees
    it, so a hook that fails reports a problem rather than leaving the reader guessing whether
    anything was written. A pre-write point would catch a bad edit before it landed — a real
    advantage, recorded and deliberately not taken (T-011 §1), because a second point is a second
    config key every adopting project pays for.

    The output is captured and re-printed rather than inherited. Two reasons: a caller that
    redirected this command's output would otherwise get the hook's on a different stream, and
    the console has already been reconfigured to UTF-8 here, which a child process has not.
    """
    if not schema.after_write_argv:
        return 0
    sys.stdout.flush()
    print("Hook   %s" % schema.after_write)
    try:
        done = subprocess.Popen(schema.after_write_argv, cwd=root,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = done.communicate()[0]
    except OSError as exc:
        # Resolution happened when the config was read, so reaching here means the world moved
        # underneath us — the file was deleted, or is not executable after all.
        print("HOOK ERROR    could not run '%s': %s" % (schema.after_write, exc))
        return 1
    for line in out.decode("utf-8", "replace").splitlines():
        print("  " + line)
    if done.returncode != 0:
        print("HOOK FAILED   '%s' exited %d; the write happened, the check did not pass"
              % (schema.after_write, done.returncode))
        return 1
    return 0


def cmd_index(root, schema, tasks, args):
    path = os.path.join(root, schema.tasks_dir, "README.md")
    block = index_block(root, schema, tasks)

    if os.path.exists(path):
        text = read(path)
        if BEGIN in text and END in text:
            head = text[:text.index(BEGIN)]
            tail = text[text.index(END) + len(END):]
            new = head + block + tail
        else:
            # No generated region yet: append one, leaving every existing byte in place.
            new = text.rstrip("\n") + "\n\n" + block + "\n"
    else:
        new = "# Task index\n\nGenerated from each task's front-matter.\n\n" + block + "\n"

    write(path, new)
    active = len([t for t in tasks.values() if t.is_open])
    print("Wrote %s - %d active, %d closed"
          % (rel(root, os.path.relpath(path, root)), active, len(tasks) - active))
    return run_after_write(root, schema)


# --------------------------------------------------------------------------------- check

def check_vocabularies(schema, tasks, problems):
    for task in ordered(tasks):
        for field, values in sorted(schema.vocabularies.items()):
            value = task.fields.get(field, "")
            if value and value not in values:
                problems.append("VOCABULARY    %s.%s is '%s'; allowed: %s"
                                % (task.id, field, value, ", ".join(values)))


def check_references(schema, tasks, problems):
    for task in ordered(tasks):
        for field in sorted(task.edges):
            for target in task.edges[field]:
                if target not in tasks:
                    problems.append("DANGLING      %s.%s -> %s does not exist"
                                    % (task.id, field, target))


def check_blocked_without_blocker(schema, tasks, problems):
    if not schema.blocked_status:
        return
    dependencies = [f for f, e in schema.edges.items() if e.kind == "dependency"]
    for task in ordered(tasks):
        if task.status != schema.blocked_status:
            continue
        if not any(task.edges[f] for f in dependencies):
            problems.append("NO BLOCKER    %s is '%s' with nothing in %s"
                            % (task.id, schema.blocked_status, ", ".join(sorted(dependencies))))


def check_cycles(schema, tasks, problems):
    dependencies = [f for f, e in schema.edges.items() if e.kind == "dependency"]
    seen, stack, reported = set(), [], set()

    def walk(tid):
        if tid in stack:
            loop = tuple(sorted(stack[stack.index(tid):]))
            if loop not in reported:
                reported.add(loop)
                problems.append("CYCLE         dependency loop: %s"
                                % " -> ".join(stack[stack.index(tid):] + [tid]))
            return
        if tid in seen or tid not in tasks:
            return
        stack.append(tid)
        for field in dependencies:
            for up in tasks[tid].edges[field]:
                walk(up)
        stack.pop()
        seen.add(tid)

    for tid in sorted(tasks):
        walk(tid)


def check_stored_derived(schema, tasks, problems):
    derived = set(e.derives for e in schema.edges.values() if e.derives)
    for task in ordered(tasks):
        for name in sorted(derived & set(task.fields)):
            problems.append("STORED DERIVED %s stores '%s:', which is computed from '%s'; remove it"
                            % (task.id, name, source_of(schema, name)))


def source_of(schema, derived):
    for field, edge in schema.edges.items():
        if edge.derives == derived:
            return field
    return "?"


def check_deliverables(root, schema, tasks, problems):
    if not schema.deliverables_field:
        return
    for task in ordered(tasks):
        for path in task.deliverables:
            if not os.path.exists(os.path.join(root, path.replace("/", os.sep))):
                problems.append("MISSING OUTPUT %s declares '%s', which does not exist"
                                % (task.id, path))


def check_links(root, schema, problems):
    for md in markdown_files(root, schema):
        base = os.path.dirname(md)
        for match in LINK.finditer(read(md)):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                problems.append("BROKEN LINK   %s -> %s"
                                % (rel(root, os.path.relpath(md, root)), target))


def ordered(tasks):
    return [tasks[t] for t in sorted(tasks)]


def cmd_check(root, schema, tasks, args):
    problems = []
    check_vocabularies(schema, tasks, problems)
    check_references(schema, tasks, problems)
    check_blocked_without_blocker(schema, tasks, problems)
    check_cycles(schema, tasks, problems)
    check_stored_derived(schema, tasks, problems)
    check_deliverables(root, schema, tasks, problems)
    check_links(root, schema, problems)

    if problems:
        for problem in problems:
            print(problem)
        print("")
        print("%d problem(s) over %d task(s)" % (len(problems), len(tasks)))
        return 1
    print("OK - %d task(s), vocabulary valid, references resolve, no broken links" % len(tasks))
    return 0


# ---------------------------------------------------------------------------------- list

def dependency_fields(schema):
    return [f for f, e in schema.edges.items() if e.kind == "dependency"]


def is_blocked(schema, tasks, task):
    """An open dependency. Not a status value — a task can be marked anything and still be held."""
    for field in dependency_fields(schema):
        for target in task.edges[field]:
            if target in tasks and tasks[target].is_open:
                return True
    return False


def effective_values(schema, tasks):
    """Each task's value rank, improved by the best value it transitively unblocks.

    This is "dependencies first": a cheap blocker is pulled ahead *by what it releases* rather
    than waiting behind unrelated work. Computed per call and stored nowhere. The rule it
    implements is written in `## Ordering` in the schema config, and is not restated here.
    """
    inverses = [schema.edges[f].derives for f in dependency_fields(schema)
                if schema.edges[f].derives]
    own = dict((tid, schema.rank(schema.value_field, t.fields.get(schema.value_field, "")))
               for tid, t in tasks.items()) if schema.value_field else \
        dict((tid, 0) for tid in tasks)

    memo = {}

    def walk(tid, seen):
        if tid in memo:
            return memo[tid]
        if tid in seen:
            return own[tid]  # a dependency cycle is `check`'s to report, not this command's to hang on
        best = own[tid]
        for name in inverses:
            for other in tasks[tid].links(name):
                if other in tasks:
                    best = min(best, walk(other, seen | {tid}))
        memo[tid] = best
        return best

    return dict((tid, walk(tid, frozenset())) for tid in tasks)


def order(schema, tasks, selection):
    """Blocked last, then effective value, then effort, then id — see `## Ordering` in the config."""
    values = effective_values(schema, tasks)

    def key(task):
        effort = schema.rank(schema.effort_field, task.fields.get(schema.effort_field, "")) \
            if schema.effort_field else 0
        return (is_blocked(schema, tasks, task), values[task.id], effort, task.id)

    return sorted(selection, key=key)


def filter_names(schema):
    """Every `--name` the command accepts, as {name: kind}."""
    names = dict((f, "vocabulary") for f in schema.vocabularies)
    for name in link_names(schema):
        names[name] = "link"
    return names


def parse_filters(schema, args):
    """(filters, options) or (None, message). Every rejection happens before a line is printed."""
    known = filter_names(schema)
    filters, options = [], {"limit": None, "json": False, "state": None}
    rest = list(args)
    while rest:
        arg = rest.pop(0)
        if arg == "--json":
            options["json"] = True
            continue
        if arg in ("--open", "--closed"):
            options["state"] = arg[2:]
            continue
        if not arg.startswith("--"):
            return None, ("unexpected argument: %s. Filters are given as --<field> <value>" % arg)
        name = arg[2:].replace("-", "_")
        if not rest:
            return None, "%s needs a value" % arg
        value = rest.pop(0)
        if name == "limit":
            if not value.isdigit():
                return None, "--limit needs a whole number, not '%s'" % value
            options["limit"] = int(value)
            continue
        if name not in known:
            return None, ("unknown filter: --%s. This project accepts: %s"
                          % (name, ", ".join("--" + n for n in sorted(known))))
        if known[name] == "vocabulary" and value not in schema.vocabularies[name]:
            return None, ("--%s does not take '%s'. This project's %s values are: %s"
                          % (name, value, name, ", ".join(schema.vocabularies[name])))
        filters.append((name, known[name], value))
    return (filters, options), None


def matches(task, filters):
    for name, kind, value in filters:
        if kind == "vocabulary":
            if task.fields.get(name, "") != value:
                return False
        elif value not in task.links(name):
            return False
    return True


def cmd_list(root, schema, tasks, args):
    """A subset of the tasks, in priority order, rendered so the caller can use it as printed.

    The fourth command. `docs/SCOPE.md` non-goal 11 was amended for it: filtering is in, a query
    language is not, and the reason is that grep cannot answer these questions at all — a derived
    edge exists nowhere on disk. Writes nothing.
    """
    parsed, problem = parse_filters(schema, args)
    if problem:
        print(problem)
        return 2
    filters, options = parsed

    chosen = [t for t in tasks.values() if matches(t, filters)]
    if options["state"]:
        chosen = [t for t in chosen if t.is_open == (options["state"] == "open")]
    chosen = order(schema, tasks, chosen)
    if options["limit"] is not None:
        chosen = chosen[:options["limit"]]

    columns = [schema.status_field] + [c for c in schema.index_columns if c != schema.status_field]
    if options["json"]:
        import json
        payload = []
        for task in chosen:
            row = {"id": task.id, "title": task.title,
                   "blocked": is_blocked(schema, tasks, task), "open": task.is_open}
            for column in columns:
                row[column] = task.fields.get(column, "")
            for name in link_names(schema):
                row[name] = task.links(name)
            payload.append(row)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    # Tab-separated: a line format a caller can read as printed and a script can cut, without
    # either of them knowing the terminal width. Padding would have made the second impossible.
    for task in chosen:
        cells = [task.id] + [task.fields.get(c, "") or "-" for c in columns] + [task.title]
        print("\t".join(cells))
    return 0


# ---------------------------------------------------------------------------------- main

COMMANDS = {"context": cmd_context, "index": cmd_index, "check": cmd_check, "list": cmd_list}


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    root, rest = None, []
    argv = list(argv)
    while argv:
        arg = argv.pop(0)
        if arg == "--root":
            if not argv:
                print("--root needs a path")
                return 2
            root = argv.pop(0)
        else:
            rest.append(arg)

    if not rest or rest[0] not in COMMANDS:
        # `taskmd`, not `python -m taskmd`: this line is read by someone who has already mistyped,
        # and the one who needs telling is the adopter, who has the plugin on PATH and no source
        # tree. It cannot be derived - every route into this module ends in `python -m taskmd`, so
        # argv[0] is the same however the user got here (T-055).
        print("usage: taskmd {%s} [args] [--root PATH]"
              % ",".join(sorted(COMMANDS)))
        return 2

    # `--root` is the override; with no flag the project is found by walking up from where the
    # command was run (`taskmd.discovery`). That order is what makes a clone work unedited, and
    # it is why the flag is not simply a default of ".".
    if root is None:
        root = discovery.find_root()
        if root is None:
            print(discovery.not_found_message())
            return 2
    elif not os.path.isdir(root):
        print("No such directory: %s" % root)
        return 2

    try:
        schema, tasks = load(root)
    except SchemaError as exc:
        print("CONFIG ERROR  %s" % exc)
        return 2
    return COMMANDS[rest[0]](root, schema, tasks, rest[1:])
