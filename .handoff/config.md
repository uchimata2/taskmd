# Handoff config — taskmd

Read by the `handoff` skill. Plain Markdown, read by the agent — no parser.

**Keys, and short notes on what a key means or how to change it. No history and no log entries** —
those belong in tasks, commit messages or `docs/`. See `../CLAUDE.md` *Write the fact, not its
history*.

## Core keys

- `handoff_file`: .handoff/HANDOFF.md
- `tracker`: local-markdown-dir
- `project_docs`: CLAUDE.md, docs/ (start with `docs/SCOPE.md` — goal, requirements, non-goals)
- `reconcile_targets`: `tasks/`, `docs/**/*.md`, `CLAUDE.md`, `control/`, `.handoff/config.md` (this file)
- `language`: (omitted — match the source; this project is English)

> **Keep `reconcile_targets` derived: patterns, never an enumeration, and no depth limit.** Resolve
> the globs against the working tree at sweep time. A hand-kept list goes stale exactly when a home
> is added, which is the moment the sweep matters most — so name a directory such as `control/`
> rather than a file inside it, and write `docs/**/*.md` rather than `docs/*.md`. A gitignored folder
> is swept too, which does not make anything in it publishable. (T-073, 2026-08-09.)

## Tracker keys — `local-markdown-dir`

- `tracker_dir`: tasks/
- `tracker_id_prefix`: T-
- `tracker_template`: tasks/_task-template.md
- `tracker_closed_dir`: (not set — done tasks stay in `tasks/` so links keep resolving)
- `tracker_lint`: `./plugin/bin/taskmd check` (`.\plugin\bin\taskmd.cmd check` on Windows)

> **`tracker_lint` must be a command that starts on this machine**, which is why it is written by
> path — a lint that cannot start reports no drift and reads as a pass. It matters here because this
> project's index is *generated*: a task file can be correct while `tasks/README.md` is behind, and
> `check` is what makes that loud. (T-005, T-054, 2026-08-18.)
