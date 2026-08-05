---
id: T-010
title: Write the GitHub Issues binding
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-009]
related: [T-004]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-04
updated: 2026-08-04
deliverables: []
---

# T-010 — Write the GitHub Issues binding

## 1. Specify

**Outcome**
A binding that maps every taskmd concept onto native GitHub features, so a project on GitHub
Issues follows the identical method with no local task files — and a project moving there changes
its binding, not how it works.

**Requirements served**
R-13, R-14 (`docs/SCOPE.md`). Bounded by assumption **A3**: a binding document, not code.

**Why this one**
This is the requirement that proves the method/technical split is real rather than claimed. It is
also more tractable than expected — GitHub gained native sub-issues and issue dependencies, so two
of the three edge kinds map directly, and both derive their inverse exactly as taskmd does.

**Scope**
- In: the concept mapping; the three structural mismatches below; the "assumptions this binding
  makes" section; how a project declares it uses this backend.
- Out: any taskmd code that calls GitHub, and any migration of existing tasks into issues — both
  excluded by A3 and non-goal 8. The agent drives `gh`; the tool does not.

**The three mismatches this task exists to solve**

1. **Ids are assigned by the server.** Locally the next id is picked before the file is written;
   GitHub assigns `#N` on create and the create response may not carry it. Any id rule must
   tolerate "id unknown until created" — this constrains T-004, which is currently written
   local-only.
2. **There is no soft-link field.** `parent` maps to sub-issues and `blocked_by` to issue
   dependencies, but `related` has no native carrier. It must map to a cross-reference or a label,
   and the choice must not fabricate a stored inverse.
3. **Status is binary.** GitHub has open/closed plus a state reason; a richer vocabulary must live
   in labels or a Projects field. Whichever is chosen, it stays **one** home — the label and the
   Projects field must not both be authoritative.

**Inputs**
- `docs/SCOPE.md` §3B, and T-007 §3 for the mapping evidence already gathered
- Handoff `PROJECT_BOARD.md` — a working precedent: issues are the source, the board is a derived
  view auto-synced from `status:` labels, and cards are never dragged by hand
- GitHub documentation for sub-issues, issue dependencies, issue types and Projects — verify
  current limits rather than trusting this file (sub-issues were documented at 100 children and
  8 levels; dependencies at 50 per relationship)

**Acceptance criteria**
- [ ] Every concept in the method has a named GitHub carrier, or a stated reason it has none
- [ ] Each of the three mismatches above has a decided resolution with its rationale
- [ ] No taskmd concept maps to two authoritative carriers
- [ ] The "assumptions this binding makes" section is present and checkable in thirty seconds
- [ ] Proven on a real repository: one task walked through all four phases as an issue, including a
      dependency and a sub-issue, with the inverse edges confirmed to appear without being written
- [ ] The method document required no change to support this backend — if it did, that is a defect
      in T-008 and a child task

**Open questions**
- Labels or a Projects single-select for `phase` and `status`? Labels need no Projects board and
  work on any repo; a Projects field is tidier but adds setup and a token scope. — decide here.

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
| 2026-08-04 | → proposed | Raised by T-007 to carry R-14, the seamless local↔GitHub transition. |
