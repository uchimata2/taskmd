---
id: T-028
title: Budget the whole always-loaded context, not one file
type: decision
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-015, T-027]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-028 — Budget the whole always-loaded context, not one file

## 1. Specify

**Outcome**
The line budget `CLAUDE.md` sets governs everything that is actually loaded on every turn, so that
the test it states — *a spine that costs more than the flat version has inverted the point of
splitting it at all* — is a test the project can pass or fail rather than one it cannot see.

**Why this one**
Raised as **F-2** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 3 and 4. `CLAUDE.md` sets a 150-line limit on `docs/METHOD.md`, justified as sitting below
`reference/TASK-WORKFLOW.md` — the flat, single-document alternative — with headroom. The
justification's arithmetic is correct; the measurement is of one file:

| File | Lines | Loaded |
| :--- | ---: | :--- |
| `CLAUDE.md` | 139 | every turn |
| `docs/METHOD.md` | 147 | every turn, by its own statement |
| **Total always-loaded** | **286** | |
| `reference/TASK-WORKFLOW.md` — the flat alternative the limit is set against | 173 | — |

So by the stated test, the split has already inverted the point it was meant to protect — the budget
just does not measure the quantity it names. `docs/METHOD.md` is meanwhile at 147 of its 150, which
means the constraint is about to bind hardest on the file that is not the problem, and the next
addition to the spine will be refused for the wrong reason.

**This is not an argument that the split was wrong.** Progressive disclosure is R-21 and
[T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) did real work. The finding
is that the budget has one file in scope and two files in the cost.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Token cost*, which is a falsifiable property rather than a decoration.

**Scope**
- In: what the budget counts, what number it is set to, and where that is written.
- In: re-measuring after [T-027](T-027-give-the-design-rule-one-home.md) lands, since removing a
  duplicated section from `CLAUDE.md` changes the total this task is budgeting.
- Out: moving content out of either file. That is the *consequence* of a budget, and belongs to
  whichever task the budget forces. Deciding the measure first is what stops the cut being chosen to
  fit a number nobody agreed.
- Out: `docs/SCOPE.md`, `docs/BRIEF.md` and the `docs/method/` files — they are read on demand, not
  every turn, which is the distinction the budget exists to draw.

**Inputs**
`CLAUDE.md` §*Working method*, `docs/METHOD.md` §*Load on demand*, `docs/SCOPE.md` §1 and R-21,
[T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-2.

**Acceptance criteria**
- [ ] The budget names the **set** of always-loaded files, not one of them, and the set is checkable
      against the repository rather than being a list someone must remember to update
- [ ] The stated comparison against the flat alternative is one the project currently passes, or the
      gap is stated as a known, dated debt with the task that will close it — an unmet budget that
      reads as met is worse than no budget
- [ ] The number and its justification live in exactly one place, and the two do not have to be
      updated together
- [ ] Re-measured after T-027, so the decision is taken against the total the project will actually
      have rather than today's

**Open questions**
- Is `CLAUDE.md` in the budget's scope at all? It is the harness's project-instruction file rather
  than part of the method, so an argument exists for budgeting it separately — but it is loaded on
  every turn either way, and a budget that excludes the largest always-loaded file measures nothing.
  — maintainer. This decides the outcome, so it must be answered before `specify` closes.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Raised as F-2 from the T-026 audit, clauses 3 and 4. Measured, not asserted: 139 + 147 = 286 always-loaded lines against the 173-line flat alternative the limit is justified by. Typed `decision` rather than `fix` because what to count is a judgement, and moving content is deliberately out of scope until it is made. |
