---
id: T-138
title: Report a front-matter value that reads as a version
type: fix
status: proposed
phase: specify
parent: null
blocked_by: [T-137]
related: [T-100, T-106, T-136]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-12
updated: 2026-08-12
deliverables: []
---

# T-138 — Report a front-matter value that reads as a version

## 1. Specify

**Outcome**
`check` reports a front-matter value shaped like a version, so a project that labels its groupings
`v0.2` learns it on the next run rather than after its labels and its releases have come apart. The
task template and the shipped default stop pointing an adopter at a version in the first place.

**Why this one**
[T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) decided this and measured
the rule that carries it: 137 hits on this repository before the rename, 0 across 53 shipped
fixtures, and one false-positive class that the two estimate fields already exempt. The build is out
of that task's scope on purpose, so it is here. **Two independent projects reached the same defect**,
which is why it is the tool's to catch rather than each backlog's to remember.

**Scope**
- In: the check, its line, and a fixture proving the alarm — no existing fixture can serve, because
  all 53 are quiet (T-137 §3).
- In: the wording in [`_task-template.md`](_task-template.md) and the shipped default config that
  told an adopter the field holds *the release*.
- Out: the predicate, the exemption, the line granularity, the surface and the advisory semantics.
  All five are decided in T-137 §3 D1–D5 and are implemented here, not revisited.
- Out: a config key. T-137 D2, on T-106's price.
- Out: relabelling this repository, which is
  [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md).

**Inputs**
- [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) §3 — the five decisions
  and the two runs behind them.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) — the advisory
  line class this reuses, including why it has no off switch.

**Acceptance criteria**
- [ ] <written at specify>

**Open questions**
- <specify has not run; T-137 settled the mechanism, not this task's boundary>

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

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → proposed | Raised by [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md), whose scope put the build out so that the mechanism question could be settled without one. It carries no open mechanism question: the predicate, the exemption, the granularity and the semantics are all decided and measured there. **The owner's authorisation of 2026-08-12 covers T-136 and T-137 and does not reach this task** (METHOD §3.1), so it waits to be asked for. |
