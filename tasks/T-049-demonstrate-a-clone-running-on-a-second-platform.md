---
id: T-049
title: Demonstrate a clone running on a second platform
type: fix
status: done
phase: review
parent: T-011
blocked_by: []
related: [T-006, T-054, T-056]
work_package: v0.1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-09
deliverables: []
---

# T-049 — Demonstrate a clone running on a second platform

## 1. Specify

**Outcome**
The claim that a clone runs unedited on Windows, macOS and Linux is carried by output from **two**
of them rather than one. Today it is carried by Windows alone.

**Why this one**
Raised by [T-011](T-011-runtime-discovery-and-project-hook-commands.md)'s review. Its first
acceptance criterion asks for at least two platforms, and the environment T-011 was built in had no
Linux distribution installed and no container runtime — so the second platform could not be run.
Recording it as a child rather than counting the criterion met is METHOD §2's rule for `review`: a
criterion is met, or it carries a task that will meet it.

**This is not a code task.** Nothing is known to be wrong. Auto-discovery and the launchers were
written to be portable and the portability constraints in `CLAUDE.md` were followed, but written-to-be
and shown-to-be are exactly the distinction that section draws. If it turns out something *is* wrong
— a `#!` line, a path separator, a shell builtin — that is a finding this task raises, not one it
fixes.

**Requirements served**
R-18, R-20 (`docs/SCOPE.md`), and §9's first bullet.

**Scope**
- In: running the CLI and both launchers on a second platform from a fresh clone, with no
  configuration and no path editing, and recording the output.
- Out: any second implementation of the commands (assumption A1), and any change to the tool unless
  the run turns one up.

**Inputs**
`T-011` §3 *Verification* — the Windows half, and the commands to repeat; `CLAUDE.md` *Publishing
constraints*; `docs/SCOPE.md` R-20.

**Acceptance criteria**
- [ ] A fresh clone runs `check`, `index`, `list` and `context` on a second platform with no
      configuration, no dependency install and no path editing — with the actual output
- [ ] Both launchers are exercised there, or the absent one is stated as absent with the reason
- [ ] The generated index is **byte-identical** to the one this repository already carries, which is
      what R-20 actually claims and what a platform difference would break first
- [ ] A hook written in that platform's own shell is run, since criterion 4 of T-011 was proven with
      PowerShell and the mechanism's language-freedom is the point
- [ ] The shipped `bin/taskmd` entry point resolves and runs from the clone, and **arrives
      executable without anyone running `chmod`**
      <br>*Added 2026-08-09. The four above predate it and are unchanged — they were agreed on
      2026-08-07, before [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)
      made `bin/taskmd` the thing an adopter types.
      [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md) then closed on an
      explicit assumption — that git applies the recorded `100755` on checkout — which no machine
      available at the time could test. This criterion retires that assumption as a side effect of
      work this task was doing anyway.*

**Open questions**
- **When, and on what.** The maintainer's answer on 2026-08-07 was "hand it to T-006, or after the
  first version is published" — so the route (a CI runner at packaging time, or a real machine after
  publication) is chosen with T-006 rather than here. That is why this task is `related` to T-006
  and not blocked by it: it could be done sooner if a second platform becomes available.

  **Re-measured 2026-08-09, and the premise has changed: a second platform is reachable today.**
  WSL2 is the configured default on this machine and the mechanism is functional — `wsl --list
  --online` returns the catalogue, several Ubuntu LTS images among them — with 483 GB free. What is
  absent is only an *installed distribution*; there is still no container runtime under any name.
  So the phrase "if a second platform becomes available" now resolves to a decision rather than to
  waiting.

  Two further facts bear on the route. **There is no git remote at all**, so the CI-runner option is
  not merely deferred to T-006, it is unavailable until this repository is published — which is
  T-006's own work. And a fresh clone does not need one: `git clone <local path>` produces exactly
  the unconfigured checkout the criteria ask for, so the clone half of this task has never been the
  blocked half.

- **Does the `bin/` entry point belong in the criteria?** The four above were agreed on 2026-08-07,
  before [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) existed. Since then
  `plugin/bin/taskmd` is what an adopter actually types, and
  [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md) closed on an explicit
  **assumption** — that git applies the recorded `100755` on checkout — which no machine here could
  test. A Linux clone settles that in one command, so this task can retire another task's open
  assumption at no extra cost. Needs the owner, being an addition to an agreed set.

**Both answered by the maintainer, 2026-08-09.** The route is a real Linux machine, now — a WSL2
Ubuntu distribution was installed rather than the work being deferred to T-006 or routed through a
CI runner. And the fifth criterion is added, with the original four recorded as predating it.

**The platform, measured before planning against it.** `Linux 6.18.x-microsoft-standard-WSL2
x86_64` — the kernel's patch component is elided throughout this record, because a four-part version
number is indistinguishable from an IP address to the pre-publish check
([T-058](T-058-say-that-a-four-part-version-trips-the-leak-check.md)) — home on **ext4** — which matters: mode bits carry no meaning on the mounted Windows drive,
so criterion 5 would have been unfalsifiable had the clone gone there. Present with no install:
`python3` 3.14.4, `git` 2.53.0, `bash`. **Absent: `pwsh`** — criterion 2's "or the absent one is
stated as absent with the reason" arriving as anticipated rather than as a surprise.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Clone into the Linux filesystem from the local path, configuring nothing | A checkout on ext4, and the clone command recorded in §3 |
| 2 | Read what **arrived** — the mode bits on the two POSIX scripts, before running anything | §3, and with it criterion 5's second half and the verdict on T-056's assumption |
| 3 | Run `check`, `index`, `list` and `context` through `./plugin/taskmd.sh` | Their actual output in §3 |
| 4 | Run the same commands through the shipped `bin/taskmd`, reached by name on `PATH` | §3 — criterion 5's first half |
| 5 | Compare the index the clone generates against the one this repository carries, byte for byte | A comparison in §3 that distinguishes "same" from "not compared" |
| 6 | Declare a hook in the clone's own config, written in that platform's shell, and run the command that fires it | §3 — criterion 4 |
| 7 | Record the PowerShell launcher as unexercised, with the reason | §3 — criterion 2's second branch |
| 8 | Run the test suite there, beyond what the criteria ask | §3, labelled as extra evidence rather than as a criterion |

Step 2 is deliberately **before** anything is run: the mode bits are the one thing a later step could
destroy by accident, and reading them first is what makes criterion 5 a measurement of the checkout
rather than of whatever the session did to it afterwards. It is also where this plan can be
invalidated — if the bit did not survive, T-056's assumption was wrong, criterion 5 fails, and steps
4 onward are describing a different situation.

**Shape decisions.**

**D1 — The clone goes on ext4, not on the mounted Windows drive.** `/mnt/c` is a translation layer
that reports mode bits it does not store, so a clone there would let criterion 5 pass without the
checkout ever having carried an executable bit. *Rejected: cloning into the Windows tree and running
it from Linux* — cheaper to set up and it would have quietly answered the one question this task was
extended to ask.

**D2 — The clone is made from the local path, not from a remote.** There is no remote, and creating
one means publishing, which is T-006's decision. `git clone <path>` produces the same unconfigured
checkout the criteria describe: no configuration, no dependency install, no path editing.
*Rejected: copying the working tree* — it would carry this session's untracked files and the mode
bits of the source filesystem rather than of the commit, which is precisely what step 2 measures.

**D3 — Nothing is installed inside the distribution.** `python3`, `git` and `bash` are already
there, which is what makes the "no dependency install" half of criterion 1 a real observation. If
something turns out to be missing, that is a finding to record, not a gap to fill with `apt`.

**Planned outputs**
- No files. This task's output is recorded evidence in §3 — plus, per §1, any finding the run turns
  up, which becomes its own task rather than a fix here.

## 3. Implement

Absolute paths are redacted throughout — the machine's own home directory is the class the
pre-publish check in `CLAUDE.md` exists to catch, and this record is the one most likely to trip it.

### Steps 1 and 2 — the clone, and what arrived in it

```text
filesystem : ext4
commit     : 2c0df09
config     : no .taskmd/ - shipped defaults
python     : /usr/bin/python3  Python 3.14.4
```

`git clone <repo> <dir>` from the local path, nothing configured afterwards. One setup detail worth
recording because it is **not** a property of the project: cloning across the mounted Windows drive
trips git's `dubious ownership` guard, so the clone was made with `-c safe.directory=…` scoped to
that single command rather than by changing any config.

Then, before running anything:

```text
-rwxr-xr-x  plugin/bin/taskmd
-rw-r--r--  plugin/bin/taskmd.cmd
-rwxr-xr-x  plugin/taskmd.sh
```

**This settles [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md)'s open
assumption.** That task recorded, as an assumption it could not test, that git applies the recorded
mode on checkout. It does: both POSIX scripts arrived executable and the `.cmd` did not, which is
also the control — the reading distinguishes the two states rather than reporting everything as
executable.

*Deviation, recorded: the first clone landed on `tmpfs` and was redone on ext4.* `tmpfs` stores POSIX
modes correctly and the result was identical, so nothing turned on it — but **D1**'s reason was that
the filesystem must really store the bit, and matching its word costs one command.

### Steps 3 and 4 — the four commands, through both ways in

Through `./plugin/taskmd.sh`, from the clone root:

```text
OK - 56 task(s), vocabulary valid, references resolve, no broken links
Wrote tasks/README.md - 20 active, 36 closed
T-006	specified	-	specify	Package, document and publish
T-049	proposed	-	specify	Demonstrate a clone running on a second platform
T-025	specified	-	specify	Let check notice a stale generated index

T-049  Demonstrate a clone running on a second platform
status proposed | phase specify | type fix | work_package - | owner maintainer
```

Through the shipped `bin/taskmd`, reached **by name on `PATH`** and run from `tasks/` — a
subdirectory, so the walk-up discovery from T-011 is exercised in the same breath:

```text
cwd is a subdirectory: tasks
~/…/clone/plugin/bin/taskmd
OK - 56 task(s), vocabulary valid, references resolve, no broken links
Wrote tasks/README.md - 20 active, 36 closed
T-006	specified	-	specify	Package, document and publish
```

No configuration, no dependency install, no path editing, and no `chmod` — the entry point was
usable as it arrived.

### Step 5 — the generated index, byte for byte

The clone regenerated `tasks/README.md` on Linux and it is identical to the blob committed from
Windows:

```text
byte-identical: git reports no difference after regenerating on Linux
sha256 of the regenerated file : 4c7ba95a4b644f45...
sha256 of the committed blob   : 4c7ba95a4b644f45...
```

Two readings rather than one, because `git diff` staying quiet is also what a file nobody wrote
looks like — the hashes distinguish "same" from "not compared", which is what R-20 actually claims
and what a line-ending difference would have broken first.

### Step 6 — a hook in this platform's own shell

The default config was copied to `.taskmd/config.md` per `adopt.md` §2 and `after_write` pointed at
a `#!/bin/sh` script:

```text
after_write: ./hook.sh
Wrote tasks/README.md - 20 active, 36 closed
Hook   ./hook.sh
    hook says: Linux 6.18.x-microsoft-standard-WSL2 x86_64, and it is not PowerShell
```

T-011's criterion 4 was proven with PowerShell; the mechanism's point is that it does not care, and
this is the other half of that claim.

### Step 7 — the PowerShell launcher, absent with a reason

Neither `pwsh` nor `powershell` is present, and no PowerShell is installed by default on this
distribution. `taskmd.ps1` is the Windows way in; on this platform `taskmd.sh` and `bin/taskmd` are
what a clone uses, and both were exercised above. This is criterion 2's second branch taken as
written rather than a gap.

### Step 8 — the suite, and the one finding

Beyond the criteria, and it earned its place:

```text
test_cli.py       Ran 31 tests  OK
test_list.py      Ran 18 tests  OK
test_runtime.py   Ran 23 tests  FAILED (failures=4)
test_schema.py    Ran 44 tests  OK
total tests run on Linux: 116
```

116, the same count as Windows, so nothing was skipped into a false pass. The four failures are all
in `RunsTheProjectsHook`, and **the tool is not implicated**:

```text
CONFIG ERROR  .taskmd/config.md: after_write starts with 'python', which is not on PATH and is not
a path in this project. Name an executable that is installed, or a file the project ships.
```

The fixtures declare their hook as `python hooks/after-write.py`, and **Ubuntu ships no `python`,
only `python3`**. taskmd refused a hook it could not run and said why in the project's own terms,
which is what T-011 built it to do — so the failure message is evidence the mechanism works, not
evidence against it. Windows has `python`, which is why the assumption was invisible where it was
written.

Raised as [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) and **not fixed
here**, on §1's own rule.

**Decisions & assumptions**

- **The suite's four failures are a finding, not a criterion failure.** — No criterion mentions the
  suite; step 8 was planned as extra evidence. R-20 claims the *tool* runs on a clone, and it does —
  what carries a Windows assumption is a test fixture. Recording it as a failure of this task would
  misattribute it and would leave T-057 without a reason to exist. — 2026-08-09
- **Nothing was installed inside the distribution, and that is a result rather than a constraint
  obeyed.** — `python3`, `git` and `bash` were already present, so the "no dependency install" half
  of criterion 1 is an observation about a stock Ubuntu rather than about a machine someone had
  prepared. **D3** said a missing tool would be a finding; none was missing. — 2026-08-09
- **`safe.directory` was scoped to one command rather than configured.** — The guard fires because
  the *source* sits on a mounted Windows drive, which is an artifact of how this second platform was
  obtained and would not exist for anyone cloning from a remote. Persisting it would have written a
  machine-specific workaround into the record of a portability test. — 2026-08-09

**Outputs produced**
- No files, as planned. The output is the evidence above, plus
  [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md).

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A fresh clone runs `check`, `index`, `list` and `context` on a second platform with no configuration, no dependency install and no path editing — with the actual output | met | §3 steps 1, 3 and 4. `Linux 6.18.x-…-WSL2 x86_64`, clone on ext4 from the local path, no `.taskmd/` so the shipped defaults were in force, and `python3`/`git`/`bash` already present on a stock Ubuntu — so "no dependency install" is an observation rather than a rule obeyed. All four commands ran through both ways in, one of them from a subdirectory, which exercised T-011's walk-up at the same time. |
| Both launchers are exercised there, or the absent one is stated as absent with the reason | met | `taskmd.sh` exercised (§3 step 3). `taskmd.ps1` not exercised, and §3 step 7 gives the reason: neither `pwsh` nor `powershell` is present and no PowerShell ships by default on this distribution. This is the criterion's second branch taken as written. |
| The generated index is **byte-identical** to the one this repository already carries | met | §3 step 5, and read two ways on purpose: `git diff` quiet **and** matching sha256 against the committed blob. The second reading is what distinguishes "identical" from "never compared", which a quiet diff alone cannot. |
| A hook written in that platform's own shell is run | met | §3 step 6: a `#!/bin/sh` hook declared through the project's own config, fired by `index`, its output shown inline by taskmd. T-011 proved the mechanism with PowerShell; this is the half that shows it does not care which language. |
| The shipped `bin/taskmd` entry point resolves and runs from the clone, and **arrives executable without anyone running `chmod`** | met | §3 steps 2 and 4. It arrived `-rwxr-xr-x` straight out of the checkout, with `bin/taskmd.cmd` arriving `-rw-r--r--` beside it as the control, and then resolved by bare name on `PATH`. *Added 2026-08-09; the four above predate it.* |

**This retires an assumption in another task.** [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md)
closed recording, as an explicit assumption, that git applies the recorded `100755` on checkout —
no machine available to it could test that. Criterion 5 tested it: the bit survived. T-056's record
is left as it stands, because the assumption was true and correctly labelled at the time; editing a
closed task to remove a caveat that its successor confirmed would destroy the audit trail rather
than tidy it.

**The finding, and why it is not a criterion failure.** The suite was run beyond what any criterion
asks and produced 116 tests with **4 failures**, all hook fixtures declaring `python` on a
distribution that ships only `python3`. taskmd itself refused the hook and named the reason in the
project's own terms — the behaviour T-011 built — so what carries a Windows assumption is a test
fixture, not the tool. R-20 claims the tool runs on a clone, and it did. Recorded as
[T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) and left unfixed, on §1's
rule that a defect this run turns up is a finding it raises rather than one it repairs.

**Child fix tasks raised**
- [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) — the hook tests name an
  interpreter that does not exist on Linux, so the suite cannot pass there. Found by step 8, raised
  rather than fixed.
- [T-058](T-058-say-that-a-four-part-version-trips-the-leak-check.md) — the pre-publish check cannot
  tell a four-part version number from an IP address, and fired on this task's own record. Nothing
  leaked; what is wrong is that `CLAUDE.md` promises every hit is a leak, so the next person hunts
  for one. Worked around here by eliding the kernel's patch component, which is a fix for one record
  and not for the next.

**Verdict.** All five criteria met, one finding carried as a task. The task closes, and the platform
claim is now carried by output from two platforms rather than one.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met; **the platform claim is now carried by output from two platforms rather than one**. A fresh clone on `Linux …-WSL2 x86_64`, on ext4, from the local path with nothing configured, ran `check`, `index`, `list` and `context` through both `./plugin/taskmd.sh` and the shipped `bin/taskmd` — the latter by bare name on `PATH` from a subdirectory, which exercised T-011's walk-up in the same breath. Nothing was installed: `python3`, `git` and `bash` were already on a stock Ubuntu, so "no dependency install" is an observation rather than a rule obeyed. The regenerated index is byte-identical to the committed blob, read two ways because a quiet `git diff` looks the same as a file nobody wrote. A `#!/bin/sh` hook ran and its output was shown, which is the half of T-011's criterion 4 that PowerShell could not carry. `taskmd.ps1` is recorded absent with the reason. **Criterion 5 retires T-056's open assumption**: both POSIX scripts arrived `-rwxr-xr-x` out of the checkout with the `.cmd` arriving non-executable as the control, so git does apply the recorded mode. T-056's record is left as it stands — the assumption was true and honestly labelled, and editing a closed task to delete a caveat its successor confirmed would destroy the audit trail. One finding, raised not fixed: the suite ran 116 tests there, the same count as Windows, with **4 failures**, all hook fixtures naming `python` on a distribution that ships only `python3`. taskmd refused the hook and named the reason in the project's own terms, which is the behaviour T-011 built, so the assumption is in a test fixture and not in the tool — **T-057**. |
| 2026-08-09 | → specified → planned → in_progress | Whole lifecycle in one request. `specify` re-measured the premise the task was raised on and it had changed: WSL2 was functional here with Ubuntu one command away, while the CI route the maintainer sketched in August turned out unavailable — **there is no git remote at all**, so CI needs publishing, which is T-006's own work. A clone never needed a remote either. Maintainer chose to install a distribution and run it now, and to **add a fifth criterion** for the `bin/` entry point and its mode bit, the original four being recorded as predating T-054. `plan` put "read what arrived" before anything is run, because the mode bits are the one thing a later step could destroy by accident, and it fixed the clone to a real POSIX filesystem — a clone on the mounted Windows drive would have let criterion 5 pass without the checkout ever carrying an executable bit. |
| 2026-08-07 | → proposed | Raised by T-011's review, which met five of six criteria and could not run the sixth's second half: no Linux distribution and no container runtime in the environment, so the platform claim rests on Windows alone. Recorded as a child rather than as a caveat, because METHOD §2 lets a criterion be unmet only if a task carries it. Soft-linked to T-006 rather than blocked by it, on the maintainer's routing — it should travel with packaging, but nothing stops it being done the moment a second platform exists. |
