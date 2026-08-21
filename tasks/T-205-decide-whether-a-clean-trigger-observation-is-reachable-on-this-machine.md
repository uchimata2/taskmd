---
id: T-205
title: Decide whether a clean trigger observation is reachable on this machine
type: decision
status: proposed
phase: specify
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
- [ ] <written at `specify`>

**Open questions**
- ~~**Is a confounded negative enough to act on?** T-175's result is that the skill was not reached in
  a session that had read the very config the description names. Two confounds each supply an
  alternative explanation, and neither can now be removed.~~ **Answered by the owner on 2026-08-21:
  yes — act on it.** The reason, the two rejections and what the answer rules out are in the Log row
  of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | (no change) | **Answered by the owner: act on the negative.** [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md)'s result is treated as a real risk and the skill's `description` is to be examined, confounds and all. **The asymmetry is the reason, and it is the part worth keeping**: examining a description that turns out to be fine costs effort and is reversible, while shelving the result risks the plugin quietly doing nothing for every adopter — nobody writes this tool's name into their own always-loaded conventions, and not having to is what a skill description is for. *Rejected: shelve it as unanswerable*, which accepts that if the description does fail for adopters, nothing would ever say so. *Rejected: manufacture a cleaner venue* — removing this tool's name from the machine's user-level instruction file and probing a throwaway project outside the shell-first mode — which removes two of the three confounds and tests a synthetic project rather than an adopter, the objection the venue selection of 2026-08-19 was built around. **What it rules out**: no third venue is being sought, so §1's *Out: re-running the observation* has no branch behind it any more. This task still owes its own criteria and its lifecycle, and the follow-on description task is **its** to raise rather than something raised ahead of it. |
| 2026-08-21 | (no change) | **Confirmed by the owner on 2026-08-21 as belonging**, having been raised outside the two-task grant of the same day — the same ruling as on [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md). It matters more here than there: this task is the only thing carrying the expired premise, so cancelling it would have put that finding back out of every view. Written into this record rather than left in the reporting thread, for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) gives. |
| 2026-08-21 | → proposed | Raised by [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 step 6, which is the step its fifth criterion required. `medium` and `s`: it settles whether anything follows that observation, and it is a decision rather than work. **It exists because a premise expired**: [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) put the naming confound in the project's own conventions and a venue was selected on that basis; the user-level instruction file names the tool in every session on this machine, so the selection could not have removed it. Its parent is T-175 rather than the closed umbrella above it, because that is where the question was produced. |
