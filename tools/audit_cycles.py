"""The pre-release audit's cycle membership, derived rather than typed (T-255).

T-244 §2 assigns every item in the audit's subject to exactly one examining cycle. That assignment
was computed by hand on 2026-08-23 from a list that lived nowhere in the repository, so a file added
to `plugin/` afterwards would have belonged to no cycle and nothing would have said so. The audit
runs across many sessions and the tree moves between them, which is exactly the interval a
hand-typed partition cannot survive.

**The evidence is another project's and it is not hypothetical.** htmldeck ran the same method first
and its finding `PR-06` was this shape: the plan stated counts rather than deriving them, its two
coverage tables could not reconcile, and four files went unread while the run looked complete.

**The whole-partition verdict prints before any per-cycle answer.** An unassigned path stops the
reading rather than surviving it, and the exit code moves - a caution printed beside a table is read
once, by whoever wrote it.

This is repository machinery. It is outside `plugin/`, so an install never copies it.

Usage:

    python tools/audit_cycles.py            # the verdict alone
    python tools/audit_cycles.py --plan     # per-cycle files and bytes, as a table
    python tools/audit_cycles.py --cycle 4  # the files one cycle reads
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLUGIN = "plugin/skills/taskmd/"
DOCS = PLUGIN + "docs/"
METHOD = DOCS + "method/"
CODE = PLUGIN + "taskmd/"

# The three top-level files in the subject that are not under `plugin/`. T-244 §2 pins the subject
# as `git ls-files plugin/` plus these, plus the GitHub repository description - which is the 32nd
# item, carries no bytes, and is therefore not a path.
TOP_LEVEL = ["README.md", "LICENSE", ".claude-plugin/marketplace.json"]

REPOSITORY_DESCRIPTION = "the GitHub repository description"

# One rule per cycle, and this table is the only home for the assignment. Each rule is a callable
# taking a repo-relative path and returning whether that path belongs to the cycle. Order matters
# only for reporting: `assign` fails loudly on a path two rules claim, so the rules must be
# disjoint rather than merely ordered.
CYCLES = [
    (1, "The entry points", "A", lambda p: p in (
        "plugin/bin/taskmd",
        "plugin/bin/taskmd.cmd",
        PLUGIN + "taskmd.sh",
        PLUGIN + "taskmd.ps1",
        CODE + "__main__.py",
        CODE + "__init__.py",
    )),
    (2, "The landing surface", "B", lambda p: p in TOP_LEVEL or p == "plugin/.claude-plugin/plugin.json"),
    (3, "The adoption path", "C", lambda p: p in (
        PLUGIN + "SKILL.md",
        PLUGIN + "adopt.md",
        DOCS + "HANDOFF.md",
        CODE + "defaults/config.md",
    )),
    (4, "The binding documents", "D", lambda p: p == DOCS + "BINDING.md" or p.startswith(DOCS + "bindings/")),
    (5, "The method spine and its phases", "D", lambda p: p in (
        DOCS + "METHOD.md",
        METHOD + "specify.md",
        METHOD + "plan.md",
        METHOD + "implement.md",
        METHOD + "review.md",
    )),
    (6, "The method's supporting documents", "D", lambda p: p in (
        METHOD + "audit.md",
        METHOD + "rationale.md",
        METHOD + "uninvolved-reader.md",
        METHOD + "where-facts-live.md",
    )),
    (7, "cli.py, schema.py, and the two small modules", "A", lambda p: p in (
        CODE + "cli.py",
        CODE + "schema.py",
        CODE + "classes.py",
        CODE + "discovery.py",
    )),
    (8, "method/pre-release-audit.md", "B", lambda p: p == METHOD + "pre-release-audit.md"),
]


def subject(root=ROOT):
    """Every tracked path in the audit's subject, derived from git.

    Deriving rather than listing is the point of this module: a file added under `plugin/` appears
    here on the next run without anyone editing anything, which is what makes `assign` able to
    notice that no cycle claims it.
    """
    out = subprocess.check_output(
        ["git", "ls-files", "plugin/"] + TOP_LEVEL, cwd=root)
    return sorted(p for p in out.decode("utf-8").replace("\r\n", "\n").split("\n") if p.strip())


def assign(paths):
    """Map each path to its cycle number, and return (assignment, unassigned, doubled).

    Two failure modes, and both are reported rather than raised, so one run can name every problem
    instead of stopping at the first. A doubled path is checked because a total cannot see it: a
    file counted by two cycles keeps the sum correct while one of the two readings is wrong.
    """
    assignment = {}
    unassigned = []
    doubled = []
    for path in paths:
        claimed = [number for number, _, _, rule in CYCLES if rule(path)]
        if not claimed:
            unassigned.append(path)
        elif len(claimed) > 1:
            doubled.append((path, claimed))
        else:
            assignment[path] = claimed[0]
    return assignment, unassigned, doubled


def size_of(path, root=ROOT):
    return os.path.getsize(os.path.join(root, path.replace("/", os.sep)))


def verdict(root=ROOT):
    """The whole-partition verdict: (ok, lines, assignment, paths).

    Printed before any per-cycle answer, by every entry point below.
    """
    paths = subject(root)
    assignment, unassigned, doubled = assign(paths)
    lines = []
    ok = not unassigned and not doubled
    if unassigned:
        lines.append("UNASSIGNED  %d tracked path(s) in the subject belong to no cycle."
                     % len(unassigned))
        for path in unassigned:
            lines.append("    %s" % path)
        lines.append("    Add a rule in tools/audit_cycles.py CYCLES, or say in T-244 why the "
                     "subject changed. Until then no cycle's denominator is trustworthy.")
    if doubled:
        lines.append("DOUBLED  %d path(s) claimed by more than one cycle." % len(doubled))
        for path, claimed in doubled:
            lines.append("    %s -> cycles %s" % (path, ", ".join(str(c) for c in claimed)))
        lines.append("    A doubled path is invisible in a total: the sum still reconciles while "
                     "one of the two readings is wrong.")
    if ok:
        lines.append("PARTITION OK  %d tracked path(s), every one in exactly one of %d cycles."
                     % (len(paths), len(CYCLES)))
        lines.append("              plus %s, which carries no bytes - %d items."
                     % (REPOSITORY_DESCRIPTION, len(paths) + 1))
    return ok, lines, assignment, paths


def plan_table(assignment, root=ROOT):
    """Per-cycle file counts and byte totals, as a table.

    **T-244 §2 no longer has columns for these** — they were cut on 2026-08-23, because
    replacing typed figures with fresh ones bought about three hours before they drifted again.
    So this is read when a session wants the sizing, not pasted into a record.
    """
    rows = []
    total_files = 0
    total_bytes = 0
    for number, name, aspect, _ in CYCLES:
        members = sorted(p for p, c in assignment.items() if c == number)
        count = len(members)
        size = sum(size_of(p, root) for p in members)
        items = count + (1 if number == 2 else 0)  # the repository description sits in cycle 2
        rows.append("| %d | %s | %s | %d | %s | %d |" % (number, name, aspect, count, format(size, ","), items))
        total_files += count
        total_bytes += size
    rows.append("| | **Examining total** | | **%d** | **%s** | **%d** |"
                % (total_files, format(total_bytes, ","), total_files + 1))
    return rows


def main(argv):
    ok, lines, assignment, paths = verdict()
    for line in lines:
        print(line)
    if not ok:
        return 1

    if "--plan" in argv:
        print("")
        print("| # | Subject | Asp | Files | Bytes | Items |")
        print("| :-- | :--- | :-: | ---: | ---: | ---: |")
        for row in plan_table(assignment):
            print(row)
    for index, arg in enumerate(argv):
        if arg == "--cycle" and index + 1 < len(argv):
            number = int(argv[index + 1])
            members = sorted(p for p, c in assignment.items() if c == number)
            name = [n for num, n, _, _ in CYCLES if num == number]
            print("")
            print("cycle %d - %s - %d file(s), %s bytes"
                  % (number, name[0] if name else "?", len(members),
                     format(sum(size_of(p) for p in members), ",")))
            for path in members:
                print("    %s" % path)
            if number == 2:
                print("    %s (no bytes)" % REPOSITORY_DESCRIPTION)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
