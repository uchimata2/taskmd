---
id: T-093
title: Decide whether check resolves a section reference
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-092, T-095]
work_package: M6
owner: maintainer
business_value: medium
effort: l
created: 2026-08-09
updated: 2026-08-19
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, README.md]
---

# T-093 — Decide whether check resolves a section reference

## 1. Specify

**Outcome**
A decision, recorded with its alternative, on whether a citation of the form *document §n* is a
reference `check` resolves — and if so, what binds a mark to a document and what happens to a mark
nothing binds.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`) from the same migration that
produced [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md). Its observation is
sharp and checkable: **taskmd uses the convention throughout its own documentation and cannot check
it.** This repository's prose cites `METHOD §4`, `METHOD §1 rule 5`, `docs/SCOPE.md §9`, `T-011 §1`
and `BINDING.md §4` — including in the source comments of the tool itself. Renumber a section and
every citation of it lies, silently, exactly like a moved file.

That project cites 497 of them and had 1394 unresolved before it built a rule.

**Why it is more than a link check.** A `§n` is a pointer whose target is a number *printed inside
the document it points at*, so it is mechanically resolvable — but only once you know **which**
document a bare `§n` belongs to. The reporting project measured two bindings and recorded the result:
*adjacency* — the document named next to the mark — against *nearest document mentioned in the
paragraph*, and the second picked the wrong target for a third of the misses it reported. That
measurement is the most valuable thing in the report and is the reason this task is `l` rather than
`m`.

**Requirements served**
R-16. R-13 in the same sense as T-092.

**Scope**
- In: whether this belongs in taskmd at all, given the convention is the method's rather than the
  tool's.
- In: if yes — the binding rule, what `§n.m` may resolve against, and the treatment of marks the
  form does not bind. The reporting project **counts and reports those as skipped** rather than
  dropping them, which is the same argument as [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md).
- In: that a `§` inside a code span or fence is literal text — which is what lets a document quote a
  reference that is wrong, and this repository's task records do exactly that.
- Out: renumbering anything, or any opinion on how sections should be numbered.
- Out: bare paths in prose, which is [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md).

**Inputs**
- The reporting project's `tools/docs/refcheck.py`, MIT, with a self-test that rejects `§9.4` and
  `§0.9` while accepting `§5.1` and `§0.8`. Offered as a reference implementation, not a patch.
- This repository's own `§` citations, as the corpus to try any rule against.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative
- [ ] If in: a fixture cites a document at a section it does not have, and `check` reports it, shown
      failing first
- [ ] If in: a mark the rule cannot bind is reported as skipped and counted, never dropped
- [ ] If in: a `§` inside a fence is not resolved, proven by a fixture that quotes a wrong reference
      on purpose
- [ ] If out: the reason is written where an adopter reads it, since taskmd's own documents use the
      convention and a reader will assume it is checked

**Open questions**
- ~~**Whether this is taskmd's job.** It is a documentation-integrity check, not a task-graph check,
  and everything else `check` does is about tasks and their edges. Adding it widens what the tool is
  for. Against that: the method's own documents are the thing most cited by section, and the tool
  already validates Markdown links across the whole tree rather than only in task files. The
  maintainer's.~~ **Answered by the owner on 2026-08-19: yes, it is taskmd's job** — see the Log row
  of that date for the rejected option and its cost.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure the corpus **before designing the rule**: how many marks there are, and what sits beside each one | The shapes and their counts, in §3 |
| 2 | Try each candidate binding against the real section numbers and count what it resolves, misses and cannot bind | The three rules, scored, in §3 |
| 3 | Decide the binding, the sub-number rule, and the reporting shape from those numbers | The decisions, in §3 |
| 4 | Write the check, aggregated one line per document-and-section | `cli.py` |
| 5 | Build a fixture carrying the resolving case, the failing case, the unbound case, the list-item case and two quoted-in-code cases; show the tests failing with the check unwired | The failing run, in §3 |
| 6 | Document the class where an adopter meets the others | `README.md` |
| 7 | Run the suite, `check` and `index` | The output, in §3 |

**Step 1 comes first because the hard part is the rule and the corpus is the only thing that can
settle it.** §1 already says so: the reporting project's measurement of adjacency against proximity
is the most valuable thing in their report, and a rule designed before measuring would be a guess
dressed as a design.

**Decisions taken at `plan`**

- **The rule is measured on this repository before it is written, and the measurement is quoted.**
  This is the corpus §1 names, and it is also the corpus the check must not be noisy on.
  *Rejected: porting the reporting project's `refcheck.py`*, offered as a reference implementation:
  it encodes their conventions, and the point of measuring is to find out whether they are ours.
  — 2026-08-19
- **Aggregate to one line per document-and-section.** *Rejected: one line per citation*, which is
  how a warning becomes something a reader scrolls past. — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/section-reference/
- tests/test_cli.py
- README.md

## 3. Implement

### Step 1 — the corpus, before any rule

**2,916 section marks, in 294 documents**, counted outside code spans and fences. What sits
immediately before each one:

| Beside the mark | Marks |
| :--- | ---: |
| a bare document name (`METHOD §5`) | 365 |
| a code span (`` `docs/SCOPE.md` §9 ``) | 285 |
| a Markdown link | 176 |
| a task id | 140 |
| nothing that names a document | the rest |

**The first probe was wrong, and the corpus said so.** It read the context out of the
`without_code` copy, where the code span holding the document's name has been blanked — so
`` `docs/SCOPE.md` §9 `` looked like an unbound mark, and adjacency scored 66.8% unbound instead of
its real figure. `without_code` blanks character for character, so the fix is to find the mark in
the blanked copy and read what binds it from the original. **That is the single most important line
in the implementation** and it exists because a measurement disagreed with a reading.

### Step 2 — three candidate bindings, scored against real section numbers

| Binding | Resolved | Missed | Bound to nothing |
| :--- | ---: | ---: | ---: |
| adjacency only | 646 | 223 | — |
| adjacency + conjunction (`§3.1 and §3.3`) | 664 | 241 | 2,011 |
| the above + *bind a loose mark to the document it is written in* | 2,193 | 508 | 215 |

**The third rule was tried and rejected, and its numbers are why.** It looks like free coverage: a
bare `§1` in a task record usually does mean that record's §1. But a task record *has* sections 1
to 4, so every `§1`..`§4` meant for METHOD or for a sibling resolves against the wrong document and
comes back **correct**. It bound 1,796 more marks and got 267 of them wrong, and those errors are
invisible by construction — the one failure mode a checker must not have. Adjacency gives up
two thirds of the corpus and reports what it gave up.

*Rejected: proximity — the nearest document mentioned in the paragraph.* Not re-measured here: the
reporting project measured it and it picked the wrong target for a third of the misses it reported,
which is §1's reason for this task being `l`.

### Step 3 — the sub-number rule, from the misses

The first working rule reported **nine** distinct document-and-section pairs. Reading them changed
the design:

```text
139  METHOD.md §3.1        13  METHOD.md §1.5         3  BINDING.md §6.5
 81  METHOD.md §3.3         1  BINDING.md §6.2        1  BINDING.md §6.4
```

`METHOD §1.5` is **rule 5 under *Core rules***, and `BINDING §6.2` is **step 2 of *Writing a
binding***. Both are numbered list items, not sub-headings. A rule reading headings alone calls
them dead, which is a checker disagreeing with the convention it was built to check — so a
document's sections are its numbered headings **plus the top-level ordered items directly under
each**. An item under an *unnumbered* heading yields nothing, there being no number to prefix it
with, which is why `review.md §5` is still reported.

### Step 4 — the ruling, and why it is an advisory

**`check` resolves a section reference, keyed on adjacency, and reports an unresolved one as an
advisory.** With the list-item rule the class reports **seven** lines on this repository:

```text
SECTION REF  plugin/skills/taskmd/docs/METHOD.md has no section 3.1; 136 reference(s) name it
SECTION REF  plugin/skills/taskmd/docs/METHOD.md has no section 3.3; 74 reference(s) name it
SECTION REF  plugin/skills/taskmd/docs/method/review.md has no section 1; 1 reference(s) name it
SECTION REF  plugin/skills/taskmd/docs/method/review.md has no section 2; 1 reference(s) name it
SECTION REF  plugin/skills/taskmd/docs/method/review.md has no section 4; 1 reference(s) name it
SECTION REF  plugin/skills/taskmd/docs/method/review.md has no section 5; 1 reference(s) name it
SECTION REF  tasks/T-047-...md has no section 3.2; 1 reference(s) name it
Scope  1885 of 2915 section reference(s) resolved against nothing: no document is named beside them, so none was guessed
```

**All seven are real**, and 210 citations sit behind the first two: `METHOD.md` numbers its §3
subsections and prints only §3.2, because §3.1 and §3.3 are carried in tier 1 instead (T-047). A
reader following `METHOD §3.1` opens `METHOD.md` and finds no such section. That is precisely the
defect this class exists to report, and it is the project's most-cited reference.

*Rejected: shipping it as a `problem`.* It is the honest severity — a dead citation is an error and
not a choice, which is the test [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md)
set — and it would turn this repository's own gate red over seven items whose repair is out of this
task's scope by §1 and is another task's by METHOD §5. A gate that is red on arrival is switched
off. **Advisory is a sequencing decision, not a claim about severity**, and promoting it is one line
once [T-194](T-194-print-the-two-method-sections-this-project-cites-most.md) lands.
*Rejected: narrowing the rule until this repository is clean.* That is fitting the instrument to the
answer, and it would have hidden the 210.

### Step 5 — the fixture, and the tests failing first

`tests/fixtures/section-reference/` carries six marks outside code and two inside: a citation that
resolves, one that does not, a sub-number naming a list item, a mark bound to nothing, a conjoined
pair, and the same wrong citation quoted in a fence and in a code span. Four of the six exist **to
stay silent**, which is [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s
rule in its second use.

**The check was written before the fixture** — the corpus drove it, and step 1 says why — so
fail-first was demonstrated by unwiring it from `cmd_check` and running the tests against the tree
without it:

```text
Ran 9 tests in 0.843s
FAILED (failures=5)
AssertionError: 'METHOD.md has no section 3.1' not found in 'OK - 193 task(s), ...'
```

Rewired, all nine pass. Four passed while unwired, and they are the four asserting silence — which
is the honest shape and also the warning [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)
attached to its own rule: a must-not-fire case passes vacuously until something makes it fire.

### Steps 6–7 — the document, and the suite

`README.md` gains the class inside the marked advisories region, which is what
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s guard is
for: adding `SECTION REF` to `ADVISORY_PREFIXES` failed
`test_each_marked_list_names_exactly_the_set_that_exists` until the paragraph existed. The quoted
empty-project transcript needed regenerating for the new denominator and the new `Scope` line.

```text
Ran 304 tests in 34.249s
OK
Wrote tasks/README.md - 14 active, 179 closed
OK - 193 task(s), ..., 2915 section reference(s)
EXIT=0
```

**Decisions & assumptions**

- Both `plan` decisions held. — 2026-08-19
- **A `§` outside code is always a section mark.** No attempt is made to tell a citation of another
  project's document from a citation of one of ours: an unresolvable name is simply not bound, and
  falls into the skipped count. `docs/PUBLISHING.md` cites the humanizer skill's `§14`, and it is
  skipped rather than misreported, which is the behaviour that needs no special case. — 2026-08-19
- **Assumption, recorded as one**: the skipped figure — 1,885 of 2,915 — is large, and this task
  does not claim it is irreducible. It claims that the two rules known to reduce it were both
  measured wrong here, and that reporting the gap beats guessing at it. A later rule that reduces it
  *and* is measured has this record's numbers to beat. — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/taskmd/cli.py — `check_section_references`, `numbered_sections`
- tests/fixtures/section-reference/
- tests/test_cli.py
- README.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative | **met** | §3 steps 2–4. Rejected: binding a loose mark to its own document (with the numbers that killed it), proximity, porting the reference implementation, shipping as a problem, and narrowing until this tree is clean |
| A fixture cites a document at a section it does not have and `check` reports it, shown failing first | **met** | §3 step 5. Five of nine tests failed with the check unwired; `docs/handbook.md has no section 9` is what the fixture produces |
| A mark the rule cannot bind is reported as skipped and counted, never dropped | **met** | The `Scope` line, on every run. `1 of 6` on the fixture and `1885 of 2915` here, and `test_a_mark_nothing_binds_is_counted_and_never_guessed` asserts the fixture's |
| A `§` inside a fence is not resolved, proven by a fixture quoting a wrong reference on purpose | **met** | The fixture quotes `handbook.md §404` in a fence and again in a code span; `test_a_wrong_citation_quoted_in_a_fence_is_not_resolved` asserts `404` appears nowhere in the output |
| If out: the reason is written where an adopter reads it | **n/a** | The ruling is *in*, so this criterion's condition does not arise. The class is documented in `README.md` instead, which is where the same reader would have met the refusal |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. Nothing here
is addressed to anyone else.

**What the check found is a task, not a note.** Seven lines, 210 citations behind two of them, in
the documents this project's own method lives in. Raised as
[T-194](T-194-print-the-two-method-sections-this-project-cites-most.md) rather than repaired here:
§1 puts renumbering out of scope, METHOD §5 forbids fixing a finding where it is found, and the
repair is a judgement about tier-2 content that deserves its own argument.

**Child fix tasks raised**
- [T-194](T-194-print-the-two-method-sections-this-project-cites-most.md) — the seven the class reports on this repository

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 8 of the eight and the only `l` among them. **`check` now resolves a citation of the form *document §n*, as the advisory `SECTION REF`.** The corpus decided every part of it: 2,916 marks in 294 documents, and three candidate bindings scored against the real section numbers. **Adjacency binds, conjunction inherits, and a mark bound to nothing is counted rather than guessed** — the third rule, binding a loose mark to the document it is written in, looked like free coverage and got 267 of 1,796 wrong in the one way that cannot be seen, because a task record has sections 1 to 4 of its own. A sub-number may name a numbered list item, because most of them do. Reported one line per document-and-section, so 210 citations of two missing sections are two lines. **It is advisory, and that is sequencing rather than severity**: the seven it reports here are all real, and repairing them is [T-194](T-194-print-the-two-method-sections-this-project-cites-most.md). The first probe was wrong in an instructive way and §3 keeps it: it read context from the code-blanked copy, so every document name inside a code span looked like no name at all. |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 8 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). It is last in the order and the only `l` in the eight, so it is the one most likely to end in a recorded question rather than a close — which the instruction above makes an acceptable outcome. |
| 2026-08-19 | (no change) | **The open question is answered by the owner: yes, this is taskmd's job.** Asked in the backlog-wide round of 2026-08-19. The reason given is the one §1 already carried — `check` validates Markdown links across the whole tree rather than only in task files, so resolving the section a reference names is the same job one level deeper, not a widening. *Rejected: ruling it out of scope as a documentation check*, which keeps a clean task-graph boundary at the price of section references breaking in silence whenever a document is reorganised, in a project that cites its own method by section throughout. The binding rule and the reporting shape are still open and belong to `specify`. This row is the answer, not authorisation to start. |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report. The observation that carries it is that taskmd uses `§n` citations throughout its own documentation, including in the tool's source comments, and has no way to check one. `M3` rather than `M2` because it widens what the tool is for and that question should not be answered in a milestone about holding up in another project. `l` because the binding rule is the hard part and the reporting project has already measured that adjacency beats proximity — proximity picked the wrong target a third of the time. |
