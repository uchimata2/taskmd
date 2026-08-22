---
id: T-213
title: Test whether the description loses a competition rather than turning a session away
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-206, T-175, T-205]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-213 — Test whether the description loses a competition rather than turning a session away

## 1. Specify

**Outcome**
A tested answer to whether the shipped `description` fails to *win* against a realistic field of
other skills in a project on a non-file backend — as distinct from failing to *apply*, which
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) tested
and answered.

**Why this one**
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) ran its
rig on 2026-08-22 and got a clean null: **6 of 6 arm runs invoked the skill**, three under each
wording, in a project whose config says there are no task files. So the opening clause does not give
a session a reason to *stop*.

**That answers the hypothesis T-206 stated, and it does not explain the observation both tasks came
from.** [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) watched a
session that was served this skill **among 68** and never invoked it. T-206's arms serve **one**
skill, so a prompt near its own words has nothing to lose to — the rig can detect a description that
turns a session away and cannot detect one that comes second.

**The two hypotheses are not the same and only one has been tested.** *Does not apply* is about the
description's content read on its own. *Does not win* is about it read beside sixty-seven others, and
the observation is equally consistent with both. Closing the question on T-206's null would be
reading a result about the first as though it settled the second.

**Scope**
- In: a rig whose arms carry a **realistic field** of other skills, not one
- In: the same two wordings T-206 built, so the arms remain comparable to its runs
- In: what counts as *winning* when several skills could plausibly serve one request
- Out: T-206's verdict, which stands. This does not re-open it
- Out: a third real venue.
  [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) settled
  that none is sought, and the owner licensed a synthetic rig on 2026-08-22

**Inputs**
- [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) §3 —
  the rig, its build script, the two wordings, and the eight runs
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 — the
  observation, and the field of 68 it happened in
- `plugin/skills/taskmd/SKILL.md` — the description, unchanged by T-206

**Acceptance criteria**
- [ ] The result names a direction and does not hedge — the description loses the competition, does
      not, or cannot be determined by this rig
- [ ] **The field is realistic and its composition is stated**, so a reader can judge whether the
      competitors were ones a real session would have. What failure looks like: a field of decoys
      chosen to be easy to beat, which measures nothing
- [ ] The arms are shown to differ **only** in the wording, by diffing them — T-206's criterion, and
      the field must be identical between arms as well
- [ ] Each arm's instrument is shown to have loaded the wording it is testing, quoted from the run
- [ ] The run count per arm is fixed and stated before any result is read
- [ ] **The confound T-206 could not remove is shown to be removed here** — its runs are quoted
      beside these so the difference between one skill and a field is visible, not asserted

**Open questions**
- **None.** The scope is the residual T-206 named when its own confound list was written.

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
| 2026-08-22 | → proposed | Raised from [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) while writing that task's confound list, which is where its own rig's limit became legible. T-206 got a clean null — 6 of 6 arm runs invoked the skill — and that answers *does the clause turn a session away*. It does not answer *does the description come second among 68*, which is what [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) actually watched. Raised rather than folded in: T-206's run count was fixed before its results were read, and adding a condition after seeing a clean null is the iteration that criterion exists to prevent. `m` because a realistic field has to be built and justified, and the justification is the hard half. |
