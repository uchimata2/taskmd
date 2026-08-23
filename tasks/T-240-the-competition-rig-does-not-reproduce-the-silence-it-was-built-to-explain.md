---
id: T-240
title: The competition rig does not reproduce the silence it was built to explain
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-213, T-206, T-175]
work_package: M6
owner: the project owner
waiting_on: the project owner
business_value: medium
effort: m
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-240 — The competition rig does not reproduce the silence it was built to explain

## 1. Specify

**Outcome**

An answer, recorded, on **which difference between the rig and the venue** accounts for the observed
session invoking nothing while every rig run invokes — or a statement that it cannot be found with
the instruments available, and what that costs the two records resting on it.

**Where this came from**

[T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) observed a real
session in a migrated-away project on 2026-08-21. It was handed the skill, asked *"What should I do
next?"*, and **never invoked it**.
[T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) then
tested the wording with no competition and got 8/8 invocations.
[T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)
added the observed 68-skill field on 2026-08-23 and got **14/14**.

**So neither explanation the two tests were built to separate occurred.** The description did not
turn a session away and it did not lose a competition. **What has not been explained is the
observation itself**, and two records now rest on rigs that cannot reproduce it.

**The three carried confounds are the candidates, and none has been tested.**

| # | Difference between rig and venue | Why it could account for the whole gap |
| :-- | :--- | :--- |
| 1 | The rig's skill is named `rigtask` | The description's closing clause is *whenever the user says taskmd*. Renamed, that clause matches nothing a user could say, so the rig has never exercised the one sentence written to force a match — and it still won every time, which makes the clause look unnecessary rather than untested |
| 2 | The rig serves a **project-local** skill; the venue served an **installed plugin** | Different load path, possibly different placement and weight in the listing. T-053 and T-083 both turn on the plugin boundary being a real thing |
| 3 | The field is **reconstructed** from a transcript listing, not served by the mechanism that served it | It reproduces the descriptions, and not necessarily their ordering, grouping or weight |

**And a fourth arrived in T-213's own run, unplanned.** The field it served was **77**, not the 68 it
built: nine skills came from the running machine's own user-level plugins, one of them **the real
`taskmd` with its shipped description**. So the rig is not only unlike the venue, it is unlike itself
as specified. Whatever is tried next has to control for the harness's own additions, which T-213's
plan did not know it had to.

**Scope**

- In: which of the four differences accounts for the gap, tested one at a time rather than argued
- In: what the answer costs [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md)'s
  and [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)'s
  verdicts, both of which stand on rigs that do not reproduce the observation
- In: controlling the harness's own skill additions, which is a rig defect and not a finding about
  the description
- Out: changing the shipped description. T-206 drafted a candidate and neither test found evidence
  it is better; applying it is a separate decision on evidence nobody has yet
- Out: re-opening T-175's observation. What it recorded happened, and this record exists because it
  cannot be reproduced rather than because it is doubted
- Out: any further reader protocol. Different instrument, different question

**Inputs**

- [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)
  §3 — the 14 runs, the served-field measurement, and the confound list
- [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) — the
  8 runs with no competition, and the candidate wording it drafted
- [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) §3 — the
  observation, its prompt, and what the session did instead

**Acceptance criteria**

- [ ] Each of the four differences is either tested or declined **by name**, with a reason for each
      decline
- [ ] Any run reports the field it was **actually served**, not the field it was built with — the
      measurement T-213 only made after the fact
- [ ] The answer says what it costs T-206's and T-213's verdicts, in their own terms
- [ ] If no difference accounts for the gap, that is stated as the result rather than filled with
      judgement

**Open questions**

- **Is a second real observation available, and is it yours to arrange?** — the **project owner**.
  Differences 2 and 3 can only be closed by observing a real session in a real migrated-away project
  again, which no session here can arrange for itself. **Recommendation: test difference 1 first**,
  which is cheap and local — rename the rig's skill to `taskmd` and re-run, so the closing clause is
  exercised for the first time. If the gap survives that, ask for the observation. *Against:*
  renaming makes the rig's skill collide with the real plugin the harness already serves, which is
  the fourth difference arriving again and would have to be controlled first.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

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
| 2026-08-23 | (no change) | **Answered by the owner on 2026-08-23: test the cheap difference first.** Rename the rig's skill to `taskmd` and re-run, so the closing clause is exercised for the first time. **The fourth difference has to be controlled before that run means anything** — §1 records that the rig served 77 skills where it built 68 and one of the nine extras was the real `taskmd`, so a rename collides with it. *Rejected: arrange the real observation now* — the only thing that can settle differences 2 and 3, and it costs a real project's time for a question that blocks nothing. *Rejected: fold it into [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md)* — it defers a record that is already deferred. **`waiting_on` stays set**: the observation may still be needed if the cheap test does not close the gap. |
| 2026-08-23 | → proposed | Raised from [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md)'s `review`, under the owner's instruction of 2026-08-23 to complete every task except the release and what is scheduled after it — which is what authorised T-213 past `plan` and reaches what that work raises. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), and **any audit**, which remains the boundary the owner named on 2026-08-22. **This record stops at `specify`**: its open question is the owner's, because two of the four differences can only be closed by observing a real session in a real migrated-away project, and no session can arrange that for itself. `waiting_on` is set so a view says so rather than a sentence here — the mechanism [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) built the same day. **A soft edge from T-213 and not a child**: T-213's outcome is a verdict on the competition question and that verdict exists and is stated in two parts. Why the venue and the rig disagree is a further question, not a missing piece of that one. **The fourth difference is the one worth reading**: T-213's rig served 77 skills where it built 68, and one of the nine extras was the real `taskmd`. A rig that is not what its own builder says it is has to be fixed before any of the other three can be tested cleanly. |
