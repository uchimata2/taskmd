# Handoff config — taskmd

Read by the `handoff` skill. Plain Markdown, read by the agent — no parser.

## Core keys

- `handoff_file`: .handoff/HANDOFF.md
- `tracker`: local-markdown-dir
- `project_docs`: CLAUDE.md, docs/ (start with `docs/SCOPE.md` — goal, requirements, non-goals)
- `reconcile_targets`: `tasks/`, `docs/*.md`, `CLAUDE.md`, `.handoff/config.md` (this file)
- `language`: (omitted — match the source; this project is English)

> **`reconcile_targets` is a pattern, not a list — keep it that way.** It previously named
> `docs/BRIEF.md` explicitly. `docs/SCOPE.md` was then added to the project and, being absent from
> the enumeration, was invisible to the reconcile sweep: a session updated it, wrote a handoff, and
> left it contradicting `CLAUDE.md` — caught by the maintainer, not the process. An enumerated list
> of homes is itself a second copy of "what the project docs are", and it goes stale exactly when a
> home is added, which is the moment the sweep matters most. Resolve the globs against the working
> tree at sweep time; never hand-maintain the membership.

## Tracker keys — `local-markdown-dir`

- `tracker_dir`: tasks/
- `tracker_id_prefix`: T-
- `tracker_template`: tasks/_templates/task-template.md
- `tracker_closed_dir`: (not set — done tasks stay in `tasks/` so links keep resolving)

## Notes for whoever resumes

Start with `docs/SCOPE.md` — the goal, the numbered requirements (R-1…R-24) and the explicit
non-goals. `docs/BRIEF.md` holds the problem evidence, the carried lessons and the remaining open
questions. Tasks cite the requirements they serve, so coverage is derived rather than tabulated.

`docs/METHOD.md` is the working method itself. Since T-028 it is **tier 2** — loaded when task work
starts, not on every turn; tier 1 is `CLAUDE.md` alone, and `docs/method/` is tier 3, a file per
phase. `CLAUDE.md` no longer restates the method and neither should anything else.

The schema question that used to block everything is answered (T-001), and the CLI it gated is built:
`python -m taskmd {context,index,check,list}`, proven by `tests/`. Run `check` **and** `index` after
any edit to a task file — this project uses its own tool on itself, so a regression shows up
immediately, and the generated index goes stale silently until `index` is re-run (T-025).
`list --open --limit 1` answers "what next" by the project's own ordering rule, so it is not
something to work out by hand from the index.

`docs/BINDING.md` is the backend contract and `docs/bindings/` holds the bindings. A binding is a
document, not code — read `docs/BINDING.md` §4 before writing or adopting one.

`reference/` holds proven prior art. It is **not** the plugin: it works, but it is written
around one project's assumptions. Read it for behaviour that is already verified, not for code
to copy wholesale.

This repository will be published. Nothing personal, client-specific or machine-specific goes
in — see `CLAUDE.md`.
