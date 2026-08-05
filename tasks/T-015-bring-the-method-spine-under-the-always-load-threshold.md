---
id: T-015
title: Bring the method spine under the always-load threshold
type: fix
status: done
phase: review
parent: T-008
blocked_by: []
related: [T-014]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-04
updated: 2026-08-04
deliverables:
  - docs/METHOD.md
  - docs/method/rationale.md
  - docs/method/where-facts-live.md
  - CLAUDE.md
---

# T-015 — Bring the method spine under the always-load threshold

## 1. Specify

**Outcome**
A spine short enough that always loading it is obviously cheaper than loading the method as one
document — with the threshold stated as a number, so the claim can be checked rather than argued.

**Requirements served**
R-21 (`docs/SCOPE.md`).

**Why this one**
Found reviewing [T-008](T-008-write-the-backend-neutral-method-document.md), against its own
acceptance criterion 5 ("a spine short enough to always load, details on demand"):

```
188 docs/METHOD.md          <- the always-loaded spine
173 reference/TASK-WORKFLOW.md   <- the single-file option D4 rejected
```

The spine is **larger than the whole document it was meant to improve on**. Progressive disclosure
that loads more up front than the flat alternative has inverted its own purpose, and D4's rationale
("this is how criterion 5 becomes checkable rather than a judgement about length") currently argues
against the thing it chose. The five phase files are not the problem — they load on demand and are
60–90 lines each. The spine is.

The comparison is not perfectly like-for-like: the spine carries a conduct section and a departures
section the prior art had no equivalent of, so some growth is real content rather than bloat. That
is an argument about *how far* to cut, not about whether the criterion is met — as written, it is
not.

**Scope**
- In: deciding what genuinely has to be resident on every turn, moving the rest to on-demand files,
  and writing the threshold down.
- Out: the phase procedure files; changing what the method *says*. This is placement, not content —
  nothing may be deleted, only relocated.

**Candidates for eviction** (each needed only at a specific moment, not on every turn)
- §7 *Deliberate departures* — rationale; needed when someone questions the design, which is what
  a rationale file is for
- §5 *Audit* — a summary of `method/audit.md`, needed only when an audit is in play
- §6 *Where each kind of fact lives* — needed when writing something down, not when reading

**Must stay resident** — §1 core rules, §2 the lifecycle table, §3 conduct (it gates every turn),
§4 edges (every phase touches them).

**Acceptance criteria**
- [ ] A stated threshold, with the reasoning for that number, written where a future editor will see
      it before adding to the spine
- [ ] The spine is under it, measured and shown
- [ ] The spine is smaller than `reference/TASK-WORKFLOW.md` — the flat option must lose on its own
      terms
- [ ] Nothing is deleted: every evicted section is reachable from the spine's load-on-demand table
- [ ] Someone who reads only the spine can still run a phase correctly, or is told which file to
      open

**Open questions**
- ~~Where does the threshold live?~~ **Answered — `CLAUDE.md`** (see *Decisions*).

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Inventory every normative statement across the seven method files **before** touching anything. | a baseline list, for step 5 |
| 2 | Set the threshold and write down the reasoning. | `CLAUDE.md` |
| 3 | Relocate the on-demand sections; create the files that receive them. | `docs/method/rationale.md`, `docs/method/where-facts-live.md` |
| 4 | Compress what stays, where the reasoning moved out from under it. | `docs/METHOD.md` |
| 5 | Re-inventory and diff against step 1; account for **every** difference. | the diff, in §4 |

## 3. Implement

**Decisions & assumptions**
- **The threshold is 150 lines, and it lives in `CLAUDE.md`** (2026-08-04). It constrains a shipped
  artifact; it is not a rule of the method, and putting it in the method would have been a project
  fact in a document that must carry none. 150 sits below the 173-line flat alternative with
  headroom, and `CLAUDE.md` states the consequence explicitly: an addition that would breach it is a
  signal the content belongs on-demand, **not an argument for raising the limit**. Without that
  sentence the number is decorative.
- **Nothing was deleted — the constraint was relocation only** (2026-08-04, maintainer). Every
  evicted section is reachable from the spine's §7 table, and step 5 exists to prove it rather than
  claim it.
- **Two duplications were created by this task and then removed** (2026-08-04). Moving a section to
  an on-demand file makes it tempting to leave a one-line summary behind; twice that summary was a
  verbatim restatement — the tie-break rule in `where-facts-live.md`, and the no-inline-fix rule in
  `audit.md`. Both now open by *pointing* at the spine and going straight to the elaboration. This
  is T-014's finding recurring inside its own fix, which is the argument for holding the standard on
  every file rather than only the ones under review.
- **The limit was reached by trimming, not by moving the limit** (2026-08-04). The first pass landed
  at 156, then 151, then 150 — over or level three times. Each was resolved by finding real
  redundancy, per the rule written in step 2.

**Outputs produced**
- `docs/METHOD.md` — 188 → **147** lines
- `docs/method/rationale.md` (58) — five *why*s: the derived inverse, no audit phase, no
  effort/tools/model guidance, verification exiting `implement`, one phase per request
- `docs/method/where-facts-live.md` (41) — the fact→home table and the two-homes tie-break
- `CLAUDE.md` — the threshold and its reasoning

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A stated threshold with reasoning, where an editor will see it before adding | met | `CLAUDE.md`, in the *Working method* section, directly above what the project adds to the method — the place someone edits before touching `docs/METHOD.md`. |
| The spine is under it, measured and shown | met | `147 docs/METHOD.md`, limit 150. |
| The spine is smaller than the flat alternative | met | 147 vs `173 reference/TASK-WORKFLOW.md` — a 26-line margin, where before the "progressive" version was 15 lines *larger*. |
| Nothing deleted; every evicted section reachable from the spine | met | Inventory diff below. Both new files are rows in `METHOD.md` §7. |
| A spine-only reader can run a phase or is told which file to open | met | §7 names the load-when condition for all seven files; each phase row states when to open it. |

**The inventory diff** (plan steps 1 and 5). Eight statements present before and absent after, each
accounted for — no rule lost:

| Gone from the inventory | Where it is now |
| :--- | :--- |
| `## 7. Deliberate departures` | Section dissolved; both its bullets are `rationale.md` sections |
| `## 8. Load on demand` | Renumbered `## 7` — the spine lost a section, so the tail shifted |
| `**An audit is a kind of task, not a phase.**` | Reworded in the spine to "**task type, not a phase**"; the argument is `rationale.md` |
| `**Exit criterion — acceptance criteria written…**` | T-014: now only in `METHOD.md` §2 |
| `**Exit criterion — the outcome has been checked…**` | T-014: now only in `METHOD.md` §2 |
| `**There is no audit phase.**` | `rationale.md` → *Why there is no audit phase* |
| `**There is no guidance on… effort, which tools, or which model…**` | `rationale.md` → *Why the method says nothing about effort, tools or which model does the work* |
| `**points**` | Not a rule — a stray bold-marker artifact of the inventory regex |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → done | Worked with T-014 at the maintainer's request, under the constraint that no rule be cut. 188 → 147 lines, all of it relocation; the before/after inventory diff in §4 accounts for every difference. Two duplications created by the move were caught and removed. |
| 2026-08-04 | → proposed | Raised by T-008's review: acceptance criterion 5 not met. Interacts with [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) — one way of resolving the duplicated exit criteria also shortens the spine. |
