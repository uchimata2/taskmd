---
id: T-030
title: Settle the schema module's own entry point
type: decision
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-020, T-023, T-065]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-06
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/schema.py]
adopter_visible: no
---

# T-030 — Settle the schema module's own entry point

## 1. Specify

**Outcome**
taskmd has one documented command surface. `python -m taskmd.schema` is either removed, or it is a
stated part of the surface with the same argument convention and the same output guarantees as the
rest — not a fifth entry point that only its own module docstring knows about.

**Why this one**
Raised as **F-4** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 1 and 3. `taskmd/schema.py` carries its own `main()`, advertised in that module's docstring
as `python -m taskmd.schema [project_dir]`. It runs, and it prints a debug dump of the resolved
schema and the whole task graph.

It is absent from `COMMANDS`; from `taskmd/cli.py`'s docstring, which opens *"The four commands"*;
from `CLAUDE.md`, which says the same; and from `docs/SCOPE.md` non-goal 11, whose 2026-08-05
amendment carved out exactly one addition and named it. It also takes a **positional** directory
where every other entry point takes `--root PATH`.

~~**The output is the harder half.**~~ **The output half is gone.** It was the harder half when this
task was raised: on the success path the entry point printed the config's `source`, which for a
project with no `.taskmd/config.md` was the absolute path to wherever taskmd was installed. That
stopped being true when `_display()` landed in commit `580d22b`, closing
[T-011](T-011-runtime-discovery-and-project-hook-commands.md) — **after** this task was raised. Run
today against a project outside this repository:

```
python -m taskmd.schema <a project elsewhere>
SCHEMA ERROR: taskmd/defaults/config.md: tasks_dir is 'tasks', but the project root has no such
folder. ...
```

Machine-independent, and criterion 2 below is therefore already satisfied and **cannot drive the
removal**. Reconciled by [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) on
2026-08-09; the decision this task exists to take is untouched.

**What still stands, and it is the whole task.** The entry point exists, runs, is absent from every
statement of the command surface, and takes a **positional** directory where everything else takes
`--root PATH`. One command surface, stated once and true — that is the outcome, and it never
depended on the output.

**Dedupe — this is not [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md).**
T-023 shares the root cause (`schema.source`) and has itself been overtaken: its leak is gone too,
and what remains there is a wording preference — whether the prefix reads `<shipped default>` or the
file's real name. If that string changes, this entry point prints it too while it exists, which is a
reason to check the two together and not a reason to merge them.

**Requirements served**
R-18, R-20 (`docs/SCOPE.md`); non-goal 11, which is about what the surface is.

**Scope**
- In: whether `taskmd/schema.py`'s `main()` exists, and if it does, its arguments and its output.
- In: the inline re-implementation of `link_names` inside that `main()` — the same derivation is
  already written in `taskmd/cli.py`, and it survives or dies with the entry point.
- Out: `taskmd/cli.py`'s four commands.
- Out: the `SchemaError` prefix, which is T-023's.

**Inputs**
`taskmd/schema.py` (`main`, `load_schema`, `DEFAULT_CONFIG`, `_check_tasks_dir`), `taskmd/cli.py`
(`link_names`, module docstring), `docs/SCOPE.md` R-20 and non-goal 11,
[T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-4.

**Acceptance criteria**
- [ ] Exactly one statement of what taskmd's command surface is, and it is true — falsified by any
      runnable entry point the documented surface does not name
- [x] No entry point prints an absolute path on **any** path, success or failure (R-20); shown on a
      project with no `.taskmd/config.md`, which is the case that produces it — **already met**, by
      `_display()` in `580d22b`. Kept as written, per
      [`review.md`](../plugin/skills/taskmd/docs/method/review.md) *Changing a criterion*: it was a real criterion
      and it is satisfied, but by another task, so it can no longer be evidence for removing this
      entry point
- [ ] If the entry point survives, it takes `--root PATH` like everything else — two conventions for
      the same argument is the drift this project exists to remove
- [ ] The `link_names` derivation exists in one place
- [ ] Checked against T-023 before implementing, so the overlapping half is fixed once

**Open questions**
- None. **Q1 — keep it or remove it? — answered by the maintainer on 2026-08-06: remove.**

  The recommendation offered here was that everything it prints is available from `context` and
  `list --json`. That is true of the task-graph half only, and it was the weaker argument. The
  decisive one is that **the entry point's one distinguishing capability does not exist**: it is the
  only view of the *resolved schema* as opposed to the tasks — but a taskmd config **replaces** the
  default rather than merging with it (`taskmd/defaults/config.md` §*Deliverables*, and the same
  rule stated for every key), so there is no resolution step to inspect. "The resolved schema" is
  always the config file the reader already has open.

  *Rejected: keeping it as part of the documented surface.* It would have to gain `--root PATH`,
  test coverage, R-20-clean output and a line in every place that says what the surface is — the
  cost of a fifth command for a view whose content is a file plus two commands.

  **Not affected by the removal, and to be stated when it lands:** `taskmd/schema.py` remains
  importable and is exercised directly by `tests/test_schema.py`; T-019's review used this module as
  evidence that config validation fires for callers that never touch the CLI. That guarantee lives in
  `load_schema`, not in `main()`, and survives it. The removal closes an undocumented *command*, not
  the module's API — bindings (`docs/BINDING.md`) reach the schema through the import, which is the
  path that matters.

## 2. Plan

The answer is *remove*, so the code half is small. What the plan spends its steps on is the
criterion the removal is judged by — criterion 1 is about the whole surface, not about this module,
and it can only be judged against a set gathered **before** the edit.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Gather the two sets criterion 1 is judged against, before touching anything: every runnable entry point in the shipped tree, and every place that states what the surface is. | Both lists in §3 |
| 2 | Check the removal against what depends on it — the config's pass-through claim once rested on this `main()` being the only thing that printed carried fields, and `load_schema`'s guarantee must survive. | A recorded verdict in §3, with the task that settled it |
| 3 | Remove `main()`, the `if __name__` guard, and the advert in the module docstring; drop `sys` if nothing else in the file uses it. | The edited `plugin/skills/taskmd/taskmd/schema.py` |
| 4 | Run `python -m taskmd.schema` after the removal and say exactly what it now does — "removed" is a claim about behaviour and this project does not accept it from a diff. | The literal output in §3 |
| 5 | Show `link_names` exists in one place, by grep rather than by assertion. | The hit list in §3 |
| 6 | Run the suite, `check` and `index`. `tests/test_schema.py` imports this module, so the removal is not obviously invisible to it. | The literal output in §3 |

**Criterion 5 is already discharged, and by the right order.**
[T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) closed earlier in this same
session, before this task started — the check it asks for is that the overlapping half is fixed once,
and it was: T-023 changed `_display()`, which this entry point printed through, and removing the
entry point now takes that surface away rather than duplicating the fix. Recorded here because the
criterion asks for the check to have happened *before* implementing, not for a conclusion.

**What is deliberately not attempted.** Criterion 1's first clause asks for *exactly one* statement
of the command surface. There are four — `README.md`'s table, `cli.py`'s docstring, `docs/SCOPE.md`,
and `CLAUDE.md` pointing at the first — and collapsing them is outside this task's scope, which is
`schema.py`'s `main()`. The clause was already unmet on the day it was written, so the removal cannot
be judged against it; the review judges the falsifier the same criterion supplies, and the
duplication is raised as its own task rather than absorbed or ignored.

**Outputs promised**

- plugin/skills/taskmd/taskmd/schema.py
- tasks/T-030-settle-the-schema-module-s-own-entry-point.md
- tasks/README.md
- one new task file in tasks/, for the surface-statement duplication

## 3. Implement

**Decisions & assumptions**
- **The removal is the whole of `main()`, its `__main__` guard, the `Usage` block that advertised
  it, and the `sys` import it was the last user of** — 2026-08-11. Nothing else in the module
  imported `sys`; leaving it would have been a dependency on a removed feature that no test could
  see.
- **The module docstring gained what the removal takes away** — 2026-08-11. It now says the module
  has no command of its own, that `load_schema` is where a bad config is caught for callers that
  never touch the CLI, and that a `main()` used to exist and T-030 removed it. Written because
  §1 asked for it to be stated when the removal landed: the guarantee T-019's review rests on lives
  in the import path, not in the entry point, and a reader who finds the module bare should not have
  to reconstruct that.
- **A stale claim in the same docstring was corrected, and it is worth naming why** — 2026-08-11.
  It said a field the schema does not name is *"carried and **displayed** but never interpreted"*.
  [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) corrected exactly that
  sentence in `taskmd/defaults/config.md` and did not reach this second copy of it. The removal is
  what made it indefensible — `main()` was the only code that printed carried fields, which is the
  finding T-059 raised as F-5 — so correcting it is part of removing the behaviour rather than a
  separate fix. The wording now matches the config's: carried, never interpreted, shown by naming
  the field in `context_fields` or `index_columns`.
- **The surface-statement duplication was raised, not absorbed** — 2026-08-11, as
  [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md). See §4's first row.

**Outputs produced**
- plugin/skills/taskmd/taskmd/schema.py — 45 lines shorter; no `main`, no guard, no `sys`
- tasks/T-030-settle-the-schema-module-s-own-entry-point.md — this record
- tasks/T-117-decide-whether-the-command-surface-needs-one-statement.md — raised here
- tasks/README.md — regenerated

**Evidence — step 1's two sets, gathered before the edit.** Runnable entry points in the shipped
tree: `plugin/bin/taskmd` and `taskmd.cmd`, `plugin/skills/taskmd/taskmd.sh` and its `.ps1` twin,
`python -m taskmd` via `__main__.py`, and `python -m taskmd.schema` — all of which reach
`cli.main` except the last. Statements of the surface: `README.md`'s table, `cli.py`'s module
docstring, `docs/SCOPE.md`, and `CLAUDE.md` pointing at `README.md`. Neither list is in the task
description; both were produced by grep, because a criterion about "any entry point" cannot be
judged against the ones somebody remembered.

**Evidence — what the entry point does now.** Run from the package's own directory, both forms:

```
python -m taskmd.schema      exit=0, no output
python -m taskmd.schema .    exit=0, no output
```

**It still runs, and it cannot be made not to.** Any importable module can be named to `python -m`;
what has gone is everything it did. That is worth stating rather than claiming removal: the criterion
is falsified by an entry point the surface does not name, and one that produces nothing and exits 0
is not an entry point in that sense — but a future reader running it and getting exit 0 should find
this line rather than wonder whether the removal half-landed.

**Evidence — `link_names` is in one place.**

```
plugin/skills/taskmd/taskmd/cli.py:150  def link_names(schema):
plugin/skills/taskmd/taskmd/cli.py:234, 314, 850, 935   four call sites
```

One definition, four callers, no second implementation anywhere in the tree. The inline copy died
with `main()`, which is what criterion 4 asked for.

**Evidence — the suite, `index` and `check`.**

```
=== test_budget.py (exit 0) tier 1 7844 chars under by 2 (bound 7846, reference/TASK-WORKFLOW.md)
=== test_cli.py (exit 0) OK
=== test_list.py (exit 0) OK
=== test_runtime.py (exit 1) FAILED (failures=4)
=== test_schema.py (exit 0) OK
Wrote tasks/README.md - 18 active, 99 closed
OK - 117 task(s), 585 field value(s), 369 reference(s), 22 dependency edge(s), 185 declared output(s), 1 index file(s), 145 document(s), 1153 link(s), 2 template(s), 10 template field value(s), 0 vocabulary row(s)
```

`tests/test_schema.py` imports this module and is unaffected — 46 tests, all passing — which is the
positive form of §1's claim that the removal closes a command and not the API. The four failures are
the standing `Launchers` ones ([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)),
absent on the Linux runner and unchanged by this task.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Exactly one statement of what the command surface is, and it is true — falsified by any runnable entry point the documented surface does not name | **partly — the falsifier is met, the clause is not** → **[T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md)** | The falsifier: six runnable entry points in the shipped tree, five of which reach `cli.main` and are named by the surface; the sixth is this one, and it now does nothing. So no entry point escapes the documented surface. The first clause asks for *exactly one statement* and there are four — `README.md`, `cli.py`'s docstring, `docs/SCOPE.md`, `CLAUDE.md` — which was equally true on 2026-08-06 when this criterion was written. It is not something the removal could have achieved and not something this task's scope allows, so it is raised rather than ticked or quietly reworded. |
| No entry point prints an absolute path on any path, success or failure (R-20) | met, by another task | Ticked in `specify` as already met by `_display()` in `580d22b`, and kept as written. Now met twice over and for a better reason: the entry point that printed the path no longer prints anything. |
| If the entry point survives, it takes `--root PATH` like everything else | n/a — it did not survive | Kept as written, exactly as the 2026-08-06 log said it would be: a criterion written to survive either answer, recorded as inapplicable rather than deleted so the review can show which branch was taken. |
| The `link_names` derivation exists in one place | met | One definition in `cli.py`, four call sites, no second implementation in the tree — shown by grep in §3. The copy was inside `main()` and died with it, so this needed no separate edit, which is what made *remove* cheaper than *keep* on this criterion too. |
| Checked against T-023 before implementing, so the overlapping half is fixed once | met | T-023 closed earlier in the same session, before this task began. It changed `_display()`, which this entry point printed through; removing the entry point afterwards takes that surface away rather than fixing the same string twice. The order was the check: had this task gone first, T-023 would have had one fewer caller to reason about and the same wording decision to take. |

**A second stale statement was found and corrected here** rather than raised, and the distinction
matters: `schema.py`'s docstring claimed carried fields are *displayed*, which was T-065's sentence
in another home and which **this removal is what falsifies**. Correcting the documentation of a
behaviour being removed is part of removing it. Everything else this task noticed — the four
statements of the surface — is in T-117.

**Child fix tasks raised**
- [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md) — whether the command
  surface needs one home, or whether four statements addressed to four readers are legitimate

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | Plan through review in one session, under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1), re-confirmed by them for this task by name. Raised [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md); `related` gained T-065, whose sentence turned up in a second home here. Two things the removal exposed rather than caused: `main()` was the only code that printed carried fields, so a docstring still claiming they are *displayed* had to go with it; and criterion 1's first clause was unmet on the day it was written, which no amount of removing could have fixed. The criterion 5 check was discharged by ordering — T-023 closed first in the same session, so the shared string was settled once and then deleted. |
| 2026-08-06 | → specified | Q1 answered by the maintainer: remove. The criteria were written to survive either answer and none needed amending — criterion 3 ("if the entry point survives…") is now vacuous rather than wrong, and is kept as written so the review can record that it did not apply. The recommendation's own rationale was replaced by a stronger one found while agreeing it: a config replaces rather than merges, so the resolved-schema view has no content of its own. Noted for `implement`: the module stays importable and `load_schema` keeps the guarantee T-019 rests on — this removes a command, not the API a binding uses. |
| 2026-08-06 | → proposed | Raised as F-4 from the T-026 audit, clauses 1 and 3. Run before being written up: the entry point works and prints an absolute install path on the success path. Deduped against T-023, which shares the root cause but is scoped to error messages only. Typed `decision` because keep-or-remove changes what the fix is. |
