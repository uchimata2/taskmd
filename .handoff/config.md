# Handoff config — taskmd

Read by the `handoff` skill. Plain Markdown, read by the agent — no parser.

## Core keys

- `handoff_file`: .handoff/HANDOFF.md
- `tracker`: local-markdown-dir
- `project_docs`: CLAUDE.md, docs/ (start with `docs/SCOPE.md` — goal, requirements, non-goals)
- `reconcile_targets`: `tasks/`, `docs/*.md`, `CLAUDE.md`, `control/`, `.handoff/config.md` (this file)
- `language`: (omitted — match the source; this project is English)

> **`reconcile_targets` is a pattern, not a list — keep it that way.** It previously named
> `docs/BRIEF.md` explicitly. `docs/SCOPE.md` was then added to the project and, being absent from
> the enumeration, was invisible to the reconcile sweep: a session updated it, wrote a handoff, and
> left it contradicting `CLAUDE.md` — caught by the maintainer, not the process. An enumerated list
> of homes is itself a second copy of "what the project docs are", and it goes stale exactly when a
> home is added, which is the moment the sweep matters most. Resolve the globs against the working
> tree at sweep time; never hand-maintain the membership.
>
> **`control/` is the directory, not a file in it** — added 2026-08-09 by T-073, for the same
> reason. That folder was outside every sweep because it is gitignored, and a sentence in it
> claiming a three-command CLI outlived its correction in two tracked files by four days. Naming
> `control/LOCAL-CONTEXT.md` would have been the enumeration this entry warns against; naming the
> folder keeps the membership derived. Being swept does not make anything in there publishable —
> the quarantine that file describes is unchanged.

## Tracker keys — `local-markdown-dir`

- `tracker_dir`: tasks/
- `tracker_id_prefix`: T-
- `tracker_template`: tasks/_task-template.md
- `tracker_closed_dir`: (not set — done tasks stay in `tasks/` so links keep resolving)

## Notes for whoever resumes

Start with `docs/SCOPE.md` — the goal, the numbered requirements (R-1…R-24) and the explicit
non-goals. `docs/BRIEF.md` holds the problem evidence, the carried lessons and the remaining open
questions. Tasks cite the requirements they serve, so coverage is derived rather than tabulated.

`plugin/skills/taskmd/docs/METHOD.md` is the working method itself. Since T-028 it is **tier 2** — loaded when task work
starts, not on every turn; `plugin/skills/taskmd/docs/method/` is tier 3, a file per phase. Tier 1 is whatever the harness
loads unasked, and **measured on 2026-08-08 that is `CLAUDE.md` plus the taskmd `description`**
(T-050) — the skill in `plugin/skills/taskmd/` is the loader that makes tier 2 real, and it was only served
once the plugin was installed rather than merely declared. **Since T-053 the plugin is the `plugin/`
subtree, not the repository** — the harness has no exclusion mechanism, so the boundary is the
directory, and what an install copies is exactly what is inside it. A served skill is still a
snapshot of that subtree, which is a property of installing rather than a defect.
Do not restate the method here or anywhere else; `CLAUDE.md` does not.

The schema question that used to block everything is answered (T-001), and the CLI it gated is built:
`./plugin/bin/taskmd {context,index,check,list}` (or `.\plugin\bin\taskmd.cmd`), proven by `tests/`.
Since T-083 that is the **same file** an adopter reaches by typing `taskmd`; only the lookup differs,
because this machine's shell snapshot drops the `PATH` entry the harness adds (T-054). So `SKILL.md`
naming the bare command is not an inconsistency with this file. Run `check` **and** `index` after
any edit to a task file — this project uses its own tool on itself, so a regression shows up
immediately, and the generated index goes stale silently until `index` is re-run (T-025).
`list --open --limit 1` answers "what next" by the project's own ordering rule, so it is not
something to work out by hand from the index.

Since T-011 the commands find the project by walking up from wherever they are run, so `--root` is
an override rather than something to remember; `plugin/skills/taskmd/taskmd.sh` and its `.ps1` twin
are thin launchers that find an interpreter and put the package on the path, and `plugin/bin/` holds
the two-line shims that reach them. A project may declare
one `after_write` command in its config, which taskmd runs after **its own** write — that is `index`,
never a task-file edit, so it cannot be what keeps the index fresh.

`plugin/skills/taskmd/docs/BINDING.md` is the backend contract and `plugin/skills/taskmd/docs/bindings/` holds the bindings. A binding is a
document, not code — read `plugin/skills/taskmd/docs/BINDING.md` §4 before writing or adopting one.

`reference/` holds proven prior art. It is **not** the plugin: it works, but it is written
around one project's assumptions. Read it for behaviour that is already verified, not for code
to copy wholesale.

This repository will be published. Nothing personal, client-specific or machine-specific goes
in — see `CLAUDE.md`.
