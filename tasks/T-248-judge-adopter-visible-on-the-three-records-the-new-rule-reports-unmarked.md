---
id: T-248
title: Judge adopter_visible on the three records the new release-note rule reports unmarked
type: admin
status: done
phase: review
parent: null
blocked_by: []
related: [T-243, T-242, T-245]
work_package: M7
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables:
  - tasks/T-027-give-the-design-rule-one-home.md
  - tasks/T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md
  - tasks/T-231-cut-the-next-release.md
---

# T-248 — Judge adopter_visible on the three records the new release-note rule reports unmarked

## 1. Specify

**Outcome**
The three closed records that [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 reports as `UNMARKED`
carry a judged `adopter_visible` value, so the next release is not blocked by them. Nothing else about
the field or the rule changes.

**Why this one**
[T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) changed
§7 to key on the tag range. Running the new rule over `v0.5.0..v0.6.0` on 2026-08-23 returned 155
closed records: 104 `yes`, 48 `no`, and **3 unmarked**. §7 says an unmarked task blocks the note, so
those three block the next release until somebody judges them:

| Task | Label | Title |
| :--- | :---: | :--- |
| [T-027](T-027-give-the-design-rule-one-home.md) | M1 | *Give the design rule one home* |
| [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) | M5 | *Check that every prose list of the commands names the commands there are* |
| [T-231](T-231-cut-the-next-release.md) | M6 | *Cut the next release* |

> **The figures in the paragraph above do not reproduce, and the paragraph is not corrected** —
> annotated instead, per METHOD rule 5, because it states a dated past measurement. Re-run on
> 2026-08-23 before anything was changed, §7's command over the same range returned **156 lines: 105
> `yes`, 48 `no`, 3 `UNMARKED`** — one more `yes` and one more line than recorded. **The three
> unmarked records are the same three**, so nothing about this task's work changes. The gap was
> chased rather than shrugged at: the range is two immutable tags, and across all 156 records neither
> a `status` nor an `adopter_visible` value differs between this record's creating commit and now, so
> the command is deterministic over that range and the recorded total is simply one short. Take 156
> as the denominator.

They are unmarked because they closed while the rule that reads the field was keyed on a milestone
they do not carry, so no release note ever asked about them.
[T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) cleared 78
marks and swept the `M6` set, which is why only three are left rather than the 81 the rejected variant
in T-243 §3 would have surfaced.

**Scope**
- In: judging `adopter_visible` on exactly the three records above, against §7's stated test
- Out: **the rule that reads the field.** That was
  [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)
- Out: **why the field goes unfilled in the first place.** That is
  [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md), and clearing
  three marks by hand is not a substitute for it
- Out: any record the rule does not report as `UNMARKED`. A sweep of the whole backlog is a different
  and much larger question, and §7 does not ask for one

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 — the rule, its command, and the test the
  judgement is made against
- The three records named above

**Acceptance criteria**
- [ ] Each of the three records carries `adopter_visible: yes` or `adopter_visible: no`, with the
      reason recorded on the record rather than here
- [ ] §7's command, run over `v0.5.0..v0.6.0`, reports `UNMARKED` zero times, shown by running it
- [ ] The three counts still sum to the size of the set, so nothing was dropped while clearing them

**Open questions**
- None. The test is §7's and the records are named.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run §7's command **before changing anything**, extracting it from the document rather than retyping it, and compare what it returns with the figures in §1. | A reproduced baseline, or a stated discrepancy |
| 2 | For each of the three, read what the record actually **produced** — its declared outputs, not its title — and apply §7's test to that. Where the project has judged the same kind of task before, use the precedent rather than a fresh reading. | A verdict per record, each with the fact that settled it |
| 3 | Write the field into the front matter and the reason into the **Log**, as an annotation. These are closed records: METHOD rule 5 forbids rewriting what they say about the past. | Three records changed, no past statement altered |
| 4 | Re-run §7 and check `UNMARKED` is zero **and** that the three counts still sum to the lines printed. | The before and after counts |
| 5 | The project's own gates. | `index`, `check`, the suite |

**Decisions taken here**

- **Step 1 exists because §1 quotes a figure, and a quoted figure reads as evidence** — 2026-08-23.
  It is the cheapest step here and the only one that can reveal the record was written against a
  different set than the one being worked.

- **Step 2 reads outputs rather than titles** — 2026-08-23. Two of the three have titles that suggest
  an answer and outputs that decide it: *Cut the next release* sounds adopter-facing and *Check that
  every prose list…* sounds internal, and in both cases the declared deliverables are what settle it.

## 3. Implement

**Decisions & assumptions**

- **Step 1 found the record's own figure does not reproduce, and the discrepancy was chased rather
  than absorbed** — 2026-08-23. §1 records 155 lines with 104 `yes`; the command returns 156 with
  105. Both sum, so neither is internally inconsistent, which is why nothing would have caught it.
  Ruled out, by measurement rather than by argument: the range is two immutable tags; and across all
  156 records, **no `status` and no `adopter_visible` value differs** between this record's creating
  commit `2e783548` and now — so the command is deterministic over that range and the two runs must
  agree. The paragraph is **annotated, not corrected**, because it states a dated measurement.

- **T-027 → `no`.** Its sole declared output is `CLAUDE.md` §*The one design rule*, made a pointer.
  §7 names instruction files as the `no` case in its own words, and an install copies `plugin/`,
  which this record did not touch. *Checked rather than assumed*: its §3 table names
  `docs/METHOD.md` — a **shipped** file — as the rule's one home, so the question was whether it
  edited that too. It did not; it found METHOD.md already correct and changed only `CLAUDE.md`.

- **T-134 → `no`, and this is the one that needed running rather than reading.** Its outputs include
  the marked regions in `plugin/skills/taskmd/taskmd/cli.py`, which **ships**, and a marker sitting
  in a command list is exactly where a stray `<!-- taskmd:commands -->` would reach a user's screen.
  It does not: the markers are in that module's **docstring**, and the tool prints
  `usage: taskmd {check,context,index,list} [args] [--root PATH]` with no marker in it.
  `tests/test_publishing.py`, its other output, is not shipped.

- **T-231 → `no`, on this project's own precedent rather than on a fresh reading** — 2026-08-23.
  [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md), *Cut 1.0.0*, is the same kind of
  task and already carries `no`. A release cut is the vehicle rather than the cargo: the note it
  feeds describes what the release contains, and a note describing its own cutting says nothing.
  **It needed a precedent rather than a glance** because the version in `plugin.json` genuinely does
  reach an adopter, so the mechanical test alone pulls both ways. *Rejected: `yes` on the strength of
  the version bump*, which would put a row in every release note saying the release happened.
  ([T-006](T-006-package-document-and-publish.md) is `yes` and is not a counter-example: that was the
  first publication, where what the adopter received was the plugin's existence.)

**Outputs produced**

- [T-027](T-027-give-the-design-rule-one-home.md),
  [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) and
  [T-231](T-231-cut-the-next-release.md) — `adopter_visible: no` in the front matter, and the reason
  in each record's Log. No section of any of the three was rewritten.

**Checked by using it.** §7's command was extracted from the document with `awk` rather than retyped,
and its `RANGE` set to `v0.5.0..v0.6.0`. Before:

```text
lines=156  yes=105  no=48  UNMARKED=3
UNMARKED T-027
UNMARKED T-134
UNMARKED T-231
```

After:

```text
lines=156  yes=105  no=51  UNMARKED=0
sum check: 105 + 51 + 0 = 156   lines printed = 156   -> SUM HOLDS
```

`yes` did not move, `no` gained exactly three, and the partition still accounts for every line — which
is the third criterion, and is what would catch a record dropping out of the set while being edited.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each of the three records carries `adopter_visible: yes` or `no`, with the reason recorded on the record rather than here | met | All three carry `no`, each with its reason in its own Log as an annotation. The front matter gained a field; **no section of any of the three was rewritten**, which METHOD rule 5 requires of a closed record. §3 carries the fact that settled each, not a restatement of the reasons |
| §7's command, run over `v0.5.0..v0.6.0`, reports `UNMARKED` zero times, shown by running it | met | `UNMARKED=0`, from a command extracted out of the document with `awk` rather than retyped. It was run **before** the edits too, which is what turned up the discrepancy in §1 |
| The three counts still sum to the size of the set, so nothing was dropped while clearing them | met | `105 + 51 + 0 = 156`, against 156 lines printed. `yes` did not move and `no` gained exactly three — so the three were cleared **into** the set rather than out of it, which a total alone could not show |

**Adopter-visible?** no. This record changed three task files' front matter and logs. Task records are
not shipped — an install copies `plugin/` — so an adopter sees no different output, receives no
different file and acts no differently. It is also, in `docs/PUBLISHING.md` §7's own phrasing, this
repository's backlog administration.

**Child fix tasks raised**
- none. Every criterion is met.

**One discovery routed out of scope.**
[T-254](T-254-sweep-for-history-prose-living-outside-markdown.md) — while checking whether T-134's
shipped `cli.py` change was inert, its module docstring turned out to carry *"the command surface
stood at three until 2026-08-05"*, which is the shape `../CLAUDE.md` *Write the fact, not its
history* forbids. **T-250 swept this project for exactly that rule and could not have seen it**: its
corpus was derived as every Markdown file, so a `.py` docstring was outside the denominator by
construction. Raised rather than fixed, and rather than re-opening T-250, whose corpus and edits
stand.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **Worked `specify` through `review` and closed**, on the owner's instruction of 2026-08-23: *"continue with T-248, full lifecycle, commit and push."* Three criteria, three met. All three records judged **`no`**, each with its reason in its own Log as an annotation — the front matter gained a field and no section of any closed record was rewritten. **Two things the plan's first step earned**: §1's quoted figure does not reproduce, and the discrepancy was traced far enough to say the command is deterministic over that range, so the paragraph is annotated rather than corrected; and T-231 was settled on this project's own precedent ([T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md)) rather than on a mechanical test that pulls both ways. **One discovery routed out of scope**: [T-254](T-254-sweep-for-history-prose-living-outside-markdown.md), history prose in a shipped `.py` docstring that T-250's Markdown-derived corpus could not see. |
| 2026-08-23 | → proposed | **Raised from [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)'s implement phase**, where the new rule was run and reported three unmarked records. Raised rather than fixed there: T-243 §1 puts the marks themselves out of scope, and the owner's grant on that record covered its own lifecycle and no other task. **Not blocked by T-245**: that record stops the count growing again, and these three already exist. |
