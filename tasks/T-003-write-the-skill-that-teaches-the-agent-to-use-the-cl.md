---
id: T-003
title: Write the skill that teaches the agent to use the CLI
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-002, T-008]
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

**Requirements served**
R-6, R-7, R-8, R-9, R-21, R-22 (`docs/SCOPE.md`).

**What the skill must carry that the CLI cannot enforce**
The CLI validates files; it cannot govern how the agent behaves. These three are the skill's real
content, and none of them is a restatement of something the tool checks:

- **R-6 — one phase per request, never auto-advance.** A "next step" note, a handoff pointer or an
  obvious continuation is context, not authorization.
- **R-7 — ask to the phase's exit criterion**, batched into one turn, never drip-fed.
- **R-8 — surface what you discover.** Anything found mid-execution that would reasonably improve
  quality becomes a question (if it changes the current task's spec) or a task (if it is actionable
  and out of scope). Never absorbed silently, never dropped.

**Acceptance criteria**
- [ ] The skill body is short enough to load on every turn without cost
- [ ] No rule stated in the skill is also enforced by the CLI
- [ ] Creating a task through the skill produces a file `check` accepts
- [ ] Structured for progressive disclosure — a spine that always loads, the rest on demand (R-21)
- [ ] The three behavioural rules above are present and each is testable by a walked example
- [ ] Contains no software vocabulary — proven by walking a non-code task through it (R-9)
- [ ] Points at the method document rather than restating any part of it (R-22)

**Open questions**
- Should the skill be model-invocable, user-invocable, or both?
- Does the method document (T-008) become the skill's spine, or a file the spine points at?

**Why the new blocker**
`blocked_by` gained T-008: the skill teaches the method, so it cannot be written before the method
document exists without becoming the second copy this task is specifically meant to avoid.

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
