---
id: T-004
title: Settle the id scheme and the claimed scale ceiling
type: decision
status: proposed
phase: specify
parent: null
blocked_by: [T-001]
related: [T-002]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-004 — Settle the id scheme and the claimed scale ceiling

## 1. Specify

**Outcome**
A decided id format and a measured statement of how many tasks the tool handles well.

**Why this one**
The source used `T-NNN`, zero-padded, never reused, next id in the generated index. Fine at 17 files; `context` and `index` re-read everything on each run. Claiming a ceiling without measuring is the exact unverified-claim failure this project exists to avoid.

**Requirements served**
R-14, R-15, R-20 (`docs/SCOPE.md`).

**Acceptance criteria**
- [ ] ID format and width decided, with merge-conflict behaviour described
- [ ] Measured timing at 50, 500 and 5000 tasks
- [ ] The README states a supported scale that the measurement supports
- [ ] **The scheme tolerates ids assigned by the backend** — GitHub allocates `#N` on create and
      the create response may not carry it, so "id unknown until created" must be a supported
      state rather than an error (R-14; the mismatch is catalogued in T-010)

**Open questions**
- ~~Configurable prefix and width, or fixed?~~ — **answered by T-001 (D8): configurable**, via the
  `id_prefix` and `id_width` config keys. This task still owns the default values, the
  merge-conflict behaviour and the measured ceiling.

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
