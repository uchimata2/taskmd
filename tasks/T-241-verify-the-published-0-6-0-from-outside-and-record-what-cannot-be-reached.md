---
id: T-241
title: Verify the published 0.6.0 from outside, and record what cannot be reached
type: audit
status: proposed
phase: specify
parent: null
blocked_by: [T-231]
related: [T-085, T-231]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-241 — Verify the published 0.6.0 from outside, and record what cannot be reached

## 1. Specify

**Outcome**

The `0.6.0` artifact is checked from outside this working tree — installed the way an adopter
installs it, and exercised — with every part that **cannot** be reached from any machine here named
rather than left as an implied pass.

**Where this came from**

The owner answered [T-231](T-231-cut-the-next-release.md)'s first question **yes** on 2026-08-23: a
verification-from-outside task follows the release.
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) is why. `0.5.0`
had such a task and `0.4.0` did not, and the difference is the whole of what T-085 records — a
release verified only by the tree that produced it has been verified by the one party that cannot
see its own gaps.

**And T-085's other half is the reason this record exists rather than a checklist.** It found that
**half of that verification was unreachable from any machine here**, and closed with half proven and
half not. Repeating the reachable half is cheap; the value of this task is that it says, again and
in the open, which half was not — because an audit that quietly drops what it could not do reads
exactly like one that found nothing wrong.

**Scope**

- In: installing the published `0.6.0` as an adopter does, from the published artifact rather than
  from this tree, and exercising what an install is supposed to give them
- In: naming every part that cannot be reached from any machine available, with the reason — T-085's
  unreachable half re-checked rather than assumed still unreachable
- In: whether anything shipped in `0.6.0` that should not have — the pre-release audit document, the
  new `check --classes` flag, the two repaired bindings and the reader protocol all went in on
  2026-08-23
- Out: the release itself, which is [T-231](T-231-cut-the-next-release.md)
- Out: the release note, which is
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)
- Out: repairing anything found. A finding here is its own task — this is an audit and
  [`audit`](../plugin/skills/taskmd/docs/method/audit.md)'s no-inline-fix rule applies

**Inputs**

- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — what was
  proven for `0.5.0`, what could not be, and why
- [T-231](T-231-cut-the-next-release.md) — the release this verifies, and the three answers that
  shaped it
- the published `0.6.0` artifact, once it exists

**Acceptance criteria**

- [ ] The plugin is installed from the **published** artifact, not from this working tree, and the
      route used is stated
- [ ] What an adopter gets is exercised rather than inspected — at least one command run and one
      skill reached from the install
- [ ] Every part that could not be reached is **named**, with the reason, and T-085's unreachable
      half is re-checked rather than carried forward as still-unreachable
- [ ] Anything shipped that should not have been is named; if nothing, that is stated as a checked
      result rather than left silent
- [ ] Every finding becomes its own task; none is repaired here

**Open questions**
- **None.** The shape is T-085's and the owner has already said this follows the release.

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
| 2026-08-23 | → proposed | Raised on the **project owner's** answer of 2026-08-23 to [T-231](T-231-cut-the-next-release.md)'s first question. **Raised now rather than at tag time**, and that is the point of raising it at all: an answer recorded only inside a struck-through question is invisible to every view, which is the defect [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) recorded when its own wait lived in a Log row. `blocked_by` names T-231, so the ordering rule reports this held until the release exists rather than a session having to remember a sentence. **`audit` by type and by the rule that follows from it**: its findings become their own tasks and none is repaired here. **Not part of the unattended grant** — that grant excluded the release and anything scheduled after it, and this is scheduled after it. Whoever picks it up is acting on the owner's answer above, not on that grant. **The half T-085 could not reach is in scope as a re-check, not as an inherited excuse**: unreachable in August is a fact about the machines of that week, and carrying it forward untested is how an audit comes to report what its author already expected. |
