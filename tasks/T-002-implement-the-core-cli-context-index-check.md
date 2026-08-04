---
id: T-002
title: Implement the core CLI: context, index, check
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-001]
related: []
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-002 — Implement the core CLI: context, index, check

## 1. Specify

**Outcome**
A dependency-free CLI providing `context`, `index` and `check`, driven by the schema decision from T-001.

**Why this one**
These three carry the plugin's whole thesis: `context` is the token saving, `index` is the derived view that removes drift, `check` validates what is left hand-made. `reference/task.py` proves the behaviour — it is evidence, not code to lift.

**Acceptance criteria**
- [ ] Runs on a clone with no configuration and no dependencies
- [ ] `index` regenerates without touching hand-written regions
- [ ] `check` proven **failing** on every class of problem it claims to catch
- [ ] Output byte-identical across Windows, macOS and Linux (`newline` set explicitly)
- [ ] Console output survives a cp1252 terminal

**Open questions**
- Are `decisions` and `deliverables` core commands or config-declared derived views? — see brief

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
