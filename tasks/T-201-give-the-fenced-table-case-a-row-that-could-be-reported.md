---
id: T-201
title: Give the fenced-table case a row that could be reported
type: fix
status: proposed
phase: specify
parent: T-198
blocked_by: []
related: [T-150, T-151]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-201 — Give the fenced-table case a row that could be reported

## 1. Specify

**Outcome**
`wide-table-row`'s *A table inside a fence* case holds a row that **is** wider than its header, so
that unfencing it would be reported — and the case can therefore detect a regression in fence
skipping. Its prose stops claiming something the row does not do.

**Why this one**
Finding **F-1** of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md). The
case is written as:

```text
| ID | Title |
| :--- | :--- |
| T-001 | this row is wider than its header and is not read |
```

**The row has two cells and the header has two columns.** It is not wider than its header. Measured
2026-08-21, on a copy of the fixture:

| Trial | Result |
| :--- | :--- |
| Unfenced, row left as it is | **silent** |
| Unfenced, and the row made genuinely wide | `WIDE ROW  ...T-002...:53 has 3 cells against a 2-column header` |

So the silence the fixture records is produced by the row's width, not by the fence. **If
`check_wide_rows` stopped skipping fenced blocks tomorrow, this case would stay quiet and nothing
would say so** — and the test that asserts an exact count of `WIDE ROW` lines would still pass,
because the count would not move.

**It is T-150 again, in the fixture T-150 built.**
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) found a negative case
in this same fixture that could not fire, and fixed that one. This is a second case beside it with
the same defect, and the reason it survived is that both look correct when read — which is
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s whole argument for making
a quiet case fire before trusting it.

**Scope**
- In: the row inside the fenced block, and the sentence describing it
- In: checking the fixture's other fenced or quoted cases for the same defect, since one instance
  makes the others worth a look
- Out: `check_wide_rows` itself. **The check is correct** — T-198 proved fence skipping works by
  removing the guard and watching the front matter report. This is a fixture defect
- Out: the exact-count test, which is right to exist and is not what failed here

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 — the two trials and
  their output
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`
- [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) — the same defect,
  found once before in this file

**Acceptance criteria**
- [ ] The fenced row is wider than its header, shown by unfencing a copy and quoting the `WIDE ROW`
      line that arrives
- [ ] With the fence restored, the fixture is silent again and the exact-count test passes unchanged
- [ ] The prose beside the case says what the row does, and does not claim what it does not
- [ ] The fixture's other quoted cases are each stated as checked or fixed

**Open questions**
- none

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
| 2026-08-21 | → proposed | Raised as finding F-1 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), the one quiet case of fifteen that could not be made to fire. `medium` and `xs`: the edit is one table row, and what it buys is a fixture case that can detect the regression it was written for. A child of T-198, which does not close until this resolves (`audit.md` step 5). |
