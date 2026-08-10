---
id: T-118
title: Decide what leaves tier 1 when the budget binds
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-026, T-028, T-047, T-115]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-118 — Decide what leaves tier 1 when the budget binds

## 1. Specify

**Outcome**
A decision, taken before the test goes red rather than during the edit that turns it red: what comes
out of tier 1 when it next exceeds its bound — or that the bound moves, with the reason it may.

**Why this one**
Carried out of [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md)'s review so that
closing the umbrella does not bury it. That review recorded a residual against its third criterion:
F-2, the audit's one clause-5 finding, named the cheaper **measure** — budget the whole always-loaded
set rather than one file — but not what to cut, and
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) put choosing the cut out of
scope. The residual was flagged for the owner and never answered.

**What has happened since, which changes the question rather than closing it.** The cheaper measure
was built and is now enforced: [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md)
made the budget a test, and it passes.

```
tier 1 7844 chars under by 2 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
```

So no cut was ever required — F-2's proposal was sufficient on its own, which is the answer to the
residual as it was posed. What is left is the next margin: **two characters**. The next ordinary
reconcile of `CLAUDE.md` turns the suite red, and at that moment somebody is mid-edit on something
else, which is the worst time to decide what a project's always-loaded context is for.

**This has been declined in passing twice.** T-028 scoped the cut out; T-047 moved two method rules
*into* `CLAUDE.md` and did not reopen it. Both were right to — a decision taken in passing while
doing something else is how the wrong thing gets cut. But twice declined and never raised leaves it
owned by nobody, which is the state this task exists to end.

**Requirements served**
R-15 (`docs/SCOPE.md`); `CLAUDE.md` *Three tiers, and only the first is budgeted*.

**Scope**
- In: what may leave tier 1, and by what rule — so the answer survives the next addition rather than
  naming one paragraph.
- In: whether the bound itself is right. It is `reference/TASK-WORKFLOW.md`'s size, chosen because it
  is the flat alternative the split must beat; a bound that is an artifact of another file's length
  is worth confirming deliberately rather than inheriting.
- Out: the two method rules `CLAUDE.md` carries verbatim (T-047). They bind before tier 2 loads, so
  tier 2 cannot be their home; moving them is not a cut, it is a regression.
- Out: changing how tier 1 is measured. That is settled and tested.

**Inputs**
`CLAUDE.md`, `plugin/skills/taskmd/SKILL.md`, `tests/test_budget.py`,
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md),
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md),
[T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) §4 criterion 3.

**Acceptance criteria**
- [ ] A rule is recorded for what belongs in tier 1, such that a reader with a candidate paragraph
      can tell whether it qualifies without asking — falsified by an answer that names what to cut
      today and gives the next session nothing
- [ ] The alternative is recorded with what it costs: moving the bound, and why the flat file is or
      is not the right thing to be measured against
- [ ] Whatever is decided, the test still passes and its margin is stated — a decision that leaves
      the margin at two characters has deferred the problem rather than taken it

**Open questions**
- ~~Is the answer a cut, or a different bound?~~ **Answered by the maintainer on 2026-08-11: state
  the rule first and let the cut fall out of it.** Tier 1's membership is already derived from the
  tree rather than listed, so a rule about what may be there is the same shape as everything else
  here, and it is what makes the *next* addition decidable rather than only this one. *Rejected:
  raising the bound.* It was defensible — the bound is another file's byte count, not a measured cost
  — but it converts a constraint into a number somebody chose, which is what the flat-file comparison
  exists to avoid, and it would have to be re-chosen every time the pressure returned.

  **What the answer settles, and what it deliberately does not.** It fixes the *order*: no paragraph
  is cut until the rule that would justify cutting it is written down. It does not pre-judge whether
  anything is cut at all — a rule may well find tier 1 already correct at 7,844 characters, in which
  case the finding is that the bound is the thing under pressure and criterion 2 is where that gets
  argued. Either outcome satisfies criterion 1; what it forbids is reaching for the largest paragraph
  under deadline, which is the failure this task was raised to prevent.

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
| 2026-08-11 | → specified | Answered by the maintainer the day it was raised: state the rule first, let the cut follow. Criteria stand as written — they were drafted to survive either answer, and criterion 2 is where the rejected option keeps its say, since "why the flat file is or is not the right thing to be measured against" is exactly the argument raising the bound would have made. Nothing here needed the owner beyond that: the remaining questions are `plan`'s. Handed to a clean session at the maintainer's request with `specify` complete and no work started. |
| 2026-08-11 | → proposed | Raised at T-026's close, so the umbrella's one unanswered residual gets an open home instead of expiring inside a closed task. The residual as posed is answered by events — F-2's cheaper measure was built, is enforced, and passes with no cut — so this is not that question re-asked; it is the two-character margin that answer left behind, and the fact that two tasks have now declined the cut in passing without anyone raising it. |
