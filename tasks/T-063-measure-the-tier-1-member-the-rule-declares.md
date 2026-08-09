---
id: T-063
title: Measure the tier-1 member the rule declares
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-047, T-028]
work_package: v0.1
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-063 — Measure the tier-1 member the rule declares

## 1. Specify

**Outcome**
The command `CLAUDE.md` names for checking the tier-1 budget measures everything `CLAUDE.md` says is
in tier 1 — so the rule can be failed by the thing it was written to catch.

**Why this one**
Raised as **F-6** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 4. `CLAUDE.md` states two things a few lines apart:

1. tier 1 is *"this file **plus the taskmd `description`**"* — membership defined as a property, which
   is what [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) proved correct by
   measuring a session that was handed it;
2. *"both sides are counted from the tree (`wc -l CLAUDE.md reference/TASK-WORKFLOW.md`), so
   re-measuring never rewrites the rule"* — a command that counts one file.

The second cannot see the member the first just added. Measured 2026-08-09:

```
wc -l CLAUDE.md reference/TASK-WORKFLOW.md
164 CLAUDE.md
173 reference/TASK-WORKFLOW.md
```

The description is a further **397 characters**, which at this file's own 83-character average is
about five lines — so the stated 9-line margin is really about four. `CLAUDE.md` half-acknowledges
this (*"with less room than a count of this file shows"*) and then attributes the shortfall to the 26
lines [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) owes, not to
the description at all.

**What is new against T-047.** T-047 owns the move and the cut, and its log already records that tier
1 grows whenever a task closes. Two things it does not have:

- **The rule's own check is blind**, which is a defect in `CLAUDE.md` rather than a number T-047 has
  to chase. Nothing about re-measuring fixes a measurement that omits a member.
- **Tier 1 has grown 153 → 164** since T-047's last recorded measurement on 2026-08-08, so its
  projection moves from 153 + 26 = 179 (over by six) to 164 + 26 = 190 (over by seventeen). That is
  not a correction to T-047's arithmetic; it is a change in what that task has to find room for, and
  it arrived from ordinary reconcile edits with nobody touching the budget.

**Requirements served**
R-21 (`docs/SCOPE.md`) — *falsified by measuring a session*, which is exactly what a blind measurement
prevents; §1 *Token cost*.

**Scope**
- In: how the tier-1 side of the comparison is counted, given that one member is a file and one is a
  character count served by the harness.
- In: whether the rule's stated command stays a command someone can run, which is the property that
  keeps the rule from needing a written number.
- Out: **what leaves tier 1.** T-047's, explicitly, and this task must not pre-empt it — a
  measurement that also chooses the cut is the failure
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) declined to make.
- Out: the bound itself and the choice of `reference/TASK-WORKFLOW.md` as the comparator, both
  settled in T-028.
- Out: moving §3.1 and §3.3, which is T-047's whole content.

**Inputs**
`CLAUDE.md` *Working method*, `plugin/skills/taskmd/SKILL.md` front-matter (the description),
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md),
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) and its four
re-measurement log entries, [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-6.

**Acceptance criteria**
- [ ] The stated check counts every declared member of tier 1, and is a command a reader can run
- [ ] Running it today produces a result, and that result is stated — pass or fail, both count
- [ ] A character count and a line bound are reconciled explicitly; the conversion is written down
      once rather than left to whoever next re-measures
- [ ] Adding a second served skill would change the measured figure — the check tests the property,
      not a list of two files
- [ ] T-047's open question is untouched: nothing here says what should leave

**Open questions**
- ~~**Does the bound become a character count on both sides?**~~ **Decided at `plan` on 2026-08-09:
  yes.** The question was posed as exactness against the cost of invalidating recorded figures. It
  turned out not to be a trade at all — measuring both units first showed the line count was not
  merely imprecise, it was **giving the wrong answer**. See §3 D1.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure both sides in **both** units before choosing one, so the open question is answered by what the units say rather than by which is tidier | The two figures, and the density that explains them |
| 2 | Decide the unit on that evidence | §3 D1 |
| 3 | Write a check that derives tier-1 membership from the tree — not a list of two paths — so the next served skill joins it with nothing edited | The command in `CLAUDE.md` |
| 4 | Run it and state the result, pass or fail | §3 step 3 |
| 5 | Prove criterion 4 by adding a second skill and watching the figure move, then removing it | The transcript |
| 6 | Keep the verdict in `CLAUDE.md` and the **numbers** out of it, so the file does not acquire a figure that goes stale | The edited paragraph |

**Why step 1 comes before step 2, and not after.** The open question reads as a matter of taste —
lines are conventional here, characters are exact. Choosing first and measuring afterwards would have
produced a defensible answer either way and missed the thing that actually settles it.

## 3. Implement

**Decisions & assumptions**

- **D1 — characters, on both sides** — 2026-08-09. Measured first, and the two units disagree about
  whether the rule passes:

  ```
  wc -l   CLAUDE.md 164   reference/TASK-WORKFLOW.md 173      passes, by 9 lines
  wc -c   CLAUDE.md 11451 reference/TASK-WORKFLOW.md 7846     fails, by 3605 characters
  ```

  The cause is density, not rounding. `CLAUDE.md` runs at **69.8 characters a line** against the
  comparator's **45.4** — 29 blank lines out of 164 against 47 out of 173. A line count charges a
  blank line the same as a full one, so it **flatters the denser document**, which is exactly
  backwards for a rule about what a turn costs. The line figure was not an approximation of the right
  answer; it was the wrong answer.

  That disposes of the recorded cost. Invalidating T-028's and T-047's line figures is a real loss and
  it was the argument for staying with lines — but those figures were measuring the wrong thing, so
  keeping them buys continuity with a mistake.

  *Rejected: lines on both sides, with the description converted at this file's average width.* It
  keeps every prior figure comparable and it is what criterion 3's wording anticipated. It also keeps
  the density bias, which is larger than the conversion it would have fixed: the description is worth
  about 5 lines, and the bias is worth about 80.

- **D2 — membership is derived, the verdict is stated, the numbers are not** — 2026-08-09.
  `CLAUDE.md` keeps *"No number is written here"* and gains a command that reads
  `plugin/skills/*/SKILL.md`, so tier 1's membership is a property of the tree in the check as well as
  in the prose. The verdict — that it does not pass — replaces the old *"It passes"* in kind: the file
  already carried a verdict, so this adds no maintenance it did not have. Today's figures live in this
  record, which is dated, rather than in a file that is not.

- **Recorded rather than glossed: this task made tier 1 bigger.** The paragraph grew by 279
  characters, because a check that reads the tree does not fit where a two-path `wc -l` did. Tier 1
  went from 11,924 to 12,203 against a bound of 7,919. That is the honest cost of making the rule
  checkable, and it is T-047's to absorb along with everything else.

### Steps 3–4 — the check, and today's result

```bash
{ cat CLAUDE.md; sed -n 's/^description: //p' plugin/skills/*/SKILL.md; } | wc -c; wc -c < reference/TASK-WORKFLOW.md
```

```
12203      tier 1: this file plus every served skill's description
 7919      reference/TASK-WORKFLOW.md
```

**It does not pass — tier 1 is 1.54× the flat single-document alternative.** Stated plainly because
the old check said the opposite: under `wc -l` this rule passed with nine lines to spare, every time
anyone ran it, while the thing it exists to bound was half as large again as its limit.

### Step 5 — criterion 4, proved by adding a member

A second skill was created, the check re-run, and the skill removed:

```
one skill    12203
two skills   12315      +112, the probe's own description
one skill    12203      probe removed; git status clean
```

The figure moved with the tree and with nothing edited in `CLAUDE.md`, which is the property the
paragraph claims for tier 1 and which the retired command could not have.

**Outputs produced**
- `CLAUDE.md` *Working method* — the check now counts every declared member, in the unit the budget
  is actually about, and says what it currently says

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The stated check counts every declared member of tier 1, and is a command a reader can run | met | §3 step 3. Membership comes from `plugin/skills/*/SKILL.md` rather than from a path list, so it counts the declared property and not two files |
| Running it today produces a result, and that result is stated — pass or fail, both count | met | §3 step 4 — **fail**, 12,203 against 7,919. The verdict is in `CLAUDE.md`; the figures are here, where they are dated |
| A character count and a line bound are reconciled explicitly; the conversion is written down once | met | Reconciled by retiring the line bound rather than by converting to it, with the reason measured: a line count flatters a dense file by ~80 lines' worth, against a description worth ~5. The criterion anticipated a conversion; D1 records why there is none instead of quietly re-reading it |
| Adding a second served skill would change the measured figure | met | §3 step 5 — not reasoned, run: 12,203 → 12,315 → 12,203 |
| T-047's open question is untouched: nothing here says what should leave | met | No line of `CLAUDE.md` was removed or moved. What this task changed T-047's problem *into* is recorded above and is a fact about the measurement, not a proposal about the cut |

**Child fix tasks raised**
- none. The failure this exposes is [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)'s
  by this task's own scope, and that task already exists and already owns the cut. Raising a second
  one would split an owner. What T-047 inherits is a different problem from the one it was sized
  against — not 26 lines to find room for, but a tier already over its bound before those lines
  arrive — and the soft edge between the two tasks is how a reader of either meets this record.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met, and the headline result is not the one the task expected: **tier 1 does not pass its own bound, and never did.** Measuring both units before choosing one turned the open question from a matter of taste into a matter of fact — `wc -l` says 164 against 173 and passes; `wc -c` says 12,203 against 7,919 and fails by more than half again. The cause is density, not rounding: a line count charges a blank line the same as a full one, so it flatters the denser document, and this file runs at 69.8 characters a line against the comparator's 45.4. The retired check was therefore not an approximation of the right answer, which is what dissolved the argument for keeping lines — continuity with a mistake. Membership is now derived from `plugin/skills/*/SKILL.md`, proved by adding a second skill and watching the figure move with nothing edited here. Recorded rather than glossed: this task made tier 1 279 characters bigger, because a check that reads the tree does not fit where a two-path `wc -l` did. |
| 2026-08-09 | → in_progress | Plan puts the measurement before the decision on purpose. The open question reads as a choice between exactness and continuity, and either answer would have been defensible if argued rather than measured — which is how the wrong unit survived this long. |
| 2026-08-09 | → specified | Criteria stand as raised. Criterion 5 is the one doing work: it keeps this task from pre-empting T-047, which is the failure T-028 declined to make. |
| 2026-08-09 | → proposed | Raised as F-6 from the T-059 audit, clauses 1 and 4. Measured before write-up: 164 against 173, with a 397-character member the named command cannot see. `high` because it is a rule paid on every turn whose check cannot fail, and because T-047 is currently sized against a figure that moved by eleven lines without anyone editing the budget. Deliberately narrow: what leaves tier 1 stays T-047's, since a measurement that also chooses the cut is what T-028 refused to do. |
