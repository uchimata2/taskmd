---
id: T-127
title: Decide whether a release note is text a stranger reads
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-079, T-081, T-125, T-126]
work_package: v0.3
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-127 — Decide whether a release note is text a stranger reads

## 1. Specify

**Outcome**
`docs/PUBLISHING.md` §1 says whether a tag message and its GitHub release are covered by the
humanization rule, so the next person writing one is not deciding it again by themselves.

**Why this one**
Met while writing `v0.4.0`'s notes in
[T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md). §1's test is *text a stranger reads before
they have installed anything*, and a release page is exactly that: it is the second thing someone
evaluating the plugin opens after the README. But §1's worked list does not name it, §1 explicitly
excludes commit messages on the grounds that they are read *after* arriving, and the §5 gate's
pathspec covers four files, none of them a tag.

So the question was answered in the moment, by writing the notes without em dashes anyway, and that
answer is recorded nowhere the next release can find it. **This is the residue §5 names out loud** —
*what it cannot do is notice a covered document of a new kind* — arriving for the first time.

**Why `low`.** Nothing is wrong today: the three published release notes carry no em dashes, and the
one written under this uncertainty was written to the stricter reading. The cost is that the next
person re-derives it, and may derive it the other way.

**Requirements served**
R-21 (`docs/SCOPE.md`).

**Scope**
- In: whether a tag message and a GitHub release are covered by §1's test, and one sentence in §1
  saying which.
- In: if covered, whether the §5 gate can reach them at all, given it reads files and a tag message
  is not one.
- Out: when the gate runs, which is [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md).
- Out: the humanizer patterns and the three exceptions. Settled in T-079 and T-081.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §1 and §5, in particular the commit-message exclusion
  and the *what it covers, and the one thing it cannot derive* paragraph.
- The three existing tag messages, as evidence of what has been done in practice.

**Acceptance criteria**
- [ ] `docs/PUBLISHING.md` §1 answers the question for a release note, either way, in one place
- [ ] If they are covered, the answer says what enforces it, or states plainly that nothing does
- [ ] The existing three release notes are checked against whichever answer is given, so the rule
      starts from a known state rather than from an assumption

**Open questions**
- **Covered or excluded.** Covered is the literal reading of §1's test and costs a rule nothing
  mechanical can check. Excluded is defensible on the commit-message grounds, since a release note is
  also an audit trail entry, and it keeps the covered set to things the gate can actually read.
  Maintainer's: it is the same trade §1 already made once for commit messages.

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
| 2026-08-11 | → proposed | Raised from T-125 at the moment the question had to be answered to ship, and not fixed there: T-125's job was to publish this tree, and deciding what the publishing rule covers is a different outcome that changes a document T-125 only reads. The notes for `v0.4.0` were written to the stricter reading so nothing shipped under an unresolved rule, and that choice is recorded here rather than left as the reason a later reader finds no em dashes and assumes a rule exists. Filed `v0.3`, outside the standing `v0.2` authorization, and not started. |
