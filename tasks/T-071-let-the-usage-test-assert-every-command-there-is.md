---
id: T-071
title: Let the usage test assert every command there is
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-022, T-055]
work_package: M1
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-071 — Let the usage test assert every command there is

## 1. Specify

**Outcome**
The test that checks taskmd's usage line asserts every command taskmd has, derived from the tool
rather than from a list written in the test.

**Why this one**
Raised as **F-11** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 1. `tests/test_cli.py`:

```python
def test_no_command_explains_the_three(self):
    code, out = run()
    self.assertEqual(code, 2)
    for command in ("context", "index", "check"):
        self.assertIn(command, out)
```

Both the name and the tuple predate `list`, added by
[T-022](T-022-filtered-task-listing-for-scripts.md) on 2026-08-05. A regression that dropped `list`
from the usage line would pass, and the test's name would tell the next reader the surface is three
commands wide.

**The sibling test already shows the shape.**
`test_every_usage_line_names_the_command_the_skill_names` was written for
[T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) and deliberately reads the
expected name **out of `SKILL.md`** rather than hardcoding it, with the reasoning recorded in its own
docstring: *"two copies that must agree, instead of three that can drift."* The same treatment here
reads the command set out of `cli.COMMANDS`, which is the dict the usage line is built from — so the
assertion becomes "the usage line names everything the tool dispatches" and cannot go stale when a
fifth command arrives or a fourth is removed.

**Why `low`.** Nothing is broken. The cost is a test that has quietly stopped covering what its name
claims, in a suite whose value is that a regression is caught rather than argued about.

**Requirements served**
R-16 (`docs/SCOPE.md`) — a check is worth what you believe it would catch; R-1, since the command set
has one home and the test keeps a second.

**Scope**
- In: `test_no_command_explains_the_three` — its name and its assertion.
- In: whether any other test in the suite carries a written copy of the command set. One sweep, done
  once, rather than this recurring.
- Out: what the usage line says. That is
  [T-029](T-029-reject-unknown-arguments-on-every-command.md)'s, which also owns whether `--help` is
  answered at all.
- Out: the command name the line prints, settled in T-055 and pinned by the sibling test.

**Inputs**
`tests/test_cli.py` (`Usage`), `plugin/taskmd/cli.py` (`COMMANDS`, `main`),
[T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) for the pattern,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-11.

**Acceptance criteria**
- [ ] The test asserts every command in `cli.COMMANDS`, derived rather than listed
- [ ] Shown failing first, per R-16 — removing a command from the usage line turns it red
- [ ] The test's name describes what it now checks
- [ ] No other test carries a written copy of the command set, or the ones that do are recorded with
      the reason

**Open questions**
- None.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the set from `cli.COMMANDS`, and give the test a name that describes what it now checks | `tests/test_cli.py` |
| 2 | Sweep the suite for any other written copy of the command set | The sweep result, either way |
| 3 | Show it failing — drop one command from the **usage line** while leaving `COMMANDS` intact, which is the regression the old test could not see | The transcript |
| 4 | In the same run, keep the **retired** assertion alongside the new one, so the vacuous pass is recorded rather than erased by the repair | Both results, side by side |

**Why step 4 is a step.** A test that passes for the wrong reason leaves no trace once it is fixed:
after the change, "the old one would have passed" is a claim rather than an observation. Running
both against the same broken build is the only moment it can be shown.

## 3. Implement

**Decisions & assumptions**

- **D1 — derived from `cli.COMMANDS`, with a guard against an empty set** — 2026-08-09. Same
  treatment the sibling test already gives the command *name*, which reads it out of `SKILL.md`:
  two things that must agree rather than three that can drift. `assertTrue(cli.COMMANDS, ...)` is
  there because a derived loop over an empty collection passes without asserting anything, which is
  the failure mode being removed rather than relocated.

- **D2 — the other written copies stay, and here is why** — 2026-08-09. The sweep found three, all
  in tests that run each command in turn:

  ```
  tests/test_cli.py:411      (("check",), ("index",), ("context", "T-001"))
  tests/test_runtime.py:282  ("check", "list", "context")
  tests/test_runtime.py:300  (("check",), ("index",), ("list",), ("context", "T-001"))
  ```

  None is a claim about *what the command set is*. Each is a list of invocations with per-command
  arguments — `context` needs an id, the others do not — so deriving them would need a second
  mapping from command to arguments, which is a written copy of something else. Recorded per
  criterion 4 rather than silently left.

### Steps 3-4 — the vacuous pass and the failure, in one run

`list` removed from the usage line only; `COMMANDS` untouched. The retired assertion was restored
beside the new one for this run:

```
test_PROBE_the_retired_assertion                       PASSED
test_no_command_explains_every_command_there_is        FAILED
  AssertionError: 'list' not found in
  'usage: taskmd {check,context,index} [args] [--root PATH]'
  : usage line omits 'list'
```

The old assertion passing is the finding, not a footnote: it is what the suite would have done for
as long as the regression lived. Both files were restored afterwards.

**Outputs produced**
- `tests/test_cli.py` - `test_no_command_explains_every_command_there_is`, replacing
  `test_no_command_explains_the_three`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The test asserts every command in `cli.COMMANDS`, derived rather than listed | met | Derived, plus a guard that fails if the set is ever empty - a derived loop over nothing passes, which would have moved the defect rather than removed it |
| Shown failing first, per R-16 - removing a command from the usage line turns it red | met | Step 3, with `COMMANDS` left intact so the probe is a usage-line regression and not a missing command |
| The test's name describes what it now checks | met | *the three* was the tell; the name is now `..._every_command_there_is` and has nothing to go stale |
| No other test carries a written copy of the command set, or the ones that do are recorded with the reason | met | Three found, all recorded in D2. None asserts what the set *is*; each pairs a command with its arguments, and deriving those would write down a different fact |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met. The part worth keeping is step 4: the **retired assertion was run beside the new one** against the same broken build, so the vacuous pass is an observation rather than a claim — `test_PROBE_the_retired_assertion` PASSED while the derived one FAILED on a usage line missing `list`. After a repair there is no way to show that. Three other written command lists were found and deliberately kept: none asserts what the set *is*, each pairs a command with its arguments, and deriving those would write down a different fact. |
| 2026-08-09 | → in_progress | Plan adds a guard against an empty `cli.COMMANDS`, because a derived loop over nothing passes without asserting anything — which would relocate the defect rather than remove it. |
| 2026-08-09 | → specified | Criteria stand as raised; no open question. |
| 2026-08-09 | → proposed | Raised as F-11 from the T-059 audit, clause 1. `low`/`xs` — nothing is broken, and the fix is the pattern the neighbouring T-055 test already uses. Recorded rather than absorbed because a test whose name overstates its coverage is the kind of thing a reader trusts without re-reading. |
