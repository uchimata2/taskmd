---
id: T-153
title: E-10 — Move the maintainer's justification into comments the harness strips
type: fix
status: proposed
phase: specify
parent: T-152
blocked_by: []
related: []
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-153 — E-10: move the maintainer's justification into comments the harness strips

## 1. Specify

**Outcome**
The passages of `CLAUDE.md` that argue a rule to a human maintainer stop being paid on every turn,
without leaving the file and without anything operative going with them.

**Why this one**
Finding [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md): block-level HTML comments
are stripped before an instruction file is injected. The finding is stated there and is not restated
here. The maintainer ruled on 2026-08-15 that **this one is taken first** — it saves less than
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) and it cannot fail.

**Scope**
- In: `CLAUDE.md`, and the split of each candidate passage into *justification for a human* or
  *instruction for the agent*.
- In: what the budget check should count afterwards — see the open question.
- Out: moving anything to another file. That is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md), and it is a
  hypothesis where this is not.
- Out: the tier-1 membership rule and the bound. Both are
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md)'s and stand.

**Inputs**
- [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) — the mechanism and its one risk
- `CLAUDE.md`
- `tests/test_budget.py`

**Acceptance criteria**
- [ ] Every passage moved into a comment is justification for a human, and the split is stated passage
      by passage rather than as a total
- [ ] Nothing operative for the agent went into a comment, checked by reading the result as a session
      would receive it
- [ ] The saving is measured after the change, in characters, with the date, and written here
- [ ] `tests/test_budget.py` passes, and what it now counts is stated
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Does the budget still measure what a session pays?** Verified 2026-08-15: `measure()` in
  `tests/test_budget.py` reads the whole file, so a comment stays inside the counted figure while
  leaving the per-turn cost. After this change the check over-counts by exactly what the change saved.
  Decide at `specify` whether the check strips block comments, or whether the figure stands and the
  discrepancy is recorded beside it. **The maintainer answers.**

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
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-10. `xs` and `medium`: the change is a pair of comment delimiters, and the gain is exact rather than estimated — the bytes leave the per-turn cost entirely. Filed as `fix` rather than `decision` because the mechanism is documented and the only judgement is which passages are justification, which the acceptance criteria make checkable. |
| 2026-08-15 | — | The open question above was found while raising this task, not by the audit: `measure()` reads the file whole, so E-10's remedy silently makes the budget check over-count. Recorded here rather than fixed, and it is the reason this task cannot be a two-line edit. |
