---
id: T-020
title: Confirm byte-identical output on macOS and Linux
type: analysis
status: done
phase: review
parent: T-002
blocked_by: []
related: [T-006, T-049, T-132]
work_package: M5
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

Absolute paths are redacted, as [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)
redacted its own: the capture directories are under this machine's temp tree, which is the class the
pre-publish check exists to catch.

### The two sides

```text
                Windows                          Linux
platform        Windows 11                       Linux 6.18.x-microsoft-standard-WSL2
filesystem      NTFS                             ext4
interpreter     CPython 3.12.10                  CPython 3.14.4
tree            clone of d611dc2, 0 dirty        clone of d611dc2, 0 dirty
```

**The interpreters are not the same version, and that is stated rather than hidden.** It makes the
run a weaker isolation of the platform variable and a stronger result: what follows held across two
CPython minor versions as well as across two operating systems. Making them match would have meant
installing an interpreter inside the distribution, which T-049's D3 rules out for good reason — the
value of a stock Ubuntu is that it is stock.

### Steps 1–4 — the captures, and the trap in the first attempt

Six captures per side, in a fixed order, each the raw stdout+stderr bytes of one command:
`context T-020`, `index`, `check` on the repository, then `context ISSUE-0002`, `index`, `check` on
`tests/fixtures/alt-project`. The fixture is a real second configuration — prefix `ISSUE-`, tasks in
`issues/`, four-digit ids — so this is not the same project measured twice.

**The first attempt compared the Windows *working tree* against the Linux *clone*, and it produced a
content difference that has nothing to do with the platform:**

```text
windows working tree   Scope  48 document(s) not read: a clone would not receive them
linux clone            Scope   0 document(s) not read: a clone would not receive them
```

Every other counted quantity on that line was already identical. The `Scope` line is
[T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s, and it was answering exactly
what it was built to answer: a clone receives everything a clone has, so `0` is correct there, and
`48` is correct in a working tree carrying gitignored `control/`. The measurement was wrong, not the
tool. **A working tree is not a clone, and comparing one against the other measures the difference
between them.** So the Windows side was re-taken from a clone of the same commit, and both sides then
read `Scope 0`. Recorded because a session that had not looked would have reported a content
difference across platforms that does not exist.

### The result, clone against clone

```text
1-repo-context.txt         DIFFERS    win 798 B / linux 782 B; CR win 16 / linux 0; equal after CR strip: YES
2-repo-index.txt           DIFFERS    win  47 B / linux  46 B; CR win  1 / linux 0; equal after CR strip: YES
3-repo-check.txt           DIFFERS    win 367 B / linux 364 B; CR win  3 / linux 0; equal after CR strip: YES
4-alt-context.txt          DIFFERS    win 456 B / linux 440 B; CR win 16 / linux 0; equal after CR strip: YES
5-alt-index.txt            DIFFERS    win  45 B / linux  44 B; CR win  1 / linux 0; equal after CR strip: YES
6-alt-check.txt            DIFFERS    win 352 B / linux 349 B; CR win  3 / linux 0; equal after CR strip: YES
A-repo-index-artifact.md   IDENTICAL  (31712 bytes)
B-alt-index-artifact.md    IDENTICAL  (762 bytes)
```

**Two answers, and they are different answers.**

**Step 5 — the generated artifacts are byte-identical.** Both of them, on both projects, at 31712 and
762 bytes: the same SHA-256 on NTFS and on ext4. T-002's mechanism argument — explicit `newline="\n"`
on every write, no `os.linesep`, separators normalised to `/` — is now a measurement. This is the
half the criterion was written about, and it holds.

**Steps 4 and 6 — console output is not byte-identical, and the whole of the difference is the line
terminator.** Every one of the six captures differs, every one is byte-for-byte equal after `\r` is
removed, and the CR counts are exactly the line counts. No content byte differs anywhere:
`check`'s eleven counts, `context`'s derived children and dependents, `index`'s written-file line —
all identical. The cause is one line: `cli.py` reconfigures `sys.stdout` to UTF-8 and does not set
`newline`, so Python's text layer keeps translating `\n` to `\r\n` on Windows. The project's own
`newline="\n"` discipline is applied to files and not to the console.

**Characterising it on the command that is consumed by scripts.** Out of the criteria's three
commands, but the finding is only actionable if its consequence is known, so `list` was captured the
same way. The trailing bytes of the last row:

```text
windows   \t   -  \r  \n
linux     \t   -  \n
```

[T-022](T-022-filtered-task-listing-for-scripts.md) built `list` as *filtered task listing for
scripts*. A script splitting a row on tabs gets a final field of `-\r` on Windows and `-` on Linux.
That is the finding's cost, and it is why this is a fix task rather than a note.

### Step 7 — what this does to T-002

T-002's assumption is annotated, not rewritten (METHOD rule 5): its record is correct about the past,
and a log row on it now says what the measurement found. Half of its criterion is met and half is
not, which is a more useful sentence than either "confirmed" or "failed".

**Decisions & assumptions**

- **The difference is reported, not fixed here.** §1 Scope says so, and this task would otherwise be
  the thing it exists to prevent: an analysis task that quietly changes behaviour and then reviews
  its own change. Raised as [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md).
  — 2026-08-11
- **macOS remains unverified, and the record says so in those words.** Criterion 1 asked for at least
  one non-Windows platform and criterion 4 for the result either way; neither is satisfied by
  implying that Linux covered it. The two classes macOS can expose and Linux cannot — filename
  Unicode normalisation and default case-insensitivity — are unchanged from the 2026-08-07 answer.
  — 2026-08-11
- **WSL2 is what was run, and the record does not call it anything else.** It is a Linux kernel with
  Ubuntu's own `python3`; what it is not is a separate machine. **D3.** — 2026-08-11

**Outputs produced**
- No files. The evidence is the tables above, and the finding is
  [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md).

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The three commands run on at least one non-Windows platform, at a named commit | met | Linux 6.18.x (WSL2 Ubuntu, ext4), commit `d611dc2`, both on this repository and on `tests/fixtures/alt-project` — a genuinely different configuration rather than the same project twice. |
| `index` output compared byte for byte with the Windows run; any difference reported rather than normalised away | met | Two comparisons, because `index` has two outputs. The **artifact** is identical on both projects (31712 and 762 bytes, same SHA-256). The **console line** differs by one CR and is reported as such, not folded away. |
| Console output of `context` and `check` compared as bytes, not read and judged equivalent | met | Compared with `cmp`, which is why the answer is "differs at byte 73" rather than "looks the same". All six captures differ; all six are equal after stripping CR. |
| The result recorded either way — a confirmation is as much the outcome as a difference is | met | Both were recorded, and they point opposite ways: the artifacts confirm T-002's mechanism, the console does not. §3 also records the **discarded first attempt**, whose apparent content difference was the working tree, not the platform. |
| T-002's recorded assumption is marked closed, or replaced by what was actually found | met | Annotated by a log row on [T-002](T-002-implement-the-core-cli-context-index-check.md) — the assumption is half closed and half replaced, and its record is left correct about the past. |

**Child fix tasks raised**
- [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md) — the console line
  terminator. It is the entire content of the failing half, and §1 Scope reserved fixing for a task
  of its own.

**Verdict.** All five criteria met. The task closes with a result that is **not** a clean
confirmation, and that is the outcome rather than a shortfall: R-20's claim holds for what taskmd
writes and does not hold for what it prints. macOS stays unverified and named.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | Reviewed against all five criteria; **all five met, none carried**, and the answer is split rather than clean. The generated artifacts are byte-identical on NTFS and ext4, on both projects — T-002's mechanism argument is now a measurement. Console output is **not**: all six captures differ, all six are equal after stripping CR, and no content byte differs anywhere. So R-20 holds for what taskmd writes and fails for what it prints, which is a more useful sentence than either verdict alone. One child raised, [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md), because §1 Scope reserved fixing. macOS is still unverified and the record says the words. T-002 is annotated rather than rewritten, per METHOD rule 5. |
| 2026-08-11 | → in_progress | All seven steps taken, and the run's own method had to be corrected mid-measurement. The first attempt compared the Windows **working tree** against the Linux **clone** and produced a content difference — `Scope 48` against `Scope 0` — that is not a platform difference at all: [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s line was correctly reporting that a clone receives everything a clone has, while a working tree carries gitignored `control/`. Re-taken from a clone on both sides, both read `Scope 0` and every one of the eleven counts matched. Recorded because reporting the first result would have invented a cross-platform content difference. Two further honesties: the interpreters are **not** the same version — CPython 3.12.10 against 3.14.4 — which weakens the isolation and strengthens the result, and matching them would have meant installing into the stock Ubuntu that T-049's D3 keeps stock; and `list` was captured beyond the three commands the criteria name, because a finding is only actionable once its cost is known, and its cost is a trailing `\r` on the last field of every row of the command built for scripts. |
| 2026-08-11 | → planned | Seven steps. The route is [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)'s — a clone on ext4 inside WSL2 Ubuntu — so this task inherits a proven setup rather than deciding one, and **D3** names WSL2 as what it is instead of letting "Linux" do work the record cannot support. Two decisions are about the measurement itself and both exist because the subject is bytes: **D1** captures through `cmd /c` because PowerShell's `>` decodes and re-encodes a native command's output, so it would compare the shell's pipeline rather than the tool's; **D2** clones rather than reading the Windows tree from Linux, since one checkout read twice cannot show a difference in what a clone receives. Step 5 splits the generated artifact from the console output because only the artifact is covered by `WritesTheSameBytesEverywhere` — folding them together would let the tested half hide the untested one. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: M5`, through all four phases — including a task raised into M5 *by* that work, which is a M5 task and not a fresh grant. It **does not generalise** to `M6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a M5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-07 | → specified | Answered: Linux, macOS untested and said so. The **Outcome** was amended to match, because it named both platforms and would otherwise have promised what the answer declines to do; the acceptance criteria needed no change, since criterion 1 asks for at least one non-Windows platform and criterion 4 requires the result recorded either way. The macOS gap is named rather than waved through — filename normalisation and default case-insensitivity are a class Linux cannot stand in for, so R-20's third platform stays a claim until someone runs it. |
| 2026-08-05 | → proposed | Raised by T-002's review. The criterion was not met as written and is carried here rather than reinterpreted as "the mechanism is right". |
