---
id: T-156
title: E-16 — Decide whether a read-only phase can skip the binding
type: decision
status: proposed
phase: specify
parent: T-152
blocked_by: []
related: []
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-156 — E-16: decide whether a read-only phase can skip the binding

## 1. Specify

**Outcome**
Either `SKILL.md`'s scoping of the binding becomes load-bearing — a phase that only reads does not load
it — or the reason it stays unconditional is recorded where the next person looking at the read path
will find it.

**Why this one**
Finding [E-16](../docs/audits/2026-08-15-context-economy-taskmd.md#e-16) of
[T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), stated there: on a measured
unit of work the binding was the largest item on the read path apart from the task file itself, and
`SKILL.md` already scopes it to *before creating or changing any task* without that scoping doing
anything.

**The finding stands regardless of the remedy's fate.** The measurement is a fact about the read path;
the change is a hypothesis with a named risk, and deciding against it is a legitimate outcome of this
task rather than a failure of it.

**Scope**
- In: `SKILL.md`'s load table and the sentence scoping the binding.
- In: which phases read only, and what a session does when one of them turns out to write after all —
  the risk the finding names, that a rule firing mid-phase is the kind that gets missed.
- In: what share of phases only read. A remedy that fires rarely is worth less than its size suggests.
- Out: cutting the binding's content. The finding is about **when** it loads, not how long it is.
- Out: the second binding. Only one is ever loaded, which the audit records as already working.

**Inputs**
- [E-16](../docs/audits/2026-08-15-context-economy-taskmd.md#e-16) — the measured read path and the risk
- `plugin/skills/taskmd/SKILL.md` — the load table
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the document in question, and its
  *After any write* step, which is what a read-only phase would not need

**Acceptance criteria**
- [ ] The decision names which phases are read-only, and what a session does when one is not
- [ ] The read path is re-measured at decision time on a named unit of work, not carried from the audit
- [ ] If the scoping is made load-bearing, the instruction to load the binding late is stated in one
      place, not repeated per phase
- [ ] Whatever is decided, the finding is recorded as standing
- [ ] The measured outcome is written into this record on the day it is known, not reconstructed later

**Open questions**
- **Is the expected saving worth the mid-phase rule?** Most phases write, so the gain is `M` in
  expectation against `L` on the occasions it fires. Whether to measure the share of read-only phases
  before deciding, or to decide on the risk alone, is the first thing to settle. **The maintainer
  answers, at `specify`.**

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
| 2026-08-15 | → proposed | Raised from [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md), finding E-16. `decision` because the finding's own risk field says the change may not be worth making, so the work is the judgement and not the edit. `s`, `medium`: independent of the other children and takeable in any order. |
