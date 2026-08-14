---
id: T-140
title: Restore the log row a table cell swallowed in T-099
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-099, T-141]
work_package: M6
owner: the project owner
business_value: high
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-140 — Restore the log row a table cell swallowed in T-099

## 1. Specify

**Outcome**
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)'s log carries the
`→ proposed` row it was written with, so the reason a `critical` task was raised is readable again
by whoever reads that record next.

**Why this one**
Found on 2026-08-15 by scanning every Markdown table in this repository for a body row holding more
cells than its header — the failure the htmldeck adopter report describes as `O-T4`. The whole tree
has exactly one such row, and it is T-099's.

The provenance is exact. At `d56486f` the log held five rows, and the last was a full
`→ proposed` entry recording where the task came from, why it was `critical`, why it was `s`, and
the two facts it did not want `specify` to rediscover. At `2810997`, the commit that closed the
task, that row lost its leading `| <date> | → proposed | Raised as R-1 from the first adopting
project's recommendations,` and the rest of the sentence became a **fourth cell on the row above
it**, which has a three-column header.

**What that costs, and why it went unseen for five days short of a week.** GitHub-flavoured Markdown
drops a cell past the header, so the text is in the file and renders nowhere. Every instrument this
project owns said the tree was fine: `check` was clean, the suite was green, the pre-publish gate
printed its count and nothing else. The task also reads as complete — a log with four plausible rows
does not look like a log missing one. So the only reader who could have caught it is one comparing
the file against a commit five days older, and nobody had a reason to.

**Two things are lost, not one.** The rationale is the obvious loss. The other is the attribution:
`Raised as R-1 from the first adopting project's recommendations` is the sentence that says T-099
came from an adopter at all, and it is the half that vanished completely rather than being displaced.

**Scope**
- In: T-099's log, restored to the five rows the file was written with.
- In: how the restoration is marked, given METHOD §1.5 — *correct what the record says about the
  present, never rewrite what it says about the past, annotate instead*. A row that was written,
  then damaged by a later edit, is arguably neither.
- Out: the class. [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) owns whether
  anything catches the next one, and fixing the instance must not be read as covering it.
- Out: any other edit to T-099. Its findings, decisions and criteria stand as reviewed.

**Inputs**
- [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md), the damaged row.
- `d56486f`, which holds the row as written.
- `2810997`, the close commit that damaged it.

**Acceptance criteria**
- [ ] T-099's log holds five rows, and the restored one carries the text at `d56486f` rather than a
      paraphrase of it
- [ ] No row in the file has more cells than its header, shown by re-running the scan over the whole
      tree rather than by reading the one file
- [ ] The restoration is visible as a restoration, so a later reader is not left thinking the row was
      always there
- [ ] `check` and the suite are green, and the file still renders as four phases and one log

**Open questions**
- **Does an annotation belong on the restored row?** METHOD §1.5 forbids rewriting what a record says
  about the past, and this is the unusual case where restoring the past is what puts it right. Against
  an annotation: it is text about the repository's edit history sitting inside a task's own account of
  itself. For it: a reader who diffs this file later will otherwise find a row appearing in a closed
  task with nothing saying why. Decide at `specify`, since it changes what the outcome is.

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
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T4`, which named the failure mode without knowing this repository had an instance. The scan that found it read 270 Markdown files, 558 tables and 2,769 body rows and returned exactly one hit, so the instance is isolated and the repair is bounded. `high` rather than `medium` because the lost text is the raising rationale of a `critical` task and the sentence attributing it to an adopter, and because the loss survived `check`, the suite and the pre-publish gate — the record was wrong in a way nothing this project runs could report. `xs` because the original text is in git and the edit is one row. The class is deliberately not here: it is T-141, and closing this one does not close that one. |
