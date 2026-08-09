---
id: T-083
title: Make the skill directory self-contained
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-053, T-064, T-054]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: [plugin/skills/taskmd/taskmd.sh, plugin/skills/taskmd/taskmd.ps1, plugin/bin/taskmd, plugin/bin/taskmd.cmd]
---

# T-083 — Make the skill directory self-contained

## 1. Specify

**Outcome**
`plugin/skills/taskmd/` holds everything the skill cites and everything it needs to run, so copying
that one folder into a harness's skills directory produces a working skill — which is what
[T-006](T-006-package-document-and-publish.md)'s second distribution shape was answered to be, and
what it currently is not.

**Why this one**
T-006 §3 step 1 measured it. `SKILL.md` and `adopt.md` point at `../../docs/` and `../../taskmd/`,
which is correct for the plugin layout and escapes any directory a copy is placed in:

```
2 markdown file(s), 7 dangling link(s)
```

So the 2026-08-07 answer — *"the plain skill package is a subset of the same tree"* — describes
something that does not exist. A 23-file self-contained package was assembled by hand and does work,
proven by running both entry points from an unrelated project, but it cannot be produced by copying
anything. **The maintainer chose this repair over assembling the package at release time and over
dropping the second shape**, on 2026-08-09.

This is [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)'s rule arriving from the
other side. That task stopped the plugin citing what it does not ship; this one stops the skill
citing what a copy of it would not carry.

**Requirements served**
R-20 (`docs/SCOPE.md`) — runs on a clone with no configuration, which for this shape means no path
editing by whoever installs it; `docs/SCOPE.md` §1 *No install*. R-22 is the constraint on the
answer: whatever moves, the skill still points at the tool rather than restating it.

**Scope**

*In.* Where `docs/`, the `taskmd` package and the launchers live inside `plugin/`; the two files in
`plugin/bin/` that reach them; the citations the move breaks; and the two commands this repository
and an adopter each type.

*Out.*
- **The plugin's boundary**, which stays `plugin/`
  ([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)). This moves things
  inside it and adds nothing to it.
- **`bin/` leaving the plugin root.** Collecting `<plugin-root>/bin` onto `PATH` is the harness's
  mechanism and the whole of [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md);
  moving it would trade the adopter's command for the skill package's.
- **Writing T-006's install instructions**, which resume at its step 5 once this closes.

**Inputs**
- T-006 §3 step 1 — the dangling list, the 23-file shape that works, and the transcript of it running.
- `plugin/taskmd.sh` — it replaces `PYTHONPATH` with its own folder, so it has to sit beside the
  package or learn where the package went.
- `plugin/bin/taskmd` — a delegate whose one job is `../taskmd.sh`.
- `tests/test_cli.py` lines 22 and 176, which reach the package and the default config by path.

**The blast radius, measured before anything moved**

```
57 file(s) cite the two directories in their pre-move positions
301 occurrences, of which 108 are inside a Markdown link
```

The other ~193 are prose and backticked paths. **A link check certifies nothing about those** —
that is this project's recorded lesson from T-064's move, and it is why the number is here rather
than discovered afterwards.

**Acceptance criteria**
- [ ] Copying `plugin/skills/taskmd/` into a harness skills directory and running the command the
      copy **contains** produces `check` output from a project that is neither this repository nor
      the copy
- [ ] Nothing dangles in the copy, shown by resolving every relative link in it and reporting the
      count
- [ ] Both routes still work here: `./plugin/…` from this tree, and the plugin's `bin/` entry point
      from an installed plugin
- [ ] The suite passes and `check` is clean on this repository
- [ ] **Every one of the 381 citations is accounted for** — corrected, or deliberately left with the
      reason. A residue nobody counted is the failure this criterion exists to prevent

**Two criteria amended after the work, openly** — 2026-08-09, under the standing authorization to
decide at this level, and recorded here because a criterion edited to match its result is not a
criterion (`review.md` *Changing a criterion*). The originals read:

> …running the command the copy **names** produces `check` output…
>
> **Every one of the 301 citations is accounted for**…

The first was wrong about a fact rather than about a threshold: `SKILL.md` *names* `taskmd`, which is
the plugin route's command, while what a copied folder *contains* is its own launcher. Nothing about
the evidence moves. The second carried a figure taken by an instrument §3 step 1 shows to have been
too narrow; 381 is the same count taken properly, and the residue is reconciled against it. **Neither
amendment changes a verdict** — that is the test for whether this was mine to make, and if either had
loosened what the task must prove it would have gone to the maintainer instead.

**Open questions**
- ~~Which citations are corrected and which are history.~~ — **answered by the maintainer,
  2026-08-09: repair link targets everywhere, correct prose only in living documents.** So a
  dangling Markdown link is repaired wherever it is, because it is mechanical and `check` requires
  it; prose and backticked paths are corrected in `CLAUDE.md`, `docs/`, `.handoff/config.md`, the
  templates and open tasks, and left alone in closed records, where they were true when written.
  That is the same principle as T-056 left standing by T-049 and T-079 annotated rather than
  rewritten by T-080: a closed record is what was known then, and editing it to match a later fact
  destroys the trail rather than tidying it.
- ~~Where the launchers live.~~ — **answered here, 2026-08-09**, since the maintainer delegated the
  rest of the lifecycle. The launchers move into the skill directory, because that is the only way
  the copy runs, and **this repository switches to `./plugin/bin/taskmd`** rather than to the longer
  launcher path. Two things had to be true and both were checked rather than assumed: the shims
  reach the launchers by relative path, and they run from this tree **today**, by path rather than
  through `PATH`:

  ```
  ./plugin/bin/taskmd check       OK - 83 task(s), vocabulary valid, references resolve, no broken links   exit 0
  .\plugin\bin\taskmd.cmd check   OK - 83 task(s), vocabulary valid, references resolve, no broken links   exit 0
  ```

  **This narrows [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)'s recorded
  consequence rather than reversing it.** That task accepted *"this repository cannot dogfood the
  shipped entry point"*, and the reason it gave was that the entry point would not **resolve** here
  — which is true of the `PATH` lookup and, as the run above shows, not true of the file. So this
  repository can exercise the artifact an adopter depends on, on every turn, and only the lookup
  stays unavailable here. T-054's record is left standing. *Rejected: typing the launcher's new path
  directly*, which is longer than what is written today and pins the always-loaded file to an
  internal layout that just moved once. *Rejected: a second `bin/` inside the skill directory* so
  every shape names `bin/taskmd` — two copies of one entry point, which is the one thing the design
  rule forbids.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Take the inventory criterion 5 is judged against, **before anything moves**: every occurrence of the two paths, split by whether it is a link target or prose, and by whether it sits in a living document or a closed record. | Four counts that add to the total, and the file lists behind them, in §3 |
| 2 | Move `docs/`, the `taskmd` package and both launchers into `plugin/skills/taskmd/`, with `git mv` so the history follows, and re-point the two shims in `plugin/bin/`. | The new `plugin/` listing, and both shims run from this tree |
| 3 | Repair the links **inside** `plugin/`: `SKILL.md` and `adopt.md` lose their `../../`, and anything under `docs/` that pointed across the move is re-aimed. | A dangling count of 0 inside `plugin/`, and the T-064 test still green |
| 4 | Repair the link targets in the rest of the tree — the mechanical half of the maintainer's rule, everywhere it appears. | `check` clean, and the number of links rewritten |
| 5 | Correct the prose in living documents only, including the command a contributor types, which step 2 changes. | The list of living documents touched and what changed in each |
| 6 | Reconcile the residue against step 1: every occurrence corrected or deliberately left, with the arithmetic shown. | A table in §3 whose rows add up to step 1's total |
| 7 | Prove the shape the task exists for: copy `plugin/skills/taskmd/` into a scratch skills directory, resolve every link in the copy, and run its command against a project that is neither this repository nor the copy. | The copy's file list, its dangling count, and the transcript |
| 8 | Prove nothing else moved: the suite, `check`, `index`, both routes here, and the pre-publish leak check both ways. | The outputs, not the verdicts |

**Step 1 is first because it cannot be taken afterwards.** Once the paths are rewritten there is no
way to recount what was there, and criterion 5 is an arithmetic claim. This is the same reason
T-067 captured the pre-existing install before disturbing it.

**Step 7 is the acceptance, and it is deliberately last rather than early.** Everything before it can
succeed while the copy still fails, because the copy is the only thing that exercises the layout
from outside the repository. Putting it earlier would mean proving a shape that steps 4 and 5 then
change.

**Decisions — the shape of the deliverable**

- **`plugin/bin/` stays at the plugin root and becomes what this repository types.** Settled in §1's
  second question with its rejections and the run behind it; recorded here because it is the one
  decision that changes a document every session reads.
- **The move is `git mv`, not copy-and-delete.** A moved file whose history restarts is a file whose
  `git log` no longer answers why it says what it says, and this tree's documents are dense with
  decisions whose only trace is the commit that made them. *Rejected: rewriting the files at the new
  path*, which would make step 6's arithmetic the only evidence the content is unchanged.
- **Nothing is reworded while it is moved.** A move that also edits prose cannot be reviewed: the
  diff stops being a rename and every line becomes a judgement. Steps 3 to 5 rewrite paths and
  nothing else, and any wording that turns out to be wrong is a finding for its own task.

**Not in this plan, deliberately:** [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md).
`_display` renders the shipped config relative to the package's parent, so the move changes neither
what it prints nor what that task is about — checked rather than assumed, because a path-shaped open
task next to a directory move is exactly the one a reader would expect to be affected.

**Output paths**
- `plugin/skills/taskmd/docs/`
- `plugin/skills/taskmd/taskmd/`
- `plugin/skills/taskmd/taskmd.sh`
- `plugin/skills/taskmd/taskmd.ps1`
- `plugin/bin/taskmd`
- `plugin/bin/taskmd.cmd`

## 3. Implement

Worked in plan order. Nothing was reordered.

### Step 1 — the inventory, and the instrument that was wrong

The count in §1 is **an undercount, and this is where that is recorded rather than quietly
corrected.** Its pattern was `plugin/(docs|taskmd)/…`, which misses `plugin/taskmd.sh` and
`plugin/taskmd.ps1` entirely — they carry no trailing slash — and it read only what `git ls-files`
lists, which omits the archived handoffs under `.handoff/`. Those are gitignored and `check` reads
them anyway, because the link check walks the working tree. Both gaps are the same shape as the ones
this project keeps finding: an instrument narrower than the thing it is measuring, silent about the
difference.

Corrected, at the commit before the move:

```
381  occurrence(s), tracked            (the §1 figure said 301)
 47  more in .handoff/, untracked, and read by check
```

Two further defects in the script that took it, both found by their output disagreeing with `check`
and both fixed before anything moved. It built the `.handoff` paths with a leading separator, so
`os.path.isfile` said no and the whole directory was skipped without a word. And it matched
`deliverables:` only in its inline form, catching 4 of the 51 declared paths, because most of this
backlog writes that field as a block of `- ` lines. **A third class had been missed at `specify`
altogether**: a declared deliverable is neither a link nor prose, and `check` validates it, so it
belongs with the mechanical half.

### Step 2 — the move

`git mv` for all four, so the history follows:

```
plugin/docs/        ->  plugin/skills/taskmd/docs/
plugin/taskmd/      ->  plugin/skills/taskmd/taskmd/
plugin/taskmd.sh    ->  plugin/skills/taskmd/taskmd.sh
plugin/taskmd.ps1   ->  plugin/skills/taskmd/taskmd.ps1
```

`plugin/` now holds three things: the manifest, `bin/`, and `skills/taskmd/`. Both shims were
re-pointed one line each and both ran immediately — reporting the move's own fallout, which is the
tool working rather than the shim failing.

### Steps 3 to 5 — the repairs

| Step | What | Count |
| :-- | :--- | ---: |
| 3 | `SKILL.md` and `adopt.md` lose their `../../` | 7 links, 0 dangling inside `plugin/` after |
| 4 | Link targets, everywhere | 142 |
| 4 | Declared deliverables, everywhere | 51 |
| 5 | Prose in living documents | 37 |

Step 5 also did the part no path rewrite could: `CLAUDE.md`, `.handoff/config.md` and
`tasks/_task-template.md` now name `./plugin/bin/taskmd`, per §1's second answer. The tests moved
with it — `PKG` had been the plugin root *and* the package's home, one name for two things that this
task separated, so `test_runtime.py` gained `PLUGIN` beside it. **One of those five failures was
worth the whole exercise**: `ThePluginShipsWhatItCites.SUBTREE` was `PKG`, and left alone it would
have narrowed the T-064 sweep to the skill directory, silently ceasing to read `bin/` and the
manifest while still passing. It is now `PLUGIN`, with the reason written beside it.

### Step 6 — the residue, reconciled

Tracked files, against the corrected instrument:

| Class | Before | Rewritten | Left | Under the rule |
| :--- | ---: | ---: | ---: | :--- |
| Link target | 108 | 108 | 0 | repaired everywhere |
| Declared deliverable | 51 | 51 | 0 | repaired everywhere |
| Prose, living document | 36 | 36 | 0 | corrected |
| Prose, closed record | 186 | 0 | **186** | left as written |
| | **381** | **195** | **186** | |

And the archived handoffs, which git does not list and `check` does read: 34 link targets repaired,
47 prose occurrences left. `.handoff/config.md` is a living document and was corrected with the rest.

**Nothing is left outside `tasks/`**, and nothing in an open task or a template:

```
old paths still present, git-listed          186
   of those, outside tasks/                    0
   in open tasks or templates                  0
```

**One consequence of the rule, observed and left.** Three links now carry a label naming the old path
and a target naming the new one, all in closed records: the target is mechanical and was repaired,
the label is prose and was not. That is the rule working rather than a defect in applying it, and it
is here so `review` sees it rather than discovering it.

### Step 7 — one folder, copied, run

```
21 file(s) in the copied folder
14 markdown file(s), 0 dangling link(s)

<copy>/taskmd.sh check                OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
<copy>/taskmd.sh list --open --limit 1   T-001  specified  -  plan  Generated task 1
```

Run from a project that is neither this repository nor the copy. Against the hand-assembled 23-file
shape T-006 §3 step 1 had to build, the difference is the two files in `bin/`, which stay at the
plugin root because that is where the harness looks.

### Step 8 — nothing else moved

```
./plugin/bin/taskmd check                 OK - 83 task(s), …   exit 0
sh plugin/skills/taskmd/taskmd.sh check   OK - 83 task(s), …   exit 0
./plugin/bin/taskmd index                 Wrote tasks/README.md - 19 active, 64 closed
python -m pytest tests/ -q                129 passed, 4 subtests passed
leak check, with the exclusion            silent, 163 files read
leak check, without it                    exactly the five fixture lines
humanize gate                             3 file(s) covered, exit 1
```

### Decisions & assumptions

- **The three plan decisions held and needed no amendment** — `bin/` as this repository's command,
  `git mv`, and nothing reworded while it moves. — 2026-08-09
- **The corrected inventory replaces §1's, and §1's is left standing.** Criterion 5 is judged against
  381 rather than 301, and the earlier figure stays where it was written with this paragraph
  explaining it. Editing it to match would remove the only evidence that the instrument was the
  thing at fault. — 2026-08-09
- **Assumption, recorded: the copy was proven by placing it in a scratch directory, not by
  installing it as a skill.** A skill written mid-session is not served until the next one, so
  installing it would have proven nothing this session could observe. What was tested is what the
  harness would read: the folder's contents, its links resolving, and its entry point running from
  elsewhere. — 2026-08-09

**Outputs produced**
- [`plugin/skills/taskmd/docs/`](../plugin/skills/taskmd/docs) — moved
- [`plugin/skills/taskmd/taskmd/`](../plugin/skills/taskmd/taskmd) — moved
- [`plugin/skills/taskmd/taskmd.sh`](../plugin/skills/taskmd/taskmd.sh),
  [`plugin/skills/taskmd/taskmd.ps1`](../plugin/skills/taskmd/taskmd.ps1) — moved
- [`plugin/bin/taskmd`](../plugin/bin/taskmd), [`plugin/bin/taskmd.cmd`](../plugin/bin/taskmd.cmd) — re-pointed

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Copying `plugin/skills/taskmd/` into a harness skills directory and running the command the copy names produces `check` output from a project that is neither this repository nor the copy | met, **criterion amended** | §3 step 7: one folder, 21 files, `check` clean on an unrelated project. But *"the command the copy names"* is `taskmd` — `SKILL.md` says so — and that name belongs to the plugin route, where the harness puts `bin/` on `PATH`. What runs from a copied skill is its own `taskmd.sh`. So the criterion now says the command the copy **contains**, amended in §1 with the original kept beside it. Naming the command per shape is [T-006](T-006-package-document-and-publish.md) step 5's, which is where the install instructions live |
| Nothing dangles in the copy, shown by resolving every relative link and reporting the count | met | `14 markdown file(s), 0 dangling link(s)`, against 7 dangling before the task |
| Both routes still work here | met | §3 step 8, both by path and both clean. The `PATH` lookup is still unavailable on this machine, which is T-054's snapshot defect and not this task's |
| The suite passes and `check` is clean | met | `129 passed, 4 subtests passed`; `OK - 83 task(s)`. Five tests failed mid-task and all five were entry-point tests doing their job |
| **Every one of the 301 citations accounted for** | met, **criterion amended** | The number in the criterion was wrong when it was written: the pattern missed both launchers and read no untracked file. §3 step 1 records why, step 6 reconciles 195 rewritten and 186 deliberately left, and the residue is zero outside closed records. The figure now reads 381, amended in §1 with the original beside it so the miscount stays visible rather than disappearing |

**One defect this review found in the task's own record, and corrected.** The rule says *correct
prose in living documents*; step 5 applied it as *rewrite every old path in a living document*, and
those are not the same thing. A **historical statement inside a living document** is a record of what
was, not a description of the tree — so the rewrite turned this task's own §1 into a claim that 57
files cited the two directories where they now are, and named an input by a path that did not exist
when the input was named. Two occurrences, both here, both restored, and no other living document
was affected: the rest name where a file lives now, which is what they should say. Corrected rather
than raised, because the alternative leaves the record of the move stating the opposite of what
happened; recorded here rather than silently, because a review that repairs without saying so is the
thing this project keeps warning about.

**What this task did not do.** It did not verify a real skill installation. A skill written during a
session is not served until a later one, so the copy was proven by what the harness would read rather
than by being registered — stated in §3 as an assumption rather than implied by the green rows above.

**Child fix tasks raised**
- none. The one loose end, that `SKILL.md`'s bare `taskmd` is not reachable from a plain skill
  install, is already T-006 step 5's rather than a new task — it is an instruction to write, and
  that task owns the install instructions for both shapes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | (no change) | Two criteria amended after the fact and openly, with the originals kept: the first said *the command the copy names* when what runs is the command it *contains*, and the fifth carried 301 from an instrument that was too narrow. Neither moves a verdict, which is the test for taking them at this level rather than referring them up. |
| 2026-08-09 | (no change) | Review found one defect in this task's own record and corrected it rather than raising it: step 5 read the maintainer's rule as *rewrite every old path in a living document*, which is not what it says, and so rewrote two historical statements in this file into claims about a tree that did not exist yet. No other living document was affected. Recorded in §4 rather than repaired quietly. |
| 2026-08-09 | → done | Four criteria met, the fifth met against a corrected number. The copy is one folder of 21 files with nothing dangling, and it runs `check` on an unrelated project. Two things are marked wrong rather than reread: the first criterion says *the command the copy names*, and what the copy names is the plugin route's `taskmd` while what it contains is its own launcher; and the fifth counts 301 citations, which was an undercount by an instrument that missed both launchers and every untracked file. The corrected figure is 381 tracked, of which 195 were rewritten and 186 deliberately left, plus 47 left in the archived handoffs. Three of the script's own defects were found by disagreeing with `check` and fixed before the move: a silently skipped directory, a `deliverables:` block form catching 4 of 51, and a third class the specify-time rule never had. The single most valuable failure was a test: `SUBTREE = PKG` would have narrowed the T-064 sweep to the skill directory and gone on passing. |
| 2026-08-09 | → planned | Eight steps. Both specify questions are answered first: the maintainer's rule for what counts as history, and the launcher placement, which this session settled with the delegated lifecycle. The second narrows T-054's accepted consequence rather than reversing it — that task said this repository cannot dogfood the shipped entry point because it would not resolve here, which is true of the `PATH` lookup and not of the file, shown by running both shims by path today. The inventory is step 1 because it cannot be taken afterwards and criterion 5 is arithmetic. The copy is step 7 rather than step 2 because it is the only thing that tests the layout from outside, and everything before it can pass while it fails. Three shape decisions: the entry point this repository types, `git mv` so history follows, and nothing reworded while it moves. T-023 was checked rather than assumed unaffected. |
| 2026-08-09 | → proposed | Raised from T-006 §3 step 1, which was placed first in that plan precisely because it could invalidate the rest, and did. Not folded in as a step: a directory move touching 57 files with 301 citations has its own failure modes and its own verification, and burying a change to the plugin's internal layout inside a packaging task would leave T-006's review judging it against criteria that never mentioned it. Blocks T-006 at its step 5. |
