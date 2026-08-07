---
id: T-038
title: Reconcile BINDING section 5's worked example with the binding it predicted
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-009, T-010]
work_package: none
owner: maintainer
business_value: high
effort: s
created: 2026-08-07
updated: 2026-08-07
deliverables: [docs/BINDING.md]
---

# T-038 — Reconcile BINDING section 5's worked example with the binding it predicted

## 1. Specify

**Outcome**
`docs/BINDING.md` §5 and `docs/bindings/github-issues.md` say the same thing about what the GitHub
backend materialises, with whichever of them is wrong corrected rather than both softened.

**Why this one**
§5 was written before the binding, deliberately, to test the contract's wording against a backend
with no files — and it closes by claiming the exercise changed nothing but one paragraph of §3. It
states: *"this binding materialises nothing, and its assumptions section says so, which is the same
sentence that would be false for local Markdown."* The binding that was actually derived from it
says the opposite in its assumption 2: the issue's open/closed `state` is a materialised rendering
of the status label, because taskmd derives open/closed from `status` while GitHub stores it, and
something has to give.

So a worked example inside the contract now contradicts the binding written from that contract.
This matters more than a stale sentence usually would, for two reasons. §5 exists *as evidence*
that the contract does not assume a filesystem — an example that mispredicts the binding is weak
evidence for that claim. And §5's "materialises nothing" is the exact sentence BINDING §4 offers as
the model of a premise an adopter can check in thirty seconds; an adopter checking it would confirm
something false.

**Scope**
- In: deciding which document is wrong, and correcting that one. Whether §5's closing claim — that
  writing it changed nothing in the contract — still holds once the example is corrected.
- Out: re-opening D3 itself. T-010 §3 decided how `state` is carried and recorded the rejected
  alternative; this task reconciles the documents with that decision, and if it wants to overturn
  it, that is a different task with T-010's criteria in view.

**Inputs**
- `docs/BINDING.md` §3 (the materialised-derived-view rule) and §5 (the worked example)
- `docs/bindings/github-issues.md` — assumption 2, and D3 in T-010 §3 with its rejected alternative

**Acceptance criteria**
- [ ] The two documents agree on what the GitHub backend materialises, and the agreement is checked
      by reading them side by side rather than asserted
- [ ] The correction names which document was wrong and why, so the next person does not re-derive it
- [ ] §5's closing paragraph — "what this changed in the contract: nothing" — is either still true
      after the correction, or is replaced by what it did change
- [ ] Whether §3's materialised-view rule needs sharpening is answered either way. §5 reached
      "materialises nothing" from a genuine reading of §3, so if §3 permitted that reading, the
      rule is what needs the work and not just the example

**Open questions**
- None blocking `specify`. The likely answer is that §5 is the wrong document — it predicted from
  the documentation rather than from the tool, and T-010's probe found `state` only when the
  mapping had to be made real. But that is a finding to confirm during the work, not a premise.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide which document is wrong, on the evidence rather than on which is newer. | A decision in §3, naming the loser and why |
| 2 | Test the more interesting question: did §3's rule *permit* §5's reading? Read §3 as its author read it and see whether "materialises nothing" was a defensible conclusion from it. | A verdict in §3 — either §5 misread a sound rule, or the rule invited the misreading |
| 3 | Correct §5's worked example, and its closing paragraph, which claims the exercise changed nothing in the contract. | `docs/BINDING.md` §5, edited |
| 4 | Sharpen §3, if and only if step 2 says the rule was at fault. | `docs/BINDING.md` §3, edited or deliberately not |
| 5 | Read §5, §3 and the binding's assumption 2 side by side and confirm they say one thing. | A confirmation in §3 naming what was compared |

**Sequencing.** Step 2 sits before both edits because it decides how much is being fixed. If §5
merely mispredicted, this is a one-paragraph correction; if §3 invited it, then every future binding
was going to make the same mistake and the example is the symptom rather than the defect. Getting
that backwards would produce a corrected example sitting under a rule that still misleads.

**Shape of the deliverable — decided.** Edits in place in `docs/BINDING.md`, no new document.
Rejected: an erratum note recording that §5 once said otherwise — the contract is normative and read
by adopters, and a document carrying its own history of wrong statements makes the reader work out
which sentence is live. The history belongs in this task's record, which is where a reader who wants
it will look.

**Output paths**
- `docs/BINDING.md` — §5, and §3 if step 2 warrants it
- This task's §3 — the decision, the verdict on the rule, and the side-by-side confirmation

## 3. Implement

**Step 1 — §5 is the wrong document.** Not because it is older, but because of how each was
arrived at. §5 was written from GitHub's documentation, reasoning about what the backend would
require; the binding's assumption 2 was written after probing the tool and finding that `state` is a
stored property with no way to avoid writing it. Where a prediction and a measurement disagree, the
measurement wins, and there is no reading of the evidence in which "materialises nothing" is true.

**Step 2 — the rule invited it, so this is not a one-paragraph correction.** §3's materialised-view
rule illustrated itself with "a generated index file, a saved board". Both are whole-set artefacts,
and both read as the category rather than as examples of it. Applying that rule to GitHub, a careful
reader looks for an index-like thing, finds that the issue list already *is* the index, and
concludes nothing is materialised — which is exactly the inference §5 made, from a sound intention
and a rule that did not cover the case.

That matters beyond this example: a per-task property is the *harder* kind to notice, because it has
none of the tells of a stale artefact. There is no file with an old timestamp, nothing to regenerate,
and no second place to look. Every future binding would have had the same blind spot, so the example
was the symptom.

**Decisions & assumptions**
- **Both §5 and §3 are edited.** — Step 2's verdict. Correcting only the example would have left the
  rule that produced it in place, and the next binding author reasoning from §3 alone would reach
  the same wrong answer with no way to know. — 2026-08-07
- **§3 gains *Size is not the test* rather than a longer example list.** — Adding "…or a stored
  status flag" to the examples would fix this instance and leave the next per-item case uncovered.
  The defect was that the examples read as the category, so the fix names the test — does the
  backend store something your schema derives — and says explicitly that size is not it. — 2026-08-07
- **No erratum note in the contract.** — Decided at `plan` and held: `BINDING.md` is normative and
  read by adopters, and a document that carries its own corrections makes a reader work out which
  sentence is live. The history is here. — 2026-08-07
- **§5's closing paragraph is rewritten, not patched.** — It claimed the exercise changed nothing in
  the contract. It has now changed §3 twice, and the second change came from the opposite direction:
  the real binding correcting the worked example. Saying so is more useful than the original claim,
  because it bounds what an exercise like §5 is evidence *for* — the wording, not the backend. — 2026-08-07

**Step 5 — the side-by-side.** `BINDING.md` §3 *Size is not the test*, `BINDING.md` §5's corrected
paragraph, and `bindings/github-issues.md` assumption 2, read together. All three now say: `state`
is stored by the backend, derived by the schema, written from the status label, and never read.
The enumeration rule is stated in §5 and in the binding with the same reason attached, rather than
as a rule in one place and a habit in the other.

**Outputs produced**
- [`docs/BINDING.md`](../docs/BINDING.md) — §3 gains *Size is not the test*; §5's prediction and
  closing paragraph corrected

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The two documents agree on what the backend materialises, checked by reading them side by side | met | Step 5 in §3: §3's new paragraph, §5's corrected prediction and the binding's assumption 2 read together. All three say `state` is stored, schema-derived, written from the label, never read — and §5 and the binding now give the enumeration rule the same reason rather than one stating it and the other assuming it. |
| The correction names which document was wrong and why | met | §5, and the "why" is the part worth keeping: it was written from documentation while the binding was written from the tool. Recorded as a general limit on that kind of exercise, in §5 itself, so the next person does not over-trust the next worked example. |
| §5's closing claim is still true, or replaced by what it did change | met | Replaced. "What this changed in the contract: nothing" became "§3, twice", with the second change attributed to the binding correcting the example rather than the other way round. |
| Whether §3's rule needs sharpening is answered either way | met | Answered **yes**, and it turned out to be the larger half of the task. §3's two illustrations were both whole-set artefacts and read as the category, so "materialises nothing" was a sound inference from an unsound rule. Fixed by naming the test — does the backend store something your schema derives — rather than by lengthening the example list, which would have covered this case and missed the next. |

Four met, none carried. The task was raised expecting a stale sentence and found a rule that would
have reproduced the same error in every future binding.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | All four criteria met. §5 was the wrong document — written from GitHub's documentation, where the binding was written from the tool — but step 2 found the larger defect: §3 illustrated materialisation with two whole-set artefacts, so "materialises nothing" was a sound inference from a rule that did not cover a per-task property. Fixed by naming the test rather than lengthening the examples, since a longer list covers this case and misses the next. §5's closing claim that the exercise changed nothing in the contract is replaced by what it did change, including the admission that the real binding corrected the worked example rather than the reverse. |
| 2026-08-07 | → proposed | Raised by T-010 while writing the binding §5 anticipated. Not fixed in place: the contradiction is in T-009's deliverable, and METHOD rule 4 keeps a finding out of the task that found it — a silent edit to BINDING §5 here would have made T-009's record false and left no trace that the contract's one worked example had mispredicted. |
