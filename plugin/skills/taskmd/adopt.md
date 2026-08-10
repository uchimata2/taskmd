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

[`docs/METHOD.md`](docs/METHOD.md) §3 names which of its rules bind *before* it is clear
that there is any task work, and therefore cannot wait for the method to be loaded. Put those where
your project's own always-loaded conventions live.

This skill cannot do it for you, and the reason is worth knowing rather than working around: a
session that has not invoked a skill has been handed its `description` and nothing else. That is a
measurement rather than a claim about this file — it was taken by starting a session, writing down
what it had been given before invoking anything, and checking whether an ordinary request reached
the skill. Re-take it the same way in your own project if you want to know it holds there.

## 5. Confirm

```bash
taskmd check
```

Anything it names is a problem to fix before the first task. If what it names is the configuration,
the file to fix is the one from step 2. If the **name itself** is not found, that is not a problem
with your project — [`SKILL.md`](SKILL.md) says what to run instead.
