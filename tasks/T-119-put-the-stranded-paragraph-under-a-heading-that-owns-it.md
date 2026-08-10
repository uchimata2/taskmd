---
id: T-119
title: Put the stranded paragraph under a heading that owns it
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-047, T-118]
work_package: v0.2
owner: the project owner
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: []
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
- Does fixing this need a new heading, or does the paragraph move up to sit before
  `### Two rules that bind before there is any task`? — whoever takes it; both are cheap and the
  second adds no characters, which is the tie-breaker if they are otherwise equal.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → proposed | Found while implementing T-118, which removed the bullet block that used to sit between the verbatim rules and this paragraph. The stranding is **pre-existing** — T-047 moved the rules in and left what followed underneath them — and removing the bullets only made it visible; recorded that way so this does not read as damage the cut caused. Raised rather than fixed in place, because T-118 decides what *leaves* tier 1 and this is about where what stays sits, and because a heading edit made silently inside another task's diff is indistinguishable from tidying. `low`/`xs`: it misleads a reader about where a verbatim quotation ends, which is worth fixing, but nothing acts wrongly on it. |
