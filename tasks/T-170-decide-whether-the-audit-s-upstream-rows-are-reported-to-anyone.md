---
id: T-170
title: Decide whether the audit's upstream rows are reported to anyone
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-152]
work_package: M6
owner: maintainer
business_value: low
effort: xs
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-170 — Decide whether the audit's upstream rows are reported to anyone

## 1. Specify

**Outcome**
A decision on what *handed over* means for the two upstream rows of the context-economy audit, U-01
and U-02 — either they are actually sent to whoever owns the harness, or being written in the
deliverable **is** the whole of the handover — and the disposition wording in
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 corrected to say
whichever it is.

**Why this one**
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) dispositions both rows as
*no task, and nothing implemented locally — they stay in the deliverable, which is the handover*. The
session of 2026-08-17 flagged that as a residual aimed at the maintainer: **it is a claim about where
the rows live, not about anyone having received them.** The audit's own scope says the reader should
be able to tell which costs belong to the harness, and a row nobody has sent is a cost still sitting
here. T-152 closed the same day, and **a question left inside a closed record leaves every view the
project has** — which is why it is a task rather than a sentence there.

**It may be a one-line close, and that is a fine outcome.** If the maintainer's position is that
publishing the observation is the handover this project intends, the decision is recorded, the wording
in T-152 §3 is corrected from *the handover* to what it actually is, and this closes. The cost of
raising it is one record; the cost of not raising it was losing it.

**Scope**
- In: the decision, and the correction to T-152 §3's disposition wording so the record says what was
  actually done
- In: naming the recipient, if the answer is that they are sent
- Out: re-opening the audit's findings or its bands. U-01 and U-02 are observations about the harness
  that assert no failure, and neither is a finding
- Out: writing anything into the two audit deliverables. They are a dated examination record, and
  correcting them would destroy what a dated record is for — the same reason
  [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) left the step-11 table alone

**Inputs**
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3 — the upstream
  disposition table and the residual flagged against it
- [`docs/audits/2026-08-15-context-economy-portable.md`](../docs/audits/2026-08-15-context-economy-portable.md) — where U-01 and U-02 are stated in full

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**Is there a recipient at all?** Both rows are about the harness, which this project does not
  own and has no channel to. If the answer is that no route exists, that is the decision and the
  wording changes to say so. **The maintainer answers, at `specify`.**~~ **Answered by the owner on
  2026-08-19: no route exists, so the wording changes** — see the Log row of that date.

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
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 2 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: there is no route, so the wording is what changes.** Asked in the backlog-wide round of 2026-08-19. §1 anticipated this outcome and called it a fine one: the decision is recorded, and [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) §3's disposition is corrected from *they stay in the deliverable, which is the handover* to what was actually done — an observation published, with no recipient and nothing sent. *Rejected: naming a recipient and delivering the two rows*, which would make the disposition literally true and commits this project to a reporting channel it has never used and would then have to keep. The correction lands in T-152 §3 and nowhere else; the two dated audit deliverables are not touched, for the reason §1 already gives. This row is the answer, not authorisation to start. |
| 2026-08-17 | → proposed | Raised at [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md)'s close, routing a residual that task's own log had flagged the same day as *live and would die silently at close*. **Soft edge, not a child**, and deliberately: a child would re-open the closure rule this task exists because of, and the residual is not a finding needing repair — it is a question about whether a disposition already taken describes what happened. `xs` and `low`, because the likeliest outcome is a recorded answer and a two-word correction. |
