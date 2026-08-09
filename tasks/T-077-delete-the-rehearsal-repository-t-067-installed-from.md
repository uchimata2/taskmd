---
id: T-077
title: Delete the rehearsal repository T-067 installed from
type: admin
status: done
phase: review
parent: null
blocked_by: []
related: [T-067, T-037]
work_package: v0.1
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

Short, and it borrows [T-037](T-037-delete-the-throwaway-proof-repository.md)'s shape deliberately —
same action, same account, same reason the middle step is not an agent's.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Confirm nothing needs the repository, before it goes rather than after | A verdict, and the check behind it |
| 2 | **The owner removes it** from the repository settings page. Not an agent step: `gh repo delete` returns 403 for this token, and an agent must not re-authenticate on the owner's behalf | The repository gone |
| 3 | Verify it is *gone* and not emptied or archived — fetch it through the API, which distinguishes the two, rather than the web view, which does not | The command output |
| 4 | Mark the `control/LOCAL-CONTEXT.md` row gone, after the deletion and not before | The edited (gitignored) file |
| 5 | Confirm no scope was granted to reach step 2, since the chosen route should have needed none | `gh auth status` |

**Why step 1 leads even though the answer is obvious.** It is obvious here and it was obvious in
T-037, where the same step was skipped and the wrong repository was deleted. The check costs one
command; being sure which repository is which is what it actually buys.

## 3. Implement

Worked in plan order.

**Decisions & assumptions**

- **D1 — step 1 was run first this time, on both repositories rather than one** — 2026-08-09. T-037's
  deletion went wrong because two labels three words apart were not distinguished before acting. So
  the check here named the survivor **and** the casualty, and was run against the API rather than the
  web view:

  ```
  taskmd-install-rehearsal    HTTP/2.0 200 OK        the one to delete
  taskmd-binding-proof        HTTP/2.0 404 Not Found the one already gone, by mistake
  ```

  Nothing needed the survivor. [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md)'s
  evidence is its own §3; [T-006](T-006-package-document-and-publish.md) will want a **marketplace**
  remote when it proves both distribution shapes, and T-067 recorded how to create one, which takes
  seconds. Holding a repository open for weeks against that is the trade this task exists to refuse.

- **D2 — the surviving repository was not repurposed** — 2026-08-09. The owner asked whether it could
  be renamed and used for what T-037's repository had been kept for. It could not: that fixture was
  **three issues carrying property blocks**, and this was a code push with none. Creating the issues
  would re-run T-010's walk, whose transcript already exists, so it would yield no evidence — and a
  scratch repository with a purposeful-sounding name is how one becomes permanent. Recorded here as
  well as in T-037 D3 because the question was asked about *this* repository.

- **D3 — the row is marked gone, not removed** — 2026-08-09. Same treatment T-037 took, and the
  reason has stopped being hypothetical: **these two labels are the ones that got confused.** A
  reader who meets an absence learns nothing; a reader who meets both tombstones learns that the
  project had two scratch repositories with similar names and now has none.

### Steps 3–5 — verification

```
gh api -i repos/<owner>/<the install-rehearsal repository>
HTTP/2.0 404 Not Found                       gone, not emptied and not archived

gh repo list
handoff-skill            public
Project-Leviathan-RIMT   public              no taskmd scratch repository remains

git remote -v                                (no output — this clone has no remotes)
git ls-files -z | xargs -0 grep -nl <its name>
(no output)                                  no tracked file names it

gh auth status | grep scopes
Token scopes: 'gist', 'project', 'read:org', 'repo', 'workflow'
                                             delete_repo never granted
```

The last line is the recorded answer confirmed by use for the second time in one day: the settings
route deletes the repository and grants nothing, so there is no standing permission to drop
afterwards.

**Outputs produced**
- None, by design — the outcome is an absence plus this record. `control/LOCAL-CONTEXT.md`
  (gitignored) keeps a tombstone.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The repository does not exist, confirmed by asking for it and being told so | met | `HTTP/2.0 404` through the API, which distinguishes gone from archived where the web view does not; and `gh repo list` shows no taskmd scratch repository at all |
| `control/LOCAL-CONTEXT.md`'s row for it is removed or marked gone, so that file does not outlive the thing it describes | met | Marked gone. The criterion offered either; D3 says why the tombstone is the better half of it here, and the reason is this week's own near-miss rather than a principle |
| Nothing in this repository names it, and no remote in any local clone points at it — T-067 removed the remote it added, and that stays true | met | `git remote -v` empty, `git ls-files` piped to grep empty. The remote T-067 added was removed in that task and has not returned |

**Child fix tasks raised**
- none. **Both scratch repositories are now gone**, T-037 and this one, and the project holds no
  remote it did not intend to hold.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All three criteria met. Step 1 — *confirm nothing needs it* — was run **before** the deletion this time and against **both** repositories rather than one, because T-037's deletion went wrong precisely by not distinguishing two labels three words apart; the check named the survivor and the casualty and used the API rather than the web view, which is what tells gone from archived. Nothing needed it: T-067's evidence is its own §3, and T-006 will want a *marketplace* remote, which T-067 recorded how to create in seconds. The repository was **not** repurposed for what T-037's had been kept for — that fixture was three issues carrying property blocks and this was a code push with none, so creating them would re-run a walk whose transcript exists. `delete_repo` was never granted, confirming the recorded answer by use for the second time in a day. The `control/` row is a tombstone rather than an absence, and the reason has stopped being hypothetical: these are the two labels that got confused. **No taskmd scratch repository now exists.** |
| 2026-08-09 | → specified | Answered: **the web UI**. It grants nothing; the scope refresh hands a standing delete-any-repository capability to every process using that token, permanently, to save one browser visit. The rejected option is recorded with the reason it may still win later: this is the second throwaway repository in three days and T-037 needs the same capability, so if scratch repositories become routine the scope is worth granting once for both. Criteria unchanged — the route does not change what has to be true at the end. |
| 2026-08-09 | → proposed | Raised from T-067's `implement`, where cleanup was a plan step with its own output and the step failed on a missing token scope — the same 403 that produced T-037 two days earlier. Deliberately **not** folded into T-037: that repository is alive on purpose until T-006 publishes, and merging would inherit a block this one does not have. `medium`/`xs` — one action, and the reason it is not `low` is that the failure mode being guarded against is a scratch repository nobody remembers to remove. |
