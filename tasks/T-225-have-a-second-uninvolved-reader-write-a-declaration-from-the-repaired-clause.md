---
id: T-225
title: Have a second uninvolved reader write a declaration from the repaired clause
type: audit
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-222, T-199, T-176]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-225 — Have a second uninvolved reader write a declaration from the repaired clause

## 1. Specify

**Outcome**
A reader who has read no taskmd binding produces a coverage declaration from the repaired
`BINDING.md` §4, and every place they had to guess is recorded — so it is known whether
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s repair
works on somebody who was not in the room.

**Why this one**
T-222 repaired eight defects a stranger found, and **the author reading it back is not a test** —
that is the failure the whole line of work came from, and T-222's own sixth criterion says so.
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) built the
instrument and it worked: one reader, one prompt, one declaration, eight defects and a blank.

**Set the terms before running it, because this is the run that turns an instrument into a loop.**
A second reader on a repaired document is fresh, and the loop is still *edit until somebody agrees*.
Two things must be fixed in advance: **how many readers** (one), and **what counts as a pass** —
which is not *no questions*, since T-199's reader asked four re-read questions that were about
ordinary density rather than about defects. Decide the bar with the owner before the prompt is sent.

**Scope**
- In: one reader, one prompt, the repaired §4 embedded verbatim, no other file within reach
- In: a **different backend** from T-199's Jira Cloud, so the run is not the same question twice
- In: the pass bar, agreed before the run
- Out: repairing whatever it finds. T-199 established that repairing inside the measuring task
  destroys the evidence the measurement happened
- Out: a third reader. If the second finds defects, that is a repair task and then a decision about
  whether to measure again — not an automatic next round

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 as repaired on 2026-08-22
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3 — the
  instrument, the prompt shape, and the eight defects this run is testing the repair of

**Acceptance criteria**
- [ ] The reader states, in their own words, that they had read no taskmd binding
- [ ] The declaration is recorded verbatim, including anything they refused to write
- [ ] Every question they had to settle by guessing is listed, and each is matched against the eight
      T-222 repaired — so it is visible whether a repair worked, missed, or created a new gap
- [ ] The pass bar was written down before the run, and the verdict is given against it

**Open questions**
- **What is the pass bar, and how many readers?** — the project owner. The recommendation is **one
  reader**, and **pass = none of the eight recurs and no new defect blocks the declaration**; a
  re-read question is not a defect. Deciding this after seeing the result is what turns the
  instrument into iteration.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → proposed | Raised by [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s sixth criterion, which asks what would test the repair and permits that test to be a separate task. **Separate rather than folded in**, for T-199's own reason: a repair measured by the person who wrote it is not measured. `medium` and `s` — the instrument exists and the run is one prompt. **The hazard is named in §1 rather than left to the run**: a second reader on a repaired document is one edit away from being iteration, so the count and the bar are set before the result is known. |
