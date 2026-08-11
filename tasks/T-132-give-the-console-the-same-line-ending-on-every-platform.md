---
id: T-132
title: Give the console the same line ending on every platform
type: fix
status: proposed
phase: specify
parent: T-020
blocked_by: []
related: [T-002, T-020, T-022, T-049]
work_package: v0.5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
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

**Decisions & assumptions**
-

**Outputs produced**
-

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised by [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md)'s review, which measured the difference rather than inferring it and was scoped to measure only. `medium` and `s`: the change is one argument, but the claim it repairs is in the goal and in the definition of done, and the command it affects is the one built to be machine-read. `v0.5` by the maintainer's release rule of 2026-08-10 — a minor correction goes in the near release. Two things are already settled and are written here so `specify` does not re-derive them: the cause is `cli.py`'s `reconfigure` call omitting `newline`, and the cost is a trailing `\r` on the last field of every `list` row on Windows. |
