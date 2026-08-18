---
id: T-178
title: Give the GitHub binding a standing verification, not only a migration-day one
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-108, T-177, T-041]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-178 — Give the GitHub binding a standing verification, not only a migration-day one

## 1. Specify

**Outcome**
A procedure in the GitHub Issues binding that a project can run at any time to check its own issue
backlog — the standing counterpart of the migration-day *Verify* that binding already carries.

**Why this one**
**There is one verification in that binding and it runs once.**
[T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) built a real one —
165 tasks to 165 issues, five checks, and three recorded failing states including a rule that was
wrong when first written. It compares a source against a destination, so it can only run on the day
there is a source. The day after a migration, nothing checks anything again, ever.

**The gap this leaves is silent data loss, not degraded convenience.** The binding's own *update*
rules say it plainly: `related` lives in the property block and nowhere else on this backend, there
is no far end holding a copy and no derived view that can notice one has gone, a partial body
rewrite deletes it — and **`gh` exits 0 for the destructive edit exactly as for the correct one**.
On the local backend `check` catches a dangling reference. Here nothing does. A warning in prose is
not a control.

**It belongs in the binding and not in the tool**, and that is settled rather than open: non-goal 5
keeps every network call out of the core, and says anything remote is the agent's job through its
own tools. The migration *Verify* is already built that way, so this follows a shape that has been
walked on a live repository rather than inventing one.

**Scope**
- In: a procedure an agent can run against a live issue backlog, checking what the local `check`
  checks and this backend can still answer — references resolving, vocabularies, edges present in
  both directions, and `related` surviving
- In: making it fail first, on a deliberately broken issue, before it is allowed to pass. That is
  this repository's rule and it is the reason the migration verification is trustworthy
- Out: putting any of it in the CLI. Non-goal 5, and it is not a close call
- Out: the local-Markdown binding, which has `check` and needs nothing
- Out: continuous or scheduled running. Non-goal 10, and a procedure is what is being asked for

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Operations* for what a write can destroy,
  and *Verify — and make it fail first* for the shape and the standard
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the three
  failing states the migration verification was made to produce, including `gh` exiting 0 on the
  destructive edit
- [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) — the body-rewrite rule proven by
  being made to fail

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**How much of `check` can this backend actually answer, and is the honest answer worth
  shipping?** Some of the 17 checks have no meaning here — a stale index cannot exist where the issue
  list *is* the index. **Answer at `specify` by walking the list of checks against the backend**, so
  the procedure ships with a stated coverage rather than an implied one; a verification whose reach
  nobody wrote down is the failure this repository keeps re-learning.~~ **Answered by the owner on
  2026-08-19: walk all seventeen, and the coverage belongs to whichever backend is in use rather
  than to GitHub** — see the Log row of that date.

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
| 2026-08-19 | (no change) | **The open question is answered by the owner: walk all seventeen checks first — and the outcome must not be GitHub-shaped.** Asked in the backlog-wide round of 2026-08-19. The coverage statement ships with the procedure rather than being implied, for the reason §1 gives: a verification whose reach nobody wrote down is the failure this repository keeps re-learning. *Rejected: shipping the procedure without the coverage list*, which is faster and turns a green result into a false assurance. **The answer widens the outcome, and the widening is the owner's own words**: today the backend is GitHub, tomorrow it may be Notion or another service, so what ships must be flexible — the coverage belongs to whichever backend is in use, declared per binding, rather than being seventeen rows written once about GitHub. `plugin/skills/taskmd/docs/BINDING.md` is the contract that would carry that, so `specify` judges whether the generic half is in scope here or is a sibling task, and says which. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about whether taskmd is prepared to keep providing controls after a migration. The honest answer was no on the enforcing side, and this is the sharpest instance: **a documented path to unrecoverable loss of every soft edge, with a zero exit code and no detector**. Shaped as a binding procedure rather than a tool feature because `docs/SCOPE.md` §4 non-goal 5 settles that, and because the migration verification beside it is already built that way and was proven on a live repository. **Not covered by any standing authorisation.** |
