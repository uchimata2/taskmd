---
id: T-183
title: Decide what to do about a machine block already published in T-085
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-034, T-080, T-085, T-133]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-18
updated: 2026-08-18
adopter_visible: no
deliverables: []
---

# T-183 — Decide what to do about a machine block already published in T-085

## 1. Specify

**Outcome**
A decision, taken by the owner, on whether the environment block in
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) §3 stays, is
redacted, or is labelled as accepted — and the pre-publish check left in a state where its output can
be trusted again.

**Why this one**
Found on 2026-08-18 while running `docs/PUBLISHING.md` §6 before a push. **The check is red and has
been for some time.** It printed four hits; two are known false positives and two are not:

| Hit | Reading |
| :--- | :--- |
| T-085 §3, two lines: a `user` name, `home /home/<name>`, and an OS version | **A real hit.** This is the category `CLAUDE.md` forbids by name — OS usernames, home directories, machine and OS specifics |
| T-129, `6.18.33.2` in a kernel version | False positive. The record itself says so |
| T-142, the scan's own patterns quoted in prose | False positive, and structural: a document describing the checker trips the checker |

**The block is already public.** T-085 was committed and pushed well before this was noticed, so the
question is not how to prevent it — it is what to do about a dated public record, which is the
question [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md)
answered for a release note and which METHOD rule 5 bears on directly.

**Why this is not simply fixed.** Three things are tangled and the owner holds two of them:

1. Whether the exposure matters at all. The name resembles the public GitHub handle this repository
   is published under, so the marginal disclosure may be nil — but that is the owner's judgement
   about their own data, not a call this project can make for them.
2. Whether a task record may be edited to remove it. Task files are an audit trail, and §1 of
   `docs/PUBLISHING.md` excludes them from rewriting for exactly that reason.
3. Whether history is rewritten. It is a published repository with adopters pulling from it.

**The half that is not a judgement call**: while the two false positives stay unlabelled, §6's
"it must print nothing" is unreachable, so the check gets read as *noisy* rather than *failing*. That
is how a real hit sat in the output unnoticed — the same failure shape as
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) and T-080, where the check's
output stopped being evidence.

**Scope**
- In: the decision on T-085's block, and a state where §6's output means something again.
- In: whether the two false positives are labelled, exempted by pathspec, or left.
- Out: rewriting published history unless the owner asks for it.
- Out: any change to the check's patterns. If they are wrong that is a separate finding.

**Inputs**
- `docs/PUBLISHING.md` §6 — the check, and what it says a hit means
- `CLAUDE.md` *Publishing constraints* — the categories, and what each costs to get wrong
- [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) — the
  precedent for a published record that breaks a rule adopted later

**Acceptance criteria**
- [ ] The owner's decision on T-085's block is recorded with its reason, whichever way it goes
- [ ] Running §6 afterwards prints nothing, or prints only what a named label accounts for
- [ ] If the block stays, the reason is written where the next person running §6 will meet it —
      not only in this record

**Open questions**
- **All three of the tangled questions above are the owner's**, and the first is about their own
  personal data. Nothing here can be settled by running something, which is why this task was raised
  rather than worked: it is outside the standing grant of 2026-08-18 on both counts.

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
| 2026-08-18 | → proposed | Raised while running the §6 pre-publish check before a push, during unrelated work on the six-task grant. **Not fixed, and deliberately**: the grant excludes anything its tasks raise, the decision is the owner's, and one third of it concerns their own personal data. The push it was found before went ahead — the block was already public, so holding the push would have blocked authorised work over an exposure it does not add to. Reported to the owner in the same session rather than left to be found here. |
