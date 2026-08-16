---
id: T-149
title: Check that every prose list of list's options names the options there are
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-117, T-134, T-144]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-149 — Check that every prose list of list's options names the options there are

## 1. Specify

**Outcome**
A document stating `list`'s flags and getting the set wrong fails the suite, the same way
[T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) already
makes that true of the command set.

**Why this one**
T-134 built exactly this check for the four command *names* and put the flags explicitly out of
scope, on a reason it stated: `list`'s options "are not a set anything else states, and checking them
would be a second surface with its own drift". That was true when it was written.

[T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) made it false.
`LIST_OPTIONS` is now the one home for those flags, read by `parse_filters` and by `list --help`, so
there **is** something else to check a document against and the second surface T-134 declined to
build already exists. The prose copies did not go away: `cli.py`'s module docstring and the skill's
own `SKILL.md` both spell the flags out, and nothing holds either to the table.

This is the same defect class T-073 measured — a document outliving its correction for four days —
one surface over.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule from the other side, that a fact allowed two homes needs
the two homes held together by something.

**Scope**
- In: the flag lists in `plugin/skills/taskmd/taskmd/cli.py`'s module docstring and in the skill's
  `SKILL.md`, checked against `cli.LIST_OPTIONS`.
- In: whether a document mentioning one flag in passing is a list — the same question T-134 answered
  for commands, and its answer may not transfer, since a flag is named in prose far more often than a
  command is.
- Out: the filters. Those are the project's own vocabulary rather than taskmd's, so a shipped
  document naming this repository's fields would be the defect, not the check's subject.
- Out: reopening T-117 or T-134. This exists because both answers were chosen.
- Out: `--root`, which is `main`'s and not in `LIST_OPTIONS`.

**Inputs**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  shape of the check, and the out-of-scope line this task exists to revisit.
- [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) §3 — what
  `LIST_OPTIONS` is and what already reads it.
- `tests/test_publishing.py` — how a test reads a rule out of a document rather than restating it.

**Acceptance criteria**
- [ ] A document listing `list`'s flags and missing one, or naming one that does not exist, fails the
      suite — shown by making it fail, not by reading the test
- [ ] The check derives the true set from `cli.LIST_OPTIONS` and writes no flag name of its own
- [ ] T-134's out-of-scope line carries a note saying what changed, so a reader does not conclude the
      flags were considered and excluded on grounds that still hold

**Open questions**
- **Is `SKILL.md` in reach of a test that runs here?** T-134's check reads `README.md` and `cli.py`;
  `SKILL.md` is inside the plugin subtree and is what an adopter is actually served. If the existing
  test's mechanism does not reach it, that is a finding worth more than this check — the project
  owner decides whether to widen it or to record the gap.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-15 | → proposed | Raised from T-144's `implement`, under METHOD §3.3: actionable, outside that task, so it costs one record rather than a silent widening. T-144 §1 named it as out of scope while `specify` was being written, before the home existed that makes it possible. `low` because the prose is correct today and the risk is drift rather than a live defect — but it is the drift class T-073 measured at four days, and the flags now have exactly the computed home whose absence was T-134's reason for declining. |
