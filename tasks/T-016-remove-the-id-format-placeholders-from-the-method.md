---
id: T-016
title: Remove the id-format placeholders from the method
type: fix
status: done
phase: review
parent: T-008
blocked_by: []
related: []
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - plugin/docs/method/plan.md
  - plugin/docs/method/review.md
---

# T-016 — Remove the id-format placeholders from the method

## 1. Specify

**Outcome**
No document in the method implies what a task identifier looks like.

**Requirements served**
R-13 (`docs/SCOPE.md`).

**Why this one**
Found reviewing [T-008](T-008-write-the-backend-neutral-method-document.md), against its acceptance
criterion 1 ("contains no field name, file path, **id format** or command"). Two occurrences leaked:

| Where | Text |
| :--- | :--- |
| `docs/method/plan.md:26` | a plan saying `"this needs T-x first"` |
| `docs/method/review.md:60` | a review row whose action is `→ **T-x**` |

Both are illustrative placeholders inside worked examples, which is exactly why they slipped past —
they read as prose, not as specification. But `T-x` says the identifier is a prefixed short code,
which is a local-Markdown convention. A project on an issue tracker has `#412`; one on a board has a
URL. The method must not have an opinion.

The fix is small. It is a task rather than an edit because review does not repair what it finds
([`../plugin/docs/method/review.md`](../plugin/docs/method/review.md)), and because a two-word fix that skips the
record is how the next one becomes invisible.

**Scope**
- In: the two occurrences above, and a check for any others.
- Out: task identifiers used in *this repository's own* task files, `CLAUDE.md`, `docs/SCOPE.md` or
  `docs/BRIEF.md` — those are this project's records, not the shipped method, and `T-NNN` is
  correct there.

**Acceptance criteria**
- [ ] `grep -rnE "T-[Nx0-9]" docs/METHOD.md docs/method/*.md` returns nothing
- [ ] Both worked examples still read as concrete examples — the fix must not turn them into
      abstractions, since their concreteness is what makes them useful
- [ ] No replacement smuggles in a different format (`#123`, a URL shape) in place of the old one

**Open questions**
- none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Widen the search beyond the two known hits, to any identifier shape rather than this project's. | the full occurrence list |
| 2 | Replace each with something equally concrete drawn from the surrounding worked example. | `docs/method/plan.md`, `docs/method/review.md` |
| 3 | Prove both the removal and the absence of a substituted format. | `grep` output in §4 |

## 3. Implement

**Decisions & assumptions**
- **Replaced with concrete references, not abstractions** (2026-08-04). The obvious fix — "the
  blocking task", "a child task" — would have satisfied the letter of the criterion and spoiled the
  examples, whose value is that they read like a real task rather than a schema. Both worked examples
  belong to the same research task, so each replacement was taken from *that* task's material:
  `plan.md` now says the plan needs "the contact-volume extract" first, and `review.md`'s unmet row
  carries "child task: state the seasonal confounder". Both name the thing itself, which is what an
  identifier stands in for anyway.
- **The search was widened past the reported defect** (2026-08-04). T-008's review found `T-x`; the
  step-1 sweep looked for any identifier shape — `#123`, `ITEM-`, `TASK-n`, an issue URL — on the
  grounds that a fix which only removes the format someone happened to notice leaves the next one in
  place. No further occurrences existed.

**Outputs produced**
- `docs/method/plan.md:25`, `docs/method/review.md:59`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `grep -rnE "T-[Nx0-9]" docs/METHOD.md docs/method/*.md` returns nothing | met | Exit 1, no output. |
| Both worked examples still read as concrete examples | met | Each replacement names a real object from the same research task — the contact-volume extract, the seasonal confounder — so the examples became *more* specific, not less. |
| No replacement smuggles in a different format | met | `grep -rnE "#[0-9]\|ITEM-\|TASK-[0-9]\|/issues/\|\bid\b"` across all seven method files: exit 1, no output. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Raised by T-008's review: acceptance criterion 1 not met. |
| 2026-08-04 | → done | Both occurrences replaced with concrete material from the same research example. Search widened to any identifier shape, not just this project's; nothing further found. |
