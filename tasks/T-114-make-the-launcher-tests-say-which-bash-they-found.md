---
id: T-114
title: Make the launcher tests say which bash they found
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-091]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised from a run rather than from reading, while verifying T-091: four of `test_runtime.py`'s 27 failed, and establishing that none of them was T-091's took a stash, a re-run and a probe under both shells. Three turned out to be this one. The `bash` a session finds is not a property of the tree, and the suite currently reports it as one. |
