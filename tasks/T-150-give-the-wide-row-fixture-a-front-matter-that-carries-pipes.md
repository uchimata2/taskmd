---
id: T-150
title: Give the wide-row fixture a front matter that carries pipes
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-032, T-141, T-151]
work_package: M6
owner: the project owner
business_value: low
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-150 — Give the wide-row fixture a front matter that carries pipes

## 1. Specify

**Outcome**
`WIDE ROW` staying silent on a front matter full of pipes is protected by the fixture rather than by
the accident that this repository's corpus happens to contain one.

**Why this one**
From the deck-building sibling's comment on `github.com/uchimata2/taskmd/issues/1`, 2026-08-14. Their
own scanner reported this project's shipped task template as the only defect in their tree, because
`effort: xs | s | m | l | xl` has five pipes and no table. It is one of three false positives they
hit, and the only one of the three ours could plausibly share.

**Ours does not fire, and that was measured rather than reasoned.** A specimen carrying all three of
their traps was run on 2026-08-15: a front matter with two pipe-carrying menus produced no alarm,
because a header line is only a header when the next line is a delimiter row, and no front-matter
line is. The evidence is in T-151 §1, which holds the whole specimen result.

**What is missing is the promise, not the behaviour.**
`tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md` is a genuinely strong
negative fixture — a blank excess cell, an escaped pipe, a short row, a fenced table, and a real
table after the fence, with the test asserting an exact count of three. Front matter carrying pipes
is the one class of theirs it does not hold. So the silence is currently proven by the corpus, and a
corpus is a weaker instrument than a fixture: it changes without anyone deciding to change it, and
the shipped template could stop using a `|`-separated menu for reasons that have nothing to do with
this check.

**Requirements served**
R-16 (`docs/SCOPE.md`) — read in the direction the reporter names: a check is unproven where it has
no case that must *not* fire.

**Scope**
- In: one section added to the existing negative fixture, or its front matter extended, whichever the
  fixture's own shape prefers.
- In: the count the test asserts, which has to stay exact for the negative to mean anything.
- Out: changing `check_wide_rows`. It behaves correctly; this is about what holds it there.
- Out: the other two traps. Neither can arise here, and the reasoning is in T-151 §1.
- Out: whether the negative-case discipline earns a documented home, which is
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md).

**Inputs**
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md`
- `tests/test_cli.py` — `test_a_pipe_inside_a_code_span_is_still_a_cell_boundary`, which asserts the
  count.
- [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) — why the check reads code
  spans rather than blanking them.
- `tasks/_task-template.md` — the file their scanner reported, and the corpus evidence this replaces.

**Acceptance criteria**
- [ ] The fixture carries a front matter with a `|`-separated menu, and the asserted count does not
      move — shown by running the test, not by reading it
- [ ] Deleting the guard in `check_wide_rows` that keeps it quiet makes the test fail, so the new case
      is proven to be doing work rather than merely present

**Open questions**
- None.

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
| 2026-08-15 | → proposed | Raised from triaging the newest comment on issue #1. **Not a defect** — the specimen run that day shows the check already silent on this class, and the row is filed as a fixture gap rather than as the false positive the reporter met in their own code. `low` and `xs` because nothing is broken and the whole change is one section in a file that already exists. The second criterion is there because a negative case that would pass without the code under test is the failure mode this task exists to remove, one level up. |
