---
id: T-153
title: E-10 — Move the maintainer's justification into comments the harness strips
type: fix
status: done
phase: review
parent: T-152
blocked_by: []
related: [T-142]
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-15
updated: 2026-08-16
deliverables: []
---

# T-153 — E-10: move the maintainer's justification into comments the harness strips

## 1. Specify

**Outcome**
The passages of `CLAUDE.md` that argue a rule to a human maintainer stop being paid on every turn,
without leaving the file and without anything operative going with them.

**Why this one**
Finding [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md): block-level HTML comments
are stripped before an instruction file is injected. The finding is stated there and is not restated
here. The maintainer ruled on 2026-08-15 that **this one is taken first** — it saves less than
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) and it cannot fail.

**Scope**
- In: `CLAUDE.md`, and the split of each candidate passage into *justification for a human* or
  *instruction for the agent*.
- In: what the budget check should count afterwards — see the open question.
- Out: moving anything to another file. That is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md), and it is a
  hypothesis where this is not.
- Out: the tier-1 membership rule and the bound. Both are
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md)'s and stand.

**Inputs**
- [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) — the mechanism and its one risk
- `CLAUDE.md`
- `tests/test_budget.py`

**Acceptance criteria**
- [ ] Every passage moved into a comment is justification for a human, and the split is stated passage
      by passage rather than as a total
- [ ] Nothing operative for the agent went into a comment, checked by reading the result as a session
      would receive it
- [ ] The saving is measured after the change, in characters, with the date, and written here
- [ ] `tests/test_budget.py` passes, and what it now counts is stated
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Does the budget still measure what a session pays?** Verified 2026-08-15: `measure()` in
  `tests/test_budget.py` reads the whole file, so a comment stays inside the counted figure while
  leaving the per-turn cost. After this change the check over-counts by exactly what the change saved.
  Decide at `specify` whether the check strips block comments, or whether the figure stands and the
  discrepancy is recorded beside it. **The maintainer answers.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Split every candidate passage in `CLAUDE.md` into *justification for a human* or *instruction for the agent* — passage by passage, never as a total | The five passages listed below, each named with what it justifies |
| 2 | Wrap each justification in a **block-level** comment, placed after the paragraph it explains, and leave that paragraph reading correctly without it | `CLAUDE.md` |
| 3 | Answer the open question: make the budget count **what a session is handed**, not what the file holds | `strip_block_comments` in `tests/test_budget.py` |
| 4 | Prove the strip on the case it must catch **and** on the case it must not — a comment inside a code fence is content | Two tests |
| 5 | Keep the unobserved premise visible instead of quiet: name the stripped figure on every run | The second line of `report`'s output |
| 6 | Measure the result, and print exactly what a session will no longer see | The command output below |

## 3. Implement

**The split, passage by passage.** Five passages moved; each is an argument addressed to whoever
edits `CLAUDE.md`, and none of them tells a session what to do.

| Passage | Why it is justification |
| :--- | :--- |
| *This plugin manages tasks, so it uses its own method on itself.* | Explains why the method section exists. The instruction is the sentence after it. |
| *A first tier costing more than the flat version has inverted the point of splitting it…* | Argues for the **shape** of the bound. The operative half — tier 1 stays under it, run the suite — stays in the file. |
| *It hard-codes a folder contract, a work-package vocabulary and specific commands…* | Explains why `reference/TASK-WORKFLOW.md` is not the standard. The clause that says it is not stays. |
| *The exception is why this paragraph is here and not one tier down…* + the T-118 pointer | Self-justification and provenance. The exception itself — an activity nobody announces — stays, because it is a criterion for what earns a place. |
| *The method is tier 2, so it is not loaded yet when these two apply…* | Defends the two conduct rules against being deleted as duplication. A reader deleting them is a human. |

**Deliberately left alone.** The `PATH` clause in *What this is* is justification by the same test,
and it is [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md)'s sentence. Taking
it here would decide that task's question inside this one.

**Decisions & assumptions**

- **The budget strips block comments too** — 2026-08-15, the open question above, answered by the
  maintainer. The budget bounds what a session pays, and a comment is not paid; a check that counts
  it would grow stricter than reality and would report this change as having saved nothing.
  *Rejected:* leave the figure and record the discrepancy.
- **The stripped figure is printed on every run** — 2026-08-15, and it is the reason the answer above
  is safe. The check now depends on a documented behaviour **no session here has observed**, so if
  the harness does not strip comments this file grew and the check went blind to it. Naming the
  stripped count on every run keeps that visible until it is observed. *Rejected:* strip silently.
- **Whole sentences and trailing clauses only** — 2026-08-15. Sub-clauses were left where moving them
  would have meant rewriting the maintainer's sentence. The measured result is smaller than the
  audit's estimate for this remedy, and the estimate is not what is reported.

**Outputs produced**

`CLAUDE.md` and `tests/test_budget.py`. Measured after the change:

```
tier 1 6305 chars under by 1541 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       836 chars of block comment are not counted: the harness is documented to strip them before injecting and this check follows it - not yet observed here (T-153)
```

**663 characters off the counted tier 1**, from 6,968 on 2026-08-15. The file itself grew: 836
characters now sit in comments, the difference being connective wording the passages needed once they
stood alone.

Checked by being used — the strip printed exactly what a session will no longer see, and it is the
five passages above and nothing else:

```
removed 836 chars
  | <!--
  | This plugin manages tasks, so it uses its own method on itself.
  | -->
  ... four more blocks, all listed in the split table
```

## 4. Review

**Re-judged 2026-08-16, against the criteria `specify` wrote.** The 2026-08-15 table judged five rows,
and only four of them were criteria: it added *verified by observation that the commented text does
not reach a session*, which `specify` never wrote, and left criterion 5 unjudged. The substance was
honest — that row is what criterion 2 actually demands, and admitting the gap is why this task stayed
open — but the bookkeeping hid two things. Criterion 2 was marked **met** on the strip's own printout,
which is the checker's view of the file and not a session's view, and the criterion the maintainer did
write was never ruled on at all. Both are corrected below rather than in the row above, which stands
as what was judged on the day.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every passage moved is justification for a human, and the split is stated passage by passage | met | The table above. Five passages, each with the reason. Unchanged from 2026-08-15. |
| Nothing operative went into a comment, **checked by reading the result as a session would receive it** | met | **2026-08-16, and it was not met on 2026-08-15.** [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) read what a session was handed: all five blocks absent, proven by `T-047` and `T-118` — present in `CLAUDE.md` only inside comments — reaching nothing, while `T-054` in the uncommented prose arrived. The strip's printout could never have settled this: it is the checker reading the file, and the project's rule is to run the thing on a real case. |
| The saving is measured after the change, in characters, with the date | met | 663 characters, 2026-08-15, against 6,968 measured the same day. Re-derived independently on 2026-08-16 and identical, so nothing drifted between writing the strip and observing it. |
| `tests/test_budget.py` passes, and what it now counts is stated | met | Suite `OK (skipped=3)` on 2026-08-16. It counts the file with block comments stripped and names the stripped figure on every run. **The figure is right and its provenance clause is now false** — see the child task; the criterion asks what it counts, and that part still holds. |
| The measured outcome is written into this record on the day it is known, not reconstructed later | met | **Judged here for the first time.** 663 characters written 2026-08-15, the day measured; the observation written into T-159 on 2026-08-16, the day made. |

**Child fix tasks raised**
- [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) — the one observation this task
  cannot make. Answered 2026-08-16; it is what moved criterion 2 to met.
- [T-160](T-160-retire-the-budget-check-s-unobserved-premise-warning.md) — `report()`'s second line
  still says `not yet observed here`, which T-159 made false. Raised rather than fixed here: this
  session was authorised for `review`, and the correction is `implement` work.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-10. `xs` and `medium`: the change is a pair of comment delimiters, and the gain is exact rather than estimated — the bytes leave the per-turn cost entirely. Filed as `fix` rather than `decision` because the mechanism is documented and the only judgement is which passages are justification, which the acceptance criteria make checkable. |
| 2026-08-15 | — | The open question above was found while raising this task, not by the audit: `measure()` reads the file whole, so E-10's remedy silently makes the budget check over-count. Recorded here rather than fixed, and it is the reason this task cannot be a two-line edit. |
| 2026-08-15 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review` — in a request covering T-153, T-154, T-155, T-156 and T-157 and **nothing else**. Any task raised from here takes one phase per request unless separately authorised (METHOD §3.1). Recorded in each of the five records because an authorisation kept anywhere else is one a later session can miss or stretch. |
| 2026-08-15 | → in_progress | All four phases run. 663 characters off the counted tier 1, measured. **The task stays open**: its verification criterion needs a session that has not started yet, which the maintainer chose to leave to a later one rather than spend a subagent on. [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) carries it, and this task is `blocked_by` it. |
| 2026-08-16 | → done | `review` re-run on the maintainer's request, `blocked_by` cleared when [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) closed. All five criteria met; the saving is now observed rather than documented. **The re-run found the 2026-08-15 table judging a row `specify` never wrote and skipping one it did** — criterion 2 held a pass earned on the checker's printout rather than on a session's input, and criterion 5 was never ruled on. Both corrected above; the original row is left standing as what was judged that day (METHOD rule 5). Raised [T-160](T-160-retire-the-budget-check-s-unobserved-premise-warning.md) for the one live falsehood the answer created. |
