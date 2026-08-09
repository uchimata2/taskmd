---
id: T-028
title: Budget the whole always-loaded context, not one file
type: decision
status: done
phase: review
parent: T-026
blocked_by: [T-027]
related: [T-015, T-003]
work_package: v0.1
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-07
deliverables:
  - CLAUDE.md
  - plugin/skills/taskmd/docs/METHOD.md
---

# T-028 — Budget the whole always-loaded context, not one file

## 1. Specify

**Outcome**
The line budget `CLAUDE.md` sets governs everything that is actually loaded on every turn, so that
the test it states — *a spine that costs more than the flat version has inverted the point of
splitting it at all* — is a test the project can pass or fail rather than one it cannot see.

**Why this one**
Raised as **F-2** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 3 and 4. `CLAUDE.md` sets a 150-line limit on `docs/METHOD.md`, justified as sitting below
`reference/TASK-WORKFLOW.md` — the flat, single-document alternative — with headroom. The
justification's arithmetic is correct; the measurement is of one file:

| File | Lines | Loaded |
| :--- | ---: | :--- |
| `CLAUDE.md` | 139 | every turn |
| `docs/METHOD.md` | 147 | every turn, by its own statement |
| **Total always-loaded** | **286** | |
| *(re-measured 2026-08-06: `CLAUDE.md` 145, total **292** — T-034 added six lines to it)* | | |
| `reference/TASK-WORKFLOW.md` — the flat alternative the limit is set against | 173 | — |

So by the stated test, the split has already inverted the point it was meant to protect — the budget
just does not measure the quantity it names. `docs/METHOD.md` is meanwhile at 147 of its 150, which
means the constraint is about to bind hardest on the file that is not the problem, and the next
addition to the spine will be refused for the wrong reason.

**This is not an argument that the split was wrong.** Progressive disclosure is R-21 and
[T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) did real work. The finding
is that the budget has one file in scope and two files in the cost.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Token cost*, which is a falsifiable property rather than a decoration.

**Scope**
- In: what the budget counts, what number it is set to, and where that is written.
- In: re-measuring after [T-027](T-027-give-the-design-rule-one-home.md) lands, since removing a
  duplicated section from `CLAUDE.md` changes the total this task is budgeting.
- Out: moving content out of either file. That is the *consequence* of a budget, and belongs to
  whichever task the budget forces. Deciding the measure first is what stops the cut being chosen to
  fit a number nobody agreed.
- Out: `docs/SCOPE.md`, `docs/BRIEF.md` and the `docs/method/` files — they are read on demand, not
  every turn, which is the distinction the budget exists to draw.

**Inputs**
`CLAUDE.md` §*Working method*, `docs/METHOD.md` §*Load on demand*, `docs/SCOPE.md` §1 and R-21,
[T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-2.

**Acceptance criteria**
- [ ] The budget names the **set** of always-loaded files, not one of them, and the set is checkable
      against the repository rather than being a list someone must remember to update
- [ ] The stated comparison against the flat alternative is one the project currently passes, or the
      gap is stated as a known, dated debt with the task that will close it — an unmet budget that
      reads as met is worse than no budget
- [ ] The number and its justification live in exactly one place, and the two do not have to be
      updated together
- [ ] Re-measured after T-027, so the decision is taken against the total the project will actually
      have rather than today's
- [ ] The tier boundary is stated where a reader of either file will meet it, and `docs/METHOD.md`
      no longer describes itself as loaded on every turn — the sentence that made the budget
      unmeasurable is the sentence that has to change
      <br>*Added 2026-08-06 with Q1's answer, which changed the outcome from "what does the budget
      count" to "how many tiers are there". Criteria 1–4 stand as written and are unaffected.*

**Open questions**
- None. **Q1 — is `CLAUDE.md` in the budget's scope? — answered on 2026-08-06: yes, and it should
  end up being the only thing in it.** The maintainer delegated the decision, directing that the
  sibling `handoff` plugin be studied first and a better approach taken if one was found. One was.

  **What the sibling actually does.** `handoff.core.md` describes itself as *"the always-loaded
  spine"* and is 282 lines — but that is not what a session always loads. The artifact that is always
  present is the agent stub, `agents/claude.SKILL.md`, at **31 lines**. The core loads on
  *activation*; a flow file (71 or 92 lines) loads on *mode*. **Three tiers, and the phrase
  "always-loaded" is relative to the skill being active, not to the session.**

  This project took the phrase without the tier. `docs/METHOD.md` says it is loaded on every turn and
  means it literally — including every turn containing no task work at all. That is why the budget
  reads as unwinnable: it is not measuring a spine against a flat alternative, it is measuring **two
  spines** against one.

  **The decision: budget tier 1, and make tier 1 one file.**

  | Tier | Loaded | Holds |
  | :--- | :--- | :--- |
  | 1 | every turn | Project conventions, and the conduct rules that must bind *before* the agent knows it is doing task work |
  | 2 | when task work starts | `docs/METHOD.md` — lifecycle, edges, audit, where facts live |
  | 3 | when a phase begins | `docs/method/*.md` — already this shape |

  Tier 1 is checkable against the repository rather than being a list to maintain (criterion 1): it
  is *what the harness loads without being asked*, which is a property of the tree, not an
  enumeration. Tier 3 already exists and is untouched.

  **The counter-argument, which is real and constrains the answer.** METHOD §3.1 (*never
  auto-advance*) and §3.3 (*surface what you discover*) apply on every turn by their own statement,
  and an agent that has not yet realised it is doing task work will not have loaded tier 2. Those
  rules — roughly a dozen lines — stay in tier 1. Everything else in `docs/METHOD.md` is only needed
  once a task is in hand. A tiering that demotes the conduct rules is the one way this decision is
  wrong, and it is the thing to check when the move is made.

  *Rejected: widen the budget to cover both files and cut content until 292 fits under 173.* It
  accepts the two-spine structure as given and pays for it in deletions, which is the cut chosen to
  fit a number that this task's own scope warns against.

  *Rejected: budget the two files separately, with a limit each.* Two numbers that must be updated
  together whenever content moves between them — criterion 3 forbids exactly that.

- **Sequencing, not a blocker.** The loader for tier 2 is the skill
  ([T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)); a soft edge records it.
  This task decides the measure and does not move content, so it does not wait on T-003 — but the
  task that performs the move will, and should carry a dependency edge rather than a sentence.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what tier 1 *is* by observation rather than assertion: which documents a session receives without asking for them, and the membership rule that makes the set readable off the tree instead of maintained as a list. | A stated membership rule, and the set it resolves to today, recorded in §3 |
| 2 | Measure tier 1 against the content it will hold rather than the file as it stands: `CLAUDE.md` once T-027 has removed the duplicated design rule, plus the conduct rules the decision keeps in tier 1 (`docs/METHOD.md` §3.1 and §3.3). Compare the total with `reference/TASK-WORKFLOW.md`. | A table — each component, its line count, the total — and a verdict: under the flat alternative, or over it and by how much |
| 3 | Set the bound, and choose the form it is written in so that re-measuring never rewrites its justification. | A recorded decision in §3: the bound, how it is derived, and what was rejected |
| 4 | Write the budget into `CLAUDE.md` — the set, the bound, its justification, and the tier boundary a reader of tier 1 meets on arrival. If step 2's verdict was *over*, the same paragraph carries the gap as dated debt naming the task that closes it. | The edited §*Working method* |
| 5 | Replace `docs/METHOD.md`'s statement that it is loaded on every turn, and state the boundary where a reader of *that* file meets it. | The edited opening of `docs/METHOD.md` |
| 6 | Raise the task that moves the conduct rules into tier 1, carrying a dependency edge on T-003 — the loader tier 2 needs. This task decides a measure and moves no content. | A new task file, carrying the edge |

**Sequencing, and what can actually run now.** Step 1 leads because it can invalidate the rest: the
budget's whole defect is that it counts a file on the strength of that file's own claim, so the first
move is to stop asserting the set and go and look at it. There is already a reason to expect the
answer to be interesting — the project instructions a session is handed unasked appear to be
`CLAUDE.md` alone, with `docs/METHOD.md` reached through a link in it — which would make the
286/292 figure a measurement of a claim rather than of a load. That is an observation, not step 1's
result; step 1 is where it gets established or overturned, and either way the number in §1 moves.

**Only step 1 can run before T-027 closes**, which is why that is now a dependency edge rather than a
sentence in criterion 4. T-027 removes the duplicated design rule from `CLAUDE.md`, so it changes the
one quantity this task is budgeting; setting a bound against today's total and re-deriving it
afterwards is the same work twice, with a written-down number in between that was never true.
T-027 is itself at `proposed` with an open question to the maintainer, so that answer is the gate.

Step 6 is last and deliberately separate. Moving §3.1 and §3.3 into tier 1 is the one way this
decision goes wrong (§1, *the counter-argument*), and doing it inside this task would be the budget
choosing its own cut — the thing the scope forbids.

**Shape of the deliverable — decided: the budget lives in `CLAUDE.md`.** Under this task's own
decision `CLAUDE.md` *is* tier 1, so the rule is written in the file it governs and a reader meets
the boundary at the moment it starts binding them, which is criterion 5's first half.
*Rejected: `docs/SCOPE.md` §1* Token cost, where the falsifiable property is already stated — but
SCOPE is read on demand, so the reader who needs the boundary never reaches it, and the property
stays a claim about a number written elsewhere.
*Rejected: `docs/METHOD.md` §7*, the natural home while METHOD was believed to be always-loaded —
under this decision it becomes tier 2, and a budget for tier 1 stated in a tier-2 file is a rule
written where the people it binds have not loaded it.

**The bound is stated as a relation, not as a constant.** Criterion 3 asks the number and its
justification to share one home without having to be updated together, which is this project's own
design rule turned on itself: express the budget as a relation to `reference/TASK-WORKFLOW.md` — the
flat alternative it has always been justified against — so that re-measuring either file changes a
measurement and leaves the rule alone. *Rejected: a hand-set constant with the arithmetic beside it.*
That is what 150 is today, and it is precisely the pair that has to be edited together: the number
was set from a comparison, the comparison drifted, and nothing forced the number to follow.

**Output paths**
- `CLAUDE.md` — the §*Working method* budget paragraph
- `docs/METHOD.md` — its opening statement of when it is loaded
- `tasks/` — one new task file for the content move; its id is not known until step 6 raises it

## 3. Implement

**Step 1 — the suspicion was right, and it reframes every figure above.** Tier 1 is what a session
receives without asking for it. Observed: the project instructions supplied unasked are `CLAUDE.md`,
and `docs/METHOD.md` is not among them — it is reached through a link in `CLAUDE.md` and read on
demand. Enumerating every candidate a push would send returns exactly one file. So the membership
rule is *what the harness loads without being asked*, a property of the tree; and **the 286/292
figure was never a measurement of a load.** It counted a file on the strength of that file's own
claim about itself, which is why the budget read as unwinnable: it was measuring two spines where the
session pays for one.

This does not retire the finding, it sharpens it. A document asserting a load discipline the harness
does not implement is worse than an over-budget document — it makes the budget unfalsifiable, and
content kept being written into `docs/METHOD.md` on the belief that it was always-loaded.

**Step 2 — measured against the content tier 1 will hold, not today's file.**

| Component | Lines |
| :--- | ---: |
| `CLAUDE.md`, after T-027 and T-046 | 140 |
| `docs/METHOD.md` §3 header + §3.1 (46–58) | 13 |
| `docs/METHOD.md` §3.3 (73–85) | 13 |
| **projected tier 1** | **166** |
| `reference/TASK-WORKFLOW.md` — the flat alternative | 173 |

**The counter-argument's own estimate was half the real figure.** §1 puts the conduct rules at
"roughly a dozen lines"; they are 26. Verdict: **under the flat alternative, and not comfortably.**
After this task's own edit `CLAUDE.md` is 144, so the projected total is 170 of 173 — three lines.
Some of the 26 is METHOD's section scaffolding and will not travel, but not obviously three lines'
worth, so T-047 is written to budget for removals rather than to assume it fits.

**Steps 3 and 4 — the bound is a relation, and no number is written.** `CLAUDE.md` §*Working method*
now states the three tiers, the membership rule for tier 1, and one rule: tier 1 stays shorter than
`reference/TASK-WORKFLOW.md`. Both sides are counted from the tree by the command the paragraph
carries, so re-measuring changes a measurement and never the rule. Today:

```text
  144 CLAUDE.md
  173 reference/TASK-WORKFLOW.md
```

Tiers 2 and 3 are stated as carrying no line budget, which is the consequence of budgeting tier 1
alone and is better written down than left to be inferred.

**Step 5 — `docs/METHOD.md` stops claiming a load it never had.** Its opening says it is not loaded
on every turn and that the project's always-loaded conventions say when it arrives; §3's framing
sentence now says §3.1 and §3.3 bind before it is clear there is any task work, and that §3.2
presupposes a phase and does not. Both are written **without naming a project file**, since METHOD
names none by design — which is also why METHOD cannot perform the move itself.

**A confirmation nobody arranged.** These edits put `docs/METHOD.md` at exactly **150** — the limit
this task has just removed. The next addition to it would have been refused by a budget aimed at the
wrong file, which is clause 4 of the finding happening while the fix for it was being written.

**Decisions & assumptions**
- **No number is written in tier 1 at all.** — Criterion 3 asks the number and its justification not
  to need updating together; deriving both sides from the tree removes the number rather than pairing
  it, and the measurements live here, dated, where a stale figure is evidence instead of a rule.
  — 2026-08-07
- **Tier 2 and tier 3 get no line budget.** — They are not paid on every turn, so a line limit would
  be measuring the wrong cost; what constrains them is R-21 and METHOD §7's load-one-at-a-time rule.
  The risk this accepts is that `docs/METHOD.md` can now grow, and the answer is that its growth is
  paid once by a session doing task work rather than by every session. Stated rather than implied,
  because it is the visible cost of the decision. — 2026-08-07
- **The projected total is reported as a pass with three lines to spare, not rounded to "passes".**
  — A margin inside the noise of one edit is not headroom, and T-047 inherits that as a constraint.
  — 2026-08-07

**Outputs produced**
- [`CLAUDE.md`](../CLAUDE.md) — §*Working method*: the three tiers, tier 1's membership rule, and the
  bound as a relation
- [`docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) — its opening statement of when it loads, and §3's framing

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The budget names the **set** of always-loaded files, not one of them, and the set is checkable against the repository rather than being a list someone must remember to update | met | It names a membership rule — what the harness loads unasked — which today resolves to one file. Checkable two ways, and both were run: enumerating every candidate a push would send returns one, and the file that claimed to be always-loaded was observed not to be. A nested addition later would join the set without anyone editing the budget, which is the property the criterion asked for. |
| The stated comparison against the flat alternative is one the project currently passes, or the gap is stated as dated debt with the task that will close it | met | Passes: 144 against 173, by the command the paragraph itself carries. The pressure is stated rather than smoothed over — the two conduct rules owed to tier 1 are named with their task, so a reader adding to `CLAUDE.md` knows the margin is not what a count of it suggests. |
| The number and its justification live in exactly one place, and the two do not have to be updated together | met | In the strongest available form: **there is no number**. The bound is a relation between two files both counted from the tree, so the pair that could drift does not exist. The dated measurements live in this record, where being stale makes them evidence rather than a false rule. |
| Re-measured after T-027, so the decision is taken against the total the project will actually have rather than today's | met | T-027 closed first, by the dependency edge added at `plan` — 145 → 139 — and T-046 then took it to 140. The bound was set and verified at 144, after this task's own edit, so the decision was taken against the total the project actually has and not against the one it had when the task was raised. |
| The tier boundary is stated where a reader of either file will meet it, and `docs/METHOD.md` no longer describes itself as loaded on every turn | met | Tiers stated in `CLAUDE.md` §*Working method*, where a tier-1 reader arrives; `docs/METHOD.md`'s opening now states it is not loaded on every turn, and §3's framing sentence — which was the load-bearing half — distinguishes the two rules that bind before task work from the one that does not. Both written without naming a project file, so METHOD stays backend-neutral. |

Five met, none carried. The task was raised because the budget had one file in scope and two in the
cost; it turns out to have had one file in scope, **one** in the cost, and a second that only said it
was — so the fix is a tier model rather than a bigger number, and the arithmetic that made the
finding look like an over-budget problem was measuring a claim.

**Child fix tasks raised**
- **T-047** — moves METHOD §3.1 and §3.3 into tier 1. Not a carried criterion: it is step 6's planned
  output, kept separate because a budget that also chooses the cut is a cut chosen to fit a number.
  It carries the dependency on T-003 that this task's specify had written as a sentence.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Five criteria met, none carried. **Step 1's suspicion held, and it changes what the finding was.** The always-loaded set is `CLAUDE.md` alone; `docs/METHOD.md` is reached through a link and read on demand, so the 286/292 figure was never a measurement of a load — it counted a file on the strength of that file's own claim. The budget did not have two files in the cost, it had one file and a second that said it was one, which is why it read as unwinnable. Worse than over-budget, and better fixed: a document asserting a load the harness does not implement makes the budget unfalsifiable. **The counter-argument's estimate was half.** §1 puts the conduct rules at "roughly a dozen lines"; §3 header + §3.1 is 13 and §3.3 is 13, so 26 — which takes projected tier 1 to 170 of 173 after this task's own edit, three lines of margin rather than the comfortable fit the decision assumed. Recorded as a pass with the margin named, not rounded to "passes", and T-047 is written to budget for removals instead of assuming it fits. The bound is a relation with **no number written anywhere**: both sides counted from the tree by the command the paragraph carries, so criterion 3's pair cannot drift because it does not exist. Tiers 2 and 3 get no line budget, stated explicitly along with what that accepts — METHOD can now grow, and its growth is paid once by a session doing task work rather than by every session. One confirmation nobody arranged: these edits put `docs/METHOD.md` at exactly 150, the limit this task removed, so the next addition would have been refused by a budget aimed at the wrong file — clause 4 of the finding occurring during its own fix. |
| 2026-08-07 | → planned | Six steps, and only the first can run: **T-027 moved from `related` to `blocked_by`.** Criterion 4 already required re-measuring after T-027, which is the METHOD §4 test answered — this task can start while T-027 is open but cannot finish — so it was prose standing in for an edge, invisible to `list` and to anyone asking why this is not moving. T-027 is at `proposed` with an open maintainer question, so that answer now gates this task. §1's measurement table was **left as measured** rather than refreshed: 145 + 147 = 292 is what today's count gives and what the parenthetical already records, and the movement is the log's to carry — rewriting §1 would delete the evidence the task was raised on. Step 1 is placed first on the suspicion that the always-loaded set is `CLAUDE.md` alone and `docs/METHOD.md` is reached by link, which would make every figure so far a measurement of a claim; recorded as the reason for the ordering, not resolved, because settling it is step 1's output and not planning's. |
| 2026-08-07 | — | **Measured three times in one day: 286 at raise, 292 at agree, 296, then 292 again.** The rise came from T-010's session — closing the GitHub binding made the *Status* paragraph false, and reconciling it plus a warning that the binding's `update` destroyed data cost seven lines on the spine. T-042 then fixed `update`, which made the warning false in turn, and removing it returned `CLAUDE.md` to 145. `METHOD.md` unchanged at 147 throughout. Recorded rather than absorbed, and the round trip is the useful part: the spine grew to carry a temporary fact and shrank when the fact expired, so some of what lands there is transient by nature — which is a question about what the budget is *for*, not only about what it counts. |
| 2026-08-06 | → specified | Q1 answered, and the answer changed the task rather than just unblocking it. The maintainer delegated the decision, directing that the sibling `handoff` plugin be studied first — which showed that its "always-loaded spine" is 282 lines that are *not* always loaded: the always-present artifact is a 31-line stub, with the core on activation and a flow on mode. Three tiers, where this project has two and calls both of its files always-loaded. So the outcome moved from *what does the budget count* to *how many tiers are there*, one criterion was added and the four existing ones stand. Two alternatives recorded as rejected, and the one way the decision can be wrong is named: demoting METHOD §3.1 and §3.3, which must bind before the agent knows it is doing task work. Re-measured while agreeing it — 292, not 286; T-034 added six lines to `CLAUDE.md` earlier the same day, which is the budget drifting during the task raised to fix it. Soft edge to T-003, which is the loader tier 2 needs; not a dependency, because this task decides a measure and moves nothing. |
| 2026-08-06 | → proposed | Raised as F-2 from the T-026 audit, clauses 3 and 4. Measured, not asserted: 139 + 147 = 286 always-loaded lines against the 173-line flat alternative the limit is justified by. Typed `decision` rather than `fix` because what to count is a judgement, and moving content is deliberately out of scope until it is made. |
