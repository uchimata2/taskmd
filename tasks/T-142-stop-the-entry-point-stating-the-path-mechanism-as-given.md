---
id: T-142
title: Stop the entry point stating the PATH mechanism as given
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-054, T-085, T-099, T-161]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-142 — Stop the entry point stating the PATH mechanism as given

## 1. Specify

**Outcome**
`plugin/bin/taskmd` describes how it is reached in terms that are true on the machines where it is
not reached, so the file an adopter opens when the command is missing does not tell them the command
cannot be missing.

**Why this one**
Raised from the htmldeck adopter report, row `O-T2` — the corrected row, whose remaining clause is
this and nothing larger. The comment at the top of the launcher reads, in substance, that the file is
on `PATH` because the harness appends every enabled plugin's `bin/` to the `PATH` it hands the
agent's shell, so there is no install step, no `PYTHONPATH` to set and no path to a cache directory
anyone has to know.

Every clause of that is true of the design and false on at least one real machine, including the one
this project is written on. [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3
step 2 measured why: the harness does write the directory into the shell snapshot, and the snapshot's
`export PATH=` line is truncated mid-value, so sourcing fails and the inherited `PATH` survives. The
defect is the harness's and is filed against the harness. What is left here is that a shipped file
states the mechanism as a guarantee.

**Why the comment rather than the behaviour.** [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md)
already gave the adopter the second way in, and it ships: `SKILL.md` names the condition and the
launcher beside it, and `adopt.md` points at that rather than carrying a copy. So the documentation an
adopter reads is correct, and the file they open when it fails is the one that is not. The two are a
few directories apart and disagree.

**The cost is a real one and it has been paid.** The reporting project wrote its own locator rather
than using the shipped fallback. The obvious implementation of such a locator globs the version
directory and **sorts the paths as text**, which picks `0.5.0` over `0.10.0` at the next minor bump.
They wrote it, found it and fixed it before the report was written: their locator parses the version,
and a self-test in the same file asserts `0.10.0` beats `0.5.0` and `0.9.1`, with a failure message
spelling out that text order would run an older skill than the one installed.

**So nothing about that locator is open, and the general point is the whole of what survives**: an
adopter who believes the mechanism is unconditional, then finds it failing, re-derives a locator
instead of looking for a documented fallback — and the obvious implementation of it is wrong. That is
evidence for this task, not a defect anyone has to chase.

**Requirements served**
R-18 (`docs/SCOPE.md`) — auto-discovery so a clone runs unedited — in the sense T-099 left it: the
promise holds, and the file explaining it does not say what happens when the machine breaks it.

**Scope**
- In: the comment at the top of `plugin/bin/taskmd`, and whether `plugin/bin/taskmd.cmd` says
  anything with the same problem.
- In: whether the file points at the fallback, given that the fallback's one home is `SKILL.md` and
  this project does not keep two copies of a fact.
- Out: the fallback itself, which T-099 settled and shipped.
- Out: fixing the harness, which T-054 settled is not taskmd's.
- Out: adding any detection or automatic re-route. T-099 decided the reader switches, not the tool.

**Inputs**
- `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`.
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 2 — the mechanism
  and the truncation.
- [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) — the fallback, and D1 on
  why it names the launcher beside `SKILL.md` rather than this file.

**Acceptance criteria**
- [x] The comment no longer states as unconditional a mechanism known to fail, and says what the
      reader does when it has
- [x] It does not become a second copy of the fallback — the one home stays `SKILL.md`
- [x] Both entry points are checked, not only the one the report named
- [x] The launcher still runs unchanged from both shells, shown rather than assumed
- [x] `check` and the suite are green, and no path from any machine appears in the file

**Open questions**
- ~~**Can a shipped file point at `SKILL.md` at all?**~~ **Answered at `specify`, 2026-08-16: yes,
  and the file already does.** [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)
  forbids a reference from inside `plugin/` to a path **outside** it;
  `../skills/taskmd/SKILL.md` is inside. The question assumed the pointer might resolve in one
  shipped shape and not the other, and that premise is wrong in a way only reading the file shows:
  its own last line is `exec sh "$here/../skills/taskmd/taskmd.sh"`, and the `.cmd` twin's is
  `%~dp0..\skills\taskmd\taskmd.ps1`. **Each shim is inoperable unless that directory is beside it**,
  so a pointer with the same reach resolves in exactly every shape where the file can run at all —
  there is no shape in which it ships broken, because there is no shape in which it ships alone.
  T-083's self-contained skill folder is the shape where `bin/` is **absent**, not the shape where
  it is present and dangling.

  *Rejected: state the condition and name no path.* It was the draft's own guess and it is the
  cheaper answer, but it leaves the reader who opened this file exactly where they started — knowing
  the mechanism can fail and not where the way in is. The reason to prefer it was a resolution risk
  that does not exist.

  Citing a task id from inside the plugin is separately established practice rather than a judgement
  taken here: `taskmd/cli.py`, `taskmd/schema.py`, `taskmd/defaults/config.md` and
  `docs/bindings/local-markdown.md` all do it, and all post-date T-064.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Settle the open question by reading what the two shims **already** reach, rather than reasoning about shipped shapes | The answer recorded in §1 |
| 2 | Read `SKILL.md`'s fallback paragraph, so the new comment can point at it without restating it | Its wording, quoted nowhere |
| 3 | Rewrite the comment in `plugin/bin/taskmd`: mechanism as intent, the failure as observed, the pointer | `plugin/bin/taskmd` |
| 4 | Judge `plugin/bin/taskmd.cmd` on the same question and act on the answer, whichever way it goes | `plugin/bin/taskmd.cmd`, or a recorded finding of nothing |
| 5 | Run both shims, from both shells, and compare their output | The two runs below |
| 6 | Run the suite and `check`, and scan both files for a machine path | Their output below |

Step 1 is first for the sequencing rule: if the pointer could not resolve, steps 3 and 4 would be
different steps, so the cheapest thing that could invalidate the plan goes at the front.

## 3. Implement

**`plugin/bin/taskmd` — what the comment said, and says now.** The old three lines asserted the
mechanism flatly (*It is on PATH because the harness appends…*). The replacement keeps the design,
demotes it from guarantee to intent, records the observed failure with its cause and its owner, and
points once:

```
# That is the design and not a guarantee, and this comment used to state it as one - which is the
# worst place for it, because a reader who opens this file has usually got here by the command not
# being found.
...
# When it has failed, there is a second way in that does not depend on PATH at all. It is stated
# once, in ../skills/taskmd/SKILL.md, and deliberately not repeated here - two copies of it would
# drift, and the one an adopter is pointed at is that one.
```

**`plugin/bin/taskmd.cmd` did not carry the fault, and still needed a line.** Its prose never states
the harness mechanism as given — it explains `PATHEXT` and why there are two files, both true. So on
the literal question the scope asks, the answer is *no, it says nothing with the same problem*. But
the outcome this task is for is about **the file an adopter opens when the command is missing**, and
on Windows that file is this one. It pointed at nothing. Four lines added: the mechanism is intent
not guarantee, the twin carries why, and the way in is `..\skills\taskmd\SKILL.md`.

**Both shims run unchanged, from both shells** — 2026-08-16, same two rows, exit 0 from each:

```
$ sh plugin/bin/taskmd list --open --limit 2
T-108	proposed	M6	specify	Support a project moving its tasks from local files to GitHub Issues	-
T-142	proposed	M6	specify	Stop the entry point stating the PATH mechanism as given	-
exit=0

PS> .\plugin\bin\taskmd.cmd list --open --limit 2
T-108	proposed	M6	specify	Support a project moving its tasks from local files to GitHub Issues	-
T-142	proposed	M6	specify	Stop the entry point stating the PATH mechanism as given	-
exit=0
```

```
264 passed, 3 skipped, 6 subtests passed
OK - 160 task(s), ... 2353 front-matter value(s)          exit=0
```

A scan of both files for a drive letter, either common home-directory prefix, a mount prefix, a
UNC prefix or this machine's user name returns nothing. Every path in either file is relative.

**What the green suite does and does not cover here — checked rather than assumed.**
`tests/test_runtime.py` reads both shims twice, and the two readings are not the same:

- `test_every_entry_point_produces_what_the_module_produces` **executes** each entry point and
  compares its output to `python -m taskmd check`. That is a real reader, and it is the suite's own
  evidence for the *still runs unchanged* criterion — independent of the two manual runs above.
- `test_no_entry_point_names_a_command_a_flag_or_a_field` strips every comment line before
  asserting, by an explicit decision recorded there: *a launcher's body is what carries logic; its
  prose is allowed to say anything, and does.*

So **nothing in the suite reads the prose this task changed.** The claim it now makes could go false
again, exactly as the old one did, and every test would stay green. That is not a defect in this
change and it is not fixed here — it is [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md).

**Decisions & assumptions**

- **The comment names `../skills/taskmd/SKILL.md`** — 2026-08-16, argued in §1's answered question.
  *Rejected:* stating the condition and naming no path, which was the draft's guess and leaves the
  reader stranded at the moment the file is opened.
- **`taskmd.cmd` gets the pointer although it never carried the fault** — 2026-08-16. *Rejected:*
  recording *checked, nothing to do*, which is the literal reading of the scope line and would have
  shipped a fix that works only for readers on the platform the report came from. The scope admits
  the file for a judgement; the judgement went the other way than expected, and this is the widening
  recorded rather than taken silently.
- **The fallback itself is not repeated in either shim** — 2026-08-16. Both name `SKILL.md` and stop.
  The launcher command differs per platform and `SKILL.md` already carries both forms, so a copy here
  would be two copies, not one.
- **The pointer is left without a test** — 2026-08-16, raised as T-161 instead. *Rejected:* adding the
  test inside this task, on T-160's precedent of giving a citation a reader. What decided it against
  is the standing authorisation, which covers these four tasks and explicitly not what they raise —
  and the guard is the same class T-139 is about to generalise, so writing a fifth bespoke one the
  day before that is the mistake T-139 exists to stop.

**Outputs produced**
- `plugin/bin/taskmd` — the rewritten header comment.
- `plugin/bin/taskmd.cmd` — four lines naming the condition and the pointer.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The comment no longer states as unconditional a mechanism known to fail, and says what the reader does | met | Read off the file. *It is on PATH because…* is gone; the mechanism is stated as design, the failure as observed with its cause and its owner (T-054), and the next step named. |
| It does not become a second copy of the fallback — the one home stays `SKILL.md` | met | Neither shim names `taskmd.sh` or `taskmd.ps1` as the way in, nor any command form. Both name `SKILL.md` and stop. Judged by reading; see the row below on what checks it. |
| Both entry points are checked, not only the one the report named | met | Checked, and the answer differed from the expected one: `.cmd` never carried the fault. It was still changed, because the outcome is about the file a stranded reader opens and on Windows that is `.cmd`. Recorded as a decision with its rejection. |
| The launcher still runs unchanged from both shells, shown rather than assumed | met | Two ways. Manually from `sh` and from PowerShell — identical two rows, exit 0 each. And by the suite, which **executes** both shims and compares to `python -m taskmd check`. |
| `check` and the suite are green, no machine path in the file | met | `264 passed, 3 skipped`; `check` exit 0; the path scan returns nothing. **With one honest limit**: every entry-point test strips comments by design, so the green suite is evidence for the row above and for nothing else in this table. The three prose criteria are judged by reading, and have no reader → T-161. |

**Child fix tasks raised**
- [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md) — the pointer this task wrote has
  nothing reading it, which is the condition that let the old claim go stale unnoticed.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | — | **Typographic only, no claim changed.** §3 listed the leak check's own home-directory patterns literally while reporting that a scan found nothing, so the sentence asserting cleanliness was itself two of the hits — `docs/PUBLISHING.md` §6 names this exact failure and says to describe rather than paste. The patterns are now described. Applied by [T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md). |
| 2026-08-16 | → done | All five criteria met; one child raised. **The open question's premise was wrong**, and reading the file settled it in one line: each shim already `exec`s into `../skills/taskmd/`, so it cannot ship without that directory and a pointer there cannot dangle. The task was `xs` and the two surprises were both about reach rather than about the comment. `taskmd.cmd` **did not** carry the fault the report named and was changed anyway, because the reader this task is for is the one whose command is missing, and on Windows that reader opens `.cmd` — recorded as a widening with its rejection. And the suite reads these two files in two different ways, only one of which is evidence for anything here: it **runs** both shims, and it **strips** every comment before asserting, so the prose this task exists to correct has no reader at all. That is T-161 and not a caveat in a paragraph. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): the maintainer asked for this task's full lifecycle**, given 2026-08-16 as the subject of a handoff — *work all 4 from the list, full lifecycle*. The list is the four unblocked `fix` tasks named that day: [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md), [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md), [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md). It covers those four and **nothing else** — not the five `decision` tasks beside them on the same list, and not anything these four raise. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. |
| 2026-08-15 | (no change) | **Corrected**, from the reporter's follow-up on the same thread. §1 said their locator sorts the version directory as text and treated that as live. It is not: they hit it, fixed it and self-tested it before the `O-T2` row was written, and the row did not say so. Their locator parses the version and asserts `0.10.0` beats `0.5.0`. Our disposition comment repeated the error, listing *the version sort goes with them* as one of three things that were theirs to act on; that comment is public and uncorrected, and this row is where the correction lives. Nothing else changes: `O-T2`'s surviving clause is what this task was raised for, we accepted it correctly, and it stands as evidence that re-deriving this locator is error-prone rather than as an open defect. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T2`, which is the row the reporter corrected: it originally pointed at T-085 and would have sent this project hunting a packaging defect that does not exist. The correction is right — the launcher runs, the harness does emit the directory, and the truncation is upstream — and what survives it is small and real. `medium` because the fallback already ships, so nobody is blocked; the file is simply wrong where a reader meets it at the worst moment. `xs` because it is a comment. Two facts recorded here rather than left for `specify`: the report's version-sorting locator bug is the reporting project's, not a defect to copy, and the open question below may end with the comment naming no path. |
