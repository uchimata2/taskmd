---
id: T-069
title: Skip a nested project at any depth, not below the first
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-011]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-069 — Skip a nested project at any depth, not below the first

## 1. Specify

**Outcome**
`check` skips a nested taskmd project wherever it sits, including directly inside the project root —
so a host project never reports another project's defects as its own.

**Why this one**
Raised as **F-7** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Shown, not asserted — an outer project with one task, and a complete
taskmd project one directory below it holding a deliberately dead link:

```
taskmd check --root <the outer project>
BROKEN LINK   inner/tasks/T-001-b.md -> ./nope.md

1 problem(s) over 1 task(s)
exit=1
```

One task, one problem, and the problem belongs to a different project.

**The mechanism.** `markdown_files()` guards its nested-project test with `base != root`, so while
walking the top level of the tree it never asks whether a subdirectory is a project. One level down
it does, which is why this repository has never seen it: every fixture project sits at
`tests/fixtures/<name>`, two levels down, and is correctly skipped.

**A documented claim is broader than the behaviour.** `tests/fixtures/README.md` closes with
*"`check` skips a nested project — a directory holding its own `.taskmd/` or its own tasks folder —
so the host repository does not report the defects these exist to hold. A taskmd project inside a
taskmd project is validated on its own."* True at depth two and greater; false at depth one.

**Who pays.** An adopter whose repository holds a sub-project at the top level — a monorepo with a
`frontend/` or a `docs-site/` that tracks its own tasks — gets that project's problems reported
against theirs, with no way to tell which is which. `load_tasks` is unaffected (it walks only
`tasks_dir`), so the damage is confined to the link sweep, which is also the only check that reads
the whole tree.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`) — the validator must be believable, and a report naming another
project's file is the kind of noise that trains people to ignore it.

**Scope**
- In: the `base != root` guard in `plugin/taskmd/cli.py::markdown_files`, and whether it has a reason
  nobody wrote down.
- In: a fixture exercising the depth-one case, since none of the ten existing `broken-*` projects
  can — they are all at depth two by construction.
- In: the sentence in `tests/fixtures/README.md`, which states the rule without its exception.
- Out: `discovery.is_project` and the nearest-wins resolution rule, both settled in
  [T-011](T-011-runtime-discovery-and-project-hook-commands.md) and correct.
- Out: whether nested projects should be validated *by* the host, which is settled the other way and
  not reopened.

**Inputs**
`plugin/taskmd/cli.py` (`markdown_files`, `is_nested_project`), `plugin/taskmd/discovery.py`
(`is_project`), `tests/fixtures/README.md`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-7.

**Acceptance criteria**
- [ ] A project holding another project **directly** inside its root does not report that project's
      problems
- [ ] Shown failing first on a fixture, per R-16 — the current behaviour is reproduced before the
      change
- [ ] The ten existing `broken-*` fixtures each still report exactly one class, and this repository's
      own `check` is unchanged
- [ ] The guard's removal or replacement is explained — if `base != root` was protecting something,
      that thing still works
- [ ] `tests/fixtures/README.md`'s claim is true of the code afterwards, checked against the sentence

**Open questions**
- **Can the root itself be caught by its own test?** The obvious fix is to drop the `base != root`
  guard, and the obvious worry is that the walk then declines to enter the project it was asked
  about. It cannot — the guard is applied to *subdirectories* of `base`, never to `root` itself — but
  the guard exists, so `plan` should establish whether it was written against a case that is no longer
  reachable rather than deleting it on the strength of a reading.

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
| 2026-08-09 | → proposed | Raised as F-7 from the T-059 audit, clauses 1 and 3. Reproduced before write-up on a scratch project outside the repository. `medium`/`s`: invisible here because every fixture is two levels down, real for a monorepo adopter, and it makes a documented claim broader than the behaviour. Confined to the link sweep — `load_tasks` walks only `tasks_dir` and is unaffected. |
