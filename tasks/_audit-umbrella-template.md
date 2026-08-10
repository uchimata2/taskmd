---
id: T-NNN
title: Audit — <scope>
type: audit
status: proposed
phase: specify
parent: null
blocked_by: []
related: []
work_package: <the release or grouping this belongs to>
owner: <name>
business_value: critical | high | low | medium
effort: xs | s | m | l | xl
created: YYYY-MM-DD
updated: YYYY-MM-DD
deliverables: []
---

<!--
An audit is a task type, not a phase, and it runs the same four phases as anything else:
[`plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §5, procedure in
[`plugin/skills/taskmd/docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md). Two
rules to keep in view while filling this in: say what counts as a finding **before** looking, and
never fix a finding where you find it. Do not add `children:` or `blocks:` — both are derived.
After filling this in, run:
    ./plugin/bin/taskmd index
-->

# T-NNN — Audit: <scope>

## 1. Specify

**Outcome**
<The findings that exist at the end, and what a reader can conclude from them. An audit's
deliverable is a set of findings, not a set of repairs.>

**Scope**
- In: <which deliverables, task files or documents are under review>
- Out: <what is deliberately not being looked at — worth more thought than the in-list>

**What counts as a finding**
<Stated before looking, per audit. Without this the audit reports whatever its author happens to
dislike and cannot be compared with the last one. Name the threshold, not a list of dimensions.>

**Inputs**
- `docs/...`

**Acceptance criteria**
- [ ] Every item named in scope has been examined, and the record says so even where nothing was found
- [ ] Each finding carries a severity and enough detail for someone who was not present
- [ ] <criterion specific to this audit>

**Open questions**
- <question — who answers it>

## 2. Plan

The audit **procedure** is designed here, for this audit — what will be looked at in what order, and
how each item will be examined. It is not the same from one audit to the next.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Findings**

| # | Finding | Severity | Child task | Status |
| :-- | :--- | :---: | :--- | :--- |
| F-1 |  | high / medium / low | T-NNN | open |

Findings needing no action stay in this table with the reason, and are the evidence that the area
was examined — worth as much as the ones that produced work.

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <the child tasks raised, and where the examination is recorded>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

**Closing**
This umbrella closes only when every finding is resolved — a `done` child, or dropped with the
reason recorded above. Closing over open children erases the link between the examination and its
consequences.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| YYYY-MM-DD | → proposed | Created. |
