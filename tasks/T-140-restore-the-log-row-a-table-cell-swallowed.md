---
id: T-140
title: Restore the log row a table cell swallowed in T-099
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-099, T-141]
work_package: M6
owner: the project owner
business_value: high
effort: xs
created: 2026-08-15
updated: 2026-08-15
adopter_visible: no
deliverables: [tasks/T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md]
---

# T-140 — Restore the log row a table cell swallowed in T-099

## 1. Specify

**Outcome**
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)'s log carries the
`→ proposed` row it was written with, so the reason a `critical` task was raised is readable again
by whoever reads that record next.

**Why this one**
Found on 2026-08-15 by scanning every Markdown table in this repository for a body row holding more
cells than its header — the failure the htmldeck adopter report describes as `O-T4`. The whole tree
has exactly one such row, and it is T-099's.

The provenance is exact. At `d56486f` the log held five rows, and the last was a full
`→ proposed` entry recording where the task came from, why it was `critical`, why it was `s`, and
the two facts it did not want `specify` to rediscover. At `2810997`, the commit that closed the
task, that row lost its leading `| <date> | → proposed | Raised as R-1 from the first adopting
project's recommendations,` and the rest of the sentence became a **fourth cell on the row above
it**, which has a three-column header.

**What that costs, and why it went unseen for five days short of a week.** GitHub-flavoured Markdown
drops a cell past the header, so the text is in the file and renders nowhere. Every instrument this
project owns said the tree was fine: `check` was clean, the suite was green, the pre-publish gate
printed its count and nothing else. The task also reads as complete — a log with four plausible rows
does not look like a log missing one. So the only reader who could have caught it is one comparing
the file against a commit five days older, and nobody had a reason to.

**Two things are lost, not one.** The rationale is the obvious loss. The other is the attribution:
`Raised as R-1 from the first adopting project's recommendations` is the sentence that says T-099
came from an adopter at all, and it is the half that vanished completely rather than being displaced.

**Scope**
- In: T-099's log, restored to the five rows the file was written with.
- In: how the restoration is marked, given METHOD §1.5 — *correct what the record says about the
  present, never rewrite what it says about the past, annotate instead*. A row that was written,
  then damaged by a later edit, is arguably neither.
- Out: the class. [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) owns whether
  anything catches the next one, and fixing the instance must not be read as covering it.
- Out: any other edit to T-099. Its findings, decisions and criteria stand as reviewed.

**Inputs**
- [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md), the damaged row.
- `d56486f`, which holds the row as written.
- `2810997`, the close commit that damaged it.

**Acceptance criteria**
- [ ] T-099's log holds five rows, and the restored one carries the text at `d56486f` rather than a
      paraphrase of it
- [ ] No row in the file has more cells than its header, shown by re-running the scan over the whole
      tree rather than by reading the one file
- [ ] The restoration is visible as a restoration, so a later reader is not left thinking the row was
      always there
- [ ] `check` and the suite are green, and the file still renders as four phases and one log

**Open questions**
- ~~**Does an annotation belong on the restored row?**~~ **Decided at `specify` on 2026-08-15: yes,
  and not on that row.** The question assumed one placement and there are two, which is what dissolves
  it. The `→ proposed` row goes back **verbatim and unmarked**, because it is T-099's account of
  2026-08-10 and any mark on it would be this project editing what the record says about the past —
  the thing METHOD §1.5 forbids. The annotation is a **separate log row, dated today**, saying the
  row was damaged by a later edit and restored. That row is about the present: what the file has been
  through, which is a fact of 2026-08-15 and not of 2026-08-10.

  *Rejected: restore the row silently.* It is the smaller edit and it leaves T-099 reading exactly as
  written, which has real appeal for a closed record. What decided it against: a row materialising in
  a closed task is precisely the shape a later reader cannot check, and this task exists because
  nobody could tell that something had gone missing. Putting a row back with no account of why
  reproduces that, one direction reversed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Take the row from `d56486f` as bytes rather than by reading and retyping it | The extracted file in a scratch directory |
| 2 | Locate the seam in the damaged row, so the restored text is joined at the character the edit cut | The seam, recorded in §3 |
| 3 | Close the over-wide row and put the `→ proposed` row back below it, in one edit | `tasks/T-099-...md` |
| 4 | Add the annotation row the open question settled, dated today, at the top of the log | the same file |
| 5 | Re-run the whole-tree scan, not the one file, and confirm the count goes to zero | Recorded output |
| 6 | `index`, `check`, the suite, and a line-ending check, since the repository is pinned to `eol=lf` | Recorded output |

**Why step 1 is an extraction and not a transcription.** The row is 700-odd characters of prose
carrying two backticked identifiers and an em dash. Retyping it would produce something that reads
correctly and is not what the record said, which is the failure this task exists to repair rather
than to repeat.

**Why step 5 scans the tree.** The second acceptance criterion asks for it, and the reason is
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md)'s: a check narrowed to the file
you just edited cannot tell you that it passed because there was nothing to find.

**Planned outputs**
- `tasks/T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md` — the log, five rows plus
  the annotation

## 3. Implement

### Step 2 — the seam

The damaged row's third cell ends `...rather than a hypothetical.` and the fourth begins
`which ranked it the largest of its seven divergences.` At `d56486f` that sentence read
`Raised as R-1 from the first adopting project's recommendations, which ranked it the largest...`,
so what the edit removed is a leading fragment: the date cell, the status cell, and the first nine
words of the note. Everything after the comma survived, one cell to the right of where it belonged.

**That is why nothing looked wrong.** The surviving text starts mid-sentence with a lower-case
relative clause, which reads as a continuation of whatever precedes it — and what preceded it was a
cell that had just finished a sentence. Two grammatical fragments abutting produced one row that
scanned as prose.

### Steps 3–4 — the edit

The row is joined at that comma, so the restored text is continuous with what survived rather than
appended near it. The `→ proposed` row now sits at the bottom of the log, where it was, and the log
runs five rows plus one.

The annotation is a `(no change, closed)` row dated 2026-08-15 at the top, per §1's answered
question. It says what happened, when it was found and how, and it does not touch the restored row.

### Steps 5–6 — proof, on the tree rather than the file

The tree, after:

```text
scanned 277 markdown file(s), 579 table(s), 2812 body row(s)
rows with more cells than their header: 0
```

**The tree cannot carry the before-and-after on its own, and the first write-up of this section
pretended it could.** Numbers were drafted from the pre-repair run and the arithmetic did not
survive contact with the second one: the tree gained twelve rows, not two, because this task's own
plan and review tables were filled in between the two scans, and the table count did not move at all
where the draft said it would. Recorded rather than quietly corrected, because a predicted figure in
an evidence block reads exactly like a measured one and nothing downstream re-checks it.

The isolating measurement, on T-099 alone at `HEAD` and in the working tree:

```text
damaged    scanned 1 markdown file(s), 3 table(s), 15 body row(s)
           rows with more cells than their header: 1
             T-099.md:284  header 3 cells, row 4 cells
repaired   scanned 1 markdown file(s), 3 table(s), 17 body row(s)
           rows with more cells than their header: 0
```

15 to 17 is the claim this task makes: two rows added, the restored one and the annotation. The
table count holds at 3, which is what separates this from the other repair available — deleting the
excess cell would have left 15 rows and also reported zero.

```text
taskmd index    Wrote tasks/README.md - 15 active, 131 closed
taskmd check    OK - 146 task(s), ... 2173 front-matter value(s)          exit 0
suite           245 passed, 3 skipped, 6 subtests passed
line endings    LF throughout; no CRLF introduced
```

**Decisions & assumptions**

- **The row goes back verbatim, and the account of what happened to it goes in its own row** —
  2026-08-15. §1's open question, answered at `specify` with the rejected alternative recorded there.
- **The restored row keeps its original date, not today's** — 2026-08-15. It records a status change
  that happened on 2026-08-10. Re-dating it would make the log say the task was raised five days
  after it was closed, which is a second falsehood in place of the first.
- **Nothing else in T-099 was touched** — 2026-08-15. Its findings, decisions and criteria stand as
  reviewed. The scope said so and it is worth stating as done rather than intended: a task that opens
  a closed record to fix one row is exactly where unrelated tidying gets in.

**Outputs produced**
- [`T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md`](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)
  — the log, restored and annotated

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Five rows, and the restored one carries the text at `d56486f` rather than a paraphrase | met | Extracted as bytes and joined at the seam, per plan step 1. Six rows in total, the sixth being the annotation §1 called for |
| No row wider than its header, shown by scanning the tree rather than the file | met | §3 steps 5–6. Zero over 2,812 body rows in 579 tables, counted after this record was written, since writing it adds rows. The tree run proves the criterion; the 15-to-17 run on T-099 alone is what distinguishes a restored row from a deleted cell, and it is there because the tree's own deltas turned out to be unreadable — see the correction in §3 |
| The restoration is visible as a restoration | met | A `(no change, closed)` row dated 2026-08-15, separate from the restored row, so T-099's account of 2026-08-10 is unedited |
| `check` and the suite green, and the file still renders as four phases and one log | met | §3 step 6, and the log renders as six rows of three cells |

**Beyond the written criteria**
- The repository is pinned to `eol=lf` and this machine's shells do not all honour that, so the edit
  was checked for line endings as well as for content. No criterion asked; the `.gitattributes`
  comment says why it would have mattered. Zero carriage returns in the file afterwards.
- **A drafted figure was caught in this task's own evidence block**, and it is worth naming because
  the task is about a record saying something untrue. The first §3 carried a before-and-after written
  from the first scan and the expected delta, not from the second scan. It was wrong in both
  directions — twelve rows rather than two, and a table count that did not move — and the reasoning
  built on it would have read as proof. Corrected in place, with what it got wrong left visible.

**Child fix tasks raised**
- none. The class is [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md), raised
  alongside this task rather than by it, and closing this one does not close that one — which is what
  the scope said and is repeated here because a repaired instance is the usual reason a class gets
  dropped.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → done | All four criteria met. Specify through review in one session, under the authorisation below. **The open question dissolved rather than being answered**: it assumed the annotation had one possible home, and once there were two the restored row goes back unmarked and today's row carries the account, so T-099's statement about 2026-08-10 is untouched while a later reader is not left with a row that materialised. The repair itself is nine words and two cells, and the useful half is why it was invisible — the surviving fragment began with a lower-case relative clause immediately after a cell that had finished a sentence, so two fragments abutted and read as prose. **This task then produced the same class of fault in its own evidence and caught it**: §3's before-and-after was drafted from one scan plus an expected delta rather than from two, and was wrong about both numbers. It is corrected in place with the error visible, because a task about a record saying something untrue cannot quietly fix its own. The class stays open as T-141, and a repaired instance is the usual reason a class gets dropped. |
| 2026-08-15 | → in_progress | Plan taken in six steps. Two of them are the task's whole content: the row is **extracted as bytes** from `d56486f` rather than retyped, because 700 characters of prose carrying two backticked identifiers and an em dash would come back reading correctly and not being what the record said; and the proof scans the **tree**, not the file, on T-034's ground that a check narrowed to what you just edited cannot report that it passed on nothing. |
| 2026-08-15 | (no change) | **Authorisation (METHOD §3.1):** the project owner answered *All recommended answers accepted. Commit changes, then take T-140* on 2026-08-15, against a next step offering to take this task now and out of order. It covers this task through all four phases and reaches no other — T-141, T-144 and T-146 wait to be asked for, and the two owner answers recorded in T-144 and T-146 today authorise no phase of either. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T4`, which named the failure mode without knowing this repository had an instance. The scan that found it read 270 Markdown files, 558 tables and 2,769 body rows and returned exactly one hit, so the instance is isolated and the repair is bounded. `high` rather than `medium` because the lost text is the raising rationale of a `critical` task and the sentence attributing it to an adopter, and because the loss survived `check`, the suite and the pre-publish gate — the record was wrong in a way nothing this project runs could report. `xs` because the original text is in git and the edit is one row. The class is deliberately not here: it is T-141, and closing this one does not close that one. |
