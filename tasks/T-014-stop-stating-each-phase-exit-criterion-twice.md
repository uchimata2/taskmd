---
id: T-014
title: Stop stating each phase exit criterion twice
type: fix
status: done
phase: review
parent: T-008
blocked_by: []
related: [T-015]
work_package: v0.1
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - plugin/skills/taskmd/docs/METHOD.md
  - plugin/skills/taskmd/docs/method/specify.md
  - plugin/skills/taskmd/docs/method/plan.md
  - plugin/skills/taskmd/docs/method/implement.md
  - plugin/skills/taskmd/docs/method/review.md
---

# T-014 — Stop stating each phase exit criterion twice

## 1. Specify

**Outcome**
Each phase's exit criterion is written in exactly one place.

**Requirements served**
R-1 (`docs/SCOPE.md`); `CLAUDE.md` *The one design rule*.

**Why this one**
Found reviewing [T-008](T-008-write-the-backend-neutral-method-document.md). All four exit criteria
are stated **verbatim twice** — in `docs/METHOD.md` §2's table and again in the header of each phase
file:

| Fact | Copy A | Copy B |
| :--- | :--- | :--- |
| specify's exit criterion | `docs/METHOD.md:34` | `docs/method/specify.md:4` |
| plan's | `docs/METHOD.md:35` | `docs/method/plan.md:4` |
| implement's | `docs/METHOD.md:36` | `docs/method/implement.md:4` |
| review's | `docs/METHOD.md:37` | `docs/method/review.md:4` |

This is the exact failure the plugin exists to remove, in the document that defines the rule. It is
also load-bearing: R-7 measures "enough detail" against the exit criterion, so two copies that drift
give two different answers to "am I finished?" — and nothing would report the disagreement.

Neither copy is obviously the wrong one, which is why this is a task and not an edit. The spine
needs the criteria to make the lifecycle table meaningful at a glance; the phase file needs them so
a reader who loaded only that file knows when to stop.

**Scope**
- In: deciding which copy is authoritative and removing the other, or replacing one with a pointer.
- Out: the *phase names* and *what happens* column — those are summary, not the same fact.

**Acceptance criteria**
- [ ] Each exit criterion appears once; `grep` for its wording returns one hit per phase
- [ ] A reader who loads only a phase file can still tell when that phase is finished
- [ ] The spine's lifecycle table is still readable as a table without opening five files
- [ ] No new fact is introduced that the other copy would have to mirror

**Open questions**
- ~~Which way round?~~ **Answered — the spine keeps them** (see *Decisions*).

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide which copy is authoritative. | a decision in §3 |
| 2 | Replace the losing copy with a pointer. | the four phase files |
| 3 | Sweep for third copies — the *Leaving this phase* sections paraphrase the same fact. | the four phase files |
| 4 | Prove one hit per criterion. | `grep` output in §4 |

## 3. Implement

**Decisions & assumptions**
- **The spine keeps the exit criteria; the phase files point up** (2026-08-04). The open question
  assumed a trade-off that does not exist: **the spine is loaded on every turn by definition**, so a
  phase file pointing at it costs the reader nothing — there is no file to go and open. Pointing the
  other way would have cost something, because the spine's lifecycle table would stop being readable
  as a table without opening five files. So the direction that also shrinks the spine is the one that
  makes the spine useless, and the cheap direction is the correct one.
- **The *Leaving this phase* sections were third copies** (2026-08-04). Not flagged when this task
  was raised: three of the four closed by paraphrasing the exit criterion ("The criteria are written
  and the owner has agreed them"). Paraphrase drifts more quietly than a verbatim copy, because it
  never looks like a duplicate. They now carry only what is genuinely theirs — `specify`'s "nothing
  else has started", and the handoff to the next phase.

**Outputs produced**
- `docs/METHOD.md` §2 — sole home of all four exit criteria
- `docs/method/specify.md`, `plan.md`, `implement.md`, `review.md` — headers point at §2; closing
  sections no longer paraphrase

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each exit criterion appears once | met | One hit each, all in the spine: `METHOD.md:31` (specify), `:32` (plan), `:33` (implement), `:34` (review). Case-insensitive search across all seven method files. |
| A reader who loads only a phase file can still tell when the phase is finished | met | The spine is always loaded, so §2 is already in hand; each phase header names it explicitly rather than assuming it. |
| The spine's lifecycle table is still readable without opening five files | met | The *Exit criterion* column is intact — this is the copy that was kept, for exactly this reason. |
| No new fact introduced that the other copy would have to mirror | met | The phase headers gained a pointer, not a statement. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → done | Worked with T-015 at the maintainer's request. Spine keeps the criteria, phase files point up — the open question dissolved once it was noticed that the spine is always loaded. A third layer of copies (the *Leaving this phase* paraphrases) was found and removed. |
| 2026-08-04 | → proposed | Raised by T-008's review. Beyond T-008's criteria — criterion 2 only required that an exit criterion exist — but a defect in what T-008 produced, so it is a child rather than an audit. |
