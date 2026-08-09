---
id: T-073
title: Correct the command surface local context still states
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-013, T-022]
work_package: none
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-073 — Correct the command surface local context still states

## 1. Specify

**Outcome**
`control/LOCAL-CONTEXT.md` states the command surface taskmd actually has, and the gitignored file is
brought inside whatever sweep keeps the rest of the project's statements true.

**Why this one**
Raised as **F-13** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. The file closes with:

> Run the check in `CLAUDE.md` *Publishing constraints*. It is a grep, deliberately — `docs/SCOPE.md`
> non-goal 11 keeps the CLI to `context`, `index` and `check`, and says anything else is grep.

Non-goal 11 was **amended on 2026-08-05** by [T-022](T-022-filtered-task-listing-for-scripts.md):
`list` is the fourth command, and the non-goal now excludes a query language rather than everything
beyond three commands. The identical sentence was corrected in `CLAUDE.md` and `.handoff/config.md` at
the time; this copy was missed. It is the last place in the tree that still states the superseded
surface.

**Why the miss happened, which is the more useful half.** The file is gitignored, so it is outside
`git ls-files`, outside the pre-publish check by construction, and outside `.handoff/config.md`'s
`reconcile_targets` — which names `tasks/`, `docs/*.md`, `CLAUDE.md` and itself. Every mechanism this
project has for keeping statements true resolves against the tracked tree. A quarantined file is
quarantined from the sweeps too.

**Why it still costs something.** No publishing risk — that is what gitignoring it buys, and
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md) settled it. But the file's stated
job is resumption context, and it is read by a session that has not yet read anything else. A stale
claim there is read early and trusted.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, which a superseded copy defeats regardless of whether it is
tracked.

**Scope**
- In: the sentence quoted above.
- In: the rest of `control/LOCAL-CONTEXT.md`, checked once against the current tree rather than only
  this line — the same reasoning that made T-027's review find a second copy fifty lines from the one
  it was fixing.
- In: whether the file joins `reconcile_targets`, so this class stops recurring.
- Out: what the file records and why it is quarantined, settled in T-013.
- Out: the pre-publish check, which correctly does not read gitignored files.
- Out: the entry about the throwaway repository, which
  [T-037](T-037-delete-the-throwaway-proof-repository.md) removes at its own step 4.

**Inputs**
`control/LOCAL-CONTEXT.md`, `.handoff/config.md` (`reconcile_targets`),
[T-022](T-022-filtered-task-listing-for-scripts.md) for the amendment,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-13.

**Acceptance criteria**
- [ ] The file names the command surface taskmd has
- [ ] Every other statement in it is checked against the current tree, and the ones found true are
      recorded as checked
- [ ] Nothing recorded there moves into the tracked tree — the quarantine is the point
- [ ] Whether the file is swept in future is decided and written down, either way

**Open questions**
- **Does a gitignored file belong in `reconcile_targets`?** Adding it closes the class that produced
  this finding. Against it: `reconcile_targets` is resolved against the working tree at sweep time and
  its whole documented virtue is being a pattern rather than a list, so naming one specific
  gitignored file is the enumeration that entry warns against. A pattern that covers `control/`
  without naming the file may be the answer. `plan` decides.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised as F-13 from the T-059 audit, clause 1. `low`/`xs` — no publishing risk, and the file is read early by a resuming session, which is what keeps it worth correcting. The transferable half is why it was missed: every mechanism this project has for keeping statements true resolves against the tracked tree, so a quarantined file is outside all of them. |
