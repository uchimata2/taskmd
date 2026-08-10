---
id: T-035
title: Warn that a fabricated specimen must not cross a shell
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-034, T-013, T-018]
work_package: v0.2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-06
updated: 2026-08-10
deliverables: []
---

# T-035 — Warn that a fabricated specimen must not cross a shell

## 1. Specify

**Outcome**
`CLAUDE.md` §*The pre-publish check* warns that a fabricated specimen must be written by something
that does not shell-escape it, so the next author who proves the check by making it fail is not
handed a false result.

**Why this one**
Found during [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md)'s `implement`,
which had to produce exactly such a specimen. Written through the shell, the UNC line lost one
leading backslash in transit and stopped being a UNC path; a quoted heredoc did not help. The run
then reported three of the four classes caught.

**The failure mode is that this looks like a finding.** The natural reading of "three of four" is
that the pattern has a hole in its UNC branch — a defect in a regex settled in T-013 and T-018,
raised against the wrong thing, and "fixed" by loosening a branch that was already correct. The
damage is silent in both directions: the specimen looks like what was typed, and the check looks
like it failed.

`CLAUDE.md` instructs a future author to do this — *"a validator is only proven when it has been
shown to **fail** on a case it is supposed to catch"* — and says nothing about the trap. Three of
the four classes are backslash-bearing, so it is the common case, not an edge one.

**Requirements served**
R-16 (`docs/SCOPE.md`), whose whole content is proof-by-failure, and R-20's cross-platform concern —
this is the same class as the existing `newline="\n"` note, which is already in `CLAUDE.md` for the
same reason.

**Scope**
- In: one warning in `CLAUDE.md` §*The pre-publish check*, beside the two-run proof it applies to.
- Out: the regex, its four classes and its two limits. Settled in T-013 and T-018; this task exists
  because they are correct and were nearly re-opened on false evidence.
- Out: `tests/fixtures/leak-check/samples.txt`, which is committed and crosses no shell.
- Out: any change to the check command itself — that was T-034.

**Inputs**
`CLAUDE.md` §*The pre-publish check* and §*Verifying*,
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) §3 *Found while verifying*.

**Acceptance criteria**
- [ ] `CLAUDE.md` names the failure — a specimen damaged in transit — and what to do instead
- [ ] It says how to detect it, since the damaged text is indistinguishable from the intended text
      by reading; a byte-level check on the stored line is what identified it in T-034
- [ ] It says why it matters: the result is a *false negative attributed to the pattern*, not an
      obvious error
- [ ] No fabricated specimen or matched line is quoted into this task's record or into `CLAUDE.md`
- [ ] The addition does not restate the two-run proof, which already has one home

**Open questions**
- None.

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
| 2026-08-06 | → proposed | Raised from T-034's `implement`, which hit it while producing the specimen its criterion 2 demanded. Raised rather than fixed in place (METHOD §5) even though it is one paragraph: T-034's scope explicitly excludes the regex and the fixture, and this warning is about neither the command nor the pattern but about how the proof is produced. Medium value — it does not affect what the check catches, only whether the next person proving it can trust the answer. |
