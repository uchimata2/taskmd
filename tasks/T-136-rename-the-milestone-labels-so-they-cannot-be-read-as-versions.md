---
id: T-136
title: Rename the milestone labels so they cannot be read as versions
type: admin
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-086, T-110, T-125, T-128, T-137]
work_package: v0.6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-12
updated: 2026-08-12
deliverables:
  - tasks/README.md
---

# T-136 — Rename the milestone labels so they cannot be read as versions

## 1. Specify

**Outcome**
No `work_package` value in this repository can be read as a version. A reader who sees a label on a
task knows immediately that it is a grouping, and reaches the release it shipped in without a
translation table. The table that exists today to perform that translation is deleted rather than
extended, because nothing is left for it to translate.

**Why this one**

The two number spaces have already come apart, and
[T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) said so in those words. It bought
the cheaper remedy: keep the labels version-shaped, make the open ones name their release, and
annotate the closed ones in a table. **That was the right call then and the evidence has moved.**

Five labels are in use against five tags, and they wear the same clothes:

| Label | Tasks | A tag with that number | What the label is actually worth |
| :--- | ---: | :--- | :--- |
| `v0.1` | 67 | `v0.1.0` | true, and the table says so |
| `v0.2` | 47 | `v0.2.0` | **false** — that work shipped in `v0.4.0`; one table row is the only record |
| `v0.3` | 4 | `v0.3.0` | true **by accident**, and written nowhere |
| `v0.5` | 11 | `v0.5.0` | true, and the handoff notes call it luck |
| `v0.6` | 6 | none yet | not yet decided |

The `v0.3` row is the one T-128 could not have priced, because it looks like nothing. All four of
those tasks closed in commits first contained in `v0.3.0`, so the label happens to resolve correctly
— to a tag that [`README.md`](README.md) states is **not a milestone**, but a batch version bump.
A reader is right for the wrong reason, gets no warning, and there is no row in the mapping table to
give them one. That is worse than the `v0.2` case, which at least announces itself as wrong.

So of five labels: one false, one true by accident, one true by luck, one true, one undecided. **A
reader cannot tell which is which by looking, and the table that would tell them carries three of
the five rows.** [`../.handoff/config.md`](../.handoff/config.md) spends a paragraph teaching each
new session not to assume — which is the reading cost, paid once per session, for ever.

**The table is the tell.** This plugin exists to remove hand-written second copies of a fact, and
its one design rule is *store the forward edge; derive the rest*
([`../CLAUDE.md`](../CLAUDE.md)). A translation table between two of this project's own label spaces
is exactly the feature that rule forbids, kept by a project that ships the rule. It earns a task on
that ground alone.

**The shape is the defect, not the number.** Renumbering inside the version space was already
considered and rejected — T-128 D3, on the grounds that new numbers would collide with the same
tags. That rejection is sound and is not being re-opened: it prices *renumbering*, and this task
proposes *leaving the version shape*, which the collision argument does not reach.

**Scope**
- In: the `work_package` value on all 135 tasks that carry one, one-to-one. Whether **closed** tasks
  are included is an open question below, because METHOD rule 5 speaks to it.
- In: every label mention in project documents and task prose — [`README.md`](README.md) *Releases*,
  [`../.handoff/config.md`](../.handoff/config.md), the example queries, and the task logs that name
  a label.
- In: deleting the mapping table, or reducing it to the historical note the rename makes it.
- Out: renaming any real version. Tags `v0.1.0` through `v0.5.0`, the manifest, the published release
  notes and the release bodies stay exactly as written. Nothing published moves.
- Out: the release **grouping** rule, which is the maintainer's of 2026-08-10 and is applied here
  rather than revisited ([T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md)).
- Out: what taskmd ships so an adopting project avoids this. That is
  [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md), split off so its
  mechanism question does not hold this rename.
- Out: a second field recording which version each task shipped in. The adopting project that
  surfaced this added one; here the label will carry it, so a second field would be the duplication
  this task removes.

**Inputs**
- [`../plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)
  — `work_package` is a field the schema **names** and does not enumerate, so no vocabulary row
  changes and no config key is added. Confirmed by T-128's own assumption, which the two empty
  queries in its §3 step 4 proved.
- [`README.md`](README.md) *Releases* — the mapping table, and the closure criterion that must
  survive the rename unchanged.
- [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) — the decision this revisits, and
  the reason its D1 has to be answered again rather than assumed.
- `git tag` and the closing commit of each labelled task, for what actually shipped.
- **The trap, carried from the adopting project that hit it.** Its rewriter guarded every
  version-shaped token: record them, substitute, record again, refuse to write if the two lists
  differ. That held over 49 files. What it could not guard was a sentence **whose subject is the old
  name** — three sentences written during the work to quote the old labels were rewritten into
  saying nothing, and the two files excluded by hand were the two that never needed excluding. This
  repository is dense with such sentences: T-128's whole body, the mapping table, and the handoff
  paragraph exist *to talk about the old labels*. The exclusion list will be right and incomplete,
  which is the failure mode of every exclusion list. The project label is in
  `control/LOCAL-CONTEXT.md`, not here.

**Acceptance criteria**
- [ ] No tracked file contains a version-shaped `work_package` value, and every surviving `v0.N.N`
      token is a real tag, manifest or release reference — shown by naming each survivor, not by a
      clean grep.
- [ ] The substitution is proved not to have touched a version: the guard above ran on every file,
      and a file deliberately seeded with a version it must not change is shown to **abort** it. A
      guard that has only ever passed is not proven.
- [ ] `./plugin/bin/taskmd check` and `index` are green, `list --work_package <new label> --open`
      returns the same membership as the old label did, and the suite passes — including
      `test_list`, which filters on `work_package` against this tree.
- [ ] The mapping table is gone, and [`README.md`](README.md) answers *which release did this task
      ship in* without one.
- [ ] Every sentence whose subject is an old label still says what it said. Counted before starting
      and read back individually after.
- [ ] [`../.handoff/config.md`](../.handoff/config.md), [`../CLAUDE.md`](../CLAUDE.md) and
      [`../docs/BRIEF.md`](../docs/BRIEF.md) read correctly under the new names, and T-128 records
      that the annotation it chose was later replaced and why the first answer was right at the time.

**Open questions**
- none. Both were put to the project owner and answered on 2026-08-12.

**Q1 — what the labels become. Answered: keep each label's digit and change its shape**, so
`v0.1`→`M1`, `v0.2`→`M2`, `v0.3`→`M3`, `v0.5`→`M5`, `v0.6`→`M6`, leaving a true gap at `M4` because
no milestone was ever labelled `v0.4`. This keeps the property T-128 bought — the label's number
names its release — and removes only the shape that makes it resolvable as a version. *Rejected:
renumber sequentially to `M1`–`M5`.* It reads tidier and destroys the correspondence, turning every
closed task's label into a fact a reader has to look up. The digit is the cheap half of what T-128
built; only its clothes are the problem.

**Q2 — whether closed tasks are renamed. Answered: yes, all 135.** *Rejected: open tasks only, per
T-128 D1 and METHOD rule 5.* D1 is the stronger objection and it is answered by what the rename is:
rule 5 forbids rewriting what a record **says about the past**, and a label is not a statement about
the past — it is an index entry, whose whole value is that the same query reaches the same set.
Leaving 118 closed tasks version-shaped keeps the mapping table alive, which is the outcome this task
exists to end. The log rows that say *filed `v0.3`* are statements about the past and stay untouched,
which is where rule 5 actually bites.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → specified | Both questions answered by the project owner: keep the digit and change the shape, and rename closed tasks too. Their rivals are recorded beside them rather than dropped. **Authorisation (METHOD §3.1):** *full lifecycle on T-136 and T-137*, from the project owner on 2026-08-12, given with the answers. It covers this task end to end — specify through review — and nothing beyond the two tasks it names. |
| 2026-08-12 | → proposed | Raised after an adopting project hit the same defect and fixed it, and the maintainer asked for this repository's version of that work. **T-128 already named this problem and chose the cheaper remedy, correctly**: it priced the rewrite and bought protection for the release sequence, which is where the failure had happened. What it could not price was the reading cost, and the `v0.3` row is what came due — four closed tasks whose label resolves to a real tag, correctly and by accident, with no row in the table that exists to catch exactly that. Split from [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) for the reason T-128 was not folded into [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md): re-labelling a backlog and changing what the tool ships are different outcomes, and one diff carrying both is reviewable as neither. |
