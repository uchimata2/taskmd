---
id: T-028
title: Budget the whole always-loaded context, not one file
type: decision
status: specified
phase: specify
parent: T-026
blocked_by: []
related: [T-015, T-027, T-003]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-06
deliverables: []
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
| 2026-08-06 | → specified | Q1 answered, and the answer changed the task rather than just unblocking it. The maintainer delegated the decision, directing that the sibling `handoff` plugin be studied first — which showed that its "always-loaded spine" is 282 lines that are *not* always loaded: the always-present artifact is a 31-line stub, with the core on activation and a flow on mode. Three tiers, where this project has two and calls both of its files always-loaded. So the outcome moved from *what does the budget count* to *how many tiers are there*, one criterion was added and the four existing ones stand. Two alternatives recorded as rejected, and the one way the decision can be wrong is named: demoting METHOD §3.1 and §3.3, which must bind before the agent knows it is doing task work. Re-measured while agreeing it — 292, not 286; T-034 added six lines to `CLAUDE.md` earlier the same day, which is the budget drifting during the task raised to fix it. Soft edge to T-003, which is the loader tier 2 needs; not a dependency, because this task decides a measure and moves nothing. |
| 2026-08-06 | → proposed | Raised as F-2 from the T-026 audit, clauses 3 and 4. Measured, not asserted: 139 + 147 = 286 always-loaded lines against the 173-line flat alternative the limit is justified by. Typed `decision` rather than `fix` because what to count is a judgement, and moving content is deliberately out of scope until it is made. |
