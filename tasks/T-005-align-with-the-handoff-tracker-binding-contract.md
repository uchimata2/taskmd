---
id: T-005
title: Align with the handoff tracker-binding contract
type: research
status: specified
phase: specify
parent: null
blocked_by: [T-009]
related: [T-002]
work_package: none
owner: maintainer
business_value: medium
effort: m
created: 2026-08-04
updated: 2026-08-07
deliverables: []
---

# T-005 — Align with the handoff tracker-binding contract

## 1. Specify

**Outcome**
Either a contributed/updated `local-markdown-dir` binding, or a documented statement of how taskmd projects should configure handoff.

**Why this one**
The binding states *"the folder is the index"*, which is false for any project using a generated one — see the Handoff repo's improvement brief, F1. taskmd is exactly such a project, so it will hit this. Doing it after the binding changes avoids building against a contract about to move.

**Requirements served**
R-24 (`docs/SCOPE.md`).

**Two binding contracts, not one**
Kept distinct because they run in opposite directions, and conflating them is the easy mistake
here:

- **handoff's** contract (`find`/`read`/`create`/`update`/`reference`) lets handoff drive *a*
  tracker. This task makes taskmd be that tracker.
- **taskmd's own** contract (T-009) lets taskmd drive *a* backend — local files or GitHub Issues.

They may share vocabulary, and T-009 owns that decision. Hence the new blocker.

**Acceptance criteria**
- [ ] The handoff F1 outcome is known before this is designed
- [ ] A taskmd project can be driven by handoff with no hand-written workaround
- [ ] `tracker_lint` documented as the way the invariant is enforced
- [ ] Works for a taskmd project on **either** backend — a project on GitHub Issues must be
      resumable through handoff too, or the limitation is stated (R-14, R-24)
- [ ] The binding states the assumptions it makes about the adopting project — the F1 fix applied
      to taskmd's own contribution rather than only asked of others

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: ship a config recipe for v1, and propose the
  binding upstream after publishing.** R-24 asks for interoperation, not for adoption by another
  project: a recipe is verifiable inside this repository and blocks nothing, where an upstream
  contribution depends on someone else's review and would sit in T-006's path. *Rejected:
  contributing upstream now.* It is the better long-term shape — the handoff core resolves its
  `tracker` key to a file in its own `bindings/`, so a recipe alone is a binding that project cannot
  load — which is why it is deferred rather than dropped.
- **What criterion 1's F1 dependency now covers.** It stands, but the answer scopes it: the v1
  recipe does not wait on the F1 outcome; the upstream contribution does.

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
| 2026-08-07 | → specified | Answered: recipe for v1, upstream contribution deferred until after publishing. Recorded with the reason the rejected option is the better long-term shape rather than the wrong one — the handoff core loads a `tracker` binding from its own folder, so a recipe is not a substitute for one, only a thing that works without it. Criterion 1 is unchanged and now scoped: the recipe half does not wait on the F1 outcome, the contribution half does. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
