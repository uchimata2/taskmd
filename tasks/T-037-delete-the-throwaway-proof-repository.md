---
id: T-037
title: Delete the throwaway repository the GitHub binding was proven on
type: admin
status: planned
phase: plan
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
| 1 | Confirm nothing still needs the repository before removing it — every task that used it closed, and no open task references it. | A verdict, and the check that produced it |
| 2 | **The owner removes it**, by either route: `gh auth refresh -h github.com -s delete_repo` then `gh repo delete`, or the repository settings page. Not an agent step — see below. | The repository gone |
| 3 | Verify it is *gone*, not emptied or archived: fetching it returns not-found. | The command output |
| 4 | Confirm no tracked file references it by name or URL, and remove the entry in `control/LOCAL-CONTEXT.md` that points at it — that file is the one place it was ever named, so it is the last thing to clear. | Grep output, and the edited (gitignored) file |
| 5 | If `delete_repo` was granted to reach step 2, drop it again or record the decision to keep it. | A recorded outcome |

**Sequencing.** Step 1 leads because it can stop the task: deleting a repository another task still
needs would be discovered only when that task tried to use it, and nothing would be recoverable.
Step 4 comes after the deletion rather than before, because until the repository is gone the
`LOCAL-CONTEXT.md` entry is still true and removing it early would leave a live repository with no
record of what it was.

**Step 2 is not an agent step, and that is the whole reason this task exists.** `gh repo delete`
returns HTTP 403 for this token — `repo` scope without `delete_repo` — and adding the scope is an
interactive re-authentication. An agent must not authenticate on the owner's behalf, so the deletion
is theirs to perform in both routes. Everything either side of it can be prepared and verified
without them.

**Shape of the deliverable — decided.** There is no file to produce; the outcome is an absence plus
the record that it was verified. Rejected: keeping a note in the tracked tree saying the repository
once existed — it would name a thing that no longer exists, and `CLAUDE.md`'s publishing constraint
puts the identity in `control/LOCAL-CONTEXT.md` precisely so the tracked tree never carries it. The
history is this task.

**Output paths**
- None. This task's §3 records the verification; `control/LOCAL-CONTEXT.md` (gitignored) loses its
  entry at step 4.

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
| 2026-08-07 | — | **Retention reaffirmed by the owner after step 1 removed its original reason.** The decision was first taken while T-041 was about to need a live repository; that consumer and every other one — T-042, T-043, T-044 — has since closed, so the repository is no longer a fixture in use. Put to the owner as delete-now against keep-until-publication, with the expiry-drift risk named, and they kept the original call. So the dependency on T-006 stands and this task is parked at `planned` rather than advanced. What has changed is the *reason*: it is now held against binding work that may yet arrive before v1 — GHES verification for T-044, or a second walk once T-003 exists — not against work already queued. Recorded because a dependency whose justification has silently changed is the same defect as one that has silently expired. |
| 2026-08-07 | → planned | Five steps, and only step 2 is blocked. `specify` was at `proposed` — criteria written when T-010 raised this and never separately agreed; the instruction to plan is taken as that agreement, as for T-042, T-043 and T-044. Step 1 has already run and its answer is that nothing needs the repository any more: T-041, T-042, T-043 and T-044 all closed, and a sweep of every open task found this one as the sole remaining reference. So the retention rationale recorded below has expired, which is a question for the owner rather than a licence to delete. |
| 2026-08-07 | — | Owner decided the repository stays until the first published version, so it is a fixture rather than an orphan. Dependency on T-006 added to record that, and `updated` bumped: the missing token scope is no longer the reason this is open, and leaving the old reason standing would have made the record false. |
| 2026-08-07 | → proposed | Raised by T-010 step 6, which could not complete its own cleanup. The blocker is a missing token scope, and re-authenticating is the owner's action — so this is an owner task by nature rather than by delegation. |
