---
id: T-064
title: Stop the plugin citing documents it does not ship
type: fix
status: specified
phase: specify
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
| 2026-08-09 | → specified | Answered: (a), drop the citation and keep the sentence, applied to all 19 with **no exception for code comments** — the exception is defensible and costs a rule someone has to remember, which §1 *Invisibility* rejects. Recorded as an application of T-053's own precedent rather than a new decision: `adopt.md` hit this once and was rewritten to state the measurement instead of citing R-21. The task is cheaper than its count implies, because most of these sentences already state the property and the number is a prefix — which is worth knowing at `plan`, since it changes the work from nineteen rewrites to a sweep plus a handful. What is lost is written down rather than glossed: the trace from code back to requirement, which survives in the task records and `git log -S` and is a worse index than a footnote. Criterion 3 was a fork and is now a plain requirement; kept as written, so `review` can record which branch applied. |
| 2026-08-09 | → proposed | Raised as F-1 from the T-059 audit, clauses 1 and 3. Counted before write-up: 29 references escape the subtree, one of them broken inside this repository as well. `high` because it costs a release if it survives into T-006 and because the worst carrier is the file every adopter is told to copy; `m` rather than `s` because the 19 requirement citations need one decision applied consistently, not a search and replace. T-053's closure criterion was honest and swept links; every escape here is prose, which is the class it could not see. |
