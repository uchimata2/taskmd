---
id: T-129
title: Release v0.5
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-125, T-085, T-126, T-127]
work_package: v0.5
owner: maintainer
business_value: high
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-129 — Release v0.5

## 1. Specify

**Outcome**
The v0.5 work is published as `0.5.0`: the manifest names it, the gates pass, the tag is annotated,
and the GitHub release says what changed.

**Why this one**
`v0.2` had no release task until the moment it shipped, and
[T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md) was raised at that moment because METHOD
rule 1 applies to a release like anything else. Raising it up front is the same rule applied earlier.

**It is not the last task in this release, and that is deliberate.** The maintainer's instruction on
2026-08-11 is that [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md)
comes last, after v0.5 is out, so what gets installed on a clean machine is the thing that just
shipped rather than the one before it. So **v0.5 is not complete when it is tagged.** It is complete
when the published artifact has been proven from outside.

That is a change from `v0.2`, where the release was the final act and nothing checked the result.
`0.4.0` is published today and nobody has installed it anywhere.

**Requirements served**
R-21 and R-22 (`docs/SCOPE.md`), the publishing constraints.

**Scope**
- In: the manifest version; both publication gates; the annotated tag; the GitHub release.
- Out: [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md), which
  runs *after* this and is its own task.
- Out: which tasks are in v0.5. That is `work_package`, read with the tool. **Do not list them
  here and do not put them in `blocked_by`** — an enumerated membership is the defect
  [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) removed from the exit criteria,
  and a dependency list would rebuild it in the graph.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §2, §5 and §6.
- [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md) §2 and §3, which is the worked procedure
  and the record of what went wrong last time.

**Acceptance criteria**
- [ ] Every v0.5 task except T-085 is closed when this starts, read with
      `list --work_package v0.5 --open` rather than from a list
- [ ] Both gates pass on the tree being tagged, and the dash gate is read by its **count** and its
      exit code, where exit 1 is the clean outcome
- [ ] The manifest names a version above `0.4.0`, and the bump is minor or patch with the reason
      stated
- [ ] The tag is annotated and the GitHub release exists
- [ ] `check`, `index` and the full suite pass on the tagged commit

**Open questions**
- **Minor or patch?** It depends on what v0.5 turns out to contain, and
  [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) is the one to watch:
  a new test that fails on an adopter's tree is the case the minor rule exists for. Decide at
  `plan`, from the closed set rather than from this sentence.

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
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised during a handoff, from the maintainer's instruction that T-085 is v0.5's last item and runs once v0.5 is released. That instruction needs something to depend on, and a dependency edge needs a task: this is it. **The ordering is the point, not the paperwork.** `0.4.0` shipped with nothing verifying it from outside, and T-085 pointed at whichever version happened to be current when someone got to it. Now it points at this one. Its `blocked_by` carries the edge; nothing here lists what v0.5 contains. |
