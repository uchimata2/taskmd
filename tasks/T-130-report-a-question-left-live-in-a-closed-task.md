---
id: T-130
title: Report a question left live in a closed task
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-025, T-095, T-107, T-121]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-11
updated: 2026-08-16
adopter_visible: yes
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

  **Answered 2026-08-16: neither. No checker, and no convention.** The measurement is in §3 and it
  settles both halves at once. A convention *would* make recognition exact — but the convention
  required is *the answer is written inside the bullet it answers*, and **16 of the 21 bullets it
  would have to move are answered in §3 as numbered decisions**, which is where a decision belongs.
  Requiring them beside the question makes the record state one fact in two places, which is the one
  thing this project's design rule forbids. A convention that buys a checker by breaking the rule the
  tool exists to serve is not a cheaper answer than no checker.

## 2. Plan

The task is research first. Nothing is written until the rules have been run and their alarms read,
because the outcome §1 admits — *nothing reliable* — is only honest if it was reached by trying.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Rebuild the hand sweep as a program and validate it against the numbers the hand sweep recorded: 128 files, 119 closed, 9 open | the partition reproduced, so the parser is trusted before anything is concluded from it |
| 2 | Run four candidate rules, each narrower than the last, over the current tree, and **read every alarm** | a false-positive count per rule |
| 3 | Run the same four over the tree **as it stood on 2026-08-11**, the only corpus with a known live question, so recall is measured and not assumed | which rules catch the one true positive |
| 4 | Decide from the two tables together, and answer §1's open question with the rejection recorded | the decision, in §3 |
| 5 | If no class: name what catches these instead, in the one document where someone is in a position to act — and check that `check`'s own scope statement does not already imply coverage | the statement, and the check on the statement |
| 6 | Run the suite, `check` and `index`; `check` is untouched, so every fixture must still report exactly what it did | green output quoted in §3 |

## 3. Implement

**The parser was validated before anything was concluded from it.** Run against the tree as it stood
at the commit before this task was raised, it reproduces the hand sweep's own partition — which is
what makes the numbers below evidence rather than a second opinion:

```
task files: 128   closed: 119   open: 9   (sum 128)
```

**The four rules.** Each is the one above it, narrowed. All four read bullets under an
`Open questions` heading in a **closed** task, skipping any whose first word is *none*:

| Rule | Adds |
| :--- | :--- |
| **A** | the 2026-08-11 hand sweep: the bullet is not struck through |
| **B** | A, and the **bullet** carries no answer marker — a strikethrough, or an emphasised *answered / settled / decided / ruled / withdrawn / measured / verified / chosen* |
| **C** | B, and **nothing later in the record** carries one either — a sibling bullet, a following paragraph, a §3 decision, a log row |
| **D** | C, and the bullet **names someone else** as the one who answers |

**Two runs, and the second is the one that decides it.** The current tree has no live question at
all, so it can only measure noise; the 2026-08-11 tree is the only corpus where a true positive is
known, so it is the only one that can measure whether a rule finds anything.

| | today: 162 tasks, 148 closed, 178 question bullets | 2026-08-11: 128 tasks, 119 closed, 146 bullets |
| :--- | :--- | :--- |
| **A** | 46 flags, 0 live | 38 flags, **catches it** — 1 in 38 |
| **B** | 21 flags, 0 live | 23 flags, **catches it** — 1 in 23 |
| **C** | 5 flags, 0 live | 6 flags, **misses it** |
| **D** | 0 flags | 0 flags, **misses it** |

Every one of today's flags was read. All are answered — 25 in the bullet, 16 elsewhere in the record,
5 by a numbered decision or by a task raised to carry them ([T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md)'s
cancelled case is [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md)). The
three counts partition the 46, which is what makes *zero live* a measurement rather than an
impression.

**Why C misses the one case, and why that is not a fixable pattern.** T-109 carried two questions.
The first was answered in place — *Settled at `specify` on 2026-08-11* — so the record contains an
answer marker, and C, which asks whether the record answers **anything**, falls silent about the
second. Tightening C to ask whether the record answers **this question** is the thing no pattern can
do: a question and its answer are both free prose in the same section, and the association between
them is the fact being looked for. That is a property of the record, not of the regular expression.

**Decisions & assumptions**
- **No `check` class** — 2026-08-16. Not on an estimate of precision: on the table above. A rule
  precise enough to run (C, D) misses the case the task exists for, and a rule that finds it (A, B)
  reports it at 1 in 23 — the rate
  [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) already priced and rejected.
  This is the outcome §1 admitted as possible, reached by building the thing and reading its alarms
  rather than by predicting them.
- **No convention either** — 2026-08-16, and it is the same measurement. The convention that would
  make B exact is *the answer goes inside the bullet it answers*; 16 of the 21 bullets it would move
  are answered as numbered decisions in §3, whose home is the decision list. Requiring a copy beside
  the question writes one fact twice.
- **The statement goes in [`review`](../plugin/skills/taskmd/docs/method/review.md), as a numbered
  step and a section beside it** — 2026-08-16. Review is the phase that judges a task before it
  closes, so it is the last moment anyone is in a position to act, and it is tier 3 — loaded when
  that phase begins, paid by nobody else. *Rejected: `METHOD.md`*, which is the spine and is paid by
  every task; the rule is a step in one phase, not a rule about the method. *Rejected: this
  repository's `CLAUDE.md`*, which would keep the finding here and let every adopter meet it fresh.
- **`check`'s scope statement was checked rather than assumed** — 2026-08-16. `README.md` says
  `check` *"validates ids, vocabularies, references, links, and your task templates"*, and every run
  closes with `structure and references only - it cannot tell you whether a spec or an outcome is
  good`. Both are enumerations that exclude this, so criterion 3's second half needed no edit — and
  the new section says outright that whatever a tracker validates, it is not this.
- **The sweep is not shipped** — 2026-08-16. It is the detector this task rejected; shipping it would
  hand an adopter the 1-in-23 rule under the name of a check. The four rules are stated above
  precisely enough to rebuild, which is what a future reader needs — not a program that runs.

**Outputs produced**
- `plugin/skills/taskmd/docs/method/review.md` — step 5, and *A question aimed at someone else*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision rests on a measured false-positive rate over this repository's own tasks, not on an estimate | met | Four rules, two corpora, every alarm read. The criterion said 128 tasks; the tree is now 162, and **both were run** — the older one because it is the only corpus holding a known live question, which a false-positive rate alone cannot see |
| If a class is added, it is shown failing on a task that carries a live question and staying quiet on the others | n/a | No class added |
| If no class is added, one document says what catches a question aimed at someone else, and `check`'s own scope statement does not imply it is covered | met | [`review`](../plugin/skills/taskmd/docs/method/review.md) step 5 and the section beside it. The scope statement was read, not assumed: two enumerations, neither implying coverage, quoted in §3 |
| Every existing fixture still reports exactly one class | met | `check` was not touched, so this is the strongest form of the criterion — the fixtures report what they reported before. `267 passed, 3 skipped` |

**Child fix tasks raised**
- none. The measurement turned up no live question anywhere in the tree, which is the thing this task
  was built to look for and did not find.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | Full lifecycle in one session under the authorisation below, and it ended in the recommendation the maintainer was told it might. **No `check` class and no convention**, both rejected on measurement rather than on judgement: four rules over two corpora, and the second corpus is what made the decision — today's tree carries no live question at all, so it can measure noise and nothing else. On the 2026-08-11 tree, where one is known, every rule precise enough to run missed it and every rule that found it reported it at 1 in 23. The reason is structural and is now written down: a question and its answer are both prose, so no pattern can say which answer belongs to which question. What catches these is the closing discipline, and it is a numbered step in [`review`](../plugin/skills/taskmd/docs/method/review.md) with the measurement behind it beside it. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. **This task's own open question — convention or checker — is left to `specify` under the standing delegation**, deciding it with the rejected alternative recorded, because both outcomes are already inside the agreed criteria: criterion 2 covers a class being added and criterion 3 covers none being added. The maintainer chose this task into the batch having been told it may end in a recommendation rather than a guard. |
| 2026-08-11 | → proposed | Raised from a hand sweep the maintainer asked for during a handoff. The sweep is the evidence and its numbers are in §1: 128 files read, 24 flagged, 1 genuinely live. **The one find had been invisible for five days** and would have stayed so, which is the argument for the task; **23 of 24 were false** , which is the argument against the obvious fix. Filed `M6` because deciding what a machine can recognise here is research rather than a correction, and `m` for the same reason. |
