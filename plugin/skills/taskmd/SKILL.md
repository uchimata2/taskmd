---
name: taskmd
description: Work with tasks kept as Markdown files — one per task, plus a generated index, real dependency links and a validator — for any kind of work, not only software. Use in a project that tracks tasks this way (a folder of Markdown task files, or a .taskmd config) when asked what to work on next, or to start, specify, plan, implement, review, audit or close a task. Also whenever the user says taskmd.
---

# taskmd

Tasks are Markdown files. The index, the far end of every link, what is blocked and what to do next
are **derived by the tool** — so run a command, do not read the folder, and never maintain a list.

## Run first

```bash
taskmd list --open --limit 1
```

answers what to work on next, by the project's own ordering rule.

```bash
taskmd context <id>
```

returns everything needed to start that one task, and is the only read of it you need.

`taskmd` runs from any directory, including a subdirectory of the project: it finds the project by
walking up from wherever it is run. Add `--root <path>` only to override the one it finds.

These commands are the local-Markdown backend. If this project keeps its tasks somewhere else, its
binding supplies the operations instead — and everything below is unchanged, which is the point.

## Then load, each at its own moment — never in advance

| Load | When |
| :--- | :--- |
| [`docs/METHOD.md`](docs/METHOD.md) | Now, before doing anything to a task. It is the method. |
| the phase file it names in its §7 | Beginning that phase |
| this project's binding, in [`docs/bindings/`](docs/bindings/) | Before creating or changing any task. It says which artifact plays each role here, and what a write still owes afterwards. |
| [`adopt.md`](adopt.md) | The project has no tasks yet, or a command reports its task folder missing |

A write is not finished until the binding's *after any write* step has run, and it is yours to run —
the binding says why the tool cannot do it for you.

## Two things this tool makes easy to get wrong

- **`context` shows you every phase of a task at once**, including a plan you were not asked to
  execute — which is the situation [`docs/METHOD.md`](docs/METHOD.md) §3.1 exists for.
- **The field names and their allowed values are configuration, not something to remember**:
  [`taskmd/defaults/config.md`](taskmd/defaults/config.md) is the schema, and
  `taskmd check` reports every violation of it by name. Do not carry it in your head, and
  do not copy any of it into a task or a project document.
