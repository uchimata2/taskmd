---
id: T-047
title: Move the conduct rules that bind before task work into tier 1
type: fix
status: done
phase: review
parent: null
blocked_by: [T-003]
related: [T-028, T-015]
work_package: M2
owner: maintainer
business_value: high
effort: m
created: 2026-08-07
updated: 2026-08-10
deliverables: [CLAUDE.md, plugin/skills/taskmd/docs/METHOD.md, plugin/skills/taskmd/adopt.md, docs/PUBLISHING.md, docs/SCOPE.md]
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

- ~~**What leaves tier 1?**~~ **Answered by the maintainer on 2026-08-09, ahead of `plan`: the
  pre-publish check section leaves, and it is not enough on its own.**

  Taken early because the sequencing this task inherited — *measure the move before choosing the
  cut* — has had its first half done. [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md)
  replaced the blind line count with a character count that reads every declared member, so tier 1
  is now measurable rather than estimated. Measured 2026-08-09, by section:

  ```
  tier 1 = 11,728 (CLAUDE.md) + 411 (the served description) = 12,139   bound 7,846   over by 4,293

  ### The pre-publish check      3,961   32.6% of tier 1
  ## Working method              2,815   23.2%
  ## What this is                2,725   22.4%
  ## Publishing constraints      1,271   10.5%
  ## The one design rule           528    4.3%
  ## Verifying                     347    2.9%

  METHOD §3.1 + §3.3, which this task must ADD           1,722
  so the cut has to find                                6,015
  ```

  **The pre-publish check is the cut, and it covers 66% of what is needed.** It is the largest single
  block in the file by a wide margin, and it is needed **once, before publishing** — which is the
  definition of an on-demand document rather than an always-loaded one. Everything a turn actually
  needs from it is that the check exists and where to find it.

  **This does not close the task, and the arithmetic says why.** 6,015 − 3,961 leaves **2,054
  characters** still to find after the move. `plan` owns where they come from; the measurement above
  is what it now works against, in place of the estimate it had.

  *Rejected: trimming `## Working method` or `## What this is`.* Together they are 5,540 characters
  and would close the gap on their own. They are also the two sections read on **every** turn, and
  are the whole of what tier 1 exists to deliver — cutting them trades the budget for the thing the
  budget protects. They may still give up some of the remaining 2,054, and that is a different
  question from making them the primary cut.

  *Rejected: raising the bound, or changing the comparator.* Both are T-028's and are not reopened;
  and a bound moved to fit the file it measures is not a bound.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-measure tier 1, the bound and the two rules, and state the gap the cut has to close | The arithmetic in §3 below |
| 2 | Give the two rules a home an adopter can still reach, and repoint `adopt.md` §4 at it — removing them from `METHOD.md` orphans that step otherwise | `plugin/skills/taskmd/adopt.md` |
| 3 | Move `### The pre-publish check` out of tier 1, leaving only that it exists, what it covers and the command | `CLAUDE.md`, `docs/PUBLISHING.md` |
| 4 | Compress the tier-budget passage to what a turn uses — which tier loads when, the bound, the command — and point at the tasks that argued the rest | `CLAUDE.md` *Working method* |
| 5 | Compress `## What this is` status narrative to pointers, keeping only what a turn acts on | `CLAUDE.md` |
| 6 | Copy §3.1 and §3.3 into tier 1 **verbatim**, and cut them from `METHOD.md` §3, leaving §3.2 and the obligation sentence that names no project file | `CLAUDE.md`, `plugin/skills/taskmd/docs/METHOD.md` |
| 7 | Compare the moved text against the pre-move text mechanically, not by eye | A diff quoted in §3 |
| 8 | Re-measure tier 1 against the bound; run `check`, `index`, the suite and the leak check | Evidence in §3 |

**Where the two rules live afterwards, and what was rejected.** `adopt.md` §4 already exists to tell
an adopter to carry these rules, and it does it by pointing at `METHOD.md` §3 for *which* they are.
Once §3 no longer states them, that pointer resolves to a document that names the rules without
saying what they require, so the text lands in `adopt.md` and §4 stops delegating. *Rejected: leaving
a short paraphrase in `METHOD.md` and the long form in tier 1* — two lengths of one rule is the
drift this project's design rule exists to prevent, and the acceptance criterion asks for a
comparison against the pre-move text, which a paraphrase defeats.

**The copy in tier 1 is compelled by the architecture, not by this task.** A rule that binds before
the method is loaded cannot have its only home in the method; that is T-028's tiering, and one copy
in the always-loaded file is what it costs. What this task chooses is only the *other* copy's home.

**Steps 4 and 5 are the residual cut, and they were rejected as the primary one.** `specify` rejected
making *Working method* and *What this is* the main source of room, because they are what tier 1
exists to deliver. They are still where the remainder comes from, and the distinction is what gets
cut: **rationale and status, never the rule**. Both have durable homes already — the tasks that
argued them and the generated index — so this is *point, don't restate*, not deletion.

*Rejected: a new on-demand document for the tier budget.* The passage is mostly the reasoning behind
a rule, and reasoning has a home in T-028 and T-063. A third file to hold it would be a place for the
argument to drift from the tasks that made it.

## 3. Implement

**Decisions & assumptions**

- **The two rules' canonical text moved to `adopt.md` §4, not to a paraphrase in `METHOD.md`** —
  2026-08-10. §4 already existed to tell an adopter to carry them and did it by pointing at §3; once
  §3 stops stating them that pointer resolves to a document naming rules it does not give. §3 now
  states the obligation and names `adopt.md` for the text, which keeps it free of any *project* file.
- **The rationale cross-reference was dropped from the `adopt.md` copy and rewritten in the tier-1
  copy** — 2026-08-10. `(method/rationale.md)` resolves from `docs/`, from nowhere an adopter pastes
  it, and from a different depth in `CLAUDE.md`. This is the one difference from the pre-move text
  and it is a path, not a word; §7's comparison normalises exactly it and nothing else.
- **The cut was chosen by what tier 1 is *for*, then measured — not sized to a figure** — 2026-08-10,
  which is the sequencing this task inherited from T-028 and the standing instruction in its own log.
  The line drawn: a **rule** a turn must obey stays; **status**, **rationale** and anything binding at
  a *moment* rather than on a turn goes to the document that owns that moment.
- **`### The pre-publish check` → `docs/PUBLISHING.md` §6** — 2026-08-10, the maintainer's answer of
  2026-08-09. `PUBLISHING.md` had already recorded that the two publish-time rules belong together and
  named this task as their consolidation, so the destination was chosen before this session.
- **`## Publishing constraints` → `docs/SCOPE.md` §5** — 2026-08-10, and this was **not** in the plan.
  After the approved cut tier 1 was still 1,541 over, and the constraints were the next block that
  binds at a moment rather than on a turn. `SCOPE.md` §5 existed and pointed *back* at `CLAUDE.md` as
  their one home, so this is an inversion of an existing pointer rather than a new home — the five
  constraints keep a one-line form in tier 1 and their detail is one hop away, in the first document
  tier 1 tells you to read.
- **Rejected: cutting anything from the two rules to make the arithmetic easier** — 2026-08-10. The
  scope forbids changing what they say, and a rule trimmed to fit a budget is the failure the budget
  was written to prevent.

**Outputs produced**
- `CLAUDE.md` — the two rules in full; *What this is*, *Working method* and *Publishing constraints*
  compressed
- `plugin/skills/taskmd/docs/METHOD.md` — §3 states the obligation and no longer carries §3.1/§3.3
- `plugin/skills/taskmd/adopt.md` — §4 carries the text
- `docs/PUBLISHING.md` — §6, the pre-publish check
- `docs/SCOPE.md` — §5, the constraints

**Evidence**

**The two rules are byte-identical to the pre-move text.** Extracted before the move, re-extracted
from `CLAUDE.md` after it, normalised only for heading depth and the rationale link's path, and
compared with `diff` rather than by eye — both empty:

```
=== 3.1 diff (empty means identical) ===
(none)
=== 3.3 diff (empty means identical) ===
(none)
```

**Tier 1 against the bound**, before and after:

```
tier 1 = 12736   bound = 7919   margin = -4817
tier 1 =  7911   bound = 7919   margin =     8   PASSES
```

By section, after: *What this is* 1,850 · *The one design rule* 563 · *Working method* 1,435 ·
*the two rules* 2,767 · *Publishing constraints* 746 · *Verifying* 349.

**It passes by 8 characters, which is not a durable pass** — see the finding below.

**`check` caught a bad link I had just written**, which is the tool working on itself and is worth
recording rather than quietly fixing:

```
BROKEN LINK   plugin/skills/taskmd/docs/METHOD.md -> ../../adopt.md
```

`METHOD.md` sits in `docs/`, so the new pointer to its sibling `adopt.md` needed one `..`, not two.
**That one link failed six tests** — the suite went 4 → 10, because six cases run `check` over this
repository and assert it passes. Fixing the link returned all six. Final suite: **4 failed, 183
passed, 2 subtests passed**, the same four inherited by this session and confirmed against a stashed
tree during T-098 — T-114 and T-112, neither this change.

`check` clean afterwards, on a regenerated index:

```
OK - 114 task(s), ..., 142 document(s), 1107 link(s), ...
Scope  38 document(s) not read: a clone would not receive them
```

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| §3.1 and §3.3 are readable in tier 1 without following a link, and `METHOD.md` no longer carries them in full | met | Both are in `CLAUDE.md` under *Two rules that bind before there is any task*, in full and with no link to follow. `METHOD.md` §3 now states only the obligation and §3.2. |
| Tier 1 is still shorter than `reference/TASK-WORKFLOW.md` after the move, measured and stated | met, **barely** | 7,911 against 7,919 — **8 characters**, measured by the command in `CLAUDE.md` and stated in §3. It meets the criterion as written and it is one sentence from failing, which is [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md). |
| The two rules say what they said — compared against the pre-move text, not judged by eye | met | `diff` against text extracted before the move, both empty. The only difference normalised out was the rationale link's path, recorded as a decision in §3 because it is a path and not a word. |
| `METHOD.md` §3 still reads coherently for a project whose tier 1 is not this repository's, and names no project file | met | §3 names the two rules, says why they cannot live there, and points at `adopt.md` §4 — a skill file, which is what an adopter has. No project file is named. The pointer was wrong on the first attempt and `check` caught it, per §3. |
| R-6 and R-8 still resolve to a rule that exists, and `docs/SCOPE.md` §3's requirement-versus-rule division is not disturbed | met | Both requirements state the rule as a requirement and neither points at `METHOD.md` §3.1/§3.3 by number, so nothing dangled. `SCOPE.md` §3 is untouched; §5 changed, and that is a different section and a deliberate output. |

**One criterion met barely enough to name.** The budget row is a pass on the number and not on the
margin, and review does not repair what it finds — so it is carried as T-115 rather than fixed by
cutting more here, which would also be the cut-chosen-to-fit-a-figure this task refused twice.

**Child fix tasks raised**
- [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md) — nothing enforces the bound,
  which was harmless while tier 1 was 4,817 over and is not harmless at 8 under.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Tier 1 passes for the first time: **7,911 against 7,919**. Re-measured at the start rather than trusting the entry below — it had drifted to 12,736 against 7,919, over by 4,817 against the 4,293 recorded a day earlier, which is that entry's own point arriving on schedule. The approved cut covered 4,567 of the 6,633 needed; the rest came from `## Publishing constraints`, which was **not** in the plan and which `docs/SCOPE.md` §5 already claimed to point at rather than hold, so moving it inverted an existing pointer instead of inventing a home. The rules are byte-identical by `diff`, not by eye. Two things worth carrying: `adopt.md` §4 delegated to `METHOD.md` §3 for the rule text, so removing it from §3 would have orphaned the adoption step — found by reading §4, not by any check; and the margin is **8 characters**, which is a pass nobody should rely on, raised as T-115. |
| 2026-08-09 | (no status change) | **The cut is answered ahead of `plan`, on a measurement that did not exist before today.** T-063 replaced the blind line count with a character count over every declared member, so the first half of this task's inherited sequencing — measure, then choose — is done: tier 1 is **12,139 against 7,846**, over by 4,293, and §3.1 and §3.3 add a further 1,722, so the cut has to find **6,015**. `### The pre-publish check` is 3,961 of it — 32.6% of tier 1, for something needed once before publishing. It goes. What this changes for `plan` is that the remaining **2,054** is a stated number rather than an open-ended search, and that the two sections which could close it alone are the two read every turn. Status unchanged: the task was already `specified`, and answering a `plan` question does not re-run `specify`. |
| 2026-08-08 | (no status change) | **The description is now counted, not projected.** [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 7 observed a session actually handed it, so the entry below's last clause — "installed as of today but has never been observed being served" — is settled and the ~397 characters are in tier 1 for real. The line figure is unchanged at **153 against 173**: that session's reconcile of `CLAUDE.md` was six lines in and six out. So nothing about the arithmetic moved, and the finding the entry below carries into `plan` is untouched — what changed is that the projection became a measurement, which is the one thing that was holding the conversion question open. |
| 2026-08-08 | (no status change) | **Re-measured after the plugin was installed and `CLAUDE.md` reconciled again: 153 against 173, so 153 + 26 = 179, over by six.** The 177 in the entry below was true when written and is superseded by two more lines of reconcile — which is the third different figure this task has been given in two days, all from the same cause and none from anyone editing it. That is the finding worth carrying into `plan` rather than the number: **tier 1 moves whenever a task closes and the tree is made honest, so any cut sized against a measurement is sized against a stale one.** The `plan` should therefore decide what leaves on the grounds of what tier 1 is *for*, and re-measure at the end to state the result — not choose the cut from a figure. The description is still not counted: it is installed as of today but has never been observed being served, which is [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)'s remaining work, and when it is counted it arrives as ~397 characters against a line bound — the conversion this task still owes. |
| 2026-08-07 | (no status change) | **The entry below is withdrawn: tier 1 never gained that member.** [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) measured a session in this repository and the taskmd plugin is not installed — declared in `.claude/settings.json`, absent from every one of the harness's plugin state files, and refused by name when invoked. So the 397 characters were never served: **the reason the entry gave for going over is wrong.** What is not wrong is the conclusion. Re-measured rather than back-calculated — `wc -l` on both sides, after T-050's own reconcile edits landed — `CLAUDE.md` is **151** and `reference/TASK-WORKFLOW.md` is 173, so the projection is 151 + 26 = **177 of 173, over by four, on line count alone and with no description counted at all**. Three of those lines are T-050's reconcile of this very statement, which is the entry below's own point arriving from an unexpected direction: tier 1 grows when a task closes and the tree is made honest, so the room this task has to find is not a fixed quantity and is currently larger than any figure yet recorded. The membership rule itself is not what was wrong — a description *does* join tier 1 when the harness serves the skill — so the two things the entry below hands this task's `plan` stand, one of them now conditional: how a character count is weighed against a line bound binds from the moment the plugin is actually installed, which the maintainer is doing by hand and which the next session verifies. |
| 2026-08-07 | (no status change) | ~~**Re-measured after T-003 closed: the margin is gone, and tier 1 has gained a member that is not a file.**~~ *(withdrawn by T-050 — see above)* A skill's `description` is handed to a session unasked, so enabling the taskmd plugin here puts it in tier 1 by T-028's own membership rule — 74 words, 397 characters, one physical line in `skills/taskmd/SKILL.md`. `CLAUDE.md` also went 146 → 148, reconciling *Status* and the membership sentence, so the projection is 148 + 26 = **174 against 173, before the description is counted at all**. So this task is now over rather than one line under, which changes its character: finding room is no longer optional and the pre-publish-check candidate in the open question above is no longer merely the largest candidate. Recorded, not acted on — what leaves tier 1 is this task's `plan`, and trimming from outside would be the cut chosen to fit a number that T-028 and this task both refuse. Two things worth carrying into that plan: the description is a *character* count against a *line* bound, so `plan` has to say how it is counted before it can say whether it fits; and tier 1 now grows whenever a skill is added, not only when this file is edited. |
| 2026-08-07 | (no status change) | **Re-measured after T-011 closed: the margin is now one line, not three.** `CLAUDE.md` went 144 → 146 — T-011 added three clauses to *Status* for auto-discovery, the launchers and the hook — so projected tier 1 is 26 + 146 = **172 of 173**. §1 is unchanged because it says "mid-140s" and still does, and T-028's 170 figure stays in its own record as what was true then. Recorded rather than acted on: what leaves tier 1 is this task's `plan` to decide, and trimming `CLAUDE.md` from outside would be the cut chosen to fit a number that T-028 and this task both refuse. The direction is the useful part — tier 1 grows whenever a task closes and *Status* is reconciled, so the room this task has to find is not a fixed quantity. |
| 2026-08-07 | → specified | Confirmed by the maintainer that what leaves tier 1 is `plan`'s decision, not theirs. Nothing else was outstanding, so this moves to `specified` with the question intact rather than answered. One sizeable candidate recorded while it was in view: the pre-publish check is about a third of tier 1 and is needed once, before publishing — a candidate, not a plan, since choosing the cut before measuring the move is what T-028 declined to do. |
| 2026-08-07 | → proposed | Raised by T-028 step 6, which decided the measure and moved no content on purpose. Carries a dependency on T-003 as an edge rather than the sentence T-028's specify had, because tier 2 without a loader is not a tier. The measurement T-028 took is the reason this is `effort: m` rather than `s`: the content is 26 lines, not the dozen the decision's counter-argument estimated, so it does not fit as a straight addition and the task has to find room. |
