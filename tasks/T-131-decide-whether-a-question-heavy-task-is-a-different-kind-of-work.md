---
id: T-131
title: Decide whether a question-heavy task is a different kind of work
type: decision
status: done
phase: review
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

**Measure first, then decide** — the owner's answer of 2026-08-19, and step 1 is placed first so
that an empty result ends the task rather than arriving too late to.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Count, for every record, the questions it asked, what it settled itself and what it produced — then check the counter against records whose contents are known, before reading any total | the measurement, in §3 |
| 2 | Ask whether the shape has a **closed** member. An open task that has asked and not yet answered is a task nobody has worked, not a kind of work | §3 |
| 3 | Ask what the existing vocabulary already does with the candidates, and whether `decision`'s stated test separates them | §3 |
| 4 | Measure what adding a value to the shipped vocabulary costs a project that already has a config, by adding one and running `check` | §3, then reverted |
| 5 | Address the non-software cases, and say plainly which part of that answer is measured and which is argued | §3 |
| 6 | Record the ruling with the rejected option, and say what a reader applies instead | §3, §4 |

## 3. Implement

**Decisions & assumptions**
- **No value is added, and no such kind exists** — 2026-08-19. The distinction the maintainer named
  is real as a *feeling about a task at `specify`* and does not survive contact with the corpus.
- **The test that would separate it already exists and belongs to `decision`** — 2026-08-19. The
  shipped vocabulary's own words: *read the task's stated **outcome**; if that outcome is an answer
  someone else could act on, the type is `decision`.* A task that asks in order to rule still has a
  ruling as its outcome — **asking is a step, not a product** — so the proposed kind and `decision`
  read the same tasks. That is the answer criterion 1 allows: no test separates the proposed kind
  from ordinary `specify` uncertainty, because the outcome is what types a task and the outcome is
  unchanged by how many questions stand between here and it.
- *Rejected: adding a value* — for the three reasons the measurement produced, in order of weight:
  **it has no closed member**, **it cuts across three existing types rather than filling a gap in
  them**, and **it would make every configured project print a drift advisory** for a distinction
  none of them could apply. [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md)'s
  rule is that a value which finds nothing is a defect; this one finds seven tasks and none of them
  for a reason a reader could act on.
- **The counter was wrong twice and both errors were found by checking known records** —
  2026-08-19, and this is the part worth carrying. First, `~~` sat in the placeholder pattern, so
  every **answered** question counted as no question at all: `q` read 0 on records whose questions
  had been answered that same morning. Second, section 3 carries two heading shapes —
  `**Decisions & assumptions**` in 184 records and `### Decisions & assumptions` in 9, with six
  further spellings between them — so matching only the bold form reported *no decisions* for tasks
  that plainly had them. Both passes looked entirely reasonable as totals. Neither would have been
  caught by reading the output.

**The measurement**

Scope: **195 task records**, every file in `tasks/`. §1 of this task says *the 128 task records
here*, which was true when it was written on 2026-08-11 and is corrected here rather than there.

| | Result |
| :--- | :--- |
| **A. Records whose product is questions only** — a question naming the owner, nothing settled, nothing produced | **7, and every one of them is open.** Closed members: **0** |
| **B. Closed records where questions outnumber recorded decisions** | 3 of 183 — and all three produced outputs, so none of them is a task whose product was questions |
| **C. The `type` the seven candidates already carry** | `decision` 3, `research` 3, `deliverable` 1 |
| **D. Open questions per record** | 0 in 65, 1 in 101, 2 in 21, 3 in 4, 4 in 3, 5 in 1 |

**A is the finding.** The shape has no closed member in 195 records: every candidate is a task at
`specify` that has asked and not yet been answered, which is a task nobody has worked rather than a
kind of work. The emptiness of its *Decisions* and *Outputs* sections measures how far it has got,
not what it produces.

**C is the second finding.** The seven already carry three different types, so the proposed value
would not fill a gap in the vocabulary — it would cut across it, and a task would qualify for two
values at once with nothing to break the tie. `decision` was given a stated test precisely to stop
that (T-109).

**D says there is no cluster.** The distribution is a smooth tail with its mode at one question and
4% of records at three or more. *Question-heavy* is not a population in this corpus; it is the right
half of an ordinary spread.

**What a value would cost a configured project, measured rather than argued.** One value was added
to the shipped default, `check` was run on this repository — which has carried its own config since
[T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) — and the change was
reverted:

```text
CONFIG DRIFT  type: shipped default adds 'inquiry'; this project's row does not carry it
```

So the cost is not zero and it is not a one-off: **every project with its own config prints that
line until someone edits their vocabulary row**, for a value none of them has a test to apply. The
same mechanism is what [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md)
built, working as intended.

**The non-software cases, addressed and with the limit stated.** The vocabulary has to read for a
training course and an ops runbook, and the honest position is that **this corpus cannot measure
them**: 195 records from one software project, so what follows is argued and is marked as argued.
The argument is that the proposed kind gets *worse* outside software, not better. *What does this
audience already know?* and *which failure modes are in scope for this runbook?* are early tasks
dominated by questions, and both have an outcome a reader can name — a syllabus, a runbook. A
domain with more unknowns per task makes the proposed kind match **more** tasks and separate
**less**, which is the opposite of what a vocabulary value is for. If a non-software corpus ever
becomes readable, that is the thing to count, and this paragraph is what it would be tested against.

**Outputs produced**
- none — this task's product is the ruling above, and the shipped vocabulary is deliberately
  unchanged

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer names a test a reader can apply to a task's record, or states that no test separates the proposed kind from ordinary `specify` uncertainty | met | The second branch, and it names the test that *does* apply instead: `decision`'s own, reading the stated outcome. Asking is a step, not a product |
| If a value is added, this repository's own tasks are searched for it and the count is stated | met | No value is added, so the clause does not bind — and the count is stated anyway, because it is the evidence for not adding one: 7 candidates, 0 of them closed, across 195 records |
| The answer says what it costs a configured project | met | Measured by adding a value and running `check`, not estimated: one `CONFIG DRIFT` line per configured project until its vocabulary row is edited. Quoted in §3, and reverted |
| The non-software cases are addressed rather than assumed away | met | §3's last paragraph, with the limit stated in the same breath: the corpus is one software project's, so the answer there is argued and says so. The argument is that the distinction weakens outside software rather than strengthening |

Four criteria, four met, no child raised.

**What this task nearly did.** Its own §1 warns that
[T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) decided ahead
of its evidence and came close to shipping a value that matched nothing. Deciding first here would
have reached *yes* comfortably: seven candidate tasks exist, they feel alike, and three of them were
being worked the same week. It is the **closed** column that refuses it, and nothing but the pass
produces that column.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | All four criteria met, no child raised. **Authorisation (METHOD §3.1):** the owner's grant of 2026-08-19 covering T-194, T-189, T-148, T-131 and T-181, full lifecycle. **Ruled: no such kind, and no value is added.** The corpus refuses it — the shape has **no closed member in 195 records**, its seven candidates are all open tasks at `specify`, and they already carry three different types between them. The test that separates them already exists and is `decision`'s: read the stated outcome, because asking is a step and not a product. **The counter was wrong twice and both errors were caught by checking records whose contents were known** — `~~` in the placeholder pattern made every answered question invisible, and section 3's two heading shapes made decisions invisible in nine records. Both wrong passes read as reasonable totals. The cost of a value was measured rather than argued: one `CONFIG DRIFT` line in every configured project. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: measure the corpus first, then decide.** Asked in the backlog-wide round of 2026-08-19. The precedent is the argument — [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) decided ahead of its evidence and came close to shipping a value that matched nothing, and a category invented before the pass is one the pass then confirms rather than tests. *Rejected: deciding first and measuring after*, which reaches a ruling sooner at the price of repeating exactly that. The cost of the chosen order is one pass over the records, and `plan` puts it first so that an empty result ends the task instead of arriving too late to. This row is the answer, not authorisation to start. |
| 2026-08-11 | → proposed | Carried out of T-109, which closed with this question live and unanswered on 2026-08-11 after the maintainer raised it. Recovered by the sweep that also produced [T-130](T-130-report-a-question-left-live-in-a-closed-task.md). Filed `M6`: it is a vocabulary decision that reaches every adopter, and nothing waits on it. `low` because nothing is wrong today — the existing values type every task in this repository — and the cost of the gap is that a distinction the maintainer thought worth naming stays unnamed. |
