---
id: T-047
title: Move the conduct rules that bind before task work into tier 1
type: fix
status: proposed
phase: specify
parent: null
blocked_by: [T-003]
related: [T-028, T-015]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-047 — Move the conduct rules that bind before task work into tier 1

## 1. Specify

**Outcome**
`docs/METHOD.md` §3.1 and §3.3 bind on turns where no task work has been recognised yet, because they
are carried in tier 1 rather than in a document that loads only once task work starts — and tier 1 is
still shorter than `reference/TASK-WORKFLOW.md` afterwards.

**Why this one**
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) decided the tiering and
deliberately moved no content: a budget that also chooses the cut is a budget chosen to fit a cut.
It named the one way that decision goes wrong — demoting the two rules that must bind *before* the
agent knows it is doing task work — and this is the task that stops it going wrong.

§3.1 (*never auto-advance*) and §3.3 (*surface what you discover*) are the two. §3.2 presupposes a
phase and travels with the rest of the method. `docs/METHOD.md` now says so, in backend-neutral
terms; what it cannot do is put them anywhere, because it names no project file by design.

**The measurement makes this harder than T-028 assumed.** T-028 §1 estimated the affected content at
"roughly a dozen lines"; measured, §3 header + §3.1 is 13 lines and §3.3 is 13, so 26. Against a bound
of 173 and a `CLAUDE.md` in the mid-140s, the move does not fit as a straight addition. Some of the
26 is METHOD's own section scaffolding and will not travel, but the gap is not obviously covered by
that alone, so **this task has to budget for removals as well**.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: the text of §3.1 and §3.3, where it lands in tier 1, and what leaves tier 1 to make room.
- In: what `docs/METHOD.md` §3 says once the two rules live elsewhere — it must not become a
  pointer to a project file, since it names none.
- Out: the tiering decision and the bound. T-028 settled both; this task executes against them.
- Out: §3.2, which stays.
- Out: any change to what the two rules *say*. This is a move, and a move that improves the wording
  on the way cannot be checked against the original.

**Inputs**
[T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) §1 and §3, `docs/METHOD.md` §3,
`CLAUDE.md` §*Working method*, `docs/SCOPE.md` R-6 and R-8 — which state the same two rules as
requirements and must still be satisfiable after the move.

**Acceptance criteria**
- [ ] §3.1 and §3.3 are readable in tier 1 without following a link, and `docs/METHOD.md` no longer
      carries them in full
- [ ] Tier 1 is still shorter than `reference/TASK-WORKFLOW.md` after the move, measured and stated
- [ ] The two rules say what they said — compared against the pre-move text, not judged by eye
- [ ] `docs/METHOD.md` §3 still reads coherently for a project whose tier 1 is not this repository's,
      and names no project file
- [ ] R-6 and R-8 still resolve to a rule that exists, and `docs/SCOPE.md` §3's requirement-versus-rule
      division is not disturbed

**Open questions**
- What leaves tier 1 to make room, if the arithmetic needs it. Not answerable until the move is
  drafted and measured, which is `plan`'s first step rather than an owner question.

**Dependency, and why it is an edge.** This task waits on
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md): tier 2 needs a loader, and
demoting `docs/METHOD.md` before anything reliably loads it on starting task work would leave the
lifecycle unloaded rather than tiered.

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
| 2026-08-07 | → proposed | Raised by T-028 step 6, which decided the measure and moved no content on purpose. Carries a dependency on T-003 as an edge rather than the sentence T-028's specify had, because tier 2 without a loader is not a tier. The measurement T-028 took is the reason this is `effort: m` rather than `s`: the content is 26 lines, not the dozen the decision's counter-argument estimated, so it does not fit as a straight addition and the task has to find room. |
