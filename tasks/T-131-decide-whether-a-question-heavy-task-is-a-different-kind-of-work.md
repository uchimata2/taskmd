---
id: T-131
title: Decide whether a question-heavy task is a different kind of work
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-088, T-109, T-130]
work_package: M6
owner: maintainer
business_value: low
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-131 — Decide whether a question-heavy task is a different kind of work

## 1. Specify

**Outcome**
The shipped `type` vocabulary either gains a value for a task whose questions outnumber its answers,
or the project records that no such kind exists and says what the existing values do with those
tasks.

**Why this one**
The maintainer raised it inside
[T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md) and it closed
without an answer:

> Is there a second kind of work here, and does it need a name? A task whose questions outnumber its
> answers, or whose questions could significantly move its scope, may be a different kind rather than
> a badly-typed one. No recommendation yet — the research it needs has deliberately not been done.

T-109 settled the neighbouring question: `decision` means *the outcome is an answer*, and it beats
`fix` when a task is both. That test reads the stated outcome. It says nothing about a task whose
outcome is not yet knowable because the questions might move it, and that is what this asks.

**It was found by a sweep, not by anyone needing it.** It sat in a closed record for five days.
[T-130](T-130-report-a-question-left-live-in-a-closed-task.md) is the mechanism question that comes
from the same find; this is the content.

**The steer already given, and it constrains the answer.** The maintainer rejected *"a task with open
questions is a decision"* on 2026-08-10, because every task has open questions at `specify`. So any
new value has to separate a genuinely different kind of work from the ordinary uncertainty of an
early phase, and a value that cannot do that is one nobody can apply.

**Requirements served**
R-11, since the vocabulary is configuration; and the rule
[T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) established,
that a vocabulary value which finds nothing is a defect.

**Scope**
- In: whether the distinction exists, and whether it survives outside software — a training course
  and an ops runbook are the cases the vocabulary has to read for.
- In: if it exists, its name, its test a reader can apply, and what it costs every configured
  project, since adding a value to a shipped vocabulary reaches every adopter.
- Out: re-opening T-109's answer, which is settled.
- Out: retyping any existing task. If a value is added, applying it is separate work.

**Inputs**
- [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md) §1, for the
  question as raised and for the rejected first attempt.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md), for the rule
  that a value must find something.
- The 128 task records here, as the corpus that would show whether the kind exists.

**Acceptance criteria**
- [ ] The answer names a test a reader can apply to a task's record, or states that no test
      separates the proposed kind from ordinary `specify` uncertainty
- [ ] If a value is added, this repository's own tasks are searched for it and the count is stated —
      a value that finds nothing is the defect T-088 removed
- [ ] The answer says what it costs a configured project, since a shipped vocabulary reaches every
      adopter
- [ ] The non-software cases are addressed rather than assumed away

**Open questions**
- ~~**Does the corpus have to be measured before the answer, or does the answer come first?** T-088
  measured after deciding and nearly shipped a value that found nothing. Measuring first costs a pass
  over 128 records; deciding first risks repeating that. Maintainer's, at `specify`.~~ **Answered by
  the owner on 2026-08-19: measure first** — see the Log row of that date.

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
| 2026-08-19 | (no change) | **The open question is answered by the owner: measure the corpus first, then decide.** Asked in the backlog-wide round of 2026-08-19. The precedent is the argument — [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) decided ahead of its evidence and came close to shipping a value that matched nothing, and a category invented before the pass is one the pass then confirms rather than tests. *Rejected: deciding first and measuring after*, which reaches a ruling sooner at the price of repeating exactly that. The cost of the chosen order is one pass over the records, and `plan` puts it first so that an empty result ends the task instead of arriving too late to. This row is the answer, not authorisation to start. |
| 2026-08-11 | → proposed | Carried out of T-109, which closed with this question live and unanswered on 2026-08-11 after the maintainer raised it. Recovered by the sweep that also produced [T-130](T-130-report-a-question-left-live-in-a-closed-task.md). Filed `M6`: it is a vocabulary decision that reaches every adopter, and nothing waits on it. `low` because nothing is wrong today — the existing values type every task in this repository — and the cost of the gap is that a distinction the maintainer thought worth naming stays unnamed. |
