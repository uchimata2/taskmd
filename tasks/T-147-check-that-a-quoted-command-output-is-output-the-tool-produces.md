---
id: T-147
title: Check that a quoted command output is output the tool produces
type: fix
status: proposed
phase: specify
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
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, unattended**, given 2026-08-16 as the subject of a handoff — *a vast amount of task alone, unattended*, the maintainer having selected the batch from a list put to them and answered two questions about it. It covers [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md), [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) and [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) and **nothing else** — not the six `decision` tasks beside them, not the three parked on the `InstructionsLoaded` hook, and **not anything these four raise**, which are filed and left. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. **The owner ruled on this task's open question in the same exchange** — guarded by comparison, not generation; the ruling and its rejected alternative are in §1. |
| 2026-08-15 | → proposed | Raised by [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md), which had to edit the README's sample `check` run and found it already stale by one denominator, three days old, from T-138. Not fixed where it was found beyond the one line T-141 owed (METHOD §5). `medium` because the fault is a subtly wrong sample rather than a broken instruction, and `m` because the honest part is deciding which quotes are guarded: this repository is full of transcripts that are records of past runs and must **not** be kept current, so the set cannot be "every fenced block" and choosing it is the work. The sharp fact is in §1: `examined()` derives the summary from the checks that ran, so every new check changes that line by construction, and two of the last three did. |
