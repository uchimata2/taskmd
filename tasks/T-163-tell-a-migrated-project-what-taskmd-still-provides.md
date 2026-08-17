---
id: T-163
title: Tell a migrated project what taskmd still provides, without judging whether it should stay
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-108, T-164]
work_package: M6
owner: maintainer
business_value: high
effort: m
created: 2026-08-17
updated: 2026-08-17
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-163 — Tell a migrated project what taskmd still provides, without judging whether it should stay

## 1. Specify

**Outcome**
A project whose tasks now live in GitHub Issues is told which parts of taskmd keep working and which
stop applying, in a place it meets at the point of the move rather than in a task record — and can
act on that by removing taskmd or an overlapping task-management skill, with taskmd naming neither
side and removing nothing itself.

**Why this one**
Requested by the maintainer on 2026-08-10 as the second half of the migration request, and **split
out of [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) on 2026-08-17**
on the maintainer's answer to that task's Q4. The reason for the split is in Q4 and is not restated:
T-108's outcome describes the migration alone, so a third of its criteria were judging something its
own stated outcome did not cover.

**This is the unusual half and it should not be softened into a summary line.** It commits taskmd to
naming the point at which it stops earning its place, which is the honest version of a
storage-neutral method: if the method is what matters and the backend is now GitHub, a project should
not also be running a second tracker's habits out of momentum.

**Note the shape of the answer before specifying it — the four commands are local-Markdown only.**
`context`, `index`, `check` and `list` read a folder of task files; after the move there is no
folder, so what remains is the method, the binding, and the skill that routes an agent through them.
Whether that is worth keeping is the question the listing has to let someone answer, and it is a real
question rather than a rhetorical one.

**Requirements served**
R-13 and R-14 (`../docs/SCOPE.md`) — the claim that changing backend changes the binding and not the
method is what decides which entries land on which side of this listing.

**Scope**
- In: **what taskmd still provides once the tasks live in GitHub** — which parts keep working, which
  stop applying, and what the method is still worth when the folder is gone.
- In: **where the migrated project meets that listing.** A task record is not where an adopter meets
  anything; which document carries it is `plan`'s, but that it is not this file is the criterion.
- In: **the removal path** — its trigger, its wording, and what it must never do.
- In: who enumerates what else is installed on the device. Settled by
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) Q3 and carried
  here: the agent can see what its harness serves, and taskmd's code must not scan a machine.
- Out: **the migration itself** —
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md). This task is
  soft-linked to it and not blocked by it: what taskmd still provides after the move is a fact about
  today's CLI, not about a migration having happened.
- Out: **taskmd naming which of the two to drop.** Answered by the maintainer on 2026-08-17,
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) Q3.
- Out: taskmd making network calls, or its code inspecting the machine. Non-goal 5.
- Out: a fifth CLI command. Non-goal 11.
- Out: taskmd removing anything. Removal is the person's action.

**Inputs**
- [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) §1 — the request as
  it arrived, and Q2 and Q3, which settle the division of labour and the verdict question.
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — what a project on this backend actually gets.
- [`../plugin/skills/taskmd/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
  — the half that stops applying, and its six assumptions.
- [`../plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) — what survives a
  backend change by construction.
- `../docs/SCOPE.md` non-goals 5 and 11, and R-13/R-14.

**Acceptance criteria**
- [ ] The listing names what keeps working and what stops applying, **as facts rather than as a claim
      about value** — no entry asserts that taskmd is worth keeping
- [ ] **Every entry was checked by running the command**, against a project with no task folder,
      rather than by reading the CLI or this record — `CLAUDE.md` *Verifying*
- [ ] The listing is written where an adopter meets it, **not only in this task record**
- [ ] **taskmd names neither side**, and shows the facts each half rests on — the maintainer's answer
      to [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) Q3,
      2026-08-17
- [ ] **The removal path is reached when it should be, shown on a case**: what remains is not enough,
      or another task-management skill on the device overlaps it. Demonstrated, not described
- [ ] Nothing is removed by taskmd, and the division is visible in what ships
- [ ] Someone who was not involved can read the listing and say what would change their decision —
      which is the test that it states facts rather than issuing a verdict

**Open questions**
- **Where does the adopter meet the listing?** Candidates: the GitHub binding's own text, the skill,
  or the migration procedure
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) produces. It
  depends on what that procedure turns out to be, so it blocks `plan` and not this phase. **The
  maintainer answers, at `plan`.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Run each of the four commands against a project whose tasks are not local files**, and record what each actually does — not what the CLI reads like. This is the step every entry in the listing rests on, so it goes first | A table, one row per command, carrying the real output |
| 2 | **Derive the two lists from that table and from the two bindings**: what stops applying, and what survives. Each entry names the evidence it came from | The two lists, in §3 |
| 3 | **Write the listing into the GitHub binding** as facts, in the reader's own document rather than in this record | A new section in `plugin/skills/taskmd/docs/bindings/github-issues.md` |
| 4 | **Write the removal path**: what reaches it, what it says, and what it must never do. It names neither side and removes nothing | The same section |
| 5 | **Demonstrate it on the real case this device supplies** — the harness serves its own task tools alongside taskmd, which is exactly the overlap the requirement describes | A worked case in §3, with what the listing showed and what it did not say |
| 6 | **Test the reader criterion**: hand the listing to something that was not involved and ask what would change the decision. An answer that cannot name a fact is the listing issuing a verdict | The result, recorded in §3 |

**Decisions taken at `plan`**

- **The listing's home is the GitHub binding, answering `specify`'s open question** — 2026-08-17,
  decided here rather than asked, under the lifecycle authorisation recorded in the log. The binding
  is the document a project on this backend actually reads, and it is where
  [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)'s migration
  procedure lands, so the reader meets the listing at the end of the move rather than by being sent
  somewhere. *Rejected: a document of its own* — one more file to find, for a reader who already has
  a document. *Rejected: `SKILL.md`* — tier 1 is budgeted and this is read once, at a moment the
  session knows it has reached. *Rejected: leaving it in the migration procedure* — the listing is
  true for any project on this backend, including one that was never migrated.
- **The demonstration uses this device's own overlap and does not manufacture one** — 2026-08-17.
  The harness serves task-creation tools of its own in the same session that serves taskmd, which is
  the collision the requirement describes, found rather than staged. *Rejected: installing a second
  task-management skill to demonstrate against*, which proves the listing against a case chosen to
  suit it.

**Outputs this task will produce**

- plugin/skills/taskmd/docs/bindings/github-issues.md — the listing and the removal path
- the table, the worked case and the reader test, in §3 of this record

## 3. Implement

**Step 1 — the four commands, run rather than read.** 2026-08-17, each against a project root with
no task directory (an empty scratch folder, `--root` pointed at it). `context` was given an id so its
argument parser could not answer first:

```
=== context 42 ===  CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but the project root has
                    no such folder. ...  exit=2
=== index ===       CONFIG ERROR  ... exit=2
=== check ===       CONFIG ERROR  ... exit=2
=== list ===        CONFIG ERROR  ... exit=2
```

Four for four, same error, same exit code. **None of them degrades, warns, or falls back** — which is
what makes the listing a statement about behaviour rather than about intent. The message tells the
reader to *create the folder*, which is right for a misconfigured project and wrong for a migrated
one, where there is deliberately no folder to create. Recorded because it is what a migrated project
actually sees; it is not this task's to change.

**Steps 2–4 — the listing itself is in the binding, not here.** It is
[`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md),
section *What taskmd still gives you here*. Copying it into this record would give it two homes; what
this record holds is the evidence above and the decisions below.

**Step 5 — the worked case, on the overlap this device already had.** The harness serving this
session offers task-creation and task-status tools of its own, alongside taskmd. That is the
collision the requirement describes, and it was found rather than staged. Running the listing against
it:

| The listing asks | The answer here |
| :--- | :--- |
| Which taskmd commands still run after the move? | None of the four. Measured above |
| What does taskmd still supply that nothing else does? | The lifecycle and its exit criteria, the three edge kinds, the audit rule, the schema vocabulary — all durable, all outside any session |
| What does the other tool cover? | In-session work items: create, set status, list. No phases, no exit criteria, no dependency edges, and nothing that outlives the session |

**The overlap turned out to be partial, and the listing said so rather than resolving it.** The two
tools answer different questions — one tracks what this session is doing, the other tracks what the
project has decided — so the honest output is three groups of facts and no recommendation. That is
the criterion being met in the awkward direction: a listing built to justify a removal would have
found a conflict here, and this one reported that the case for removing either is weaker than the
requirement assumed.

**Step 6 — the reader test was run structurally and not independently.** The criterion asks whether
someone uninvolved can name what would change their decision. No uninvolved reader was available
without spawning an agent, which was not requested, so what ran instead was a check of the same
property from the other side: **every claim in the listing must be either a measured output or a
pointer to a document, and none may be a judgement.** Walking the section, the four-command table is
measured, *What survives* is four pointers, *What is gone* is three named absences each traceable to
a command or a binding rule, and the closing paragraph states the tool's own interest and declines.
No claim asserts value. **This is a weaker test than the one specified** and is recorded as such —
see §4.

**Decisions & assumptions**

- **The listing states the tool's own conflict of interest out loud** — 2026-08-17. It is the one
  sentence a reader cannot check for themselves, and leaving it implicit would make the neutrality a
  style rather than a claim. *Rejected: neutral tone without saying why*, which reads as modesty and
  gives the reader nothing to hold the document to.
- **The `check` loss is stated first and without softening** — 2026-08-17. Of the three things with
  no replacement it is the one an adopter meets latest and least visibly, since nothing reports its
  own absence. *Rejected: listing the three in the order they were found.*
- **The migrated project's misleading config error is recorded, not fixed** — 2026-08-17. It is real
  and it is outside this task's boundary; fixing it silently would make this record false about what
  was done (`CLAUDE.md`, *surface what you discover*). It is [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md).

**Outputs produced**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — section *What taskmd still gives you here*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Facts rather than a claim about value; no entry asserts taskmd is worth keeping | met | Walked claim by claim in §3 step 6. The closing paragraph states the tool's interest and declines to resolve it |
| Every entry checked by running the command against a project with no task folder | met | §3 step 1. Four commands, four runs, same error and exit 2. `context` was given an id so its parser could not answer first |
| Written where an adopter meets it, not only in this record | met | The binding's *What taskmd still gives you here*. This record holds the evidence and points |
| taskmd names neither side, and shows the facts each half rests on | met | Three fact groups, no recommendation. The conflict of interest is stated rather than implied |
| The removal path reached on a real case — demonstrated, not described | met | §3 step 5, on the harness's own task tools. **It reported a partial overlap and no conflict**, which is the criterion holding in the direction that does not flatter the feature |
| Nothing removed by taskmd; the division visible in what ships | met | The section says removal is the reader's action, and taskmd's code does not inspect the machine — the same division Q2 drew on T-108 |
| An uninvolved reader can say what would change their decision | **carried** | Met by a **weaker** structural test and recorded as such in §3 step 6. The specified test is [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) |

**One criterion is carried rather than met, and the record says so in both places.** The structural
check asks whether every claim is measurable; the criterion asks whether a reader can act on it, and
the second can fail while the first passes. Closing on the substitute without naming it would have
left a tick nobody could later tell was unearned.

**Child fix tasks raised**
- [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) — carries the seventh
  criterion.

**Raised, but not children** — found during the work and outside this task's boundary:
- [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) — the config error a
  migrated project meets tells it to create a folder it deliberately does not have.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → done | `implement` and `review` complete, closing the lifecycle the maintainer authorised the same day. Six of seven criteria met; **the seventh is carried by [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md)** because it was met by a structural substitute rather than by the test it names, and the substitution is recorded in §3 and §4 rather than absorbed into a tick. Two results worth more than the deliverable. **The demonstration reported no conflict**: run against this device's real overlap — the harness's own task tools — the listing found the two answer different questions and said so, which is the neutrality criterion holding where it costs the feature something. And **the four commands were shown to stop rather than degrade**, exit 2 on all four, which is what lets the listing state behaviour instead of intent. One by-product raised: [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md), the config error telling a migrated project to create a folder it deliberately does not have — recorded and not fixed here, since a silent fix would have made this record false. Neither raised task is covered by the authorisation, which named T-108 and T-163 and excluded what they raise. |
| 2026-08-17 | → planned | `plan` written, six steps, and **`specify`'s open question answered inside it** rather than carried: the listing's home is the **GitHub binding**, with three alternatives rejected and recorded there. The question was written as the maintainer's at `plan`; the lifecycle authorisation is what makes it mine, and the rejections are recorded where the decision is so a later reader can re-open it on evidence rather than on preference. Step 1 runs the four commands against a project with no task folder and goes first because **every entry in the listing rests on it** — criterion 2 refuses an entry derived by reading the CLI. Step 5's demonstration uses an overlap this device already has: the harness serves task-creation tools of its own in the same session that serves taskmd, which is the collision the requirement describes, found rather than staged. |
| 2026-08-17 | → specified | **The seven criteria were agreed by the maintainer** on the day they were written, closing `specify`. **The maintainer authorised the whole lifecycle in the same request** — `specify` → `plan` → `implement` → `review` — covering **this task and [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) and nothing else**: no other task, and nothing either of these two raises, which takes one phase per request unless separately authorised (METHOD §3.1). Recorded here as well as in T-108 because an authorisation kept in one place is one a later session reading the other can miss. **The open question below is therefore mine to decide, with the rejected alternatives recorded beside it** — it was written as the maintainer's at `plan`, and the lifecycle authorisation is what changes that. |
| 2026-08-17 | → proposed | **Split from [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)** on the maintainer's answer to its Q4, taken the same day. The evidence for splitting was inside T-108's own record: its **Outcome** paragraph described the migration alone while three of its nine criteria judged this deliverable, so a third of the criteria sat outside the stated outcome. The two are joined by a **soft** edge and not a dependency (METHOD §4) — what taskmd still provides once the folder is gone is knowable from today's CLI, so this task can start and finish while T-108 is open. T-108's criteria 7, 8 and 9 came here; **criterion 9 is not carried as written**. It required the offer to *say plainly which of the two it is proposing to drop*, which is the verdict T-108's Q3 says to withhold, and the maintainer answered Q3 on 2026-08-17 in favour of **naming no side**. It is replaced by two criteria: taskmd names neither side and shows the facts each half rests on, and a reader who was not involved can say what would change their decision. `high` because the maintainer raised it deliberately and it is the point at which the tool states where it stops earning its place; `m` as the part that took T-108 from `l` to `xl` on 2026-08-10. |
