---
id: T-134
title: Check that every prose list of the commands names the commands there are
type: fix
status: proposed
phase: specify
parent: T-117
blocked_by: []
related: [T-030, T-031, T-055, T-071, T-073, T-117]
work_package: v0.5
owner: maintainer
business_value: low
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-134 — Check that every prose list of the commands names the commands there are

## 1. Specify

**Outcome**
A document listing taskmd's commands and getting the set wrong fails the suite, so
[T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)'s answer — *distinct
registers, deliberately repeated* — is safe rather than only argued.

**Why this one**
T-117 decided that `README.md` and `cli.py`'s docstring may both list the four commands, because they
say different things about them: purposes against flags, for readers who need one or the other. That
answer holds exactly as long as the two agree about **which** commands exist, and nothing checks
that. `usage_line` is derived from `COMMANDS` ([T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md),
[T-071](T-071-let-the-usage-test-assert-every-command-there-is.md)), so the *usage string* cannot
drift; the two prose lists can.

**It has already happened once.**
[T-073](T-073-correct-the-command-surface-local-context-still-states.md) is this project carrying a
document that stated a three-command CLI for four days after it was four, and the correction outlived
it in two tracked files. That is the failure this guards, measured rather than imagined.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule, from the other side — a fact allowed two homes needs
the two homes held together by something.

**Scope**
- In: the prose lists in `README.md` and in `plugin/skills/taskmd/taskmd/cli.py`'s module docstring,
  checked against `cli.COMMANDS`.
- In: what the check does about a document that mentions one command in passing, which is not a list.
- Out: reopening T-117. This exists because that answer was chosen, not instead of it.
- Out: the flags. `list`'s options are not a set anything else states, and checking them would be a
  second surface with its own drift.
- Out: `docs/SCOPE.md` non-goal 11 and `CLAUDE.md`, neither of which names a command — T-117 §3
  measured that, and a check aimed at them would be aimed at nothing.

**Inputs**
- [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md) §3, for which documents
  state the surface and which only appear to.
- `tests/test_publishing.py`, for the shape of a test that reads a rule out of a document rather than
  restating it.
- `plugin/skills/taskmd/taskmd/cli.py` — `COMMANDS`, the derived truth.

**Acceptance criteria**
- [ ] A command added to `COMMANDS` and not to `README.md` fails the suite, shown by doing it
- [ ] A command removed from a prose list fails too — the check is a set comparison, not a
      one-directional "everything listed exists"
- [ ] The check does not fire on a document mentioning a command in a sentence, shown on the real
      tree
- [ ] The test names, in its failure, which document is behind and which commands are missing

**Open questions**
- **Q1 — how does the check find "a list" in prose? — for whoever plans it.** *Recommended: a marked
  region*, the way the generated index uses markers, so what is checked is declared rather than
  guessed. *Alternative: heuristic* — treat any document containing every current command name as a
  list, which needs no markup and silently stops checking a document the day one command is dropped
  from it, which is the failure being guarded.

## 2. Plan

_Not planned._

## 3. Implement

_Not started._

## 4. Review

_Not started._

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised by [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)'s criterion 3, which asked what would have to be true for its answer to change. One of the two falsifiers has already happened in this project ([T-073](T-073-correct-the-command-surface-local-context-still-states.md), four days of a document naming a three-command CLI), so it is raised rather than left as a sentence. `low` and `s`: the failure is a wrong front door rather than a broken tool, and the work is one test plus a decision about how a list is recognised. Q1 is left open deliberately — it is a real fork with a cost either way, and answering it inside the task that raised it would be the absorption METHOD §3.3 forbids. |
