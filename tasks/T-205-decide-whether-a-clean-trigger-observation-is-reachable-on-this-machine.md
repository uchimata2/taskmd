---
id: T-205
title: Decide whether a clean trigger observation is reachable on this machine
type: decision
status: done
phase: review
parent: T-175
blocked_by: []
related: [T-050, T-168]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-205 — Decide whether a clean trigger observation is reachable on this machine

## 1. Specify

**Outcome**
A decision, recorded with what it rules out: whether *does a request for task work in ordinary words
reach this skill* can be observed on this machine without a confound that changes the answer — and
where it cannot, that said plainly, so nobody spends a third venue finding out.

**Why this one**
[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) ran the observation its
venue was chosen for and got a **negative with three confounds**, two of which nobody predicted. One of
them outlives the run.
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9 located the naming
confound in **the project's** always-loaded conventions, and said a measurement would be clean in a
project that uses taskmd and does not describe it there. The venue was such a project — verified, not
assumed. **The machine's user-level instruction file names the tool anyway**, in every session on this
machine, so the confound was never the project's to remove and no choice of project removes it.

**The two observations that exist point opposite ways, and neither is clean.**

| Run | Venue | Result | The confound on it |
| :--- | :--- | :--- | :--- |
| [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9, 2026-08-08 | this repository | **Positive** — *what should I work on next?* routed to the skill on the description alone | Its tier-1 file names the skill, so the session was told it exists before it chose anything |
| [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3, 2026-08-21 | a project with no instruction file of its own | **Negative** — the same question, seven shell commands, the skill never invoked | Issue labels carrying this tool's own vocabulary, and a session mode disposed toward the shell |

One confounded positive and one confounded negative, and **the confounds do not overlap**, so neither
run checks the other. That is the whole of the evidence, and there is no third venue to break the tie
— which is why this is a decision and not a measurement.

**Two facts bound the answer before anyone starts.**

- **The qualifying venues are spent.**
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s class A was two
  projects. The owner rejected the tracker-shaped one on 2026-08-19 as too close to task work to
  distinguish a matched request from a matched subject, and the other has now had its first session,
  which cannot happen twice.
- **The instrument was confounded as well as the venue.** T-175's third confound — the session was
  disposed toward the shell by a mode nobody had accounted for — is a property of how such a session is
  *started*, not of where. Choosing a better project does not touch it.

**Scope**
- In: whether any arrangement available on this machine removes the user-level naming confound, and
  what it costs
- In: whether the negative T-175 recorded is worth acting on **as it stands**, confounds and all
- In: the answer either way, recorded where a later reader meets it before choosing a third venue
- Out: **rewriting the description.** It was out of
  [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md)'s scope and stays out
  of this one
- Out: re-running the observation. Where the decision is that a clean run is reachable, that run is its
  own task

**Inputs**
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 steps 5–6 — the
  three confounds and what each does to the result
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 steps 8–9 — the confound as
  first located, and the arrangement it called out of reach
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 steps 1–3 —
  the subset rule that identifies a qualifying project, and how many there were

**Acceptance criteria**

Each is derived from a clause of the Scope above, and the clause is named beside it.

- [ ] The decision is stated **once**, in one sentence, together with what it rules out
      (*the answer either way*)
- [ ] The arrangement that would remove the user-level naming confound is named and **costed**, and
      the reason it was refused is recorded, so that nobody re-derives it from scratch
      (*whether any arrangement available on this machine removes it, and what it costs*)
- [ ] Both rejected alternatives carry the reason they were rejected, not only the fact
      (*recorded with what it rules out*)
- [ ] **The negative is examined as it stands** — including what the venue's own configuration says
      about whether the skill applied there at all — and the reading is stated whether or not it
      supports the decision (*whether the negative is worth acting on as it stands, confounds and all*)
- [ ] A later reader choosing a venue meets this decision **before** choosing, shown by the venue
      register pointing at it (*recorded where a later reader meets it before choosing a third venue*)
- [ ] The follow-on work leaves here as a **raised task** whose scope survives the criterion above,
      and nothing in this run edits the description (both *Out* clauses)

**Open questions**
- ~~**Is a confounded negative enough to act on?** T-175's result is that the skill was not reached in
  a session that had read the very config the description names. Two confounds each supply an
  alternative explanation, and neither can now be removed.~~ **Answered by the owner on 2026-08-21:
  yes — act on it.** The reason, the two rejections and what the answer rules out are in the Log row
  of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | State the decision and what it rules out. | One sentence in §3, and nowhere else. |
| 2 | Name the arrangement that would remove the user-level naming confound, price it, and record why it was refused. | A costed arrangement in §3. |
| 3 | Read what the venue's own `.taskmd` config declares, and put the negative to the one reading nobody has tried: that the skill may not have applied there. | A stated finding, and what it does to step 4. |
| 4 | Raise the follow-on task, with a scope shaped by step 3 rather than by the decision alone. | The task file. |
| 5 | Point the venue register at this decision. | One line in the register, beside the venues it governs. |
| 6 | Annotate [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) where step 3 makes its record incomplete. | A dated Log row there. |

**Sequencing.** Step 3 comes before step 4 because it decides what the follow-on task is *for*, and a
task cannot scope itself. It comes before step 6 for the same reason a finding precedes the record it
corrects. Steps 1 and 2 are first because they are the decision the owner already gave, and writing
them down before looking further is what stops step 3 quietly re-opening a question that is settled.

**Decisions**

- **Step 3 sits in this task and not in the one it shapes.** The reading it tests changes what the
  follow-on is for, and a task written to examine the description cannot also decide whether the
  evidence for examining it means what it appears to — that is this task's *worth acting on as it
  stands* clause, and it expires the moment the follow-on is written — 2026-08-21.
- **The decision itself is not re-opened by step 3.** Whatever the reading turns out to be, the owner
  answered *act*, and a step that could reverse an owner's answer without asking is not a step. Where
  step 3 bears on the answer it is reported, not applied — 2026-08-21.

**Outputs**

- tasks/T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md (§3)
- one task file for the follow-on
- control/LOCAL-CONTEXT.md — the pointer beside the venues

## 3. Implement

### Step 1 — the decision

**Act on the negative.** [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md)'s
result is treated as a real risk to what the plugin is for, and the skill's `description` is to be
examined. Given by the owner on 2026-08-21.

The reason, written once: examining a description that turns out to be fine costs effort and is
reversible, while shelving the result risks the plugin quietly doing nothing for every adopter — nobody
writes this tool's name into their own always-loaded conventions, and not having to is exactly what a
skill description is for.

**What it rules out.** No third venue is being sought, so §1's *Out: re-running the observation* has no
branch behind it any more, and §1's *In* clause about removing the confound is answered by step 2 and
closed rather than left standing. A later reader is not to spend a project on this question.

### Step 2 — the arrangement that would remove the confound, priced and refused

It exists, and it is cheap. T-175's second confound is that the machine's user-level instruction file
names this tool in every session. Removing that one line, then starting a session in a throwaway
project carrying a `.taskmd` config and not in the shell-first mode, removes **two** of the three
confounds at once.

**What it costs:** one line edited and restored, one throwaway project, one session. Minutes, not a
day. Nothing about it is difficult, and that is why it needs a reason rather than a price.

**Refused, and not on cost.** What it produces is a project built in order to be probed, rather than a
project that adopted the tool — which is the objection the venue selection of 2026-08-19 was built
around. The owner rejected the likelier of the two real venues there precisely because a matched
*subject* cannot be told from a matched *request*. A synthetic project has neither a subject nor a
history, so a positive in it says the description matches a config directory, which nobody doubted,
and a negative in it says nothing at all.

Written down because it is the obvious next idea, and refusing it silently guarantees that somebody
proposes it again.

### Step 3 — the venue's own config, and the reading nobody had put to the negative

**The venue is not a project that migrated away.** Its `.taskmd/config.md` describes a project
**actively using taskmd through a different binding**:

```text
id_prefix: #               # a GitHub issue number: #7, #41, #1024
id_width: none             # GitHub allocates ids; no width can describe them
tasks_dir: tasks           # unused on this backend; see "The folder that is not used"
after_write: none          # taskmd writes nothing here - there are no task files
```

and its body opens *"Work on this repository is one task per GitHub issue, under taskmd's GitHub Issues
binding"*. So the file the session opened at command 3 of 7 is a document declaring that this project's
tasks are issues and that there are no task files at all.

**Two readings follow, and only one survives.**

*Reading A — the skill did not apply, so not firing was correct.* The description opens *"Work with
tasks kept as Markdown files"*, and this project keeps none. **Against it:** the skill's own body says
the opposite. `plugin/skills/taskmd/SKILL.md:42` reads *"These commands are the local-Markdown backend.
If this project keeps its tasks somewhere else, its binding supplies the operations instead — and
everything below is unchanged, which is the point."* The plugin ships that binding, and
[T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) verified taskmd's
own recipe on **this very project** on 2026-08-19. The skill applied.

*Reading B — the skill applied and did not fire.* This is the one that survives, and it **sharpens**
the negative rather than softening it: the session went on to do by hand roughly what the binding
prescribes — list the issues, read the labels, rank them — without ever loading the binding or the
method.

**What it gives the follow-on.** A hypothesis to test, instead of a starting point of *the description
does not work*: the description's first clause promises Markdown files while its trigger clause admits
*"or a .taskmd config"*, so a session that reads a config declaring the tasks are **not** files has
been handed the first clause as a reason to stop. Whether that is what happened cannot be known from
one transcript whose reasoning block is empty, which is why this is a hypothesis and not a finding.

**It does not re-open the decision**, per the plan's second decision. The owner answered *act*; this
says more precisely what there is to act on.

### Step 4 — the follow-on raised

[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md), scoped by
step 3 rather than by step 1 alone, and free to change the description — which this task was not.

### Step 5 — the venue register points here

One line beside the two venues in the gitignored roster, so a reader arriving there to choose a third
meets this decision first. That is criterion 5, and the roster is the right home because venue
selection is the only thing that happens in it.

### Step 6 — T-175 annotated

Its §3 records that the session read the venue's `.taskmd` config and does not record **what the config
says**, which is the whole of step 3. A dated Log row there carries it, annotating rather than
rewriting (METHOD rule 5).

**Decisions & assumptions**

- **Reading B is adopted and Reading A recorded against it, rather than left as an open pair.** A pair
  of readings with no verdict is a decision task that decided nothing. The evidence separating them is
  named — the skill's own line 42, the shipped binding, and a recipe verified on that project — and it
  is checkable, so a later reader can overturn it on the same terms — 2026-08-21.
- **Step 3 is a hypothesis handed on, not a finding recorded.** The transcript's reasoning block is
  empty, so nothing in it says why the session did not reach the skill. Calling it a finding would be
  the failure this chain of tasks keeps meeting: a plausible account that nobody could have
  falsified — 2026-08-21.
- **The description is not touched here**, though step 3 makes it tempting: this task's §1 puts it out
  of scope, and the task that may change it is the one that will have tested the hypothesis first —
  2026-08-21.

**Outputs produced**

- this record
- [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md)
- the pointer line in the gitignored venue register, beside the venues it governs

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is stated **once**, in one sentence, together with what it rules out | met | §3 step 1. *Act on the negative*, with the reason written once and the rule-out named: no third venue is sought, so §1's *Out: re-running the observation* has no branch behind it and its *In* clause on removing the confound is closed by step 2 rather than left open |
| The arrangement that would remove the user-level naming confound is named and **costed**, and the reason it was refused is recorded | met | §3 step 2. Named: remove the one line from the machine's user-level instruction file, probe a throwaway project outside the shell-first mode — which removes two of the three confounds. Costed: one line edited and restored, one throwaway project, one session. Refused **not on cost** but because a project built to be probed has no subject and no history, which is the distinction the venue choice of 2026-08-19 exists to protect |
| Both rejected alternatives carry the reason they were rejected, not only the fact | met | The Log row of 2026-08-21 carries both. *Shelve it as unanswerable* is refused because nothing would then ever say so if the description does fail adopters; *manufacture a cleaner venue* is refused for the reason step 2 sets out at length |
| **The negative is examined as it stands** — including what the venue's own configuration says about whether the skill applied there at all — and the reading is stated whether or not it supports the decision | met | §3 step 3. Reading A — *the skill did not apply, so silence was correct* — is stated in full and then argued against on `SKILL.md:42`, the shipped GitHub binding, and [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) having been verified on that same project. It happens to support the decision, and it was written before that was known to be the direction |
| A later reader choosing a venue meets this decision **before** choosing, shown by the venue register pointing at it | met | §3 step 5. The pointer sits in the roster row that already says it is where the venue mapping lives, so it is on the path a reader takes to choose one. It points rather than restates: the decision and the refused arrangement stay here |
| The follow-on work leaves here as a **raised task** whose scope survives the criterion above, and nothing in this run edits the description | met | §3 step 4. [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) is scoped from step 3's hypothesis rather than from step 1's decision, and it is free to change the description, which this task was not. `plugin/skills/taskmd/SKILL.md` is unmodified in this run |

**Open questions, re-read before closing** (`review.md` step 5). §1's only question was answered by the
owner on 2026-08-21 and is struck through in place. One new question is aimed at someone who is not
doing the work, and it is written into
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) rather than
here, where closing would take it out of every view: **whether a synthetic project is acceptable as a
before-and-after *test rig*, given that step 2 refused one as *evidence about adopters*.** Those are
different uses of the same thing, and only the first was refused — but nobody has ruled on the second,
and T-206 cannot be finished until somebody does.

**What this task is worth, stated plainly.** It converted an owner's one-word answer into something a
later reader can act on and argue with: the decision, the alternative that was refused and why it was
not refused on cost, and a venue register that now stops the refused idea being proposed again.

**Its most useful output is the one it was not asked for.** Step 3 read the venue's own configuration —
which the observation task had opened and not quoted — and found that the venue was not a project that
had migrated away at all, but one using this tool through its GitHub Issues binding. That turns *the
description does not trigger* into a specific clause pulling against another clause, which is a thing
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) can test
rather than a suspicion it would have had to start by inventing.

**Child fix tasks raised**
- [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) — test
  whether the description's Markdown-files clause turns a session away from a non-file backend, and
  change the description or show it does not need changing

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Decision recorded, and one thing found that was not asked for.** The decision is the owner's *act on the negative*, written once with what it rules out; the arrangement that would have removed two of the three confounds is named, priced at minutes, and refused because a project built to be probed has no subject and no history — which is what the venue choice of 2026-08-19 was protecting. **Step 3 is the unasked-for half**: the venue's `.taskmd` config declares a GitHub-issues backend and says outright that there are no task files, so the venue was not a migrated-away project but one using this tool through a different binding — and the skill applied there, by `plugin/skills/taskmd/SKILL.md:42` and by [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) having been verified on that same project. The negative is sharpened rather than softened, and [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) carries an annotation saying so. Raised [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) with a scope shaped by that finding, and pointed the venue register here so the refused arrangement is not proposed again. Run under the authorisation of 2026-08-21 recorded below, which covered this task through its full lifecycle and reaches no other. |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21.** The owner granted this session **this task through its full lifecycle**, and the commit and push after it. Written here rather than only in the session that received it, for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) gives. **It reaches this task and no others** — in particular it does not reach the follow-on task §3 raises, which is an output of this run and not a continuation of it. |
| 2026-08-21 | (no change) | **Answered by the owner: act on the negative.** [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md)'s result is treated as a real risk and the skill's `description` is to be examined, confounds and all. **The asymmetry is the reason, and it is the part worth keeping**: examining a description that turns out to be fine costs effort and is reversible, while shelving the result risks the plugin quietly doing nothing for every adopter — nobody writes this tool's name into their own always-loaded conventions, and not having to is what a skill description is for. *Rejected: shelve it as unanswerable*, which accepts that if the description does fail for adopters, nothing would ever say so. *Rejected: manufacture a cleaner venue* — removing this tool's name from the machine's user-level instruction file and probing a throwaway project outside the shell-first mode — which removes two of the three confounds and tests a synthetic project rather than an adopter, the objection the venue selection of 2026-08-19 was built around. **What it rules out**: no third venue is being sought, so §1's *Out: re-running the observation* has no branch behind it any more. This task still owes its own criteria and its lifecycle, and the follow-on description task is **its** to raise rather than something raised ahead of it. |
| 2026-08-21 | (no change) | **Confirmed by the owner on 2026-08-21 as belonging**, having been raised outside the two-task grant of the same day — the same ruling as on [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md). It matters more here than there: this task is the only thing carrying the expired premise, so cancelling it would have put that finding back out of every view. Written into this record rather than left in the reporting thread, for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) gives. |
| 2026-08-21 | → proposed | Raised by [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 step 6, which is the step its fifth criterion required. `medium` and `s`: it settles whether anything follows that observation, and it is a decision rather than work. **It exists because a premise expired**: [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) put the naming confound in the project's own conventions and a venue was selected on that basis; the user-level instruction file names the tool in every session on this machine, so the selection could not have removed it. Its parent is T-175 rather than the closed umbrella above it, because that is where the question was produced. |
