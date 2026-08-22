---
id: T-222
title: Repair the coverage clause against the eight defects a stranger found
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-199, T-192]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-22
updated: 2026-08-22
deliverables:
  - plugin/skills/taskmd/docs/BINDING.md
---

# T-222 — Repair the coverage clause against the eight defects a stranger found

## 1. Specify

**Outcome**
`plugin/skills/taskmd/docs/BINDING.md` §4 answers, from its own text, every question
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader had
to settle by guessing — or says where the answer lives.

**Why this one**
**A clause every binding anybody writes inherits had never been read by anybody who had not written
it.** T-199 ran it past a reader who had read no binding and asked them to produce a real
declaration. They produced one, and with it eight questions they could only answer by guessing, and
one blank.

**The blank is the sharpest result and it is the shape of the whole problem.** §4 describes the
stale-index state twice and never names its class. The reader guessed the name, got it **right**, and
refused to write it down — *"Guessing would pass a human and fail the one check the region exists to
support."* A clause that asks for class names in backticks, and never says where class names come
from, cannot be completed honestly by anyone who does not already know the answer.

**The repair's shape is decided by the clause's own argument, which is why this is a fix and not a
decision.** §4 already refuses a per-check coverage table, and gives the reason: *"one new check
falsifies every binding's table at once."* So the repair must **not** enumerate the classes. It must
point at whatever owns them — the same single-source rule the clause already argues for, applied to
the clause itself.

**Scope**
- In: the eight defects listed in
  [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3, each
  repaired or declined **by name**, with a reason for each decline
- In: where the validator's class list lives, stated in the clause
- In: what the marked-region check **scans**, not only what it confirms — the reader avoided
  backticking a command in case the scan was wider than the text says
- In: **reporting** whether the repaired clause leaves either shipped binding's existing declaration
  non-compliant
- Out: changing the validator, its classes, or the marked-region check. Every defect here is in the
  description, not in the behaviour
- Out: **fixing** a shipped binding the repair invalidates — that is a finding here and a task of its
  own, because editing a binding inside the task that changed the contract hides which one moved
- Out: re-running the reader. T-199 fixed one reader and its verdict stands; a second reading after a
  repair is a different question and would be a different task

**Inputs**
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3 — the
  eight defects, the four re-reads, and the declaration verbatim including the blank
- `plugin/skills/taskmd/docs/BINDING.md` §4, and its subsection *The coverage a binding declares*
- [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) §3 step 5 — the author's
  own fragment, and the defect it found in the previous wording

**Acceptance criteria**
- [ ] Each of the eight defects is repaired or declined **by name**, and every decline carries its
      reason
- [ ] The clause says where the validator's class list lives, and **does not enumerate it** — the
      shape its own anti-table argument requires
- [ ] The clause states what the marked-region check reads, so a writer can tell whether a backticked
      word that is not a class name is safe inside the region
- [ ] Whether the declaration is an entry or a section, what its bold lead may claim, and how long
      that lead may be, are all answerable from the text alone
- [ ] Both shipped bindings' declarations are checked against the repaired clause, and any that no
      longer complies is **named** — repaired or raised, stated either way
- [ ] What would test the repair is stated, even where that test is a separate task. The author
      reading it back is not a test, and that is the failure this whole line of work came from

**Open questions**
- **None.** The reader's eight items are specific, and the shape of the repair is settled by §4's own
  argument against hand-copied tables rather than by a preference.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure the two facts the clause cannot currently state: what the marked-region check actually reads, and where the class set's one home is. Run the region's own pattern over a specimen carrying a class name, an acronym and a command | the two runs, dated — the evidence steps 2 and 4 cite |
| 2 | Repair the **class-name** group — defects 1, 2 and 7 — by naming the two classes the clause already describes and pointing at the set's home. Never by listing the set | the repaired *where the class names come from* text |
| 3 | Repair the **form** group — defects 3, 4, 5 and 6 — from what the two shipped bindings already do, rather than from preference | the repaired *where the declaration goes* text |
| 4 | Repair defect 8: give the closing line a second form for a binding with nothing local | the repaired closing-line guidance |
| 5 | Check both shipped declarations against the repaired clause and re-run the marked-region tests. Name any that no longer complies; raise it rather than fix it | the compliance result, and a task if one fails |
| 6 | State what would test the repair, and raise it as a task | the statement, and the task |

**The class-name defect fixes the shape of the whole repair, and it is the one place this could go
wrong quietly.** §4 refuses a per-check coverage table because *one new check falsifies every
binding's table at once*. A list of class names written into §4 is that same table with the second
column removed, and it would fail on exactly the same day — measured: a class was added to this
validator on 2026-08-22, mid-task. So step 2 points at the home and never copies it. *Rejected:
enumerate the classes in §4* — it answers the reader in one line and re-creates the defect the clause
is built to argue against. *Rejected: add a `taskmd classes` command that prints the set* — it is the
right answer to *how does a binding author read the list*, and §1 puts changing the validator out of
scope, so it is step 6's task rather than this task's edit.

**Steps 3 and 4 are answered by the two shipped bindings, not by choosing.** Both already put the
declaration in a section of its own, both open it with a bold lead stating the answer, and both wrap
the whole declaration in the markers. The clause never said any of that, so a reader had to guess
three times and guessed right three times. Writing down what the practice already is costs nothing
and removes three defects; deciding something different would invalidate two shipped bindings to no
purpose.

**Step 1 runs before step 2 commits**, for the reason
[T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md) recorded the
same day: a sentence about behaviour that is reasoned rather than run is how this document got into
this state. Defect 7 in particular is a question about a regular expression, and the reader guessed
its answer wrongly in the safe direction — they avoided backticking a lowercase command, which the
pattern never looks at.

**Step 5 reports and does not repair**, per §1. If the repaired clause leaves a shipped binding
non-compliant, editing that binding here would hide which of the two moved.

## 3. Implement

### Step 1 — the two runs the repair is built on

**What the marked-region scan reads**, run 2026-08-22 over a specimen carrying a class name, an
acronym and a command, using the region's own pattern from `tests/test_publishing.py`:

```text
specimen:  `JQL`  `check`  `STALE INDEX`  `T-042`  `gh`  `API`  `DUPLICATE ID`
caught  :  API, DUPLICATE ID, JQL, STALE INDEX
unknown :  API, JQL          → these two would fail the check
ignored :  check, gh, T-042  → never looked at
```

So the reader's caution was right in substance and wrong about the trigger: a lowercase command in
backticks is invisible to the scan, and `local-markdown.md` has backticked one inside its region
since it was written. What is unsafe is any backticked run of capitals.

**Where the class set lives**, established the same day: `tests/classes.py` derives it from the
validator's source — the literal at each `problems.append` site plus `ADVISORY_PREFIXES`, both in
`taskmd/cli.py` — and that derivation is its one home since T-197. **No document anywhere holds the
list**, which is what the reader could not find because it is not there. 22 classes on the day.

### Every defect, and what was written

| # | The reader could not tell | What §4 now says |
| :-- | :--- | :--- |
| 1 | the name of the stale-index class | names `STALE INDEX` and `DUPLICATE ID` in the sentence that already described both states, and says since when |
| 2 | where the validator's class list lives | a new subsection: no document holds it, the home is the two places in `cli.py`, and read the set by running `check` or reading those |
| 3 | entry, or section | a section of its own — and the minimum-entries table now says the last row is the exception |
| 4 | what the bold lead is a claim about | a fact about the **mapping**; the one place in a binding exempt from claim-about-your-project, with the reason |
| 5 | how long the lead may be | the thirty-second budget is over the Assumptions section's leads and does not reach this one |
| 6 | where the region starts and ends | the markers wrap the whole declaration, bold lead included |
| 7 | what the hygiene check scans | the measurement above, written out — what it accepts, what it rejects, what it ignores, and what it cannot see |
| 8 | whether *still runs locally* presumes a working copy | two closing forms, and which to use when nothing is local |

None was declined.

### Step 5 — the two shipped declarations against the repaired clause

Both comply, and neither was edited. `local-markdown.md` and `github-issues.md` each put the
declaration in a section of its own, open it with a bold lead stating the answer, and wrap the whole
declaration in the markers — which is why steps 3 and 4 could be written from the practice instead of
decided. `github-issues.md` carries both halves of the closing line and has files; `local-markdown.md`
is the all-local backend and needs no second form.

**The check itself is where the non-compliance turned out to be.** Scanning both regions against the
derived set, 2026-08-22:

```text
github-issues.md   names 4 classes, scan reads 3   (ID WIDTH invisible: first word is two letters)
local-markdown.md  names 4 classes, scan reads 4
```

The pattern requires three or more capitals, so a two-letter first word escapes it and is neither
passed nor failed. The declaration is right; the guard over it is partly absent. Raised as
[T-227](T-227-the-marked-region-scan-cannot-see-a-class-whose-first-word-is-two-letters.md), and §4
now states the limit rather than implying the scan reads everything.

**Decisions & assumptions**
- **Naming `STALE INDEX` and `DUPLICATE ID` in the clause is not enumerating the set** — 2026-08-22.
  They are the two states the clause already described in prose; naming what it is already talking
  about adds no member and creates no list. A new class does not falsify them, which is the test §4's
  anti-table argument actually applies.
- **Point at `cli.py`, not at `tests/classes.py`** — 2026-08-22. The derivation is the tests'; the
  *names* are the code's, and `tests/` is not in what an adopter installs. Pointing a binding author
  at a file they do not receive would have been a fresh version of the same defect.
- **Say the clause sends a writer to source code, rather than soften it** — 2026-08-22. It is the
  honest answer and it is not a usable one, so the gap is recorded as
  [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) instead
  of being written around.
- **Do not name the invisible class in `BINDING.md`** — 2026-08-22. Which class has a two-letter
  first word is a fact about the code-owned set, and writing it into the contract is the copy this
  clause argues against. The dated measurement and the pointer to the binding that declares it answer
  the reader without creating one.
- **The four re-read questions in T-199 §3 were not treated as defects** — 2026-08-22. §1 scopes this
  task to the eight, and the four are about density rather than about a missing fact; a reader who has
  to read a contract twice has read a contract. Recorded rather than silently skipped, and named in
  [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) as
  not being what its pass bar is about.

**Outputs produced**
- `plugin/skills/taskmd/docs/BINDING.md` §4 — the minimum-entries lead-in, the two named classes, two
  new subsections (*Where the class names come from*, *Where the declaration goes, and what shape it
  takes*), and the paragraph stating what the region scan reads and what it misses

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Each of the eight defects repaired or declined **by name**, every decline with its reason | met | Eight rows in §3, all repaired, none declined |
| The clause says where the class list lives and **does not enumerate it** | met | It says no document holds it and names the two places in `cli.py` that do. The two class names now in the clause are its own long-standing examples, not members added to a list — a new class falsifies neither, which is the test §4's argument applies |
| The clause states what the marked-region check reads | met | Written from the run in §3: accepted, rejected, ignored, and — found while measuring — what the pattern cannot see at all |
| Entry or section, what the lead may claim, and how long, all answerable from the text | met | Answered as a section, a claim about the mapping, and outside the budget. Taken from what both shipped bindings already do rather than decided, so nothing shipped was invalidated |
| Both shipped bindings checked against the repaired clause, any non-compliance **named** | met | Both comply and neither was edited. The scan is what fails, on `github-issues.md`'s fourth class name — named, measured, and raised as [T-227](T-227-the-marked-region-scan-cannot-see-a-class-whose-first-word-is-two-letters.md) rather than fixed here, per §1 |
| What would test the repair is stated, even where that test is a separate task | met | [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), with the count and the pass bar required **before** the run — the author reading it back is not a test, and a second reader whose bar is set afterwards is not one either |

**Child fix tasks raised**
- [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md) — the test of this repair
- [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) — the class list is reachable only by reading source
- [T-227](T-227-the-marked-region-scan-cannot-see-a-class-whose-first-word-is-two-letters.md) — the guard over the declarations reads three names in four

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | proposed → done | `plan` through `review` in one session, under the four-task grant recorded below. **All eight repaired, none declined.** The class-name defect was answered by pointing at the validator's source and never by writing a list, which is the shape §1 fixed and the one a grant of phases could have walked past. **Three of the eight were answered by the two shipped bindings rather than decided** — both already put the declaration in its own section, opened it with a bold lead and wrapped the whole thing in the markers, so the clause was made to say what the practice already was, and nothing shipped was invalidated. **Measuring what the scan reads found a defect nobody was looking for**: the pattern needs three or more capitals, so a class name whose first word is two letters is invisible, and `github-issues.md`'s region has one — four names declared, three read. The declaration is right and the guard over it is partly absent. Raised as [T-227](T-227-the-marked-region-scan-cannot-see-a-class-whose-first-word-is-two-letters.md) rather than fixed, because §1 puts the check out of scope by name and the clause was repaired on the strength of that measurement. Two more raised: [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), the test of this repair, with its count and pass bar required before the run; and [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), because the repaired clause honestly sends a binding author to read Python in order to write Markdown. **All three are soft edges** — none is part of this outcome, which is a repaired clause and exists. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that [T-221](T-221-correct-the-two-behavioural-claims-the-migrated-away-run-falsifies.md), this task, [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md)'s remaining phases and [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) be worked through the **full lifecycle**, and the result committed and pushed. **What it covers here:** this record, from the plan phase onward - its own specify section is already written - through to closure without stopping to ask for each phase. **What it does not cover:** any other task, and in particular not repairing a shipped binding this repair invalidates. §1 puts that out by name, and a grant of phases does not widen a scope the owner set. **It authorises phases, not answers.** **Specific to this task**: §1 fixes the shape of the repair - the clause argues against hand-copied tables, so the class-name defect must not be answered by writing the class list into it - and the grant does not license choosing the easier shape. [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) is `blocked_by` this record, so the order is forced rather than preferred. Written into this record rather than kept in the session's handoff (`CLAUDE.md`, *one phase per request*). |
| 2026-08-22 | → proposed | Raised from [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader run under the owner's decision of 2026-08-22, which chose a separate task over repairing inside T-199. **The reason is size, not process**: T-199's fifth criterion permits the repair in place, and eight defects in a contract every binding inherits is a rewrite rather than an edit. T-199 records that reason and stays open on that criterion alone. `high` because the clause is inherited by every binding anybody ever writes, and the one reader who has tried to use it could not complete it without guessing eight times. `m` because the hard half is not the edits but keeping the repair inside the clause's own rule — it argues against hand-copied lists and must not answer the class-name defect by writing one. |
