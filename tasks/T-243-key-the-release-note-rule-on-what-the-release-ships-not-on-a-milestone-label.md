---
id: T-243
title: Key the release-note rule on what the release ships, not on a milestone label
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-135, T-182, T-242, T-231]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-243 — Key the release-note rule on what the release ships, not on a milestone label

## 1. Specify

**Outcome**
[`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 builds the set a release note must cover from a
**milestone label**. It should build it from **what the release actually ships**, so that no task can
fall outside the query by carrying a different label. What exists at the end is a §7 whose set is
derived from the tag range, and a recorded decision if the owner prefers to keep the label.

**Why this one**
Measured on 2026-08-23, while cutting `0.6.0`. §7's command reads one work package, so a task that
closed inside the release window but carries an older label is invisible to it. Two did:

| Task | Label | Closed | Files it touched under `plugin/` |
| :--- | :---: | :---: | ---: |
| `T-006` *"Package, document and publish"* | M1 | 2026-08-16 | 23 |
| `T-085` *"Install the published plugin on a machine that has never seen it"* | M5 | 2026-08-16 | 0 |

`T-006` is the one that matters: it changed 23 shipped files after the `v0.5.0` tag and §7 would have
left it out of the note with nobody having chosen to leave it out. That is the exact failure §7
exists to prevent — an omission nobody made a decision about — arriving through the rule's own query
rather than through a writer's memory.

**The alternative already exists and is derived.** What the release ships is one command:

```bash
git diff --name-only v0.5.0..HEAD -- plugin/
```

which returned **17 files** for this release. An install copies exactly the `plugin/` subtree
([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)), so that diff is the
release, with nothing to label and nothing to keep in step.

**Scope**
- In: whether §7 keys on the tag range, on the milestone, or on both
- In: the edit to `docs/PUBLISHING.md` §7 if the answer changes it, and to whatever the suite reads
- Out: the marks themselves. That was
  [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md)
- Out: **why the field goes unfilled in the first place.** A rule that reads the right set still
  reads a field nobody was asked to fill; that is its own task and neither this nor T-242 fixes it

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 — the rule, its three counts and its stated limits
- [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) — where the rule
  came from, and the `v0.4.0` worked example it was derived against
- [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) §3 — the
  measurement above, and the two tasks that were added to `0.6.0`'s set by hand

**Acceptance criteria**
- [ ] §7 states which set it reads, and that statement is true of a task carrying any label
- [ ] The decision names what it rejected and why
- [ ] If the rule changes, the suite reads the new shape from `docs/PUBLISHING.md` rather than
      restating it, as `tests/test_publishing.py` already does for §5 and §6
- [ ] Running the new rule against `0.6.0` returns a set that contains `T-006`

**Open questions**
- ~~**Does §7 key on the tag range, keep the milestone, or read both?**~~ **Answered by the project
  owner on 2026-08-23: the tag range.** *The question as it stood, kept so a later reader can see what
  was chosen over what: — the project owner. The recommendation is* **the tag range**, *because it is
  derived and a label is maintained. Against: the milestone is what a reader of the note thinks in,
  and a tag range says nothing about which release a piece of work was scheduled into — reading both
  keeps that and costs a second command.* The rejected options and their costs are in the Log.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **Answered by the owner on 2026-08-23: §7 keys on the tag range.** *Rejected: read both* — it keeps the milestone as the thing a reader thinks in and still catches the strays, at the cost of two sets to reconcile by hand every release and a rule with two answers. *Rejected: keep the milestone and add strays by hand*, which is what `0.6.0` did: no work now, and the gap returns at every release depending on somebody noticing it again — which this time took running the rule rather than reading it. **The work is unchanged by the answer**; §1's acceptance criteria already covered either outcome, and the criterion requiring the new rule to return a set containing `T-006` is now the one that matters. |
| 2026-08-23 | → proposed | **Raised on the owner's answer of 2026-08-23**, given as a survey while `0.6.0` was blocked. They chose *add the two strays to this release's set by hand and raise the rule change separately*, over *change the rule now* — which was cheaper to state and would have held the release for a rule edit — and over *ship M6 as it stands*, which would have dropped `T-006` *"Package, document and publish"* and its 23 shipped files out of the note with nobody choosing to drop them. So this record carries the durable half and `0.6.0` is not waiting on it. **The measurement is here rather than in the release record**, because it is a fact about the rule and outlives the release that found it. |
