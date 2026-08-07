---
id: T-003
title: Write the skill that teaches the agent to use the CLI
type: deliverable
status: specified
phase: specify
parent: null
blocked_by: [T-002, T-008]
related: []
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-07
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

They are **[`docs/METHOD.md`](../docs/METHOD.md) §3.1, §3.2 and §3.3** — serving R-6, R-7 and R-8
respectively. Their wording is not repeated here: this task exists to stop the skill becoming a
second copy of the method, and a task file that opens by making one would be arguing against itself.
Read §3 before specifying the skill; what the skill adds is the *mechanism* that makes those rules
fire on every turn, not the rules.

**Acceptance criteria**
- [ ] The skill body is short enough to load on every turn without cost
- [ ] No rule stated in the skill is also enforced by the CLI
- [ ] Creating a task through the skill produces a file `check` accepts
- [ ] Structured for progressive disclosure — a spine that always loads, the rest on demand (R-21)
- [ ] The three behavioural rules above are present and each is testable by a walked example
- [ ] Contains no software vocabulary — proven by walking a non-code task through it (R-9)
- [ ] Points at the method document rather than restating any part of it (R-22)

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: both model-invocable and user-invocable.**
  Model invocation is what `docs/SCOPE.md` §1 *Invisibility* requires — the tool has to work without
  being asked for. User invocation costs one line of front-matter and is the only way to force the
  skill when the model does not trigger, or to find out why it did not. *Rejected: model-invocable
  only.* It would keep the user surface to the CLI, which is a real preference, but it makes a skill
  that fails to trigger undiagnosable.
- ~~Does the method document (T-008) become the skill's spine, or a file the spine points at?~~
  **Answered** — [T-008](T-008-write-the-backend-neutral-method-document.md) *Specify → Decisions*
  **D1**: standalone document at `docs/METHOD.md`; this skill points at it. The rationale lives
  there, not here.

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
| 2026-08-07 | → specified | Invocation answered: both. Nothing else was outstanding, and the second question was already closed by T-008 D1. What now rests on this task is worth stating: T-028 made `docs/METHOD.md` tier 2, loaded when task work starts, and this skill is the loader — so T-047 waits on it, and the tiering is a decision rather than a working arrangement until it is built. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
