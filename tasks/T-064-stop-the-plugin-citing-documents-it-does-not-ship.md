---
id: T-064
title: Stop the plugin citing documents it does not ship
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-053, T-006]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-064 — Stop the plugin citing documents it does not ship

## 1. Specify

**Outcome**
Nothing inside `plugin/` refers a reader to a file the plugin does not contain — and the check that
establishes it reads **references**, not only Markdown links.

**Why this one**
Raised as **F-1** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clauses 1 and 3. Counted across the subtree:

| Kind of citation | Count | Where |
| :--- | ---: | :--- |
| `R-NN` requirement citations | 19 | `docs/BINDING.md`, `taskmd/{cli,schema,discovery}.py` |
| `docs/SCOPE.md` | 5 | `taskmd/{cli,discovery}.py`, `taskmd/defaults/config.md` |
| a numbered non-goal | 4 | `taskmd/cli.py`, `taskmd/defaults/config.md` |
| `../CLAUDE.md` | 1 | `docs/BINDING.md` |

`docs/SCOPE.md` and `CLAUDE.md` are this repository's own papers and were deliberately left outside
the plugin by [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md). An adopter
receives none of them, so nineteen requirement numbers and ten path references resolve to nothing.

**One of them is broken inside this repository too.** `plugin/docs/BINDING.md:193` cites
`../CLAUDE.md`, which from `plugin/docs/` resolves to `plugin/CLAUDE.md` — a file that has never
existed. Before the restructure that path was correct; the move made it wrong and nothing noticed.

**The worst carrier is the file adopters are told to copy.**
[`adopt.md`](../plugin/skills/taskmd/adopt.md) step 2 instructs every adopting project to copy
`plugin/taskmd/defaults/config.md` into its own `.taskmd/config.md` and edit it. That file holds five
of the dangling citations, so adoption propagates them into each new project.

**Why T-053's closure criterion did not catch it, and was not wrong.** Its replacement criterion reads
*"No pointer inside the plugin resolves outside it — demonstrated by sweeping `plugin/` for links that
escape the subtree."* The sweep was honest and returned none. Every escape above is **backticked
prose or a code comment**, which is the class a link sweep cannot see — the generalisable half of this
finding, and the reason criterion 3 below is about references rather than a one-time cleanup.

**Requirements served**
R-13 (`docs/SCOPE.md`) — a binding states its premises so an adopter can check them, which a citation
they cannot resolve defeats; R-22, R-23; and `CLAUDE.md` *Out-of-the-box*.

**Scope**
- In: every reference from inside `plugin/` to a path or a document outside it.
- In: the 19 `R-NN` citations. They are not paths, and the question of what a shipped document may
  cite is the substantive part of this task rather than a search-and-replace.
- In: a repeatable check, so the next move is caught by something other than an audit.
- Out: the *content* of any argument that currently cites a requirement. Where a citation carries real
  reasoning, this task decides how it is referred to, not whether the reasoning is right.
- Out: what the plugin ships, settled in T-053 and not reopened.
- Out: `docs/SCOPE.md` and `CLAUDE.md` themselves, which are free to cite anything.

**Inputs**
`plugin/docs/BINDING.md`, `plugin/taskmd/defaults/config.md`, `plugin/taskmd/{cli,schema,discovery}.py`,
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) §4 for the criterion as
reworded, [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-1.

**Acceptance criteria**
- [ ] No file under `plugin/` refers a reader to a path outside it; demonstrated by a sweep over
      **references**, not links
- [ ] `plugin/docs/BINDING.md`'s `../CLAUDE.md` resolves, or is gone
- [ ] Every `R-NN` citation inside `plugin/` either resolves for an adopter or has been replaced by
      the statement it was standing in for — decided once and applied consistently, not case by case
- [ ] The sweep is written down where the next restructure will meet it, and is shown catching a
      deliberately reintroduced escape, per R-16
- [ ] `taskmd/defaults/config.md` is checked as the copied artifact it is: a project that copies it
      gets a file with no dangling reference
- [ ] Nothing in the tracked tree outside `plugin/` is changed

**Open questions**
- ~~**What replaces a requirement citation in a shipped document?**~~ **Answered by the maintainer on
  2026-08-09: (a) — drop the citation and keep the sentence.**

  **One rule, no exception for code.** A "code comments may cite, prose may not" split was available
  and was **not** taken: contributors have the whole repository and adopters do not, so the exception
  is defensible on its merits and costs something worse — a rule someone has to remember, which
  `docs/SCOPE.md` §1 *Invisibility* is exactly the property that rejects. So all 19 citations, in
  documents and in docstrings alike, get the same treatment.

  **The work is smaller than the count suggests, and that is why (a) is cheap.** Most of these
  sentences already carry themselves and the number is decoration —
  `plugin/taskmd/cli.py`'s `load()` reads *"R-17: a configuration problem is reported here, when the
  config is read, and the command never starts"*, which states the property in full. Deleting the
  prefix loses nothing. Only where a sentence genuinely leans on the number does anything have to be
  written, and then it is rewritten to state the thing rather than to cite it.

  **This applies a decision already taken rather than making a new one.** T-053 §3 step 4 hit exactly
  this case once, in `adopt.md`, and resolved it the same way: *"the sentence was rewritten to state
  the measurement instead of citing R-21."* That is the precedent, it is in-tree, and it is what makes
  this a consistent application rather than a fresh judgement call.

  *Rejected: (b), stating the requirement inline where it is cited.* It resolves for an adopter and
  buys that by giving a requirement a second home in a shipped file — the one thing this plugin
  exists to prevent, traded away for a footnote.

  *Rejected: (c), shipping a short requirements document inside `plugin/`.* It reverses part of
  T-053's boundary and hands an adopter the requirements list for a tool they are merely using, which
  is the exact reason `SCOPE.md` and `BRIEF.md` were left at the repository root.

  **What is lost, stated rather than waved past:** the trace from a line of code back to the
  requirement that shaped it. It survives where
  [`METHOD.md`](../plugin/docs/METHOD.md) §6 says rationale belongs anyway — the task records — and
  is recoverable with `git log -S` on the removed citation. That is a worse index than a footnote and
  it is the price of the boundary being real.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-count the escapes against the tree rather than against the audit's table, since the audit is two days and four tasks old | The current list, per file and line |
| 2 | Rewrite them file by file, reading each sentence's context — the decision says *keep the sentence*, so a blanket deletion is not the work | `BINDING.md`, then the three modules, then the copied config |
| 3 | Build the sweep as a **test**, so the next restructure meets it without anyone remembering to run it — and sweep references, not links, since links are the class the last boundary criterion could already see | `tests/test_runtime.py` |
| 4 | Show the sweep failing on a deliberately reintroduced escape of **each** kind — a code comment and a document | The transcript |
| 5 | Check `taskmd/defaults/config.md` as the artifact adopters copy: copy it into a fresh project and run against it | The adopting-project transcript |
| 6 | Full suite under both runners, and all four commands, since every edit was inside a docstring or a comment and a broken one is a syntax error | The transcripts |

**Why step 1 re-counts.** The audit's table says 19 requirement citations. Four tasks have landed
since, and two of them — [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) and
[T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) — added `R-17` comments to the very files
this task cleans, plus [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) added an
`R-20` to `taskmd.ps1`. Working from the audit's number would have left three behind, which is a
tidy illustration of why step 3 has to be a test rather than a cleanup.

**Why the sweep is a test and not a paragraph in the always-loaded conventions.** Tier 1 is over its
bound ([T-063](T-063-measure-the-tier-1-member-the-rule-declares.md), measured this session), and a
check that only fires when someone remembers it is the property the last sweep already had.

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the count was 21 and 16, not 19 and 10** — 2026-08-09. Re-swept before editing: **21**
  `R-NN` citations rather than the audit's 19, because three arrived during this session's own
  earlier tasks. `plugin/taskmd.ps1` was not in the audit's list at all. Every one is fixed; none
  was carried on the strength of a two-day-old count.

- **D2 — most sentences lost a prefix; five were rewritten** — 2026-08-09. The maintainer's answer
  predicted this and it held. `cli.load()`'s *"R-17: a configuration problem is reported here…"*
  drops four characters and states the property in full. Five leaned on the number and were
  rewritten to say the thing: `_resolve_hook`'s *"so R-17 is structural rather than remembered"* →
  *"so reporting it early is structural rather than remembered"*; `_display`'s *"which R-20 forbids
  and the pre-publish check in `CLAUDE.md` is aimed at"* → *"which no output of this tool may do, on
  any path"*; and three in `discovery.py` and `config.md` where a non-goal number was carrying the
  argument.

- **D3 — the sweep reads references and lives in the suite** — 2026-08-09. Two tests, kept
  together on purpose: one for **references** (the class that escaped), one for **relative paths
  that climb out** (the class T-053 already swept). Keeping both stops the two halves drifting
  apart, which is how this finding was born — a criterion that swept one half honestly and read as
  though it covered both.

- **Assumption, recorded:** that `R-\d+`, `non-goal`, and the three paper names are the whole of what
  escapes. It is a denylist, so a *new* kind of escape — a fifth document at the repository root —
  would pass it. The relative-path half is a genuine allowlist and has no such hole; the reference
  half cannot be one, because prose can name anything.

### Steps 3–4 — the sweep, shown catching what it is for

Two escapes reintroduced, one of each kind: an `R-99` comment in `cli.py` and a `` `docs/SCOPE.md` ``
in `BINDING.md`.

```
AssertionError: Lists differ: [] != ["plugin/docs/BINDING.md:8 cites 'SCOPE.md'",
                                     "plugin/taskmd/cli.py:44 cites 'R-99'"]
```

Both caught, including the code comment — which is precisely what T-053's link sweep could not see
and what made this finding invisible for a restructure. Files restored, sweep green.

### Step 5 — the file adopters are told to copy

`plugin/taskmd/defaults/config.md` holds three references after the rewrite, and all three are
things an adopter has: `.taskmd/config.md` twice — their own file — and `taskmd/schema.py`, which
ships. Copied into a fresh project with nothing else in it:

```
cp plugin/taskmd/defaults/config.md <a fresh project>/.taskmd/config.md
taskmd check --root <a fresh project>
OK - 0 task(s), vocabulary valid, references resolve, no broken links     exit 0
```

No dangling reference in the copied file. Adoption no longer propagates five of them.

### Step 6 — validation

```
python -m pytest tests -q             124 passed in 3.81s
python -m unittest discover -s tests  Ran 124 tests ... OK
taskmd check                          OK - 76 task(s), ...
taskmd index                          Wrote tasks/README.md - 32 active, 44 closed
taskmd list --open --limit 3          T-006 / T-025 / T-029
taskmd context T-064                  renders
```

**Outputs produced**
- `plugin/docs/BINDING.md` — 7 rewrites, including the `../CLAUDE.md` that was broken in this
  repository too
- `plugin/taskmd/{cli,discovery,schema}.py` — 22 rewrites
- `plugin/taskmd/defaults/config.md` — 3 rewrites, the copied artifact
- `plugin/taskmd.ps1` — 1, which this session had added an hour earlier
- `tests/test_runtime.py` — `ThePluginShipsWhatItCites`, two tests

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| No file under `plugin/` refers a reader to a path outside it; demonstrated by a sweep over **references**, not links | met | Both tests green over the whole subtree; the reference half is what the boundary never had |
| `plugin/docs/BINDING.md`'s `../CLAUDE.md` resolves, or is gone | met | Gone. The sentence it ended — *"worth what your confidence in it is worth, and no more"* — was already complete without it |
| Every `R-NN` citation inside `plugin/` either resolves for an adopter or has been replaced by the statement it was standing in for — decided once and applied consistently | met | All 21, documents and docstrings alike, on the maintainer's one rule. Five needed a rewritten sentence rather than a deleted prefix; those are D2 |
| The sweep is written down where the next restructure will meet it, and is shown catching a deliberately reintroduced escape, per R-16 | met | §3 step 4, one escape of each kind. It is a test, so "will meet it" needs nobody to remember |
| `taskmd/defaults/config.md` is checked as the copied artifact it is | met | §3 step 5 — copied into a fresh project, `check` clean, no dangling reference in the copy |
| Nothing in the tracked tree outside `plugin/` is changed | **not met, deliberately** | `tests/test_runtime.py` changed. Criterion 4 cannot be satisfied without it: the sweep's subject is the subtree, so it must not live *in* the subtree and ship to every adopter. The two criteria are inconsistent as written and this is the one that gave. Original kept above rather than edited to match, per [`review.md`](../plugin/docs/method/review.md) *Changing a criterion*. Nothing else outside `plugin/` was touched by this task |

**Child fix tasks raised**
- none. The one unmet criterion is a conflict between two criteria rather than a gap in the work —
  there is nothing for a child task to do, and saying so is more honest than raising one to close a
  row. The assumption in D3 (a denylist cannot see a *new* kind of escape) is recorded there rather
  than raised, because a task for it would have no trigger until a fifth root document exists.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Five criteria met, one **not met deliberately** and recorded as such rather than re-read: criterion 6 (nothing outside `plugin/` changes) is inconsistent with criterion 4 (a sweep the next restructure meets), because a sweep whose subject is the subtree must not live in it and ship to every adopter. The re-count is the part worth carrying: the audit said 19 requirement citations and the tree said **21**, because three arrived from this session's own earlier tasks — T-062 and T-075 put `R-17` into the very files this cleans, and T-061 put `R-20` into `taskmd.ps1`, which the audit never listed. Working from the recorded number would have left three behind, which is the argument for step 3 being a test in one line. The sweep reads references and paths as two tests kept together, since drift between those two halves is how this finding was born. |
| 2026-08-09 | → in_progress | Plan re-counts before rewriting, and makes the sweep a test rather than a paragraph in the always-loaded conventions — tier 1 is over its bound as of T-063, and a check that fires only when someone remembers it is the property the last sweep already had. |
| 2026-08-09 | → specified | Answered: (a), drop the citation and keep the sentence, applied to all 19 with **no exception for code comments** — the exception is defensible and costs a rule someone has to remember, which §1 *Invisibility* rejects. Recorded as an application of T-053's own precedent rather than a new decision: `adopt.md` hit this once and was rewritten to state the measurement instead of citing R-21. The task is cheaper than its count implies, because most of these sentences already state the property and the number is a prefix — which is worth knowing at `plan`, since it changes the work from nineteen rewrites to a sweep plus a handful. What is lost is written down rather than glossed: the trace from code back to requirement, which survives in the task records and `git log -S` and is a worse index than a footnote. Criterion 3 was a fork and is now a plain requirement; kept as written, so `review` can record which branch applied. |
| 2026-08-09 | → proposed | Raised as F-1 from the T-059 audit, clauses 1 and 3. Counted before write-up: 29 references escape the subtree, one of them broken inside this repository as well. `high` because it costs a release if it survives into T-006 and because the worst carrier is the file every adopter is told to copy; `m` rather than `s` because the 19 requirement citations need one decision applied consistently, not a search and replace. T-053's closure criterion was honest and swept links; every escape here is prose, which is the class it could not see. |
