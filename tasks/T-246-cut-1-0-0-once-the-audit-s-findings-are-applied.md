---
id: T-246
title: Cut 1.0.0 once the audit's findings are applied
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: [T-244]
related: [T-231, T-243, T-241]
work_package: M7
owner: the project owner
business_value: high
effort: m
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables:
  - plugin/.claude-plugin/plugin.json
---

# T-246 — Cut 1.0.0 once the audit's findings are applied

## 1. Specify

**Outcome**
A tagged and published `1.0.0` whose manifest, tag and release note agree, cut by
[`docs/PUBLISHING.md`](../docs/PUBLISHING.md), after
[T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
closes and its findings have been applied.

**Why this one**
The owner said on 2026-08-23, in the same breath as asking for the audit: *"After the audit and all
findings applied I want a v1.0.0 live."* This record exists so that wish is not held only in a survey
answer inside a closed exchange.

**That is exactly why [T-231](T-231-cut-the-next-release.md) was raised**, and the reason is worth
repeating rather than pointing at: on 2026-08-22 a survey of the open backlog found no task carried
the release the owner wanted, and the two things that had gone wrong at previous releases had both
gone wrong *around* the act rather than in it. An act with no record repeats them.

**What is already known and does not need rediscovering**
- **The `0.6.0` cut was stopped by its own release-note rule**, which found 78 unjudged tasks. What it
  cost is in [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md).
- **That rule is being changed.**
  [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) keys
  it on the tag range rather than a milestone label, on the owner's answer of 2026-08-23. This release
  is the first that will run the changed rule, so it is also that change's first real test.
- **A release is not the last step of a release.** Whether `1.0.0` is verified from outside is a
  decision this record has to take, not inherit.

**Scope**
- In: the version bump to `1.0.0`, `docs/PUBLISHING.md` end to end, the tag and the published release
- In: whether `0.6.0`'s beta framing is stated anywhere at `1.0.0`, given that it was never put on the
  release page
- In: what the cut was stopped for, or how *nothing* was checked
- Out: the audit and its findings. Those are
  [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
  and the records it raises
- Out: anything a session may do unattended. Tagging and publishing are outward-facing and the
  owner's to authorise, as they were for `0.6.0`

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) — the procedure, §5's gate, §6's check, §7's rule
- [T-231](T-231-cut-the-next-release.md) — the last cut, its plan, and the two gates' real output
- [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) — the four
  behavioural claims that were false until they were run, and why a note is read back from where it
  lands

**Acceptance criteria**
- [ ] The manifest version, the tag and the published release all name `1.0.0`
- [ ] Every finding [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
      raised is closed, or is consciously carried with the reason named
- [ ] §5's gate, §6's check and §7's rule were all run, and their output recorded
- [ ] Whether `1.0.0` is verified from outside is decided and recorded either way
- [ ] What the cut was stopped for is recorded, and if the answer is *nothing*, how that was checked

**Open questions**
- **Does a verification-from-outside task follow this one, as [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) follows `0.6.0`?**
  — the project owner. The recommendation is **yes**, on the same grounds as last time. *Against:
  T-085 found half of that verification unreachable from any machine here and T-241 inherits the same
  boundary, so a third run buys less again.*

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

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised from the owner's answer of 2026-08-23**, which asked for the audit and said `1.0.0` should follow it once the findings are applied. **Raised now rather than when the audit closes**, for the reason [T-231](T-231-cut-the-next-release.md) records: a wanted release that no task carries is invisible to every view, and that is how the last one came to have no record until somebody swept the backlog looking. **`blocked_by` names the audit**, so the tool reports this held rather than a sentence here doing it. **Grouped under `M7`**, a label raised with this record: the digit-equals-version rule already carries two named exceptions, and this is a third — `M7` ships as `1.0.0`. Chosen over stretching `M6`, which closes on membership and would then never close. |
