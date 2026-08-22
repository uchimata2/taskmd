---
id: T-215
title: Show a paired fixture's quiet case is in reach, or record that a per-fixture assertion cannot
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-211, T-202, T-198, T-089]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-215 — Show a paired fixture's quiet case is in reach, or record that a per-fixture assertion cannot

## 1. Specify

**Outcome**
`planned-deliverable`'s quiet case is either marked — because `MISSING OUTPUT` has been shown able to
fire inside that fixture — or `tests/test_quiet_cases.py` records that a **paired** fixture cannot
satisfy a per-fixture reach assertion, and says what the reading does about it instead.

**Why this one**
Found by [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) putting the
mark in and running the reader, rather than reasoning about it:

```text
FAIL: test_every_marked_class_fires_somewhere_in_its_own_fixture
AssertionError: [] is not true : planned-deliverable marks a case quiet for MISSING OUTPUT and
nothing in that fixture reports MISSING OUTPUT, so the silence may be the check not reaching it
rather than the case
```

**The reader is right and the fixture is not wrong.** That third assertion asks a marked class to
fire *somewhere in the same fixture*, because a silence proves nothing where the check never looked.
`planned-deliverable` is one half of the pair
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) built: this fixture
is the silent direction and `broken-deliverable` is the firing one, a fixture over. The structure the
assertion generalises — `leak-check` stating both directions in one file — is exactly what a
two-fixture pair does not have.

So the question is not how to make the mark pass. It is **whether reach can be read across a declared
pair without giving either fixture a second defect**, and if it cannot, what the reading should say
in place of nothing. Today the case sits in `NAMED_AND_UNMARKED` with its reason asserted, which is
honest and is not coverage.

**Scope**
- In: deciding whether the reach assertion can read a declared pair, and implementing it if so
- In: whichever of the two the decision produces — the mark, or a statement in the reading that a
  paired fixture's reach is shown elsewhere, and how
- Out: **giving `planned-deliverable` its own firing `MISSING OUTPUT` case.** That makes it a second
  `broken-deliverable` and destroys the pair T-089 built, which is the thing under test
- Out: `migrated-away`'s `CONFIG ERROR` case, refused for a different and in-principle reason — see
  [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) §3 and
  [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md)

**Inputs**
- `tests/test_quiet_cases.py` — `NAMED_AND_UNMARKED`, and the third assertion that refuses the mark
- [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) §3 — the measured
  run above, and the two rows it could not mark
- `tests/fixtures/planned-deliverable/`, `tests/fixtures/broken-deliverable/` — the pair
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) — where this case is
  named, and recorded as unproven

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, and the rejection names what that
      alternative would have cost the pair
- [ ] If reach is made readable across a pair, the mechanism is shown **failing first** on a pair
      whose firing half does not fire
- [ ] `planned-deliverable`'s row leaves `NAMED_AND_UNMARKED`, or the reading states why a paired
      fixture keeps a row there permanently rather than as a residual awaiting work
- [ ] `python tests/test_quiet_cases.py` and the suite are green, and the reading is quoted

**Open questions**
- **None.** The scope is the residual T-211 measured; the decision inside it is this task's work.

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
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its scope forbids the obvious fix.** Giving `planned-deliverable` its own firing `MISSING OUTPUT` case would make it a second `broken-deliverable` and destroy the pair T-089 built. §1 puts that out by name, and this grant does not license it. |
| 2026-08-22 | → proposed | Raised from [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)'s step 1, by applying the mark and running the reader. Raised rather than absorbed: T-211's scope puts *exercising* these fixtures out by name, and the grant on that task authorises phases and not answers — so widening it to make its own first criterion pass is exactly what that grant excludes. `s` because the decision is the work and the code change may be none; `medium` because until it lands, one case T-198 names is held with a reason rather than covered, which is honest and is still a gap in the reading that replaced F-2. |
