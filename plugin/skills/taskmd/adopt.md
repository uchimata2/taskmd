# Adopting taskmd

> Read once, when a project has no tasks yet or a command reports its task folder missing. Nothing
> here is needed a second time, which is why it is not in [`SKILL.md`](SKILL.md).

## 1. Make the task folder

`tasks_dir` in the schema names it, and **no command creates it** — creating it is the whole of
setup.

## 2. Take the default schema, or replace it

[`taskmd/defaults/config.md`](taskmd/defaults/config.md) is what a project gets with no
configuration at all, and is also the only description of what a configuration may contain. To
change any of it, copy that file to `.taskmd/config.md` and edit it there; the rules for writing one
are in the file itself.

## 3. Choose a binding

[`docs/bindings/`](docs/bindings/) holds one document per backend. Read the candidate's
*Assumptions this binding makes* section before anything else: every entry is a claim about **your**
project rather than a description of the backend, and a claim that is false for you is how a project
ends up inconsistent while appearing to comply. Stop at the first one you cannot answer.

## 4. Carry the conduct rules your harness loads unasked

Two of the method's conduct rules bind *before* it is clear that there is any task work, so they
cannot wait for the method to be loaded — [`docs/METHOD.md`](docs/METHOD.md) §3 says which and why.
They are below. **Copy them into wherever your project's own always-loaded conventions live**, and
copy them whole: each carries the sentence that stops the obvious misreading, and a version trimmed
to the heading is one an agent talks itself out of.

> ### One phase per request — never auto-advance
>
> Do the phase that was asked for, then stop and report. Do not continue into the next one because it
> is obvious, because the plan already describes it, or because a note said it was next.
>
> **A pointer is context, not authorization.** A "next step" line, a resumption note, an unfinished
> checklist, the rhythm of the last three tasks — none of these is a request.
>
> **Asking for more is.** A request for two phases, or for the whole lifecycle, is as valid as a
> request for one; write it into the task's own record, naming who gave it and what it covers, because
> an authorization kept anywhere else is one a later session can miss or stretch to a task it never
> reached.
>
> ### Surface what you discover — never absorb it, never drop it
>
> Work turns up things nobody anticipated: a better approach, a flawed premise, an unrelated defect,
> a missing prerequisite. Each one goes to exactly one of two places:
>
> - **It changes what the current task should produce** → raise it as a question now, before
>   continuing. Quietly widening or narrowing the outcome substitutes your judgement for the owner's.
> - **It is actionable but outside this task** → raise a new task for it. This costs one record and
>   keeps the current task honest.
>
> What must never happen is the third option: fixing it silently, or noticing it and moving on. A
> silent fix makes the task's record false; a dropped observation is lost the moment the session ends.

The two cross-references the originals carried are dropped on purpose: they point into the method's
own `method/rationale.md`, which resolves from the skill and not from wherever you paste this.

This skill cannot do it for you, and the reason is worth knowing rather than working around: a
session that has not invoked a skill has been handed its `description` and nothing else. That is a
measurement rather than a claim about this file — it was taken by starting a session, writing down
what it had been given before invoking anything, and checking whether an ordinary request reached
the skill. Re-take it the same way in your own project if you want to know it holds there.

## 5. Write a template, or do not

Optional, and a project with none is a normal project — nothing creates one, nothing reports its
absence, and no configuration key names one. If you want one, it is a Markdown file whose name
starts with `_`, sitting **directly in** your tasks folder rather than in a folder under it, and
carrying a placeholder where a real id would go. All three of those are how the create path finds it
and how everything else declines to read it as work; [`docs/bindings/local-markdown.md`](docs/bindings/local-markdown.md)
says why each one is load-bearing.

taskmd ships no template to copy, deliberately — a second one under this skill would sit outside
your tasks folder, where `check` neither follows its links nor reads its front-matter, and an
unvalidated template rots in silence and hands you an invalid task every time somebody uses it.
Yours is checked because of where it lives. Start from the one in taskmd's own repository if you
want a worked example; it is written to survive the copy, and **it carries no links**, for the
reason its own comment block gives.

## 6. Confirm

```bash
taskmd check
```

Anything it names is a problem to fix before the first task. If what it names is the configuration,
the file to fix is the one from step 2. If the **name itself** is not found, that is not a problem
with your project — [`SKILL.md`](SKILL.md) says what to run instead.
