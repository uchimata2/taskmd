---
id: T-097
title: Decide whether a published document may point at a file no clone receives
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-013, T-034, T-092, T-094]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, README.md]
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
- [x] The decision is recorded with its rejected alternative, whichever way it goes
- [x] If it is in: a fixture holds a published document linking to a gitignored file and `check`
      reports it, shown failing first
- [x] If it is in: this repository's own published-to-quarantined pointers still pass, or the
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
| 5 | Reverse T-094's test rather than add one beside it: the case it asserts is now the case that must be reported. Add the two shapes that must stay silent — a link to a directory, and a link to an ordinary published file. | `tests/test_cli.py`, in T-094's own class. |
| 6 | Report the class in `check_links`, reusing the `visible` set it already computes, and only when the target is a **file**. | `plugin/skills/taskmd/taskmd/cli.py` `check_links`. |
| 7 | Pin the no-git branch: with `visible` unavailable the class cannot be claimed, the same way the document side already declines. | A case in `tests/test_cli.py`, with no git skip-guard — it must hold on a machine that has none. |
| 8 | Say what the class is where an adopter meets the rest of them, and annotate the reversal where the decision was recorded. | `README.md`; `tasks/T-094-...md` §3. |
| 9 | Run the affected modules, and `check` on this repository, which must stay at exit 0 — the measurement's claim, re-made by the shipped rule instead of by the probe. | Recorded output in §3. |

*Steps 5–9 were written at step 4, once the maintainer's answer had decided the branch. Steps 1–4
are as first written. Two alternatives were discarded here: the out-branch table, never drafted for
the reason the note above gives; and a committed fixture directory, which **cannot exist** — its
defect is a gitignored file, so this repository's own `.gitignore` would govern it and a clone would
not receive the thing under test. `ScratchProject` in `tests/test_cli.py` exists for exactly that,
and T-094 built it for exactly that.*

## 3. Implement

**Decided in** — by the maintainer on 2026-08-11, on the measurement below, which is why steps 1–4
are recorded before the change rather than as its justification.

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

**The answer, and what it cost.** *In* — asked with the measurement and the reversal both stated,
answered by the maintainer on 2026-08-11. So the class ships as `IGNORED LINK`, a **problem** rather
than an advisory; the third option offered, reporting it the way `CONFIG DRIFT` is reported with the
exit status unmoved, was rejected with the other. The probe was never committed: it decided the
question and the shipped rule replaces it, which is why step 1 put it in a scratchpad.

**Evidence — the validator failing on the case it is for**, on a scratch project holding all three
shapes in one document: a link to a gitignored file, a link to a published file, and a link to a
gitignored directory.

```
IGNORED LINK  docs/guide.md -> ../private/local.md is here but no clone receives it, so the link
resolves for you and 404s for every reader

1 problem(s) - 1 task(s), 5 field value(s), 0 reference(s), 0 dependency edge(s),
0 declared output(s), 0 index file(s), 3 document(s), 3 link(s), ...
Scope  1 document(s) not read: a clone would not receive them
exit=1
```

Three links read, one reported — so the rule is not simply firing on everything, which is the way a
membership test fails while looking correct on the tree that motivated it.

**And on this repository, with the rule live rather than as a probe:**

```
OK - 123 task(s), ..., 151 document(s), 1205 link(s), ...
Scope  45 document(s) not read: a clone would not receive them
```

Exit 0. That is the measurement's central claim re-made by the shipped code: the class exists, it
is enforced, and this project does not commit it.

**Decisions & assumptions**
- **`IGNORED LINK`, not a widening of `BROKEN LINK`** — 2026-08-11, as §1's scope required. The
  file is *there*; a reader told their link is broken would go looking for a missing file and find
  one. The two have different fixes — publish it, or stop pointing at it — and one label cannot
  carry both.
- **Directories are exempt by testing `os.path.isfile`, not by special-casing the message** —
  2026-08-11. `git ls-files` lists files, so a directory is in nobody's visible set whether or not a
  clone receives its contents; without this the rule is 100% false positives here.
- **The no-git branch inherits the document side's answer rather than restating it** — 2026-08-11.
  `visible is not None` guards the class, so a project without version control is not told that a
  file it can see is unpublished. Its test carries no `skipUnless`, deliberately: it is the branch
  for a machine with no git, and guarding it with git would be the one shape that never runs where
  it matters.
- **T-094's test was replaced, not left beside a new one** — 2026-08-11. It asserted the exact
  behaviour now reversed, so keeping it would have meant asserting both. The reversal is annotated
  in T-094 §3 where the decision lives.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_links`
- `tests/test_cli.py` — the reversed case plus three new ones
- `README.md` — *Which documents `check` reads, and which pointers in them*
- `tasks/T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md` — the annotation

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative, whichever way it goes | met | §3 *The answer, and what it cost* — *out*, and the advisory third option, both named. The reversal is annotated in [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) §3, where the decision it overturns lives, rather than only here. |
| If it is in: a fixture holds a published document linking to a gitignored file and `check` reports it, shown failing first | met, by a different vehicle | Not a committed fixture — one cannot exist, because its defect is a gitignored file and this repository's `.gitignore` would govern it. `ScratchProject` builds it with a real `git init`; output in §3. *Shown failing first* is satisfied twice over: the case is exactly what T-094's now-replaced test asserted **passing**. |
| If it is in: this repository's own published-to-quarantined pointers still pass, or the convention is changed deliberately and `CLAUDE.md` says so | met | `check` exit 0 on 123 tasks and 1205 links with the rule live. The convention needed no change and `CLAUDE.md` needed no edit — §3's measurement says why: it is carried by bare paths in prose, which are out of scope by T-092. |
| If it is out: the adopter-facing documentation says so where it already says what `check` reads | n/a | It is in. The same section of `README.md` was updated for the branch that was taken; the criterion's branch was not skipped, it was not reached. |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-11 | → done | Three criteria met, the fourth closed by its branch not being taken. **The maintainer answered *in* the same day, so the pause at `implement` cost one turn rather than a session** — and the pause is the part worth keeping: the measurement was complete and committed before the question was asked, so the answer had evidence under it rather than an argument. `check` reports `IGNORED LINK`; this repository stays exit 0 with the rule live, which is the measurement re-made by the shipped code. **The `plugin/` subtree moved**, so this joins the manifest batch, and it is the second change in it that can turn a *passing* adopter tree red — the first being T-032's template class. Worth naming when the bump is finally spent. |
| 2026-08-11 | → in_progress | Run under the standing v0.2 full-lifecycle authorization, given by the maintainer on 2026-08-10, re-confirmed and widened on 2026-08-11 to *multiple tasks, full lifecycle, until you need to stop*. `specify` needed no owner turn — the criteria were already written and branch on the answer — but one premise had expired and is annotated in §1 rather than rewritten: the pre-publish grep moved to `docs/PUBLISHING.md` §6 by T-047, before this task was raised, and what the sentence asserts about that grep is unchanged. **The authorization does not reach step 4.** It covers running the lifecycle, not overturning a decision another task recorded and tested; §3 says why this is that. Stopped at `implement` with the measurement done and nothing in the tool touched, which is the state that costs least whichever way the answer goes. |
| 2026-08-10 | → proposed | Raised at T-094's review as the alternative it rejected, rather than dropped with the rejection. `medium` and `s`: the set of published files is already computed once per run, so the mechanism is nearly free — what is not free is the rule, because the obvious strict version forbids a convention this project relies on and the obvious lenient version is what it does today. |
