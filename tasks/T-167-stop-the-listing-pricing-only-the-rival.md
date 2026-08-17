---
id: T-167
title: Stop the post-migration listing pricing only the rival skill
type: fix
status: cancelled
phase: specify
parent: null
blocked_by: []
related: [T-166, T-165, T-163, T-168]
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
  to prevent? Answered by the maintainer, 2026-08-17: stop here, the document is good enough.** The
  task is cancelled on that answer and the five mechanisms are accepted rather than deferred — see the
  Log for what that leaves standing, and what would justify re-opening it.

**What this task's cancellation does not decide**
The five mechanisms are accepted **as framing**. One of them is also a **factual** gap and does not
depend on this judgement: the survivor bullet *the skill that routes an agent through them* is the
only claim in the listing that is neither a measured output nor a pointer, which is the standard
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) set and
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) held itself to. That is
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s subject, and it
outlives this task rather than falling with it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- Not run — the task was cancelled at `specify`, so no decision was ever taken here.

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- Not run — the task was cancelled at `specify`, so it never reached `review`.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → cancelled | **The maintainer answered the open question with the option it was shaped to make cheap: *stop here, the document is good enough.*** Cancelled the same day it was raised, and that is the mechanism working rather than a waste — the task existed so that stopping could be a decision with a record instead of a thing that quietly did not happen. **What is being accepted, stated so nobody re-derives it:** the listing still argues mildly toward keeping taskmd, by five mechanisms an uninvolved reader named and [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 records in their own words. **What would justify re-opening this:** not another reading of the same document — two runs have each found a fresh layer, and a third would too, which is the reason to stop rather than a reason to continue. A new fact would: an adopter reporting that the listing pushed them, or [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) returning a number that makes the unpriced side material rather than merely absent. **The dependency edge on [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) was dropped to a soft link at the same time**, because a cancelled task holding a dependency makes the live one look like it gates something; the condition above is where that relationship now lives, and it is prose because it is conditional rather than a blocker. |
| 2026-08-17 | → proposed | Raised from [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md), carrying its one failed acceptance criterion. Raised rather than fixed there under the rule that created T-166 itself: **a repair made in the same breath as the measurement leaves no evidence the measurement happened**, and T-166 ran its reader once by an explicit decision so that a failing verdict would leave as a task instead of starting a retry loop. `high` — same reasoning as its parent, the listing's whole claim is that it lets someone decide. `s`: four of the five edits are small, and the fifth is one sentence that cannot be written yet. **Blocked by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)** rather than merged with it, because a measurement and an edit are different work and merging them is what would let the sentence be written before the number exists. The open question above is deliberately shaped so that stopping is an answer. |
