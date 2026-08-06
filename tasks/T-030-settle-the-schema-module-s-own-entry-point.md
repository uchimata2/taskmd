---
id: T-030
title: Settle the schema module's own entry point
type: decision
status: proposed
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

**The output is the harder half.** On the success path it prints the config's `source`, which for a
project with no `.taskmd/config.md` is the absolute path to wherever taskmd is installed:

```
schema   <absolute install path>/taskmd/defaults/config.md
```

R-20 requires byte-identical output across platforms, and `_check_tasks_dir`'s own docstring in the
same file names this as the reason it prints the configured *value* rather than the resolved path —
so the module states the rule and then breaks it eleven lines from the bottom.

**Dedupe — this is not [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md).**
T-023 shares the root cause (`schema.source`) but its scope is explicitly *"how the shipped default
config is named in **error messages**"*, and its out-list keeps to the prefix. What is left here is
the success path and the existence of the entry point itself. If T-023's fix is to change `source`
at the point it is built, this finding's output half is resolved with it and this task should say so
rather than redo it — that check is part of the work.

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
- [ ] No entry point prints an absolute path on **any** path, success or failure (R-20); shown on a
      project with no `.taskmd/config.md`, which is the case that produces it
- [ ] If the entry point survives, it takes `--root PATH` like everything else — two conventions for
      the same argument is the drift this project exists to remove
- [ ] The `link_names` derivation exists in one place
- [ ] Checked against T-023 before implementing, so the overlapping half is fixed once

**Open questions**
- Keep it or remove it? *Recommendation: remove.* Everything it prints is available from `context`
  and `list --json`, which are supported, tested and documented, so keeping it means maintaining a
  second renderer of the same derivation for debugging that the supported commands already serve.
  The argument for keeping it is that it is the only view of the **resolved schema** as opposed to
  the tasks — if that is worth having, it is worth having as part of the surface rather than beside
  it. — maintainer; this decides the outcome, so it blocks `specify`.

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
| 2026-08-06 | → proposed | Raised as F-4 from the T-026 audit, clauses 1 and 3. Run before being written up: the entry point works and prints an absolute install path on the success path. Deduped against T-023, which shares the root cause but is scoped to error messages only. Typed `decision` because keep-or-remove changes what the fix is. |
