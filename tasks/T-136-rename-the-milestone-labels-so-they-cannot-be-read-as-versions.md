---
id: T-136
title: Rename the milestone labels so they cannot be read as versions
type: admin
status: done
phase: review
parent: null
blocked_by: []
related: [T-086, T-110, T-125, T-128, T-137]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-12
updated: 2026-08-12
deliverables:
  - tasks/README.md
  - .handoff/config.md
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
| 1 | Extract every occurrence of a label-shaped token across all tracked files, with its line, and partition it into front matter and prose | The two counts, §3 |
| 2 | Rewrite `work_package` in front matter, under the version guard | 138 task files |
| 3 | Read every prose occurrence and mark each one keep or rename, before any of them is touched | The decision list, §3 |
| 4 | Apply only the marked occurrences, under the same guard | Project documents and task prose |
| 5 | Rewrite the *Releases* section and delete the mapping table | [`README.md`](README.md) |
| 6 | Prove it: the guard aborts on a seeded file, T-137's detector goes quiet, `check`, `index`, the suite | Recorded output, §4 |

**Shape decisions.**

**D1 — the guard is the adopting project's, reused unchanged.** Record every `v?N.N.N` token in a
file, substitute, record them again, and **refuse to write if the two lists differ**. That makes *no
version was touched* enforced per file rather than asserted afterwards. It ran over 49 files there
and never aborted, which is the second thing worth copying: a guard that has only ever passed is not
proven, so step 6 seeds a file it must reject.

**D2 — the prose is decided per occurrence, not per file, and this is where the plan departs from
the project it is copying.** Theirs excluded documents by hand, and its own record says the exclusion
list "was right and incomplete, which is the failure mode of every exclusion list" — three sentences
written to quote the old names were rewritten into saying nothing. A file-level list cannot express
*this paragraph quotes the old label on purpose and the one below it does not*, which is the actual
distinction. So step 3 marks occurrences, step 4 applies only what is marked, and a file is never a
unit of the decision. *Rejected: exclude by file and read the excluded ones back.* It is far cheaper
and it is the approach whose failure is already measured.

**D3 — this repository is unusually dense with sentences whose subject is the old name**, and three
of them are load-bearing: [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) exists to
explain the labels, the mapping table exists to translate them, and §1 of *this* task quotes all five.
Those must survive verbatim; step 3 finds them by reading, not by remembering them here.

**D4 — front matter and prose are different populations and are done in different steps.** The 138
`work_package:` values carry no meaning beyond the label, so they are mechanical and safe. Every
risky occurrence is in prose. Keeping them in one pass is what makes a sweep feel proven when only
its safe half was.

**Planned outputs**
- 138 task files, `work_package` only
- [`README.md`](README.md), [`../.handoff/config.md`](../.handoff/config.md), and the task prose that
  names a label

## 3. Implement

### Step 1 — the count, and what it corrected

```text
work_package: 138   other front matter: 3   prose to read: 352   inside the generated block: 141
```

**The three are the reason this step exists.** §2 D4 asserted that front matter was mechanical
because it held nothing but the label. It holds titles too, and three of them name a label:

```text
tasks\T-124-...:3  title: Stop a test asserting this repository has open v0.2 work
tasks\T-125-...:3  title: Ship the completed v0.2 work as 0.4.0
tasks\T-129-...:3  title: Release v0.5
```

A plan written an hour earlier was wrong about the population it had just partitioned, and the count
is what said so rather than the reading. The 141 inside the generated block need no decision at all —
`index` rewrites them from front matter, which is the design rule paying for itself here.

### Step 3 — the classification, and the rule that made it mechanical

89 of the 352 prose occurrences sit on a line that also carries a real version or a naming word.
Reading those 89 produced one rule that decides every case:

> **A label names a set of tasks. A quotation names words.** A sentence referring to the set is
> renamed, because the set is what was renamed. A sentence reporting what somebody said is not, because
> renaming it would misreport them.

That splits cleanly into four keeps: whole files whose subject is the naming itself
([T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md), this file,
[T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md),
[T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md)); quoted instructions from the
maintainer; a quoted line from a published release note; and recorded command output, which is never
edited whatever it says.

### Step 2 and 4 — the sweep, and the guard proven before it ran

The guard was proven by making it fail. It ran twice on one seeded line, once with the pattern in use
and once with the naive pattern the lookahead exists to prevent:

```text
naive (no lookahead)   ABORT - refused to write
  before ['v0.2.0', 'v0.1.5']
  after  []
  result The `M2` work shipped as `M2.0` and the tag `M1.5` is untouched.
shipped pattern        written
  before ['v0.2.0', 'v0.1.5']
  after  ['v0.2.0', 'v0.1.5']
  result The `M2` work shipped as `v0.2.0` and the tag `v0.1.5` is untouched.
```

Then 135 files, and it never aborted.

**Two things the sweep got wrong, and both were found by counting rather than by reading.**

**The unit was still too coarse, in the same way the other project's was.** Their keeps were per file;
mine were per line, and a log row here is one line of 900 characters carrying a quotation *and* five
paraphrases. Nine files kept six tokens each where they should have kept one. Protecting the span
between the quote marks instead of the whole line fixed all nine at once; three more, whose quotation
is italic-delimited rather than quoted, were done by hand. **The principle was right both times and
the granularity was not, which is the part worth carrying: an exclusion rule is only as good as the
smallest thing it can name.**

**A substitution map cannot see a label nobody used.** T-087 argues about `--work_package v0.4`, a
label that never existed — so it was absent from the map, survived the sweep, and left the file
mixing `M1` with `v0.4` in one sentence. Three tokens, renamed after the recount. The pattern found
them; the map is what decided, and its completeness is bounded by the labels in use rather than by
the shape.

### Step 6 — no version was touched, enforced across the whole tree

Every tracked Markdown file compared against `HEAD`, by multiset of version tokens:

```text
218 tracked markdown file(s) compared against HEAD
  .handoff/config.md
    lost   ['0.4.0', '0.5.0']
    gained []
  tasks/README.md
    lost   ['v0.1.0', 'v0.4.0']
    gained ['0.4.0', 'v0.3.0']
```

**Two files, both hand-edited on purpose, and no other file in the repository moved a version token.**
Both losses are the mapping sentences being deleted; both gains are the two exceptions being written
once. The 136 files the tool swept are unanimous.

**Decisions & assumptions**
- **D5 — a quotation is not renamed; everything else that refers to the set is** — 2026-08-12, step 3.
  This is the rule the whole sweep rests on, and it is what makes *what about the past* answerable
  without an exclusion list: METHOD rule 5 protects statements about the past, and a quotation is one.
  A label in a closed task's prose is not — it is an index entry, and it must keep reaching the same
  set or the record stops being findable.
- **D6 — the three titles are renamed, and their filenames are not** — 2026-08-12. A title is shown in
  every generated view, so leaving it version-shaped defeats the task. The slug is opaque and already
  does not track its title elsewhere in this repository. *Rejected: rename the files too* — it would
  break every link to three well-cited tasks to fix a string nobody reads.
- **D7 — the mapping table is replaced by naming only the exceptions** — 2026-08-12. Two sentences:
  `M2` shipped as `0.4.0`, and `M3`'s tasks went out inside the `v0.3.0` batch bump. A row per label
  is a second copy of a fact each task already carries and goes stale when a label is added; naming
  the exceptions cannot, because a new label that behaves is not an exception.
- **Assumption: no schema or config change is needed.** `work_package` is named and not enumerated, so
  a new value needs no vocabulary row — the same assumption T-128 recorded, re-proven by `check`
  reporting 0 vocabulary rows and by both `list --work_package M5/M6 --open` queries returning the
  memberships their old labels had.

**Outputs produced**
- 138 task files — `work_package` in all of them, three titles, and the prose in 135
- [`README.md`](README.md) — the *Releases* section, with the mapping table deleted
- [`../.handoff/config.md`](../.handoff/config.md) — the paragraph that existed to teach the ambiguity
- [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) — one dated row recording that the
  remedy it chose was replaced, and that its own prose keeps the old names on purpose

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| No tracked file contains a version-shaped `work_package` value, and every surviving `v0.N` is named rather than grepped away | met | `work_package: 0` across 218 tracked files, and T-137's own detector reports no dotted-number front-matter value in 142 files. 92 prose survivors in 20 files, each accounted for in §3 step 3: 66 in the four files whose subject is the naming, 12 quotations one per file, 5 in the README sentence that says what the labels were, 2 in the handoff config saying the same, 6 in T-087's typo example and its recorded output, 1 illustration in T-138 |
| The substitution is proved not to have touched a version, and the guard is shown to abort | met | §3 step 6: two files moved a version token, both hand-edited, both intended; 216 did not. The guard aborts on the naive pattern, §3 step 2 — it was made to fail before it was trusted |
| `check` and `index` green, membership unchanged, suite passes | met | `OK - 138 task(s)`, 0 problems. `list --work_package M5 --open` returns T-085; `--work_package M6 --open` returns the eight. 236 tests, `OK (skipped=3)` |
| The mapping table is gone and the page answers the question without one | met | Deleted. Replaced by two sentences naming the two exceptions, D7 |
| Every sentence whose subject is an old label still says what it said | met | 89 candidates read before anything was substituted, which is the step that licensed using a tool. Two granularity defects found afterwards by recounting, both repaired: nine over-kept quotation lines and three tokens outside the map |
| `.handoff/config.md`, `CLAUDE.md` and `docs/BRIEF.md` read correctly, and T-128 records the reversal | met | `CLAUDE.md` and `BRIEF.md` never named a label — neither appears in the survivor list or the swept list. T-128 carries a dated row saying its remedy was replaced, that its D3 still stands, and that its prose keeps the old names deliberately |

**Child fix tasks raised**
- none

**One residual, recorded rather than raised.** *Which release did this task ship in* is now answered
by the label's digit plus two named exceptions. It could instead be derived per task from the first
tag containing its closing commit, which is uniform and cannot drift — the route the adopting project
took. It is not raised because it needs a tool feature nobody has asked for, and the hand-written
residue it would remove is two sentences. If a third exception ever appears, that is the moment.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | (no change, closed) | **The residual above was put to the project owner and declined**, 2026-08-12: *which release shipped this* stays the label's digit plus the two named exceptions, rather than being derived per task from the first tag containing its closing commit. The reason to revisit is stated in §4 and has not changed — a third exception. |
| 2026-08-12 | → done | All six criteria met. **Counting corrected the plan twice, and reading corrected it once.** §2 D4 said front matter was mechanical; it holds three titles that name a label, and the count said so an hour after the plan was written. The keep-rule was right and its granularity was wrong in exactly the way the other project's was, one level down: their unit was a file, mine was a 900-character log line carrying a quotation *and* five paraphrases, so nine files kept six tokens where they should have kept one. And a map cannot see a label nobody used — T-087 argues about `M4`, which never existed, so it was absent from the substitution map and survived a sweep whose pattern had found it. **The rule that made the other 352 mechanical is worth more than the rename**: a label names a set and a quotation names words, so the set is renamed everywhere and the words nowhere, which answers *what about the past* without an exclusion list. The tell that started this is gone — the mapping table between two of this project's own label spaces was the one feature this plugin's design rule forbids, kept by the project that ships the rule. |
| 2026-08-12 | → in_progress | Plan agreed under the owner's authorisation of 2026-08-12. Run after [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) on purpose: that task needed this tree while it still had the defect. |
| 2026-08-12 | → specified | Both questions answered by the project owner: keep the digit and change the shape, and rename closed tasks too. Their rivals are recorded beside them rather than dropped. **Authorisation (METHOD §3.1):** *full lifecycle on T-136 and T-137*, from the project owner on 2026-08-12, given with the answers. It covers this task end to end — specify through review — and nothing beyond the two tasks it names. |
| 2026-08-12 | → proposed | Raised after an adopting project hit the same defect and fixed it, and the maintainer asked for this repository's version of that work. **T-128 already named this problem and chose the cheaper remedy, correctly**: it priced the rewrite and bought protection for the release sequence, which is where the failure had happened. What it could not price was the reading cost, and the `v0.3` row is what came due — four closed tasks whose label resolves to a real tag, correctly and by accident, with no row in the table that exists to catch exactly that. Split from [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) for the reason T-128 was not folded into [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md): re-labelling a backlog and changing what the tool ships are different outcomes, and one diff carrying both is reviewable as neither. |
