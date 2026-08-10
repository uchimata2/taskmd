---
id: T-103
title: Say whether a closed task's declared output may be repointed when the file moves
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-076, T-089, T-090]
work_package: v0.3
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-103 — Say whether a closed task's declared output may be repointed when the file moves

## 1. Specify

**Outcome**
A project reorganising its files knows, from a document rather than from first principles, whether
editing a closed task's declared path preserves its record or falsifies it.

**Why this one**
Raised as **R-5** by the first adopting project (`control/LOCAL-CONTEXT.md`). `check` reports a
declared deliverable path that does not exist, including on a `done` task — correctly, since
`deliverables` asserts production. The consequence is that anything a closed task declared is
**frozen in place**: move it and the project owns a permanent `MISSING OUTPUT`; leave it and the
project cannot reorganise. The only third option is editing a closed record, and nothing says whether
that is allowed.

That project met the choice twice. Complying with the template-location rule meant moving two files
that three closed tasks declared, and it had already refused the same trade once, leaving two
superseded tools on disk rather than invalidate a closed record. It settled on *updating the path
preserves the record, because the file still exists and the task still produced it* — the declaration
names an artefact, not a location in amber. That reasoning is sound and it is **theirs**, derived
under time pressure, with nothing to lean on.

**This is the third case of one question and the only one with no home.**
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) settled what an
**open** task's declared outputs assert;
[T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) is open for the **cancelled**
case. The closed-and-moved case is neither, and it is the one every project reaches the first time it
reorganises — which is also the moment it is least willing to stop and think.

**The record-integrity rule is what makes it a real question.** A closed task is evidence; the
project's own habit is to annotate rather than rewrite, and a reconcile sweep that edits a stale
statement can destroy the thing an audit produced. Whether a path is a *statement about the past* or a
*pointer to a present artefact* is precisely what has to be decided.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, which is the question: whether the closed record or the
filesystem is the home of where an artefact lives. R-16, since whatever is decided is what `check`'s
`MISSING OUTPUT` is then claiming.

**Scope**
- In: whether a closed task's `deliverables` may be edited to follow a moved file, and what the edit
  owes — a log row, nothing, or a rule about which fields may move after closing.
- In: which document says it. The field name is the binding's, the principle is the method's.
- In: what a project does when the artefact is genuinely gone rather than moved, since that is the
  case the frozen reading is protecting.
- Out: changing what `check` reports. It reports a declared path that is missing, and that is right
  under either answer.
- Out: the cancelled case — [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md).
- Out: the open case, settled by
  [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md).

**Inputs**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, the closing-conditions paragraph — the one
  place that already says `deliverables` asserts production.
- `plugin/skills/taskmd/docs/METHOD.md` §1 rule 5 and §6.
- [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), for the argument
  already made about what the field asserts and when.

**Acceptance criteria**
- [ ] The answer is written in exactly one document, with the rejected alternative recorded
- [ ] It covers a moved artefact and a deleted one, since the two look identical to `check`
- [ ] An adopter meets it where the question arises — reading it should not require knowing the
      answer exists
- [ ] Nothing else in the tree states a second version of it, checked against the whole tree rather
      than the file that was edited
- [ ] `check` is clean on this repository, and the suite still passes if any code changed

**Open questions**
- **Which document?** *Recommended: METHOD §6 states the principle, and the binding says which
  artifact it applies to.* The question — is a closed record a statement about the past or a pointer
  to a present artefact — is backend-independent, and a GitHub-Issues project meets it too.
  *Alternative: the binding alone*, on the grounds that `deliverables` is a field name and field names
  are the binding's; that is cheaper and leaves the next backend to answer it again.
- **Is the answer yes?** *Recommended: yes — update the path, and the log row is the record of the
  move.* The task's evidence is that it produced the artefact, and the artefact still exists.
  *Alternative: no — closed records are immutable, and a project that must move a file records the
  move somewhere else.* The maintainer decides; both are defensible and the projects have already
  diverged.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised as R-5 from the first adopting project's recommendations, where it arrived twice and was answered from first principles both times with nothing to lean on. `high` because it is the first question a reorganising project hits and the two live projects have already answered it differently — one leaving superseded files on disk to protect a closed record, then updating paths in the other direction; `s` because the work is a paragraph and a rejected alternative, not code. Placed in v0.3 with the other method-settling items rather than v0.2, which is about the tool holding up in another project. Recorded so `specify` does not re-derive it: this is the third case of one question — T-089 settled the open case, T-090 carries the cancelled one — and it is the only one with no home. |
