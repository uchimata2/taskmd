# taskmd — working conventions

Read this before doing anything in this folder.

## What this is

A publishable Claude Code plugin: **Markdown files as a task tracker**, with a generated index,
real dependency links, and a validator. Extracted from a working implementation that ran a real
consulting project — see `reference/` for the code that already works and `docs/BRIEF.md` for
what has to change to make it general.

**Read in this order:** [`docs/SCOPE.md`](docs/SCOPE.md) — the goal, the numbered requirements and
what is explicitly **out** of scope — then [`docs/BRIEF.md`](docs/BRIEF.md) for the problem
evidence and the measured prior art behind them. `tasks/README.md` is the generated backlog.

**Status: published** (T-006), at `github.com/uchimata2/taskmd`, in both shapes — the marketplace
plugin and the copyable skill folder. `README.md` is the front door and the four commands are listed
there. **Run them here as `./plugin/bin/taskmd <cmd>`, or `.\plugin\bin\taskmd.cmd <cmd>` on
Windows**: the shipped entry point, invoked by path because this machine's shell snapshot drops the
`PATH` entry an adopter gets (T-054). It finds the project by walking up from where it is run, and a
project may declare one `after_write` command that taskmd runs and reports on.

`check` has been shown failing on **every** class it claims — one deliberately-broken fixture each,
so the set is `tests/fixtures/broken-*` and not a count written here. It does **not** yet notice a
generated index that has gone stale (T-025). The backend contract exists
([`plugin/skills/taskmd/docs/BINDING.md`](plugin/skills/taskmd/docs/BINDING.md), T-009) and **both bindings** are written
([`plugin/skills/taskmd/docs/bindings/`](plugin/skills/taskmd/docs/bindings/)) — so storage-neutrality is no longer a claim about one backend
plus a worked example about another: the GitHub binding (T-010) was proven by being walked on a live
repository, and the method needed no change to carry it. The skill exists (`plugin/skills/taskmd/`, T-003)
and declaring it from this tree turned out not to be the same as installing it (T-050). Installed, it
is **served**: a session here is handed its `description` unasked, and the body, the method and the
phase file each arrive at their own later moment.

## The one design rule

**Store the forward edge; derive the rest.** Stated in full — including what the word *requires*
below does and does not forbid — in [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) §4.

In this repository it comes out as: a task file's front-matter is the only place a fact about that
task is written, and children, dependents, the index and the deliverable map are all computed. Check
every design decision here against it — a feature that *requires* writing the same fact twice is the
wrong feature.

## Working method

This plugin manages tasks, so it uses its own method on itself. **The method has one home:
[`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md)** — the lifecycle and its exit criteria, the edge kinds, the
audit mechanism, and how the agent is expected to behave. It is not restated here; if you find it
written out somewhere else, that copy is the defect.

**Three tiers, and only the first is budgeted.** Tier 1 is whatever the harness loads unasked —
a property of the tree rather than a list to maintain, so a skill's `description` joins it the moment
the harness actually **serves** that skill, without this paragraph being edited — declaring one does
not, which is what T-050 measured. Re-measured after the install (2026-08-08), tier 1 is this file
**plus the taskmd `description`** — the rule above unedited, the membership moved by the install
alone, which is the property it was written to have. Tier 2 is
[`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md), on starting task work; tier 3 is [`plugin/skills/taskmd/docs/method/`](plugin/skills/taskmd/docs/method/),
a file per phase. **Tier 1 stays smaller than `reference/TASK-WORKFLOW.md`**, the flat
single-document alternative, because a first tier costing more than the flat version has inverted the
point of splitting it at all. No number is written here — both sides are counted from the tree, in
**characters**, which is what a turn is billed for. Membership is read from the tree too, so a second
served skill joins the count with nothing here edited:

```bash
{ cat CLAUDE.md; sed -n 's/^description: //p' plugin/skills/*/SKILL.md; } | wc -c; wc -c < reference/TASK-WORKFLOW.md
```

**It does not pass, and it never did** — the retired check counted lines and read only this file, so
it missed the `description` and flattered a dense one besides (T-063). What comes out is T-047's,
which also owes this tier METHOD §3.1 and §3.3. Tiers 2 and 3 carry no budget — they are not paid on
every turn, and R-21 with METHOD §7 governs them instead.

What this project adds on top, because the method is deliberately storage-agnostic:

- Task files live in `tasks/`, created from `tasks/_task-template.md` — beside the task it becomes,
  not under it, so links survive the copy (T-076).
- The field names and their allowed values are the schema — `plugin/skills/taskmd/taskmd/defaults/config.md`.
- The index is **generated**, never hand-edited.
- When a task is `done` is [`plugin/skills/taskmd/docs/METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) §1 rule 5; which artifact satisfies
  each of its conditions here is in
  [`plugin/skills/taskmd/docs/bindings/local-markdown.md`](plugin/skills/taskmd/docs/bindings/local-markdown.md).

`reference/TASK-WORKFLOW.md` is the pre-split standard from one real project — evidence of what
worked, not the standard. It hard-codes a folder contract, a work-package vocabulary and specific
commands, which is precisely what `plugin/skills/taskmd/docs/METHOD.md` had to leave behind.

## Publishing constraints

This repository goes to GitHub. Everything written here must be:

- **Free of personal, client and machine data.** No real names, no absolute local paths, no
  drive letters, no hostnames. Write `<project>/tasks/` not a real path. Where a real identity is
  genuinely load-bearing evidence, it goes in `control/LOCAL-CONTEXT.md` — which is gitignored — and
  the tracked tree refers to it by the label that file defines. **Run the check below before
  publishing**; it is a grep because a leak check is not one of the things the CLI does — settled in
  T-013 under `docs/SCOPE.md` non-goal 11, which still excludes it after its 2026-08-05 amendment.
- **Out-of-the-box.** Someone who clones it must be able to run it with no path editing.
  Resolve paths relative to the repository root, not the working directory.
- **Dependency-free.** Python standard library only. A tracker that needs `pip install` before it
  can list your tasks is a tracker people abandon.
- **Cross-platform.** Windows, macOS, Linux. Write files with an explicit `newline="\n"` —
  Python's default text mode rewrites every `\n` on Windows and breaks byte-for-byte comparison.
  Console output should survive a cp1252 terminal: reconfigure stdout to UTF-8 at startup.
- **Humanized, if a stranger reads it before installing.** The rule, what it covers and the
  exception it carries: [`docs/PUBLISHING.md`](docs/PUBLISHING.md) (T-079).

### The pre-publish check

Run over every file a push would send. It must print nothing; every hit is either a leak or a label
that needs adding to `control/LOCAL-CONTEXT.md`.

```bash
( cd "$(git rev-parse --show-toplevel)" && git ls-files -z --cached --others --exclude-standard ':!tests/fixtures/leak-check/' | xargs -0 grep -nIE '\b[A-Za-z]:[\\/][A-Za-z0-9._-]+[\\/]|/(home|Users)/|[\\]{2}[A-Za-z0-9._-]+[\\]|[0-9]{1,3}(\.[0-9]{1,3}){3}' )
```

Four classes: Windows drive paths, home directories, UNC paths, IP addresses. `git ls-files` is what
makes it meaningful, but **only with those three flags**: on its own it lists what git already
*tracks*, which silently omits every file the session just created. `--cached --others
--exclude-standard` is tracked files **plus** untracked-but-not-ignored ones — so it sees exactly
what a push would send, and anything gitignored is still out of scope by construction. Do not
shorten it to `-co`: the point of the line is that a reader can see what it covers. The omission was
silent for as long as it existed — a check that reads none of the files it was aimed at prints
nothing, which is also what success looks like (T-034, which measured it and proved the fix by
making it catch a leak in an untracked file).

**The `cd` is not decoration.** `ls-files` lists the subtree you are standing in, and the exclusion
is a pathspec resolved against the same place — so run from a subdirectory the unanchored command
read a quarter of the tree *and* printed its own fixture as five leaks. Both halves are invisible:
the alarm hides the under-scan, and anchoring only the exclusion silences the alarm while leaving the
blindness (T-080, which measured both and rejected that smaller fix for exactly this reason). Judge a
run by the file count, not by its silence.

**Run it last, after the task record is written — not before.** The check reads files, so it cannot
see one that does not exist yet, and the text most likely to trip it is the write-up of a task
*about* the check: quoting a matched line into a task record re-creates the leak. This has now
happened twice, in T-013 and again in T-018 while fixing T-013. Describe the result and point at the
fixture; never paste the lines.

**The excluded path is the check's own fixture, and dropping the exclusion is how the check is
proven.** `tests/fixtures/leak-check/samples.txt` holds nine deliberately-fabricated lines: five that
must be caught, one per class, and four safe forms that must not be. So there are two runs of one
command — with the exclusion, the tree must print **nothing**; without it, the output must be
**exactly those five lines and nothing else**. The second run is what a clean tree can never prove
on its own (*Verifying*, below), and keeping it in the same command is what stops the proof drifting
from the check. The exclusion is one pathspec, not a second contract: any leak outside that one file
is still caught, and the file's only content is the fixture.

**Three limits, all deliberate.** A drive path is only matched with **two or more segments** after the
letter; a single-segment one is let through, because that form collides with ordinary text such as a
`d:\n` escape inside a code string — and a check that cries wolf gets ignored, which is worse than a
narrow one. (Do not write an example drive path here to illustrate that: the check reads this file
too, and an illustration is indistinguishable from a leak.) Second, **a dotted four-part version
number fires the IP branch** — a kernel or build string in a task record will trip it, and nothing
has leaked when it does; elide a component and move on. Requiring valid octets does not fix it,
because a version's parts are under 256 too, and it triples the branch (T-058). And third, **a
real name or a client project is not mechanically detectable at all**: that half is the label
discipline above, and it holds only if every new identity goes into `control/LOCAL-CONTEXT.md`
rather than into a task.

The pattern was verified by being made to fail (per *Verifying*, below), and the fixture that did it
is the one named above rather than a transcript pasted into a task — which is what T-018 was raised
to fix, after the pasted copy left a real drive path in the tracked tree and made the documented
"prints nothing" unreachable. Two earlier drafts were wrong: one matched `http://` and a `d:\n`
escape, and one ended a branch in `\\`, which grep read as an escaped `|` and which silently
swallowed the entire IP branch. Both bugs were invisible on a clean tree.

## Verifying

Claims about behaviour are verified by **running the thing on a real case**, never by reading the
code or its documentation. In particular, a validator is only proven when it has been shown to
**fail** on a case it is supposed to catch — a clean-tree pass proves nothing.

State results as the actual command output, not as "works".
