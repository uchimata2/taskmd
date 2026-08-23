---
id: T-250
title: Give the context registers and shipped documents the permitted shape for history
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-249, T-073, T-092]
work_package: M7
owner: the project owner
business_value: medium
effort: m
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-250 — Give the context registers and shipped documents the permitted shape for history

## 1. Specify

**Outcome**
Every file this project keeps that is **not** a record carries history only in the shape
[`../CLAUDE.md`](../CLAUDE.md) *Write the fact, not its history* permits: the fact, its source, the
date, one clause of why. Guide prose stays untouched. `control/LOCAL-CONTEXT.md` is the largest case;
the shipped bindings are the highest-stakes one.

**Why this one**
[T-249](T-249-cut-the-handoff-config-back-to-a-config.md) fixed one file and recorded the rule. It
scoped every other file out, on the owner's answer, so the rule now exists with one instance. This
record is the rest.

**What was measured, 2026-08-23.** Two signals over every Markdown file outside `tasks/` and
`reference/`: dates per KB, and lines carrying changelog phrasing (*previously*, *until 20…*,
*renamed*, *had been*).

| File | Bytes | Dates/KB | Changelog lines | Reading |
| :--- | ---: | ---: | ---: | :--- |
| `control/LOCAL-CONTEXT.md` | 30,810 | 1.6 | 6 | The case. Its largest single table **cell** is **11,374 characters** |
| `plugin/skills/taskmd/docs/bindings/github-issues.md` | 52,392 | 0.6 | 9 | Shipped. An adopter reads it |
| `plugin/skills/taskmd/docs/BINDING.md` | 28,047 | 0.4 | 5 | Shipped |
| `plugin/skills/taskmd/docs/bindings/local-markdown.md` | 16,650 | — | 5 | Shipped |
| `.taskmd/config.md` | 25,076 | 0.04 | 5 | Mostly guide. Small edit |
| `plugin/skills/taskmd/taskmd/defaults/config.md` | 25,047 | 0.04 | 5 | Shipped. Mostly guide. Small edit |

**The two configs are not the problem, which is the finding that shapes this.** 25 KB each and one
date between them: their bulk explains what a key means and what changing it costs, which is exactly
the guide prose the rule keeps. Expecting them to shrink is the wrong expectation, and the ~5
changelog lines in each are the whole edit.

**Neither signal can judge, and the calibration says so.** `.handoff/config.md` **after** T-249 fixed
it scores 1.1 dates/KB — mid-table, above `docs/BRIEF.md` — because the permitted shape *ends in a
date*. So both numbers rank files for a human to read and neither condemns one. Any implementation
that sorts by them and edits the top is measuring the wrong thing.

**Scope**
- In: files where the rule binds — configs, instruction files, project documents, and hand-kept
  registers such as `control/`
- In: compressing a passage to the permitted shape, never deleting the fact. Where a task record
  already holds the detail, the surviving line cites the id
- Out: **records, where history is the content** — `tasks/`, `docs/audits/`, the
  `control/adopter-report-*.md` copies, `tests/fixtures/`, and this file. Rewriting a copy of
  somebody else's document falsifies the copy
- Out: **the 249 existing task records.** T-249 settled that: new writing only, and METHOD rule 5
  forbids rewriting what a record says about the past
- Out: guide prose of any length. Length is not the test

**Inputs**
- [`../CLAUDE.md`](../CLAUDE.md) *Write the fact, not its history* — the rule, and the only authority
  here
- [T-249](T-249-cut-the-handoff-config-back-to-a-config.md) §3 — the worked example: sixteen blocks
  classified, two moved, fourteen deleted against a named home
- `control/LOCAL-CONTEXT.md` — gitignored, so `check` does not read it and no link in it is verified

**Acceptance criteria**
- [ ] Every file edited is listed with what was compressed and what it now cites, so a reader can
      check that no fact was dropped rather than relocated
- [ ] No adopter-facing statement changed meaning. The shipped documents are contracts, and a
      compression that alters what a binding promises is a defect, not an edit
- [ ] `control/LOCAL-CONTEXT.md` holds no cell that restates a task record it already cites
- [ ] `taskmd check` passes, and the shipped documents still pass whatever the suite asserts of them
- [ ] The membership of this sweep is derived from the rule's own test at implement time, not from
      the table above — that table is dated evidence and will be stale

**Open questions**
- ~~**One commit per file, or one for the sweep?**~~ **Answered by the owner on 2026-08-23: one
  commit per file.** *The question as it stood, kept so a later reader can see what was chosen over
  what: — whoever implements it. The recommendation is* **one commit per file**, *because the shipped
  bindings are contracts and a reviewer needs to see each against its own diff. Against: six commits
  for one outcome, and the sweep then has no single point where it can be judged complete — mitigated
  by the first acceptance criterion, which is that list.*
- ~~**Does `control/LOCAL-CONTEXT.md` count as a record?**~~ **Answered by the owner on 2026-08-23:
  no — it is a register, and is compressed.** *The question as it stood: — the project owner. The
  recommendation is* **no, it is a register**: *history is what it holds, but its rows reproduce
  narratives that already live in the task records they cite, which is the duplication the rule
  exists to stop. Against: it is gitignored and costs nothing to publish, so the only reader it
  burdens is a session that opens it — which is the same argument that let the handoff config reach
  16 KB.*

Both answers leave the acceptance criteria unchanged; §1 already covered either outcome. The second
one settles which file the third criterion binds on.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, with commit and push** — given 2026-08-23 in these words: *"Work T-250, T-241, full lifecycle, commit and push, including anything raised during the work of these tasks."* Recorded here rather than only in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, committing and pushing, and the same for any task raised *by this work*. **What it does not:** any other task in the backlog — T-244, T-246, T-247, T-248 and T-240 are untouched by it. |
| 2026-08-23 | → specified | **Both open questions answered by the owner on 2026-08-23**, in these words: *"Your picks accepted."* `control/LOCAL-CONTEXT.md` is a register and is compressed; the sweep lands one commit per file. The rejected halves are kept in §1 beside each question. No acceptance criterion moved. **No phase beyond `specify` was authorised.** |
| 2026-08-23 | → proposed | **Raised on the owner's request of 2026-08-23**: *"Raise a task for control/LOCAL-CONTEXT.md, any other similar files in the project."* The membership was measured rather than guessed, and the measurement narrowed it: the two 25 KB configs carry one date between them and are almost entirely guide prose, so they are a five-line edit each and not the sweep they look like. |
