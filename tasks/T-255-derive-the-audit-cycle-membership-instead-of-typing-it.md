---
id: T-255
title: Derive the audit cycle membership instead of typing it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: []
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables:
  - tools/audit_cycles.py
  - tests/test_audit_cycles.py
---

# T-255 — Derive the audit cycle membership instead of typing it

## 1. Specify

**Outcome**
One command prints the Files and Bytes columns of
[T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
§2, and the file list for any single cycle, from membership rules held in one place. **It fails when a
tracked path in the subject belongs to no cycle**, so a file added after the plan was written stops
the reading rather than surviving it unexamined.

**Why this one**
T-244's per-cycle figures were computed by hand on 2026-08-23 from a membership list that lives
nowhere in the repository. The totals were verified per item on that day and were correct; nothing
keeps them correct. The audit runs across many sessions and the tree moves between them, which is
exactly the interval a hand-typed partition cannot survive.

**The evidence is another project's, and it is not hypothetical.** htmldeck ran the same method first
and its finding `PR-06` was this: the plan stated counts rather than deriving them, its two coverage
tables could not reconcile, **four files went unread and the run looked complete**. It raised
`T-223` to derive the membership and found a file its old table had counted twice. This task is that
lesson taken before the same cost is paid here, per
[`../CLAUDE.md`](../CLAUDE.md) *Working across my own repositories*.

**Scope**
- In: the membership rules for T-244's eight examining cycles, in one place, with one rule per cycle
- In: a `--plan` output that emits the columns ready to paste, and a per-cycle output naming the files
  a session reads
- In: the whole-partition verdict printed **before** any per-cycle answer, so an unassigned path is
  seen rather than scrolled past
- Out: assigning findings, severities or the register — that is T-244's own work
- Out: shipping this to adopters. It is repository machinery, not part of what an install copies

**Inputs**
- [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
  §2 — the eight cycles and the subject the rules must cover
- htmldeck's `tools/docs/cycles.py` — the working implementation of exactly this, for its shape rather
  than its rules

**Acceptance criteria**
- [ ] The command prints T-244 §2's Files and Bytes columns, and its figures match a hand check of the
      subject on the day it is run
- [ ] Adding a file to `plugin/` and re-running it makes the command **fail**, naming that path. A
      clean run on an untouched tree proves nothing
- [ ] A single cycle's file list can be asked for, and the whole-partition verdict prints first
- [ ] T-244 §2's Files and Bytes are printed by this command rather than typed, and its *how to run
      one cycle* step 2 — which already names this command — resolves to something that runs

**Open questions**
- **Where it lives, and whether it is one script or a check inside the suite.** `tests/` already runs
  on every change, which would catch an unassigned file without anyone asking — but a test cannot emit
  columns to paste. Whoever plans this.

## 2. Plan

**The open question, decided: both, over one set of rules.** `specify` asked whether this is a script
or a check inside the suite, and priced the trade — a test runs unasked but cannot emit columns to
paste. **The trade is false once the rules are separated from their consumers.** A module holds the
membership rules and the subject query; a script front-end prints the columns, and a test module
imports the same rules and asserts the partition on every change. One home, two readers — so this
is not the second write METHOD §4 forbids.

**Rejected: a test alone**, because T-244 §2's table has to be pasted and a test emits a pass or a
failure. **Rejected: a script alone**, because nothing would run it — the defect being fixed is
precisely a check nobody performs, and htmldeck's `PR-06` is what an unrun check costs.

**It lives in `tools/`, not in `plugin/` and not in `tests/`.** `plugin/` is the install boundary and
§1 scopes shipping out. `tests/` would make it a test helper, which is the half of its job that is
not true — a person runs it and pastes what it prints. htmldeck put the same thing in `tools/`, and
§1 already names that file as the shape to follow.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the subject from git rather than typing it — `git ls-files plugin/` plus the three named top-level files — and hold one membership rule per cycle in a single table. | `tools/audit_cycles.py`, carrying the rules and the subject query |
| 2 | Print the whole-partition verdict **first**, before any per-cycle answer, and make an unassigned tracked path a non-zero exit rather than a caution. | The verdict, and the exit behaviour |
| 3 | Emit `--plan` (T-244 §2's Files and Bytes columns, ready to paste) and `--cycle N` (the file list a session reads). | Two outputs from one rule table |
| 4 | Add a test module that imports the rules and asserts the partition, so an unassigned file is caught on every change without anyone asking. | `tests/test_audit_cycles.py` |
| 5 | Show it **failing**: add a file under `plugin/` and confirm both the command and the test name that path. A clean run on an untouched tree proves nothing, and that is this task's whole subject. | The failing output, in §3 |
| 6 | Reconcile the emitted figures against T-244 §2's hand-computed table and account for **every** difference, in both directions. A figure that merely matches is not checked. | The comparison, in §3 |
| 7 | Replace T-244 §2's typed Files and Bytes with what the command prints, and make its *how to run one cycle* step 2 resolve to something that runs. | T-244 §2, edited |

**Step 7 edits T-244 and does not start it.** That record's own criteria ask for the figures to be
derived and for step 2 to resolve; supplying them is this task's outcome. The audit remains unstarted,
and the grant recorded in the Log below covers this record only.

**Outputs this task will produce**

- `tools/audit_cycles.py`
- `tests/test_audit_cycles.py`
- `tasks/T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md`

## 3. Implement

**Decisions & assumptions**
- **A rule is a callable per cycle, and two rules claiming one path is reported rather than resolved
  by order** — 2026-08-23. Ordering would make a doubled member silently belong to the first
  matching cycle, and a doubled member is invisible in a total: the sum still reconciles while one of
  the two readings is wrong. Rejected because it is the failure this task exists to prevent, wearing
  a different hat.
- **The specimen is injected into the derived list, not written to disk** — 2026-08-23, for the
  test. The rule under test is the assignment, and a fixture on disk would also be measuring the
  walk. The disk case is exercised separately, once, by hand — see step 5 below.
- **T-244's decision-section figures were annotated, not rewritten** — 2026-08-23. METHOD rule 5
  corrects the present and annotates the past, and those two figures are evidence an owner accepted.

**Evidence — what was actually run**

**The partition, and it reconciles per cycle rather than only in total.** Seven of T-244 §2's eight
hand-typed rows match the command exactly. The eighth does not, and the difference is the whole
argument for this task:

```
cycle 4 (the binding documents)   typed 2026-08-23: 94,850    derived: 96,417    delta: +1,567
```

Accounted for, in both directions, rather than assumed:

```
BINDING.md                  at ca25d87: 26,803   now: 26,803   delta: 0
bindings/github-issues.md   at ca25d87: 51,397   now: 51,397   delta: 0
bindings/local-markdown.md  at ca25d87: 16,650   now: 18,217   delta: +1,567
```

**The table was correct when it was typed and stale within a day, from a change this project made to
itself** — [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) added a
paragraph to that binding the same evening. Nothing was wrong with the arithmetic; the interval was
the defect, which is exactly htmldeck's `PR-06`.

**Step 5 — shown failing on a real file, which is the criterion this task exists for.** A file was
added under `plugin/` and tracked, then removed:

```
$ python tools/audit_cycles.py --plan
UNASSIGNED  1 tracked path(s) in the subject belong to no cycle.
    plugin/skills/taskmd/docs/method/SPECIMEN-T255.md
    Add a rule in tools/audit_cycles.py CYCLES, or say in T-244 why the subject changed. ...
rc=1

$ python tests/test_audit_cycles.py
FAIL: test_the_partition_is_complete
FAIL: test_the_counts_sum_to_the_subject
```

Both instruments named the path. On the clean tree: `PARTITION OK  31 tracked path(s) ... 32 items`,
`rc=0`, and `Ran 4 tests ... OK`.

**A defect in the test, found by that same run and fixed.** `test_an_unassigned_path_is_reported_by
_name` asserted its injected specimen was the **only** unassigned path, so the moment the tree
genuinely had one it failed — and named the specimen as the problem. It now asserts membership and
checks the specimen is not already in the subject. **A test that fails for someone else's reason is
worse than one that does not fail**, because it is read as evidence about its own subject.

**Outputs produced**
- `tools/audit_cycles.py` — the membership rules, the git-derived subject, the partition verdict,
  `--plan` and `--cycle <n>`
- `tests/test_audit_cycles.py` — four assertions over the same rules, run by CI on every change
- `tasks/T-244-...md` — §2's figures replaced by what the command prints, its *how to run one
  cycle* step 2 made to resolve, and its decision-section figures annotated

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The command prints T-244 §2's Files and Bytes columns, and its figures match a hand check of the subject on the day it is run | met | Seven of eight rows match the hand-typed table; the eighth differs by 1,567 bytes and **every byte of that is accounted for per file, in both directions**. The mismatch is the evidence, not a failure. §3. |
| Adding a file to `plugin/` and re-running it makes the command **fail**, naming that path | met | Done with a real tracked file, not a simulation: `rc=1`, the path named, and the test module failing alongside. §3 step 5. |
| A single cycle's file list can be asked for, and the whole-partition verdict prints first | met | `--cycle <n>` prints the list; `verdict()` runs first in `main` and returns 1 before any per-cycle output, so an unassigned path stops the reading rather than heading it. |
| T-244 §2's Files and Bytes are printed by this command rather than typed, and its *how to run one cycle* step 2 resolves to something that runs | met | §2 now names `python tools/audit_cycles.py --plan`; step 2 names `--cycle <n>`. Both run. |

**Adopter-visible?** no — `tools/` and `tests/` are outside the plugin boundary, so an install copies
neither. `adopter_visible: no` set at `specify` and unchanged.

**Child fix tasks raised**
- none. **One observation was recorded rather than raised**: T-244's subject total lives in four
  places in that one document — §2's grade table, §2's cycle table, and twice in the decisions prose —
  and this command reaches the first two only. It is written into T-244 beside the figures it
  concerns, where the next reader of them meets it. It is not a task because rewriting a dated
  decision is what METHOD rule 5 forbids, and no other action is available.

**The audit is not started, and closing this does not start it.** The grant in the Log covers this
record only, and says so.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **Annotation, not a correction: T-244 §2's Files and Bytes columns were cut later the same day**, on the owner's instruction, so §1's outcome and two of the criteria name columns that no longer exist. They are left as written because they describe what was true when this task ran, which is what METHOD rule 5 protects. **The command is unchanged and still prints the figures** — what changed is that nothing pastes them into a record any more. The reason is in T-244's own Log: the derived figures this task supplied had drifted again within three hours, which argued for the table holding none. |
| 2026-08-23 | planned → done | All four criteria met. **The reconciliation returned a real difference rather than a match**: T-244's cycle 4 was 1,567 bytes behind within a day of being typed, from a change this project made to itself. Shown failing on a real file added under `plugin/`. A defect in the new test — it asserted its specimen was the only unassigned path — was found by that same run and fixed. |
| 2026-08-23 | proposed → planned | Seven steps. **The open question is decided in §2 rather than left for `implement`**: both a script and a test, over one rule table, with each single-sided reading rejected and priced. Step 5 is the criterion this task exists for — a partition check that has never been seen to fail is the defect, not the fix. |
| 2026-08-23 | (no change) | **The owner authorised the full lifecycle on this record**, 2026-08-23, as the subject of a handoff: *"Work T-255 full lifecycle."* **What it covers:** `specify`, `plan`, `implement` and `review` on **T-255 only**, run by the session that picks the handoff up. **What it does not cover:** any other record — in particular [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md), which this unblocks on closing. Closing this does not authorise starting the audit; that is a request the owner makes separately, and the standing rule that a session starts no audit is unchanged. Recorded here rather than left in the handoff because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached. |
| 2026-08-23 | (no change) | **This task now blocks [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)**, on the owner's instruction of 2026-08-23. It was raised as a soft link on the session's recommendation that the generator *should probably* land first; the owner made it a gate. **What changed in T-244:** the edge is on that record's `blocked_by`, its §2 no longer says the defect is shipped knowingly, and its *how to run one cycle* step 2 now asks this command for the file list instead of describing a manual `git ls-files` check nobody would have run. **The `related` edge here was removed** — a dependency already connects the pair in both directions and the inverse is derived, so keeping both would have been the same fact in two homes. |
| 2026-08-23 | → proposed | **Raised while planning [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)**, 2026-08-23, on the owner's instruction to compare that plan against htmldeck's run of the same method and take the better of the two. The comparison returned one defect rather than a preference: T-244's per-cycle Files and Bytes are hand-typed, and htmldeck's `PR-06` is the measured cost of that exact shape — four files unread, two tables that could not reconcile. **Raised rather than fixed inside T-244** because it is machinery T-244 consumes and not part of the audit, per METHOD §5 and this repository's rule that a discovery outside the current task costs one record. T-244 §2 ships the defect knowingly and names this task beside it, so a session running a cycle before it lands knows the partition check is manual. |
