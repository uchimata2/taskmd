---
id: T-026
title: Audit the whole project before the remaining build
type: analysis
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-003, T-006, T-010, T-025]
work_package: none
owner: maintainer
business_value: high
effort: l
created: 2026-08-05
updated: 2026-08-05
deliverables: []
---

# T-026 — Audit the whole project before the remaining build

## 1. Specify

**Outcome**
A recorded examination of every tracked file in this repository, with each finding written down at a
stated severity and each actionable one carried by its own child task — so the work that remains
(T-003, T-006, T-010) is built on a base that has been looked at rather than assumed.

**Requested by the maintainer, 2026-08-05**, verbatim, because the wording is the scope until
`specify` narrows it:

> a thorough audit on all project files, looking for stale info, potential inconsistency generating
> methods, contradictory feature, unnecessary complexity, performance issues, technical challenges,
> duplication, inefficient token usage, better out-of-the-box ideas for a feature, anything.

**Why now**
Three sessions have added a backend contract, a fourth command, two schema fields and two amendments
to `docs/SCOPE.md`'s non-goals. Amendments are the expensive kind of change: each one licenses
something a previous decision forbade, and every document that cited the old wording is a candidate
for having quietly become false. Two such drifts were already caught by hand this session — a
`.handoff/config.md` and a `CLAUDE.md` still claiming three commands — which is evidence that the
sweep is worth doing deliberately rather than opportunistically.

The project is also close to the point where auditing gets harder: T-003 writes the skill and T-006
publishes. A finding raised after publication costs a release.

**Requirements served**
None directly — an audit examines conformance to the requirements rather than adding to them. Its
findings will cite them.

**Scope**
- In: every tracked file. Documents (`CLAUDE.md`, `docs/`, `tasks/`), code (`taskmd/`), tests and
  fixtures (`tests/`), configuration, and the generated index.
- In: the seven concerns the maintainer named, plus "anything" — which is deliberately open, and is
  why the finding threshold below matters more than usual.
- Out: **fixing anything**. METHOD §5 and [`audit`](../docs/method/audit.md) — a finding is never
  fixed where it is found, and the one exception is a finding that makes continuing impossible.
- Out: `reference/`, which is prior art from another project and is not this repository's to
  correct.
- Out: re-litigating settled decisions as such. `docs/SCOPE.md` §6 assumptions and the amendments to
  non-goals 1 and 11 were taken deliberately; an audit may find a *consequence* of one that was not
  foreseen, which is a finding, but "I would have decided differently" is not.

**Inputs**
- [`docs/method/audit.md`](../docs/method/audit.md) — the procedure, including why the
  no-inline-fix rule is the whole product
- `docs/SCOPE.md` — the requirements findings will cite, the non-goals, and §1's three properties
- `CLAUDE.md` — the publishing, portability and verification constraints
- `python -m taskmd list --json` — the whole graph, in one call, without reading 26 files

**Acceptance criteria**
- [ ] The finding threshold is written down **before** looking, and every finding is judged against
      it — without one, an audit reports whatever its author happens to dislike and cannot be
      compared to the next one
- [ ] Every area in scope is recorded as examined, including the areas that produced **no** finding
      — that half is what distinguishes "checked and clean" from "not looked at"
- [ ] Each finding carries a severity and enough detail for someone who was not present to act on it
- [ ] Each actionable finding has its own child task pointing back here; each non-actionable one
      stays recorded with the reason it needs no action
- [ ] Nothing is fixed in place — falsified by any commit from this task that changes behaviour or
      wording outside this task's own record
- [ ] The umbrella closes only when every child is resolved or dropped with a reason

**Open questions**
- **What is the finding threshold?** — maintainer, and it must be answered before `specify` can
  close, because it decides what the audit is. "Anything" is a request, not a threshold: applied
  literally it produces a list nobody acts on, which is the failure `audit.md` step 1 names.
  *Recommendation:* a finding is **anything that would cost a later reader or session real work** —
  a statement that is false or stale, two places that must be updated together, a decision whose
  consequence contradicts a stated goal, or a cost paid on every turn (tokens, an always-loaded
  file, a step someone must remember). Explicitly below the line: style, wording preference, and
  ideas for features nobody asked for — except where the "out-of-the-box idea" is *cheaper* than
  what exists, which is a simplification finding rather than a proposal.
- **Does the audit rank findings by the project's own ordering rule?** The two estimate fields exist
  now, so each child task will carry them. Worth deciding whether the umbrella also reports the
  order, since that is the first real use of `list` on tasks nobody has hand-sorted.

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
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Requested by the maintainer for the next session. Raised as an umbrella task rather than carried in the handoff, because an audit is a task type (METHOD §5) and its scope is durable content — a handoff points, it does not store. The request's wording is quoted intact so `specify` narrows it deliberately rather than by paraphrase, and the threshold it lacks is the first open question. |
