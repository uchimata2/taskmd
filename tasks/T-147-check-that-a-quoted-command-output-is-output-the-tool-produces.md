---
id: T-147
title: Check that a quoted command output is output the tool produces
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-095, T-134, T-139, T-141]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-147 — Check that a quoted command output is output the tool produces

## 1. Specify

**Outcome**
A block of command output pasted into a tracked document cannot quietly stop being what the command
prints, or the project records that it will not be guarded and says what a reader should assume about
a transcript instead.

**Why this one**
Found on 2026-08-15 during [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md),
which added a counted noun to `check` and so had to touch the sample run in
[`../README.md`](../README.md). The block was **already wrong before that edit**:

```
README quoted    OK - 0 task(s), ... 0 template field value(s), 0 vocabulary row(s)
actually printed OK - 0 task(s), ... 0 template field value(s), 0 vocabulary row(s), 0 front-matter value(s)
```

`front-matter value(s)` arrived with [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md)
on 2026-08-12 and the README was not updated, so the first `check` output a stranger sees has been
missing a denominator for three days. T-141 then added a second.

**Why a transcript rots differently from a list.**
[T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) guarded
the command lists and [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)
is raised for the advisory lines. Both are **enumerations**, where the drift is a missing member and
a reader who knows the set can spot it. This is a **quoted result**, and it reads as evidence: it
carries a shape nobody re-derives, because the whole point of pasting output is that it was
observed. Nothing about it looks like a list with a gap.

**And it is the summary line specifically that will keep drifting.** [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)
made `check` report what it examined, and `examined()` builds that line from the checks that actually
ran — so **every new check changes it, by construction**. Two of the last three checks added did.
That is not a documentation habit that can be improved; it is a guarantee that the quoted line goes
stale on a schedule.

**Requirements served**
R-16, and §5 *humanized* in `docs/SCOPE.md`: the README is what a stranger reads before installing,
so its first sample run being subtly untrue is the worst place in the tree for this.

**Scope**
- In: quoted `taskmd` output in tracked documents, and whether a run can be compared against the
  quote mechanically.
- In: which quotes are in the guarded set. Many transcripts in this repository are **records of a
  past run** inside a closed task and must never be re-derived — METHOD §1.5 forbids rewriting what a
  record says about the past — so the set is not "every fenced block".
- In: whether the answer is the same mechanism as T-134's and T-139's or a different one, since the
  fault is different.
- Out: what any command prints. This is about the copies.
- Out: the advisory-line paragraphs, which are [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md).

**Inputs**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  marker mechanism, and why a list is guarded rather than a sentence.
- [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) — why the summary line is
  derived, which is what makes it drift on every new check.
- `tests/test_publishing.py`, where the existing document assertions live.
- [`../README.md`](../README.md), the sample run under *check*.

**Acceptance criteria**
- [ ] The guarded set is decided by reading what is actually quoted in tracked documents, with a
      count, rather than by naming the README
- [ ] A quote inside a closed task's record is demonstrably **not** in the set, and the reason is
      stated where someone tempted to widen it will read it
- [ ] Shown **failing**: a guarded quote is made stale and the suite goes red
- [ ] The README's sample run is correct as of the run that proves it, and dated or derived rather
      than transcribed again

**Open questions**
- ~~**Is a quote guarded by comparison or by generation?**~~ **Answered by the project owner on
  2026-08-16: by comparison.** The suite runs the command and diffs what the document quotes.

  *Rejected: generation between markers.* It removes the drift class outright rather than reporting
  it, which is the stronger guarantee, and it is the idiom this project already uses for the task
  index. What decided it against: the README is the document a stranger reads **before** installing,
  and `CLAUDE.md`'s *humanized* publishing constraint is about exactly that page. Machine-written
  blocks in it buy correctness at the cost of the thing the constraint protects. Comparison is also
  what [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) and
  [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) already do,
  so this is one more instance of an established mechanism rather than a second one.

  **This does not settle which quotes are guarded**, which criterion 1 says is decided by reading
  what is actually quoted, with a count. That is still `specify`'s and is the larger half.

- **Which quotes are guarded?** **Answered 2026-08-16 by counting, not by judgement.** Every fenced
  block in every tracked file was placed in exactly one bucket, so the buckets sum to the total and a
  block cannot fall between them:

  ```
  tracked files: 278  scanned: 278  unreadable/binary: 0
  fenced blocks: 516
  sum of buckets: 516

    312  not taskmd output
    204  carrying at least one shape the tool prints

  blocks that look like taskmd output, by top-level location:
    195  tasks
      7  plugin
      2  (root)
  ```

  The 204 break down as follows. **195 are inside task records** — transcripts of a run that happened,
  which METHOD §1.5 forbids rewriting, so they are out by rule and not by taste. Of the 7 under
  `plugin/`, **5 are invocations rather than output** (`taskmd check`, `taskmd list --open --limit 1`
  — lines to type, with no result under them) and **2 are advisory specimens** in
  `taskmd/defaults/config.md`, describing a hypothetical project's drift; no run here produces them,
  so there is nothing to compare against. Of the 2 at the root, one is `README.md`'s
  `mkdir tasks` / `taskmd check` invocation and one is its result.

  **So the guarded set is one block**: the `check` transcript in [`../README.md`](../README.md), and
  it is the block §1 was raised about. That is not a smaller answer than expected — it is the measured
  one, and it says something the task could not assume: this project quotes results almost nowhere
  outside its own records.

  **The set stays opt-in by marker** rather than being this count written down. A count is a fact
  about today; a marker is a claim the document makes about itself, and it is how a second guarded
  block arrives without this task being reopened. It is also what keeps the 195 out **structurally** —
  a task record cannot enter the set by resembling one.

**Acceptance criteria, amended 2026-08-16.** Criterion 4 asked for the README's sample run to be
*correct as of the run that proves it, and dated or derived rather than transcribed again*. The first
half stands and is met by the guard itself. **The second half is withdrawn**: dating the block, or
generating it, are the two things the owner's ruling above rejected — a machine-written block in the
page a stranger reads before installing. A quote the suite re-runs on every pass needs no date,
because there is no interval over which it can be believed and be wrong.

## 2. Plan

The mechanism is T-134's, so the first step is to make that mechanism able to answer a question about
**text** rather than about a set. Everything after it is one region and one run.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Split `marked_region` in two: a `region_lines` that returns what is inside a marker pair, and the set-of-names reading layered on it. `opens`/`closes` take a marker name rather than a `Kind`, since a region now has two kinds of consumer | `tests/test_publishing.py`, refactor with no behaviour change — the 6 existing assertions stay green |
| 2 | Mark the README's `check` transcript with the same marker convention | `README.md`, one pair around one fenced block |
| 3 | Reproduce the run the block records — a directory holding nothing but `tasks/`, outside any repository — and compare it line for line with what the region carries | the guard, in `tests/test_publishing.py` |
| 4 | Assert no document under the project's own `tasks_dir` carries this marker, with METHOD §1.5's reason in the docstring. The directory is read from the schema, not written here | criterion 2, armed structurally rather than stated |
| 5 | Make it fail: change a denominator in the README, and delete the markers | two recorded failures in §3 |
| 6 | Run the suite, `check` and `index` | green output quoted in §3 |

## 3. Implement

**Decisions & assumptions**
- **`marked_region` was split rather than copied** — 2026-08-16. A region now answers two different
  questions: *which members does this list name* (T-134, T-139) and *what text does this block
  carry* (here). `region_lines` returns the lines; the set-of-names reading is one line on top of it,
  and `opens`/`closes` take a marker name instead of a `Kind` because the second consumer has no set
  and no pattern. Six existing assertions were green before and after, which is what makes it a
  refactor rather than a change.
- **The comparison re-runs the command instead of trusting a recorded value** — 2026-08-16. The
  README's block records a run in a directory holding nothing but `tasks/`, outside any repository,
  so the test builds that directory and runs `check` in it. A stored expected string would be the
  same quote in a second place, which is the fault under repair.
- **The task folder's name comes from the schema** — 2026-08-16. Both the temporary project and the
  records exclusion ask the schema for `tasks_dir`, so a project that renamed it is not compared
  against a directory it does not have.
- **`self.maxDiff = None`** — 2026-08-16. The first failure truncated at unittest's default and the
  cut landed mid-summary, hiding the changed word. The diff *is* the repair instruction here, so it
  is printed whole. Written after seeing it.
- **The survey was a one-off measurement and is not shipped** — 2026-08-16. Its numbers are in §1 as
  a finding, dated, with what was counted; the script itself would be a second guard nobody runs.
  This is the same judgement the task makes about transcripts, applied to its own evidence.

**Evidence — made to fail three ways, on the real tree**

A denominator dropped from the quote, which is the exact T-138 drift that raised this task:

```
AssertionError: Lists differ: ...
  ['OK - 0 task(s), 0 field value(s), 0 reference(s), 0 dependency edge(s), 0 '
   'declared output(s), 0 index file(s), 0 document(s), 0 link(s), 0 table '
-  'row(s), 0 template(s), 0 template field value(s), 0 vocabulary row(s), 0 '
?                                                                         ----
+  'row(s), 0 template(s), 0 template field value(s), 0 vocabulary row(s)',
: README.md quotes a `check` run this tool no longer produces
```

The opening marker deleted — the disarming case, which no comparison can notice by itself:

```
AssertionError: unexpectedly None : README.md carries no taskmd:sample-check region, so its sample
run is guarded by nothing
```

A task record marked, which is criterion 2 shown rather than asserted — the marker was put in this
task's own §1 survey block and then removed:

```
AssertionError: ['tasks/T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md'] is
not false : tasks/T-147-...-produces.md carries a taskmd:sample-check region; a record of a run that
happened must not be re-derived
```

Everything restored — `git diff` against `README.md` is the two marker lines and nothing else — then
the suite:

```
267 passed, 3 skipped, 6 subtests passed in 20.41s
```

**Outputs produced**
- `tests/test_publishing.py` — `region_lines`, `opens`/`closes`/`documents_carrying` taking a marker
  name, and `AQuotedRunIsWhatTheCommandPrints` with its two assertions
- `README.md` — a `taskmd:sample-check` marker pair around the `check` transcript

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The guarded set is decided by reading what is actually quoted in tracked documents, with a count, rather than by naming the README | met | 516 fenced blocks in 278 tracked files, partitioned so the buckets sum; the breakdown and what each bucket is are in §1. The README block was the answer, but it was the answer the count gave |
| A quote inside a closed task's record is demonstrably **not** in the set, and the reason is stated where someone tempted to widen it will read it | met | `test_no_record_of_a_past_run_is_in_the_guarded_set`, shown failing in §3 by marking a task record. METHOD §1.5's reason is that test's docstring — the file the widener is editing |
| Shown **failing**: a guarded quote is made stale and the suite goes red | met | §3, first failure, and two more the criterion did not ask for |
| The README's sample run is correct as of the run that proves it | met | It is re-run on every pass, and was byte-identical before any of this was written — T-141 had repaired it |
| ~~dated or derived rather than transcribed again~~ | withdrawn | At `specify`, 2026-08-16: both remedies are what the owner's ruling rejected. A quote the suite re-runs has no interval over which it can be believed and be wrong, so a date would state a weaker fact than the guard already keeps |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | Full lifecycle in one session under the authorisation below. `specify` answered the larger half by counting rather than judging: 516 fenced blocks partitioned across 278 tracked files, and the guarded set is **one** — this project quotes results almost nowhere outside its own records. One criterion was **withdrawn** with the reason recorded, because its second half asked for what the owner's ruling had rejected. `implement` split T-134's region reader so a marker can carry text as well as a set, and proved three failures including a task record being marked. `review` judged four criteria met and one withdrawn, no child task. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. **The owner ruled on this task's open question in the same exchange** — guarded by comparison, not generation; the ruling and its rejected alternative are in §1. |
| 2026-08-15 | → proposed | Raised by [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md), which had to edit the README's sample `check` run and found it already stale by one denominator, three days old, from T-138. Not fixed where it was found beyond the one line T-141 owed (METHOD §5). `medium` because the fault is a subtly wrong sample rather than a broken instruction, and `m` because the honest part is deciding which quotes are guarded: this repository is full of transcripts that are records of past runs and must **not** be kept current, so the set cannot be "every fenced block" and choosing it is the work. The sharp fact is in §1: `examined()` derives the summary from the checks that ran, so every new check changes that line by construction, and two of the last three did. |
