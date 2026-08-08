---
id: T-047
title: Move the conduct rules that bind before task work into tier 1
type: fix
status: specified
phase: specify
parent: null
blocked_by: [T-003]
related: [T-028, T-015]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-07
updated: 2026-08-08
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
- **None as an owner question. Confirmed by the maintainer on 2026-08-07: `plan` decides.** The
  question stands as written and is `plan`'s first step — draft the move, measure it, and only then
  choose what leaves. One candidate is on the record and is much the largest: `CLAUDE.md`'s
  pre-publish check section runs to roughly a third of tier 1 for something needed once, before
  publishing, which makes it a candidate for an on-demand file rather than a conventions one.
  Recorded as a candidate and not a decision, because measuring the move before choosing the cut is
  the whole of the sequencing this task inherited from T-028.

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
| 2026-08-08 | (no status change) | **Re-measured after the plugin was installed and `CLAUDE.md` reconciled again: 153 against 173, so 153 + 26 = 179, over by six.** The 177 in the entry below was true when written and is superseded by two more lines of reconcile — which is the third different figure this task has been given in two days, all from the same cause and none from anyone editing it. That is the finding worth carrying into `plan` rather than the number: **tier 1 moves whenever a task closes and the tree is made honest, so any cut sized against a measurement is sized against a stale one.** The `plan` should therefore decide what leaves on the grounds of what tier 1 is *for*, and re-measure at the end to state the result — not choose the cut from a figure. The description is still not counted: it is installed as of today but has never been observed being served, which is [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)'s remaining work, and when it is counted it arrives as ~397 characters against a line bound — the conversion this task still owes. |
| 2026-08-07 | (no status change) | **The entry below is withdrawn: tier 1 never gained that member.** [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) measured a session in this repository and the taskmd plugin is not installed — declared in `.claude/settings.json`, absent from every one of the harness's plugin state files, and refused by name when invoked. So the 397 characters were never served: **the reason the entry gave for going over is wrong.** What is not wrong is the conclusion. Re-measured rather than back-calculated — `wc -l` on both sides, after T-050's own reconcile edits landed — `CLAUDE.md` is **151** and `reference/TASK-WORKFLOW.md` is 173, so the projection is 151 + 26 = **177 of 173, over by four, on line count alone and with no description counted at all**. Three of those lines are T-050's reconcile of this very statement, which is the entry below's own point arriving from an unexpected direction: tier 1 grows when a task closes and the tree is made honest, so the room this task has to find is not a fixed quantity and is currently larger than any figure yet recorded. The membership rule itself is not what was wrong — a description *does* join tier 1 when the harness serves the skill — so the two things the entry below hands this task's `plan` stand, one of them now conditional: how a character count is weighed against a line bound binds from the moment the plugin is actually installed, which the maintainer is doing by hand and which the next session verifies. |
| 2026-08-07 | (no status change) | ~~**Re-measured after T-003 closed: the margin is gone, and tier 1 has gained a member that is not a file.**~~ *(withdrawn by T-050 — see above)* A skill's `description` is handed to a session unasked, so enabling the taskmd plugin here puts it in tier 1 by T-028's own membership rule — 74 words, 397 characters, one physical line in `skills/taskmd/SKILL.md`. `CLAUDE.md` also went 146 → 148, reconciling *Status* and the membership sentence, so the projection is 148 + 26 = **174 against 173, before the description is counted at all**. So this task is now over rather than one line under, which changes its character: finding room is no longer optional and the pre-publish-check candidate in the open question above is no longer merely the largest candidate. Recorded, not acted on — what leaves tier 1 is this task's `plan`, and trimming from outside would be the cut chosen to fit a number that T-028 and this task both refuse. Two things worth carrying into that plan: the description is a *character* count against a *line* bound, so `plan` has to say how it is counted before it can say whether it fits; and tier 1 now grows whenever a skill is added, not only when this file is edited. |
| 2026-08-07 | (no status change) | **Re-measured after T-011 closed: the margin is now one line, not three.** `CLAUDE.md` went 144 → 146 — T-011 added three clauses to *Status* for auto-discovery, the launchers and the hook — so projected tier 1 is 26 + 146 = **172 of 173**. §1 is unchanged because it says "mid-140s" and still does, and T-028's 170 figure stays in its own record as what was true then. Recorded rather than acted on: what leaves tier 1 is this task's `plan` to decide, and trimming `CLAUDE.md` from outside would be the cut chosen to fit a number that T-028 and this task both refuse. The direction is the useful part — tier 1 grows whenever a task closes and *Status* is reconciled, so the room this task has to find is not a fixed quantity. |
| 2026-08-07 | → specified | Confirmed by the maintainer that what leaves tier 1 is `plan`'s decision, not theirs. Nothing else was outstanding, so this moves to `specified` with the question intact rather than answered. One sizeable candidate recorded while it was in view: the pre-publish check is about a third of tier 1 and is needed once, before publishing — a candidate, not a plan, since choosing the cut before measuring the move is what T-028 declined to do. |
| 2026-08-07 | → proposed | Raised by T-028 step 6, which decided the measure and moved no content on purpose. Carries a dependency on T-003 as an edge rather than the sentence T-028's specify had, because tier 2 without a loader is not a tier. The measurement T-028 took is the reason this is `effort: m` rather than `s`: the content is 26 lines, not the dozen the decision's counter-argument estimated, so it does not fit as a straight addition and the task has to find room. |
