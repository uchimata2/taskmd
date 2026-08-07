---
id: T-050
title: Measure the skill's tiers on a session that was handed it
type: fix
status: proposed
phase: specify
parent: T-003
blocked_by: []
related: [T-006]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-07
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
| 2026-08-07 | → proposed | Carried from T-003's review rather than counted as met, which is METHOD §2's rule for `review`. `xs` because the whole of the work is starting a session and reporting what it was handed; `high` because the claim it checks is R-21's, and R-21 is the requirement this project has already believed wrongly once. |
