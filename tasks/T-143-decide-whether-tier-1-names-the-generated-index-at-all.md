---
id: T-143
title: Decide whether tier 1 names the generated index at all
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-028, T-087, T-118]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-18
deliverables: []
---

# T-143 — Decide whether tier 1 names the generated index at all

## 1. Specify

**Outcome**
`CLAUDE.md` and the skill agree about which instrument answers *what is in the backlog*, so a session
handed both does not take the expensive route because the always-loaded file named it first.

**Why this one**
Raised from the htmldeck adopter report, row `O-T3`, which observed that a generated index grows with
the whole board while a query grows only with what is open, and offered its own conclusion tentatively:
the index is for people, and the fix may simply be that agents never read it.

**That conclusion is already what this project ships**, in the first two lines of `SKILL.md` — *run a
command, do not read the folder, and never maintain a list* — and in the `Run first` block, whose
first command is `list --open --limit 1`. So the row asks for nothing from the tool. Applying it here
finds something else: **`CLAUDE.md` names the index, and `CLAUDE.md` is tier 1.**

**Measured on this repository, 2026-08-15.**

```
tasks/README.md            33,607 bytes
taskmd list --open            707 bytes      47.5x smaller
taskmd list --open --limit 1   96 bytes     350x smaller
```

The index grows with every task ever closed; 131 of this repository's 143 files are done and every one
of them is a row. `list --open` grows only with what is open, which is eight.

**Re-measured later the same day by
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), in characters:**

```
tasks/README.md              36,393 chars
taskmd list --open            1,473 chars      24x smaller
taskmd list --open --limit 1     95 chars     383x smaller
```

**Both measurements are 2026-08-15 and they disagree**, which is the reason the acceptance criteria
below refuse to let either be carried: eight tasks were raised between them, the corpus grew from 143
files to 151, and the two are in different units — bytes above, characters here, which is the unit the
tier-1 budget uses. Neither is the decision-time figure.

**Two of tier 1's own rules disagree about this line.** `CLAUDE.md` admits a line only if it changes
what a session does *before it has chosen what to work on* — and where to find the backlog is exactly
that, so the line qualifies. It also says **where the project has got to never qualifies**, being
derived from the tasks that got it there — and a generated index of every task is precisely that, so
the line does not qualify. The same file says both, four paragraphs apart, and the sentence
*Where the project stands is in the tasks that got it there — never here* sits immediately below the
pointer. [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) wrote the rule and cut to
it; this line survived the cut.

**Why it is not simply a deletion.** The pointer is also true and useful to a human opening the
repository, and `CLAUDE.md` is read by people as well as served to sessions. The question is whether
tier 1 is where that sentence is paid for, given that every session pays for it and the sessions that
act on it take a route the skill tells them not to.

**Requirements served**
R-21 (`docs/SCOPE.md`) — the always-loaded cost, falsified by measuring a session rather than argued.

**Scope**
- In: whether `CLAUDE.md` names `tasks/README.md`, and if so what it says about it.
- In: whether the same sentence should name the command instead, given that naming a command in tier 1
  is a cost too and the skill already carries it.
- Out: the index itself, its columns, and whether it is generated at all. It is for people and that is
  settled.
- Out: `list`, which already answers this and needs nothing
  ([T-022](T-022-filtered-task-listing-for-scripts.md),
  [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md)).
- Out: re-opening the membership rule or the bound. Both are
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md)'s and stand.

**Inputs**
- `CLAUDE.md`, the *What this is* paragraph and the *What earns a place here* paragraph.
- `plugin/skills/taskmd/SKILL.md`, lines 8 to 17.
- [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) — the rule this line is measured
  against, and what it cut instead.

**Acceptance criteria**
- [ ] The decision is stated against both of tier 1's own clauses, naming which one governs and why
- [ ] The measurement is re-run at decision time rather than carried from here, since both figures move
- [ ] Whatever is decided, `CLAUDE.md` and `SKILL.md` do not send a session to two different
      instruments for the same question
- [ ] The tier-1 budget test still passes, and the effect of the change on the figure is stated —
      including if it is zero
- [ ] No number from this task is written into `CLAUDE.md`

**Open questions**
- **Should tier 1 name a command at all?** Replacing the pointer with `taskmd list --open --limit 1`
  answers the question at 96 bytes and duplicates the skill's `Run first` block, which is the one
  thing this project's design rule forbids. Leaving nothing means a session with no skill loaded has
  no route to the backlog. The third possibility is that the sentence points at the skill rather than
  at either artifact. Decide at `specify`.

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
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T3`. The row asks nothing of the tool — its proposed answer is what `SKILL.md` has said since it was written — so what survives is the same rule applied to this repository, where the always-loaded file names the 33,607-byte instrument and the skill names the 96-byte one. `medium` because nothing is broken and no adopter is affected; the cost is one repository's own sessions taking the long route. `s` because the decision is a sentence and the evidence is two commands. Filed as `decision` rather than `fix` because tier 1's two clauses genuinely disagree here and picking one is the work. |
| 2026-08-15 | — | [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s finding E-12 is this task, arrived at independently, and **raised no second task for it** — what the audit adds is the character measurement recorded above, written here because this is where the question lives. The two same-day figures disagreeing is the finding's own evidence for the criterion that already said to re-run them. |
