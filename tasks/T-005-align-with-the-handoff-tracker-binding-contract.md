---
id: T-005
title: Align with the handoff tracker-binding contract
type: research
status: done
phase: review
parent: null
blocked_by: [T-009]
related: [T-002]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-04
updated: 2026-08-18
deliverables: [plugin/skills/taskmd/docs/HANDOFF.md, plugin/skills/taskmd/SKILL.md]
---

# T-005 — Align with the handoff tracker-binding contract

## 1. Specify

**Outcome**
Either a contributed/updated `local-markdown-dir` binding, or a documented statement of how taskmd projects should configure handoff.

**Why this one**
The binding states *"the folder is the index"*, which is false for any project using a generated one — see the Handoff repo's improvement brief, F1. taskmd is exactly such a project, so it will hit this. Doing it after the binding changes avoids building against a contract about to move.

**Requirements served**
R-24 (`docs/SCOPE.md`).

**Two binding contracts, not one**
Kept distinct because they run in opposite directions, and conflating them is the easy mistake
here:

- **handoff's** contract (`find`/`read`/`create`/`update`/`reference`) lets handoff drive *a*
  tracker. This task makes taskmd be that tracker.
- **taskmd's own** contract (T-009) lets taskmd drive *a* backend — local files or GitHub Issues.

They may share vocabulary, and T-009 owns that decision. Hence the new blocker.

**Acceptance criteria**
- [ ] ~~The handoff F1 outcome is known before this is designed~~
      **Replaced on 2026-08-10 by [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md)**,
      which found it unfalsifiable rather than unmet: nobody could say what "known" meant, and the
      label was defined nowhere a reader could reach. What replaces it keeps the maintainer's
      2026-08-07 scoping intact — the recipe half does not wait, the contribution half does.
- [ ] Before the **upstream contribution** is designed, this task records whether the handoff
      binding still states "the folder is the index", checked against the binding as it then stands,
      and names where that was checked. The **v1 recipe** does not wait on it
- [ ] A taskmd project can be driven by handoff with no hand-written workaround
- [ ] `tracker_lint` documented as the way the invariant is enforced
- [ ] Works for a taskmd project on **either** backend — a project on GitHub Issues must be
      resumable through handoff too, or the limitation is stated (R-14, R-24)
- [ ] The binding states the assumptions it makes about the adopting project — the F1 fix applied
      to taskmd's own contribution rather than only asked of others

**Open questions**
- None. **Answered by the maintainer on 2026-08-07: ship a config recipe for v1, and propose the
  binding upstream after publishing.** R-24 asks for interoperation, not for adoption by another
  project: a recipe is verifiable inside this repository and blocks nothing, where an upstream
  contribution depends on someone else's review and would sit in T-006's path. *Rejected:
  contributing upstream now.* It is the better long-term shape — the handoff core resolves its
  `tracker` key to a file in its own `bindings/`, so a recipe alone is a binding that project cannot
  load — which is why it is deferred rather than dropped.
  *(2026-08-18: **the deferred half is now dropped, by the maintainer**, on evidence rather than by
  reversal. The deferral existed to keep an F1 fix moving upstream; `plan` found F1 already fixed
  there — see the log — so the contribution has nothing left to carry. The 2026-08-07 reasoning is
  untouched above because it was right about the world it was written in: a recipe alone is still not
  a loadable binding, and that remains the reason this task ships a recipe and not a binding. What
  changed is the thing the contribution was for, not the argument. **Consequence for the criteria**:
  criterion 2's trigger — "before the upstream contribution is designed" — can no longer fire, so
  step 1 records the check on its own merits and `review` judges it on what was recorded, not on
  whether a contribution was designed.)*
- **What criterion 1's F1 dependency now covers.** It stands, but the answer scopes it: the v1
  recipe does not wait on the F1 outcome; the upstream contribution does. *(2026-08-10: criterion 1
  has since been replaced by T-033 with wording that can be checked; this scoping is carried into
  the replacement unchanged, which is why the note is annotated rather than rewritten.)*

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Before anything is designed on top of it**, check whether the handoff `local-markdown-dir` binding still states "the folder is the index", against the binding as it now stands, and name the file and sections the check read | A dated finding in §3, naming where it was checked and what it leaves for the rest of this task |
| 2 | Map each `tracker_*` key that binding reads onto the taskmd fact that answers it, and mark the ones it leaves to the project | A key-by-key table in §3, one row per key the binding names |
| 3 | Settle which of the binding's two index topologies a taskmd project is, and the exact command that enforces the invariant for it | A recorded decision in §3 naming the topology and the `tracker_lint` command |
| 4 | Test the derived recipe against this repository's own `.handoff/config.md` — the one live specimen — and record every key it under-declares | The comparison in §3, and the corrected local config where the recipe demands one |
| 5 | **Before the recipe is written**, answer whether a taskmd project on the GitHub backend is resumable through handoff, by reading handoff's own `github-issues` binding against taskmd's | A recorded answer in §3: the second recipe, or the limitation with the reason it stands |
| 6 | Write the recipe into its chosen home | plugin/skills/taskmd/docs/HANDOFF.md |
| 7 | Make it reachable at the moment a session would need it, rather than in advance | The edited row in plugin/skills/taskmd/SKILL.md |

**Steps 1 and 5 are placed early because either can move what step 6 writes.** Step 1 is the
cheaper of the two and it has already half-answered itself during planning — see the first decision
below. Step 5 can turn one recipe into two, or into one with a stated limitation, and finding that
out after the document is drafted means drafting it twice.

**Decisions taken at `plan`**

- **The F1 check is kept as a step even though the upstream contribution it gates is deferred.** —
  Criterion 2 scopes it to *before the upstream contribution is designed*, and the owner's 2026-08-07
  answer defers that contribution out of v1, so the criterion's trigger does not fire in this task.
  It is kept anyway because planning had to read the binding to plan at all, so the check costs
  nothing now, and because [`docs/BRIEF.md`](../docs/BRIEF.md) *Interop* still states the premise as
  current. *Rejected: leaving the criterion untriggered*, which would have review record it as not
  applicable while the stale sentence stands unchallenged and unowned. — 2026-08-18
- **The recipe ships inside `plugin/skills/taskmd/`, not under the repository's `docs/`.** — Since
  T-053 the plugin boundary is the `plugin/` subtree, so an adopter installing the plugin never
  receives the repository's `docs/`. *Rejected: a repository-level document*, which would be a recipe
  the people who need it cannot read. — 2026-08-18
- **It is a new document, not a section of [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md).**
  — §1 above keeps the two contracts distinct on purpose: they run in opposite directions, and that
  document is taskmd's own backend contract. *Rejected: extending `BINDING.md`*, which would put the
  contract taskmd *offers* and the contract it *consumes* under one heading — the exact conflation §1
  names as the easy mistake here. — 2026-08-18
- **`deliverables` stays empty until step 6 lands.** — A plan lists what is promised; the field
  records what exists. — 2026-08-18

**Outputs this task will produce**

- tasks/T-005-align-with-the-handoff-tracker-binding-contract.md — §3, the F1 check, the key
  mapping, the topology decision, the specimen comparison and the either-backend answer
- plugin/skills/taskmd/docs/HANDOFF.md — the recipe
- plugin/skills/taskmd/SKILL.md — the row that makes it reachable

## 3. Implement

### Step 1 — the F1 check, and where it was read

**The handoff `local-markdown-dir` binding no longer states "the folder is the index".** Checked
2026-08-18 against the binding as installed on this machine, at
`bindings/local-markdown-dir.md` in the handoff skill package. Three sections carry the remedy:

- ***Index topology*** — presents folder-as-index and *a central index exists* as two supported
  shapes rather than one premise, and splits the second into **generated** (never hand-edit;
  regenerate after any write) and **maintained** (update in the same pass);
- ***Keeping the tracker consistent*** — makes `tracker_lint` the invariant-enforcement hook, run
  after every create and update, exiting non-zero on drift, and names it as what gives the core's
  reconcile sweep a concrete check;
- ***Assumptions this binding makes*** — the file-set-is-authoritative assumption now carries the
  clause *"unless the project declares a central index"*.

**What this leaves for the rest of the task.** Criteria 3 and 5 describe work that already exists
upstream, so this task neither invents `tracker_lint` nor asks another project to state its
assumptions — it *uses* the first and *imitates* the second in its own deliverable. The premise in
[`docs/BRIEF.md`](../docs/BRIEF.md) *Interop* — "that binding assumes the folder is the index" — is
now false as a statement about the present. It is left standing there and corrected in §4's residual
rather than edited here, because it is this task's finding to carry and a silent fix would erase it.

### Step 2 — what each key the binding reads is answered by

| Key handoff reads | Answered by | Note |
| :--- | :--- | :--- |
| `tracker_dir` | taskmd's `tasks_dir` | Same fact, two configs; the recipe says to copy from yours, not from the example |
| `tracker_id_prefix` | taskmd's `id_prefix` | |
| `tracker_template` | Convention, not a taskmd key | taskmd discovers `_task-template.md`; nothing in its schema names one |
| `tracker_lint` | No taskmd key — the **command** `taskmd check` | The hook. Step 3 |
| `tracker_closed_dir` | Deliberately unset | Step 3 |
| id zero-padding | Neither — **inferred** | taskmd configures `id_width`; the binding says to match the width of existing ids. Two mechanisms, same result, no key to map |

### Step 3 — topology, and the command that enforces it

**A taskmd project is topology (b), generated.** `tasks/README.md` is built from the task files by
`taskmd index` and never hand-edited. *Rejected: describing taskmd as folder-as-index*, which is what
the pre-fix binding would have forced and is the exact false claim F1 was raised about — the folder
is authoritative for content, and the index is a second durable home that can disagree with it.
— 2026-08-18

**`tracker_lint` is `taskmd check`.** *Rejected: a purpose-written lint script*, which would be a
second checker of the same invariant and would drift from the one the project already runs.
— 2026-08-18

**`tracker_closed_dir` stays unset.** taskmd records closure as a status value and leaves the file
where it is, so every link into a task keeps resolving after it closes. *Rejected: pointing it at a
closed folder*, which moves files out from under existing links to record a fact the front matter
already carries. — 2026-08-18

### Step 4 — tested against this repository's own config

`.handoff/config.md` is the one live specimen: this project has been driven by handoff through that
binding since before the recipe existed. Comparing it to the recipe found **one key missing and
nothing wrong**:

| Recipe says | The specimen had | Verdict |
| :--- | :--- | :--- |
| `tracker_dir`, `tracker_id_prefix`, `tracker_template` | all three, correct | matched |
| `tracker_closed_dir` unset, with the reason | unset, with the reason | matched |
| `tracker_lint: taskmd check` | **absent** | **under-declared — fixed** |

**The missing key is the one that matters**, which is the finding rather than a coincidence: it is
the only key in the recipe that does anything at run time, and the project it was missing from is
the one that raised F1. Every other key describes where things are; `tracker_lint` is the only one
that fails. Written into `.handoff/config.md` the same day, by path (T-054), with the reason.

### Step 5 — the other backend

**A taskmd project on GitHub Issues is resumable through handoff, with no workaround.** It uses
handoff's own `github-issues` binding rather than anything here, and the join is exact: taskmd stores
every enumerated field as a `<field>:<value>` label
([`bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)), and that
binding's `tracker_status` accepts a `label:<prefix>` form. So `tracker_status: label:status:` and
`tracker_status_done: done` read taskmd's status with no translation layer.

**One limitation is stated rather than solved**: handoff writes a status in exactly one place — its
reconcile sweep marking finished work done — and knows one value. `phase`, the edges and the exit
criteria are invisible to it. That is the intended division of labour and not a gap in either tool:
handoff moves between *sessions*, the method moves work through *phases*. Recorded in the recipe's
closing section so an adopter meets it before assuming otherwise.

### Verification — by use, and by making the check fail

**The recipe's live use.** The session that wrote this resumed *through* the configuration it
documents: handoff read `.handoff/config.md`, resolved `tracker: local-markdown-dir` against
`tracker_dir: tasks/`, and located this task from a pointer. That is the recipe performing its
intended function before it was written down.

**The invariant hook, proven by failing.** A hook that has only ever passed is worth nothing, so it
was tested on the case it exists to catch. Changing this task's `status` and `phase` without
regenerating the index, then running the command `tracker_lint` names:

```text
STALE INDEX   tasks/README.md no longer matches the tasks it was generated from; run 'taskmd index'

1 problem(s) - 180 task(s), 900 field value(s), 606 reference(s), ...
EXIT=1
```

Non-zero exit on drift is exactly what handoff's binding requires of `tracker_lint`, and the message
names the command that fixes it. After `taskmd index`:

```text
Wrote tasks/README.md - 16 active, 164 closed
OK - 180 task(s), 900 field value(s), 606 reference(s), 24 dependency edge(s), ...
EXIT=0
```

**What was not verified.** No adopter has followed this recipe on a project that is not this one, and
the GitHub half of step 5 was derived by reading two binding documents against each other rather than
by configuring a live issues-backed project. Both are honest gaps, carried into §4 rather than
implied away.

**Decisions & assumptions**
- The three step-3 decisions above are the substantive ones; the plan's four are unchanged by
  contact with the work. — 2026-08-18
- **Assumption, recorded as one**: an adopter's `taskmd` is startable by the name they put in
  `tracker_lint`. It is stated in the recipe as an assumption rather than defended, because a lint
  that cannot start reports no drift and reads as a pass — the failure mode is silence. — 2026-08-18

**Outputs produced**
- plugin/skills/taskmd/docs/HANDOFF.md
- plugin/skills/taskmd/SKILL.md
- .handoff/config.md (untracked by design; the specimen fix, step 4)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| ~~The handoff F1 outcome is known before this is designed~~ | replaced | Not judged. Replaced on 2026-08-10 by [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) as unfalsifiable; the row is kept so a reader can see it was retired rather than skipped |
| Records whether the binding still states "the folder is the index", checked against it as it then stands, naming where | **met** | §3 step 1. Checked against the installed `bindings/local-markdown-dir.md`, naming the three sections that carry the remedy. **The trigger stopped applying mid-task** — the upstream contribution it was scoped to was dropped on 2026-08-18 — so this is judged on what was recorded, per §1's annotation |
| A taskmd project can be driven by handoff with no hand-written workaround | **met** | Five config lines, no workaround, no code. Strongest evidence is not the document: this session *resumed through* the configuration, so the recipe was performing its function before it was written down |
| `tracker_lint` documented as the way the invariant is enforced | **met** | `HANDOFF.md` *The index is the part that goes stale silently*. Documented **and** shown failing on the case it exists to catch — `EXIT=1` on a real stale index, quoted in §3. Note the upstream binding now documents the hook too; what this task adds is the taskmd command and the proof it fires |
| Works on **either** backend — GitHub Issues resumable too, or the limitation stated | **carried** | Split verdict, recorded rather than averaged. The *limitation* is stated (handoff sees one status value, never `phase`). The *configuration* is derived from two binding documents and has never been run, where the local half was verified by use. → **[T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md)** |
| The binding states the assumptions it makes about the adopting project | **met** | `HANDOFF.md` *Assumptions this recipe makes about your project* — five, each with what to change if it is false. The F1 fix applied to our own deliverable rather than only asked of others, which is what the criterion demanded |

**Open questions, re-read before closing** (procedure step 5)

- §1's first question was answered by the owner on 2026-08-07 and **half of it was retired on
  2026-08-18** — the deferred upstream contribution, dropped once `plan` found F1 already fixed
  there. Both are annotated in §1 and neither is live.
- §1's second question is annotation on a criterion that no longer exists. Not live.
- **Nothing here is addressed to anyone else.** T-181 carries the only open thread, and its own
  owner-question is written into that record rather than left in this one.

**Residual — reconciled at close, not deferred**

[`docs/BRIEF.md`](../docs/BRIEF.md) *Interop* stated "that binding assumes 'the folder is the index'"
as a present-tense fact, and §3 step 1 measured it false. **Annotated on close** rather than left for
a later sweep: the first draft of this row deferred it to the next handoff's reconcile, which is a
sweep nobody had scheduled — a residual parked against an event that may not happen is the shape that
goes invisible the moment a task closes. It was safe to correct only once §3 carried the measurement;
before that, editing the sentence would have destroyed the finding instead of recording it. The
original sentences are kept and annotated, per METHOD rule 5 — correct the present, annotate the
past — because the argument they carry is what raised this task.

**Child fix tasks raised**
- [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) — verify the
  GitHub half of the recipe against a live issues-backed project

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | Four criteria met, one carried into [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md), one retired before the work began. Shipped `plugin/skills/taskmd/docs/HANDOFF.md` — a configuration recipe, not a binding, because handoff resolves `tracker` against its own folder and a document here cannot be loaded as one. **The task's founding premise had expired before it was implemented**: F1 is fixed upstream, so the recipe uses a working binding rather than routing around a broken one, and criteria 3 and 5 describe work this task imitates rather than invents. Verified two ways — this session resumed *through* the configuration being documented, and `tracker_lint` was shown exiting 1 on a real stale index rather than only passing. Reconciled [`docs/BRIEF.md`](../docs/BRIEF.md) *Interop* on close, once §3 carried the measurement that made the edit safe. |
| 2026-08-18 | — | **The maintainer extended the grant below on 2026-08-18**, in the session that resumed the handoff carrying it. It adds **committing and pushing**, which the first grant excluded by name, and it confirms the whole remaining lifecycle for the same six tasks, run **unattended**. **The boundary is otherwise unchanged**: these six and nothing any of them raises; the seven tasks whose open question is reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179) and the three that cannot run unattended (T-175, T-176, T-178) stay outside it, and a task that turns out to need the owner after all is still a question to raise rather than a judgement to take. Recorded here for the same reason the row below gives: the handoff that carried the first grant has already been consumed and renamed, so a record is the only home that survives. |
| 2026-08-18 | → planned | Seven steps, ordered so that the two that can move what gets written come first. **Planning found the premise this task was raised on has expired**: handoff's `local-markdown-dir` binding no longer states "the folder is the index" — it carries an *Index topology* section offering folder-as-index and central-index as two supported shapes, a *Keeping the tracker consistent* section making `tracker_lint` the invariant hook, and an *Assumptions this binding makes* section. Those are the F1 remedy, and they are also the shape of criteria 3 and 5, so both are now largely satisfied upstream rather than by anything this task ships. That does not change the outcome the owner agreed — a v1 config recipe is still what this produces, and it is now a recipe that *uses* a fixed binding instead of one working around a broken one. Step 1 records the check properly, with where it was read; [`docs/BRIEF.md`](../docs/BRIEF.md) *Interop* still states the old premise as current and is left alone here, because it is a statement this task carries and reconciling it elsewhere would destroy what step 1 exists to produce. |
| 2026-08-18 | — | **The maintainer authorised the whole remaining lifecycle for this task** — `plan` → `implement` → `review` (this task's `specify` is already closed and owner-agreed, so the authorisation starts where the work does) — on 2026-08-18, as the subject of a handoff written the same day. **What it covers, exactly**: the six tasks named there as workable with no further input — [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md), [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md), [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md), [T-177](T-177-run-the-checks-that-need-no-task-folder.md) and [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) — **and nothing any of them raises**. **What it does not cover**, written down because a grant covering six tasks is the kind a later session stretches: the seven tasks whose open question was reserved to the owner (T-093, T-131, T-148, T-151, T-170, T-174, T-179), the three that cannot run unattended at all (T-175, T-176, T-178), and committing or pushing, which was granted separately for earlier work and was not granted here. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed, so an authorisation kept only there is invisible to the session after next (METHOD §3.1, and T-105 which settled where this goes). |
| 2026-08-07 | → specified | Answered: recipe for v1, upstream contribution deferred until after publishing. Recorded with the reason the rejected option is the better long-term shape rather than the wrong one — the handoff core loads a `tracker` binding from its own folder, so a recipe is not a substitute for one, only a thing that works without it. Criterion 1 is unchanged and now scoped: the recipe half does not wait on the F1 outcome, the contribution half does. |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
