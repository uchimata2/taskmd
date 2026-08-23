---
id: T-NNN
title: <imperative, one line — it appears in every generated view, so make it read out of context>
type: admin | analysis | audit | decision | deliverable | fix | research
status: proposed
phase: specify
parent: null
blocked_by: []
related: []
work_package: <the grouping this belongs to — a label, not a version number>
owner: the project owner
business_value: critical | high | medium | low
effort: xs | s | m | l | xl
created: YYYY-MM-DD
updated: YYYY-MM-DD
deliverables: []
---

<!--
Named rather than linked, because this file is copied into whichever project uses it and a relative
link would resolve from there and not from here. The lifecycle, which edge to use and where each
fact lives are in the taskmd skill's `docs/METHOD.md`. The field names and allowed values are this
project's schema — its own `.taskmd/config.md`, or the skill's `taskmd/defaults/config.md` if it has
none. Do not add `children:` or `blocks:` — both are derived. After filling this in, run:
    taskmd index
-->

# T-NNN — <title>

## 1. Specify

**Outcome**
<What exists at the end that does not exist now. One paragraph.>

**Scope**
- In: <...>
- Out: <...>

**Inputs**
- `docs/...`

**Acceptance criteria**
- [ ] <criterion 1>
- [ ] <criterion 2>

**Open questions**
- <question — who answers it>

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

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| YYYY-MM-DD | → proposed | Created. |
