---
id: T-029
title: Reject unknown arguments on every command
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-002, T-022]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-029 — Reject unknown arguments on every command

## 1. Specify

**Outcome**
An argument taskmd does not understand is an error naming what *is* accepted, on all four commands,
before anything is printed or written — instead of being discarded in silence by three of them.

**Why this one**
Raised as **F-3** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clause 3. `cmd_check`, `cmd_index` and `cmd_context` each take an `args` parameter and never read it
past the first element. Observed:

```
python -m taskmd check nonsense
OK - 26 task(s), vocabulary valid, references resolve, no broken links
exit=0

python -m taskmd index nonsense --wat
Wrote tasks/README.md - 12 active, 14 closed
exit=0

python -m taskmd context T-026 extra junk
(normal output for T-026)
```

The `index` case is the sharp one: a mistyped invocation **performed a write** and reported success,
so the user's evidence that their flag did something is the same output they would get if it had.

**`list` already does this correctly**, and does it well — `parse_filters` returns a message rather
than printing, every rejection happens before a line reaches stdout, and an unknown value names the
project's own vocabulary. That was built deliberately in
[T-022](T-022-filtered-task-listing-for-scripts.md). So this is one command's behaviour that three
commands did not get, not a design nobody has settled.

**Why it is clause 3 and not tidiness.** R-17 puts configuration errors at setup rather than
mid-run, on the reasoning that a validator which is believed must not report success over something
it never examined — the same reasoning [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md)
acted on. An ignored argument is that failure at the command layer.

**Requirements served**
R-17, R-18 (`docs/SCOPE.md`); §1 *Invisibility* — the tool should not need the user to notice.

**Scope**
- In: argument handling for `check`, `index` and `context`, and the no-command and unknown-command
  paths in `main`.
- In: whether `--help` / `-h` is answered at all. `python -m taskmd --help` currently prints the
  usage line and exits **2**, so the conventional way to ask what a tool does is reported as misuse —
  which matters more here than usual, since the intended caller is an agent probing the surface.
- Out: adding any new flag or command. `docs/SCOPE.md` non-goal 11 stands; this is about rejecting
  what is not there, not accepting more.
- Out: `list`, which already behaves correctly and is the model to follow.

**Inputs**
`taskmd/cli.py` (`main`, `cmd_check`, `cmd_index`, `cmd_context`, and `parse_filters` as the
pattern), `docs/SCOPE.md` R-17, [T-022](T-022-filtered-task-listing-for-scripts.md) §3 *Rejections
arrive before output*, [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-3.

**Acceptance criteria**
- [ ] Each of the four commands rejects an argument it does not understand, naming what it does
      accept, and exits non-zero
- [ ] **Nothing is printed and nothing is written before the rejection** — asserted for `index`
      specifically, whose current failure mode is a silent successful write
- [ ] Shown failing first on the three commands, per R-16 — a check that has only ever passed proves
      nothing, and this one is being added to code that currently accepts everything
- [ ] `list`'s existing behaviour and messages are unchanged, verified by the T-022 tests still
      passing untouched
- [ ] The rejection message is the same bytes on every platform (R-20) and contains no path

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: the top-level line only.** Their reason goes
  past the wording: the goal is a lightweight tool, and if it is difficult enough to use that
  detailed help is needed, that is a reason to stop the project rather than to write the help.
  Per-command usage would be treating a symptom. It is also `docs/SCOPE.md` §2 principle 3, since it
  restates what the top-level line and the config already state. *Rejected: per-command help.*
  Discoverability for someone who mistyped one command is real, and it is bought with a second
  surface that drifts the first time a flag changes.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce all three, plus the `--help` exit code, before changing anything | evidence in §3 |
| 2 | One table of what each command accepts after its name, beside `COMMANDS` | `ARGUMENTS` in `cli.py` |
| 3 | One usage line, top-level and per-command, derived from that table | `usage_line` in `cli.py` |
| 4 | Validate in `main` **before discovery and before the config is read**, so nothing can be printed or written first | `cli.py` |
| 5 | Answer `--help` / `-h` with the top-level line and exit 0 | `cli.py` |
| 6 | Delete `cmd_context`'s own arity guard, now that `main` owns the shape | `cli.py` |
| 7 | Cover the criteria, deriving the command set from `COMMANDS` | `tests/test_cli.py` |

## 3. Implement

**Reproduced first, per R-16.** Before any change, at `50fc36d`:

```
taskmd check nonsense              -> exit 0, OK - 112 task(s), ...
taskmd index nonsense --wat        -> exit 0, Wrote tasks/README.md - 26 active, 86 closed
taskmd context T-029 extra junk    -> exit 0, normal output
taskmd --help                      -> exit 2, usage: taskmd {check,context,index,list} ...
taskmd wat                         -> exit 2, usage line  (already correct)
```

The `index` line is the one the audit called sharp: the mistyped invocation **performed the write**
and reported success.

**Decisions & assumptions**
- **The check lives in `main`, not in each command** — 2026-08-10. It has to run before discovery
  and before the config is read, or the criterion "nothing printed and nothing written before the
  rejection" is decided by whichever error happens to fire first. One place also means adding a
  command cannot forget it: the omission this task fixes was three commands not getting one
  command's behaviour. Rejected: a guard per `cmd_*`, which is the shape that produced the defect.
- **`list` is not in the table** — 2026-08-10. Its flags are the project's own vocabulary, read from
  the config at run time, so a table here could not name the values its rejection names. It keeps
  validating its own arguments, which is what it already did well.
- **`cmd_context`'s own usage line is gone** — 2026-08-10. It named the shape in a printed string,
  which after step 2 would be a second home for "context takes an id" — and the one that would
  drift, since nothing tested it against the table. Its exit code for a missing id therefore moves
  from **1 to 2**, which is the more accurate of the two: misuse, not a problem found in the tasks.
  No test asserted the old code.
- **`--help` is answered and exits 0** — 2026-08-10, on the maintainer's ruling in §1. Answering it
  with the top-level line costs nothing and is not the per-command surface that was rejected; the
  exit code is the part that mattered, since the intended caller is an agent probing the surface and
  was being told the tool had failed.
- **The reasoning is cited without its requirement id** — 2026-08-10. The first draft of the comment
  cited `R-17`, and `test_no_file_in_the_plugin_cites_something_it_does_not_ship` failed: `docs/`
  is not inside the plugin boundary (T-053, T-064), so shipped code may carry the reasoning but not
  the pointer. Caught by the suite, not by review.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `ARGUMENTS`, `usage_line`, the `main` gate, `--help`,
  and `cmd_context`'s guard removed.
- `tests/test_cli.py` — four tests, including one derived from `cli.COMMANDS` rather than written.

**Evidence — after**

```
taskmd check nonsense              -> exit 2, usage: taskmd check [--root PATH]
taskmd index nonsense --wat        -> exit 2, usage: taskmd index [--root PATH]
taskmd context T-029 extra junk    -> exit 2, usage: taskmd context <id> [--root PATH]
taskmd context                     -> exit 2, usage: taskmd context <id> [--root PATH]
taskmd --help / -h / check --help  -> exit 0, usage: taskmd {check,context,index,list} ...
taskmd list --wat x                -> exit 2, unknown filter: --wat. This project accepts: ...
```

Suite **179 passed** (175 before), `check` clean on 113 tasks. `tests/test_list.py` is untouched and
its 25 tests still pass, which is the fourth criterion.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each of the four rejects what it does not understand, names what it accepts, exits non-zero | met | `test_every_command_rejects_an_argument_it_does_not_understand`, with the set derived from `cli.COMMANDS` so a fifth command cannot slip past it. |
| Nothing printed or written before the rejection, asserted for `index` | met | `test_index_writes_nothing_before_rejecting` asserts the index file does not exist at all afterwards, then that the same call without the junk creates it — so the assertion cannot pass on a project that could not have written one. |
| Shown failing first on the three commands | met | Recorded verbatim in §3 above, at `50fc36d`, before the change. |
| `list`'s behaviour and messages unchanged, T-022 tests passing untouched | met | `tests/test_list.py` has no diff; 25 tests pass. |
| The message is the same bytes everywhere and contains no path | met | `test_a_rejection_names_no_path` asserts neither separator appears, for every command. |

**Beyond the written criteria**
- `--help` was in scope but had no criterion. `test_asking_what_the_tool_does_is_not_misuse` covers
  all four forms and compares against `cli.usage_line()` rather than a written string.

**Child fix tasks raised**
- [T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md) — `list` reports an
  unknown flag as *needing a value* when it is given none, checking the argument's shape before its
  name. Found by this task's derived probe and not fixed here (METHOD §5). It does not weaken §1's
  claim that `list` is the model: the refusal is early and names the vocabulary; one branch of it is
  ordered wrongly.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `v0.2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1), which covers each task in that set end to end and nothing outside it. Raised one child, T-113. |
| 2026-08-07 | → specified | Answered: top-level usage only. The maintainer's reason is recorded because it is stronger than the one the question offered — not that per-command help is a second surface, but that needing it would be evidence against the tool's premise. Kept as a standing test rather than a preference about wording. |
| 2026-08-06 | → proposed | Raised as F-3 from the T-026 audit, clause 3. Reproduced on all three commands before being written up; the `index` case writes the index and exits 0 on a mistyped invocation. Not fixed where it was found (METHOD §5). |
