---
id: T-212
title: Report a closed parent that still has an open child
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
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
  green with it. The grant on this record authorises phases and not answers, so `plan` has not been
  written.

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
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that raised this task, that [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) and [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the two — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), raised the same day and not named; nor [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) or [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), whose closure the earlier grant of the same date already confined away from. It authorises **phases, not answers**: an open question that is the owner's stops this record where it stands, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it adds a check class, so it owes the two things a class owes here.** A committed fixture holding exactly one defect, shown failing first; and a judgement of every shipped binding's *cannot occur* statement against the new class, which `plugin/skills/taskmd/docs/BINDING.md` §4 requires and `tests/test_publishing.py` reads. Its quiet cases mark themselves, per [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md). |
| 2026-08-22 | (no change) | **Stopped at an open question before `plan`, under the grant recorded above.** Measuring this repository rather than reading the rule showed the class as scoped would fire three times here, on parents that are `deliverable` and `research` and not one of them an audit - while the rule §1 cites, `audit.md` step 5, is written about an audit's **umbrella**. So the class's meaning is unsettled, and with it whether three records here are wrong. It is not a plan detail: five tests assert `check` is clean on this repository, so a class that fires here turns the suite red rather than reporting. The grant authorises phases and not answers, so no plan was written. The question, both readings and what each costs are in §1. |
| 2026-08-22 | → proposed | Raised from [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md) while answering that task's fourth criterion — *whether `check` reports it too* — by building the case and running it rather than reasoning about it. The answer for the **open** parent is no: an umbrella with an open child is the ordinary state of every audit mid-flight, and reporting it would make a healthy backlog noisy. The **closed** parent is the opposite and returns `OK`, quoted in §1. Raised rather than folded into T-209 because it is a new validator class with a fixture and coverage rows, not a change to what a derived line says — a different size and a different set of things to get right. `medium` and `s`: the rule, the edge and the derivation all exist, so this is a reader for data already there. |
