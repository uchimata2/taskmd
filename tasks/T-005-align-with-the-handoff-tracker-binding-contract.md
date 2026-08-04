---
id: T-005
title: Align with the handoff tracker-binding contract
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-002]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-005 — Align with the handoff tracker-binding contract

## 1. Specify

**Outcome**
Either a contributed/updated `local-markdown-dir` binding, or a documented statement of how taskmd projects should configure handoff.

**Why this one**
The binding states *"the folder is the index"*, which is false for any project using a generated one — see the Handoff repo's improvement brief, F1. taskmd is exactly such a project, so it will hit this. Doing it after the binding changes avoids building against a contract about to move.

**Acceptance criteria**
- [ ] The handoff F1 outcome is known before this is designed
- [ ] A taskmd project can be driven by handoff with no hand-written workaround
- [ ] `tracker_lint` documented as the way the invariant is enforced

**Open questions**
- Contribute a binding upstream, or ship a config recipe? — depends on the F1 outcome

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
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
