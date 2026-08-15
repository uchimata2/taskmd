---
id: T-152
title: Audit — what this repository costs a session on every turn
type: audit
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-118, T-143]
work_package: M6
owner: maintainer
business_value: medium
effort: m
created: 2026-08-15
updated: 2026-08-15
deliverables: [docs/audits/2026-08-15-context-economy-portable.md, docs/audits/2026-08-15-context-economy-taskmd.md]
---

# T-152 — Audit: what this repository costs a session on every turn

## 1. Specify

**Outcome**
A set of findings about what a session pays here, each with a measured figure, a date, and a named
mechanism for changing it — plus, for every area examined where nothing was found, a record saying
so. A reader can conclude which costs this repository can reach, which belong to the person running
the agent, which belong to the harness, and what the difference between those three is worth. The
deliverable is the findings, not the repairs; the repairs are child tasks.

**Scope**
- **In:** everything a session pays without asking for it (the project's always-loaded conventions,
  the served skill descriptions, and — inventoried and marked — the personal instruction file, the
  auto-memory index, the output style and the capability catalogue); what one unit of work must read;
  what this project's commands print on a green run; what a unit of work writes; and the workflow
  decisions that change *when* a cost is paid.
- **Out:** security, compliance, licensing, quality and correctness. They are not searched for, and
  anything noticed anyway goes to the byproduct register and is never ranked. Also out: measuring the
  harness's own system prompt and tool schemas — they are on the load path and are inventoried as
  such, but they are not measurable from this machine and are therefore never banded.

**What counts as a finding**
A fact about this repository that changes what a session pays, stated as a measured figure with the
date it was taken, **and** with a mechanism for changing it that can be named. Three exclusions do
the work:

- A figure with no named mechanism is not a finding — it prices the wrong thing, because the size of
  a region is not the share of it that can be changed.
- An observation with no measurable figure is a byproduct-register row, never a finding.
- An area examined where nothing was found is **recorded as a result**, not omitted. Those rows are
  what separate *examined and clean* from *not examined*.

*The threshold above is the method's and was applied throughout the examination. This umbrella was
created after the examination ran, so it records the threshold rather than having set it — see the
log.*

**Inputs**
- [`docs/audits/2026-08-15-context-economy-taskmd.md`](../docs/audits/2026-08-15-context-economy-taskmd.md) — this project's report, ranked, with the upstream section and the byproduct register
- [`docs/audits/2026-08-15-context-economy-portable.md`](../docs/audits/2026-08-15-context-economy-portable.md) — the half any project can act on, and the technique catalogue with its search record
- [`plugin/skills/taskmd/docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) — the five steps this task follows

**Acceptance criteria**
- [ ] Every item named in scope has been examined, and the record says so even where nothing was found
- [ ] Each finding carries a severity and enough detail for someone who was not present
- [ ] Every finding either has a child task or a recorded reason for needing none, and no finding is
      fixed inside this task
- [ ] Every byproduct-register row is dispositioned — raised as its own task, or recorded as needing
      none — and the row points at the task where one was raised
- [ ] Phase 2 of the method exists as a task, blocked on the children this umbrella raises

**Open questions**
- Does this task run one phase per request, or the whole lifecycle in one — given the examination is
  already complete and its later phases are largely retroactive? — **the owner**
- Is `business_value: medium` right for an audit whose top finding is `L` on one surface and whose
  next four are enablers? — **the owner**
- How does a child task carry its finding id? The method wants a structured field a command can
  read; this project's shipped config states that adding a key is a breaking change for every
  adopter who wrote their own. The project's rule stands, so the question is what replaces the
  field. — **the owner, at plan**
- Is finding E-13 attempted at all, given it re-opens a decision T-118 recorded with a reason? The
  new evidence licenses re-opening, not reversing. — **the owner, at implement**

## 2. Plan

The audit **procedure** is designed here, for this audit — what will be looked at in what order, and
how each item will be examined. It is not the same from one audit to the next.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Findings**

| # | Finding | Severity | Child task | Status |
| :-- | :--- | :---: | :--- | :--- |
| F-1 |  | high / medium / low | T-NNN | open |

Findings needing no action stay in this table with the reason, and are the evidence that the area
was examined — worth as much as the ones that produced work.

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <the child tasks raised, and where the examination is recorded>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

**Closing**
This umbrella closes only when every finding is resolved — a `done` child, or dropped with the
reason recorded above. Closing over open children erases the link between the examination and its
consequences.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-15 | → proposed | Created. |
| 2026-08-15 | — | **The examination ran before this umbrella existed.** The owner asked for a report only, so the method's phase 1 was performed and written to the two documents in `deliverables`, and nothing was raised. Recorded here rather than smoothed over: `audit.md` step 2 says to state the finding threshold *before* looking, and this task records a threshold that was applied during the examination rather than set by this file. The consequence is that `plan` describes a procedure already carried out and `implement` records findings already written — which is the first open question above. |
| 2026-08-15 | — | `effort: m` prices the work that remains — recording the findings here and raising the children. The examination itself was larger and is already spent. |
