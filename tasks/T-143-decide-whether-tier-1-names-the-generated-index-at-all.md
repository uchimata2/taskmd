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
updated: 2026-08-15
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
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T3`. The row asks nothing of the tool — its proposed answer is what `SKILL.md` has said since it was written — so what survives is the same rule applied to this repository, where the always-loaded file names the 33,607-byte instrument and the skill names the 96-byte one. `medium` because nothing is broken and no adopter is affected; the cost is one repository's own sessions taking the long route. `s` because the decision is a sentence and the evidence is two commands. Filed as `decision` rather than `fix` because tier 1's two clauses genuinely disagree here and picking one is the work. |
