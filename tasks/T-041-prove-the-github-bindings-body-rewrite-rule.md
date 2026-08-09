---
id: T-041
title: Prove the GitHub binding's body-rewrite rule by making it fail
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-010, T-037]
work_package: v0.1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-041 — Prove the GitHub binding's body-rewrite rule by making it fail

## 1. Specify

**Outcome**
The one rule in the GitHub binding that carries the contract's byte-identical guarantee has been
executed against a live repository, both correctly and incorrectly, and the record says what each
did.

**Why this one**
T-010's walk proved the binding's edges, phases, closure and enumeration — including two silent
failures made to fail on purpose. It did not touch the issue body once. So `update`'s sharpest
sentence is untested:

> Editing the body rewrites all of it, so read it first and put back everything you are not
> changing — including fields the schema does not name.

That sentence is where BINDING §1's "leaves everything it was not asked to change byte-identical"
is won or lost on this backend, because `gh issue edit --body` replaces rather than patches and
gives no warning that it did. It is also the rule most likely to be broken by an agent that is
confident it remembers the body. Everything else in the binding was proven; leaving this one on the
strength of having written it down carefully is the pattern `CLAUDE.md` *Verifying* rejects.

**Scope**
- In: performing the update both ways against a live repository — putting the whole body back, and
  writing only the changed field — and recording what each produced.
- Out: changing the rule. If the demonstration shows the rule is wrong or insufficient, that is a
  finding and a task, not an edit made while testing.

**Inputs**
- `docs/bindings/github-issues.md`, the `update` operation and D4 in T-010 §3
- A live repository with an issue carrying a property block, including at least one field the schema
  does not name — that is the field a careless rewrite drops silently, so it is the one that
  demonstrates anything

**Acceptance criteria**
- [ ] The correct procedure is executed and the untouched fields come back byte-identical, compared
      as bytes and not by eye
- [ ] The careless procedure is executed and **is shown to destroy** an unnamed field with no error
      and no warning — a pass on the correct path alone proves nothing here
- [ ] The binding's wording is confirmed sufficient to prevent the second outcome, or a finding says
      what it is missing
- [ ] ~~Whatever repository is used for this is either removed afterwards or recorded as needing to
      be~~ — dropped at `specify`; see the open question for the original text and the reason

**Open questions**
- ~~Which repository?~~ — **answered by the owner, 2026-08-07: the one T-010 used.** It stands until
  the first published version, so it is a fixture rather than something this task is keeping alive —
  which was the objection. T-037 now records the retention and its end date, so the failure mode
  this question was guarding against is closed by a written expiry rather than by avoiding the
  repository. Criterion 4 therefore has nothing to do here and is dropped, with its original text
  kept below.

  > *Original criterion 4, dropped:* "Whatever repository is used for this is either removed
  > afterwards or recorded as needing to be, so this does not leave a second orphan behind." It
  > measured a risk that no longer exists — no second repository is created, and the first one's
  > removal is T-037's, recorded there with a dependency. Keeping it would have made this task
  > responsible for another task's outcome.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Create an issue whose property block carries a field **the schema does not name**, alongside the fields it does. That unnamed field is the whole instrument: a rewrite that drops it breaks BINDING §1's `read` guarantee, and it is the only field whose loss no vocabulary check could ever catch. | An issue on the fixture repository, and its body captured as bytes before anything touches it |
| 2 | Perform `update` **as the binding says**: fetch the body, change one field, put everything else back. | The post-edit body captured, and a byte comparison against step 1 restricted to the untouched region |
| 3 | Perform `update` **as a confident agent would**: `--body` carrying only what it meant to change. | The resulting body, the exit code, and whatever warning was or was not emitted |
| 4 | Judge the binding's wording against what step 3 actually did — does the sentence as written stop it, or does it only stop someone who already knows? | A verdict in §3, and a finding if the wording is insufficient |

**Sequencing.** Step 3 must come after step 2, not before: it is destructive by design, and running
it first would leave nothing intact to compare against. The comparison in step 2 is byte-level
because "looks the same" is exactly the failure — a dropped line in a fenced block is invisible in
rendered Markdown, which is how this class of loss survives review.

**Shape of the deliverable — decided.** The output is evidence in this task's §3, not a change to
the binding. If the wording turns out to be insufficient, that is a finding and a task, per the
scope's out-list. Rejected: amending `github-issues.md` in the same breath as testing it, which
would leave no record of which wording was the one that failed.

**Output paths**
- This task's §3 — the two transcripts, the byte comparison, and the verdict on the wording

## 3. Implement

Run against the fixture repository on 2026-08-07, `gh` 2.96.0. Issue #4 carried a property block
with `review_ticket: EXT-4417` — a field the schema does not name, its value invented for this run
and referring to nothing — plus `Related: #1`, a soft edge,
and a paragraph of prose. All three are things an update must not touch.

**Step 2 — the correct procedure, and it failed.** Fetch the body, change `effort`, write it back.
The changed line changed. The untouched region did **not** come back byte-identical:

```
11a12
> 
```

One byte, and it is not a fluke. Three further round trips that changed **nothing at all** —
fetch the body, write the same body back — measured the fetched body at **230, then 231, then 232
bytes**. One byte per cycle, monotonic, forever.

The cause is the procedure, not the server. `gh issue view --json body --jq .body` appends jq's
trailing newline to the value it prints; feeding that straight back through `--body-file` stores a
body one newline longer than the one that was read. The binding tells you to fetch and write back,
and following it exactly is what does this. Over one task's four phase transitions that is four
bytes of drift; over a project's life it is unbounded. It is invisible in rendered Markdown, which
is why it would never have been found by looking.

So BINDING §1's "leaves everything it was not asked to change **byte-identical**" is not satisfied
by this binding's `update` as written — on every update, in the ordinary case, with nobody doing
anything wrong.

**Step 3 — the careless procedure, and it destroyed more than the criterion asked about.** Sending
`--body-file` with only the fields meant to change returned **exit 0**, in silence, and the stored
body afterwards contained neither `review_ticket` (grep count 0), nor `Related: #1` (grep count 0),
nor the prose.

The unnamed field was expected — that is what criterion 2 was built to demonstrate. **The soft edge
was not.** Losing `Related: #1` is a different order of failure: `related` has no native carrier on
this backend (D2 in T-010), so the body is its only home. There is no far end holding a copy, no
derived view to notice the absence, and no validator that could — the issue after the careless edit
is perfectly well-formed and simply has one fewer edge than it had a second earlier. On the local
backend the same mistake is recoverable from the other task; here it is not.

**Step 4 — the verdict on the wording: insufficient.** The binding says:

> Editing the body rewrites all of it, so read it first and put back everything you are not
> changing — including fields the schema does not name.

Three things it does not say, each of which step 2 or step 3 showed to matter: that following it
literally adds a byte every time; that the soft edges live in the body too and die with it; and
that `gh` reports success either way, so nothing distinguishes a correct update from a destructive
one at the point of running it. The sentence warns someone who already knows what to look for.

**Decisions & assumptions**
- **The binding is not edited here.** — This task's scope put wording changes out, and for a reason
  that held up: the record now names the exact wording that failed. Amending it in the same breath
  would have left the fix and no evidence of what it fixed. → **T-042**. — 2026-08-07
- **Issue #4 is left in its destroyed state.** — It is the artefact. Restoring it would erase the
  one example of what the failure looks like from the outside, which is: entirely normal. — 2026-08-07

**Outputs produced**
- This task's §3 — the two transcripts, the byte measurements, and the verdict on the wording

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The correct procedure leaves untouched fields byte-identical, compared as bytes | **not met** | It does not. `diff` reported one added byte after a single correct update, and three no-op round trips measured 230 → 231 → 232 — one byte each, monotonic. The criterion said "compared as bytes and not by eye", and that clause is the only reason this was found: the difference is a trailing newline, invisible in every rendered view. → **T-042** |
| The careless procedure destroys an unnamed field, with no error and no warning | met | `review_ticket` gone, grep count 0, **exit 0**. Met more comprehensively than intended: it also destroyed `Related: #1`, a soft edge whose only home on this backend is the body, and the prose. The criterion asked for one class of loss and got three. |
| The binding's wording is confirmed sufficient, or a finding says what it is missing | met | Judged **insufficient**, with three specific omissions named in §3: the byte growth, the soft edges, and the exit-0 silence. The criterion is met by the finding existing and being specific — its own text admits that answer. → **T-042** |
| ~~The repository is removed or recorded as needing to be~~ | n/a | Dropped at `specify` when the owner made the repository a fixture with a written expiry; original text and reason are in §1. |

Two met, one carried, one dropped before the work began. The failed criterion is the one this task
existed for — and it failed in the direction nobody was watching. The task was raised on the premise
that the *careless* path was the risk and the correct path was fine; the correct path is also
broken, and would have stayed broken indefinitely because it produces no symptom anyone looks at.

**Child fix tasks raised**
- **T-042** — both defects: the byte growth caused by following the binding, and the warning that
  understates what a careless rewrite destroys.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Two criteria met, one carried to T-042, one dropped at `specify` after the owner made the proof repository a fixture. The task was raised believing the careless rewrite was the risk; the **correct** procedure turned out to be broken too, adding one byte per round trip because the prescribed fetch feeds jq's trailing newline back in — 230, 231, 232 across three no-op cycles. The careless rewrite destroyed more than the criterion asked for: an unnamed field, the prose, and a soft edge whose only home on this backend is the body. Both at exit 0. |
| 2026-08-07 | → proposed | Raised by T-010's review. Criterion 5 named four phases, a dependency, a sub-issue, the derived inverses and the after-close enumeration, and every one of those was met — so the criterion passes and this is a gap it did not ask about, not a failure of it. Recorded as a task rather than as a caveat, since a caveat in a closed task's review is exactly the buried-gap failure `review` warns against. |
