---
id: T-226
title: Decide whether taskmd should print the class list a binding author needs
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-222, T-197, T-191]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-226 — Decide whether taskmd should print the class list a binding author needs

## 1. Specify

**Outcome**
An answer, recorded, on whether taskmd gains a way to print the set of classes `check` can report —
and if so, what shape it takes.

**Why this one**
`BINDING.md` §4 requires a binding to name the classes its mapping makes impossible, in the
validator's own names. **Nothing an adopter installs tells them what those names are.** The set has
one home and it is source code — the literal at each `problems.append` site and the
`ADVISORY_PREFIXES` constant, both in `taskmd/cli.py`. On 2026-08-22
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md) repaired the
clause to say so, which is honest and is not the same as reachable: it asks a binding author to read
Python to write Markdown.

**The alternative is not a document.** A list written into any document is the per-check coverage
table §4 refuses, with its second column removed — falsified by the same event, and one class was
added to this validator on 2026-08-22. So the only shapes that do not re-create the defect are ones
that **derive** the set: a command that prints it, or nothing.

**Scope**
- In: whether to add it, and if yes its shape — a subcommand, a flag on `check`, or something else
- In: what it costs. A fifth command is adopter-visible surface and this project has kept to four
- In: whether `tests/classes.py`'s derivation moves into the package or stays in `tests/`. It is the
  derivation that exists; a command would need one, and two would be the defect T-191 found
- Out: building it. This task answers whether and what shape; the build is its own task if the answer
  is yes
- Out: changing what the classes are

**Inputs**
- `tests/classes.py` — the derivation that exists today, and its recorded reasons
- `plugin/skills/taskmd/taskmd/cli.py` — the two places the names live
- `plugin/skills/taskmd/docs/BINDING.md` §4 *Where the class names come from* — the clause that
  currently sends a reader to the source

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and the rejected shapes are named
- [ ] If the answer is yes, the shape is specific enough that a build task could start from it
- [ ] Whether the derivation gets one home or two is answered either way — a yes that leaves two
      derivations has re-created T-191

**Open questions**
- ~~**Is a fifth command worth it, against reading two places in `cli.py`?** — the project owner. The
  recommendation is **yes, as `check --classes` rather than a fifth command**: it adds no verb to the
  surface, it sits on the command that owns the classes, and it makes the clause's instruction
  runnable. The cost is one flag and moving the derivation into the package.~~ **Answered by the
  owner on 2026-08-22: yes, as `check --classes`.** See the Log row of that date — this record's
  outcome is that answer, so what is left here is the lifecycle and not the decision.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Answer the third criterion — where the derivation lives once a *shipped* flag needs one — with the placements rejected and why | a recorded decision in §3, naming what it rules out |
| 2 | Write the build task's `specify` **from this record alone**, and keep a list of anything that had to be invented rather than read off it | the new task, plus the list of what was missing |
| 3 | State the shape precisely: how the flag is spelled, what it prints, and what it deliberately does not do | §3, in the same terms a build task would restate |

**Step 2 is the verification, not the paperwork.** This record's outcome is an answer, and
[`implement`](../plugin/skills/taskmd/docs/method/implement.md) says a decision is verified when the
people bound by it can state what it commits them to. The people bound are whoever builds the flag,
so the smallest real use available is to **write their `specify` from this record and see what is
missing**. Anything that has to be invented at that point is a gap in the answer, discovered while it
is still cheap. *Rejected: re-read this record and judge it sufficient* — reading your own answer
cannot surprise you, which is the whole distinction that phase draws.

**Step 1 before step 2, because it can invalidate it.** If the derivation cannot get one home, the
shape changes and the build task is a different task. The ordering rule is *what reduces uncertainty
soonest*, and this is the only step here that could.

**Outputs**

- no file: the answer's home is §3 of this record, and the build task it commits to

## 3. Implement

**Decisions & assumptions**

- **The derivation gets one home, and it is the package — `tests/classes.py` becomes an import**
  — 2026-08-23. This answers the third criterion, and it is **forced rather than chosen**: `tests/`
  sits outside `plugin/`, so an install receives none of it (T-053), and a shipped flag therefore
  cannot import from there. One home plus a shipped flag leaves exactly one arrangement.
  *Rejected: keep the derivation in `tests/` and import it from the flag* — it would work in this
  checkout and fail for every adopter, which is the worst available failure shape because this
  repository is the one place it passes. *Rejected: two derivations, one shipped and one for tests*
  — that is precisely [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md)'s
  defect, re-created in the module written to remove it, whose own docstring says so.
  *Rejected: move it and delete the test-side module* — `tests/test_publishing.py` holds two readers
  against it, `TestTheDerivationCanStillRead` and `TestTheGuardOnTheDerivedSetStillBites`, and a thin
  re-export keeps their imports working while leaving one derivation.
- **The shape, stated to the precision a build needs** — 2026-08-23. `check --classes`, a flag and not
  a fifth verb; it prints the set `check` can report; `CONFIG ERROR` stays out of it, because the
  config loader reports it before any check runs and no binding can declare it and no fixture be
  asserted silent about it. What the flag prints line by line, and whether it also runs the checks,
  are named as open questions on the build rather than settled here — they are output-format choices
  a measurement answers, not part of the decision this record was asked for.
- **The regex-versus-constant question is handed on, not decided** — 2026-08-23. `tests/classes.py`
  reads the 20 `problems.append` literals out of the source because giving them a constant *"would
  change `cli.py` at every append site, which is a plugin change with adopter reach and is out of
  T-197's scope"*. **That reason has expired**: the build is a plugin change. It is recorded as the
  build's first open question with a recommendation and its cost, because answering it here would be
  deciding a build detail from a decision record, and the measurement that settles it belongs to the
  build.

**Outputs produced**

- the answer above, and
  [T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md)

**Verification**

**By use, and the use was writing the build's `specify` from this record alone** — a decision is
verified when the people bound by it can state what it commits them to, and the people bound are
whoever builds the flag. Reading this record back would have proved nothing.

**What the set actually is, measured rather than assumed**, since the answer commits to printing it:

```text
python -c "import sys; sys.path.insert(0,'tests'); import classes; ..."
22 classes: ABANDONED SLOT, BROKEN LINK, CLOSED PARENT, CONFIG DRIFT, CYCLE, DANGLING,
DUPLICATE ID, DUPLICATE INDEX, ID WIDTH, IGNORED LINK, LABEL SHAPE, MALFORMED DATE,
MISSING OUTPUT, NO BLOCKER, PARKED TASK, SECTION REF, STALE INDEX, STORED DERIVED,
TEMPLATE FIELD, TEMPLATE UNREACHABLE, VOCABULARY, WIDE ROW
```

`grep -c 'problems\.append(' cli.py` returns **20**, against 22 classes — the difference being the
advisories, which come from `ADVISORY_PREFIXES` rather than from an append site. That pair of figures
is what makes the regex-versus-constant question concrete rather than rhetorical.

**Four things had to be invented while writing
[T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md), and they
are this step's result.** They are recorded as that record's open questions, not repeated here:
whether the shipped derivation keeps the regex or the 20 sites gain a constant; **whether a runtime
source-read works from an installed copy at all**; what the flag prints line by line; and whether it
still runs the checks. **The second is the one worth the exercise.** The derivation opens
`cli.__file__` and has only ever run from a checkout; nothing in this record, in T-197 or in
`tests/classes.py` had considered that shipping it means running it from an install, where the
question is no longer hypothetical. It is T-236's first acceptance criterion for that reason.

**None of the four sent anything back to this record**, which is what *could start from it* asks for.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded with its reason, and the rejected shapes are named | met | The owner's answer and its three rejected shapes are in the Log row of 2026-08-22 — a fifth command, nothing, and a list in a document. §3 adds the three rejected *placements* for the derivation, which is the same criterion applied to the part the owner's answer did not reach |
| If the answer is yes, the shape is specific enough that a build task could start from it | met | Tested rather than judged: [T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md) was written from this record alone and has a scope, inputs, six criteria and four questions. **Four things had to be invented, and none of them came back here** — all four are output-format or measurement questions belonging to the build, which is what *could start from it* means. Had one of them been *what is the flag for*, this row would read differently |
| Whether the derivation gets one home or two is answered either way — a yes that leaves two derivations has re-created T-191 | met | One home, in the package, with `tests/classes.py` reduced to an import. §3 carries it with three rejected placements. The answer is forced by the plugin boundary rather than preferred: `tests/` is not shipped, so a shipped flag cannot import from it |

**Child fix tasks raised**
- none. [T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md)
  is the build and is **not** a child: this record's outcome is an answer and that answer is complete,
  so a hierarchy edge would hold a finished decision open for as long as the build takes. It is the
  residual case [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4 names, and it carries the
  soft edge from its own `related`, which is the forward direction.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds one and it is struck
through, answered by the owner on 2026-08-22. Nothing here is addressed to anybody else: the four
questions this phase produced are all on T-236, where they are open and visible, rather than left in
a record about to close.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | planned → done | **Closed: three criteria, three met, no child raised.** The decision itself was the owner's on 2026-08-22; what this record added is the part their answer did not reach — **the derivation gets one home and it is the package**, which turns out to be forced rather than chosen, because `tests/` is outside `plugin/` and a shipped flag cannot import from what an install never receives. **The verification was writing [T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md)'s `specify` from this record alone**, and it earned its keep: four things had to be invented, and one of them is that a derivation reading `cli.__file__` has only ever run from a checkout — nobody had asked whether it works from an install, which is the whole point of shipping it. That is now T-236's first acceptance criterion. **None of the four came back to this record**, which is what the second criterion asks. **T-236 is a soft edge and not a child**, so this decision closes rather than waiting out its own build. |
| 2026-08-23 | proposed → planned | **`specify` closed and `plan` written, both under the unattended grant.** `specify` needed nothing added: the one open question was answered by the owner on 2026-08-22, and the three criteria stand as agreed — **including the third, which the answer does not settle and which is this record's remaining work rather than the owner's.** Nothing was widened; the scope's *out* on building it is untouched. **The plan is three steps and its second is the verification** — write the build task's `specify` from this record alone and keep what had to be invented, because a decision is verified when the people bound by it can say what it commits them to, and reading your own answer cannot surprise you. **Step 1 goes first because it can invalidate step 2**: if the derivation cannot get one home, the flag is a different build. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** the decision exists, so what remains is the lifecycle and a build task, not the choice. **Its third criterion is not answered by the decision and is the part with teeth** — a shipped flag needs a derivation in the package, `tests/classes.py` already has one, and two derivations is the defect T-191 found. |
| 2026-08-22 | (no change) | **The owner answers the question this record exists to ask: yes, as `check --classes`.** Answered 2026-08-22. It adds no verb to a surface this project has held at four commands, it sits on the command that owns the classes, and it makes runnable an instruction `BINDING.md` §4 currently gives in the form *go and read `cli.py`*. *Rejected: a fifth command* — adopter-visible surface for something only a binding author needs. *Rejected: nothing, and leave the clause pointing at source* — honest, and it asks somebody to read Python in order to write Markdown. *Rejected: a list in a document* — the per-check coverage table §4 refuses, one column narrower. **The third criterion is not answered by this and is the part with teeth**: the derivation lives in `tests/classes.py`, a shipped flag needs one in the package, and two derivations is the defect T-191 found. **The outcome of this record now exists**, so what remains here is the lifecycle and a build task, not the decision. |
| 2026-08-22 | → proposed | Raised from [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md), whose §1 puts changing the validator out of scope. The repaired clause tells a binding author where the class names live and that place is source code, which is the honest answer and is not a usable one — so the gap is recorded as a decision rather than left as a shrug in a shipped document. `decision` by the schema's own test: the outcome is an answer somebody else could act on, and the change follows from it. |
