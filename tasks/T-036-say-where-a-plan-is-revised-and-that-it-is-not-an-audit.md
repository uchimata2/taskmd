---
id: T-036
title: Say where a plan is revised, and that reviewing one is not an audit
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-032, T-026]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-06
updated: 2026-08-06
deliverables: []
---

# T-036 — Say where a plan is revised, and that reviewing one is not an audit

## 1. Specify

**Outcome**
The method says what happens when someone examines a plan that has not been implemented yet: it is
plan revision, not an audit, no umbrella task is created, and the revision has one recorded home.
`docs/method/audit.md` also states that the audit procedure is designed in `plan`, per audit.

**Why this one**
Split from [T-032](T-032-repair-the-audit-template-and-validate-templates.md), whose subject is a
template and a validation gap. The maintainer's answer to T-032's Q1 arrived with an account of the
audit workflow, of which two parts are method changes and belong here — writing them into the
template would reproduce the exact defect T-032 exists to fix.

**The part that is agreed.** An audit's procedure is not fixed in advance: `specify` carries the
goals and requirements, and `plan` researches and produces the procedure for *that* audit. This is
consistent with [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 2, which already requires a
finding threshold stated per audit rather than a standing checklist, and it is what the retired
*Review dimensions* checklist in the template got wrong. It needs saying in `audit.md`.

**The part this task argues against, and why it is raised rather than implemented.**
The maintainer's position: a user may ask for a task's *plan* to be audited; that is a different
exercise, so no audit task is created, the ticket is analysed and updated, and major findings are
added to the ticket as decisions rather than applied automatically where the change is not obviously
authorised.

Everything in that position is right about the **behaviour**. The disagreement is only about calling
it an audit, and the objection is that the name is what forces the exception:

1. **A plan that has not been implemented has produced nothing.** An audit's product is traceability
   over work that exists; `audit.md`'s own justification is that a reader must be able to tell "we
   examined this and it was clean" from "we examined this and quietly patched eleven things". Before
   `implement`, there is nothing patched and nothing to trace.
2. **The no-inline-fix rule cannot bite, because the plan is not a deliverable.** METHOD rule 4 says
   a finding is never fixed where it is found. A plan is the thing still being decided — changing it
   *is* the work of the plan phase, not a fix applied to a finished artifact.
3. **So an exception has to be written into rule 4 for a case that never needed to be inside it.**
   `audit.md` already says the no-inline-fix rule is *"the one most often waived"*. A sanctioned
   waiver for the commonest case is how it stops being a rule.

**And the behaviour described is already the method, under its own names.** "Do not apply it if the
change is not obviously authorised" is METHOD §3.3's first branch: *it changes what the current task
should produce → raise it as a question now, before continuing.* "Add major findings as decisions"
is [`plan`](../plugin/skills/taskmd/docs/method/plan.md) step 5: *choose, and write down what was rejected and why.*

**The real gap** is narrower than either reading: the method never says a plan **may be revised after
it is written**, nor where the revision is recorded. `plan.md` describes writing a plan once;
`implement` records decisions; nothing covers a plan changed between the two. That silence is what
made an exception look necessary.

**Requirements served**
R-3, R-21 (`docs/SCOPE.md`), and METHOD rule 4, whose integrity is the thing at stake.

**Scope**
- In: `docs/method/audit.md` — the audit procedure is produced in `plan`, per audit; and that
  reviewing an unimplemented plan is not an audit.
- In: `docs/method/plan.md` — revising a written plan, and where the revision is recorded.
- In: whether METHOD's spine needs any of this, or none of it. Default is none: the spine is at
  147/150 and [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) is re-deciding
  what the budget covers.
- Out: the template. That is T-032's, and this content must not land there.
- Out: the `type: audit` vocabulary value, decided in T-032.
- Out: re-opening whether audit is a task type rather than a phase — settled, and `audit.md` §*Why it
  is a task and not a phase* is the record.

**Inputs**
[`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md), [`docs/method/plan.md`](../plugin/skills/taskmd/docs/method/plan.md),
`docs/METHOD.md` §3.3 and rule 4, [T-032](T-032-repair-the-audit-template-and-validate-templates.md)
§1 *Deliberately not answered here*.

**Acceptance criteria**
- [ ] `audit.md` says the procedure is designed in `plan`, per audit, and does not restate the
      threshold rule it already carries at step 2
- [ ] The method states what examining an unimplemented plan is, and it is reachable by someone who
      arrives asking for an "audit" of a plan — a distinction nobody finds is not a distinction
- [ ] METHOD rule 4 gains **no** exception, or the exception is argued explicitly and agreed by the
      owner against the objection recorded above
- [ ] `plan.md` says a written plan may be revised, and names the one place a revision is recorded
- [ ] Nothing added here is a second copy of METHOD §3.3 or `plan.md` step 5 — both already carry
      part of this, and the addition points rather than restates
- [ ] The always-loaded spine is unchanged, or the change is agreed against T-028's decision

**Open questions**
- None. **Q1 — plan revision, or an audit with an exception to rule 4? — answered by the maintainer
  on 2026-08-06: plan revision. Reviewing a task's plan is not to be called an audit, and rule 4
  gains no exception.**

  So criterion 3's second branch is closed: there is no exception to argue, and the criterion is now
  a plain requirement rather than a fork. The behaviour the maintainer originally described is
  unchanged and was never in dispute — only its name, and the exception the name would have forced.
  What remains is to write the distinction where someone arriving with the word "audit" will meet it
  (criterion 2), and to close the real gap: that the method never says a written plan may be revised
  or where the revision is recorded.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-06 | → specified | Q1 answered by the maintainer, accepting the objection: reviewing an unimplemented plan is plan revision, not an audit, and rule 4 gains no exception. Criterion 3's fork collapses to its first branch; no criterion amended. Worth recording that the disagreement was only ever about the name — the behaviour originally described (raise rather than apply, record what was rejected) is what the method already prescribes under METHOD §3.3 and `plan` step 5, and it is unchanged by the answer. The task's remaining content is therefore the two writing jobs, not a design argument. |
| 2026-08-06 | → proposed | Split from T-032 while answering its Q1, which was a narrow vocabulary question answered with a fuller account of the audit workflow. Two parts of that account are method changes: one agreed (the procedure is produced in `plan`, per audit), one argued against (that reviewing a task's plan is an audit needing an exception to rule 4). Raised rather than absorbed into T-032 — METHOD §3.3 — because T-032's subject is a template that had rotted into a stale copy of the method, and answering a method question inside it repeats the fault. The disagreement is recorded as the open question rather than resolved by the agent: rule 4 is the method's load-bearing rule and an exception to it is the owner's to grant. |
