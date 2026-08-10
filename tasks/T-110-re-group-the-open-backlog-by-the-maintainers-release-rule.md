---
id: T-110
title: Re-group the open backlog by the maintainer's release rule
type: admin
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-026, T-086, T-109]
work_package: v0.2
owner: maintainer
business_value: high
effort: m
created: 2026-08-10
updated: 2026-08-10
deliverables: []
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

> **v0.2** — all dependencies, plus minor and moderate-sized fixes.
> **v0.3** — bigger tasks and new features.

This replaces the principle T-086 grouped by, which was **theme**: v0.2 was *the tool holds up in a
project that is not this one*, v0.3 *the claims are proven off this machine, and the method's
documents settle*. Grouping by size and dependency instead is not a re-phrasing of those sentences —
it cuts across them, which is why the purpose statements are in scope below and not just the clauses.

**Why this one**
Two things are wrong at once and the second is the reason to do them together. The grouping predates
the rule. And **eleven open tasks sit in a milestone no exit clause requires** — measured on
2026-08-10 against the current membership:

```text
v0.2  T-021 T-024 T-078 T-087 T-090 T-097 T-098 T-109   (8)
v0.3  T-035 T-093 T-108                                 (3)
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
  rewriting what a record says about the past, and v0.1's content is defined as *every task that was
  closed when it shipped* — a definition that stops meaning anything if closed tasks can be re-filed.
- Out: **tagging.** `v0.3.0` is untagged by a live choice; a milestone here is what work is grouped
  into, not a promise about a release.
- Out: **a third milestone.** If the rule leaves v0.2 carrying most of the backlog, that is the
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
  already shipped — so `fix` and `decision` both count, at `xs`, `s` or `m`.* The current v0.2 already
  holds three `decision` tasks and the `audit` umbrella, so a size reading ratifies where four tasks
  already sit. *Alternative: read the word literally as `type: fix`* — then T-021, T-030, T-109 and
  T-026 all leave v0.2, which evicts the umbrella that v0.2's own exit clause is written around.
- **What counts as a dependency?** *Recommended: a task another **open** task cannot close without —
  today exactly T-026's five open children (T-029, T-030, T-031, T-032, T-033), since no open task
  carries an unsatisfied `blocked_by`.* That makes the first clause of the rule bite on a real chain
  rather than on nothing. *Alternative: count every `blocked_by` edge, including the two pointing at
  closed tasks* — T-005 and T-047 would join on edges that are already satisfied, which reads
  "dependency" as history rather than as a constraint.
- **When the rule sends a task out of the milestone whose exit clause names it, which wins?** Five
  are affected — T-036, T-047, T-082, T-085, T-107 — all `s` or `m`, all named in a v0.3 clause.
  *Recommended: the rule wins and the clause moves with the task.* The clauses are derived from
  membership; the rule is the principle that produces it, and a clause that pins a task in place
  would make the grouping size-based for some tasks and thematic for others. The consequence is
  visible and worth saying: v0.3's headline half *the method's documents settle* was T-036 and T-047,
  so it does not survive them and the purpose statement is rewritten rather than trimmed.
  *Alternative: a task stays where a clause names it* — cheaper by five edits, and it re-creates
  exactly the mismatch this task exists to remove.
- **Do `analysis` and `research` tasks of moderate size go to v0.2?** T-005, T-020 and T-085 are
  `m`, `m` and `s`. *Recommended: no — they are v0.3, because they prove a claim or add a capability
  rather than correct something, and T-085 cannot be run on this machine at all.* Under the first
  question's recommendation this needs no special case: none of the three corrects anything already
  shipped. *Alternative: send T-085 to v0.2 on its `s` estimate alone* — it is cheap only for
  whoever has the second machine, and a milestone none of whose clauses can be reached here is not
  what "minor" describes.

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
| 2026-08-10 | → proposed | Raised to carry out the maintainer's release rule of the same day, which had no task and lived only in a machine-local handoff. Written down here because that is the input the work is judged against and a gitignored file is not a home. `admin` because nothing about the product changes — this is the backlog's own filing. `high` because until it lands every answer to "what is in v0.2" is wrong, and two milestone clauses have already been widened twice to avoid the question. `m` for 26 front-matter edits plus a rewrite of both purpose statements and both clause sets; the edits are trivial and the rewrite is not. The eleven unpaired tasks were re-derived here rather than carried over from the status review's ten — the review was right when it counted, and T-108 arrived afterwards. **Specify only, and stopped here**: the resumption note asking for the restructure is context and not authorization to run further phases (METHOD §3.1), and the four questions below are the owner's, not the writer's. |
