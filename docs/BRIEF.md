# taskmd — brief

What to build, why it exists, and what has already been proven. Read `../CLAUDE.md` first.

For the goal, the numbered requirements and — above all — what is **out** of scope, see
[`SCOPE.md`](SCOPE.md). This brief holds the evidence behind the decisions; the scope holds the
boundary they are made within.

---

## The problem

Markdown task files are the natural tracker for agent-assisted work: plain text, diffable, no
service to log into, and the agent can read them. Every project that tries it hits the same three
walls.

**1. Reading a task costs too much.** The task file alone is not enough — you also need the
project's conventions, the index, what blocks this task, and what is waiting on it. In the source
project, starting one task meant reading six files, **37,909 bytes**, to extract a few hundred
that mattered. In an agent session that is paid for on every turn.

**2. The index drifts.** A central list of tasks and statuses duplicates what is already in each
file. It goes stale within days. The instinctive fix — a linter that compares the two copies — was
built in the source project and deleted a day later, because generating the index removes the
failure mode instead of monitoring it.

**3. Dependencies live in prose.** "This can't close until that lands" gets written in a comment,
a chat message, or a handoff note, and is lost. Nothing can compute what is actually blocked.

---

## What already works

`reference/task.py` is a working implementation, in production on a real project with 17 tasks.
It is **not** the plugin — it hardcodes one project's schema — but its behaviour is proven:

| Command | What it does | Measured result |
| :--- | :--- | :--- |
| `context T-NNN` | Everything needed to start one task | 37,909 bytes → **992** (2.6%) |
| `index` | Regenerates the index from front-matter | Drift became structurally impossible |
| `decisions` | Open questions and what each blocks | Surfaced 5 blocking open work |
| `deliverables` | Declared outputs and whether they exist | Caught a declared file that had been deleted |
| `check` | Validates what is still hand-made | Proven on 6 distinct failure cases |

`reference/TASK-WORKFLOW.md` is the standard it implements. `reference/templates/` holds the task
and audit templates.

---

## What to build

A plugin providing a skill plus a CLI, where **the schema is configuration, not code**.

### The central design question

`reference/task.py` hardcodes one project's front-matter: `status`, `phase`, `work_package`,
`decisions`. A general plugin cannot. Options, in rough order of preference:

1. **A config file** (`.taskmd/config.md` or `.yaml`) declaring field names, the status
   vocabulary, which status values mean "open", and which fields are edges. The tool reads it and
   everything else follows. Most flexible; needs a sane default so a new project works with none.
2. **A fixed core schema plus pass-through.** `id`, `title`, `status`, `blocked_by` are known;
   everything else is carried and displayed but not interpreted. Simplest; less useful `context`.
3. **Convention over configuration** — one opinionated schema, take it or leave it. Cheapest to
   build, and the reason most tools like this do not get adopted.

**Recommendation: (1) with the defaults of (3)** — zero config gets you the opinionated schema;
a config file adapts it. Decide this before writing code; it shapes everything.

**Settled in [T-001](../tasks/T-001-decide-how-the-front-matter-schema-is-configured.md)**
(2026-08-04): (1), with the defaults of (3) **and the pass-through of (2)** — the three were not
in fact alternatives. The decisions and their rationale live in that task file; the resulting
schema lives in [`plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md), which is also the
only documentation of what a config may contain.

### Commands

`context`, `index`, `check`, `list` are the core.

**Settled in [T-002](../tasks/T-002-implement-the-core-cli-context-index-check.md)** (2026-08-05):
`decisions` and `deliverables` are **neither** built in nor config-declared views — the one
behaviour of theirs that nothing else replaces, catching a declared output that has been deleted,
survives as a `check` class rather than as a command. It earned that on its first real run, finding
a deleted file still declared by T-008.

**Amended in [T-022](../tasks/T-022-filtered-task-listing-for-scripts.md)** (2026-08-05): the
surface stood at three because [`SCOPE.md`](SCOPE.md) non-goal 11 sent everything else to grep, and
`list` is the exception the maintainer argued for. Grep cannot answer these questions at all — what
a task blocks and the far end of a soft link are derived, and exist nowhere on disk — and reading
every task file to find the next one spends exactly what `context` was built to save. The non-goal
still excludes the query language; it is the *listing* that was carved out.

### The skill

A thin skill (`plugin/skills/taskmd/SKILL.md`) that teaches the agent to run the CLI rather than read
files, and to create tasks from the template. **Point at the tool; do not restate its rules in
prose** — a skill that describes what the CLI already enforces is a second copy that will drift.

### Interop

The source project drove this from the handoff skill's `local-markdown-dir` binding, using
`tracker_lint` to enforce its invariant. That binding assumes "the folder is the index", which
is false for any project with a generated one. Shipping a **binding contribution** to the handoff
package alongside this plugin is worth considering — see that repository's improvement brief, F1.

---

## Carried lessons

Learned the expensive way in the source project. Each cost something.

| | Lesson |
| :--- | :--- |
| **Delete duplication rather than policing it** | A check whose only job is comparing two copies of one fact is evidence the second copy should not exist. This is the plugin's whole thesis. |
| **Verify by running, on the real case** | Documentation and search summaries were both wrong about tools here. A validator is proven only when it has been made to **fail** on a case it should catch. |
| **"Installed" is not "working"** | Two packages installed cleanly and were unusable. If this plugin ever grows a dependency, its install instructions must end with a command that proves it runs. |
| **What is read every time must be short** | The reason `context` exists. It also applies to the plugin's own docs. |
| **Determinism is a platform property** | A regression comparison failed on all 196 lines on Windows — text-mode newline translation. Write with `newline="\n"`. |
| **An imported convention carries its author's assumptions** | State this plugin's assumptions where an adopter can check them, rather than leaving them implicit. |

---

## Open questions

1. ~~**Schema configuration**~~ — **closed** by
   [T-001](../tasks/T-001-decide-how-the-front-matter-schema-is-configured.md), 2026-08-04.
2. ~~**ID scheme**~~ — **closed** by
   [T-004](../tasks/T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md), 2026-08-09.
   Configurable (T-001 D8), defaulting to `T-` at width 3, and a merge collision costs a message
   rather than a task: every command reports it and none of them renumbers anything.
3. ~~**Scale**~~ — **closed** by
   [T-004](../tasks/T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md), 2026-08-09.
   Measured at seven scales, and the answer is that the two ceilings coincide: the default width
   stops a project at 999 tasks, which is just short of where `check` crosses a second. Nothing was
   optimised, because nothing needed to be.
4. ~~**Sub-tasks vs. dependencies**~~ — **closed** by
   [T-008](../tasks/T-008-write-the-backend-neutral-method-document.md), 2026-08-04. The distinction
   is a two-question test in [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4 *Which edge to use*, and it turned out to
   need a third answer as much as the first two: if neither question fires, do not link them at all.
5. ~~**Should `check` fix?**~~ — **closed**: an automatic fixer that rewrites task content is
   non-goal 6 in [`SCOPE.md`](SCOPE.md). The reason turned out to be stronger than the original
   worry: a `--fix` for "stale derived fields" cannot be needed, because derived fields are not
   stored and so cannot go stale.

---

## Definition of done

Moved to [`SCOPE.md` §9](SCOPE.md#9-definition-of-done), alongside the requirements it is written
against. This brief keeps the evidence; the scope keeps the boundary.
