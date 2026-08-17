---
id: T-168
title: Price what keeping taskmd installed costs a project that has no tasks folder
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-166, T-167]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-168 — Price what keeping taskmd installed costs a project that has no tasks folder

## 1. Specify

**Outcome**
A measured answer to two questions about a project that has migrated its backlog away and has no task
folder left: **does the skill still fire**, and **what does having it installed cost per session** —
in the same units the rest of this repository measures context in, taken by running something rather
than by reasoning about the harness.

**Why this one**
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 put the edited migration
listing in front of an uninvolved reader. Asked what missing fact would most change their
recommendation, they named this one, and their argument for why it is decisive is the part worth
keeping: the document quotes `gh` versions, task counts, byte deltas and exit codes, and **the single
claim carrying the whole installation decision is the only sentence in it with no source** — *the
skill that routes an agent through them*. Three of the four survivors are documents, which need
nothing installed. The fourth is the only thing installation buys, and nobody has measured it.

**It is probably already half-answered, and that is the first move.** `tests/test_budget.py` measures
tier 1 in characters and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) measured
what a session is handed unasked. Whether either covers a project with **no task folder** is the
open part. Read the shipped artefact before building anything — a gap this repository has already
shipped an answer to has cost a round trip before.

**Scope**
- In: whether the skill is served, and whether it triggers, in a project with no task folder and no
  local task config
- In: what the install costs a session there, measured, with the command that produced the number
- In: whether the existing budget test and
  [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) already answer either half
- Out: editing the listing. That is
  [T-167](T-167-stop-the-listing-pricing-only-the-rival.md), which this blocks
- Out: changing what the skill does in that situation. If the measurement argues for a change, it is
  its own task

**Inputs**
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the reader's argument
  for why this gap is decisive
- `tests/test_budget.py` and [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) —
  what is already measured, and in what units
- `tests/fixtures/migrated-away/` — a project shaped the way this question is about

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Can a session measure this about itself?** Memory says an instruction file's effect cannot be
  observed from inside the session that wrote it, and a spawned subagent has been the instrument
  before. Whether that generalises to *is this skill served here* decides whether the answer is
  measurable at all or only arguable. **Answer at `specify`, by trying it.**

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
| 2026-08-17 | → proposed | Raised from [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3, where an uninvolved reader named it as the fact that would most change their recommendation. Raised separately from [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) because it is a **measurement**, not an edit: the listing cannot price keeping taskmd alone until somebody knows the price, and writing the sentence first would put an unevidenced claim into the one place this repository has just finished removing them from. `high` — it is the load-bearing claim of the whole listing and currently the only unsourced one. **Not covered by the authorisation of 2026-08-17**, which named [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) and excluded what it raises. |
