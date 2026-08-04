---
id: T-003
title: Write the skill that teaches the agent to use the CLI
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-002]
related: []
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-003 — Write the skill that teaches the agent to use the CLI

## 1. Specify

**Outcome**
A skill that makes the agent run the CLI rather than read task files, and create tasks from the template.

**Why this one**
The failure mode is a skill that restates the CLI's rules in prose — a second copy that drifts. It must point, not describe.

**Acceptance criteria**
- [ ] The skill body is short enough to load on every turn without cost
- [ ] No rule stated in the skill is also enforced by the CLI
- [ ] Creating a task through the skill produces a file `check` accepts

**Open questions**
- Should the skill be model-invocable, user-invocable, or both?

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
