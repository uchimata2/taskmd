---
id: T-086
title: Group the backlog into release milestones
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-006, T-022, T-026]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: [tasks/README.md]
---

# T-086 — Group the backlog into release milestones

## 1. Specify

**Outcome**
Every task carries the release it belongs to, and `tasks/README.md` says what v0.2 and v0.3 are for,
so "what is left before the next release" is answered by a command instead of by reading the
backlog.

**Why this one**
Asked for by the maintainer on 2026-08-09, straight after publication: v0.1 is what is now public,
and the next two releases need to exist as something a session can be pointed at.

**The obvious way to do it is the wrong one.** A release plan that lists its tasks in
`tasks/README.md` is a second copy of the backlog, in the one file this project has already watched
rot for exactly that reason ([T-084](T-084-correct-the-generated-index-preamble-after-the-move.md),
closed hours earlier). So the membership is stored where every other fact about a task is stored,
which is the task, and the plan names only what a release is *for*.

**Requirements served**
R-1 and R-12 (`docs/SCOPE.md`) are the constraint rather than the goal: the grouping has to be
derived, not tabulated. R-15 in the sense the `list` carve-out was argued on, since "what is left
before v0.2" is another question grep cannot answer.

**This does not widen non-goal 1.** `work_package` is an existing schema field whose meaning the
adopting project chooses, `index_columns` already names it, and `list` already filters on it. No
command, field or behaviour is added, and nothing here counts time, capacity or velocity. What is
added is values in a field that has always been there.

**Scope**
- In: a `work_package` value on every task, and the milestone definitions in `tasks/README.md`.
- Out: any code change. If the grouping wants something the tool cannot do, that is a finding.
- Out: tagging the repository or bumping `plugin.json`. A version marker is outward-facing and is
  the maintainer's, and this task can be complete without one.
- Out: re-planning the tasks themselves. They keep their outcomes, their estimates and their edges.

**Acceptance criteria**
- [ ] Every task in `tasks/` carries a `work_package`, and no task file lists which milestone any
      *other* task is in
- [ ] `taskmd list --work_package v0.2` and `--work_package v0.3` each return exactly the tasks the
      plan describes, shown by running them
- [ ] The generated index shows the milestone without anything being written into it by hand
- [ ] `check` is clean and the suite passes

**Open questions**
- ~~Whether closed tasks are labelled too.~~ — **answered here, 2026-08-09**: yes, `v0.1`. Everything
  closed is in the published tree, so the label is a true statement rather than a guess, and it makes
  "what shipped in v0.1" answerable by the same command as the other two. *Rejected: leaving them
  `none`*, which makes v0.1 the only milestone whose membership has to be worked out by hand, and
  leaves the index's new column empty for four fifths of the rows.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read every open task's outcome and estimates, and allocate each to v0.2 or v0.3 by what the release is for rather than by size. | The allocation, with its rejections, in §3 |
| 2 | Write the `work_package` value into every task's front-matter: `v0.1` for closed, the allocation for open. | The counts per value |
| 3 | Write the milestone definitions into `tasks/README.md`'s preamble, above the marker, naming no task. | The preamble |
| 4 | Regenerate, and check the derived view carries the milestone. | The index's new column, and both `list` runs |
| 5 | `check`, the suite, and the publish gates, since a covered document is not being touched but the tree is. | The outputs |

**Step 1 is a judgement and is recorded as one.** The allocation is the whole of the deliverable's
value, and a table of ids with no reasoning would be unreviewable.

## 3. Implement

Worked in plan order.

### Step 1 — the allocation

Two releases, split by **what each is for** rather than by what is cheap:

**v0.2 — the tool holds up in a project that is not this one.** Every open task about what the
commands do when an adopter's project is wrong, or when their arguments are: the validator's one
known blind spot, arguments nothing rejects, a template that produces an invalid task, and config
errors that name the wrong thing. It also carries the [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md)
umbrella, which cannot close until its five children do, and four of those five sit naturally here
anyway.

**v0.3 — the claims are proven off this machine, and the method's own documents settle.** The two
portability claims that are still assertions here, the tier-1 restructure, the plan-and-audit
boundary, the config that describes ids a backend allocates, and taskmd as a binding for the handoff
skill.

*Rejected: splitting by effort*, which produces two releases nobody can describe. *Rejected: one
milestone per audit finding*, which is a work-breakdown of a work-breakdown. *Rejected: leaving
T-047 in v0.2* on the strength of its `high` value: it is the always-loaded budget in this
repository's own conventions, so it costs a contributor rather than an adopter, and the maintainer is
the one likeliest to want it moved.

### Step 2 — the field

Written into every task, nowhere else:

```
v0.1   67 tasks, every closed one
v0.2   13 open, including this one and the child it raised
v0.3    7 open
```

`updated:` was deliberately **not** bumped on the closed tasks. The label says which release a task
shipped in; it does not change what the task said or did, and rewriting eighty-six dates to today
would erase when each task was actually last worked, which is the one thing that field is for.

### Step 3 — the preamble

The three milestones, what each is for, and its exit criteria. **No task is named**, and the line
under each one is the command that lists it, so the membership is derived at read time exactly like
`blocks` and the index.

### Step 4 — the derived view, and the command this plan could not use

The index grew a **Work Package** column with nothing written into it by hand: `index_columns`
already named the field, and a view omits a column no task has a value for, which is why it was
absent until today. That is the derived membership this task exists to produce, and it works.

**The other half of this step failed, and it failed on an assumption made at `specify`.**

```
taskmd list --work_package v0.2
unknown filter: --work_package. This project accepts: --blocked_by, --blocks, --business_value,
--children, --effort, --parent, --phase, --related, --status, --type
```

`parse_filters` builds what it accepts from the vocabularies plus the link names, so a stored field
nothing enumerates cannot be filtered even though both views will show it. Criterion 2 was written
as though it could be, which nobody checked before writing it down. Two things follow, and both are
recorded rather than smoothed over:

- **The preamble was drafted naming those two commands and was corrected before it shipped.** It now
  points at the generated column instead. Writing a release plan whose own instruction does not run
  would have re-created [T-084](T-084-correct-the-generated-index-preamble-after-the-move.md) in the
  same file, on the same day, by hand.
- **The gap is the tool's, not this task's**, so it is
  [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) rather than a code change here,
  which §1 scoped out. It is not about `work_package`: the schema promises an unnamed field is
  carried and can be surfaced by naming it in a view, and that promise stops at the filter.

### Step 5 — nothing else moved

```
./plugin/bin/taskmd check     OK - 87 task(s), vocabulary valid, references resolve, no broken links
python -m pytest tests/ -q    129 passed, 4 subtests passed
humanize gate                 4 file(s) covered, exit 1
leak check                    silent, 168 files read
grep -L 'work_package: v0\.'  0 task files without a milestone
```

**Decisions & assumptions**

- **`work_package` carries the release, rather than a new field** — it exists, `index_columns`
  names it, `list` filters on it, and its values are the project's to choose. A `release:` field
  would be a second grouping mechanism for one kind of fact. — 2026-08-09
- **The plan names no task and the tasks name no plan** — one direction only, which is the same
  rule as every edge here. — 2026-08-09
- **Closed tasks are `v0.1`**, per §1's answered question. — 2026-08-09

**Outputs produced**
- [`tasks/README.md`](README.md) — the milestone definitions
- Every task file — one front-matter value

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every task carries a `work_package`, and no task file lists which milestone any other task is in | met | §3 step 2's counts add to the whole backlog. The only prose about membership is in the preamble, and it names no id |
| `taskmd list --work_package v0.2` and `--work_package v0.3` each return exactly the tasks the plan describes | **not met, carried** | The command does not exist. `list` accepts vocabulary fields and link names, and `work_package` is neither, so the criterion asked for something the tool cannot do and nobody checked that before agreeing it. → **child task [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md)**. The membership is still derived, by the column in the next row |
| The generated index shows the milestone without anything written into it by hand | met | §3 step 4: the column appeared because the field now has values, which is the schema's *a view omits a column no task has a value for* working rather than a change |
| `check` is clean and the suite passes | met | §3 step 5 |

Three met, one carried.

**What this does not do.** It does not make a release happen. Nothing here tags the repository or
touches `plugin.json`, which is scoped out and is the maintainer's, and until they do, v0.2 is a
plan rather than a version.

**The allocation is a judgement and should be read as one.** Nineteen tasks were sorted by what each
release is for, by one session, in one pass. The row most likely to be wrong is
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) in v0.3, and moving
any task between milestones is one field in one file.

**Child fix tasks raised**
- **[T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md)** — criterion 2, carried.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | (no change, closed) | **Superseded by [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md)**, which re-grouped this backlog on a maintainer's rule of size and dependency. §3 above is left exactly as it was — it is what this task decided and why, and the two headlines it wrote are no longer the milestones' purposes. Read them as this task's record, not as the current definition; that lives in `tasks/README.md`. Worth noting for whoever follows the argument: Step 1 **rejected splitting by effort** on the grounds that it produces two releases nobody can describe, and it was right about the cost — T-110 had to state that consequence in the file rather than avoid it. The maintainer accepted the cost knowingly. |
| 2026-08-09 | → done | Three criteria met, one carried. The milestone is a value in each task and the generated index grew a **Work Package** column for it with nothing hand-written, which is the whole deliverable working: 67 in v0.1, 13 in v0.2, 7 in v0.3, and no task without one. **The fourth criterion asked for a command that does not exist.** `list` accepts vocabulary fields and link names, and `work_package` is neither, so `--work_package v0.2` is rejected even though `index_columns` displays the field and `--json` emits it. The preamble had been drafted naming that command and was corrected before it shipped, which is the only reason this did not re-create T-084 in the same file on the same day. The gap belongs to the tool and is [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md): the schema promises an unnamed field is carried and can be surfaced by naming it in a view, and that promise stops at the filter. |
| 2026-08-09 | → in_progress | Asked for by the maintainer after publication. The obvious implementation was rejected first: a release plan listing its tasks in `tasks/README.md` is a second copy of the backlog in the file T-084 had just been raised about, so membership lives in each task's `work_package` and the preamble carries only what a release is *for*. Closed tasks are labelled `v0.1`, which is true rather than a guess, and their `updated` dates are left alone because a milestone label does not change what a task did. The allocation splits on purpose rather than size: v0.2 is what an adopter's project can make the commands do wrong, v0.3 is the claims that are still assertions off this machine plus the method's own documents. T-047 sits in v0.3 despite being `high`, because it costs a contributor rather than an adopter, and that is the row most likely to be moved. |
