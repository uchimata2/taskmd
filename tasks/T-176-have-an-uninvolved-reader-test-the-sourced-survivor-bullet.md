---
id: T-176
title: Have an uninvolved reader test the sourced survivor bullet
type: research
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-168, T-166, T-167]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-22
deliverables: []
---

# T-176 — Have an uninvolved reader test the sourced survivor bullet

## 1. Specify

**Outcome**
A verdict from a reader who was not involved on whether the sourced survivor bullet in the migration
listing reads as evidence or as advocacy — the check every other claim in that document passed, and
the one [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) declared
rather than ran.

**Why this one**
**[T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) §3 step 7
records this as an honest gap rather than implying it was covered.** Its mechanical checks all passed
— `check`, `index`, the suite, and a diff confirming one hunk — and none of them can see the thing
that matters here.

**The risk is specific and it has a history.** The bullet now attaches a per-session cost to one of
four survivors in a document whose lean
[T-167](T-167-stop-the-listing-pricing-only-the-rival.md) closed as **accepted**. A number can
re-balance a document without changing a single other sentence, and
[T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 is the precedent: a fresh
reader found five framing mechanisms nobody had seen, on a document that had already passed a
claim-by-claim check. A claim-by-claim check cannot see framing, which is exactly what this needs
looking at.

**Set the reader count before the result is known.** T-166 ran one reader and let the verdict stand,
deliberately, because a second reader after an unwelcome first is iteration wearing a fresh reader's
clothes. That decision is the one to copy.

**Scope**
- In: whether the sourced bullet reads as evidence or tilts the document, judged by someone who was
  not involved in producing it
- In: whether the *unobserved* half of the bullet reads as an honest limit or as a hedge
- Out: re-balancing the listing. The five framing mechanisms accepted in
  [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) stay out, and a reader's opinion does not
  re-open a decision the maintainer took
- Out: the figures themselves, which are
  [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s and are not
  in doubt

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md`, *What survives* — the bullet, and the three
  beside it that set the form
- [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) §3 — the reader protocol, and
  the extraction lesson: a slice that cuts what the document points at tests a document nobody
  receives

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- ~~**One reader, or does this need the same protocol T-166 used?** One reader with the verdict
  standing is the recorded precedent and the cheaper option. **The maintainer decides**, and the
  count is set before the reader runs, not after the verdict is read.~~ **Answered by the owner on
  2026-08-19: one reader, and the count is fixed now** — see the Log row of that date.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **Re-edged from `parent: T-168` to a soft edge, by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md).** [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) was not raised from a failed criterion — five of its six were met and the sixth went to T-174. This task came out of `review` step 5, as a residue nobody there could settle: the bullet has not had an **uninvolved reader**, and no session can supply one. T-168's own outcome — the price, with the evidence behind it — exists and was checked. So this is a stronger test of a finished result, not a part of it, and holding T-168 open would park a closed research task on a person who may never be available. `related` was already recorded here, so the repair is one field. The alternative — reopening T-168 — is rejected on that reasoning and is recorded in T-216 §3. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: one reader, count fixed now.** Asked in the backlog-wide round of 2026-08-19. One reader with the verdict standing is the recorded precedent and the cheaper option, and setting the count before anyone reads is the whole of what makes it a check. *Rejected: the fuller [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) protocol*, which buys more confidence at more of the owner's time — and buys it only if the count is fixed in advance either way, since a second reader added after an unwelcome verdict converts the check into editing until somebody agrees. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised by [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md)'s review. Its §3 step 7 declared the gap rather than papering over it, which is what [`implement`](../plugin/skills/taskmd/docs/method/implement.md) asks for when no use is available; this is the task that makes the declaration actionable instead of a sentence in a closed record. **Not covered by the authorisation of 2026-08-18.** |
