# Handoff config — taskmd

Read by the `handoff` skill. Plain Markdown, read by the agent — no parser.

## Core keys

- `handoff_file`: .handoff/HANDOFF.md
- `tracker`: local-markdown-dir
- `project_docs`: CLAUDE.md, docs/ (start with `docs/SCOPE.md` — goal, requirements, non-goals)
- `reconcile_targets`: `tasks/`, `docs/**/*.md`, `CLAUDE.md`, `control/`, `.handoff/config.md` (this file)
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
>
> **`docs/**/*.md`, not `docs/*.md`** — changed 2026-08-15, and it is the same defect a third time.
> A single `*` stops at the top level, so the moment a session put documents in `docs/audits/` the
> sweep could not see them: the glob was derived-looking and was still enumerating one directory.
> A depth limit is an enumeration of folders in the way the paragraph above is an enumeration of
> files, and it fails at the same moment — when a home is added.

## Tracker keys — `local-markdown-dir`

- `tracker_dir`: tasks/
- `tracker_id_prefix`: T-
- `tracker_template`: tasks/_task-template.md
- `tracker_closed_dir`: (not set — done tasks stay in `tasks/` so links keep resolving)
- `tracker_lint`: `./plugin/bin/taskmd check` (`.\plugin\bin\taskmd.cmd check` on Windows)

> **`tracker_lint` was missing until 2026-08-18**, found by T-005 testing its own recipe against this
> file. This project has a *generated* central index, which is the one topology the handoff binding
> warns goes stale silently — the task file is right, `tasks/README.md` is behind, and nothing
> complains. The hook is what makes that loud: `check` exits 1 and names `index` as the fix, measured
> on a real stale index the same day. It is written by path here for the reason T-054 records, and
> the recipe in `plugin/skills/taskmd/docs/HANDOFF.md` says an adopter writes whichever form starts
> on their machine — a lint that cannot start reports no drift and reads as a pass.

## Notes for whoever resumes

**Published on 2026-08-09** at `github.com/uchimata2/taskmd`, in both shapes. **The current release
is `v0.6.0`**, tagged and released on 2026-08-23, and the manifest reads `0.6.0`. It is the first
release whose note was written to `docs/PUBLISHING.md` §7's rule, and the rule stopped it: 78 closed
tasks in the milestone had never been judged for the note. What that cost and what it caught is in
[T-182](../tasks/T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) and
[T-242](../tasks/T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md),
not here.

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
that. The definition of done (`docs/SCOPE.md` §9) is closed. **M5 closed on 2026-08-16** when T-085
did, so what is left is grouped into **M6** alone, whose purpose is in `tasks/README.md` and whose
membership is each task's `work_package` — do not maintain a list of that anywhere. It closes when
every task in it closes; it has no enumerated exit criterion, and the reason is in T-128.

**A release is not the last step of a release.** T-085 verified the published artifact from a clean
machine and was `blocked_by` the release task, so M5 was not complete when it was tagged. `0.4.0`
shipped with nothing checking it from outside; `0.5.0` did not. The ordering held: `0.5.0` was tagged
and then installed from its own tag onto a profile that had never held any of this. **It closed on
2026-08-16 with half proven and half unreachable**, and nothing carries the remainder: which half,
and why the plugin route cannot be run from any machine here, is in T-085 and not here.

Start with `docs/SCOPE.md` — the goal, the numbered requirements (R-1…R-24) and the explicit
non-goals. `docs/BRIEF.md` holds the problem evidence, the carried lessons and the remaining open
questions. Tasks cite the requirements they serve, so coverage is derived rather than tabulated.

**The plugin now has users outside this repository** — four projects as of 2026-08-09, labelled in
`control/LOCAL-CONTEXT.md`; three run it, and the fourth was assessed against the GitHub binding and
does not adopt it. **Re-counted 2026-08-18 and the roster was one short**: four sibling checkouts
carry their own `.taskmd/config.md`, of which two are validating local task files, and one of the
four had no row at all. Both figures, and why they answer different questions, are in that file —
do not carry either number around in prose. Expect an adopter to find in a day what this repository's habits had hidden for a
week: route what they report into tasks, not into notes, and treat a migration report as evidence
rather than as a feature request. **A written report is worth working straight through.** The first
adopting project delivered seven recommendations on 2026-08-10; all seven closed the same day, they
raised two further tasks between them, and two of the seven turned out to rest on premises that were
wrong in instructive ways — the command they recommended did not run, and the method they said was
silent had answered them one tier down. So read a report as a set of leads to verify, never as
findings to implement.

**Three reports in, the verification is mostly against *this* repository rather than against the
report.** The second adopter report — 2026-08-14, six observations, a public issue rather than a
handover — came out very differently from the first: **two of six asked for behaviour the version
they were running already shipped**, one had been ruled on by the owner months of commits earlier,
and one cited an id of ours that was correctly namespaced and still the wrong task. Exactly one row
was a defect nobody here knew about, and it was the row its author expected to be marginal. So the
first move on any row is to read the shipped artifact the reporter would have read, at the version
they name, and the second is to resolve every id they cite — including the ones labelled as ours. A
row that turns out to be already-shipped is worth more to the reporter than a task is: tell them what
they can delete. **The third move is the mirror of the first**: where a row describes a defect in the
reporter's *own* code, ask whether it is still there before handing it back. A row records the
observation and not the repair, so silence about the state reads as open — we listed one as theirs to
act on that they had found and fixed before writing the row, and the correction cost a round trip.
The row can be perfectly good as evidence and wrong as an item. **The fourth is the one a triage
skips by construction**: a row that *declines* to act still carries a claim about this tool, and
because it asks for nothing it is filed rather than checked. On 2026-08-15 the adopter refused to
build their own checker and wrote down the condition that would reverse the refusal — that `check`
reads only tasks and the documents those resolve, so their `skills/` and `examples/` trees were
uncovered. A specimen showed it reads every document a clone would receive and both trees fired, so
the condition cannot occur. That correction was worth more than either task the same comment
produced, and it would have been lost to *nothing here needs a reply*. Test the reasons, not only the
asks, and test them by running something. Where the trail for each report lands is in
`control/LOCAL-CONTEXT.md`, one row per adopter, and nowhere else.

**The channel changed on 2026-08-15, so these four rules now cover fewer arrivals than they did.**
The owner's other projects — htmldeck first among them — no longer send reports at all: a defect one
of them finds here arrives as a branch with a failing test and a three-line pull request, because
every one of these repositories is cloned side by side on the owner's machine. They report instead of
fixing only when the defect breaks a gate or destroys data. **Read a pull request the same way**: the
four rules above still apply to the sentences in its body, and its test is the *running something*
rule 4 asks for, already written. **On 2026-08-22 one arrived carrying a feature rather than a
finding** — a drafted method document, plus a task record saying it was a draft — and the four
rules had nothing to say about it. A contribution is reviewed on a second axis they do not reach:
not *is this true* but **is it agreed, and is it in the right place**. That one was true, and it
sat at its declared deliverable path inside `plugin/`, where nothing but a task record knew it was
unfinished and the next tag would have shipped it. Check where a contributed file lands before
checking what it says. The two live threads carry a note saying so, and both registers
that produced them are history rather than a practice.

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

**A third overlap exists and is not a copy — read this before reporting one.** `CLAUDE.md`'s
*Verifying* section states two rules that `plugin/skills/taskmd/docs/method/implement.md` also
states. T-190 put that to the owner on 2026-08-19 and the ruling was that they are **one wider rule
and one narrower one**: these bind on *any* claim about behaviour, `implement.md` binds inside a
phase that has loaded the method, and a session answering a question or triaging a report never
loads it. So the tier-1 text stays, and since 2026-08-21 its opening clause says the wider scope out
loud. The argument sits in a block comment in `CLAUDE.md`, which the harness strips before injecting,
so it costs the file and not the session. Deleting the section as a duplicate was offered and
declined; so was measuring the transcripts first.

**Since 2026-08-18 this project has its own `.taskmd/config.md`**, where it had none and ran the
shipped default. It is that default with one field added, and the reason — deriving a release-note
rule without adding a key to the shipped config, which T-106 shows would error every adopter's
config on upgrade — is in T-135. Two consequences: **edit `.taskmd/config.md`, not
`plugin/skills/taskmd/taskmd/defaults/config.md`**, when changing this project's schema; and this
repository no longer demonstrates the zero-config path, which is a price T-135 names rather than a
thing to fix.

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
