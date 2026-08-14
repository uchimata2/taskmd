---
id: T-099
title: Give an adopter a command that runs when the plugin's bin is not on PATH
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-054, T-055, T-067, T-083, T-085]
work_package: M2
owner: maintainer
business_value: critical
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/SKILL.md, plugin/skills/taskmd/adopt.md]
---

# T-099 — Give an adopter a command that runs when the plugin's bin is not on PATH

## 1. Specify

**Outcome**
An adopter whose harness does not put the plugin's `bin/` on `PATH` is told one invocation that
works, in the documents they already read — so they run taskmd instead of writing a launcher of
their own.

**Why this one**
Raised as **R-1** by the first adopting project (`control/LOCAL-CONTEXT.md`), which ranked it the
largest of seven divergences it hit. Every command in taskmd's documentation is `taskmd <verb>`. On
that project's machine the bare name resolves in neither shell, so the project wrote its own 60-line
launcher that finds the newest installed version and runs it. Every command in every task file, every
skill, every project document and every handoff there now reads that shim rather than the documented
command — across roughly forty task files, and **permanently**, because a task record is not rewritten
after the fact.

**This repository already knows the cause and shipped nothing for it.**
[T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 step 2 found it: the
harness does append every enabled plugin's `bin` to `PATH`, but it does so by writing one `export
PATH=` line into a shell snapshot, and on a machine with a long `PATH` that line is truncated
mid-value. Sourcing fails, the shell keeps its inherited `PATH`, and the directory is written
correctly and never loaded. T-054 recorded that as an upstream defect and deliberately raised no task
— correctly, since taskmd cannot fix the harness. **What it did not do is give the adopter a second
way in**, and the failure is not rare: it is the same machine class the maintainer develops on.

**The recommended fallback does not run as written.** R-1 proposes
`python <plugin>/skills/taskmd/taskmd/__main__.py <verb>` on the grounds that `__main__.py` already
exists and already walks up to find the project. Run:

```text
python <plugin>/skills/taskmd/taskmd/__main__.py check
ImportError: attempted relative import with no known parent package        exit 1
```

`__main__.py` is `from .cli import main` — a module inside a package, which is why `python -m taskmd`
works and naming the file does not. So this task cannot adopt the recommendation as stated; it has to
choose between making that form work and documenting a different one.

**Requirements served**
R-18 (`docs/SCOPE.md`) — *"the interpreter and the repository root are auto-discovered so a clone runs
unedited"*, which is unmet for anyone whose harness does not deliver the `PATH` entry. Also §1
*Invisibility*: a tool the agent cannot invoke is not invisible, it is absent.

**Scope**
- In: what `plugin/skills/taskmd/SKILL.md` and `plugin/skills/taskmd/adopt.md` say when the bare name
  is not found, and whether the shipped binding says it too.
- In: which fallback form is documented — the launchers by path
  (`plugin/skills/taskmd/taskmd.sh`, `.ps1`), `plugin/bin/taskmd` by path, or `python -m taskmd` with
  the package directory named — and whether one form covers both platforms.
- In: whether `__main__.py` gains a `sys.path` bootstrap so the obvious command works. It is one
  block, and the recommendation shows an adopter reaching for exactly that file.
- Out: fixing the harness. Not taskmd's, and T-054 settled that.
- Out: adding a command. The four exist; this is about reaching them.

**Inputs**
- [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) §3 steps 2–4, for the
  mechanism, the truncation and the two-audience decision (**D2**) that any answer here must not undo.
- `plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`.
- `plugin/skills/taskmd/taskmd/__main__.py`, `plugin/bin/taskmd`, `plugin/bin/taskmd.cmd`.

**Acceptance criteria**
- [ ] The failure is reproduced first, from a project that is neither this repository nor the plugin
      folder, with no plugin directory on `PATH` — per `CLAUDE.md` *Verifying*
- [ ] The documented fallback is then **run** from that same place, on both platforms, and its output
      recorded
- [ ] `SKILL.md` and `adopt.md` name the same fallback as each other, and say plainly which condition
      it is for
- [ ] The short form stays the primary instruction — an adopter whose `PATH` works types `taskmd`
- [ ] The suite still passes and `check` is clean on this repository

**Open questions**
- None. **Q1 — can an adopter discover the plugin path at all? — answered by measurement, 2026-08-10:
  they never need to.**

  The question assumed the reader has to fill in `<plugin>` from knowledge they do not have. They do
  not: **the harness names the skill's own directory when it serves the skill**, on the first line it
  hands the agent, and the launchers sit *in that directory*, beside `SKILL.md`. So the fallback is
  written relative to a path the reader has already been given — no marketplace layout, no version
  folder, no `${CLAUDE_PLUGIN_ROOT}`, which
  [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) D1 established does not
  substitute into a Markdown pointer anyway.

  Observed rather than reasoned: this session was handed that line on invoking the skill, and the
  installed copy holds `taskmd.sh` and `taskmd.ps1` next to `SKILL.md` and `adopt.md`. The path
  itself is a home directory and is quoted nowhere in this record.

  **It also settles which entry point the fallback names.** Not `bin/taskmd`, which lives one
  directory *out* of the skill and is absent from the copyable skill-folder shape this project also
  publishes — [T-083](T-083-make-the-skill-directory-self-contained.md) made that folder
  self-contained, and a fallback that climbs out of it would work in one shipped shape and not the
  other.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce the failure natively: a project outside this repository and outside the plugin folder, with the bare name looked up in both shells | Recorded transcript in §3 |
| 2 | Run each candidate fallback from that same place, against the **installed** copy — the launchers beside `SKILL.md`, on both platforms | Recorded transcript, and the shortlist reduced to one form per platform |
| 3 | Write the fallback into `SKILL.md`, at the point the bare name is first named | `plugin/skills/taskmd/SKILL.md` |
| 4 | Make `adopt.md` reach the same answer without carrying a second copy of it | `plugin/skills/taskmd/adopt.md` |
| 5 | Run the repository's own launchers by absolute path from the adopter project, so the artifact being shipped today is the one demonstrated | Recorded transcript |
| 6 | Suite, `index`, `check`, pre-publish check | Recorded output |

Step 1 is first because criterion 2 asks for the failure before the fix and it costs two commands.
Step 2 before step 3 because **the document cannot name a form that has not run** — this task exists
because R-1's recommended form was written without running it. Step 5 is separate from step 2 on
purpose: step 2 proves the mechanism on what an adopter actually has installed, step 5 proves it on
what this repository would ship next, and collapsing them would leave one of the two assumed.

**Shape decisions.**

**D1 — The fallback is the launcher beside `SKILL.md`, named relative to the skill directory the
harness announces.** Settled by Q1. *Rejected: `bin/taskmd` by path* — outside the skill folder, so
it does not exist in the copyable shape (T-083). *Rejected: `python -m taskmd` with the package
directory named* — it needs the adopter to supply a working interpreter, which is the exact job the
launchers exist to do, and this machine's `python3` is a Store stub that passes `command -v` and then
refuses to run.

**D2 — `__main__.py` does not gain a `sys.path` bootstrap, so R-1's literal suggestion is rejected
rather than enabled.** It is one block and it would make the recommended command work — and it would
create a second entry point that must stay working, reached by an interpreter the caller chose rather
than one the launcher proved. The failure it invites is silent: the Store stub answers `python3`,
exits 49, and reports nothing a reader can act on. The launchers already solve interpreter discovery,
and this project's rule is that a feature *requiring* a second copy of a solved problem is the wrong
feature.

**Planned outputs**
- `plugin/skills/taskmd/SKILL.md` — the fallback and the condition it is for
- `plugin/skills/taskmd/adopt.md` — reaching the same answer without restating it

## 3. Implement

### Step 1 — the failure, reproduced natively rather than simulated

This machine **is** the adopter condition: the plugin is installed and enabled, and the truncated
shell snapshot T-054 §3 step 2 diagnosed means its `bin/` never reaches a live `PATH`. So no
arrangement had to be staged. A scratch project was made outside this repository — a folder
containing only `tasks/` with one task in it, which is what an adopter has after `adopt.md` §1 — and
the name the documents tell them to type was looked up from both shells, working directory that
project:

```text
Get-Command taskmd     taskmd: not found
command -v taskmd      taskmd: not found
```

That is R-1 reproduced. Every command in `SKILL.md`, `adopt.md` and the shipped binding names
`taskmd`, and there is no third way in — which is what the first adopting project answered by writing
a launcher of its own.

### Step 2 — the fallback, run from the same place against the installed copy

The installed skill directory holds `SKILL.md`, `adopt.md`, `taskmd.sh` and `taskmd.ps1` — the
launchers are beside the document that names them, which is D1's whole mechanism. Working directory
still the adopter project, launcher named by absolute path:

```text
sh <skill dir>/taskmd.sh check                        OK - 1 task(s), vocabulary valid, ...   exit 0
pwsh -File <skill dir>/taskmd.ps1 check               OK - 1 task(s), vocabulary valid, ...   exit 0
powershell -File <skill dir>/taskmd.ps1 list --open --limit 1
                                    T-001  proposed  -  specify  Write the quarterly summary  exit 0
```

Three shells, including Windows PowerShell 5.1, which is the one T-054 found breaking the launcher's
interpreter probe and the one a stock Windows machine has. The paths are elided: they are under a
home directory, which is the class `CLAUDE.md`'s pre-publish check exists to catch.

**A second fact fell out of the install directory, and it is not this task's to fix.** The cache
holds **two** installed versions side by side. That is why the first adopting project's shim had to
"find the newest installed version" — a fallback naming the skill directory the harness announced
does not have that problem, because the harness announces the one it is serving. Recorded here
because it is the reason R-1's author reached for a version-scanning launcher rather than a path.

### Steps 3–4 — where it is written, and where it is only pointed at

`SKILL.md` carries the fallback, immediately after the paragraph that promises `taskmd` runs from any
directory — the sentence a reader is holding when the promise fails for them. It names the condition
(the harness did not put the plugin's `bin/` on `PATH`, a fact about the machine rather than the
project), gives one form per platform, and says it covers every `taskmd <verb>` in the documents this
skill points at, so the shipped binding needs no second copy for its *after any write* step.

`adopt.md` §5 **points** at it rather than repeating it. That is the criterion "name the same
fallback as each other" met by construction instead of by discipline: two copies can drift, and a
pointer cannot. It is also R-22 — the skill points where it would otherwise restate.

### Step 5 — the same demonstration against what this repository ships today

Step 2 ran the installed 0.1.1 copy, which is what an adopter has. This repository is ahead of it, so
the same two commands were run again from the adopter project against **this tree's** launchers:

```text
sh <repo>/plugin/skills/taskmd/taskmd.sh check
pwsh -File <repo>/plugin/skills/taskmd/taskmd.ps1 check
  OK - 1 task(s), 5 field value(s), 0 reference(s), 0 dependency edge(s), 0 declared output(s),
       0 index file(s), 1 document(s), 0 link(s)
  Scope  every document read; no git here, so .gitignore was not consulted        exit 0, both
```

Same answer from both. **And it is visibly not the installed build**: 0.1.1 answers step 2's command
with the one-line `OK - 1 task(s), vocabulary valid, references resolve, no broken links`, while this
tree answers with T-095's itemised form. The two are distinguishable from their output, so step 5
demonstrably ran what it claims to have run rather than resolving back to the copy step 2 used.

### Step 6 — the suite and this repository

```text
Ran 147 tests in 6.097s                                                                      OK
OK - 105 task(s), 525 field value(s), 320 reference(s), 22 dependency edge(s), 129 declared
     output(s), 1 index file(s), 133 document(s), 994 link(s)
```

Run from bash, per `control/LOCAL-CONTEXT.md`: `tests/test_runtime.py` spawns the launchers, and
spawning them from PowerShell eats the backslashes in the path it passes.

**Decisions & assumptions**

- **D2 stands: R-1's literal recommendation is rejected, and the task says so rather than quietly
  shipping something else.** — The report asked for `python <plugin>/…/__main__.py <verb>` on the
  argument that it needs no code. It needs no code *and does not run*; making it run means a second
  entry point reached by an unproven interpreter. The adopter gets a working answer to the question
  they asked, not the answer they proposed. — 2026-08-10
- **The fallback is documented, not automated.** — Nothing detects that `bin/` is missing and
  switches; the reader does, on the one failure it produces. A tool that silently re-routed would
  hide a harness defect the adopter may want to fix. — 2026-08-10
- **Assumption, recorded as one: the harness announces the skill directory to every agent it serves
  the skill to.** — Observed in this session and in the install layout. It is the whole mechanism, so
  if a harness does not do it, the fallback degrades to "find the plugin cache" — which is where an
  adopter already was. The work survives being wrong about it. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/SKILL.md` — the fallback, the condition, one form per platform
- `plugin/skills/taskmd/adopt.md` — §5 points at it

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The failure is reproduced first, from a project that is neither this repository nor the plugin folder, with no plugin directory on `PATH` | met | §3 step 1, taken before any file was edited. Not staged — this machine is natively in that state, for the reason T-054 §3 step 2 diagnosed. Both shells, transcript recorded. |
| The documented fallback is then **run** from that same place, on both platforms, and its output recorded | met | §3 step 2 — three shells including Windows PowerShell 5.1 — and §3 step 5 again against this tree's launchers rather than only the installed build. |
| `SKILL.md` and `adopt.md` name the same fallback as each other, and say plainly which condition it is for | met | Met by `adopt.md` **pointing** rather than naming, which is stronger than the criterion asked: two copies can drift and a pointer cannot. Said plainly here because it is a deliberate reading of the criterion rather than a literal one. |
| The short form stays the primary instruction — an adopter whose `PATH` works types `taskmd` | met | The `Run first` block is unchanged; the fallback follows it and opens on the condition, so a reader whose commands work skips it. |
| The suite still passes and `check` is clean on this repository | met | §3 step 6: `Ran 147 tests … OK`, and `check` OK on 105 tasks. The pre-publish check was run after this record was written, per `CLAUDE.md`, and is reported in the log row below rather than here. |

**What this does not cover.** The harness's own `PATH` append is still unexercised on this machine
and cannot be — that is T-054's finding, unchanged, and
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) already carries
the check on a machine that has never held the plugin. No new task for it.

**Child fix tasks raised**
- none. The two installed versions found in §3 step 2 are a fact about the install route, already
  recorded in agent memory and visible to
  [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md); nothing about
  it is taskmd's to change.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | (no change, closed) | **The `→ proposed` row below was damaged by a later edit and is restored here.** The commit that closed this task removed its leading two cells and the first nine words of its note, and what was left became a fourth cell on the row above — which has a three-column header, so Markdown dropped it. The text was in the file and rendered nowhere from 2026-08-10, and nothing this project runs could say so: `check` was clean, the suite was green, and the pre-publish gate printed its count and no lines. Found on 2026-08-15 by a scan prompted by an adopter report, which counted every table row in the repository against its header and returned this one row out of 2,797. The row itself is put back as it stood at `d56486f`, unmarked, because it is this task's account of 2026-08-10 and marking it would edit what the record says about the past (METHOD §1.5). This row is the annotation instead. [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md) is the repair; [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) is whether anything catches the next one. |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. Criterion 3 is met by `adopt.md` pointing at `SKILL.md` rather than carrying its own copy of the fallback — a deliberate reading of "name the same fallback as each other", stated in the review row because two copies can drift and a pointer cannot. Nothing new is raised: the harness's own `PATH` append is still unexercised on this machine, which is T-054's finding unchanged and already carried by T-085's criteria. `deliverables` names the two documents. Pre-publish check run last, after this record was written, per `CLAUDE.md` — **189 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. No path from step 1, 2 or 5 is quoted anywhere in this record; they are under a home directory or a temp directory, which is the class that check exists to catch. |
| 2026-08-10 | → in_progress | All six steps taken. Step 1 reproduced R-1 **natively rather than by staging it** — this machine already is the adopter condition, since T-054 §3 step 2 found its shell snapshot truncated, so `taskmd` resolves in neither shell from a scratch project outside this repository. Step 2 ran the fallback from that same project against the **installed** copy, in three shells including Windows PowerShell 5.1. Step 5 ran it again against this tree's launchers, and the two builds are distinguishable from their output — 0.1.1 answers with the old one-line `OK`, this tree with T-095's itemised form — so step 5 provably exercised what it claims. **D2 was carried out rather than quietly dropped**: R-1's literal recommendation is rejected, because making `python <plugin>/…/__main__.py` work means a second entry point reached by an interpreter nobody proved, which is the job the launchers exist to do and the failure the Store-stub `python3` produces silently. One fact fell out of the install directory and is recorded rather than actioned: the cache holds two installed versions side by side, which is why the reporting project's shim had to scan for the newest — a fallback naming the directory the harness announced does not have that problem. Suite `Ran 147 tests … OK` from bash, `check` OK on 105 tasks. |
| 2026-08-10 | → planned | Plan written, and §1's open question **settled by measurement rather than by asking**: an adopter never needs to discover the plugin path, because the harness names the skill's own directory when it serves the skill, and the launchers sit in that directory beside `SKILL.md`. That also chose the entry point — the launcher rather than `bin/taskmd`, which lives outside the skill folder and is absent from the copyable skill-folder shape T-083 made self-contained. Step 2 is ordered before step 3 because the document must not name a form nobody ran, which is precisely how R-1 came to recommend a command that does not work. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10**, in the same request that authorised the milestone amendment: *"move on in the suggested order. Full lifecycle."* It covers this task and [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md), the two named in that reply's next steps, and **it does not generalise** — the next task starts at one phase per request again. Recorded here because there is nowhere else for it yet, which is the whole of [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md): this row is that task's first live specimen rather than a hypothetical. |
| 2026-08-10 | → proposed | Raised as R-1 from the first adopting project's recommendations, which ranked it the largest of its seven divergences. `critical` because the documented command failing is the adoption path not working, which is the same reason T-054 carried that value, and because the cost is permanent — a shim written into forty task records is not retracted later. `s` because nothing new is built; the entry points exist and this is what the documents say when the harness does not deliver the `PATH` entry. Two facts recorded here rather than left for `specify` to rediscover: the cause is known and is upstream (T-054 §3 step 2, a truncated shell-snapshot `PATH` line), and **the recommended command does not run** — `__main__.py` is a package module, so naming the file raises `ImportError: attempted relative import with no known parent package`. Verified by running it. |
