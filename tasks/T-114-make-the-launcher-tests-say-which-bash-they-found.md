---
id: T-114
title: Make the launcher tests say which bash they found
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-091]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-11
deliverables: [tests/test_runtime.py]
---

# T-114 — Make the launcher tests say which bash they found

## 1. Specify

**Outcome**
`tests/test_runtime.py` gives the same answer on a machine that has more than one `bash`, or says
plainly which one it used and why the result is not a verdict on the launcher. Today it silently
picks whichever comes first on `PATH` and reports a launcher defect when the answer is a shell.

**Why this one**
Found on 2026-08-10 while verifying [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md).
Three of the 27 fail like this:

```
AssertionError: 0 != 127 : bin/taskmd exited 127: b'/bin/bash: C:WorkAgentPluginsbintaskmd:
No such file or directory'
```

The path in that message is a Windows one with its separators eaten, and the reason is that
`shutil.which("bash")` resolved to **WSL** rather than to Git Bash in that session. WSL cannot
execute a script named by a Windows path, so it exits 127 — a fact about which shell was found,
reported as a fact about the launcher. Every word of the message points at the wrong thing.

**What makes it worth a task rather than a shrug.** The previous session recorded 185 passing over
the same commit; this one gets 181 with nothing changed, because `PATH` differs between sessions on
this machine (T-054's truncated shell snapshot is the same hazard from the other side). So the
suite's headline number is not reproducible, and the project's central habit — *claims are verified
by running the thing* — is exactly the habit a test that fails for environmental reasons teaches a
session to stop trusting. The cost is paid once per session, by whoever has to work out that three
red tests mean nothing.

**Scope**
- In: how `tests/test_runtime.py` selects a `bash`, and what it reports when the one it finds cannot
  run a script named the way the test names it.
- In: whether such a case is a skip with a stated reason or a pass against a differently-formed
  argument — a skip that nobody reads is how a platform silently stops being covered.
- Out: making the launchers themselves work under WSL. The launcher is fine; nothing about the
  shipped code is implicated, and a change there would be fixing the wrong end.
- Out: the fourth failure in the same run, which is a real cross-platform difference in `check` and
  belongs to [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md).

  **Since 2026-08-11 there are four of this kind, not three.** T-112 has closed, so its failure is
  gone and a fourth shell failure has taken its place in the count —
  `test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has`, which reaches `bash` through
  `available_launchers` rather than through `how_to_run`. The line above is left as written because
  it was true of the run it describes; the count *now* is four, and all four are in scope. This is
  the hazard the task itself names: the number is not a property of the tree, so a later reader who
  counts four and expects three should suspect the count, not the fix.

**Inputs**
- `tests/test_runtime.py`, the `Launchers` class — `how_to_run`, and the two tests that call it.
- [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md) §3 for the run that found it.

**Acceptance criteria**
- [ ] With WSL first on `PATH`, the module reports no failure attributable to the shell — shown by
      running it that way, not by reading the selection code
- [ ] The run states which `bash` it used, so a reader can tell a skip from a pass
- [ ] With Git Bash first on `PATH`, the same tests still run and still cover what they cover today
      — falsified by a fix that makes them skip everywhere and prove nothing

**Open questions**
- None.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what this machine actually offers, since the fix is worthless if it is written against a guess. | Recorded in §3: how many `bash` are on `PATH`, which one wins, and what it is |
| 2 | Add a probe that asks a candidate shell to **run** a script named the way these tests name one, and returns the first that can — over every `bash` on `PATH`, not the first. | A helper in `tests/test_runtime.py`, with the candidate scan separate from the probe |
| 3 | Make the module say which shell it settled on, and when none worked, name every candidate and why each was rejected. | One printed line per run, in `test_budget.py`'s idiom |
| 4 | Route all four call sites through it — `how_to_run`, `available_launchers`, the shell-launcher test's literal `bash`, and its skip guard. | The four sites, none of them calling `shutil.which("bash")` |
| 5 | Run the module with the WSL shell first on `PATH` — criterion 1, which is about a run and not about the code. | Recorded output |
| 6 | Run it again with Git Bash first on `PATH`, and show the same tests **ran** rather than skipped — criterion 3. | Recorded output, with the count that separates a pass from a skip |
| 7 | `check`, `index`, and the rest of the suite. | Recorded output |

Steps 5 and 6 are separate runs and both are required: a fix that turns four failures into four skips
passes the first and fails the third, and only running both can tell them apart. Step 1 is first
because the whole defect is that the code assumed an environment.

**Shape decisions.**

**D1 — Probe by running, never by inspecting the path.** A shell is usable here if it can execute a
script named by an absolute path in this platform's own form; that is a behaviour, and the only way
to know it is to try. *Rejected: recognise WSL by where its executable lives* — the failing shell is
reached through a per-user launcher stub, so the test would encode one machine's layout, and it would
still be wrong on the next machine that puts a different shell first. It would also put a local
absolute path into a published file, which this repository does not permit.

**D2 — The probe script is written and thrown away, not committed as a fixture.** It exists to be
named by a path, so its content is one `echo`; a fixture would imply there is something to maintain.

**D3 — A skip is only honest if it says what it skipped and why.** Criterion 2 asks the run to state
which `bash` it used, and the same line has to serve the no-usable-shell case by naming every
candidate and the reason each was rejected. Otherwise the fix converts a loud wrong answer into a
quiet absence of one, which is what the scope warns against. *Rejected: raise on no usable shell* —
that is the current behaviour with a better message, and it still reports a fact about the machine as
a fact about the launcher.

**Planned outputs**
- tests/test_runtime.py

## 3. Implement

### Step 1 — one `bash`, and it is the wrong one

This machine has **exactly one** `bash` on `PATH`, a per-user WindowsApps launcher stub, and it
reports itself as `GNU bash, version 5.3.9(1)-release (x86_64-pc-linux-gnu)` — a Linux build, so
`shutil.which` was never choosing badly between two shells. It was taking the only one there is.
Git Bash exists on disk, under Program Files, and is simply not on this session's `PATH`.

**That sharpens the fix rather than shrinking it.** A selection rule that preferred Git Bash by
location would have found nothing to prefer here and changed no outcome; what is needed is a shell
that *can be rejected*, leaving a stated skip rather than a failure. The scan over every `PATH`
entry stays, because the machine that has two is the one the earlier reading was written from.

### Step 2–4 — probed, reported, and routed through one place

`shell_candidates()` walks `PATH` for `bash` and then for `sh`, de-duplicating case-insensitively;
`usable_bash()` writes a two-line probe script into a temporary directory, names it by an absolute
path in this platform's form, and takes the first candidate that runs it and echoes the token back.
`sh` is scanned for the same reason `bash` is: it was `how_to_run`'s fallback, and an unprobed
fallback is the same hole under a different name.

Four call sites now go through it — `how_to_run`, `available_launchers`, the shell-launcher test's
guard, and that test's literal `"bash"` argv, which was invoking a shell nobody had checked.

**One message was still lying after the fix worked**, and it is worth recording because it is the
same defect one layer down: the entry-point test skipped with `cannot be run on this platform`,
when the platform is fine and it is the shell that is missing. `how_to_run` returns `None` for two
different facts, so the caller now says *nothing here can run it* and points at the `shell:` line
for the shell case, instead of blaming the platform.

### Step 5 — with the WSL shell first on `PATH`

```text
shell: none of 1 candidate(s) can run a script named the way these tests name one, so the launcher
checks are SKIPPED and prove nothing here:
  <per-user WindowsApps>\bash.EXE: exited 127, said b'/bin/bash: C:UsersTemptmp…probe.s'
Ran 27 tests in 5.296s
OK (skipped=3)
```

**Four failures became zero, and three named skips**, listed by `-v` as the `taskmd.sh` and
`bin/taskmd` sub-cases of the entry-point test and the whole of the shell-launcher test. The two
sub-case skips are per-`subTest`, so `taskmd.cmd` and `taskmd.ps1` were still asserted in the same
run — the entry points this machine *can* run did not lose their coverage to a shell it cannot.

*(The candidate's path is abbreviated above; the run prints it in full. The eaten separators in the
127 message are the shell's own mangling and are what the earlier reading mistook for a launcher
defect.)*

### Step 6 — with Git Bash first on `PATH`

```text
shell: C:\Program Files\Git\bin\bash.EXE - ran a probe script named the way these tests name one
Ran 27 tests in 5.815s
OK
```

**No skips at all**, which is the criterion that a fix cannot satisfy by skipping everywhere: the
same three checks that were skipped above ran here and passed. Taken together the two runs also
settle the question the failures were being read as — the launchers were never broken, and the same
tree answers `OK` under both shells.

**The probe has been seen to reject as well as accept**, which is what stops it being a check nobody
has tested: step 5 is it saying no, with the candidate and the reason, and step 6 is it saying yes.

### Step 7 — the rest

```text
OK - 123 task(s), 615 field value(s), 391 reference(s), 22 dependency edge(s), 204 declared output(s),
     1 index file(s), 151 document(s), 1235 link(s), 2 template(s), 10 template field value(s),
     0 vocabulary row(s)
```

`test_cli` 92 OK, `test_list` 35 OK, `test_schema` 53 OK, `test_budget` 5 OK.

**A stale index cost one run and is worth recording**, because it arrived disguised: the first
execution of the finished fix still failed one test, and the message was
`STALE INDEX tasks/README.md no longer matches the tasks it was generated from` — this task's own
front-matter edits, not the launcher. It is exactly the trap the project already knows about, and it
reads as a regression in whatever you last touched.

**Decisions & assumptions**
- **A shell is usable if it runs a script named this way, and it must prove it** — 2026-08-11, D1;
  recognising WSL by where it lives would encode one machine's layout and put a local absolute path
  into a published file.
- **`sh` is probed too** — 2026-08-11: it was the existing fallback, and leaving it unprobed would
  have reproduced the defect under a different name.
- **The no-shell answer is a printed line and a skip, not an exception** — 2026-08-11, D3.
- **Assumption: one machine, two `PATH` orders, is enough evidence.** Both branches of the new code
  were executed and the CI runner is `ubuntu-latest`, where the first candidate is an ordinary
  `bash`. If it is ever wrong, it is wrong in the direction of skipping, which now says so out loud.

**Outputs produced**
- [`tests/test_runtime.py`](../tests/test_runtime.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| With WSL first on `PATH`, the module reports no failure attributable to the shell — shown by running it that way, not by reading the selection code | met | Step 5: `Ran 27 tests … OK (skipped=3)`, where the same `PATH` produced four failures before. Judged from a run, and the run is quoted |
| The run states which `bash` it used, so a reader can tell a skip from a pass | met | One `shell:` line per run, and it carries the harder case too — when nothing is usable it names each candidate, its exit code and what it said. Step 6 shows the accepting form |
| With Git Bash first on `PATH`, the same tests still run and still cover what they cover today — falsified by a fix that makes them skip everywhere and prove nothing | met | Step 6: `Ran 27 tests … OK` with **no skips**, so the three checks skipped in step 5 ran here. The falsifier the criterion names would have shown `skipped=3` in both runs |

**What changed beyond the criteria, and stayed inside the task.** The entry-point test's skip
message said `cannot be run on this platform` for a missing shell — the same misattribution the task
exists to remove, one layer down and inside the file being edited. Corrected here rather than raised,
because it is this task's own output: leaving it would have satisfied criterion 2's letter with a
line that still blames the wrong thing.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met from two runs, no child raised. **The premise turned out to be half wrong and the fix survived it**: this machine has exactly one `bash` on `PATH`, a WSL stub, so nothing was choosing badly between two shells — it was taking the only one there is, and a rule that preferred Git Bash by location would have found nothing to prefer. What was needed was a shell that can be *rejected*, and the probe is that. **Four failures became zero and three named skips with WSL first; no skips at all with Git Bash first**, which is the pair the third criterion asks for, since a fix that skipped everywhere would satisfy the first two and prove nothing. Two things worth carrying: the probe has been seen to say **no** as well as yes, so it is not a check that has only ever succeeded; and the first run of the finished fix still failed, on a `STALE INDEX` caused by this task's own front-matter edits — the failure that most reliably reads as a regression in whatever was last touched. The launchers were never broken, which the two runs now establish rather than assert. |
| 2026-08-11 | → planned | **Authorisation, recorded here and not inherited from a note (METHOD §3.1).** The maintainer gave *work every open `v0.2` task through its full lifecycle — specify, plan, implement, review, fix, commit and push, one task at a time* on 2026-08-10, re-confirmed on 2026-08-11 and widened the same day to *multiple tasks until you need to stop*; it covers this task end to end and nothing outside the open `v0.2` set. `specify` needed no new agreement — the outcome, the boundary and three criteria were already written and there were no open questions — but the scope gained a **dated correction**: T-112 has closed, so what used to be the fourth, unrelated failure is gone and a fourth *shell* failure has taken its place. The original sentence is left standing because it was true of the run it describes; the task's own point is that this count is not a property of the tree. Plan is seven steps, and the two that carry it are **5 and 6, which are two runs rather than one**: a fix that converts four failures into four skips satisfies criterion 1 and violates criterion 3, and nothing but running it both ways can tell those apart. **D1** probes a candidate shell by making it run a script rather than by recognising where it lives — the failing shell here is reached through a per-user launcher stub, so a location test would encode one machine's layout and would also put a local absolute path into a published file. |
| 2026-08-10 | → proposed | Raised from a run rather than from reading, while verifying T-091: four of `test_runtime.py`'s 27 failed, and establishing that none of them was T-091's took a stash, a re-run and a probe under both shells. Three turned out to be this one. The `bash` a session finds is not a property of the tree, and the suite currently reports it as one. |
