---
id: T-135
title: Derive what a release note must cover from the tasks it ships
type: deliverable
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-086, T-125, T-127, T-128, T-129, T-133]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-135 — Derive what a release note must cover from the tasks it ships

## 1. Specify

**Outcome**
A release note has a rule for what it must mention, and the rule is checked against the set the
tracker already knows — so what reaches the note stops depending on who wrote it.

**Why this one**
Reported by an adopting project on 2026-08-11: *`v0.4.0`'s note omits T-112.* Verified, and it is
one instance rather than the finding.

`v0.4.0` shipped **47** closed tasks. Its note describes about eight changes and opens with
*"Everything grouped as the v0.2 milestone"*, which reads as a completeness claim. Neither the tag
message nor the release body names a single task id, so nothing connects the note to the set it
covers. Sampled against the closed set, these change what an adopter sees and appear nowhere in it:

| Task | What an adopter would have noticed |
| :--- | :--- |
| [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) | `check` stops reporting link syntax shown inside a code span as a broken link |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | `check` reports a stale generated index, which it never used to |
| [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) | `check` prints denominators and a `Scope` line on every run |
| [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) | `list` marks blocked rows |
| [T-111](T-111-stop-the-index-showing-a-closed-task-as-a-live-blocker.md) | the generated index stops showing a closed task as a live blocker |
| [T-101](T-101-report-a-template-the-create-path-cannot-see.md), [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) | two new `check` classes |

**This is the project's own design rule pointing at itself.** The membership of a release is
`work_package`, read with the tool and written down nowhere — that is
[T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md)'s whole point. The note is then
written by hand from memory of that set, which is the second copy arriving through the back door: not
a stale *list*, but a stale *selection*.

**What this is not.** Not a generated changelog. A note that prints 47 titles is worse than one that
describes eight changes well, and `docs/PUBLISHING.md` §1 makes the note covered prose that a stranger
reads. The question is what it must **not** omit, not what it must contain.

**Requirements served**
R-8 (`docs/SCOPE.md`) — everything found leaves a trace, applied to the one document an adopter reads
to find out what changed. R-21, since the note is covered text.

**Scope**
- In: a rule for what a note must mention, expressed against something the tracker already holds.
- In: whether anything checks it, and if so what it can honestly judge — the same proxy problem
  [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) met.
- In: whether the opening sentence should keep claiming completeness.
- Out: rewriting `v0.4.0`'s published note. Same answer as
  [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md), agreed by
  the maintainer on 2026-08-11: a dated public record is not rewritten after the rule changed.
- Out: generating the note. See *what this is not*.
- Out: the covered-text question. Settled in T-127.

**Inputs**
- The measurement above, reproducible with `list --work_package M2 --closed`.
- [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md), for why membership is derived.
- [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) §3, for a check that
  reads its rule out of the document that owns it, and for what a proxy may claim.
- `docs/PUBLISHING.md` §1 and §5.

**Acceptance criteria**
- [ ] `docs/PUBLISHING.md` states what a release note must not omit, in one place, as a test rather
      than a list
- [ ] The rule is applied to `v0.4.0`'s note as a worked example, and the result recorded either way
- [ ] If anything automated is added, it says what it cannot judge, in its output or its name
- [ ] The note for the next release is written to the rule, and the rule found something the writer
      had not already thought of — or the record says it did not

**Open questions**
- None. Both answered by the maintainer on 2026-08-11.

  **Q1 — what is the trigger for "must mention"? — a field on the task.** The note's coverage is then
  derived from the same front-matter everything else is derived from, which is the design rule applied
  rather than worked around. It costs a config key, and
  [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) says a key is not free: the shipped
  config replaces rather than merges, so every project that has written one stops seeing the new row
  until it re-copies. **That cost is now `plan`'s first problem**, not a reason to reopen the answer.
  *Rejected: a type-and-status rule* — "every closed `fix` and `deliverable` must be mentioned or
  waived" adds no key and over-fires on internal work, and a rule that fires on work an adopter
  cannot see teaches the writer to waive by reflex.

  **Q2 — does the opening sentence keep claiming completeness? — no.** *"Everything grouped as the
  M2 milestone"* is true of the milestone and false of the note, and it is the sentence that turns
  an omission into a defect rather than an editorial choice. Dropping it makes the note honest about
  being a selection, which is what Q1's rule then bounds. *Rejected: keep it and make it true* — that
  is a note naming 47 tasks, which §1 already rules out as worse than eight described well.

## 2. Plan

_Not planned._

## 3. Implement

_Not started._

## 4. Review

_Not started._

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → specified | Both questions answered by the maintainer, with the rejections recorded in §1. **Q1: a field on the task**, so coverage derives from the same front-matter as everything else. That buys a config key, and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s constraint makes the key the first thing `plan` has to solve rather than a detail: the shipped config replaces rather than merges, so a project that already wrote one stops seeing the new row. **Q2: the opening sentence stops claiming completeness**, because it is the clause that turns an omission into a defect. Criteria unchanged; both answers are choices inside them. Still `M6` and still not started. |
| 2026-08-11 | → proposed | Reported by an adopting project as *"`v0.4.0`'s note omits T-112"* and **verified before filing**, which changed what it is: the note omits T-112 and it omits at least five other adopter-visible changes, out of 47 tasks shipped, while opening with a sentence that reads as a completeness claim. So the report is a specimen and the finding is that a note has no rule. Filed `M6` by the maintainer's release rule of 2026-08-10 — this is a new capability and a config decision rather than a minor correction, and nothing about it holds up `0.5.0`, whose note is written by hand to the same standard in the meantime. Not started: both open questions are the maintainer's, and Q1 turns on whether the schema gains a key. |
