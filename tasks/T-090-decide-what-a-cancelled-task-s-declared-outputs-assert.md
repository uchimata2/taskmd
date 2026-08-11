---
id: T-090
title: Decide what a cancelled task's declared outputs assert
type: decision
status: proposed
phase: specify
parent: T-089
blocked_by: []
related: [T-002, T-032]
work_package: v0.2
owner: maintainer
business_value: low
effort: s
created: 2026-08-09
updated: 2026-08-11
deliverables: []
---

# T-090 — Decide what a cancelled task's declared outputs assert

## 1. Specify

**Outcome**
`check` treats a task that was abandoned differently from one that was completed, or the project is
told plainly that abandoning a task means clearing its declared outputs. Either way the rule stops
resting on the accident that nobody's cancelled task has a missing path yet.

**Why this one**
Raised from [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), which
settled that `deliverables` is checked once a task is **closed**, because METHOD §1 rule 5 is the one
place the method requires an outcome to exist. `cancelled` is closed and rule 5 does not apply to it:
a task that was abandoned did not close by producing its outcome. So the fixed rule reports a
cancelled task's declared paths for the same bad reason the original defect reported an open task's.

**It is not hypothetical, and it is not yet firing.** Of the four projects onboarded on 2026-08-09,
two carry a cancelled task and one of those declares two outputs. Nothing is reported today only
because both of those paths happen to exist — one deletion away from the noise T-089 removed.

**Why `low` even so.** Nobody is being cried wolf at right now, and the cheap fix has a real price:
the only clean mechanism is a config key naming the abandoned status, on the `blocked_status`
precedent, and **every key in that file is required** — a config replaces the default rather than
merging with it. That is a line every adopting project writes to settle a case none of them has hit.

**Requirements served**
R-16 — a false positive is the other half of proving a validator. R-11, since the likely answer is a
schema key rather than code.

**Scope**
- In: whether `check` should skip a task closed by abandonment, and how it would know which status
  that is.
- In: the alternative that needs no mechanism — documenting that cancelling a task means clearing
  `deliverables`, on the grounds that the field asserts production and an abandoned task produces
  nothing.
- In: what a project with no such status pays. `blocked_status` takes `none`; whatever is added here
  must too.
- Out: [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md)'s rule
  itself, which is settled and is not reopened by this.
- Out: any other use for knowing which status means abandoned. If a second use appears, that changes
  the economics and should be said here rather than assumed.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `check_deliverables`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` — `blocked_status` as the precedent for naming one
  distinguished value, and the *Deliverables* section's note that every key is required.
- [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) §1, for the rule
  and the rejected alternative.

**Acceptance criteria**
- [ ] A cancelled task declaring a path that does not exist behaves the way this task decides, shown
      on a fixture rather than argued from the config
- [ ] A project that has no abandoned status is unaffected, and pays nothing it did not already pay
- [ ] Whatever is decided, one document says it and the others point — the binding already carries
      the sentence about which of rule 5's conditions is mechanical

**Open questions**
- **Mechanism or documentation.** A config key is exact and costs every project a line; a documented
  convention costs nothing and is not enforced. The maintainer's, because it is the same trade the
  `blocked_status` key already made once and the answer should be consistent with it.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-09 | → proposed | Raised from T-089 rather than solved inside it. T-089 keyed the deliverables check on the task being closed, which is METHOD §1 rule 5 stated mechanically; `cancelled` is closed and rule 5 does not cover it, so the same false positive survives under a different status. Carried rather than fixed because the clean mechanism is a required config key every adopter pays for, and the case fires in none of the four projects onboarded today — two of which do have a cancelled task, one declaring two outputs that happen to exist. `low` for that reason, and `s` because the whole of it is one branch and one key. |
