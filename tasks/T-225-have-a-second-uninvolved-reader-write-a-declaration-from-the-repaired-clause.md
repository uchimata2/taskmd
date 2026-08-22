---
id: T-225
title: Have a second uninvolved reader write a declaration from the repaired clause
type: audit
status: done
phase: review
parent: null
blocked_by: []
related: [T-222, T-199, T-176]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
deliverables: []
---

# T-225 — Have a second uninvolved reader write a declaration from the repaired clause

## 1. Specify

**Outcome**
A reader who has read no taskmd binding produces a coverage declaration from the repaired
`BINDING.md` §4, and every place they had to guess is recorded — so it is known whether
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s repair
works on somebody who was not in the room.

**Why this one**
T-222 repaired eight defects a stranger found, and **the author reading it back is not a test** —
that is the failure the whole line of work came from, and T-222's own sixth criterion says so.
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) built the
instrument and it worked: one reader, one prompt, one declaration, eight defects and a blank.

**Set the terms before running it, because this is the run that turns an instrument into a loop.**
A second reader on a repaired document is fresh, and the loop is still *edit until somebody agrees*.
Two things must be fixed in advance: **how many readers** (one), and **what counts as a pass** —
which is not *no questions*, since T-199's reader asked four re-read questions that were about
ordinary density rather than about defects. Decide the bar with the owner before the prompt is sent.

**Scope**
- In: one reader, one prompt, the repaired §4 embedded verbatim, no other file within reach
- In: a **different backend** from T-199's Jira Cloud, so the run is not the same question twice
- In: the pass bar, agreed before the run
- Out: repairing whatever it finds. T-199 established that repairing inside the measuring task
  destroys the evidence the measurement happened
- Out: a third reader. If the second finds defects, that is a repair task and then a decision about
  whether to measure again — not an automatic next round

**Inputs**
- `plugin/skills/taskmd/docs/BINDING.md` §4 as repaired on 2026-08-22
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) §3 — the
  instrument, the prompt shape, and the eight defects this run is testing the repair of

**Acceptance criteria**
- [ ] The reader states, in their own words, that they had read no taskmd binding
- [ ] The declaration is recorded verbatim, including anything they refused to write
- [ ] Every question they had to settle by guessing is listed, and each is matched against the eight
      T-222 repaired — so it is visible whether a repair worked, missed, or created a new gap
- [ ] The pass bar was written down before the run, and the verdict is given against it

**Open questions**
- ~~**What is the pass bar, and how many readers?** — the project owner. The recommendation is **one
  reader**, and **pass = none of the eight recurs and no new defect blocks the declaration**; a
  re-read question is not a defect. Deciding this after seeing the result is what turns the
  instrument into iteration.~~ **Answered by the owner on 2026-08-22: the recommendation stands** —
  one reader, and that pass bar. See the Log row of that date.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Run 2026-08-22, by the owner. Two readers, where §1 fixed the count at one.** Both were given the
same prompt, at the same time, with no edit to `BINDING.md` between them and neither shown the other's
answer. **Recorded as a deviation and not as an improvement**, because the count was set in advance and
was not met. What it does not do is damage the result: the hazard §1 names is *a second reader after an
unwelcome first*, which needs an edit or a verdict in between, and there was neither. **Two parallel
readers of one text are a stronger instrument than one**, and this run produced its sharpest finding
only because they disagreed. What that argues for revisiting is the count's wording, not the count.

Both stated, unprompted, that they had read no taskmd binding. Both chose **Linear**, independently and
for the same stated reason: it allocates its own identifiers and computes its list, which is the pair
the clause turns on. Neither was told a repair was being tested, that eight defects had been found
before, or that a blank was an acceptable answer.

### Reader A — the declaration, verbatim

```markdown
Under this mapping, Linear assigns and enforces task identifiers while dynamically computing task
listings on demand.

Because task identity is allocated directly by Linear and task lists are generated live via API
rather than read from an index file, `STALE INDEX` and `DUPLICATE ID` cannot occur.

The rest applies as written.
```

### Reader B — the declaration, verbatim

```markdown
Two of the validator's classes cannot occur under the mapping in §3: `STALE INDEX` and `DUPLICATE ID`.

`STALE INDEX` cannot occur because nothing under this mapping holds a second copy of the task list.
§3 maps "the list of tasks" onto a query run against Linear when someone asks for it. The answer is
computed and then discarded. There is no index that can fall behind the thing it indexes. This holds
only while the mapping is followed: a project that exports its issues to a file on a schedule and then
reads that file has put an index back, and this line stops being true for it. §3 forbids that export
for this reason.

`DUPLICATE ID` cannot occur because §3 makes Linear's own issue identifier the task id. Linear
allocates it at creation and no writer supplies or edits it, so two tasks cannot arrive holding the
same one. Note what that rests on: the mapping, not the service. A binding over this same service that
kept a human-chosen id in a custom field would leave this class fully live, because Linear does not
police that field.

This binding names no other class, and that is a gap, not a finding. The class names have one home,
the validator's own source, and this binding was written without access to it. Other classes may also
be impossible under this mapping. Rather than guess a name from a state, they are left out — a gap a
reviewer can see is worth more than a name that reads well and matches nothing. Before adoption, run
`check` against a live project, read the prefixes it prints, and add any further class this mapping
makes impossible.

The machine check on this section is hygiene, not truth. It confirms the statement is present and that
each name is one the validator reports. Whether Linear really makes these two states impossible is a
fact about Linear, and nothing running locally knows it. Read the two paragraphs above as claims to be
checked, not as results.

The rest applies as written.
```

**Reader B added, unasked, that its own substance is the part it has least right to assert** — that
Linear's identifiers are unique across a workspace, never reused after deletion and not user-editable
are three assumptions it did not verify. That is the clause's *hygiene is not truth* paragraph arriving
back as a reader's own caveat, which is the one thing in this run that reads as the document working.

### The eight, one by one

| # | What T-222 repaired | Recurred? |
| :-- | :--- | :--- |
| 1 | the stale-index class had no name | **No.** Neither reader asked; both used `STALE INDEX` without comment |
| 2 | where the validator's class list lives | **No, but its consequence arrived from both.** Both found the answer and both reported they could not reach it from the prompt. That is [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md)'s subject, already raised and already answered |
| 3 | entry, or section | **No — and the answer opened a new gap both readers hit.** *A section of its own* names no heading text and no level. A asked for a title and a depth; B chose one and asked for a canonical one, and separately asked where in the document the section goes |
| 4 | what the bold lead claims | **No.** B asked the adjacent question — whether the lead must carry the class names or a bare count |
| 5 | how long the lead may be | **No.** Neither reader raised it |
| 6 | where the region starts and ends | **No.** Both inferred it correctly. B asked two refinements: whether the closing line sits inside, and whether the region may hold anything besides classes and their reasoning |
| 7 | what the hygiene check scans | **No, and the form of the answer is the finding.** B asked for the pattern written out once rather than inferred from a four-sample measurement: an identifier like a team key plus number, a mixed-case name, and a bare two-letter word are all unanswerable from it. A asked for the acronym rule, **which is present and explicit in that same paragraph** — a reader missed a stated sentence, which is the same defect seen from the other side |
| 8 | does *still runs locally* presume a working copy | **Yes. Recurred, from both readers.** The repair's three sentences key on three different things: sentence one on the project (*the adopter kept a working copy*), sentence two on the backend (*a binding whose backend is remote-only*), sentence three on the project again. B named the mismatch exactly; A said it was left to infer. Confirmed by reading the paragraph |

### The finding neither reader could have produced alone

**Naming two classes in the clause made one reader treat them as the set.** *Some of the validator's
classes … `STALE INDEX` …, `DUPLICATE ID` …* is written as an illustration and reads as an inventory.
Reader A declared exactly those two and gave its reason in its own words: *"I declared only `STALE
INDEX` and `DUPLICATE ID` because they were explicitly identified in Section 4."* Reader B read them as
examples, said so, and wrote a paragraph declaring the gap instead.

**Two shippable declarations, differing in what they claim about the backend, from one text.** This is
a defect the 2026-08-22 repair introduced: before it the clause named no class and the failure was a
blank; after it the failure is silent under-declaration that no check can see, because every name in
A's region is a real class. It is visible only because two readers ran, which is why the deviation
above is recorded as a deviation and its result kept.

**Decisions & assumptions**
- **Both runs recorded, and the count deviation recorded with them** — 2026-08-22. Suppressing either
  reader to match the stated count would have destroyed the one finding that needed both, and reporting
  two as though two had been planned would falsify the instrument.
- **The verdict is given against the bar as written, not against the bar the result suggests** —
  2026-08-22. The bar was fixed before the prompt existed, and a bar rewritten after a result is not a
  bar.
- **Reader A's missed sentence is recorded as a legibility finding, not as a gap** — 2026-08-22. The
  acronym rule is in the text, verbatim, in the paragraph B separately criticised for describing the
  pattern by measurement. Two readers, two symptoms, one paragraph.
- **Nothing was repaired here** — 2026-08-22, §1's own rule and T-199's before it.

**Outputs produced**
- the two readings above, and the verdict in §4
- [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The reader states, in their own words, that they had read no taskmd binding | met | Both did, in their first line, unprompted |
| The declaration is recorded verbatim, including anything they refused to write | met | Both in §3. Reader B's refusal to name a class it could not source is recorded as written, and it is the half of that reading worth most |
| Every question settled by guessing is listed, and each matched against the eight | met | The eight are walked one by one in §3, and the questions falling outside them are grouped there rather than dropped. Reader B produced nineteen about the contract and three about Linear; the three about Linear are outside the clause and are marked so |
| The pass bar was written down before the run, and the verdict is given against it | met | Bar fixed 2026-08-22 in the Log, before the prompt was built. Verdict below |

**Verdict: FAIL, on the first half of the bar.**

The bar was *none of the eight recurs, and no new defect blocks the declaration*.

- **Defect 8 recurred**, from both readers independently, and reading the paragraph confirms it: the
  repair answered *what the two closing forms are* and left *which fact chooses between them* keyed on
  the project in one sentence and on the backend in the next.
- **No declaration was blocked.** Both readers shipped one. The second half passes.

**What the fail is worth, stated because a failing verdict invites being explained away.** Seven of the
eight held under readers trying to break them, one recurred in a form sharper than the original, and
the repair introduced one new defect that only two readers could reveal. That is a working instrument
reporting a real result rather than a repair that failed — and the reason the bar was written first is
that this paragraph is exactly where a verdict would otherwise get softened.

**Child fix tasks raised**
- [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) — everything above, repaired where it was found to be wrong rather than here

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | review → done | **Closed by the owner on 2026-08-22, with a FAIL recorded as its result.** All four criteria are met and the outcome exists: the repair was measured by readers who were not in the room, against a bar written before the prompt was built. **A failing verdict is a result and not an unfinished task** — leaving this open would have read as work remaining when the work is done, and would have invited the verdict being softened by whoever came to finish it. The repair leaves as [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md), which the owner made a blocker of the release the same day. **Two things this record carries that nothing else does**: both declarations verbatim, including the one that under-declared and the one that refused to guess, and the deviation on the reader count — recorded as a deviation and kept, because the finding that mattered most needed both readers. That deviation is now [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md)'s occasion. |
| 2026-08-22 | (no change) | **The prompt is built and handed to the owner, who runs it.** Assembled the same day from `BINDING.md` §4 as repaired, extracted whole with `awk` from the section heading to the next one and embedded verbatim beneath the ask — so it is **regenerated, never stored**: a copy kept in this repository would be a second home for §4 and would go stale the first time §4 is edited, which is the defect the clause it tests argues against. **What the ask contains**: state whether you have read a taskmd binding; pick a tracker and say why, not Jira Cloud; state the mapping before writing; write the declaration as you would ship it; then list every question you had to settle by guessing, with what you decided and what you wanted the text to say. **What it deliberately does not contain**: that a repair is being tested, that eight defects were found before, and any invitation to leave a blank — [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader left one unprompted and that was the finding, so prompting for one here would manufacture the result. The pass bar was fixed in the row of this date **before** the prompt existed. |
| 2026-08-22 | (no change) | **The pass bar and the reader count are fixed by the owner, before the run: answered 2026-08-22.** **One reader**, and **pass = none of the eight defects recurs and no new defect blocks the declaration**; a re-read question is explicitly *not* a defect, because [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s reader asked four of those and they were density rather than missing facts. *Rejected: decide the bar after seeing the result* — it is the same failure as writing acceptance criteria to a known verdict, one instrument along, and it is what turns a check into *edit until somebody agrees*. *Rejected: two readers* — more confidence, and only if the count is fixed in advance either way, which is the condition that makes one enough. **The date matters as much as the answer**: this row precedes any prompt being sent, so a later session can see the bar was not tuned to the result. |
| 2026-08-22 | → proposed | Raised by [T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s sixth criterion, which asks what would test the repair and permits that test to be a separate task. **Separate rather than folded in**, for T-199's own reason: a repair measured by the person who wrote it is not measured. `medium` and `s` — the instrument exists and the run is one prompt. **The hazard is named in §1 rather than left to the run**: a second reader on a repaired document is one edit away from being iteration, so the count and the bar are set before the result is known. |
