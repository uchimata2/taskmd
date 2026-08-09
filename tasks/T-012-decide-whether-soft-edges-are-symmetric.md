---
id: T-012
title: Decide whether soft edges are symmetric
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-001, T-009]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - plugin/skills/taskmd/taskmd/schema.py
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - tests/test_schema.py
---

# T-012 — Decide whether soft edges are symmetric

## 1. Specify

**Outcome**
A decision on whether a `soft` edge (`related`) is visible from both ends, and if so how — with
the loader and the method updated to match.

**Requirements served**
R-1, R-2 (`docs/SCOPE.md`).

**Why this one**
Found while linking T-004 and T-010. T-001 defined `soft` as *a list with no inverse*. That makes
a soft link **one-directional in display**: T-010 lists T-004 as related, but someone reading
T-004 sees nothing. The only way to see it from both ends today is to write the edge in both
files — which is one fact stored twice, the exact thing R-1 forbids. So the current design quietly
forces a violation, or quietly hides half the graph.

The evidence from other trackers points one way: GitHub cross-references appear on both timelines,
and Notion's `Related item` relation is explicitly bidirectional. Neither asks you to write it
twice.

**Scope**
- In: the semantics of the `soft` kind; whether `derive()` computes a symmetric closure; what the
  config declares; how `context` displays it; the effect on the two bindings.
- Out: `hierarchy` and `dependency` — both already have real inverses and are unaffected.

**Inputs**
- `taskmd/schema.py` — `EDGE_KINDS`, `derive()`, and the validator rule that a soft edge may not
  name a `Derives` value
- `taskmd/defaults/config.md` — the `## Edges` table
- T-001 §3 D5 and D7 — the decisions this refines

**Options**
1. **Symmetric closure.** A soft edge is stored on one side and appears on both, derived under the
   same name. Matches GitHub and Notion; keeps one home; the config's `Derives` column stays `-`
   because the inverse has no separate name.
2. **Named inverse.** `related → related_from`, like the other two kinds. Explicit, but invents a
   direction users do not think in, and the name will read oddly in every view.
3. **Leave it one-directional.** Cheapest, and honest about being a display convention rather than
   a graph edge — but the method must then say plainly: *write it on the task that benefits from
   seeing it, and accept the other end is blind*.

**Acceptance criteria**
- [ ] One option chosen, with the reason recorded
- [ ] If symmetric: `derive()` computes it, and a test proves the edge is visible from the end that
      does **not** store it
- [ ] A test proves the same fact is never written twice to achieve two-way visibility
- [ ] The method document (T-008) states the chosen semantics in one sentence a user can act on

**Open questions**
- If symmetric, should `check` warn when both sides store the same soft edge? It is harmless but is
  a duplicate, and duplicates are what this project exists to remove.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**The decision: option 1 — symmetric closure.**

**Decisions & assumptions**

- **D1 — A soft edge is symmetric: stored once, derived under its own name, visible from both
  ends.** The requirement, set by the maintainer, is that *whichever task you open you see every
  link it has*. Deriving the inverse delivers that from a single stored edge. — 2026-08-04
- **D2 — Storing the link on both tasks is explicitly allowed, and collapses to one entry.**
  Per the maintainer: a two-way reference naturally lives in two places, and that is not a defect.
  So this is **tolerated, not rejected** — no validator error, no warning. The open question about
  `check` warning on a both-sides link is closed as *no*: warning about a legitimate way to write a
  link would be the tool arguing with the user over something with no consequence. Writing one side
  is merely sufficient, not mandatory. — 2026-08-04
- **D3 — `Task.links(name)` is the accessor every view uses.** It merges what the task stores with
  what was derived, de-duplicates, and drops self-links, so no view has to know which side of a
  link it is looking at. `Task.edges` remains the untouched record of what is literally written in
  the file. — 2026-08-04
- **D4 — Named inverses go through the same accessor.** `links("children")` and `links("blocks")`
  work identically, so a view needs one code path rather than one per edge kind. — 2026-08-04
- **D5 — A self-link resolves to nothing** and a link to a non-existent task is ignored by the
  derivation. Reporting either is `check`'s job (T-002), not the loader's. — 2026-08-04
- **Rejected — option 2, a named inverse (`related_from`).** It invents a direction users do not
  think in and reads badly in every view. **Rejected — option 3, leave it one-directional.** It
  fails the stated requirement outright.

**Outputs produced**
- [`taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py) — symmetric derivation, `Task.links()`, self-link guard
- [`taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — the `soft` row and its explanation
- [`tests/test_schema.py`](../tests/test_schema.py) — six tests covering both ends and both writings

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One option chosen, with the reason recorded | pass | Option 1, D1–D5 above. |
| If symmetric: a test proves the edge is visible from the end that does not store it | pass | `test_a_soft_edge_is_visible_from_the_end_that_does_not_store_it`, and on the real case `test_this_repositorys_own_soft_links_resolve_both_ways` — T-010 stores `related: [T-004]`, T-004 stores nothing about it and still sees it. |
| A test proves the same fact is never written twice to achieve two-way visibility | pass | `test_one_stored_side_is_enough`. Its companion `test_both_sides_stored_collapses_to_one_entry` proves writing both is also fine — the point is that it is optional, not forbidden. |
| The method document states the chosen semantics in one sentence | carried to T-008 | The method document does not exist yet; T-008 owns it and this is in its scope. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Discovered during T-007 while linking T-004 and T-010: two-way visibility of a soft edge currently requires storing the fact twice. |
| 2026-08-04 | → done | Maintainer set the requirement — every task shows all its links, inverse included — and confirmed a two-way reference living in two places is not duplication. Implemented as symmetric derivation with both-sides tolerated. Amends T-001 D5. |
