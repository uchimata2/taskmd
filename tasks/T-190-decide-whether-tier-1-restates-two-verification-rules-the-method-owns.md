---
id: T-190
title: Decide whether tier 1 restates two verification rules the method owns
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-151, T-047, T-028]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: []
---

# T-190 — Decide whether tier 1 restates two verification rules the method owns

## 1. Specify

**Outcome**
A ruling on whether `CLAUDE.md`'s *Verifying* section may state two rules that
[`plugin/skills/taskmd/docs/method/implement.md`](../plugin/skills/taskmd/docs/method/implement.md)
also states — and, if not, which text goes and what replaces it.

**Why this one**
Found by [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) having to choose
between the two files as a home, which meant reading both. They carry the same two rules:

| Rule | `CLAUDE.md` *Verifying*, tier 1 | `implement.md` *Verification*, tier 3 |
| :--- | :--- | :--- |
| a check is proven by failing | *a validator is only proven when it has been shown to fail on a case it is supposed to catch* | *A check that has only ever succeeded has not been tested* |
| report the result, not a verdict | *State results as the actual command output, not as "works"* | *State the result, not the verdict* |

**`CLAUDE.md` states its own rule about this, and states that it has exactly two exceptions.** It
says the method has one home, that a copy found elsewhere is the defect, and then: *`CLAUDE.md`
carries exactly two of its rules — METHOD §3.1 and §3.3, verbatim, since
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — and that is not an
exception to the rule but the only way to obey it: those two bind before the method is loaded, so
tier 2 cannot be their home.*

**Neither of these two binds before the method is loaded**, which is the whole test that admitted the
other pair. Verification happens inside `implement`, and a session doing task work has loaded the
method by then.

**The counter-argument is real and is why this is a `decision`.** A session may make a claim about
behaviour without doing task work at all — answering a question, triaging a report, checking
something for the owner — and in that case the method never loads and the rule never arrives. If that
is the reading, the tier-1 text is not a copy of the method's rule but a differently scoped rule that
happens to overlap it, and the repair is to say so rather than to delete it.

**Requirements served**
`CLAUDE.md`'s own *What earns a place here*, and the tier bound `tests/test_budget.py` measures.

**Scope**
- In: the ruling, and whichever edit follows from it
- In: whether the overlap is duplication or two differently scoped rules, decided against
  `CLAUDE.md`'s own stated test rather than by preference
- In: what the tier-1 characters change by, measured
- Out: the negative-case rule itself, which is
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s and is closed. This task
  does not move it
- Out: a sweep of tier 1 for other restatements. If the answer is that this is duplication, that
  sweep is its own task raised from this one

**Inputs**
- `CLAUDE.md` — *Verifying*, and the paragraph naming its two admitted exceptions
- [`plugin/skills/taskmd/docs/method/implement.md`](../plugin/skills/taskmd/docs/method/implement.md)
  — *Verification*
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — why two rules were
  admitted, and the test used to admit them
- `tests/test_budget.py` — what tier 1 costs today

**Acceptance criteria**
- [ ] The ruling is stated as *duplication, remove it*, *two scoped rules, say so*, or *leave it*,
      with the rejected options named
- [ ] It is argued against `CLAUDE.md`'s own admitted-exception test, quoting it, rather than against
      a general preference for short files
- [ ] If text moves, tier 1's character count before and after is stated, from
      `tests/test_budget.py` rather than by counting by hand
- [ ] **If text is removed, something is checked to show the rule still reaches a session that never
      loads the method** — the counter-argument above is the whole risk, and a ruling that does not
      test it has assumed it away
- [ ] Whether other tier-1 lines restate the method is answered or raised as its own task

**Open questions**
- ~~**Does a session that never loads the method still need these two rules?**~~ **Answered
  2026-08-19: yes, and the tier-1 text stays, reworded to state its wider scope out loud.** The
  ruling is that the two are not copies of the method's rules but a wider-scoped rule that overlaps
  them: they bind on any claim about behaviour, not only on task work, and a session answering a
  question, triaging a report or checking something for the owner never loads the method. Two
  alternatives were offered and not taken — **deleting the tier-1 text** as a duplicate, which
  removes both rules from exactly the sessions where an unverified claim is most likely; and
  **measuring first**, a probe over the session transcripts of the kind
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) built and
  [T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) made re-runnable. So the repair
  is to say the scope, not to delete the text, and `tests/test_budget.py` still bounds what saying
  it may cost.

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
| 2026-08-19 | (no change) | **Answered by the owner in a question round.** The tier-1 text stays and is reworded to state the wider scope; deleting it, and measuring the transcripts before ruling, were both offered and declined. The question in §1 is struck through with both alternatives named. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) raised it. **It does not answer §1's question**, which asks what sessions actually do and is settled by evidence or by the owner, not by permission to run phases. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s review, from having to read both candidate homes to choose between them. Not fixed there: T-151's scope is where the negative-case rule goes, and removing text from tier 1 is a change the owner should see argued on its own. Typed `decision` because the counter-argument is real — a session that never loads the method never meets these rules — and the answer may be that both texts stay with their scopes made explicit. |
