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
business_value: medium
effort: s
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
- **Criterion 3 cannot be met by this task as written, and it is circular.** *"The README states a
  supported scale"* needs a README, which [T-006](T-006-package-document-and-publish.md) step 5
  writes — and T-006 is `blocked_by` this task. So each waits on the other. Noticed 2026-08-09 while
  handing this over, and left as a question rather than resolved unilaterally because the answer
  changes what closing means. The shape that worked twice this week is to **split the fact from its
  publication**: this task measures and states the ceiling in its own record, T-006 step 4 already
  says the README claims *"whatever T-004 measured and nothing past it"*, and criterion 3 becomes a
  claim about the measurement rather than about a document that does not exist yet.
  [T-079](T-079-humanize-the-human-facing-documents-before-publishing.md) is the precedent, and
  [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md) is what it cost to notice the same
  circularity late. Decide this in `specify`, before planning any measurement.

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
| 2026-08-09 | (no change) | Handed to a fresh session with the full lifecycle authorised by the maintainer. One question added before it starts: criterion 3 asks the README to state the ceiling, the README does not exist, and T-006 — which writes it — is blocked by this task, so the two wait on each other. That is the same circularity T-079 hit and T-081 had to repair, found here before any work was planned against it. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
