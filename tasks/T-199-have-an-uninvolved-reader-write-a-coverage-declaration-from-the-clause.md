---
id: T-199
title: Have an uninvolved reader write a coverage declaration from the clause
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-192, T-176]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-199 — Have an uninvolved reader write a coverage declaration from the clause

## 1. Specify

**Outcome**
Someone who has not read either shipped binding writes a `cannot-occur` declaration for a backend of
their choosing, from `BINDING.md` §4 alone — and what they produce is compared against what the
clause meant, so the clause is judged by how it reads rather than by how it was written.

**Why this one**
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) met its fourth criterion by
writing a Notion-shaped fragment from the clause, and **that exercise immediately found the clause
wrong**: it said *cannot occur on this backend* when what decides the answer is the binding's
mapping, not the service. Two backends that both allocate identifiers answer differently on
`DUPLICATE ID`, depending on whether the binding uses the service's identifier as the task id.

**So the residue is not a doubt, it is a demonstrated rate.** One reading of the clause by its own
author, in a session that had already read both shipped bindings, produced one defect. That is the
weakest form of the test — the author cannot un-know the examples, and the clause is a contract every
binding anybody ever writes inherits. What a stranger does with it is the thing worth knowing, and it
is the one thing a session cannot stand in for.

**Scope**
- In: one reader, one backend of their choosing, one fragment written from `BINDING.md` §4 without
  reading `plugin/skills/taskmd/docs/bindings/`
- In: what they asked, what they got wrong, and what they could not decide — those are the clause's
  defects, not the reader's
- Out: **rewriting the clause during the exercise.** Whatever the reading turns up is recorded first
  and repaired afterwards; a clause edited while somebody is reading it has been tested against
  nothing
- Out: adopting the fragment as a third binding. §1 of
  [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) rules a third binding out
  and that is unchanged — this produces a reading, not a document to ship

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 — *The coverage a binding declares* — which is all the
  reader gets
- [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) §3 step 5 — the author's
  own fragment and the defect it found, read **after** the reader has finished and not before

**Acceptance criteria**
- [ ] The reader had not read either shipped binding, and that is stated rather than assumed
- [ ] What they produced is recorded verbatim, including anything they left blank
- [ ] Every question they asked is recorded as a defect in the clause, with what the clause should
      have said
- [ ] Whether their fragment classifies any class differently from the author's, and why, is stated
- [ ] The clause is repaired afterwards, or the reasons for leaving it are recorded

**Open questions**
- **Who reads it?** The owner's to choose. It cannot be a session: `BINDING.md` is in this
  repository, so any session working here has the shipped bindings within reach and cannot honestly
  claim not to have read them. This is the same constraint
  [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) waits on. **Answered in part by the owner on 2026-08-22: one route, chosen once and used for both tasks. Who that reader is remains open** — see the Log row of that date.

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
| 2026-08-22 | (no change) | **Re-edged from `parent: T-192` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** The clearest of the three: every one of [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)'s criteria is **met**, and its §4 already says in its own words why it closed — this task is *"a stronger test of a clause that already works rather than a gap in it"*. It waits on an uninvolved reader, which no session can supply. The soft edge keeps the pointer in both directions without holding a finished deliverable open. Reopening T-192 was rejected because there is no criterion to reopen it against; recorded in T-216 §3. |
| 2026-08-21 | → proposed | Raised by [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)'s review. Its criterion 4 was **met** — a fragment was written from the clause and changed it — so this is not a gap left behind but the stronger version of a test that already paid for itself once. Raised rather than noted, because it needs a person and a note inside a closing task leaves every view a project has. `medium` and `s`: the exercise is short and the clause it judges is inherited by every binding anybody writes. **Waits on a person**, so the 2026-08-19 grant does not reach it. |
| 2026-08-22 | (no change) | **The open question is answered in part by the owner: one route, chosen once and used for this task and for [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md).** Asked in the batched round of 2026-08-22. Both are blocked on this and on nothing else, so one answer unblocks two. *Rejected: a different reader for each*, which makes each reading true first contact, but needs two people and blocks both tasks until they are found. *Rejected: the owner reads both*, available immediately, but they cannot un-know material they have already ruled on — the exact weakness this task exists to remove. **Still open: who that reader is.** The shape is settled and the person is not, so §1's question is narrowed rather than closed. This row is the answer, not authorisation to start. |
