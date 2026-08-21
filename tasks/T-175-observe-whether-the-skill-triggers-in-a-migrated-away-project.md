---
id: T-175
title: Observe whether the skill triggers in a project that has migrated its backlog away
type: research
status: done
phase: review
parent: T-168
blocked_by: []
related: [T-168, T-050]
work_package: M6
owner: maintainer
business_value: high
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-175 — Observe whether the skill triggers in a project that has migrated its backlog away

## 1. Specify

**Outcome**
An observation, not an argument, of whether a request for task work in ordinary words reaches the
taskmd skill in a project that carries a `.taskmd` config with no resolvable task folder — the half
[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) measured the cost
of and could not measure the behaviour of.

**Why this one**
**[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 step 3
recorded this unobserved and named what would show it**, which its criterion 3 allows as a pass. The
corpus could not answer it: across the 11 sessions in the two qualifying projects, **none asked for
task work in ordinary words**, so nothing put the description to the test and the zero is noise.

**The venue is the part that is new.** [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)
§3 step 9 recorded a confound it called unremovable from inside this repository — `CLAUDE.md` names
the skill in tier 1, so any probe run here has already told the session the skill exists. It said a
clean measurement "would need a project that uses taskmd and does not describe it in its
always-loaded conventions", and treated that as out of reach. T-168's class A is two such projects.
So this closes a residue of T-050 as well as its own question.

**It cannot be arranged from inside a session, and that is not a detail.** T-050 §3 step 8 is the
precedent and the argument: reading a handoff, a task record or a note *is* the confound, so the
instruction belongs to the maintainer and the record holds the arrangement rather than the
instruction.

**Scope**
- In: one session in a qualifying project whose **first** substantive request is task work in
  ordinary words, with the skill unnamed and no command or handoff supplying it
- In: whichever way it goes, recorded as what was observed rather than what was expected
- Out: rewriting the description if it does not trigger. That is a separate task, exactly as
  [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)'s scope drew the same line
- Out: the cost half, which
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) answered

**Inputs**
- [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 steps 1–3 —
  the subset rule that identifies a qualifying project, and what the corpus could and could not say
- [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 steps 8–9 — how the same
  probe was arranged before, and the confound this venue removes

**Acceptance criteria**

**Written 2026-08-21, after the observation existed — which is stated rather than hidden.** The venue
was spent on 2026-08-21 by the owner, before this phase ran, because §1 says the observation cannot be
arranged from inside a session. So these criteria carry the hazard `review.md`'s *Changing a criterion*
warns about, one phase earlier: criteria written after a result can be fitted to it. The guard is that
**each one below is derived from a clause of the Scope agreed on 2026-08-18 and the venue choice of
2026-08-19**, and none from anything the transcript turned out to contain. The derivation is named in
each line.

- [ ] The observation is recorded as **what happened** — the session's first request quoted, and what
      it did in response — and not as a judgement of whether the description is good
      (*Scope: whichever way it goes, recorded as what was observed rather than what was expected*)
- [ ] The skill is shown to have been **served** to that session, from the session's own record, so a
      negative cannot be the skill having been absent (*Scope: the skill unnamed and no command or
      handoff supplying it* — unnamed is not the same as unavailable, and only one of the two is a
      valid negative)
- [ ] The venue's **precondition** — that the project does not name this skill in its always-loaded
      conventions — is checked against that project as it stood, and the answer stated either way
      (Log 2026-08-19: *`specify` states the precondition it depends on rather than assuming it holds
      on the day*)
- [ ] **Every confound the run exposes is named**, including any nobody predicted, and each is stated
      as weakening the result or not (Log 2026-08-19, which recorded one confound in advance and said
      the venue is destructible)
- [ ] If the result invites a change to the description, it leaves this task as a **raised task**, not
      as a recommendation inside this record (*Scope: Out — rewriting the description if it does not
      trigger. That is a separate task*)

**Open questions**
- ~~**Which qualifying project, and is one session enough?** Two qualify. One is a tracker-shaped
  project whose own work is close to task work, so a trigger there is more likely and also more
  confounded; the other is further away. **The maintainer decides**, and the choice is worth
  recording because it changes what a positive means.~~ **Answered by the owner on 2026-08-19: the
  project further away, one session** — the Log row of that date carries the reason, the two
  rejections, and the precondition the venue depends on.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Resolve the roster's pointer to an actual transcript, and record what it resolves *through*. | The transcript identified, and the resolution route recorded in the roster rather than here. |
| 2 | Check the venue's precondition against that project as it stood: does anything always-loaded there name this skill? | A stated answer, with what was read to reach it. |
| 3 | Read the session's own record of what it was **served**, and find the skill in it. | The served description, quoted in §3. |
| 4 | Record the first request and every action the session took in response, in order. | The sequence, in §3. |
| 5 | Name every confound the run exposes — predicted or not — and say what each does to the result. | One entry per confound, each with a verdict. |
| 6 | Decide whether the result invites a task, and raise it or state that it does not. | A raised task, or a stated no with the reason. |

**Sequencing.** Step 2 comes before steps 3–4 because a precondition that has failed voids the
observation, and finding that out after writing the observation up would mean writing up something
that measures nothing. Step 3 comes before step 4 for the reason criterion 2 exists: a session that
was never served the skill cannot be evidence about the skill, and *unnamed* and *unavailable* look
identical in a transcript unless the served list is read.

**Decisions**

- **The observation is read from the transcript, not asked of the owner.** The owner ran the session
  and could describe it, but a description of a session is a memory of it, and the criterion asks for
  what the session did. The transcript is the record `CLAUDE.md`'s *Verifying* section means by
  running the thing on a real case — 2026-08-21.
- **The machine-local session id stays out of this record.** It is a pointer to a local store on one
  machine, this repository is published, and the roster is where it already lives — 2026-08-21.
- **A confound found during the run is recorded and weighed, never used to withhold the result.**
  A negative that is put aside because something might explain it is a negative nobody ever has to
  answer, and the venue cannot be re-run — 2026-08-21.

**Outputs**

- tasks/T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md (§3)
- control/LOCAL-CONTEXT.md — the pointer's resolution route, where the pointer already lives

## 3. Implement

### Step 1 — the pointer crosses two id spaces, and reads as dead in between

The roster carries the session's id. That id does **not** name a file in the transcript store: on this
harness the two are different id spaces, and searching the store for the recorded id finds nothing at
all. The pointer is good and the obvious way of following it fails silently, which is worth exactly
one line beside the id — written into the roster, where the id already lives, and not here.

### Step 2 — the precondition held, at the level it was written about

The project carries **no instruction file of its own**: no `CLAUDE.md`, no `AGENTS.md`, no `.claude/`
directory. So nothing that project always-loads names this skill, and the precondition the Log of
2026-08-19 made this venue depend on was intact on the day.

**It held at project level and not above it.** That is step 5's second confound rather than a footnote
here.

### Step 3 — the skill was served, so a silence is about the description

The session's own record of what it was handed lists 68 skills, this one among them, carrying the
description it ships:

```text
- taskmd:taskmd: Work with tasks kept as Markdown files - one per task, plus a generated index, real
  dependency links and a validator - for any kind of work, not only software. Use in a project that
  tracks tasks this way (a folder of Markdown task files, or a .taskmd config) when asked what to work
  on next, or to start, specify, plan, implement, review, audit or close a task. Also whenever the
  user says taskmd.
```

Which is criterion 2 met: whatever follows is the description failing to route a request, not the
skill being absent from the session.

### Step 4 — what happened

The session ran on 2026-08-21, on one model at high reasoning effort, and lasted about eighty seconds.
Its first request was substantive, in ordinary words, and was the whole of the message:

```text
What should I do next?
```

The description names that case in almost those words. What the session did with it, in order:

| # | Action | Instrument |
| :-- | :--- | :--- |
| 1 | Listed the repository root, then looked inside its handoff and taskmd config directories | shell |
| 2 | Read the git log, the status and the tracked-file list | shell |
| 3 | Read the handoff config and **the `.taskmd` config** | shell |
| 4 | Read the README | shell |
| 5 | Read the ignore file, the remotes and the branch | shell |
| 6 | Listed the project's issues, then read every open one in full | shell |
| 7 | Answered: nothing in flight, six issues all at `status:proposed` and `phase:specify`, and two named to start with, in order | — |

**The skill was never invoked. No skill was, at any point in the session.**

**The strongest single fact is row 3.** The description's stated applicability condition is *a folder
of Markdown task files, or a `.taskmd` config*. The session opened that project's `.taskmd` config,
read it, and carried on answering by other means. The condition was not merely true of the tree; it
was in front of the session, and the skill was still not reached.

**The answer it gave was a good one**, which is worth saying because a negative here reads easily as a
session that did badly. It was not: it found the work, ranked it, and named where to start. What it
did not do is arrive there through the skill.

### Step 5 — the confounds, of which one was predicted

| # | Confound | What it does to the result |
| :-- | :--- | :--- |
| 1 | **The venue's issues already carry `status:`, `phase:`, `type:`, `business_value:` and `effort:` labels** — this tool's own convention. Predicted on 2026-08-19, and observed acting: the session read them and answered from them | **Weakens the negative.** There was a complete path to a good answer without the skill, so this run cannot separate *the description did not match the request* from *nothing was missing* |
| 2 | **The machine's user-level instruction file names this tool**, in a list of the owner's repositories cloned side by side. It is loaded in every session on this machine, including that one, and it plausibly produced the first command's probe into a taskmd config directory | **Does not weaken it — it biases the other way**, since the name was in front of the session and the skill still was not reached. Its real consequence is below |
| 3 | **The session ran under a mode that directs work to the shell.** Its text names the file-reading and file-editing tools rather than skills, but its disposition is shell-first, and every action in step 4 is a shell command | **Weakens the negative**, and nobody predicted it. A session disposed toward the shell is not a neutral instrument for asking whether a request reaches a skill |
| 4 | **One session.** The decision of 2026-08-19 chose one clean venue over two, deliberately | Bounds what the run can say. Not a defect, and not a reason to discount it |

**Confound 2 is the finding, and it is bigger than this task.**
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9 called the naming confound
unremovable *from inside this repository*, and said a clean measurement would need a project that uses
taskmd and does not describe it in its always-loaded conventions. This venue was chosen to be exactly
that, and it is exactly that — at project level. The confound survived one level up, in a file no
choice of project can change, and **that possibility is recorded nowhere**: T-050 located it in the
project, [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) selected
on the project, and this task's own precondition was written about the project. So the venue did what
it promised, and the premise underneath the promise was incomplete.

### Step 6 — what this raises

**Not a description change.** Criterion 5 asks that any such change leave here as a task rather than as
a recommendation, and this result is too confounded to ask for one: confounds 1 and 3 each offer an
explanation for the silence that has nothing to do with the description's wording.

What it does raise is whether the question can be put cleanly at all on this machine —
[T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md).

**Decisions & assumptions**

- **The observation was read from the transcript, not asked of the owner** — the criterion asks what
  the session did, and a description of a session is a memory of it — 2026-08-21.
- **The negative is published with its confounds rather than withheld pending a cleaner run.** The
  venue is spent, so withholding it means never reporting it. Rejected: recording the run as
  inconclusive, which would put the two unweighed confounds out of every view — 2026-08-21.
- **Confound 3 is stated as weakening the result even though its text names only file tools.** Read
  narrowly it does not reach skills at all; read as a disposition it produced seven shell commands and
  no tool call of any other kind. Taking the narrow reading would be choosing the reading that flatters
  the result — 2026-08-21.
- **The machine-local session id and the checkout path stay out of this record**, and the resolution
  route is written beside the id in the roster instead — 2026-08-21.

**Outputs produced**

- this record
- [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md)
- the roster row's resolution route, in the gitignored local-context file where that pointer lives

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The observation is recorded as **what happened** — the first request quoted, and what the session did in response — and not as a judgement of whether the description is good | met | §3 step 4. The request is quoted in full, being the whole message, and the response is seven numbered actions in order with the instrument each used. The one evaluative sentence in the section says the session's *answer* was good, which is the opposite of judging the description |
| The skill is shown to have been **served** to that session, from the session's own record, so a negative cannot be the skill having been absent | met | §3 step 3. The session's own record of what it was handed lists 68 skills including this one, and the description it carried is quoted verbatim from that record rather than from the repository |
| The venue's **precondition** — that the project does not name this skill in its always-loaded conventions — is checked against that project as it stood, and the answer stated either way | met | §3 step 2. The project has no `CLAUDE.md`, no `AGENTS.md` and no `.claude/` directory, so the precondition held. It held **at project level**, which is stated in the same breath rather than left as an unqualified pass |
| **Every confound the run exposes is named**, including any nobody predicted, and each is stated as weakening the result or not | met | §3 step 5. Four, each with a direction: one predicted on 2026-08-19 and observed acting, one that biases toward a positive, one nobody predicted at all, and the sample size. Two weaken the negative and this is said plainly rather than in a closing caveat |
| If the result invites a change to the description, it leaves this task as a **raised task**, not as a recommendation inside this record | met | §3 step 6. No description change is proposed, and the reason is given: two confounds each explain the silence without touching the wording. What left instead is [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md), whose scope excludes rewriting the description exactly as this one did |

**Open questions, re-read before closing** (`review.md` step 5). §1's only question was answered by the
owner on 2026-08-19 and is struck through in place. The run produced one more, and it is aimed at
someone who is not doing the work: **whether a negative this confounded is worth acting on** is a
judgement about risk appetite. It is written into
[T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md)'s own open
questions, where an open task keeps it in every view — rather than here, where closing this record
would take it out of all of them.

**What this task is worth, stated plainly.** It answers its question with a **negative**: asked *what
should I do next* in a project carrying a taskmd config, with the skill served and its description
naming that case in almost those words, the session did not reach the skill — and it had read the
project's `.taskmd` config on the way past. That is the observation, and it is the first direct one
this project has; everything before it was a corpus with no positives in it.

**It is worth less than a clean run would have been, and the gap is named rather than absorbed.** Two
of the four confounds offer an explanation for the silence that has nothing to do with the
description's wording, and neither can be removed now: the venue is spent, and the one nobody predicted
lives in how a session is started rather than where. So this record does not license a description
change, and [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md)
exists to decide whether anything follows it at all.

**Child fix tasks raised**
- [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) — whether a
  clean observation is reachable on this machine, raised at `implement` step 6 under criterion 5. It
  does not gate this task, which is `research` and not an audit

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | (no change) | **§3 records that the session read the venue's `.taskmd` config and does not record what that config says, which turns out to matter.** It declares `id_prefix: #`, `id_width: none`, `tasks_dir` unused on this backend and `after_write: none` because *there are no task files*, and its body opens by saying the project's work is one task per GitHub issue under this tool's own GitHub Issues binding. So the venue was not a project that had migrated away; it was a project using taskmd through a different backend, and the skill applied there — `plugin/skills/taskmd/SKILL.md:42` says a project keeping its tasks elsewhere is served by its binding, and [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) verified that on this same project two days earlier. **The negative is sharpened, not softened**: the session went on to do by hand what the binding prescribes. Weighed in [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) §3 step 3, which is where it belongs; this row annotates rather than rewrites (METHOD rule 5), and no criterion above changes. |
| 2026-08-21 | (no change) | **The §1 acceptance criteria were agreed by the owner on 2026-08-21, after this record closed.** They were written during this task's `specify` and derived from the Scope agreed on 2026-08-18, which is what §1 states and why it states it — the agreement METHOD §2 asks for arrived when the run was reported, not before it. **No criterion changed**, and the owner was shown the after-the-fact ordering as part of the question. Recorded here rather than edited into §1, because §1 is a dated statement about how the criteria were made and this is a later fact about them (METHOD rule 5). |
| 2026-08-21 | → done | **Negative, and confounded.** Asked *What should I do next?* as its first substantive request, in a project with no instruction file of its own, the session ran seven shell commands — including reading that project's `.taskmd` config, the very condition the description names — listed the project's issues and answered from their labels. **The skill was never invoked, and neither was any other.** It was served: the session's own record lists 68 skills with this one among them, so this is the description failing to route a request rather than the skill being absent. Four confounds are recorded, two of them weakening the result and only one predicted; the one that outlives the run is that [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) located the naming confound in the *project's* conventions and the machine's user-level instruction file names this tool in every session, so no choice of venue could ever have removed it. No description change proposed — out of scope by §1 and unlicensed by this evidence; raised [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) to decide whether a clean run is reachable at all. Run under the authorisation of 2026-08-21 recorded below, which covered this task through its full lifecycle. |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** two tasks: [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) **and stop**, then [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) **through its full lifecycle**. Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **It reaches these two and no others.** *And stop* names a specific thing not to do: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) is T-201's sibling finding and the owner chose not to spend the session on it, so closing T-201 leaves [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) open on its other child, and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) open with it (`audit.md` step 5). Neither umbrella is to be closed. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: the qualifying project that is *further* from task work, and one session.** Asked in the backlog-wide round of 2026-08-19. The reason is that a trigger there is unconfounded — nothing about that project's own subject nudges the description into matching — so a positive means what it says and a negative is honest. *Rejected: the tracker-shaped project*, likelier to fire and unable to distinguish a matched request from a matched subject. *Rejected: both, one session each*, which would let the two hits be compared and costs a second session for a distinction one clean venue does not need. **A risk surfaced while resolving which checkout that names, and it belongs here**: the venue's value rests entirely on that project not naming this skill in its always-loaded conventions, which is the confound [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9 called unremovable from inside this repository. It has an open issue of its own about whether to commit its taskmd and handoff configs, and how that is answered could put the skill's name in front of every session there. **The venue is destructible and nothing currently watches it**, so `specify` states the precondition it depends on rather than assuming it holds on the day. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review under [`review`](../plugin/skills/taskmd/docs/method/review.md) step 5 — a question aimed at someone who is not doing the work fails no criterion, so nothing else would have carried it, and it leaves every view the moment its parent closes. `high` because it is the half of the installation decision that is still unevidenced after T-168, and because it also closes a residue [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) recorded as out of reach. **Not covered by the authorisation of 2026-08-18.** |
