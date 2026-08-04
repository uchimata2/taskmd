# taskmd — brief

What to build, why it exists, and what has already been proven. Read `../CLAUDE.md` first.

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

### Commands

`context`, `index`, `check` are the core. `decisions` and `deliverables` proved their worth but
are arguably separate concerns — decide whether they are built in or left to config-declared
"derived views".

### The skill

A thin skill (`skills/taskmd/SKILL.md`) that teaches the agent to run the CLI rather than read
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

1. **Schema configuration** — the design question above. Blocks everything.
2. **ID scheme.** The source used `T-NNN`, zero-padded, never reused, with the next id in the
   generated index. Configurable prefix? Configurable width? What happens on a merge conflict?
3. **Scale.** `context` and `index` re-read every task file on each run. Fine at 17 files. At 500?
   Measure before optimising, but decide where the ceiling is claimed to be.
4. **Sub-tasks vs. dependencies.** The source had `parent` (audit umbrella → findings) *and*
   `blocked_by`. Both earned their place, but the distinction needs explaining in one sentence or
   users will pick wrongly.
5. **Should `check` fix?** It currently only reports. A `--fix` for mechanical problems (stale
   derived fields) is tempting and risks becoming a second source of truth.

---

## Definition of done

- Works on a clone with no configuration and no dependencies.
- `check` demonstrated failing on every class of problem it claims to catch.
- The measured `context` saving reproduced on a sample project, and stated in the README.
- No personal, client, or machine data anywhere in the repository.
