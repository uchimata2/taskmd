---
id: T-141
title: Report a table row with more cells than its header
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-025, T-095, T-107, T-121, T-140]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-141 — Report a table row with more cells than its header

## 1. Specify

**Outcome**
A Markdown table row carrying more cells than its header is reported by `check`, or this project
records that it will not be and says what a project relying on Markdown records is meant to do
instead.

**Why this one**
Raised from the htmldeck adopter report, row `O-T4`. The reporting project hit it twice in one
document, decided against building the equivalent gate for itself, and recorded the observation
anyway on the grounds that the trade may come out differently for a tool whose whole subject is
Markdown records. It does, and for a reason the report could not have known: **this repository has
the defect too**, and the instance destroyed part of a task record.

**Measured here before being argued.** A scan on 2026-08-15 read 270 Markdown files, 558 tables and
2,769 body rows, and found exactly one row wider than its header — in
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md), where a whole `→ proposed`
log entry was absorbed into the row above it during the commit that closed the task. It had rendered
as nothing on GitHub for five days short of a week. The repair is
[T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md); this task is the class.

**The failure mode is invisible by construction, and that is the argument.** Markdown drops the
excess cell silently, so the text is in the file and absent from the page. Nothing this project runs
had anything to say about it: `check` was clean on 105 tasks, the suite was green, and the
pre-publish gate printed its count and no lines. The instrument that finds it is counting cells
against the header, and there is no second one — which is what separates this from the classes
`check` already reports, where a reader could in principle have noticed.

**Why `check` is the only tool in the neighbourhood.** It already walks every Markdown document a
clone would receive and parses their links (`check_links`), so the file set, the read and the
gitignore reasoning all exist. The addition is a counting pass over the same text, not a new walk.

**The measured false-positive rate is what makes it worth deciding rather than assuming.** Zero over
2,769 rows here, which is a very different starting point from
[T-130](T-130-report-a-question-left-live-in-a-closed-task.md)'s 1-in-24 and from the precision
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) rejected. What the scan does not
yet know is the rate on a project that is not this one — and a row *narrower* than its header, which
Markdown pads rather than truncates, is a different question this task should decide is in or out.

**Requirements served**
R-16, and the rule behind it: a validator is worth what you believe it would catch. The belief here
is measured rather than estimated, in both directions.

**Scope**
- In: whether `check` counts a body row's cells against its header row, on the documents it already
  reads.
- In: what a short row does, since Markdown pads it and no text is lost — a different fault, possibly
  not one.
- In: the escape and code-span cases. GitHub-flavoured Markdown requires `\|` inside a table cell
  even within backticks, so an unescaped pipe in inline code splits a cell and is one of the ways a
  row grows without its author intending it.
- In: whether the class is advisory or a problem, on the precedent of
  [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) and
  [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md).
- Out: the T-099 instance, which is [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md).
- Out: any other opinion about Markdown a document could carry. This is one countable property, not a
  linter.

**Inputs**
- [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md) — the one instance and its provenance.
- The scan itself, to be re-run and recorded in §3 rather than quoted from here.
- [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) and
  [T-025](T-025-let-check-notice-a-stale-generated-index.md) — the two precedents for reporting a loss
  that produces no other signal.
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) — what a new counted class owes
  the itemised line.

**Acceptance criteria**
- [ ] The decision rests on a rate measured over this repository's own documents and over the shipped
      fixtures, not on an estimate
- [ ] If a class is added, it is shown **failing** on a fixture carrying the fault and staying quiet
      on every existing fixture and on this repository — a clean pass proves nothing
- [ ] The fixture is a fixture, not an example in prose: a task file demonstrating this fault would
      itself be a hit, so nothing outside `tests/fixtures/` may carry a specimen
- [ ] Whatever is decided about short rows is stated, including if the answer is that they are ignored
- [ ] If no class is added, one document says what a Markdown-native tracker does about a cell past
      the header, and `check`'s own scope statement does not imply it is covered
- [ ] Every existing fixture still reports exactly the classes it reported before

**Open questions**
- **Is this a problem or an advisory?** A row past its header is text the author wrote and no reader
  will ever see, which argues for a problem and a non-zero exit. Against: it is a rendering fault
  rather than a broken pointer, the adopting project weighed exactly that and declined to build it,
  and this repository's advisory classes exist for findings that are certainly real and not certainly
  wrong. Decide at `specify`, since it changes the acceptance criteria rather than the build.

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
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T4`. The report was written as an observation the reporter expected to be marginal, and it is not marginal here: the scan it prompted found this repository carrying the same fault, and the instance had silently destroyed a log row in a closed task. `high` because the loss is invisible to every instrument this project owns and the record it damaged is the kind this project exists to keep honest. `m` rather than `s` because the decision needs a rate on more than one corpus, a fixture that cannot live in a task file, and an answer about short rows. The third criterion is unusual and load-bearing: writing this checker up re-creates what it catches, so a specimen may not be quoted anywhere a scan would read it. |
