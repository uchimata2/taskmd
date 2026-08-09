---
id: T-089
title: Stop check reporting an open task's planned outputs as missing
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-002, T-025, T-032]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-089 — Stop check reporting an open task's planned outputs as missing

## 1. Specify

**Outcome**
A project can declare a task's outputs when it plans them, and `check` stays quiet about them until
the task claims to have produced them.

**Why this one**
`check` reports every declared path that does not exist, whatever the task's status. So a project
that fills `deliverables` at `specify` or `plan` time gets a permanent complaint about work it has
not started:

```
MISSING OUTPUT T-006 declares 'deliverables/D6-executive-board-presentation.md', which does not exist
```

Three of the six problems the first adopting project (`control/LOCAL-CONTEXT.md`) reported on the
day it migrated are of exactly this kind, and its tasks are correct: the field says what the task
will produce, which is what makes the deliverable map derivable before the work happens.

**This repository is not the counter-example it looks like.** Its tasks carry `deliverables: []`
until `implement`, so it never sees the message. That is a habit this repository fell into, not a
rule anything states, and it is why the defect survived to publication: the validator was only ever
run against a project that avoided the case.

**The retiring standard had the distinction and taskmd dropped it.** `reference/TASK-WORKFLOW.md`'s
tool separated `check` from `check --closing`, and only the closing form required declared outputs
to exist. That separation is the thing to reconstruct, in whatever shape suits four commands rather
than five.

**Why `high`.** A validator that cries wolf gets ignored, which is the argument `../CLAUDE.md` makes
for keeping the leak check narrow. This one cries wolf at exactly the moment an adopter is deciding
whether to trust it: their first run, on their real backlog.

**Requirements served**
R-16 (`docs/SCOPE.md`) — the validator is proven by being made to fail on what it claims to catch,
and a false positive is the other half of that. R-4 in spirit: verification belongs at `implement`'s
exit, not before it.

**Scope**
- In: when a declared-but-missing output is a problem, and what `check` says when it is not.
- In: whether the rule keys on `status` being closed, on the phase reaching `implement`, or on
  something the project configures. Each is a different claim about what `deliverables` means.
- Out: `deliverables` becoming a command again. It is a validation, settled in T-002 under non-goal
  11.
- Out: [T-025](T-025-let-check-notice-a-stale-generated-index.md), the other thing `check` cannot
  see. They touch the same command and answer different questions.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, the deliverables check inside `cmd_check`.
- `reference/TASK-WORKFLOW.md` §0, for the `--closing` distinction as it was.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, which assigns `deliverables` the role of
  METHOD §1 rule 5's *outcome* and already says only that one of the three closing conditions is
  mechanical.

**Acceptance criteria**
- [ ] A fixture with an **open** task declaring a path that does not exist passes `check`
- [ ] A fixture with a **closed** task declaring a path that does not exist fails it, with the
      message naming the task and the path
- [ ] Both fixtures are in `tests/fixtures/`, so the rule is proven by failing as well as by passing
- [ ] The binding says which condition it now checks, in one sentence, and nothing else restates it

**Open questions**
- **What "not yet" means, exactly.** Keying on closed status is the simplest and lets a task in
  `review` still be caught before it closes. Keying on the phase reaching `implement` catches a task
  that claims to be implementing while its outputs do not exist, which is closer to R-4 and is more
  to explain. The maintainer's, since it decides what the field asserts.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py`, `tests/`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised on the day the first project outside this repository adopted taskmd. Half of what its validator reported was noise of this one kind: tasks that declare their outputs when they plan them, which is what makes a deliverable map derivable in advance. This repository never saw it because its own habit is to leave `deliverables` empty until `implement`, so the case existed and was untested at publication. The retiring standard had the distinction as `check --closing`; taskmd dropped it without deciding to. `high` because a validator that cries wolf on an adopter's first real run is worse than one that says less. |
