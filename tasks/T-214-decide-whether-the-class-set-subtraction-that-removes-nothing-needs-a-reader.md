---
id: T-214
title: Decide whether the class-set subtraction that removes nothing today needs a reader
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-197, T-211, T-191]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-214 — Decide whether the class-set subtraction that removes nothing today needs a reader

## 1. Specify

**Outcome**
An answer, recorded in `tests/classes.py` beside the constant, on whether `NOT_A_CHECK_CLASS` needs
something that reads it — because measured today it subtracts nothing, and nothing says so.

**Why this one**
Found by [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) trying to
break its own new assertion and failing to. The first break attempt emptied `NOT_A_CHECK_CLASS` and
the assertion stayed green, which is what prompted the measurement:

```text
CONFIG ERROR in problem prefixes : False
CONFIG ERROR in ADVISORY_PREFIXES: False
union before subtraction         : False
NOT_A_CHECK_CLASS                : ('CONFIG ERROR',)
```

`cli.py` prints `CONFIG ERROR` from the config loader with a bare `print()` rather than a
`problems.append()`, so `PROBLEM_PREFIX_RE` never finds it and the union never holds it. The
subtraction removes nothing.

**It is a guard rather than dead code, and that is the whole difficulty.** Turning that `print` into
a `problems.append` — one line, and a change somebody could make for good reasons — puts
`CONFIG ERROR` into the set and the subtraction starts biting. T-211 measured both states: with only
the print changed the guard held and the assertion stayed green; with the guard also removed the
class entered the set and the assertion failed. So the line does real work in a world one edit away,
and none in this one.

**The risk is the ordinary shape of a guard nobody reads.** A reader meets a subtraction and assumes
it subtracts. If the derivation's shape changed so that `CONFIG ERROR` could never enter the union
again, the line would be inert permanently and nothing would report it — the same silence
[T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) and
[T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) exist over, one module
down.

**Scope**
- In: the decision — leave it with a note stating what it subtracts today, give it a reader, or
  remove it — recorded with the rejected alternatives and why
- In: implementing whichever the decision picks
- Out: changing how `cli.py` reports a config error. That is a shipped-behaviour question with
  adopter reach, and it is not this one
- Out: the two quiet cases T-211 could not mark, which are that task's record and
  [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md)

**Inputs**
- `tests/classes.py` — `NOT_A_CHECK_CLASS`, the derivation, and the comment stating the reason
- `plugin/skills/taskmd/taskmd/cli.py` — the two `print("CONFIG ERROR ...")` sites
- [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) §3 — the three
  break attempts that found this, and what each one measured

**Acceptance criteria**
- [ ] The decision is recorded in `tests/classes.py` beside the constant, with its rejected
      alternatives and the reason each was rejected
- [ ] If a reader is added, it is shown **failing first** on a tree where the guard has stopped
      mattering
- [ ] `python tests/test_quiet_cases.py` and the suite are green, and the output is quoted

**Open questions**
- **None.** The three options are named above; choosing between them is this task's work.

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
| 2026-08-22 | → proposed | Raised from [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md), which met it while obeying METHOD's *a check that has only ever succeeded has not been tested*: two successive attempts to break a new assertion both left it green, and this was why. `low` and `xs` — nothing is broken today, and the value is in not letting a measured fact about a guard evaporate with the session that measured it. Raised rather than fixed in place: T-211's scope is the marks and the reading, and `tests/classes.py` is T-197's artifact. |
