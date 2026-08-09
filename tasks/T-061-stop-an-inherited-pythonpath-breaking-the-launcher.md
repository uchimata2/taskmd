---
id: T-061
title: Stop an inherited PYTHONPATH breaking the shell launcher
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-049, T-056, T-068]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-061 — Stop an inherited PYTHONPATH breaking the shell launcher

## 1. Specify

**Outcome**
`plugin/taskmd.sh` — and `plugin/bin/taskmd`, which delegates to it — finds its own package whatever
`PYTHONPATH` the caller's environment already holds.

**Why this one**
Raised as **F-3** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Reproduced across five environments, running the same `check` command
through `bash plugin/taskmd.sh`:

```
PYTHONPATH unset                  OK - 58 task(s), ...            exit 0
PYTHONPATH = a POSIX-absolute path  OK - 58 task(s), ...          exit 0
PYTHONPATH = a drive-lettered path  No module named taskmd        exit 1
PYTHONPATH = a relative path        No module named taskmd        exit 1
```

*(The two failing lines are transcribed with their leading path elided: the real output names the
interpreter's own location, and quoting it would put an absolute local path into this record.)*

**The mechanism.** The launcher builds `PYTHONPATH="$here${PYTHONPATH:+:$PYTHONPATH}"` where `$here`
is a POSIX path and `:` is hardcoded as the separator. On Windows the separator is `;` and a POSIX
path is not a path at all, so this only ever works because the shell layer rewrites the whole
variable on its way to a native process — and that rewrite is abandoned the moment one element of the
list is relative or drive-lettered. Python then receives the raw POSIX string and reports a missing
module. `plugin/taskmd.ps1` builds the same value with `[IO.Path]::PathSeparator` and native paths
and is unaffected.

**Who pays.** Anyone whose environment already sets `PYTHONPATH` — which is to say a Python developer,
the likeliest adopter. `plugin/bin/taskmd` is the command the skill names and it `exec`s this script,
so the adopter's documented entry point inherits the whole defect. The error names their interpreter
rather than taskmd, so it does not read as a taskmd problem.

**And this repository tells them to set it.** `CLAUDE.md` and `.handoff/config.md` both explain that a
bare `python -m taskmd` needs `PYTHONPATH` — advice which, followed and then left in place, breaks the
launcher the same documents recommend.

**Why the suite is green.** `tests/test_runtime.py::Launchers::test_the_shell_launcher_produces_what_
the_module_produces` runs the launcher under whatever environment the runner happens to have, and
compares it against a direct invocation given a *different*, correct environment. Under a plain run
both pass; the assertion cannot see the case it is closest to.

**Requirements served**
R-18, R-20 (`docs/SCOPE.md`) — one implementation whose launchers carry no logic, behaving identically
across platforms.

**Scope**
- In: how `plugin/taskmd.sh` composes `PYTHONPATH`, including whether it inherits an existing value
  at all.
- In: the same question asked of `plugin/taskmd.ps1`, which is believed correct and has not been
  tested against a hostile value.
- In: a regression test that fixes the environment rather than inheriting it.
- Out: `plugin/bin/*` coverage in general, which is [T-068](T-068-cover-the-entry-point-an-adopter-runs.md).
- Out: interpreter discovery, settled in [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)
  and its children.

**Inputs**
`plugin/taskmd.sh`, `plugin/taskmd.ps1`, `plugin/bin/taskmd`, `tests/test_runtime.py` (`Launchers`),
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-3.

**Acceptance criteria**
- [ ] The launcher works with `PYTHONPATH` unset, set to a relative path, set to a drive-lettered
      path, and set to a POSIX path — all four demonstrated
- [ ] Shown failing first on at least two of those, per R-16 — the current behaviour is reproduced
      before the change
- [ ] The PowerShell launcher is put through the same four values, and the result recorded either way
- [ ] A test asserts it, with the environment **set by the test** rather than inherited, so the case
      cannot go quiet again
- [ ] Whatever the launcher does with an existing `PYTHONPATH` is stated in its own comment — the
      current comment claims a property the code does not have
- [ ] No absolute path appears in this task's record (R-23)

**Open questions**
- **Does the launcher keep inheriting `PYTHONPATH` at all?** Dropping the inheritance is one line and
  removes the whole class; it also means a caller cannot extend the path for a plugin of their own,
  which nothing today asks for. The alternative is to convert `$here` to the platform's own form
  before joining, which keeps the inheritance and costs a platform test in a file whose whole claim
  is that it contains no logic. `plan` decides, after checking whether anything in the tree relies on
  the inherited value.

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
| 2026-08-09 | → proposed | Raised as F-3 from the T-059 audit, clauses 1 and 3. Reproduced across five environments before write-up; two of the five fail. `high` because it makes the adopter's own entry point fail outright for the reader most likely to have a `PYTHONPATH` set, and because this repository's own documents tell people to set one. `s` because the fix is a line or two, and the cost is deciding which line. Not fixed where it was found (METHOD §5). |
