---
id: T-181
title: Verify the handoff GitHub recipe against a live issues-backed project
type: research
status: proposed
phase: specify
parent: T-005
blocked_by: []
related: [T-108]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-181 — Verify the handoff GitHub recipe against a live issues-backed project

## 1. Specify

**Outcome**
A recorded result of configuring the handoff skill against a taskmd project whose backend is GitHub
Issues, and resuming through it — or a statement of why that could not be done here, naming what
would show it.

**Why this one**
[T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) shipped
`plugin/skills/taskmd/docs/HANDOFF.md`, whose GitHub half was derived by **reading two binding
documents against each other**: taskmd stores enumerated fields as `<field>:<value>` labels, and
handoff's `github-issues` binding accepts a `label:<prefix>` form for `tracker_status`. The join is
exact on paper and has never been run. T-005's review carried the criterion rather than met it, which
is what raised this.

**This is the failure mode the method names.** A configuration that has only ever been reasoned about
is worth what the reasoning is worth, and the reasoning here spans two projects' documents — the
class of claim [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) exists because
nothing was checking. The local half of the same recipe *was* run, which is exactly why the
difference between the halves should not be papered over.

**Scope**
- In: the four keys the recipe names for this backend — `tracker`, `tracker_status`,
  `tracker_status_done`, `tracker_workflow` — exercised through at least one handoff operation that
  reads a work item, and one that writes a status.
- Out: any change to taskmd's own GitHub binding. If this finds one needed, that is a separate task.

**Inputs**
- `plugin/skills/taskmd/docs/HANDOFF.md` — the recipe under test
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — taskmd's own backend binding
- The handoff skill's `bindings/github-issues.md` — the other half of the derivation

**Acceptance criteria**
- [ ] The result is stated as what the commands printed, not as a verdict
- [ ] Both directions are exercised: handoff **reads** an item, and handoff **writes** a status
- [ ] Where it works, the recipe's GitHub section says so and names what was run; where it does not,
      the recipe states the limitation instead of the configuration
- [ ] If no live issues-backed project is reachable, that is recorded as the result, naming what
      would show it — an honest gap, not an implied assurance

**Open questions**
- ~~**Is a taskmd project on the GitHub backend reachable to test at all?** Nobody has been observed
  running one; `control/LOCAL-CONTEXT.md` carries the adopter roster and is where the answer would
  come from. **This is the question that decides whether the task can run unattended**, so it is the
  owner's — the same property that keeps T-175, T-176 and T-178 outside the standing grant.~~
  **Answered on 2026-08-19: yes — one is reachable, and it was checked rather than assumed.** The
  Log row of that date names the venue, the evidence, and why the second candidate was rejected.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-19 | (no change) | **The open question is answered, and the answer falsifies the premise §1 was written on.** Asked in the backlog-wide round of 2026-08-19; the owner named two candidates rather than accepting the *unreachable* result, and both were checked before answering. **A live issues-backed taskmd project is reachable: the context-audit sibling**, labelled in `control/LOCAL-CONTEXT.md`. Its `.taskmd/config.md` declares the GitHub Issues binding with `id_prefix: '#'` and `id_width: none`, and its open issues carry `status:proposed`, `phase:specify`, `type:*`, `business_value:*` and `effort:*` as labels — which is taskmd's `<field>:<value>` convention, the exact join the recipe's GitHub half was derived from and which §1 says has never been run. So the *unreachable* branch of criterion 4 is closed as a possibility, not as a result. **The other candidate was rejected on its own written evidence**: the handoff skill's own repository carries a `.taskmd/config.md` too, and that file states plainly that the taskmd CLI does not run on the project and that its operations are `gh` instructions followed by an agent; its status labels also take a different form. It is a project configured *for* the binding rather than one running it, so a pass there would not exercise the join. *Rejected: recording the task as unreachable*, which §1's criterion 4 allows and which the check above shows would have been false. `specify` still confirms the venue on the day rather than trusting this row — the configs there are local and uncommitted, and that project has an open issue about whether they stay that way. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md)'s review, which carried its either-backend criterion rather than meeting it. The local half of that recipe was verified by use — the session that wrote it resumed through the configuration it documents — and the GitHub half was not, so shipping both under one heading would have made them look equally tested. **Outside the standing grant of 2026-08-18**, on both counts: it is a task T-005 raised, and its open question is the owner's. |
