# Task Workflow Standard

Version 2.0 — 2026-08-04 (v1.0 2026-08-04, T-000; reworked in T-015)
Applies to: **<project>**

**This file is the only home for the working method.** `CLAUDE.md` and `.handoff/config.md`
point here; they do not restate it. If you find the rules written out somewhere else, that copy
is the defect — delete it and link here instead.

---

## 0. Start here

To work on a task, do **not** read this file, the index, and the task file. Run:

```
python tools/tasks/task.py context T-NNN
```

It prints the task's status and phase, what blocks it, what is waiting on it, its parent,
children, related tasks, and any open decision naming it — then tells you whether you can
proceed. That is the whole working set.

The other two commands:

```
python tools/tasks/task.py index              # regenerate tasks/README.md from front-matter
python tools/tasks/task.py decisions          # every decision and what it is holding up
python tools/tasks/task.py deliverables       # declared outputs, and whether they exist yet
python tools/tasks/task.py check [--closing]  # validate; --closing also requires an empty _working/
```

---

## 1. Core rules

1. **No task file, no work.** Before any analysis, writing, or file creation, a task file must
   exist in `tasks/`.
2. **Lifecycle is mandatory.** Every task passes `specify → plan → implement → review` (§2).
3. **Audit findings are children.** A QA/audit pass creates one umbrella task; each finding
   becomes a child task whose `parent` points at the umbrella (§6).
4. **Done means consistent.** A task is `done` only when deliverables are in `deliverables/`,
   linked documents are updated, the task file's status and log are current, and
   `python tools/tasks/task.py check --closing` passes.
5. **One home per fact.** Task files outrank chat, notes, and memory. Within a task file, the
   front-matter outranks prose. Nothing is written in two places — see §8.

---

## 2. Lifecycle

| Phase | What happens | Exit criterion |
| :--- | :--- | :--- |
| **specify** | Define the outcome, scope, acceptance criteria, and which deliverable it feeds. Ask the project owner about anything genuinely ambiguous. | Acceptance criteria written and agreed. |
| **plan** | Break into steps, name the inputs and the output paths, record dependencies in `blocked_by`. | Step list and output paths recorded. |
| **implement** | Do the work. Write outputs to `deliverables/`. Log decisions and assumptions. | All planned outputs exist. |
| **review** | Check against acceptance criteria. Fix, or raise a child task for what fails. | Every criterion ticked or carrying a child fix task. |

`phase` tracks where the work is; `status` tracks whether it can move. They are independent —
a `done` task sits in phase `review`; a `blocked` task keeps whatever phase it reached.

---

## 3. Front-matter schema

The **only** place a fact about a task is stored. `task.py check` enforces this table.

| Field | Values | Notes |
| :--- | :--- | :--- |
| `id` | `T-NNN` | Zero-padded, sequential, never reused. Take it from **Next ID** in the index. |
| `title` | one line, imperative | Appears in every generated view — write it to be read out of context. |
| `type` | `analysis` · `deliverable` · `research` · `fix` · `admin` | |
| `status` | `proposed` · `specified` · `planned` · `in_progress` · `blocked` · `review` · `done` · `cancelled` | see §4 |
| `phase` | `specify` · `plan` · `implement` · `review` | see §2 |
| `parent` | `T-NNN` or `null` | The umbrella, for audit children. |
| `blocked_by` | `[T-NNN, …]` | **Hard** dependency: this cannot proceed until those close. |
| `related` | `[T-NNN, …]` | **Soft** link: context worth having, not a gate. |
| `work_package` | `WP1`–`WP5` · `final` · `none` | |
| `owner` | name | |
| `created`, `updated` | `YYYY-MM-DD` | Absolute dates, never "yesterday". |
| `decisions` | `[D-NNN, …]` | Decisions gating this task. Register: [`DECISIONS.md`](DECISIONS.md). |
| `deliverables` | list of paths | What this task produces or changes. `task.py deliverables` reports whether each exists. |

### Derived — never write these down

`children`, `blocks`, which tasks a decision blocks, the deliverable map, and the whole of
`tasks/README.md` are **computed** from the fields above.
A stored inverse edge is a second copy of a fact and will eventually disagree with the first.

- `children` ← every task whose `parent` is this one.
- `blocks` ← every task listing this one in `blocked_by`.
- the index ← all front-matter, via `task.py index`.

`check` fails on a `children:` field for exactly this reason.

### Linking: which edge to use

- Can this task's work start and finish while the other is open? **No** → `blocked_by`.
- Would someone working this task make a worse decision without knowing about the other?
  **Yes** → `related`.
- Neither → don't link it. A graph that links everything says nothing.

Record the edge on the task that *is* blocked, not on the blocker — the inverse is derived.

---

## 4. Statuses

| Status | Meaning |
| :--- | :--- |
| `proposed` | Captured, not yet specified. |
| `specified` | Acceptance criteria agreed; ready to plan. |
| `planned` | Steps and outputs defined; ready to implement. |
| `in_progress` | Implementation underway. |
| `blocked` | Waiting on a decision, input, or another task. `blocked_by` must be non-empty. |
| `review` | Output exists, being checked against acceptance criteria. |
| `done` | Closed per rule 4. |
| `cancelled` | Dropped. Reason in the log. |

---

## 5. Files and folders

The folder contract has one home: the adopting project's own conventions file.

Task-specific naming:

- Filename: `T-NNN-short-kebab-title.md`, from [`templates/task-template.md`](templates/task-template.md).
- Audit umbrella: `T-NNN-audit-<scope>.md`, from [`templates/audit-umbrella-template.md`](templates/audit-umbrella-template.md).
- Closed tasks stay in `tasks/`. Nothing is moved on closure — links must keep resolving.

---

## 6. Audit procedure

1. Create an umbrella task from the audit template, scoped to what is being audited.
2. Record every finding in the umbrella's findings table with a severity (High / Medium / Low).
3. For each finding needing action, create a child task with `parent: T-NNN` and a `finding:`
   reference. **Findings are never fixed inline** — that is what makes the fix traceable.
4. The umbrella closes only when every child is `done` or `cancelled` with a recorded reason.

---

## 7. The index

`tasks/README.md` is a **generated view**, not a source. Change a task's front-matter, then run
`task.py index`. Its hand-written regions — Standards, Open decisions — sit outside the
generated block and are preserved. Decisions live in [`DECISIONS.md`](DECISIONS.md).

The old rule "update the index in the same edit as any status change" is retired: the index
cannot disagree with the task files any more, because it is made from them.

---

## 8. Where each kind of fact lives

Applies rule 5. Before writing anything down, find its one home here.

| Fact | Home |
| :--- | :--- |
| What a task is, needs, and produces | its task file |
| A task's status, phase, dependencies | its front-matter |
| Which tasks exist, and their state | generated — `task.py index` |
| The working method | this file |
| Folder contract, environment, content rules | `../CLAUDE.md` |
| Client, scenario, the CEO's question | `../docs/PROJECT-BRIEF.md` |
| A reusable lesson | `../docs/LESSONS.md` |
| A modelling rule | `../docs/standards/BPMN-MODELING-STANDARD.md` |
| A decision that is the project owner's to make | [`DECISIONS.md`](DECISIONS.md), linked from tasks via `decisions:` |
| Where to resume next session | `../.handoff/HANDOFF.md` (pointers only) |

If a fact seems to belong in two of these, it belongs in the more durable one, and the other
**links** to it.
