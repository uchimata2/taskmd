---
id: T-248
title: Judge adopter_visible on the three records the new release-note rule reports unmarked
type: admin
status: proposed
phase: specify
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
deliverables: []
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
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised from [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)'s implement phase**, where the new rule was run and reported three unmarked records. Raised rather than fixed there: T-243 §1 puts the marks themselves out of scope, and the owner's grant on that record covered its own lifecycle and no other task. **Not blocked by T-245**: that record stops the count growing again, and these three already exist. |
