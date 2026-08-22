---
id: T-222
title: Repair the coverage clause against the eight defects a stranger found
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-199, T-192]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/BINDING.md
---

# T-222 — Repair the coverage clause against the eight defects a stranger found

## 1. Specify

**Outcome**
`plugin/skills/taskmd/docs/BINDING.md` §4 answers, from its own text, every question
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader had
to settle by guessing — or says where the answer lives.

**Why this one**
**A clause every binding anybody writes inherits had never been read by anybody who had not written
it.** T-199 ran it past a reader who had read no binding and asked them to produce a real
declaration. They produced one, and with it eight questions they could only answer by guessing, and
one blank.

**The blank is the sharpest result and it is the shape of the whole problem.** §4 describes the
stale-index state twice and never names its class. The reader guessed the name, got it **right**, and
refused to write it down — *"Guessing would pass a human and fail the one check the region exists to
support."* A clause that asks for class names in backticks, and never says where class names come
from, cannot be completed honestly by anyone who does not already know the answer.

**The repair's shape is decided by the clause's own argument, which is why this is a fix and not a
decision.** §4 already refuses a per-check coverage table, and gives the reason: *"one new check
falsifies every binding's table at once."* So the repair must **not** enumerate the classes. It must
point at whatever owns them — the same single-source rule the clause already argues for, applied to
the clause itself.

**Scope**
- In: the eight defects listed in
  [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3, each
  repaired or declined **by name**, with a reason for each decline
- In: where the validator's class list lives, stated in the clause
- In: what the marked-region check **scans**, not only what it confirms — the reader avoided
  backticking a command in case the scan was wider than the text says
- In: **reporting** whether the repaired clause leaves either shipped binding's existing declaration
  non-compliant
- Out: changing the validator, its classes, or the marked-region check. Every defect here is in the
  description, not in the behaviour
- Out: **fixing** a shipped binding the repair invalidates — that is a finding here and a task of its
  own, because editing a binding inside the task that changed the contract hides which one moved
- Out: re-running the reader. T-199 fixed one reader and its verdict stands; a second reading after a
  repair is a different question and would be a different task

**Inputs**
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3 — the
  eight defects, the four re-reads, and the declaration verbatim including the blank
- `plugin/skills/taskmd/docs/BINDING.md` §4, and its subsection *The coverage a binding declares*
- [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) §3 step 5 — the author's
  own fragment, and the defect it found in the previous wording

**Acceptance criteria**
- [ ] Each of the eight defects is repaired or declined **by name**, and every decline carries its
      reason
- [ ] The clause says where the validator's class list lives, and **does not enumerate it** — the
      shape its own anti-table argument requires
- [ ] The clause states what the marked-region check reads, so a writer can tell whether a backticked
      word that is not a class name is safe inside the region
- [ ] Whether the declaration is an entry or a section, what its bold lead may claim, and how long
      that lead may be, are all answerable from the text alone
- [ ] Both shipped bindings' declarations are checked against the repaired clause, and any that no
      longer complies is **named** — repaired or raised, stated either way
- [ ] What would test the repair is stated, even where that test is a separate task. The author
      reading it back is not a test, and that is the failure this whole line of work came from

**Open questions**
- **None.** The reader's eight items are specific, and the shape of the repair is settled by §4's own
  argument against hand-copied tables rather than by a preference.

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
| 2026-08-22 | → proposed | Raised from [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader run under the owner's decision of 2026-08-22, which chose a separate task over repairing inside T-199. **The reason is size, not process**: T-199's fifth criterion permits the repair in place, and eight defects in a contract every binding inherits is a rewrite rather than an edit. T-199 records that reason and stays open on that criterion alone. `high` because the clause is inherited by every binding anybody ever writes, and the one reader who has tried to use it could not complete it without guessing eight times. `m` because the hard half is not the edits but keeping the repair inside the clause's own rule — it argues against hand-copied lists and must not answer the class-name defect by writing one. |
