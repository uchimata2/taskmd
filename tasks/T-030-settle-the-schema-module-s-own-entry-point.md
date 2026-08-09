---
id: T-030
title: Settle the schema module's own entry point
type: decision
status: specified
phase: specify
parent: T-026
blocked_by: []
related: [T-020, T-023]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-06
updated: 2026-08-06
deliverables: []
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

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-06 | → specified | Q1 answered by the maintainer: remove. The criteria were written to survive either answer and none needed amending — criterion 3 ("if the entry point survives…") is now vacuous rather than wrong, and is kept as written so the review can record that it did not apply. The recommendation's own rationale was replaced by a stronger one found while agreeing it: a config replaces rather than merges, so the resolved-schema view has no content of its own. Noted for `implement`: the module stays importable and `load_schema` keeps the guarantee T-019 rests on — this removes a command, not the API a binding uses. |
| 2026-08-06 | → proposed | Raised as F-4 from the T-026 audit, clauses 1 and 3. Run before being written up: the entry point works and prints an absolute install path on the success path. Deduped against T-023, which shares the root cause but is scoped to error messages only. Typed `decision` because keep-or-remove changes what the fix is. |
