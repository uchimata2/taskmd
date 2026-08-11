---
id: T-129
title: Release v0.5
type: deliverable
status: planned
phase: plan
parent: null
blocked_by: []
related: [T-125, T-085, T-126, T-127, T-133]
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
- ~~**Minor or patch?**~~ **Decided at `plan`, 2026-08-11: minor, `0.5.0`.** From the closed set read
  with the tool, not from a guess. Two of the closed tasks change what an adopter sees:
  [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) adds a new
  `DUPLICATE INDEX` line to `check`'s output, which is a new capability and a new line for anyone
  parsing it, and [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md) changes
  the bytes every command prints on Windows. Either alone is more than a patch.
  [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) turned out **not** to
  be the one to watch: its test reads this repository's own documents and an adopter never runs it,
  so the case the §1 sentence anticipated did not arise. *Rejected: patch* — it would say nothing
  changed for the adopter, and `check` printing a line it has never printed is exactly something
  changing for the adopter.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the open v0.5 set with `list --work_package v0.5 --open` and confirm only T-085 remains | Criterion 1, or a stop |
| 2 | Bump the manifest to `0.5.0`, in the one place that holds it | `.claude-plugin/plugin.json` (per T-072, one home) |
| 3 | Run the dash gate, reading its **count** and its exit code, where exit 1 is clean | Recorded output |
| 4 | Run the pre-publish leak check, both directions — with the fixture excluded and without | Recorded output |
| 5 | `check`, `index` and the full suite on the commit about to be tagged | Recorded output |
| 6 | Annotate the tag, and write the release notes to the rule [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md) settled — **covered text, checked by eye** | The tag |
| 7 | Push, and create the GitHub release | The published release |
| 8 | Re-read the release **body** after publishing, not the tag message | A figure, and criterion 4 |

**Step 8 is new and it is not ceremony.** [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md)
measured that a tag message and a GitHub release body are **different texts** — `v0.2.0`'s are 936
and 2591 characters — and that the body is the one nobody had checked. Checking the tag and calling
the release verified is the mistake that produced
[T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md).

**Steps 7 and 8 need the maintainer.** Pushing and creating a public release are outward-facing acts,
and the standing waiver of METHOD §3.1 grants *phases*, not the right to publish. It is recorded here
so a later session does not read the plan as the authorization.

## 3. Implement

_Not started — and blocked on two things, neither of which is a phase._

**Criterion 1 is not met.** Read with the tool on 2026-08-11, after the rest of v0.5 closed:

```text
T-129   proposed   v0.5   specify   Release v0.5
T-133   proposed   v0.5   specify   Decide what to do about a published release note that breaks the rule
T-085   proposed   v0.5   specify   Install the published plugin ...                          blocked
```

[T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) is open and
its one question is the maintainer's, because both answers concern a page that is already published.
The criterion says *every v0.5 task except T-085*, and it says it as a **precondition**, so this does
not start.

**And steps 7 and 8 would need permission regardless.** Even with T-133 closed, tagging, pushing and
creating a release are not covered by a waiver about phases.

**Decisions & assumptions**
- **Not started rather than started-and-parked.** Bumping the manifest before the precondition holds
  would leave the tree claiming a version that was never released if the answer to T-133 changes what
  ships. — 2026-08-11

**Outputs produced**
- None yet.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → planned | Eight steps, and the plan **stops there deliberately**. Criterion 1 is a precondition and it is not met: [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) is an open v0.5 task whose single question is the maintainer's, because both answers concern an already-published page. Steps 7 and 8 would need permission in any case — the standing waiver grants *phases*, not the right to tag, push or publish, and that distinction is written into the plan so a later session does not read the plan as the authorization. The open question is answered from the closed set rather than deferred: **minor, `0.5.0`**, because [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) adds a line `check` has never printed and [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md) changes the bytes every command prints on Windows. §1 expected [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) to be the deciding one; it is not, since its test reads this repository's own documents and an adopter never runs it. Step 8 is added to the worked procedure T-125 left: the release **body** is re-read after publishing, because T-127 measured that it is a different text from the tag message and is the one nobody had checked. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised during a handoff, from the maintainer's instruction that T-085 is v0.5's last item and runs once v0.5 is released. That instruction needs something to depend on, and a dependency edge needs a task: this is it. **The ordering is the point, not the paperwork.** `0.4.0` shipped with nothing verifying it from outside, and T-085 pointed at whichever version happened to be current when someone got to it. Now it points at this one. Its `blocked_by` carries the edge; nothing here lists what v0.5 contains. |
