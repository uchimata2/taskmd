---
id: T-034
title: Let the pre-publish check see files not yet tracked
type: fix
status: proposed
phase: specify
parent: T-026
blocked_by: []
related: [T-013, T-018, T-006]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-06
updated: 2026-08-06
deliverables: []
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

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-06 | → proposed | Raised as F-8 from the T-026 audit, clauses 1 and 3 — found in that audit's step 10, while running the check over the audit's own output, which is the situation the blind spot is worst in. Measured before being written up: 83 files seen versus 90 that a push would send. Raised rather than fixed in place (METHOD §5), even though the fix is one flag, because a silent gap in the last check before publication is exactly the kind of change that should carry a record of having been proven. |
