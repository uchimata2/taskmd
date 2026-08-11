# taskmd

taskmd keeps tasks as plain Markdown files, one file per task, and generates everything else from
them: the index, the far end of every link, what is blocked, and what to do next. It ships a
validator, needs no dependencies, and does not assume the work is software. Research, a course, a
deck and an ops runbook all fit.

## Using it

You talk to Claude, and the commands below are what it runs underneath.

| What you say | What happens |
| :--- | :--- |
| *What should I work on next?* | `taskmd list --open --limit 1` picks the task by the project's ordering rule, and `taskmd context` reads that one task. It never opens the rest of the folder. |
| *Add a task for drafting the onboarding email sequence* | The next id is taken, the template is copied, and the front-matter and any links are written in the same edit. Then the index is regenerated. |
| *Specify T-014* | The specify phase is worked and then it stops. One phase per request, so it stops there instead of carrying on into planning just because planning is next. |
| *Take T-014 through to done* | Asking for the whole lifecycle is what authorizes it: specify, plan, implement, review, in that order. |
| *Audit the handbook chapters and raise a task per finding* | An audit produces one umbrella task and one child task per finding. Nothing is fixed where it was found, which is what keeps a fix traceable. |

## The lifecycle

```mermaid
flowchart LR
    C([task created]) --> S[specify] --> P[plan] --> I[implement] --> R[review]
    R -->|every criterion met| D([done])
    R -->|criterion not met| F[fix task]
    F -.->|a task in its own right| S
```

Four phases, mandatory however small the task. Each one has a written exit criterion, and the
criterion is what counts as enough: `specify` ends when the acceptance
criteria are agreed, `plan` ends when every step names an output, `implement` ends when the outcome
has been checked by being used and the evidence is written down, and `review` ends when every
criterion is either met or carries a child task that will meet it.

Phase and status are separate. The phase says where the work reached; the status says whether it can
move. A task waiting on someone keeps the phase it reached and never moves backwards to record an
obstacle.

## What a task is

A file with front-matter for the facts and Markdown for the content:

```markdown
---
id: T-014
title: Draft the onboarding email sequence
type: deliverable
status: in_progress
phase: implement
parent: T-009
blocked_by: [T-011]
related: [T-006]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-04
updated: 2026-08-09
deliverables: [drafts/onboarding-1.md]
---

# T-014 ...
```

Nothing else is stored. **Store the forward edge, derive the rest**: T-011 says nothing about T-014,
and both ends of that link still show up on both tasks, because the tool computes the other end. The
same goes for children, for what a task blocks, for the index, and for which task comes next. Nobody
maintains a list by hand, so no list can be wrong.

The field names and their allowed values are configuration rather than code. A project keeps the
shipped schema or copies it to `.taskmd/config.md` and edits it there.

## The commands

<!-- taskmd:commands -->
| Command | What it does |
| :--- | :--- |
| `taskmd context <id>` | Everything needed to start that one task, and nothing else |
| `taskmd list --open --limit 1` | What to work on next, by the project's own ordering rule |
| `taskmd index` | Regenerates the task index |
| `taskmd check` | Validates ids, vocabularies, references, links, and your task templates |
<!-- taskmd:end-commands -->

They find the project by walking up from wherever they are run, so they work from a subdirectory
too. Pass `--root <path>` to override the project they find.

`list` filters on any link name and on **any field your schema names**: the ones it enumerates and
the ones it only shows, so a field the tool does not interpret is still one you can select on
(`taskmd list --status blocked`, `taskmd list --parent T-009`,
`taskmd list --work_package v0.2 --open`). `--json` turns it into a script's input. An unknown
field is an error listing what your project accepts; a value nothing carries is simply no rows.

Every command rejects an argument it does not understand *before* it reads or writes anything, so a
mistyped flag cannot come back as a successful run. `taskmd --help` prints the list of commands.

### Which documents `check` reads, and which pointers in them

**It reads the documents a clone of your project would receive.** Anything `.gitignore` excludes is
not read, and the count of what was skipped is printed on every run, so the exclusion cannot quietly
grow. A project with no git gets the whole tree read and is told so on the same line. This is the
question the command answers, and it is the same one the repository's own publishing checks ask.

The *targets* are asked two questions. Is the file here? If not, the link is broken. And would a
clone receive it? If not, the link resolves for you and 404s for everyone else, which is reported as
`IGNORED LINK` and is a different fact with a different fix. **Links to directories are exempt**,
because git lists files and never folders, so a folder is in nobody's clone by that test.

You can still say where a local-only file lives, such as a machine-specific note or a credentials
location, by naming it as a **path in prose** rather than as a link. A path in prose is not checked
either way (below). That is how this project's own quarantined material is referenced, in every one
of its documents. The rule was first written the other way and reversed on measurement in T-097:
across 151 published documents here it caught nothing that was deliberate, and twelve directory
links that were not the class at all.

**So the pointers inside your machine-local documents are validated by nothing, and that is a
decision rather than a gap nobody noticed.** If you keep working state a clone never sees, such as a
resumption note, a scratch plan or local context, its links are unchecked, and a dead one there is
found by the next person who follows it. It belongs to whatever writes that document: a tool that
generates one can resolve its own pointers at the moment it has them, and a hand-written one is
hand-checked. Three alternatives were each priced and rejected in T-098, which is also where to
reopen it: a flag, a config key naming paths to read anyway, and reading everything but demoting the
findings.

**Only Markdown link syntax counts as a pointer.** A path written as prose or inside a fenced block
is not checked, and a dead one will not be reported. That covers `docs/plan.md` in a sentence, and a
path a tool printed into output you pasted. If you are retiring your own link checker in favour of
this one, that is the coverage you give up. The decision is recorded in T-092 with what it cost,
measured on two projects rather than argued. Here: 683 such paths examined, 237 reported, none a
real defect. On the project that asked for the check: 481 examined, 31 dead, and 19 of those named
one file its own backlog had retired. Both corpora fail the same way, because a task record is a **dated statement,
not a promise**: it correctly describes a tree that has since moved, and a path checker cannot tell
the two apart. A validator that cries wolf gets ignored, which is worse than a narrow one.

## Install

There are two shapes. Both carry the method document and both backend bindings; the plugin adds the
manifest and the `bin/` entry point.

### As a plugin (the route to prefer)

```bash
claude plugin marketplace add uchimata2/taskmd
claude plugin install taskmd@taskmd
```

Claude Code puts an enabled plugin's `bin/` directory on `PATH`, so you type `taskmd`. Setting up a
project is one folder, and no command creates it for you:

```bash
mkdir tasks
taskmd check
```

```
OK - 0 task(s), 0 field value(s), 0 reference(s), 0 dependency edge(s), 0 declared output(s), 0 index file(s), 0 document(s), 0 link(s), 0 template(s), 0 vocabulary row(s)
Scope  every document read; no git here, so .gitignore was not consulted
structure and references only - it cannot tell you whether a spec or an outcome is good
```

**The summary carries what was examined, not only what passed**, so a scan that quietly shrinks is
visible, and a clean run on an empty project reads as the nothing it is rather than as an
endorsement. The `Scope` line is the same idea aimed at what was *skipped*, and it prints on a
failing run too, because an exclusion hides behind a problem as easily as behind a pass. Run outside
a project, `taskmd check` says so and exits 2 instead of reporting a clean tree it never opened.

**If you write your own config, `check` also tells you when the shipped default moves ahead of it.**
A config replaces the default rather than merging with it, so a copy taken today cannot see a value
added tomorrow. A real project raised work to fix a defect that had already been fixed upstream for
exactly this reason. One `CONFIG DRIFT` line names the row and the difference. It is advisory: the
exit status does not move, because pinning is a choice and not a fault. What counts as drift, and the
much longer list of differences that deliberately do *not*, is in the shipped config under *When this
file moves ahead of yours*.

### As a plain skill

Copy [`plugin/skills/taskmd/`](plugin/skills/taskmd) into your skills directory, so that it lands at
`~/.claude/skills/taskmd/`. That folder is self-contained: 21 files, no path to edit, and nothing
cited that it does not carry.

A copied skill gets no `PATH` entry, because that mechanism belongs to plugins. This shape therefore
runs the launcher inside the folder:

```bash
mkdir tasks
~/.claude/skills/taskmd/taskmd.sh check
```

```powershell
& ~\.claude\skills\taskmd\taskmd.ps1 check
```

Both print the same line as the plugin does. The two shapes name different commands on purpose.

## What it costs to start a task

Starting one task on this repository, with the tool and without it:

| Reading | Bytes |
| :--- | ---: |
| The task file, the project conventions, the generated index, and every task it links to | 156,901 |
| `taskmd context T-029` | 693 |

That is 0.44%, and it counts only the links the task stores. What waits *on* a task is derived and
written nowhere, so a session without the tool cannot know it without reading every task file, which
here is 1,274,604 bytes.

Two other things follow from deriving rather than storing. An inverse edge cannot go stale, because
there is no second copy to update. And a link recorded on either end is visible from both, so nobody
has to know which end owns it.

## What it is not

taskmd runs no server, daemon, watcher or database. It has no GUI and no web view, because the files
are the interface and the terminal is the view. It never touches the network. There is no query
language, no migration tooling, no notifications or scheduling, and no time tracking, velocity or
capacity. Two estimated fields exist for one purpose, ordering the listing, and either can be
switched off.

Nor is there an automatic fixer. Derived fields cannot go stale, because they are not stored.

## Backends

**Changing backend changes the binding, not the method.** A project that moves from local files to
GitHub Issues keeps the same lifecycle, the same edges and the same rules, and the binding absorbs
the backend's realities such as server-assigned ids or a missing soft-link field. The package ships
[`METHOD.md`](plugin/skills/taskmd/docs/METHOD.md), which names no backend, the contract a binding
implements ([`BINDING.md`](plugin/skills/taskmd/docs/BINDING.md)), and both bindings written against
it ([`docs/bindings/`](plugin/skills/taskmd/docs/bindings)): local Markdown, which is what the
commands above operate on, and GitHub Issues, which was walked on a live repository.

Each binding opens by stating the assumptions it makes about the adopting project, so you can see in
thirty seconds whether one of them is false for you.

## Scale and platforms

At its shipped id width taskmd handles up to 999 tasks with every command finishing in under a
second (measured at 999 tasks: `check`, the slowest, took 0.83 s), and a project that raises
`id_width` to go further pays 1.34 s for `check` at 2000 tasks and up to 3.9 s at 5000.

Run on Windows and on Linux, where a fresh clone regenerated a byte-identical index. macOS is
untested rather than unsupported: nothing in the tool is known to depend on the platform, and nobody
has run it there.

The implementation is standard-library Python, with bash and PowerShell launchers that hold no
logic. It needs no install step, no configuration and no dependencies.

## Documentation

| Read | For |
| :--- | :--- |
| [`METHOD.md`](plugin/skills/taskmd/docs/METHOD.md) | The working method: the lifecycle, the edge kinds, and what each phase has to produce |
| [`adopt.md`](plugin/skills/taskmd/adopt.md) | Setting up a project that has no tasks yet |
| [`config.md`](plugin/skills/taskmd/taskmd/defaults/config.md) | The schema, which is also the only description of what a config may hold |
| [`BINDING.md`](plugin/skills/taskmd/docs/BINDING.md) | Writing or adopting a binding for another backend |
| [`SCOPE.md`](docs/SCOPE.md) | The goal, the numbered requirements, and what is deliberately out |

## License

MIT. See [`LICENSE`](LICENSE).
