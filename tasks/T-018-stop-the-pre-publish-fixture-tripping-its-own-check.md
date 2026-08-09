---
id: T-018
title: Stop the pre-publish fixture tripping its own check
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-013]
work_package: v0.1
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-05
updated: 2026-08-05
deliverables:
  - tests/fixtures/leak-check/samples.txt
  - tests/fixtures/README.md
  - CLAUDE.md
---

# T-018 — Stop the pre-publish fixture tripping its own check

## 1. Specify

**Outcome**
The pre-publish check in `CLAUDE.md` prints nothing on a clean tracked tree, while the evidence that
it was proven by failing is still readable — and no tracked file contains a real absolute local path.

**Why this one**
T-013 proved the check by running it against a fixture with one line per leak class, then pasted
that fixture verbatim into `tasks/T-013-…md` §4 as its evidence. Two things follow, and the second
is worse than the first:

1. **The check now always prints five lines.** `CLAUDE.md` *Publishing constraints* says it "must
   print nothing; every hit is either a leak or a label that needs adding". A check whose documented
   pass condition can never be met is a check that will be read as noise and waved through — the
   exact failure mode T-013's own write-up warns about.
2. **Line 1 of that fixture is a real absolute path from the machine T-013 ran on**, drive letter
   included. It is not reproduced here, for the same reason it should not be there. That is a
   straight R-23 violation (`docs/SCOPE.md`), sitting in the task whose subject is removing exactly
   this class of data, and it is in the definition of done (§9).

Neither was visible to T-013's own review, because the review ran the check *before* writing the
evidence down. Recording proof and staying clean are in tension here; resolving that tension is the
task.

**Requirements served**
R-23 (`docs/SCOPE.md`).

**Scope**
- In: the fixture's home, whatever `CLAUDE.md` has to say about how the check is proven, and the
  real path in T-013.
- Out: changing the grep pattern itself — it works, and T-013 records two earlier drafts that did
  not. If a candidate fix needs the pattern loosened, that is a signal the fix is wrong.

**Inputs**
`CLAUDE.md` *Publishing constraints* and *Verifying*; `tasks/T-013-…md` §4; `docs/SCOPE.md` R-23, §9.

**Acceptance criteria**
- [ ] The check, run over `git ls-files`, prints nothing — demonstrated, not asserted
- [ ] No tracked file contains a real absolute local path, drive letter, home directory, UNC path
      or IP address
- [ ] The fixture can still be re-run by a future session, and it is still visible **which** four
      safe forms must not trip the check — losing the negative cases would make a later loosening of
      the pattern undetectable
- [ ] T-013's review still shows the check was proven by failing, with a pointer to wherever the
      fixture now lives, so the evidence is relocated rather than deleted
- [ ] **The proof run and the clean run are the same command**, differing only by whether the
      fixture is excluded — so the thing a future session re-runs is the check itself, not a
      second command that could drift from it
- [ ] The relocation left **no copy behind**: a grep for a fixture line over the tracked tree
      returns exactly one file

**Open questions**
- none. ~~Gitignored `control/`, or a documented exclusion?~~ **Decided 2026-08-05 — a tracked
  fixture, excluded by path in the documented command.** The owner delegated the run; this is
  recorded with its alternatives so it can be reversed in one edit.

  *Rejected — the gitignored `control/` folder,* which the question leaned toward. It fails the
  third criterion outright: a clone cannot re-run a fixture it does not receive, so the negative
  cases would exist only on the machine that wrote them, and a later loosening of the pattern
  would be undetectable by exactly the person most likely to attempt one. Quarantine is right for
  *identities*, which nobody outside needs; it is wrong for *evidence*, which is the thing a
  publishable repository exists to carry.

  *The stated objection to an exclusion — "a second place the check's contract is written" — does
  not survive contact with the shape.* The exclusion is one pathspec inside the one command, in
  the same fenced block, not a second document. And it turns the two runs into one command: with
  the exclusion the tree must print nothing, without it the fixture must print exactly its five
  lines and none of its four safe ones. The proof is therefore the check, run twice, rather than a
  transcript someone pasted in — which is what created this task.

  *Also rejected — constructing the leak lines in code* so no literal exists (`"C" + ":" + ...`).
  It would need no exclusion, and it makes the fixture unreadable at the exact moment someone is
  trying to judge whether the pattern is right.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Write the fixture to its own tracked file**, carrying all nine lines — five that must be caught, four that must not. The drive-path line is **fabricated**, not the one currently in T-013: that line is the R-23 violation, and copying it forward would move the leak rather than remove it. | `tests/fixtures/leak-check/samples.txt`, and a paragraph in `tests/fixtures/README.md` saying why this fixture is not a taskmd project like its neighbours |
| 2 | **Add the pathspec exclusion to the one documented command** in `CLAUDE.md`, and state the two runs there: with the exclusion the tree prints nothing; without it the fixture prints exactly its five lines. | The amended command and its paragraph in `CLAUDE.md` |
| 3 | **Cut the inlined fixture out of T-013 §4 and leave a pointer.** A summary left behind is a copy and will drift; the review keeps its finding — two earlier drafts were wrong and only the failure test found them — and points at the file for the lines themselves. | The edited `tasks/T-013-…md` §4 |
| 4 | **Run both runs and paste the actual output**, then grep the tracked tree for a fixture line to prove the relocation left exactly one copy. | The transcript in §3 |

**Deliverable shape — decided here.** The fixture is **data, not a taskmd project**, so it sits in
`tests/fixtures/` beside the others but holds no config and no tasks. That is worth stating because
every current neighbour *is* a project, and a future reader who assumes the folder's convention
would look for a `.taskmd/` that is deliberately absent.

*Rejected:* a Python test that applies the pattern with `re` and asserts five hits. It would run
automatically, which is genuinely better than a command someone must remember — but `re` is not
POSIX ERE, so the thing under test would no longer be the thing that runs before publishing, and
the pattern would acquire a second home. The task's own scope forbids touching the pattern; giving
it a second implementation is the same mistake wearing a different hat.

**Output paths**

- `tests/fixtures/leak-check/samples.txt`
- `tests/fixtures/README.md`
- `CLAUDE.md`
- `tasks/T-013-quarantine-local-only-information-behind-gitignore.md`

## 3. Implement

### Decisions & assumptions

- **Every path in the fixture is fabricated, and the drive line was not carried over** —
  2026-08-05. The old line was this machine's checkout path; copying it into the new file would
  have relocated the leak rather than removed it, and the fixture does not need a *real* path to
  prove the pattern matches the *shape* of one. The new drive letter is one nobody's checkout uses.
- **The fixture's IP now comes from the range RFC 5737 reserves for documentation** — 2026-08-05.
  The old one was a private-network address, which is a specimen of the class the check exists to
  catch; the replacement cannot be mistaken for a real one. The addresses are not written here, for
  the reason recorded under *What this task got wrong first* below.
- **The fixture is a `.txt` file, not a Markdown one** — 2026-08-05. `check` walks every `.md` in
  the repository looking for broken links, and a Markdown file full of deliberate path-shaped junk
  is an invitation to a second, unrelated failure. The extension keeps the two validators apart.
- **`tests/fixtures/leak-check/` is not a taskmd project**, and `tests/fixtures/README.md` says so
  — 2026-08-05. Every other folder there is one; an unstated exception is a trap for the next
  reader, who will look for a `.taskmd/` that was deliberately never created.

### Outputs produced

- `tests/fixtures/leak-check/samples.txt` — the nine lines, five to catch and four to ignore
- `CLAUDE.md` — the pathspec exclusion, the two-runs paragraph, and the verification note rewritten
  to point at the fixture rather than describe it
- `tasks/T-013-…md` §4 — the inlined copy cut, replaced by a pointer and by what its absence taught
- `tests/fixtures/README.md` — why this fixture is the odd one out

### Verification

**Both runs of the one command.** Run 1 is the check as a session runs it before publishing; run 2
is the same command with the exclusion dropped, which is the proof:

```
RUN 1  git ls-files -z ':!tests/fixtures/leak-check/' | xargs -0 grep -nIE '<pattern>'
       (no output)                      exit 123 -- xargs' code for "grep exited non-zero",
                                        which is grep's code for "found nothing". Clean.

RUN 2  git ls-files -z | xargs -0 grep -nIE '<pattern>'
       5 hits, all in tests/fixtures/leak-check/samples.txt, at lines 8, 9, 10, 11 and 12 --
       one per class, in the fixture's declared order, and nothing else in the tree.
```

Five lines, one per class, and **only** those five — so the four safe forms sharing the file, at
lines 14 to 17, were correctly ignored, which is the half a clean tree can never demonstrate. The
matched text is not quoted here; the file is one click away and quoting it is what this task exists
to undo.

### What this task got wrong first

**The first version of this record re-created the defect it was fixing.** §3 quoted the five matched
lines as a transcript and §4 quoted two IP addresses in a criterion note, so the tracked tree
printed nine hits — from *this file*. The review above had already been written and marked those
criteria met, because, exactly as in T-013, **the check was run before the task record was
written**. One task later, with the failure named in its own *Why this one*, the same sequencing
produced the same result.

Two things follow, and the second is the durable one:

1. The offending prose was rewritten to describe rather than quote, and both runs were repeated
   afterwards. The criteria are met on the second pass, and the review notes say so rather than
   implying they passed first time.
2. **The check must be the last thing a session runs, after the record is complete.** A check that
   inspects the tracked tree cannot validate a file that does not exist yet, and the evidence a
   task writes about the check is exactly the text most likely to trip it. This is a project-wide
   working rule rather than a fact about this task, so it belongs in `CLAUDE.md` — added there
   under *The pre-publish check*.

**The relocation left one copy**, not two:

```
git grep -l "fileserver"
tests/fixtures/leak-check/samples.txt
```

One file. T-013 §4 keeps its *finding* — two earlier drafts were wrong and only the failure test
caught them — and points at the fixture for the lines, rather than restating them where they would
drift from the file that is actually run.

**Not verified by a fresh clone.** The claim that a clone can re-run the fixture rests on the file
being tracked, which `git ls-files` showing it demonstrates; no clone was actually made. Recorded
rather than implied.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The check, run over `git ls-files`, prints nothing — demonstrated, not asserted | met **on the second pass** | Run 1 in §3: no output, and the tracked tree is clean for the first time since T-013 wrote its evidence down. It was **not** clean on the first pass — this task's own §3 and §4 quoted the fixture and produced nine hits, which is recorded in §3 *What this task got wrong first* rather than quietly corrected. The documented pass condition in `CLAUDE.md` is now reachable, which was the point |
| No tracked file contains a real absolute local path, drive letter, home directory, UNC path or IP address | met | The old fixture's first line was this machine's checkout path; it was not carried over, and the replacement uses a drive letter no checkout here uses. The address moved into the range RFC 5737 reserves for documentation, from a private-network one — that is, from a specimen of the very class the check catches. Neither is written into this record, which is the lesson of the first pass. Run 1 is the mechanical confirmation |
| The fixture is re-runnable, and **which** four safe forms must not trip the check is still visible | met | All nine lines are in one tracked file, each labelled *must be caught* or *must be ignored*, so the negative half is as legible as the positive half. Run 2 shows only the five, which is what proves the four were ignored rather than merely present. Tracked rather than quarantined in `control/`, so a clone receives it — the reason the specify decision went against the question's own leaning |
| T-013's review still shows the check was proven by failing, with a pointer to where the fixture now lives | met | §4 there keeps the finding — two earlier drafts wrong, only the failure test caught them — and now also records *why* inlining was the mistake, which the original could not know. The lines themselves are gone from it |
| The proof run and the clean run are the same command, differing only by the exclusion | met | One pattern, one pipeline, one pathspec of difference. There is no second command that could drift from the check, which is the failure mode that produced this task in the first place |
| The relocation left no copy behind — one file | met | `git grep -l "fileserver"` returns exactly one path. Checked because a summary left behind when relocating is still a copy, and the more plausible failure here was leaving "an abbreviated version for convenience" in T-013 |

**Also checked, beyond the criteria**

- The fixture is `.txt`, not `.md`, so `check`'s broken-link walk never reads a file of deliberate
  path-shaped junk. `check` clean on 25 tasks; suite 92/92 — neither touched by this task, which
  changed no code.
- `tests/fixtures/README.md` now states that this one folder is not a taskmd project. Every other
  entry there is, and the exception would otherwise be discovered by someone looking for a
  `.taskmd/` that was deliberately never made.
- **`docs/SCOPE.md` §9 definition of done** lists "no personal, client or machine data anywhere in
  the repository (R-23)". That line was false while this task was open and is now true; it needed
  no edit, which is the correct outcome for a definition of done.

**Child fix tasks raised**
- none — every criterion is met.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → done | Review worked. All six criteria met, no child fixes. The tracked tree prints nothing for the first time since T-013, and `docs/SCOPE.md` §9's "no machine data anywhere" became true without needing an edit. Review also confirmed the relocation left exactly one copy — the likelier failure was leaving an abbreviated version behind "for convenience", which is still a copy. |
| 2026-08-05 | → review | Implemented in plan order, no reordering. Three things the fixture's content decided rather than the plan: the drive line was rebuilt rather than carried over (copying it would have moved the leak, not removed it), the IP moved into RFC 5737's documentation range so the fixture is not itself a specimen of what it catches, and the file is `.txt` so `check`'s broken-link walk never reads it. |
| 2026-08-05 | → specified, planned | Run in one pass under the owner's instruction to take the task through the full lifecycle. The open question was the owner's and was decided here with its alternatives recorded: a **tracked** fixture excluded by pathspec, not the gitignored `control/` the question leaned toward — quarantine suits identities, which nobody outside needs, and not evidence, which a clone must be able to re-run. The shape that settled it is that the proof run and the clean run become the same command, differing by one pathspec. |
| 2026-08-05 | → proposed | Found while running the pre-publish check as a routine verification during T-002's specify phase. Raised rather than fixed inline, per `docs/METHOD.md` §3.3. |
