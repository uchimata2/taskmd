---
id: T-007
title: Define the project scope, goals and requirements
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-002, T-004, T-005]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - docs/SCOPE.md
---

# T-007 — Define the project scope, goals and requirements

## 1. Specify

**Outcome**
A numbered, testable requirement set with an explicit goal and — the part that actually does the
work — an explicit **non-goal** list, so scope creep is visible rather than arguable.

**Why this one**
`docs/BRIEF.md` is a good specification of *what to build and why*, with measured evidence, but it
states no goal, no numbered requirements and no boundary. Nothing in the repository could be used
to answer "is this in scope?". Six tasks were being worked against an unstated scope.

**Scope**
- In: goal, requirements, non-goals, constraints, definition of done, and the assumptions the
  requirements rest on.
- Out: how any requirement is met — that is the tasks' job. No design, no schema, no file formats.

**Inputs**
- The maintainer's stated goal and eight requirements (2026-08-04)
- `docs/BRIEF.md` — problem evidence, prior art, carried lessons
- Handoff (`bindings/`, `handoff.core.md`, `control/IMPROVEMENT-BRIEF.md`) — core/binding split,
  progressive disclosure, reconcile, the config-validation and binding-assumptions findings
- Crafted Legends (`.agents/docs/task-workflow.md`, `workflow/5a`–`5e`, `rationale.md`) — the
  delivery pipeline as actually run, computed task state, one-phase-per-request, lean ceremony
- GitHub — native sub-issues, issue dependencies, issue types, milestones, Projects

**Acceptance criteria**
- [ ] A goal statement that a stranger could judge the project against
- [ ] Requirements numbered, each one testable rather than aspirational
- [ ] Non-goals stated explicitly, not implied
- [ ] Every one of the maintainer's eight requirements traceable to a numbered requirement
- [ ] No fact restated from `docs/BRIEF.md`, `CLAUDE.md` or a task file

**Open questions**
- ~~Three assumptions (A1–A3 in `docs/SCOPE.md`) were taken rather than blocking the work.~~ —
  **closed 2026-08-04**: confirmed by the maintainer after a full session working with them. They
  are decisions now; `SCOPE.md` §6 says so, so no session re-raises them.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Study task management as practised in Handoff, Crafted Legends and GitHub | findings, §3 |
| 2 | Reconcile the eight stated requirements against the repository's current specs; surface contradictions | §3 |
| 3 | Write the goal, requirements, non-goals and definition of done | `docs/SCOPE.md` |
| 4 | Move the definition of done out of `docs/BRIEF.md` and leave a pointer | `docs/BRIEF.md` |
| 5 | Break the requirement gaps into tasks | T-008 … T-011 |

## 3. Implement

**Decisions & assumptions**

- **D1 — `docs/SCOPE.md` owns goal, requirements, non-goals and the definition of done;
  `docs/BRIEF.md` keeps the problem evidence, prior art and carried lessons.** Two documents only
  because they answer different questions ("what are we allowed to build?" vs "what do we know?").
  The definition of done moved out of the brief, which now points at it — one home, per R-1.
  — 2026-08-04
- **D2 — Requirement→task traceability is stored on the task, never in the scope doc.** Each task
  names the requirements it serves; a coverage view is derived. A mapping table inside `SCOPE.md`
  would be a second copy of the task list and would drift within days — the exact failure this
  plugin exists to delete. — 2026-08-04
- **A1 (assumption) — one implementation, in standard-library Python**, with the interpreter and
  repository root auto-discovered; bash and PowerShell appear only as thin launchers holding no
  logic, plus as languages a project may write its *own* hook commands in. Three parallel
  implementations of one command set would be three copies of one fact. — 2026-08-04
- **A2 (assumption) — the mandatory pipeline is four phases**, with verification as `implement`'s
  exit criterion and audit as a task *type* whose findings become child tasks, rather than six
  linear phases. This is what both reference projects converged on independently, and it keeps the
  mandatory path light enough for research, deck and training work. — 2026-08-04
- **A3 (assumption) — the GitHub backend ships as a binding document, not code, in v1.** The
  method and the mapping are proven; no taskmd code touches the network, so "runs on a clone with
  nothing installed" stays literally true. — 2026-08-04

**Findings worth recording (R-8 in practice)**

- **GitHub and Notion already store the forward edge and derive the inverse.** GitHub's issue
  dependencies expose `--blocked-by` / `--blocking` as two views of one relation; Notion's
  `Parent item` auto-fills the parent's `Sub-item`. The design rule is not a local-file quirk —
  it is what mature trackers do, which makes the GitHub mapping natural rather than a workaround.
- **GitHub covers two of the three edge kinds natively** (sub-issues for hierarchy, dependencies
  for `blocked_by`) and has **no soft-link field** — `related` must map to a cross-reference or a
  label. This is the one real gap in the mapping, and T-010 owns it.
- **Config errors surfacing mid-run is a known field failure** (Handoff F2): the adopter learns
  their config is wrong while trying to stop work. Became R-17.
- **A binding silently imposes its author's assumptions** (Handoff F1): `local-markdown-dir`
  states "the folder is the index", which is false for any project with a generated one — a
  handoff could be correct by the binding's rules while breaking the project. Became R-13's
  "assumptions this binding makes" clause.

**Outputs produced**
- [`docs/SCOPE.md`](../docs/SCOPE.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A goal statement that a stranger could judge the project against | pass | `docs/SCOPE.md` §1, with the two properties that make it falsifiable — token cost and no-install. |
| Requirements numbered, each one testable | pass | R-1 … R-24, grouped Method / Storage / Tool / Product. |
| Non-goals stated explicitly | pass | §4, eleven of them. |
| All eight stated requirements traceable | pass | §7 maps each of the maintainer's eight to the R-numbers carrying it. |
| No fact restated from BRIEF, CLAUDE.md or a task file | pass | Constraints point at `CLAUDE.md`; evidence points at `docs/BRIEF.md`; the schema decision points at T-001. |

**Child fix tasks raised**
- T-008, T-009, T-010, T-011 — the requirement gaps with no existing owner.
- T-012 — raised under R-8: linking T-004 and T-010 exposed that a soft edge is only visible from
  the end that stores it, so two-way visibility currently requires storing one fact twice.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Raised: the project had no scope or requirements document. |
| 2026-08-04 | → done | Scope written after studying Handoff, Crafted Legends and GitHub. Three assumptions (A1–A3) taken rather than blocking; revisable while T-008–T-011 are still `proposed`. |
