---
id: T-145
title: Stop --help answering for a command that does not exist
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-029, T-113, T-120, T-144]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-16
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
- [x] Shown **failing** first: the three commands above, run and recorded before anything is changed
- [x] An unknown command exits 2 whether or not `--help` is present, and the message is unchanged
- [x] `taskmd --help` and `-h` with no command still exit 0 with the top-level line
- [x] A known command with `--help` behaves exactly as it does today, so this task decides nothing
      T-144 owns
- [x] The new case is covered by a test derived from `cli.COMMANDS` rather than a written name, on
      T-029's precedent
- [x] The suite and `check` are green

**Open questions**
- none. The behaviour T-029 chose is recorded and this is not it; what the right answer is for a
  *known* command is the only genuine question here and it belongs to T-144.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run the whole invocation matrix before touching anything — the three from §1, plus every command with `--help`, so what must **not** move is recorded beside what must | The before-table below |
| 2 | Write the test first and prove it on the case it exists to catch, by running it against the unfixed `main` | A recorded failure, not a clean pass |
| 3 | Guard the help branch on the command name instead of reordering the two checks, so `list --help` keeps T-144's answer | `plugin/skills/taskmd/taskmd/cli.py`, `main` |
| 4 | Re-run the matrix and read the actual exit codes, per this repository's verifying rule | The after-table below |
| 5 | Run the suite and `check` | Their output below |

Step 1 is first because the 2026-08-15 log row says the branch now has two outcomes: the repair has
to keep `list --help` intact, and a before-table is the only thing that can show it did.

## 3. Implement

**Shown failing first**, 2026-08-16, before any edit — the fault as §1 describes it, and the
surrounding cases it must not disturb:

```
taskmd wat                  -> exit 2 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd wat --help           -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd frobnicate --help    -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd --help               -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd -h                   -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd list --help          -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd check --help         -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
```

**The test failed on the case it is for**, run against the unfixed `main`:

```
FAIL: test_help_does_not_answer_for_a_command_that_does_not_exist
AssertionError: 0 != 2 : --help suppressed the rejection:
'usage: taskmd {check,context,index,list} [args] [--root PATH]\n'
```

**The change is one condition on the branch, not a reordering.** `main` now reads:

```python
if asked_for_help and (not rest or rest[0] in COMMANDS):
```

**After**, 2026-08-16, same matrix and four more commands:

```
taskmd wat                  -> exit 2 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd wat --help           -> exit 2 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd wat -h               -> exit 2 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd frobnicate --help    -> exit 2 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd --help               -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd -h                   -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd list --help          -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd check --help         -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd context --help       -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
taskmd index --help         -> exit 0 | usage: taskmd {check,context,index,list} [args] [--root PATH]
```

```
264 passed, 3 skipped, 6 subtests passed
OK - 160 task(s), ... 2353 front-matter value(s)          exit=0
```

**Decisions & assumptions**

- **The branch is guarded, not moved below the command gate** — 2026-08-16. *Rejected:* moving the
  whole `asked_for_help` block after the `COMMANDS` check, which is the repair §1 implies. It breaks
  `taskmd --help` with no command at all: `rest` is empty, so the gate rejects it before help is ever
  reached, and recovering that needs a second help branch above the gate. One condition keeps one
  branch, and keeps `list_help`'s dispatch exactly where T-144 put it.
- **The unknown-command probe is built from `cli.COMMANDS`, not written** — 2026-08-16, on T-071's
  precedent already in this file. A literal `wat` is a name that could be adopted as a real command
  later, at which point the test would quietly assert the opposite of what it says. `"not" +
  "".join(sorted(cli.COMMANDS))` cannot collide, and the test asserts that it does not.
- **The known side is swept too, and asserted as a prefix** — 2026-08-16. Testing only the unknown
  case would leave the fix's blast radius unmeasured. Every command in `COMMANDS` is run with both
  flags; what all four share is that the top-level line comes **first**, which is exactly T-144's
  superset decision, so `list` needs no exception written by name. *Rejected:* asserting equality
  for the three and special-casing `list`, which reintroduces the written name the criterion excludes.
- **`test_asking_what_the_tool_does_is_not_misuse` is left untouched** — 2026-08-16. §1 names it as
  the test any change here must keep honest, and it passed unaltered; rewriting it to derive its own
  set would have removed the independent witness this change most needed.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — the guard on `main`'s help branch, and the comment recording
  why it is there.
- `tests/test_cli.py` — `test_help_does_not_answer_for_a_command_that_does_not_exist`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Shown **failing** first | met | Both ways, and before any edit: the seven-case matrix above, and the new test's recorded `AssertionError: 0 != 2`. The second is the one that matters — a matrix can be re-run, a failing test proves the guard would catch a regression. |
| An unknown command exits 2 with or without `--help`, message unchanged | met | Read off the after-matrix: `wat`, `wat --help`, `wat -h` and `frobnicate --help` all exit 2 on the same line. The test additionally asserts the message is byte-identical to the no-flag case, so a future change cannot keep the code and drift the text. |
| `taskmd --help` and `-h` with no command still exit 0 with the top-level line | met | Both rows unchanged in the after-matrix, and `test_asking_what_the_tool_does_is_not_misuse` covers them unaltered. |
| A known command with `--help` behaves exactly as today | met | All four commands, both flags, exit 0 — the four `--help` rows unchanged and `context`/`index` added to the matrix. `list --help` still prints its own answer; nothing T-144 owns was decided here. |
| Covered by a test derived from `cli.COMMANDS` | met | Both directions derive from it: the known side iterates the vocabulary, and the unknown probe is built from it and asserted absent. No command name is written down. |
| The suite and `check` are green | met | `264 passed, 3 skipped, 6 subtests passed`; `check` exit 0. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | All six criteria met, and the task was the size it claimed. **The repair §1 implied does not work**: moving the help branch below the command gate breaks `taskmd --help` with no command, so the branch is guarded instead of reordered — recorded as a decision because the next reader will reach for the reorder. Two things came out larger than the fix. The test sweeps **both** directions from `cli.COMMANDS`, because a test for the unknown case alone would have left the four known ones unmeasured by the change that moved them; and the known side asserts the usage line as a **prefix**, which is T-144's superset ruling doing the work a hand-written exception for `list` would otherwise have done. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): full lifecycle, renewed and widened**, given 2026-08-16 as the subject of a handoff — *work all 4 from the list, full lifecycle*. The list is the four unblocked `fix` tasks named that day: [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md), [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md), [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md). It covers those four and **nothing else** — not the five `decision` tasks beside them on the same list, and not anything these four raise. **The 2026-08-15 grant below was never spent**, so this renews it rather than adding a second one. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-15 | (no change) | **Authorisation (METHOD §3.1): the maintainer asked for this task to be taken through its full lifecycle**, given on 2026-08-15 as the subject of a handoff. It covers T-145 and reaches no other task. Written here rather than left in the handoff, because an authorisation kept anywhere but the task's own record is one a later session can miss or stretch — which is the correction T-144 needed on the same day, for the same reason. Nothing has been started under it: the task is still at `proposed`, and this row records the permission, not any phase of the work. |
| 2026-08-15 | (no change) | **The branch this task has to change now has two outcomes**, since [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) closed: `main`'s help branch answers with the top-level line, or with `list`'s help when the command is `list`. §1's reproduction is unaffected and was re-run — `taskmd wat --help` still exits 0 on the top-level line — so nothing here is superseded. What changes is the repair: moving the branch after the command check has to keep `list --help` working, which is one more thing for its plan to say than "the order of two checks". Recorded because it happened underneath this task while it was open. |
| 2026-08-15 | (no change) | **Negative result from the reporting project, recorded in §1.** We asked them to check their wrappers for this and they did: `-h`/`--help` is consumed as the first argument only and never passed through, so their `wat --help` exits 2 and nothing there reads a status from a `--help` call. Kept because a negative result that was asked for dies with the session otherwise, and because it is evidence about exposure and not about the fault — the ranking below is unchanged. |
| 2026-08-15 | → proposed | Found while reproducing the htmldeck adopter report's row `O-T5` and **not reported by it** — the row is about which usage line prints, and this is the exit code beside it. Reproduced before write-up: `taskmd wat` exits 2 and `taskmd wat --help` exits 0 on identical output. Raised separately from T-144 on METHOD §5 and on T-029's own precedent, which raised T-113 rather than fixing what its probe turned up: T-144 may end with the ruling unchanged, and this is wrong either way. `medium` and `xs` because the printed line is already correct and the repair is the order of two checks. |
