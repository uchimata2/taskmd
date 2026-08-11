---
id: T-097
title: Decide whether a published document may point at a file no clone receives
type: fix
status: in_progress
phase: implement
parent: null
blocked_by: []
related: [T-013, T-034, T-092, T-094]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-11
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

> *Read on 2026-08-11:* the pre-publish grep is in `docs/PUBLISHING.md` §6, moved out of `CLAUDE.md`
> by T-047 before this task was raised. The sentence above is left as written because what it
> asserts is unchanged — that check looks for leaked identifiers and not for pointers, so it is not
> the thing that would catch this class. Only its address was wrong.

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

  *2026-08-11: the move was taken and the number is in §3 — zero real alarms, twelve directory
  false alarms, and the convention this rule was feared to forbid turns out not to use links at all.
  The second half of the question answers itself on that evidence: **the deliberate case needs no
  spelling**, because a bare path in prose already expresses it and T-092 put that class out of
  scope. No opt-out, no annotation, no second copy of `.gitignore` — which §1 says should have been
  rejected on that ground anyway. The first half is with the maintainer, because answering it
  reverses T-094 rather than filling a gap it left.*

## 2. Plan

**Planned to the measurement and no further, deliberately.** Step 2's number decides whether this
class is in or out, and the steps after it are different work in each case — inventing them now
would be inventing most of them to be discarded ([`plan`](../plugin/skills/taskmd/docs/method/plan.md),
*Do not plan past the horizon you can actually see*). Step 4 revises this table once the answer is
known.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the rule as a throwaway probe outside the tool: for every document a clone receives, every relative link whose target exists on disk but is not in `clone_would_receive`. Outside, because a rule that turns out to be *out* should leave nothing to remove. | A script under the session scratchpad, not in the repository; its output pasted into §3. |
| 2 | Run it on this repository and read every alarm individually — how many, in which documents, and for each one whether it is the 404 the class is for or the deliberate pointer the convention needs. | A count and a per-alarm verdict in §3. The number T-092 got by this move, for the question of this shape. |
| 3 | Check the two shapes the probe cannot see from the count alone: a link to a **directory** (git lists files, so no directory is ever in the set) and a project with **no git** (the set is `None`, not empty). Both would be false alarms in a rule built straight from step 1. | Named in §3 as handled or as reasons the strict rule cannot ship as written. |
| 4 | Decide in or out, record the rejected alternative, and rewrite steps 5+ of this table for whichever it is. | The decision in §3; this table revised in place. |
| 5 | Write the fixture and watch it fail: a published document linking to a gitignored file, plus the two shapes that must **not** be reported — a link to a directory, and a link to an ordinary published file. | `tests/fixtures/ignored-link/`, and `check --root` on it exiting 0 before the rule exists. |
| 6 | Report the class in `check_links`, reusing the `visible` set it already computes, and only when the target is a **file**. | `plugin/skills/taskmd/taskmd/cli.py` `check_links`. |
| 7 | Pin the no-git branch: with `visible` unavailable the class cannot be claimed, the same way the document side already declines. | A case in `tests/test_cli.py`. |
| 8 | Say what the class is where an adopter meets the rest of them, and record the fixture. | `README.md`, `tests/fixtures/README.md`. |
| 9 | Run the affected modules and `check`/`index` on this repository, which must stay at exit 0. | Recorded output in §3. |

*Steps 5–9 were written at step 4, once the measurement had decided the branch. Steps 1–4 are as
first written. The discarded alternative is the out-branch table, which was never drafted — the
plan's own note above says why.*

## 3. Implement

**Steps 1–3 are done. Step 4 — the decision — is with the maintainer**, for the reason under
*Why this needs an owner turn* below. Nothing has been changed in the tool.

**The measurement (steps 1–2).** The strict rule, run over this repository as a probe outside the
tool: 151 documents a clone receives, every relative Markdown link whose target exists on disk but
is not in `clone_would_receive`.

```
documents read: 151
alarms: 12
  DIR    CLAUDE.md                       -> plugin/skills/taskmd/docs/method/
  DIR    README.md                       -> plugin/skills/taskmd
  DIR    README.md                       -> plugin/skills/taskmd/docs/bindings
  DIR    plugin/skills/taskmd/SKILL.md   -> docs/bindings/
  DIR    plugin/skills/taskmd/adopt.md   -> docs/bindings/
  DIR    plugin/skills/taskmd/docs/BINDING.md -> bindings/
  DIR    tasks/T-001-...md               -> ../tests/fixtures/alt-project
  DIR    tasks/T-003-...md               -> ../plugin/skills/taskmd/docs/method/
  DIR    tasks/T-083-...md               -> ../plugin/skills/taskmd/docs
  DIR    tasks/T-083-...md               -> ../plugin/skills/taskmd/taskmd

directory links (false alarms): 12
FILE links to something no clone receives: 0
```

**Every alarm is a link to a directory, and every one is a false alarm** — `git ls-files` lists
files, so no directory is ever in the set, published or not. Exempt directories and the rule fires
**zero** times on this repository, across 151 documents and ~1200 links. That is step 3's first
shape, and it is not a detail: a rule built straight from step 1 would be 100% false positives here.
Step 3's second shape needs no new answer — with no git the set is `None`, and the document side
already declines to claim anything in that case, so the class inherits that.

**The tension §1 was raised to resolve does not exist** (step 2, the per-alarm verdict). §1 says a
strict rule "forbids the convention" of naming quarantined material from the tracked tree. It does
not: **every reference to `control/LOCAL-CONTEXT.md` in the tracked tree is a bare path in
backticks, not a Markdown link** — 40-odd of them across `docs/`, `CLAUDE.md` and the task records,
and not one is a link. So the convention lives entirely in the class
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) already decided **out**, and the
strict rule would forbid nothing this project does. The two tasks compose in a way neither could see
alone.

**Why this needs an owner turn, rather than the standing authorisation.**
[T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) did not leave this open — it
**decided it**, the other way, and pinned the decision with a test whose docstring names it as the
rejected alternative: `test_a_published_document_may_still_point_at_a_gitignored_one` in
`tests/test_cli.py`. Implementing the class means deleting that test and reversing a recorded
decision. The measurement is evidence that its stated reason no longer holds, not authority to
overturn it; and the change is adopter-visible in the one shape the maintainer has already ruled on
once — a tree that passed yesterday going red. So it is asked rather than assumed.

**Recommendation: in.** It costs nothing here, the mechanism is a single set membership on a set
`check_links` already computes, and the class it catches is a real 404 for every reader but the
author. The rejected alternative is *out* — leave the behaviour and say so in the adopter
documentation — which is defensible only while no project has ever hit the class, and is the
position that quietly expires the first time one does, silently, in the direction of a broken
published link.

**Outputs produced**
- none yet — nothing in the tool has been changed. The probe was written to the session scratchpad
  deliberately, so that deciding *out* would leave nothing to remove.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → in_progress | Run under the standing v0.2 full-lifecycle authorization, given by the maintainer on 2026-08-10, re-confirmed and widened on 2026-08-11 to *multiple tasks, full lifecycle, until you need to stop*. `specify` needed no owner turn — the criteria were already written and branch on the answer — but one premise had expired and is annotated in §1 rather than rewritten: the pre-publish grep moved to `docs/PUBLISHING.md` §6 by T-047, before this task was raised, and what the sentence asserts about that grep is unchanged. **The authorization does not reach step 4.** It covers running the lifecycle, not overturning a decision another task recorded and tested; §3 says why this is that. Stopped at `implement` with the measurement done and nothing in the tool touched, which is the state that costs least whichever way the answer goes. |
| 2026-08-10 | → proposed | Raised at T-094's review as the alternative it rejected, rather than dropped with the rejection. `medium` and `s`: the set of published files is already computed once per run, so the mechanism is nearly free — what is not free is the rule, because the obvious strict version forbids a convention this project relies on and the obvious lenient version is what it does today. |
