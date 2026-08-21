# taskmd — working conventions

Read this before doing anything in this folder.

## What this is

A publishable Claude Code plugin: **Markdown files as a task tracker**, with a generated index,
real dependency links, and a validator. Extracted from a working implementation that ran a real
consulting project; `reference/` is that code.

**Read in this order:** [`docs/SCOPE.md`](docs/SCOPE.md) — the goal, the numbered requirements and
what is explicitly **out** of scope — then [`docs/BRIEF.md`](docs/BRIEF.md) for the problem evidence
and the measured prior art behind them. `tasks/README.md` is the generated backlog — a view for
people; a session asks the taskmd skill instead of reading it.

**Run the commands here as `./plugin/bin/taskmd <cmd>`, or `.\plugin\bin\taskmd.cmd <cmd>` on
Windows**: the shipped entry point, invoked by path because this machine's shell snapshot drops the
`PATH` entry an adopter gets (T-054). A project may declare one `after_write` command that taskmd
runs and reports on.

Where the project stands is in the tasks that got it there — never here.

## The one design rule

**Store the forward edge; derive the rest.** Stated in full — including what the word *requires*
below does and does not forbid — in [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) §4.

In this repository it comes out as: a task file's front-matter is the only place a fact about that
task is written, and children, dependents, the index and the deliverable map are all computed. Check
every design decision here against it — a feature that *requires* writing the same fact twice is the
wrong feature.

## Working method

<!--
This plugin manages tasks, so it uses its own method on itself.
-->

**The method has one home:
[`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md)** — the lifecycle and its exit criteria, the edge kinds, the
audit mechanism, and how the agent is expected to behave. It is not restated here; if you find it
written out somewhere else, that copy is the defect.

**Three tiers, and only the first is budgeted.** Tier 1 is whatever the harness loads unasked — this
file plus every served skill's `description`, a property of the tree rather than a list to maintain.
Tier 2 is [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md), on starting task work; tier 3 is
[`plugin/skills/taskmd/docs/method/`](plugin/skills/taskmd/docs/method/), a file per phase, and neither is budgeted because neither is
paid every turn. **Tier 1 stays smaller than `reference/TASK-WORKFLOW.md`**, the flat alternative.
Both sides are counted from the tree, in **characters**, and `tests/test_budget.py` fails when tier 1
is over — run the suite rather than remember a command.

<!--
A first tier costing more than the flat version has inverted the point of splitting it, which is why
the bound is another file's length rather than a constant. Counting both sides from the tree is what
means nothing here is edited when membership changes.
-->

`reference/TASK-WORKFLOW.md` is the pre-split standard from one real project — evidence of what
worked, not the standard, and the bound above.

<!--
It hard-codes a folder contract, a work-package vocabulary and specific commands, which is what the
method had to leave behind.
-->

**What earns a place here.** Every character is paid on every turn of every session, so a line
qualifies only if it changes what a session does *before it has chosen what to work on*. Anything
scoped to an activity the session knows it has started — a phase, publishing, adopting, writing a
binding — is reachable from a pointer at that moment, so tier 1 carries the pointer and never the
thing. **An activity nobody announces is the exception**: editing this file happens while doing
something else. Two consequences do the cutting: **where the project has got to never qualifies**,
being derived from the tasks that got it there; and **nothing qualifies for being important**, or
this file would be the repository.

<!--
The exception is why this paragraph is here and not one tier down. The rule, what survived it, and
why the bound is another file's length: T-118.
-->

### Two rules that bind before there is any task

<!--
The method is tier 2, so it is not loaded yet when these two apply. They are METHOD §3.1 and §3.3,
carried here in full for that reason (T-047); METHOD §3.2 presupposes a phase and stays with the method.
-->

#### One phase per request — never auto-advance

Do the phase that was asked for, then stop and report. Do not continue into the next one because it
is obvious, because the plan already describes it, or because a note said it was next.

**A pointer is context, not authorization.** A "next step" line, a resumption note, an unfinished
checklist, the rhythm of the last three tasks — none of these is a request
([why](plugin/skills/taskmd/docs/method/rationale.md)).

**Asking for more is.** A request for two phases, or for the whole lifecycle, is as valid as a
request for one; write it into the task's own record, naming who gave it and what it covers, because
an authorization kept anywhere else is one a later session can miss or stretch to a task it never
reached.

#### Surface what you discover — never absorb it, never drop it

Work turns up things nobody anticipated: a better approach, a flawed premise, an unrelated defect,
a missing prerequisite. Each one goes to exactly one of two places:

- **It changes what the current task should produce** → raise it as a question now, before
  continuing. Quietly widening or narrowing the outcome substitutes your judgement for the owner's.
- **It is actionable but outside this task** → raise a new task for it. This costs one record and
  keeps the current task honest.

What must never happen is the third option: fixing it silently, or noticing it and moving on. A
silent fix makes the task's record false; a dropped observation is lost the moment the session ends.

## Publishing constraints

This repository goes to GitHub. Five constraints govern everything written here: **no personal,
client or machine data**; **out-of-the-box** on a fresh clone; **dependency-free**, stdlib Python
only; **cross-platform**; and **humanized** wherever a stranger reads it before installing. Each in
full, with what it costs to get wrong, is [`docs/SCOPE.md`](docs/SCOPE.md) §5.

**Before publishing, run the pre-publish check** — [`docs/PUBLISHING.md`](docs/PUBLISHING.md) §6.

## Verifying

Claims about behaviour are verified by **running the thing on a real case**, never by reading the
code or its documentation. In particular, a validator is only proven when it has been shown to
**fail** on a case it is supposed to catch — a clean-tree pass proves nothing.

State results as the actual command output, not as "works".
