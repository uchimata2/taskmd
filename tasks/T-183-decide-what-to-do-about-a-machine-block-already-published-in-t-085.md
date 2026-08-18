---
id: T-183
title: Decide what to do about a machine block already published in T-085
type: decision
status: done
phase: review
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
deliverables: [docs/PUBLISHING.md]
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
| T-085 §3, two lines: a `user` name, a home-directory path naming it, and an OS version | **A real hit.** This is the category `CLAUDE.md` forbids by name — OS usernames, home directories, machine and OS specifics |
| T-129, a four-part kernel version quoted in prose | False positive. The record itself says so |
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

**Described, never reproduced.** The rows above name the shapes without writing either of them
out, because quoting a scanner's match trips the scanner — this record would otherwise have
added two hits to the output it exists to clean up.

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

  **Answered by the owner on 2026-08-18: accept the block, and repair the check around it.**

  The exposure is a user name one character from the public account this repository is published
  under, a home path built from that same name, and an OS version. No host, no address, no secret.
  *Rejected: editing T-085.* It leaves the text in git history, so it buys the appearance of a repair
  rather than a repair, and it damages an audit trail the project's own rules protect. *Rejected:
  rewriting history.* It genuinely removes the text and breaks every clone, moves every commit hash
  and every tag, for a disclosure already made — a real cost against a marginal gain. **The reversing
  condition, recorded so it is not re-derived**: if that user name is ever shared with an identity the
  owner does not want linked here, the marginal-disclosure argument fails and history rewriting
  becomes worth its price.

  **The second half was not a judgement call and is not treated as one.** The two remaining hits were
  never acceptable noise: `docs/PUBLISHING.md` §6 already carried a written remedy for each, and
  neither had been applied.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Record the owner's decision and both rejections, with the condition that would reverse it | The answered question in §1 |
| 2 | **Check whether the two false positives are actually tolerated or merely unrepaired**, by reading what §6 already says about each | The finding, in §3 |
| 3 | Apply §6's own remedies at the source, and log each edit as typographic | The two edited task records |
| 4 | Give the accepted hit a home a runner meets, and restate §6's pass condition so it can be read at a glance | The edited docs/PUBLISHING.md |
| 5 | Run both of §6's runs and confirm the counts match what it now claims | The two counts, in §3 |

**Step 2 is placed before any exemption is designed**, because an exemption for something that should
simply be fixed is the expensive answer to the wrong question.

**Decisions taken at `plan`**

- **T-085 is not excluded by pathspec.** — An exclusion silences the file for ever, including
  whatever it gains later, and §6 states its single exclusion is *one pathspec, not a second
  contract*. A counted pass condition keeps the file scanned and still lets a run be judged in one
  glance. *Rejected: a second pathspec exclusion.* — 2026-08-18
- **Nothing goes into `control/LOCAL-CONTEXT.md`.** — That file maps labels to identities kept **out**
  of the tracked tree. This decision does the opposite: the identity stays, accepted. A row there
  would imply a redaction that did not happen. — 2026-08-18

**Outputs this task will produce**

- docs/PUBLISHING.md — §6's pass condition and the accepted exception
- tasks/T-129-release-v0-5.md, tasks/T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md
  — the two source repairs

## 3. Implement

### Step 2 — the finding that changed the shape of this task

**Neither "false positive" was a false positive to be tolerated. Both were documented rules nobody
had applied.** §6 already says, in its own words:

- *"a dotted four-part version number fires the IP branch — a kernel or build string in a task record
  will trip it, and nothing has leaked when it does; **elide a component and move on**"*;
- *"quoting a matched line into a task record re-creates the leak. This has now happened twice, in
  T-013 and again in T-018 while fixing T-013. **Describe the result and point at the fixture; never
  paste the lines**"*.

T-129 quoted a four-part kernel version in full **while describing the leak check reporting it**.
T-142 listed the check's own home-directory patterns literally **inside a sentence asserting that a
scan found nothing** — so the sentence claiming cleanliness was itself two of the hits. Both are the
third and fourth instances of a failure §6 had already counted twice.

So the scope line *"whether the two false positives are labelled, exempted by pathspec, or left"*
offered three options and the answer was a fourth: **repaired**.

### Step 3 — the two source repairs

Each is typographic and changes no claim; each carries a log row in its own record saying so.

| Record | Was | Now |
| :--- | :--- | :--- |
| T-129 | the four-part version, quoted in full | described as *a four-part kernel version string* |
| T-142 | the two home prefixes, listed literally | described as *either common home-directory prefix* |

### Step 4 — the accepted hit, given a home

§6's opening now states the pass condition as a **count**, and two paragraphs after the command carry
the decision, its two rejections and why no pathspec exclusion was used. A person running the check
meets all of it before they read the command, which is what criterion 3 asks for. The proving run's
expected output was corrected in the same edit — it had claimed the fixture's five lines, and it is
now those five plus the two accepted.

### Step 5 — both runs, measured

```text
with the fixture exclusion      2 lines   both in tasks/T-085-...md   (the accepted pair)
without it                      7 lines   = the 2 accepted + exactly 5 fixture lines
fixture lines in that run       5         one per class, all still caught
```

Matches what §6 now claims, in both directions. **The second run is the one that matters**: it proves
the check still catches all five classes, which the first run can never show — and it is why the
accepted pair was left in scope rather than excluded.

**Decisions & assumptions**
- Both `plan` decisions held. — 2026-08-18
- **Assumption, recorded as one**: T-085 is closed and will not gain content, so keeping it scanned
  costs nothing today. If it were ever reopened the counted condition is what would notice. — 2026-08-18

**Outputs produced**
- docs/PUBLISHING.md
- tasks/T-129-release-v0-5.md
- tasks/T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The owner's decision recorded with its reason, whichever way it goes | **met** | §1's answered question: accept, with both rejections and the condition that would reverse it |
| Running §6 afterwards prints nothing, or only what a named exception accounts for | **met** | Exactly 2 lines, both named in §6. Down from 4, and the two removed were repaired at source rather than exempted |
| If the block stays, the reason is where the next person running §6 will meet it | **met** | `docs/PUBLISHING.md` §6, in the opening pass condition and the two paragraphs above the command — not only in this record |

**Open questions, re-read before closing** (procedure step 5)

§1's question is answered by the owner and carries its own reversing condition, which is the part a
later reader must not lose: this is an accepted exposure, not a settled one.

**A residue that is not a criterion.** §6's *three limits* paragraph says a four-part version and a
quoted pattern will trip the check, and both have now tripped it four times between them. The
document states the remedy and nothing applies it; every instance has been caught by a person, twice
by accident. Whether that warrants a mechanical guard is a question this task did not ask and does not
answer — noted here because closing it would otherwise take the observation with it.

**Child fix tasks raised**
- none

## Log


| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | The owner accepted the block the same day it was raised, and the repair around it ran `specify` to close. **The task's shape changed at step 2**: its scope offered three ways to handle the two other hits — label, exempt, or leave — and the answer was a fourth, *repair*. Neither was a false positive to tolerate; §6 already carried a written remedy for each and neither had been applied, making them the third and fourth instances of a failure that document had already counted twice. So four hits became two by fixing two records, not by exempting them. The accepted pair is **not** excluded by pathspec — §6's pass condition is now a count, so T-085 stays scanned and a run is still judgeable at a glance. Both documented runs measured: 2 with the fixture exclusion, 7 without, of which exactly 5 are the fixture's, so the check is proven to still catch every class. |
| 2026-08-18 | → proposed | Raised while running the §6 pre-publish check before a push, during unrelated work on the six-task grant. **Not fixed, and deliberately**: the grant excludes anything its tasks raise, the decision is the owner's, and one third of it concerns their own personal data. The push it was found before went ahead — the block was already public, so holding the push would have blocked authorised work over an exposure it does not add to. Reported to the owner in the same session rather than left to be found here. |
