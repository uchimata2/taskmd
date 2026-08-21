---
id: T-190
title: Decide whether tier 1 restates two verification rules the method owns
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-151, T-047, T-028]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-21
adopter_visible: no
deliverables: [CLAUDE.md]
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
| 1 | Measure tier 1 as it stands, from `tests/test_budget.py` rather than by hand. | The characters, the bound and the margin, recorded in §3 as the test printed them. |
| 2 | Widen the scope **in the rule's own sentence** rather than in a paragraph beside it, so the text a session is handed says who it binds and costs a clause to say so. | The edited *Verifying* section of `CLAUDE.md`. |
| 3 | Put the *argument* — why this overlaps `implement.md` and why that is not the duplication `CLAUDE.md` forbids — in a block-level HTML comment. | The comment, and a §3 note that it is addressed to whoever next reads the overlap and wonders. |
| 4 | Re-measure, and state the delta. | Before and after, from the same test. |
| 5 | Judge criterion 4 honestly rather than tick it: the ruling keeps the text, so no text is removed and the risk that criterion guards does not arise. Say what would have been checked if it did, and say what this session could not have run. | A §3 note, and a `not applicable` row in §4 with its reason. |
| 6 | Answer criterion 5 by reading tier 1 against the method, section by section, rather than deferring it. | A verdict per tier-1 section: pointer, admitted exception, or restatement — and a task if any is the third. |

**Sequencing.** Step 1 before step 2, because a margin measured after an edit cannot say what the
edit cost. Step 6 last: whether *other* lines restate the method is a different question from this
one, and doing it first would have let its answer colour the ruling the owner already made.

**Decisions**

- **The scope goes in the rule's own sentence; the argument goes in a block comment.** The ruling
  asks for the wider scope stated out loud, and a session's behaviour changes on *who the rule
  binds* — so that is visible text. It does not change on *why the overlap is legitimate*, which is
  addressed to a maintainer reading the two files side by side, and `tests/test_budget.py` proves a
  block-level comment is stripped before injection and so costs the file rather than the session.
  *Rejected:* a visible paragraph carrying both, which charges every turn of every session for a
  justification; and *rejected:* a comment carrying both, which hides from the session the one half
  written for it.

**Outputs**

- `CLAUDE.md`
- `tasks/T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md` (§3)

## 3. Implement

**The ruling, restated as it was made.** *Two scoped rules — say so.* Not duplication to remove, not
text to leave alone. The owner made it on 2026-08-19; §1 carries it struck through with both rejected
alternatives, and this phase carries it out rather than re-opening it.

### Steps 1 and 4 — what tier 1 cost, before and after

```text
tier 1 6380 chars under by 1474 (bound 7854, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       843 chars of block comment are not counted
```

```text
tier 1 6451 chars under by 1403 (bound 7854, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       1839 chars of block comment are not counted
```

**+71 characters on every turn of every session; the margin falls from 1474 to 1403.** Both figures
are `tests/test_budget.py`'s, printed by the test rather than counted by hand — which is the
criterion, and also the only way to get it right, since the bound is a file that moves.

**The argument cost 996 characters and none of them are paid by a session.** Block comment characters
went 843 → 1839 while the counted figure rose by 71, so the same edit that widened the rule for every
session put its justification where only a maintainer meets it. That split is the decision below,
and the test is what makes it a fact rather than a claim.

### Steps 2 and 3 — the edit

The scope moved **into the rule's own sentence**, which is the shortest place it can be and still be
read by the session it binds:

```text
- Claims about behaviour are verified by **running the thing on a real case**, [...]
+ **Any claim about behaviour** — in task work, in answering a question, in triaging a report — is
+ verified by **running the thing on a real case**, [...]
```

The argument — why this overlaps `implement.md`, why that is not the copy `CLAUDE.md` forbids, and
which two alternatives were declined — went into a block-level HTML comment below the section, citing
T-190 and `tests/test_budget.py` for the stripping rather than asserting it.

### Step 5 — criterion 4, judged rather than ticked

The criterion reads *if text is removed, something is checked to show the rule still reaches a session
that never loads the method*. **No text was removed**: the ruling keeps both rules in tier 1 and adds
a clause, so the risk it guards — the rules leaving the only file such a session is handed — does not
arise. It is recorded as *not applicable* in §4, with the condition quoted, rather than ticked.

**What would have been checked, had text been removed, and what this session could not have run.**
The check is whether a session that does no task work still meets the rules, and it cannot be run by
the session doing the editing: `CLAUDE.md` is fixed before the first tool call, so this session is
still being governed by the version it started with. The instrument is a **separate session** —
started after the edit, given a question that invites a claim about behaviour, and observed for
whether it runs something before answering. That is stated here so a future ruling that *does* remove
text knows what it owes, and knows that the answer cannot come from inside the run that makes the
change.

### Step 6 — criterion 5, answered rather than deferred

Tier 1 is two files, and both were read against `plugin/skills/taskmd/docs/METHOD.md` and the seven
files in `plugin/skills/taskmd/docs/method/`. All six sections of `CLAUDE.md` and the served
description:

| Tier-1 section | Verdict |
| :--- | :--- |
| *What this is* | Not method. Describes the repository and points at `docs/SCOPE.md` and `docs/BRIEF.md` |
| *The one design rule* | **Pointer plus application.** It shares a heading with METHOD §4 and says so in its second clause — *stated in full [...] in METHOD.md §4* — and its body is what the rule comes out as *in this repository*, which METHOD deliberately cannot contain because it names no file and no field |
| *Working method* | Not method. States that the method is not restated here, names the three tiers, and carries the budget |
| *One phase per request*, *Surface what you discover* | The two admitted exceptions, verbatim by design since [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) |
| *Publishing constraints* | Not method. Project-specific, and points at `docs/SCOPE.md` §5 |
| *Verifying* | This task's subject, now a wider-scoped rule that says its scope |
| `plugin/skills/taskmd/SKILL.md` description | **A name, not a rule.** It lists *specify, plan, implement, review, audit* as trigger words; a description that did not name the phases would not match a request to run one. It states no exit criterion and no ordering |

**So the answer is no, and no task is raised.** The two overlaps that exist — a shared heading and a
list of phase names — are both a name used to point at the method rather than a rule copied out of
it, which is the distinction the *Verifying* ruling turns on and is now the worked example of.

**Decisions & assumptions**

- **The scope went in the rule's own sentence and the argument in a block comment — rationale: a
  session's behaviour changes on *who a rule binds* and not on *why the overlap is legitimate*, and
  `tests/test_budget.py` proves a block-level comment is stripped before injection.** Measured on
  this edit: 71 counted characters against 996 uncounted. Rejected: one visible paragraph carrying
  both, which charges every session for a justification; and a comment carrying both, which hides
  from the session the half written for it — 2026-08-21.
- **Criterion 4 is recorded not applicable rather than met — rationale: a conditional criterion whose
  condition did not occur is not evidence, and ticking it would make a vacuous pass look like a
  tested one.** What the check would have been, and why this session is the wrong instrument for it,
  is written above so a later removal does not re-derive it — 2026-08-21.

**Outputs produced**

- `CLAUDE.md`
- this record

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The ruling is stated as *duplication, remove it*, *two scoped rules, say so*, or *leave it*, with the rejected options named | met | **Two scoped rules, say so.** §1 carries it struck through and §3 opens by restating it; the two rejected options are named in both — deleting the tier-1 text as a duplicate, and measuring the session transcripts before ruling |
| It is argued against `CLAUDE.md`'s own admitted-exception test, quoting it, rather than against a general preference for short files | met | The test is *those two bind before the method is loaded, so tier 2 cannot be their home*, quoted in §1. §3's block comment applies it rather than a size argument: these bind on any claim about behaviour, `implement.md` binds inside a phase that has loaded the method, and a session answering a question never loads it |
| If text moves, tier 1's character count before and after is stated, from `tests/test_budget.py` rather than by counting by hand | met | 6380 → 6451, **+71**; margin 1474 → 1403 against a bound of 7854. Both lines are the test's own output, quoted in §3. The uncounted half moved 843 → 1839, which is the decision's evidence and not an aside |
| **If text is removed, something is checked to show the rule still reaches a session that never loads the method** | **not applicable** | Its condition did not occur: the ruling keeps both rules in tier 1 and adds a clause, so nothing left the only file such a session is handed. Recorded rather than ticked, because a conditional criterion whose condition never fired is not evidence. §3 step 5 writes down what the check would be and why the editing session cannot be the one to run it — `CLAUDE.md` is fixed before its first tool call |
| Whether other tier-1 lines restate the method is answered or raised as its own task | met | **Answered: no**, from reading both tier-1 members against `METHOD.md` and the seven `method/` files, with a verdict per section in §3 step 6. Two overlaps exist and neither is a restatement — *The one design rule* shares a heading and points at METHOD §4 in its next clause, and the skill description lists the phase names as trigger words. No task raised |

**The scope out-clause did not fire.** §1 says a sweep of tier 1 for other restatements is out of
scope *if the answer is that this is duplication* — it is not, so the condition never arose and the
sweep was done here rather than deferred. Recorded because a reader meeting the out-list and the
criterion together would otherwise have to work out which won.

**Open questions, re-read before closing.** §1's one question was answered by the owner on 2026-08-19
and is struck through. §3 raises none aimed at anyone else; the one thing it hands forward — what a
future text-removing ruling owes, and which session can run it — is written into the record rather
than left as a question, because nobody is being asked for it now.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Four criteria met, one recorded not applicable, no child task.** The ruling was carried out, not re-opened: the scope went into the rule's own sentence at a cost of **+71 tier-1 characters** (6380 → 6451, margin 1403), and the argument went into a block comment costing 996 characters the harness strips. Criterion 4's condition never occurred, so it is recorded rather than ticked, with what a future removal owes written down. Criterion 5 answered no, from reading both tier-1 members against the method. |
| 2026-08-21 | → review | Implemented under the 2026-08-19 grant. |
| 2026-08-21 | → planned | **Six steps, under the 2026-08-19 grant.** One decision: the wider scope goes in the rule's own sentence, because a session's behaviour changes on who a rule binds; the argument for the overlap goes in a block comment, which `tests/test_budget.py` proves is stripped before injection and so costs the file rather than the session. |
| 2026-08-21 | → specified | **`specify` closed with nothing added.** The criteria were written when the task was raised and the ruling was made by the owner on 2026-08-19, struck through in §1 with both rejected alternatives named. |
| 2026-08-19 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-19, and not yet acted on.** The owner granted a later session the four tasks that need nobody else - T-193, T-190, T-191 and T-192 - **each through its full lifecycle, committed and pushed**. It is written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)), and an authorisation kept only there is one the session after next cannot find. **It reaches these four and no others**: the remaining open tasks each wait on a person, an external event, or a question still the owner's. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round.** The tier-1 text stays and is reworded to state the wider scope; deleting it, and measuring the transcripts before ruling, were both offered and declined. The question in §1 is struck through with both alternatives named. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) raised it. **It does not answer §1's question**, which asks what sessions actually do and is settled by evidence or by the owner, not by permission to run phases. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s review, from having to read both candidate homes to choose between them. Not fixed there: T-151's scope is where the negative-case rule goes, and removing text from tier 1 is a change the owner should see argued on its own. Typed `decision` because the counter-argument is real — a session that never loads the method never meets these rules — and the answer may be that both texts stay with their scopes made explicit. |
