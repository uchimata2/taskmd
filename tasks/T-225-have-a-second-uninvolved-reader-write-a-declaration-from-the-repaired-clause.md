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
- ~~**What is the pass bar, and how many readers?** — the project owner. The recommendation is **one
  reader**, and **pass = none of the eight recurs and no new defect blocks the declaration**; a
  re-read question is not a defect. Deciding this after seeing the result is what turns the
  instrument into iteration.~~ **Answered by the owner on 2026-08-22: the recommendation stands** —
  one reader, and that pass bar. See the Log row of that date.

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
| 2026-08-22 | (no change) | **The prompt is built and handed to the owner, who runs it.** Assembled the same day from `BINDING.md` §4 as repaired, extracted whole with `awk` from the section heading to the next one and embedded verbatim beneath the ask — so it is **regenerated, never stored**: a copy kept in this repository would be a second home for §4 and would go stale the first time §4 is edited, which is the defect the clause it tests argues against. **What the ask contains**: state whether you have read a taskmd binding; pick a tracker and say why, not Jira Cloud; state the mapping before writing; write the declaration as you would ship it; then list every question you had to settle by guessing, with what you decided and what you wanted the text to say. **What it deliberately does not contain**: that a repair is being tested, that eight defects were found before, and any invitation to leave a blank — [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader left one unprompted and that was the finding, so prompting for one here would manufacture the result. The pass bar was fixed in the row of this date **before** the prompt existed. |
| 2026-08-22 | (no change) | **The pass bar and the reader count are fixed by the owner, before the run: answered 2026-08-22.** **One reader**, and **pass = none of the eight defects recurs and no new defect blocks the declaration**; a re-read question is explicitly *not* a defect, because [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader asked four of those and they were density rather than missing facts. *Rejected: decide the bar after seeing the result* — it is the same failure as writing acceptance criteria to a known verdict, one instrument along, and it is what turns a check into *edit until somebody agrees*. *Rejected: two readers* — more confidence, and only if the count is fixed in advance either way, which is the condition that makes one enough. **The date matters as much as the answer**: this row precedes any prompt being sent, so a later session can see the bar was not tuned to the result. |
| 2026-08-22 | → proposed | Raised by [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s sixth criterion, which asks what would test the repair and permits that test to be a separate task. **Separate rather than folded in**, for T-199's own reason: a repair measured by the person who wrote it is not measured. `medium` and `s` — the instrument exists and the run is one prompt. **The hazard is named in §1 rather than left to the run**: a second reader on a repaired document is one edit away from being iteration, so the count and the bar are set before the result is known. |
