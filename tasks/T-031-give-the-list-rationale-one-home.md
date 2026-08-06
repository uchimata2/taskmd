---
id: T-031
title: Give the list rationale one home
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-022, T-027]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-031 — Give the list rationale one home

## 1. Specify

**Outcome**
The reason `list` exists — that grep cannot answer these questions because a derived edge is stored
nowhere — is written once, and the other places point at it.

**Why this one**
Raised as **F-5** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clause 2. The same argument, in the same words, appears in four non-task homes:

| File | Line |
| :--- | ---: |
| `docs/SCOPE.md` — non-goal 11's amendment | 152 |
| `docs/BRIEF.md` — *Commands* | 89 |
| `taskmd/cli.py` — module docstring | 12 |
| `taskmd/cli.py` — `cmd_list` docstring | 477 |

Two of them are in the same file. The phrasing is close enough that all four would have to be
revised together if the argument were ever refined — which is clause 2 exactly, and which is what
makes this a finding rather than a matter of taste.

**Task records are not copies and are out of scope.**
[T-022](T-022-filtered-task-listing-for-scripts.md) states the argument because that task is where
it was made, and [T-002](T-002-implement-the-core-cli-context-index-check.md) states an earlier
version because that is the record of what was true then. A task record is a dated account of a
decision, not a live claim to keep in step; rewriting one to match a later document would destroy
the history the method exists to keep.

**Requirements served**
R-1 (`docs/SCOPE.md`); §2 principle 3, *point, don't restate*.

**Scope**
- In: the four live homes listed above.
- Out: `tasks/`, for the reason above.
- Out: the argument itself, which is settled and correct.
- Out: `CLAUDE.md`'s statement of the design rule — that is a different fact and is
  [T-027](T-027-give-the-design-rule-one-home.md)'s.

**Inputs**
`docs/SCOPE.md` non-goal 11, `docs/BRIEF.md` §*Commands*, `taskmd/cli.py`,
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-5.

**Acceptance criteria**
- [ ] The argument is written in full in one file; the others carry a pointer of a line or less
- [ ] A grep for its distinctive phrasing returns one hit outside `tasks/`
- [ ] Both `taskmd/cli.py` docstrings still say what their reader needs at that point — the module
      docstring's job is "what is this file", `cmd_list`'s is "what does this function do", and
      neither is served by silence
- [ ] Nothing in `docs/SCOPE.md` non-goal 11 that is *not* this argument is touched; the amendment's
      carve-out wording is load-bearing and was settled in T-022

**Open questions**
- Which is the one home? `docs/SCOPE.md` non-goal 11 is the natural candidate, since the argument
  exists to justify an amendment to that non-goal, and the code and the brief are both downstream of
  it. — maintainer. Affects only where the pointer aims, so it does not block this phase.

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
| 2026-08-05 | → proposed | Raised as F-5 from the T-026 audit, clause 2. Four live homes located by grep, two of them in one file. Task records deliberately excluded — a dated record of a decision is not a copy to keep in step. |
