---
id: T-175
title: Observe whether the skill triggers in a project that has migrated its backlog away
type: research
status: proposed
phase: specify
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
- [ ] <written at `specify`>

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-21, and not yet acted on.** The owner granted a **new session** two tasks: [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) **and stop**, then [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) **through its full lifecycle**. Written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). **It reaches these two and no others.** *And stop* names a specific thing not to do: [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) is T-201's sibling finding and the owner chose not to spend the session on it, so closing T-201 leaves [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) open on its other child, and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) open with it (`audit.md` step 5). Neither umbrella is to be closed. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: the qualifying project that is *further* from task work, and one session.** Asked in the backlog-wide round of 2026-08-19. The reason is that a trigger there is unconfounded — nothing about that project's own subject nudges the description into matching — so a positive means what it says and a negative is honest. *Rejected: the tracker-shaped project*, likelier to fire and unable to distinguish a matched request from a matched subject. *Rejected: both, one session each*, which would let the two hits be compared and costs a second session for a distinction one clean venue does not need. **A risk surfaced while resolving which checkout that names, and it belongs here**: the venue's value rests entirely on that project not naming this skill in its always-loaded conventions, which is the confound [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) §3 step 9 called unremovable from inside this repository. It has an open issue of its own about whether to commit its taskmd and handoff configs, and how that is answered could put the skill's name in front of every session there. **The venue is destructible and nothing currently watches it**, so `specify` states the precondition it depends on rather than assuming it holds on the day. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review under [`review`](../plugin/skills/taskmd/docs/method/review.md) step 5 — a question aimed at someone who is not doing the work fails no criterion, so nothing else would have carried it, and it leaves every view the moment its parent closes. `high` because it is the half of the installation decision that is still unevidenced after T-168, and because it also closes a residue [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) recorded as out of reach. **Not covered by the authorisation of 2026-08-18.** |
