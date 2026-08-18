# Being resumed by the handoff skill

> How to configure the [handoff skill](https://github.com/uchimata2/handoff) so it can drive a
> taskmd project as its tracker — a session stops, and a later one resumes into the right task.

This is a **configuration recipe, not a binding**. Handoff resolves its `tracker` key to a file in
its own `bindings/` folder, so a document here cannot be loaded as one. What it can do is say which
of handoff's existing bindings fits each taskmd backend, and what to put in the project config so
the fit is exact. Nothing here is installed; you write one config file in your own project.

**Two contracts run in opposite directions, and conflating them is the mistake this page exists to
prevent.** Handoff's binding contract lets handoff drive *a* tracker — here, yours. taskmd's own
contract ([`BINDING.md`](BINDING.md)) lets taskmd drive *a* backend. They share vocabulary and
answer different questions. This page is entirely about the first.

## Which binding, by backend

| Your taskmd backend | Handoff binding | Why |
| :--- | :--- | :--- |
| Markdown files in a folder (the default) | `local-markdown-dir` | One file per item, ids in the filename — the shape that binding is for |
| GitHub Issues ([`bindings/github-issues.md`](bindings/github-issues.md)) | `github-issues` | taskmd stores every enumerated field as a `<field>:<value>` label, which that binding reads directly |

## Recipe — Markdown-file backend

In your project's handoff config:

```text
- `tracker`: local-markdown-dir
- `tracker_dir`: tasks/
- `tracker_id_prefix`: T-
- `tracker_template`: tasks/_task-template.md
- `tracker_lint`: taskmd check
- `tracker_closed_dir`: (leave unset)
```

Take `tracker_dir`, the id prefix and the template from **your** taskmd config rather than from the
lines above — they are that config's values, and copying them here would be a second home for
them. [`../taskmd/defaults/config.md`](../taskmd/defaults/config.md) is the schema that names them.

**`tracker_closed_dir` stays unset**, and that is a decision rather than an omission. taskmd signals
closure with a status value and leaves the file where it is, so every link that ever resolved to a
task keeps resolving after it closes. Setting a closed folder would move files out from under those
links to record a fact the front matter already carries.

**`tracker_lint` is the whole reason this recipe is short.** Handoff's binding calls it the
invariant-enforcement hook: a command run after every create and update that exits non-zero when the
folder or the index has drifted. `taskmd check` is exactly that command, and it is the one thing
here you should not leave out — see the next section.

## Recipe — GitHub Issues backend

```text
- `tracker`: github-issues
- `tracker_status`: label:status:
- `tracker_status_done`: done
- `tracker_workflow`: <the doc that tells a session how work moves here>
```

taskmd writes each enumerated field as a `<field>:<value>` label, so handoff's `label:<prefix>` form
reads the status with no translation layer. Point `tracker_workflow` at whatever your project uses
to say how work moves — [`METHOD.md`](METHOD.md) if you follow the method as shipped.

`tracker_repo` can usually be left out: it defaults to the repository resolved from the working
directory, which is right whenever the issues and the work live together.

## The index is the part that goes stale silently

A taskmd project has a **generated central index**. In handoff's terms that is topology (b) —
*a central index exists*, produced by a script — and its binding is explicit that following it
without accounting for one is the classic silent failure: the task file is correct, the index is
stale, and nothing complains.

Two things close that hole, and they are both already in the recipe above:

- **`tracker_lint: taskmd check`**, so drift fails the write rather than surviving it;
- **regenerate, never hand-edit.** The index is built from the task files by `taskmd index`. Handoff's
  reconcile sweep is where a stale one would otherwise be left behind.

The two commands back each other up: `check` reports a stale index and names the command that fixes
it, so a forgotten `index` is loud rather than silent.

## Assumptions this recipe makes about your project

Check these in about thirty seconds. Where one is false, adapt your **project config** — not this
page and not handoff's binding.

- **Your task folder is where `tracker_dir` points, and ids are the leading segment of the
  filename.** Handoff's *find* scans `<id>-*.md`; a project that renamed its files past that pattern
  needs its own answer.
- **Closure is a status value, not a folder.** The recipe leaves `tracker_closed_dir` unset for the
  reason given above. If your project does move closed files, set it — and expect links to closed
  tasks to need updating, which is the cost that decision buys.
- **"Done" is the complement of a set, not a single value.** taskmd defines `open_statuses` and
  treats everything outside it as closed, where handoff's file binding asks which one value means
  done. Nothing breaks while `tracker_closed_dir` is unset, because nothing moves on closure and the
  question is never asked. Set that key and the mismatch becomes real: a project with two closed
  values must say which one triggers the move.
- **`taskmd` is runnable as `tracker_lint` names it.** If the command is reached by path in your
  environment, write that path — a lint that cannot start reports no drift and looks like a pass.
- **The index is generated and never hand-edited.** An index someone edits by hand is a second home
  for facts the task files already carry, and this recipe cannot keep it honest.

## What this recipe does not do

It does not make taskmd's lifecycle visible to handoff. Handoff writes a status in exactly one
place — its reconcile sweep marking finished work done — and knows one value, whichever
`tracker_status_done` names. `phase`, the edges, and the exit criteria are taskmd's and stay
taskmd's. That is the intended division rather than a gap: handoff moves *between* sessions, and the
method moves work *through* phases.
