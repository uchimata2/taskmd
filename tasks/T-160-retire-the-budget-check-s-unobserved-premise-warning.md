---
id: T-160
title: Retire the budget check's unobserved-premise warning, now that it is observed
type: fix
status: done
phase: review
parent: T-153
blocked_by: []
related: [T-159]
work_package: M6
owner: maintainer
business_value: low
effort: xs
created: 2026-08-16
updated: 2026-08-16
deliverables: []
---

# T-160 — Retire the budget check's unobserved-premise warning, now that it is observed

## 1. Specify

**Outcome**
`tests/test_budget.py` stops printing a sentence that is false. Its second report line currently ends
`not yet observed here (T-153)`; [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md)
observed it on 2026-08-16.

**Why this one**
The line was [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s plan step 5,
and its stated job was to keep an unobserved premise visible **until it was observed**. That
condition has now been met, so the line has outlived the reason it was written. It is small and it is
the kind of thing this repository treats as a defect rather than as tidying: a gate that prints a
false sentence on every run trains its reader to skim it.

**What replaces it is the decision, not the deletion.** The stripped figure itself is still worth
printing — it says how much of the file a session is not paying for. What has to change is the clause
claiming nobody has checked.

**Scope**
- In: the second line of `report()` in `tests/test_budget.py`, and any test that asserts on its
  wording.
- In: **the same claim wherever else it stands in that file** — widened at `specify`, 2026-08-16;
  see the decision below.
- In: whether the observation is cited by date and task, so the claim stays checkable rather than
  becoming an unsourced assertion in the other direction.
- Out: the strip itself, and the figure it produces. Both are proven and neither changes.
- Out: `CLAUDE.md`. Nothing moves there; that is
  [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md)'s question.

**The scope was widened at `specify`, and the draft that named one line was wrong.** The raising
session wrote *the second line of `report()`* from the outside, before reading the module.
`strip_block_comments`'s docstring carried the same claim — *a documented behaviour no session here
has yet observed* — and it explains **why** the printed line says what it says. Correcting the output
and leaving its explanation standing would have left the file arguing against itself, which is a
worse state than the one this task was raised to fix. Fixing one falsehood and stepping over its twin
four lines up is not a narrower task, it is a half-done one.

**Inputs**
- `tests/test_budget.py` — `report()`, `strip_block_comments`, and the two tests that assert on the
  report's output
- [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) — the observation, its date and
  its marker
- [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) — why the line was written

**Acceptance criteria**
- [x] The report no longer claims the behaviour is unobserved
- [x] It still names the stripped figure, so the reader learns what a session does not pay for
- [x] The new wording cites the observation by date and task, rather than asserting soundness flatly
- [x] Any test asserting on the old wording is updated, and the suite passes
- [x] The change is checked by running the report and reading its actual output, not by reading the
      code

**Open questions**
- none.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Reword `report()`'s second line: keep the figure, replace the provenance clause with the observation, cited by date and task | The line below |
| 2 | Sweep the same file for the same claim rather than fixing only the printed one | `strip_block_comments`'s docstring |
| 3 | Give the citation a reader. Nothing in the suite read past the line's first clause, so its provenance could have gone stale or been deleted in silence | One test |
| 4 | Prove that test on the case it exists to catch — run it against the old wording and record the failure | A recorded failure, not a clean pass |
| 5 | Run the report and read its **actual output**, per this repository's verifying rule | The output below |

## 3. Implement

**The line now reads** — `tests/test_budget.py`, `report()`:

```
       836 chars of block comment are not counted: the harness strips them before injecting, observed 2026-08-16 in what a session was handed (T-159)
```

It is shorter than the sentence it replaces, keeps the figure, and says how the claim was established
rather than asserting it. `in what a session was handed` is the part that matters: it names the
instrument, so a later reader can tell this apart from a premise read off documentation — which is
what the old line was warning about.

**The same claim stood four lines up**, in `strip_block_comments`'s docstring, and is corrected to
match: *that premise was documented rather than seen until T-159 observed it on 2026-08-16; `report`
cites the observation on every run rather than asserting the behaviour flatly.*

**Nothing in the suite had ever read the clause that was false.** The two existing tests assert on
`chars of block comment are not counted` and `chars of block comment` — both substrings of the half
that did not change. So the provenance clause, which carried the *whole* of T-153's safety mechanism,
could have been deleted or gone stale and no test would have failed. That is why step 3 exists and
why this task produced a test rather than only an edit:

```
test_the_stripped_line_cites_its_observation
```

**Proved by failing, not by passing.** Run against the old wording before the fix was restored:

```
FAIL: test_the_stripped_line_cites_its_observation
AssertionError: 'T-159' not found in '       210 chars of block comment are not counted: the
harness is documented to strip them before injecting and this check follows it - not yet
observed here (T-153)' : the observation is cited by task
```

**Checked by being used** — the report run on the real tree, 2026-08-16:

```
tier 1 6305 chars under by 1541 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
       836 chars of block comment are not counted: the harness strips them before injecting, observed 2026-08-16 in what a session was handed (T-159)
scope  this repository's own tier 1 - the files named above. ...
also   instruction count is a second constraint on the same file, ...
```

```
Ran 264 tests - OK (skipped=3)
```

**Decisions & assumptions**

- **The scope was widened at `specify` to the whole file's version of the claim** — 2026-08-16,
  argued in `specify` above. *Rejected:* keeping the literal draft scope and raising a second task
  for the docstring, which would have spent a record on four lines of the file already open, and
  left the two contradicting each other in the meantime.
- **A test was added, not just an edit made** — 2026-08-16. The old clause had no reader, so
  correcting it without one would reproduce exactly the condition that let it go false: a claim
  nothing checks. *Rejected:* trusting the wording to stay right, which is what the last day
  disproved.
- **The date and task are asserted separately** — 2026-08-16, so a citation that loses half of
  itself fails rather than passing on the surviving half.
- **The module docstring is deliberately left alone** — 2026-08-16. Its point 5 says the harness
  strips block comments and attributes the fenced-comment case to T-153. Neither statement was ever
  a claim about observation, so neither is false, and editing true prose to look freshly touched is
  churn.

**Outputs produced**

- `tests/test_budget.py` — `report()`'s second line, `strip_block_comments`'s docstring, and
  `test_the_stripped_line_cites_its_observation`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The report no longer claims the behaviour is unobserved | met | Read off the real run above, not off the source. `not yet observed` is additionally asserted absent by the new test. |
| It still names the stripped figure | met | `836 chars of block comment are not counted`, unchanged, and still the first clause. |
| The new wording cites the observation by date and task | met | `observed 2026-08-16 in what a session was handed (T-159)`. Date and task are asserted as two separate reads, so half a citation fails. |
| Any test asserting on the old wording is updated, and the suite passes | met | **The first clause is vacuous and the finding is in why.** No test asserted on the wording that changed — both existing ones read only the unchanged half, which is how the false clause survived a day unnoticed. Nothing needed updating; something needed adding. Suite `OK (skipped=3)`, 264 tests, one more than before. |
| Checked by running the report and reading its actual output | met | Both directions: the report's real output above, and the new test **failed** against the old wording before the fix was restored. A clean pass alone would have proved nothing. |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | → proposed | Raised from [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md)'s `review`, which found the line false the moment [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) answered. Filed rather than fixed inside that review: correcting it is `implement` work, and T-153 was authorised for `review` only. `low` and `xs` — one sentence, and nothing depends on it being taken soon; the falsehood is in a warning that has already done its job, not in a figure. |
| 2026-08-16 | — | **The maintainer authorised this task's whole lifecycle in one request** — `specify` → `plan` → `implement` → `review`, and the commit and push after it — covering **T-160 and nothing else**. Recorded here rather than only in the request (METHOD §3.1). |
| 2026-08-16 | → done | All five criteria met. The task came out larger than `xs` in substance if not in size: the draft scope named one line, and reading the module found the same claim in a docstring that explains it, plus the fact that **nothing in the suite had ever read the clause that went false**. So the output is a reworded line, a corrected docstring and a test that reads the citation — proved by failing against the old wording, not by passing against the new. `low` was right about the stakes and wrong about what the work was. |
