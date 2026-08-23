---
id: T-231
title: Cut the next release
type: deliverable
status: proposed
phase: implement
parent: null
blocked_by: [T-232, T-242]
related: [T-182, T-085, T-135, T-223]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-23
deliverables:
  - plugin/.claude-plugin/plugin.json
---

# T-231 — Cut the next release

## 1. Specify

**Outcome**
A tagged, published release of taskmd whose manifest, tag and release note agree, cut by
`docs/PUBLISHING.md`, and a record of what the cut had to be stopped for.

**Why this one**
The owner wants a release soon, and until now it had no record. Every other release this project has
made left one: the act itself is a handful of commands, and everything that has gone wrong went wrong
around it rather than in it. Three things this project already knows and that a release with no task
would have to remember unaided:

- **A bump exists because `claude plugin update` compares version strings.** A directory install whose
  manifest never changes reports *already at the latest version* and keeps serving its snapshot.
- **A release is not the last step of a release.** `0.4.0` shipped with nothing checking it from
  outside; [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) is why
  `0.5.0` did not, and it closed with half proven and half unreachable from any machine here.
- **The gate at `docs/PUBLISHING.md` §5 was red for two releases and nobody had disobeyed it** —
  nobody had run it. The suite runs it now, which is a reason to trust it and not a reason to skip
  reading its count.

**Scope**
- In: the version bump, `docs/PUBLISHING.md`'s procedure end to end, the tag, and the published release
- In: which milestone this release ships, and therefore what
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) runs §7 against
- In: **what the cut was stopped for.** A release that reports nothing had a gate that examined nothing
- Out: writing the release note to the rule and recording whether the rule caught anything. That is
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), which the owner
  scheduled after this one
- Out: **the pre-release audit.** It is not a step in the release procedure and never becomes one, which
  the method document says in its own words; the owner's instruction of 2026-08-22 keeps the two apart
- Out: anything a session may do unattended. **This record is deliberately outside the unattended grant
  of 2026-08-22** — tagging and publishing are outward-facing acts and the owner's to make

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) — the procedure, §5's gate, §6's pre-publish check, and
  §7's release-note rule
- `plugin/.claude-plugin/plugin.json` — the manifest, and the only place the version is written
- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — what verifying a
  release from outside proved last time, and which half of it could not be run from any machine here

**Acceptance criteria**
- [ ] The manifest version, the tag and the published release all name the same version
- [ ] `docs/PUBLISHING.md` §5's gate and §6's pre-publish check were both **run**, and their output is
      recorded — including §5's file count, not only its silence
- [ ] Which milestone the release ships is stated, so §7 has a set to run against
- [ ] What the cut was stopped for is recorded, and if the answer is *nothing*, how that was checked
- [ ] Whether this release is verified from outside is decided and recorded either way

**Open questions**

*All three answered by the **project owner** on **2026-08-23**. Struck through with the answer, and
the original wording and recommendation kept beneath each, so a later reader can see what was chosen
over what.*

- ~~**Does a verification-from-outside task follow this one?**~~ **Answered 2026-08-23: yes.**
  Raised as [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md),
  which carries `blocked_by` naming this record, so the ordering rule reports it held rather than a
  sentence here doing it. *Original: — the project owner. The recommendation is* **yes, and blocked
  by this**: `0.5.0` had one and `0.4.0` did not, and the difference is the whole of what
  [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) records.
  *Against it: T-085 also found half of that verification unreachable from any machine here, so a
  repeat buys less than the first one did and the reachable half is the cheaper half.*
- ~~**Is a third exception taken, or does M6 ship as `0.6.0`?**~~ **Answered 2026-08-23: no
  exception — ship `0.6.0`.** *Original, corrected 2026-08-22: this asked "which version number" and
  called it not derivable, which was wrong.* [`tasks/README.md`](README.md) *states the rule and its
  two exceptions, so the default is* `0.6.0` *and the only judgement left is whether this is a third
  exception. The recommendation was* **no exception, ship `0.6.0`**: *the two that exist were
  mid-milestone batch bumps taken to get fixes out, and this is a milestone.*
- ~~**Which milestone does this release ship, given M6 holds ten open tasks?**~~ **Answered
  2026-08-23: ship M6 as it stands.** The alternative offered — move what is not release-critical to
  a later label first — was not taken. *Original: — the project owner. M6's three stated capabilities
  are all closed and none of the ten is one of them, so this is a scoping decision rather than a
  lookup.*

~~**One question the instruction to ship does not answer, and it is the owner's.**~~
**Answered 2026-08-23: no audit before this tag.** The owner will run one **after** the release and instructed that this session not deal with it — so **no audit task is raised here**, and the boundary in `CLAUDE.md` and in every grant row of 2026-08-22 stands unchanged: a session does not start one. The release therefore has nothing in front of it. *The question as it stood, kept because the answer is a change of sequence the owner stated on 2026-08-22 and a later reader should see it was noticed rather than overlooked:* On 2026-08-22 the same owner said a session should work *"toward a release they want soon, **stopping before the audit** that will precede it"* — so an audit was, in their own words, going to come first. The instruction of 2026-08-23 is to ship in a new session and says nothing about one. **Either the audit is no longer wanted before this tag, or it still is and the instruction named the goal rather than the next step**; both readings are ordinary and the difference is a release. **Recommendation: ask before tagging, and do not infer it from the silence** — a boundary the owner stated in those words is not lifted by an instruction that does not mention it. Cheap either way: the question is one line, and [the pre-release audit method](../plugin/skills/taskmd/docs/method/pre-release-audit.md) now ships, so running one is possible for the first time. *Against asking: the owner has just answered three questions on this record and may reasonably have considered the sequence settled.*

**What the third answer now commits to, because its premise moved.** It was written when M6 held
**ten** open tasks; seven of those closed on 2026-08-23 and two more were raised and closed the same
day. What M6 holds now is this record, the release note that follows it, and one research task —
`taskmd list --work_package M6 --open` is what says so, and no count is written here. **So M6 does
not close when the tag goes out**, because the label closes on membership and a research task will
still be in it. That is a consequence of shipping as-is rather than a problem: the next session
should not read an open M6 as a reason to stop.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Run `docs/PUBLISHING.md` §7's three counts against M6, before anything is written or bumped. | The three figures, recorded, and whether they sum |
| 2 | Run §5's dash gate and read its **count**, not its silence. | The file count and the gate's own exit code, recorded |
| 3 | Run §6's pre-publish leak check twice — with the fixture exclusion and without it. | Both outputs, recorded, showing the accepted set and that the check fires |
| 4 | Set `plugin/.claude-plugin/plugin.json` to the version §1's second answer fixed. | The manifest at `0.6.0` |
| 5 | Compose the tag message and release body **to a file**, never through a shell. | Two files, unstyled, ready for §2's humanizer pass |
| 6 | Commit, `git tag -F`, push, and `gh release create --notes-file`. | The tag and the published release |
| 7 | Record what the cut was stopped for, or how *nothing* was checked. | This record's §3 |

Step 1 is first on purpose, and it is the sequencing rule in [`plan`](../plugin/skills/taskmd/docs/method/plan.md)
doing its work rather than a formality: it is the one step whose result can invalidate every step
after it. It did.

## 3. Implement

**Decisions & assumptions**

- **The cut is stopped at step 1, and steps 4 to 6 were not run — 2026-08-23.** §7's counts do not
  sum: 108 closed tasks in M6, 11 marked `adopter_visible: yes`, 19 marked `no`, and **78 carrying no
  value**. §7 says an unmarked task blocks the note and does not pass as `no`. Raised as
  [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md), which
  now blocks this record. *Rejected: mark the 78 in passing and carry on.* The derivation was
  computed — it is in T-242 §1 and yields 60 `yes` and 18 `no` — and applying it unattended was
  refused for one reason: a release note is a dated public record that
  [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) forbids
  rewriting, so a note resting on 78 marks made silently at the moment of writing prose about the
  release is the exact thing §7 says the field exists to prevent. Stopping is recoverable; the note
  is not.
- **The manifest was not bumped either — 2026-08-23.** A version bump with no tag behind it leaves
  the repository claiming a release that does not exist, and `claude plugin update` compares version
  strings, so a directory install would start reporting a version nobody published. The bump belongs
  to the same act as the tag.
- **The owner's instruction of 2026-08-23 covers the full lifecycle of this record, unattended** —
  given on resuming the handoff, in these words: *"Do the full release. Deploy, Tag, Create release,
  update project, commit and push, unattended."* It is recorded here rather than inherited, per §1's
  note that this record sits outside the grant of 2026-08-22. **It authorized the acts; it did not
  answer what stops them**, and §1's own acceptance criteria ask for a stop to be recorded rather
  than worked around.

**What the two mechanical gates said**

§5's dash gate, exit code captured separately from the pipe:

```text
4 file(s) covered
EXIT=1
```

Exit 1 is the clean outcome in §5's own table, and the count is the half that matters: four files
covered, not zero. §6's leak check, both runs, reduced to one line per file:

```text
with the fixture exclusion:      2 hits in the T-085 record        (the whole accepted set)
without the fixture exclusion:   those 2, plus exactly 5 in the leak-check fixture
```

The second run is what a clean tree cannot prove on its own: every class in the pattern still fires,
so the first run's near-silence is a pass rather than a check that read nothing.

**Outputs produced**
- none. No commit, no tag, no release, no manifest change.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The manifest version, the tag and the published release all name the same version | not met | None of the three exists. The cut stopped at §7 |
| §5's gate and §6's check were both **run**, and their output recorded — including §5's file count | met | §3 above, both gates, with the count and the exit code rather than the silence |
| Which milestone the release ships is stated, so §7 has a set to run against | met | M6, answered by the owner on 2026-08-23 and recorded in §1. It is what §7 was run against |
| What the cut was stopped for is recorded, and if the answer is *nothing*, how that was checked | met | §7's counts, and [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) |
| Whether this release is verified from outside is decided and recorded either way | met | Yes, decided by the owner on 2026-08-23 and carried by [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) |

Four of five criteria are met and the first cannot be met by this session. The record stays open on
its new blocker rather than closing over a criterion nothing will meet.

**Child fix tasks raised**
- [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) — as a
  dependency, not a child. It is not part of this record's outcome; it is a thing this record cannot
  proceed without, which is the distinction [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4
  draws.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **The cut was attempted under the owner's unattended instruction of 2026-08-23, and stopped at the first step of its own plan.** `docs/PUBLISHING.md` §7's counts do not sum — 108 closed tasks in M6, 30 marked, **78 with no `adopter_visible` value at all** — and §7 says an unmarked task blocks the note. Raised as [T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) and recorded here as a dependency. **Nothing outward-facing was done**: no manifest bump, no commit of one, no tag, no release. **Both mechanical gates were run and passed** and their output is in §3 — §5's gate covering four files at exit 1, and §6's leak check in both of its runs, the second proving every class still fires. So the release is held by one thing and it is named. `phase` advances to `implement` because that is where the work reached; `status` is left alone, since the tool derives *blocked* from the edge and writing it twice is the one rule this project does not break. |
| 2026-08-23 | (no change) | **The owner answers the fourth question: no audit before this tag.** They will run one after the release and said not to deal with it now, so **nothing was raised for it** — recording the decision is the whole of the work, and the standing boundary that a session starts no audit is unchanged rather than lifted. **The release now has nothing in front of it.** Asked rather than inferred, because the same owner had said on 2026-08-22 that an audit *would* precede the release, and a sequence stated in those words is not reversed by an instruction that omits it — the answer confirms the change and costs one line, which is what asking was for. |
| 2026-08-23 | (no change) | **The owner answers all three questions, and instructs that the release be cut in a new session.** **Yes** to a verification-from-outside task, raised as [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) with `blocked_by` naming this record — raised now rather than at tag time, because a task that exists only as an answer inside a closed question is invisible to every view, which is the defect [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) recorded. **No third exception: `0.6.0`.** **Ship M6 as it stands**, the offered alternative of moving non-release-critical work to a later label declined. **`waiting_on` is cleared**: it was set on 2026-08-23 because the release was the owner's act with nothing else holding it, and the instruction to ship removes that gate — the field is the one [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) built, so leaving it set would make a view say this is still waiting on a person. **No phase is advanced here.** The answers are recorded and the work is the next session's; `specify` is not closed by a session that was asked to write a handoff. **The third answer's premise moved and the answer is recorded against the premise it now has** — §1 says what shipping as-is commits to, which is that M6 does not close when the tag does. |
| 2026-08-22 | (no change) | **Reconcile: one of this record's open questions was answered by a project document, and this record said it was not derivable.** [`tasks/README.md`](README.md) states the rule in its own words — *the digit says which release the work is scheduled into, `M5` ships as `0.5.0`, `M6` as `0.6.0`* — with two named exceptions, `M2` as `0.4.0` and `M3` inside the `v0.3.0` batch bump. So the default **is** derivable and it is `0.6.0`; the judgement that remains is narrower, and it is whether to take a third exception. The question is corrected in §1 rather than deleted, because *not derivable* was wrong and a reader of this record would have gone looking for a decision nobody had to make. **And the milestone question is live rather than a formality.** M6's purpose in that same document names three capabilities — the GitHub Issues migration, taskmd as a tracker binding for the handoff skill, and what `check` does with a section reference — and all three are closed ([T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md), [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) with [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md), and T-093). The ten tasks still open in M6 are none of those. That is not a defect in the index, which says in its own words that a purpose is not an exit criterion — but it makes *which milestone this release ships* a real decision for this record, not a lookup. |
| 2026-08-22 | (no change) | **Blocked by [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md), by the owner's decision of 2026-08-22.** `plugin/skills/taskmd/docs/BINDING.md` ships, and cutting a release now would publish a clause this project has already measured and found wanting — [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md)'s verdict is a **FAIL** against a bar fixed before its run. *Rejected: release now and repair after* — nothing an adopter meets is wrong today, both readers shipped a declaration, so the cost of shipping is a worse binding somebody writes later rather than a broken one now; the owner weighed that and chose to hold. **The edge is recorded here rather than as a sentence**, because this record's blocker is a task and therefore expressible — which is exactly what [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)'s was not until this record existed. |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, when they said a release was wanted soon and a survey of the open backlog found **no task carried it**. **Raised rather than left as an act** for the reason this project's own records give twice over: `0.4.0` shipped with nothing checking it from outside, and the dash gate was red for two releases because it lived in a document read only at publication. An act with no record repeats both. **Deliberately outside the unattended grant of the same date** — tagging and publishing are outward-facing and the owner's to make, and the grant's own boundary says the release is not in it. **It gives [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) a blocker it never had**, which is worth more than it looks: that record was gated on *there being a release to make*, an event no field could carry, and it sorted as startable in every view. The gate is now an edge. |
