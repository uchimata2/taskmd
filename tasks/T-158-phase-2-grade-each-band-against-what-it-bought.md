---
id: T-158
title: Phase 2 of the context-economy audit — grade each band against what it bought
type: analysis
status: cancelled
phase: specify
parent: T-152
blocked_by: []
related: [T-143, T-155]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-158 — Phase 2 of the context-economy audit: grade each band against what it bought

## 1. Specify

**Outcome**
Every band in [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s two reports
carries a grade — what the change actually bought, measured after it landed, set against what phase 1
estimated — including the bands whose task decided to change nothing.

**Why this one**
Phase 2 of the audit method. It cannot be produced from phase 1: a band is an estimate, and the only
thing that grades an estimate is the outcome. The prior fully graded run is the evidence that this is
worth doing — **eleven of thirteen bands missed, and every error was in the remedy rather than in the
measurement**, which is a fact about how this kind of audit fails and is invisible without phase 2.

**Blocked on the repairs, deliberately.** A phase that runs once, later, on a trigger nobody watches is
a phase that does not run — so it is a task with dependencies rather than a note in the umbrella. It
unblocks when the five tasks it names close, whatever each of them decided.

**Scope**
- In: every finding banded in the two deliverables of
  [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md).
- In: re-measuring at grading time. Subjects grow between ranking and implementation — the audit
  records three of thirteen figures moving before their task began in the prior run.
- In: attributing each miss to the measurement or to the remedy, which is what the prior run's result
  makes worth recording.
- Out: new findings. Phase 2 grades; something newly noticed is a new task or a new audit, and folding
  it in here would make the grades unreadable.
- Out: the byproduct register. Those rows are never banded, so there is nothing to grade.
- Out: the bands whose controller is the user or the harness. Nothing landed for them to be graded
  against, and saying so is the grade.

**Inputs**
- [The project's report](../docs/audits/2026-08-15-context-economy-taskmd.md) and
  [the portable half](../docs/audits/2026-08-15-context-economy-portable.md) — the bands
- [`method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) — the procedure
- The five blocking tasks, each of which owes one line of measured outcome recorded on the day it was
  known

**Acceptance criteria**
- [ ] Every band has a grade, including the ones whose task changed nothing
- [ ] Each grade names what was measured and the date it was measured
- [ ] Every miss is attributed to `Finding` or to `Change`, and the split is reported as a count
- [ ] No figure is carried from phase 1 without being re-measured or marked as not re-measurable
- [ ] The grades do not overwrite what the reports say about 2026-08-15 — see the open question

**Open questions**
- **Where do the grades live?** The two reports are dated records, and a record's statement about the
  past is annotated rather than rewritten. So the grades are appended to them, written into this task,
  or written into a third document that the reports point at. The first keeps the band and its grade
  side by side; the last keeps each document about one date. **The maintainer answers, at `specify`.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- Not run — the task was cancelled at `specify`, so no decision was ever taken here.

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
| 2026-08-17 | → cancelled | **Dropped by the maintainer**, taking the route `audit.md` step 5 names explicitly: an umbrella's child may be *dropped with a recorded reason* as well as done, and this is the reason. Asked for as the way to unblock [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), whose closure it was the last long pole in. **What is being given up, so nobody re-derives it as an oversight:** phase 2 was to grade each phase-1 band against what the repair actually bought — the only mechanism that would have caught a band that was confidently wrong, and the reason the bands were recorded with gain, effort and risk rather than as a ranked list. Phase 1's findings keep their bands; nothing now checks them. **What would justify raising it again:** a phase-1 band turning out to have been badly wrong in a way somebody notices anyway, which is the cheap version of the same signal. **The audit deliverable is deliberately not edited.** Its step-11 table still proposes phase 2 and says it is blocked on the repairs — a true statement about what the examination proposed on 2026-08-15, which is what a dated examination record is for. A reconcile sweep that "corrected" it would destroy the audit's product, and the disposition of every step-11 proposal already lives in [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 with this row's outcome here. **The dependency edges were cleared to a soft link at the same time** — [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) and [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) are live, and a cancelled task holding a dependency on a live one makes the live one look like it gates something. |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) as the method's phase 2, and blocked on the five tasks that carry its bands — including [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), which pre-existed the audit and carries E-12. `analysis` rather than `audit`: it produces grades over an examination that already happened, not findings over a body of work, so it raises no children of its own. |
