---
id: T-008
title: Write the backend-neutral method document
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-007]
related: [T-003]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-008 — Write the backend-neutral method document

## 1. Specify

**Outcome**
One document that defines how work is tracked — lifecycle, edges, audit, when to ask — containing
**no instruction specific to any backend**. It is the plugin's shipped standard and the thing a
GitHub-based project and a Markdown-based project follow identically.

**Requirements served**
R-3, R-4, R-5, R-6, R-7, R-8, R-9, R-13, R-21, R-22 (`docs/SCOPE.md`).

**Why this one**
R-13 splits the method from the technical spec, and nothing implements the split yet. There is
also a live defect: `CLAUDE.md` points at `docs/TASK-WORKFLOW.md` and the CLI footer points at
`tasks/TASK-WORKFLOW.md`, and **neither file exists** — only `reference/TASK-WORKFLOW.md`, which is
one project's copy and names Unity, Notion and a client brief. `check` does not catch it because
they are plain-text mentions rather than links.

**Scope**
- In: the lifecycle and its exit criteria; the two edge kinds and when to use which; the audit
  mechanism (umbrella → child findings); one-phase-per-request; the ask-to-the-exit-criterion rule
  and discovery escalation; where each kind of fact lives.
- Out: field names, file layout, id format, folder contract, any command — all backend-specific
  (T-009, T-010) or already decided (T-001).

**Inputs**
- `docs/SCOPE.md` §3A — the requirements this document implements
- `reference/TASK-WORKFLOW.md` — the proven standard, to be generalised, not copied
- Crafted Legends `.agents/docs/task-workflow.md` + `workflow/5a`–`5e` — the same lifecycle run
  against a non-file backend, with the exit criteria and preflights that survived real use

**Acceptance criteria**
- [ ] Contains no field name, file path, id format or command — proven by reading it against a
      GitHub-only project and finding nothing that does not apply
- [ ] Every phase has a written exit criterion, so R-7 has something to measure "enough" against
- [ ] The audit mechanism is defined such that a finding cannot be fixed inline
- [ ] Reads sensibly for research, a deck and a training course — verified by walking one
      non-software example through all four phases
- [ ] Structured for progressive disclosure: a spine short enough to always load, details on demand
- [ ] `CLAUDE.md`, the CLI footer and the task template point at it, and every pointer resolves

**Open questions**
- Does the method document ship as the skill's spine, or does the skill point at it as a separate
  file? — decide with T-003, which owns the skill.

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
| 2026-08-04 | → proposed | Raised by T-007: R-13 requires the split, and the referenced workflow document does not exist. |
