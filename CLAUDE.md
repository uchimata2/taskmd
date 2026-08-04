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

**Status:** the schema layer exists (`taskmd/`) and is proven by `tests/test_schema.py`. The CLI,
the method document and the bindings are not written yet.

## The one design rule

**Store the forward edge; derive the rest.**

A task file's front-matter is the only place a fact about that task is written. Children,
dependents, the index, the deliverable map — all computed. Facts that are computed cannot drift
from facts that are stored, so no validator is needed to keep them honest.

Every design decision in this plugin should be checked against that rule. If a feature *requires*
writing the same fact twice, it is the wrong feature.

Note the word "requires". A link written on one task is visible from both ends because the inverse
is derived — so one write is always sufficient. Writing the other side as well is permitted and
collapses to a single entry; a two-way reference living in two places is the nature of references,
not drift. The rule forbids a design that **compels** the second write, not a user who makes one.

## Working method

This plugin manages tasks, so it uses its own method on itself:

1. **No work without a task file** in `tasks/`, from `tasks/_templates/task-template.md`.
2. Lifecycle: `specify → plan → implement → review`.
3. A task is `done` only when its deliverables exist, its log is current, and the validator
   passes.
4. The index is **generated**, never hand-edited.

The full standard — and the backend-neutral method the plugin will ship — is **not written yet**;
[T-008](tasks/T-008-write-the-backend-neutral-method-document.md) owns it. Until it exists, the four
rules above are the whole method, and `reference/TASK-WORKFLOW.md` shows how they were applied on
one real project (evidence, not the standard: it names that project's tools and vocabulary).

## Publishing constraints

This repository goes to GitHub. Everything written here must be:

- **Free of personal, client and machine data.** No real names, no absolute local paths, no
  drive letters, no hostnames. Write `<project>/tasks/` not a real path.
- **Out-of-the-box.** Someone who clones it must be able to run it with no path editing.
  Resolve paths relative to the repository root, not the working directory.
- **Dependency-free.** Python standard library only. A tracker that needs `pip install` before it
  can list your tasks is a tracker people abandon.
- **Cross-platform.** Windows, macOS, Linux. Write files with an explicit `newline="\n"` —
  Python's default text mode rewrites every `\n` on Windows and breaks byte-for-byte comparison.
  Console output should survive a cp1252 terminal: reconfigure stdout to UTF-8 at startup.

## Verifying

Claims about behaviour are verified by **running the thing on a real case**, never by reading the
code or its documentation. In particular, a validator is only proven when it has been shown to
**fail** on a case it is supposed to catch — a clean-tree pass proves nothing.

State results as the actual command output, not as "works".
