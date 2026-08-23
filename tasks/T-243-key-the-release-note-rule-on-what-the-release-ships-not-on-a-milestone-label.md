---
id: T-243
title: Key the release-note rule on what the release ships, not on a milestone label
type: decision
status: done
phase: review
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
deliverables:
  - docs/PUBLISHING.md
  - tests/test_publishing.py
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
| 1 | Measure what each candidate set returns for `v0.5.0..v0.6.0`, by membership and not by count | The three candidates in §3, each with its yes / no / unmarked split |
| 2 | Choose the one that contains `T-006` without blocking the note on an unmarked backlog | A decision recorded in §3 with the rejected candidates and what each cost |
| 3 | Rewrite `docs/PUBLISHING.md` §7's set-derivation to that rule, and say why the milestone went | §7, carrying a command and the measurement behind it |
| 4 | Add tests that **lift** §7's command rather than restate it, as §5 and §6 already are | `tests/test_publishing.py`, four cases |
| 5 | Show the tests fail on the milestone rule they replaced | A recorded failing run, in §3 |

## 3. Implement

**Decisions & assumptions**

- **A task ships when a commit in the tag range changed both its record and something under
  `plugin/`** — decided 2026-08-23, and it answers *how* to key on the tag range, which the owner's
  answer left open. Three candidates were measured against `v0.5.0..v0.6.0`, by membership rather
  than by count:

  | Candidate | Set | Contains `T-006`? | Unmarked, which block the note |
  | :--- | ---: | :---: | ---: |
  | The milestone query, as it stood | 72 | **no** | — |
  | Every closed task whose record changed in the range | 104 | yes | **81** |
  | **Closed, and sharing a commit with a `plugin/` change** | **104** | **yes** | **3** |

  The second and third return the **same 104 tasks** — the symmetric difference of the two id sets
  is empty, checked per item and not by count. They differ only in what else they drag in: the
  second admits every closed task a reconcile sweep happened to touch, and 81 of those predate the
  `adopter_visible` field, so §7's *an unmarked task blocks the note* would have held the next
  release hostage to judging 81 tasks that shipped in earlier ones. The third excludes them because
  a sweep commit changes no shipped file. *Rejected: the second*, on that measurement. *Rejected:
  intersecting with each task's `deliverables`*, which cannot work here — `T-006` declares none, so
  the one task the criterion names would have been the one it missed.

- **The set is a strict superset of the milestone query's**, verified per item: all 72 are present,
  and the 32 added include `T-006`. That is the property that matters, because §7 bounds what may be
  **left out** — a superset is safe, and a subset is the failure the milestone rule was.

- **The rule now depends on commit hygiene, and that is stated in §7 rather than left to be found.**
  A project that commits a task record separately from the work it produced breaks the link. Here it
  holds — 155 of 240 closed records linked to a shipped file this way — but it is an assumption
  about how this project commits, not a fact about git, so it is written where the rule is.

- **The command is written for `sh`, matching §5 and §6.** `docs/PUBLISHING.md` is the maintainer's
  release procedure and is excluded from what a stranger reads (§1), so no cross-platform obligation
  reaches it. The tests skip when `sh` or `git` is absent rather than failing.

**Outputs produced**

- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 — the set now comes from the tag range, with the
  measurement and the commit-hygiene limit stated beside it.
- [`tests/test_publishing.py`](../tests/test_publishing.py) — `TheReleaseNoteSetIsKeyedOnWhatShips`,
  four cases, which **lift §7's command out of the document** rather than restate it, exactly as
  `gate_from_the_document` and `leak_check_from_the_document` already do for §5 and §6.

**Checked by using it.** The command was lifted from the document and run, not read:

```text
total: 155   yes: 104   no: 48   UNMARKED: 3
T-006 -> yes T-006
```

104 + 48 + 3 = 155, so the three marks partition the set and nothing was skipped.

**And shown to fail.** A clean pass proves nothing, so §7 was reverted to the milestone query it
replaced and the suite re-run:

```text
FAILED test_no_label_appears_in_the_rule
FAILED test_the_set_contains_the_task_the_milestone_query_missed
FAILED test_the_three_marks_partition_the_set
3 failed, 1 passed
```

The document was then restored from a copy taken **before** the break — not with `git checkout --`,
which restores `HEAD` and would have destroyed the fix being measured.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| §7 states which set it reads, and that statement is true of a task carrying any label | met | The command consults no label. `test_no_label_appears_in_the_rule` fails if `work_package` returns to it, and did fail when the milestone query was put back |
| The decision names what it rejected and why | met | §3 rejects the touched-in-range set on its 81 unmarked tasks, and the `deliverables` intersection on `T-006` declaring none. The owner's own rejections are in the Log |
| If the rule changes, the suite reads the new shape from `docs/PUBLISHING.md` rather than restating it | met | `shipped_set_command_from_the_document` lifts the fenced block, and raises rather than guesses if the shape stops parsing — the same strictness §5 and §6 already have |
| Running the new rule against `0.6.0` returns a set that contains `T-006` | met | `yes T-006`, in a run of the command lifted from the document. Shown to fail on the rule it replaced |

**Child fix tasks raised**
- [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md) — the
  three records the new rule reports as `UNMARKED`. Out of scope here for the reason §1 gives: the
  marks themselves were T-242's, and this record changes the rule that reads them, never the values.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **Landed under the owner's unattended full-lifecycle grant, recorded below.** §7 keys on the tag range, by the commit-linked reading measured in §3: the same 104 adopter-visible tasks as the plain touched-in-range set, and 3 unmarked instead of 81. The one thing the grant did not cover arrived during the work — 3 records the new rule reports as `UNMARKED` — and it is [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md), raised rather than fixed here. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, unattended, and asks that it land before the audit** — given on 2026-08-23 in these words: *"Update the handoff file to land T-243 and T-245 before the audit in the new session, full lifecycle, commit and push"*. Recorded here rather than in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, and committing and pushing the result. **What it does not:** any other task, and starting [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md), which stays the owner's to begin. |
| 2026-08-23 | (no change) | **Answered by the owner on 2026-08-23: §7 keys on the tag range.** *Rejected: read both* — it keeps the milestone as the thing a reader thinks in and still catches the strays, at the cost of two sets to reconcile by hand every release and a rule with two answers. *Rejected: keep the milestone and add strays by hand*, which is what `0.6.0` did: no work now, and the gap returns at every release depending on somebody noticing it again — which this time took running the rule rather than reading it. **The work is unchanged by the answer**; §1's acceptance criteria already covered either outcome, and the criterion requiring the new rule to return a set containing `T-006` is now the one that matters. |
| 2026-08-23 | → proposed | **Raised on the owner's answer of 2026-08-23**, given as a survey while `0.6.0` was blocked. They chose *add the two strays to this release's set by hand and raise the rule change separately*, over *change the rule now* — which was cheaper to state and would have held the release for a rule edit — and over *ship M6 as it stands*, which would have dropped `T-006` *"Package, document and publish"* and its 23 shipped files out of the note with nobody choosing to drop them. So this record carries the durable half and `0.6.0` is not waiting on it. **The measurement is here rather than in the release record**, because it is a fact about the rule and outlives the release that found it. |
