---
id: T-070
title: Decide whether an unused field column is shown at all
type: decision
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-022, T-001]
work_package: v0.1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-070 — Decide whether an unused field column is shown at all

## 1. Specify

**Outcome**
One rule governs whether a column appears in a generated view, applied to stored fields as well as to
edges — so a project that never uses a field does not read it in every index row and every `context`
header.

**Why this one**
Raised as **F-8** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 4 and 5. The shipped default names `work_package` in both `context_fields` and
`index_columns`. Every one of this repository's 58 tasks carries `work_package: none`. Result:

```
tasks/README.md   | ID | Title | Work Package | Status | Phase | ...
                  58 rows, every Work Package cell "-"

taskmd context T-053
status done | phase review | type decision | work_package - | owner maintainer
```

**The code already implements the opposite rule, and says so.** `index_block()`:

> Edge columns appear only when some task uses them. Omitting an unused edge is derived from the data
> rather than configured — a project with no hierarchy should not read a column of dashes, and one
> that starts using it should not have to remember to switch a column on.

That reasoning is exactly as true of `work_package` as of `parent`. It is applied to one of the two
column families and not the other, and this repository is the demonstration.

**The cost, stated rather than asserted.** A dead column in the index is read by everyone who opens
the generated file and by every agent that reads it; a dead field in the `context` header is paid on
**every** `context` call, which is the command whose entire justification is that it returns what is
needed *and nothing else* (R-15). Neither is large. Both are permanent, and both are paid by every
adopting project that takes the default and does not use work packages.

**Why `decision` and not `fix`.** Three answers are defensible and they differ in what they cost an
adopter, not in effort — see the open question. This is a design call about the shipped defaults, and
one of the options touches R-15's headline claim.

**Requirements served**
R-15 (`docs/SCOPE.md`) — *and nothing else* is the claim; §1 *Token cost*; §2 principle 2, since
"which columns have content" is derivable.

**Scope**
- In: whether a stored-field column with no values in the project is rendered, in `index` and in
  `context`.
- In: whether `work_package` belongs in the shipped default's `context_fields` and `index_columns` at
  all.
- Out: the `work_package` **field** and its vocabulary. Removing a field a project may use is not on
  the table; this is about views.
- Out: edge columns, which already behave correctly.
- Out: the ordering rule and the estimate fields, settled in
  [T-022](T-022-filtered-task-listing-for-scripts.md).

**Inputs**
`plugin/taskmd/cli.py` (`index_block`, `cmd_context`, `cmd_list`),
`plugin/taskmd/defaults/config.md` (`context_fields`, `index_columns`), `tasks/README.md`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-8.

**Acceptance criteria**
- [ ] One stated rule covers both column families, or it is recorded why they differ
      <br>*Read after the answer as: the rule covers edge and field columns alike, in the two views.
      `list --json` is outside it by decision rather than by omission, which criterion 6 below now
      carries.*
- [ ] Whatever is chosen, this repository's generated index and `context` output are shown before and
      after, so the saving is measured rather than claimed
- [ ] A project that *does* use the field is unaffected — demonstrated, since
      `tests/fixtures/alt-project` has its own field names and can carry the case
- [ ] Nothing requires an adopter to remember to switch a column on or off (§1 *Invisibility*)
- [ ] `taskmd/defaults/config.md` describes the resulting behaviour, since it is the only description
      of what a config may contain
- [ ] **`list --json` still emits every configured key on a project where a field is unused** —
      asserted, not assumed. Added 2026-08-09 with the answer; the six above predate it and are
      unchanged

**Open questions**
- ~~**Which of three?**~~ **Answered by the maintainer on 2026-08-09: (a), derive it — scoped to
  `index` and `context`, with `list --json` keeping every configured key.**

  So the stated rule is: **a view omits a column no task has a value for; a contract does not.**
  `index` and the `context` header are read — by a person opening the generated file, by an agent
  spending tokens on it — and a column of dashes costs both for nothing. `list --json` is the surface
  a script consumes, and a key that disappears the moment a field falls out of use is a breaking
  change to a caller that did nothing wrong.

  **That scoping is a refinement of (a), not a fourth option, and it disposes of (a)'s own
  counter-argument.** The worry recorded when the question was written — *"a project's `context`
  header changes shape as fields get used, which a script parsing it would feel"* — turned out to be
  about the machine surface rather than about `context`, which
  `plugin/taskmd/cli.py` already documents as a read for a person or an agent while `--json` and the
  tab-separated form are what a script cuts. Once the two are separated the objection has nowhere to
  land.

  *Rejected: (b), dropping `work_package` from the shipped defaults' views.* One line and no
  behaviour change, and it fixes this field while leaving the next unused one to reproduce the
  finding — the inconsistency, not the column, is what makes this worth doing.

  *Rejected: (c), leaving it.* A reserved column does tell a reader the field exists, which is a real
  argument for `index` and a weak one for `context`; it is outweighed by §1 *Invisibility*, since it
  makes a project's views depend on someone remembering to prune a config key.

  **What this does not change:** the `work_package` field, its vocabulary, and its availability to
  any project that uses it. A project that fills the field in sees the column, with nothing to switch
  on — which is the half of `index_block()`'s existing reasoning that the fix inherits.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Capture the **before**: this repository's index header and byte count, and a `context` header, so criterion 2 has something to measure against rather than a claim | The before figures |
| 2 | Extract the test `index_block` already applies to edge columns into one named helper, so the two families share a rule rather than resembling one | `cli.in_use()` |
| 3 | Apply it to `index` and to `context`, and to nothing else | `index_block`, `cmd_context` |
| 4 | Measure the after, on the same two artefacts | The after figures |
| 5 | Demonstrate the case the rule is *for*: a project where one configured field is used and another is not, and then the same project once a single task starts using it | Both transcripts |
| 6 | Assert the contract half — `list --json` and the tab-separated form keep every configured column | `tests/test_cli.py` |
| 7 | Describe the resulting behaviour in the shipped config, which is the only description of what a config may contain | `plugin/taskmd/defaults/config.md` |

**Why the test is project-wide and not per-task.** `context` renders one task, so "a column no task
has a value for" could plausibly mean *this* task. It does not: a header that changed shape between
two tasks in the same project is exactly the instability the rejected counter-argument worried
about, and the project-wide reading gives every task the same header.

**Why step 5 is two transcripts and not one.** "The column disappears" is half the rule. The half
that matters for §1 *Invisibility* is that it comes **back** without anyone editing a config, and
that can only be shown by changing a task and re-running.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — one helper, named for the rule** — 2026-08-09. `in_use(names, tasks)` is the test, and both
  families call it. The alternative was a second inline comprehension beside the edge one; they
  would have looked alike and been free to drift, which is how this finding existed at all — the
  reasoning was written once, in `index_block`'s docstring, and applied to half of what it described.

- **D2 — the tab-separated `list` is a contract too** — 2026-08-09. The answer names `list --json`
  explicitly. `cli.py`'s own comment on the tab-separated form settles the other one: *"a line format
  a caller can read as printed and a script can cut"*. Both are what a script consumes, so both keep
  every configured column. Recorded because the answer did not say it in those words and a later
  reader should not have to infer it from a code comment.

- **What is deliberately not changed:** the `work_package` field, its vocabulary, and its presence in
  the shipped defaults' `context_fields` and `index_columns`. Option (b) — dropping the key — was
  rejected in `specify` for fixing this field while leaving the next unused one to reproduce the
  finding, and nothing here reverses that.

### Steps 1 and 4 — measured, not claimed

All 78 tasks in this repository carry `work_package: none`.

```
                          before                                   after
index header    | ID | Title | Work Package | Status | ...   | ID | Title | Status | ...
tasks/README.md 16755 bytes                                  16399 bytes      -356
context header  status … | type … | work_package - | owner   status … | type … | owner
context T-070   646 bytes                                    629 bytes        -17
```

356 bytes off a generated file a person opens, and 17 off **every** `context` call — which is the
one paid per turn, and the reason this was a finding rather than a preference.

### Step 5 — the rule doing what it is for

A scratch project on the shipped default, two tasks, `owner` used and `work_package` not:

```
context T-001    status proposed | phase specify | type deliverable | owner someone
index header     | ID | Title | Status | Phase |
```

`work_package` gone; `owner`, which is used, still there — so this drops unused columns and not
configured ones. Then **one** task is given `work_package: WP1` and nothing else changes:

```
context T-001    status proposed | phase specify | type deliverable | work_package - | owner someone
index header     | ID | Title | Work Package | Status | Phase |
```

The column is back with no config edited, and it is back on **T-001**, which still has no value —
because the question is whether the project uses the field. That is criterion 4 in a transcript.

### Step 6 — the contract, untouched

```
taskmd list --json --limit 1
  ['blocked', 'blocked_by', 'blocks', 'children', 'id', 'open', 'parent', 'phase',
   'related', 'status', 'title', 'work_package']

taskmd list --limit 1
  T-018   done   -   review   Stop the pre-publish fixture tripping its own check
```

`work_package` still keyed in the JSON, still a column in the tab-separated form — the `-` in that
line is it. Asserted by `test_list_emits_every_configured_column_even_when_unused`.

### A project that uses its fields is unaffected

`alt-project` names three fields no other project does, and uses all three:

```
context ISSUE-0001   state shipped | size S | area exterior
index header         | ID | Title | Size | State | Epic | Stories | Depends On | ... |
```

Nothing dropped. Its generated index was removed again afterwards; the fixture ships without one.

```
python -m pytest tests -q             129 passed, 4 subtests passed
python -m unittest discover -s tests  Ran 129 tests ... OK
taskmd check                          OK - 78 task(s), ...
```

**Outputs produced**
- `plugin/taskmd/cli.py` — `in_use()`, and the two views calling it
- `plugin/taskmd/defaults/config.md` — a `## Views` section stating the rule and its exception
- `tests/test_cli.py` — `AViewOmitsAnUnusedColumnAndAContractDoesNot`, three tests
- `tasks/README.md` — regenerated, one column narrower

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One stated rule covers both column families, or it is recorded why they differ | met | One helper, `in_use()`, called by the edge and field paths alike. The rule was always *written* once — in `index_block`'s docstring — and applied to half; now the code matches the sentence |
| This repository's index and `context` output are shown before and after, so the saving is measured | met | §3 — 16,755 → 16,399 bytes of index, 646 → 629 per `context`. The second is the one paid every turn |
| A project that *does* use the field is unaffected — demonstrated on `alt-project` | met | Three fields, all used, all still shown. And the sharper case in §3 step 5: a project using one configured field and not another keeps the one it uses |
| Nothing requires an adopter to remember to switch a column on or off | met | §3 step 5's second transcript — one task gains a value, the column returns, no config touched |
| `taskmd/defaults/config.md` describes the resulting behaviour | met | A new `## Views` section, carrying the rule, the contract exception, and the note that edge columns have always worked this way |
| `list --json` still emits every configured key on a project where a field is unused — asserted, not assumed | met | §3 step 6, and a test. D2 extends it to the tab-separated form on the strength of `cli.py`'s own description of that surface, which the answer did not name |

**Child fix tasks raised**
- none. All six met, including the one added with the maintainer's answer.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All six criteria met, including the one added with the answer. The rule now lives in **one** helper that both column families call — it had always been *written* once, in `index_block`'s docstring, and applied to half of what it described, which is exactly how the finding came to exist. Saving measured rather than claimed: 356 bytes off the generated index, and 17 off every `context` call, which is the one paid per turn. The transcript that matters is the second one: after a single task gains a `work_package`, the column returns — on a task that still has no value, because the question is whether the *project* uses the field — with no config edited. D2 extends the contract half to the tab-separated `list` as well as `--json`, on the strength of `cli.py`'s own description of that surface, and records that the answer did not say so in those words. |
| 2026-08-09 | → in_progress | Plan captures the *before* as step 1, because criterion 2 asks for a measured saving and the artefacts it measures are both regenerated by the fix. It also settles the reading of "a column no task has a value for" as project-wide rather than per-task: a `context` header that changed shape between two tasks in one project is the instability the rejected counter-argument worried about. |
| 2026-08-09 | → specified | Answered: (a), derive it, scoped to `index` and `context` with `list --json` keeping every configured key. The rule that comes out of it is worth more than the choice — **a view omits a column no task has a value for; a contract does not** — and it settles the next unused field without anyone re-deciding, which is why (b)'s one-line fix was rejected. The scoping is a refinement rather than a fourth option, and it removes (a)'s own recorded counter-argument: the variable-shape worry was about the machine surface, and `--json` and the tab-separated form are what a script cuts, not `context`. One criterion added with the answer — that `--json` still emits every configured key on a project where a field is unused — because a carve-out that is only written in prose is a carve-out the implementation can forget; the six that predate it are unchanged, and criterion 1 gains a reading note rather than an edit. Not in scope and worth restating: the `work_package` field itself survives, and a project that fills it in sees the column with nothing to switch on. |
| 2026-08-09 | → proposed | Raised as F-8 from the T-059 audit, clauses 4 and 5. Counted before write-up: all 58 tasks carry `work_package: none`, so the generated index holds 58 dashes and every `context` header carries a dead field. Typed `decision` because the three answers differ in what they cost an adopter rather than in effort, and one of them changes the shape of `context`'s output. The clause-5 half is that the code already states the cheaper rule for edge columns and applies it to half the problem. |
