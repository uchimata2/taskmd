---
id: T-160
title: Retire the budget check's unobserved-premise warning, now that it is observed
type: fix
status: proposed
phase: specify
parent: T-153
blocked_by: []
related: [T-159]
work_package: M6
owner: maintainer
business_value: low
effort: xs
created: 2026-08-16
updated: 2026-08-16
deliverables: []
---

# T-160 — Retire the budget check's unobserved-premise warning, now that it is observed

## 1. Specify

**Outcome**
`tests/test_budget.py` stops printing a sentence that is false. Its second report line currently ends
`not yet observed here (T-153)`; [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md)
observed it on 2026-08-16.

**Why this one**
The line was [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s plan step 5,
and its stated job was to keep an unobserved premise visible **until it was observed**. That
condition has now been met, so the line has outlived the reason it was written. It is small and it is
the kind of thing this repository treats as a defect rather than as tidying: a gate that prints a
false sentence on every run trains its reader to skim it.

**What replaces it is the decision, not the deletion.** The stripped figure itself is still worth
printing — it says how much of the file a session is not paying for. What has to change is the clause
claiming nobody has checked.

**Scope**
- In: the second line of `report()` in `tests/test_budget.py`, and any test that asserts on its
  wording.
- In: whether the observation is cited by date and task, so the claim stays checkable rather than
  becoming an unsourced assertion in the other direction.
- Out: the strip itself, and the figure it produces. Both are proven and neither changes.
- Out: `CLAUDE.md`. Nothing moves there; that is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)'s question.

**Inputs**
- `tests/test_budget.py` — `report()`, and the two tests that assert on its output
- [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) — the observation, its date and
  its marker
- [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) — why the line was written

**Acceptance criteria**
- [ ] The report no longer claims the behaviour is unobserved
- [ ] It still names the stripped figure, so the reader learns what a session does not pay for
- [ ] The new wording cites the observation by date and task, rather than asserting soundness flatly
- [ ] Any test asserting on the old wording is updated, and the suite passes
- [ ] The change is checked by running the report and reading its actual output, not by reading the
      code

**Open questions**
- none.

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
| 2026-08-16 | → proposed | Raised from [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s `review`, which found the line false the moment [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) answered. Filed rather than fixed inside that review: correcting it is `implement` work, and T-153 was authorised for `review` only. `low` and `xs` — one sentence, and nothing depends on it being taken soon; the falsehood is in a warning that has already done its job, not in a figure. |
