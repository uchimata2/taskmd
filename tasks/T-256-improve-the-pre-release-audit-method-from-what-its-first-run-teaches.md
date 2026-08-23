---
id: T-256
title: Improve the pre-release audit method from what its first run teaches
type: fix
status: proposed
phase: specify
parent: null
blocked_by: [T-244]
related: [T-223]
work_package: M7
owner: the project owner
business_value: high
effort: m
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-256 — Improve the pre-release audit method from what its first run teaches

## 1. Specify

**Outcome**
[`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) carries what running
it taught, so the next project to load it gets the method as executed rather than as proposed. Every
change is traceable to something a real run refused, and a rule that survived untouched is recorded
as having survived.

**Why this one**
[T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
§1 states it: *any change the method needs is a separate task, not an edit made here*. This is that
task. It is raised now rather than at the end because **planning T-244 already produced five
method-level observations**, and an observation held only in a session is one that dies with it.

**This task must not run before T-244 does**, and the edge says so. The method's own position is that
a document shipped on practice without execution is a claim —
[T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) did exactly that and T-244 exists to
test the result. Editing the method now, on planning alone, would repeat the error the method was
written to name.

**The five observations planning produced, before any cycle ran**

Candidates, not conclusions. T-244 step 11's judgement comes from the run and merges with these; a
row the run does not support is dropped and the drop is recorded.

| # | Observation | What in the method it touches |
| :-- | :--- | :--- |
| 1 | **A partition must be derived by a command that fails on an unassigned item.** §2 says coverage is a partition and that it fails, then names no mechanism — so both projects that have planned one hand-typed the membership. htmldeck's `PR-06` is what that cost there: two coverage tables that could not reconcile, four files unread, and it looked like one. Here it produced [T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md) before a cycle ran. **Two independent projects, same failure, from a rule that is correct and unactionable** | §2 |
| 2 | **A grade with no members is stated, not omitted.** §1's table reads as an invitation to list the grades that apply. This subject has no Narrow members at all, which is a fact about it — that the project ships nothing settled — and a dropped row leaves a reader unable to tell that from an oversight | §1 |
| 3 | **A cycle-size figure does not travel between projects.** §3 says the limit is attention rather than volume, which is right and is not what a reader does with another project's number. htmldeck sizes a cycle at ~300 KB; this subject is 378,979 bytes total, so the figure said *merge eight cycles into two*. It was wrong because half of that project's byte mass is Grade-B closed record and this subject has none. The mix stays behind and the number travels | §3 |
| 4 | **Aspects and stages are two things, and the method names one.** §1's aspects are lenses that stop two cycles examining the same thing under different names. What orders the program is something else — where findings are expected, and what would invalidate the rest. Both plans needed both, and both invented the second | §1, §3 |
| 5 | **The method gives no shape for the plan's own display, and two projects converged on the same one.** A coverage-grade table with a totals row, stage separators that argue their own placement, per-cycle Files / Bytes / Status columns, a register with a reserved id space, and a *how to run one cycle in a fresh session* block. Independent convergence is the evidence a worked shape is missing rather than a preference | the worked example |

**Scope**
- In: `plugin/skills/taskmd/docs/method/pre-release-audit.md` — the only home of the method
- In: each of the five above, and each finding T-244 step 11 adds, either applied or refused **with
  the reason recorded**. A refusal is a result
- In: whether any of them belongs in [`audit`](../plugin/skills/taskmd/docs/method/audit.md) instead,
  because it is true of every audit rather than of this size
- Out: the judgement itself. T-244 step 11 produces it; this task applies it
- Out: T-244's own findings about the *product*. Those are that record's children
- Out: any change to how this project runs its audit. The document is the deliverable

**Inputs**
- [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)
  §4 — the judgement on the six rules, which does not exist until that record reaches step 11
- [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) — what was shipped, and on what
  evidence

**Acceptance criteria**
- [ ] Every one of the five observations above, and every finding T-244 step 11 raises, is either
      applied to the document or refused with a recorded reason
- [ ] The document states which of its six rules earned their place on a real run and which did not,
      and a rule that survived untouched is recorded as having survived rather than left silent
- [ ] No change is made that the run did not support — each edit names what refused the old text
- [ ] `docs/PUBLISHING.md`'s adopter-visible test is applied, since this document ships to every
      adopter

**Open questions**
- **Does observation 1 belong to `audit` rather than here?** A partition that cannot be checked
  mechanically fails at any size; it is only *fatal* at this one. Whoever plans this.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised on the owner's question of 2026-08-23**: whether the audit method had been improved from what listing the cycles taught, or whether only the current process had been patched. **The answer was the second, and this record is the correction.** [T-255](T-255-derive-the-audit-cycle-membership-instead-of-typing-it.md) is repository machinery for this one audit and explicitly out of scope for what an install copies, so it improves nothing an adopter receives. Nothing in `plugin/` had been touched. **The five observations above come from planning T-244, not from running it**, and are recorded now because a session's observations die with the session — but the record is `blocked_by` T-244 so that the judgement from the actual run merges with them before the document is edited. Editing on planning alone would repeat T-223's error, which is the error T-244 exists to test. |
