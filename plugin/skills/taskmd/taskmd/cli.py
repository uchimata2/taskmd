#!/usr/bin/env python
"""The four commands: `context`, `index`, `check`, `list`.

<!-- taskmd:commands -->
  python -m taskmd context T-002        [--root PATH]
  python -m taskmd index                [--root PATH]
  python -m taskmd check                [--root PATH]
  python -m taskmd list [--<field> V]   [--open|--closed] [--limit N] [--json] [--root PATH]
<!-- taskmd:end-commands -->

Four, and the fourth was argued for rather than added — the command surface stood at three until
2026-08-05 (T-022). Filtering is in; a query language is still out, and the argument for the
difference is T-022's — not restated here, and not nameable here either: it lives in a paper this
plugin deliberately does not ship (T-031). What the retired `deliverables` command did that nothing
else does still survives as a `check` class rather than as a command.

The front-door document lists the same four with what each is *for*, which is a different register
for a different reader: the lines above give the flags, and someone deciding whether to install has
no use for them. The repetition is deliberate and was decided rather than tolerated (T-117).

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
from .schema import (DUPLICATE_ID, PARKED, SchemaError, drift_from_default, load_schema, load_tasks,
                     read, split_front_matter, templates)

BEGIN = "<!-- taskmd:index - generated, do not edit by hand -->"
END = "<!-- taskmd:end -->"

LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)\s]*)?\)")

# Link syntax inside a fence or a code span is text being *shown*, not a pointer being made: it
# renders as literal characters, nobody can follow it, and it cannot be broken. So it is neither
# resolved nor counted — T-112, which is the same boundary as the comment below, one syntax over.
# Spans are line-scoped on purpose: a stray backtick then costs one line rather than swallowing the
# rest of a document and hiding the real links in it.
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"(`+)[^\n]*?\1")

# A path written as prose rather than as a Markdown link is **not** a reference this command
# resolves, and that is a decision rather than an omission — T-092 measured the alternative on this
# repository and `README.md` tells an adopter what is not covered.
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

    Walking rather than globbing is deliberate: `glob`'s `**` skips dot-directories, and a project
    keeps tracked documents in them — config, workflows, templates — which a glob would silently
    never open.

    **The case this walk was originally written for no longer reaches `check_links`** (T-098). It was
    a live handoff pointer, in a dot-directory *and* gitignored, and the document-side filter there
    now removes it: nothing validates the links in a document a clone would not receive, which is a
    decision with the alternatives priced in T-098 and not an oversight. The walk keeps its job
    because the tracked half of a dot-directory is real; do not read it as covering the other half.

    **The exclusion applies at every depth, including directly inside the root.** It used to carry a
    `base != root` guard, which meant a project holding another project at the top level reported
    that project's problems as its own — invisible here only because every fixture happens to sit two
    levels down (T-069). Removing it cannot make the walk decline to enter the project it was asked
    about: the test is applied to *subdirectories* of `base`, never to `root` itself.
    """
    for base, dirs, files in os.walk(root):
        keep = []
        for d in dirs:
            if d in SKIP_DIRS:
                continue
            if is_nested_project(schema, os.path.join(base, d)):
                continue
            keep.append(d)
        dirs[:] = sorted(keep)
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(base, name)


def clone_would_receive(root):
    """The set of files a clone of `root` would contain, or **None** if there is no git to ask.

    `git ls-files --cached --others --exclude-standard` is tracked files *plus* untracked ones that
    are not ignored — exactly what a push would send. It is the same flag combination this project's
    own pre-publish check is built on, argued for at length where that check lives (T-047 moved it
    out of the always-loaded conventions into the publishing document); `check` standing next to that
    check and answering a different question about the same tree is what T-094 was raised to settle.
    `-z` because a path may contain anything, including a newline.

    **None is not the empty set.** "git says nothing here would be published" and "there is no git
    here to ask" are different answers, and only the first is an exclusion — a project with no
    version control gets the whole tree read, and is told so rather than quietly getting less.
    """
    try:
        done = subprocess.Popen(["git", "ls-files", "-z", "--cached", "--others",
                                 "--exclude-standard"],
                                cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = done.communicate()[0]
    except OSError:
        return None                     # no git on PATH at all
    if done.returncode != 0:
        return None                     # a directory, but not inside a work tree
    return set(os.path.normpath(os.path.join(root, name.decode("utf-8", "replace")))
               for name in out.split(b"\0") if name)


def link_names(schema):
    """Every name a link can appear under — stored fields and derived inverses, in config order."""
    names = []
    for field, edge in schema.edges.items():
        for name in (field, edge.derives):
            if name and name not in names:
                names.append(name)
    return names


def dependency_fields(schema):
    return [f for f, e in schema.edges.items() if e.kind == "dependency"]


def dependency_names(schema):
    """Both names a dependency appears under — the stored field *and* its derived inverse.

    `schema.edges` is keyed by the stored field, so `blocks` is not a key in it: asking
    `name in schema.edges` answers "not a dependency" for one end of every dependency edge. That
    answer is right in `context`, which flags only the side that holds this task up, and wrong in
    any view that has to resolve both.
    """
    names = []
    for field in dependency_fields(schema):
        for name in (field, schema.edges[field].derives):
            if name and name not in names:
                names.append(name)
    return names


def in_use(names, tasks):
    """Of `names`, the configured field columns some task in this project has a value for.

    The same test `index_block` has always applied to **edge** columns, now applied to field columns
    too — a project with no work packages should not read a column of dashes, and one that starts
    using them should not have to remember to switch a column on (T-070).

    Project-wide, never per-task: the question is whether the *project* uses the field, so every
    task's `context` header has the same shape and a reader is not left wondering why a field
    disappeared between two tasks.

    **Views only.** `list`'s two machine forms keep every configured column, because a key that
    vanishes the moment a field falls out of use is a breaking change to a caller that did nothing
    wrong. A view omits a column no task has a value for; a contract does not.
    """
    return [n for n in names if any(t.fields.get(n) for t in tasks.values())]


def label(name):
    return name.replace("_", " ").upper()


def summarise(task):
    return "%-12s %-11s %s" % (task.id, task.status, task.title)


def load(root):
    """Resolve the schema and the tasks, or explain why not.

    A configuration problem is reported *here*, when the config is read, and the command never
    starts. It is never raised from inside a task the user is trying to finish.
    """
    schema = load_schema(root)
    return schema, load_tasks(root, schema)


# ------------------------------------------------------------------------------- context

def cmd_context(root, schema, tasks, args):
    # No arity guard here: `main` rejects a wrong argument count for every command before dispatch,
    # so a second one would be a second home for "context takes an id" — and the copy that used to
    # be here is the one that would have drifted, since it named the shape in a printed string.
    wanted = args[0]
    if wanted not in tasks:
        print("No such task: %s" % wanted)
        return 1
    task = tasks[wanted]

    out = [RULE, "%s  %s" % (task.id, task.title), RULE]
    shown = [(f, task.fields.get(f, "")) for f in in_use(schema.context_fields, tasks)]
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

    # Facts, not an instruction: a next-step pointer is context, not authorization, so the
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
    """The generated region. A column appears only when some task uses it — edge **or** field.

    Omitting an unused column is derived from the data rather than configured, so a project with no
    hierarchy does not read a column of dashes and one that starts using it does not have to
    remember to switch a column on. That rule was here from the start and applied to edges only,
    which left `work_package` rendering 58 dashes in this repository's own index; T-070 extended it
    to the half it had always described.

    A **dependency** cell carries what still gates, not what once did (T-111). `context` prints each
    linked task's status beside its id, so a reader sees a closed blocker for what it is; a cell here
    is ids alone, so a satisfied edge and a live one are the same string and the artifact people open
    to choose work overstates what is held. Hierarchy and soft edges are untouched — a closed parent
    is still a parent, and a soft link gates nothing to begin with.
    """
    deps = set(dependency_names(schema))

    def shown(task, name):
        """The ids a cell prints: for a dependency, only those still outstanding.

        An id no task claims is **kept**. `check` reports a dangling reference, and filtering it out
        here on the grounds that it does not resolve would hide, from the one artifact people read,
        the very edge `check` is complaining about.
        """
        ids = task.links(name)
        if name in deps:
            ids = [t for t in ids if t not in tasks or tasks[t].is_open]
        return ids

    # `shown`, not `links` — filtering the cells alone would leave a project whose dependencies are
    # all satisfied reading a column of dashes, which is the defect the docstring above records as
    # fixed for fields. Both halves move together or the fix reintroduces it one edge kind over.
    names = [n for n in link_names(schema)
             if any(shown(t, n) for t in tasks.values())]
    columns = in_use(schema.index_columns, tasks)
    header = ["ID", "Title"] + [c.replace("_", " ").title() for c in columns] + \
             [n.replace("_", " ").title() for n in names]

    def row(task):
        cells = ["[%s](%s)" % (task.id, os.path.basename(task.path)), task.title]
        cells += ["`%s`" % task.fields.get(c, "-") if task.fields.get(c) else "-"
                  for c in columns]
        cells += [", ".join(shown(task, n)) or "-" for n in names]
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


def index_path(root, schema):
    """Where the generated index lives. One home for the name, because `check` compares against it."""
    return os.path.join(root, schema.tasks_dir, "README.md")


def cmd_index(root, schema, tasks, args):
    path = index_path(root, schema)
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
    examined = 0
    for task in ordered(tasks):
        for field, values in sorted(schema.vocabularies.items()):
            value = task.fields.get(field, "")
            if value and value not in values:
                problems.append("VOCABULARY    %s.%s is '%s'; allowed: %s"
                                % (task.id, field, value, ", ".join(values)))
            examined += 1
    return [("field value", examined)]


def check_references(schema, tasks, problems):
    examined = 0
    for task in ordered(tasks):
        for field in sorted(task.edges):
            for target in task.edges[field]:
                if target not in tasks:
                    problems.append("DANGLING      %s.%s -> %s does not exist"
                                    % (task.id, field, target))
                examined += 1
    return [("reference", examined)]


def check_blocked_without_blocker(schema, tasks, problems):
    if not schema.blocked_status:
        return []   # nothing walked; claiming the task count would be the very thing T-095 fixed
    dependencies = [f for f, e in schema.edges.items() if e.kind == "dependency"]
    for task in ordered(tasks):
        if task.status != schema.blocked_status:
            continue
        if not any(task.edges[f] for f in dependencies):
            problems.append("NO BLOCKER    %s is '%s' with nothing in %s"
                            % (task.id, schema.blocked_status, ", ".join(sorted(dependencies))))
    return [("task", len(tasks))]


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
    return [("dependency edge", sum(len(tasks[t].edges[f]) for t in tasks for f in dependencies))]


def check_stored_derived(schema, tasks, problems):
    derived = set(e.derives for e in schema.edges.values() if e.derives)
    for task in ordered(tasks):
        for name in sorted(derived & set(task.fields)):
            problems.append("STORED DERIVED %s stores '%s:', which is computed from '%s'; remove it"
                            % (task.id, name, source_of(schema, name)))
    return [("task", len(tasks))]


def source_of(schema, derived):
    for field, edge in schema.edges.items():
        if edge.derives == derived:
            return field
    return "?"


def check_deliverables(root, schema, tasks, problems):
    """Declared outputs must exist — but only once the task claims to have produced them.

    `deliverables` asserts production, and METHOD §1 rule 5 is the one place the method requires an
    outcome to exist: a task closes when its outcome exists. So the check keys on the task being
    closed, and an open task may name what it *will* produce — which is what makes a deliverable map
    derivable before the work happens (T-089).

    Keying on the phase reaching `implement` was rejected: a task that has just entered `implement`
    legitimately has no outputs yet, since producing them is what the phase is for.
    """
    if not schema.deliverables_field:
        return [("declared output", 0)]
    examined = 0
    for task in ordered(tasks):
        if task.is_open:
            continue
        for path in task.deliverables:
            if not os.path.exists(os.path.join(root, path.replace("/", os.sep))):
                problems.append("MISSING OUTPUT %s declares '%s', which does not exist"
                                % (task.id, path))
            examined += 1
    return [("declared output", examined)]


def check_stale_index(root, schema, tasks, problems):
    """The generated index against what the tasks would produce now — rendered, never fingerprinted.

    The comparison re-renders through `index_block`, the same call `cmd_index` writes with, so there
    is one idea of what the index looks like rather than two that eventually disagree. A stored hash
    or timestamp would be a written derived value, which the design rule forbids (METHOD §4), and
    one more field somebody has to remember to keep true — which is the condition this check exists
    to catch, so paying for it in a second place would be a poor trade (T-025 §1).

    **Nothing generated is not stale.** No file, or a file carrying no markers, reports nothing —
    otherwise a project is reported on its first run, before `index` has ever been asked for, and one
    that keeps a hand-written index deliberately is reported forever. The prose outside the markers
    is nobody's to police in either direction.

    **It is a denominator all the same.** Reporting nothing and comparing nothing were the same
    output until T-095: `0 index file(s)` is how a run says it had nothing to compare, which on a
    project that believes it generates an index is the whole finding.
    """
    path = index_path(root, schema)
    if not os.path.exists(path):
        return [("index file", 0)]
    text = read(path)
    if BEGIN not in text or END not in text:
        return [("index file", 0)]
    on_disk = text[text.index(BEGIN):text.index(END) + len(END)]
    if on_disk != index_block(root, schema, tasks):
        problems.append("STALE INDEX   %s no longer matches the tasks it was generated from; "
                        "run 'taskmd index'" % rel(root, os.path.relpath(path, root)))
    return [("index file", 1)]


def check_anomalies(root, schema, tasks, problems):
    """Files under `tasks_dir` that are not the task somebody thought they were.

    `load_tasks` records these rather than raising, so a defect in one file cannot stop a command
    about another — a problem is never raised from inside a task the user is trying to finish. This is where they surface — which is what makes `check`
    the one place a project's problems are listed, instead of a thing you find out by noticing a
    task is missing.
    """
    for anomaly in tasks.anomalies:
        where = [rel(root, os.path.relpath(p, root)) for p in anomaly.paths]
        if anomaly.kind == DUPLICATE_ID:
            problems.append("DUPLICATE ID  %s is claimed by %s. Only the first is loaded, so the "
                            "other is in no view and on no edge"
                            % (anomaly.task_id, " and ".join(where)))
        elif anomaly.kind == PARKED:
            problems.append("PARKED TASK   %s declares '%s', a valid id, but it sits under a "
                            "folder beginning with '_' or '.', which enumerate skips - so it is "
                            "loaded by nothing, is in no view and is on no edge"
                            % (where[0], anomaly.task_id))
        else:
            problems.append("ID WIDTH      %s declares '%s', which is not %s plus %d digit(s), so "
                            "it is not loaded as a task"
                            % (where[0], anomaly.task_id, schema.id_prefix, schema.id_width))
    return [("task", len(tasks))]


def blanked(text):
    return re.sub(r"[^\n]", " ", text)


def without_code(text):
    """`text` with fenced blocks and inline code spans blanked out, character for character.

    Blanked rather than deleted so every other offset stays where it was. An unclosed fence runs to
    the end of the document, which is what Markdown itself does with one.
    """
    out, fence = [], None
    for line in text.splitlines(True):
        opener = FENCE.match(line)
        if fence is None:
            if opener:
                fence = opener.group(1)
                out.append(blanked(line))
            else:
                out.append(CODE_SPAN.sub(lambda found: blanked(found.group(0)), line))
        else:
            out.append(blanked(line))
            if opener and opener.group(1)[0] == fence[0] and len(opener.group(1)) >= len(fence):
                fence = None
    return "".join(out)


def check_links(root, schema, problems, notes):
    """Every Markdown link in every document a clone would receive.

    **Two questions, answered differently on purpose** (T-094). On the *document* side the question
    is "would someone who cloned this find it?", so a gitignored document is not read: a dead link
    inside something no reader can reach is a promise to nobody. On the *target* side the question
    is asked twice: the file must be **here**, or the link is broken, and it must be **shipped**, or
    the link resolves for its author and 404s for every reader.

    T-094 asked only the first, deliberately, on the grounds that a project quarantining
    machine-local material has to be able to say where it lives. T-097 measured that: across this
    project's 151 published documents, every reference to its own quarantined file is a bare path in
    prose, which T-092 had already put out of scope, and the strict rule raised **no** file-level
    alarm at all. So the convention was never carried by links, and the exemption was protecting
    nothing. Reversed on that evidence, by the maintainer, on 2026-08-11.

    **Directories are exempt, and that is the whole of the difficulty.** `git ls-files` lists files,
    so no directory is ever in the visible set — published or not. Every one of the 12 alarms the
    unrefined rule raised here was a link to a directory. The rule as an adopter meets it is in the
    project's own README; this is the mechanism.

    The excluded count goes to `notes` rather than into the denominators, because a document that
    was skipped was not examined and reporting it as one would be the very claim T-095 removed.
    """
    visible = clone_would_receive(root)
    documents = links = excluded = 0
    for md in markdown_files(root, schema):
        if visible is not None and os.path.normpath(md) not in visible:
            excluded += 1
            continue
        base, where = os.path.dirname(md), rel(root, os.path.relpath(md, root))
        documents += 1
        for match in LINK.finditer(without_code(read(md))):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            full = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(full):
                problems.append("BROKEN LINK   %s -> %s" % (where, target))
            elif visible is not None and os.path.isfile(full) and full not in visible:
                problems.append("IGNORED LINK  %s -> %s is here but no clone receives it, so the "
                                "link resolves for you and 404s for every reader"
                                % (where, target))
            links += 1
    notes.append("every document read; no git here, so .gitignore was not consulted"
                 if visible is None else
                 "%d document(s) not read: a clone would not receive them" % excluded)
    return [("document", documents), ("link", links)]


def ordered(tasks):
    return [tasks[t] for t in sorted(tasks)]


def examined(counted):
    """The denominators, merged by noun in the order the checks ran.

    Every check returns what it looked at, so the summary is assembled from the checks that actually
    ran rather than from a list somebody maintains — add a check without a `return` and the merge
    raises here rather than quietly reporting a coverage the run never had (T-095).

    Merged by **largest**, never summed: three checks walk the task set, and summing would report
    288 tasks over a project that has 96.

    **A narrower walk gets its own noun rather than merging into the wider one** (T-096). The first
    cut let `check_cycles` report its dependency edges as `reference`s, on the argument that the
    wider count would witness any narrowing — which is false, and measurably: reclassify one edge
    field from `dependency` to `soft` and the cycle walk covers nothing while the edge stays in
    `task.edges`, so the reference count does not move and the two summaries are byte-identical.
    """
    merged = []
    for noun, count in counted:
        for i, (seen, before) in enumerate(merged):
            if seen == noun:
                merged[i] = (noun, max(before, count))
                break
        else:
            merged.append((noun, count))
    return ", ".join("%d %s(s)" % (count, noun) for noun, count in merged)


def check_unreachable_templates(root, schema, problems):
    """A template the create path can never find — reported, because its absence is legal (T-101).

    The failure this exists for is silent in both directions. A project that keeps its templates in
    `tasks/_templates/` gets an empty listing, and the documented reading of empty is *a project
    with no template is a normal project* — so a template that is present and unreachable is
    indistinguishable from one that was never written. `_templates/` is not a careless place to put
    them either; it is the obvious one, and this repository used it until T-076.

    The count is the other half. Templates are counted whether reachable or not, so a project is
    told it has none by a number rather than by silence — the gap was reported in both directions,
    and the absent one must not become a failure because the binding says a project with no template
    is a normal project. What counts as a template is `schema.templates`.
    """
    found = 0
    for path, reachable in templates(root, schema):
        found += 1
        if not reachable:
            problems.append("TEMPLATE UNREACHABLE %s carries a placeholder id, so it is a "
                            "template - but create lists '_'-prefixed files directly in %s/, so "
                            "nothing will find it" % (rel(root, os.path.relpath(path, root)),
                                                      schema.tasks_dir))
    return [("template", found)]


def check_template_fields(root, schema, problems):
    """A template's front-matter, held to the rules the task made from it will be held to (T-032).

    `load_tasks` reads a template and discards it, because a placeholder id is neither an id nor a
    near miss. That is right — a template is not work — and it is why both shipped templates could
    rot in silence: the audit one named a `type` the config did not have and stored a derived field,
    and the only thing that ever noticed was a person copying it out and running `check` on the
    result. Two of the four defects in that template were of exactly the classes `check` already
    reports for tasks; they were simply never asked of the file that produces them.

    **A placeholder is not a defect.** A value in angle brackets is a slot for the author to fill and
    is skipped. A `|`-separated value is a menu of what may go in the slot, and a menu is held to the
    *whole* vocabulary rather than to mere membership — a menu that has quietly fallen behind is the
    drift this exists to catch, and when this was written the shipped task template was still
    offering five of the seven types.
    """
    derived = set(e.derives for e in schema.edges.values() if e.derives)
    examined = 0
    for path, _ in templates(root, schema):
        where = rel(root, os.path.relpath(path, root))
        try:
            fields = split_front_matter(read(path))[0]
        except (OSError, ValueError, UnicodeDecodeError):
            continue    # `templates` already parsed it to get here; a race is not this check's to report
        for name in sorted(derived & set(fields)):
            problems.append("TEMPLATE FIELD %s stores '%s:', which is computed from '%s'; every "
                            "task copied from it starts invalid"
                            % (where, name, source_of(schema, name)))
        for field, values in sorted(schema.vocabularies.items()):
            examined += 1
            value = (fields.get(field) or "").strip()
            if not value or (value.startswith("<") and value.endswith(">")):
                continue
            if "|" in value:
                offered = sorted(v.strip() for v in value.split("|"))
                if offered != sorted(values):
                    problems.append("TEMPLATE FIELD %s offers '%s' for '%s'; the schema allows %s"
                                    % (where, " | ".join(offered), field, ", ".join(values)))
            elif value not in values:
                problems.append("TEMPLATE FIELD %s sets '%s' to '%s'; allowed: %s"
                                % (where, field, value, ", ".join(values)))
    return [("template field value", examined)]


def check_config_drift(root, schema, advisories):
    """A pinned config that has fallen behind the shipped default — advisory, never a problem.

    It appends to `advisories` and never to `problems`, so the exit status does not move. That and
    the rule for what counts as drift are in `## When this file moves ahead of yours` in the
    default config; this does not restate them (T-100).
    """
    drifted, compared = drift_from_default(root, schema)
    for field, missing in drifted:
        advisories.append("%s: shipped default adds %s; this project's row does not carry %s"
                          % (field, ", ".join("'%s'" % v for v in missing),
                             "it" if len(missing) == 1 else "them"))
    return [("vocabulary row", compared)]


LABEL_SHAPED = re.compile(r"^v?[0-9]+\.[0-9]+$")


def check_label_shape(schema, tasks, advisories):
    """A front-matter value a reader will resolve as a version — advisory, never a problem.

    Two projects grouped a backlog into milestones, named the milestones after the version they
    expected to ship in, and in both the two sequences came apart: a release takes the next number on
    the published line whatever grouping its tasks belong to, so they are independent by construction
    and only look coupled at the start. The label then does not merely lag. It resolves, to a real tag
    that holds something else (T-137).

    It reads the **shape of a value** and never the name of a field, which is what lets it work with
    no configuration: taskmd has no concept of a milestone field, and gaining a key to name one would
    fail every project that wrote a config. Measured rather than assumed — it catches the defect under
    field names no schema mentions, and a project that means its labels reads one line per distinct
    value, for ever, with nothing to switch off. Legal states do not fail (T-100).

    Three or more components is a version recorded correctly and is left alone. The two estimate
    fields are exempt because a project estimating in days writes `1.5` and means a number.
    """
    exempt = set(f for f in (schema.value_field, schema.effort_field) if f)
    seen, examined = {}, 0
    for task in ordered(tasks):
        for field, value in sorted(task.fields.items()):
            if field in exempt:
                continue
            # A field the schema does not name is carried as written, so it arrives as a list when
            # the task wrote one. Both shapes hold values a reader resolves.
            values = value if isinstance(value, list) else [value]
            for item in values:
                examined += 1
                item = item.strip() if isinstance(item, str) else ""
                if LABEL_SHAPED.match(item):
                    seen.setdefault((field, item), []).append(task.id)
    for (field, value), ids in sorted(seen.items()):
        advisories.append("%s: '%s' on %d task(s) reads as a version; a release of that number is a "
                          "different thing" % (field, value, len(ids)))
    return [("front-matter value", examined)]


def table_cells(line):
    """A table row's cells, split the way GitHub-flavoured Markdown splits them.

    **Code spans are read, not skipped, and that is the whole subtlety.** `without_code` is what
    every other text check here reaches for and it is the wrong tool: Markdown splits a table row
    into cells *before* it parses inline spans, so a pipe inside backticks is a cell boundary and
    the code span is broken too. Two authors in this repository escaped a pipe inside a code span
    inside a table cell, which nobody does unless the backticks did not protect it (T-141 §3).

    Only `\\|` is an escape. It is blanked to NUL rather than removed so nothing shifts.
    """
    text = line.strip().replace(r"\|", "\0")
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return text.split("|")


def is_delimiter_row(line):
    """The `| :--- | ---: |` row. Its presence is what makes the line above it a header."""
    if "|" not in line:
        return False
    parts = table_cells(line)
    return any(cell.strip() for cell in parts) and \
        all(re.fullmatch(r":?-+:?", cell.strip()) for cell in parts if cell.strip())


def check_wide_rows(root, schema, problems):
    """A table row carrying more cells than its header — text that renders nowhere.

    Markdown drops a cell past the header count. So the text is in the file, absent from the page,
    and invisible to everything else this project runs: the instance that produced this check sat in
    a closed task for most of a week with `check` clean, the suite green and the pre-publish gate
    silent. The only instrument is counting cells against the header (T-141, from an adopter report).

    **A problem rather than an advisory**, which is the opposite of the three lines above it. Those
    report legal states a project may mean — a config behind the default, a version-shaped label, a
    second index mid-migration. Nobody means to write a cell that does not render, so the *legal
    states do not fail* test (T-100) puts this with the broken links instead.

    Two exemptions, both measured rather than assumed. **A fence is not a table**: this project
    quotes taskmd's own output constantly and `index` emits a table, so reading fenced blocks would
    make the tool's output the one thing a project could not quote (T-112's reasoning, for links).
    **An excess cell that is entirely blank is not reported**: the rule is text that renders nowhere,
    and a trailing pipe with nothing after it loses nothing. That is the one false-positive class the
    corpus could not price, having none of them.

    A short row is not reported at all: Markdown pads it and nothing is lost. Measured 0 in 2,812
    rows here, so the silence costs nothing either.
    """
    visible = clone_would_receive(root)
    scanned = 0
    for md in markdown_files(root, schema):
        if visible is not None and os.path.normpath(md) not in visible:
            continue
        where = rel(root, os.path.relpath(md, root))
        lines, index, fence = read(md).split("\n"), 0, None
        while index < len(lines):
            opener = FENCE.match(lines[index])
            if fence is not None:
                if opener and opener.group(1)[0] == fence[0] and len(opener.group(1)) >= len(fence):
                    fence = None
                index += 1
                continue
            if opener:
                fence = opener.group(1)
                index += 1
                continue
            if index + 1 < len(lines) and "|" in lines[index] and is_delimiter_row(lines[index + 1]):
                width, row = len(table_cells(lines[index])), index + 2
                while row < len(lines) and lines[row].strip() and "|" in lines[row]:
                    scanned += 1
                    cells = table_cells(lines[row])
                    if len(cells) > width and any(cell.strip() for cell in cells[width:]):
                        problems.append("WIDE ROW      %s:%d has %d cells against a %d-column "
                                        "header; Markdown drops the rest and that text renders "
                                        "nowhere" % (where, row + 1, len(cells), width))
                    row += 1
                index = row
                continue
            index += 1
    return [("table row", scanned)]


def check_duplicate_index(root, schema, tasks, duplicates):
    """A second table of the same tasks, outside the markers taskmd owns — advisory, never a problem.

    An adopting project has an old index generator by definition, and for a while both write the same
    file. Neither validator can see a block it does not own, so the duplicate passes every check
    either tool runs: the reporting project's `tasks/README.md` carried taskmd's generated block *and
    a second complete table of the same 56 ids*, and `check` said `OK` twice over it. It was found by
    a person noticing the file had grown (T-121).

    Nothing new is read. The known id set and the marker positions are both already in hand, so this
    is a scan over material the command has parsed.

    **A majority of the known set, not a fixed number** (T-121 Q1). A count that is quiet in a
    500-task project fires on ordinary cross-linking in a 20-task one, and there is no basis for
    choosing between them; a majority scales by construction. Distinct ids, counted once per file — a
    document naming one task eleven times is one id.

    **A task file does not count the ids it is entitled to carry** — its own, and the ones in its own
    edge fields. Q1 chose a majority partly on the ground that one "cannot be reached by a task file
    linking to its neighbours", and at scale that holds. It is arithmetic at three: this project's own
    `alt-project` fixture has three tasks, no duplicate anywhere, and the first cut of this rule fired
    on two of its files — each naming its own id, its epic and one sibling, which is three of three.
    Discounting the structural ids removes that whole class without touching the threshold, and a
    genuine duplicate table pasted into a task file still fires, because a table names ids the task
    never declared.
    """
    if not tasks:
        return [("document", 0)]
    visible = clone_would_receive(root)
    known, pattern = set(tasks), re.compile(r"%s\d+" % re.escape(schema.id_prefix))
    structural = {}
    for task in tasks.values():
        entitled = {task.id}
        for ids in task.edges.values():
            entitled.update(ids)
        structural[os.path.normpath(task.path)] = entitled
    scanned = 0
    for md in markdown_files(root, schema):
        if visible is not None and os.path.normpath(md) not in visible:
            continue
        scanned += 1
        outside, text = [], read(md)
        start = text.find(BEGIN)
        if start == -1:
            outside.append(text)
        else:
            end = text.find(END, start)
            outside.append(text[:start])
            if end != -1:
                outside.append(text[end + len(END):])
        seen = known & set(pattern.findall("\n".join(outside)))
        seen -= structural.get(os.path.normpath(md), set())
        if len(seen) * 2 > len(known):
            duplicates.append("%s: a second table of %d known task ids sits outside the taskmd "
                              "markers" % (rel(root, os.path.relpath(md, root)), len(seen)))
    return [("document", scanned)]


def cmd_check(root, schema, tasks, args):
    problems, counted, notes, advisories = [], [], [], []
    duplicates, label_shaped = [], []
    counted += check_anomalies(root, schema, tasks, problems)
    counted += check_vocabularies(schema, tasks, problems)
    counted += check_references(schema, tasks, problems)
    counted += check_blocked_without_blocker(schema, tasks, problems)
    counted += check_cycles(schema, tasks, problems)
    counted += check_stored_derived(schema, tasks, problems)
    counted += check_deliverables(root, schema, tasks, problems)
    counted += check_stale_index(root, schema, tasks, problems)
    counted += check_links(root, schema, problems, notes)
    counted += check_wide_rows(root, schema, problems)
    counted += check_unreachable_templates(root, schema, problems)
    counted += check_template_fields(root, schema, problems)
    counted += check_config_drift(root, schema, advisories)
    counted += check_label_shape(schema, tasks, label_shaped)
    counted += check_duplicate_index(root, schema, tasks, duplicates)

    if problems:
        for problem in problems:
            print(problem)
        print("")
        print("%d problem(s) - %s" % (len(problems), examined(counted)))
    else:
        print("OK - %s" % examined(counted))
    # Advisories before scope, and on both branches: a project whose config has fallen behind is
    # in a legal state, so the line has to survive a run that also found real problems.
    for advisory in advisories:
        print("CONFIG DRIFT  %s" % advisory)
    # Its own prefix rather than a second `CONFIG DRIFT` line: both are advisories and neither is
    # the other, so a project grepping for one should not receive the other (T-121).
    for duplicate in duplicates:
        print("DUPLICATE INDEX  %s" % duplicate)
    for shaped in label_shaped:
        print("LABEL SHAPE  %s" % shaped)
    # What was *not* looked at, on both branches for the reason the denominators are on both: a
    # scan narrowed by an exclusion hides behind a problem exactly as well as behind a pass.
    for note in notes:
        print("Scope  %s" % note)
    if problems:
        return 1
    print("structure and references only - it cannot tell you whether a spec or an outcome is good")
    return 0


# ---------------------------------------------------------------------------------- list

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
    """Every `--name` the command accepts, as {name: kind}.

    Vocabularies and link names were the whole set (T-022), which left the schema's own promise
    half-kept: a field taskmd does not enumerate is *carried*, and naming it in a view makes it
    appear with no code change — but not selectable, which is the one thing wanted once the view
    gets long. So **a field the project has named in a view is a field the project can filter on**
    (T-087). It needs no new config key, and it keeps the two halves of one promise together.

    Read from the config, never from what the tasks happen to hold. An accepted set derived from
    current contents would make a command's validity depend on when it runs — the argument that
    settled this task's open question about *values*, which applies to names just as squarely.
    """
    names = dict((f, "vocabulary") for f in schema.vocabularies)
    for name in link_names(schema):
        names[name] = "link"
    for name in list(schema.context_fields) + list(schema.index_columns):
        # `setdefault`: a field that is both enumerated and shown keeps its vocabulary kind, so its
        # value is still validated. Only the ones nothing enumerates arrive as a plain field.
        names.setdefault(name, "field")
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
        # The name is checked before the value, because a flag this project does not have is not one
        # any value could complete (T-113). The other order answered the likelier typing — a flag
        # remembered wrongly and typed alone — with `needs a value`, pointing away from the message
        # that names the vocabulary. `limit` is recognised here as well as below: it is accepted but
        # is not a filter, so it never appears in `known`.
        if name != "limit" and name not in known:
            # `arg`, not `name`: the flag is quoted back as the caller typed it, hyphens and all
            # (T-120). Normalising it here quoted a string they could not find in their own history,
            # in the one case — a misspelling — where they are comparing character by character.
            # The accepted list beside it is the schema's own spelling and teaches the canonical
            # form, so the two are doing different jobs rather than disagreeing.
            return None, ("unknown filter: %s. This project accepts: %s"
                          % (arg, ", ".join("--" + n for n in sorted(known))))
        if not rest:
            return None, "%s needs a value" % arg
        value = rest.pop(0)
        if name == "limit":
            if not value.isdigit():
                return None, "--limit needs a whole number, not '%s'" % value
            options["limit"] = int(value)
            continue
        if known[name] == "vocabulary" and value not in schema.vocabularies[name]:
            # The third of the three rejections, on the same rule as the two above (T-122). It names
            # the field twice and the two spellings are deliberate: `arg` is the flag as typed, to be
            # recognised; `name` is the schema's own, to be copied. Dropping the second would read
            # better and would stop the message stating the field's canonical form anywhere.
            return None, ("%s does not take '%s'. This project's %s values are: %s"
                          % (arg, value, name, ", ".join(schema.vocabularies[name])))
        filters.append((name, known[name], value))
    return (filters, options), None


def matches(task, filters):
    for name, kind, value in filters:
        if kind == "link":
            if value not in task.links(name):
                return False
        # `vocabulary` and `field` compare the same way — the kinds differ in whether the *value*
        # was validated at parse time, not in how it is matched. An unenumerated value is matched
        # literally and an empty result at exit 0 is the answer (T-087): with no list to check
        # against, the tool cannot tell a typo from an empty bucket, so any error would be a guess.
        elif task.fields.get(name, "") != value:
            return False
    return True


def cmd_list(root, schema, tasks, args):
    """A subset of the tasks, in priority order, rendered so the caller can use it as printed.

    The fourth command, and the one that was argued for: filtering is in, a query language is not.
    The module docstring says where that was settled. Writes nothing.
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
    #
    # The blocked column is appended last so no existing field moves, and only when the project
    # has a blocked task at all — the omit-when-unused rule `## Views` states, tested project-wide
    # so every call has the same shape. `--json` carries it unconditionally for callers that need
    # it whatever the project looks like. The rule is in `## Ordering`; this does not restate it.
    marked = any(is_blocked(schema, tasks, t) for t in tasks.values())
    for task in chosen:
        cells = [task.id] + [task.fields.get(c, "") or "-" for c in columns] + [task.title]
        if marked:
            cells.append("blocked" if is_blocked(schema, tasks, task) else "-")
        print("\t".join(cells))
    return 0


# ---------------------------------------------------------------------------------- main

COMMANDS = {"context": cmd_context, "index": cmd_index, "check": cmd_check, "list": cmd_list}

# What each command accepts after its own name, as the placeholders its rejection line shows.
# `list` is absent on purpose: its flags *are* the project's vocabulary, read from the config at
# run time, so it validates its own arguments and names the project's own values when it refuses
# (T-022). A second table here could not know those values and would be a second home for the ones
# it did know.
ARGUMENTS = {"check": (), "index": (), "context": ("<id>",)}


def usage_line(command=None):
    """The one usage line. `taskmd`, not `python -m taskmd`.

    It is read by someone who has already mistyped, and the one who needs telling is the adopter,
    who has the plugin on PATH and no source tree. It cannot be derived — every route into this
    module ends in `python -m taskmd`, so argv[0] is the same however the user got here (T-055).
    """
    if command is None:
        return "usage: taskmd {%s} [args] [--root PATH]" % ",".join(sorted(COMMANDS))
    return "usage: taskmd %s%s [--root PATH]" \
        % (command, "".join(" " + placeholder for placeholder in ARGUMENTS[command]))


def main(argv):
    # `newline="\n"` for the same reason `write()` sets it: without it Python's text layer rewrites
    # every `\n` as `\r\n` on Windows, so what taskmd *prints* was the one thing the promise of
    # identical output on every platform did not cover. Measured by T-020 — the generated files
    # matched byte for byte across Windows and Linux, all six console captures differed, and the
    # whole difference was the `\r`. It shows up in `list`, which exists to be parsed: the last
    # field of a row read back as `-\r` on one platform and `-` on the other. stderr is set the
    # same way even though one line goes there, so the next caller does not inherit a stream
    # configured unlike its twin (T-132).
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace", newline="\n")

    root, rest, asked_for_help = None, [], False
    argv = list(argv)
    while argv:
        arg = argv.pop(0)
        if arg == "--root":
            if not argv:
                print("--root needs a path")
                return 2
            root = argv.pop(0)
        elif arg in ("--help", "-h"):
            asked_for_help = True
        else:
            rest.append(arg)

    # Asking a tool what it does is not misuse. This printed the right line and exited 2, so the
    # conventional probe was reported as a failure — which costs more here than usual, because the
    # intended caller is an agent working out the surface. The top-level line only: per-command help
    # was offered and rejected by the maintainer (T-029), on the ground that a tool needing it would
    # be evidence against its own premise rather than a tool short of documentation.
    if asked_for_help:
        print(usage_line())
        return 0

    if not rest or rest[0] not in COMMANDS:
        print(usage_line())
        return 2

    # Before discovery, before the config is read, before anything is printed or written. An
    # argument the tool does not understand used to be dropped in silence by three of the four
    # commands, and `index` would go on to *perform its write* and report success — so the evidence
    # that a mistyped flag had done something was the same output as the evidence that it had
    # (T-029). The reasoning that puts a configuration error at setup, applied at the command
    # layer: a tool that is believed must not report success over something it never looked at.
    if rest[0] in ARGUMENTS and (len(rest) - 1 != len(ARGUMENTS[rest[0]])
                                 or any(a.startswith("-") for a in rest[1:])):
        print(usage_line(rest[0]))
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

    command = COMMANDS[rest[0]]
    if command is not cmd_check and tasks.anomalies:
        # One line, and not the detail — the detail is `check`'s, and a second copy of it here
        # would be a second home for one fact. What this removes is the silence: before it, a task
        # could vanish from `list` with nothing printed anywhere and exit 0. It goes to stderr so
        # stdout stays byte-for-byte what it was, and a script cutting the tab-separated form or
        # parsing `--json` is unaffected.
        sys.stderr.write("taskmd: %d problem(s) with the task files - run 'taskmd check'\n"
                         % len(tasks.anomalies))
    return command(root, schema, tasks, rest[1:])
