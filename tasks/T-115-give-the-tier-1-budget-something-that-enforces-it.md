---
id: T-115
title: Give the tier 1 budget something that enforces it
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-028, T-047, T-063]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [tests/test_budget.py]
adopter_visible: no
---

# T-115 — Give the tier 1 budget something that enforces it

## 1. Specify

**Outcome**
The tier 1 budget either has something that reports a breach without being remembered, or it is
written down that nothing does and the number is advisory — so the next edit that crosses it is
noticed by the project rather than by whoever happens to re-run a documented command.

**Why this one**
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) brought tier 1 under
the bound for the first time. It **passes by 8 characters** — 7,911 against 7,919. That margin is
smaller than a single sentence, and T-047's own log records the mechanism that will spend it: tier 1
grows whenever a task closes and the tree is made honest, which happens most sessions and is nobody's
edit to tier 1 in particular.

**Nothing runs the check.** The budget is a bash line in `CLAUDE.md` that someone has to remember to
run. That was harmless while the file was 4,817 over — a permanently failing budget cannot be
regressed — and it stops being harmless the moment the margin is 8. This is the shape
[T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) rejected an `--all`
flag for and [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) and
[T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) were both raised about: a check
nobody is prompted to run is silence with a command attached.

**And the command does not measure what the rule says it measures.** `CLAUDE.md` states the budget in
**characters** — [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) D1, taken after
measuring both units — while the shipped command is `wc -c`, which counts bytes. The two disagree
about the verdict, not merely the figure: 7,911 against 7,919 in bytes is a pass by 8; 7,856 against
7,846 in characters is a **failure by 10**. Both files are LF-only, so this is punctuation rather than
line endings — `—`, `§` and `→` cost three bytes and one character, and the two documents use them at
different densities, so the byte view flatters the denser one. `wc -m` is not the repair: this
machine's `wc` reports 3 for both `-c` and `-m` on a single em dash, so a bash one-liner cannot count
characters here at all. T-063's own record already carries both numbers for the same file under the
same command — 7,846 in D1, 7,919 in its closing log — without reconciling them. Settled with the
maintainer on 2026-08-10: the unit is **characters**, so tier 1 is in breach now and whatever enforces
it is red from the moment it exists.

**The awkward part is that this is not `check`'s job.** The budget compares one project file against
another and is specific to this repository's tiering; taskmd validates a task tree and ships to
adopters who have neither. So an answer that adds it to `check` has to say why an adopter is made to
carry it, and an answer that adds a test has to say why the suite tests the repository's prose.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: whether anything enforces the bound, and what — a test, a `check` rule, an `after_write` hook,
  or nothing with the consequence written down.
- In: whether the margin is a number worth stating at all, given that both sides move.
- In: what the check counts. The documented rule and the documented command disagree, and the
  disagreement decides the verdict — so enforcement cannot be built without settling it.
- Out: bringing tier 1 back under the bound, if it is still over once this task's own edits land.
  That is a cut, which the line below owns; it becomes a child task rather than work done here.
- Out: the bound and the tiering. T-028 settled both and T-047 executed against them.
- Out: what tier 1 contains. That is T-047's, now closed, and re-opening it here would be a cut
  chosen to fit a number.

**Inputs**
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) §3, for the
  measurement and the sections it came from.
- [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md), for why the count reads the tree
  rather than a list, and why characters rather than lines.
- `CLAUDE.md` *Working method*, which holds the command.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative
- [ ] If something enforces it: a tier 1 deliberately pushed over the bound is reported, shown
      failing first
- [ ] If nothing does: `CLAUDE.md` says so where the command is, so a reader does not assume the
      number is guarded
- [ ] Whatever is decided does not make an adopter carry this repository's tiering
- [ ] The check counts the unit `CLAUDE.md` states, and the same tree yields the same figure whatever
      shell it is run from

**Open questions**
- ~~**Whether an 8-character margin is a passing state or a defect.**~~ **Answered by the maintainer,
  2026-08-10: a passing state, but unguarded** — the bound is met, so nothing is cut to fit a number,
  and what this task fixes is that no breach is reported rather than how close the margin is. Then
  **superseded the same day**, because the 8 was a byte margin: in the unit the rule states there is
  no margin to judge. The ruling survives in the part that still applies — no cut is chosen here.
- ~~**Which unit the budget is denominated in.**~~ **Answered by the maintainer, 2026-08-10:
  characters**, as T-063 D1 decided, against the rival of amending `CLAUDE.md` to say bytes. Bytes
  would have kept every recorded figure true and the tree green, at the cost of re-opening a decision
  taken *after* measuring both units and of denominating the budget in a unit that moves with
  punctuation rather than with content.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Weigh the four candidates — a suite test, a `check` rule, an `after_write` hook, and nothing-with-the-consequence-written-down — against the two constraints `specify` names: it reports without being remembered, and it does not make an adopter carry this repository's tiering. | The decision and its rejected alternatives, recorded in §3 |
| 2 | Build whatever step 1 chose, deriving tier 1's membership from the tree rather than a list, counting the unit the rule states, and printing both figures and the margin rather than a bare verdict. Steps 3–7 assume step 1 chooses a mechanism that runs; if it chooses *nothing*, they collapse into a single edit saying so where the command lives. | tests/test_budget.py |
| 3 | Run it on the tree as it stands, which is over the bound, and again on a tier 1 deliberately put under it — so it is shown failing **and** shown able to pass, rather than being a check that is merely red. | Both runs' output, recorded in §3 |
| 4 | Move the procedure out of `CLAUDE.md` to wherever step 1 put it, leaving a pointer. The rule's home does not move; the command's does. | Edited CLAUDE.md |
| 5 | Re-measure tier 1 after step 4, because step 4 edits the thing being measured, and state the figure whichever way it falls. | The number, recorded in §3 |
| 6 | If tier 1 is still over, raise the cut as a child task — it is an out-line here. If step 4 brought it under, record that, and record that the reduction was a consequence rather than a target. | A child task, or a recorded finding that none is needed |
| 7 | Run `check` and `index`, and the full suite, stating the result against the four failures this tree is already known to carry. | The commands' output, recorded in §3 |

**Deliverable shape** — a Python `unittest` module in `tests/`, run the same way as its neighbours.
Rejected: **keeping it a shell one-liner**, because this machine's `wc` counts bytes under `-m` as
well as `-c`, so bash cannot express the unit the rule uses; and **a shell script beside the
launchers**, which would put a repository-specific check inside `plugin/`, the subtree an install
copies. `tests/` is outside that subtree, which is what lets the suite carry this without an adopter
receiving it.

**Promised outputs**
- tests/test_budget.py
- CLAUDE.md

## 3. Implement

**Decisions & assumptions**

- **D1 — the budget is enforced by a test in `tests/`** — 2026-08-10. Four candidates, judged against
  the two constraints `specify` set. **A `check` rule** was rejected first: `check` lives in
  `plugin/`, which is exactly what an install copies, so every adopter's tree would carry a rule
  comparing two files only this repository has — the criterion about not exporting this repository's
  tiering rules it out on its own. **An `after_write` hook** was rejected on two counts: taskmd runs
  it after *its own* write, which is `index`, so it would fire when tasks change and stay silent when
  `CLAUDE.md` changes — the wrong moment in both directions — and this repository has no
  `.taskmd/config.md` at all, so hanging a hook on one means writing a config, and a config
  *replaces* the shipped defaults rather than merging with them. That would pin this repository to a
  frozen copy of the schema for the sake of one command. **Nothing, with the consequence written
  down** was rejected because the tree turned out to be *over* the bound, so the honest version of
  that answer is a documented breach nobody is obliged to fix.
- **What the chosen answer does and does not buy** — 2026-08-10, recorded because the criterion says
  "reports a breach without being remembered" and this meets it only in part. There is **no CI here**
  and no `.github/` at all, so the test fires when somebody runs the suite. What changed is that the
  budget stopped being a single-purpose command with no other reason to run and became one assertion
  among 190 that a session already has a habit of running. That is a reduction, not an elimination,
  and pretending otherwise would make this task's own record the thing it was raised to fix. Raised
  as [T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md) rather than widened
  into here.
- **The unit is characters, and bash cannot express it** — 2026-08-10. Measured, not assumed: this
  machine's `wc` prints **3** for both `-c` and `-m` on a single em dash, so the documented one-liner
  could not have been repaired by switching flags. That is what forced the deliverable to be Python
  and is the reason the shape was fixed at `plan`.
- **The margin moved because the check moved, and that was not the point** — 2026-08-10. Step 4
  replaced a four-line fenced command with a one-clause pointer, which is 11 characters smaller, and
  those 11 characters are the whole difference between over-by-9 and under-by-2. **The reduction is a
  consequence of relocating the procedure, not a cut chosen to fit the number** — the out-line
  forbidding that cut was written before the figure was known, and nothing was removed for its size.
  A reader who suspects otherwise can check: the only text that left `CLAUDE.md` is the command that
  now lives in `tests/test_budget.py`.
- **9, not 10** — 2026-08-10. `specify` quotes the breach as 10 characters and the check reports 9.
  The difference is the newline the shell pipeline put after each description, which is an artefact of
  `sed` rather than part of the description; `measure()` counts the description's own characters and
  says so. The earlier figure is left as written — it was true of the pipeline it described.

**Verification**

The check was shown **failing on the real tree first**, before any edit that could have made it pass:

```
tier 1 7855 chars over by 9 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
AssertionError: 7855 not less than or equal to 7846
Ran 5 tests in 0.027s
FAILED (failures=1)
```

Its own four cases passed in that same run, which is what distinguishes a working check from a red
one: a tree pushed over is reported (`over by 20`), a tree under passes (`under by 20`), adding a
skill moves the figure by exactly the description's length with nothing else edited, and the
byte/character inversion is reproduced on a fixture — 105 against 100 in characters, 105 against 160
in bytes, the same tree passing or failing depending only on the unit.

After step 4 moved the command out of `CLAUDE.md`:

```
tier 1 7844 chars under by 2 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
Ran 5 tests in 0.023s
OK
```

Whole suite, per module — the four failures are `test_runtime.py`'s, already known to this tree and
untouched by this task:

```
test_budget.py     Ran 5 tests   OK
test_cli.py        Ran 84 tests  OK
test_list.py       Ran 29 tests  OK
test_runtime.py    Ran 27 tests  FAILED (failures=4)
test_schema.py     Ran 45 tests  OK
```

`taskmd check` exits 0 on 115 tasks and the index is regenerated.

**Outputs produced**
- [`tests/test_budget.py`](../tests/test_budget.py)
- [`CLAUDE.md`](../CLAUDE.md) — *Working method*, the command replaced by a pointer

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative | met | D1 carries three, each with the reason it lost: a `check` rule exports this repository's tiering to every adopter, an `after_write` hook fires on the wrong write *and* would force this repository to write a config that replaces the shipped schema, and nothing-with-it-written-down became dishonest the moment the tree turned out to be over |
| If something enforces it: a tier 1 deliberately pushed over the bound is reported, shown failing first | met | Twice over, and the stronger one was not planned: the check failed on the **real** tree — `7855 not less than or equal to 7846` — before any edit that could have made it pass, and `test_a_tier_1_over_the_bound_is_reported` does the deliberate version on a fixture. The criterion asked only for the second |
| If nothing does: `CLAUDE.md` says so where the command is | n/a | The branch was not taken. Recorded rather than ticked, because a criterion marked *met* on the branch that did not happen is how a review stops meaning anything |
| Whatever is decided does not make an adopter carry this repository's tiering | met | `tests/` is not inside `plugin/`, which T-053 made the plugin's boundary, and an install copies that subtree. Judged on the path and that decision, not on an install — this task installed nothing, and says so rather than implying a check it did not run |
| The check counts the unit `CLAUDE.md` states, and the same tree yields the same figure whatever shell it is run from | met | Characters, over UTF-8-decoded text, with `test_the_unit_is_characters_and_the_two_units_disagree` holding the two units apart on a fixture. Run from PowerShell and from Git Bash: **7844 both times**, which is the point — the previous command gave a different answer in the one shell it was written for. Windows only; no Linux is available here. The remaining cross-platform exposure would be line endings, and `git check-attr` reports `eol: lf` on both files, so a checkout cannot introduce the `\r` that would inflate the count |

**Child fix tasks raised**
- none. [T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md) was raised from
  `implement` as a discovery, not because a criterion failed — the criteria never asked *how often*
  the enforcement runs, and answering that inside this task would have been the widening METHOD §3.3
  forbids.

**One thing this review will not tick and will not bury.** The margin is now **two characters**. That
is smaller than the eight this task was raised about, and it is not a regression: the eight was
unwatched and the two is not, which was the entire outcome. But the next ordinary reconcile of
`CLAUDE.md` will turn the suite red, and *that is the mechanism working*, not a defect to be
pre-empted by trimming now. Whoever meets it decides what leaves, which is where T-028 and T-047 both
put that decision.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → in_progress → review → done | Four of five criteria met, the fifth recorded `n/a` because its branch was not taken. The result the task did not expect: **the tree was already in breach**, so the failing demonstration criterion 2 asks for arrived on the real repository rather than on a fixture, and arrived *before* any edit that could have hidden it. Moving the four-line command out of `CLAUDE.md` and leaving a pointer is 11 characters smaller, which is the whole distance between over-by-9 and under-by-2 — recorded as a consequence of relocating the procedure, not as the cut this task's out-line refuses, and checkable by anyone who looks at what actually left the file. The enforcement is honest about its own limit: there is no CI here, so it fires when somebody runs the suite, which converts *remember one command* into *run the 190 assertions you already run*. That gap is [T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md), which also carries an expired premise found on the way — T-011 and T-049 both declined a CI runner because **there is no git remote at all**, which stopped being true when this was published on 2026-08-09 and was never revisited, because a premise recorded inside a closing task goes stale in silence. Suite unchanged otherwise: 4 failures, all `test_runtime.py`'s, all pre-existing. |
| 2026-08-10 | → planned | Seven steps, and the ordering is doing one job: step 4 edits `CLAUDE.md`, which is one of the two things being measured, so the figure step 3 records and the figure step 5 records are different numbers about the same tree and both are true. Saying that at `plan` is what stops step 5 reading as a correction of step 3. Step 6 is the plan admitting it does not know its own result — moving a four-line shell command out of tier 1 might close a ten-character breach by itself, and if it does, the record has to say the reduction was a consequence of relocating the check rather than the cut this task refused to make. The deliverable shape is decided here rather than left to `implement` because it turns on a fact already measured: bash cannot count characters on this machine under either flag, so the only candidate that can state the unit is Python, and `tests/` is the only home for it that an install does not copy. |
| 2026-08-10 | → specified | **Whole-lifecycle authorisation, given by the maintainer in this session**: specify through to a push for this task, then each remaining open `M2` task the same way, one at a time, stopping to hand off before the context runs out — and nothing outside that set. Recorded here rather than relied on from the handoff that carried it, which METHOD §3.1 says is not a substitute. The phase's yield was not the answer it went looking for. The open question was answered *passing but unguarded*, and then the answer's own premise collapsed: the budget command is `wc -c`, which counts **bytes**, while the rule it implements says **characters** — a unit T-063 chose after measuring both, and then lost inside its own record, which carries 7,846 for `reference/TASK-WORKFLOW.md` in D1 and 7,919 for the same file under the same command in its closing log. Measured both ways before raising it: 7,911 against 7,919 is a pass by 8 in bytes; 7,856 against 7,846 is a **failure by 10** in characters. The sign flips because `—`, `§` and `→` cost three bytes and one character and the two documents use them at different densities, so the byte view flatters the denser one. Not a line-ending artefact — both files are LF-only, CR=0, checked rather than assumed. The maintainer chose characters over amending the rule to say bytes, so this task begins from a tree already in breach, which hands criterion 2 its failing demonstration on the real tree instead of a fabricated one. What it must not do is close that gap by cutting `CLAUDE.md`, now an explicit out-line. |
| 2026-08-10 | → proposed | Raised by T-047's review, which brought tier 1 under the bound by 8 characters and could not honestly call that guarded. `high` because the margin is smaller than one sentence and the thing that spends it is ordinary reconcile work, not an edit anyone would think to measure; `s` because the command already exists and only the question of who runs it is open. |
