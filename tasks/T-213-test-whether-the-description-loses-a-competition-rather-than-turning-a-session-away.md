---
id: T-213
title: Test whether the description loses a competition rather than turning a session away
type: research
status: done
phase: review
parent: null
blocked_by: []
related: [T-206, T-175, T-205]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-213 — Test whether the description loses a competition rather than turning a session away

## 1. Specify

**Outcome**
A tested answer to whether the shipped `description` fails to *win* against a realistic field of
other skills in a project on a non-file backend — as distinct from failing to *apply*, which
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) tested
and answered.

**Why this one**
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) ran its
rig on 2026-08-22 and got a clean null: **6 of 6 arm runs invoked the skill**, three under each
wording, in a project whose config says there are no task files. So the opening clause does not give
a session a reason to *stop*.

**That answers the hypothesis T-206 stated, and it does not explain the observation both tasks came
from.** [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) watched a
session that was served this skill **among 68** and never invoked it. T-206's arms serve **one**
skill, so a prompt near its own words has nothing to lose to — the rig can detect a description that
turns a session away and cannot detect one that comes second.

**The two hypotheses are not the same and only one has been tested.** *Does not apply* is about the
description's content read on its own. *Does not win* is about it read beside sixty-seven others, and
the observation is equally consistent with both. Closing the question on T-206's null would be
reading a result about the first as though it settled the second.

**Scope**
- In: a rig whose arms carry a **realistic field** of other skills, not one
- In: the same two wordings T-206 built, so the arms remain comparable to its runs
- In: what counts as *winning* when several skills could plausibly serve one request
- Out: T-206's verdict, which stands. This does not re-open it
- Out: a third real venue.
  [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) settled
  that none is sought, and the owner licensed a synthetic rig on 2026-08-22

**Inputs**
- [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) §3 —
  the rig, its build script, the two wordings, and the eight runs
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 — the
  observation, and the field of 68 it happened in
- `plugin/skills/taskmd/SKILL.md` — the description, unchanged by T-206

**Acceptance criteria**
- [ ] The result names a direction and does not hedge — the description loses the competition, does
      not, or cannot be determined by this rig
- [ ] **The field is realistic and its composition is stated**, so a reader can judge whether the
      competitors were ones a real session would have. What failure looks like: a field of decoys
      chosen to be easy to beat, which measures nothing
- [ ] The arms are shown to differ **only** in the wording, by diffing them — T-206's criterion, and
      the field must be identical between arms as well
- [ ] Each arm's instrument is shown to have loaded the wording it is testing, quoted from the run
- [ ] The run count per arm is fixed and stated before any result is read
- [ ] **The confound T-206 could not remove is shown to be removed here** — its runs are quoted
      beside these so the difference between one skill and a field is visible, not asserted

**Open questions**
- **None.** The scope is the residual T-206 named when its own confound list was written.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Recover [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md)'s rig — `build.py`, `run.py`, the four projects and the **eight raw streams** — into this task's own scratch, and prove the instrument can start before anything is built | the recovered rig, and one headless run that reaches a result rather than the `401` T-206 met |
| 2 | Take the field from the **observed session's own record** of what it was handed — the 68-skill listing [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 step 3 read — and state its composition and its source | the field, its size, where it was read from, and the rejected alternatives |
| 3 | Fix the run count **and** the win rule in writing before the rig is built | both recorded in §3, attested by this plan's date rather than by §3's own ordering |
| 4 | Extend `build.py` so all four projects carry the **identical** field, with the arm's own wording substituted for the real entry, then diff the arms | the diff, showing one line differs and it is the description |
| 5 | Run the arms and the controls, quoting each arm's loaded wording from its own stream | per-run routing, every skill invoked and in what order, and the quoted wordings |
| 6 | Quote T-206's eight runs beside these, from the recovered raw streams rather than from its record's prose | the side-by-side that makes one-skill against a field visible |
| 7 | Name the direction, and take *cannot be determined* if that is what the split says | the verdict, and any task the result raises |

**Step 1 measures before steps 4–5 commit, and it is not a formality.** T-206's first attempt could
not start — the headless CLI answered `401 OAuth access token has expired` — and no arm ran. A rig
that cannot start produces nothing, and the most dangerous place to stop is a run that looks
permitted. The rig itself survives whole in a prior session's scratch, which is why this is a
recovery rather than a rebuild; a scratch directory is not a durable home, so step 1 copies it before
reading anything from it.

**The field is the observation's own field, and that is the whole of criterion 2's answer.**
[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 step 3 read the
session's record of what it was handed and found 68 skills with this one among them. Using that
listing means the competitors are the ones a real session actually had, so nobody has to be persuaded
they were realistic. *Rejected: a field assembled by hand from plausible-looking skills* — the decoy
failure criterion 2 names by name, and unfalsifiable besides. *Rejected: the skills served to
whichever session builds the rig* — a different field from the one the observation happened in, and
this repository's own harness rather than the migrated-away project's.

**The real entry must come out of the field, or the arms contaminate each other.** The recovered
listing contains this skill's own description. Left in, every arm would carry the shipped wording
beside the wording under test. So the build removes that one entry and substitutes the arm's
`rigtask` wording in its place — 67 competitors plus the arm's skill, which keeps the field size at
the observed 68 and keeps the arms differing in one line.

**Fixed now, before the rig exists: five runs per arm, two per control.** T-206 used three and one,
and recorded that only its own ordering attested the count. Writing it at `plan` is the stronger
form of the same guarantee. **Its limit is stated with it**: five runs separate 0/5 from 5/5 and
cannot separate 3/5 from 2/5, so a middling split is *cannot be determined by this rig* — criterion
1's third answer, which step 7 must take rather than round to a direction.

**Winning is invocation, and the ordering is recorded beside it.** A run counts as a win if a `Skill`
tool call naming `rigtask` appears in the event stream — T-206's detection rule unchanged, so the two
sets of runs stay comparable. Every skill invoked and its order is recorded as well, so *came second*
is visible rather than inferred. *Rejected: winning means invoked first* — a session may reasonably
open a general skill and then this one, and scoring that as a loss would measure politeness.

**The controls carry the field too.** With 68 skills in play, an all-null result is equally
consistent with competition and with a dead instrument. The controls sit on the backend the
description already gets right, with the same field, so they distinguish the two before any negative
is read — which is the job T-206's controls did for it.

**Two confounds carry over unchanged and one is new.** The skill is named `rigtask`, so the
description's closing clause *whenever the user says taskmd* stays unexercised; the arms serve a
project-local skill rather than a plugin snapshot. New: the field is reconstructed from a listing
rather than served by the same mechanism that served it originally, so it reproduces the
descriptions and not necessarily their ordering or weight.

**Whether anything ships is not settled here.** T-206 drafted and priced a candidate wording and did
not apply it. If this rig finds the description loses, applying that candidate is a change to a
shipped file on evidence the owner has not yet seen — so it is raised, not made.

## 3. Implement

**Decisions & assumptions**

- **Authorised beyond `plan` on 2026-08-23.** The grant of 2026-08-22 covered `plan` and said so.
  The owner then asked for every task complete except the release and what is scheduled after it,
  which is this record's authorisation for the remaining phases — recorded here rather than inferred
  later.
- **The rig was recovered, not rebuilt** — 2026-08-23. `build.py`, `run.py`, the four projects and
  the eight raw streams survived whole in a prior session's scratch and were copied into this task's
  own before anything was read from them.
- **New run labels, so nothing overwrites T-206's evidence** — 2026-08-23. `run.py` writes
  `out-<label>.jsonl` and the recovered streams use the same arm names; every run here is prefixed
  `t213-`. Step 6 reads those eight files, so overwriting them would have destroyed the comparison
  the last criterion asks for.
- **The verdict is split, and both halves are stated rather than the convenient one** — 2026-08-23.
  The primary question is answered; the arm-versus-arm comparison is **cannot be determined by this
  rig**, which is the third answer criterion 1 permits and the ceiling the plan named in advance.

**Outputs produced**

- no repository file. The rig, the 14 new streams and the 8 recovered ones live in this task's
  scratch; the result is this record

**Verification**

**Step 1 — the instrument starts, which is what T-206 could not do.** A headless session in an empty
directory returned a real event stream and exit 0. No `401`. Nothing was built until this passed.

**Step 2 — the field, from the observed session's own record.** Every transcript on this machine was
searched for a `skill_listing` attachment carrying `taskmd`. Exactly one session in a migrated-away
sibling project listed **68**, first timestamped **2026-08-21T12:17:30Z** — the date T-175 records
for the observation. Its 67 non-taskmd entries are the competitors, written out as real project
skills.

**Step 4 — the arms differ in one line.** `diff -r arm-old arm-new` returns exactly one hunk, the
`description:` line of `rigtask/SKILL.md`. Both directories carry 68 skill folders built from one
list.

**Step 5 — the runs. Counts fixed at `plan`, before the rig existed: five per arm, two per control.**

| Arm | Wins | `rigtask` reached at tool # |
| :--- | :---: | :--- |
| `arm-old` — shipped wording, issue backend | **5/5** | 5, 6, 8, 5, 4 — mean 5.6 |
| `arm-new` — candidate wording, issue backend | **5/5** | 7, 5, 6, 5, 5 — mean 5.6 |
| `ctl-old` — shipped wording, file backend | **2/2** | 4, 4 |
| `ctl-new` — candidate wording, file backend | **2/2** | 3, 3 |

**No competitor skill was invoked in any of the 14 runs.** `rigtask` is the only `Skill` call in
every stream.

**The controls did their job.** They reach the skill at tool 3–4 against the arms' 4–8, so the
instrument still distinguishes the backend the description already routes well from the one under
test — which is what stops an all-win result being read as a dead rig.

**Each arm loaded the wording it was testing**, read back from each run's own served listing rather
than from the file that was written:

```text
arm-old / ctl-old  ->  1 distinct wording: "Work with tasks kept as Markdown files - one per task…"
arm-new / ctl-new  ->  1 distinct wording: "Work with tasks tracked by rigtask - one task per record…"
```

**Step 6 — T-206's eight runs, re-read from the recovered streams with the same win rule.**

| | Field | Result |
| :--- | :--- | :--- |
| T-206, 2026-08-22 | **1 skill**, no competition | 8/8 — arms 3/3 and 3/3, controls 1/1 and 1/1 |
| T-213, 2026-08-23 | **77 skills served** | 14/14 — arms 5/5 and 5/5, controls 2/2 and 2/2 |

**So the confound T-206 named is removed and the answer did not move.** That is what criterion 6 asks
to be visible rather than asserted.

**The field served was 77, not the 68 that was built — measured, and it matters.** Nine skills came
from the running machine's own user-level plugins rather than from the observed session: six `bpmn`
sub-skills, `htmldeck`, `humanizer`, and **the real `taskmd`, carrying its shipped description**. The
plan's contamination guard removed `taskmd` from the *reconstructed* field and could not remove what
the harness adds on top. **Every arm therefore carried the shipped wording beside the wording under
test**, which is the contamination the plan set out to prevent, arriving by a route it did not
consider.

**What that costs, in both directions.** It is a confound on the **comparison**, and a neutral one:
both arms were contaminated identically, so it favours neither. It **strengthens** the primary
result — a taskmd-shaped description was invoked in 14 of 14 runs against 76 competitors, one of them
a near-duplicate of itself.

**Step 7 — the verdict, in two parts.**

1. **The description does not lose the competition.** 14/14, against a served field of 77. A
   direction, not a hedge.
2. **Whether the candidate wording beats the shipped one cannot be determined by this rig.** 5/5
   against 5/5, with identical mean invocation position — the ceiling the plan named in advance,
   where five runs separate 0/5 from 5/5 and nothing finer.

**And the rig does not reproduce the observation, which is the result nobody planned for.** The
session T-175 observed invoked nothing; here the skill was invoked every time. So **neither** of the
two explanations this task was built to separate occurred, and what needs explaining is the gap
between the rig and the venue. The three carried confounds are the candidates — the skill is named
`rigtask` so the description's closing clause stays unexercised, the arms serve a project-local skill
rather than a plugin snapshot, and the field is reconstructed rather than served by the mechanism
that served it. Raised as
[T-240](T-240-the-competition-rig-does-not-reproduce-the-silence-it-was-built-to-explain.md).

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The result names a direction and does not hedge — loses, does not, or cannot be determined | met | Both parts named. **Does not lose**, 14/14. And **cannot be determined by this rig** for the arm comparison, 5/5 against 5/5 — the third answer taken because it is what the split says, not to avoid one |
| The field is realistic and its composition is stated | met | 67 competitors read from the observed session's own transcript, the one listing 68 skills first timestamped 2026-08-21, which is T-175's recorded date. **And the field actually served was 77** — nine came from this machine, one of them the real `taskmd`. Measured and stated, with what it costs each half of the verdict |
| The arms differ **only** in the wording, shown by diffing, and the field is identical between them | met | `diff -r arm-old arm-new` returns one hunk: the `description:` line. Both serve 68 skill folders built from one list |
| Each arm's instrument is shown to have loaded the wording it is testing, quoted from the run | met | Read back from each run's own served listing rather than from the file that was written: one distinct wording per arm, and the right one |
| The run count per arm is fixed and stated before any result is read | met | Fixed at `plan` — five per arm, two per control — attested by that phase's date, which precedes the rig's existence, and quoted in the driver's own docstring |
| **The confound T-206 could not remove is shown to be removed here**, its runs quoted beside these | met | The two-row table in §3: one skill and 8/8 against 77 skills and 14/14, re-read from T-206's raw streams with the same win rule rather than from its record's prose |

**Child fix tasks raised**
- [T-240](T-240-the-competition-rig-does-not-reproduce-the-silence-it-was-built-to-explain.md) — the
  rig does not reproduce the observed silence. **A soft edge, not a child**: this record's outcome is
  a verdict on the competition question and that verdict exists. Why the venue and the rig disagree is
  a further question, not a missing piece of this one.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 recorded none and none arose
that belongs here. **Two things are flagged rather than left implicit.** The candidate wording T-206
drafted is **not** applied, because this rig gives no evidence it is better — 5/5 against 5/5 — and
§1 says a change to a shipped file on evidence the owner has not seen is raised, not made. And the
contamination above is a defect in a scratch rig rather than in anything shipped, so it is recorded
here and carried by T-240 instead of being given a task of its own.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | planned → done | **Closed: six criteria, six met, and the verdict is in two parts.** **The description does not lose the competition** — 14 invocations in 14 runs against a served field of 77 skills, with no competitor skill invoked in any run. **Whether the candidate wording beats the shipped one cannot be determined by this rig** — 5/5 against 5/5 with identical mean invocation position, which is the ceiling the plan named in advance rather than a result. **Authorised beyond `plan` by the owner on 2026-08-23.** **Step 1 was the gate T-206 failed and it passed**: a headless session started, exit 0, no `401`. **The field is the observed session's own** — the transcript listing 68 skills first timestamped 2026-08-21, T-175's recorded date. **The field actually served was 77, nine of them from this machine including the real `taskmd`** — the contamination the plan set out to prevent, arriving by a route it did not consider; neutral between the arms and strengthening the primary result. **The finding nobody planned for is that the rig does not reproduce the observation at all**: the observed session invoked nothing and here it invoked every time, so neither explanation this task was built to separate occurred. Raised as [T-240](T-240-the-competition-rig-does-not-reproduce-the-silence-it-was-built-to-explain.md). **The candidate wording is not applied**, there being no evidence it is better. |
| 2026-08-22 | proposed → planned | Plan written under the owner's authorisation of 2026-08-22 recorded above, which covers **this phase and no more**. **Step 1 measures before steps 4–5 commit**, because the instrument has already failed to start once: [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) met `401 OAuth access token has expired` and ran no arm. **Two things were found while planning and neither was absorbed.** T-206's rig survives whole in a prior session's scratch — `build.py`, `run.py`, the four projects and the eight raw `.jsonl` streams — so this is a recovery rather than a rebuild, and criterion 6 can quote its runs from the streams instead of from its record's prose. And the field has a source nobody had named: [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 step 3 read the observed session's own record of the 68 skills it was handed, so the competitors can be the ones a real session actually had rather than a set assembled to look realistic — which is what criterion 2 asks for and the one thing a hand-built field could never supply. **The run count is fixed here, at `plan`, and its power is stated with it**: five per arm separates 0/5 from 5/5 and not 3/5 from 2/5, so a middling split is criterion 1's *cannot be determined by this rig* rather than a rounded direction. **One thing is deliberately left for the owner**: if the rig finds the description loses, applying T-206's drafted candidate wording is a change to a shipped file, and step 7 raises it rather than makes it. |
| 2026-08-22 | (no change) | **Authorised by the project owner on 2026-08-22**, answering the batched question of that date. §1 records no open question; what this task lacked was authorisation, having been raised after the eight-task grant of the same date and named as outside it in the Log of every record that grant touches. The owner's word was *do it*. **What it covers, read against `CLAUDE.md`'s *one phase per request*: the next phase only — `plan` — because no wider extent was named.** A later session must not read it as the full lifecycle: the grant of the same date that did cover multiple phases said so in those words, and this one does not. **What it does not cover:** any other task, and any answer — a grant of phases cannot settle a question that is the owner's. Recorded here rather than in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached. |
| 2026-08-22 | → proposed | Raised from [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) while writing that task's confound list, which is where its own rig's limit became legible. T-206 got a clean null — 6 of 6 arm runs invoked the skill — and that answers *does the clause turn a session away*. It does not answer *does the description come second among 68*, which is what [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) actually watched. Raised rather than folded in: T-206's run count was fixed before its results were read, and adding a condition after seeing a clean null is the iteration that criterion exists to prevent. `m` because a realistic field has to be built and justified, and the justification is the hard half. |
