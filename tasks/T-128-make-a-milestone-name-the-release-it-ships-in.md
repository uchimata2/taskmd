---
id: T-128
title: Make a milestone name the release it ships in
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-086, T-110, T-125]
work_package: M5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [tasks/README.md]
---

# T-128 — Make a milestone name the release it ships in

## 1. Specify

**Outcome**
A `work_package` value names the release its tasks ship in. Every open task carries the value for the
release it is scheduled into, and where a past label does not match what shipped, `tasks/README.md`
says so.

**Why this one**
The two numbering schemes have come apart. Milestones are labelled `v0.1`, `v0.2`, `v0.3`. Releases
are tagged `v0.1.0` through `v0.4.0`. Only the first pair agrees:

| Milestone | Shipped as |
| :--- | :--- |
| `v0.1` | `v0.1.0` |
| `v0.2` | **`v0.4.0`** |
| `v0.3` | not yet |

`v0.2.0` and `v0.3.0` were batch bumps taken mid-milestone so that installed projects would receive
fixes. Neither is a milestone. So a reader who sees `work_package: v0.2` and looks for a `v0.2.0`
release finds one, and it is the wrong one. The label does not merely lag: it points somewhere real
and false.

**Nine open tasks carry `v0.3`**, and the next release cannot be `v0.3.0` because that tag is taken.
Every one of those labels is wrong before the work starts.

**The second defect is in the exit criteria.** `v0.3`'s are five named outcomes. Four of its nine
tasks are not required by any of them. This is the drift [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md)
removed from `v0.2` by replacing an enumerated clause set with *done when every task grouped here is
closed* — and it has rebuilt itself in the milestone T-110 left enumerated.

**Requirements served**
None directly. This is backlog hygiene, and it earns a task because a wrong label is read as a fact.

**Scope**
- In: the `work_package` value on every **open** task, and which release each is scheduled into.
- In: the *Releases* section of `tasks/README.md`: what each release is for, when it is done, and the
  mapping for labels that do not match what shipped.
- Out: the `work_package` value on **closed** tasks. METHOD rule 5 forbids rewriting what a record
  says about the past. `v0.2` meant something when those tasks carried it, and the annotation is the
  remedy.
- Out: re-tagging, re-pointing or deleting any published release.
- Out: the grouping rule itself, which is the maintainer's of 2026-08-10 and is applied here rather
  than revisited.

**Inputs**
- `tasks/README.md`, *Releases*.
- `git tag` and `gh release list`, for what actually shipped.
- [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md), for the grouping rule
  and for why `v0.2`'s exit criterion is a closure test rather than a list.

**Acceptance criteria**
- [ ] No open task carries a `work_package` naming a version that is already tagged
- [ ] Each open task is in exactly one release, and the split follows the maintainer's stated rule
      rather than a fresh one
- [ ] `tasks/README.md` states what each open release is for and when it is done
- [ ] A reader can find, from `tasks/README.md` alone, which release a closed `v0.2` task shipped in
- [ ] `check` and `index` pass, and no task file loses history to the edit

**Open questions**
- none. One was raised and answered inside this task: see D2.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Split the nine open tasks between two releases by the maintainer's rule, using each task's own `effort` and `type` rather than a judgement about it. | The split, in §3 |
| 2 | Rewrite `work_package` on those nine, and on nothing else. | Nine task files |
| 3 | Rewrite the *Releases* section: purpose and closure criterion per open release, and the mapping for the labels that shipped elsewhere. | `tasks/README.md` |
| 4 | Confirm the membership is readable from the tool and written nowhere. | Recorded output |
| 5 | `index`, `check`, and the suite. | Recorded output |

**Shape decisions.**

**D1 — Only open tasks are re-labelled.** A closed task's `work_package` records the grouping it was
worked under, which is a statement about the past. METHOD rule 5 says to annotate that, not rewrite
it, so the mapping goes in `tasks/README.md` where a reader meets the labels.

**D2 — Both new releases close on *every task grouped here is closed*, and their named outcomes stay
as description.** This re-opens T-110, which kept enumerated criteria for `v0.3` on the grounds that
a handful of outcomes was worth naming. The evidence for re-opening is the same evidence T-110 acted
on for `v0.2`: four of nine tasks are outside the criteria. *Rejected: keep enumerating.* It reads
better and it tells a reader what the release is about, which is real and is why the outcome
sentences are kept. What it cannot do is stay true, because a task added to a release does not add
itself to a hand-written clause. The synthesis is to keep the sentences and stop them being the gate.

**D3 — The next release is `v0.5`, not `v0.4.1` or a renumber.** `0.4.0` is published, so the next
minor is `0.5.0` and the label matching it is `v0.5`. Renumbering the milestone labels to start again
would collide with the same four tags.

**Planned outputs**
- tasks/README.md
- the nine open task files

## 3. Implement

### Step 1 — the split

The rule sorts on size and on what blocks what. Every open task's `effort` and `type` were read from
its front-matter rather than judged:

| Task | Type | Effort | Release |
| :--- | :--- | :--- | :--- |
| T-020 confirm byte-identical output on macOS and Linux | analysis | m | v0.5 |
| T-085 install the published plugin on a fresh machine | analysis | s | v0.5 |
| T-121 report a second index outside the markers | fix | s | v0.5 |
| T-126 catch dash-gate drift | fix | s | v0.5 |
| T-117 decide whether the command surface needs one statement | decision | xs | v0.5 |
| T-127 decide whether a release note is text a stranger reads | decision | xs | v0.5 |
| T-005 align with the handoff tracker-binding contract | research | m | v0.6 |
| T-093 decide whether check resolves a section reference | decision | l | v0.6 |
| T-108 move a backlog from local files to GitHub Issues | deliverable | xl | v0.6 |

Nothing blocks anything, so the rule reduces to size and kind. **The line falls where the sizes do**:
`v0.5` is every `xs`, `s` and one `m`; `v0.6` is the `l`, the `xl` and the one remaining `m`, which is
a new integration rather than a correction. T-093 is the only judgement call, and its `l` decided it:
a decision that large is bigger work whatever its type says.

### Step 2 — the labels

Nine files, `work_package` only. Closed tasks were not touched, so 118 of them still read `v0.1` or
`v0.2` and still describe the grouping they were worked under.

### Step 3 — the *Releases* section

Rewritten with the mapping table, the two open releases, and one closure criterion for both. The
example command in it now names `v0.5`, so the page does not teach a query that returns nothing.

### Step 4 — the membership is readable and written nowhere

```text
$ taskmd list --work_package v0.5 --open
T-020  T-085  T-121  T-126  T-128  T-117  T-127

$ taskmd list --work_package v0.6 --open
T-108  T-005  T-093

$ taskmd list --work_package v0.3 --open
$ taskmd list --work_package v0.2 --open
```

**The last two return nothing**, which is criterion 1: no open task names a version that is already
tagged. They exit 0 and print no rows, because `work_package` is not an enumerated field and an
empty bucket is a legal answer.

### Step 5 — the tree

```text
Wrote tasks/README.md - 10 active, 118 closed
OK - 128 task(s), 640 field value(s), 408 reference(s), 22 dependency edge(s), 228 declared
     output(s), 1 index file(s), 156 document(s), 1287 link(s), 2 template(s), 10 template field
     value(s), 0 vocabulary row(s)
```

`test_cli` 100 OK, `test_list` 37 OK, `test_schema` 53 OK, `test_budget` 5 OK, `test_runtime` 27
`OK (skipped=3)`. `test_list` is the one that could have broken: it filters on `work_package` against
this tree. It does not, because T-124 stopped it naming a value and made it read one from the data.
**That fix is one day old and this is the change it was written for.**

**Decisions & assumptions**
- **D1 — closed tasks keep their labels** — 2026-08-11, §2; the mapping table is the annotation.
- **D2 — both releases close on every task being closed; the outcomes stay as description** —
  2026-08-11, §2. This re-opens T-110 on evidence, and the rejected alternative is recorded there.
- **D3 — the next label is `v0.5`** — 2026-08-11, §2.
- **Assumption: no config change is needed.** `work_package` is a field the schema names and does not
  enumerate, so a new value needs no vocabulary row. Confirmed by the two empty queries in step 4
  returning exit 0 rather than a rejection.

**Outputs produced**
- [`tasks/README.md`](README.md)
- Nine task files: T-005, T-020, T-085, T-093, T-108, T-117, T-121, T-126, T-127

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| No open task carries a `work_package` naming a version that is already tagged | met | §3 step 4: `--work_package v0.2 --open` and `v0.3 --open` both return no rows, read from the tool rather than from the index page |
| Each open task is in exactly one release, and the split follows the maintainer's stated rule rather than a fresh one | met | §3 step 1 tabulates all nine with the `effort` and `type` they already carried. The rule sorts on size and on blocking; nothing blocks anything here, so size decided it |
| `tasks/README.md` states what each open release is for and when it is done | met | One sentence of purpose each, and one shared closure criterion, with the reason the enumerated form was dropped |
| A reader can find, from `tasks/README.md` alone, which release a closed `v0.2` task shipped in | met | The mapping table says `v0.2` shipped as `v0.4.0`, and says that row is the only place recording the mismatch |
| `check` and `index` pass, and no task file loses history to the edit | met | §3 step 5. Only `work_package` changed on the nine; the log rows that say "Filed `v0.3`" are left standing, because they record what was true when they were written |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | (no change, closed) | **The remedy this task chose was replaced, and it was the right one when it was chosen.** [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) renamed the labels to `M1`–`M6` and deleted the mapping table D1 put in `tasks/README.md`. What this task priced was the rewrite, and it bought protection for the release sequence, which is where the failure had happened; what it could not price was the reading cost, which kept accruing. D3 is untouched and remains correct — it rejected *renumbering inside the version space*, and the collision argument it rests on does not reach a label that leaves that space. **Everything above this row keeps the old names on purpose**: this task's whole subject is what the labels were called, so a sweep that renamed its prose would have left it saying nothing. |
| 2026-08-11 | → done | All five criteria met. **The split needed no judgement it could not show its working for**: nothing in the backlog blocks anything, so the maintainer's rule reduces to size, and the line fell exactly where the `effort` values already sat. T-093 is the single call worth naming, and its `l` settled it. Two things worth carrying. **A wrong label here was worse than a stale one**: `work_package: v0.2` sent a reader to a `v0.2.0` release that exists and is not what those tasks shipped in, so the mapping table is the fix rather than a renumber. And **`test_list` was the test most likely to break and did not** — it filters on `work_package` against this tree, and it survived because T-124, one day old, stopped it naming a value and made it read one from the data. This change is the one that fix was written for, sooner than expected. |
| 2026-08-11 | → planned | **Authorisation (METHOD §3.1):** *update the backlog to schedule the items to the corresponding next release*, from the maintainer on 2026-08-11, given with the observation that the versions had come apart. It covers this task end to end. `specify` needed no new agreement, and the one question it raised is answered in D2 with its rival recorded, under the standing delegation. **The label is not merely stale, it is false**: a reader following `work_package: v0.2` to a `v0.2.0` release finds one, and that release is not what those tasks shipped in. They shipped in `0.4.0`. |
| 2026-08-11 | → proposed | Raised when the maintainer named the problem. Not folded into T-125, which had already shipped: re-labelling a backlog is a different outcome from publishing a tree, and doing it inside the release commit would have made the diff unreviewable as either. |
