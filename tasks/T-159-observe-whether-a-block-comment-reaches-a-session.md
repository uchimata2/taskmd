---
id: T-159
title: Observe whether a block comment in CLAUDE.md reaches a session
type: analysis
status: proposed
phase: specify
parent: T-153
blocked_by: []
related: [T-050, T-155]
work_package: M6
owner: maintainer
business_value: high
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-159 — Observe whether a block comment in `CLAUDE.md` reaches a session

## 1. Specify

**Outcome**
An observation, from a session that started after the change, of whether the five block comments now
in `CLAUDE.md` are in what it was handed. Either the 663-character saving
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) recorded is real, or it is
not and the file grew instead.

**Why this one**
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) rests on a documented
harness behaviour that **no session in this repository has ever observed**, and it changed
`tests/test_budget.py` to follow that documentation. If the documentation is wrong, tier 1 is larger
than before and the one check that would have noticed is now looking past it.

**`high` for an `xs` task, deliberately.** The work is reading one thing once. What hangs on it is a
gate this project relies on, and [the project's own rule](../CLAUDE.md) is that a claim about
behaviour is verified by running the thing, never by reading its documentation.

**Scope**
- In: whether the commented text is present in what a fresh session receives unasked.
- In: the counted figure at that moment, so the observation and the check are compared rather than
  assumed to agree.
- Out: the path-scoped rule mechanism. That is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md), a different
  mechanism needing a different test, and folding them would make one failure look like two.
- Out: reverting anything. If the comments do reach a session, what to do about it is a decision, and
  this task supplies the evidence for it.

**Inputs**
- `CLAUDE.md` — the five comment blocks, listed in T-153's `implement`
- [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) — the documented behaviour
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) — how this repository
  established tier 1 by observation before, which is the method to repeat

**Acceptance criteria**
- [ ] The observation is made in a session that started **after** the change, and the record says so
- [ ] It reports what was found, not what was expected — including if the comments arrived
- [ ] The counted figure is taken in the same session and compared with the observation
- [ ] If the comments arrive, `tests/test_budget.py`'s strip is reported as unsound, and the task
      that decides what to do about it is named
- [ ] The result is written into this record on the day it is known

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
| 2026-08-15 | → proposed | Raised from [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s review, which met four of five criteria and could not meet the fifth: a session cannot observe a change to the instruction file it was handed before its first tool call. The maintainer chose to leave the observation to a later session rather than spend a subagent on it. T-153 is `blocked_by` this task and does not close until it answers. |
