---
id: T-167
title: Stop the post-migration listing pricing only the rival skill
type: fix
status: proposed
phase: specify
parent: null
blocked_by: [T-168]
related: [T-166, T-165, T-163]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-167 — Stop the post-migration listing pricing only the rival skill

## 1. Specify

**Outcome**
The listing in
[`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
— *What taskmd still gives you here* — stops leaning toward keeping taskmd through the five
mechanisms a second uninvolved reader named, the load-bearing one being that it prices the overlap
against a rival skill and never prices keeping taskmd alone.

**Why this one**
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) removed the three mechanisms
[T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) found — confirmed removed
by a fresh reader who volunteered two of them as now correct — and that reader still answered *yes,
softly, toward keep*, on five mechanisms nobody had seen. They were invisible until the first layer
came off, which is what a second measurement is for. The five, and the reader's wording, are in
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 and are not restated here.

**The one that is not editorial.** Four of the five are wording, heading, column and placement. The
fifth is an absence: the document knows the unit of cost — the overlap paid on every session — and
spends it only against a hypothetical rival. It cannot spend it on itself until somebody measures
what keeping taskmd installed costs a project with no task folder, which is
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) and why this task
is blocked by it. Writing the sentence before the measurement exists would put back exactly the kind
of unevidenced claim
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) took out.

**Scope**
- In: the five mechanisms in
  [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the listing's own
  heading, the *What that costs you* column, the verb *survives*, the unpriced side of the overlap,
  and the section's placement at the end of the spec
- In: the unevidenced survivor claim — *the skill that routes an agent through them* — which is the
  same gap seen from the document's side
- Out: re-running the reader test. That is how this is judged and it is
  [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)'s shape; `review` needs
  a **new** reader, which `specify` must decide again rather than inherit
- Out: taking the measurement.
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) does that
- Out: anything the three earlier readers' repairs already settled. Undoing a repair to balance a new
  one is how a document oscillates

**Inputs**
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the five mechanisms and
  the reader's wording, and §4 for what the first repair is known to have achieved
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) — the number
  the fifth mechanism needs
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 — the per-claim measurement
  that must survive this repair as it survived the last

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Is a third reader still the test, or does repeated reader-testing become the tuning it was meant
  to prevent?** Two runs have now each found a fresh layer, which is either the method working or a
  document being polished against an unfalsifiable bar. **The maintainer answers, at `specify`** — and
  *stop here, the document is good enough* is an available answer that this task should make cheap to
  give.

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
| 2026-08-17 | → proposed | Raised from [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md), carrying its one failed acceptance criterion. Raised rather than fixed there under the rule that created T-166 itself: **a repair made in the same breath as the measurement leaves no evidence the measurement happened**, and T-166 ran its reader once by an explicit decision so that a failing verdict would leave as a task instead of starting a retry loop. `high` — same reasoning as its parent, the listing's whole claim is that it lets someone decide. `s`: four of the five edits are small, and the fifth is one sentence that cannot be written yet. **Blocked by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)** rather than merged with it, because a measurement and an edit are different work and merging them is what would let the sentence be written before the number exists. The open question above is deliberately shaped so that stopping is an answer. |
