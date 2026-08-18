---
id: T-177
title: Decide whether check runs the checks that never look at a task file
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-163, T-178, T-179]
work_package: M6
owner: maintainer
business_value: high
effort: m
created: 2026-08-18
updated: 2026-08-18
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-177 — Decide whether check runs the checks that never look at a task file

## 1. Specify

**Outcome**
A decision, and if it is yes the behaviour, on whether `check` still runs in a project whose
`tasks_dir` does not resolve — reporting the checks that do not read a task file, and refusing only
the ones that do.

**Why this one**
**Measured on 2026-08-18, reading `cmd_check`: it runs 17 checks, and five of them take no `tasks`
argument at all** — `check_links`, `check_wide_rows`, `check_unreachable_templates`,
`check_template_fields` and the `check_config_drift` advisory. They walk the document tree from the
project root. The task folder is not an input to any of them.

**A migrated project loses all seventeen anyway**, because the config error is raised while loading,
before `cmd_check` is entered. So the shipped listing's *No validator. Everything it checked is now
unchecked* is true as behaviour and **overstated as necessity**: roughly a third of the validator
never needed the folder, and the documents it reads — the binding, the method, the project's own
docs and deliverables — are exactly what a migrated project still keeps locally.

**This is the cheapest large thing available to a migrated project**, and it is why it is raised
ahead of the two beside it. It adds no command (non-goal 11 holds at four), makes no network call
(non-goal 5), and writes nothing (non-goal 6). It changes when the loader refuses, not what checking
means.

**It is a decision and not a fix, because the honest answer might be no.** A `check` that prints
`OK` in a project it cannot validate is a worse failure than one that refuses, and the *Scope* line
is the mechanism that would have to carry the difference.

**Scope**
- In: whether the four checks and one advisory that take no `tasks` argument should run when the
  task folder does not resolve
- In: what such a run must print so that nobody reads a document-only pass as a full one — the
  existing `Scope` line is the candidate and may not be enough
- In: whether the refusal message changes, given it currently tells a migrated project the commands
  do not apply
- Out: any check that reads a task file. Those refuse, and the reason is not in doubt
- Out: reading the remote backend. Non-goal 5 keeps every network call out of the core; that is
  [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s subject and it lives in a
  binding, not here
- Out: a fifth command or a flag that means "documents only" if the answer can be reached without
  one

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `cmd_check` and the five check functions whose signatures
  carry no `tasks`
- `tests/fixtures/migrated-away/` — the project shape this is about, and `broken-tasks-dir`, which
  is the shape that must keep refusing
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *What is gone and has no replacement here*,
  item 1, which this task would make partly false and which is then its to correct

**Acceptance criteria**
- [ ] The ruling is yes or no, with the rejected option named
- [ ] If yes, it names exactly which checks run and which refuse, against the measured signatures
      rather than against a description of them
- [ ] It judges whether the existing `Scope` line can carry a document-only pass, rather than
      assuming it can — the whole case rests on that line being read correctly
- [ ] It says whether a migrated project and a mistyped `tasks_dir` are treated alike, and on what
      the tool distinguishes them if not
- [ ] The answer is reached by running against a fixture that **has documents**. The shipped
      `migrated-away` fixture holds a config and nothing else, so a run against it cannot tell a
      working rule from a silent one
- [ ] No fifth command and no new flag (non-goal 11), or a stated reason one is unavoidable
- [ ] The shipped listing's item 1 is corrected, since this task is what makes it overstated

**Open questions**
- **Does a document-only pass mislead more than a refusal helps?** The whole case rests on the
  `Scope` line being read. It is printed on both branches today and was built for exactly this class
  of misreading, but it has never had to carry a *pass* that covers a third of what the reader thinks
  it covers. **Answer at `specify`, by running the command against the fixture and reading the output
  as an adopter would** — not by arguing about it.

  **Answered 2026-08-18, by running it: no — but only because the `Scope` line is changed as part of
  the same ruling.** Left as it is, it would mislead, and the run says so in one line.

  Built a migrated project that keeps its own documents — the shipped fixture's config verbatim, plus
  a README and a method document carrying two dead links and an over-wide table row — deferred the
  `tasks_dir` guard, and ran the five checks that take no `tasks` argument:

  ```text
  BROKEN LINK   README.md -> docs/NOPE.md
  BROKEN LINK   docs/METHOD.md -> ../docs/ALSO-GONE.md
  status: shipped default adds 'specified', 'planned', ...; this project's row does not carry them
  Scope  every document read; no git here, so .gitignore was not consulted
  ```

  **Two real defects, currently unreportable**, in a project that today gets `CONFIG ERROR` and exit 2
  and is told the commands do not apply. That is the case for yes.

  **And the last line is the case against, in the tool's own words.** *"every document read"* is true
  and reads as *everything checked*. A reader who has just been handed two broken links has no signal
  that the task half was not examined at all — the `Scope` line reports documents it skipped, and has
  no vocabulary for a half of the validator that never ran. So the existing line **cannot** carry this
  pass. It does not need replacing, it needs the omission it was never asked to describe.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reproduce the present refusal on both fixtures, so the two shapes are distinguished by what the tool actually prints | The two outputs, in §3 |
| 2 | **Build a migrated project that has documents**, since the shipped fixture has none, and run the five no-`tasks` checks against it with the folder guard deferred | What they report, in §3 |
| 3 | Read that output as an adopter would and judge the `Scope` line against it | The answered question in §1 |
| 4 | Rule, naming which checks run, which refuse, and how the two failure shapes are told apart | The ruling, in §3 |
| 5 | Correct item 1 of the shipped listing, which this task makes overstated | The edited binding document |

**Step 2 exists because step 1 cannot answer anything.** The `migrated-away` fixture holds a config
and nothing else, so every document check would report zero and a broken rule would look identical to
a working one.

**Decisions taken at `plan`**

- **The ruling is separated from its implementation.** — Same reason as
  [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md): a ruling that arrives
  with its code cannot be reviewed on its merits. *Rejected: shipping the loader change here.*
  — 2026-08-18
- **The listing correction is not deferred with it.** — Item 1 is overstated **as necessity** today,
  before any code changes, because a third of the validator never needed the folder. That is a true
  statement now and does not wait on the fix. — 2026-08-18

**Outputs this task will produce**

- tasks/T-177-run-the-checks-that-need-no-task-folder.md — §3, the ruling and its evidence
- plugin/skills/taskmd/docs/bindings/github-issues.md — item 1, corrected

## 3. Implement

### Step 1 — the present behaviour, both shapes

```text
$ taskmd check --root tests/fixtures/migrated-away
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder.
Create it, or correct tasks_dir. Or nothing here is broken and these commands do not apply:
id_width is 'none', which says a backend allocates the ids, so this project's tasks are not
local files.                                                                          EXIT=2

$ taskmd check --root tests/fixtures/broken-tasks-dir
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'taks', but the project root has no such folder.
Create it, or correct tasks_dir.                                                      EXIT=2
```

**The tool already tells the two apart** — the first carries a clause the second does not, keyed on
`id_width: none` meaning a backend allocates the ids. That distinction is the ruling's whole
mechanism, and it is already shipped and already tested.

### Step 2 — where the refusal actually happens

`load_schema` raises from `_check_tasks_dir` before `cmd_check` is entered — confirmed by calling it
directly and reading the traceback, not by reading the source. So all seventeen checks are lost to a
guard that only twelve of them need. The five that take no `tasks` argument are `check_links`,
`check_wide_rows`, `check_unreachable_templates`, `check_template_fields` and the
`check_config_drift` advisory, confirmed against their signatures in `cli.py`.

Their output on a migrated project that keeps documents is in §1's answered question: **two broken
links and one advisory**, none of which anything reports today.

### Step 3 — the ruling

**Yes, with three parts.**

1. **The five document checks run when `tasks_dir` does not resolve *and* the config says a backend
   allocates the ids** — `id_width: none`, the discriminator the message already uses. The twelve
   that read a task file do not run.
2. **A mistyped `tasks_dir` keeps refusing exactly as it does now.** There the folder is supposed to
   exist, the project is broken rather than migrated, and a partial pass would help nobody. This is
   why the ruling is not "run the five whenever the folder is missing".
3. **The `Scope` line gains the omission it has no words for.** It reports documents it skipped and
   says *every document read*; it must also say that the task half was not checked and why. Without
   this the ruling is refused — §1's question is answered *no* only on this condition.

*Rejected: no, keep refusing.* It is the safe answer and it costs a migrated project the two defects
found above, in documents it still keeps locally, for a folder none of those checks reads.
*Rejected: a `--documents-only` flag.* Non-goal 11 holds at four commands, and a flag asks the user
to know a distinction the config already states. *Rejected: running the five whenever the folder is
missing.* It would turn a typo into a partial pass, which is the misreading this whole task is
about.

**No command and no flag is added**, which criterion 6 asked for: everything above is a change to
where one guard sits and what one line says.

### Step 4 — the listing corrected

Item 1 of *What is gone and has no replacement here* said `check`'s verification is entirely lost.
Annotated rather than rewritten, per METHOD rule 5: it is true of today's behaviour and overstated as
necessity, and the measurement that shows why is here.

**Decisions & assumptions**
- Both `plan` decisions held. — 2026-08-18
- **Assumption, recorded as one**: the five signatures are the whole no-`tasks` set. Read from
  `cli.py` on 2026-08-18 and consistent with §1's independent count of 17 total. — 2026-08-18

**Outputs produced**
- plugin/skills/taskmd/docs/bindings/github-issues.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Yes or no, with the rejected option named | **met** | §3 step 3: yes, in three parts, with three rejections named including the two that look like the ruling but are not |
| Names exactly which checks run and which refuse, against measured signatures | **met** | The five named from `cli.py`'s signatures; the other twelve refuse. Confirmed by calling the loader and reading where it raises, not by reading prose about it |
| Judges whether the existing `Scope` line can carry a document-only pass | **met** | It cannot, and the run said so: *every document read* is true and reads as *everything checked*. Part 3 of the ruling is conditional on fixing it — the answer is *no it does not mislead* **only** if that changes |
| Says whether a migrated project and a mistyped `tasks_dir` are alike, and what distinguishes them | **met** | Not alike. `id_width: none` is the discriminator, and it is one the shipped message already uses — the ruling adds no new signal |
| Reached by running against a fixture that has documents | **met** | The shipped fixture has none and would have proved nothing; §1's answer records the built one and what it found |
| No fifth command and no new flag, or why one is unavoidable | **met** | Neither. A `--documents-only` flag is named and rejected |
| The shipped listing's item 1 is corrected | **met** | §3 step 4, annotated rather than rewritten |

**Open questions, re-read before closing** (procedure step 5)

§1's only question is answered, by running the thing as it demanded. Its answer is **conditional**,
which is the part a later reader must not lose: the ruling is *yes* only with the `Scope` change, and
that condition is carried into the child task's criteria rather than left in this record alone.

**Child fix tasks raised**
- [T-185](T-185-run-the-document-checks-in-a-project-whose-tasks-moved.md) — implement the ruling

## Log


| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | `specify` through `review` in one session under the standing grant. **Ruled yes, conditionally**: the five checks that take no `tasks` argument run when the folder is missing *and* `id_width: none` says a backend allocates the ids; a mistyped `tasks_dir` keeps refusing; and the `Scope` line must gain the omission it has no words for, without which the answer is no. **The question was settled by running it, as §1 demanded** — and the shipped `migrated-away` fixture could not settle it, holding a config and no documents, so a working rule and a silent one would have scored alike. Built one that keeps documents: two broken links and an advisory, none of them reportable today. The same run produced the argument against — *every document read* is true and reads as everything checked. Implementation is [T-185](T-185-run-the-document-checks-in-a-project-whose-tasks-moved.md); the listing correction was not deferred with it, because item 1 is overstated as necessity today. |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about what survives a migration to GitHub Issues. **The finding is a measurement, not an opinion**: `cmd_check` runs 17 checks and 5 take no `tasks` argument, while the config error aborts before any of them run. Checked against `docs/SCOPE.md` §4 before raising — it touches non-goals 5, 6 and 11 and violates none, which is why it is raised in this shape rather than as a GitHub-aware validator. `high` because it is the largest thing a migrated project could get back for the least weight. **Not covered by any standing authorisation.** |
