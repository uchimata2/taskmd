---
id: T-057
title: Let the hook tests name an interpreter that exists on the platform
type: fix
status: proposed
phase: specify
parent: T-049
blocked_by: []
related: [T-049, T-011]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
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

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised by T-049 under METHOD §3.3 and left unfixed there on that task's own rule that a defect the run turns up is a finding rather than a repair. The first run of this suite on a non-Windows machine produced 116 tests and **4 failures**, all in `RunsTheProjectsHook`: the fixtures declare `after_write: python hooks/after-write.py` and Ubuntu ships no `python`, only `python3`. The tool is not implicated — it refused the hook and named the reason in the project's own terms, which is precisely what T-011 built it to do, so the failure message is the evidence that the mechanism works. `high` because a suite that cannot pass on Linux is a suite a Linux contributor cannot use to detect anything; `xs` because `sys.executable` is the interpreter already running the tests. The open question is whether that substitution weakens what the four tests prove, which turns on their being about hook *behaviour* rather than about which program the hook names. |
