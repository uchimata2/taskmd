---
id: T-057
title: Let the hook tests name an interpreter that exists on the platform
type: fix
status: done
phase: review
parent: T-049
blocked_by: []
related: [T-049, T-011]
work_package: v0.1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: [tests/test_runtime.py]
---

# T-057 — Let the hook tests name an interpreter that exists on the platform

## 1. Specify

**Outcome**
Someone who clones this repository on Linux and runs the tests sees the suite pass, so a real
failure would stand out instead of being lost among four that are about the test's own assumptions.

**Why this one**
Found by [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) — the first time the
suite had ever been run on a platform other than Windows — and raised rather than fixed there,
because T-049 §1 says a defect the run turns up is a finding it raises and not one it repairs.

Four tests in `tests/test_runtime.py::RunsTheProjectsHook` fail on a stock Ubuntu clone. They
declare their fixture project's hook as `after_write: python hooks/after-write.py`, and **Ubuntu has
no `python`** — only `python3`. Windows has `python` through the launcher, so the assumption was
invisible where it was written.

**The tool is not at fault, and the evidence for that is the failure message itself:**

```text
CONFIG ERROR  .taskmd/config.md: after_write starts with 'python', which is not on PATH and is not
a path in this project. Name an executable that is installed, or a file the project ships.
```

That is taskmd doing exactly what [T-011](T-011-runtime-discovery-and-project-hook-commands.md) built
it to do — refusing a hook it cannot run, and saying why in the project's own terms. The tests are
what carry the platform assumption, and `sys.executable` is the interpreter actually running them.

**Requirements served**
R-20 (`docs/SCOPE.md`) — a clone running on Linux — at the layer that tells a contributor whether it
did. Also `CLAUDE.md` *Cross-platform*, and *Verifying*: a suite that cannot pass on a platform
cannot be used to check anything there.

**Scope**
- In: how the hook fixtures name an interpreter, in `tests/test_runtime.py`.
- In: whether any other test hard-codes a program name that is not guaranteed to exist.
- Out: the hook mechanism itself. It behaved correctly, and its diagnostic is quoted above.
- Out: anything about `python` versus `python3` in the launchers — settled, and covered by
  `test_neither_launcher_names_a_command_a_flag_or_a_field` plus the launchers' own comments.
- Out: running the suite on a third platform — [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md).

**Inputs**
- `tests/test_runtime.py` — the five `after_write="python hooks/after-write.py"` call sites, four of
  which fail.
- [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) §3 step 8 — the run, the counts
  and the message.
- [T-011](T-011-runtime-discovery-and-project-hook-commands.md) §3 — what the hook mechanism
  promises, so the fix does not weaken the thing being tested.

**Acceptance criteria**
- [ ] `tests/test_runtime.py` passes on a Linux clone, shown by its own output there
- [ ] It still passes on Windows — the change must not trade one platform for the other
- [ ] The tests still exercise a hook that **really runs**, rather than being made to pass by
      declaring a hook that is never invoked
- [ ] Any other hard-coded program name in the suite is either shown to exist on both platforms or
      changed — answered by looking, not by assuming this was the only one

**Open questions**
- **Does `sys.executable` weaken what these tests prove?** They exist to show a hook is run, its
  output shown, and its failure propagated — none of which is about *which* program the hook is. If
  that holds, the substitution is free. Confirm it at `specify` against T-011 §3 rather than
  assuming it.

  **Answered 2026-08-09: it does not weaken them, and it also cannot be used.** Two separate
  findings, and the second is why this task is not a one-word edit.

  *It would not weaken them.* The four tests assert that the hook runs after the write, that its
  output is shown, that a non-zero exit fails the writing command, and that the working directory is
  the project root. `cli.run_after_write` is indifferent to which program it launches, so none of
  those claims is about Python. The one test that *is* about language —
  `test_a_hook_written_in_another_language_runs` — already picks the platform's own shell through
  `shutil.which`, and it passed on Linux.

  *But `sys.executable` cannot be written into a config.* The resolver puts the declared line
  through `shlex.split`, which is POSIX-mode and **eats the backslashes of a Windows path** — the
  interpreter's path comes out the other side as one run-together token. And a program containing a
  separator is deliberately resolved as *a file inside the project*, which an interpreter is not.
  So the value has to be a **bare name**, resolved by `shutil.which`, which is the same route a real
  project's hook takes.

- **A fifth call site passes today, and passing is the bug.**
  `test_a_command_that_writes_nothing_does_not_run_the_hook` declares the same hook and asserts the
  hook's output is *absent*. On Linux the config is rejected before any command runs, so the output
  is absent for a reason that has nothing to do with what the test is about. It is a vacuous pass,
  which is worse than the four failures because nothing draws attention to it — and it is why
  criterion 3 is written the way it is.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Enumerate every program name the suite hands to a shell, a config or a subprocess, and say which are already guarded | A table in §3 — criterion 4 answered by looking rather than by assuming the five known sites are all of them |
| 2 | On Linux, before any change, record both halves of the current state: the four failures **and** the fifth test passing vacuously | §3 — the *before*, and the only chance to catch the vacuous pass in the act |
| 3 | Give the fixtures an interpreter name that resolves on both platforms | the helper and the five call sites in `tests/test_runtime.py` |
| 4 | Re-run on Linux — all five pass, and the fifth is shown to pass **for the right reason** now | §3 |
| 5 | Re-run on Windows, and `check` on this repository | §3 |

Step 2 is before step 3 for the usual reason, with a twist worth stating: the four failures would
still be visible afterwards from the git history, but **the vacuous pass would not**. Once the fixture
names a real interpreter, that test passes either way and no later reader could tell it had ever been
hollow. If it is not recorded here it is lost.

**Shape decisions.**

**D1 — The fixtures name a bare interpreter, chosen at runtime, not `sys.executable` and not a
literal.** A bare name is what `shutil.which` resolves, which is the route a real project's hook
takes, so the test exercises the resolver the same way a user does. The name tried first is the
basename of the interpreter running the tests, so the hook is that same Python; `python3` and
`python` follow, because an interpreter can be launched from a directory that is not on `PATH`.
*Rejected: `sys.executable`* — unusable, per §1. *Rejected: a hard-coded `python3`* — it trades the
Windows failure for a Linux one, which criterion 2 exists to forbid. *Rejected: `python3` on POSIX
and `python` on Windows* — a platform branch encoding an assumption about each, where probing
answers it.

**D2 — If no interpreter resolves under any of those names, the tests skip rather than fail.** They
would be reporting on their environment rather than on taskmd. The suite already does this for
`bash` and for `git`. *Rejected: failing* — it would make a machine without a `PATH`-visible Python
look like a defect in the hook mechanism, which is the exact confusion this task exists to remove.

**D3 — The five call sites share one module-level constant.** The command string is one fact; five
copies of it is what let this drift unnoticed in the first place. *Rejected: a helper called five
times* — same thing, more ceremony.

**Planned outputs**
- `tests/test_runtime.py` — the interpreter helper and the five fixture declarations

## 3. Implement

### Step 1 — every program name the suite hands to a shell, and which were already guarded

| Name | Where | Guarded? |
| :--- | :--- | :--- |
| `python` ×5 | the hook fixtures | **no** — the defect |
| `bash` | `non_python_hook` | yes — `shutil.which`, falling back to a `.cmd` hook |
| `cmd` | `non_python_hook`'s fallback | yes — only reached when `bash` is absent |
| `bash` | the shell-launcher comparison | yes — `skipTest` when absent |
| `git` | the mode-bit guard from T-056 | yes — skips on a non-zero return |
| `sys.executable` | a `subprocess` argv list | yes — a list, so nothing is parsed by a shell |
| `definitely-not-a-program` | the missing-hook test | deliberate; it is the thing being tested |

**Criterion 4 answered by looking: the five were the only unguarded names.** Every other place had
already been written to probe or to skip — including `non_python_hook`, whose docstring says exactly
why ("the honest test is one that picks the platform's own shell rather than one that skips where
the shell it assumed is absent"). The rule was known and stated in this very file; the hook fixtures
simply predate it being applied to them.

### Step 2 — the *before*, including the pass that would otherwise have vanished

On Linux, on the tree as it stood:

```text
Ran 7 tests in 0.416s
FAILED (failures=4)
```

And the fifth, `test_a_command_that_writes_nothing_does_not_run_the_hook`, caught in the act of
passing for the wrong reason:

```text
exit code                                : 2
what a user sees                         : CONFIG ERROR  .taskmd/config.md: after_write starts
                                           with 'python', which is not on PATH and is n…
assertNotIn('hook ran', out) is satisfied: True
```

The test claims that a command which writes nothing does not fire the hook. What it actually
observed was a project whose config was rejected outright, so no command ran at all. **This is the
only moment that observation could be made** — once the fixture names a real interpreter the test
passes either way, and no later reader could tell it had ever been hollow.

### Step 3 — the change

`python_on_path()` picks a **bare name**: the running interpreter's basename first, then `python3`,
then `python`, each checked with `shutil.which`. `PYTHON_HOOK` is the one command string the five
call sites now read, and `RunsTheProjectsHook.setUp` skips the class if nothing resolves.

The helper's docstring records *why* it is not `sys.executable`, because that is the question a
later reader will have: `shlex.split` is POSIX-mode and eats the backslashes of a Windows path, and
a program containing a separator is deliberately resolved as a file inside the project. Both are
properties of the resolver rather than accidents, so a future reader should not "simplify" this back.

### Steps 4 and 5 — both platforms

What the fixtures resolve to on Linux:

```text
PYTHON      = python3
PYTHON_HOOK = python3 hooks/after-write.py
```

The whole suite there, where four tests failed an hour earlier:

```text
test_cli.py          Ran 31 tests  OK
test_list.py         Ran 18 tests  OK
test_runtime.py      Ran 23 tests  OK
test_schema.py       Ran 44 tests  OK
```

116, the same count as Windows, all passing. And the fifth test now passes on the contrast it
claims, rather than on a rejected config:

```text
check  -> exit 0 | hook ran? False    (check writes nothing, so the hook must not fire)
index  -> exit 0 | hook ran? True     (index writes, so it must)
```

Windows unchanged: `116 passed`, and `RunsTheProjectsHook` on its own `Ran 7 tests … OK`.

**Decisions & assumptions**

- **The vacuous pass is treated as part of this task, not as a new one.** — It is the same defect at
  the same five call sites, and the fix repairs it in the same edit. Splitting it out would have
  produced a task whose evidence could no longer be gathered, because step 3 destroys the conditions
  that make it observable. Criterion 3 already asked for hooks that really run, so it is judged
  rather than smuggled. — 2026-08-09
- **The interpreter is chosen at runtime rather than branched on the platform.** — `os.name` would
  have encoded an assumption about each platform; `shutil.which` asks. That is also what the
  neighbouring `non_python_hook` does, so the file now applies one rule throughout instead of two.
  — 2026-08-09
- **Assumption, recorded as one: the running interpreter's basename is on `PATH`.** — True on both
  machines here, and the `python3`/`python` fallbacks cover the case where it is not. If none
  resolves the class skips, which is D2: the tests would be reporting on the machine rather than on
  the hook mechanism. — 2026-08-09

**Outputs produced**
- `tests/test_runtime.py` — `python_on_path`, `PYTHON_HOOK`, the class `setUp` skip, and the five
  call sites

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `tests/test_runtime.py` passes on a Linux clone, shown by its own output there | met | §3 step 4: `Ran 23 tests … OK`, and the whole suite `31 + 18 + 23 + 44 = 116` all passing — the same count Windows reports, so nothing was skipped into a green result. Four of those were failing before the change, on the same clone. |
| It still passes on Windows — the change must not trade one platform for the other | met | §3 step 5: `116 passed`, and `RunsTheProjectsHook` alone `Ran 7 tests … OK`. The fixtures resolve to `python3` on Linux and to the running interpreter's basename on Windows, from one helper rather than a platform branch. |
| The tests still exercise a hook that **really runs**, rather than being made to pass by declaring a hook that is never invoked | met | This is the criterion the task's second finding was written for, and it is the one that would have been easiest to fake. §3 step 4 shows the contrast directly: `check` exits 0 with the hook **not** fired, `index` exits 0 with it fired. Before the change the same test was satisfied by a config rejected at exit 2 — recorded in §3 step 2, which was the only moment it could be. |
| Any other hard-coded program name in the suite is either shown to exist on both platforms or changed — answered by looking, not by assuming this was the only one | met | §3 step 1 tabulates all seven. The other six were already guarded — `shutil.which` with a fallback, `skipTest`, a return-code skip, or an argv list no shell parses. The five hook fixtures were the only unguarded names, so the scope of the defect is now a measurement rather than an assumption. |

**Nothing in the tool changed, and that is the finding standing up.** T-049 raised this saying the
tool was not implicated; the fix touches only `tests/test_runtime.py`, so that judgement held once
someone worked on it. The message that started this — taskmd refusing a hook it could not run, and
naming why in the project's own terms — is unchanged and still correct.

**Child fix tasks raised**
- none

**Verdict.** All four criteria met, none carried. The task closes, and the suite now passes on both
platforms this project has ever run on.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met. The suite now passes on **both** platforms this project has ever run on: 116 on Linux where four were failing, 116 on Windows unchanged. Only `tests/test_runtime.py` changed, which is T-049's judgement standing up — it raised this saying the tool was not implicated, and nobody had to touch the tool. `specify` produced two findings rather than the expected one-word answer. First, `sys.executable` **cannot** be used: the resolver runs the declared line through `shlex.split`, which is POSIX-mode and eats the backslashes of a Windows path, and it treats a program containing a separator as a file inside the project. The value has to be a bare name resolved by `shutil.which`, which is the route a real project's hook takes anyway. Second, a **fifth** call site was passing, and the passing was the bug: `test_a_command_that_writes_nothing_does_not_run_the_hook` asserts the hook's output is absent, and on Linux it was absent because the config was rejected at exit 2 before any command ran. `plan` put the *before* measurement first specifically to catch that — the four failures survive in git history, but a vacuous pass leaves no trace once the fixture is repaired, so it was recorded in the one moment it was observable. It now passes on the contrast it claims: `check` writes nothing and the hook stays silent, `index` writes and it fires. Criterion 4 was answered by tabulating all seven program names the suite hands to a shell; the other six were already guarded by `shutil.which`, a `skipTest`, a return-code skip, or an argv list, so the five hook fixtures were the whole of the defect. |
| 2026-08-09 | → proposed | Raised by T-049 under METHOD §3.3 and left unfixed there on that task's own rule that a defect the run turns up is a finding rather than a repair. The first run of this suite on a non-Windows machine produced 116 tests and **4 failures**, all in `RunsTheProjectsHook`: the fixtures declare `after_write: python hooks/after-write.py` and Ubuntu ships no `python`, only `python3`. The tool is not implicated — it refused the hook and named the reason in the project's own terms, which is precisely what T-011 built it to do, so the failure message is the evidence that the mechanism works. `high` because a suite that cannot pass on Linux is a suite a Linux contributor cannot use to detect anything; `xs` because `sys.executable` is the interpreter already running the tests. The open question is whether that substitution weakens what the four tests prove, which turns on their being about hook *behaviour* rather than about which program the hook names. |
