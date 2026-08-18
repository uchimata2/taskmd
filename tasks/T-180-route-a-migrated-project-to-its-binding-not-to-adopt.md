---
id: T-180
title: Route a migrated project to its binding rather than to adopt.md
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-163, T-164, T-177]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-180 — Route a migrated project to its binding rather than to adopt.md

## 1. Specify

**Outcome**
A skill that sends a project whose task folder does not resolve to the document that helps it, in
the one case where it currently sends it to the document written for a project that has not
started.

**Why this one**
**`SKILL.md`'s load table has one row for this and it points the wrong way.** It reads: load
[`adopt.md`](../plugin/skills/taskmd/adopt.md) when "the project has no tasks yet, **or a command
reports its task folder missing**". Those two conditions have different answers. `adopt.md` is 92
lines about taking taskmd up and choosing a backend; it mentions bindings once and says nothing
about a project that has already migrated and whose commands now correctly refuse.

**The error message already does the right thing, which is why this is small and also why it is
worth doing.** [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) gave that
refusal a third possibility, and it is good — run against the fixture it says the commands do not
apply and names `id_width` as the reason. So the skill's table and the tool's own message currently
point in different directions on the same event, and the table is the one a session reads first.

**The whole cost of taskmd to such a project is the skill** — measured at 414 characters a session in
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md). If it routes
that project to the wrong document, the one thing installation buys is spent pointing away from the
binding, which is the thing that would have helped.

**Scope**
- In: the load-table row that fires on a missing task folder
- In: whether `adopt.md` should also cover the migrated case, or whether the row should split
- Out: the error message, which [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md)
  settled and which is not the defect here
- Out: growing tier 1. `SKILL.md`'s description is the budgeted part and this task must not touch
  it; the load table is in the body

**Inputs**
- `plugin/skills/taskmd/SKILL.md` — the load table, and the paragraph above it that already says a
  different backend's binding supplies the operations
- `plugin/skills/taskmd/adopt.md` — what it actually covers, which is the evidence for the split
- [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) — the message that gets this
  right, and the wording to stay consistent with

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Split the row, or widen `adopt.md`?** Splitting keeps each document about one thing and adds a
  row to a table that is loaded whenever the skill is; widening keeps the table at four rows and
  makes one document cover two situations. Both are cheap. **Decide at `specify`**, weighing the
  table's own weight, since it is read every time the skill is invoked.

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
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question. Small, and raised anyway because the skill is the *only* survivor a migrated project pays for and this is the one place it misdirects. Found by reading `SKILL.md` against `adopt.md` rather than by a failure — nothing reports it, and nothing could. **Not covered by any standing authorisation.** |
