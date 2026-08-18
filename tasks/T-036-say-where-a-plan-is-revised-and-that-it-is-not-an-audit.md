---
id: T-036
title: Say where a plan is revised, and that reviewing one is not an audit
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-032, T-026]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-06
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/docs/method/audit.md, plugin/skills/taskmd/docs/method/plan.md]
adopter_visible: yes
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
| 1 | Say in `audit.md` that an audit's procedure is produced in its own `plan`, pointing at step 2's threshold as part of that design rather than restating it. | A short paragraph introducing the Procedure list in `plugin/skills/taskmd/docs/method/audit.md`. |
| 2 | Give the distinction its own heading in `audit.md`, so someone arriving with the word "audit" for a plan meets it — carrying the three-part argument in short form and sending them to `plan.md`. | A new section in `plugin/skills/taskmd/docs/method/audit.md`. |
| 3 | Say in `plan.md` that a written plan may be revised, that the table is edited in place, and that the revision is recorded once as a decision — pointing at step 5 and METHOD §3.3, never restating either. | A new section in `plugin/skills/taskmd/docs/method/plan.md`. |
| 4 | Leave `METHOD.md` untouched and say so against criterion 6, whose wording predates T-028. | The review row, plus the note below on what that criterion now means. |
| 5 | Run `check`, `index` and the suite; confirm T-064 is not tripped by the two new sections. | Recorded output in §3. |

**Output paths**

- `plugin/skills/taskmd/docs/method/audit.md`
- `plugin/skills/taskmd/docs/method/plan.md`

## 3. Implement

**Decisions & assumptions**
- The distinction is stated in `audit.md`, not in `plan.md` — 2026-08-11. Criterion 2 is about
  reachability, and the reader who needs it is holding the word "audit"; they open the audit
  document. `plan.md` carries the mechanics and links back, so the two halves are each where their
  own reader arrives. Rejected: one section in `plan.md` with a pointer from `audit.md`, which puts
  the correction one hop behind the misconception.
- A plan revision gets **no home of its own** — 2026-08-11. It is recorded as a decision, under
  `plan` step 5, because a revision *is* a choice with a rejected alternative: the superseded steps.
  Rejected: a revision log in the plan section, which would be a second history beside the task's
  own, and would make the plan table describe both the present and the past.
- The superseded steps are replaced rather than struck through — 2026-08-11. Follows METHOD rule 5:
  the plan table states the present. The past is annotated in the decision, which is where a reader
  looking for *why* already goes.
- `METHOD.md` is untouched, taking Scope's stated default — 2026-08-11. Nothing here needs to bind
  before a phase file is opened: both readers of this distinction are already inside `plan` or
  reading `audit.md`.

**Evidence**

`check` exit 0 on 120 tasks, 1188 links resolved — five more than before the edit, which are the new
cross-references between the two sections and the spine. `test_runtime` holds T-064's rule that
nothing under `plugin/` may name `SCOPE.md`, `BRIEF.md`, `CLAUDE.md`, an `R-NN` or a non-goal; both
new sections are under `plugin/`, and it passes with the same four `Launchers` failures and no new
ones. `test_cli` 89, `test_list` 32, `test_schema` 46, `test_budget` 5 green.

`test_budget` passing is the check on criterion 6, and it is worth being precise about what it
proves: it measures tier 1, which since T-028 is `CLAUDE.md` plus the served skill descriptions.
`METHOD.md` is not in it, so that suite would have stayed green had this task edited the spine. What
holds criterion 6 is the diff — `METHOD.md` is not among the changed files — not the test.

**Outputs produced**
- `plugin/skills/taskmd/docs/method/audit.md` — the procedure paragraph, and *Auditing a plan that
  has not been implemented*.
- `plugin/skills/taskmd/docs/method/plan.md` — *Revising a written plan*.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `audit.md` says the procedure is designed in `plan`, per audit, and does not restate the threshold rule at step 2 | met | The paragraph introducing Procedure. It names step 2's threshold as *part of* that design and sends the reader there, rather than saying again what a threshold is. |
| The method states what examining an unimplemented plan is, and it is reachable by someone arriving asking for an "audit" of a plan | met | `audit.md`, *Auditing a plan that has not been implemented* — a heading in the document that reader opens, carrying the three-part argument and sending them to `plan.md`. |
| METHOD rule 4 gains **no** exception | met | Rule 4 is untouched; `METHOD.md` is not in the diff. The new section says explicitly that the case was never inside the rule, which is why no exception is needed. |
| `plan.md` says a written plan may be revised, and names the one place a revision is recorded | met | *Revising a written plan*: edited in place, recorded once as a decision under step 5. |
| Nothing added is a second copy of METHOD §3.3 or `plan.md` step 5 | met | Both are pointed at by name and neither is paraphrased. The §3.3 pointer carries the one fact that is this section's own — that a revision changing the *outcome* is not a revision at all. |
| The always-loaded spine is unchanged, or the change is agreed against T-028's decision | met | Unchanged. See the note below on what this criterion now means. |

**Criterion 6's wording predates the decision it defers to.** It was written on 2026-08-06 calling
`METHOD.md` "the always-loaded spine", and Scope's default reads "the spine is at 147/150 and T-028
is re-deciding what the budget covers". T-028 has since closed and decided exactly that: the budget
covers the whole always-loaded context, `METHOD.md` is tier 2 and is no longer always-loaded, and the
147/150 line count is not the measure any more. So the criterion's premise expired while the task
sat, and both readings — leave the spine alone, or leave the always-loaded set alone — are satisfied
by the same fact, that `METHOD.md` is not in the diff. Recorded rather than amended, per METHOD rule
5: what the record said about 2026-08-06 stays as it was.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All six criteria met, evidence in §3. Run under the full-lifecycle authorization the maintainer gave on 2026-08-11 for every open `M2` task, which covers that set and nothing outside it (METHOD §3.1). Criterion 6's premise had expired against T-028 while this task sat for five days; satisfied under both readings and recorded rather than amended. Raised nothing: the two writing jobs were the whole of it, and the design argument had been settled on 2026-08-06. |
| 2026-08-06 | → specified | Q1 answered by the maintainer, accepting the objection: reviewing an unimplemented plan is plan revision, not an audit, and rule 4 gains no exception. Criterion 3's fork collapses to its first branch; no criterion amended. Worth recording that the disagreement was only ever about the name — the behaviour originally described (raise rather than apply, record what was rejected) is what the method already prescribes under METHOD §3.3 and `plan` step 5, and it is unchanged by the answer. The task's remaining content is therefore the two writing jobs, not a design argument. |
| 2026-08-06 | → proposed | Split from T-032 while answering its Q1, which was a narrow vocabulary question answered with a fuller account of the audit workflow. Two parts of that account are method changes: one agreed (the procedure is produced in `plan`, per audit), one argued against (that reviewing a task's plan is an audit needing an exception to rule 4). Raised rather than absorbed into T-032 — METHOD §3.3 — because T-032's subject is a template that had rotted into a stale copy of the method, and answering a method question inside it repeats the fault. The disagreement is recorded as the open question rather than resolved by the agent: rule 4 is the method's load-bearing rule and an exception to it is the owner's to grant. |
