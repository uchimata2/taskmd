---
id: T-182
title: Write the next release note to the rule and say what it caught
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-135, T-125, T-127, T-133]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-182 — Write the next release note to the rule and say what it caught

## 1. Specify

**Outcome**
The next release note is written using `docs/PUBLISHING.md` §7, and the record says whether the rule
surfaced anything the writer had not already thought of — including if the answer is no.

**Why this one**
[T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) shipped the rule and
met three of its four criteria. The fourth cannot be met by the task that wrote the rule, because it
asks for the rule to be *used* on a release, and no release was in progress. Carrying it here keeps
the gap visible instead of letting a criterion be ticked by the document that created it.

**The point is the second half, not the first.** Applying the rule is mechanical — one command. What
this task exists to record is whether it **found something**, because that is the only evidence that
the rule is worth its cost. A rule that reproduces exactly what the writer would have written anyway
is a rule to drop, and nothing but a real release can tell the difference.

**Scope**
- In: running §7's commands against the milestone being shipped, before the note is styled.
- In: the recorded answer, either way, and what it cost.
- Out: changing the rule. If the rule is wrong, that is a finding here and a separate task.
- Out: rewriting any published note — [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md).

**Inputs**
- `docs/PUBLISHING.md` §7 — the rule, its commands and its stated limits
- [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) §3 — the `v0.4.0`
  worked example the rule was derived against

**Acceptance criteria**
- [ ] The three counts in §7 are run and recorded, and the two filtered ones sum to the whole set
- [ ] Every task the rule required is described in the note or waived, and the waivers are named
- [ ] The record says whether the rule caught anything the writer had not already listed — including
      "it did not", stated plainly
- [ ] The opening sentence claims no completeness, per §7

**Open questions**
- ~~**When does this run?** It is gated on there being a release to make, so it cannot be scheduled from
  here. Whoever tags the next version runs it as part of publishing.~~ **Answered 2026-08-22: after
  [T-231](T-231-cut-the-next-release.md)**, which now carries the release and is recorded as this
  record's `blocked_by`. See the Log row of that date, which also carries a tension the scheduling
  raises for §1.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run §7's three counts against the milestone being shipped, and check the two filtered ones sum. | The counts, and whether they sum |
| 2 | Partition the required set into the groups the note will describe, and check the partition covers it in both directions. | A group per section, with no task missing and none counted twice |
| 3 | Write the note and the tag message as two texts, to files, never through a shell. | Two files |
| 4 | Verify every behavioural claim in them by running it, before either is published. | A corrected note |
| 5 | Apply §2's humanizer pass and §5's dash rule to both, neither of which any gate reaches. | Both texts clean |

## 3. Implement

**Did the rule catch anything? Yes, and it stopped the release.**

This is the question the record exists for, and the answer is not marginal. §7's counts were the
first thing run, before a word of the note was drafted:

```text
$ taskmd list --work_package M6 --closed                        | wc -l   → 108
$ taskmd list --work_package M6 --closed --adopter_visible yes  | wc -l   →  11
$ taskmd list --work_package M6 --closed --adopter_visible no   | wc -l   →  19
```

11 + 19 = 30 against 108. **78 closed tasks had never been judged**, and §7 says an unmarked task
blocks the note. The release was held, the owner was asked, and
[T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) cleared
them. After it closed the same three commands returned 108, 72 and 36, which sum.

**Nobody would have found this by writing prose.** A writer describing the release from memory would
have described roughly the changes described below and never known that most of the milestone had
never been examined. That is the rule doing exactly what
[T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) built it for, on its
first real use, and it is worth more than the note.

**It caught a second thing, which is a defect in the rule itself.** §7 reads one milestone label, so
a task that closed inside the release window under an older label is invisible to it.
`T-006` *"Package, document and publish"* closed on 2026-08-16 with 23 shipped files changed and sits
in M1. The note covers it because the owner said to add it by hand; the durable fix is
[T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md).

**Decisions & assumptions**

- **The note describes the required set in groups, not one task at a time — 2026-08-23.** §7 permits
  it and says in its own words that a person maps prose onto the checklist. *Rejected: name every id*
  — a note listing 74 ids is the changelog §7's own argument rules out.
- **The partition was checked by command, not by eye — 2026-08-23.** 74 required, 74 assigned, no
  duplicate and no gap, compared in both directions. A group list is exactly the kind of hand-kept
  set that drops a member invisibly, and a total cannot show it.
- **One required task is waived, and the waiver is named — 2026-08-23.**
  [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md), whose
  outputs were this repository's own `.taskmd/config.md` and one task file. An installed copy
  receives neither. It was marked `yes` by T-242's deliberately loose rule, which is that rule
  failing safe into this mechanism rather than a mistake.

**Four claims were wrong before they were verified, and none would have been caught by reading**

CLAUDE.md requires a behavioural claim to be verified by running the thing. Applied to the draft:

| Draft claim | What running it showed |
| :--- | :--- |
| "`waiting_on` is a real field" adopters get | Not in the shipped default config. It is this project's own `context_fields`, so an adopter receives nothing |
| A person-gated task stops sorting as startable | T-230's own record says the default ordering is unchanged. The draft claimed the opposite |
| `list --fields` returns the filterable fields | No such flag. The behaviour is an unknown filter exiting 2 and naming what it accepts |
| Two of the six new classes move the exit status | Four do. Only `LABEL SHAPE` and `SECTION REF` are advisory |

The six new classes were themselves derived rather than recalled, by holding `check --classes`
against the class names present in `v0.5.0`'s `cli.py`.

**Outputs produced**
- The `v0.6.0` tag message and the GitHub release body. Two separate texts, both written to files and
  passed by path, never through a shell, per §1's record of what a here-string did to `v0.4.0`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The three counts in §7 are run and recorded, and the two filtered ones sum | met | Run twice: before, where they did not sum, and after T-242, where 72 + 36 = 108 |
| Every task the rule required is described in the note or waived, and the waivers are named | met | 74 required, partition checked by command in both directions, one waiver named above |
| The record says whether the rule caught anything the writer had not already listed | met | It did, twice. Stated at the top of §3 rather than buried |
| The opening sentence claims no completeness, per §7 | met | The note opens by calling itself a selection, and closes by saying what it leaves out |

**Child fix tasks raised**
- [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) — as
  a soft edge. The rule's defect is not part of this note's outcome.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **The note and the tag message are written, and the answer this record exists for is yes.** §7 caught two things on its first real use: **78 closed tasks nobody had judged**, which stopped the release until [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) cleared them, and **a defect in the rule itself** — it reads one milestone label, so `T-006` *"Package, document and publish"* closed inside the release window under an older label and was invisible to it. **Four behavioural claims in the draft were false and were caught by running them**, not by reading: the shipped config carries no `waiting_on`, the ordering is unchanged for a person-gated task, `list --fields` does not exist, and four of the six new classes move the exit status rather than two. §3 carries the table. **One required task is waived with the waiver named**, which is T-242's deliberately loose rule failing safe rather than a gap. |
| 2026-08-23 | (no change) | **Unblocked, and the direction of the edge reversed on the owner's answer of 2026-08-23**: [T-231](T-231-cut-the-next-release.md) now carries `blocked_by` naming this record, because the note is an input to the command that creates the release and not a thing written after it. The answer of 2026-08-22 that put this record after T-231 is superseded rather than deleted — §1's struck-through question still shows it was asked and how it was answered then. [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) closed, so §7's counts sum and the rule can now be run. |
| 2026-08-23 | (no change) | **§7 was run for the first time on a real release, and it caught something — which is the half this record exists to answer.** The three counts were 108, 11 and 19: the two filtered ones sum to 30, so **78 closed M6 tasks carry no `adopter_visible` value**, and §7 is explicit that absent does not pass as `no`. The note therefore cannot be written yet; the blocker is [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md), reached through [T-231](T-231-cut-the-next-release.md) rather than recorded again here. **What it caught is bigger than a backlog.** The field's own rule says the judgement is made when the work is understood, not while writing prose about a release; 78 tasks say that never happened, so the finding is about the practice and not only about the marks. Recorded now rather than at this record's own implement, because the evidence was produced by the session that ran the commands and would otherwise have to be re-derived. **No phase advanced and nothing was written to the note.** |
| 2026-08-22 | (no change) | **The gate is an edge now.** The owner raised [T-231](T-231-cut-the-next-release.md) on 2026-08-22 and scheduled this record **after** it, so `blocked_by` carries what an *Open questions* bullet carried before — and `list --open` sorts this record last and reports it blocked, where it had been sorting as startable in every view. That is the repair [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) made for a wait on a task, now available here because the event acquired one. **A tension the scheduling raises, recorded rather than resolved:** §1's scope says §7's commands run *before the note is styled*, and a release cut first means the note already exists when this record starts — so whoever works it must check whether the outcome is still reachable, or say what it became. That is this record's own `specify` and not something to settle from outside it. **Not in the unattended grant of the same date**, and its own exclusion is recorded in the five records that grant covers. |
| 2026-08-22 | (no change) | **The owner's answer: a project-wide audit comes before the release.** Asked in the batched round of 2026-08-22 — §1's open question says the trigger is an **event** rather than a decision, so the only thing an owner can settle is whether that event is wanted now. **Answered: not yet.** An audit of the entire project runs first, and its requirements are to be given separately; this task is unaffected by what that audit contains and stays gated on a release actually being made. So the gate is now two conditions where §1 records one, and neither is scheduled from here. This row is the answer, not authorisation to start. |
| 2026-08-22 | (no change) | **Re-edged from `parent: T-135` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** This is the hardest of the three, because it *was* raised from a criterion [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) recorded as **not met**. The judgement is that T-135's outcome is nevertheless finished: the rule exists in `docs/PUBLISHING.md` §7 and was **used** — applied to `v0.4.0`'s note, where it found at least 21 omissions against the 6 a hand-sample had found. That is `implement`'s exit criterion satisfied on the real thing. The unmet criterion asks for the rule to be applied to a release that does not exist yet, which is an external condition and not a gap in the deliverable. Reopening T-135 would put a finished rule back on every open view until an unscheduled release happens. Rejected for that reason; recorded in T-216 §3. |
| 2026-08-18 | → proposed | Raised by [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md)'s review, which carried its fourth criterion rather than meeting it. **Planned for at `plan`, not discovered at `review`**: satisfying it would have meant writing a note for a release nobody was making, which is a criterion describing the work instead of judging it. Gated on a real release, so it sits outside any standing grant until one is being made. |
