---
id: T-211
title: Mark the quiet cases in the two fixtures outside T-202's scope
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-202, T-198, T-210]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-211 — Mark the quiet cases in the two fixtures outside T-202's scope

## 1. Specify

**Outcome**
`migrated-away` and `planned-deliverable` carry marks for the quiet cases
[T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)'s record names in them, so
the reading `tests/test_quiet_cases.py` produces covers every case that record names rather than
every case inside one document's list.

**Why this one**
[T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) made the marks the authority
for the quiet-case set, and its agreed scope was **the five fixtures `tests/fixtures/README.md`
named**, plus `leak-check`. Those five were the set because that document was the thing being
dethroned as the authority.

**Three cases named by T-198 are outside that five**, added to its record on 2026-08-22 by
[T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md):

| Fixture | Quiet case | Named by |
| :--- | :--- | :--- |
| `planned-deliverable` | `MISSING OUTPUT` must not fire on an **open** task declaring a path that is not there | `test_an_open_task_declaring_a_path_that_does_not_exist_passes` |
| `migrated-away` | exactly one `BROKEN LINK`, and no report of `notes.md` | `test_a_link_that_resolves_is_not_reported` |
| `migrated-away` | **no** `CONFIG ERROR`, on a fixture where `index` and `context` still report one | `test_it_reports_a_document_defect_it_used_to_refuse_to_look_for` |

Until they are marked, the reading is short by three against what T-198 names, and the difference is
carried by prose in T-202's §3 — which is the shape F-2 exists to remove, one document over.

**Scope**
- In: marking those three cases in the two fixtures, in the form
  `tests/test_quiet_cases.py` defines
- In: re-stating the two counts in that module's reading, so the difference against T-198 closes or
  is explained by something other than scope
- Out: **exercising them.** Neither fixture has been mutated to show its cases in reach, and T-198
  declined that for all eighteen of its unexercised set. Marking is not exercising, and the reach
  assertion the reader already makes — that the class fires somewhere in the same fixture — is what
  will judge them
- Out: the sixteen `broken-*` fixtures, whose quiet case is the cross-fixture `fails()` silence
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) owns and closed

**Inputs**
- `tests/test_quiet_cases.py` — the mark's form, its anchors and its three assertions
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3, the corrected
  partition below step 4 — where the three cases are named, with the assertion that states each
- [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) §3 step 4 — the
  reconciliation this task closes

**Acceptance criteria**
- [ ] The three cases are marked, and the reading names them
- [ ] The reading's count and the count T-198 names are stated together, and either agree or differ
      for a reason that is **not** "one fixture was out of scope"
- [ ] `migrated-away`'s `CONFIG ERROR` case is marked or is recorded as unmarkable with the reason —
      `CONFIG ERROR` is excluded from the derived class set by name in `tests/classes.py`, so a mark
      naming it fails the reader's first assertion, and that is a real constraint rather than an
      oversight to work around

**Open questions**
- **None.** The scope is the residual T-202's plan named; nothing here is new ground.

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
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task, that [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) and [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the two — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), raised the same day and not named; nor [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) or [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure the earlier grant of the same date already confined away from. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its third criterion may be unmeetable and that is a legitimate outcome.** `CONFIG ERROR` is excluded from the derived class set by name in `tests/classes.py`, so a mark naming it fails `tests/test_quiet_cases.py`'s first assertion. The criterion already says to record that with the reason rather than work around it, and the grant does not license changing the class set to make a mark fit. |
| 2026-08-22 | → proposed | Raised from [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md)'s plan step 4, which named the residual before implement met it. T-202's scope is the five fixtures `tests/fixtures/README.md` named, because that document was the authority being replaced; T-198's record names three quiet cases in two fixtures outside that five, added by [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md) on the same date. Raised rather than absorbed into T-202: widening a scope the owner agreed at `specify` is the owner's, and the grant on those six tasks authorises phases and not answers. `xs` because the mechanism exists and this is applying it; `medium` because until it lands the reading's difference against T-198 is carried by prose, which is the shape F-2 exists to remove. **The third criterion may turn out to be unmarkable**: `CONFIG ERROR` is excluded from the derived class set by name, so a mark naming it fails the reader's first assertion — recorded here so `specify` meets it rather than `implement`. |
