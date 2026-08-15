---
id: T-145
title: Stop --help answering for a command that does not exist
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-029, T-113, T-120, T-144]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-145 — Stop --help answering for a command that does not exist

## 1. Specify

**Outcome**
A command name the tool does not have is rejected whether or not `--help` was typed beside it, so the
exit code says the same thing about the same mistake.

**Why this one**
Found on 2026-08-15 while reproducing the htmldeck adopter report's row `O-T5`. The report is about
which usage line is printed; this is a different fault in the same three lines of `main`, and it is
not in the report. Run:

```
taskmd wat               -> exit 2, usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd wat --help        -> exit 0, usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd frobnicate --help -> exit 0, same line
```

The two outputs are identical and the exit codes are not. `main` collects `--help` while parsing,
answers it before the command is looked at, and returns 0 — so the flag suppresses the
unknown-command rejection and a script sees success.

**Why this is T-029's standard rather than a new opinion.**
[T-029](T-029-reject-unknown-arguments-on-every-command.md) exists because three commands used to
drop an argument they did not understand and report success, and its own comment states the principle
plainly: a tool that is believed must not report success over something it never looked at. Here the
thing never looked at is the command name. T-029's evidence block records `taskmd wat -> exit 2,
usage line (already correct)`; adding `--help` makes it exit 0, and nothing in that task's record
chose it.

**It is a small fault with an asymmetric cost.** Nobody is misled by the printed line, which is
correct. What is misled is anything reading the exit code — which is the caller T-029 was written
for, and the same class as the `index` case that made T-029 `critical`: mistyped invocation, exit 0,
no signal.

**The one external caller we could ask is not affected.** The exposure was flagged to the reporting
project when it was found, and they checked on 2026-08-15: their query wrapper consumes `-h` and
`--help` only as its **first** argument and never passes either through, so `wrapper wat --help`
falls to the unknown-command path and exits 2. No exit-code handling there reads a status from a
`--help` call. That is a negative result, recorded because it was asked for and would otherwise be
lost — it bounds the known damage at zero and changes nothing about the fault, which is a promise to
callers nobody has surveyed.

**Requirements served**
R-17 (`docs/SCOPE.md`); §1 *Invisibility*, in the reading T-029 established — the tool must not be
silent about a mistake.

**Scope**
- In: the order in which `main` answers `--help` and validates the command name, and the exit code
  each path returns.
- In: what `taskmd --help` alone does, which is correct today and must stay so — asking a tool what it
  does is not misuse.
- Out: which usage line is printed for a command that exists. That is
  [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) and this task
  must not pre-empt it.
- Out: `list`'s own argument handling, which validates itself
  ([T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md),
  [T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md)).

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `main` — the `asked_for_help` branch and the `COMMANDS` gate
  below it.
- [T-029](T-029-reject-unknown-arguments-on-every-command.md) §3, the before-and-after evidence blocks
  and decision 3.
- `tests/test_cli.py`, `test_asking_what_the_tool_does_is_not_misuse`, which covers all four forms and
  is the test any change here has to keep honest.

**Acceptance criteria**
- [ ] Shown **failing** first: the three commands above, run and recorded before anything is changed
- [ ] An unknown command exits 2 whether or not `--help` is present, and the message is unchanged
- [ ] `taskmd --help` and `-h` with no command still exit 0 with the top-level line
- [ ] A known command with `--help` behaves exactly as it does today, so this task decides nothing
      T-144 owns
- [ ] The new case is covered by a test derived from `cli.COMMANDS` rather than a written name, on
      T-029's precedent
- [ ] The suite and `check` are green

**Open questions**
- none. The behaviour T-029 chose is recorded and this is not it; what the right answer is for a
  *known* command is the only genuine question here and it belongs to T-144.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | (no change) | **The branch this task has to change now has two outcomes**, since [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) closed: `main`'s help branch answers with the top-level line, or with `list`'s help when the command is `list`. §1's reproduction is unaffected and was re-run — `taskmd wat --help` still exits 0 on the top-level line — so nothing here is superseded. What changes is the repair: moving the branch after the command check has to keep `list --help` working, which is one more thing for its plan to say than "the order of two checks". Recorded because it happened underneath this task while it was open. |
| 2026-08-15 | (no change) | **Negative result from the reporting project, recorded in §1.** We asked them to check their wrappers for this and they did: `-h`/`--help` is consumed as the first argument only and never passed through, so their `wat --help` exits 2 and nothing there reads a status from a `--help` call. Kept because a negative result that was asked for dies with the session otherwise, and because it is evidence about exposure and not about the fault — the ranking below is unchanged. |
| 2026-08-15 | → proposed | Found while reproducing the htmldeck adopter report's row `O-T5` and **not reported by it** — the row is about which usage line prints, and this is the exit code beside it. Reproduced before write-up: `taskmd wat` exits 2 and `taskmd wat --help` exits 0 on identical output. Raised separately from T-144 on METHOD §5 and on T-029's own precedent, which raised T-113 rather than fixing what its probe turned up: T-144 may end with the ruling unchanged, and this is wrong either way. `medium` and `xs` because the printed line is already correct and the repair is the order of two checks. |
