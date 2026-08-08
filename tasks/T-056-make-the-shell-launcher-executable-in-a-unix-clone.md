---
id: T-056
title: Make the shell launcher executable in a Unix clone
type: fix
status: done
phase: review
parent: T-054
blocked_by: []
related: [T-054, T-011, T-049]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-08
updated: 2026-08-09
deliverables: [plugin/taskmd.sh, tests/test_runtime.py]
---

# T-056 — Make the shell launcher executable in a Unix clone

## 1. Specify

**Outcome**
Someone who clones this repository on Linux or macOS can run the command `CLAUDE.md` tells them to
run, without first being told to repair the checkout.

**Why this one**
Found during [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) `implement`,
while deciding how `plugin/bin/taskmd` should invoke its target, and raised at that task's `review`
under METHOD §3.3 rather than fixed there.

`plugin/taskmd.sh` is recorded in the index as **`100644`**. Git stores the executable bit and
applies it on checkout, so on any Unix checkout the file arrives non-executable and
`./plugin/taskmd.sh check` — the form `CLAUDE.md`, `tasks/README.md` and the task template all
name — fails on permission before it reaches a shell. `plugin/bin/taskmd`, added by T-054, is
`100755` and is unaffected; so are the two Windows files, where the mode bit means nothing.

**It has never been visible here.** This project is developed on Windows, whose filesystem does not
enforce the bit, and Git Bash runs the script regardless — so every recorded run of the documented
command has succeeded on the one platform where the defect cannot appear. That is the same shape as
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md)'s finding and T-054's PowerShell
5.1 defect: a thing that works only where it was tested.

**Requirements served**
**R-18** (`docs/SCOPE.md`) — *"the repository root are auto-discovered so a clone runs unedited"* —
and `CLAUDE.md` *Publishing constraints*, which requires that someone who clones this can run it
with no path editing. A clone that needs `chmod` before its documented command works has not met
either, and this repository is going to be published.

**Scope**
- In: the mode recorded for `plugin/taskmd.sh`, and whether anything else in the tree that is meant
  to be executed carries the wrong one.
- In: whether this is checkable, so it cannot silently regress on a Windows-developed repository —
  the mode is readable from the index without a Unix machine.
- Out: what the launchers do. T-054 settled the entry points and this changes none of them.
- Out: the harness `PATH` mechanism and anything about installs —
  [T-006](T-006-package-document-and-publish.md).

**Inputs**
- `git ls-files -s plugin/` — the recorded modes, which is the whole of the evidence.
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 3, for why
  `bin/taskmd` invokes its target through `sh` and therefore does not depend on this.
- `CLAUDE.md` and `tasks/README.md` — the places that name `./plugin/taskmd.sh`.

**Acceptance criteria**
- [ ] `plugin/taskmd.sh` is recorded `100755`
- [ ] **What a clone receives** is shown to carry the executable bit — read out of the artifact a
      clone is actually built from, before and after, not out of this machine's filesystem
- [ ] Nothing else in the tree that is meant to be executed is left with the wrong mode — answered
      by enumerating what is executed, not by inspecting what looks like a script
- [ ] A regression is caught mechanically, and the guard is shown **failing** on the mode as it
      stands today — a guard against an invisible defect that has only ever passed is worth nothing
- [ ] The suite still passes and `check` is still clean on this repository

*Criterion 2 replaces the draft written when this task was raised, which asked for "a checkout of
the current mode into a fresh worktree, with the failure the command actually gives". That is not
reachable here and the reason is the defect itself: this machine has no Unix filesystem — no WSL
distribution and no container runtime — and Git Bash does not enforce the bit, so `chmod -x`
followed by `./probe.sh` still prints `ran`. **The permission failure cannot be produced on this
machine at all**, so a criterion demanding it would have been an aspiration in specify.md's sense.
What replaces it is stronger than a proxy: `git archive` emits the tree with the modes a Unix
extraction applies, so the bit a clone receives is readable directly, and the mode is precisely what
decides whether the command runs.*

**Open questions**
- None. **Answered here: yes, add the guard**, and criterion 4 carries it. The argument that settled
  it is not "tests are good" but *where* this defect lives: it is invisible on the only machine the
  project is developed on, so a regression would be silent until a stranger cloned it — the same
  shape that produced T-052, T-054's PowerShell 5.1 defect and this task. A guard reading the
  recorded mode costs one assertion and is the only thing that can see the difference locally.
  *Rejected: the fix alone*, on the grounds that the file changes rarely — true, and irrelevant,
  because the cost of a silent recurrence is paid by whoever clones rather than by whoever caused
  it. *Rejected: a guard naming the two files*, which would be a hand-maintained list of what is
  executable; the set is derivable, and criterion 3's enumeration is what says how.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Enumerate what the tree actually executes by path, and record the recorded mode of each | A table in §3, and with it the answer to whether one file is wrong or several |
| 2 | Read the bit **out of what a clone receives**, before any change | The `git archive` modes for the enumerated set, recorded in §3 — the *before* |
| 3 | Write the guard, and run it against the tree as it stands | The guard **failing**, output in §3. This is the step that can invalidate the rest: a guard that passes now is testing the wrong thing |
| 4 | Change the recorded mode | `plugin/taskmd.sh` at `100755` |
| 5 | Re-read what a clone receives, and re-run the guard | The *after*, and the guard passing, both in §3 |
| 6 | Re-run the suite and `check` | Recorded output in §3 |

Step 1 is first because it decides the size of step 4 — the task was raised on one file and the
criterion asks whether it is only one. Step 3 is deliberately **before** the fix and is where this
plan can be invalidated: a guard written after the change would pass on its first run and prove
nothing, which is the `Verifying` rule in `CLAUDE.md` and the reason criterion 4 asks to see it fail.

**Shape decisions.**

**D1 — The guard derives its subject from the shebang, and names no file.** The rule it encodes:
*a tracked file whose shebang names a POSIX shell must be recorded executable*. That set is read
from the tree, so a launcher added later is covered without anyone remembering to add it, and there
is no list to drift. It is also the correct rule rather than a convenient one: a shell script has no
equivalent of `python -m`, so a `#!/bin/sh` file exists to be run by path, whereas the Python files
in this tree all carry a shebang and are all documented to run *through* the interpreter.
*Rejected: asserting the mode of `taskmd.sh` and `bin/taskmd` by name* — it is a hand-maintained
second copy of "what is executable", and it goes stale exactly when a file is added, which is the
moment it would matter.

**D2 — The guard reads git's index, not the filesystem.** `core.fileMode` is `false` here, so the
working tree's bits are ignored by git and are not what a clone receives; the index is. Reading the
filesystem would produce a test that passes on Windows regardless of what is committed, which is the
defect wearing a test's clothes. *Rejected: `os.access(..., os.X_OK)`* — on Windows it answers for
the wrong thing entirely.

**D3 — It goes in `tests/test_runtime.py`'s existing `Launchers` class.** That class already holds
the claims about how the launchers are reached, and this is one more. *Rejected: a new test module*
— a file per assertion makes the suite harder to read for no gain here.

**Planned outputs**
- `plugin/taskmd.sh` — the recorded mode
- `tests/test_runtime.py` — the guard

## 3. Implement

### Step 1 — what the tree executes by path, and it is one file

Every tracked file whose first line is a shebang, with the mode git records for it:

```text
100755  plugin/bin/taskmd            #!/bin/sh
100644  plugin/taskmd.sh             #!/bin/sh
100644  plugin/taskmd/__main__.py    #!/usr/bin/env python
100644  plugin/taskmd/cli.py         #!/usr/bin/env python
100644  plugin/taskmd/discovery.py   #!/usr/bin/env python
100644  plugin/taskmd/schema.py      #!/usr/bin/env python
100644  reference/task.py            #!/usr/bin/env python
100644  tests/test_cli.py            #!/usr/bin/env python
100644  tests/test_list.py           #!/usr/bin/env python
100644  tests/test_runtime.py        #!/usr/bin/env python
100644  tests/test_schema.py         #!/usr/bin/env python
```

Eleven files carry a shebang and **one** is wrong, which is criterion 3 answered rather than
assumed. The nine Python files are not a second finding: every one of them is documented to run
*through* the interpreter — `python -m taskmd`, `python tests/test_cli.py`,
`python tools/tasks/task.py` — and none is invoked by path anywhere in the tree. A shebang on a file
nobody executes directly is decoration, not a wrong mode.

That distinction is the rule the guard encodes, and it is why the guard keys on the shebang naming a
**shell**: `#!/bin/sh` has no `-m` equivalent, so such a file exists to be run by path.

### Step 2 — the bit a clone receives, before

Read out of `git archive`, which emits the tree with the modes a Unix extraction applies — the
artifact a clone is built from, rather than this machine's filesystem:

```text
-rwxrwxr-x  plugin/bin/taskmd
-rw-rw-r--  plugin/taskmd.sh
```

`bin/taskmd` carries the bit because T-054 set it; `taskmd.sh` does not. This is the defect in the
only form it takes here.

### Step 3 — the guard, failing on the tree as it stood

Written before the fix, per the plan, and run against the unfixed tree:

```text
FAILED tests/test_runtime.py::Launchers::test_every_posix_shell_script_is_recorded_executable
- []
+ ['plugin/taskmd.sh is recorded 100644']
```

It names the one file and no other, so it is discriminating rather than merely red. Had it passed
here, it would have been testing something other than what this task is about — which is why the
plan put it before step 4.

### Steps 4 and 5 — the change, and the same two readings after

`git update-index --chmod=+x plugin/taskmd.sh`. The working tree is untouched: `core.fileMode` is
`false`, so the filesystem bit is neither read nor written by git, and the index is the whole of what
changes.

```text
100755  plugin/bin/taskmd            100755  plugin/taskmd.sh

-rwxrwxr-x  plugin/bin/taskmd        -rwxrwxr-x  plugin/taskmd.sh

tests/test_runtime.py::Launchers::test_every_posix_shell_script_is_recorded_executable  1 passed
```

### Step 6 — the suite and this repository

```text
115 passed
OK - 56 task(s), vocabulary valid, references resolve, no broken links
```

114 before, 115 after: the guard is the one addition.

**What was not verified, and why it is not a gap this task can close.** The permission failure
itself — `./plugin/taskmd.sh` refused on a Unix checkout — has never been produced and cannot be
produced here. This machine has no WSL distribution and no container runtime, and Git Bash does not
enforce the bit: `chmod -x` on a scratch script leaves it `-rwxr-xr-x` and `./probe.sh` still prints
`ran`. So the chain rests on git's documented behaviour, that the recorded mode is applied on
checkout, plus the `git archive` reading above, which is that same mode in the artifact a clone
receives. `specify` replaced the criterion accordingly rather than leaving one nobody could meet.

**Decisions & assumptions**

- **The nine Python shebangs are left alone.** — They are inaccurate in the weak sense that nothing
  runs those files by path, but changing them is neither this task's outcome nor a defect: no
  document names them as commands, and removing nine shebangs would be an unrequested edit to nine
  files. Recorded because step 1's table makes them visible, and a later reader should know they
  were seen and judged rather than missed. — 2026-08-09
- **The guard skips rather than fails outside a git work tree.** — Someone running the suite from a
  downloaded archive has no index to read, and the recorded mode is exactly what the assertion is
  about, so there is nothing to assert. A failure there would be the test reporting on its own
  environment. — 2026-08-09
- **Assumption, recorded as one: git applies the recorded mode on checkout.** — Not verified on a
  Unix machine by this task, for the reason above. The work survives being wrong about it only in
  the sense that `100755` is still the correct thing to record; if git did not apply it, the fix
  would be inert rather than harmful, and the defect would lie somewhere this task never reached.
  — 2026-08-09

**Outputs produced**
- `plugin/taskmd.sh` — recorded `100755`, content unchanged
- `tests/test_runtime.py` — `test_every_posix_shell_script_is_recorded_executable`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `plugin/taskmd.sh` is recorded `100755` | met | §3 step 4. The content is byte-identical; `core.fileMode` is `false`, so the index is the only thing that changed. |
| **What a clone receives** is shown to carry the executable bit — read out of the artifact a clone is actually built from, before and after | met | §3 steps 2 and 5, both from `git archive`: `-rw-rw-r--` before, `-rwxrwxr-x` after, with `bin/taskmd` unchanged beside it as a control that the reading distinguishes the two states. |
| Nothing else in the tree that is meant to be executed is left with the wrong mode — answered by enumerating what is executed, not by inspecting what looks like a script | met | §3 step 1 lists all **11** tracked files carrying a shebang. One was wrong. The nine Python files are each documented to run through the interpreter and none is invoked by path anywhere in the tree, so their shebangs are decoration rather than a second finding — seen and judged, not missed. |
| A regression is caught mechanically, and the guard is shown **failing** on the mode as it stands today | met | §3 step 3, run before the fix: it failed naming `plugin/taskmd.sh is recorded 100644` and nothing else, so it discriminates rather than merely going red. Passing after, and it derives its subject from the shebang, so a launcher added later is covered without anyone remembering. |
| The suite still passes and `check` is still clean on this repository | met | `115 passed` — 114 before, the guard being the one addition — and `OK - 56 task(s), vocabulary valid, references resolve, no broken links`. |

**The gap this task could not close, and where it is carried.** The permission failure itself has
never been produced: there is no Unix filesystem on this machine, and Git Bash does not enforce the
bit. So the fix rests on git applying the recorded mode on checkout — recorded in §3 as an
assumption rather than as a result. It is **not** raised as a new task, because two open ones
already carry exactly this:
[T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) *Demonstrate a clone running on
a second platform* and [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) *Confirm
byte-identical output on macOS and Linux*. T-049 is now linked from this task, so whoever takes it
finds what was left unverified here without having to know to look.

**Child fix tasks raised**
- none

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met, none carried. `plugin/taskmd.sh` is recorded `100755` and a clone now receives it `-rwxrwxr-x`, read both times out of `git archive` — the artifact a clone is built from — with `bin/taskmd` beside it as a control. The enumeration answered criterion 3 rather than leaving it assumed: **11** tracked files carry a shebang, exactly one was wrong, and the nine Python ones are each documented to run through the interpreter and invoked by path nowhere, so their shebangs are decoration. The guard was written **before** the fix and shown failing on `plugin/taskmd.sh is recorded 100644` and nothing else; it keys on the shebang naming a shell rather than on a list of filenames, so a launcher added later is covered without anyone remembering, and it reads git's index rather than the filesystem because `core.fileMode` is `false` here and the working tree's bits are not what a clone receives. Suite 115 (114 before), `check` OK on 56. The gap this could not close is named rather than papered over: the permission failure itself has never been produced, there being no WSL distribution or container runtime here and Git Bash not enforcing the bit, so the fix rests on git applying the recorded mode on checkout — recorded as an assumption. No task raised for it: T-049 and T-020 already carry exactly that, and T-049 is now linked from here so whoever takes it finds what was left open. |
| 2026-08-09 | → specified → planned → in_progress | Whole lifecycle run in one request, which is the request rather than an auto-advance. `specify` replaced the demonstration criterion drafted at raise-time — it asked for the failure the command actually gives, which this machine cannot produce — with a reading of what a clone receives, and answered the open question **yes**: the guard is worth it precisely because the defect is invisible on the only machine the project is developed on, so a regression would be silent until a stranger cloned it. `plan` put the guard **before** the fix, since one written afterwards passes on its first run and proves nothing. |
| 2026-08-08 | → proposed | Raised at T-054's `review` under METHOD §3.3, having been found during that task's `implement`; not fixed there, because review does not repair what it finds. `plugin/taskmd.sh` is recorded `100644`, so a Unix clone gets it non-executable and `./plugin/taskmd.sh` — the form `CLAUDE.md`, the index preamble and the task template all name — fails on permission. Invisible here because Windows does not enforce the bit and Git Bash runs the file anyway, so every recorded run of the documented command has been on the one platform where the defect cannot appear. `high`/`xs`: one mode bit, but it is R-18 failing for every non-Windows contributor of a repository that is about to be published. T-054's `bin/taskmd` is `100755` and invokes its target through `sh`, so nothing shipped to an adopter depends on this. The open question is whether to add a guard asserting the recorded mode, since a regression would recur exactly where it cannot be seen. |
