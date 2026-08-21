---
id: T-204
title: Count the short-row quiet case the wide-row audit left out
type: fix
status: proposed
phase: specify
parent: T-198
blocked_by: []
related: [T-201, T-202]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-204 — Count the short-row quiet case the wide-row audit left out

## 1. Specify

**Outcome**
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 records `wide-table-row`
as carrying **four** quiet cases. It carries **five**, and the fifth — *A short row, which Markdown
pads* — appears nowhere in that record: not examined, not unproven, not true by construction. The
record names five and says what is known about each.

**Why this one**
Found while doing [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md), whose
scope reaches the fixture's fenced and quoted cases and stops there. The test asserting the fixture
silent names three quiet cases in its own words — blank excess, an escaped pipe and a short row
(`test_the_three_quiet_cases_are_quiet`). T-198 exercised blank excess and the escaped pipe, then
added the fence and the front matter and reached four. **The short row was substituted out rather
than counted.**

**It is already in reach, which is why this is small rather than why it should be dropped.** Measured
2026-08-21 on a copy of the fixture, by widening a row under that same three-column header:

```text
WIDE ROW      tasks/T-002-three-rows-that-lose-nothing.md:47 has 4 cells against a 3-column header
```

So the check reads that table, and the case is quiet because the row is short. Nothing is broken.
What is wrong is the record. T-198's third criterion requires a case that was not mutated to be
recorded as **unproven**; a case absent from the table is not recorded at all, which is the state
that criterion exists to prevent. And
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) will reconcile a computed set
against T-198's hand count, so a count that is one short is a discrepancy it has to spend work
resolving before it can trust either side.

**Scope**
- In: T-198 §3's case list and table, annotated so the fifth case is present with what is now known
- In: whether the other four fixtures T-198 examined case by case carry the same omission
- Out: **the mechanism** that would compute the set instead of counting it by hand, which is
  [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)
- Out: the fixture itself, which is correct and which
  [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) repaired

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 steps 2–4 — the case
  list, the alarms and the table
- [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) §3 — where the omission
  was found, and the trial quoted above
- `tests/test_cli.py`, class `TableRowWiderThanItsHeader` — the docstring naming three quiet cases
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`

**Acceptance criteria**
- [ ] T-198's record names five quiet cases for `wide-table-row`, each carrying what is known about
      it — proven, unproven, or true by construction
- [ ] The addition is written as an annotation: it says what was added and when, and does not rewrite
      what the audit said it did (METHOD rule 5)
- [ ] The other four fixtures T-198 examined are each stated as checked for the same omission
- [ ] The totals T-198 quotes elsewhere — fifteen cases, thirteen positives — are reconciled with the
      new count, or shown to be unaffected and why

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
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** the next steps by the project's own ordering rule, each through its **full lifecycle**. Resolved against `taskmd list --open` on 2026-08-21, the grant is [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md), then [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md), then [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) — **these three and no others.** Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **What the grant skips, and why, so nobody reads the order as arbitrary**: T-182, T-199, T-202, T-203 and T-206 each carry a live open question that is the owner's, and T-176 needs an uninvolved reader, who is a person and not a session. T-191 and T-198 are audit umbrellas that close when their children do, so neither is work to start. **This one is third.** Closing it also clears one of the two children holding [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) open; the other is T-202, which the grant does not reach, so **neither umbrella closes**. |
| 2026-08-21 | (no change) | **Confirmed by the owner on 2026-08-21 as belonging**, having been raised outside the two-task grant of the same day. Worth asking because that grant said it reached two tasks and no others; the answer is that raising is not starting, and `CLAUDE.md`'s *surface what you discover* binds whatever the grant covers. Written into this record rather than left in the reporting thread, for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) gives. |
| 2026-08-21 | → proposed | Raised under `CLAUDE.md`'s *surface what you discover* while doing [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md), and outside its scope, which reaches the fixture's fenced and quoted cases only. `low` and `xs`: the case is proven in reach, so this corrects a record rather than a behaviour — what it buys is that [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) reconciles against a count that is right. A child of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), which does not close until this resolves (`audit.md` step 5). |
