---
id: T-085
title: Install the published plugin on a machine that has never seen it
type: analysis
status: done
phase: review
parent: T-006
blocked_by: [T-129]
related: [T-049, T-054, T-067, T-020, T-129]
work_package: M5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-16
adopter_visible: no
deliverables: []
---

# T-085 — Install the published plugin on a machine that has never seen it

## 1. Specify

**This is M5's last task, and it runs after the release.** The maintainer's instruction of
2026-08-11: install what M5 actually shipped, not whatever version happened to be current when
someone reached this task. The `blocked_by` edge to
[T-129](T-129-release-v0-5.md) carries it, so no view can miss it. **The consequence is that M5 is
not complete when it is tagged** — it is complete when the published artifact has been proven from
outside, which is a change from `M2`, where the release was the final act.

**Outcome**
It is known, by running it, whether `claude plugin marketplace add uchimata2/taskmd` followed by
`claude plugin install taskmd@taskmd` works for someone whose machine has never held this project,
and whether the command the README then tells them to type resolves.

**Why this one**
[T-006](T-006-package-document-and-publish.md) criterion 4 says *installs from a clean clone on a
machine that has never seen it*, and that is the one criterion its review could not tick. Everything
around it was proven at publication: the route was exercised from the published remote, the harness
cloned it fresh, the install materialised 24 files, and both entry points ran on an unrelated
project. All of that happened on the machine the project was written on.

What that machine cannot answer is the part the criterion is actually about: another operating
system, another Python, another user profile, and a `PATH` that has never been touched by any of
this. Two known local facts make it worth asking rather than assuming. `taskmd` does not resolve by
name here at all, which [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)
diagnosed as this machine's truncated shell snapshot and not the plugin's defect, and the README's
first install section ends in the bare name. And the install cache here already held a stale layout
from an earlier install, which is a state a fresh machine cannot be in.

**A real adopter has now paid for this, which was not true when this task was raised.** The first
adopting project (`control/LOCAL-CONTEXT.md`) moved onto the published plugin on 2026-08-09, on this
machine, and could not use the command the README gives: it had to add a small launcher of its own
that finds the install and runs it. That is one project's workaround for one machine's defect, and
it is evidence for the third criterion below rather than a fix to copy — the README says an adopter
types `taskmd`, and the first one could not.

**Requirements served**
R-20 (`docs/SCOPE.md`) — runs on a clone with no configuration; `docs/SCOPE.md` §1 *No install*.

**Scope**
- In: the marketplace-plus-install route from the published repository, on a machine that has never
  held taskmd.
- In: whether bare `taskmd` resolves there, which is the half T-054 could not settle locally and
  [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) settled only for a clone on
  `PATH`.
- In: the plain skill shape by the same test, since a copied folder depends on a launcher finding an
  interpreter it did not choose.
- Out: macOS specifically. [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) owns
  the platform claim and the README says macOS is untested rather than unsupported.
- Out: changing anything. If the install fails, the finding is the outcome and the fix is its own
  task.

**Inputs**
- [T-006](T-006-package-document-and-publish.md) §3 steps 7 and 8 — what was proven, and where.
- [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) — the same test against a
  throwaway remote, including that a remote marketplace silently replaces a same-named local one.
- [`README.md`](../README.md) — the two install sections, which are what is being tested.

**Acceptance criteria**
- [ ] Both install sections of the README are followed **as written** on a machine that has never
      held this project, and each ends in the command it names, with the transcript recorded
- [ ] Whether bare `taskmd` resolves there is stated either way, because a negative is the finding
      that T-054 left open
- [ ] Anything the README has to change is named, with the wording, rather than fixed here

**Open questions**
- **What stands in for the machine — half answered by measuring, half still the maintainer's.**
  Measured 2026-08-11: the WSL2 Ubuntu 26.04 profile on this machine has **never held any of this** —
  no `~/.claude` directory at all, no `taskmd` on `PATH`, a different user, a different home, a
  different Python. That is a real answer for the **plain skill** shape and it was used. It cannot
  answer the **plugin** shape: that profile has no Node and no `claude` CLI, and standing one up ends
  in an interactive sign-in, which a session does not perform. So the remaining question is narrower
  than when it was written: *where does the plugin route get tested*.

  **Answered by the maintainer on 2026-08-11: wait for an adopter to report it.** Three projects
  already run taskmd, so the next migration exercises the real route on a real machine at no cost to
  this one, and an adopter's transcript is better evidence than a prepared environment. *Rejected: a
  container or VM carrying the CLI* — it answers sooner, and §1 already says a machine prepared for
  the test is a developer machine, which answers the less interesting question. **This task therefore
  stays open until that report arrives**, and it is not waiting on anything anyone here can do.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure what candidate environments actually have, before choosing one | The survey in §3 |
| 2 | Clone the **published** repository at the `v0.5.0` tag, not the working tree | A checkout of what shipped |
| 3 | Follow the README's plain-skill section **as written**, and count the files against the number it claims | A transcript |
| 4 | Run the command that section ends in, then go beyond it: a real task through `index`, `check`, `list` and `context` | A transcript |
| 5 | State whether bare `taskmd` resolves, for each shape | §3 — criterion 2 |
| 6 | Name anything the README has to change, with the wording, and change nothing | §3 — criterion 3 |

Step 2 is what makes this M5's last task rather than a rehearsal: the artifact under test is the
one that shipped, reached the way a stranger reaches it.

## 3. Implement

### Step 1 — what the candidate actually is

```text
user        uchimata            (not the Windows profile)
home        /home/uchimata
os          Ubuntu 26.04 LTS
python3     /usr/bin/python3    Python 3.14.4
python      NONE                (no bare `python`)
node        NONE
claude      NONE
docker      NONE
~/.claude   does not exist
taskmd      not on PATH
```

**It has never held any of this**, which is the phrase the criterion turns on, and `~/.claude` not
existing is the strongest form of that. It is also missing what the plugin route needs.

### Steps 2 to 4 — the plain skill shape, from what shipped

```text
commit : f53ab37
tag    : v0.5.0
version:   "version": "0.5.0",

landed at: /home/uchimata/.claude/skills/taskmd
files    : 21   (README says 21)

OK - 0 task(s), 0 field value(s), 0 reference(s), 0 dependency edge(s), 0 declared output(s),
0 index file(s), 0 document(s), 0 link(s), 0 template(s), 0 template field value(s),
0 vocabulary row(s)
Scope  every document read; no git here, so .gitignore was not consulted
structure and references only - it cannot tell you whether a spec or an outcome is good
exit: 0
```

Followed as written: copy the folder, `mkdir tasks`, run the launcher. **The file count matches the
number the README claims**, which is a claim nobody had checked from outside. The empty-project line
matches the README's quoted output exactly, which it would **not** have done before
[T-129](T-129-release-v0-5.md) corrected that quotation earlier the same day.

Then past the README, on a real task file written by hand:

```text
Wrote tasks/README.md - 1 active, 0 closed
OK - 1 task(s), 5 field value(s), ... 1 index file(s), 2 document(s), 1 link(s), ...
T-001	proposed	-	specify	A first task on a machine that has never seen taskmd
T-001  A first task on a machine that has never seen taskmd
status proposed | phase specify | type deliverable
file   tasks/T-001-first.md
```

All four commands, no configuration, no dependency install, no path edited. The launcher found
`python3` on a profile with no bare `python`, which is the case
[T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) found a stock Ubuntu presents.

### Step 5 — bare `taskmd`

```text
plain skill shape:  taskmd on PATH: NONE      (before and after the install)
plugin shape:       not tested
```

For the plain skill this is **correct and documented**: the README says a copied skill gets no `PATH`
entry because that mechanism belongs to plugins, and it gives the launcher path instead. So this half
confirms the README rather than contradicting it. The half
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) left open is the **plugin**
one, and it is still open.

### Step 6 — what the README has to change

**Nothing.** Every claim its second section makes was followed and held: the destination path, the
self-contained folder, the file count, the two commands, and the output. The first section is
untested rather than wrong.

### What is not done, and why it is not a skip

The plugin route — `claude plugin marketplace add` then `claude plugin install` — was **not run**.
The profile that satisfies *never seen it* has no Node and no `claude` CLI, and installing one ends
in an interactive sign-in that a session does not perform. Installing the CLI into that profile would
also stop it being the thing being tested: an environment prepared for the test is a developer
machine, which §1 already says answers a less interesting question.

So criterion 1 is half met, criterion 2 is half met, and the task stays open. **That is the outcome
this task exists to produce** rather than a failure to reach one: §1 says M5 is complete when the
published artifact has been proven from outside, and half of it now has been, on a real second
operating system, from the tag.

### 2026-08-16 — what has moved since the decision, measured

Asked to work this task's full lifecycle. It cannot be run, and the reason is a recorded decision
rather than an obstacle: §1 says wait for an adopter, and no session can manufacture one. So the work
done instead was to test whether that decision's **premise** still holds, and to check that the half
already proven has not gone stale underneath it. Nothing was changed, per §1 Scope.

**The half that was proven still holds against the current tree.** The 2026-08-11 transcript was
taken against `v0.5.0`, and the README has moved since:

```
git diff v0.5.0..HEAD --stat -- README.md
 README.md | 25 +++++++++++++++++++++++--
```

**None of it is in the two install sections.** The whole diff is body documentation — the `WIDE ROW`
and `LABEL SHAPE` paragraphs, the `--work_package M2` example, and the empty-project `check` output
quotation gaining `table row(s)` and `front-matter value(s)`. So the sections under test are
byte-identical to the ones followed as written, and criterion 3's verdict — *the README needs
nothing* — is still a statement about the current file and not only about the tag.

**The file count the README claims still holds**, checked because it is the one number in that
section a tree can falsify without anyone editing prose:

```
tracked at HEAD     21
tracked at v0.5.0   21     README says 21
```

*A filesystem count says 31 and is wrong* — `plugin/skills/taskmd/taskmd/__pycache__/` is ignored and
is not in a clone. Recorded because the wrong number is what an adopter's own `ls` would show after
they run the tool once, and it is the kind of thing that gets reported as a defect.

**Nothing has shipped since**, so the artifact under test is unchanged: `v0.5.0` is still the newest
tag and the manifest still reads `0.5.0`.

**What has weakened is the decision's premise, and this is the finding.** §1 rejected a prepared
container in favour of waiting, reasoning that *three projects already run taskmd, so the next
migration exercises the real route on a real machine at no cost to this one*. Five days on:

- **No new adopter has appeared.** All four projects in the label map are the maintainer's own, and
  every one of them is a checkout on this machine — including the first adopting project, which §1
  already records as having migrated *here*. A migration by any of them cannot satisfy *a machine
  that has never seen it*, so the population being waited on has no member that can answer.
- **The channel that would have carried the report narrowed on 2026-08-15.** The sibling projects now
  send a branch and a pull request instead of a report, which is the right change for defects and
  removes the migration write-up this task was waiting to read.

That is evidence against the premise, not against the ruling. **Per the maintainer's standing rule
that new evidence licenses re-opening a recorded decision and never reversing it, this session
measured and stopped**, and the question goes back to the owner in the log below.

**Decisions & assumptions**

- **Cloned at the tag, not copied from the working tree.** The artifact under test has to be the one
  a stranger receives. — 2026-08-11
- **`git clone --depth 1 --branch v0.5.0` prints `warning: refs/tags/v0.5.0 <sha> is not a commit!`** and then
  checks out the right commit. It is git's note about a shallow clone of an **annotated** tag, not a
  defect in the tag or the repository, and `git describe` confirms `v0.5.0`. Recorded because it
  looks alarming in a transcript an adopter might produce. — 2026-08-11
- **The PowerShell launcher is not exercised.** That profile has no `pwsh`, and the Windows side is
  covered by every other run in this repository. — 2026-08-11
- **Nothing was changed.** §1 Scope says a failure is the finding. There was no failure in the half
  that ran. — 2026-08-11

**Outputs produced**
- This record.

## 4. Review

**Closed on the boundary, by the maintainer's ruling of 2026-08-16.** The finding this task produces
is *where the test can and cannot reach*, and that is now known: the plain-skill shape is proven from
outside on a real second operating system, and the plugin shape is **unreachable from here by
construction** — not merely untested. The two facts that make it a boundary rather than a backlog
item are in §3, 2026-08-16: every adopter is a checkout on this machine, and the channel that would
have carried an outside report narrowed on 2026-08-15.

**One criterion closes unmet, with no child task, and that is the ruling rather than an oversight.**
METHOD's `review` exit criterion is that every criterion is met *or* carries a child task that will
meet it. The maintainer chose neither: a successor would park an obligation on the same event that
cannot be caused, which is the state this close exists to leave. It is written here plainly so no
later reader takes the close as evidence the plugin route was verified.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Both install sections followed **as written** on a machine that has never held this project, each ending in the command it names, transcript recorded | **not met — closed unmet** | The plain-skill section: fully met, §3 steps 2–4, from a clone at `v0.5.0` on a WSL2 Ubuntu 26.04 profile with no `~/.claude` at all. 21 files against the 21 the README claims, and the empty-project output matching its quotation exactly. **The plugin section was never run**: that profile has no Node and no `claude` CLI, and standing one up both ends in an interactive sign-in a session does not perform and turns the untouched profile into the prepared machine §1 rejects. **No child task carries it** — 2026-08-16 ruling. |
| Whether bare `taskmd` resolves there is stated either way | **half met — closed as stated** | Stated for the plain skill: it does **not** resolve, before or after the install, which is what the README says will happen because the `PATH` mechanism belongs to plugins. Unstated for the plugin shape, which is the half [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) left open and which this close does not shut. |
| Anything the README has to change is named, with the wording, rather than fixed here | met | **Nothing**, and re-confirmed on 2026-08-16 against `HEAD` rather than left standing on the tag: the whole `v0.5.0..HEAD` diff to `README.md` is body documentation, so both install sections are byte-identical to the ones followed, and the 21-file claim is still true of the tracked tree. |

**Child fix tasks raised**
- none, deliberately. See the ruling above.

**What a later reader should not conclude.** That `claude plugin marketplace add` followed by
`claude plugin install taskmd@taskmd` works on a stranger's machine. It has never been run anywhere
but here. If an outside adopter ever reports it, the transcript belongs in a fresh task citing this
one — not in a reopening of this record, whose account of 2026-08-16 is true about 2026-08-16.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → done | **Closed on the boundary, the maintainer's ruling the same day**, chosen over splitting the task, over continuing to wait, and over re-opening the container rejection. The outcome is *where the test reaches*: the plain-skill shape proven from outside, the plugin shape unreachable from here by construction. **Criterion 1 closes unmet with no successor task** — a deliberate departure from METHOD's `review` exit criterion, taken because a successor would park the obligation on the same event nobody can cause. Written into the review in full so the close is never read as the plugin route having been verified. **This was M5's last open task**, and §1's ordering held to the end: the release was tagged on 2026-08-11 and the milestone closes five days later on what the artifact could be shown to do. |
| 2026-08-16 | (no change) | **Asked for the full lifecycle; it cannot be run, and the block is a recorded decision rather than an obstacle.** The maintainer's 2026-08-11 ruling is to wait for an adopter, and no session can produce one. Measured instead — §3, 2026-08-16 — that the proven half still holds against the current tree (neither install section has changed since the tag, and the 21-file claim is still true) and that **the ruling's premise has weakened**: every adopter in the label map is a checkout on this machine, so none can satisfy *a machine that has never seen it*, and the 2026-08-15 channel change replaced migration reports with pull requests. New evidence licenses re-opening a decision, never reversing it, so the question is put to the owner and nothing was changed. **The task stays `in_progress` at `implement`** — waiting is not a phase, and it has not moved backwards. |
| 2026-08-11 | (no change) | **The remaining question is answered: wait for an adopter.** Three projects already run taskmd, so the next migration exercises the plugin route on a real machine at no cost here, and an adopter's transcript beats a prepared environment. The rival, a container carrying the CLI, is rejected in §1 with its cost. **The task stays open and is waiting on nobody here** — that is a deliberate resting state, not a stall. |
| 2026-08-11 | → in_progress | **Half of it is now proven from outside, on the published `v0.5.0` artifact, and the task stays open.** The open question was half answered by measuring rather than by asking: the WSL2 Ubuntu 26.04 profile here has **no `~/.claude` at all**, a different user, a different home and no `taskmd` on `PATH`, which is a real answer to *a machine that has never seen it* for the plain-skill shape. Followed as written from a clone at the tag, it holds completely: 21 files, exactly the count the README claims and nobody had checked from outside; the empty-project output matches the README's quotation, which it would not have done before [T-129](T-129-release-v0-5.md) corrected that quotation hours earlier; all four commands work on a real task, with the launcher finding `python3` on a profile that has no bare `python`. Bare `taskmd` does **not** resolve there, which for this shape is what the README says will happen. **The plugin route was not run**: that profile has no Node and no `claude` CLI, and standing one up ends in an interactive sign-in a session does not perform, besides turning the untouched profile into a prepared one. Criterion 3 is met and says the README needs nothing. Nothing was changed. |
| 2026-08-11 | → planned | Six steps, and step 2 is what makes this M5's last task rather than a rehearsal: the artifact under test is cloned from the published tag, not copied from the working tree. Step 1 measures the candidate environments before choosing one, because `a container that ships no Python answers a more interesting question` is a claim about environments nobody had checked. |
| 2026-08-11 | (no change) | **Unblocked**: [T-129](T-129-release-v0-5.md) closed and `0.5.0` is published, so what gets installed here is what M5 shipped. The `blocked_by` edge stays as the record of the ordering the maintainer asked for. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: M5`, through all four phases — including a task raised into M5 *by* that work, which is a M5 task and not a fresh grant. It **does not generalise** to `M6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a M5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-09 | (no status change) | Second independent report of the same thing, from the deck-building sibling's migration (`control/LOCAL-CONTEXT.md`): `bin/` is dropped from `PATH` in agent shells built from the shell snapshot, so every invocation there needs `PYTHONPATH=<skill> python -m taskmd`. That is T-054's defect seen from outside this repository, which is what this task exists to measure. Their suggestion is that taskmd either document it or ship a shim; the first adopting project wrote its own, and its header says to delete it the day the bare name resolves. Two projects have now each solved it privately, which is the evidence that it is not a local quirk. |
| 2026-08-09 | → proposed | Raised by [T-006](T-006-package-document-and-publish.md)'s review as the child carrying its criterion 4. The route was proven end to end from the published remote on the day of publication, and the part that could not be proven is the phrase *a machine that has never seen it*: another OS, another Python, another profile, and a `PATH` this project has never touched. Carried as a task rather than ticked, because the local `PATH` failure T-054 recorded means the README's first install section ends in a command nobody has yet watched resolve by name on a stranger's machine. |
