---
id: T-196
title: Delete the scratch repository the standing check ran against
type: admin
status: done
phase: review
parent: T-193
blocked_by: []
related: [T-108]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-196 — Delete the scratch repository the standing check ran against

## 1. Specify

**Outcome**
`github.com/uchimata2/taskmd-standing-check-scratch` no longer exists, and
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s fifth acceptance criterion
is met in full rather than in half.

**Why this is a task and not a line in T-193**
T-193's criterion reads *the scratch repository is deleted, and the record says the destination was
never the evidence*. The second half is met; the first cannot be met by the session that ran the
work, and that was **measured rather than assumed** — `gh auth status` reports `gist`, `project`,
`read:org`, `repo`, `workflow`, and deleting a repository needs `delete_repo`. T-193 §1 records the
same limit from the day the grant was given, and says a plan whose last row is a session deleting the
repository cannot execute.

So the remainder belongs to whoever holds the account. It is a task rather than a sentence in a
closing record because **views read open work**: T-193 closes, and a note inside it stops being
anywhere anyone looks. The maintainer deleted [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)'s
scratch repository the same day for the same reason, and that disposal is the precedent this follows.

**Scope**
- In: deleting the repository, and recording that it is gone
- Out: adding `delete_repo` to any credential. Widening what a session can do to a hosting account
  is a decision for the owner, taken on its own evidence and not as a side effect of tidying up
- Out: anything about the nine rows or the binding. Both are T-193's, and T-193 is closed

**Inputs**
- [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) §3 step 10 — the
  repository name and why it was never the evidence
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §3 — the same
  disposal, done once before

**Acceptance criteria**
- [ ] `gh repo view uchimata2/taskmd-standing-check-scratch` fails with *not found*, and what it
      printed is recorded here
- [ ] This record says the repository held nothing that is not reproducible by re-running the
      procedure, so nothing was lost with it

**Open questions**
- none. The owner said on 2026-08-21, in the session that raised this, that they would do it by
  hand.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Ask the owner to delete it, since the credential a session reaches carries `repo` and not `delete_repo`. | The request made, and the owner's confirmation. |
| 2 | Verify by running `gh repo view` against it and reading what comes back — not by trusting the confirmation. | The command's actual output, quoted. |
| 3 | State what the repository held, so the record says what was and was not lost with it. | A sentence naming the contents and where the evidence lives instead. |

**Sequencing.** Step 2 after step 1 and not instead of it: a session cannot delete the repository, so
the only thing it can contribute is the check — and a task whose evidence is somebody else's word is
the shape this project's *Verifying* rule exists to refuse.

## 3. Implement

### Steps 1–2 — asked, and then checked

The owner confirmed the deletion on 2026-08-21. Verified rather than taken:

```text
$ gh repo view uchimata2/taskmd-standing-check-scratch
GraphQL: Could not resolve to a Repository with the name
'uchimata2/taskmd-standing-check-scratch'. (repository)
```

That is the *not found* the criterion asks for, and it is GitHub answering rather than this record
asserting.

### Step 3 — what went with it

The repository held 28 labels and 24 issues carrying a copy of this project's own public task
records, created for
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s run and mutated twice
during it. **Nothing in it is unrecoverable, and nothing in it was the evidence.** The four runs and
what each printed are in that task's §3 and in the binding's *What this procedure has been run
against*; anyone doubting them re-runs the procedure against a backlog of their own, which is what
the register tells them to do. Re-creating this particular repository would prove nothing that
reading it could have.

**Decisions & assumptions**

- **The confirmation was verified rather than accepted — rationale: `CLAUDE.md`'s *Verifying* rule
  binds on any claim about behaviour, including somebody else's report of an action.** The check
  costs one command and the alternative is a closed task whose only evidence is a sentence —
  2026-08-21.

**Outputs produced**

- this record

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `gh repo view uchimata2/taskmd-standing-check-scratch` fails with *not found*, and what it printed is recorded here | met | §3 quotes GitHub's own reply — `Could not resolve to a Repository with the name 'uchimata2/taskmd-standing-check-scratch'`. Run after the owner confirmed, not instead of confirming |
| This record says the repository held nothing that is not reproducible by re-running the procedure, so nothing was lost with it | met | §3 step 3 names what it held — 28 labels, 24 issues copied from public task records — and where the evidence lives instead: T-193 §3 and the binding's register |

**This closes T-193's fifth criterion**, which that task recorded as *not met* because a session
cannot delete a repository. The half T-193 could meet — *the record says the destination was never
the evidence* — was met there; this is the other half, and it needed the owner.

**Open questions, re-read before closing.** §1 recorded none, and none arose.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Both criteria met.** The owner deleted it and confirmed; `gh repo view` was then run and returned *Could not resolve to a Repository*, which is the evidence rather than the confirmation. This closes [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s fifth criterion, the one a session could not meet. |
| 2026-08-21 | → proposed | Raised by [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s review as the one criterion it did not meet. `medium` and `xs`: the repository is private and holds a copy of 24 public task records, so leaving it costs tidiness rather than exposure — but the criterion is not met until it is gone. A child of T-193 rather than a soft link, because T-193's criterion is what this closes. |
