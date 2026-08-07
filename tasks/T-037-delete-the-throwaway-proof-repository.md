---
id: T-037
title: Delete the throwaway repository the GitHub binding was proven on
type: admin
status: proposed
phase: specify
parent: null
blocked_by: [T-006]
related: [T-010, T-041]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-037 — Delete the throwaway repository the GitHub binding was proven on

## 1. Specify

**Outcome**
The private repository created to prove T-010's binding no longer exists, and nothing about this
project depends on it.

**Not yet — it is being kept on purpose.** The owner decided on 2026-08-07 that it stands until the
first complete published version of taskmd, so it stops being a loose end and becomes the fixture
the remaining binding work runs against; T-041 is the first task to use it that way. Hence the
dependency on T-006: this task cannot proceed while the repository still has a job. What it
protects against is the opposite failure — a scratch repository that quietly becomes permanent
because nobody ever wrote down when it should go.

**Why this one**
T-010 criterion 5 required the binding to be followed on a live repository. One was created, used
for a single walk, and could not be removed: `gh repo delete` returned HTTP 403 because the
authenticated token carries `repo` but not `delete_repo`. Adding that scope is an interactive
re-authentication, which is the owner's action and not an agent's — so the cleanup step could not
close and is carried here rather than left as a loose end inside a finished task.

**Scope**
- In: removing the repository, by whichever route the owner prefers, once T-006 has published.
- Out: using it in the meantime. Every task that does is a `related` edge, not a reason to reopen
  this one.
- Out: anything about the binding itself. T-010 owns that, and its proof is already recorded — the
  evidence is the transcript in T-010 §3, not the repository, so deleting it destroys nothing.

**Inputs**
- The repository's name, which is recorded in `control/LOCAL-CONTEXT.md` rather than here: it is
  qualified by an account name, and `CLAUDE.md`'s publishing constraint keeps that out of the
  tracked tree.

**Acceptance criteria**
- [ ] The repository is gone — a fetch of it returns not-found rather than an empty or archived repo
- [ ] No file in the tracked tree references it, by name or by URL
- [ ] If the `delete_repo` scope was added to reach this, it is dropped again afterwards, or the
      decision to keep it is recorded — a scope granted for one deletion and left in place is a
      standing permission nobody chose

**Open questions**
- None. Two routes work and the choice does not change the outcome: refresh the scope
  (`gh auth refresh -h github.com -s delete_repo`) and delete from the CLI, or delete it from the
  repository settings page in a browser. The second needs no scope change and so leaves nothing to
  undo under criterion 3.

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
| 2026-08-07 | — | Owner decided the repository stays until the first published version, so it is a fixture rather than an orphan. Dependency on T-006 added to record that, and `updated` bumped: the missing token scope is no longer the reason this is open, and leaving the old reason standing would have made the record false. |
| 2026-08-07 | → proposed | Raised by T-010 step 6, which could not complete its own cleanup. The blocker is a missing token scope, and re-authenticating is the owner's action — so this is an owner task by nature rather than by delegation. |
