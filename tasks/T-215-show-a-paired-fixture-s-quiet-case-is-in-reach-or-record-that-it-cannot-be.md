---
id: T-215
title: Show a paired fixture's quiet case is in reach, or record that a per-fixture assertion cannot
type: fix
status: done
phase: review
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
| 1 | Run `check` on **both** halves of the pair and read the denominators, not only the alarms — the question is whether the check looked, and a denominator is what answers that. | Both runs quoted in §3 |
| 2 | Decide, on what step 1 measures, whether reach can be read across a declared pair. Record the rejected alternative and what it would have cost the pair. | A decision in §3 |
| 3 | Implement whichever the decision produces, and give the row in `NAMED_AND_UNMARKED` whatever it needs to state its own reason mechanically. | Edited `tests/test_quiet_cases.py` |
| 4 | Write the general form of the finding into the module docstring, where *What this cannot see* already lives. | A paragraph in `tests/test_quiet_cases.py` |
| 5 | Show each new assertion **failing**, one perturbation at a time, and restore the tree between them. | Three failing runs quoted in §3 |
| 6 | Run the module, the suite and `check`, and quote the reading. | Their output in §3 |

**Step 1 is placed first because it can invalidate steps 2–5**, and it did: the plan was written
expecting the question to be *how do you read reach across two project roots*, and the measurement
turned it into a different question with a different answer.

**Outputs**
- tests/test_quiet_cases.py

## 3. Implement

**Step 1 — both halves, with their denominators**

```text
$ ./plugin/bin/taskmd check --root tests/fixtures/planned-deliverable
OK - 1 task(s), 5 field value(s), 6 front-matter value(s), 0 reference(s), 0 dependency edge(s), 0 declared output(s), ...
EXIT=0

$ ./plugin/bin/taskmd check --root tests/fixtures/broken-deliverable
MISSING OUTPUT T-001 declares 'out/report.md', which does not exist

1 problem(s) - 1 task(s), 5 field value(s), 6 front-matter value(s), 0 reference(s), 0 dependency edge(s), 1 declared output(s), ...
```

**`0 declared output(s)` is the whole answer, and it was not the answer this task expected.**
`planned-deliverable` declares `out/report.md`, and the check's own denominator says it examined
**none**. [`check_deliverables`](../plugin/skills/taskmd/taskmd/cli.py) skips an open task *before*
counting, which is T-089's decision working exactly as written.

**So the silence there is not the check looking and staying quiet. It is the check not looking.**

**Decisions & assumptions**

1. **Reach cannot be read across a declared pair, and the reason is not that it is hard** —
   2026-08-22. The partner is a **different project root**. A class firing in `broken-deliverable`
   says nothing about whether the check examined `planned-deliverable`, which is the only thing
   assertion 3 asks. Reading the pair as reach would produce a green that means less than the
   current honest red. **Rejected: a `PAIRS` table teaching assertion 3 to accept a partner
   fixture** — it would have cost the assertion its meaning, and it would have been a hand-kept
   list of exactly the kind `tests/classes.py` and the marks exist to remove.
2. **This is a *gate case*, and no fixture can ever satisfy assertion 3 for one** — 2026-08-22.
   The generalisation is worth more than the row: some quiet cases are quiet because the check
   **excluded the input before looking**. Asking such a case to show the class firing in its own
   fixture is asking for the gate to be removed. So its row in `NAMED_AND_UNMARKED` is **permanent
   by construction**, not a residual awaiting work — and the row now says so, in those words.
   §1's scope-out clause said giving the fixture its own firing case would destroy the pair; the
   measurement says something stronger, that it would destroy the *case*.
3. **What is asserted instead is the gate, labelled as a weaker claim** — 2026-08-22.
   `TheGateCaseShowsItsGateInstead` holds three things true at once, and only the three together
   mean anything:
   - the quiet fixture reports a **zero denominator** for the class's own counter — the check
     looked at nothing, which is what makes the row permanent;
   - the same input **does** fire in the partner — so the class is not simply broken;
   - the two fixtures **differ in the gating field** and **agree on the value the class reads** —
     without which a partner firing for some unrelated reason would pass the second.
   A fourth test asserts there is at least one such row, so the other three cannot pass over an
   empty list.
4. **The row carries the pair; there is no separate table** — 2026-08-22 — so the fact lives once,
   beside the reason it exists, and a row deleted takes its assertions with it.
5. **`check_deliverables` was not changed** — 2026-08-22. Its denominator of zero is *correct*: it
   counts what it examined, and it examined nothing. A reader could misread `0 declared output(s)`
   as *this project declares none*, but the counter's contract is what was examined (T-095), and
   changing it to count what was skipped would make every other denominator mean something else.
   Recorded as judged rather than left as a silence.

**Step 5 — each assertion shown failing, one perturbation at a time**

```text
### "fires_in": "broken-deliverable"  ->  "planned-deliverable"
FAILED ...TheGateCaseShowsItsGateInstead::test_the_pair_differs_in_the_gating_field_and_agrees_on_the_rest
FAILED ...TheGateCaseShowsItsGateInstead::test_the_same_input_fires_once_the_gate_opens
2 failed, 2 passed, 10 deselected

### "gating_field": "status"  ->  "type"
FAILED ...TheGateCaseShowsItsGateInstead::test_the_pair_differs_in_the_gating_field_and_agrees_on_the_rest
1 failed, 3 passed, 10 deselected

### "denominator": "declared output"  ->  "task"
FAILED ...TheGateCaseShowsItsGateInstead::test_the_check_examined_nothing_in_the_quiet_fixture
1 failed, 3 passed, 10 deselected

### tree restored
4 passed, 10 deselected in 0.15s
```

Three perturbations, each hitting the assertion it was aimed at and leaving the others green — so
none of the three is carrying the others.

**Step 6 — the reading, and the gates**

```text
$ python tests/test_quiet_cases.py
Ran 14 tests in 2.271s
OK

$ python tests/test_quiet_cases.py --list
Named by T-198 and not marked - the reading is short by 2, and not because a fixture was out of scope:
  migrated-away          CONFIG ERROR    ...
  planned-deliverable    MISSING OUTPUT  MISSING OUTPUT must not fire on an open task declaring a path that is not there
                                           because the check does not examine the case at all, so no per-fixture assertion can ever show it in reach - `check` on that fixture reports `0 declared output(s)`, its own denominator saying it looked at nothing, because check_deliverables skips an open task before counting (T-089). This row is permanent by construction, not a residual awaiting work - measured 2026-08-22, T-215

$ python -m pytest tests -q
334 passed, 8 subtests passed in 42.69s

$ ./plugin/bin/taskmd check
OK - 219 task(s), ...
EXIT=0
```

330 before, 334 after: the four tests of decision 3.

**Outputs produced**
- [`tests/test_quiet_cases.py`](../tests/test_quiet_cases.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative, and the rejection names what that alternative would have cost the pair | met | §3 decision 1. Rejected: a `PAIRS` table teaching assertion 3 to accept a partner fixture — named with two costs, that it would take the assertion's meaning away and that it is a hand-kept list of the kind the marks exist to remove |
| If reach is made readable across a pair, the mechanism is shown **failing first** on a pair whose firing half does not fire | met | Reach was **not** made readable across a pair — decision 1 — so the criterion's condition does not hold. Its *standard* was applied to what was built instead: §3 step 5 runs exactly the perturbation this clause describes, `fires_in` pointed at a half that does not fire, and two assertions fail. Two further perturbations show the other two biting |
| `planned-deliverable`'s row leaves `NAMED_AND_UNMARKED`, or the reading states why a paired fixture keeps a row there permanently rather than as a residual awaiting work | met | The row stays, and its `why` now says *permanent by construction, not a residual awaiting work*, with the measurement behind it. The module docstring carries the general form under *What this cannot see*, where the reading's other limit already lives. Both are quoted in §3 step 6 |
| `python tests/test_quiet_cases.py` and the suite are green, and the reading is quoted | met | §3 step 6: `Ran 14 tests ... OK`, `334 passed, 8 subtests passed`, and the reading's two unmarked rows quoted in full |

**What review found beyond the table.** The task was framed around *a pair*, and the pair turned out
not to be the operative fact. What makes `planned-deliverable` unmarkable is that its class is
**gated**, and the gate would defeat any instrument — a pair, a second fixture, a cleverer mark. The
title still says *paired*, and that is left as written: it is what the task was raised to ask, and
§3 decision 2 is where the answer moved. A reader who searches for *pair* finds both.

The general form is in the module rather than only in this record, because a premise inside a closed
task expires in silence — which is the same reason
[T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) exists.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none and none arose.
Decision 5 records one thing judged and deliberately not acted on — `check_deliverables`'s
denominator — with the reason, so it is not left as an unstated silence.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All four criteria met, and **the measurement in step 1 changed the question**. `check` on `planned-deliverable` reports `0 declared output(s)` — the check examined nothing, because it skips an open task before counting — so the case is not *hard to reach*, it is **gated**, and no fixture or pair can ever satisfy a reach assertion for one. The row stays in `NAMED_AND_UNMARKED` **permanently by construction**, and what is asserted instead is the gate: four tests, each shown failing under its own perturbation. The general form is in the module docstring, not only here. 330 → 334 tests. **Worked under the multi-phase grant recorded at the top of this Log.** |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its scope forbids the obvious fix.** Giving `planned-deliverable` its own firing `MISSING OUTPUT` case would make it a second `broken-deliverable` and destroy the pair T-089 built. §1 puts that out by name, and this grant does not license it. |
| 2026-08-22 | → proposed | Raised from [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)'s step 1, by applying the mark and running the reader. Raised rather than absorbed: T-211's scope puts *exercising* these fixtures out by name, and the grant on that task authorises phases and not answers — so widening it to make its own first criterion pass is exactly what that grant excludes. `s` because the decision is the work and the code change may be none; `medium` because until it lands, one case T-198 names is held with a reason rather than covered, which is honest and is still a gap in the reading that replaced F-2. |
