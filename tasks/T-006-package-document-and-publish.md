---
id: T-006
title: Package, document and publish
type: deliverable
status: specified
phase: specify
parent: null
blocked_by: [T-002, T-003, T-008, T-009, T-010, T-011, T-018]
related: [T-004]
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-07
deliverables: []
---

# T-006 — Package, document and publish

## 1. Specify

**Outcome**
An installable plugin with a README that only claims what has been demonstrated.

**Why this one**
A README written before the thing works becomes the unverified claim the whole project warns about. Written last, on purpose.

**Requirements served**
R-15, R-20, R-23 (`docs/SCOPE.md`). This task closes the definition of done, `SCOPE.md` §9.

**Acceptance criteria**
- [ ] Install instructions end with a command that proves it runs
- [ ] The measured `context` saving reproduced on a sample project and quoted
- [ ] No personal, client or machine data anywhere in the repository
- [ ] Installs from a clean clone on a machine that has never seen it
- [ ] The package ships the method document and **both** bindings, and the README states that
      changing backend changes the binding, not the method (R-13, R-14)
- [ ] The README claims a supported scale that T-004 measured, and nothing it did not
- [ ] Every non-goal in `SCOPE.md` §4 still holds at publish — checked, not assumed
- [ ] **Both** distribution shapes install from a clean clone and are each proven by a command that
      runs — the marketplace plugin and the plain skill package
      <br>*Added 2026-08-07 with the answer to the distribution question. The seven above predate it and
      are unchanged.*

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: both, with the marketplace plugin primary.**
  The tree is already a plugin and the marketplace is how it is found; the plain skill package is a
  subset of the same tree and is what someone not using the marketplace needs. *Rejected: the plugin
  alone.* Two shapes are two sets of install instructions and paths to keep true — which is the cost
  this answer accepts, and which the criterion added with it exists to hold.

**Why the new blockers**
`blocked_by` gained T-008, T-009, T-010 and T-011. The definition of done requires the method
document, both bindings implementing the same lifecycle, and a clone that runs with nothing
installed — publishing before those exist would ship a product that fails its own stated scope.

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
| 2026-08-07 | → specified | Answered: both shapes, plugin primary. One acceptance criterion added with the answer — both shapes install from a clean clone and are proven by a command — because shipping two distributions and testing one is how the second becomes stale, and the criteria named no shape at all. The seven that predate this are unchanged. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-05 | (no change) | `blocked_by` gained T-018: a tracked file carries a real absolute local path, which R-23 and §9 put inside this task's definition of done. |
