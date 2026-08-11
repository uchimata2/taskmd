---
id: T-132
title: Give the console the same line ending on every platform
type: fix
status: done
phase: review
parent: T-020
blocked_by: []
related: [T-002, T-020, T-022, T-049, T-064]
work_package: v0.5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-132 — Give the console the same line ending on every platform

## 1. Specify

**Outcome**
Everything taskmd prints ends its lines the same way wherever it runs, so a script that reads the
output of `list` gets the same bytes on Windows as on Linux. Today it does not: the files taskmd
writes are already identical, and only the console is not.

**Why this one**
Measured, not suspected. [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) ran
`context`, `index` and `check` on two projects from clones of one commit on Windows and on Linux, and
compared the raw bytes:

```text
generated artifacts        identical, both projects (31712 B and 762 B, same SHA-256)
all six console captures   differ, and are byte-equal after stripping CR
```

The whole difference is the line terminator, and the cause is one line: `cli.py` reconfigures
`sys.stdout` to UTF-8 without setting `newline`, so Python's text layer keeps rewriting `\n` as
`\r\n` on Windows. The project applies `newline="\n"` to every file it writes and not to what it
prints.

**What it costs.** [T-022](T-022-filtered-task-listing-for-scripts.md) built `list` as a *filtered
task listing for scripts*. T-020 captured the last row of `list --open --limit 3` on both:

```text
windows   \t   -  \r  \n
linux     \t   -  \n
```

A script splitting a row on tabs reads a final field of `-\r` on Windows and `-` on Linux. So the
command that exists to be parsed is the command that returns different bytes to the parser.

**Requirements served**
R-20 (`docs/SCOPE.md`) — identical behaviour across platforms, which its §9 puts in the definition of
done. This is the half of it that is currently false.

**Scope**
- In: the line ending of everything written to stdout and stderr by every command.
- In: a test that fails today, in the same file as
  `tests/test_cli.py::WritesTheSameBytesEverywhere` — the assertion that covered files and not the
  console is exactly why this went unmeasured until T-020.
- Out: the encoding. UTF-8 is already set and is not in question.
- Out: re-running the cross-platform comparison. T-020 did that; this task's evidence is the new test
  plus one re-measurement of the command it changes.

**Inputs**
- [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) §3 — the measurement, the
  capture method, and the Linux route.
- `plugin/skills/taskmd/taskmd/cli.py` — the `reconfigure` call.
- `tests/test_cli.py::WritesTheSameBytesEverywhere`.

**Acceptance criteria**
- [ ] A test asserts the console line ending and **fails on the unfixed code**, with its failure
      recorded before the fix
- [ ] Every command prints `\n` line endings on Windows, shown by re-capturing the bytes rather than
      by reading the code
- [ ] The Windows console still renders correctly — a fix that produces right bytes and unreadable
      output is not a fix
- [ ] The suite passes on both platforms
- [ ] `check` clean on this repository

**Open questions**
- None. Raised by T-020's review with the cause and the cost already measured, so there is nothing
  left for someone else to decide.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the test **first**, as a subprocess capture of raw bytes, and record it failing on the unfixed code | A failing test, its output quoted in §3 |
| 2 | Set `newline="\n"` when `sys.stdout` is reconfigured, and give `sys.stderr` the same treatment | `plugin/skills/taskmd/taskmd/cli.py` |
| 3 | Re-run the test, then re-capture the bytes of `list` from outside the suite | §3 — criterion 2, from two independent directions |
| 4 | Look at the console with the fix in place, on Windows | §3 — criterion 3 |
| 5 | Run the suite on Windows and on the Linux clone | §3 — criterion 4 |
| 6 | `index` and `check` | §3 — criterion 5 |

**Shape decisions.**

**D1 — The test spawns a subprocess, and this is the whole reason the defect survived.**
`tests/test_cli.py`'s `run()` helper swaps `sys.stdout` for an `io.StringIO`, which has no
`reconfigure` — so the line under repair **never executes** in the existing suite, and an in-process
assertion would pass on the unfixed code and prove nothing. Criterion 1 asks for a test that fails
today, and only a real process has a real `TextIOWrapper`. *Rejected: asserting through `run()`* — it
is every other test's helper, and reaching for it here would have produced the vacuous pass this
criterion exists to prevent.

**D2 — Fix the stream, not the call sites.** One `reconfigure` covers every command, and every
command written later. Normalising at each `print` would leave the next one free to regress, and
there is no way to test for a `print` nobody has written yet. *Rejected: writing through
`sys.stdout.buffer`* — it would mean re-encoding by hand at every site, which is the same fault with
more code.

**D3 — `sys.stderr` gets the same treatment, though only one line goes there today** (`cli.py`'s
"N problem(s)" warning). A stream configured differently from its twin is a defect waiting for its
second caller, and the criterion says *stdout and stderr*.

**Planned outputs**
- `tests/test_cli.py` — one test in `WritesTheSameBytesEverywhere`, the class whose gap this is
- `plugin/skills/taskmd/taskmd/cli.py` — the `reconfigure` call

## 3. Implement

### Step 1 — the test, failing, before anything was changed

```text
FAIL: test_what_the_commands_print_carries_no_carriage_returns
AssertionError: b'\r' unexpectedly found in b'OK - 1 task(s), 5 field value(s), ... 0 vocabulary
row(s)\r\nScope  every document read; no git here, so .gitignore was not consulted\r\n...' :
stdout of 'taskmd check'
Ran 3 tests in 0.071s
FAILED (failures=1)
```

Recorded before the repair, because afterwards there is nothing left to show. It fails on the first
of the five commands it walks, and it fails on `stdout` — the assertion that matters.

**D1 in practice.** Written through the suite's own `run()` helper the same assertion **passes** on
the unfixed code, because `run()` substitutes an `io.StringIO` for `sys.stdout` and `StringIO` has no
`reconfigure` — the guarded line never runs, so no translation happens and no `\r` appears. That is
not a near miss; it is the reason a project that already had a class called
`WritesTheSameBytesEverywhere` shipped four releases with this defect.

### Step 2 — the change

One loop in `cli.py`, over both streams:

```python
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace", newline="\n")
```

### Steps 3 and 5 — the suite, and a gate that caught the comment

The first full run failed, and not on this change's behaviour:

```text
FAIL: test_no_file_in_the_plugin_cites_something_it_does_not_ship
AssertionError: [] != ["plugin/skills/taskmd/taskmd/cli.py:1013 cites 'R-20'"]
```

The comment explaining the fix cited the requirement it serves.
[T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)'s guard is right: `R-20` lives in
`docs/SCOPE.md`, which the plugin does not ship, so an adopter reading that comment would meet a
citation they cannot follow. The comment now states the promise instead of naming it. Worth recording
because the guard was doing its job on a file whose *code* was correct — the defect was in the prose
next to it.

Then, both platforms, one process per module:

```text
                Windows                        Linux
test_cli        Ran 101  OK                    Ran 101  OK
test_list       Ran  37  OK                    Ran  37  OK
test_schema     Ran  53  OK                    Ran  53  OK
test_budget     Ran   5  OK                    Ran   5  OK
test_runtime    Ran  27  OK (skipped=3)        Ran  27  OK (skipped=2)
```

The skip counts differ by the launcher case each platform cannot exercise, which is what the
`shell:` line in those skips says.

### Steps 3 and 4 — measured from outside the suite

**The bytes.** T-020's comparison re-run on the fixed commit `f63e375`, Windows clone against Linux
clone:

```text
1-repo-context.txt     IDENTICAL  (1011 bytes)
2-repo-index.txt       IDENTICAL  (  46 bytes)
3-repo-check.txt       IDENTICAL  ( 364 bytes)
7-repo-list.txt        IDENTICAL  ( 251 bytes)
```

The same measurement that produced the finding now produces identity, on the same two machines. The
last row of `list` ends `... \t - \n` on both, where Windows read `\t - \r \n` before.

**The console.** Bytes being right is half of criterion 3; a Windows console that stair-steps bare
line feeds would make the tool unreadable while passing every test above. Measured in a real console
rather than argued from documentation — a hidden `powershell.exe` was started, which allocates its
own screen buffer, and the cursor was read after each command and the buffer scraped back:

```text
console attached  : True
taskmd list       : rows advanced 4, cursor column after 0
taskmd check      : rows advanced 4, cursor column after 0
screen row 0      : [OK - 132 task(s), 660 field value(s), 427 reference(s), 23 dependency edge(s), ...
screen row 1      : [160 document(s), 1333 link(s), 2 template(s), 10 template field value(s), 0 voca...
screen row 2      : [Scope  48 document(s) not read: a clone would not receive them]
screen row 3      : [structure and references only - it cannot tell you whether a spec or an outcome ...
```

Cursor column 0 after each command, and every row starts at column 0 — no staircase. Rows 0 and 1 are
one printed line wrapped at the buffer width, which is wrapping and not the failure mode being looked
for.

**Decisions & assumptions**

- **The test walks five commands including an unknown one**, so the assertion covers `stderr` and the
  usage path as well as the three commands T-020 measured. A stream fixed for the commands someone
  remembered is fixed until the next one. — 2026-08-11
- **`errors="replace"` is unchanged.** It is not this task's subject and changing it while the file is
  open would be the silent widening METHOD §3.3 forbids. — 2026-08-11
- **The Windows console evidence is a cursor position and a buffer scrape, not a screenshot.** It is
  the same claim measured mechanically, and it is reproducible by re-running the script. — 2026-08-11

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — the `reconfigure` loop
- `tests/test_cli.py` — `WritesTheSameBytesEverywhere.test_what_the_commands_print_carries_no_carriage_returns`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A test asserts the console line ending and **fails on the unfixed code**, with its failure recorded before the fix | met | §3 step 1 quotes the failure. **D1** is the substance of this criterion: the same assertion written through the suite's own helper passes on the unfixed code, because `run()` swaps in a `StringIO` that has no `reconfigure` — so only a spawned process can fail here. |
| Every command prints `\n` line endings on Windows, shown by re-capturing the bytes rather than by reading the code | met | Two independent directions. The test walks five commands and both streams; T-020's clone-against-clone comparison re-run at `f63e375` reports all four captures **IDENTICAL**, where every one of them differed before. |
| The Windows console still renders correctly | met | Measured in an allocated console: cursor column 0 after each command, and the scraped screen buffer shows every row starting at column 0. |
| The suite passes on both platforms | met | 223 tests each, Windows and Linux, one process per module. The first Windows run **failed** — on T-064's shipped-citation guard, because the new comment cited `R-20`, a requirement the plugin does not ship. Recorded rather than quietly corrected. |
| `check` clean on this repository | met | §3, with `index` run first. |

**Child fix tasks raised**
- none. The one thing this run turned up — a comment citing an unshipped document — is a defect in
  this task's own change, caught by an existing guard and repaired here, not a separate finding.

**Verdict.** All five criteria met. The claim T-020 found half-false is now true on both measured
platforms, and macOS is still what it was: unverified, and said so.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All five criteria met. The measurement that found the defect now reports **IDENTICAL** on all four captures, Windows clone against Linux clone at `f63e375`, and the suite is 223 green on both. Two things are worth carrying out of this record. **D1**: the same assertion written through the suite's own `run()` helper *passes* on the unfixed code, because `run()` substitutes a `StringIO` that has no `reconfigure` — so the line under repair never executed in-process, which is how a project with a class named `WritesTheSameBytesEverywhere` shipped four releases with this. And the first full Windows run **failed on [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)'s guard**, because the comment explaining the fix cited `R-20`, which lives in a document the plugin does not ship: the code was right and the prose beside it was not. No child raised — that was this change's own defect, caught and repaired here. |
| 2026-08-11 | → in_progress | Six steps taken in order, and step 1 was written to fail before anything was changed. Console rendering was measured rather than argued: a hidden `powershell.exe` allocates a real screen buffer, and the cursor read 0 after each command with every scraped row starting at column 0 — bytes being right is only half of criterion 3, since a console that stair-steps bare line feeds would pass every other check here while making the tool unreadable. The test walks five commands including an unknown one, so `stderr` and the usage path are covered too. |
| 2026-08-11 | → planned | Six steps, and one decision does the work. **D1** spawns a subprocess because the suite's `run()` helper swaps `sys.stdout` for an `io.StringIO`, which has no `reconfigure` — an assertion through the helper would pass on unfixed code, which is exactly the vacuous pass criterion 1 exists to prevent. **D2** fixes the stream rather than the call sites, since there is no way to test for a `print` nobody has written yet. **D3** treats `sys.stderr` the same as `sys.stdout` though one line goes there today. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised by [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md)'s review, which measured the difference rather than inferring it and was scoped to measure only. `medium` and `s`: the change is one argument, but the claim it repairs is in the goal and in the definition of done, and the command it affects is the one built to be machine-read. `v0.5` by the maintainer's release rule of 2026-08-10 — a minor correction goes in the near release. Two things are already settled and are written here so `specify` does not re-derive them: the cause is `cli.py`'s `reconfigure` call omitting `newline`, and the cost is a trailing `\r` on the last field of every `list` row on Windows. |
