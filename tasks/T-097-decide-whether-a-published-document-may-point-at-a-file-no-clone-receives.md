---
id: T-097
title: Decide whether a published document may point at a file no clone receives
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-013, T-034, T-092, T-094]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-097 — Decide whether a published document may point at a file no clone receives

## 1. Specify

**Outcome**
`check` states whether a link from a document a clone *does* receive to a file it *does not* is a
problem, and behaves accordingly — so a project cannot publish a front page whose links 404 for
everyone but its author, and cannot be told off for naming where its local-only material lives.

**Why this one**
[T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) split the question `check`
answers across the two sides of a link: documents are judged by what a clone would receive, targets
by what is on disk. The asymmetry is deliberate and is argued there. What it leaves open is the class
the strict reading would have caught, and that class is real: a `README.md` linking to a gitignored
file resolves perfectly on the author's machine and is broken for every reader.

**Nothing detects it today, in either check.** `check` resolves the target against the filesystem, so
it passes. The pre-publish grep in `CLAUDE.md` looks for leaked identifiers, not for pointers. The
gap is therefore not a narrowing introduced by T-094 — it predates it — but T-094 is where it became
a decision rather than an oversight.

**The tension to resolve, and it is why this is not obvious.** Quarantining local-only material
behind `.gitignore` (T-013) requires the tracked tree to refer to that material by name; the
convention exists precisely so a published document can say "this lives in the file that is not
here". A rule that reports every published-to-ignored pointer forbids the convention. A rule that
reports none permits the 404. The decision is where the line goes, and whether it can be drawn
without a project having to annotate its links.

**Requirements served**
R-16.

**Scope**
- In: whether the class is reported at all, and under what label — it is a new problem class, not a
  scoping change to `BROKEN LINK`, which is why T-094 declined to absorb it.
- In: how a deliberate pointer at quarantined material is distinguished from an accidental one, if
  it is reported. An opt-out that every project must maintain by hand is a second copy of
  `.gitignore` and should be rejected on that ground alone.
- In: what a project with no git gets, since the class cannot exist without an ignore mechanism.
- Out: bare paths in prose — decided out in
  [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md), and re-opening it here would
  merge two questions that were deliberately separated.
- Out: the document side, which T-094 settled.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `clone_would_receive` and `check_links` — the set this
  decision needs is already computed once per run, so the mechanism is nearly free; the rule is not.
- [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) §3, for the rejection this
  task carries and the reasoning behind the asymmetry.
- [T-013](T-013-quarantine-local-only-information-behind-gitignore.md), for why local-only material is
  quarantined rather than deleted, and what the tracked tree is expected to say about it.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If it is in: a fixture holds a published document linking to a gitignored file and `check`
      reports it, shown failing first
- [ ] If it is in: this repository's own published-to-quarantined pointers still pass, or the
      convention is changed deliberately and `CLAUDE.md` says so
- [ ] If it is out: the adopter-facing documentation says so where it already says what `check` reads

**Open questions**
- **In or out, and if in, how the deliberate case is spelled.** The maintainer's. Note that T-092
  answered a question of this shape by building the rule and measuring it before deciding, which cost
  little and produced a number no argument would have; the same move is available here and this
  repository is again the corpus.

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
| 2026-08-10 | → proposed | Raised at T-094's review as the alternative it rejected, rather than dropped with the rejection. `medium` and `s`: the set of published files is already computed once per run, so the mechanism is nearly free — what is not free is the rule, because the obvious strict version forbids a convention this project relies on and the obvious lenient version is what it does today. |
