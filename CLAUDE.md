# taskmd — working conventions

Read this before doing anything in this folder.

## What this is

A publishable Claude Code plugin: **Markdown files as a task tracker**, with a generated index,
real dependency links, and a validator. Extracted from a working implementation that ran a real
consulting project; `reference/` is that code.

**Read in this order:** [`docs/SCOPE.md`](docs/SCOPE.md) — the goal, the numbered requirements and
what is explicitly **out** of scope — then [`docs/BRIEF.md`](docs/BRIEF.md) for the problem evidence
and the measured prior art behind them. `tasks/README.md` is the generated backlog.

**Status: published**, at `github.com/uchimata2/taskmd`, in both shapes — the marketplace plugin and
the copyable skill folder. `README.md` is the front door and lists the four commands. **Run them here
as `./plugin/bin/taskmd <cmd>`, or `.\plugin\bin\taskmd.cmd <cmd>` on Windows**: the shipped entry
point, invoked by path because this machine's shell snapshot drops the `PATH` entry an adopter gets
(T-054). It finds the project by walking up from where it is run, and a project may declare one
`after_write` command that taskmd runs and reports on.

`check` has been shown failing on **every** class it claims — one deliberately-broken fixture each,
so the set is `tests/fixtures/broken-*` and not a count written here. The backend contract is
[`BINDING.md`](plugin/skills/taskmd/docs/BINDING.md) and both bindings are written
([`bindings/`](plugin/skills/taskmd/docs/bindings/)). Everything else about where the project stands
is in the tasks that got it there.

## The one design rule

**Store the forward edge; derive the rest.** Stated in full — including what the word *requires*
below does and does not forbid — in [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) §4.

In this repository it comes out as: a task file's front-matter is the only place a fact about that
task is written, and children, dependents, the index and the deliverable map are all computed. Check
every design decision here against it — a feature that *requires* writing the same fact twice is the
wrong feature.

## Working method

This plugin manages tasks, so it uses its own method on itself. **The method has one home:
[`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md)** — the lifecycle and its exit criteria, the edge kinds, the
audit mechanism, and how the agent is expected to behave. It is not restated here; if you find it
written out somewhere else, that copy is the defect.

**Three tiers, and only the first is budgeted.** Tier 1 is whatever the harness loads unasked — this
file plus every served skill's `description`, a property of the tree rather than a list to maintain.
Tier 2 is [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md), on starting task work; tier 3 is
[`plugin/skills/taskmd/docs/method/`](plugin/skills/taskmd/docs/method/), a file per phase, and neither is budgeted because neither is
paid every turn. **Tier 1 stays smaller than `reference/TASK-WORKFLOW.md`**, the flat alternative —
a first tier costing more than the flat version has inverted the point of splitting it. Both sides
are counted from the tree, in **characters**, so nothing here is edited when membership changes:

```bash
{ cat CLAUDE.md; sed -n 's/^description: //p' plugin/skills/*/SKILL.md; } | wc -c; wc -c < reference/TASK-WORKFLOW.md
```

Why membership is derived rather than listed, why characters rather than lines, and why the bound is
that file: T-028, T-050 and T-063 — not restated here, which is the same rule this section opens with.

### Two rules that bind before there is any task

The method is tier 2, so it is not loaded yet when these two apply. They are METHOD §3.1 and §3.3,
carried here in full for that reason (T-047); §3.2 presupposes a phase and stays with the method.

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

What this project adds on top, because the method is deliberately storage-agnostic:

- Task files live in `tasks/`, created from `tasks/_task-template.md` — beside the task it becomes,
  not under it, so links survive the copy (T-076).
- The field names and their allowed values are the schema — `plugin/skills/taskmd/taskmd/defaults/config.md`.
- The index is **generated**, never hand-edited.
- When a task is `done` is [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) §1 rule 5; which artifact satisfies
  each of its conditions here is in
  [`plugin/skills/taskmd/docs/bindings/local-markdown.md`](plugin/skills/taskmd/docs/bindings/local-markdown.md).

`reference/TASK-WORKFLOW.md` is the pre-split standard from one real project — evidence of what
worked, not the standard, and the bound above. It hard-codes a folder contract, a work-package
vocabulary and specific commands, which is what the method had to leave behind.

## Publishing constraints

This repository goes to GitHub. Five constraints govern everything written here: **no personal,
client or machine data**; **out-of-the-box** on a fresh clone; **dependency-free**, stdlib Python
only; **cross-platform**; and **humanized** wherever a stranger reads it before installing. Each in
full, with what it costs to get wrong, is [`docs/SCOPE.md`](docs/SCOPE.md) §5.

**Before publishing, run the pre-publish check** — [`docs/PUBLISHING.md`](docs/PUBLISHING.md) §6. One
grep over every file a push would send, run last, and proven by a second run against its own fixture.
Read it at publication rather than on every turn; it was the largest thing this file carried, for a
moment that happens rarely (T-047).

## Verifying

Claims about behaviour are verified by **running the thing on a real case**, never by reading the
code or its documentation. In particular, a validator is only proven when it has been shown to
**fail** on a case it is supposed to catch — a clean-tree pass proves nothing.

State results as the actual command output, not as "works".
