---
id: T-192
title: Require every binding to declare its validator coverage
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-178, T-009, T-139]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-19
updated: 2026-08-21
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/BINDING.md, plugin/skills/taskmd/docs/bindings/github-issues.md, plugin/skills/taskmd/docs/bindings/local-markdown.md, tests/test_publishing.py]
---

# T-192 — Require every binding to declare its validator coverage

## 1. Specify

**Outcome**
The binding contract requires each binding to state which of the validator's checks its backend
covers, which cannot occur there, and which still run locally — and both shipped bindings satisfy it.

**Why this one**
From the owner's answer of 2026-08-19 on
[T-178](T-178-give-the-github-binding-a-standing-verification.md), in their own words: today the
backend is GitHub, tomorrow it may be Notion or another service, so what ships must be flexible, and
the coverage belongs to whichever backend is in use rather than being rows written once about
GitHub.

**T-178 shipped the GitHub half and deliberately left this out**, because making the contract
*require* something changes what every binding must satisfy — including
`plugin/skills/taskmd/docs/bindings/local-markdown.md`, whose honest answer is *all of them, it is
the backend the validator was written for*. That is a different deliverable with a different blast
radius, and folding it into a paragraph in one binding is how a contract quietly gains a clause
nobody reviewed.

**The interesting half is not the requirement, it is what the requirement is allowed to be.** A
contract clause saying *list your coverage* produces a hand-kept list of a set the code owns in every
binding anybody ever writes — which is the class
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) exists to
catch, multiplied by the number of bindings. T-178's own table says so about itself. So the question
this task must answer is whether the declaration can be made checkable, or whether the contract
should ask for something coarser that cannot go stale.

**Requirements served**
R-9 and R-10 (`docs/SCOPE.md`) — the backend contract, and a binding being a document rather than
code.

**Scope**
- In: the contract clause in `plugin/skills/taskmd/docs/BINDING.md`
- In: both shipped bindings brought into line with it
- In: whether the declaration is checkable, and by what — including the answer *it is not, and here
  is the coarser thing we ask for instead*
- Out: writing the GitHub table. [T-178](T-178-give-the-github-binding-a-standing-verification.md)
  did that, and this task may reshape it but does not re-derive it
- Out: adding any check to the validator
- Out: a third binding. If the clause needs a third to be tested, that is a finding rather than a
  licence to write one

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 — what a binding must state today
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *What this does not cover, and why*, the
  first instance, and its two stated weaknesses
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the binding whose answer is trivial, and
  therefore the one that shows whether the clause is worth its cost
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) — the
  marked-list mechanism, and its stated boundary

**Acceptance criteria**
- [ ] `BINDING.md` states the requirement, in the register the rest of that document uses
- [ ] Both shipped bindings satisfy it, and the local one's answer is written out rather than
      assumed obvious
- [ ] The task states whether the declaration can be checked mechanically, with the reason — and if
      it can, the check exists and has been shown to fail
- [ ] **The clause is tested against a binding that does not exist yet**: someone writes what a
      Notion-shaped or issue-tracker-shaped binding would put there, from the clause alone. A
      contract clause proven only by the two bindings written before it is proven by its own examples
- [ ] Whether the requirement makes an existing binding's text redundant is answered, so the contract
      does not ask for a second copy of something a binding already says

**Open questions**
- ~~**Is a hand-kept coverage list worth having at all?**~~ **Answered 2026-08-19: no, and the
  contract asks for the coarser statement.** Each binding says which checks **cannot** occur on its
  backend, and that the rest either apply or still run locally. The per-check table was offered as
  the alternative and rejected: it is a hand-written copy of a set the code owns, so a single new
  check falsifies every binding's table at once —
  [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s class
  multiplied by the number of bindings anybody ever writes. The coarser clause is stable under a new
  check **by construction**, because a new check falls under *the rest* with nobody editing
  anything. What the clause asks for is therefore settled; how it is worded is still this task's
  work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Word the clause and put it in `BINDING.md` §4 — a row in the *Must state* table and a short paragraph saying why it asks for what **cannot occur** rather than for a coverage table. | The edited §4. |
| 2 | Decide what a machine can and cannot check about such a declaration, separating the **substance** (is the classification true of that backend?) from the **hygiene** (does the binding say it, and are the classes it names real?). | A recorded decision, and the answer criterion 3 asks for. |
| 3 | Build the hygiene check where the repository already checks marked prose against a set the code owns, and **make it fail on purpose**. | A test in `tests/test_publishing.py`, and the failure output quoted in §3. |
| 4 | Bring both shipped bindings into line, the local one's answer written out rather than treated as obvious. | The edited `github-issues.md` and `local-markdown.md`. |
| 5 | Test the clause against a backend neither binding was written from: write what a Notion-shaped binding would put there, **from the clause alone**, and record who wrote it and what that is worth. | The fragment, and an honest statement of its limit. |
| 6 | Answer whether the clause makes any existing binding text redundant. | A verdict on `github-issues.md`'s *What this does not cover, and why*. |

**Sequencing.** Step 2 before step 3, because building the check first would decide the question by
what was easy to build. Step 5 after step 4 but written without re-reading either binding, so the
fragment is produced from the clause rather than copied from an example — that is the whole of what
criterion 4 buys, and doing it in the other order destroys it.

**Decisions**

- **The check goes in `tests/test_publishing.py`, not in the validator.** §1's *Out* forbids adding a
  check to the validator, and the class is not a project's defect anyway: a binding is this
  repository's shipped document, so the drift belongs to this repository's suite.
  *Rejected:* a `check` class, which would make every adopting project run a rule about documents
  only this repository ships.
- **The problem-class set is derived in that test file, and the derivation is the first of its kind.**
  `ADVISORY_PREFIXES` is already read from the module; the problem prefixes are not read anywhere.
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) needs the same
  derivation and is told to reuse this one rather than write a second.

**Outputs**

- `plugin/skills/taskmd/docs/BINDING.md`
- `plugin/skills/taskmd/docs/bindings/github-issues.md`
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`
- `tests/test_publishing.py`
- `tasks/T-192-require-every-binding-to-declare-its-validator-coverage.md` (§3, the Notion fragment)

## 3. Implement

### Step 1 — the clause

`BINDING.md` §4 gains a row in *Must state* and a subsection, `The coverage a binding declares, and
why it is stated the short way`. It asks for the exceptions and says why: a per-check table is a
hand-written copy of a set the code owns, so one new check falsifies every binding's table at once,
in every binding anybody ever writes. A class nobody has classified falls under *the rest* and
nothing needs editing.

### Step 2 — what a machine can check about a declaration like this

**The substance cannot be checked and the hygiene can, and the clause says which is which.**

- **Substance** — *is it true that this class cannot occur here?* That is a fact about a hosting
  service. Nothing running locally knows it, and no amount of parsing will. It is reviewed by a
  person, and the contract says so rather than implying the check settles more than it does.
- **Hygiene** — *does the binding carry the statement, and are the classes it names classes the
  validator reports?* Both are checkable, and the second is the staleness a hand-kept list dies of.

### Step 3 — the check, and both its failures

`tests/test_publishing.py` gains `EveryBindingDeclaresWhatCannotOccur`, using the marked-region
machinery that file already has, over a `taskmd:cannot-occur` region. The binding set is read from
the directory, so a third binding is covered with nothing edited.

Removing the region from one binding:

```text
AssertionError: Lists differ: [] != ['plugin/skills/taskmd/docs/bindings/local-markdown.md']
  ... carries no taskmd:cannot-occur region, so BINDING.md section 4 asks it for a statement it
  does not make
```

Renaming one class the GitHub binding declares, from `STALE INDEX` to `STALE FOLDER`:

```text
AssertionError: Lists differ: [] != ['plugin/skills/taskmd/docs/bindings/github-issues.md names `STALE FOLDER`']
  a binding declares a class the validator does not report, so the declaration has drifted from the
  code it is about:
    plugin/skills/taskmd/docs/bindings/github-issues.md names `STALE FOLDER`
```

Both edits reverted; the file's 17 tests pass.

**A third test guards the two above from passing vacuously.** `check_classes()` derives the set the
comparison rests on, and a derivation that silently returned too much would make
*every class named is one the validator reports* pass by construction — the shape T-191 met in its
own instrument the same day. So the derivation is held against four classes the shipped bindings
actually name, and against a floor on the size of the set.

### Step 4 — both shipped bindings

- **`github-issues.md`**: four classes named as impossible — `DUPLICATE ID`, `ID WIDTH`,
  `PARKED TASK`, `STALE INDEX` — in a marked region above the existing table, with one sentence
  saying the table below is the binding's own detail rather than the contract's requirement.
- **`local-markdown.md`**: a new section whose answer is **nothing**, written out class by class
  rather than left obvious, because it is the baseline every other binding's list is a subtraction
  from — and because a reader has to be able to tell an answer somebody gave from a section somebody
  forgot.

### Step 5 — the clause tested against a binding that does not exist

Written from the clause, for a Notion-shaped backend — pages in a database, properties, relations:

```text
<!-- taskmd:cannot-occur -->
**Two classes cannot occur here.** `STALE INDEX` cannot, because a database view is computed from
the pages in the database and there is no materialised file to fall behind. `PARKED TASK` cannot,
because a database has no folders - a page is in it or it is not, and there is nowhere for one to
sit unread.

**`DUPLICATE ID` and `ID WIDTH` can occur here, which is the answer most people expect to be the
other way round.** Notion allocates a page id, but this binding does not use it as the task id: a
page id is a UUID, and the schema's `id_prefix` and `id_width` describe a human id kept as a
database property. That property is typed by whoever writes it, so both classes apply exactly as
they do on files.

**The rest either apply here or still run locally** - the document checks walk the project's own
working tree, which a project on this backend still has.
<!-- taskmd:end-cannot-occur -->
```

**It found a defect in the clause, which is what it was for.** The row said *cannot occur on this
backend*, and the fragment above cannot be written from that: Notion allocates an identifier exactly
as GitHub does, and the two answer **differently** on `DUPLICATE ID` — because GitHub's binding maps
the task id onto the issue number and this one keeps a human id in a property. **It is the mapping
that decides, not the service.** A binding author reading the original row would have got that
backwards in the direction that costs an adopter a check they still needed. The row and the paragraph
were reworded to say so, carrying this fragment's evidence.

**What this test is worth, stated rather than implied.** It was written by the author of the clause,
in a session that had already read both shipped bindings. So it tests whether the clause is
**sufficient to write a fragment from** — and it failed that, usefully. It does **not** test whether
somebody who has never seen either binding reads the clause the same way, which is the stronger
thing criterion 4's wording gestures at. That stronger test needs a reader who is not the author, is
the same instrument
[T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) waits on, and is not
something a session can stand in for.

### Step 6 — what the clause made redundant

**It made two rows of `github-issues.md`'s table redundant, and they were removed.** That table
carried *duplicate id, id width, parked task — Cannot occur* and *stale index — Cannot occur*, which
is exactly what the new marked region now states. Leaving both would have been the contract creating
a second copy of a fact on its first day, in the document that argues hardest against hand-kept
lists. The table's introduction now says the four are above and not repeated, and the table is what
it was always most useful as: where each of the **remaining** checks went.

Nothing in `local-markdown.md` was made redundant — it had no coverage statement at all, which is
what step 4 fixed.

**Decisions & assumptions**

- **The clause asks for what cannot occur *under this binding's mapping*, not *on this backend* —
  rationale: the Notion fragment could not be written from the original wording, because two
  bindings over services that both allocate identifiers answer differently on the same class.**
  Rejected: keeping *on this backend* and adding a footnote, which leaves the row itself misleading
  to anyone who reads only the table — 2026-08-21.
- **The check lives in `tests/test_publishing.py`, not in the validator — rationale: §1's *Out*
  forbids adding a validator check, and a binding is this repository's shipped document, so the
  drift is this suite's to catch.** Rejected: a `check` class, which would make every adopting
  project run a rule about documents only this repository ships — 2026-08-21.
- **`check_classes()` derives the problem prefixes from `cli.py`'s source, and is the first
  derivation of that half in the suite.** `tests/test_cli.py`'s `LABELS` is the transcribed copy
  [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) exists to remove; that
  task reuses this function rather than writing a third — recorded in its own §1 as well as here,
  because a note kept only here is one it will not see — 2026-08-21.

**Outputs produced**

- `plugin/skills/taskmd/docs/BINDING.md`
- `plugin/skills/taskmd/docs/bindings/github-issues.md`
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`
- `tests/test_publishing.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `BINDING.md` states the requirement, in the register the rest of that document uses | met | A row in §4's *Must state* table, whose *Why it bites* column says what an adopter loses, plus a subsection arguing the short form. Both follow §4's existing shape: a claim, then what goes wrong without it |
| Both shipped bindings satisfy it, and the local one's answer is written out rather than assumed obvious | met | `github-issues.md` names four; `local-markdown.md` says **nothing**, class by class, with a sentence on why that is worth writing — a reader has to be able to tell an answer somebody gave from a section somebody forgot, and it is the baseline every other binding subtracts from |
| The task states whether the declaration can be checked mechanically, with the reason — and if it can, the check exists and has been shown to fail | met | Split in §3 step 2: the **substance** cannot — whether a class truly cannot occur on a hosting service is a fact nothing running locally knows — and the **hygiene** can. The hygiene check exists and was made to fail twice, both outputs quoted: a binding with the region removed, and a binding renaming `STALE INDEX` to `STALE FOLDER`. A third test stops the first two passing vacuously if the derivation ever returns too much |
| **The clause is tested against a binding that does not exist yet** | met | The Notion fragment in §3 step 5, written from the clause, **and it found the clause wrong** — *cannot occur on this backend* cannot be answered, because it is the binding's mapping and not the service that decides `DUPLICATE ID`. Row and paragraph reworded, carrying that evidence. The limit is stated in §3: the author wrote it, having read both bindings → **[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)** for the reader who has not |
| Whether the requirement makes an existing binding's text redundant is answered, so the contract does not ask for a second copy of something a binding already says | met | **Yes, and the copy was removed.** Two rows of `github-issues.md`'s table said exactly what the new region says; leaving both would have had the contract create a duplicate on its first day, in the document that argues hardest against hand-kept lists. The table's introduction now says the four are above, and the table is what it is most useful as: where each of the remaining checks went |

**The clause was wrong when it was first written, and the criterion that found it is the one that
looked like ceremony.** Writing a fragment for a backend nobody has bound is easy to read as
box-ticking next to shipping the contract text. It changed the contract, in the direction that would
otherwise have cost an adopter a check they still needed — and it is the one criterion the two
shipped bindings could not have caught, because both happen to map identity the same way.

**Open questions, re-read before closing.** §1's one question was answered by the owner on 2026-08-19
and is struck through. §3 leaves one thing nobody here can settle — an uninvolved reader — and it is
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) rather than
a sentence in this record, because views read open work and this task is closing.
[T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) was told in its own §1
to reuse `check_classes()`, so that note does not depend on anyone re-reading this one.

**Why this task closes and T-191 did not.** Both raised children today. `audit.md` step 5 gates an
**audit's** umbrella on its children, because an audit's product is the traceability from
examination to consequence. This is a `deliverable`: its outcome exists, every criterion is met, and
T-199 is a stronger test of a clause that already works rather than a gap in it.

**Child fix tasks raised**
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) — the uninvolved reader

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Five criteria met, one child raised.** The clause asks what cannot occur **under a binding's mapping** - reworded from *on this backend* because the criterion-4 fragment could not be written from the original, two identifier-allocating services answering differently on `DUPLICATE ID`. Hygiene is checked and was made to fail twice; the substance is a person's, and the contract says so. Two rows of the GitHub table were removed as the duplicate the clause created. [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) carries the reader who has not seen the examples. |
| 2026-08-19 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-19, and not yet acted on.** The owner granted a later session the four tasks that need nobody else - T-193, T-190, T-191 and T-192 - **each through its full lifecycle, committed and pushed**. It is written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)), and an authorisation kept only there is one the session after next cannot find. **It reaches these four and no others**: the remaining open tasks each wait on a person, an external event, or a question still the owner's. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round: the coarser statement.** A binding declares what cannot occur on its backend, not a per-check coverage table; the table was offered and rejected as a hand-kept copy of a set the code owns. This settles what the clause asks for and leaves its wording to this task. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-178](T-178-give-the-github-binding-a-standing-verification.md) raised it. **It does not answer §1's question**, which decides what the clause asks for and is a judgement about a contract every future binding inherits. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-178](T-178-give-the-github-binding-a-standing-verification.md)'s `specify`, carrying the widening the owner attached to that task's answer. Kept out of T-178 on purpose: a clause in the contract is satisfied by every binding that exists and every one that ever will, and T-178's outcome is one document. `m` because the fourth criterion needs somebody to write a binding fragment that does not exist. |
