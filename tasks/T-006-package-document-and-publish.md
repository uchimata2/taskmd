---
id: T-006
title: Package, document and publish
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-002, T-003, T-004, T-008, T-009, T-010, T-011, T-018, T-079, T-083]
related: []
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-09
deliverables: []
---

# T-006 — Package, document and publish

## 1. Specify

**Outcome**
An installable plugin with a README that only claims what has been demonstrated.

**Why this one**
A README written before the thing works becomes the unverified claim the whole project warns about. Written last, on purpose.

**Requirements served**
R-15, R-20, R-23 (`docs/SCOPE.md`). This task closes the definition of done, `SCOPE.md` §9.

**Acceptance criteria**
- [ ] Install instructions end with a command that proves it runs
- [ ] The measured `context` saving reproduced on a sample project and quoted
- [ ] No personal, client or machine data anywhere in the repository
- [ ] Installs from a clean clone on a machine that has never seen it
- [ ] The package ships the method document and **both** bindings, and the README states that
      changing backend changes the binding, not the method (R-13, R-14)
- [ ] The README claims a supported scale that T-004 measured, and nothing it did not
- [ ] Every non-goal in `SCOPE.md` §4 still holds at publish — checked, not assumed
- [ ] **Both** distribution shapes install from a clean clone and are each proven by a command that
      runs — the marketplace plugin and the plain skill package
      <br>*Added 2026-08-07 with the answer to the distribution question. The seven above predate it and
      are unchanged.*
- [ ] **Every document `docs/PUBLISHING.md` covers has been through its rule, and its §5 gate passes
      with a non-zero file count** — the count, not the silence
      <br>*Added 2026-08-09 by [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md). Without
      it `review` could tick every other box on a README nobody had humanized, which is what the
      maintainer found by asking. The eight above are unchanged.*

**Criterion 3 amended at publication, by the person who agreed the original.** It now reads: *no
personal, client or machine data in the published tree, and any exposure carried by the history is
stated and accepted rather than discovered.* The original:

> - [ ] No personal, client or machine data anywhere in the repository

It was written against what the pre-publish check reads, which is the working tree, and the history
is part of the repository a push sends. §3 step 7 has the scan and the numbers: one line, in two
commits, carrying this machine's repository path and nothing that identifies a person. No acceptable
outcome satisfied the original text — both ways of removing the line destroy the commit citations
these records are built on — so the maintainer accepted the exposure with the alternatives in front
of them. Recorded here with the original beside it, because a criterion quietly narrowed to fit its
result is a description.

**Open questions**
- **What the second shape actually is.** Step 1 falsified the premise the 2026-08-07 answer rests on:
  no subset of this tree is a working skill package, because `SKILL.md`'s `../../` pointers escape any
  directory a subset would be copied into, and `bin/` on `PATH` is a plugin mechanism a skill install
  does not have. Three ways out, and the choice changes what steps 5 and 8 write and prove.
  **Answered by the maintainer on 2026-08-09: (b)**, and raised as
  [T-083](T-083-make-the-skill-directory-self-contained.md), which now blocks this task at step 5.
  *(a) Assemble the package at release time* from the one tree, rewriting four
  link prefixes — keeps both shapes and keeps one home for the skill body, at the cost of a build step
  in a project whose pitch is that there is no build. *(b) Move `docs/` and the package under
  `skills/taskmd/`* so the skill directory is self-contained and shape two becomes a copy of one
  folder — `bin/` stays at the plugin root as the `PATH` shim and gains one line of relative path.
  The cost is a directory move at publication, and T-064 already showed that a link checker says
  nothing about the prose citations a move leaves dangling. *(c) Drop the second shape* and publish
  the plugin alone, which reverses the 2026-08-07 answer rather than repairing its premise.
- ~~Which distribution shapes~~ — **answered by the maintainer on 2026-08-07: both, with the
  marketplace plugin primary.**
  The tree is already a plugin and the marketplace is how it is found; the plain skill package is a
  subset of the same tree and is what someone not using the marketplace needs. *Rejected: the plugin
  alone.* Two shapes are two sets of install instructions and paths to keep true — which is the cost
  this answer accepts, and which the criterion added with it exists to hold.

**Why the new blockers**
`blocked_by` gained T-008, T-009, T-010 and T-011. The definition of done requires the method
document, both bindings implementing the same lifecycle, and a clone that runs with nothing
installed — publishing before those exist would ship a product that fails its own stated scope.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the **plain skill package** and run a command the skill names from it. The marketplace shape is proven (T-067); this one has never existed, and `bin/` reaching `PATH` is a plugin mechanism (T-054), not a skill one. | The list of files the shape consists of, and the transcript of the command running from it — or, if the entry point does not resolve by that route, the statement of what it offers instead |
| 2 | Reproduce the `context` saving: the bytes a session reads to start one task without the tool, against the bytes `context <id>` returns, on this repository. | Both byte counts, the id they were taken on, and the commands that produced them, in §3 |
| 3 | Check each of `SCOPE.md` §4's eleven non-goals against the tree as it stands. | An eleven-row verdict table in §3, each row naming what was looked at rather than asserting the non-goal |
| 4 | Settle what the README says about scale and about platforms — the ceiling is whatever T-004 measured and nothing past it, and T-020's amended outcome states macOS untested rather than claimed. | The two sentences as they will appear in the README, with what was rejected, in §3 |
| 5 | Write the README from steps 1–4: what the tool is, both shapes' install instructions each ending in a command that proves it runs, and the backend sentence criterion 5 asks for. | `README.md` |
| 5a | Humanize the README under [`docs/PUBLISHING.md`](../docs/PUBLISHING.md), then run its §5 gate. The rule names the exception and the skill; this step does not restate either. | The rewritten `README.md`, and the gate's count with nothing after it |
| 6 | Run the pre-publish check both ways, after this record and the README are written, after step 5a, and before anything is pushed. | The silent run with the exclusion, and the five-line run without it |
| 7 | Publish to a public remote, setting the repository description from [`docs/repo-description.txt`](../docs/repo-description.txt). The maintainer's action: it is outward-facing and not undoable, and the token this project has already failed twice to delete a repository with (T-037, T-077). | The public repository, described |
| 8 | Install **both** shapes from a clean clone of what was published, run each shape's proving command, and list what the install carries. | Two transcripts, and the installed file list — which is also how criterion 5's "ships the method document and both bindings" is read rather than assumed |

**Step 1 did invalidate part of the rest, and the plan is revised here rather than quietly.**
*Added 2026-08-09.* Its answer is in §3 and the maintainer chose the repair the same day, so steps 5
and 8 now write and prove a shape that does not exist yet:
[T-083](T-083-make-the-skill-directory-self-contained.md) makes `plugin/skills/taskmd/` self-contained
and is a new blocker on this task. **Steps 2, 3 and 4 are done and none of them moves** — they measure
this repository, not the package layout. Step 5 resumes when T-083 closes, and its second set of
install instructions is then a copy of one folder rather than the assembly step step 1 had to perform
by hand. The paragraph below is what the plan said before the answer, and it stands: it is the reason
the answer arrived cheaply.

**Step 1 is first because it can invalidate the rest.** Criterion 8 asks both shapes to be proven by
a command that runs, and the second shape is a name in an answer rather than anything that exists.
If a skill-only install cannot put `taskmd` on `PATH`, then steps 5 and 8 are writing and proving a
different document than they would otherwise be — so the horizon this plan can honestly see ends at
step 1, and steps 5 and 8 are named at the level their inputs support.

**Steps 2–4 come before step 5 on purpose.** Each produces a number or a sentence the README then
quotes. Writing the README first and measuring afterwards is exactly how a document ends up carrying
a figure nobody took, which is the failure this task was scheduled last to avoid.

**Decisions — the shape of the deliverable**

- **One README, at the repository root.** It is the front door for both shapes and for anyone
  browsing the repository, and nothing inside `plugin/` cites it, so T-064's constraint is untouched.
  *Rejected: a second README inside `plugin/`* — a second copy of the install instructions, shipped
  into every install cache, read by nobody who has not already installed it. *Rejected: one README
  per shape* — two homes for one fact, when the shapes differ in about a dozen lines.
- **The README points at the method; it carries none of it.** Criterion 5's sentence — changing
  backend changes the binding, not the method — is a claim about the *package*, so it belongs there;
  `plugin/skills/taskmd/docs/METHOD.md` and `plugin/skills/taskmd/docs/bindings/` stay the only homes for the thing itself.
- **This repository is the sample project of step 2.** It is the only real taskmd project that
  exists, and its tasks are real work. *Rejected: a project built for the measurement*, which would
  produce a ratio chosen rather than found. *Rejected: quoting `reference/`'s 37,909 → 992*, which is
  the prior art's number and is already in `docs/BRIEF.md`; criterion 2 asks for it reproduced.
- **Nothing this task writes is added to `CLAUDE.md`.** Tier 1 is over its bound already
  ([T-063](T-063-measure-the-tier-1-member-the-rule-declares.md)), and every character there is paid
  on every turn of every session; a README is read once. Whatever `CLAUDE.md` owes at close is a
  pointer, not a summary.

**The README is written here and humanized here, under a rule owned elsewhere.** This paragraph
originally said the README left for T-079 and came back. That was true while T-079 was an open
blocker and stopped being true the moment it closed, which left this plan describing a hand-off that
could not happen and no step applying the rule at all — found by the maintainer asking whether
deployment forces it, and repaired in [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md).
Step 5a is that step. The rule, the exception and the gate live in
[`docs/PUBLISHING.md`](../docs/PUBLISHING.md); nothing here restates them.

**Not in this plan, deliberately:** the remote's identity, which is `control/LOCAL-CONTEXT.md`'s;
and reconciling `CLAUDE.md`'s status paragraph and `docs/SCOPE.md` §9, which is closing work rather
than a step that produces the outcome.

## 3. Implement

Worked in plan order. Steps 1 to 6 are below. Step 5 was held for the reason step 1 gives and
resumed once [T-083](T-083-make-the-skill-directory-self-contained.md) closed; **steps 7 and 8 are
the maintainer's and what follows them**, so `implement` stops at 6 rather than being finished.

**One thing found here and raised rather than absorbed.** Grepping the tree for pre-move paths, to
be sure the README was not about to cite one, turned up three lines in `tasks/README.md`'s
hand-written preamble that still name a launcher T-083 deleted. It is the one file under `tasks/`
that describes the tree as it is now rather than as it was, and T-083's residue sweep exempted the
whole folder as closed records. That is [T-084](T-084-correct-the-generated-index-preamble-after-the-move.md),
not a quiet fix here: correcting it in passing would leave that task's `outside tasks/ 0` looking
right.

### Step 1 — the plain skill package, and why it is not a subset

The plan put this first because it can invalidate the rest. It did.

**The straight copy fails before the entry point is even reached.** A plain skill is a directory under
the harness's own `skills/` folder, so `plugin/skills/taskmd/` copied there puts `SKILL.md` two levels
below that folder — and every pointer it makes is written `../../`, which now escapes the package
into the harness's root:

```
DANGLING  taskmd/SKILL.md -> ../../docs/METHOD.md
DANGLING  taskmd/SKILL.md -> ../../docs/bindings/
DANGLING  taskmd/SKILL.md -> ../../docs/METHOD.md
DANGLING  taskmd/SKILL.md -> ../../taskmd/defaults/config.md
DANGLING  taskmd/adopt.md -> ../../taskmd/defaults/config.md
DANGLING  taskmd/adopt.md -> ../../docs/bindings/
DANGLING  taskmd/adopt.md -> ../../docs/METHOD.md
2 markdown file(s), 7 dangling link(s)
```

This is [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md)'s failure arriving from
the other direction: the plugin ships what it cites, and the skill package would cite what it does
not ship. The `../../` shape is correct for the plugin layout and is exactly what breaks the copy.

**A self-contained package does work, and it is 23 files.** Assembling `SKILL.md`, `adopt.md`,
`docs/`, `taskmd/`, `bin/` and both launchers into one directory, with the four link prefixes
rewritten, resolves everything and runs:

```
14 markdown file(s), 0 dangling link(s)

<package>/bin/taskmd check      OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
<package>/bin/taskmd list       T-001  specified  -  plan  Generated task 1
<package>/bin/taskmd.cmd check  OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
```

Run from a project that is neither this repository nor the package, through `sh` and through the
`.cmd`, so both platforms' entry points are covered. Against the marketplace install's 24 files
([T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md)) the difference is one:
`.claude-plugin/plugin.json`, which a skill has no use for.

**What it cannot offer is the command the skill names.** `taskmd` is not on `PATH` by this route and
cannot be: collecting `<plugin-root>/bin` is something the harness does for enabled **plugins**, which
is [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)'s whole mechanism, and a
skill is not a plugin. What a skill does get is its own base directory, which the harness states to
the session on invocation — so the command it can honestly name is one relative to that.

*Not a new finding, and not re-raised:* bare `taskmd` also fails on this machine from the installed
plugin, in both the bash and the PowerShell tool, with no `PATH` entry mentioning a plugin at all.
That is the truncated shell snapshot T-054 diagnosed and recorded as this machine's rather than the
plugin's, and [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) settled the question
elsewhere by running the bare name on `PATH` on Linux. `claude plugin list` reports `taskmd@taskmd`
version 0.1.0, user scope, enabled — so the install is real and the `PATH` is the known local defect.

**So the maintainer's 2026-08-07 answer rests on a premise this step falsified.** It reads *"the plain
skill package is a subset of the same tree"*. No subset of the tree is a working skill package: the
subset's own documentation dangles, and the entry point is a mechanism the route does not have. The
question that follows is in §1 *Open questions*, because it changes what steps 5 and 8 produce and
that is not this session's to decide alone.

### Step 2 — the `context` saving, re-measured on this repository

**T-029**, chosen because its shape is ordinary: one parent, three soft links, no blockers. Starting
it without the tool means the task file, the project's conventions, the generated index, and every
task it links to.

```
taskmd context T-029 | wc -c                                    693

wc -c  tasks/T-029-….md  CLAUDE.md  tasks/README.md
       tasks/T-026-….md  tasks/T-002-….md  tasks/T-022-….md  tasks/T-055-….md
                                                             156901 total
```

**156,901 bytes to 693, which is 0.44%.** `docs/BRIEF.md` records the prior art at 37,909 to 992, or
2.6%; the ratio is better here because this project's task records are far longer, which is a
property of the sample and not an improvement in the tool.

**And that figure is the generous reading.** It counts the links T-029 stores. The far end of a soft
link and every `blocks` edge are derived and written nowhere, so a session without the tool cannot
know what waits on T-029 without reading every task file: `cat tasks/T-*.md | wc -c` is **1,274,604
bytes**. The honest range is that the tool replaces between 157 kB and 1.27 MB with 693 bytes,
and the wide end is `docs/BRIEF.md`'s third wall rather than a rhetorical flourish.

### Step 3 — the eleven non-goals, against the tree

Each row names what was looked at. The shipped tree is `plugin/`.

| # | Non-goal | Verdict | What was looked at |
| :-- | :--- | :---: | :--- |
| 1 | Project management | holds | `value_field` and `effort_field` are read in exactly two places, `effective_values` and `order` in `cli.py`, both the ordering. The amendment's own test is that either field being read by anything else has left the carve-out; nothing else reads them |
| 2 | A running process | holds | The package imports `os, re, shlex, shutil, subprocess, sys` and `json`. No socket, no threading, no asyncio, no database |
| 3 | A user interface | holds | Same import list: no curses, no tkinter, no webbrowser, no server. Output is `print` |
| 4 | Multi-user coordination | holds | No locking module is imported. [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) §3 D4 settled what a collision does instead: every command reports it and nothing renumbers |
| 5 | Network access from the core | holds | No `urllib`, `http`, `socket` or `requests` anywhere in the package |
| 6 | An automatic fixer | holds | One `write()` in the whole package and one call site, `cmd_index` at `cli.py:305`. The tool writes the index and nothing else, so no task content can be rewritten |
| 7 | Model, effort or cost gates | holds | One occurrence of "model" in the shipped tree, a `rationale.md` heading saying the method says nothing about which model does the work |
| 8 | Migration tooling | holds | No match for `migrat` anywhere in the package or its docs; `COMMANDS` is `{check, context, index, list}` |
| 9 | Replacing GitHub Issues | holds | The GitHub binding applies the method to issues through `gh`, and its assumptions section asks whether the project's habits fit rather than asking anyone to leave |
| 10 | Notifications, scheduling, recurrence | holds | Three prose hits, all innocuous: "recurred" in `audit.md`, "on a schedule" in `rationale.md`, and the heading above. No scheduler, no timer |
| 11 | A query language | holds | `list`'s filters are `--<field> <value>` over the configured vocabularies and link names, plus `--open`, `--closed`, `--limit`, `--json`. No boolean expressions, no saved queries, no aggregation |

### Step 4 — the two sentences

**Scale**, quoted verbatim from [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md)
§3 D2, which wrote it to be quotable and dash-free so it survives §5a's gate:

> At its shipped id width taskmd handles up to 999 tasks with every command finishing in under a
> second (measured at 999 tasks: `check`, the slowest, took 0.83 s), and a project that raises
> `id_width` to go further pays 1.34 s for `check` at 2000 tasks and up to 3.9 s at 5000.

*Rejected: a bare "fast" or "scales to thousands"*, neither of which anything measured.

**Platforms:**

> Run on Windows and on Linux, where a fresh clone regenerated a byte-identical index. macOS is
> untested rather than unsupported: nothing in the tool is known to depend on the platform, and
> nobody has run it there.

*Rejected: claiming macOS*, which is what T-020's outcome was amended in order not to do. *Rejected:
omitting macOS silently*, which reads as a claim to a reader scanning for their own platform. The
Linux half is [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)'s, which compared
the regenerated index against the committed blob two ways.

### Step 5 — the README

[`README.md`](../README.md), at the repository root, written from steps 1 to 4 and from
[T-083](T-083-make-the-skill-directory-self-contained.md). Every number in it was quoted rather than
re-taken: the `context` saving from step 2, the scale and platform sentences verbatim from step 4,
and the 21 files of the copied skill folder from T-083 §3 step 7, re-run here as the install
instruction rather than trusted.

**What the two shapes say, which is the loose end T-083's review handed forward.** The plugin route
ends in `taskmd check`, because the harness puts an enabled plugin's `bin/` on `PATH`; the skill
route ends in `~/.claude/skills/taskmd/taskmd.sh check`, because a copied skill has no such
mechanism and runs the launcher it contains. The README says both, one line apart, and says why. It
does **not** describe the difference as a defect or promise to remove it.

**Setup is `mkdir tasks`, and the install instructions say so**, because a fresh directory is not a
project and `check` will tell the reader that rather than pass. Both branches were run, in a
directory with no taskmd project above it:

```
taskmd check          No taskmd project here. Looking upwards from the working directory, …   exit 2
mkdir tasks
taskmd check          OK - 0 task(s), vocabulary valid, references resolve, no broken links   exit 0
```

The second line is what both install sections end on, so the command that proves the install is the
same command an adopter's project keeps using. The skill shape was proven the same way from a copy
of the folder, through `taskmd.sh` and through `taskmd.ps1`, on a project that is neither this
repository nor the copy.

**Decisions taken here**

- **The marketplace source is named rather than left as a placeholder.** Asked and answered by the
  maintainer on 2026-08-09: `uchimata2/taskmd`. A published README whose first command carries
  `<owner>/<repo>` reads as unfinished, and nothing mechanical would catch the substitution being
  missed at step 7. This is not the kind of identity `control/LOCAL-CONTEXT.md` quarantines: it is
  the address of the thing being published, public the moment step 7 runs. *Rejected: the
  placeholder*, for the reason above.
- **The README opens in its own words rather than reusing
  [`docs/repo-description.txt`](../docs/repo-description.txt).** The two say the same thing about
  the same product, which is unavoidable, but copying the string would make the file a second home
  for a value the gate reads. *Rejected: quoting the description verbatim as the first paragraph.*
- **No claim about macOS, no claim about a ceiling nobody measured.** Step 4's two sentences appear
  exactly as written, and the em-dash-free form T-004 wrote them in is what let 5a leave them alone.

**Revised on the maintainer's reading, the same day.** Three notes, all applied, and the second one
is the substantive one:

1. **A lifecycle diagram**, left to right, from a task being created through the four phases to
   `done`, with a review that fails producing a fix task that re-enters at `specify`. It is a
   `mermaid` block, so it renders on the repository page and stays a text file in the tree.
2. **The section order is the maintainer's**, not the one written at step 5: what using it looks
   like comes before what a task is, and the measurement moved down from second place to seventh.
   Their list did not include *Install*, which the earlier draft carried and criteria 1 and 8
   require, so it is kept and placed after *The commands*, and the omission is reported rather than
   read as a deletion.
3. **No self-justifying framing.** *"This is the headline claim, and it is measured on this
   repository rather than asserted"* is gone, and so is the sentence calling the 0.44% a generous
   reading. The numbers are stated and the reader can judge them. The maintainer's words for the
   standard: show the benefits, no sales pitch.

A **Using it** section came with the reorder: five things somebody says to Claude, and what happens
underneath. It is the one part of the README that describes the method rather than the tool, so each
row is checked against [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) rather than written
from memory: one phase per request, a full lifecycle only when it is asked for, and an audit that
raises a child task per finding instead of fixing anything where it was found.

### Step 5a — humanized, and the gate

Run through the `humanizer` skill in file mode, under
[`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §2, with the maintainer's exception applied: tables,
code blocks, heading hierarchy and bolded labels preserved, patterns 15, 16 and 18 skipped, the rest
applied including 14. Neither escape the skill offers was taken.

What the pass actually changed, since a gate cannot tell: a one-line warm-up under a heading that
restated it, a run of subjectless fragments in *What it is not*, an opening that reused the
description's sentence fragments, and one sentence that claimed the command name was *the only*
difference between the shapes, which contradicted the paragraph above it.

```
4 file(s) covered
```

Exit 1, nothing after the count. The count moved from 3 to 4 with this README, which is the half of
that gate `docs/PUBLISHING.md` §5 says to read.

**Run again on the revision**, because a rewritten covered document is new text and the rule is
about the text rather than about the file having been through once. Same result, and the second pass
had less to do: the reorder mostly moved prose that had already been through the skill, and what was
new was four sentences and a table of five rows.

### Step 6 — the pre-publish check, both ways

Run after this record and the README were written, and after 5a, which is the order
`../CLAUDE.md` gives and the order `docs/PUBLISHING.md` §3 repeats for the rewrite.

```
with the exclusion       silent, 165 files read     (163 before this session; +2 is the README and T-084)
without the exclusion    one file matches, with 5 matching lines: the fixture
```

The second run is reported as a per-file count rather than as the lines themselves, for the reason
`../CLAUDE.md` states and this project has paid for twice: quoting a matched line into the record of
a task about the check re-creates the leak. The count is the evidence; the lines are in
`tests/fixtures/leak-check/samples.txt`, where they were fabricated to be.

**Read the file count, not the silence.** 165 is what makes the first run mean anything, and it is
two higher than the last recorded run because this session added exactly two files a push would
send.

### Step 7 — published

The maintainer instructed publication on 2026-08-09 after reading the README, which is the
authorization this step was waiting for. `uchimata2/taskmd`, public, description set from
[`docs/repo-description.txt`](../docs/repo-description.txt) in the same command, `master` at the
commit that revised the README.

**One thing was found before anything was created, and it changed the decision.** The pre-publish
check reads the working tree; a push sends the **history**. Scanning all 78 commits found one line
carrying an absolute local path, added and later removed in the two commits that
[T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) exists because of. Everything
else that matched was the fixture, or the fabricated specimens in their pre-fixture form.

```
15  matching lines in the full log stream
10  of them not a line of the fixture, which is 5 lines seen twice, added then removed
 1  distinct line containing this machine's repository path
 0  containing its user name, home directory, host name or an address
```

The classification was produced without printing a single matched line, and the identity test
reports booleans only, for the reason `../CLAUDE.md` gives about writing up a checker.

**The first instrument was wrong and is recorded rather than replaced quietly.** A one-liner passed
through the shell mangled two of the four branches, found 6 of the 15, and looked authoritative. The
gap between it and the plain `grep` count is what exposed it. This is the third time in two days
that a narrower-than-intended instrument printed a clean answer here.

**Decision — published as is, with the exposure accepted rather than absorbed.** The maintainer's,
on 2026-08-09, with the finding and the alternatives in front of them. What is public is a drive and
two folder names with no identity attached. *Rejected: squashing to a single initial commit*, which
publishes no history at all and leaves every commit hash cited across these task records pointing at
something no reader can open. *Rejected: rewriting the two commits*, which breaks the same citations,
since both are ancestors of everything, and needs a tool this project does not carry.

### Step 8 — both shapes, from a clean clone of what was published

The pre-existing install was captured before anything was disturbed, on
[T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md)'s precedent, and that capture is
where the unplanned finding came from:

```
before, directory route   33 files, and the layout from before T-083 moved anything
after,  git route         24 files, exactly plugin/'s tracked contents
```

**A directory install is a snapshot taken when it was installed.** The one on this machine was still
serving `docs/` and `taskmd/` at the plugin root, a layout that stopped existing earlier the same
day, plus four lock files and five `.pyc`. Nothing warns you: the harness serves what it copied.

Shape one, installed by the route the README names, from the published remote:

```
claude plugin marketplace add uchimata2/taskmd     Successfully added marketplace: taskmd
claude plugin install taskmd@taskmd                Successfully installed plugin: taskmd@taskmd

<install>/bin/taskmd check       OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
<install>/bin/taskmd list        T-001  proposed  -  specify  A task in a project that is …
<install>/bin/taskmd.cmd check   OK - 1 task(s), …                                                       exit 0
```

Shape two, copied out of a fresh `git clone` of the published repository:

```
21 files in plugin/skills/taskmd/

<copy>/taskmd.sh check    OK - 1 task(s), vocabulary valid, references resolve, no broken links   exit 0
<copy>/taskmd.ps1 check   OK - 1 task(s), …                                                       exit 0
```

Both run on a project that is neither this repository, nor the clone, nor the install, and both
platforms' entry points are covered. **Criterion 5 is read from the 24-file list rather than
assumed**: `skills/taskmd/docs/METHOD.md`, both files under `docs/bindings/`, all six phase files,
the package and its default config are in it.

**Restored, and the same thing had to be restored as last time.** Uninstall, remove the git
marketplace, re-add the directory one, reinstall. The harness emptied this repository's
`.claude/settings.json` during the swap, exactly as T-067 recorded; it showed up in `git status`,
which is what [T-052](T-052-decide-what-of-claude-a-published-clone-carries.md) tracks the file for,
and was restored from the index. The restored install is 29 files: the current layout plus the five
`.pyc` a directory copy takes from the working tree, and none of the stale ones, so an uninstall does
clear a version rather than merging into it.

**Outputs produced**
- Steps 1 to 8 above.
- [`README.md`](../README.md) — the deliverable.
- **https://github.com/uchimata2/taskmd** — public, described.
- [T-084](T-084-correct-the-generated-index-preamble-after-the-move.md) — raised, and closed the same
  day on the maintainer's instruction.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Install instructions end with a command that proves it runs | met | Both sections end in `check`, and §3 step 8 runs each from the published artefact rather than from this tree. The plugin section also covers the branch before setup, where `check` exits 2 and says there is no project |
| The measured `context` saving reproduced on a sample project and quoted | met | §3 step 2: 156,901 bytes to 693 on T-029, and 1,274,604 to 693 counting what a session must read to learn nothing waits on it. The README quotes both and re-measures neither |
| No personal, client or machine data anywhere in the repository | met, **criterion amended** | The published tree is clean: the check reads 165 files and prints nothing, and exactly the fixture without the exclusion. The history is not clean, and §3 step 7 says what is in it, how it was found, and why the maintainer accepted it rather than removing it. The original text is kept in §1 beside the amendment |
| Installs from a clean clone on a machine that has never seen it | **not met, carried** | Everything except the last five words was done at publication: the harness cloned the published remote, the install materialised 24 files, and both entry points ran. It all happened on the machine the project was written on. → **child task [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md)**, which also carries the bare-`taskmd` question T-054 could not settle locally |
| The package ships the method document and **both** bindings, and the README states that changing backend changes the binding, not the method | met | Read from the installed file list in §3 step 8, not from the source tree: `docs/METHOD.md`, `docs/bindings/github-issues.md`, `docs/bindings/local-markdown.md` and all six phase files are in the 24. The README's *Backends* section carries the sentence in bold |
| The README claims a supported scale that T-004 measured, and nothing it did not | met | §3 step 4's sentence appears verbatim, including the 0.83 s at 999 tasks and the two figures past the shipped width. Nothing in the README says "fast" or "scales to thousands" |
| Every non-goal in `SCOPE.md` §4 still holds at publish — checked, not assumed | met | §3 step 3's eleven rows, each naming what was read. Re-checked at close against the shipped tree: the package's imports are unchanged, and `COMMANDS` is still the four |
| **Both** distribution shapes install from a clean clone and are each proven by a command that runs | met | §3 step 8. Shape one by the README's own two commands against the published marketplace; shape two by copying one folder out of a fresh clone. Four transcripts, since each shape was run through both platforms' entry points |
| **Every document `docs/PUBLISHING.md` covers has been through its rule, and its §5 gate passes with a non-zero file count** | met | The README went through the skill at step 5a and again after the maintainer's revision, since a rewritten covered document is new text. `4 file(s) covered`, exit 1, nothing after the count |

Eight met, one carried. The gap is the phrase *a machine that has never seen it*, and it is a task
with an owner rather than a sentence in a paragraph.

**What this review does not claim.** That the README is correct for a reader who is not the
maintainer. Every instruction in it was executed here, which is what the criteria asked for, and
T-085 is where that becomes evidence about someone else's machine.

**Child fix tasks raised**
- **[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md)** — criterion
  4, carried.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Published, both shapes proven from a clean clone of what was published, eight criteria met and one carried. **The scan that preceded publication is the part worth remembering**: the pre-publish check reads the working tree, a push sends the history, and nobody here had ever read the history. It holds one line with an absolute local path, in the two commits T-018 exists because of, and nothing identifying a person. The maintainer accepted that with both removals in front of them, since either one breaks every commit hash these records cite, and criterion 3 is amended to say so with its original kept. The first scanning instrument was mangled by the shell and found 6 of 15 while looking authoritative, which is the third such tool in two days. Step 8's unplanned finding came from capturing the local install before disturbing it, again on T-067's precedent: it was still serving the pre-T-083 layout, because a directory install is a snapshot of the moment it was installed and nothing says so. The harness emptied `.claude/settings.json` during the marketplace swap exactly as T-067 recorded, and it was restored from the index. Criterion 4 is carried by [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md): everything but the phrase *a machine that has never seen it* was done, and that phrase is the whole of what a second machine would add. |
| 2026-08-09 | (no change) | README revised on the maintainer's reading: a left-to-right lifecycle diagram, their section order, and no self-justifying framing around the measurement. Their order omits *Install*, which criteria 1 and 8 require; it is kept, placed after the commands, and reported rather than treated as a deletion. Both gates re-run on the revision, because a rewritten covered document is new text: 4 files covered with nothing after the count, and the leak check silent across 165 files, which is the 166 the tree now holds less its own fixture. |
| 2026-08-09 | (no change) | Steps 5, 5a and 6 worked; `implement` now stops where the maintainer's action begins. The README is written and humanized, and every figure in it is quoted from steps 2 and 4 or from T-083 rather than re-taken. Two things were settled here rather than deferred: the marketplace source is named, `uchimata2/taskmd`, because a placeholder in the first command of a published front door is a substitution nothing would catch at step 7; and the two shapes name different commands, one line apart, with the reason given instead of an apology. Both install sections end in a command that was run, including the branch where the reader has no tasks folder yet, since `check` reports that rather than passing. The humanize gate covers 4 files now rather than 3, which is the number that moves when a covered document is added. One finding was raised rather than absorbed: `tasks/README.md`'s hand-written preamble still names the launcher T-083 moved, exempted by a sweep that treated the whole `tasks/` folder as closed records, and it is T-084. |
| 2026-08-09 | → in_progress | Steps 1 to 4 worked in plan order; step 5 held. The plan said step 1 came first because it could invalidate the rest, and it did: no subset of this tree is a working skill package. A straight copy leaves seven dangling links, because `SKILL.md`'s `../../` pointers are correct for the plugin layout and escape any other one, and `bin/` on `PATH` is a plugin mechanism a skill install does not have. A self-contained 23-file package does work and was run through both entry points from an unrelated project, but it cannot be produced by copying. So the 2026-08-07 answer's premise is false and its question is re-opened with three ways out and a recommendation, rather than one being chosen here. The `context` saving reproduces at 156,901 bytes to 693, and 1,274,604 to 693 if you count what it takes to learn nothing waits on the task. All eleven non-goals hold, each row naming what was read. Bare `taskmd` failing on this machine is T-054's snapshot defect and is recorded as not re-raised; T-049 proved the bare name on Linux. |
| 2026-08-09 | (no change) | Reconciled by [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md). When T-079 closed, this plan was left describing a hand-off to it that could no longer happen, and **no step applied the humanize rule at all** — the blocker had dissolved and taken the step with it. Step 5a now applies it and runs the gate, and a ninth acceptance criterion makes `review` able to fail for skipping it. Step 7 already named where the repository description lives; that home moved from a task record into `docs/repo-description.txt`, and the step's link resolves through `docs/PUBLISHING.md` §4 rather than being restated here. |
| 2026-08-09 | (no change) | **Answered by the maintainer: T-004 first.** So the question this plan raised is closed by a dependency rather than by the README going silent, and criterion 6 will be met by a measured ceiling instead of vacuously. `blocked_by` gains T-004, which leaves `related` — one relationship shown under two edge kinds is noise in the graph, not the permitted second write. It also gains **T-079**, raised in the same turn: the human-facing documents go through the `humanizer` skill before anything is published, which is a blocker because publication makes the first impression once and because step 5's README is that task's input. Plan steps 4 and 6 are reworded to match; nothing else in the plan moved. |
| 2026-08-09 | → planned | Eight steps. The plain skill package leads because it is the one shape that has never existed — the marketplace route was installed and listed by T-067, while `bin/` reaching `PATH` is a plugin mechanism T-054 proved for plugins, so a skill-only install may not be able to end its instructions in the command criterion 1 asks for. The plan says so rather than inventing steps 5 and 8 in detail against an unknown. Four shape decisions, each with its rejection: one root README; the README points at the method and carries none of it; this repository is the sample project the `context` saving is re-measured on, because a project built for the measurement chooses its own ratio; and nothing lands in `CLAUDE.md`, which is over its tier-1 bound already. **One thing is raised rather than absorbed**: criterion 6 asks the README to claim a scale that T-004 measured, and T-004 has measured nothing, so on the plan as written that criterion is met by claiming no ceiling at all — vacuously. Whether publication waits for T-004 is a dependency edge, and the maintainer's to add. |
| 2026-08-07 | → specified | Answered: both shapes, plugin primary. One acceptance criterion added with the answer — both shapes install from a clean clone and are proven by a command — because shipping two distributions and testing one is how the second becomes stale, and the criteria named no shape at all. The seven that predate this are unchanged. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-05 | (no change) | `blocked_by` gained T-018: a tracked file carries a real absolute local path, which R-23 and §9 put inside this task's definition of done. |
