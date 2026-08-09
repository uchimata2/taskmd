---
id: T-080
title: Stop the pre-publish check reporting its own fixture from a subdirectory
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-018, T-034, T-058]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-080 — Stop the pre-publish check reporting its own fixture from a subdirectory

## 1. Specify

**Outcome**
The pre-publish check in `CLAUDE.md` gives the same answer wherever it is run from, or says where it
must be run from. Today it does neither.

**Why this one**
Found by tripping it, in T-079: the test suite had been run with `cd tests`, the shell kept that
directory, and the next run of the check printed **five lines** — its own fixture, the five specimens
that must be caught. Nothing had leaked.

**Two things go wrong at once, and T-079's account of them was wrong.** That record says
`git ls-files` still lists the whole tree while the exclusion stops matching. Only the second half
holds. Measured while specifying this task:

```
git ls-files --cached --others --exclude-standard
  run from tests/    37 files
  run from the root  159 files
```

`ls-files` lists the **subtree**, not the tree. So from `tests/` the check reads 37 of 159 files, a
quarter of what a push would send, and the exclusion pathspec no longer matches the fixture inside
those 37 — which is why the run is loud. The alarm and the under-scan are the same event: it
**looks** like five leaks and it has actually read almost nothing.

That makes this both failure modes this project has already paid for, in one command. `CLAUDE.md`
argues in this very section that *a check that cries wolf gets ignored*, and the section's three
documented limits do not include this. And T-034 fixed the silent half of it — a check that read
none of the files it was aimed at and printed nothing, which is also what success looks like. Here
the under-scan is disguised by an alarm, which is the same defect wearing the opposite mask.

**Scope**
- In: the command in `CLAUDE.md` *The pre-publish check*, and whatever it needs to say about where it
  runs.
- Out: the pattern itself and its three limits, settled in T-013, T-018 and T-058.
- Out: turning the check into a command taskmd ships. `docs/SCOPE.md` non-goal 11 excludes it, twice
  reaffirmed.

**Acceptance criteria**
- [ ] Shown **failing first**: the current command run from a subdirectory, printing the five fixture
      lines with nothing leaked, **and** the file count it actually read
- [ ] After the fix, the run from a subdirectory prints nothing and reads the same file count as the
      run from the root — the count is the criterion, because silence alone is what the broken
      version produces when it reads nothing
- [ ] Dropping the exclusion still prints exactly the five fixture lines and nothing else, from both
      directories — the proof `CLAUDE.md` documents must survive the fix
- [ ] A reader can still see what the command covers. `CLAUDE.md` says the line is written long on
      purpose and must not be shortened to `-co`; whatever is added is subject to the same rule
- [ ] `CLAUDE.md` describes the failure rather than reproducing it — no matched line is pasted, which
      is the trap T-013 and T-018 both fell into

**Open questions**
- ~~**Pathspec magic, or an instruction?**~~ **Mine to answer**: the maintainer delegated the whole
  lifecycle on 2026-08-09. Both candidates are one line and only a run distinguishes them, so the
  answer is taken in §3 D1 on evidence rather than asserted here. The choice is between anchoring the
  command so it is correct from anywhere, and telling the reader where to stand — and `docs/SCOPE.md`
  §1 *Invisibility* says no correctness may depend on someone remembering to intervene, which is a
  strong prior against the second and not a substitute for testing the first.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Show the current command failing from a subdirectory, with the file count beside the five lines. | The failing transcript, and the two counts |
| 2 | Try each candidate from a subdirectory and from the root: pathspec magic anchoring the exclusion, and a form that anchors the whole command. Compare file counts, not just silence. | A result per candidate, including any that does not work and why |
| 3 | Pick one and record what was rejected. | D1 in §3 |
| 4 | Edit the command in `CLAUDE.md`, and the prose around it only where the fix changes what is true. | The edited section |
| 5 | Re-prove the documented proof from **both** directories: with the exclusion, silent; without it, exactly five lines. | Four runs |
| 6 | Run `index`, `check`, the suite, and the check itself. | The output of each |

**Step 1 is not ceremony.** `CLAUDE.md` says a validator is only proven when it has been made to
fail, and the whole reason this bug survived is that both of its symptoms are indistinguishable from
states the reader already expects — five lines looks like a leak, and silence looks like success.
The count is what separates them, which is why it appears in step 1 and in the criteria.

**Step 2 tests both candidates rather than the preferred one.** `:(top)` is the smaller edit and may
not be sufficient: it can anchor the *exclusion* while leaving `ls-files` listing only the subtree,
in which case the loud symptom disappears and the silent under-scan survives — the worse of the two
outcomes, and one that a silence-only test would call a pass.

**Not in this plan:** the pattern and its three documented limits (T-013, T-018, T-058), and making
the check a taskmd command, which `docs/SCOPE.md` non-goal 11 excludes.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — anchor the whole command, not the exclusion** — 2026-08-09. The command gains
  `( cd "$(git rev-parse --show-toplevel)" && … )`. *Rejected: `:(top,exclude)` on the pathspec*, which
  is the smaller and more elegant edit and which step 2 was written to catch: it drops the fixture
  from the listing and the command goes silent, while still reading **36** files instead of 158. That
  converts a loud wrong answer into a quiet one, which is strictly worse — it is T-034's bug
  restored, and a test that only checked for silence would have passed it. *Rejected: documenting
  "run it from the repository root"*, on `docs/SCOPE.md` §1 *Invisibility*: no correctness may depend
  on someone remembering to intervene, and this session forgot within one command of running the
  suite.

- **Assumption, recorded:** that `git rev-parse --show-toplevel` resolves for every reader. It is
  git's own answer to "where is the root", and the check is already meaningless outside a work tree,
  so nothing was added for a case in which the surrounding command cannot run either.

### Step 1 — the failure, shown first

Run from `tests/`, unanchored, with the file count beside it:

```
files read: 37
tests/fixtures/leak-check/samples.txt   5 matches, elided
```

Against **159** from the root. Nothing had leaked. The five lines are the fixture's own specimens,
which is why they are described here and not pasted — the trap T-013 and T-018 both fell into.

### Step 2 — both candidates, measured by file count

| Candidate | From `tests/` | Output | Verdict |
| :--- | :---: | :--- | :--- |
| unanchored (current) | 37 files | 5 lines | loud, and blind |
| `:(top,exclude)` on the pathspec | 36 files | silent | **quiet, and still blind** |
| `cd` to the toplevel | 158 files | silent | correct |

The middle row is the finding. It looks like a fix and passes any test that asks only whether the
command printed anything.

### Step 5 — the documented proof, re-run from both directories

```
root    with exclusion    158 files    silent
tests/  with exclusion    158 files    silent
tests/  without exclusion              5 matches, all in the fixture, elided
```

Identical from both, which is the criterion. The paths now print root-relative from anywhere, so a
hit names a file the reader can open without knowing where the run happened.

**Outputs produced**
- `CLAUDE.md` — the anchored command, and one paragraph saying why the `cd` is load-bearing and that
  a run is judged by its file count rather than by its silence

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Shown **failing first** from a subdirectory, with the file count beside the five lines | met | §3 step 1: 37 files against the root's 159, and five lines from the fixture with nothing leaked |
| After the fix, the subdirectory run prints nothing and reads the same count as the root run | met | §3 step 5: **158 from both**. The count is what carries this, and it is the reason the rejected candidate was caught |
| Dropping the exclusion still prints exactly the five fixture lines and nothing else, from both directories | met | §3 step 5, and §3 step 1 for the unanchored form. Five matches, all in `tests/fixtures/leak-check/samples.txt` |
| A reader can still see what the command covers | met | The three flags and the pathspec are untouched and still visible; the addition is a prefix, not an abbreviation. `-co` is still refused |
| `CLAUDE.md` describes the failure rather than reproducing it | met | No matched line appears in `CLAUDE.md` or in this record. The check was run last, after both were written |

**The rejected candidate is the result worth keeping.** `:(top,exclude)` is the smaller edit, it
looks correct, and it silences the symptom while leaving the command reading 36 files of 159. Had the
criterion been "prints nothing from a subdirectory", it would have passed and this task would have
closed having made the bug harder to find. That is why the criterion is the file count, and why
`CLAUDE.md` now says to judge a run by the count rather than by its silence.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met. The command is anchored with a `cd` to the toplevel and reads **158** files from a subdirectory and from the root alike, against **37** before. Two corrections came out of specifying it. T-079's account of the bug was wrong: `git ls-files` lists the *subtree*, not the tree, so the broken command was not merely noisy, it read a quarter of what a push would send while printing what a leak looks like. And the obvious fix is a trap — `:(top,exclude)` anchors the pathspec, drops the fixture, goes silent, and still reads 36 of 159. It would have passed a criterion written as "prints nothing", which is why the criterion is the file count and why `CLAUDE.md` now says to judge a run by its count rather than its silence. Nothing was pasted from the fixture into either document, and the check ran last, after both were written. |
| 2026-08-09 | → planned | Six steps. Step 1 shows the failure with the file count beside it, because both of this bug's symptoms are indistinguishable from states the reader already expects: five lines looks like a leak, silence looks like success, and only the count separates them. Step 2 tests **both** candidates rather than the preferred one, on the specific worry that anchoring the exclusion alone removes the alarm and keeps the blindness. The open question was answered by delegation rather than by the maintainer, and deferred to §3 because only a run distinguishes the two one-line answers. |
| 2026-08-09 | → specified | The premise this task was raised on was checked and **corrected before planning**: T-079 recorded that `ls-files` still lists the whole tree from a subdirectory, and it does not — 37 files against 159. So the defect is both of the failure modes this project has already paid for at once, T-034's silent under-scan wearing the mask of a loud false positive. Criteria rewritten around the file count for that reason, and one criterion added for the trap T-013 and T-018 both fell into: describe the matched lines, never paste them. |
| 2026-08-09 | → proposed | Raised from T-079, which tripped it: a leftover `cd tests` from running the suite made the next pre-publish check print its own five-line fixture as though the tree had leaked. The exclusion is a git pathspec and resolves against the working directory; `git ls-files` does not. Raised rather than fixed inline, per METHOD §3.3, and because the one-line choice between pathspec magic and an instruction is the maintainer's. |
