---
id: T-119
title: Put the stranded paragraph under a heading that owns it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-047, T-118]
work_package: v0.2
owner: the project owner
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [CLAUDE.md]
---

# T-119 — Put the stranded paragraph under a heading that owns it

## 1. Specify

**Outcome**
`CLAUDE.md`'s paragraph about `reference/TASK-WORKFLOW.md` sits under a heading that describes it,
rather than under `#### Surface what you discover — never absorb it, never drop it`, which is one of
the two method rules carried verbatim and has nothing to do with prior art.

**Scope**
- In: where that paragraph sits, and whatever heading structure `Working method` needs so that the
  two verbatim rules end where they end.
- Out: whether the paragraph belongs in tier 1 at all. [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md)
  kept it, on the grounds that its home elsewhere was never established — that is a separate question
  from where it sits, and answering it here would be the silent widening METHOD §3.3 forbids.
- Out: the wording of the two verbatim rules. They are METHOD's, copied (T-047).

**Inputs**
`CLAUDE.md`, [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md),
[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) §3 *Escalated*.

**Acceptance criteria**
- [ ] A reader can tell, from the headings alone, where the two verbatim method rules stop
- [ ] No content is deleted to achieve it — anything that moves is still in the file, or has a
      recorded home outside it
- [ ] `python tests/test_budget.py` still passes and the margin is stated, since any heading added
      is tier 1 like everything else here

**Open questions**
- ~~Does fixing this need a new heading, or does the paragraph move up to sit before
  `### Two rules that bind before there is any task`?~~ **Answered 2026-08-11: it moves up**, and one
  paragraph further than the question proposed — see D1 in §2. The task's own tie-breaker decided it,
  and the measurement in §3 confirms the tie was real.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Move the paragraph to sit directly after the tiers paragraph that names the file as the bound, leaving `### Two rules that bind before there is any task` holding nothing but its two rules. | `CLAUDE.md` |
| 2 | Measure the tier-1 character count either side of the move, since the tie-breaker was that it costs nothing. | Recorded output |
| 3 | Read the headings back and confirm the `###` section now ends where the verbatim quotation ends. | Recorded output |

**Shape decisions.**

**D1 — It moves up, and to just after the tiers paragraph rather than merely above the `###`.** That
paragraph is the one naming `reference/TASK-WORKFLOW.md` as the bound tier 1 is measured against, and
the moved sentence says "the bound above" — so placing it there puts the reference one paragraph from
its antecedent instead of three. *Rejected: a new heading.* It answers the criterion too, and it costs
characters in the one file whose every character is paid on every turn of every session — which is the
tie-breaker the specify wrote down, and the tie turns out to be exact: 6968 before, 6968 after.

**Planned outputs**
- CLAUDE.md

## 3. Implement

The paragraph moved from the end of `#### Surface what you discover — never absorb it, never drop it`
to just after `**Three tiers, and only the first is budgeted.**`, unedited — the diff is 4 insertions
and 4 deletions, which is the same four lines in a different place.

**Tier 1 is the same size, measured rather than assumed:**

```text
tier 1 6968 chars under by 878 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md,
plugin/skills/taskmd/SKILL.md
```

6968 before the move and 6968 after. The tie-breaker in the specify was that one option adds no
characters; that is now a measurement rather than a prediction.

**The headings afterwards:**

```text
32: ## Working method
62: ### Two rules that bind before there is any task
67: #### One phase per request - never auto-advance
81: #### Surface what you discover - never absorb it, never drop it
94: ## Publishing constraints
```

Nothing sits between line 81's rule and line 94's next `##`, so the `###` section contains exactly
the two `####` rules and stops where they stop.

**Decisions & assumptions**
- **D1 — move up, no new heading** — 2026-08-11, §2; the rejected alternative and the tie-breaker are
  recorded there.
- **The paragraph's text is untouched.** The scope puts the wording of the two verbatim rules out;
  this one is not theirs, but editing it while relocating it would make the move unreviewable as a
  move.

**Outputs produced**
- [`CLAUDE.md`](../CLAUDE.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A reader can tell, from the headings alone, where the two verbatim method rules stop | met | `### Two rules that bind before there is any task` now runs from line 62 to the next `##` at line 94, and holds only its two `####` rules; read back from the file, not from the edit |
| No content is deleted to achieve it — anything that moves is still in the file, or has a recorded home outside it | met | 4 insertions, 4 deletions: the same four lines, relocated and unedited |
| `python tests/test_budget.py` still passes and the margin is stated, since any heading added is tier 1 like everything else here | met | `OK`, and `tier 1 6968 chars under by 878 (bound 7846)` — unchanged either side, because no heading was added |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met, no child raised. **Authorisation (METHOD §3.1):** the maintainer's standing grant to work every open `v0.2` task through its full lifecycle, given 2026-08-10 and widened on 2026-08-11 to *the remaining tasks, full lifecycle, continuously*. The one open question was delegated to whoever took it and came with its own tie-breaker — the option that adds no characters wins — so it was answered here rather than escalated, with the rejected alternative recorded in §2. **It moved one paragraph further than the question proposed**: up beside the tiers paragraph that names `reference/TASK-WORKFLOW.md` as the bound, so "the bound above" sits one paragraph from its antecedent rather than three. Worth carrying: **the tie was exact, and measured rather than predicted** — 6968 characters before and after, from `test_budget`'s own line, which is the only reason a relocation in this file needs no argument about what it cost. |
| 2026-08-11 | → proposed | Found while implementing T-118, which removed the bullet block that used to sit between the verbatim rules and this paragraph. The stranding is **pre-existing** — T-047 moved the rules in and left what followed underneath them — and removing the bullets only made it visible; recorded that way so this does not read as damage the cut caused. Raised rather than fixed in place, because T-118 decides what *leaves* tier 1 and this is about where what stays sits, and because a heading edit made silently inside another task's diff is indistinguishable from tidying. `low`/`xs`: it misleads a reader about where a verbatim quotation ends, which is worth fixing, but nothing acts wrongly on it. |
