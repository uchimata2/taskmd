---
id: T-216
title: Repair the three closed parents that still have an open child
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-212, T-135, T-168, T-192]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-216 — Repair the three closed parents that still have an open child

## 1. Specify

**Outcome**
No task in this repository is closed while one of its children is open. Each of the three current
cases is judged on its own and repaired, so that
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)'s class can ship reporting a
real state rather than this project's own backlog.

**Why this one**
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) measured the proposed class
against the live tree before planning, and it fires three times:

| Parent | type | Open child | type |
| :--- | :--- | :--- | :--- |
| [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) | `deliverable` | [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | `deliverable` |
| [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | `research` | [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) | `research` |
| [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) | `deliverable` | [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) | `research` |

**The owner settled the rule on 2026-08-22**: a child holds **every** parent open, not only an audit
umbrella — so these three are real defects rather than a shape the method allows. The reasoning, both
readings and what each costs are in
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1, and are not repeated here.

**Why it is not part of T-212.** That task ships a validator class; this one corrects three records
it happens to catch, two of which are closed. They are different work with different risks, and
folding them together would let a green suite stand in for a judgement about three tasks — which is
the reverse of what a validator is for. Raised on the owner's instruction, in the same answer that
settled the rule.

**Scope**
- In: judging each of the three on its own record, and repairing it
- In: the same sweep run again afterwards, so the count is measured rather than assumed
- Out: **the check class itself**, which is
  [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)
- Out: any other edge kind. A dependency whose blocker is open on a closed task is a different
  question, and T-212 §1 already puts it out

**The default repair, and why it is a default rather than the answer.** Move the child from `parent`
to `related` on its own record: all three children are residuals parked on an external condition, and
that is how this project already raises one — [T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md)
raised its two on 2026-08-22 with `parent: null` and a `related` edge. **It is a default because the
alternative is real**: where the parent genuinely is not finished until the child is, the repair is to
reopen the parent, and only that record can say which it is. Reopening a closed task is a change to
what a record says about the **present**, which METHOD rule 5 allows; nothing here rewrites what any
of them says about the past.

**Inputs**
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1 — the question, the
  owner's answer, and the sweep that found the three
- The six records named in the table above
- `plugin/skills/taskmd/docs/METHOD.md` §4 — which edge to use, and rule 5 on correcting a record

**Acceptance criteria**
- [ ] Each of the three is judged **individually**, with the judgement and its reason recorded — a
      blanket re-edge of all three without reading them does not meet this
- [ ] Where a child is re-edged, its parent's record is annotated rather than rewritten, so the
      original relationship is still legible
- [ ] The sweep is re-run and reports zero, and the output is quoted
- [ ] `check`, `index` and the suite are green, and the output is quoted

**Open questions**
- **None.** The rule was settled by the owner on 2026-08-22; which repair each record needs is this
  task's work.

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
| 2026-08-22 | → proposed | Raised from [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), on the owner's answer of the same date settling that a child holds every parent open and not only an audit umbrella. Raised as its own task rather than folded into T-212 because the owner's answer said so, and because correcting three records — two of them closed — is a different risk from shipping a validator class. `s` and `medium`: three records, each needing a judgement rather than an edit, and T-212 cannot reach a green suite until this closes. **This task is not covered by the multi-phase grant of 2026-08-22**, which names T-211 and T-212 and no other task. |
