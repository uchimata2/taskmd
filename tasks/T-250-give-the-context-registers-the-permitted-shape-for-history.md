---
id: T-250
title: Give the context registers and shipped documents the permitted shape for history
type: fix
status: done
phase: review
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
deliverables:
  - control/LOCAL-CONTEXT.md
  - plugin/skills/taskmd/docs/BINDING.md
  - plugin/skills/taskmd/docs/bindings/github-issues.md
  - docs/PUBLISHING.md
  - plugin/skills/taskmd/docs/method/uninvolved-reader.md
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
| 1 | Derive the corpus from the rule's own reach, not from §1's table: every Markdown file the project keeps, minus the out-list, **with the count stated**. Include `control/`, which is gitignored and which `git ls-files` therefore cannot see. | A candidate list and its size, in §3 — the denominator every later count is read against |
| 2 | Run a prose signal over the whole corpus — changelog phrasing and dates — and **record what it cannot see** before using it. | Per-file hit counts, and a named statement of the signal's blind spot |
| 3 | Read every candidate the signal hit, and a sample of those it did not, and classify each against the rule's two halves: is it a record, and if not does it carry a changelog or an account of how its wording was reached? | A verdict for **every** candidate — clean or needs-edit — not only for the hits |
| 4 | Edit each needs-edit file: compress to the fact, its source, the date, one clause of why; where a task record already holds the detail, cite the id and delete the retelling. One commit per file, per the owner's answer in §1. | The edited files, one commit each |
| 5 | For every edited file under `plugin/`, state what the passage claimed before and what it claims after, so a changed promise is visible rather than inferred. | A before/after claim pair per shipped edit |
| 6 | After each file: `taskmd check`. After the last: the suite, and `tests/test_budget.py` in particular if `CLAUDE.md` was edited, since that file is tier 1 and the budget is measured in characters. | Captured exit codes |

**Decisions taken here**

- **`reference/` is out of scope** — 2026-08-23. §1's Scope out-list names records without naming
  this folder, but §1's own measurement excluded it, and `../CLAUDE.md` calls
  `reference/TASK-WORKFLOW.md` *the pre-split standard from one real project — evidence of what
  worked*. Compressing imported evidence falsifies the evidence, which is the same argument the
  out-list already makes for the `control/adopter-report-*.md` copies. *Rejected: treating it as an
  ordinary project document*, which would have put four files in the corpus whose value is that they
  are unedited. If this is wrong the cost is four files re-examined, and nothing has been deleted.

- **Step 3 records a verdict for every candidate, not only for the ones edited** — 2026-08-23. The
  first acceptance criterion asks for a list a reader can check *that no fact was dropped rather than
  relocated*; a list of only the hits cannot show what was examined, and reads as complete. *Rejected:
  listing the edited files alone*, which is what the criterion literally asks for and which would make
  the sweep's silence unfalsifiable.

- **The prose signal ranks, it never decides** — 2026-08-23, and this is §1's own finding rather than
  a new one: `.handoff/config.md` scores 1.1 dates/KB *after* it was fixed, because the permitted
  shape ends in a date. So step 2 feeds step 3 and no file is edited or cleared on a count.

**Outputs this task will produce**

```text
the files step 3 classifies as needing an edit — named in §3, not here, because
step 1 derives the membership and a list written now would be the stale table
the fifth acceptance criterion forbids
```

## 3. Implement

**The corpus, derived 2026-08-23, and its size.** Every Markdown file the project keeps, minus the
out-list and minus `reference/`: **25 candidates** — 24 tracked plus `control/LOCAL-CONTEXT.md`,
which is gitignored and which `git ls-files` cannot see. **Five were edited and twenty were read and
left alone**, and the twenty are listed because a list of only the hits cannot show what was
examined.

**Decisions & assumptions**

- **The prose signal was recomputed and then distrusted, in that order** — 2026-08-23. It reproduces
  §1's own figures — `control/` at 1.60 dates/KB, `github-issues.md` at 0.61, the two configs at 0.04,
  and the calibration case `.handoff/config.md` at 1.11 *after* being fixed — which is what says the
  derivation is the same one, and what says it cannot judge. Every file was classified by reading the
  passages, never by the count. **The signal's blind spot, stated before it was used**: it is keyed on
  English phrasing, so a history block that never says *previously* or *used to* is invisible to it.
  One such block was found by reading — `METHOD.md`'s dated decision on the child-holds-parent rule,
  which scored zero and is *kept*, being a decision with its rejected alternative rather than an
  account of a wording.

- **Two files the signal ranked low turned out to matter and one it ranked high did not** —
  2026-08-23, and this is the fifth acceptance criterion earning its keep. `docs/PUBLISHING.md`
  **is not in §1's table at all** and carried two real passages; `plugin/skills/taskmd/docs/method/
  uninvolved-reader.md` scored two hits and carried one. Meanwhile
  `plugin/skills/taskmd/docs/bindings/local-markdown.md`, which §1's table lists as a shipped file
  with five changelog lines, has **none**: both its hits are ordinary prose about behaviour — *"a
  closed task whose outcome no longer exists"* and *"a renamed file is still found"*.

- **The two 25 KB configs needed no edit at all**, against §1's expectation of a five-line edit each
  — 2026-08-23. Their three hits apiece are *"renamed fields"* and *"a claim the task no longer
  makes"*, both ordinary prose. §1 predicted the direction of the finding (their bulk is guide prose)
  and overstated the residue.

- **`control/LOCAL-CONTEXT.md` produces no commit, and the owner's one-commit-per-file answer cannot
  reach it** — 2026-08-23. It is gitignored. It was backed up to a scratch copy before editing for
  the same reason, since `git checkout --` has nothing to restore it from.

- **The register's trail columns became a command rather than a list, and then the command was
  measured** — 2026-08-23. `grep -rl "<label>" tasks/` returns the records that cite a label, which
  is **not** the same set the old rows enumerated: seven of the deck-building sibling's named tasks,
  four of the Handoff sibling's, three of the context-audit sibling's and two of the first adopting
  project's do not cite their label and are unreachable by it. Rather than present the derivation as
  equivalent, the file states what it reaches, lists that closed residue, and adds the forward rule
  that makes it complete — a record raised from a sibling cites that sibling's label.
  *Rejected: keeping the enumeration*, which drifts; *rejected: leaving the derivation unqualified*,
  which is a filter reporting its own completeness.

- **Four foreign task ids were found in the register and deleted rather than relabelled** —
  2026-08-23. The old rows carried the deck-building sibling's `T-042`, `T-062`, `T-161` and `T-218`
  in running prose beside our own ids with nothing marking them foreign, and **every one of the four
  collides with a real task in this repository** — ours are *Make the GitHub binding's update
  preserve what it did not touch*, *Report two tasks claiming one id*, *Give the entry-point
  comments' pointer a reader* and *Give the rule that a child holds its parent open a home*. Each
  belonged to a narrative that is the sibling's own to keep, so they went with it, and the file now
  states that a foreign id is written with its owner named beside it or not written.

**Outputs produced — the five edited**

| File | What was compressed | What it now cites |
| :--- | :--- | :--- |
| `control/LOCAL-CONTEXT.md` | Six label-map rows carrying the whole trail of what each sibling reported and what came of it; a blockquote recording that a sentence about the config count *stopped being true later the same day*; nine lines of another project's open defects; the account of the shell trap the suite section used to warn about. **30,810 → 11,469 bytes; longest cell 11,374 → 1,616 chars** | `grep -rl "<label>" tasks/` per row; the two `adopter-report-*.md` copies beside it; `github.com/uchimata2/taskmd/issues/1` and pull request 2; T-135 §3 and T-173 §3 for the config counts; the maintainer's global conventions for the WSL/Git Bash trap and for the fix-it-there rule |
| [`plugin/skills/taskmd/docs/BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) | Five accounts of what the document used to say: an earlier draft of *Size is not the test*, an unmeasured word count carried "for as long as it existed", what the gap clause did before 2026-08-22, the class-name pattern before 2026-08-22, and the two §3 edits §5 caused | Nothing new — every claim was already stated beside its history and now stands alone |
| [`plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) | Five: the totals removed from the coverage preamble, *this row used to sit above*, the paragraph preserving its own wrong date, the superseded *either way* sentence, and what the no-ordering item used to say | Nothing new; same reason |
| [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) | §6's *two earlier drafts were wrong*, restated as two failure shapes to expect; §7's *keyed on `--work_package` until 2026-08-23*, restated as the rejected alternative | [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md), which already held the decision |
| [`plugin/skills/taskmd/docs/method/uninvolved-reader.md`](../plugin/skills/taskmd/docs/method/uninvolved-reader.md) | *Corrected after a run that used two where its own rule said one*, and the closing sentence about what the rule had been written to forbid | Nothing new; the measured claim stands alone |

**Read and left alone — the twenty**

Four groups, and **9 + 3 + 1 + 7 = 20**, which with the five edited is the 25 the corpus derived.

- **Ordinary prose the signal mistook for history (9):** `.taskmd/config.md`,
  `plugin/skills/taskmd/taskmd/defaults/config.md`, `README.md`, `docs/SCOPE.md`,
  `plugin/skills/taskmd/docs/bindings/local-markdown.md`,
  `plugin/skills/taskmd/docs/method/review.md`, `plugin/skills/taskmd/docs/HANDOFF.md`,
  `plugin/skills/taskmd/adopt.md`, `plugin/skills/taskmd/docs/method/pre-release-audit.md` —
  *renamed*, *no longer exists*, *superseded* used as description, not as a changelog.
- **Already the permitted shape (3):** `.handoff/config.md`, T-249's own output and the calibration
  case; `plugin/skills/taskmd/docs/METHOD.md`'s dated child-holds-parent decision, which carries its
  rejected alternative and its 218-task measurement; `plugin/skills/taskmd/docs/method/plan.md`'s
  *superseded steps are the rejected alternative*, which is the rule itself.
- **Annotated evidence, where rewriting falsifies the record (1):** `docs/BRIEF.md`, whose blockquote
  says two of its own sentences stopped being true on 2026-08-18 and are kept because the argument
  they carry is what raised the work. That is METHOD rule 5's *annotate the past* applied correctly,
  in a document whose content is dated evidence. Its other signal hit, *a declared file that had been
  deleted*, is ordinary prose.
- **No history and no signal hit (7):** `CLAUDE.md`, `plugin/skills/taskmd/SKILL.md`, and the method
  files `where-facts-live.md`, `specify.md`, `rationale.md`, `implement.md`, `audit.md`.

`docs/PUBLISHING.md` is **not** in these groups — it is one of the five edited. Its §4 passage *it
moved here from T-079 §3* was read and left, being fact, source and one clause of why; that is a
passage left alone inside an edited file, not a file left alone.

**Checked by using it.**

*The corpus is derived, and it sums.* 24 tracked candidates plus 1 gitignored = 25; 5 edited + 20
left = 25.

*Every derived pointer in the register resolves*, which is the thing a command in place of a list can
get wrong:

```text
the Notion-backed project         3      the deck-building sibling      14
the throwaway proof repository    1      the diagram-modelling sibling   2
the install-rehearsal repository  1      sibling plugin                  4
the first adopting project       14      the context-audit sibling       2
```

*No adopter-facing statement changed meaning*, checked passage by passage on the four shipped files.
Every edit deleted an account of a previous wording and left the claim; none rewrote a claim. The
before/after pairs are the *What was compressed* column above, and the mechanical half is:

```text
check exit=0
345 passed, 7 skipped, 6 subtests passed
```

run after each of the four tracked files, not once at the end.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every file edited is listed with what was compressed and what it now cites, so a reader can check that no fact was dropped rather than relocated | met | §3's *Outputs produced* table, five rows, two columns doing exactly that. **The criterion did its job rather than merely passing**: checking it found two facts in the register with no home anywhere — the sibling's disproof of a brief written here, and the one handoff ever written into that checkout — and both were restored rather than dropped. `grep -rl` over `tasks/` and `docs/` is what showed they had no home |
| No adopter-facing statement changed meaning. The shipped documents are contracts | met | Four shipped files edited, passage by passage. Every edit deleted an account of a previous wording; none rewrote a claim, and the before/after is the table's second column. The mechanical half is `check exit=0` and `345 passed, 7 skipped` re-run after each file rather than once at the end |
| `control/LOCAL-CONTEXT.md` holds no cell that restates a task record it already cites | met | No cell now carries a trail. **30,810 → 11,469 bytes, longest cell 11,374 → 907 chars.** What survives is identity, the facts with no other home, and a command per row. Its own former last sentence — *"this row is the trail; the tasks carry the detail"* — is what the file had been admitting and now acts on |
| `taskmd check` passes, and the shipped documents still pass whatever the suite asserts of them | met | `check exit=0`, `index exit=0`, `345 passed, 7 skipped, 6 subtests passed`, after each of the four tracked edits |
| The membership of this sweep is derived from the rule's own test at implement time, not from the table above | met | Derived at implement, and it disagreed with the table in both directions — `docs/PUBLISHING.md` absent from the table and carrying two real passages, `local-markdown.md` listed with five changelog lines and carrying none. Had the table been the membership, one file would have been edited that needed nothing and one needing work would never have been opened |

**Adopter-visible?** no. Four of the five edited files ship inside `plugin/`, so this is the row that
needed thinking about rather than assuming. What changed in them is prose recording how their own
wording was reached; **no rule, no operation, no assumption and no promise moved**, which is the
second acceptance criterion and is why it was written to be judged separately from the first. An
adopter who installs the next release sees the same output, receives the same files and has nothing
to do differently — they read four documents that are shorter. `docs/PUBLISHING.md` and
`control/LOCAL-CONTEXT.md` are not shipped at all.

**Child fix tasks raised**
- none. Every criterion is met.

**Two residuals, routed rather than dropped.**

- **The register now carries a forward rule that nothing enforces**: *a record raised from a sibling
  cites that sibling's label*. It is what keeps the derived trail column complete, and today it rests
  on a session remembering. Not raised as a task, because the register is gitignored and a checker
  for a convention in an unpublished file is a cost this project has declined before
  ([T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)); the residue it protects is
  a closed set and is written out beside it.
- **The one-commit-per-file answer cannot reach `control/LOCAL-CONTEXT.md`**, which is gitignored and
  produced no commit. Stated in §3 as an assumption rather than treated as an exception, because the
  owner's answer was given before that consequence was visible.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no status change) | **`control/LOCAL-CONTEXT.md` was produced by this task and is quarantined, and its path was removed from `deliverables` here.** The removal is not a correction of what happened: the file exists, this task made it, and `control/` is gitignored by T-013 so no clone will ever hold it. Declaring it took `check` to exit 1 for every reader but this machine, and CI red for a day. Removed under the decision recorded in the local-markdown binding, taken on the owner's answer of 2026-08-23 (T-257). **T-258 is raised to make the declaration safe again** — when `check` reports an untracked declared path as excluded rather than missing, this line can come back. |
| 2026-08-23 | → done | **`review` done and the record closed**, under the grant below. Five criteria, five met, no child raised. The first one is the row to read: checking that no fact was dropped rather than relocated found two facts in the register with no home anywhere, and both were restored. `adopter_visible` is `no` and was judged rather than assumed — four of the five edited files ship, and what moved in them is prose about their own wording, not a rule, an operation, an assumption or a promise. Two residuals are named in §4 rather than left for a sweep: the forward rule the register now depends on, and that the one-commit-per-file answer cannot reach a gitignored file. |
| 2026-08-23 | → in_progress | **`implement` done**, under the grant below. **25 candidates derived, 5 edited, 20 read and left**, and §3 lists all twenty because a list of hits cannot show what was examined. Three things the plan did not foresee, all in §3 as decisions: **§1's table was wrong in both directions** — `docs/PUBLISHING.md` is absent from it and carried two real passages, while `local-markdown.md` is listed with five changelog lines and has none, which is the fifth criterion earning its keep; **the register's derived trail is not equivalent to the enumeration it replaced**, so the file states its reach, lists the closed residue and adds the forward rule that completes it; and **four foreign task ids were found in the register, every one colliding with a real task here**. |
| 2026-08-23 | → planned | **`plan` written**, under the grant below. Six steps. Two shape it: step 1 states the corpus size before anything is classified, so the sweep has a denominator; and step 3 records a verdict for every candidate, not only the ones edited, because a list of hits alone cannot show what was read. `reference/` was decided out — imported evidence, like the adopter-report copies. |
| 2026-08-23 | (no change) | **The owner re-stated the grant on resuming**, 2026-08-23: *"continue with T-250, full lifecycle, commit and push."* Recorded because it arrived in a session that had not yet opened this record, and the row below — *"No phase beyond `specify` was authorised"* — was written before it and is about the answers to the two questions, not about the grant two rows down. Neither is corrected; both were true when written. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, with commit and push** — given 2026-08-23 in these words: *"Work T-250, T-241, full lifecycle, commit and push, including anything raised during the work of these tasks."* Recorded here rather than only in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, committing and pushing, and the same for any task raised *by this work*. **What it does not:** any other task in the backlog — T-244, T-246, T-247, T-248 and T-240 are untouched by it. |
| 2026-08-23 | → specified | **Both open questions answered by the owner on 2026-08-23**, in these words: *"Your picks accepted."* `control/LOCAL-CONTEXT.md` is a register and is compressed; the sweep lands one commit per file. The rejected halves are kept in §1 beside each question. No acceptance criterion moved. **No phase beyond `specify` was authorised.** |
| 2026-08-23 | → proposed | **Raised on the owner's request of 2026-08-23**: *"Raise a task for control/LOCAL-CONTEXT.md, any other similar files in the project."* The membership was measured rather than guessed, and the measurement narrowed it: the two 25 KB configs carry one date between them and are almost entirely guide prose, so they are a five-line edit each and not the sweep they look like. |
