---
id: T-077
title: Delete the rehearsal repository T-067 installed from
type: admin
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-067, T-037]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-077 — Delete the rehearsal repository T-067 installed from

## 1. Specify

**Outcome**
The private repository created so that
[T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) had a remote to install *from*
no longer exists.

**Why this one**
T-067's answered open question made cleanup a plan step with its own output, precisely so this would
not become a loose end — and the step could not close. `gh repo delete` returns:

```
HTTP 403: Must have admin rights to Repository.
This API operation needs the "delete_repo" scope.
```

The authenticated token carries `repo` and not `delete_repo`. Adding the scope is an interactive
re-authentication, which is the owner's action and not an agent's, so the deletion is carried here
rather than left unsaid inside a finished task.

**Why this is not [T-037](T-037-delete-the-throwaway-proof-repository.md), and not folded into it.**
Same root cause, same account, same one-line fix. But T-037's repository is being kept **on
purpose** until [T-006](T-006-package-document-and-publish.md) publishes — it became the fixture the
remaining binding work runs against, which is why that task is `blocked_by: [T-006]`. This one has no
job at all: it was pushed once, installed from once, and its evidence is the transcript in T-067 §3
rather than the repository. Merging the two would inherit a block that does not apply and would keep
a dead repository alive for the length of a release.

**Unlike T-037, nothing depends on it.** It can go the moment someone has the scope.

**Requirements served**
None directly. `CLAUDE.md` *Publishing constraints* in spirit — a scratch artefact that quietly
becomes permanent because nobody wrote down when it should go.

**Scope**
- In: removing the repository, by whichever route the owner prefers.
- Out: the `delete_repo` scope itself. Granting it is a decision about the owner's credentials, not
  about this repository — and the web UI removes the need for it entirely.
- Out: anything T-067 established. Its evidence is its own record; deleting this destroys nothing.
- Out: T-037's repository, which is deliberately alive.

**Inputs**
The repository's name, recorded in `control/LOCAL-CONTEXT.md` rather than here — it is qualified by
an account name, which `CLAUDE.md`'s publishing constraint keeps out of the tracked tree.

**Acceptance criteria**
- [ ] The repository does not exist, confirmed by asking for it and being told so
- [ ] `control/LOCAL-CONTEXT.md`'s row for it is removed or marked gone, so that file does not
      outlive the thing it describes
- [ ] Nothing in this repository names it, and no remote in any local clone points at it —
      T-067 removed the remote it added, and that stays true

**Open questions**
- ~~**Two routes, and the owner picks.**~~ **Answered by the maintainer on 2026-08-09: the web
  UI.**

  It deletes the repository and grants nothing. Refreshing the token's scope would hand a standing
  *delete any repository* capability to every process that uses it, permanently, to save one browser
  visit on a one-off cleanup — which is a poor trade for a credential that already carries `repo`.

  *Rejected: `gh auth refresh -h github.com -s delete_repo`.* Not unreasonable, and the case for it
  is getting stronger rather than weaker: this is the **second** throwaway repository in three days
  ([T-037](T-037-delete-the-throwaway-proof-repository.md) is the first) and that task needs the same
  capability. If scratch repositories become routine, granting the scope once and deleting both is
  the cheaper shape — recorded here so the option is available on evidence rather than rediscovered
  at the third one.

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
| 2026-08-09 | → specified | Answered: **the web UI**. It grants nothing; the scope refresh hands a standing delete-any-repository capability to every process using that token, permanently, to save one browser visit. The rejected option is recorded with the reason it may still win later: this is the second throwaway repository in three days and T-037 needs the same capability, so if scratch repositories become routine the scope is worth granting once for both. Criteria unchanged — the route does not change what has to be true at the end. |
| 2026-08-09 | → proposed | Raised from T-067's `implement`, where cleanup was a plan step with its own output and the step failed on a missing token scope — the same 403 that produced T-037 two days earlier. Deliberately **not** folded into T-037: that repository is alive on purpose until T-006 publishes, and merging would inherit a block this one does not have. `medium`/`xs` — one action, and the reason it is not `low` is that the failure mode being guarded against is a scratch repository nobody remembers to remove. |
