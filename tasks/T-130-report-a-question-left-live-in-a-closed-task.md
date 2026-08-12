---
id: T-130
title: Report a question left live in a closed task
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-025, T-095, T-107, T-121]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-130 — Report a question left live in a closed task

## 1. Specify

**Outcome**
A task that closes while its record still carries an unanswered question is reported, or the project
records that it will not be and says what catches those questions instead.

**Why this one**
Found by a hand sweep on 2026-08-11, run because the maintainer asked for one during a handoff. The
sweep read all 128 task files and partitioned them: 119 closed, 9 open. It looked for a bullet under
**Open questions** in a closed task that is neither `none` nor struck through as answered.

It found 24 such bullets. Most are answered in place, in prose the pattern cannot recognise. **One
was genuinely live**, and it is the shape that matters:
[T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md) closed
carrying *"Is there a second kind of work here, and does it need a name?"*, raised by the maintainer,
with *"No recommendation yet — the research it needs has deliberately not been done."* It is now
[T-131](T-131-decide-whether-a-question-heavy-task-is-a-different-kind-of-work.md), five days later,
and only because someone asked for a sweep.

**A question aimed at someone else dies at close.** Every sweep this project runs reads *open* work.
A closed task is out of every view by design, so its residue is invisible in exactly the way the
project's other silent-loss classes were before `check` learned to report them:
[T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) for a parked file,
[T-025](T-025-let-check-notice-a-stale-generated-index.md) for a stale index.

**Why it is not simply a new `check` class.** The hand sweep's precision was 1 in 24. A validator
with that rate is one a project passes flags to, which is the failure
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) already priced and rejected
once. So the work is mostly in deciding what a machine can recognise, and the honest answer may be
*nothing reliable*, in which case saying so is the outcome.

**Requirements served**
R-16, and the rule behind it: a validator is worth what you believe it would catch.

**Scope**
- In: whether a live question in a closed task is mechanically recognisable at an acceptable rate.
- In: if it is, a `check` class for it; if it is not, a written statement of what catches these
  instead, and where.
- In: the convention that makes recognition possible at all, since the 1-in-24 rate is a property of
  free prose rather than of the idea.
- Out: the questions themselves. The one live find is [T-131](T-131-decide-whether-a-question-heavy-task-is-a-different-kind-of-work.md).
- Out: changing what a task record looks like beyond whatever minimum this needs.

**Inputs**
- The sweep's own output, in this task's §3 once it is run again.
- [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) and
  [T-025](T-025-let-check-notice-a-stale-generated-index.md), as the two precedents for reporting a
  silent loss.
- [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md), for the rejected-on-precision
  precedent, which is the likelier outcome here.

**Acceptance criteria**
- [ ] The decision rests on a measured false-positive rate over this repository's own 128 tasks, not
      on an estimate
- [ ] If a class is added, it is shown failing on a task that carries a live question and staying
      quiet on the 23 that do not
- [ ] If no class is added, one document says what catches a question aimed at someone else, and
      `check`'s own scope statement does not imply it is covered
- [ ] Every existing fixture still reports exactly one class

**Open questions**
- **Is the answer a convention rather than a checker?** A struck-through bullet already marks an
  answered question in the tasks written since 2026-08-11, and the sweep recognised it. If the
  convention were required rather than incidental, recognition becomes exact and the checker becomes
  trivial. Against it: it is a rule about prose that a project adopting taskmd would have to keep,
  and this project has rejected that shape before. Decide at `specify`, since it changes what the
  outcome is.

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
| 2026-08-11 | → proposed | Raised from a hand sweep the maintainer asked for during a handoff. The sweep is the evidence and its numbers are in §1: 128 files read, 24 flagged, 1 genuinely live. **The one find had been invisible for five days** and would have stayed so, which is the argument for the task; **23 of 24 were false** , which is the argument against the obvious fix. Filed `M6` because deciding what a machine can recognise here is research rather than a correction, and `m` for the same reason. |
