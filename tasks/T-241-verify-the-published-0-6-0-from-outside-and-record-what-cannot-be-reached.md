---
id: T-241
title: Verify the published 0.6.0 from outside, and record what cannot be reached
type: audit
status: planned
phase: plan
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

**What counts as a finding, stated before looking** — [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
step 2, and the reason it is here rather than in §1 is that the threshold is part of how *this*
subject is examined:

- a statement an adopter would act on that the installed `0.6.0` contradicts;
- a file the install carries that should not ship, or lacks that the project promises;
- a documented route that does not run when followed as written.

**Not a finding:** prose that could be worded better; a gap already carried by an open task; a
difference between the install and this working tree that is explained by commits made after the
tag. The third exclusion is the one that will do work — the tree is 23 commits ahead of `v0.6.0`,
so *the install is missing something the tree has* is the expected state and not a defect.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what the published artifact **is** — tag, release, and whether it carries built assets or is source-only — and prove the installed copy on this machine came from **there** rather than from this tree. A cache directory named for a version is a claim, not provenance. | A stated route and the evidence that the install is not this tree |
| 2 | Inventory the install against `plugin/` **at the tag**, not at `HEAD`, since the tree has moved. Anything in the install and not at the tag, or the reverse, is examined. | A file-level comparison, and the answer to criterion 4 either way |
| 3 | Exercise it: run a command **from the install** and reach a skill **from the install**. Neither may resolve back into this working tree — check what the command actually loads, not only that it exits 0. | Captured output, plus proof of which copy answered |
| 4 | Re-check T-085's unreachable half rather than inherit it: is `claude plugin marketplace add` / `claude plugin install` runnable from any machine available now? Answer it by trying, and record what stops it if anything does. | A dated answer, with the command and its result |
| 5 | Check the four things `0.6.0` newly shipped are in the install: the pre-release audit document, `check --classes`, the two repaired bindings, and the reader protocol. | Present or absent, per item |
| 6 | Record every finding in this record with a severity, including the ones needing no action, and raise a child task per finding that needs one. Nothing is repaired here. | The findings table, and the child tasks |

**Decisions taken here**

- **The subject is the install, not a fresh never-seen-it machine** — 2026-08-23. §1's criteria ask
  for *the published artifact rather than this tree*, which is a different and weaker condition than
  T-085's *a machine that has never held any of this*. Conflating them is what would make this record
  unrunnable for the same reason T-085 was. *Rejected: waiting for a clean machine*, which
  [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) already recorded
  as a decision whose premise had weakened, and which is that record's to revisit and not this one's.

- **Step 1 proves provenance rather than assuming it** — 2026-08-23. A directory called `0.6.0` under
  a cache is a name somebody wrote; what makes it the published artifact is where it was fetched
  from. This is the step most likely to turn the whole audit vacuous if skipped, which is why it is
  first — a comparison against a copy of this tree would report *no differences* and mean nothing.

- **Step 2 compares against the tag, not `HEAD`** — 2026-08-23. The tree is 23 commits ahead, several
  of them written today, so comparing against `HEAD` would generate a finding per commit and bury a
  real one. The exclusion is written into the threshold above rather than applied silently while
  reading the results.

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → planned | **`specify` closed and `plan` written**, under the grant below, re-stated by the owner the same day on resuming: *"continue with T-241, full lifecycle, commit and push."* `specify` needed nothing — its open questions were already none, and no criterion moved. The plan carries the two things [`audit`](../plugin/skills/taskmd/docs/method/audit.md) says belong there rather than in a standing checklist: **the finding threshold, stated before looking**, and how this subject in particular is examined. **This record now carries the `adopter_visible` prompt** and still no field, which is [T-251](T-251-give-the-open-records-the-adopter-visible-prompt-they-predate.md) working as intended — the prompt asks at close, the field is written when it is answered. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, with commit and push** — given 2026-08-23 in these words: *"Work T-250, T-241, full lifecycle, commit and push, including anything raised during the work of these tasks."* Recorded here rather than only in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, committing and pushing, and the same for any task raised *by this work*. **What it does not:** any other task in the backlog — T-244, T-246, T-247, T-248 and T-240 are untouched by it. |
| 2026-08-23 | → proposed | Raised on the **project owner's** answer of 2026-08-23 to [T-231](T-231-cut-the-next-release.md)'s first question. **Raised now rather than at tag time**, and that is the point of raising it at all: an answer recorded only inside a struck-through question is invisible to every view, which is the defect [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) recorded when its own wait lived in a Log row. `blocked_by` names T-231, so the ordering rule reports this held until the release exists rather than a session having to remember a sentence. **`audit` by type and by the rule that follows from it**: its findings become their own tasks and none is repaired here. **Not part of the unattended grant** — that grant excluded the release and anything scheduled after it, and this is scheduled after it. Whoever picks it up is acting on the owner's answer above, not on that grant. **The half T-085 could not reach is in scope as a re-check, not as an inherited excuse**: unreachable in August is a fact about the machines of that week, and carrying it forward untested is how an audit comes to report what its author already expected. |
