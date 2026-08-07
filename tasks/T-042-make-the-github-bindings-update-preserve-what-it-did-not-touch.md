---
id: T-042
title: Make the GitHub binding's update preserve what it did not touch
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-010, T-041]
work_package: none
owner: maintainer
business_value: critical
effort: m
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-042 — Make the GitHub binding's update preserve what it did not touch

## 1. Specify

**Outcome**
`docs/bindings/github-issues.md`'s `update` operation satisfies BINDING §1's byte-identical
guarantee when followed, and its warning names the failure that actually happens rather than the one
that was imagined — both demonstrated on a live repository, not argued.

**Why this one**
T-041 executed the operation and found two defects, one in each direction:

1. **Following the binding correctly corrupts the body.** `gh issue view --json body --jq .body`
   appends jq's trailing newline; feeding that back through `--body-file` stores a body one byte
   longer. Measured across three no-op round trips: 230 → 231 → 232 bytes. Monotonic, unbounded,
   invisible in rendered Markdown, and caused by the procedure the binding prescribes.
2. **The warning understates what a careless rewrite destroys.** It names "fields the schema does
   not name". T-041's run also silently destroyed a **soft edge** — and `related` has no native
   carrier on this backend, so the body is its only home. No far end holds a copy, no derived view
   can notice, and the resulting issue is perfectly well-formed with one fewer edge. `gh` returned
   exit 0 for the destructive edit and exit 0 for the correct one.

This is `business_value: critical` because it is the one operation in the binding that can lose data
that exists nowhere else, and because defect 1 means the binding does not currently conform to the
contract it claims to implement.

**Scope**
- In: the `update` operation's procedure and its warning; whatever else in the binding has to change
  so `read` and `update` compose without drift.
- Out: the carrier decisions. D2 put `related` in the body and D3 made `state` a rendering; both
  stand. If defect 2 is judged to be an argument against D2 rather than against the wording, that is
  a separate task with T-010's criteria in view — not a reversal made while fixing a sentence.

**Inputs**
- T-041 §3 — the transcripts, the byte counts and the verdict on the wording
- `docs/BINDING.md` §1, `update`, for the guarantee being missed
- The fixture repository, which stands until first publication (T-037)

**Acceptance criteria**
- [ ] A no-op update — fetch the body, write it back unchanged — leaves the stored body **byte-identical**,
      shown by repeating it at least three times and measuring, since one clean cycle is what the
      broken procedure also looks like
- [ ] A real update changes only the intended field, with the rest byte-identical, measured the same way
- [ ] The warning names all three of what T-041 found: the soft edges in the body, the fields the
      schema does not name, and that `gh` exits 0 either way
- [ ] The destructive case is **run again after the fix** and still destroys what it destroyed
      before — the fix must make the correct path safe without making the careless path look safe
- [ ] Nothing in the fix requires a tool the binding does not already assume; if it needs one, that
      is stated as an assumption per BINDING §4

**Open questions**
- None blocking `specify`. The likely shape is to prescribe a fetch that does not add the newline
  and to say so explicitly rather than leaving it to whoever pipes the command — but which
  invocation to standardise on is `plan`'s to choose, and criterion 1's repeat-and-measure is what
  decides between candidates rather than preference.

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
| 2026-08-07 | → proposed | Raised by T-041, which was itself raised by T-010's review to test the one operation T-010 never executed — and found the operation broken in the ordinary case, not just the careless one. Kept out of T-041 because that task's scope explicitly put wording changes out, so that the record would name the exact text that failed; fixing it there would have left the correction with no evidence of what it corrected. |
