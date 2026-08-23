---
id: T-255
title: Derive the audit cycle membership instead of typing it
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: []
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-255 — Derive the audit cycle membership instead of typing it

## 1. Specify

**Outcome**
One command prints the Files and Bytes columns of
[T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
§2, and the file list for any single cycle, from membership rules held in one place. **It fails when a
tracked path in the subject belongs to no cycle**, so a file added after the plan was written stops
the reading rather than surviving it unexamined.

**Why this one**
T-244's per-cycle figures were computed by hand on 2026-08-23 from a membership list that lives
nowhere in the repository. The totals were verified per item on that day and were correct; nothing
keeps them correct. The audit runs across many sessions and the tree moves between them, which is
exactly the interval a hand-typed partition cannot survive.

**The evidence is another project's, and it is not hypothetical.** htmldeck ran the same method first
and its finding `PR-06` was this: the plan stated counts rather than deriving them, its two coverage
tables could not reconcile, **four files went unread and the run looked complete**. It raised
`T-223` to derive the membership and found a file its old table had counted twice. This task is that
lesson taken before the same cost is paid here, per
[`../CLAUDE.md`](../CLAUDE.md) *Working across my own repositories*.

**Scope**
- In: the membership rules for T-244's eight examining cycles, in one place, with one rule per cycle
- In: a `--plan` output that emits the columns ready to paste, and a per-cycle output naming the files
  a session reads
- In: the whole-partition verdict printed **before** any per-cycle answer, so an unassigned path is
  seen rather than scrolled past
- Out: assigning findings, severities or the register — that is T-244's own work
- Out: shipping this to adopters. It is repository machinery, not part of what an install copies

**Inputs**
- [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
  §2 — the eight cycles and the subject the rules must cover
- htmldeck's `tools/docs/cycles.py` — the working implementation of exactly this, for its shape rather
  than its rules

**Acceptance criteria**
- [ ] The command prints T-244 §2's Files and Bytes columns, and its figures match a hand check of the
      subject on the day it is run
- [ ] Adding a file to `plugin/` and re-running it makes the command **fail**, naming that path. A
      clean run on an untouched tree proves nothing
- [ ] A single cycle's file list can be asked for, and the whole-partition verdict prints first
- [ ] T-244 §2's Files and Bytes are printed by this command rather than typed, and its *how to run
      one cycle* step 2 — which already names this command — resolves to something that runs

**Open questions**
- **Where it lives, and whether it is one script or a check inside the suite.** `tests/` already runs
  on every change, which would catch an unassigned file without anyone asking — but a test cannot emit
  columns to paste. Whoever plans this.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **This task now blocks [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)**, on the owner's instruction of 2026-08-23. It was raised as a soft link on the session's recommendation that the generator *should probably* land first; the owner made it a gate. **What changed in T-244:** the edge is on that record's `blocked_by`, its §2 no longer says the defect is shipped knowingly, and its *how to run one cycle* step 2 now asks this command for the file list instead of describing a manual `git ls-files` check nobody would have run. **The `related` edge here was removed** — a dependency already connects the pair in both directions and the inverse is derived, so keeping both would have been the same fact in two homes. |
| 2026-08-23 | → proposed | **Raised while planning [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)**, 2026-08-23, on the owner's instruction to compare that plan against htmldeck's run of the same method and take the better of the two. The comparison returned one defect rather than a preference: T-244's per-cycle Files and Bytes are hand-typed, and htmldeck's `PR-06` is the measured cost of that exact shape — four files unread, two tables that could not reconcile. **Raised rather than fixed inside T-244** because it is machinery T-244 consumes and not part of the audit, per METHOD §5 and this repository's rule that a discovery outside the current task costs one record. T-244 §2 ships the defect knowingly and names this task beside it, so a session running a cycle before it lands knows the partition check is manual. |
