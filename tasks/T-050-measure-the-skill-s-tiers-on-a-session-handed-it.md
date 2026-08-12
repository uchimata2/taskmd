---
id: T-050
title: Measure the skill's tiers on a session that was handed it
type: fix
status: done
phase: review
parent: T-003
blocked_by: []
related: [T-006, T-053]
work_package: M1
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-08
deliverables: []
---

# T-050 — Measure the skill's tiers on a session that was handed it

## 1. Specify

**Outcome**
The claim that the taskmd skill's tiers arrive one at a time — description unasked, body on
invocation, method when the body points at it, phase file when the phase begins — is carried by
observation of a session that was actually handed the skill, and so is the claim that both
invocation paths reach it.

**Why this one**
Carried from [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)'s review,
criteria 4 and 8. T-003 measured everything a session can measure about a skill it wrote: the size
of each tier, and the fact that the harness **fixes its skill list at session start** — established
by writing a throwaway skill mid-session and having the invocation refused by name. The one thing
left needs the harness to hand this skill to a session, which the session that wrote it cannot be.

The obvious way round was tried and failed: a fresh headless session (`claude -p`) exits on an
expired OAuth token. Recording that here so the next attempt does not repeat it — if the token is
live, that route answers this task in one command.

**This is not a code task, and nothing is known to be wrong.** The mechanism was measured for skills
in general by [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md), and
this skill is built to it. But *the mechanism applies* is an argument and this project does not
accept arguments about behaviour — which is the whole reason R-21 names a measurement.

**Requirements served**
R-21 (`docs/SCOPE.md`); §1 *Invisibility*, which the model-invocation half is.

**Scope**
- In: what a session in this repository is handed before invoking the skill, and what arrives at each
  later moment.
- In: whether the skill is reached without being named — the model-invocation path — and whether
  naming it reaches it.
- In: whether the plugin declared in `.claude/settings.json` is picked up from this tree at all. If
  it is not, that is this task's finding and the registration is what gets fixed.
- Out: the skill's content. If the description turns out not to trigger, the fix is a task of its own
  — a trigger that needs rewriting is not the same defect as one that was never registered.
- Out: install instructions and the published shapes — [T-006](T-006-package-document-and-publish.md).

**Inputs**
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) §3, which holds the tier table
this task is checking, and `skills/taskmd/SKILL.md`.

**Acceptance criteria**
- [ ] The tier table in T-003 §3 is confirmed or corrected against a session that was handed the
      skill, with what was observed at each moment
- [ ] A request to do task work reaches the skill **without the user naming it**, or the failure is
      recorded with what the session was handed instead
- [ ] Naming the skill reaches it
- [ ] Whichever of the three fails, the record says what was observed rather than what was expected

**Open questions**
- None. This is a measurement, and the way to take it is to start a session and look.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Before invoking anything, write down what the session was handed — the observation exists only at this moment, so it is taken first and everything else is arranged around it | §3 step 1 |
| 2 | Exercise the named-invocation path and record the harness's answer verbatim, whichever way it goes | §3 step 2 |
| 3 | Establish whether the plugin declared in `.claude/settings.json` reached the harness's plugin machinery **at all**, read out of the harness's own state rather than inferred from the declaration | §3 step 3 |
| 4 | Say which rows of T-003 §3's tier table this session settles and which it cannot, and what the result makes false elsewhere | §3 step 4 |

**Shape decision.**

**D1 — The measurement is taken and recorded; the registration fix is not applied in the same
pass.** The two halves have opposite perishabilities. The observation is destroyed by the first
skill invocation of the session, so it cannot wait; the fix cannot be *verified* in the session that
applies it — a skill registered mid-session is refused by name, which
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) §3 step 7 established by
probe and which step 2 below has now seen from the other side. So applying a fix here buys nothing
this session can check, while choosing the mechanism unasked would pick between options that belong
to the maintainer and touch [T-006](T-006-package-document-and-publish.md). *Rejected: fix and
report in one pass* — it reads as faster and it would put an unverified change into the tree under a
task whose whole point is that this project does not accept unverified claims about behaviour.

## 3. Implement

### Step 1 — what the session was handed, before anything was invoked

Taken on a session started in this repository on 2026-08-07, reading only what was already in
context. Three things arrived unasked:

| Arrived unasked | Form |
| :--- | :--- |
| `CLAUDE.md`, in full | a project-instructions block, presented as overriding default behaviour |
| the agent's own cross-project memory index | an unrelated mechanism, outside this project's tier model |
| a list of available skills, each as name + description | ~45 entries |

**The taskmd skill is not in that list.** Neither `taskmd` nor `taskmd:taskmd` appears, and no text
from `skills/taskmd/SKILL.md` — description or body — was present anywhere in what the session was
given.

The list *did* contain skills supplied by two installed plugins, under the `plugin:skill` naming the
harness uses for them. So plugin-provided skills reach the list in this harness, on this session:
the failure is specific to this repository's registration and not to the mechanism T-048 measured.

### Step 2 — naming the skill

Both forms of the user-invocation path, and the harness's answer:

```text
Unknown skill: taskmd. Did you mean tasks?
```

```text
Unknown skill: taskmd:taskmd
```

**Criterion 3 fails.** Criterion 2 — reaching the skill without naming it — cannot fail *on its
merits* and did not: a skill absent from the session's list has no description in context for a
request to match, so there was nothing to trigger. That distinction is the one T-050's scope draws,
and it decides which task owns the fix: this is a registration that never happened, not a trigger
that did not fire, so the out-of-scope clause for a rewritten description is not reached.

### Step 3 — where the registration stops

Read out of the harness's own plugin state rather than from the declaration:

| Harness state | Holds | taskmd present? |
| :--- | :--- | :---: |
| `~/.claude/plugins/known_marketplaces.json` | 2 marketplaces, both `github`-sourced, each with an install location and a fetch timestamp | no |
| `~/.claude/plugins/installed_plugins.json` | 2 plugins, each with a version-stamped install path and an install time | no |
| `~/.claude/plugins/cache/` | one folder per marketplace, then plugin, then version | no |
| `~/.claude/plugins/plugin-catalog-cache.json` | the catalog | no |

Nothing in the machinery has heard of it. Two facts narrow what that means:

- **The settings shape is right, not merely plausible.** `extraKnownMarketplaces` and
  `enabledPlugins` are the keys the shipped binary validates, and the user-level settings on this
  machine enable a plugin through exactly the same pair — that plugin's skills are in the session's
  list. So the declaration is not being rejected as malformed.
- **The project's trust dialog was accepted**, so this is not the project settings file going
  unread.

What the four rows above have in common is that every plugin the harness *does* serve was
**installed** — downloaded into a versioned cache and written into two state files. Declaring a
marketplace and enabling a plugin in project settings did not produce that install. Whether an
install is expected to follow from the declaration, or is a separate action the maintainer has to
take once, is the question the fix turns on, and it is asked at the end of this section rather than
answered here.

**This is the plainest form of a fact this project keeps re-learning.** `.claude/settings.json` is a
declaration of intent; the T-003 record reads it as an accomplished state — "the registration is in
place" — and the registration is what is missing.

### Step 4 — against T-003 §3's tier table, and what this makes false

| Tier | Row's claim | This session |
| :--- | :--- | :--- |
| 0 | the `description` arrives every session, unasked | **not observed** — nothing arrived, because nothing is installed. The row is untested, not refuted |
| 1 | the `SKILL.md` body arrives on invocation | **not reachable** — invocation is refused (step 2) |
| 2 | `docs/METHOD.md` when the body points at it | **not evidence for the skill.** This session did load it at the right moment, but by way of `CLAUDE.md` and the handoff, not by the body — a different loader, so it says nothing about the skill's routing |
| 3 | a phase file when its phase begins | same — `specify.md` was loaded at its moment, by the method spine, not by the skill |

So **criterion 1 is not met and not carried onward in the same form**: the tier table cannot be
confirmed or corrected until the skill is actually served to a session, and the reason it was not is
now a known, fixable condition rather than an unexamined one. Criterion 4 — that the record says
what was observed rather than what was expected — is what the three rows above are.

**What the result makes false.** All three descend from one sentence in T-003 §3 step 8: that
enabling the plugin here put the description into tier 1 by T-028's membership rule.

- **`CLAUDE.md` *Working method*** says tier 1 is "this file plus the skill's `description`".
  Measured: **this file alone.** The membership rule itself is untouched and still correct — tier 1
  is whatever the harness loads unasked, and the description would join it the moment the plugin is
  served. What is wrong is the claim that it currently does.
- **`.handoff/config.md`** repeats the same pairing.
- **[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) is not over its
  bound.** Its arithmetic went over on 397 characters that are not in tier 1 of any session in this
  repository. Its margin is whatever it was before T-003's step 8, and the two things its `plan` was
  handed — how a character count weighs against a line bound, and that tier 1 grows when a skill is
  added — are premature until the description is actually being served.

### Step 5 — the maintainer's answer, and the reconcile it made writable

**Answered 2026-08-07: leave the declaration and install once by hand.** The maintainer runs the
harness's marketplace-add and install from an interactive terminal; `.claude/settings.json` stays as
written and is not the defect. *Rejected: a project-level `.claude/skills/taskmd/`*, which is served
with no install at all and was already refused by T-003 **D2** for creating a second home for the
skill — the measurement gives that rejection a cost but does not overturn it. *Rejected: treating it
purely as [T-006](T-006-package-document-and-publish.md)'s* — that leaves this repository unable to
run on its own skill until packaging lands, which is the arrangement T-003's scope was written to
avoid. **T-006 still owes an install line**: an adopter who copies the declaration and stops has
exactly the tree measured above.

**And that line has to say `./`, not `.`** — read out of the shipped binary rather than assumed. The
marketplace-add prompt takes one field, a source, and treats it as a local path only when it begins
with `./`, `../`, `/`, `~`, `.\`, `..\` or a drive letter. A bare `.` matches none of them, falls
through to the GitHub `owner/repo` branch and is rejected as a malformed source. `.claude/settings.json`
declares the same directory as `"path": "."` — a different code path, and valid there — so **the one
character that works in the settings file is the one that fails at the prompt**, which is precisely
what an adopter copying the declaration would type. The source resolves against the process working
directory, so the command is also root-only.

Two things this repository cannot do for itself and one it can. It cannot run the install — those
commands open an interactive panel — and it cannot verify the result, because a skill registered
mid-session is refused by name. What it can do is stop asserting the state it does not have, which
is the reconcile below.

**The three statements, corrected — and corrected to survive the install rather than to describe
today.** Writing "tier 1 is `CLAUDE.md` alone" would be true this morning and false the moment the
install lands, so each now turns on *whether the harness serves the skill*, with the measurement
attached as evidence rather than as the rule:

- **[`CLAUDE.md`](../CLAUDE.md)** — the membership sentence keeps its property (a description joins
  tier 1 when the harness serves the skill, without the paragraph being edited) and gains the
  measured fact that this file is still the whole of tier 1. *Status* now says **declares** rather
  than enables.
- **[`.handoff/config.md`](../.handoff/config.md)** — same pairing, same correction.
- **[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)** — the log
  entry that put it over its bound gave a **wrong reason and a right conclusion**, and the correction
  says both. Its margin was not restored: re-measured with `wc -l` after the two edits above landed,
  `CLAUDE.md` is 151 against 173, so 151 + 26 = **177, over by four on line count alone** with no
  description counted. Three of those four lines are this task's reconcile — which is T-047's own
  observation arriving from an unexpected direction, and the reason the number was measured here
  rather than back-calculated from a figure in an older log.

**What is deliberately not corrected.** Nothing in T-003's own record. Its review carried criteria 4
and 8 to this task rather than claiming them, which is the thing that worked — the one sentence in
its §3 step 5 that reads as accomplished state is quoted in step 3 above and left where it is, since
editing a closed task's evidence to match a later measurement destroys the audit trail the carry
exists to create.

**Decisions & assumptions**

- **The measurement was taken before the handoff's own pointers were followed any further than
  reading them.** — Step 1's observation is destroyed by the first skill invocation of a session,
  and the resuming session had one chance at it. — 2026-08-07
- **The registration failure is reported as this task's finding, not raised as a child task.** —
  T-050's scope names it in advance: "whether the plugin declared in `.claude/settings.json` is
  picked up from this tree at all. If it is not, that is this task's finding and the registration is
  what gets fixed." METHOD §5's raise-it-elsewhere rule is for findings a task did not go looking
  for. — 2026-08-07
- **The reconcile was held until the maintainer answered, then written to survive the install.** —
  Each of the three statements is false given today's state, and today's state is what the open
  question changed. Correcting them to "`CLAUDE.md` alone" would have been a second write on the same
  sentences the moment the install landed, so each was rewritten to turn on whether the harness
  serves the skill, with the measurement as evidence. — 2026-08-07
- **T-003's record is not edited.** — Its review carried the two criteria here rather than claiming
  them; editing a closed task's evidence to match a later measurement destroys the trail the carry
  exists to create. METHOD §5's rule read in the direction it is usually read backwards. — 2026-08-07

**Outputs produced**
- This record — the measurement itself. `deliverables` stays empty: the task produces an observation,
  not an artifact.
- [`CLAUDE.md`](../CLAUDE.md), [`.handoff/config.md`](../.handoff/config.md),
  [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — the reconcile.

### Step 6 — the install, verified where it lands and where it does not

**Done by the maintainer at user scope on 2026-08-08**, and confirmed by reading the harness's own
state rather than by being told:

| Harness state | Before (step 3) | After |
| :--- | :---: | :--- |
| known marketplaces | absent | present, `directory` source |
| installed plugins | absent | `taskmd@taskmd`, scope `user`, version `0.1.0` |
| the plugin cache | 2 marketplaces | 3 — taskmd among them |
| user-level settings | absent | enabled, and the marketplace declared |

**The probe that matters, and it is stronger than the one T-003 could take.** With the install
complete and every state file above showing it, this session **still** cannot reach the skill:

```text
Unknown skill: taskmd:taskmd
```

T-003 established that the skill list is fixed at session start by writing a throwaway skill
mid-session and having it refused. That left an objection open — a hand-written file dropped into a
folder is not an installed plugin, and might simply have been ignored for being irregular. This
closes it: a plugin installed by the harness's **own** command, registered in all four of its state
files, is refused by name in the same session on the same terms. The list is fixed at session start,
and nothing about the artifact's provenance changes that.

**Where the machine path went, and why that was the whole point of the scope question.** The
harness stored the marketplace source resolved to an absolute path, exactly as step 5 predicted from
the parser — and because the scope chosen was `user`, it went to the harness's own settings, outside
this repository. The tracked `.claude/settings.json` is **byte-identical**, still declaring the
relative `"path": "."` that T-003 **D3** wrote; the working tree gained nothing under `.claude/`; and
the pre-publish check prints nothing. Had the install been taken at project or local scope, that
absolute path would now be in a file a push would send — which is
[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md), raised before the install rather
than after it.

**Still outstanding, and still not this session's to close.** Criteria 1, 2 and 3 need a session that
was *handed* the skill, and the install cannot retrofit one. The next session's first act is the
verification: was `taskmd` in the list it was given, did a request to do task work reach it without
being named, and does naming it work. That is the same shape this task has had from the start — the
difference is that the precondition is now satisfied and measured, rather than assumed from a
declaration.

### Step 7 — the measurement, on a session that was handed the skill

Taken on a session started in this repository on 2026-08-08, after the step 6 install, reading only
what was already in context before anything was invoked. The same three things arrived unasked as in
step 1 — `CLAUDE.md` in full, the agent's cross-project memory index, and a list of available skills
as name + description — but the list is now ~60 entries and **`taskmd:taskmd` is one of them**, under
the `plugin:skill` naming, carrying the whole of its `description`. No text from the *body* of
`skills/taskmd/SKILL.md` was present anywhere.

**T-003 §3's tier table, against this session:**

| Tier | Row's claim | This session |
| :--- | :--- | :--- |
| 0 | the `description` arrives every session, unasked | **confirmed** — present in the skill list before anything was invoked, body absent |
| 1 | the `SKILL.md` body arrives on invocation | **confirmed** — invocation returned the body in full, plus a base directory (see below) |
| 2 | `docs/METHOD.md` when the body points at it | **confirmed, and this time by the skill** — the body's load table says to read it before doing anything to a task, and that is why it was read. Step 4 could only record a different loader |
| 3 | a phase file when its phase begins | **confirmed** — METHOD §7 named `implement`, which was loaded on entering that phase. `specify.md`, `plan.md` and `review.md` were never loaded |

So **criterion 1 is met**: the table is confirmed, not corrected, on the first session able to test
it. Each tier arrived at its own moment and no tier arrived early.

**Criterion 3 is met.** Naming the skill reached it — `taskmd:taskmd` resolved and returned the body,
against the two verbatim refusals recorded in steps 2 and 6 on the same terms. The variable between
them is the install, and nothing else changed.

**Criterion 2 is not met, and the reason is procedural rather than a property of the description.**
This session's first request was a handoff resume, not task work. The handoff then supplied
`python -m taskmd context T-050` literally, so the first task work of the session ran that command
without any routing decision being made — there was nothing for the description to be matched
against. By the time task work proper began the skill had been named, deliberately, to take
criterion 3. **What was observed is that the routing was pre-empted, not that it failed**; a session
whose *first* substantive request is task work, with the skill unnamed and no handoff supplying the
commands, is what remains to be run. That is the one thing this task still owes and it is a session,
not a change.

**What the base directory turned out to be, and the finding in it.** The invocation reported its base
directory inside `~/.claude/plugins/cache/`, under the marketplace, plugin and version — the
install-time snapshot, not this working tree. The snapshot is a copy of the **whole repository**:
`docs/`, `taskmd/`, `tasks/` (52 files, the same count as the tree), `tests/`, `reference/`,
`.handoff/`, `.pytest_cache/` and the gitignored `control/`. Every relative pointer in `SKILL.md`
therefore has two resolutions — `../../docs/METHOD.md` names a real file in the snapshot *and* a real
file in the tree — and they have already diverged: hashed against each other, `docs/METHOD.md`,
`docs/method/implement.md` and `SKILL.md` are identical, while **`CLAUDE.md` differs**, within hours
of the install. This session read the tree's copies because it was working in the repository, so the
divergence changed nothing here; which copy a session gets is currently decided by where it happens
to be rather than by anything written down. That is a second home for every fact the skill points at,
and it is raised as [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) rather
than fixed here — the observation is what this task measures; what the plugin should ship, and
whether its skill may point outside its own folder, is a packaging decision belonging with
[T-006](T-006-package-document-and-publish.md).

**Decisions & assumptions (step 7)**

- **The tier observation was written down before the skill was invoked, and the invocation was then
  made deliberately as the criterion-3 probe.** — Step 1's constraint has not changed: the skill list
  in context is the evidence, and it survives, but a record written after the fact is a
  reconstruction. — 2026-08-08
- **Criterion 2 is recorded as untested rather than argued either way.** — The honest answer to "would
  the description have routed me there" is unavailable from inside a session that has read the
  handoff, the task and the skill body. Criterion 4 is the rule that decides this: what was observed
  is that nothing was routed, and why. — 2026-08-08

### Step 8 — how criterion 2 gets taken, and why no note can carry the instruction

**Answered by the maintainer on 2026-08-08: the next session takes the probe as its first act**, and
this task stays `in_progress` until it has. *Rejected: closing now and carrying criterion 2 to a child
task* — legal under METHOD §2, and it would stop this task being the thing every session trips over,
but the probe is one turn and deferring it buys a record entry instead of a measurement. *Rejected:
declaring it unmeasurable* — step 7 shows the confound was procedural, so the criterion is reachable
and saying otherwise would retire it on the strength of one badly-arranged session.

**The trap, which is the same one that ate this criterion twice.** The probe needs a session whose
first substantive request is task work, with the skill unnamed and nothing supplying the commands. A
handoff cannot deliver that instruction: reading a handoff *is* the confound, and one saying "now ask
for task work without naming the skill" primes the reader more thoroughly than the command line that
pre-empted step 7 did. Nor can this task, for the same reason — a session that opens `context T-050`
has already been told what it is testing.

So the instruction is **to the maintainer, not to the next session**, and it is the only piece of this
project's work that is arranged outside its own records:

1. Start a fresh session in this repository. Do **not** invoke the handoff skill, and do not name
   taskmd.
2. Ask for task work in ordinary words — *"what should I work on next?"*, or *"start the next task"*.
3. Observe whether the skill is reached. Whichever way it goes, that is criterion 2 — a description
   that does not trigger is a T-050 finding and, per *Scope*, a rewritten trigger is then a task of
   its own rather than this one.
4. Only after that, resume normally.

**Decisions & assumptions (step 8)**

- **The probe is arranged by the maintainer out-of-band, and the task records the arrangement rather
  than the instruction.** — Every in-repository channel that could carry it — a handoff, this record,
  a note in `CLAUDE.md` — is read by the session being measured, and reading it is the confound. This
  is the one thing the project cannot hand to its own next session. — 2026-08-08

### Step 9 — criterion 2, taken as step 8 arranged it

**Taken on 2026-08-08 in a separate session**, by the maintainer, exactly as step 8 required: a fresh
session in this repository, the handoff skill not invoked, taskmd not named, no command supplied.

| | Observed |
| :--- | :--- |
| The request | *"what should I work on next?"* — ordinary words, no id, no command, no skill named |
| Handed before anything was invoked | `CLAUDE.md` in full, the memory index, and a ~60-entry skill list carrying `taskmd:taskmd` with its full `description` and **no body** |
| What happened | The session routed to the skill **on the description alone**. The description reads *"…when asked what to work on next"*, which matched the request almost word for word |
| Afterwards | The body, then `docs/METHOD.md`, then `implement.md` — each at its own moment |

**Criterion 2 is met, and observed rather than argued** — the thing steps 5 and 7 each failed to
reach. Tier 0 is also confirmed a second time, independently of step 7 and by a session with no
knowledge of what step 7 had found.

**The confound that survives, recorded rather than glossed.** `CLAUDE.md` is tier 1, so the probe
session was unavoidably told the skill exists and is served before it chose anything. That is much
weaker than step 7's handoff handing over the command literally — being told a tool exists is not
being told to use it, and the description matched the request on its own words — but it is not zero,
and **no probe run inside this repository can remove it**, because the file that mentions the skill
is the one the harness loads unasked. A clean measurement would need a project that uses taskmd and
does not describe it in its always-loaded conventions, which is
[T-006](T-006-package-document-and-publish.md)'s territory and not a gap this task can close.

**How this record was made.** The observation belongs to the probe session, which stopped without
writing it up — correctly, since `review` had not been asked for (METHOD §3.1). This session
transcribed it from that session's transcript rather than from anyone's recollection, and two things
corroborate the account independently of its own summary: the transcript contains
`Launching skill: taskmd:taskmd`, and it is the only session besides this one to reach the skill at
all.

**Decisions & assumptions (step 9)**

- **The probe session's own contemporaneous account is taken as the evidence, not re-derived.** —
  Criterion 4 asks for what was observed; the observation exists only in the session that made it,
  and a later session re-reasoning about it would be producing exactly the argument this task refuses
  to accept. — 2026-08-08
- **The `CLAUDE.md` confound is recorded as a limit of the venue, not carried as a child task.** —
  It cannot be fixed here by any means: removing the mention would make tier 1 false, and running the
  probe elsewhere needs an adopting project. Naming it under T-006 is enough. — 2026-08-08

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The tier table in T-003 §3 is confirmed or corrected against a session that was handed the skill, with what was observed at each moment | met | §3 step 7. **Confirmed, not corrected** — description unasked, body on invocation, `docs/METHOD.md` because the body said so, `implement.md` on entering that phase and no other phase file. Step 9 re-observed tier 0 independently |
| A request to do task work reaches the skill **without the user naming it**, or the failure is recorded with what the session was handed instead | met | §3 step 9. *"what should I work on next?"* routed on the `description` alone, in a session that had invoked nothing. Took three attempts to arrange: step 2 had no skill installed, step 7 was pre-empted by a handoff supplying the command, step 9 was run out-of-band as step 8 set out. One residual confound recorded there and not glossed |
| Naming the skill reaches it | met | §3 step 7 — `taskmd:taskmd` resolved and returned the body, against the verbatim refusals in steps 2 and 6. The install is the only variable between them |
| Whichever of the three fails, the record says what was observed rather than what was expected | met | The criterion that earned this task is step 3's: the plugin was never installed, against three documents already reconciled as though it had been. Then step 7 recorded criterion 2 as *pre-empted rather than failed* when the easier write-up was available, and step 9 records a confound that weakens its own result |

**On the criterion that took three sessions.** Criterion 2 was reachable throughout; what defeated it
twice was the venue, not the description. Step 8 is the part worth carrying forward — the discovery
that **no in-repository channel could carry the instruction**, because a handoff, this record and
`CLAUDE.md` are each read by the session under measurement. That is a general property of measuring
what a session is handed, and it is why the arrangement was left with the maintainer.

**Child fix tasks raised**
- **[T-052](T-052-decide-what-of-claude-a-published-clone-carries.md)** — raised, not carried. Found
  while answering which scope to install at: `.claude/settings.local.json` is not ignored, and the
  harness stores a directory source resolved to an absolute path. METHOD §5's distinction applies —
  this task did not make it false, and `.gitignore` is not what this task measures. Recorded as
  `related` rather than `parent`: it is not part of measuring the tiers.
- **[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)** — raised, not carried.
  Found in step 7 by reading the base directory the invocation reported: the install snapshot is the
  whole repository, so every relative pointer in `SKILL.md` resolves twice, and one of the two files
  has already drifted. Measuring what arrives is this task's; deciding what the plugin ships is not.
  `related`, for the same reason as T-052.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-08 | → done | **Criterion 2 taken exactly as step 8 arranged it, and met.** A fresh session, no handoff invoked, taskmd unnamed: *"what should I work on next?"* routed to the skill on the `description` alone — whose text, *"…when asked what to work on next"*, matched the request almost word for word — with the body, `docs/METHOD.md` and `implement.md` following at their own moments. Tier 0 confirmed a second time by a session that knew nothing of step 7's result. The observation is transcribed from that session's own transcript rather than from recollection, corroborated by its `Launching skill: taskmd:taskmd` event. **One confound recorded rather than glossed**: `CLAUDE.md` is tier 1, so any probe run here is told the skill exists before it chooses — far weaker than a handoff supplying the command, but irremovable inside this repository, and named against T-006 rather than carried as a child. All four criteria met, none carried, so the task closes. What it leaves behind is step 8: no in-repository channel can carry an instruction to a session whose *handedness* is what you are measuring, because reading it is the confound. |
| 2026-08-08 | (no status change) | Maintainer answered how criterion 2 is settled: **the next session takes the probe as its first act**, so this stays `in_progress` rather than closing with the criterion carried to a child. Writing that answer down surfaced the thing that has now eaten this criterion twice — **no in-repository channel can carry the instruction**, because a handoff, this record and `CLAUDE.md` are all read by the session being measured, and reading any of them is the confound. A handoff saying "ask for task work without naming the skill" primes its reader harder than the supplied command that pre-empted step 7 did. So step 8 records the *arrangement* and leaves the instruction with the maintainer: fresh session, no handoff invocation, ordinary words, observe, then resume. That is the one piece of this project's work it cannot hand to its own next session, and saying so is worth more than the criterion. |
| 2026-08-08 | (no status change) | **The measurement the task exists for was finally taken**, on the first session the harness actually handed the skill — `taskmd:taskmd` was in the list it was given, description in full, body absent. T-003 §3's tier table is **confirmed rather than corrected**: description unasked, body on invocation, `docs/METHOD.md` because the body said to, `implement.md` on entering that phase and no other phase file. Criterion 3 passes — the same invocation refused verbatim twice before now resolves, with the install as the only variable. **Criterion 2 was pre-empted, not failed**: the session opened on a handoff resume that handed over the `context` command literally, so no routing decision was ever put to the description; that is recorded as an observation rather than argued either way, which is criterion 4 applied to an inconvenient result. What it still owes is a session, not a change. Found while reading the base directory the invocation reported: the install snapshot is a copy of the **whole repository**, gitignored `control/` included, so every relative pointer in `SKILL.md` resolves both there and in the tree — and `CLAUDE.md` already differs between the two, hours after the install. Raised as T-053, not fixed here. |
| 2026-08-08 | (no status change) | Installed by the maintainer at **user** scope, and verified from the harness's own four state files rather than from being told — marketplace, installed plugin (`taskmd@taskmd`, `0.1.0`), cache and user settings all now carry it. **The probe this made possible is stronger than the one T-003 could take**: with the install complete, this session still gets `Unknown skill: taskmd:taskmd`. T-003 showed the skill list is fixed at session start using a throwaway skill written mid-session, which left open the objection that an irregular hand-written file might simply have been ignored; a plugin installed by the harness's own command and present in all four state files is refused on identical terms, so provenance is not the variable. The scope choice held: the harness stored the marketplace source resolved to an **absolute** path — as predicted from the parser in step 5 — into its own settings, outside this repository, leaving the tracked `.claude/settings.json` byte-identical with T-003 D3's relative path and the pre-publish check printing nothing. Criteria 1–3 remain open and remain un-closable here by construction. *This entry is dated a day after the ones below because the session spanned the boundary — the earlier entries were written on 2026-08-07 and are not misdated.* |
| 2026-08-07 | (no status change) | Maintainer answered: keep the declaration, install by hand. So the reconcile became writable and was taken — `CLAUDE.md`, `.handoff/config.md` and T-047's over-bound entry — each phrased to turn on **whether the harness serves the skill** rather than on today's state, so the install does not immediately falsify them again. **T-047 stays over its bound, for a different reason than it recorded**: the 397 characters were never served, but `wc -l` after these edits puts `CLAUDE.md` at 151 against 173, so 151 + 26 = 177 — over by four, three of them added by this reconcile. That figure was measured rather than carried forward from the older entry, which is what caught it. T-003's own record is left alone: it carried these criteria rather than claiming them, and editing a closed task's evidence to match a later measurement destroys the trail the carry exists to create. What stays open is not this session's to close — the install runs in an interactive terminal, and a skill registered mid-session is refused by name, so criteria 1, 2 and 3 are verified by the session **after** the install, in its first act, for the same reason this task exists at all. |
| 2026-08-07 | → in_progress | Measured, and the answer is the one nobody had checked for: **the plugin is not registered at all**, so the skill was never handed to this session and neither invocation path exists to test. Named invocation is refused by the harness twice, and the harness's own plugin state — known marketplaces, installed plugins, the cache, the catalog — contains no trace of taskmd, while the two plugins it *does* serve are each installed into a versioned cache. The settings shape is not the problem: the same two keys enable a plugin at user level on this machine and that plugin's skills are in the session's list, and the project's trust dialog was accepted. What separates them is an **install**, which the declaration did not produce. So T-003 §3 step 8's consequence is false: the description is not in tier 1, `CLAUDE.md` and `.handoff/config.md` both say it is, and T-047 went over its bound on 397 characters that are not being served. Those three are named as this task's reconcile debt and left uncorrected, because which correction is right depends on the one open question — how this repository should serve its own skill — and because the fix, whichever it is, **cannot be verified by the session that applies it**, which is the same constraint that created this task. Specify and plan were taken in the same pass: the specify was already complete with no open questions, and step 1's observation is destroyed by the first skill invocation of a session, so deferring it a turn would have cost the measurement. |
| 2026-08-07 | → proposed | Carried from T-003's review rather than counted as met, which is METHOD §2's rule for `review`. `xs` because the whole of the work is starting a session and reporting what it was handed; `high` because the claim it checks is R-21's, and R-21 is the requirement this project has already believed wrongly once. |
