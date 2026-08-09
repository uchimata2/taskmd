---
id: T-080
title: Stop the pre-publish check reporting its own fixture from a subdirectory
type: fix
status: proposed
phase: specify
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
that must be caught. Nothing had leaked. The exclusion is a git pathspec, and a pathspec resolves
against the current directory, so from `tests/` it stops matching the file it names while
`git ls-files` still lists the whole tree.

This is the failure mode `CLAUDE.md` already argues about in that section: *a check that cries wolf
gets ignored, which is worse than a narrow one*. The section documents three deliberate limits and
this is not one of them. It is also the more dangerous shape of the same bug T-034 fixed — there, the
check read nothing and printed nothing, which looks exactly like success; here it reads the wrong set
and prints what a real leak looks like. Both are silent about which mode they are in.

**Scope**
- In: the command in `CLAUDE.md` *The pre-publish check*, and whatever it needs to say about where it
  runs.
- Out: the pattern itself and its three limits, settled in T-013, T-018 and T-058.
- Out: turning the check into a command taskmd ships. `docs/SCOPE.md` non-goal 11 excludes it, twice
  reaffirmed.

**Acceptance criteria**
- [ ] Shown **failing first**: the current command run from a subdirectory, printing the five fixture
      lines with nothing leaked
- [ ] The same run after the fix prints nothing, and the run from the root still prints nothing
- [ ] Dropping the exclusion still prints exactly the five fixture lines and nothing else, from
      both directories — the proof in `CLAUDE.md` must survive the fix
- [ ] Whatever changes, a reader can still see what the command covers; `CLAUDE.md` says the line is
      written long on purpose so this stays readable

**Open questions**
- **Pathspec magic, or an instruction?** `:(top)tests/fixtures/leak-check/` anchors the exclusion to
  the repository root and fixes it wherever it is run; adding "run it from the repository root" to
  `CLAUDE.md` costs no syntax but relies on someone remembering, which `docs/SCOPE.md` §1
  *Invisibility* is sceptical of. The first is one token in an already dense line. — maintainer.

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
| 2026-08-09 | → proposed | Raised from T-079, which tripped it: a leftover `cd tests` from running the suite made the next pre-publish check print its own five-line fixture as though the tree had leaked. The exclusion is a git pathspec and resolves against the working directory; `git ls-files` does not. Raised rather than fixed inline, per METHOD §3.3, and because the one-line choice between pathspec magic and an instruction is the maintainer's. |
