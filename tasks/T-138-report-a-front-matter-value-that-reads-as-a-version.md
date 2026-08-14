---
id: T-138
title: Report a front-matter value that reads as a version
type: fix
status: done
phase: review
parent: null
blocked_by: [T-137]
related: [T-100, T-106, T-136]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-12
updated: 2026-08-12
deliverables:
  - plugin/skills/taskmd/taskmd/cli.py
  - plugin/skills/taskmd/taskmd/defaults/config.md
  - tasks/_task-template.md
  - tests/test_cli.py
---

# T-138 — Report a front-matter value that reads as a version

## 1. Specify

**Outcome**
`check` reports a front-matter value shaped like a version, so a project that labels its groupings
`v0.2` learns it on the next run rather than after its labels and its releases have come apart. The
task template and the shipped default stop pointing an adopter at a version in the first place.

**Why this one**
[T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) decided this and measured
the rule that carries it: 137 hits on this repository before the rename, 0 across 53 shipped
fixtures, and one false-positive class that the two estimate fields already exempt. The build is out
of that task's scope on purpose, so it is here. **Two independent projects reached the same defect**,
which is why it is the tool's to catch rather than each backlog's to remember.

**Scope**
- In: the check, its line, and a fixture proving the alarm — no existing fixture can serve, because
  all 53 are quiet (T-137 §3).
- In: the wording in [`_task-template.md`](_task-template.md) and the shipped default config that
  told an adopter the field holds *the release*.
- Out: the predicate, the exemption, the line granularity, the surface and the advisory semantics.
  All five are decided in T-137 §3 D1–D5 and are implemented here, not revisited.
- Out: a config key. T-137 D2, on T-106's price.
- Out: relabelling this repository, which is
  [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md).

**Inputs**
- [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) §3 — the five decisions
  and the two runs behind them.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) — the advisory
  line class this reuses, including why it has no off switch.

**Acceptance criteria**
- [ ] `check` prints one line per distinct version-shaped front-matter value, naming the field, the
      value and how many tasks carry it — not one line per task.
- [ ] It is advisory: the exit status does not move, the problem count does not change, and there is
      no flag to switch it off.
- [ ] A value with three or more components is never reported, so a project recording the version its
      work shipped in reads nothing.
- [ ] The fields named by `effort_field` and `value_field` are exempt, so a project estimating in days
      reads nothing.
- [ ] Shown to **fail**: a fixture carrying the defect reports it, and the existing fixtures stay
      silent. A clean pass proves nothing.
- [ ] The task template and the shipped default no longer point an adopter at a version, and the
      default documents the line — it is the only description of what `check` reports.
- [ ] `check`, `index` and the suite are green, and `check` is silent on this repository, which had
      137 hits before [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md).

**Open questions**
- none. The mechanism was settled by T-137; this task's boundary raised none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | The check and its wiring into `cmd_check`, appending to `advisories` | `cli.py` |
| 2 | A fixture carrying the defect, since all 53 existing ones are silent | `tests/fixtures/label-shaped-value/` |
| 3 | Tests: it fires, it is advisory, three-part is silent, the estimate fields are exempt, a clean project is silent | `tests/test_cli.py` |
| 4 | The wording that sent adopters to a version, in both places an adopter meets it | the template, the shipped default |
| 5 | Prove both directions and the tree | Recorded output, §4 |

**Shape decisions.**

**D1 — the line reuses `advisories`, not a new list.** `cmd_check` already prints advisories on both
branches, before `Scope`, so a project whose labels are version-shaped *and* which also has real
problems still reads it. Its own prefix rather than a second `CONFIG DRIFT`, for the reason T-121
recorded: two advisories that are not each other should not answer one grep.

**D2 — it counts its own denominator.** The check examines every scalar front-matter value of every
task, which is a different population from the vocabulary comparisons already counted as *field
value*. *Rejected: report no count*, on the grounds that it scans material already parsed — but a
scan that reports only its hits cannot be told from one that ran on nothing.

## 3. Implement

### The fixture, and the behaviour it did not have

`tests/fixtures/label-shaped-value/` is one project carrying all four behaviours, because they are
one decision and a fixture proving three would let the fourth regress in silence. Its config declares
`effort_field: days` and enumerates nothing but `status`, so every check in it has to work from shape.

```text
OK - 3 task(s), ... 1 vocabulary row(s), 16 front-matter value(s)
LABEL SHAPE  milestone: '2.1' on 1 task(s) reads as a version; a release of that number is a different thing
LABEL SHAPE  targets: '3.0' on 1 task(s) reads as a version; a release of that number is a different thing
LABEL SHAPE  work_package: 'v0.2' on 2 task(s) reads as a version; a release of that number is a different thing
```

Four silences in that run carry as much as the three lines: `shipped_in: 0.4.0` and `targets: 1.4.2`
are versions recorded correctly, `days: 1.5` is a quantity, and `v0.2` on two tasks is **one** line.

**The fixture passed all four and the check still crashed on the first real tree it met.**

```text
  File ".../cli.py", line 795, in check_label_shape
    if LABEL_SHAPED.match(value.strip()):
AttributeError: 'list' object has no attribute 'strip'
```

A field the schema does not name is carried as written, so it arrives as a **list** when the task
wrote one — and every task in this repository has `deliverables`, while the fixture had no list-valued
field at all. The fixture was decisive about the rule and silent about the data shape. `targets` is
in it now, holding `3.0` and `1.4.2` so the list path is asserted in both directions.

### Both directions

```text
this repository:  OK - 138 task(s), ... 2059 front-matter value(s)   (no LABEL SHAPE line)
every other fixture with a .taskmd:  silent
```

This tree carried **137** of these until [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md),
which is why `test_this_repository_is_silent` asserts against it: a label sneaking back in fails the
suite rather than a reader.

**Decisions & assumptions**
- **D3 — list values are read, not skipped** — 2026-08-12. Found by running the check on the real
  tree after the fixture was green, which is the only reason it was found before an adopter found it.
  A skip would have been invisible: no test would have failed and no line would have appeared.
- **Assumption: the shipped default is not in the dash gate's covered set.** It already carried em
  dashes before this edit, and `test_publishing` is green with the new section in place.

**Outputs produced**
- [`../plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py) — `check_label_shape` and its wiring
- [`../plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — *A label that reads as a version*, the only description of what the line reports
- [`_task-template.md`](_task-template.md) — the placeholder no longer says *release*
- [`../tests/test_cli.py`](../tests/test_cli.py) — ten tests
- `tests/fixtures/label-shaped-value/` — the reproduction case

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One line per distinct value, naming field, value and task count | met | `work_package: 'v0.2' on 2 task(s)`, and three lines for a fixture that would print four per task |
| Advisory: exit status unmoved, problem count unchanged, no off switch | met | Exit 0 on the fixture with three lines printed, and no `problem(s)` in the output. No flag exists |
| Three or more components never reported | met | `shipped_in: 0.4.0` and `targets: 1.4.2` silent in a run that reported `targets: 3.0` from the same list |
| `effort_field` and `value_field` exempt | met | `days: 1.5` silent. The exemption reads two keys that already exist, so no config gained one |
| Shown to fail, and the existing fixtures stay silent | met | Both directions, and the silent direction over every fixture that is a taskmd project plus this repository |
| The template and the shipped default no longer point at a version, and the default documents the line | met | Placeholder now reads *a label, not a version number*; the default carries the section and the reasoning, and nothing restates it elsewhere |
| `check`, `index` and the suite green, and this repository silent | met | `OK - 138 task(s), ... 2059 front-matter value(s)`; 246 tests, `OK (skipped=3)`, up from 236 |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → done | All seven criteria met. **A fixture can be decisive about the rule and silent about the data.** This one carried every behaviour the decision named — the shape predicate, the field-name independence, the version exemption, the estimate exemption, the per-value line — passed all of them, and the check still crashed the moment it was pointed at a project whose tasks declare `deliverables`, because a field the schema does not name arrives as a list. Nothing in the suite would have caught it; running the thing on a real case did, which is this repository's rule and is why the rule exists. The other half worth carrying is that the check is now asserted against **this tree**, which held 137 of these last week: the corpus that produced the rule is the regression test for it. |
| 2026-08-12 | → in_progress | Specify and plan agreed under the authorisation below. `specify` raised no question — T-137 had settled the mechanism, and what was left was a boundary. |
| 2026-08-12 | → specified | **Authorisation (METHOD §3.1):** the project owner accepted the recommendation *run T-138 now*, put to them on 2026-08-12 against a next step offering to take it end to end, and answered *recommended answers accepted*. It covers this task through all four phases and reaches no other task. |
| 2026-08-12 | → proposed | Raised by [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md), whose scope put the build out so that the mechanism question could be settled without one. It carries no open mechanism question: the predicate, the exemption, the granularity and the semantics are all decided and measured there. **The owner's authorisation of 2026-08-12 covers T-136 and T-137 and does not reach this task** (METHOD §3.1), so it waits to be asked for. |
