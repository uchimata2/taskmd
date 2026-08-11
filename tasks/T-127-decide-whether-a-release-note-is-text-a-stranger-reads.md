---
id: T-127
title: Decide whether a release note is text a stranger reads
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-079, T-081, T-125, T-126]
work_package: v0.5
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
- ~~**Covered or excluded.**~~ **Answered by the maintainer on 2026-08-11: covered, and §1 says
  plainly that nothing enforces it.** That is the literal reading of §1's own test, and a stated
  unenforced rule beats an unwritten one.

  *Rejected: excluded, on the commit-message grounds.* A release note is an audit trail entry too,
  and excluding it would keep the covered set to files the gate can read. It loses the more
  important half: a release page is the second thing an evaluator opens, and §1's test is about the
  reader rather than about what a script can reach.

  **This makes the residue explicit rather than removing it.** §5 already says the gate cannot notice
  a covered document of a new kind. After this, one covered document is known to be unreachable by
  it, which is the honest state and is why criterion 2 asks for it to be said out loud.

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
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every open task carrying `work_package: v0.5` at that date, through all four phases. It **does not generalise** to `v0.6`, to unlabelled work, or to anything raised after it.
| 2026-08-11 | → specified | Answered by the maintainer: **covered, and §1 says plainly that nothing enforces it.** The rival was excluding it on the commit-message grounds, which is defensible and is recorded in §1 with what it loses. The answer makes the residue explicit rather than removing it: one covered document is now known to be beyond the gate's reach, because the gate reads files and a tag message is not one. That is the state criterion 2 asks to be written down. |
| 2026-08-11 | → proposed | Raised from T-125 at the moment the question had to be answered to ship, and not fixed there: T-125's job was to publish this tree, and deciding what the publishing rule covers is a different outcome that changes a document T-125 only reads. The notes for `v0.4.0` were written to the stricter reading so nothing shipped under an unresolved rule, and that choice is recorded here rather than left as the reason a later reader finds no em dashes and assumes a rule exists. Filed `v0.3`, outside the standing `v0.2` authorization, and not started. |
