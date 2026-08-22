---
id: T-212
title: Report a closed parent that still has an open child
type: fix
status: blocked
phase: plan
parent: null
blocked_by: [T-216]
related: [T-209, T-191, T-198]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-212 — Report a closed parent that still has an open child

## 1. Specify

**Outcome**
`check` reports a task that has closed while one of its children is still open — the state
[`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 forbids, and the one nothing
currently notices.

**Why this one**
Found while working
[T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md), by asking that
task's own fourth criterion — *whether `check` reports it too* — and then running the case rather
than reasoning about it. T-209 answered **no** for the open parent, because an open umbrella with an
open child is the ordinary condition of every audit mid-flight and reporting it would make a healthy
backlog noisy. **The closed parent is the opposite**, and it is not covered:

```text
$ taskmd check --root <a project holding T-001 done, with child T-002 proposed>
OK - 2 task(s), 10 field value(s), 11 front-matter value(s), 1 reference(s), ...
```

The rule is written, the edge is stored, the derivation exists — and nothing reads it, which is the
class [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) and T-209 both
belong to. It is a *validator* concern rather than a `context` one: `context` answers about one task
somebody is already looking at, and this state is one nobody is looking at by definition, because
the parent is closed and off every open view.

**It is not the same defect as T-209 and must not be folded into it.** T-209 changed what a derived
line *says* about a task somebody opened. This asks the validator to report a contradiction between
two records, which is a new class, a fixture and a row in the coverage tables — a different size and
a different set of things to get right.

**Scope**
- In: a `check` class for a closed task with at least one open child
- In: the case that must not fire — a closed parent whose children are all closed, and an **open**
  parent with an open child, which is the ordinary state T-209 decided is not a defect
- In: the class's row wherever the shipped coverage tables enumerate classes, including each
  binding's *cannot occur* statement
- Out: `context`'s closing line, which [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) settled
- Out: a dependency whose blocker is still open on a closed task — a different edge kind and its own
  question, if it is one

**Inputs**
- [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) §3 — the
  `check` decision, its reason, and the run above
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the rule
- `tests/fixtures/` — the `broken-*` convention, one defect per fixture, and
  `tests/test_quiet_cases.py` for how a fixture's quiet cases now declare themselves

**Acceptance criteria**
- [ ] The class is shown **failing first**, on a committed fixture holding exactly one such defect
- [ ] It is shown **not** to fire on a closed parent whose children are all closed, and not on an
      open parent with an open child — both quiet cases marked in the fixture so
      `tests/test_quiet_cases.py` reads them
- [ ] The class appears wherever the shipped documents enumerate classes, derived rather than
      hand-listed where a derivation exists — `tests/classes.py` is the one home for the set
- [ ] Each shipped binding's *cannot occur* statement is judged against the new class, since
      `BINDING.md` §4 requires every binding to name what its backend makes impossible
- [ ] `check` is clean on this repository afterwards, or the tasks it names are real

**Open questions**

- ~~**None.** The scope is the residual T-209 named while answering its own criterion.~~
  **Superseded on 2026-08-22, before `plan` began** — the question below was found by measuring this
  repository rather than by reading the rule, and it decides what the class means.

- **Does a child hold *every* parent open, or only an audit umbrella? — the project owner.**
  §1 above cites [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 as the rule this
  class enforces. That step reads *"Close the **umbrella** only when every child is resolved"*, and an
  umbrella is an **audit's** umbrella task. The class as scoped would report every closed parent.

  **The two readings are not equivalent here, and this repository is the evidence.** Run against the
  live tree, the proposed class fires **three** times, and not one parent is an audit:

  | Parent | type | Open child | type |
  | :--- | :--- | :--- | :--- |
  | [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) | `deliverable` | [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | `deliverable` |
  | [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | `research` | [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) | `research` |
  | [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) | `deliverable` | [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) | `research` |

  All three are the same shape: a task finished its own work and left a residual that is parked on an
  external condition. **The tool's own model says they are defects** — `cli.py`'s `holds_open()`
  states that the derived side of a hierarchy edge is the only side that holds a task open, without
  qualifying it to audits. **The method's written rule says they are not**, because it names the
  umbrella.

  **Neither reading is free:**

  - *Every parent.* The three above are real defects and must be repaired before this class can ship,
    because five tests in `tests/test_cli.py` assert `check --root ROOT` exits 0 — so a class that
    fires here turns the suite red rather than merely reporting. The natural repair is **not** to
    reopen three finished tasks but to move those children from `parent` to `related`, which is what
    this project already does for a residual: [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)
    raised its two on 2026-08-22 with `parent: null` and a `related` edge.
  - *Audit umbrellas only.* The class must then read `type: audit`, which is **project vocabulary**
    rather than method vocabulary, so it needs a config key — and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
    shows a new key errors every adopter's config on upgrade. The class fires zero times on this
    repository, so it would also ship with no live case.

  **This is not a plan question and it cannot be assumed away.** It decides the class's meaning, its
  shipped behaviour, whether three records in this repository are wrong, and whether the suite can be
  green with it. The grant on this record authorises phases and not answers, so it was put to the owner.

  **Answered by the project owner on 2026-08-22: a child holds *every* parent open.** Not only an
  audit umbrella. Three consequences, and none of them is a plan detail: the class is a **problem**
  rather than an advisory; it needs no `type` filter and therefore no config key; and the three cases
  above are **real defects in this repository** →
  [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), raised on the same
  instruction and not covered by this record's grant. The two readings that were rejected are priced
  in §2's shape decision, where the alternatives to a rejected choice belong.

## 2. Plan

**The question above is answered, and the answer is what this plan is built on.** The owner settled
on **2026-08-22** that a child holds **every** parent open, not only an audit umbrella. So the class
is a **problem** rather than an advisory, it needs no `type` filter and therefore no config key, and
the three cases in this repository are real defects →
[T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), which this task now
waits on.

**Sequencing.** Step 1 is first because it is the failing-first evidence *and* the step that can
invalidate the rest: if the fixture cannot hold the defect and both quiet cases in one project, the
shape of steps 2–4 changes. Step 6 is placed before the gates rather than after them because the
counts it corrects are prose that a green run does not read — the way this addition goes wrong
silently is by leaving *seventeen checks* and *twelve checks* behind where they are now eighteen and
thirteen.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the fixture — one closed parent with an open child, plus the two cases that must stay silent: a closed parent whose children are all closed, and an **open** parent with an open child. Write the test that asserts the class is reported, run it, and record it **failing** before any check exists. | The fixture under `tests/fixtures/`, the test in `tests/test_cli.py`, and the failing run quoted in §3 |
| 2 | Name the class and write the check. The name answers to `tests/classes.py`'s derivation, so it must be a `problems.append("<NAME> ...` literal in the shape `PROBLEM_PREFIX_RE` reads; the message names the parent, its status and the open child. | `check_closed_parent_open_child` in `cli.py`, registered in `cmd_check`, and a decision in §3 naming the class with the rejected names and why |
| 3 | Run `check` on the fixture. It must report **exactly one** problem, of the new class, and be silent on both quiet cases. | The run quoted in §3, beside step 1's failing run |
| 4 | Mark the two quiet cases in the fixture, in the form `tests/test_quiet_cases.py` defines, and read them back. The reach assertion is satisfiable here because the firing case is in the same fixture — which is the property [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md) records `planned-deliverable` as lacking. | The marks, and the `--list` reading quoted in §3 |
| 5 | Confirm every other fixture is asserted silent about the new class. `tests/test_cli.py` reads the class set from `tests/classes.py`, so this should follow with no edit — **verify it rather than assume it**, by checking the new name appears in the derived set and that the per-fixture silence assertion covers it. | The derived set printed in §3, and a statement of which assertion covers the new class |
| 6 | Judge each shipped binding's *cannot occur* statement against the new class, and correct every count the addition falsifies. Known: `cmd_check`'s docstring says *twelve checks open a task file*; `github-issues.md` says *seventeen checks run on the local backend*. Both are prose the addition makes wrong. | Each binding's judgement recorded in §3 with its reason, the edited regions, and every corrected count named |
| 7 | Run `check` on this repository. It must be clean — which needs [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) closed, since until then the class reports three real records here and five tests in `tests/test_cli.py` assert exit 0. | The run quoted in §3 |
| 8 | Run the binding's *after any write*, run the suite, and sweep what this change made stale. | `index`, `check` and suite output in §3, and every document the sweep touched named |

**Shape of the deliverable, decided — 2026-08-22.** A **problem** class in `cli.py`, one **fixture**
carrying the defect and both quiet cases, and **rows in the shipped documents that enumerate
classes**. *Rejected: an advisory*, which would keep this repository green without T-216 and was
offered to the owner as one of three readings on 2026-08-22; it was not chosen, and it would report
as advice a state the method forbids. *Rejected: scoping the class to `type: audit`*, also offered
and not chosen — it needs project vocabulary, so a config key, and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
records that a new key errors every adopter's config on upgrade.

**Not planned past its horizon.** Step 1 decides whether one fixture can carry all three cases; if it
cannot, steps 2–4 are re-cut and this table is edited in place rather than guessed at now.

**Outputs** — plain paths, because none of them exists yet:

- plugin/skills/taskmd/taskmd/cli.py
- plugin/skills/taskmd/docs/bindings/github-issues.md
- plugin/skills/taskmd/docs/bindings/local-markdown.md
- tests/fixtures/ — one new fixture directory, named at step 1
- tests/test_cli.py

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
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: its `blocked_by` on [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) is real and not a formality.** Plan step 7 needs `check` clean on this repository, and until those three records are repaired the class reports them, which turns five tests in `tests/test_cli.py` red. So that task closes first. Its `specify` question was answered by the owner on 2026-08-22 and the plan is written against that answer — do not re-open it. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task, that [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) and [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the two — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), raised the same day and not named; nor [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) or [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure the earlier grant of the same date already confined away from. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it adds a check class, so it owes the two things a class owes here.** A committed fixture holding exactly one defect, shown failing first; and a judgement of every shipped binding's *cannot occur* statement against the new class, which `plugin/skills/taskmd/docs/BINDING.md` §4 requires and `tests/test_publishing.py` reads. Its quiet cases mark themselves, per [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md). |
| 2026-08-22 | proposed → blocked | Question answered by the **project owner** on 2026-08-22 - a child holds **every** parent open - and the plan written against it. The class is a problem, not an advisory, and needs no config key. **Blocked on [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)** rather than merely waiting on it: step 7 needs `check` clean on this repository, and until those three records are repaired the class reports them, which turns five tests in `tests/test_cli.py` red. T-216 was raised on the owner's own instruction and is **outside this record's grant**, which names T-211 and T-212 and no other task - so this task stops at the end of `plan`. |
| 2026-08-22 | (no change) | **Stopped at an open question before `plan`, under the grant recorded above.** Measuring this repository rather than reading the rule showed the class as scoped would fire three times here, on parents that are `deliverable` and `research` and not one of them an audit - while the rule §1 cites, `audit.md` step 5, is written about an audit's **umbrella**. So the class's meaning is unsettled, and with it whether three records here are wrong. It is not a plan detail: five tests assert `check` is clean on this repository, so a class that fires here turns the suite red rather than reporting. The grant authorises phases and not answers, so no plan was written. The question, both readings and what each costs are in §1. |
| 2026-08-22 | → proposed | Raised from [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) while answering that task's fourth criterion — *whether `check` reports it too* — by building the case and running it rather than reasoning about it. The answer for the **open** parent is no: an umbrella with an open child is the ordinary state of every audit mid-flight, and reporting it would make a healthy backlog noisy. The **closed** parent is the opposite and returns `OK`, quoted in §1. Raised rather than folded into T-209 because it is a new validator class with a fixture and coverage rows, not a change to what a derived line says — a different size and a different set of things to get right. `medium` and `s`: the rule, the edge and the derivation all exist, so this is a reader for data already there. |
