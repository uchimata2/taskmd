---
id: T-172
title: Catch a template placeholder left in a finished record
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-171, T-151, T-032, T-173]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-18
updated: 2026-08-18
adopter_visible: yes
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, tests/fixtures/abandoned-slot/tasks/T-001-closed-with-a-slot-nobody-filled.md, README.md, plugin/skills/taskmd/docs/bindings/local-markdown.md]
---

# T-172 — Catch a template placeholder left in a finished record

## 1. Specify

**Outcome**
Finished task records that no longer carry unfilled scaffolding from
[`_task-template.md`](_task-template.md) — and a ruling, settled by running something rather than by
argument, on whether `check` is the thing that should have caught them.

**Why this one**
Found on 2026-08-18 while reviewing
[T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md), in a record T-171 had just
annotated. It is raised separately rather than fixed there because it fails none of T-171's criteria
and has nothing to do with what T-171 tested — `review` §*What review is not* sends a problem found
outside the criteria to its own task.

Measured on the tree the same day, not estimated:

```
task files with a DUPLICATED 'Child fix tasks raised' heading: 5
  T-037-delete-the-throwaway-proof-repository.md
  T-059-audit-the-whole-project-after-the-plugin-restructure.md
  T-140-restore-the-log-row-a-table-cell-swallowed.md
  T-141-report-a-table-row-with-more-cells-than-its-header.md
  T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md

files still holding the unfilled placeholder line: 6
```

> **Annotated at `specify`, 2026-08-18 — the figure above does not reproduce, and the reason is
> instructive.** Re-resolved against the tree with a rule that derives the slot lines from the
> template instead of naming them: the *Child fix tasks raised* slot sits in **5 task files**, and in
> **both shipped templates**, where it is correct and where [T-032](T-032-repair-the-audit-template-and-validate-templates.md)
> established it must stay. So `6` counted templates in the same total as tasks — the one denominator
> this class cannot use, since the template is the source the copies are judged against. The count is
> left as written because it is what was measured at `raise`; what replaces it is below, and the
> scope's instruction to re-resolve at `implement` stands regardless of either number.
>
> **The class is also larger than one line.** Deriving *every* slot-bearing line from the template
> gives 9 of them, and they sit in **13 task files across 17 lines** — the *Decisions & assumptions*
> slot is the most common by some way, not the *Child fix tasks raised* one this record was raised
> on. The single line in the block above was the specimen, not the class.

The shape in [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md)
is the clearest: the heading appears **twice**, once answered `none` and once still reading
`<T-NNN or "none">`. A reader cannot tell whether the placeholder is an oversight or an open item.

**What makes it worth a record rather than a tidy-up.** `check` returns `exit=0` on every one of these
files. So this is not five typos; it is a class the validator does not see, in the one artifact this
project uses to argue that its records stay honest. Two of the five affected records are themselves
about defects in table and log structure, which is the kind of coincidence worth not laughing off.

**Scope**
- In: the five records above, and any the sweep finds when it is re-run at `implement` — resolve the
  set against the tree, never against the list quoted here
- In: the ruling on whether `check` gains a rule for it, taken by **building the rule and reading its
  alarms on this corpus**, which is how this project has settled in-or-out questions before
- Out: changing [`_task-template.md`](_task-template.md) itself. The placeholder is correct *in* the
  template — that is what a template is — and a fix that mangles the source to protect the copies is
  the wrong end
- Out: any other placeholder class nobody has measured. If the sweep turns one up, it is a finding and
  gets its own row, not a silent widening of this one

**Inputs**
- [`_task-template.md`](_task-template.md) — where the placeholder legitimately lives
- The five records named above
- [T-032](T-032-repair-the-audit-template-and-validate-templates.md) — **the lead is resolved, at
  `specify` on 2026-08-18, and it is prior art rather than the task that should have caught this.**
  Its `check_template_fields` validates a **template's own front-matter** — that the template will not
  produce an invalid task. It never looks at a task, and it explicitly **skips angle-bracket slots**,
  recorded there as *a placeholder is not a defect*. That ruling is right where it was made and is
  exactly inverted here: the thing a template may keep is the thing a finished record may not. So
  T-032 supplies the mechanism and the precedent for deriving a rule from the template, and leaves
  this class untouched. Neither task's decision needs revisiting

**Acceptance criteria**

Drafted at `specify` and **agreed by the owner on 2026-08-18**, after the rule was built and its
alarms on this corpus were shown. The raise deliberately left them unwritten so they would not be the
finder's; they are recorded here now that the owner has ruled.

- [ ] **No record carries a template slot line in a section it has already passed** — shown by running
      the rule and reading its exit status, never by inspection. Failure looks like: the rule reports
      one line and a person has already called the sweep finished

      > **Amended at `implement`, 2026-08-18, by the owner.** It read *no record in `tasks/` carries a
      > template slot line verbatim*. Measured, that demands an implementation section be written into
      > ten tasks that have not been implemented — the criterion was drafted before anyone had counted
      > how much of the class was open work, and it made fiction a pass condition. The gate replacing
      > it is the decision recorded in §3.
- [ ] **The rule derives its slot set from the shipped template**, so adding, changing or removing a
      slot there needs no second edit anywhere. Failure looks like: a slot line added to the template
      is not flagged when it is abandoned in a task
- [ ] **The rule is shown *failing* on a purpose-built fixture** (R-16, `CLAUDE.md` *Verifying*) — a
      clean-tree pass proves nothing. Failure looks like: the fixture is added and the suite is green
      before the rule exists
- [ ] **A record can document this class without tripping it.** A slot line quoted inside a fenced
      code block is a quotation and is skipped; the same line in ordinary body text is scaffolding and
      is reported. Failure looks like: the task explaining the rule, or the fixture's own prose, is
      flagged by it

**Open questions**
- **Does `check` own this class at all?** A validator that reports unfilled scaffolding is also a
  validator that fires on any record legitimately quoting the template — this very file quotes it
  twice. **The owner answers, at `specify`**, and the honest way to put the question is to build the
  rule first and show what it flags here.

  **Built and run on 2026-08-18, before asking.** The rule derives the slot lines from the template
  and flags a task line only when the whole stripped line is identical to one of them. On this corpus
  it reports 17 lines in 13 files and **nothing else** — and, decisively for the question as posed,
  **it does not flag this record**, whose two quotations of the template are inline in prose. Whole-line
  identity is what buys that: a quotation carries surrounding words, an abandoned slot does not. The
  feared false-positive class is not merely small here, it is **empty**.

  **Answered by the owner on 2026-08-18: yes, `check` owns it.** The objection the question rested on
  was tested rather than argued, and it did not hold. What decides it is that `check` currently
  returns `exit=0` on all 13 — a validator silently passing the artifact class this project uses to
  argue its records stay honest is the defect, not the untidy files.

  *Rejected: clean the 13 files and add no rule.* Cheapest today, and it makes this task an instance
  repair whose class returns the next time someone copies the template and stops early — which is what
  produced all 13. *Rejected: report the lines advisorily, without failing the exit code*, in the shape
  of the existing scope line. It catches the class and blocks nobody, which is also the reason to
  refuse it: nothing here would have been fixed by a line that scrolls past.
- **Does the rule skip fenced code blocks? — new at `specify`, and the corpus cannot answer it.**
  Zero of the 17 hits are inside a fence, so skipping and not-skipping score identically on today's
  tree; choosing by that measurement would be reading noise. It has to be decided by construction,
  because the case is not hypothetical — **writing this task up is the way to produce one.** Any
  record that shows the defect by reproducing a slot line on a line of its own becomes an instance of
  it. This record is written to avoid that (slots are named, never reproduced), which is a constraint
  the fix must not silently rely on every future author obeying.

  **Answered by the owner on 2026-08-18: skip fenced blocks.** A fence is an explicit *this is a
  quotation* marker, and the template's own slots never sit inside one — so skipping forfeits no real
  catch. It is decided by construction and **not** by the measurement, which could not separate the
  options; recorded that way so a later session does not read the zero as evidence.

  *Rejected: flag inside fences too.* Maximal catch, and it guarantees that the fixture, the shipped
  docs and any future record explaining the rule all trip it — the failure mode where documenting a
  checker re-creates what it catches. Acceptance criterion 4 now holds this answer, so reversing it
  means failing a criterion rather than editing a preference.
- **Does the publishing constraint raise the value above `low`?** The records are in a public
  repository, so a stranger reading T-169 meets an unresolved placeholder. Set `low` because no
  behaviour is affected; the owner may disagree.

  **Answered by the owner on 2026-08-18: `low` stands**, with the re-measured count in front of them.
  *Rejected: raise to `medium` on the strength of 13 public records rather than 5.* The count tripling
  changes the size of the class and not its kind, and no behaviour is affected either way.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-derive the slot set from **every** template `check` loads, not the one the scan used, and re-resolve the affected records against the working tree | The corrected slot set and file list, recorded in §3 as the figure the repair is measured against |
| 2 | Read [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) and follow whatever it settled about must-not-fire cases | A stated decision in §3: the shape criterion 4's fenced case takes, and whether it is this project's existing convention or a departure |
| 3 | Write the rule as a new problem class in `check`, deriving its slots from the loaded templates, skipping fenced blocks, and **gated on phase-passed-or-closed** per §3's decision | `check_abandoned_slots` in plugin/skills/taskmd/taskmd/cli.py, wired into `cmd_check` |
| 4 | Build the fixture — the class in its reporting form, **and the two cases that must stay silent**: a fenced quotation, and an unreached section in an open task | tests/fixtures/abandoned-slot/, tests/test_cli.py, and the failing output quoted in §3 |
| 5 | Repair the one affected record | tasks/T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md |
| 6 | Re-run `check`, `index` and the suite; record each as output rather than as "green" | The evidence block in §3 |
| 7 | Reconcile the binding, which states what `check` validates about templates and records | plugin/skills/taskmd/docs/bindings/local-markdown.md |

**Step 1 is first because it can invalidate the rest.** The `specify` scan derived its slots from
`_task-template.md` alone, while `check` loads **two** templates — so a slot unique to the audit
template is a class member the scan could not see, and the 13/17 figure is a floor rather than a
count. It is cheap to settle and everything downstream is measured against it.

**Steps 3 and 4 precede step 5, and that ordering is the point** — the same one
[T-032](T-032-repair-the-audit-template-and-validate-templates.md) recorded when it built
`check_template_fields` before repairing the template it was raised on: the repair is then proved by
the mechanism that has to keep proving it, rather than by the reading that missed the defect in the
first place. Reversing them would satisfy criterion 1 and leave criterion 3 unprovable, because a
rule written after a clean tree has nothing left to fail on.

**Decision — the rule reports on task records only, not on every document `check` reads.** `check`
walks 202 documents; scaffolding is a property of a file copied from a task template, so a project
doc containing a slot-shaped line is not this defect. *Rejected: scan every document.* It widens the
blast radius to prose nobody templated, and the first false positive would land on documentation
explaining the rule — the failure mode criterion 4 exists to prevent.

**Not planned past step 4.** If step 1 turns up a slot class the scan did not model, or T-151 settled
the must-not-fire question in a way that changes the fixture's shape, steps 5–7 are re-cut then
rather than invented now.

**Outputs promised**
- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/abandoned-slot/
- tests/test_cli.py
- plugin/skills/taskmd/docs/bindings/local-markdown.md
- the affected task records under tasks/, as resolved by step 1

## 3. Implement

**Step 1 — the predicted risk did not materialise, and a different one did.**

Re-derived from **both** templates rather than one. The slot set grows from 9 lines to **14**, of
which **5 are unique to the audit template**. The affected set is unchanged: still **13 files, 17
lines**, and **0 slot lines sit inside a fence**. So no audit-only slot is abandoned anywhere, and the
floor the plan worried about equals the count. The rule must still derive from every template loaded,
because that is true by construction rather than by today's tally — this corpus cannot distinguish the
two designs, which is the same reason the fence question was decided by construction at `specify`.

**Step 2 — [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) has not decided
anything yet.** It is `proposed`, and its subject is exactly whether a validator needs a case that
must not fire. So criterion 4's negative case is not this project's settled convention; it is a
practice three fixtures follow, which is the observation T-151 exists to rule on. Building one here
neither pre-empts nor waits on that: T-151's scope already excludes auditing existing checks and says
that work is its own task. **T-151 is also one of the 13 affected files**, which is how the next
finding was noticed.

**The finding that stops the plan: 10 of the 13 are not defects.**

| | Files | Where the slot sits |
| :--- | :---: | :--- |
| **Open**, all at `phase: specify` | 10 | `3. Implement` / `4. Review` — sections the task **has not reached** |
| **Closed** (`cancelled`) | 2 | `3. Implement` / `4. Review` — never reached, because the task was stopped at `specify` |
| **Closed** (`done`) | 1 | `4. Review` — [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md), the original specimen |

An unfilled `3. Implement` in a task at `phase: specify` is not an abandoned placeholder. It is the
normal, honest state of a young record, and this task's own title says so — *left in a **finished**
record*. Criterion 1 as agreed says **no** record in `tasks/` carries a slot line; applied literally it
requires writing an implementation section into ten tasks that have not been implemented, which is
fiction. The criterion is wrong, not the corpus.

**This also falsifies the evidence the owner's first answer rested on.** *Zero false positives* was
measured against the class as a set of lines. Measured against the class as this task defines it, the
same run is **10 false positives in 13 files — 77% noise**, on a rule that would move the exit status.
That is precisely the failure T-151's reporter described losing a specimen to, and T-151 is in the
sample. So the question goes back to the owner with the corrected figure rather than being resolved
here: evidence licenses re-opening an answer, it does not license reversing it.

**Decisions & assumptions**
- **The plan was held at step 2 until the owner ruled** — 2026-08-18. The plan said it was not planned
  past step 4 for exactly this reason. Re-cutting it before the gate was chosen would have baked in
  whichever one I preferred, and the gate is what moves the task's product from 13 repairs to 1.
- **The gate is phase-aware, plus closed** — owner, 2026-08-18. A slot is abandoned when it sits in a
  section the task's `phase` has already passed, or anywhere in a closed record. Both halves are
  needed and neither is redundant: the phase half alone misses T-169, whose slot is in `4. Review`
  while its phase *is* `review`; the closed half alone says nothing until a task closes, so a record
  sitting at `review` with an unfilled `implement` goes unreported for as long as it stays open.

  *Rejected: closed records only.* Simpler to write and to explain, and it defers every catch to the
  end, which is the point at which the author has stopped looking. *Rejected: no gate, the rule as
  first measured.* It is the one option the evidence rules out — 10 false positives in 13 files on a
  check that moves the exit status.
- **`cancelled` is not finished for this rule** — owner, 2026-08-18. T-158 and T-167 were both stopped
  at `specify`, so their untouched later sections record accurately where the work halted. *Rejected:
  treat closed as closed regardless of reason.* It reads tidier and it would have filled in two
  records to describe work that was deliberately never done — the same fiction the amended criterion 1
  exists to refuse, arriving by a different route.
- **The affected set is therefore 1 file, not 13** — 2026-08-18. T-169, the specimen the task was
  raised on. Recorded because the raise measured 5, `specify` re-measured 13, and the number that
  survives the task's own definition is 1; a later reader meeting three figures should find the reason
  they differ rather than reconcile them.

**Step 3 stopped: the agreed gate is not derivable, and nobody could have seen that at `specify`.**

Reading `schema.py` to write the rule, against the shape `check_template_fields` established:

| The gate needs | Does the tool know it? |
| :--- | :--- |
| Whether a record is closed | **Yes** — `schema.is_open(status)`, from the existing `open_statuses` key |
| Which front-matter field carries the phase | **No** — `phase` appears nowhere in `schema.py`. It is this project's field, not the tool's |
| That a body heading maps to a phase value | **No** — nothing relates `## 3. Implement` to the value `implement` |
| That `done` and `cancelled` differ | **No** — `open_statuses` splits open from closed and stops there; both are simply closed |

`open_statuses` is `[proposed, specified, planned, in_progress, blocked, review]`, so closed is exactly
`{done, cancelled}` and the two are indistinguishable to the tool.

**So the phase half of the gate would require the checker to learn two pieces of this project's
vocabulary**, and the `cancelled` ruling a third. Hardcoding any of them puts a project's document
shape inside the tool, which is what `BINDING.md` exists to prevent and what the one design rule in
`CLAUDE.md` forbids — a fact written in a task file would then also be written in `cli.py`.

**And the phase half catches nothing here.** It was justified by a task sitting at `review` with an
unfilled `implement`; that shape exists **0 times** in 172 tasks. The closed half alone catches T-169,
which is the whole measured class. Deciding the expensive half on a corpus that cannot exhibit it is
the same trap the fence question was pulled out of at `specify` — so it goes back to the owner rather
than getting resolved by whichever design is quicker to type.

**Step 3 stopped a second time: the chosen config key is a breaking change, and the file says so.**

`finished_statuses` was chosen as the smallest addition that honours all three rulings. Adding it
means adding a name to `CONFIG_KEYS`, and `defaults/config.md` §*Adding a key to this file is a
breaking change* states the consequence in terms this task cannot argue with: a config **replaces**
the default rather than merging, so every key must be written, so a missing key is an error naming
it — therefore **every project that wrote its own config fails on its next upgrade**, in a project
that changed nothing. The same section records that **no key has been added since the schema
shipped**, and that optional keys and merge-on-upgrade were considered and rejected as larger than
the problem.

Priced against what it buys: **three live adopters** break, to catch a class with **one instance**,
on a task valued `low`. The remedy's target class is not empty, but it is a single file — and the
cost falls on people who did nothing.

**A route nobody has costed yet, found while pricing this one.** Gate on `open_statuses`, which
already exists — no key, no breaking change. It fires on all three closed records, including the two
`cancelled` ones the owner ruled should be left alone. But the ruling's *reason* was that filling
them in would invent work that was deliberately never done, and there is a third repair that invents
nothing: replace the slot with the sentence stating the phase was never run — which is exactly what
this record carried in its own unreached sections before `plan` was written. That honours the reason
while differing from the letter, so it is the owner's to accept or refuse, not this task's to assume.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `slot_lines` and `check_abandoned_slots`, wired into
  `cmd_check`. No config key, no new schema concept, and `SLOT` is the only pattern the tool owns:
  *which* lines are slots is read from the project's own templates
- `tests/fixtures/abandoned-slot/` — one project holding all three behaviours: the closed record that
  must report, the open task that must not, and the closed record quoting a slot in a fence that must
  not
- `tests/test_cli.py` — `SlotLeftInAClosedRecord`, six tests, including an exact alarm count so a new
  alarm breaks the suite rather than passing unnoticed
- `README.md` — the new problem class, and why open records are not read. The guarded sample run also
  gained the new denominator
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the *placeholders are not defects* ruling
  reconciled: still true of a template, now paired with what it means for a closed record
- Three records repaired: T-169 (the duplicate heading removed), T-158 and T-167 (the slot replaced
  with the statement that the phase was never run, since both were cancelled at `specify`)

**Evidence**

Shown **failing** on the real corpus, before any record was repaired — the class as the gate defines
it, three files and four lines:

```
ABANDONED SLOT tasks/T-158-phase-2-grade-each-band-against-what-it-bought.md body line 63 ...
ABANDONED SLOT tasks/T-167-stop-the-listing-pricing-only-the-rival.md body line 80 ...
ABANDONED SLOT tasks/T-167-stop-the-listing-pricing-only-the-rival.md body line 92 ...
ABANDONED SLOT tasks/T-169-...-path-scoped-rule.md body line 288 ...
4 problem(s) - 172 task(s), ..., 160 closed record(s), ...
exit=1
```

The first run printed an **absolute machine path** instead of a repo-relative one, which the
publishing constraints forbid; `task.path` is absolute and the other checks reach `rel` through
`os.path.relpath`. Fixed before going further, and recorded because a clean second run is exactly
where that would have stopped being visible.

On the fixture — the alarm and both silences in one run, which is the half a positive case cannot
show:

```
ABANDONED SLOT tasks/T-001-closed-with-a-slot-nobody-filled.md body line 31 ...
1 problem(s) - 3 task(s), ..., 2 closed record(s), ...
```

Three tasks in the fixture, **two** closed records examined: the open task is outside the denominator
as well as outside the report, so the gate is visible in the summary and not only in the silence.

After the repairs, and after regenerating the index:

```
OK - 172 task(s), 860 field value(s), 581 reference(s), 24 dependency edge(s), 264 declared
output(s), 1 index file(s), 202 document(s), 2061 link(s), 3588 table row(s), 2 template(s),
10 template field value(s), 160 closed record(s), 0 vocabulary row(s), 2510 front-matter value(s)
exit=0
```

Suite **275 passed**, 3 skipped, 6 subtests (269 before). Two failures were found and fixed on the
way, both of them the suite doing its job rather than incidental breakage:

- `test_the_readme_sample_run_is_what_the_command_prints_today` — every new check changes the summary
  line by construction, so the README's quoted run went stale the moment the denominator was added.
  Re-run and diffed rather than generated, per the owner's 2026-08-16 ruling in T-147
- `test_no_covered_document_carries_an_em_or_en_dash` — two lines of the new README prose. Rewritten
  rather than find-and-replaced, per `docs/PUBLISHING.md` §2

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| No record carries a template slot line in a section it has already passed | **met in part** | Met for **closed** records: `check` reports them, three were repaired, and the tree is clean at exit 0. **Not met for an open record past the section** — a task at `review` with an unfilled `implement` is still unreported. That half was not dropped here; it was dropped by the owner's own later decision, once pricing it showed the phase gate needs three pieces of project vocabulary and the config key to carry them breaks every adopter. The gap is carried by [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) rather than buried in this note |
| The rule derives its slot set from the shipped template, so changing a slot needs no second edit | met | `slot_lines` reads `templates(root, schema)`; `cli.py` names no slot. Proved by removing the template from a copy of the fixture and watching the rule fall silent — `test_the_slots_come_from_the_project_s_own_template`, which fails if anyone ever hardcodes the list |
| The rule is shown **failing** on a purpose-built fixture | met | `tests/fixtures/abandoned-slot/`, exit 1 on `T-001`, quoted in §3. It was also shown failing on the real corpus **before** any record was repaired, which is the stronger evidence of the two and is the ordering the plan took from T-032 |
| A record can document this class without tripping it | met | `T-003` in the fixture is a closed record quoting a slot inside a fence, and stays silent. This record is the second instance: it discusses the class throughout and `check` returns 0 on it. Both are asserted, so the fence behaviour cannot regress unnoticed |

**Open questions at close** — all three from `specify` are answered in §1 with their rejected
alternatives, and the fourth raised at `specify` (fenced quotations) is answered there too. Nothing is
addressed to anyone outside this record, so nothing goes invisible when it closes.

**Child fix tasks raised**
- [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) — the phase
  half of the gate, carrying criterion 1's unmet part.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | Plan through review in the same session, under the maintainer's whole-lifecycle authorisation. Three criteria met, one met in part and carried by [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md). **The task was interrupted four times, each by evidence the previous answer produced**, and the sequence is the record's most useful part: the class was 5 at `raise`, 13 at `specify` when it was re-measured against the tree, and **1** once the task's own word *finished* was applied to it — 10 of the 13 were open tasks whose slots sat in sections they had not reached. Then the agreed phase gate turned out to need three pieces of project vocabulary the tool has never had, and the config key to carry them would have broken every adopter for a shape occurring 0 times in 172 tasks. What shipped is the half that needed no new vocabulary at all. Two suite failures on the way were both guards working: the README's quoted `check` run went stale by construction the moment a denominator was added, and two lines of new prose tripped the dash gate. |
| 2026-08-18 | → planned | Seven steps, under the same lifecycle authorisation. Step 1 is first because it can invalidate the rest: the `specify` scan derived its slots from one template and `check` loads **two**, so 13 files / 17 lines is a floor and not a count — a slot unique to the audit template is a class member nothing has yet looked for. The check-before-repair ordering of steps 3–5 is [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s, cited rather than re-argued. Two soft edges added while planning: T-032 for that precedent and the inverted placeholder ruling, and [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) because acceptance criterion 4 needs a case that must **not** fire and that task exists to settle what one looks like — reading it is step 2 rather than an assumption. One decision recorded with its rejection: the rule reads task records only, not all 202 documents `check` walks. |
| 2026-08-18 | → specified | Three owner questions answered in one turn (METHOD §3.2), each with its rejected alternative recorded above, and the four acceptance criteria agreed. The question about `check` was put the way the raise demanded — **the rule was built and run on this corpus before it was asked**, so the objection it rested on could be tested instead of argued, and it did not survive: whole-line identity flags 17 lines in 13 files and does not flag this record, which quotes the template twice. Two things the raise did not expect came out of the same run and are annotated in §1 rather than rewritten there: the quoted figure of `6` **counted both shipped templates alongside the tasks**, the one denominator this class cannot use, and the class is **9 slot lines rather than 1**, most commonly the *Decisions & assumptions* slot rather than the one the task is named for. A fourth question was raised and answered here — whether the rule skips fenced quotations — and it is the one the corpus **could not** settle, since zero hits sit in a fence; decided by construction and recorded as such, so a later session does not read that zero as evidence. |
| 2026-08-18 | — | **The maintainer authorised this task's whole lifecycle** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. It covers **T-172 and nothing it raises**. Recorded here rather than only in the handoff that carried it, because a handoff is consumed once and renamed, and an authorisation kept only there is one the session after next cannot find (METHOD §3.1). Two things it does **not** license, both because the record says so rather than because a session should infer them: the acceptance criteria are still `specify`'s to write **with the owner**, since this record was raised by the session that found the defect and criteria written by a finder are criteria the fix passes by construction; and the open question about whether `check` grows a rule is addressed to the owner, not answerable by running the lifecycle. |
| 2026-08-18 | → proposed | Raised from [T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md)'s `review`, and deliberately **not** as its child: it fails none of T-171's criteria and shares no subject with it, so a parent edge would say something false about why it exists. `fix` and not `decision` because the five records are wrong by inspection and cleaning them needs nobody's ruling; the one thing that does need a ruling — whether `check` grows a rule — is an open question inside it rather than the task's purpose. The count was **measured on the tree, not estimated**, and the scope says to re-resolve it at `implement` rather than trust the list quoted in this record. Acceptance criteria are left for `specify` on purpose: written now, by the session that found the defect, they would be criteria the fix passes by construction. |
