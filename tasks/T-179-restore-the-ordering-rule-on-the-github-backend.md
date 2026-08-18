---
id: T-179
title: Restore the what-next ordering rule on the GitHub backend
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-022, T-108, T-178]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-179 — Restore the what-next ordering rule on the GitHub backend

## 1. Specify

**Outcome**
A procedure in the GitHub Issues binding that answers *what should I work on next* by the project's
own stated ordering rule, so a migrated project keeps the question rather than handing it back to a
person.

**Why this one**
**The binding currently records this as a loss and stops there**: `list --open --limit 1` answered
what to work on next "by a stated rule — blocked last, then effective value, then effort, then id",
and GitHub "sorts by number, recency or whatever a saved filter says. The question does not
disappear; it goes back to a person."

**But the rule is stated, and every input it needs is already in the binding's own `enumerate`
output.** That command returns labels, `blockedBy` and the body, and the body carries the property
block verbatim — so effective value, effort and blocked-ness are all there. Nothing is missing but
the sorting, which is why this is a document and not a feature.

**It matters more than it looks, because of what the ordering rule is for.** `docs/SCOPE.md` non-goal
11 records why the filtered listing was let in at all: not convenience, but token efficiency — an
agent that must read every task to find the next one has already spent what the tool exists to save.
A migrated project reading its whole issue list to choose is in exactly that position, and it is the
position §1 is written against.

**Scope**
- In: the ordering rule, restated as something an agent runs against `enumerate`'s output
- In: what the rule cannot reproduce here, stated rather than glossed
- Out: a command, a flag, or anything in the core. Non-goals 5 and 11
- Out: changing the ordering rule itself. It is the local backend's and this task carries it across
  unchanged; if it is wrong, that is a different task about
  [T-022](T-022-filtered-task-listing-for-scripts.md)

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Operations*, `enumerate`, and the
  *What is gone* item this task would make partly false
- [T-022](T-022-filtered-task-listing-for-scripts.md) — the ordering rule and why the listing exists
- `plugin/skills/taskmd/taskmd/cli.py` — `is_blocked` and the ordering it feeds, which is the
  authority on what the rule actually is

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**Is a restated rule a second home for it?** The rule lives in the tool's code and would now
  also be described in a binding, which is the duplication `CLAUDE.md`'s one design rule exists to
  stop. The counter is that a binding is a mapping document and describing the local behaviour is
  what every other operation in it already does. **The maintainer decides**, because it is a
  judgement about the rule this project is most careful with.~~ **Answered by the owner on
  2026-08-19: describe it in the binding** — see the Log row of that date, which also records the
  amendment to the design rule that came with the answer and left as
  [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md).

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
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 5 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: describe the rule in the binding.** Asked in the backlog-wide round of 2026-08-19. The reason is the one §1 already carried — a binding is a mapping document, and describing local behaviour is what every other operation in it already does. *Rejected: pointing at the code instead*, which is the strictest reading of the design rule and leaves whoever implements this backend reading Python to learn the one behaviour that decides what people work on. **The owner attached a second instruction, and it is not this task's to carry**: the design rule itself is to be amended to say that single source of truth is the *goal* — its purpose being to minimise inconsistency and unnecessary administration — and that a system configuration or a comparable limitation is grounds to deviate from it. That amendment lands in the rule's own home and changes every design decision in the project rather than this binding, so it is raised as [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) rather than widened into here. This task does not wait on it: the answer above stands on the binding's own precedent. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about what survives a migration. Of the three losses that document lists, this is the one whose inputs are all still present — the rule is stated and `enumerate` already returns everything it needs, so the loss is of the sorting and not of the information. `medium` rather than `high`: it costs a person a decision each time, where [T-178](T-178-give-the-github-binding-a-standing-verification.md) costs them data. **Not covered by any standing authorisation.** |
