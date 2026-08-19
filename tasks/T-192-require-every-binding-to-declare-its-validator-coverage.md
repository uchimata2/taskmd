---
id: T-192
title: Require every binding to declare its validator coverage
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-178, T-009, T-139]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-19
updated: 2026-08-19
adopter_visible: yes
deliverables: []
---

# T-192 — Require every binding to declare its validator coverage

## 1. Specify

**Outcome**
The binding contract requires each binding to state which of the validator's checks its backend
covers, which cannot occur there, and which still run locally — and both shipped bindings satisfy it.

**Why this one**
From the owner's answer of 2026-08-19 on
[T-178](T-178-give-the-github-binding-a-standing-verification.md), in their own words: today the
backend is GitHub, tomorrow it may be Notion or another service, so what ships must be flexible, and
the coverage belongs to whichever backend is in use rather than being rows written once about
GitHub.

**T-178 shipped the GitHub half and deliberately left this out**, because making the contract
*require* something changes what every binding must satisfy — including
`plugin/skills/taskmd/docs/bindings/local-markdown.md`, whose honest answer is *all of them, it is
the backend the validator was written for*. That is a different deliverable with a different blast
radius, and folding it into a paragraph in one binding is how a contract quietly gains a clause
nobody reviewed.

**The interesting half is not the requirement, it is what the requirement is allowed to be.** A
contract clause saying *list your coverage* produces a hand-kept list of a set the code owns in every
binding anybody ever writes — which is the class
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) exists to
catch, multiplied by the number of bindings. T-178's own table says so about itself. So the question
this task must answer is whether the declaration can be made checkable, or whether the contract
should ask for something coarser that cannot go stale.

**Requirements served**
R-9 and R-10 (`docs/SCOPE.md`) — the backend contract, and a binding being a document rather than
code.

**Scope**
- In: the contract clause in `plugin/skills/taskmd/docs/BINDING.md`
- In: both shipped bindings brought into line with it
- In: whether the declaration is checkable, and by what — including the answer *it is not, and here
  is the coarser thing we ask for instead*
- Out: writing the GitHub table. [T-178](T-178-give-the-github-binding-a-standing-verification.md)
  did that, and this task may reshape it but does not re-derive it
- Out: adding any check to the validator
- Out: a third binding. If the clause needs a third to be tested, that is a finding rather than a
  licence to write one

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 — what a binding must state today
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *What this does not cover, and why*, the
  first instance, and its two stated weaknesses
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the binding whose answer is trivial, and
  therefore the one that shows whether the clause is worth its cost
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) — the
  marked-list mechanism, and its stated boundary

**Acceptance criteria**
- [ ] `BINDING.md` states the requirement, in the register the rest of that document uses
- [ ] Both shipped bindings satisfy it, and the local one's answer is written out rather than
      assumed obvious
- [ ] The task states whether the declaration can be checked mechanically, with the reason — and if
      it can, the check exists and has been shown to fail
- [ ] **The clause is tested against a binding that does not exist yet**: someone writes what a
      Notion-shaped or issue-tracker-shaped binding would put there, from the clause alone. A
      contract clause proven only by the two bindings written before it is proven by its own examples
- [ ] Whether the requirement makes an existing binding's text redundant is answered, so the contract
      does not ask for a second copy of something a binding already says

**Open questions**
- **Is a hand-kept coverage list worth having at all?** T-178's table carries its own warning that it
  will go stale, and the contract would mint one per binding. The alternative is coarser — *say
  which checks cannot occur on your backend, and say that the rest either apply or still run
  locally* — which is stable under a new check being added and answers less. **Decide at `specify`**;
  it changes what the clause asks for rather than how it is written.

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
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-178](T-178-give-the-github-binding-a-standing-verification.md) raised it. **It does not answer §1's question**, which decides what the clause asks for and is a judgement about a contract every future binding inherits. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s `specify`, carrying the widening the owner attached to that task's answer. Kept out of T-178 on purpose: a clause in the contract is satisfied by every binding that exists and every one that ever will, and T-178's outcome is one document. `m` because the fourth criterion needs somebody to write a binding fragment that does not exist. |
