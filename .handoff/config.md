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

**Published on 2026-08-09** at `github.com/uchimata2/taskmd`, in both shapes. **The current release
is `v0.5.0`**, tagged and released on 2026-08-11, and the manifest reads `0.5.0`.

**Version bumps and milestone labels are two sequences, and they have already come apart once.** A
bump exists because `claude plugin update` compares version strings, so a directory install whose
manifest never changes reports "already at the latest version" and keeps serving the snapshot it
copied. Some bumps are taken mid-milestone to get fixes out: `v0.2.0` and `v0.3.0` are those, and
neither is a milestone. The standing policy is to spend one bump on a batch rather than on a single
fix, which the maintainer confirmed on 2026-08-10 against the strongest argument available — an
adopter updating for something unrelated meets a new failure class.

**Milestone labels are `M1`…`M6` and cannot be read as versions.** They were `v0.1`…`v0.6` until
2026-08-12, when T-136 renamed them: each one resolved to a real tag of the same number that meant
something else, and a mapping table was keeping the two spaces legible at the cost of writing one
fact twice. There is nothing left to translate, so nothing here to read first — the digit says which
release the work is scheduled into, and `tasks/README.md` names the two closed labels that are not
that. The definition of done (`docs/SCOPE.md` §9) is closed. What is left is grouped into **M5 and
M6**, whose purpose is in `tasks/README.md` and whose membership is each task's `work_package` — do
not maintain a list of that anywhere. Both close when every task in them closes; neither has an
enumerated exit criterion, and the reason is in T-128.

**A release is not the last step of a release.** T-085 verifies the published artifact from a clean
machine and was `blocked_by` the release task, so M5 was not complete when it was tagged. `0.4.0`
shipped with nothing checking it from outside; `0.5.0` did not. The ordering held: `0.5.0` was tagged
and then installed from its own tag onto a profile that had never held any of this. Half of that is
proven and half is not, and which half is in T-085, not here.

Start with `docs/SCOPE.md` — the goal, the numbered requirements (R-1…R-24) and the explicit
non-goals. `docs/BRIEF.md` holds the problem evidence, the carried lessons and the remaining open
questions. Tasks cite the requirements they serve, so coverage is derived rather than tabulated.

**The plugin now has users outside this repository** — four projects as of 2026-08-09, labelled in
`control/LOCAL-CONTEXT.md`; three run it, and the fourth was assessed against the GitHub binding and
does not adopt it. Expect an adopter to find in a day what this repository's habits had hidden for a
week: route what they report into tasks, not into notes, and treat a migration report as evidence
rather than as a feature request. **A written report is worth working straight through.** The first
adopting project delivered seven recommendations on 2026-08-10; all seven closed the same day, they
raised two further tasks between them, and two of the seven turned out to rest on premises that were
wrong in instructive ways — the command they recommended did not run, and the method they said was
silent had answered them one tier down. So read a report as a set of leads to verify, never as
findings to implement.

`plugin/skills/taskmd/docs/METHOD.md` is the working method itself. Since T-028 it is **tier 2** — loaded when task work
starts, not on every turn; `plugin/skills/taskmd/docs/method/` is tier 3, a file per phase. Tier 1 is whatever the harness
loads unasked, and **measured on 2026-08-08 that is `CLAUDE.md` plus the taskmd `description`**
(T-050) — the skill in `plugin/skills/taskmd/` is the loader that makes tier 2 real, and it was only served
once the plugin was installed rather than merely declared. **Since T-053 the plugin is the `plugin/`
subtree, not the repository** — the harness has no exclusion mechanism, so the boundary is the
directory, and what an install copies is exactly what is inside it. A served skill is still a
snapshot of that subtree, which is a property of installing rather than a defect. **Since T-083
`plugin/skills/taskmd/` is self-contained**: the docs, the package and the launchers live inside it,
so copying that one folder is a working skill, and `plugin/bin/` holds only the two shims that must
sit at the plugin root for the `PATH` mechanism.
Do not restate the method here or anywhere else. `CLAUDE.md` carries exactly two of its rules —
METHOD §3.1 and §3.3, verbatim, since T-047 — and that is not an exception to the rule but the only
way to obey it: those two bind *before* the method is loaded, so tier 2 cannot be their home. Every
other part of the method is pointed at, never copied.

The schema question that used to block everything is answered (T-001), and the CLI it gated is built:
`./plugin/bin/taskmd {context,index,check,list}` (or `.\plugin\bin\taskmd.cmd`), proven by `tests/`.
Since T-083 that is the **same file** an adopter reaches by typing `taskmd`; only the lookup differs,
because this machine's shell snapshot drops the `PATH` entry the harness adds (T-054). So `SKILL.md`
naming the bare command is not an inconsistency with this file. Run `check` **and** `index` after
any edit to a task file — this project uses its own tool on itself, so a regression shows up
immediately. Since T-025 a forgotten `index` is no longer silent: `check` reports the index as stale
and names the command, so the two commands back each other up rather than one covering for the other.
`list --open --limit 1` answers "what next" by the project's own ordering rule, so it is not
something to work out by hand from the index. Since T-087 `list` also filters on any field the
schema *names* rather than only the ones it enumerates, so `list --work_package M2 --open` is how
a release's membership is read — there is no list of it to maintain anywhere, which is the point.

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
