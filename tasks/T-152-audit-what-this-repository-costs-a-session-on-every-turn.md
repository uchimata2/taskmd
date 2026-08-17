---
id: T-152
title: Audit — what this repository costs a session on every turn
type: audit
status: in_progress
phase: review
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

All four were answered by the maintainer on 2026-08-15, in the session that created this task. The
answers are kept here rather than only in the log, because each one is a condition on how a later
phase runs and a log row is read once.

- **Answered — one request, not four.** This task runs its whole lifecycle in one request, because
  the examination is already complete and its later phases are retroactive. **The authorisation
  covers this task only and no other**, and it is recorded in the log below with who gave it.
- **Answered — `business_value: medium` stands.**
- **Answered — the finding id goes in the child task's title, with `parent` pointing here.** No
  config key. The method asks for a structured field a command can read; this project's shipped
  config states that adding a key breaks every adopter who wrote their own, and the project's rule
  wins that collision. A title prefix is matchable without a schema change.
- **Answered — E-13 is tested, not carried.** Its remedy re-opens a decision
  [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) recorded with a reason, and the
  new evidence licenses re-opening rather than reversing. Take E-10 first: it saves less and cannot
  fail. E-13 becomes a `decision` task that measures and reports; it does not carry the change.

## 2. Plan

The audit **procedure** is designed here, for this audit — what will be looked at in what order, and
how each item will be examined. It is not the same from one audit to the next.

*Written after the fact, from the two deliverables — the examination ran before this umbrella existed,
which the log records and this table does not repeat. Every row names an output that exists.*

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish the load path **by observation** — what a session is handed before its first tool call — never from a file's claim about when it loads | The load-path table: every item with a size, a controller and a date, including the ones that cannot be changed |
| 2 | Measure the read path on **one representative unit of work, chosen before looking** | E-16's measured path — skill, method, phase file, binding, `context`, task file |
| 3 | Partition every measured document and the whole task corpus so the parts sum, and print the residual rather than hide it | E-17's section partition of 151 files; residual +756 on 2,430,672 |
| 4 | Capture what a green run prints, to files, measuring the lengths without printing them | E-19's table of nine commands |
| 5 | Screen every candidate against the five families, and record **a family with no finding as a result** | The families table; E-14, E-15, E-18 and the surface-D row |
| 6 | Search three axes — ideas, named tools, the harness's own documented mechanisms — to an empty round, and record the empty round | The search record and the 46-technique catalogue, each row adopted, rejected or deferred |
| 7 | Band each finding on gain, effort and risk, **with risk as a veto rather than a term** | The ranked list |
| 8 | Separate what this project controls from what the user or the harness controls, and hand the second over without implementing it | The upstream section — U-01 and U-02 |
| 9 | Record everything noticed but not searched for, never ranked | The byproduct register, B-1 to B-7 |
| 10 | Write the portable half as a document that stands alone, sharing one numbering space with the project's own and stating each finding in exactly one of them | The two deliverables |
| 11 | Propose child work for the owner's review, and **raise nothing** | The step-11 table — and this task's `implement`, which is where it was raised |

## 3. Implement

**Findings**

Each id is stated in full in one of the two deliverables and is **not** restated here; this table is
the disposition. `—` in the severity column is a row that is a result rather than a finding, and those
rows are the evidence that the area was examined.

*The last column is the **disposition**, never the child's status — that is stored once, in the child,
and `taskmd context T-152` derives it. A status column here would be a second home and would be wrong
by the end of the week it was written.*

| # | One line | Severity | Child task | Disposition |
| :-- | :--- | :---: | :--- | :--- |
| [E-01](../docs/audits/2026-08-15-context-economy-portable.md#e-01) | A passing budget covers a minority of the observed load path | medium | [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) | raised |
| [E-02](../docs/audits/2026-08-15-context-economy-portable.md#e-02) | The capability catalogue is the largest load-path item; 1.3% of it is ours | low | none | **Controller is the user.** Not available at project scope, and no clone inherits the setting. The levers are named in the finding. |
| [E-03](../docs/audits/2026-08-15-context-economy-portable.md#e-03) | The portable statement of E-13 | medium | [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) | raised |
| [E-04](../docs/audits/2026-08-15-context-economy-portable.md#e-04) | Instruction count binds and a character budget cannot see it | low | [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) | folded in; see the decisions below |
| [E-05](../docs/audits/2026-08-15-context-economy-portable.md#e-05) | The portable statement of E-12 | medium | [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) | raised |
| E-06 | — | — | none | **No such id in either deliverable.** See the decisions below; this task cannot close it. |
| [E-07](../docs/audits/2026-08-15-context-economy-portable.md#e-07) | Output caps: measured not to fire here | — | none | Result. The zero is measured, and the technique is recorded for a project whose output is large. |
| [E-08](../docs/audits/2026-08-15-context-economy-portable.md#e-08) | Screen a figure on its source and on where the effect concentrates | low | none | A rule for the audit **method**, which is another repository's. Carried in the portable deliverable, which is the handover. |
| [E-09](../docs/audits/2026-08-15-context-economy-portable.md#e-09) | `@path` imports load at launch; a split is not a deferral | low | none | Already satisfied here: this project's tier 1 was established by observation (T-050), not by a file's claim. |
| [E-10](../docs/audits/2026-08-15-context-economy-portable.md#e-10) | Block comments are stripped before injection | low | [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) | **taken first**, on the maintainer's ruling |
| [E-11](../docs/audits/2026-08-15-context-economy-portable.md#e-11) | A general-purpose subagent pays the instruction file again | low | none | Controller is the person running the agent. This repository has no mechanism that binds a subagent choice, and a tier-1 line asking for one would fail its own membership rule. |
| [E-12](../docs/audits/2026-08-15-context-economy-taskmd.md#e-12) | Tier 1 names a 36,393-char index; a command answers in 95 | medium | [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) | **already asked**. Nothing raised; the measurement was written into T-143 instead. |
| [E-13](../docs/audits/2026-08-15-context-economy-taskmd.md#e-13) | 36.3% of tier 1 is prose about tier 1 | medium | [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) | **tested, not carried** |
| [E-14](../docs/audits/2026-08-15-context-economy-taskmd.md#e-14) | The budget's comparison set is closed | — | none | Result: the family's remedy is already implemented and shown to fail on a tree it should catch. |
| [E-15](../docs/audits/2026-08-15-context-economy-taskmd.md#e-15) | Spine plus one branch: 13,905 characters present and not paid | — | none | Result. |
| [E-16](../docs/audits/2026-08-15-context-economy-taskmd.md#e-16) | The binding is 49.4% of the non-task read path | medium | [T-156](T-156-e-16-decide-whether-a-read-only-phase-can-skip-the-binding.md) | raised |
| [E-17](../docs/audits/2026-08-15-context-economy-taskmd.md#e-17) | `Log` is 16.6% of the task corpus | — | none | **Rejected at the threshold**, in the deliverable, with the reason: nothing can be named that the prose would stop deciding. |
| [E-18](../docs/audits/2026-08-15-context-economy-taskmd.md#e-18) | 858 bytes of payload per byte of tier-1 description | — | none | Result: progressive disclosure doing what it is for. |
| [E-19](../docs/audits/2026-08-15-context-economy-taskmd.md#e-19) | A whole unit of work prints ~2,400 characters on a green run | — | none | Result, and the measurement that rejects E-07 here. |
| [surface D](../docs/audits/2026-08-15-context-economy-taskmd.md#surface-d) | 36,633 lines written across 151 tasks, mean 242 | — | none | Result: the read half is already governed by `context` returning a pointer. |
| F2 | Redundancy and contradiction | — | none | No finding. The one candidate has a declared single home and the governing document says which and why. |
| F4 | Model work that should be deterministic | — | — | One instance only, E-12. The validator, index and listing are programs already. |
| F5 | Tool and workflow economics | — | — | Nothing on surface C (E-19). One item on A/E, E-11, and it is not this project's alone. |

**Byproduct register — disposition**

Never ranked and never a finding. The maintainer agreed the disposition of the rows this project owns
in advance; the two rows below that they did not name are dispositioned here with the reason.

| Row | Disposition |
| :--- | :--- |
| B-1 | **No task**, per the maintainer. The workflow's own header already records that a green run proves Linux only. |
| B-2 | **[T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md)**, per the maintainer. |
| B-3 | **No task**, per the maintainer. |
| B-4 | **No task.** The `.pyc` files have no context cost, are not in `git ls-files`, and the install route that copies them is already recorded in [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) and [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md). Not named in the agreed disposition; decided here. |
| B-5, B-6, B-7 | **No task.** Owned by the person running the agent, not by this repository or its upstream. The register says so and is their home. |

**Upstream — disposition**

| Row | Disposition |
| :--- | :--- |
| U-01, U-02 | **No task, and nothing implemented locally.** Both are observations about the harness, written to be handed over; neither asserts that a component failed. They stay in the deliverable, which is the handover. |

**Decisions & assumptions**

- **E-01 and E-04 are one task, not two** — 2026-08-15. Both edit the same sentence about what the
  budget does and does not govern, so two tasks would each rewrite the other's output. *Rejected:* two
  tasks, which the step-11 table implies by listing them separately; it also warns that specifying the
  tier-1 questions independently produces inconsistent answers, which is the same argument.
- **E-01 and E-13 are two tasks, not one** — 2026-08-15, and this is the opposite call to the one
  above, made for the reason the maintainer's ruling supplies. The step-11 table proposed one task for
  both. The ruling then made them different kinds of work: E-01 edits a rule, E-13 measures and
  reports and changes nothing. One task holding both would close on half a report. The shared policy
  question is carried by a **dependency** instead —
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) is `blocked_by`
  [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) — so neither is specified
  independently, which is what the warning asked for. *Rejected:* one combined task.
- **[T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) is not edited** — 2026-08-15.
  Its premise now has evidence against it, and the temptation is to annotate the closed record so a
  reader learns that. The soft edge on
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) already carries it:
  the forward edge is stored once and the inverse is derived, so `context T-118` shows the task that
  re-opens its question. Writing it into T-118 as well would be the second copy the design rule
  forbids. *Rejected:* a log row in T-118.
- **E-06 does not exist in either deliverable** — 2026-08-15, found while writing the table above. The
  numbering space runs E-01 to E-20 with E-06 absent, and the ranked list claims to name every id
  wherever it is stated. Either a finding was dropped while the reports were written, or the numbering
  skipped. **This task cannot tell which**, because the examination is finished and the gap is in its
  own record. Recorded rather than repaired, and rather than a child task for a number: no finding is
  known to be missing, only an id. **Answered the same day — the maintainer ruled it a numbering
  skip**, so nothing is missing from the examination and the gap is left as it is. Nothing in either
  deliverable refers to E-06, which is the evidence consistent with that ruling.
- **Severity is assigned here and was not in the deliverables** — 2026-08-15. The reports band on gain,
  effort and risk; the umbrella's acceptance criteria ask for a severity. `medium` is a finding whose
  remedy changes what a session pays; `low` is one that is real and either cheap or not ours; `—` is a
  result. Assumption, and cheap to overrule.
- **`business_value` and `effort` on the six children are estimates** — 2026-08-15, set from each
  finding's own gain and effort fields rather than judged afresh.

**Outputs produced**

- Six child tasks: [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md),
  [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md),
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md),
  [T-156](T-156-e-16-decide-whether-a-read-only-phase-can-skip-the-binding.md),
  [T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md),
  [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md).
- The E-12 measurement written into
  [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), where the question already
  lives — no task raised for it.
- The examination itself is the two paths in `deliverables`, produced before this umbrella existed.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every item named in scope has been examined, and the record says so even where nothing was found | met | Six rows in the findings table are results rather than findings, and three more are families screened clean. The load-path table marks the items that cannot be measured from here rather than omitting them. **One exception, raised and then closed the same day:** the id E-06 exists in neither deliverable, and the maintainer ruled it a numbering skip — see the decisions above. |
| Each finding carries a severity and enough detail for someone who was not present | met | Severity is in the findings table. The detail is the eleven fields each finding carries in the deliverable, which is where it is stated in full and where it is not restated. |
| Every finding either has a child task or a recorded reason for needing none, and no finding is fixed inside this task | met | Every row of the findings table names a task or a reason. Nothing was repaired here: the only edit outside this task added a measurement to [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), which is the task that already asks E-12's question. |
| Every byproduct-register row is dispositioned, and the row points at the task where one was raised | met | All seven rows. B-4 was not in the maintainer's agreed disposition and is decided above with its reason. |
| Phase 2 of the method exists as a task, blocked on the children this umbrella raises | met | [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md), `blocked_by` all four repair children **and** [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md), which carries E-12's band. |

**Child fix tasks raised**
- [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) — E-10, taken first
- [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) — E-01 and E-04
- [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) — E-13, blocked by T-154
- [T-156](T-156-e-16-decide-whether-a-read-only-phase-can-skip-the-binding.md) — E-16
- [T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md) — byproduct row B-2
- [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) — phase 2, blocked on the rest

**Closing**
This umbrella closes only when every finding is resolved — a `done` child, or dropped with the
reason recorded above. Closing over open children erases the link between the examination and its
consequences.

**Where that stands, 2026-08-17.** Four of six children are `done`:
[T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md),
[T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md),
[T-156](T-156-e-16-decide-whether-a-read-only-phase-can-skip-the-binding.md) and
[T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md). **The set is not listed here and
must not be** — `taskmd context T-152` derives it from each child's own status, which is the one home,
and a roster in this file would be wrong within the week. What is recorded is only what the derived
view cannot say: **the shape of what remains.**

Two children are open, and they are in series rather than in parallel.
[T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) is at `implement` and
unblocked. [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) is phase 2 of the method
and cannot start until [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)
and [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) close — its other three
blockers already have. So closing this umbrella is **three tasks of work in a fixed order**, not one,
and the order is a property of the edges rather than a preference.

**The five criteria were re-read against the tree on 2026-08-17 and all five still hold.** None of
them depends on how many children have closed: four are about what this record contains, and the
fifth asks that phase 2 *exist as a task blocked on the children*, which is still true and is the
criterion that deliberately does not enumerate them.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | — | **Closure was asked for and is not available; nothing was changed to make it available.** The maintainer asked to close this out, whole lifecycle. **There is no lifecycle left** — all four phases ran on 2026-08-15 under the authorisation below, and §4 judged all five criteria met that day; re-read on 2026-08-17, all five still hold. What holds this open is `audit.md` step 5 alone, and §4 *Closing* now records the shape of what remains: two children in series, three tasks of work, the order fixed by the edges. **Recorded rather than resolved**, because the two ways to resolve it are both the maintainer's: authorise the chain, or drop [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) with a reason, which step 5 permits and which would leave only [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md). Closing over open children was not considered: it is the one thing this task's own criteria and the method both forbid, and doing it on request would make every future umbrella's closing rule advisory. **Two residuals aimed at the maintainer are still live and would die silently at close** — the severity scale in `implement` is flagged there as an assumption *cheap to overrule*, and U-01/U-02 are dispositioned as handed over *by being in the deliverable*, which is a claim about where they live rather than about anyone having received them. |
| 2026-08-15 | → proposed | Created. |
| 2026-08-15 | — | **The examination ran before this umbrella existed.** The owner asked for a report only, so the method's phase 1 was performed and written to the two documents in `deliverables`, and nothing was raised. Recorded here rather than smoothed over: `audit.md` step 2 says to state the finding threshold *before* looking, and this task records a threshold that was applied during the examination rather than set by this file. The consequence is that `plan` describes a procedure already carried out and `implement` records findings already written — which is the first open question above. |
| 2026-08-15 | — | `effort: m` prices the work that remains — recording the findings here and raising the children. The examination itself was larger and is already spent. |
| 2026-08-15 | — | **The maintainer authorised the whole lifecycle in one request, for this task only.** Given in the session that created the task, in answer to the first open question above. It covers `specify` → `plan` → `implement` → `review` on T-152 and **nothing else** — every child task this umbrella raises takes one phase per request unless separately authorised. Recorded here because an authorisation kept anywhere else is one a later session can miss or stretch to a task it never reached (METHOD §3.1). |
| 2026-08-15 | — | The maintainer answered the remaining three open questions in the same turn: `business_value` stands at `medium`; a child task carries its finding id in its **title**, with `parent` pointing here, and **no key is added to the config**; and E-13 is **tested, not carried**, with E-10 taken first. The third answer resolves a collision between the audit method and this project's own policy in the project's favour, which is what the method asks for when the two disagree. |
| 2026-08-15 | → in_progress | Whole lifecycle run in one request, under the authorisation recorded above. `plan` records the procedure the examination followed, written from the deliverables; `implement` dispositions every finding, every register row and both upstream rows, and raises six children; `review` judges the five criteria. **The task does not close** — `audit.md` step 5 says an umbrella closes only when every child is resolved, and six are open. |
| 2026-08-15 | — | **E-06 is in neither deliverable.** Found while dispositioning: the numbering space runs E-01 to E-20 and E-06 is absent, though the ranked list claims to name every id wherever it is stated. Recorded in `implement` as a residual for the maintainer rather than repaired or turned into a task, because nothing tells this session whether a finding was dropped or the numbering skipped. |
| 2026-08-15 | — | **The maintainer answered E-06 the same day: a numbering skip.** No finding is missing and the deliverables are left as they are. Answered in the session that ran the lifecycle, in reply to the residual raised above — recorded here so a later reader does not re-open a question that has been settled. |
| 2026-08-15 | — | Byproduct-register disposition agreed in advance: of the rows this project owns, **B-2 becomes its own task** at review and B-1 and B-3 are recorded as needing none. Register row **B-6 was corrected** on the same day — it read a stub-and-core pair at user scope as a stale duplicate, and the correction stands in the register rather than replacing the row. |
