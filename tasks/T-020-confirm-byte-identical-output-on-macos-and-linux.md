---
id: T-020
title: Confirm byte-identical output on macOS and Linux
type: analysis
status: planned
phase: plan
parent: T-002
blocked_by: []
related: [T-006]
work_package: v0.5
owner: maintainer
business_value: high
effort: m
created: 2026-08-05
updated: 2026-08-11
deliverables: []
---

# T-020 — Confirm byte-identical output on macOS and Linux

## 1. Specify

**Outcome**
The same commands run on Linux against the same tree, with the output compared byte for byte
against the Windows run — turning T-002's mechanism argument into a measurement. macOS is stated as
untested rather than claimed. *Amended 2026-08-07 with the answer below, which named the tested pair
as Windows and Linux; the original read "on macOS and on Linux" and would have promised what the
answer declines to do. The acceptance criteria are unchanged.*

**Why this one**
T-002's criterion reads *"output byte-identical across Windows, macOS and Linux"*. Only Windows was
available, so `implement` verified the **mechanism** instead: explicit `newline="\n"` on every
write, no `os.linesep`, separators normalised to `/` in printed output, asserted in
`tests/test_cli.py::WritesTheSameBytesEverywhere`. That is a good argument and it is not the
criterion. The plan recorded the gap as an assumption rather than letting the review tick a box the
evidence does not support.

This matters more than it looks. R-20 puts cross-platform identical behaviour in the goal, and
`docs/SCOPE.md` §9 puts it in the definition of done — so an untested claim here is a claim the
README will eventually make.

**Requirements served**
R-20 (`docs/SCOPE.md`).

**Scope**
- In: `context`, `index` and `check` on this repository and on `tests/fixtures/alt-project`.
- Out: making anything pass. If a difference appears, it is a finding and its own fix task — this
  task measures.

**Inputs**
A macOS or Linux machine with a Python 3 interpreter; this repository at a known commit.

**Acceptance criteria**
- [ ] The three commands run on at least one non-Windows platform, at a named commit
- [ ] `index` output compared byte for byte with the Windows run; any difference reported rather
      than normalised away
- [ ] Console output of `context` and `check` compared as bytes, not read and judged equivalent
- [ ] The result recorded either way — a confirmation is as much the outcome as a difference is
- [ ] T-002's recorded assumption is marked closed, or replaced by what was actually found

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: Linux, with macOS left explicitly untested.**
  Windows and Linux are the tested pair. The risk this closes is the one that actually splits by
  platform — line endings and console encoding are a Windows-versus-POSIX difference rather than a
  macOS-versus-Linux one. *Rejected: testing both.* The gap is real: macOS differs from Linux in
  filename Unicode normalisation and in being case-insensitive by default, which is a class Linux
  cannot expose. So it is **stated as unverified rather than closed**, which criterion 4 already
  requires and criterion 1 already permits — it asks for at least one non-Windows platform.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Name the commit, then capture the Windows baseline — `context`, `index`, `check`, each on this repository and on `tests/fixtures/alt-project` — as **raw stdout+stderr bytes** | Six capture files, and the commit recorded in §3 |
| 2 | Clone that commit into ext4 inside WSL2 Ubuntu, configuring and installing nothing | A Linux checkout at the same commit, the command recorded |
| 3 | Take the same six captures there | Six capture files on Linux |
| 4 | Compare each pair byte for byte — hash first, then a byte-level diff naming the offset and the differing bytes wherever they are not equal | A per-command verdict in §3 that distinguishes "same" from "not compared" |
| 5 | Compare the `index` **artifact** — the generated `tasks/README.md` — separately from the console output | A verdict in §3 |
| 6 | Classify every difference as line terminator, path separator, encoding or content, and raise each as its own task | §3, plus any child tasks |
| 7 | Annotate T-002's recorded assumption with what was measured | A log row on T-002, and §3 |

Step 5 is separate from step 4 because the two are written by different mechanisms and only one of
them is covered by `tests/test_cli.py::WritesTheSameBytesEverywhere`: the artifact goes through the
project's `newline="\n"` writer, while console output goes through whatever Python's text layer does
to `sys.stdout`. Folding them into one comparison would let a pass on the tested half hide a
difference in the untested one — which is the shape of gap this task exists to close.

**Shape decisions.**

**D1 — Capture through `cmd /c` redirection on Windows, never PowerShell's `>`.** PowerShell decodes
a native command's output into strings and re-encodes it on the way to the file, so `>` measures the
shell's encoding pipeline rather than the tool's bytes — and this task's whole subject is bytes.
*Rejected: PowerShell redirection*, which would have produced a clean-looking comparison of something
other than what was asked for.

**D2 — The Linux clone goes on ext4, from the commit, not `/mnt/c`.** T-049's D1 for its reason, plus
one of this task's own: running the commands against the Windows working tree from inside Linux would
exercise **one** checkout twice, so any difference caused by what a clone receives would be invisible.
*Rejected: running against `/mnt/c`* — cheaper, and it answers a question this task is not asking.

**D3 — WSL2 is named as what it is, and the record does not upgrade it.** It is a Linux kernel with
Ubuntu's own `python3`, which is what criterion 1 asks for; T-049 set the precedent. What it cannot
stand in for is macOS, and criterion 4 already requires that to be stated rather than implied.

**Planned outputs**
- No files. The output is recorded evidence in §3, plus any finding it turns up, which becomes its own
  task rather than a fix here (§1 Scope).

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → planned | Seven steps. The route is [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)'s — a clone on ext4 inside WSL2 Ubuntu — so this task inherits a proven setup rather than deciding one, and **D3** names WSL2 as what it is instead of letting "Linux" do work the record cannot support. Two decisions are about the measurement itself and both exist because the subject is bytes: **D1** captures through `cmd /c` because PowerShell's `>` decodes and re-encodes a native command's output, so it would compare the shell's pipeline rather than the tool's; **D2** clones rather than reading the Windows tree from Linux, since one checkout read twice cannot show a difference in what a clone receives. Step 5 splits the generated artifact from the console output because only the artifact is covered by `WritesTheSameBytesEverywhere` — folding them together would let the tested half hide the untested one. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every open task carrying `work_package: v0.5` at that date, through all four phases. It **does not generalise** to `v0.6`, to unlabelled work, or to anything raised after it.
| 2026-08-07 | → specified | Answered: Linux, macOS untested and said so. The **Outcome** was amended to match, because it named both platforms and would otherwise have promised what the answer declines to do; the acceptance criteria needed no change, since criterion 1 asks for at least one non-Windows platform and criterion 4 requires the result recorded either way. The macOS gap is named rather than waved through — filename normalisation and default case-insensitivity are a class Linux cannot stand in for, so R-20's third platform stays a claim until someone runs it. |
| 2026-08-05 | → proposed | Raised by T-002's review. The criterion was not met as written and is carried here rather than reinterpreted as "the mechanism is right". |
