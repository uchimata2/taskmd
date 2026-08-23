---
id: T-216
title: Repair the three closed parents that still have an open child
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-212, T-135, T-168, T-192]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-216 — Repair the three closed parents that still have an open child

## 1. Specify

**Outcome**
No task in this repository is closed while one of its children is open. Each of the three current
cases is judged on its own and repaired, so that
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)'s class can ship reporting a
real state rather than this project's own backlog.

**Why this one**
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) measured the proposed class
against the live tree before planning, and it fires three times:

| Parent | type | Open child | type |
| :--- | :--- | :--- | :--- |
| [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) | `deliverable` | [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | `deliverable` |
| [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | `research` | [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) | `research` |
| [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) | `deliverable` | [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) | `research` |

**The owner settled the rule on 2026-08-22**: a child holds **every** parent open, not only an audit
umbrella — so these three are real defects rather than a shape the method allows. The reasoning, both
readings and what each costs are in
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1, and are not repeated here.

**Why it is not part of T-212.** That task ships a validator class; this one corrects three records
it happens to catch, two of which are closed. They are different work with different risks, and
folding them together would let a green suite stand in for a judgement about three tasks — which is
the reverse of what a validator is for. Raised on the owner's instruction, in the same answer that
settled the rule.

**Scope**
- In: judging each of the three on its own record, and repairing it
- In: the same sweep run again afterwards, so the count is measured rather than assumed
- Out: **the check class itself**, which is
  [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)
- Out: any other edge kind. A dependency whose blocker is open on a closed task is a different
  question, and T-212 §1 already puts it out

**The default repair, and why it is a default rather than the answer.** Move the child from `parent`
to `related` on its own record: all three children are residuals parked on an external condition, and
that is how this project already raises one — [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)
raised its two on 2026-08-22 with `parent: null` and a `related` edge. **It is a default because the
alternative is real**: where the parent genuinely is not finished until the child is, the repair is to
reopen the parent, and only that record can say which it is. Reopening a closed task is a change to
what a record says about the **present**, which METHOD rule 5 allows; nothing here rewrites what any
of them says about the past.

**Inputs**
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1 — the question, the
  owner's answer, and the sweep that found the three
- The six records named in the table above
- `plugin/skills/taskmd/docs/METHOD.md` §4 — which edge to use, and rule 5 on correcting a record

**Acceptance criteria**
- [ ] Each of the three is judged **individually**, with the judgement and its reason recorded — a
      blanket re-edge of all three without reading them does not meet this
- [ ] Where a child is re-edged, its parent's record is annotated rather than rewritten, so the
      original relationship is still legible
- [ ] The sweep is re-run and reports zero, and the output is quoted
- [ ] `check`, `index` and the suite are green, and the output is quoted

**Open questions**
- **None.** The rule was settled by the owner on 2026-08-22; which repair each record needs is this
  task's work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run the sweep T-212 §1 used, before touching anything, so the three cases are measured now rather than inherited from that record. | The sweep's output, quoted in §3, naming each parent, its status and type, and its open child |
| 2 | Read what the **method** says a review does with an unmet criterion, because that is what produced these three. | A recorded finding in §3 saying whether the shipped method permits the state being repaired |
| 3 | Judge [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md)/[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) on T-135's own record: is its outcome finished, or does it need T-182? | A decision in §3, with the rejected repair and why |
| 4 | The same for [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)/[T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md). | A decision in §3, with the rejected repair and why |
| 5 | The same for [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md)/[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md). | A decision in §3, with the rejected repair and why |
| 6 | Apply each repair to the **child's** front-matter, which is where the hierarchy edge is stored. | Three edited task files |
| 7 | Annotate each parent with a Log row saying what was re-edged and why, leaving its §4 untouched. | Three Log rows; no §4 rewritten |
| 8 | Re-run the sweep of step 1. | Its output, quoted in §3, reporting zero |
| 9 | Run `check`, `index` and the suite. | Their output, quoted in §3 |

**Shape decision — the repair is applied to the child, not to the parent.**
The hierarchy edge is stored once, on the child (`METHOD.md` §4, *store the forward edge*), so
`parent: null` plus a `related` edge on the child is a **one-field** change that leaves the parent's
record as the history it is. The rejected alternative was to edit the parent's `§4 Review` table
where it names the child — which would rewrite what a closed record says about the past, forbidden by
`METHOD.md` rule 5, and would not move the edge the sweep actually reads.

**Step 2 is deliberately placed before any judgement.** If the method itself tells a reviewer to
produce this state, then the three are not three careless closures and the judgements in steps 3–5
have to be made against that, not against an assumption that somebody slipped.

**Outputs**
- `tasks/T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md`
- `tasks/T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md`
- `tasks/T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md`
- `tasks/T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md`
- `tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md`
- `tasks/T-192-require-every-binding-to-declare-its-validator-coverage.md`

## 3. Implement

**Step 1 — the sweep, before anything was touched**

```text
$ python sweep.py            # parent/status read from front-matter; open_statuses from .taskmd/config.md
tasks read: 218
closed parents with an open child: 3
  T-135 (done/deliverable)  <-- open child T-182 (proposed/deliverable)
  T-168 (done/research)  <-- open child T-176 (proposed/research)
  T-192 (done/deliverable)  <-- open child T-199 (proposed/research)
```

Three, the same three [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1
found, and measured again here rather than carried across from that record.

**Step 2 — the finding that changed how steps 3–5 were judged, and it is not small**

**The shipped method tells a reviewer to produce this state.**
[`review.md`](../plugin/skills/taskmd/docs/method/review.md) step 3 reads *"For anything not met,
raise a **child** task"*, and step 6 reads *"**Close the task** when every criterion is met **or
carried**"*. [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §2's `review` exit criterion says
the same: *"Every criterion is either met or carries a child task that will meet it."*

So a task that carries an unmet criterion into a hierarchy child and then closes has done exactly
what the method instructs — and it lands in precisely the state the owner ruled on 2026-08-22 is a
defect. **All three of these were produced that way.** They are not careless closures.

Two consequences, and they go to different places:

- *For this task*: the judgements below are **not** *did somebody slip?* but *is the parent's outcome
  actually finished?* — which is the question the method's own `implement` exit criterion already
  answers, and it is answerable per record.
- *For the method*: the contradiction is real and outlives all three repairs. It belongs to
  [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md), whose §1
  surveyed `METHOD.md` §4, `audit.md` step 5 and `cli.py` and **missed `review.md` and `METHOD.md`
  §2** — the two places that state the opposite rather than merely a narrower version. Written into
  that record on 2026-08-22, not fixed here: a finding is never fixed where it is found
  (`METHOD.md` rule 4).

**Decisions & assumptions**

1. **T-135/T-182 — re-edge to a soft edge; T-135 stays closed** — 2026-08-22.
   The hard case, because T-182 was raised from a criterion recorded **not met**. T-135's outcome is
   the rule in `docs/PUBLISHING.md` §7, and that rule was **used**: applied to `v0.4.0`'s note, where
   it found at least 21 omissions against the 6 a hand-sample had found. `implement`'s exit criterion
   — the outcome checked by being used, with the evidence recorded — is met on the real artifact. The
   unmet criterion asks the rule to be applied to *the next* release, which is an external condition,
   not a missing part of the deliverable. **Rejected: reopen T-135**, which would return a finished
   and exercised rule to every open view until an unscheduled release happens, and would say the
   deliverable is incomplete when what is incomplete is the world.
2. **T-168/T-176 — re-edge to a soft edge; T-168 stays closed** — 2026-08-22.
   T-176 was **not** raised from a failed criterion at all: T-168's one failure went to T-174, and
   T-176 came out of `review` step 5 as a residue — the survivor bullet has not had an *uninvolved
   reader*. T-168's outcome, the price with its evidence, exists and was checked. A stronger test of a
   finished result is not a part of it. **Rejected: reopen T-168**, which would park a closed research
   task on a person nobody here can produce.
3. **T-192/T-199 — re-edge to a soft edge; T-192 stays closed** — 2026-08-22.
   The clearest. **Every** criterion of T-192 is met, so there is nothing to reopen it against, and
   its own §4 states the argument already: T-199 is *"a stronger test of a clause that already works
   rather than a gap in it."* **Rejected: reopen T-192** — it would contradict a review whose table
   has no failed row.
4. **The repair is written on the child, never on the parent** — 2026-08-22.
   The hierarchy edge is stored once, on the child (`METHOD.md` §4). So each repair is `parent: null`
   plus a soft edge on the child's own front-matter; T-176 already carried `related: [T-168, ...]`, so
   there it was a single field. Each parent gets a **Log row** saying what moved and why, and no
   parent's §4 is touched — `METHOD.md` rule 5: correct the present, annotate the past.
5. **All three landed on the same repair, and that is a result rather than a shortcut** — 2026-08-22.
   Criterion 1 forbids a blanket re-edge. Each was judged on its own record and the three reasons are
   different — an unmet criterion waiting on a release, a step-5 residue waiting on a reader, and a
   fully-met review whose child is a stronger test. What they share is the shape T-212 §1 named:
   **a finished outcome with a residual parked on an external condition.** Had one of them been a
   parent whose own outcome was incomplete, decision 1 shows the argument that would have reopened it.

**Step 8 — the sweep, re-run after the repairs**

```text
$ python sweep.py
tasks read: 218
closed parents with an open child: 0
```

**Step 9 — the tool on itself**

```text
$ ./plugin/bin/taskmd index
Wrote tasks/README.md - 12 active, 206 closed

$ ./plugin/bin/taskmd check
OK - 218 task(s), 1090 field value(s), 3673 front-matter value(s), 721 reference(s), 25 dependency edge(s), 331 declared output(s), 1 index file(s), 206 closed record(s), 250 document(s), 3271 link(s), 4711 table row(s), 2 template(s), 10 template field value(s), 5 vocabulary row(s), 3623 section reference(s)
EXIT=0

$ python -m pytest tests -q
325 passed, 8 subtests passed in 57.05s
```

**Outputs produced**
- [`tasks/T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md`](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)
- [`tasks/T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md`](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)
- [`tasks/T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md`](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)
- [`tasks/T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md`](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md)
- [`tasks/T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md`](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)
- [`tasks/T-192-require-every-binding-to-declare-its-validator-coverage.md`](T-192-require-every-binding-to-declare-its-validator-coverage.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each of the three is judged **individually**, with the judgement and its reason recorded — a blanket re-edge of all three without reading them does not meet this | met | §3 decisions 1–3, one per pair, each citing that parent's own §4 and naming a different reason: an unmet criterion parked on a release that does not exist, a step-5 residue parked on an uninvolved reader, and a review with no failed row. Decision 5 states outright that the common outcome is a finding about the three, and names what would have reopened one |
| Where a child is re-edged, its parent's record is annotated rather than rewritten, so the original relationship is still legible | met | Each parent gained one Log row naming the child, the edge that moved and why; no parent's §4 was edited. T-135's §4 still records criterion 4 as *carried* and still points at T-182, which is what makes the original relationship readable |
| The sweep is re-run and reports zero, and the output is quoted | met | §3 step 8: `closed parents with an open child: 0`, from the same script as step 1, quoted both times |
| `check`, `index` and the suite are green, and the output is quoted | met | §3 step 9. `check` exit 0, `index` wrote 12 active / 206 closed, `325 passed, 8 subtests passed` |

**What review found beyond the table.** Step 2's finding — that `review.md` and `METHOD.md` §2 both
**instruct** the state this task repaired — is the more valuable half of the work and is not this
task's to fix. It is written into
[T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md), which owns
where the rule lives, as an addition to a survey that had missed both documents.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none, and none arose: the
owner's ruling was already given, and every judgement here was answerable from the records
themselves. Nothing is addressed to anyone else.

**Child fix tasks raised**
- none. The one finding belongs to an open task that already exists.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All four criteria met. Three records judged one at a time and repaired on the child's own front-matter; the sweep that found them re-run and reporting zero; `check`, `index` and the suite green, all quoted in §3. The repair unblocks [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), which can now ship a class that fires on nothing here. **Worked under the multi-phase grant recorded at the top of this Log**, which covers phases and not answers — no answer was needed. `review` found one thing beyond the table and it went to [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it holds [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), so it comes first among the six.** Its first criterion asks for each of the three to be judged individually — a blanket re-edge of all three without reading them does not meet it. |
| 2026-08-22 | → proposed | Raised from [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), on the owner's answer of the same date settling that a child holds every parent open and not only an audit umbrella. Raised as its own task rather than folded into T-212 because the owner's answer said so, and because correcting three records — two of them closed — is a different risk from shipping a validator class. `s` and `medium`: three records, each needing a judgement rather than an edit, and T-212 cannot reach a green suite until this closes. **This task is not covered by the multi-phase grant of 2026-08-22**, which names T-211 and T-212 and no other task. |
