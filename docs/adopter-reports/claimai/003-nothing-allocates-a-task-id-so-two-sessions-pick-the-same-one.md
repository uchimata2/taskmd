# Nothing allocates a task id, so two sessions pick the same one

| Field | Value |
| :--- | :--- |
| **Target** | `taskmd` — the maintainer's own repository, cloned beside the reporting project |
| **Kind** | Feature |
| **Status** | `open` |
| **Severity** | High — it is a silent collision on the identifier everything else references, and `check` passes either way |
| **Found while** | Two sessions working the same `tasks/` folder, 2026-08-24. It has been a standing project rule since |
| **Version seen** | 0.6.0 |

## What happens

A new task's id is chosen by reading the folder and taking the next free number. Nothing reserves it.
Two sessions an hour apart read the same folder, both saw the same next free id, and both used it.

This project carries a hand-written rule as its only defence:

> **Re-derive the next free task id immediately before writing a new task file**, never from an
> earlier reading.

A rule that says *do the unsafe thing as late as possible* is the shape of a missing operation.

## Why it is worse than an ordinary race

The id is the **reference key**. Every dependency edge, every cross-link and every generated index row
names it. A collision does not corrupt one file; it merges two tasks in every document that points at
either.

And `check` does not object. It validates structure and references, and two files with the same id in
their front matter is a state it reports as `OK` — which is what makes this a defect rather than an
inconvenience.

## What to change

1. **Give the CLI a `new` command that allocates and writes in one step**, so the read and the claim
   cannot be separated by anything.
2. **Make `check` fail on a duplicate id.** Whatever else is decided, the validator should not pass a
   folder holding two `E28`s. This is the cheap half and it is independent of the first.
3. **Consider ids that do not need allocating.** A monotonic or content-derived id has no race, at
   the cost of the readable sequence this project chose deliberately — so this is an option, not a
   recommendation.

## Related

- [`001-index-drops-a-concurrently-created-task.md`](001-index-drops-a-concurrently-created-task.md)
  — the other concurrency finding, from the same two sessions on the same day. That one is `index`
  missing a file that exists; this one is two files that should not both exist.
