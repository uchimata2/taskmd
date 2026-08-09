---
id: T-068
title: Cover the entry point an adopter runs
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-054, T-061]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-068 — Cover the entry point an adopter runs

## 1. Specify

**Outcome**
`plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` are exercised by the suite, so deleting, renaming or
breaking either one turns the suite red instead of leaving it green.

**Why this one**
Raised as **F-10** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 3. `plugin/bin/` is the whole of the adoption path:
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) raised its absence as
`critical` — *"the adoption path not working at all"* — and
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) built it. It is what
`SKILL.md` names and what the harness puts on `PATH`.

What the suite covers today:

| Test | Reaches |
| :--- | :--- |
| `Launchers::test_both_launchers_exist_at_the_root_where_a_clone_will_look` | `taskmd.sh`, `taskmd.ps1` |
| `Launchers::test_neither_launcher_names_a_command_a_flag_or_a_field` | `taskmd.sh`, `taskmd.ps1` |
| `Launchers::test_the_shell_launcher_produces_what_the_module_produces` | `taskmd.sh` |
| `Launchers::test_every_posix_shell_script_is_recorded_executable` | `bin/taskmd` — its **mode bit** only |

Nothing runs either `bin/` file. Their existence, their delegation, and whether they produce the same
output as the module are all unasserted. T-054 verified them by hand, once.

**The gap is not hypothetical: it already hid a defect.**
[T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) is a live failure that reaches
`bin/taskmd` through its delegation to `taskmd.sh`, and no test saw it. A test of the entry point
under a fixed environment would have.

**Why `medium` and not `high`.** Nothing is broken by the absence itself — the files work. What is
missing is the thing that keeps them working, and the cost lands on whoever next moves or renames
something under `plugin/`, which after two restructures in one week is not a remote prospect.

**Requirements served**
R-16 (`docs/SCOPE.md`) — a mechanism only ever watched succeeding proves that it can run, not that a
project can rely on it; R-18, R-20.

**Scope**
- In: tests for `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` — that they exist, that they delegate
  rather than duplicate, and that each produces what the module produces.
- In: the environment the tests run them under, which must be **set** rather than inherited — the
  reason the existing launcher test could not see T-061.
- In: whether the two `Launchers` assertions that enumerate `taskmd.sh`/`taskmd.ps1` should derive
  their subject from the tree rather than from a written pair, so a third entry point is covered the
  day it is added.
- Out: fixing the `PYTHONPATH` defect, which is T-061's. This task makes it visible; that one makes
  it stop.
- Out: whether `bin/` is the right mechanism, settled in T-054.

**Inputs**
`plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`, `plugin/taskmd.sh`, `plugin/taskmd.ps1`,
`tests/test_runtime.py` (`Launchers`),
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-10.

**Acceptance criteria**
- [ ] Both `bin/` entry points are run by the suite and their output compared against the module's
- [ ] Shown failing first, per R-16 — renaming or emptying one of them turns the suite red, and the
      failure names the file
- [ ] The tests set the environment they run under, so an ambient variable cannot change the result
- [ ] A test skips honestly where the platform cannot run it, rather than passing vacuously — a
      `.cmd` on a POSIX machine is the case, and a skip that reads as a pass is worse than no test
- [ ] The subject of the launcher assertions is derived from the tree, or it is recorded why a
      written pair is correct

**Open questions**
- **Does `bin/taskmd.cmd` get a real run, or only a structural check?** It needs a Windows host, and
  the project already accepts a platform gap it states rather than hides — `docs/SCOPE.md` R-20 and
  [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) do exactly this for macOS.
  Running it where possible and stating the gap where not is the likely answer; `plan` confirms, and
  criterion 4 is what stops the skip becoming a silent pass.

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
| 2026-08-09 | → proposed | Raised as F-10 from the T-059 audit, clause 3. Established by reading what the four `Launchers` tests actually assert: only the mode bit reaches `bin/`. `medium`/`s`. The evidence that the gap is real rather than tidy-minded is T-061 — a live launcher defect that reaches `bin/taskmd` by delegation and that the suite could not see, because the one test near it inherits its environment instead of setting it. |
