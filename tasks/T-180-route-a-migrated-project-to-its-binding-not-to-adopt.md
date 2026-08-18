---
id: T-180
title: Route a migrated project to its binding rather than to adopt.md
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-163, T-164, T-177]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-18
updated: 2026-08-18
deliverables: [plugin/skills/taskmd/SKILL.md]
---

# T-180 — Route a migrated project to its binding rather than to adopt.md

## 1. Specify

**Outcome**
A skill that sends a project whose task folder does not resolve to the document that helps it, in
the one case where it currently sends it to the document written for a project that has not
started.

**Why this one**
**`SKILL.md`'s load table has one row for this and it points the wrong way.** It reads: load
[`adopt.md`](../plugin/skills/taskmd/adopt.md) when "the project has no tasks yet, **or a command
reports its task folder missing**". Those two conditions have different answers. `adopt.md` is 92
lines about taking taskmd up and choosing a backend; it mentions bindings once and says nothing
about a project that has already migrated and whose commands now correctly refuse.

**The error message already does the right thing, which is why this is small and also why it is
worth doing.** [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) gave that
refusal a third possibility, and it is good — run against the fixture it says the commands do not
apply and names `id_width` as the reason. So the skill's table and the tool's own message currently
point in different directions on the same event, and the table is the one a session reads first.

**The whole cost of taskmd to such a project is the skill** — measured at 414 characters a session in
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md). If it routes
that project to the wrong document, the one thing installation buys is spent pointing away from the
binding, which is the thing that would have helped.

**Scope**
- In: the load-table row that fires on a missing task folder
- In: whether `adopt.md` should also cover the migrated case, or whether the row should split
- Out: the error message, which [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md)
  settled and which is not the defect here
- Out: growing tier 1. `SKILL.md`'s description is the budgeted part and this task must not touch
  it; the load table is in the body

**Inputs**
- `plugin/skills/taskmd/SKILL.md` — the load table, and the paragraph above it that already says a
  different backend's binding supplies the operations
- `plugin/skills/taskmd/adopt.md` — what it actually covers, which is the evidence for the split
- [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) — the message that gets this
  right, and the wording to stay consistent with

**Acceptance criteria**
- [ ] A project whose task folder does not resolve is sent to a document that addresses it, and the
      routing is stated against what that document actually contains rather than its title
- [ ] `adopt.md` is no longer named for a condition it does not cover, and the evidence for "does not
      cover" is measured rather than asserted
- [ ] The skill's table and the tool's refusal message point the same way, checked by reading both
- [ ] `SKILL.md`'s `description` is not touched — the budgeted part stays exactly as it is
- [ ] The load table does not grow a row, or the reason it had to is stated

**Open questions**
- **Split the row, or widen `adopt.md`?** Splitting keeps each document about one thing and adds a
  row to a table that is loaded whenever the skill is; widening keeps the table at four rows and
  makes one document cover two situations. Both are cheap. **Decide at `specify`**, weighing the
  table's own weight, since it is read every time the skill is invoked.

  **Answered 2026-08-18: neither. The condition moves to a row that is already there.**

  The question offers two options and both accept a premise worth refusing — that the migrated case
  needs a *new* destination. It does not. **The load table already carries the right document**:
  *this project's binding, in `docs/bindings/`*. A project whose tasks moved to another backend is
  precisely a project whose binding says where they went, and for the GitHub backend that binding
  already carries a section on what is gone and what has no replacement. So the fix is to stop the
  `adopt.md` row claiming a condition it cannot serve, and to let the binding row claim it.

  **Cost: no new row, and one document keeps one job each.** That is the outcome splitting was meant
  to buy, without the row it was going to cost.

  *Rejected: widening `adopt.md`.* Measured — it is 92 lines, and it contains the string *migrat*
  **zero** times. Making it cover a migrated project means one document addressing two audiences
  whose situations are opposite: one has not started, the other has already moved on. *Rejected:
  splitting into a fifth row.* It is the honest version of the same idea and it pays a row for a
  destination the table already names.

  **One correction to §1 above, which does not change its conclusion.** It says `adopt.md` "mentions
  bindings once"; it is four times. The substantive claim — that it says nothing about a project that
  has already migrated — is what the zero *migrat* count establishes, and that holds.

  **A second correction, to this question's own wording.** It says widening "keeps the table at four
  rows". The table has five as of 2026-08-18: T-005 added the handoff-configuration row earlier the
  same day. The arithmetic the question invites is stale, which is a small live example of why the
  answer avoids counting rows and asks which document does the job.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure what `adopt.md` actually covers, rather than describing it, so the routing decision rests on its contents | The counts, in §3 |
| 2 | Decide the routing against those contents and the table as it now stands | The answered question in §1 |
| 3 | Edit the two rows of `SKILL.md`'s load table, leaving the `description` untouched | The edited SKILL.md |
| 4 | Read the tool's refusal message and the edited table side by side and confirm they now agree | The comparison, in §3 |

**Decisions taken at `plan`**

- **The `description` is not read, edited, or measured by this task.** — It is the budgeted part and
  §1 puts it out of scope; the safest way to keep it exactly as it is, is to touch only the two table
  rows. — 2026-08-18

**Outputs this task will produce**

- plugin/skills/taskmd/SKILL.md — two rows of the load table

## 3. Implement

### Step 1 — what `adopt.md` covers, measured

```text
adopt.md lines:          92
mentions of 'binding':    4
mentions of 'migrat':     0
```

**Zero is the number that decides it.** A document that never uses the word cannot be where a
migrated project is sent, and the count is the evidence rather than a reading of the prose. (§1 says
*mentions bindings once*; it is four. Noted in §1 and it changes nothing — the case never rested on
that figure.)

### Step 3 — the edit

Two rows changed, no row added:

| Row | Before | After |
| :--- | :--- | :--- |
| `adopt.md` | "The project has no tasks yet, **or a command reports its task folder missing**" | "The project has no tasks yet" |
| the binding | "Beginning any phase — …" | "Beginning any phase — … **Also when a command reports the task folder missing**: that is usually a project whose tasks moved to another backend, and its binding is the document that says what moved and what is gone." |

The `description` was not opened.

### Step 4 — the table and the message, read side by side

```text
message   ... Or nothing here is broken and these commands do not apply: id_width is 'none',
          which says a backend allocates the ids, so this project's tasks are not local files.
table     Also when a command reports the task folder missing: that is usually a project whose
          tasks moved to another backend, and its binding is ... what moved and what is gone.
```

Both now say *the tasks are somewhere else*, and the table names the document that describes where.
Before the edit the message said the commands do not apply and the table sent the reader to a guide
for taking taskmd up, which is the disagreement §1 raised.

**One hedge is deliberate.** The table says *usually*, because a missing folder is also what a typo
produces — the `broken-tasks-dir` shape — and the message distinguishes the two where the table
cannot. Routing a typo to the binding costs a reader one document; claiming certainty the table does
not have would cost more.

**Decisions & assumptions**
- The `plan` decision held. — 2026-08-18

**Outputs produced**
- plugin/skills/taskmd/SKILL.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Sent to a document that addresses it, stated against contents not title | **met** | The binding, and §3 step 1 is the measurement: `adopt.md` contains *migrat* zero times, the GitHub binding carries a section on what is gone |
| `adopt.md` no longer named for a condition it does not cover, with measured evidence | **met** | Its row now reads "The project has no tasks yet". The evidence is the count, not a reading |
| Table and refusal message point the same way, checked by reading both | **met** | §3 step 4, quoted side by side. They disagreed before and agree now |
| `SKILL.md`'s `description` untouched | **met** | Only the two table rows were opened; made a `plan` decision so it could not happen by accident |
| The table does not grow a row, or the reason is stated | **met** | It does not. The condition moved to a row that already existed, which is the answered question's whole point |

**Open questions, re-read before closing** (procedure step 5)

§1's only question is answered, and the answer refuses the premise both its options shared. Two
corrections to §1's own wording are recorded there — the *mentions bindings once* figure and the
*four rows* arithmetic — with a note that neither changes the conclusion. Nothing here is addressed
to anyone else.

**Child fix tasks raised**
- none

## Log


| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | `specify` through `review` in one session under the standing grant. **The answer refuses the premise both options shared** — that the migrated case needs a new destination. The load table already carried the right one, so the condition moved from the `adopt.md` row to the binding row and no row was added, which is what splitting was going to buy at the price of a row. `adopt.md` contains the string *migrat* zero times in 92 lines, and that count is the evidence rather than a reading of it. The table and the tool's refusal message now say the same thing, read side by side in §3. Two of §1's own figures were stale and are corrected in place without disturbing its conclusion — including its row count, which T-005 had moved earlier the same day. |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question. Small, and raised anyway because the skill is the *only* survivor a migrated project pays for and this is the one place it misdirects. Found by reading `SKILL.md` against `adopt.md` rather than by a failure — nothing reports it, and nothing could. **Not covered by any standing authorisation.** |
