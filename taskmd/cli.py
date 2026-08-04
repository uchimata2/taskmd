#!/usr/bin/env python
"""The three commands: `context`, `index`, `check`.

  python -m taskmd context T-002 [--root PATH]
  python -m taskmd index          [--root PATH]
  python -m taskmd check          [--root PATH]

Three, and no more — `docs/SCOPE.md` non-goal 11 in this repository, and the reason is that a
query language is grep's job. What the retired `deliverables` command did that nothing else does
survives as a `check` class, not as a fourth command.

This module holds **no field name, status value or id format of its own**. Everything it knows
about a project's shape it asks `taskmd.schema` for, which reads it from the config. If you find a
literal like "blocked" or "status" below, that is a defect.

Pure standard library. Files are written with an explicit newline so output is byte-identical on
every platform; console output is ASCII so a cp1252 terminal cannot mangle it.
"""

import os
import re
import sys

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
    own. The marks are a config of its own, or its own tasks folder.
    """
    return (os.path.isfile(os.path.join(folder, ".taskmd", "config.md")) or
            os.path.isdir(os.path.join(folder, schema.tasks_dir)))


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
        print("usage: context <id>")
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
    return 0


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


# ---------------------------------------------------------------------------------- main

COMMANDS = {"context": cmd_context, "index": cmd_index, "check": cmd_check}


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    root, rest = ".", []
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
        print("usage: python -m taskmd {%s} [args] [--root PATH]"
              % ",".join(sorted(COMMANDS)))
        return 2
    if not os.path.isdir(root):
        print("No such directory: %s" % root)
        return 2

    try:
        schema, tasks = load(root)
    except SchemaError as exc:
        print("CONFIG ERROR  %s" % exc)
        return 2
    return COMMANDS[rest[0]](root, schema, tasks, rest[1:])
