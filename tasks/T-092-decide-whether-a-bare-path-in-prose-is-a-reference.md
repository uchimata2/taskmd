---
id: T-092
title: Decide whether a bare path in prose is a reference check must resolve
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-093, T-094, T-095, T-034]
work_package: v0.2
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-092 — Decide whether a bare path in prose is a reference check must resolve

## 1. Specify

**Outcome**
A project is told whether `check` validates a path written as prose, and if it does, the rule that
decides what counts — so a project retiring its own link checker knows what it is giving up before
it deletes anything.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`) after migrating a 61-task project
off a mature bespoke checker onto taskmd 0.1.1. Reproduced here on a two-file throwaway project: a
task naming one missing document as a Markdown link and another as a bare path in prose produces

```
BROKEN LINK   tasks/T-001-x.md -> also-gone.md

1 problem(s) over 1 task(s)
```

— one problem, not two. `LINK` matches Markdown link syntax only, so the prose path is not a
reference as far as `check` is concerned. In that project it is not an edge case: it validates
around a thousand document pointers and a large share are bare, **because tools print them into
fenced blocks**.

**Why this is an adoption hazard, not a missing feature.** The migration nearly deleted that
project's checker on the strength of the two tools' command lists matching — `context`, `index`,
`check` on both sides. The lists match and the coverage does not, and nothing says so. That framing
is the reporting project's and it is the part worth keeping: a project that adopts taskmd and retires
its own checker loses this silently.

**This repository would not have noticed.** Its own prose cites paths in backticks constantly, and
`check` has never looked at one — which is also the shape of the defect
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) found in the leak check, where
the thing that read none of the files it was aimed at printed nothing and looked like success.

**Requirements served**
R-16, and R-13 in the sense that a reference that resolves is what the validator is for.

**Scope**
- In: whether a path-shaped token in prose is a reference at all. **This is the decision**; the
  mechanism is downstream of it.
- In: if yes, the rule that separates a pointer from a path merely being discussed. The reporting
  project's rule is that the token's first segment must be a real directory in the project, kept in
  a function it named `points_into_repo`.
- In: what a false positive costs here. `CLAUDE.md` already argues, for the leak check, that a check
  which cries wolf gets ignored — quoting another project's layout in prose is the obvious class.
- Out: section references, which are [T-093](T-093-decide-whether-check-resolves-a-section-reference.md).
- Out: whether it is opt-in or always on, until the first question is answered.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `LINK` and `check_links`.
- The reporting project's `tools/docs/refcheck.py`, offered MIT as a working reference.
- `CLAUDE.md` *The pre-publish check*, for the crying-wolf argument and the three deliberate limits.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If it is in: a fixture holds a dead bare path and `check` reports it, shown failing first
- [ ] If it is in: a fixture holds a path-shaped token that must **not** be reported, so the
      false-positive boundary is proven rather than asserted
- [ ] If it is out: the adopter-facing documentation says what `check` does not look at, so the next
      project to retire its own checker is told

**Open questions**
- **In or out.** Turning it on makes `check` meaningfully stronger and risks a class of false positive
  this project has argued is worse than a narrow check. Leaving it out is defensible only if the gap
  is documented, because the cost falls on adopters rather than here. The maintainer's.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised from a real migration rather than from review: the deck-building sibling moved 61 tasks off its own checker onto taskmd 0.1.1 and measured what that would cost before doing it. Reproduced here on a throwaway project — a dead bare path in prose is invisible, a dead Markdown link is caught, and `check` reports one problem where two exist. `high` because the loss is silent and the adoption path invites it: the two tools' command lists match and their coverage does not. |
