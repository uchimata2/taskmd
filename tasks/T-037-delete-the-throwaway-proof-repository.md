---
id: T-037
title: Delete the throwaway repository the GitHub binding was proven on
type: admin
status: done
phase: review
parent: null
blocked_by: [T-006]
related: [T-010, T-041]
work_package: M1
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

Worked in plan order. Step 2 happened, and not as this task expected.

**Decisions & assumptions**

- **D1 — the repository was deleted by mistake, and the task closes anyway** — 2026-08-09. The owner
  set out to delete the repository behind
  [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) and removed **this** one
  instead. The two names differ by three words and the two tasks are three days apart. Recorded as
  what happened rather than smoothed into "the owner removed it", because the sequence is the only
  reason a reader would understand why step 1's verdict was produced *after* step 2 rather than
  before it — which is the reverse of what the plan says, and the plan's sequencing note explains
  exactly what that risks.

  **Step 1 was run anyway, late, and its verdict is the same one it would have given.** Nothing
  needed the repository:

  | Candidate | Needed it? |
  | :--- | :--- |
  | [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md), *"the first task to use it that way"* | No — `done` since 2026-08-07; its evidence is its own §3 |
  | [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) criterion 4, a taskmd project on GitHub Issues | No — the criterion permits *"or the limitation is stated"*, and T-005's recorded answer scopes v1 to a config recipe verified inside this repository |
  | [T-006](T-006-package-document-and-publish.md) | No — it needs a **marketplace** remote, which is a different thing, and [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) proved that route |
  | Every other open task | No — swept for `github-issues`, *live repository*, *throwaway* and this task's own id; only T-077 matched, and only to say it is not this |

  So the accident cost nothing, and saying so is not the same as saying it was fine.

- **D2 — the stated purpose had lapsed before the deletion** — 2026-08-09. §1 says the repository
  *"becomes the fixture the remaining binding work runs against; T-041 is the first task to use it
  that way."* T-041 was also the **last**. The `blocked_by: [T-006]` therefore guarded a job that
  ended on 2026-08-07, and would have held this task open until publication for nothing. Left in the
  front matter and not rewritten — it records a real decision, and this note is where a reader learns
  it had expired.

- **D3 — the surviving repository is not renamed into this one's place** — 2026-08-09. The owner
  asked whether
  [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md)'s repository could be
  renamed and used for the same purpose. It cannot: this fixture was **three issues carrying property
  blocks**, and that one is a code push with no issues. Creating the issues would be re-running
  T-010's walk, whose transcript already exists, so it would produce no evidence. Renaming would give
  a scratch repository a purposeful-sounding name and let it become permanent — the precise failure
  §1 says this task protects against.

### Steps 3–5 — verification

```
gh api -i repos/<owner>/<the throwaway proof repository>
HTTP/2.0 404 Not Found                       gone, not emptied and not archived

git ls-files -z | xargs -0 grep -nl <its name>
(no output)                                  no tracked file names it

gh auth status | grep scopes
Token scopes: 'gist', 'project', 'read:org', 'repo', 'workflow'
                                             delete_repo was never granted
```

The third line is criterion 3 answered by the route taken: the owner used the settings page, so no
scope was added and there is nothing to drop. That is what this task's open question predicted of
that route, and it is the reason the route was the recommended one.

**Outputs produced**
- None, by design — the outcome is an absence plus this record. `control/LOCAL-CONTEXT.md`
  (gitignored) keeps the row as a **tombstone** rather than losing it, which is a deviation from plan
  step 4 and is D4 below.

- **D4 — the local-context row is marked gone rather than removed** — 2026-08-09. Plan step 4 said
  remove it. Two labels differing by three words is how the wrong repository came to be deleted, and
  a reader who meets an absence learns nothing from it. The row now records that the repository
  existed, what it held, and that its evidence lives in the task records — which costs four lines in
  a gitignored file and is what would have prevented this.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The repository is gone — a fetch returns not-found rather than an empty or archived repo | met | `HTTP/2.0 404`, checked through the API rather than the web view, which is what distinguishes gone from archived |
| No file in the tracked tree references it, by name or by URL | met | `git ls-files` piped to grep: no output. It was only ever named in `control/`, which is gitignored |
| If the `delete_repo` scope was added to reach this, it is dropped again afterwards, or the decision to keep it is recorded | met | It was not added — scopes are unchanged. The settings-page route leaves nothing to undo, which is why the open question preferred it |

**All three met, and the task still closes on an accident.** Worth stating plainly: the criteria ask
whether the repository is gone and nothing points at it, and both are true however it happened. What
the criteria could not ask — whether it was *meant* to happen — is D1, and it is the part of this
record worth reading.

**Child fix tasks raised**
- none. [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) already exists and is
  unaffected: its repository is still there, and its own answer stands.

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
| 2026-08-09 | → done | **Closed on a deletion nobody intended.** The owner set out to remove T-077's repository and removed this one; the names differ by three words. All three criteria are met regardless — 404 through the API rather than the web view, no tracked file naming it, and `delete_repo` never granted because the settings-page route was used, which is what the open question predicted of it. Plan step 1, *confirm nothing still needs it*, was run **late** and returned the verdict it would have returned early: T-041 was the first task to use it as a fixture and also the last, T-005's one candidate criterion permits stating the limitation instead, and T-006 needs a marketplace remote rather than an issues fixture. So `blocked_by: [T-006]` had been guarding a job that ended on 2026-08-07. The surviving repository was **not** renamed into this one's place — it holds no issues, and the fixture was three issues — which would have been the failure §1 says this task protects against. `control/LOCAL-CONTEXT.md` keeps the row as a tombstone rather than deleting it, against plan step 4: an absence teaches nobody why the wrong one went. |
| 2026-08-07 | — | **Retention reaffirmed by the owner after step 1 removed its original reason.** The decision was first taken while T-041 was about to need a live repository; that consumer and every other one — T-042, T-043, T-044 — has since closed, so the repository is no longer a fixture in use. Put to the owner as delete-now against keep-until-publication, with the expiry-drift risk named, and they kept the original call. So the dependency on T-006 stands and this task is parked at `planned` rather than advanced. What has changed is the *reason*: it is now held against binding work that may yet arrive before v1 — GHES verification for T-044, or a second walk once T-003 exists — not against work already queued. Recorded because a dependency whose justification has silently changed is the same defect as one that has silently expired. |
| 2026-08-07 | → planned | Five steps, and only step 2 is blocked. `specify` was at `proposed` — criteria written when T-010 raised this and never separately agreed; the instruction to plan is taken as that agreement, as for T-042, T-043 and T-044. Step 1 has already run and its answer is that nothing needs the repository any more: T-041, T-042, T-043 and T-044 all closed, and a sweep of every open task found this one as the sole remaining reference. So the retention rationale recorded below has expired, which is a question for the owner rather than a licence to delete. |
| 2026-08-07 | — | Owner decided the repository stays until the first published version, so it is a fixture rather than an orphan. Dependency on T-006 added to record that, and `updated` bumped: the missing token scope is no longer the reason this is open, and leaving the old reason standing would have made the record false. |
| 2026-08-07 | → proposed | Raised by T-010 step 6, which could not complete its own cleanup. The blocker is a missing token scope, and re-authenticating is the owner's action — so this is an owner task by nature rather than by delegation. |
