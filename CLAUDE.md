# taskmd — working conventions

Read this before doing anything in this folder.

## What this is

A publishable Claude Code plugin: **Markdown files as a task tracker**, with a generated index,
real dependency links, and a validator. Extracted from a working implementation that ran a real
consulting project — see `reference/` for the code that already works and `docs/BRIEF.md` for
what has to change to make it general.

**Read in this order:** [`docs/SCOPE.md`](docs/SCOPE.md) — the goal, the numbered requirements and
what is explicitly **out** of scope — then [`docs/BRIEF.md`](docs/BRIEF.md) for the problem
evidence and the measured prior art behind them. `tasks/README.md` is the generated backlog.

**Status:** the schema layer exists (`taskmd/`), the method document exists
([`docs/METHOD.md`](docs/METHOD.md), T-008), and the three commands exist — `python -m taskmd
{context,index,check}` (T-002). This project runs on them; the interim `tools/tasks/task.py` is
gone. `check` has been shown failing on seven of the eight classes it claims; the eighth is only
half proven, and the untested half **fails** — see T-019, which is the most load-bearing thing open.
The bindings and the skill are not written yet.

## The one design rule

**Store the forward edge; derive the rest.**

A task file's front-matter is the only place a fact about that task is written. Children,
dependents, the index, the deliverable map — all computed. Facts that are computed cannot drift
from facts that are stored, so no validator is needed to keep them honest.

Every design decision in this plugin should be checked against that rule. If a feature *requires*
writing the same fact twice, it is the wrong feature.

Note the word "requires". A link written on one task is visible from both ends because the inverse
is derived — so one write is always sufficient. Writing the other side as well is permitted and
collapses to a single entry; a two-way reference living in two places is the nature of references,
not drift. The rule forbids a design that **compels** the second write, not a user who makes one.

## Working method

This plugin manages tasks, so it uses its own method on itself. **The method has one home:
[`docs/METHOD.md`](docs/METHOD.md)** — the lifecycle and its exit criteria, the edge kinds, the
audit mechanism, and how the agent is expected to behave. It is not restated here; if you find it
written out somewhere else, that copy is the defect.

**The spine has a size limit: 150 lines.** It is loaded on every turn, so anything in it is paid for
on every turn. The number is set below `reference/TASK-WORKFLOW.md` (173 lines — the flat,
single-document alternative) with headroom, because a spine that costs more than the flat version
has inverted the point of splitting it at all. Before adding to `docs/METHOD.md`, check the count;
if the addition would breach the limit, that is the signal it belongs in an on-demand file, not an
argument for raising the limit.

What this project adds on top, because the method is deliberately storage-agnostic:

- Task files live in `tasks/`, created from `tasks/_templates/task-template.md`.
- The field names and their allowed values are the schema — `taskmd/defaults/config.md`.
- The index is **generated**, never hand-edited.
- A task is `done` only when its deliverables exist, its log is current, and the validator passes.

`reference/TASK-WORKFLOW.md` is the pre-split standard from one real project — evidence of what
worked, not the standard. It hard-codes a folder contract, a work-package vocabulary and specific
commands, which is precisely what `docs/METHOD.md` had to leave behind.

## Publishing constraints

This repository goes to GitHub. Everything written here must be:

- **Free of personal, client and machine data.** No real names, no absolute local paths, no
  drive letters, no hostnames. Write `<project>/tasks/` not a real path. Where a real identity is
  genuinely load-bearing evidence, it goes in `control/LOCAL-CONTEXT.md` — which is gitignored — and
  the tracked tree refers to it by the label that file defines. **Run the check below before
  publishing**; it is a grep because `docs/SCOPE.md` non-goal 11 keeps the CLI to three commands.
- **Out-of-the-box.** Someone who clones it must be able to run it with no path editing.
  Resolve paths relative to the repository root, not the working directory.
- **Dependency-free.** Python standard library only. A tracker that needs `pip install` before it
  can list your tasks is a tracker people abandon.
- **Cross-platform.** Windows, macOS, Linux. Write files with an explicit `newline="\n"` —
  Python's default text mode rewrites every `\n` on Windows and breaks byte-for-byte comparison.
  Console output should survive a cp1252 terminal: reconfigure stdout to UTF-8 at startup.

### The pre-publish check

Run over the tracked tree. It must print nothing; every hit is either a leak or a label that needs
adding to `control/LOCAL-CONTEXT.md`.

```bash
git ls-files -z | xargs -0 grep -nIE '\b[A-Za-z]:[\\/][A-Za-z0-9._-]+[\\/]|/(home|Users)/|[\\]{2}[A-Za-z0-9._-]+[\\]|[0-9]{1,3}(\.[0-9]{1,3}){3}'
```

Four classes: Windows drive paths, home directories, UNC paths, IP addresses. `git ls-files` is what
makes it meaningful — it sees exactly what a push would send, so anything gitignored is out of scope
by construction.

**Two limits, both deliberate.** A drive path is only matched with **two or more segments** after the
letter; a single-segment one is let through, because that form collides with ordinary text such as a
`d:\n` escape inside a code string — and a check that cries wolf gets ignored, which is worse than a
narrow one. (Do not write an example drive path here to illustrate that: the check reads this file
too, and an illustration is indistinguishable from a leak.) And **a
real name or a client project is not mechanically detectable at all**: that half is the label
discipline above, and it holds only if every new identity goes into `control/LOCAL-CONTEXT.md`
rather than into a task.

The pattern was verified by being made to fail (per *Verifying*, below): a fixture with one line per
class was caught on all four, plus a Windows drive path, while `https://`, a `d:\n` escape, a version
string and the prose phrase "drive letters" were correctly ignored. Two earlier drafts were wrong —
one ended a branch in `\\`, which grep read as an escaped `|` and which silently swallowed the entire
IP branch. That bug was invisible on a clean tree.

## Verifying

Claims about behaviour are verified by **running the thing on a real case**, never by reading the
code or its documentation. In particular, a validator is only proven when it has been shown to
**fail** on a case it is supposed to catch — a clean-tree pass proves nothing.

State results as the actual command output, not as "works".
