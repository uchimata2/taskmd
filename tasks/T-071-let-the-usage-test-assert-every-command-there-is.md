---
id: T-071
title: Let the usage test assert every command there is
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-022, T-055]
work_package: none
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
| 2026-08-09 | → proposed | Raised as F-11 from the T-059 audit, clause 1. `low`/`xs` — nothing is broken, and the fix is the pattern the neighbouring T-055 test already uses. Recorded rather than absorbed because a test whose name overstates its coverage is the kind of thing a reader trusts without re-reading. |
