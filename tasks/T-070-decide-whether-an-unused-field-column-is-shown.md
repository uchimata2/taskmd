---
id: T-070
title: Decide whether an unused field column is shown at all
type: decision
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-022, T-001]
work_package: none
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-070 — Decide whether an unused field column is shown at all

## 1. Specify

**Outcome**
One rule governs whether a column appears in a generated view, applied to stored fields as well as to
edges — so a project that never uses a field does not read it in every index row and every `context`
header.

**Why this one**
Raised as **F-8** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 4 and 5. The shipped default names `work_package` in both `context_fields` and
`index_columns`. Every one of this repository's 58 tasks carries `work_package: none`. Result:

```
tasks/README.md   | ID | Title | Work Package | Status | Phase | ...
                  58 rows, every Work Package cell "-"

taskmd context T-053
status done | phase review | type decision | work_package - | owner maintainer
```

**The code already implements the opposite rule, and says so.** `index_block()`:

> Edge columns appear only when some task uses them. Omitting an unused edge is derived from the data
> rather than configured — a project with no hierarchy should not read a column of dashes, and one
> that starts using it should not have to remember to switch a column on.

That reasoning is exactly as true of `work_package` as of `parent`. It is applied to one of the two
column families and not the other, and this repository is the demonstration.

**The cost, stated rather than asserted.** A dead column in the index is read by everyone who opens
the generated file and by every agent that reads it; a dead field in the `context` header is paid on
**every** `context` call, which is the command whose entire justification is that it returns what is
needed *and nothing else* (R-15). Neither is large. Both are permanent, and both are paid by every
adopting project that takes the default and does not use work packages.

**Why `decision` and not `fix`.** Three answers are defensible and they differ in what they cost an
adopter, not in effort — see the open question. This is a design call about the shipped defaults, and
one of the options touches R-15's headline claim.

**Requirements served**
R-15 (`docs/SCOPE.md`) — *and nothing else* is the claim; §1 *Token cost*; §2 principle 2, since
"which columns have content" is derivable.

**Scope**
- In: whether a stored-field column with no values in the project is rendered, in `index` and in
  `context`.
- In: whether `work_package` belongs in the shipped default's `context_fields` and `index_columns` at
  all.
- Out: the `work_package` **field** and its vocabulary. Removing a field a project may use is not on
  the table; this is about views.
- Out: edge columns, which already behave correctly.
- Out: the ordering rule and the estimate fields, settled in
  [T-022](T-022-filtered-task-listing-for-scripts.md).

**Inputs**
`plugin/taskmd/cli.py` (`index_block`, `cmd_context`, `cmd_list`),
`plugin/taskmd/defaults/config.md` (`context_fields`, `index_columns`), `tasks/README.md`,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-8.

**Acceptance criteria**
- [ ] One stated rule covers both column families, or it is recorded why they differ
- [ ] Whatever is chosen, this repository's generated index and `context` output are shown before and
      after, so the saving is measured rather than claimed
- [ ] A project that *does* use the field is unaffected — demonstrated, since
      `tests/fixtures/alt-project` has its own field names and can carry the case
- [ ] Nothing requires an adopter to remember to switch a column on or off (§1 *Invisibility*)
- [ ] `taskmd/defaults/config.md` describes the resulting behaviour, since it is the only description
      of what a config may contain

**Open questions**
- **Which of three?** *(a)* **Derive it** — omit any `index_columns` / `context_fields` entry no task
  has a value for, exactly as edge columns already work. Consistent, invisible, and it means a
  project's `context` header changes shape as fields get used, which a script parsing it would feel.
  *(b)* **Drop `work_package` from the shipped defaults' views**, leaving the field available and
  unlisted. One line, no behaviour change, and it leaves the inconsistency in place for the next
  unused field. *(c)* **Leave it** — a reserved column tells a reader the field exists, which is a
  real argument for `index` and a weak one for `context`. Only the maintainer can weigh (a)'s
  variable-shape output against (b)'s narrowness; `plan` cannot.

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
| 2026-08-09 | → proposed | Raised as F-8 from the T-059 audit, clauses 4 and 5. Counted before write-up: all 58 tasks carry `work_package: none`, so the generated index holds 58 dashes and every `context` header carries a dead field. Typed `decision` because the three answers differ in what they cost an adopter rather than in effort, and one of them changes the shape of `context`'s output. The clause-5 half is that the code already states the cheaper rule for edge columns and applies it to half the problem. |
