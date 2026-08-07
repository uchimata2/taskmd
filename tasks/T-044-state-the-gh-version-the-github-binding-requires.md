---
id: T-044
title: State the gh version the GitHub binding requires
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-010, T-042]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-044 — State the gh version the GitHub binding requires

## 1. Specify

**Outcome**
An adopter can tell, before following the binding, whether the `gh` they have is new enough — and
the answer rests on something that was tried rather than on a number someone thought looked safe.

**Why this one**
`docs/bindings/github-issues.md` assumption 4 says what must be true of the *repository* — issues
enabled, sub-issues and dependencies available, a token with `repo` scope. It says nothing about the
CLI, and the binding leans on flags that are not old:

| Operation | Flag it depends on |
| :--- | :--- |
| create | `--parent`, `--blocked-by` |
| update | `--add-sub-issue`, `--add-blocked-by`, `--remove-parent` |
| update | `--template '{{.body}}'`, which T-042 made load-bearing for the byte-identical guarantee |
| read, enumerate | the `parent`, `subIssues`, `blockedBy`, `blocking` JSON fields |

Every one of those was exercised on exactly one version, `gh` 2.96.0, and the binding presents them
as simply available. An adopter on an older CLI does not get a clear refusal from the binding; they
get whatever `gh` says about an unrecognised flag, at the point where they are trying to follow a
document that told them this works. That is BINDING §4's "setup that is obvious to the binding's
author and invisible to everyone else", and it is R-17's failure shape too — a configuration problem
surfacing inside the work rather than before it.

**Scope**
- In: establishing a floor and writing it into the assumptions section, with what it was established
  against. Whether the floor is one version for the whole binding or differs per operation.
- Out: making anything work on older versions, and any fallback path for a CLI that lacks a flag.
  The binding states limits rather than working around them (BINDING §6.4); if an old CLI cannot do
  this, the honest answer is the floor.

**Inputs**
- `docs/bindings/github-issues.md` — assumption 4, and every command in *Operations*
- T-042 §3, which made `--template` load-bearing, and T-010 §3's capability table
- `gh`'s own release history, for when each flag landed

**Acceptance criteria**
- [ ] The binding states a `gh` version, in the assumptions section, phrased as something an adopter
      checks about their own machine
- [ ] The number is justified by evidence naming where each flag came from — not by the version that
      happened to be installed when the binding was written
- [ ] An adopter below the floor learns it from the binding rather than from a failed command,
      checked by reading the assumptions as someone on an old CLI would
- [ ] If the flags landed in different releases, the binding states the highest and says so, rather
      than listing a floor per operation that nobody will cross-reference mid-task

**Open questions**
- Is the floor discoverable without installing old versions? `gh`'s changelog should date each flag,
  which would settle it from evidence without a matrix of installs. If it will not, say so and state
  the floor as "verified at 2.96.0, earlier untested" — an honest bound beats a guessed one, and the
  criteria are written to accept that answer. — decide during the work.

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
| 2026-08-07 | → proposed | Raised by T-042's last plan step, which asked only whether the fix added a tool. It did not — but answering that exposed that the binding has never named a version for the tool it already required. Kept out of T-042, whose scope is the `update` operation, while this concerns every operation and the assumptions section. |
