---
id: T-223
title: Ship the pre-release audit as a method document, so every adopter gets it
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-032, T-036]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/method/pre-release-audit.md
---

# T-223 — Ship the pre-release audit as a method document, so every adopter gets it

## 1. Specify

**Where this came from**

An adopting project — `htmldeck`, public — was asked for a full pre-release audit of itself and found
it had no reusable statement of how to run one. It wrote one locally, then read
[`audit`](../plugin/skills/taskmd/docs/method/audit.md) and found that most of what it had written
either already lived here or contradicted a rule here. **The owner's decision was that the pre-release
audit should be a taskmd feature rather than one project's local document**, so every adopter gets it.

This branch carries a **draft** at the deliverable path. It is the input to `specify`, not a finished
deliverable, and the outcome is not agreed until this task says so.

*Reviewed 2026-08-22, after the branch merged.* **That is true of the draft's status and false of
its location.** The branch is `master` now, and the deliverable path is inside `plugin/`, which is
exactly what an install copies (T-053). Nothing in the tree says the document is a draft — only
this record does — and `METHOD.md` §5 and §7 and [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
already point at it by name. So the three open questions below are not held open at no cost: they
are held open on a document that the next tag publishes as method, and that the adopting project is
already waiting for — `htmldeck`'s `docs/AUDIT-METHOD.md` says *"`pre-release-audit.md` arrives
with a taskmd release; until it does, this file names what it will carry"*. **Answering them, or
moving the draft off the deliverable path, is what makes the *draft* claim true of the tree as well
as of this record.**

**Outcome**

One tier-3 method document, loaded on demand, that a session can follow to run an audit whose subject
is everything a project is about to release — without that document telling anyone what to look for.

**Scope**

- In: the six things that only start to matter when an audit's subject is *everything* — coverage
  grades, coverage as a failing partition, cycles, severity that obliges something, remedy-as-hypothesis,
  and a grading pass after the remedies exist. Plus the scale exception that moves findings out of the
  umbrella, and the rule that this audit is requested and is never a step in a release procedure.
- In: one row in [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §7, one clause in its §5, and one
  pointer from [`audit`](../plugin/skills/taskmd/docs/method/audit.md). No rule in either is changed.
- Out: **anything that says what to look for.** See *The two constraints* below.
- Out: shipping a template. taskmd ships no task templates and that is a design decision (T-101, T-032);
  the audit umbrella stays project-owned. Raise it separately if it is wanted.
- Out: validating a `finding:` field against a findings register. That is schema and tool work, it is a
  real gap the adopting project has worked around, and it is a different task.

**The two constraints this was written against, and how the draft satisfies them**

1. **R-9** — nothing in the method may assume code, tests, compilers or version control; it must read
   sensibly for research, a deck, a training course or an ops runbook. The source document assumed all
   four. The draft names no artefact type, no tool and no command, and its worked example is a training
   course before its first cohort. **This is the criterion most likely to be violated by a later edit**,
   because the person editing will have a repository in mind.
2. **[`audit`](../plugin/skills/taskmd/docs/method/audit.md), *Procedure*** — *"How this one examines its
   subject is not fixed here … A standing checklist carried by every audit would examine each new subject
   for the last subject's problems."* The source document was largely such a checklist: four named
   aspects, a list of finding classes, and a forty-three cycle programme. **None of that came across.**
   What came across is the *shape* the plan must decide — grade the subject, choose aspects, order the
   cycles — with one project's aspects shown as an illustration and explicitly not a set to adopt.

**What was deliberately left behind**

The source document's aspects, its finding-class list, its cycle programme, its identifier space, its
register location, and everything reasoning from files, sizes, gates or renders. Those stay in the
adopting project's own audit plan, which is where [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
says a given audit's procedure belongs.

**Inputs**

- [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — the procedure this extends and does not change.
- [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5, §7 — the type, and the load-on-demand table.
- [`SCOPE.md`](../docs/SCOPE.md) §3 R-9, R-21, R-22 — the constraints above, and the tier discipline.

**Acceptance criteria**

- [ ] The document tells a session how to *run* an audit of everything and never what to *find* in one.
- [ ] It reads sensibly for a non-software project, demonstrated by a worked example that is not software.
- [ ] It restates no rule that [`audit`](../plugin/skills/taskmd/docs/method/audit.md) or
      [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) already owns; where it deviates from one, it
      says so and says why.
- [ ] Tier 1 is unchanged; `tests/test_budget.py` passes without editing the bound.
- [ ] `taskmd check` passes.
- [ ] The claim that the document is reachable is verified by running, not by reading the §7 table.

**Open questions**

- **Is the scale exception acceptable?** The draft lets findings move out of the umbrella into their own
  record once the umbrella stops being a task record, under three conditions. It is a documented
  deviation from [`audit`](../plugin/skills/taskmd/docs/method/audit.md) step 3, and it is the one place
  the draft argues against an existing rule rather than extending it. Owner answers.
- **Is `pre-release audit` the right name?** The document is about audit *scale*, and the release is only
  the commonest reason to reach that scale. `audit at scale` would be more accurate and less findable.
  Owner answers.
- **Does the Low-batching rule belong here or in `audit`?** The draft batches Low findings instead of
  raising a task each, and argues it as a scale rule. It may be a correction to
  [`audit`](../plugin/skills/taskmd/docs/method/audit.md) step 4 at every scale. Owner answers.
- ~~**Id collision.** `T-223` was the next free number when this branch was cut, and another session was
  committing to `master` at the time. Renumber at merge if it was taken.~~ **Settled 2026-08-22: it keeps
  `T-223`.** The other session had allocated the same number and neither could see the other. This branch
  was merged first and so was reachable by anybody else, which is the rule that decided it; the other
  record renumbered to
  [T-229](T-229-correct-the-migrated-away-fixture-s-own-prose-which-still-says-all-four-commands-refuse.md)
  and its references moved with it. Nothing here changed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Reviewed at the owner's request, who was unsure the task had landed as it should.** Phase unchanged: this is an input to `specify`, not `specify` being done for them. **What verified clean.** The generic/local split is real and both sides state it rather than duplicate — `htmldeck`'s `docs/AUDIT-METHOD.md` opens *"The method is not here"* and points at the three taskmd documents, and its register defers §5's grading rule to this one by name. **R-9 holds**: a sweep for software vocabulary over the whole document returns `source` (as in *source of findings*), `file` (as in *this file*) and `Test` (a table heading), and the worked example is a training course. **§5's figures are sourced and were re-checked today** against the adopting project's own records — *two of thirteen held as written*, *every error was in the remedy and none in the observation*, *four rows were refused by a measurement taken while implementing them* — all three verbatim in `htmldeck`'s `docs/lessons/L-90.md` and `docs/CONTEXT-AUDIT.md`. `check` and the suite are green and tier 1 is unchanged. **What did not land: the draft is at the deliverable's address inside `plugin/`.** §1 above now carries that and what follows from it. **Two of the three open questions get more expensive after a release, not less** — the name is a path that `METHOD.md`, `audit.md` and a downstream document would all have to follow, and the scale exception is a published deviation from a published rule. **Nothing was raised from this review**: every finding is an input to this record's own `specify`, and routing them elsewhere would scatter one task's inputs. |
| 2026-08-22 | → proposed | Raised from an adopting project that needed the method and found it was not shipped. A draft is in this branch at the deliverable path, as the input to `specify`. |
