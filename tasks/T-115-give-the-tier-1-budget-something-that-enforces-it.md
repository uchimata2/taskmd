---
id: T-115
title: Give the tier 1 budget something that enforces it
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-028, T-047, T-063]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-115 — Give the tier 1 budget something that enforces it

## 1. Specify

**Outcome**
The tier 1 budget either has something that reports a breach without being remembered, or it is
written down that nothing does and the number is advisory — so the next edit that crosses it is
noticed by the project rather than by whoever happens to re-run a documented command.

**Why this one**
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) brought tier 1 under
the bound for the first time. It **passes by 8 characters** — 7,911 against 7,919. That margin is
smaller than a single sentence, and T-047's own log records the mechanism that will spend it: tier 1
grows whenever a task closes and the tree is made honest, which happens most sessions and is nobody's
edit to tier 1 in particular.

**Nothing runs the check.** The budget is a bash line in `CLAUDE.md` that someone has to remember to
run. That was harmless while the file was 4,817 over — a permanently failing budget cannot be
regressed — and it stops being harmless the moment the margin is 8. This is the shape
[T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) rejected an `--all`
flag for and [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) and
[T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) were both raised about: a check
nobody is prompted to run is silence with a command attached.

**The awkward part is that this is not `check`'s job.** The budget compares one project file against
another and is specific to this repository's tiering; taskmd validates a task tree and ships to
adopters who have neither. So an answer that adds it to `check` has to say why an adopter is made to
carry it, and an answer that adds a test has to say why the suite tests the repository's prose.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: whether anything enforces the bound, and what — a test, a `check` rule, an `after_write` hook,
  or nothing with the consequence written down.
- In: whether the margin is a number worth stating at all, given that both sides move.
- Out: the bound and the tiering. T-028 settled both and T-047 executed against them.
- Out: what tier 1 contains. That is T-047's, now closed, and re-opening it here would be a cut
  chosen to fit a number.

**Inputs**
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) §3, for the
  measurement and the sections it came from.
- [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md), for why the count reads the tree
  rather than a list, and why characters rather than lines.
- `CLAUDE.md` *Working method*, which holds the command.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative
- [ ] If something enforces it: a tier 1 deliberately pushed over the bound is reported, shown
      failing first
- [ ] If nothing does: `CLAUDE.md` says so where the command is, so a reader does not assume the
      number is guarded
- [ ] Whatever is decided does not make an adopter carry this repository's tiering

**Open questions**
- **Whether an 8-character margin is a passing state or a defect.** The maintainer's. It meets
  T-047's criterion as written, and it is one sentence from failing.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised by T-047's review, which brought tier 1 under the bound by 8 characters and could not honestly call that guarded. `high` because the margin is smaller than one sentence and the thing that spends it is ordinary reconcile work, not an edit anyone would think to measure; `s` because the command already exists and only the question of who runs it is open. |
