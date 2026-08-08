---
id: T-003
title: Write the skill that teaches the agent to use the CLI
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-002, T-008]
related: []
work_package: none
owner: maintainer
business_value: critical
effort: l
created: 2026-08-04
updated: 2026-08-07
deliverables:
  - plugin/skills/taskmd/SKILL.md
  - plugin/skills/taskmd/adopt.md
  - plugin/.claude-plugin/plugin.json
  - .claude-plugin/marketplace.json
  - .claude/settings.json
---

# T-003 — Write the skill that teaches the agent to use the CLI

## 1. Specify

**Outcome**
A skill that makes the agent run the CLI rather than read task files, and create tasks from the template.

**Why this one**
The failure mode is a skill that restates the CLI's rules in prose — a second copy that drifts. It must point, not describe.

**Requirements served**
R-6, R-7, R-8, R-9, R-21, R-22 (`docs/SCOPE.md`).

**Scope**
- In: the skill itself — the text a session is handed unasked, the body, and whatever further files
  its own tiering creates.
- In: the **tier design and the measurement of it** — what arrives before invocation, on invocation,
  and after that. R-21 leaves the number of tiers to this task and fixes only how the claim is
  falsified ([T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md)).
- In: the mechanism that makes [`docs/METHOD.md`](../plugin/docs/METHOD.md) §3.1–§3.3 fire, and what the
  agent does to create a task and after any write — by pointing at the project's binding.
- In: **making the skill live in this repository**, far enough to be measured on a real session here.
  This project runs its own method on itself, and a tiering claim that cannot be measured where the
  tool is built is exactly the shape of claim T-048 was raised to stop.
- In: reconciling [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)'s
  measurement. A skill's description is handed to a session unasked, which is
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md)'s own membership rule for
  tier 1 — so installing this skill here makes T-047's one-line margin wrong, and the task that
  falsifies a statement pays for it (T-022's precedent, applied in T-048).
- Out: packaging — the manifest a marketplace reads, install instructions, the README, and the second
  distribution shape. [T-006](T-006-package-document-and-publish.md) owns all four, and is blocked by
  this task. What is in above is the minimum that makes the skill measurable, not a published shape.
- Out: moving METHOD §3.1 and §3.3 into tier 1. That is T-047, which is blocked by this task
  precisely so that the loader exists before the move is designed against it.
- Out: any change to what METHOD says. If the skill needs the method to read differently, that is a
  finding and a new task (METHOD §3.3), not an edit made here.
- Out: the CLI's behaviour. A defect met while walking the skill becomes a task; T-025, T-029 and
  T-032 already hold the known ones.
- Out: the handoff tracker binding — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md).

**Inputs**
- [`docs/METHOD.md`](../plugin/docs/METHOD.md) §3 and §7 — the rules the skill must make fire, and the
  tier-3 files it hands over to.
- [`docs/SCOPE.md`](../docs/SCOPE.md) R-6…R-9, R-21, R-22, and §1 *Invisibility*.
- [`docs/BINDING.md`](../plugin/docs/BINDING.md) §1 and
  [`docs/bindings/local-markdown.md`](../plugin/docs/bindings/local-markdown.md) — the six operations, and
  what the agent still owes after a write.
- [`CLAUDE.md`](../CLAUDE.md) §*Working method* — this repository's tier model, which the skill fits
  into rather than replaces.
- [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md) §3 step 1 — what a
  session is handed for a skill it has not invoked, already measured. Extend it; do not re-derive it.
- [`tasks/_templates/task-template.md`](_templates/task-template.md) and
  [`taskmd/defaults/config.md`](../plugin/taskmd/defaults/config.md) — what a created task must carry for
  `check` to accept it.

**What the skill must carry that the CLI cannot enforce**
The CLI validates files; it cannot govern how the agent behaves. These three are the skill's real
content, and none of them is a restatement of something the tool checks:

They are **[`docs/METHOD.md`](../plugin/docs/METHOD.md) §3.1, §3.2 and §3.3** — serving R-6, R-7 and R-8
respectively. Their wording is not repeated here: this task exists to stop the skill becoming a
second copy of the method, and a task file that opens by making one would be arguing against itself.
Read §3 before specifying the skill; what the skill adds is the *mechanism* that makes those rules
fire on every turn, not the rules.

**Acceptance criteria**
- [ ] What a session pays for **without invoking the skill** is small enough to be worth carrying in
      every session, including every session that never does task work — judged against R-21
- [ ] No rule stated in the skill is also enforced by the CLI
- [ ] Creating a task through the skill produces a file `check` accepts
- [ ] Structured for progressive disclosure, with each tier entered only at its moment, and the
      tiering **measured on a real session** rather than described (R-21)
- [ ] The three behavioural rules above are present and each is testable by a walked example
- [ ] Nothing in the skill assumes the **work being tracked** is software — proven by walking a
      non-code task through it (R-9)
      <br>*Corrected at `specify` 2026-08-07. It read "Contains no software vocabulary", which R-18
      makes unmeetable: the skill's job is to name `python -m taskmd`, so it contains software
      vocabulary by construction. The intent — that nothing here assumes the tracked work is code —
      is unchanged and is what is now written.*
- [ ] Points at the method document rather than restating any part of it (R-22)
- [ ] The skill is invocable **both ways, demonstrated**: a request to do task work reaches it
      without the user naming it, and naming it reaches it
      <br>*Added at `specify` 2026-08-07 alongside the invocation answer below, which no criterion
      held. Shipping two invocation paths and demonstrating one is how the second becomes false —
      T-006's precedent for its two distribution shapes. The seven above predate this.*

**Open questions**
- **None outstanding.** The one below was answered by the maintainer; the two decisions this
  `specify` took in their place are recorded here rather than held open, because the maintainer
  asked for all five phases in one pass and a question that blocks with nothing delivered is the
  wrong answer to that. Both carry what was rejected, so either can be reversed on sight.
  - **This repository will run on the skill, not merely ship it.** *Rejected: write the skill and
    leave this project loading `CLAUDE.md` alone.* That is cheaper and it forfeits criterion 4 —
    the tiering could then only be described, in the one repository best placed to measure it, which
    is the failure mode T-048 exists to block. It also leaves T-028's "the loader for tier 2 is the
    skill" as an intention.
  - **Criterion 6 is corrected now rather than reinterpreted at `review`.** *Rejected: leave the
    wording and read it charitably later.* A criterion whose plain reading the deliverable must fail
    is decided at `review` by whoever is judging, which is what acceptance criteria exist to prevent.
- None. **Answered by the maintainer on 2026-08-07: both model-invocable and user-invocable.**
  Model invocation is what `docs/SCOPE.md` §1 *Invisibility* requires — the tool has to work without
  being asked for. User invocation costs one line of front-matter and is the only way to force the
  skill when the model does not trigger, or to find out why it did not. *Rejected: model-invocable
  only.* It would keep the user surface to the CLI, which is a real preference, but it makes a skill
  that fails to trigger undiagnosable.
- ~~Does the method document (T-008) become the skill's spine, or a file the spine points at?~~
  **Answered** — [T-008](T-008-write-the-backend-neutral-method-document.md) *Specify → Decisions*
  **D1**: standalone document at `docs/METHOD.md`; this skill points at it. The rationale lives
  there, not here.

**Why the new blocker**
`blocked_by` gained T-008: the skill teaches the method, so it cannot be written before the method
document exists without becoming the second copy this task is specifically meant to avoid.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Fix the tier design against the measurement rather than against the sibling's shape: which artifact occupies each tier, and what each tier is **forbidden** to carry. The forbidden half is the working part — every tier's failure mode is absorbing the one below it. | The tier table in §3 |
| 2 | Write the front-matter — the only text a session pays for without invoking anything — and nothing in it that is not needed to trigger. | `skills/taskmd/SKILL.md` front-matter |
| 3 | Write the body as a **router**: the first command, then which document to load at which moment, and the after-write step. No lifecycle, no field vocabulary, no exit criteria, no command reference — each of those has a home already. | The `SKILL.md` body |
| 4 | Write the once-ever path a project walks when it has no tasks yet: the folder, the schema, the binding, and where a project must carry METHOD §3.1 and §3.3 so they bind before task work is recognised. Paid once, so it is not in the body. | `skills/taskmd/adopt.md` |
| 5 | Make the skill live in this repository **without a second copy of it**: the repository declares itself as a plugin and enables it from its own tree by relative path. | `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `.claude/settings.json` |
| 6 | Verify by use, three walks: create a task through the skill and put the result to `check`; walk a **non-code** task through it; walk each of METHOD §3.1–§3.3 and show what makes it fire. | The three walks recorded in §3 |
| 7 | Measure every tier, and state plainly what this session **cannot** measure, with the task that will. | The measurement table in §3, and one new task |
| 8 | Reconcile what this task falsifies: T-047's tier-1 figure, `CLAUDE.md` *Status*, and the generated index. | T-047's log, `CLAUDE.md`, and the `check` / `index` / leak-check transcript |

**Deliverable shape — decided here.**

**D1 — Four tiers, and only one file is new.** description → body → [`docs/METHOD.md`](../plugin/docs/METHOD.md)
→ [`docs/method/<phase>.md`](../plugin/docs/method/). The method already had the last two and
[T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md) measured the first
two on a real session; this task supplies the two artifacts in the middle and the routing between
all four. Two further documents are entered laterally rather than as a tier — the project's binding,
when a write is about to happen, and `adopt.md`, once ever. *Rejected: a skill-local spine that
restates the method*, which is the failure this task was raised against and would put a fifth tier
between the body and METHOD for no fact that has no home.

**D2 — The skill's one home is `skills/taskmd/SKILL.md`**, the layout a plugin uses, with the
repository root as the plugin root. *Rejected: `.claude/skills/taskmd/`*, the project-level location
Claude Code reads without any install. It is simpler and it makes this repository's dogfood copy the
primary artifact, leaving [T-006](T-006-package-document-and-publish.md) to ship a **copy** of the
skill — two homes for one file, and the copy is the one that would go stale.

**D3 — This repository enables the plugin from its own tree, by relative path.** The harness resolves
a non-absolute `directory` marketplace path against the project root, so nothing machine-specific is
written down. *Rejected: an absolute path*, which R-23 forbids outright and which the pre-publish
check in `../CLAUDE.md` would catch — a dogfooding arrangement that fails the project's own
publishing rule is not an arrangement.

**D4 — Both invocation paths are the harness default, so neither is written.** The front-matter flags
are opt-**out** (`user-invocable: false`, `disable-model-invocation: true`); writing either would
remove a path the maintainer asked for. This costs zero lines rather than the one the `specify`
answer estimated — recorded because a cost estimate that turns out to be zero is still a corrected
fact.

**D5 — The walked examples live in this task's record, not in the skill.** Criterion 5 asks for a
rule that is *testable by* a walked example; the example is the test, and a test's home is the
`implement` evidence. *Rejected: examples in the body* — they would be re-read on every invocation
for the life of the project to prove something once.

**D6 — Step 7 exists because two criteria cannot be closed from this session, and that was
established by probe rather than assumed.** A skill written mid-session does not register: the
harness fixes its skill list at session start, confirmed by writing one and having the invocation
refused by name. The obvious way round — a fresh headless session — fails on an expired token. So the
half of criteria 4 and 8 that needs the harness to *hand the skill to a session* is carried, with a
child task, and everything else is measured here. *Rejected: reading it across from T-048's
measurement*, which established the mechanism for skills in general and is not evidence about this
one — the distinction this whole project is built on.

**Output paths**

- `skills/taskmd/SKILL.md` — the skill
- `skills/taskmd/adopt.md` — the once-ever setup path
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.claude/settings.json` — what
  makes it live here
- `tasks/T-047-…md`, `CLAUDE.md` — the reconcile
- `tasks/` — one new task from step 7; its id is not known until it is raised

## 3. Implement

### Step 1 — the tiers, and what each is forbidden to carry

| Tier | Arrives | Artifact | Must not carry |
| :--- | :--- | :--- | :--- |
| 0 | every session, unasked | the `description` field | anything but the trigger — it is the only text a session that never does task work pays for |
| 1 | on invocation | the `SKILL.md` body | the lifecycle, the phase exit criteria, the edge kinds, the field vocabulary, the ordering rule, what `check` catches. All six have homes |
| 2 | when the body points at it | [`docs/METHOD.md`](../plugin/docs/METHOD.md) | anything naming a file, a field or a command — it is backend-neutral by design |
| 3 | when a phase begins | [`docs/method/<phase>.md`](../plugin/docs/method/) | the spine's own rules |
| — | before a write | the project's binding | the vocabulary, which belongs to the project ([`docs/BINDING.md`](../plugin/docs/BINDING.md) §2) |
| — | once, ever | `skills/taskmd/adopt.md` | anything needed twice |

The forbidden column is the working half. Every tier's failure mode is absorbing the one below it,
and it is what a reviewer can check line by line.

### Steps 2–4 — what was written

`skills/taskmd/SKILL.md` is a **router**, not a manual: two commands, a four-row table of what to
load and when, one line saying a write is not finished until the binding's after-write step has run,
and two hazards that belong to nothing else. `adopt.md` holds the once-ever path — make the folder,
take or replace the schema, choose a binding, carry the two conduct rules where the harness loads
them unasked, confirm with `check`.

**One thing the body says that no other document could.** `context` prints every phase of a task at
once, including a plan nobody asked to be executed — so the body names METHOD §3.1 at that exact
hazard. It states the hazard, not the rule; the rule stays in METHOD.

### Step 5 — live in this repository, with no second copy

`.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` make the repository root a plugin
and a marketplace containing it; `.claude/settings.json` enables `taskmd@taskmd` from a `directory`
source at path `.`. The harness resolves a non-absolute directory path against the project root —
read out of the shipped binary rather than assumed — so nothing machine-specific is written down and
the pre-publish check has nothing to find.

### Step 6 — three walks

**Walk A — a task created through the skill, and `check` put to it.** Following SKILL.md's table to
the binding's *create*: next id after the highest present, template's shape, edges written in the
same write, then the after-write step. Produced
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) and
[T-051](T-051-say-where-a-project-s-task-template-lives.md).

```text
OK - 51 task(s), vocabulary valid, references resolve, no broken links
Wrote tasks/README.md - 22 active, 29 closed
```

`context T-050` then showed `PARENT T-003` — an edge written once, on the child, and read back from
the other end without being stored there.

**Walk B — a non-code project, from empty folder to a working graph.** A two-day workshop: choosing
its closing exercises, and confirming the room layout that gates them. Nothing but `adopt.md`,
`SKILL.md` and the binding was used. `adopt.md` step 1 was checked in both directions —

```text
CONFIG ERROR  taskmd/defaults/config.md: tasks_dir is 'tasks', but the project root has no such
folder. This project has no .taskmd/config.md, so taskmd is using its shipped default; create the
folder, or write a config naming a different one.
OK - 0 task(s), vocabulary valid, references resolve, no broken links
```

— the error being exactly the condition SKILL.md's fourth row uses to send a reader to `adopt.md`.
The graph was then made to fail before it passed:

```text
DANGLING      T-001.blocked_by -> T-002 does not exist
1 problem(s) over 1 task(s)
```

and once the venue task existed:

```text
OK - 2 task(s), vocabulary valid, references resolve, no broken links
T-002	proposed	-	specify	Confirm the room layout with the venue
```

`list --open --limit 1` answered with the **blocker**, not with the task that carries the value —
the cheap `xs` admin task pulled ahead by what it releases. Nothing in the walk required a word about
software, and the only software vocabulary in play was the tool naming itself.

**Walk C — the three conduct rules, each fired and each visible.**

| Rule | What fired it | Where it shows |
| :--- | :--- | :--- |
| §3.1 one phase per request | SKILL.md's first table row loads METHOD before anything is done to a task, and the body names §3.1 where `context` makes it hardest | Walk B's two tasks sit at `proposed`/`specify` with an empty plan table under them, untouched. The invitation is a pointer, not a request |
| §3.2 ask to the exit criterion, batched | `specify` on T-051 reached its criteria without the owner, so the one genuinely undecided thing — config key or convention — is recorded and handed to `plan` rather than asked now | T-051 *Open questions*; walk B's T-001 does the same for a question that gates a later phase |
| §3.3 surface, never absorb, never drop | Three discoveries, three traces, no silent fix | T-051 (a gap in the binding), T-050 (a criterion this session cannot close), and the tier-1 consequence below — reconciled rather than raised, because this task is what falsifies it |

### Step 7 — measured, and what could not be

| Tier | Artifact | Size |
| :--- | :--- | ---: |
| 0 | the `description` field | 74 words, 397 characters |
| 1 | the `SKILL.md` body | 46 lines |
| — | `adopt.md`, once ever | 43 lines |
| 2 | `docs/METHOD.md` | 150 lines |
| 3 | one phase file | 42–84 lines |

**What this session could not measure, established by probe rather than assumed.** A skill written
mid-session does not register: a throwaway skill was written to `.claude/skills/` and the harness
refused it by name, so the skill list is fixed at session start. `claude -p`, the fresh-session route,
exits on an expired OAuth token. So *this artifact being handed to a session* is
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md), and the two criteria that rest on
it are carried in §4 rather than argued from T-048's measurement of skills in general.

### Step 8 — reconcile

- **[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)'s margin is
  gone.** Its projection was 26 + 146 = 172 of 173. A skill's description is handed to a session
  unasked, so enabling this plugin here puts 397 characters into tier 1 by T-028's own membership
  rule — one physical line in the file, four or five lines' worth of text. Recorded in T-047's log,
  not acted on: what leaves tier 1 is that task's `plan` to decide, and trimming from outside would
  be the cut chosen to fit a number T-028 and T-047 both refuse.
- **`CLAUDE.md` *Status*** said the skill was still to write.
- The membership rule itself needed no edit, which is the property T-028 claimed for it: tier 1 is
  *what the harness loads unasked*, so the description joined the set without anyone touching the
  budget.

**Decisions & assumptions**

- **The walked examples live in this record, not in the skill.** — Criterion 5 asks for rules
  *testable by* a walked example; the example is the test, and a test's home is the `implement`
  evidence. Examples in the body would be re-read on every invocation for the life of the project to
  prove something once. — 2026-08-07
- **`adopt.md` is a lateral file, not tier 4.** — It is not deeper in the same path; it is a
  different path, walked once. Calling it a tier would suggest every project pays for it on the way
  to the method, which is the opposite of true. — 2026-08-07
- **Both invocation paths are the harness default, so neither flag is written.** — The front-matter
  flags are opt-out (`user-invocable: false`, `disable-model-invocation: true`); writing either
  removes a path the maintainer asked for. The `specify` answer estimated this at one line of
  front-matter; it is zero. — 2026-08-07
- **The description is 74 words, and that is the whole always-paid cost.** — Long enough to name the
  project shape that gates it, the phases, and the words a user would actually say. Compared against
  the sibling skill T-048 measured at ~65 words, this is the same order and buys a gate that skill
  does not need. — 2026-08-07

**Outputs produced**

- [`skills/taskmd/SKILL.md`](../plugin/skills/taskmd/SKILL.md) — the skill
- [`skills/taskmd/adopt.md`](../plugin/skills/taskmd/adopt.md) — the once-ever setup path
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.claude/settings.json` — what
  makes it live here
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md),
  [T-051](T-051-say-where-a-project-s-task-template-lives.md) — raised, and created through the skill
- [`CLAUDE.md`](../CLAUDE.md) and
  [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — the reconcile

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| What a session pays for **without invoking the skill** is small enough to be worth carrying in every session, including every session that never does task work — judged against R-21 | met | One front-matter field: 74 words, 397 characters. The comparison that makes it judgeable rather than asserted is the sibling skill T-048 measured at ~65 words — same order, and the extra buys the clause that gates it on the project's shape so it does not fire in projects that do not track tasks this way. Nothing else is in the front matter: no `argument-hint`, no flags, because both invocation paths are the default |
| No rule stated in the skill is also enforced by the CLI | met | Checked line by line, not by impression, and two lines were cut for it: `adopt.md` had described what `check` reports and what an absent task folder does, both of which are the tool's own and both now left to the tool. What remains is behaviour no command can reach — run a command rather than read the folder, load a document at its moment, and finish a write with the binding's after-write step. That last is the sharpest case and it holds: taskmd never writes a task file, so the edit that made the index stale is one it never saw |
| Creating a task through the skill produces a file `check` accepts | met | Twice, on two projects. In this one, T-050 and T-051 were created by following SKILL.md to the binding's *create* — `OK - 51 task(s)`, and `context T-050` read back `PARENT T-003` from an edge written once on the child. In the workshop project, two tasks from nothing: `OK - 2 task(s)` |
| Structured for progressive disclosure, with each tier entered only at its moment, and the tiering **measured on a real session** rather than described (R-21) | **carried — [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)** | The structure is built and every tier is measured (§3 step 7), and tiers 2 and 3 were entered at their moments in this session — the method spine when task work began, `specify.md` when that phase did, the binding before the first write, and no phase file read in advance. What is **not** measured is the one transition only the harness can show: description → body, for this skill. A probe settled that it cannot be measured here — a skill written mid-session is refused by name, so the skill list is fixed at session start — and the headless route exits on an expired token. Reading it across from T-048 was refused: that measured the mechanism for skills in general, which is an argument about this one |
| The three behavioural rules above are present and each is testable by a walked example | met | §3 walk C, one row each, and each names what fired it and where it shows rather than asserting compliance. The strongest is §3.1: the workshop project's two tasks sit at `specify` under an empty plan table, which is the pointer-is-not-authorization case in its purest form. The rules are present as **mechanism** — the body's first table row loads the method before anything is done to a task — and their wording stayed in METHOD, which is what the next criterion asks |
| Nothing in the skill assumes the **work being tracked** is software — proven by walking a non-code task through it (R-9) | met | The workshop walk used `adopt.md`, `SKILL.md` and the binding and nothing else, from an empty folder to a graph with a dependency in it, and needed no word about software. The one thing that had to be said in software terms was the tool naming itself, which is what the criterion was corrected at `specify` to allow. A second result fell out of the same walk: `list --open --limit 1` answered with the `xs` venue task rather than the `high` one it blocks, so the ordering rule behaves on non-code work exactly as `taskmd/defaults/config.md` describes |
| Points at the method document rather than restating any part of it (R-22) | met | The body's row for `docs/METHOD.md` says four words about it — *it is the method* — and the load table names roles rather than contents, because a table of contents is a summary and a summary is a copy. The one place the skill names a method section, §3.1, states the **hazard** this tool creates (`context` prints a plan nobody asked to be executed) and not the rule that answers it |
| The skill is invocable **both ways, demonstrated** | **carried — [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)** | The front matter is correct for both — the flags are opt-out and neither is written — and the registration is in place. Neither path can be exercised from the session that wrote them, for the same reason as criterion 4. Recorded as carried rather than met: "the defaults are right" is exactly the kind of claim this project does not accept about behaviour |

Six met, two carried, and the two carried are the same fact seen twice — the harness cannot hand a
session a skill that session has just written. That was **established rather than assumed**, which is
the part worth defending: a throwaway skill was written and refused by name, and the fresh-session
route was tried and failed on an expired token. The alternative on offer was to argue from T-048's
measurement that the mechanism applies here too, and the whole reason R-21 names a measurement is
that this project has already believed one such argument for weeks.

**Also checked, beyond the criteria**

- **The reconcile changed T-047's character, not just its number.** Its margin was one line; tier 1 is
  now 148 + 26 = 174 against 173 *before* the description is counted at all. Recorded in its log with
  the two things its `plan` now has to settle: how a character count is weighed against a line bound,
  and that tier 1 from here on grows when a skill is added, not only when `CLAUDE.md` is edited.
- **`CLAUDE.md`'s membership rule needed no edit to admit the description**, which is the property
  T-028 claimed for it and the first time that claim has been tested by something actually joining
  the set. Only the two sentences that had become false were touched.
- `check` clean on 51 tasks; index regenerated; suite 114/114; pre-publish check prints nothing with
  its exclusion and exactly five lines without it, all in its own fixture.
- The walk projects were built outside the repository and are not part of it.
- **Four fixes applied during review, from re-reading the deliverable rather than the record.** The
  largest is real: the body opened by asserting tasks are Markdown files and then told the reader to
  load *this project's* binding, which is inconsistent for any project not on that backend. It now
  says the commands are the local-Markdown backend's and that another backend's operations come from
  its binding, with everything below unchanged — which is R-14 stated where an agent will meet it.
  `adopt.md` also cited a task file in this repository's own backlog as evidence for what a session
  is handed; it points at R-21 instead, since a shipped setup document that resolves into the
  developing project's history breaks the moment packaging decides not to ship `tasks/`. The other
  two were wording. Body 43 → 46 lines; the description, the only always-paid tier, did not change.

**Child fix tasks raised**
- **[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)** — carries criteria 4 and 8.
- **[T-051](T-051-say-where-a-project-s-task-template-lives.md)** — not a carried criterion. A
  finding: the binding's *create* says "copy the template" and nothing in the schema or the binding
  says where a project's template is. METHOD §5's distinction applies — this task did not make it
  false, so it is raised rather than reconciled.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Six criteria met, two carried by [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md), and the two carried are one fact seen twice: a session cannot be handed a skill it has just written. The deliverable is deliberately small — a 74-word description, a 43-line router, a 43-line setup path — because everything a longer skill would have said already has a home, and the tier table in §3 states what each tier is **forbidden** to carry so a reviewer can check that line by line instead of taking it on trust. Two rules the tool already owns were cut from `adopt.md` during review for exactly that reason. The verification that matters is the workshop walk: a two-day training course, from an empty folder to a graph with a dependency in it, using nothing but the skill, its setup file and the binding — and `list` answering with the cheap blocker rather than the valuable task it releases, on work with no code in it at all. |
| 2026-08-07 | → review | Eight steps worked in order. The skill is a router: two commands, a four-row load table, one line making a write unfinished until the binding's after-write step has run, and the one hazard nothing else could state — `context` prints a plan nobody asked to be executed, which is where METHOD §3.1 bites hardest with this tool. Three walks are the evidence, and the non-code one did double duty by exercising `adopt.md` from an empty folder. Two tasks raised rather than absorbed: T-051, because the binding's *create* names a template that no project can locate, and T-050, because the harness fixes its skill list at session start. Reconciled on the way out: T-047 is now **over** its bound rather than one line under, since tier 1 gained a member that is not a file, and `CLAUDE.md`'s membership rule admitted it without being edited — the first real test of the property T-028 claimed for it. |
| 2026-08-07 | → planned | Eight steps and six shape decisions. **The load-bearing one was taken by probe, not by argument:** a skill written mid-session does not register — the harness fixes its skill list at session start, shown by writing a throwaway skill and having it refused by name — and a fresh headless session, the obvious way round, fails on an expired token. So the part of criteria 4 and 8 that needs the harness to hand this skill to a session is carried to a child task, and reading it across from T-048's measurement was rejected: T-048 established the mechanism for skills in general, which is not evidence about this one. Two smaller findings on the way. Both invocation paths are the harness **default** — the front-matter flags are opt-out — so the maintainer's answer costs zero lines, not the one their note estimated. And a `directory` marketplace path is resolved against the project root when it is not absolute, which is what lets this repository run its own plugin from its own tree without writing a drive path R-23 forbids. |
| 2026-08-07 | (already `specified`) | `specify` re-run against [`docs/method/specify.md`](../plugin/docs/method/specify.md) and found two of its six steps had never been done: there was no **Scope** and no **Inputs**, so the boundary that stops the work expanding was missing from a task whose neighbours are T-006 (packaging), T-047 (the tier-1 move) and T-005 (the handoff binding) — three plausible places for it to spread. Both are now written, with each exclusion naming the task that owns it. One criterion corrected and one added, both marked in place. **One discovery, surfaced rather than absorbed:** a skill's `description` is handed to a session unasked, so installing this skill here adds to tier 1 by T-028's own membership rule — which makes T-047's one-line margin wrong. Taken into scope as reconcile debt on T-022's precedent rather than raised as a task, because this task is what falsifies it. |
| 2026-08-07 | (no status change) | Criteria 1 and 4 corrected by [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md), which settled what "always-loaded" is relative to. Criterion 1 said the skill body must be short enough to load on every turn, and the body does not load on every turn — measured, not argued: what a session is handed for an un-invoked skill is its description alone. So the criterion was false rather than imprecise, and it now points at R-21 instead of carrying a second copy of the property. Criterion 4 kept its intent and lost the unqualified phrase. Nothing else changed, and the skill's design is still entirely this task's. |
| 2026-08-07 | → specified | Invocation answered: both. Nothing else was outstanding, and the second question was already closed by T-008 D1. What now rests on this task is worth stating: T-028 made `docs/METHOD.md` tier 2, loaded when task work starts, and this skill is the loader — so T-047 waits on it, and the tiering is a decision rather than a working arrangement until it is built. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
