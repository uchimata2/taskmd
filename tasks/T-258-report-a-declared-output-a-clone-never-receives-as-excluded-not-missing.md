---
id: T-258
title: Report a declared output a clone never receives as excluded, not missing
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-257, T-103, T-098, T-013]
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-258 - Report a declared output a clone never receives as excluded, not missing

## 1. Specify

**Outcome**
`check` draws the same distinction for a declared output that it already draws for a document: an
artefact that exists but that a clone would never receive is reported as **excluded**, in the `Scope`
lines, and does not take the exit code to 1. A path that is genuinely gone still fails, unchanged.

**Why this one**
**`check` already knows this distinction and applies it on one side only.** It prints
`Scope  84 document(s) not read: a clone would not receive them` - the document-side filter
[T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) put there - and
then reports a `deliverables:` path under the same condition as
`MISSING OUTPUT ... which does not exist`. Two paths, same fact about the reader, opposite verdicts.

**It is not hypothetical, and this project has now met it twice.**
[T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) was raised when the
asymmetry took CI red for a day: `control/LOCAL-CONTEXT.md` is gitignored on purpose by
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md), so it exists here and in no
clone, and the working tree passed while every clone failed. The first time was the adopting
project's `R-5`, which became
[T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) - **the same file, the
same rule, a different gap in it.**

**This record is the second half of the owner's answer, and it is raised before the first half
lands.** The owner chose *unblock now, fix properly after* on 2026-08-23 and named the failure mode
of that choice in the option itself: once the gate is green, nothing is left arguing for the repair.
So T-257's plan raises this record as its step 1, ahead of the one-line edit that removes the pain.

**What the unblock cost, stated so this record can restore it.** Reading 1 removes
`control/LOCAL-CONTEXT.md` from T-250's `deliverables`, which means the project no longer records
that [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) produced that file
anywhere a command can see. The declaration is the fact; a Log row is a consolation. Closing this
task is what makes re-declaring it safe.

**Scope**
- In: how `check` decides that a declared path is excluded rather than missing, and what it prints
- In: the exit-code consequence - excluded does not fail, missing still does
- In: whether T-250's declaration is restored once this ships, since removing it was the unblock and
  not the answer
- Out: any new configuration key. The document side needed none, and a key is what
  [`.taskmd/config.md`](../.taskmd/config.md)'s *What this rule has already refused* declines twice
- Out: what `check` reports about a path that is genuinely gone. Right under any answer, and T-257
  scoped it out for the same reason

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` - the document-side filter and the `MISSING OUTPUT` check, so
  the two can be read side by side
- [T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) - the document
  side, with its alternatives already priced
- [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) - the decision this
  implements, and the survey of the class

**Acceptance criteria**
- [ ] A tracked declared path that is deleted still fails `check`, and the run is shown failing on it.
      A rule that never fires and a rule that cannot are worth the same
- [ ] An untracked declared path is reported in `Scope` and does not move the exit code, shown on a
      case that could have fired
- [ ] Verified in a **fresh clone** and not in the working tree, which is the instrument that missed
      the original defect for a day
- [ ] T-250's declaration is restored, or the record says why it is not

**Open questions**
- **How exclusion is detected without a config key.** The document side has a mechanism already;
  whether it reaches a `deliverables:` path unchanged is a question for whoever plans this, and the
  answer decides whether this is small or not.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision - rationale - date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised as step 1 of [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md)'s plan, deliberately before that task's one-line unblock lands.** The owner's answer of 2026-08-23 was *unblock now, fix properly after*, and the option they chose names its own failure mode: a follow-up whose only constituency is a red gate loses it the moment the gate goes green. So the record exists first. |
