---
id: T-184
title: Report a date-shaped value that is not a date
type: fix
status: proposed
phase: specify
parent: T-162
blocked_by: []
related: [T-146, T-106]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-18
adopter_visible: yes
deliverables: []
---

# T-184 — Report a date-shaped value that is not a date

## 1. Specify

**Outcome**
`check` reports a front-matter value that is date-shaped and is not a date, as a problem, and a test
holds it.

**Why this one**
[T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) ruled that it should, and
deliberately did not ship the code: a ruling that arrives with its implementation cannot be reviewed,
because a reader cannot tell whether the rule was adopted for being right or for being already
written. The ruling, its three rejections and the measurements behind it are in that record and are
not repeated here.

**The design in one line**: key on the **value**, never on the field name. That is what keeps the rule
clear of [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s refusal and of
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s price — it needs no config key,
because it never asks which field is a date.

**Scope**
- In: the check class, its message, and a test that fails without it.
- In: the shape the rule matches, and what it deliberately does not match.
- Out: re-opening whether to have it. That is T-162's, and it is closed.
- Out: detecting a date that is well-formed and wrong. Undetectable, and T-162 says so.

**Inputs**
- [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) §3 — the ruling, the
  probe's behaviour, and the three-corpus measurement
- `plugin/skills/taskmd/taskmd/cli.py` — where the other check classes live
- `plugin/skills/taskmd/README.md` and the advisory list — a new class may need naming there
  ([T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md))

**Acceptance criteria**
- [ ] `check` exits non-zero and names the file, the field and the value
- [ ] A test fails without the fix and passes with it — the fixture carries a malformed date, and it
      is shown failing first
- [ ] The rule reads no config key, and that is asserted rather than assumed
- [ ] Run on this repository and at least one sibling: the count is stated, and it is zero on clean
      data
- [ ] Wherever this project lists `check`'s classes, the list gains this one — the drift
      [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) exists to catch

**Open questions**
- None. T-162 settled the ruling, the form and the rejected alternatives.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-19 | (no change) | **The owner authorised this task to start**, on 2026-08-19, answering the backlog-wide question round the handoff of that date asked for. The authorisation covers **this task only** and nothing it raises. Recorded here rather than only in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). Nothing else changes: T-162's ruling, form and rejections stand as written, and this row is permission rather than an answer, because §1 records no open question. |
| 2026-08-18 | → proposed | Raised by [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md)'s review. The ruling is made and measured; this is the code. Kept separate on purpose — T-162 §2 records the reason as a `plan` decision rather than discovering it at close. Outside the standing grant of 2026-08-18, which covers the six named tasks and **nothing any of them raises**. |
