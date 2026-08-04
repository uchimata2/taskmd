---
id: T-018
title: Stop the pre-publish fixture tripping its own check
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-013]
work_package: none
owner: maintainer
created: 2026-08-05
updated: 2026-08-05
deliverables: []
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

**Open questions**
- Does the fixture live in the gitignored `control/` folder, or does the check gain a documented
  exclusion for its own fixture? — maintainer. An exclusion is a second place the check's contract
  is written, so `control/` looks likelier, but a gitignored fixture is one a clone cannot re-run.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-05 | → proposed | Found while running the pre-publish check as a routine verification during T-002's specify phase. Raised rather than fixed inline, per `docs/METHOD.md` §3.3. |
