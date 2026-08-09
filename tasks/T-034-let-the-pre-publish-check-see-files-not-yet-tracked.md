---
id: T-034
title: Let the pre-publish check see files not yet tracked
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-013, T-018, T-006, T-035]
work_package: v0.1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-06
updated: 2026-08-06
deliverables:
  - CLAUDE.md
---

# T-034 — Let the pre-publish check see files not yet tracked

## 1. Specify

**Outcome**
The pre-publish leak check in `CLAUDE.md` examines every file a push would send, including files
created in the session that is about to publish — instead of only those git already tracks.

**Why this one**
Raised as **F-8** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 1 and 3. Found in that audit's own step 10, while running the check on its own output.

`CLAUDE.md` justifies the check's use of `git ls-files` this way: *"it sees exactly what a push would
send, so anything gitignored is out of scope by construction."* The second half is true. The first
half is not: `git ls-files` lists **tracked** files, and a file created but not yet staged is not one.
Measured during the audit, immediately after it had written seven new task files:

```
tracked only:      83 files
tracked+untracked: 90 files
```

None of the seven new task files was visible to the documented command. The check printed nothing,
and would have printed nothing whether they were clean or not.

**The blind spot lines up exactly with the known failure mode.** `CLAUDE.md` also says: *"Run it
last, after the task record is written — not before. The check reads the tracked tree, so it cannot
see a file that does not exist yet, and the text most likely to trip it is the write-up of a task
*about* the check."* That instruction is right about the ordering and stops one step short: writing
the record makes the file exist, but it does not make it *tracked*, so running the check afterwards
still does not read it. Both prior leaks — [T-013](T-013-quarantine-local-only-information-behind-gitignore.md)
and [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) — were in a task write-up,
which is precisely the file class that is invisible when it is newest.

**What the audit ran instead**, which is one flag and produced a clean result over all 90 files:

```bash
git ls-files --cached --others --exclude-standard ':!tests/fixtures/leak-check/'
```

`--others --exclude-standard` adds untracked-but-not-ignored files, so gitignored content stays out
of scope by construction exactly as before — the property `CLAUDE.md` relies on is preserved.

**Requirements served**
R-23 (`docs/SCOPE.md`), and §9's *"No personal, client or machine data anywhere in the repository"*,
which [T-006](T-006-package-document-and-publish.md) must be able to certify.

**Scope**
- In: the command in `CLAUDE.md` §*The pre-publish check*, and the sentence justifying `git ls-files`.
- In: the two-run proof arrangement, which must keep working — with the exclusion the tree prints
  nothing, without it the output is exactly the fixture's five lines.
- Out: the regex itself, its four classes, and the two deliberate limits. All were settled in T-013
  and T-018 and none is affected.
- Out: `tests/fixtures/leak-check/samples.txt`, which is correct and is the thing that proves the
  pattern.
- Out: making this a CLI command. It stays a grep — `docs/SCOPE.md` non-goal 11, reaffirmed in T-013
  and unchanged by the 2026-08-05 amendment.

**Inputs**
`CLAUDE.md` §*Publishing constraints* and §*The pre-publish check*,
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md),
[T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-8.

**Acceptance criteria**
- [ ] The documented command reads files that exist but are not yet staged; shown by the file count
      it covers, not by it printing nothing
- [ ] **Shown catching a leak in an untracked file**, per R-16 and `CLAUDE.md` *Verifying* — the
      current command's failure is silent, so a fix verified only by a clean run proves nothing at
      all. Use a throwaway file outside the fixture, and delete it
- [ ] Gitignored content is still out of scope by construction, so `control/` and the live handoff
      state are still never read
- [ ] The two-run proof still holds: with the exclusion, nothing; without it, exactly the fixture's
      five lines
- [ ] `CLAUDE.md`'s sentence about what `git ls-files` sees is true of the command beside it
- [ ] No matched line is quoted into this task's record — describe and point at the fixture, per
      `CLAUDE.md` and the lesson T-013 and T-018 each paid for once

**Open questions**
- None. The fix is known and was executed once during the audit; what remains is making it the
  documented command and proving it by making it fail.

## 2. Plan

**The fix is one flag; the work is the proof.** Steps 1, 2 and 5 are the task; step 4 is the edit
they justify. A plan weighted the other way would have planned the easy half.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Establish what each command actually reads, before changing anything.** Run the documented command's file listing and the flagged one over this working tree, count both, and diff the lists. Four properties decide whether the rest of the plan is the right plan: the added files are untracked-and-not-ignored only; `control/` and `.handoff/HANDOFF.md` are in **neither** listing; the `':!tests/fixtures/leak-check/'` pathspec still applies to the `--others` set as well as the cached one; and no path is listed twice. | Two file counts and their difference, plus each of the four properties confirmed or refuted, recorded in §3 |
| 2 | **Make the fix fail-and-catch, before it is documented.** Create one throwaway file **outside** `tests/fixtures/leak-check/`, untracked, holding a fabricated specimen of each of the four classes. Run the currently-documented command over the tree, then the flagged one. Delete the file. | A recorded result in §3: the documented command reports **nothing** over that file, the flagged one reports it — stated as hit count and file name only. No matched line is reproduced |
| 3 | **Find every other place this command or its "what `git ls-files` sees" justification is written, and classify each.** Two kinds, and only one may be touched: a **live instruction** someone would follow (must be corrected) versus a **historical record** of what was run at the time (must not be — rewriting it destroys the evidence). Known candidates: `CLAUDE.md`, T-013 §3's `git ls-files`-over-a-directory-walk decision, T-018 §3's two-run transcript, T-026 step 1's coverage denominator. | A verdict per entry, in §3 — including "none besides `CLAUDE.md`", if that is the answer |
| 4 | **Amend `CLAUDE.md` §*The pre-publish check*.** Three edits, not one: the command gains `--cached --others --exclude-standard` and keeps `-z` and the exclusion pathspec, since `xargs -0` and the two-run proof both depend on them; the `git ls-files` justification sentence is made true of the command beside it; and the *"Run it last"* paragraph's reason — *"the check reads the tracked tree"* — is corrected. The **instruction** there survives the correction and must not be lost with the reason: a file that does not exist still cannot be read. | The amended section of `CLAUDE.md`, carrying one command and no sentence describing a set the command does not read |
| 5 | **Re-run the two-run proof against the amended command.** With the exclusion, the tree prints nothing; without it, exactly the fixture's five lines. Report run 1 with the file count it covered — "prints nothing" is what the old command did while reading none of them, so silence alone is not the evidence. | A recorded result in §3: run 1 silent over *n* files, run 2 exactly five hits, all in `tests/fixtures/leak-check/samples.txt`. Counted and pointed at, never quoted |

Step 1 is first because it is the only step that can invalidate the others: if `--exclude-standard`
did not hold gitignored content out, or the pathspec did not reach the `--others` set, this is a
different fix. Step 2 precedes the edit deliberately — the "before" state has to be the command
`CLAUDE.md` *documents*, or the demonstration is of nothing.

**Deliverable shape — decided here.** The deliverable is an edit to the existing section of
`CLAUDE.md`: one command, run by a person, at the same place in the same document. Rejected:

- **A `taskmd` subcommand, or a `scripts/` wrapper.** `docs/SCOPE.md` non-goal 11, reaffirmed in
  T-013 and restated in this task's own scope. Unchanged by the 2026-08-05 amendment, which carved
  out a task listing.
- **Two commands, one over tracked files and one over untracked.** It doubles what has to be run
  before a push and creates a second place the regex must be kept in step with. Worse, a reader who
  runs only the first is back in exactly today's blind spot, which is the failure being removed.
- **`git add -A` first, then the command unchanged.** It mutates the index as a side effect of a
  read-only check, and it makes the check's answer depend on the state it just created.
- **The short form `-co --exclude-standard`.** The line exists to let a reader see what it covers;
  `-co` hides precisely the thing this task is about.

**Not in this task.** The regex, its four classes and its two deliberate limits (settled in T-013 and
T-018), and `tests/fixtures/leak-check/samples.txt`, which is correct and is what proves the pattern.
Step 3 may find a false sentence in a *task* record; per METHOD §5 that is raised, not fixed here.

**Output paths**

- `CLAUDE.md` — the amended §*The pre-publish check*

The `deliverables:` front-matter stays empty until `implement`, as in T-019: `check` validates that
every declared path exists, so declaring one now would make this project fail its own validator for
the length of the plan.

## 3. Implement

Worked in plan order, with one documented deviation: **step 1's measurements were taken with step
2's specimen already present.** On a clean tree the two commands are indistinguishable — 91 files
each, empty diff — because this repository had no untracked-and-not-ignored file at the moment step 1
ran. Measuring first and finding "no difference" would have been a true number and a false
conclusion, so the specimen was created before step 1 was recorded rather than after.

**Decisions & assumptions**
- **The long flag form, not `-co`** — 2026-08-06. `--cached --others --exclude-standard` says what it
  covers to a reader who has not memorised the short flags, and the whole defect being fixed is that
  nobody noticed what the line covered. Rejected: `-co --exclude-standard`, which is the same command
  and hides exactly the thing this task is about.
- **The *"run it last"* instruction was kept; only its reason was corrected** — 2026-08-06. The old
  reason — *"the check reads the tracked tree"* — was the false half. The instruction outlives it: a
  file that does not exist still cannot be read, so writing the record before running the check is
  still required. What the fix removes is the second, unstated gap — that writing the record made the
  file *exist* without making it *visible*.
- **`CLAUDE.md` points at this task rather than restating its measurement** — 2026-08-06. The 83-vs-90
  figure has one home, in §1 above. A first draft of the edit copied it into `CLAUDE.md`; that is a
  second copy of a fact, which is the drift this plugin exists to remove. Rejected on the project's
  own design rule.
- **The specimen was written with a file-writing tool, not through the shell** — 2026-08-06. Forced,
  not chosen: see the finding below.

**Found while verifying — the specimen was silently damaged in transit**

The first specimen was created through the shell, and the UNC class did not match. The regex was not
at fault. One leading backslash was eaten before the shell saw the text, so the fabricated UNC line
arrived one character short and was no longer a UNC path. A quoted heredoc made no difference —
`od -c` on the stored line is what identified it, by showing a byte count that did not match the
text as written. Written instead by a tool that does not shell-escape, all four classes matched.

This is the specific way this task's evidence could have been wrong while looking right: the run
would have reported three of four classes caught, and the natural reading is "the check has a hole in
its UNC branch" — a false defect in a pattern that was settled in T-013 and is not in this task's
scope. Escalated rather than absorbed, below.

**Escalated, not fixed here** (METHOD §3.3)
- [T-035](T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) — `CLAUDE.md` tells a
  future author to prove the check by making it fail, and does not warn that the shell can damage
  the specimen on the way in. That is a gap in the project's instructions, found here; the sentence
  belongs beside the check, and adding it here would be fixing a finding where it was found.

**Outputs produced**
- `CLAUDE.md` — §*The pre-publish check*: the command's three new flags, the corrected `git ls-files`
  justification, and the corrected reason under *"Run it last"*

**Verification**

*Step 1 — what each command reads.* With one untracked, not-ignored file present:

```
documented (cached only):   91 files
flagged (cached+others):    92 files
added by the flags:         exactly the one untracked file
duplicate paths:            0
control/ or live handoff:   0 in either listing
```

`control/` (1 entry) and ten `.handoff/processed_*` files exist on this tree, so their absence is the
exclusion working, not the paths being absent. The `':!tests/fixtures/leak-check/'` pathspec reaches
the `--others` set as well as the cached one: the fixture is absent from the flagged listing with the
exclusion and present without it. All four properties the plan named hold.

*Step 2 — shown catching a leak in an untracked file.* One throwaway file at the repository root,
outside `tests/fixtures/leak-check/`, holding a fabricated specimen of each of the four classes plus
one line of safe forms. Confirmed untracked and not ignored (`git check-ignore` declines it):

```
RUN A  documented command  -> 0 hits
RUN B  flagged command     -> 4 hits, all in the throwaway file
```

Per-class, the four branches matched one distinct line each and the safe-forms line matched none.
**Run A is the failure this task was raised for**, reproduced deliberately: a file carrying four
leaks, and the documented command silent. The file was deleted; `git status` afterwards shows only
this task and the generated index.

*Step 3 — other copies.* Six other places name `git ls-files`; **one** was a live instruction and it
is the one that changed.

| Where | Verdict |
| :--- | :--- |
| `CLAUDE.md` §*The pre-publish check* | Live instruction — corrected |
| T-013 §3, `git ls-files` over a directory walk | Historical decision, and still true: the fix keeps `git ls-files`. Untouched |
| T-013 §4, the review row | Historical result. Untouched |
| T-018 §1 criterion and §3 transcript | Historical record of what was run then. Untouched |
| T-026 step 1 and its coverage table, "84 tracked files at the time" | Historical, and the measurement F-8 was raised from. Untouched |
| `docs/SCOPE.md` non-goal 11 | Says the check stays a grep; says nothing about which files it reads. Unaffected |

Rewriting any of the five would have destroyed the evidence this task was raised from.

*Step 5 — the two-run proof, against the amended command.*

```
RUN 1  with the exclusion, over 91 files a push would send   -> nothing
RUN 2  without the exclusion, over 92 files                  -> 5 hits,
       all in tests/fixtures/leak-check/samples.txt
```

Run 1 is reported with the file count it covered, because "prints nothing" is precisely what the
broken command did while reading none of them. No matched line is reproduced anywhere above.

`python -m taskmd check` — `OK - 34 task(s), vocabulary valid, references resolve, no broken links`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Reads files that exist but are not yet staged; shown by the file count it covers, not by it printing nothing | met | 91 files against 92, the difference being exactly the one untracked file, with the diff shown rather than the counts alone. The criterion's own guard is what caught the first attempt: measured on a clean tree the two commands are identical, and that number would have been true and worthless — recorded as `implement`'s one deviation from plan order |
| **Shown catching a leak in an untracked file**, per R-16; throwaway file outside the fixture, deleted | met | Documented command 0 hits, amended command 4 hits, on the same tree with the same file present. Both halves matter: the amended command catching it proves the fix, the documented command missing it reproduces the defect. The file was deleted and `git status` confirms it is gone |
| Gitignored content still out of scope by construction — `control/` and the live handoff state still never read | met | Both are **present on this tree** (`control/` with 1 entry, 10 `.handoff/processed_*`), so 0 occurrences in the listing is the exclusion working rather than the paths being absent. Review checked the distinction the criterion depends on; `implement` had already recorded it |
| The two-run proof still holds: with the exclusion nothing, without it exactly the fixture's five lines | met | Run 1 silent over 91 files, run 2 exactly 5 hits all in `tests/fixtures/leak-check/samples.txt`. Review also checked the property the two runs rest on and which the flags could have broken: the `':!…'` pathspec reaches the `--others` set, not only the cached one |
| `CLAUDE.md`'s sentence about what `git ls-files` sees is true of the command beside it | met | The sentence now names the flags and says what the bare command omits. Judged by reading, which is the weakest evidence in this task — but the sentence's claim is the same claim the four measurements above test, so it is not judged on its own |
| No matched line quoted into this task's record — describe and point at the fixture | met | Checked mechanically, not by reading: the amended command, run last over 92 files after every record here was written, prints nothing. That is the criterion's real test, and running it *last* is what makes it one. The final run is also the fix demonstrating itself on live content — T-035's file was untracked at that moment, so the old command would not have read the record that describes this defect |

**Also checked, beyond the criteria**

- **`check` and the suite.** `OK - 35 task(s), vocabulary valid, references resolve, no broken links`;
  suite 92/92. This repository runs the tool on itself, so a regression in the task files would show
  here.
- **The historical records left alone.** Step 3's five untouched entries were re-read after the edit.
  T-013's decision is the one that could have been wrongly "corrected" — it chose `git ls-files` over
  a directory walk, and that decision is unchanged by this task, which kept `git ls-files` and added
  flags to it.

**Child fix tasks raised**
- none — every criterion is met.

**Raised, not fixed here** (outside these criteria, so not a child fix — METHOD §3.3)
- [T-035](T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) — raised during
  `implement`. `CLAUDE.md` asks a future author to prove the check by making it fail and does not
  warn that the shell can damage the specimen in transit, which produces a false negative that reads
  as a defect in the pattern.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-06 | → done | Review worked; all six criteria met, no child fixes. Two criteria were judged by checking the thing they depend on rather than the thing they say: gitignored content is absent from the listing *while `control/` and ten processed handoffs sit on the tree*, and the exclusion pathspec was shown to reach the `--others` set, which the new flags could have broken without the two-run proof noticing. Criterion 6 is the one that closed itself — the check, run last over a tree that now includes this record, prints nothing. |
| 2026-08-06 | → review | Implemented in plan order with one recorded deviation: the file-count measurement had to be taken with the specimen present, because a clean tree cannot tell the two commands apart and would have returned a true number supporting a false conclusion. The demonstration is the result — the documented command silent on a file carrying four leaks, the amended one catching all four. One thing escalated rather than absorbed: the specimen was damaged in transit the first time it was created, losing a backslash and making a correct branch look broken → T-035. Step 3's sweep found six other mentions of `git ls-files` and changed one; the other five are historical records this task was raised *from*. |
| 2026-08-06 | → planned | Five steps, weighted away from the edit: the command change was already known and written into `specify`, so the plan's work is the proof around it. Two orderings are deliberate — the properties of `--others --exclude-standard` are checked first because a failure there makes this a different fix, and the fail-and-catch demonstration runs *before* the edit so the "before" state is the command `CLAUDE.md` actually documents. One step the specify did not imply: a sweep for other copies of the command, which found candidates in three task records; those are historical evidence and the plan says so rather than leaving the judgement to `implement`. No dependency edge added — nothing must close first. |
| 2026-08-06 | → specified | Agreed by the maintainer as written, with no criterion amended — the specify carried no open questions, so agreement was the only gate. Chosen over T-010 deliberately: the project's own ordering ranks T-010, T-011 and T-003 ahead of this task because each releases T-006, and the maintainer took the cheap task that guards the last check before publication instead. That disagreement between the pointer and the ordering is recorded rather than resolved — it is the second time the ordering's answer has been overridden by hand, which is worth watching if it becomes a pattern. |
| 2026-08-06 | → proposed | Raised as F-8 from the T-026 audit, clauses 1 and 3 — found in that audit's step 10, while running the check over the audit's own output, which is the situation the blind spot is worst in. Measured before being written up: 83 files seen versus 90 that a push would send. Raised rather than fixed in place (METHOD §5), even though the fix is one flag, because a silent gap in the last check before publication is exactly the kind of change that should carry a record of having been proven. |
