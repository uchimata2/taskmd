---
id: T-048
title: Say what "always-loaded" means in R-21, before the skill is built against it
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-003, T-028]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-048 — Say what "always-loaded" means in R-21, before the skill is built against it

## 1. Specify

**Outcome**
R-21 says what it means by "always-loaded", so that [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
is built against a testable property rather than the phrase this project has just shown to be
relative.

**Why this one**
R-21 reads: *"The skill is a small always-loaded spine plus files loaded only when their moment
arrives — never the whole method up front."*

[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) established, by observation
rather than argument, that **"always-loaded" is relative to something and the something is never
stated.** `docs/METHOD.md` called itself always-loaded and was not: it is reached through a link and
read on demand, which is why a budget built on the phrase measured a claim instead of a load. The
sibling `handoff` skill has the same shape one level up — its core describes itself as *"the
always-loaded spine"* at 282 lines, while the artifact a session actually always has is a 31-line
stub.

R-21 uses the phrase in exactly that unqualified sense, and **T-003 is the next task to be built**.
A skill has at least two tiers of its own — the description the harness always has, and the body it
loads on activation — so a skill built to satisfy R-21 as written will reproduce the defect T-028
was raised to fix, one level up, in the deliverable this project exists to ship.

**This is not an argument against R-21.** Progressive disclosure is right and the requirement is the
right requirement; what is missing is the referent, which was invisible until T-028 went and looked.

**Requirements served**
R-21, R-22 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: R-21's wording, and any other requirement that leans on the same phrase.
- In: what the referent is for a skill — what a session has before the skill activates, versus after.
- Out: `CLAUDE.md`'s tier model. T-028 settled it for this repository; this is about the requirement
  a shipped skill is judged against, which is a different reader.
- Out: designing the skill's tiers. That is T-003's work; this task gives it a testable target.
- Out: `docs/METHOD.md` and `docs/BINDING.md`, both already reconciled to the tier model.

**Inputs**
`docs/SCOPE.md` R-21 and R-22,
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) §1 Q1 and §3 step 1,
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md).

**Acceptance criteria**
- [ ] R-21 states what "always-loaded" is relative to, in terms someone can check against a real
      session rather than against a document's description of itself
- [ ] The requirement stays a **property**, not an instruction — `docs/SCOPE.md` §3's division, which
      T-017 settled and T-045 re-checked, is not disturbed
- [ ] Every other requirement using the phrase is found by search and resolved the same way, or
      confirmed not to use it
- [ ] T-003 can be judged against the result: someone holding the finished skill can say whether it
      passes, without re-litigating what the phrase meant

**Open questions**
- None. The referent is discoverable the way T-028 discovered it — observe what a session is handed
  before anything is asked of it — so this needs measurement rather than a decision.

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
| 2026-08-07 | → proposed | Found during the reconcile sweep after T-028 closed, and deliberately **not** fixed there: T-028's scope put `docs/SCOPE.md` out, and R-21 was not made false by that task — it carried the same unqualified phrase before it and would have carried it after. So this is a finding rather than a stale line, and METHOD §5 keeps the two apart. `high`/`xs` because the cost is one sentence and the exposure is T-003, which is `critical`, next in the ordering, and would otherwise reproduce T-028's defect inside the deliverable. Two lines *were* reconciled in the same sweep and are not part of this task: `docs/BINDING.md` said the method governs every turn, and `.handoff/config.md` called METHOD an always-loaded spine — both made false by T-028's edit rather than merely imprecise. |
