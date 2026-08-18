---
id: T-110
title: Re-group the open backlog by the maintainer's release rule
type: admin
status: done
phase: review
parent: null
blocked_by: []
related: [T-026, T-086, T-109]
work_package: M2
owner: maintainer
business_value: high
effort: m
created: 2026-08-10
updated: 2026-08-10
deliverables: [tasks/README.md]
adopter_visible: no
---

# T-110 — Re-group the open backlog by the maintainer's release rule

## 1. Specify

**Outcome**
Every open task's `work_package` follows the maintainer's rule of 2026-08-10, and `tasks/README.md`
*Releases* describes the two milestones in terms the resulting membership actually satisfies: no open
task sits in a milestone none of whose exit clauses require it, and no clause asks for an outcome no
task delivers. The two halves land in one edit, because a clause and its membership that move
separately describe different sets in between.

**The rule, as given**
Recorded here because this is its only durable home — it was stated in a session handoff, and those
are machine-local and gitignored.

> **M2** — all dependencies, plus minor and moderate-sized fixes.
> **M3** — bigger tasks and new features.

This replaces the principle T-086 grouped by, which was **theme**: M2 was *the tool holds up in a
project that is not this one*, M3 *the claims are proven off this machine, and the method's
documents settle*. Grouping by size and dependency instead is not a re-phrasing of those sentences —
it cuts across them, which is why the purpose statements are in scope below and not just the clauses.

**Why this one**
Two things are wrong at once and the second is the reason to do them together. The grouping predates
the rule. And **eleven open tasks sit in a milestone no exit clause requires** — measured on
2026-08-10 against the current membership:

```text
M2  T-021 T-024 T-078 T-087 T-090 T-097 T-098 T-109   (8)
M3  T-035 T-093 T-108                                 (3)
```

The status review that first counted this reported ten, and both numbers are right as dated: T-108
was raised later the same day. It is the count that keeps moving, not the defect — the two clauses
have already been widened twice rather than the tasks moved, which is the pressure this task exists
to take off them.

**Scope**
- In: the `work_package` field of every **open** task, all 26 of them, including this one.
- In: the *Releases* section of `tasks/README.md` — both purpose statements and both sets of exit
  criteria, rewritten to match the membership the rule produces.
- In: the eleven above. Each either moves, or the milestone it is in gains a clause requiring it —
  and which of the two happens is decided per task, not by a blanket choice.
- Out: **closed tasks' `work_package`.** They record what shipped. METHOD §1 rule 5 forbids
  rewriting what a record says about the past, and M1's content is defined as *every task that was
  closed when it shipped* — a definition that stops meaning anything if closed tasks can be re-filed.
- Out: **tagging.** `v0.3.0` is untagged by a live choice; a milestone here is what work is grouped
  into, not a promise about a release.
- Out: **a third milestone.** If the rule leaves M2 carrying most of the backlog, that is the
  rule's answer and not a signal to invent v0.4.
- Out: **T-109's own question.** The previous handoff proposed settling it in the same pass on the
  grounds that it is `xs` and touches the same front-matter. That premise expired the day it was
  written: the maintainer's steer raised it to `s` and put a research step in front of it, so it is
  no longer a free rider on this pass. Its `work_package` moves here if the rule says so; its
  answer does not.
- Out: the stale `type` row in `tasks/_task-template.md`, which offers five values where the schema
  has seven. Noticed while reading the template for this task; it is already inside
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s scope, which names that file
  as an input, so it is recorded here and not raised again.

**Inputs**
- The rule above, and `tasks/README.md` *Releases* as it stands.
- Each open task's `type`, `effort` and edges — read from the files, never from a list kept anywhere.
- [`../docs/SCOPE.md`](../docs/SCOPE.md) §9, the definition of done, which is closed: both milestones
  are beyond it, so neither clause can lean on it.
- [T-086](T-086-group-the-backlog-into-release-milestones.md), which grouped this backlog the first
  time and whose *why* is the thing being superseded.

**Acceptance criteria**
- [ ] Every open task's milestone is justified by exactly one clause of the rule — *it is a
      dependency*, *it is a minor or moderate fix*, *it is bigger*, *it is a new feature* — and the
      justification is recorded per task, so a reader can disagree with one without re-deriving all 26
- [ ] No open task sits in a milestone none of whose exit clauses require it; the pairing of task to
      clause is stated, and the count of unpaired tasks is **zero** rather than smaller
- [ ] No exit clause survives that no open or closed task delivers
- [ ] `tasks/README.md` still states that which tasks are in a release is not written there, and its
      prose still names no task
- [ ] `./plugin/bin/taskmd index` regenerated, and `check` clean on this repository
- [ ] The new split is stated as counts read off the regenerated index, not as an intention

**Open questions**

- **Does *minor and moderate-sized fixes* mean `type: fix`, or any small-to-moderate work?**
  *Recommended: size is the test, and the work qualifies if its outcome corrects or settles something
  already shipped — so `fix` and `decision` both count, at `xs`, `s` or `m`.* The current M2 already
  holds three `decision` tasks and the `audit` umbrella, so a size reading ratifies where four tasks
  already sit. *Alternative: read the word literally as `type: fix`* — then T-021, T-030, T-109 and
  T-026 all leave M2, which evicts the umbrella that M2's own exit clause is written around.
- **What counts as a dependency?** *Recommended: a task another **open** task cannot close without —
  today exactly T-026's five open children (T-029, T-030, T-031, T-032, T-033), since no open task
  carries an unsatisfied `blocked_by`.* That makes the first clause of the rule bite on a real chain
  rather than on nothing. *Alternative: count every `blocked_by` edge, including the two pointing at
  closed tasks* — T-005 and T-047 would join on edges that are already satisfied, which reads
  "dependency" as history rather than as a constraint.
- **When the rule sends a task out of the milestone whose exit clause names it, which wins?** Five
  are affected — T-036, T-047, T-082, T-085, T-107 — all `s` or `m`, all named in a M3 clause.
  *Recommended: the rule wins and the clause moves with the task.* The clauses are derived from
  membership; the rule is the principle that produces it, and a clause that pins a task in place
  would make the grouping size-based for some tasks and thematic for others. The consequence is
  visible and worth saying: M3's headline half *the method's documents settle* was T-036 and T-047,
  so it does not survive them and the purpose statement is rewritten rather than trimmed.
  *Alternative: a task stays where a clause names it* — cheaper by five edits, and it re-creates
  exactly the mismatch this task exists to remove.
- **Do `analysis` and `research` tasks of moderate size go to M2?** T-005, T-020 and T-085 are
  `m`, `m` and `s`. *Recommended: no — they are M3, because they prove a claim or add a capability
  rather than correct something, and T-085 cannot be run on this machine at all.* Under the first
  question's recommendation this needs no special case: none of the three corrects anything already
  shipped. *Alternative: send T-085 to M2 on its `s` estimate alone* — it is cheap only for
  whoever has the second machine, and a milestone none of whose clauses can be reached here is not
  what "minor" describes.

## 2. Plan

**Authorisation.** The maintainer accepted all four recommendations above and asked for the full
lifecycle on this task, on 2026-08-10. Recorded here per METHOD §3.1: it covers `plan`, `implement`
and `review` **of T-110 only**, and nothing about the tasks whose `work_package` this moves.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Allocate all 27 open tasks by the accepted rule, one recorded reason each | §3 *Allocation* |
| 2 | Move `work_package` on every task the allocation relocates, and bump its `updated` | the moved task files |
| 3 | Rewrite `tasks/README.md` *Releases* — both purpose statements and both criteria sets, in one edit | `tasks/README.md` |
| 4 | Regenerate the index and validate | `index` and `check` output |
| 5 | Pair every open task to a criterion of its milestone and count what is left unpaired | §4 |

## 3. Implement

**Allocation, 2026-08-10.** Each open task appears once, under the clause of the rule that placed it.

| Reason | Tasks |
| :--- | :--- |
| Dependency — an open task cannot close without it (T-026's unresolved findings) | T-029, T-030, T-031, T-032, T-033 |
| Head of that one chain — see D2 | T-026 |
| Minor or moderate correction: `xs`–`m`, and its outcome corrects or settles something already shipped | T-021, T-023, T-024, T-035, T-036, T-047, T-078, T-082, T-087, T-090, T-091, T-097, T-098, T-107, T-109, T-110 |
| Bigger — `l` | T-093 |
| A capability added or a claim proven, rather than a correction | T-005, T-020, T-085, T-108 (also `l`) |

Five moved, all from M3 to M2: T-035, T-036, T-047, T-082, T-107. Nothing moved the other way.

**Decisions & assumptions**

- **D1 — the four answers are the owner's, taken as given.** Accepted 2026-08-10. Size is the test
  and `fix` and `decision` both qualify; a dependency is what an **open** task cannot close without;
  where the rule and a naming clause disagree the rule wins and the clause moves; moderate `analysis`
  and `research` stay in v0.3. The rejected alternatives are recorded in §1 beside each question and
  are not repeated here.
- **D2 — T-026 stays in M2 although it is `l`, and this is the one placement the rule does not
  make on its own.** Two reasons. Its `l` is the audit that was already performed; what remains is
  closing when its findings close, and re-estimating a task to make a filing rule come out right
  would be the tail wagging the dog. And a milestone holding all five of a task's open children but
  not the task would close with an umbrella open that has no unresolved findings — an incoherent
  state, and one that D1's first answer was justified by avoiding. *Rejected: send T-026 to M3 on
  its estimate* — arithmetically clean, and it separates a parent from every one of its children.
- **D3 — M2's exit criterion is its membership, not a list of outcomes.** The substantive change,
  and the reason the eleven unpaired tasks existed. A prose list of outcomes is a second copy of the
  membership that each task's `work_package` already carries, so it drifts the moment a task is
  added — which is what happened twice, both times resolved by widening the prose. The project's own
  design rule says store the forward edge and derive the rest; the *Work Package* column is that
  derivation, so the criterion points at it. *Rejected: write out twenty-two outcomes* — it satisfies
  the letter of the acceptance criterion, restores the drift on the next task raised, and is a task
  list in prose in everything but name, which the file's own preamble forbids. *Also rejected: a
  catch-all clause appended to the existing list* — that is the widening move a third time.
  **[T-086](T-086-group-the-backlog-into-release-milestones.md) predicted this cost and was right.**
  Its Step 1 rejected splitting by effort because it *produces two releases nobody can describe*, and
  that is precisely what happened: M2 can no longer be described by an outcome, only by a size. The
  rule came from the maintainer, so the cost is accepted rather than discovered — but it was a known
  cost and is recorded here as one, not as a surprise.
- **D4 — T-087 and T-082 are corrections, not features, and stay or move accordingly.** Both are
  `s` and typed `fix`, and both were read against D1's second half rather than their size alone.
  T-087 makes `list` filter on a field the schema already promises is carried and displayable — a
  broken promise, not a new one. T-082 makes a sentence in the shipped GitHub binding stop being
  false. The capability that *uses* T-082 is T-108, which is `l` and stays in v0.3.
- **D5 — no closed task was touched**, per §1 *Scope*. M1's content is defined as every task closed
  when it shipped, and the closed M2 tasks still carry the outcomes the retired clauses named, so
  removing those clauses lost nothing that was not already in the Closed table.
- **Assumption — the eleven count is the defect, not the number.** It was re-derived here at 11 and
  the review that found it reported 10. Neither was reconciled to the other; both are correct as
  dated, and the point of the work is that the count can move at all.

**Outputs produced**
- `tasks/README.md` — *Releases* rewritten; the generated block below the marker is regenerated.
- `tasks/T-035-…`, `T-036-…`, `T-047-…`, `T-082-…`, `T-107-…` — `work_package` and `updated`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every open task's milestone justified by one clause of the rule, recorded per task | met | §3 *Allocation*; each of the 27 appears exactly once, so one row can be disputed alone |
| No open task in a milestone none of whose criteria require it — unpaired count zero | met | M2: all 22 by its single criterion. M3: T-020 byte-identical, T-085 fresh machine, T-005 handoff binding, T-093 section reference, T-108 GitHub Issues. **Achieved by changing what kind of criterion M2 has (D3), not by pairing the old list** |
| No exit clause survives that no open or closed task delivers | met | The retired M2 clauses were delivered by T-025, T-099, T-100, T-101, T-102; all closed and all still filed `M2`, so membership carries them |
| README still says membership is not written there, and its prose names no task | partly | The first half holds. The second does not, literally: the prose now links **T-110** as the record of the change. Kept deliberately — the criterion was aimed at membership leaking into prose, and a pointer to where the rationale lives is the opposite of that. Recorded rather than softened |
| `index` regenerated and `check` clean | met | `OK - 110 task(s) … 1 index file(s), 138 document(s), 1065 link(s)` |
| The new split stated as counts read off the regenerated index | met | **22 open in M2 including this task, 5 in M3** — from 16 / 10 before, and 21 / 5 once this task closed |

**Child fix tasks raised**
- none. Two things were noticed and both already have homes: the stale `type` row in
  `tasks/_task-template.md` is inside [T-032](T-032-repair-the-audit-template-and-validate-templates.md),
  and `taskmd list --work_package M2` exiting 2 — hit while trying to count this task's own result —
  is exactly [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md), which is what it was
  raised for. Neither is re-raised.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | (no change, closed) | **Reconciled against a commit that landed on `origin/master` while this task was being worked.** `6a8b316` amended `docs/SCOPE.md` non-goal 8 to carve out exactly the direction [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) takes, settled that task's two questions and raised it `l` → `xl`. So the sentence this task had just written into *Releases* — that T-108 contradicts non-goal 8 and cannot be planned until the maintainer amends it — was false within minutes of being committed, and is replaced by a pointer to the carve-out. The allocation is untouched: `xl` is further into M3, not out of it. Worth recording as a shape rather than an incident — a repository with more than one session working it can invalidate a finished task's output between the write and the push, and nothing in the lifecycle looks for that. The only reason it was caught is that `git status` reported one commit ahead where two were expected. |
| 2026-08-10 | (no change) | **The first draft of the rewrite re-created the defect it removed**, and it is annotated rather than quietly repaired. Three derived counts were written into the *Releases* prose — that M2 holds twenty-two tasks, that M3 holds five, and that the umbrella has five findings still open — every one of them a second copy of what the generated table two paragraphs below already carries. The first went stale within the same session, when this task closed and 22 became 21. So the prose now says *everything else*, *few enough*, and *its open children, in the table below*. Worth recording because the drift arrived inside the paragraph arguing against it, written by whoever had just made the argument: a number is the easiest thing to reach for when a sentence wants to sound concrete, and D3 does not stop the reflex, it only says where the number belongs. |
| 2026-08-10 | → done | Full lifecycle in one session, on the maintainer's authorisation recorded in §2. Five tasks moved M3 → M2, and the split is now 22 / 5 from 16 / 10. The substantive change is not the moves: it is **D3**, which makes M2's exit criterion its membership instead of a list of outcomes. That list was a second copy of the membership each task's `work_package` already carries, which is why it drifted twice and why eleven open tasks sat outside it — the same defect the file's own preamble was written to prevent, appearing in the prose the preamble introduces. What it costs is stated in the file rather than buried: grouping by size cannot claim anything about the product, so neither milestone asserts one any more. One acceptance criterion is recorded as **partly met** rather than softened — the prose names T-110, which the criterion forbade and which is worth keeping. |
| 2026-08-10 | → proposed | Raised to carry out the maintainer's release rule of the same day, which had no task and lived only in a machine-local handoff. Written down here because that is the input the work is judged against and a gitignored file is not a home. `admin` because nothing about the product changes — this is the backlog's own filing. `high` because until it lands every answer to "what is in M2" is wrong, and two milestone clauses have already been widened twice to avoid the question. `m` for 26 front-matter edits plus a rewrite of both purpose statements and both clause sets; the edits are trivial and the rewrite is not. The eleven unpaired tasks were re-derived here rather than carried over from the status review's ten — the review was right when it counted, and T-108 arrived afterwards. **Specify only, and stopped here**: the resumption note asking for the restructure is context and not authorization to run further phases (METHOD §3.1), and the four questions below are the owner's, not the writer's. |
