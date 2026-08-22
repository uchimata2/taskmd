---
id: T-202
title: Mark a fixture's quiet cases so a sweep can find them
type: deliverable
status: specified
phase: specify
parent: T-198
blocked_by: []
related: [T-197, T-151, T-134]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-202 — Mark a fixture's quiet cases so a sweep can find them

## 1. Specify

**Outcome**
The cases a fixture carries **in order to stay silent** are marked in the fixture itself, so the set
can be read from the tree rather than from prose — and a quiet case added tomorrow is in the next
sweep with nothing edited anywhere. **The marks are the authority**: `tests/fixtures/README.md`
keeps a short note on why quiet cases exist, points at them, and carries no list of its own (the
owner's answer of 2026-08-22, below).

**Why this one**
Finding **F-2** of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), and it
is the reason that audit's first criterion is **not met**. Two derivations were tried and neither
answers the question:

| Attempt | Found | Why it is the wrong set |
| :--- | ---: | :--- |
| Fixtures named by a must-not-catch assertion, parsed from `tests/test_cli.py` | 21 | Mostly the cross-fixture `fails()` silence. It **misses `abandoned-slot` and `wide-table-row`**, whose quiet tests iterate the fixture directory or build a tree, so no fixture name appears as a literal |
| `tests/fixtures/README.md`, which names five fixtures shaped to carry their own quiet cases | 5 | Prose. A classification somebody wrote, not a fact the tree states |

**So the set that matters is the one nothing can compute.** T-198 examined the five, and it examined
them because a document said so. A sixth fixture given a quiet case next week appears in neither
derivation, and the audit that was supposed to catch exactly that would not see it.

**The mechanism already exists in this repository, twice.** `leak-check` marks its own lines with
`CAUGHT` and `IGNORED`, and `tests/test_publishing.py` reads them to prove the pattern fires on one
and not the other — a fixture stating its own expectations. `<!-- taskmd:… -->` marked regions
([T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md)) are the same idea
for prose. Neither is applied here.

**This is the same class as [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md), one level down.** That
task removed a hand-typed list of check classes. This removes a hand-written list of quiet cases. Both
are a set the tree owns, described somewhere else.

**Scope**
- In: how a quiet case declares itself — a marker, a naming convention, or a manifest the fixture
  carries
- In: applying it to the quiet cases carried by the five fixtures `tests/fixtures/README.md` names
  **today** — that document is where the set is read from now and stops being its home — and to
  `leak-check`, whose markers may already be the answer generalised
- In: a test that reads the marks, so the set is exercised rather than merely readable
- Out: **repairing any quiet case the marks then expose.** Each is its own finding, as
  [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) is
- Out: the cross-fixture silence assertion, which is
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)'s and is closed

**Inputs**
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) §3 — the two failed
  derivations and what each missed
- `tests/fixtures/leak-check/` and its reader in `tests/test_publishing.py` — the mechanism to
  generalise or reject
- `tests/fixtures/README.md` — the prose the marks would replace as the authority

**Acceptance criteria**
- [ ] The quiet-case set is read from the tree, and the reading is shown
- [ ] **The reading answers to what [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)
      *names*, not to what it exercised.** That audit exercised fifteen cases and its record names
      more: `malformed-date`'s `keep-me`, `section-reference`'s two unmutated marks, and
      `wide-table-row`'s short row — the last of which
      [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) had to add after
      the fact. The two counts are stated together and any difference is explained, so a reading
      that reproduces the fifteen and drops the rest fails here
- [ ] **A quiet case added to a fixture with nothing else edited appears in the reading**, shown by
      adding one and quoting the result
- [ ] **A mark that names a case the check cannot reach fails**, shown by breaking one on purpose —
      otherwise this ships the same silence it is removing
- [ ] `tests/fixtures/README.md` states **why** quiet cases exist and points at the marks; it names
      no fixture's cases and carries no list, so nothing is left there to go stale

**Open questions**
- ~~**Does this replace the prose in `tests/fixtures/README.md`, or sit beside it?** The README is
  read by a person deciding where to add a fixture, and a marker is read by a test. Both may be
  wanted, and then the question is which is authoritative — the maintainer's, at `specify`.~~ **Answered by the owner on 2026-08-22: markers in the fixture are the authoritative list, and the README keeps a short note pointing at them** — see the Log row of that date.
- **None outstanding.** Specify is agreed.

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
| 2026-08-21 | → proposed | Raised as finding F-2 of [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), which is why that audit's first criterion is not met. `medium` and `s`: the mechanism exists twice in this repository already, and what it buys is that the audit above becomes repeatable instead of being a reading of a document. A child of T-198, which does not close until this resolves (`audit.md` step 5). |
| 2026-08-22 | (no change) | **The open question is answered by the owner: the markers are authoritative, and `tests/fixtures/README.md` keeps a short note on why quiet cases exist that points at them.** Asked in the batched round of 2026-08-22. The set is then read from the tree, so a quiet case added next week is in the next sweep with nothing edited anywhere — which is the whole of F-2. *Rejected: markers only, deleting the prose*, one home and no possible drift, but a marker tells a test what to do and does not tell a newcomer why the case is there. *Rejected: the README stays authoritative*, no change for its existing readers, but the set stays hand-written and the defect this task removes survives. This row is the answer, not authorisation to start. |
| 2026-08-22 | → specified | **Specify agreed.** The owner's answer of the same date is folded into the outcome, the scope and the last criterion, so the record states the decision where the work is judged rather than only where it was asked. **One criterion is sharpened rather than restated.** It read *finds every case T-198 examined by hand*, and that audit's record **names more cases than it exercised** — fifteen exercised, beside `keep-me`, `section-reference`'s two unmutated marks and `wide-table-row`'s short row, the last of which [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) had to add after the fact. A marking that reproduced the fifteen would have passed the old wording while dropping exactly the cases this task exists to make findable. **No total is written into the criteria**: a count derived by hand here would be this task's own defect one level up, so the criterion names the set by rule and asks for the two counts to be stated together. Phase stays at `specify` — `plan` is not authorised (METHOD §3.1). **A finding raised while checking those counts is [T-210](T-210-account-for-the-two-derived-fixtures-t-198-s-partition-drops.md)**, and it is why the criterion above could not simply cite T-198's figures. |
