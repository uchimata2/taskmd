# taskmd — scope, goals and requirements

The boundary. When a proposal arrives, this file answers "is that in scope?" — and §4 answers it
in the negative, which is the half that does the work.

Read `../CLAUDE.md` for how to work here. Read [`BRIEF.md`](BRIEF.md) for the problem evidence and
the measured prior art; this file does not repeat them. Decided in
[T-007](../tasks/T-007-define-the-project-scope-goals-and-requirements.md).

---

## 1. Goal

**A lightweight, token-efficient, local-first task tracker for Claude Code — Markdown files, a
generated index, real dependency links, and a validator — usable for any kind of work, not only
software.**

Two properties make the goal falsifiable rather than decorative:

- **Token cost.** Starting a task costs one command, not a reading list. The saving is measured and
  stated (`BRIEF.md`), not asserted.
- **No install.** A clone works: no configuration, no dependencies, no path editing.

If a change makes either worse, it is against the goal even if it is a good idea.

---

## 2. Principles

Three rules that every requirement below is an application of. They are listed once, here.

1. **One home per fact.** Every fact is written in exactly one place. Anything derivable is
   computed at read time, never stored. A feature that *requires* writing the same fact twice is
   the wrong feature — the emphasis is on "requires". Where the inverse is derived, one write is
   always sufficient, so a user who chooses to write the other side as well is not creating drift;
   a two-way reference living at both ends is the nature of references (R-2). This rule forbids
   designs that **compel** a second write, not users who make one.
2. **Store the forward edge, derive the rest.** Recording a relationship on one task is *enough* —
   the other end is computed, so no view can miss it. *Not a local-file quirk:* GitHub exposes
   `--blocked-by` / `--blocking` as two views of one relation, and Notion's `Parent item`
   auto-fills the parent's `Sub-item`. Mature trackers already work this way.
3. **Point, don't restate.** A document that repeats another will drift from it. Everything
   restated into an agent's context is also re-sent on every following turn.

---

## 3. Requirements

Numbered so tasks can cite them. Each is written to be **testable** — if you cannot say what would
falsify it, it is a principle, not a requirement, and belongs in §2.

### A. Method — how work is tracked, independent of where it is stored

| # | Requirement |
| :--- | :--- |
| **R-1** | Every fact about a task has exactly one home, and derived facts are computed. |
| **R-2** | **Every task shows every link it has, in both directions.** Whichever end of a link you open — the blocker or the blocked, the parent or the child, either side of a soft link — the link is visible. Storing it on one task is sufficient; storing it on both is permitted and collapses to a single entry, so nobody has to know which side "owns" it. Decided in [T-012](../tasks/T-012-decide-whether-soft-edges-are-symmetric.md). |
| **R-3** | The mandatory lifecycle is **specify → plan → implement → review**. `phase` records where the work is, `status` records whether it can move; the two are independent. |
| **R-4** | **Verification is `implement`'s exit criterion.** A task cannot leave `implement` without recorded evidence the outcome was checked by using it. For non-software work, the evidence is whatever shows the deliverable does its job. |
| **R-5** | **Audit is a task type, not a phase.** An audit produces one umbrella task; each finding becomes a child task. Findings are never fixed inline — that is what makes a fix traceable. |
| **R-6** | **One phase per request; never auto-advance.** A "next step" pointer, a handoff note, or an obvious continuation is context, not authorization. |
| **R-7** | **The phase's exit criterion sets the required level of detail.** The agent asks only what is still missing to satisfy it, batched into a single turn, never drip-fed. |
| **R-8** | **Discovery is surfaced, never absorbed.** Anything found mid-execution that would reasonably improve quality is raised — as a question if it changes the current task's spec, as a new task if it is actionable and out of scope. It is never acted on silently, and never silently dropped. |
| **R-9** | Nothing in the method assumes code, tests, compilers, or version control. It must read sensibly for research, a deck, a training course, or an ops runbook. |

### B. Storage — where tasks live

| # | Requirement |
| :--- | :--- |
| **R-10** | Tasks are **local Markdown files**, one per task: front-matter for facts, body for content. Readable and editable with no tool installed. |
| **R-11** | The front-matter schema is **configuration, not code** — decided in [T-001](../tasks/T-001-decide-how-the-front-matter-schema-is-configured.md). |
| **R-12** | The index is **generated** from the task files and never hand-edited, so drift is structurally impossible rather than policed. |
| **R-13** | **The method is implemented against a named backend contract.** Local Markdown is one backend; GitHub Issues is another. The method document contains no backend-specific instruction, and **each binding states the assumptions it makes about the adopting project** so an adopter can check them in thirty seconds. |
| **R-14** | **Changing backend changes the binding, not the method.** A project moving from local files to GitHub Issues keeps the same lifecycle, the same edges and the same rules. Backend-specific realities — server-assigned ids, a missing soft-link field — are absorbed by the binding, not by the method. |

### C. Tool — the CLI

| # | Requirement |
| :--- | :--- |
| **R-15** | `context <id>` returns everything needed to start one task **and nothing else**. This is the headline claim; the saving is measured on a real case and stated in the README. |
| **R-16** | The validator is **proven by being made to fail** on every class of problem it claims to catch. A clean-tree pass proves nothing. |
| **R-17** | **Configuration errors surface at setup, not mid-run.** A typo in a config key, a missing file, or an unresolvable reference is reported when the config is read — never inside a task the user is trying to finish. |
| **R-18** | **One implementation**, in standard-library Python. The interpreter and the repository root are auto-discovered so a clone runs unedited. bash and PowerShell appear only as thin launchers containing no logic. |
| **R-19** | **Project hooks are language-free.** A project may declare its own commands — validation, post-write, whatever it needs — in bash, PowerShell, Python or anything else; taskmd invokes what is configured and reports failures. |
| **R-20** | Runs on a clone with no configuration and no dependencies, on Windows, macOS and Linux, with byte-identical output. |

### D. Product

| # | Requirement |
| :--- | :--- |
| **R-21** | **Progressive disclosure.** The skill is a small always-loaded spine plus files loaded only when their moment arrives — never the whole method up front. |
| **R-22** | The skill **points at the tool** rather than restating what the tool already enforces. |
| **R-23** | **Publishable.** No personal, client or machine data anywhere: no real names, absolute local paths, drive letters or hostnames. |
| **R-24** | Interoperates with the **handoff** skill as a tracker binding, so a session can resume into a taskmd project. |

---

## 4. Non-goals

Not "later" — **not this tool**. Each is something a task tracker plausibly grows into, and each
would cost the goal in §1.

1. **Project management.** No estimates, time tracking, velocity, burndown, capacity or Gantt.
   Those need a team process to be meaningful; this needs a folder.
2. **A running process.** No server, daemon, database, watcher or background sync.
3. **A user interface.** No GUI, no TUI, no web view. The files are the interface; the terminal is
   the view.
4. **Multi-user coordination.** No locking, no concurrency control, no merge-conflict resolution.
   Git owns that.
5. **Network access from the core.** The tool reads and writes local files. Anything remote is the
   agent's job through its own tools.
6. **An automatic fixer that rewrites task content.** A `--fix` for "stale derived fields" is
   tempting and self-defeating: derived fields cannot go stale, because they are not stored.
7. **Model, effort or cost gates.** Which model runs a phase is agent-harness policy, not tracking.
8. **Migration tooling** (v1). Moving an existing backlog into taskmd, or local files into GitHub
   Issues, is out until the method and both bindings are proven.
9. **Replacing GitHub Issues** for teams already using them. taskmd's GitHub mode applies its
   method *to* issues; it does not ask anyone to leave them.
10. **Notifications, reminders, scheduling, recurrence.**
11. **A query language.** `context`, `index` and `check` are the surface. Anything else is grep.

---

## 5. Constraints

The publishing, portability and verification constraints have one home: **`../CLAUDE.md`**. They
are not repeated here. In short — dependency-free, cross-platform, no personal or machine data, and
behaviour is proven by running the thing, never by reading it.

---

## 6. Assumptions

**Settled 2026-08-04 — treat these as decisions, not as open questions.** They were proposed in
T-007, worked with for a full session, and confirmed by the maintainer. No session should re-raise
them for confirmation; change them only if someone deliberately revisits one.

- **A1 — One implementation, in stdlib Python** (→ R-18, R-19). Rejected: shipping parallel bash /
  PowerShell / Python versions of the same commands, which would be three copies of one fact.
- **A2 — Four mandatory phases**, verification as `implement`'s exit criterion, audit as a task
  type (→ R-3, R-4, R-5). Rejected: six linear mandatory phases — heavier than research or deck
  work needs, and it leaves audit findings with nowhere structural to go.
- **A3 — GitHub ships as a binding document, not code, in v1** (→ R-13, R-14, non-goal 8).
  Rejected: a `gh`-backed CLI, which would make `gh` a dependency and put the network inside the
  tool.

---

## 7. Where the stated requirements landed

The maintainer's eight, mapped so none was quietly dropped. Requirement **8** was "and so on" — an
explicit invitation to complete the set from what the three reference projects teach; R-15 through
R-24 are that completion.

| Stated | Carried by |
| :--- | :--- |
| 1 — local Markdown, human readable | R-10, R-12 |
| 2 — bash / PowerShell / Python, auto-discovery or configurable | R-18, R-19 (see A1) |
| 3 — don't guess; ask, to the required level of detail | R-7, R-8 |
| 4 — single source of truth, reference rather than duplicate | R-1, R-2, R-22, §2 |
| 5 — research, decks, training, skill creation — not only software | R-9 |
| 6 — principles separated from technical spec; GitHub-ready | R-13, R-14 |
| 7 — delivery pipeline, audit findings into tasks | R-3, R-4, R-5, R-6 |
| 8 — "and so on" | R-15 … R-24 |

---

## 8. Traceability

**Tasks cite requirements; this file does not list tasks.** A mapping table here would be a second
copy of the backlog and would drift within days — R-1 forbids it, and the drift would be in the
document that defines R-1.

Every task that **implements** a requirement names it under *Requirements served* in its
`## 1. Specify` section. Coverage is therefore **derivable** from the task files, exactly like
`blocks` and the index, and a future `task.py requirements` view could report it without anything
new being written down.

T-007 is the exception, and necessarily so: it *defines* the requirements rather than serving any,
so it cites none.

---

## 9. Definition of done

Moved here from `BRIEF.md`, which now points at this section.

- Works on a clone with no configuration and no dependencies (R-18, R-20).
- `check` demonstrated **failing** on every class of problem it claims to catch (R-16).
- The measured `context` saving reproduced on a sample project and stated in the README (R-15).
- The method document carries no backend-specific instruction, and both bindings implement the
  same lifecycle (R-13, R-14).
- Every non-goal in §4 still holds.
- No personal, client or machine data anywhere in the repository (R-23).
