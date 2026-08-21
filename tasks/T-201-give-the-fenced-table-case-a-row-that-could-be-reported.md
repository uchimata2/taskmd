---
id: T-201
title: Give the fenced-table case a row that could be reported
type: fix
status: done
phase: review
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
| 1 | Derive the fixture's fenced and quoted cases from the two files rather than recalling them, so *the other cases* is a set the tree states. | The list, with line numbers, in §3. |
| 2 | Give the fenced row a cell past its header, then unfence a copy and run `check` on it. | The `WIDE ROW` line the unfenced copy produces, quoted in §3. |
| 3 | Restore the fence; run `check` on the fixture and run the suite. | The fixture's silence, the unmoved row count and the suite result, quoted in §3. |
| 4 | Rewrite the sentence beside the case so it describes the row that is now there. | The edited paragraph in the fixture. |
| 5 | Put every other case from step 1 to the same question, and record each checked or fixed. | A row per case in §3. |

**Sequencing.** Step 1 is first because it is the only step that can widen the work: the scope admits
other quoted cases carrying the same defect, and meeting one at step 5 would re-cut steps 2–4. Step 2
produces an alarm before step 3 asks for a silence, because believing a silence that no positive
preceded is the failure
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s fourth criterion was
written against, and it binds on its child unchanged.

**Decisions**

- **Widen the row by giving it a third cell, not by narrowing the header to one column.** Either
  makes the row wider than its header in one line. The block is there to look like *quoted output* —
  the exemption exists because `index` emits a table and this project quotes it
  ([T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md)) — and a
  one-column header is not a shape taskmd emits, so that edit buys the alarm by making the case stop
  resembling the thing the fence protects. Three cells against a two-column header is also the shape
  [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) measured, so no trial has
  to be re-run to know what should arrive — 2026-08-21.
- **The exact-count test is not touched.** A fenced line is skipped before any row is counted, so a
  cell added inside the fence cannot move `12 table row(s)`. If it moved, that is the regression this
  case is being repaired to catch and not a number to adjust — 2026-08-21.

**Outputs**

- tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md
- tasks/T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md (§3)

## 3. Implement

### Step 1 — the fixture's fenced and quoted cases, derived rather than recalled

Both files scanned for fence openers and inline code spans, before any edit:

````text
== T-001-three-rows-that-lose-text.md
  span     31 `a | b`
== T-002-three-rows-that-lose-nothing.md
  span     15 `|`
  span     22 `check_wide_rows`
  span     23 `lines[index + 1]`
  span     23 `index + 2`
  span     25 `type`
  span     25 `business_value`
  span     26 `effort`
  fence    51 ```
  fence    55 ```
````

**One fenced block in the whole fixture**, and it is this case. Of the eight code spans, seven are in
prose; the one inside a table cell is `T-001:31`, which is a *reporting* case rather than a quiet one
and fires in every run below. So the scope's *other quoted cases* is a set of one, and it needs no
repair — recorded in step 5 rather than assumed.

### Step 2 — the row, and the alarm it now produces

The row carried two cells against a two-column header, so it was not wide. It now carries three:

````text
| ID | Title |
| :--- | :--- |
| T-001 | a cell past the header | and this one renders nowhere |
````

Quoting it here is not an instance of the fault the test class warns must not be reproduced outside
the fixture: inside a fence the line renders as text, so no cell is dropped, and `check_wide_rows`
leaves the block before it counts a row. That is the same reason the fixture may hold it.

Unfencing that block on a **copy** of the fixture, nothing else changed:

```text
WIDE ROW      tasks/T-002-three-rows-that-lose-nothing.md:59 has 3 cells against a 2-column header; Markdown drops the rest and that text renders nowhere
```

That is the shape
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) measured when it raised the
finding — three cells against a two-column header — arriving from the fixture itself rather than from
a hand-made trial.

### Step 3 — fence restored: silent, and nothing else moved

`check` on the fixture, before the edit and after it, is the same three lines and the same totals:

```text
WIDE ROW      tasks/T-001-three-rows-that-lose-text.md:16 has 3 cells against a 2-column header; ...
WIDE ROW      tasks/T-001-three-rows-that-lose-text.md:22 has 4 cells against a 2-column header; ...
WIDE ROW      tasks/T-001-three-rows-that-lose-text.md:31 has 3 cells against a 2-column header; ...
3 problem(s) - 2 task(s), ... 12 table row(s), ...
```

`12 table row(s)` is the second witness and the more direct one: the block's three lines are still
counted as no table rows at all, so the exact-count assertion has nothing to adjust. The suite agrees:

```text
310 passed, 8 subtests passed
```

### Step 4 — the prose

The claim *this row is wider than its header and is not read* used to sit inside the row's own cell,
where it was false. The case now carries a sentence above the block saying what the row is — three
cells against a two-column header — what the silence is produced by, and that the case could not
previously catch anything, since a two-cell row is silent unfenced as well.

### Step 5 — the other quoted cases

| Case | Where | Result |
| :--- | :--- | :--- |
| A table inside a fence | `T-002` | **fixed** — steps 2–3 |
| A pipe inside a code span | `T-001:31` | **checked, no action.** It is a case that must *report*, not one that must stay quiet, and it reports in every run above |

**A fifth quiet case turned up that is neither fenced nor quoted.** The test asserting the fixture
silent names three quiet cases — blank excess, an escaped pipe and a short row — and
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) counted four for this
fixture by exercising the first two plus the fence and the front matter. **The short row is in
neither reckoning.** Widening a row under its three-column header on a copy shows the check does read
that table:

```text
WIDE ROW      tasks/T-002-three-rows-that-lose-nothing.md:47 has 4 cells against a 3-column header; ...
```

So nothing is broken and the record is one short. Outside this scope, which reaches fenced and quoted
cases only, and raised as
[T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) rather than fixed here
(METHOD §5).

**Decisions & assumptions**

- **Widened by adding a third cell, not by narrowing the header** — the block has to keep looking like
  quoted taskmd output, which is what the fence exemption protects
  ([T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md)), and a
  one-column header is not a shape taskmd emits — 2026-08-21.
- **The exact-count test was not touched**, and did not need to be: fenced lines are skipped before
  any row is counted, so `12 table row(s)` was unmoved by the edit — 2026-08-21.
- **The unfencing trial was run on a copy, never on the fixture in the tree** — a fixture briefly
  holding a real defect is a tree that briefly fails its own suite, and a trial that has to be undone
  is one that can be half-undone — 2026-08-21.
- **The short-row case was diagnosed but not repaired.** Running one trial to say whether the gap is
  coverage or record is what makes
  [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) honest rather than
  speculative; repairing T-198's record from inside its own child is what METHOD §5 forbids —
  2026-08-21.

**Outputs produced**

- [`tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`](../tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md)
- this record
- [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The fenced row is wider than its header, shown by unfencing a copy and quoting the `WIDE ROW` line that arrives | met | §3 step 2. Three cells against a two-column header; unfenced on a copy it reports at `:59`, and the line is quoted in full. The trial ran on a copy, so the tree never held the defect |
| With the fence restored, the fixture is silent again and the exact-count test passes unchanged | met | §3 step 3. `check` on the fixture is the same three `T-001` lines and the same `3 problem(s)` and `12 table row(s)` as before the edit, and the suite is `310 passed, 8 subtests passed` — the figure it was at when this task was raised |
| The prose beside the case says what the row does, and does not claim what it does not | met | §3 step 4. The false claim was inside the row's own cell; the case now carries a sentence above the block naming the widths, what produces the silence, and that the case could not previously catch anything |
| The fixture's other quoted cases are each stated as checked or fixed | met | §3 steps 1 and 5. The set was derived from both files rather than recalled — one fenced block, eight code spans of which one sits in a table cell — and each of the two is given a row: the fence fixed, the code span checked and reporting |

**Open questions, re-read before closing** (`review.md` step 5). §1 recorded none, and none arose for
anyone else to settle. The one residue is a task rather than a question:
[T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md), raised at `implement`.

**What this task is worth, stated plainly.** It repaired one fixture case, and the repair is worth
what the case can now detect: a regression in fence skipping shows up here, where before it would
have been silent and the exact-count assertion would not have moved either. It did **not** examine
the fixture's quiet cases in general — that was
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s, and the one gap this run
met in passing is [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) rather
than something done here.

**Child fix tasks raised**
- none. [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) was raised at
  `implement` under `CLAUDE.md`'s *surface what you discover*, and its parent is
  [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) — the record it corrects
  — not this task

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **The fenced case can now fire.** Unfenced on a copy it reports `3 cells against a 2-column header` at `:59`; fenced it is silent and `12 table row(s)` is unmoved, so the exact-count assertion needed no adjustment and the suite is unchanged at `310 passed, 8 subtests passed`. The other quoted case — the code span in a `T-001` table cell — is a *reporting* case and fires in every run, so the scope's sweep closes with one fixed and one checked. Acted on the authorisation of 2026-08-21 recorded in the row below; **[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) was not started**, which is what *and stop* named, so [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) both stay open. Raised [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) in passing — a fifth quiet case in this fixture that T-198's count omits; it is in reach, so it corrects a record and not a behaviour. |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** two tasks: [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) **and stop**, then [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) **through its full lifecycle**. Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **It reaches these two and no others.** *And stop* names a specific thing not to do: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) is T-201's sibling finding and the owner chose not to spend the session on it, so closing T-201 leaves [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) open on its other child, and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) open with it (`audit.md` step 5). Neither umbrella is to be closed. |
| 2026-08-21 | → proposed | Raised as finding F-1 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), the one quiet case of fifteen that could not be made to fire. `medium` and `xs`: the edit is one table row, and what it buys is a fixture case that can detect the regression it was written for. A child of T-198, which does not close until this resolves (`audit.md` step 5). |
