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

Three properties make the goal falsifiable rather than decorative:

- **Token cost.** Starting a task costs one command, not a reading list. The saving is measured and
  stated (`BRIEF.md`), not asserted.
- **No install.** A clone works: no configuration, no dependencies, no path editing.
- **Invisibility.** The tool works in the background and asks nothing of the user in order to stay
  correct. Control exists for anyone who wants it — every value the tool fills in can be overridden
  — but no correctness may depend on someone remembering to intervene. *Added 2026-08-05 by the
  maintainer.* It is the property most easily lost by accident: a cache, a stored derived value, a
  field a human must keep true, a step in a README that someone has to remember. Each is useful and
  each fails this test, which is why it is written here rather than assumed.

If a change makes any of the three worse, it is against the goal even if it is a good idea.

---

## 2. Principles

Three rules that every requirement below is an application of. They govern the **whole product** —
the schema, the generated index, the config, the code — which is why they are stated here in full
rather than pointed at. Where a principle *also* holds as a narrower rule about how work is tracked,
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) states that version and this section points at it. **This is not the
convention in §3**, which governs requirements and is stated there — a principle is a rule, and a
requirement is not. Decided in
[T-045](../tasks/T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md).

1. **One home per fact.** Every fact is written in exactly one place. Anything derivable is
   computed at read time, never stored. A feature that *requires* writing the same fact twice is
   the wrong feature — and the emphasis is on "requires". What the rule does and does not forbid is
   stated once, in [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4: the case where the
   distinction bites is the inverse of a link, where one write is always sufficient and a second is
   permitted (R-2), and §4 also carries the condition under which a **system limitation** is grounds
   to write a fact twice — together with the case that does not qualify, which is a limitation
   assumed rather than demonstrated. *Widened here on 2026-08-21 by
   [T-187](../tasks/T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md).* Until then
   this pointer said §4 covered the inverse-of-a-link case, which was true when
   [T-045](../tasks/T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) wrote it
   and stopped being true when §4 gained the wider clause. T-045's decision is unchanged: this
   section **points** and does not state.
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

**These requirements and [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) say the same things, and that is correct.** A
requirement states a property the method must have; the method states the rule that gives it that
property. Two documents agreeing is what conformance *is* — R-1 governs facts about tasks, not a
specification restating what it requires, and a requirement that could not be compared against the
method would be unable to do the one job it has.

What that licenses is narrow, so the boundary is worth stating: a requirement says **what must be
true**, never **what to do**. A row that reads as an instruction has stopped being a requirement and
become a second copy of the method — which will drift, and which cannot be used to judge whether the
method got it right. The test is whether the row survives someone rewriting the method completely: a
property does, an instruction does not. Decided in
[T-017](../tasks/T-017-settle-the-overlap-between-scope-requirements-and-the-method.md).

### A. Method — how work is tracked, independent of where it is stored

| # | Requirement |
| :--- | :--- |
| **R-1** | Every fact about a task has exactly one home, and derived facts are computed. |
| **R-2** | **Every task shows every link it has, in both directions.** Whichever end of a link you open — the blocker or the blocked, the parent or the child, either side of a soft link — the link is visible. Storing it on one task is sufficient; storing it on both is permitted and collapses to a single entry, so nobody has to know which side "owns" it. Decided in [T-012](../tasks/T-012-decide-whether-soft-edges-are-symmetric.md). |
| **R-3** | The mandatory lifecycle is **specify → plan → implement → review**. `phase` records where the work is, `status` records whether it can move; the two are independent. |
| **R-4** | **Verification is `implement`'s exit criterion.** A task cannot leave `implement` without recorded evidence the outcome was checked by using it. For non-software work, the evidence is whatever shows the deliverable does its job. |
| **R-5** | **Audit is a task type, not a phase.** An audit produces one umbrella task; each finding becomes a child task. Findings are never fixed inline — that is what makes a fix traceable. |
| **R-6** | **A phase is worked only when it was requested.** Falsified by any advance into a following phase that no request asked for; the method must state that a next-step pointer, a resumption note or an obvious continuation does not constitute one. |
| **R-7** | **Every phase has a stated exit criterion, and it is the measure of "enough".** Falsified by a phase whose exit criterion is not written down, by questions that go beyond what the criterion needs, or by questions arriving across several turns when they could have been asked together. |
| **R-8** | **Everything found mid-execution leaves a trace.** Falsified by an outcome that changed without the change having been raised, or by a discovery that is actionable and out of scope with no task recording it. Silent absorption and silent dropping are the two failures. |
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
| **R-21** | **Progressive disclosure, and "always-loaded" means *before the skill is invoked*.** What a session is handed unasked — for a skill, its description rather than its body — is the only part every session pays for; the body arrives on invocation, and each further file when its moment arrives. Never the whole method up front. **Falsified by measuring a session**, which is the only evidence that counts: a document's statement about when it loads is a claim, and this project believed one for weeks ([T-028](../tasks/T-028-budget-the-whole-always-loaded-context-not-one-file.md)). The referent is named here and the tiers are not, because a count would be an architecture — see [T-048](../tasks/T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md). |
| **R-22** | The skill **points at the tool** rather than restating what the tool already enforces. |
| **R-23** | **Publishable.** No personal, client or machine data anywhere: no real names, absolute local paths, drive letters or hostnames. |
| **R-24** | Interoperates with the **handoff** skill as a tracker binding, so a session can resume into a taskmd project. |

---

## 4. Non-goals

Not "later" — **not this tool**. Each is something a task tracker plausibly grows into, and each
would cost the goal in §1.

1. **Project management.** No time tracking, velocity, burndown, capacity or Gantt. Those need a
   team process to be meaningful; this needs a folder. **Amended 2026-08-05 by the maintainer; the
   original excluded estimates outright.** Two estimated fields — effort and business value — are in
   scope for exactly one purpose: ordering the task listing
   ([T-022](../tasks/T-022-filtered-task-listing-for-scripts.md)). The carve-out is tested by use
   rather than by intent — **if either field is ever read by something other than the ordering, it
   has left it**, and that is the moment to re-argue this non-goal rather than quietly widen it.
   They are filled in by the agent, overridable, and optional (`none` disables them), which is what
   keeps them on the right side of §1 *Invisibility*: an estimate a human must maintain for the tool
   to be correct would fail that property and would not be worth having.
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
8. **Migration tooling**, in every direction but one. **Amended 2026-08-10 by the maintainer; the
   original read "Migration tooling (v1). Moving an existing backlog into taskmd, or local files
   into GitHub Issues, is out until the method and both bindings are proven."** The clause deferred
   the work until a bar was cleared rather than forever, and **the bar is cleared**: both bindings
   are written, the GitHub one was walked on a live repository
   ([T-010](../tasks/T-010-write-the-github-issues-binding.md)) with its body-rewrite rule proven by
   being made to fail ([T-041](../tasks/T-041-prove-the-github-bindings-body-rewrite-rule.md)), and the method
   needed no change to carry either.

   **So one direction is now in scope: moving a taskmd project from local Markdown to GitHub Issues**
   ([T-108](../tasks/T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md)). It is
   the direction with two proven bindings behind it, and the one an adopter reaches for when a
   project outgrows a folder.

   **Everything else this non-goal named stays out.** Importing a foreign backlog into taskmd is
   still v1 — nothing is proven about a source taskmd did not write. So is any continuous two-way
   sync between a folder and a repository, which is a different product. And the carve-out moves
   neither of the two non-goals standing next to it: **5** still keeps every network call out of the
   core, so the agent performs the migration and taskmd only prepares it, and **11** still holds the
   CLI at four commands.
9. **Replacing GitHub Issues** for teams already using them. taskmd's GitHub mode applies its
   method *to* issues; it does not ask anyone to leave them.
10. **Notifications, reminders, scheduling, recurrence.**
11. **A query language** — boolean expressions, saved queries, aggregation, ranking as a feature.
    **Amended 2026-08-05 by the maintainer; the original read "`context`, `index` and `check` are
    the surface. Anything else is grep."** A **filtered task listing** is now in scope
    ([T-022](../tasks/T-022-filtered-task-listing-for-scripts.md)), for two reasons the original
    wording did not weigh. Grep cannot answer the question at all: `blocks` and the far end of a
    soft link are derived and exist nowhere on disk, so no pattern will ever find them. And §1's
    token cost is a goal, not a nicety — an agent that must read every task file to find the next
    one has already spent what `context` exists to save, so the listing is a token-efficiency
    instrument (R-15) rather than a convenience. **The carve-out is exactly that**: selecting a
    subset by stored value or edge, rendered ready to use. Everything else this non-goal named
    stays out, and the decisions built on it stand — no `init` command (T-019), the pre-publish
    leak check remains a grep (T-013), and `deliverables` remains a validation rather than a
    command (T-002).

12. **Locating the plugin's own files for a caller the harness never served.** A release gate, a
    hook or a plain script has no `bin/` on `PATH` and is never handed a skill directory, and taskmd
    offers it no route to the launcher: where a plugin is installed belongs to the harness, and a
    route to it would be a promise about someone else's directory layout
    ([T-054](../tasks/T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) already
    establishes this project does not control that). **Added 2026-08-19 by
    [T-148](../tasks/T-148-decide-whether-a-caller-outside-a-served-skill-can-find-the-launcher.md)**,
    raised by an adopter who tried to follow this project's own advice from a release gate and could
    not. **The copied-skill install is not covered by this**: there the adopter chose the directory,
    so the launcher has a stable path a gate can name, and `README.md` says so where the two shapes
    are contrasted.

---

## 5. Constraints

**This is their home** — moved here from `../CLAUDE.md` by
[T-047](../tasks/T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md), which
needed the room for two rules that bind on every turn. These do not: they bind when something is
being written or built, and this is the first document that file tells you to read. It keeps the
one-line form and points here for the detail.

Everything this repository publishes must be:

- **Free of personal, client and machine data.** No real names, no absolute local paths, no drive
  letters, no hostnames. Write `<project>/tasks/` not a real path. Where a real identity is genuinely
  load-bearing evidence, it goes in `control/LOCAL-CONTEXT.md` — which is gitignored — and the tracked
  tree refers to it by the label that file defines. The check that enforces this is
  [`PUBLISHING.md`](PUBLISHING.md) §6; it is a grep rather than a CLI command because a leak check is
  not one of the things the CLI does, settled in T-013 under non-goal 11 above and still excluded
  after that non-goal's 2026-08-05 amendment.
- **Out-of-the-box.** Someone who clones it must be able to run it with no path editing. Resolve
  paths relative to the repository root, not the working directory.
- **Dependency-free.** Python standard library only. A tracker that needs `pip install` before it
  can list your tasks is a tracker people abandon.
- **Cross-platform.** Windows, macOS, Linux. Write files with an explicit `newline="\n"` — Python's
  default text mode rewrites every `\n` on Windows and breaks byte-for-byte comparison. Console
  output should survive a cp1252 terminal: reconfigure stdout to UTF-8 at startup — **and set
  `newline="\n"` there too**, because reconfiguring for encoding alone leaves the same rewriting in
  place for everything the tool *prints*. That half was written as if it were covered and was not:
  [T-020](../tasks/T-020-confirm-byte-identical-output-on-macos-and-linux.md) measured Windows against
  Linux and found the files identical and every console capture different, and
  [T-132](../tasks/T-132-give-the-console-the-same-line-ending-on-every-platform.md) closed it.
- **Humanized, if a stranger reads it before installing.** The rule, what it covers and the exception
  it carries: [`PUBLISHING.md`](PUBLISHING.md) (T-079).

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

**Closed on 2026-08-09 by [T-006](../tasks/T-006-package-document-and-publish.md)**, which published
the plugin and judged the list below item by item in its review. One thing was carried rather than
met, and it is **half met**: the plain-skill shape has been installed from the
published `v0.5.0` tag onto a profile that had never held any of this, and it works as the README
says. The plugin shape has not, because the profile that satisfies *never held it* has no `claude`
CLI and preparing one stops it being that profile.
[T-085](../tasks/T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) closed on
that boundary on 2026-08-16, with the half unmet and no successor task — so this is where the item
rests, not a gap something is working on. The
last bullet was amended at publication, in that task and not here, because the history carries one
absolute path the working-tree check cannot see.

Moved here from `BRIEF.md`, which now points at this section.

- Works on a clone with no configuration and no dependencies (R-18, R-20).
- `check` demonstrated **failing** on every class of problem it claims to catch (R-16).
- The measured `context` saving reproduced on a sample project and stated in the README (R-15).
- The method document carries no backend-specific instruction, and both bindings implement the
  same lifecycle (R-13, R-14).
- Every non-goal in §4 still holds.
- No personal, client or machine data anywhere in the repository (R-23).
