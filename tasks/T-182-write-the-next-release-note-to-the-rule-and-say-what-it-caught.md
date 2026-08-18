---
id: T-182
title: Write the next release note to the rule and say what it caught
type: deliverable
status: proposed
phase: specify
parent: T-135
blocked_by: []
related: [T-125, T-127, T-133]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-18
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
- **When does this run?** It is gated on there being a release to make, so it cannot be scheduled from
  here. Whoever tags the next version runs it as part of publishing.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-18 | → proposed | Raised by [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md)'s review, which carried its fourth criterion rather than meeting it. **Planned for at `plan`, not discovered at `review`**: satisfying it would have meant writing a note for a release nobody was making, which is a criterion describing the work instead of judging it. Gated on a real release, so it sits outside any standing grant until one is being made. |
