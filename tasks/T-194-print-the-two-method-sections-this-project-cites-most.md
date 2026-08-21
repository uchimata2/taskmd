---
id: T-194
title: Print the two method sections this project cites most
type: fix
status: done
phase: review
parent: T-093
blocked_by: []
related: [T-047, T-028]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: yes
deliverables: []
---

# T-194 — Print the two method sections this project cites most

## 1. Specify

**Outcome**
`check` reports no `SECTION REF` line on this repository, because every section this project cites
is a section the target document prints.

**Why this one**
[T-093](T-093-decide-whether-check-resolves-a-section-reference.md) shipped the class and it reports
seven lines here, all real:

```text
plugin/skills/taskmd/docs/METHOD.md has no section 3.1; 136 reference(s) name it
plugin/skills/taskmd/docs/METHOD.md has no section 3.3; 74 reference(s) name it
plugin/skills/taskmd/docs/method/review.md has no section 1, 2, 4, 5; 1 reference each
tasks/T-047-...md has no section 3.2; 1 reference(s) name it
```

**The first two are the interesting ones and they are not a typo.** `METHOD.md` numbers its §3
subsections and prints only §3.2, because §3.1 and §3.3 are the two rules carried in tier 1
instead ([T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md)), and
METHOD.md says so in prose. So the document explains the absence and still leaves 210 citations
pointing at nothing a reader can find. **A pointer is not a copy**, which is what makes this
repairable without re-opening T-047: a heading numbered 3.1 whose body says *this rule binds before
this document loads, so it lives in your project's always-loaded conventions* states where the rule
is, not what it is.

**The other five are ordinary.** `review.md`'s procedure is a numbered list under an unnumbered
heading, so the citations of *procedure step n* have no section to resolve against; and one task
record is cited at a §3.2 it does not have.

**Requirements served**
R-16, and `CLAUDE.md`'s standing requirement that `check` is clean on this tree.

**Scope**
- In: the seven, each resolved either by the document gaining the section or by the citation being
  corrected
- In: which of the two repairs each case gets, decided per case and not by a blanket rule
- Out: re-opening [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md).
  The two rules stay where they are; this is about whether `METHOD.md` prints a numbered heading
  saying so
- Out: promoting `SECTION REF` from advisory to problem. That becomes available once this closes and
  is its own decision, named in
  [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3
- Out: the 1,885 marks the rule binds to nothing. They are reported as skipped by design, and
  reducing that number is a different task with T-093's measurements to beat

**Inputs**
- [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3 — the class, the seven, and
  the rule that produced them
- `plugin/skills/taskmd/docs/METHOD.md` §3 — the section that prints 3.2 and not 3.1 or 3.3
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) — why those two
  rules are not in that document
- `tests/test_budget.py` — tier 1, in case a repair is proposed that touches `CLAUDE.md`

**Acceptance criteria**
- [ ] `taskmd check` on this repository prints no `SECTION REF` line, shown as output
- [ ] **No rule is copied.** If `METHOD.md` gains headings, their bodies point at where the rule
      lives and do not restate it — checked by reading them against `CLAUDE.md`'s text, not by
      intending it
- [ ] Tier 1's character count is unchanged, from `tests/test_budget.py`
- [ ] Each of the seven says which repair it got and why, so a reader can tell a corrected citation
      from a corrected document
- [ ] A test holds the result, so the seven cannot come back unnoticed

**Open questions**
- ~~**Does `METHOD.md` gaining headings for 3.1 and 3.3 weaken what T-047 achieved?**~~ **Answered
  2026-08-19: it does not, and `METHOD.md` gains the two headings.** Each body states where the rule
  lives and does not restate it. Correcting the 210 citations instead was offered as the alternative
  and rejected: it is more work and it moves the convention rather than the document. **The caution
  in the question survives as a criterion rather than as a reservation** — *pointer* is what every
  second home calls itself at the start, so the acceptance criterion that reads the new bodies
  against `CLAUDE.md`'s own text is the one carrying this answer, and it is met by reading, not by
  intending.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Locate all seven citations using the checker's own binding rule, so each repair is aimed at a site instead of at a count | file and line for all seven, in §3 |
| 2 | `METHOD.md` gains `### 3.1` and `### 3.3` — heading plus pointer, no rule text — and §3's opening paragraph says all three are numbered and only one is stated | `plugin/skills/taskmd/docs/METHOD.md` |
| 3 | The three `review.md §n` citations name the numbered **step** they mean, in the form [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) already uses | `tasks/T-027-give-the-design-rule-one-home.md`, `tasks/T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md` |
| 4 | The two section marks in the prior-art schema table read `see §n`, so the phase value beside them stops being read as a document name | `reference/TASK-WORKFLOW.md` |
| 5 | `CLAUDE.md`'s block comment names the method beside its mark, so it stops binding to the task record cited in the same clause | `CLAUDE.md` |
| 6 | A test asserting this repository prints no `SECTION REF` line, shown failing before it is trusted | `tests/test_cli.py` |
| 7 | `check`, `index` and the full suite run, and what they printed recorded | §3 |

## 3. Implement

**Decisions & assumptions**
- **Repair per case, not by rule** — decided 2026-08-19. Two cases got the document; five got the
  citation. The split is not a compromise: the two `METHOD.md` marks are cited 210 times and mean
  exactly what they say, so the document is what is missing. The other five each named something
  other than a section of the document they bound to.
- **The seven were located, not inferred** — 2026-08-19. `check` aggregates one line per
  document-and-section pair, so it says *how many* and never *where*. A throwaway script reusing the
  shipped `SECTION_MARK`, `SECTION_NAMED` and `SECTION_CONJOINED` regexes and the checker's own
  `target_of` reproduced the seven pairs at 136 / 74 / 1 / 1 / 1 / 1 / 1 — identical to `check`'s
  own aggregation, which is what makes the sites trustworthy rather than grep's guess.
- **Two of the five were mis-bindings, not wrong citations** — 2026-08-19, and this is the finding
  worth carrying. `reference/TASK-WORKFLOW.md` line 74 reads
  `` | `specify` · `plan` · `implement` · `review` | §2 | ``: the mark means that document's own §2,
  and adjacency read the **phase value** `review` beside it as a document name, resolving it to
  `review.md`. `CLAUDE.md`'s block comment carried the fragment
  `(T-047); §3.2 presupposes a phase`, so that mark bound to the task record named in the clause
  before it. Neither citation was
  wrong to a reader; both were unreadable to the rule. Corrected by naming what is meant, which is
  the repair the class exists to prompt.
- **The prior-art table's other mark was corrected too, though it was already silent** —
  2026-08-19. Line 73's `§4` binds to `` `cancelled` `` and resolves to nothing, so it never fired.
  Leaving it would have made one row of a two-row table read `see §4` and the other `§4`. *Rejected:
  touching only the firing line*, which is cheaper and leaves the table inconsistent for a reason
  no reader can see.
- **`review.md §1`, `§4` and `§5` all meant a numbered step**, not a section — 2026-08-19. That file's
  procedure is a numbered list under an unnumbered heading, which
  [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3 records as yielding no
  section number. Each was checked against the step it names before being rewritten, and all three
  matched: step 1 *take the criteria as they were written*, step 4 *do not fix things here*, step 5
  *read the task's own open questions before closing*.

**The seven, and which repair each got**

| # | Citation | Cited at | Repair |
| :-- | :--- | :--- | :--- |
| 1 | `METHOD.md` §3.1 | 136 sites | **Document** — gained `### 3.1`, a heading whose body says where the rule lives |
| 2 | `METHOD.md` §3.3 | 74 sites | **Document** — gained `### 3.3`, same shape |
| 3 | `review.md §1` | `tasks/T-027-give-the-design-rule-one-home.md:180` | **Citation** — now `step 1` |
| 4 | `review.md §2` | `reference/TASK-WORKFLOW.md:74` | **Citation** — now `see §2`; the mark meant that document's own section |
| 5 | `review.md §4` | `tasks/T-027-give-the-design-rule-one-home.md:188` | **Citation** — now `step 4` |
| 6 | `review.md §5` | `tasks/T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md:290` | **Citation** — now `step 5` |
| 7 | `T-047 §3.2` | `CLAUDE.md:84` | **Citation** — now `METHOD §3.2`, inside a block comment |

**Writing this record up re-created nine of the seven.** The first `check` after §3 was
drafted reported five lines again, every one of them cited inside this file: a table row reading
``| `review.md` §1 |`` is a citation, and the rule cannot tell a repair note from a document
pointing at a section. All nine are now quoted inside code spans, which the checker blanks before
scanning — the same device [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) used
to write about its own misses, and the reason its `test_a_wrong_citation_quoted_in_a_fence_is_not_resolved`
exists. Worth carrying beyond this task: **a document that describes a scanner's findings is inside
that scanner's corpus**, so the write-up is scanned last and the findings are quoted, never written
plain.

**The repair falsified a test, and the suite is what said so.**
[T-093](T-093-decide-whether-check-resolves-a-section-reference.md) wrote
`test_this_repository_reports_the_two_it_is_known_to_have`, asserting that this repository *does*
report §3.1 and §3.3, with the stated reason that a rule which stopped firing would fail there
rather than pass quietly. Repairing the corpus made that assertion false. It was **removed rather
than inverted**, and the comment left in its place names where its guarantee went: liveness is held
by the fixture test beside it, and the clean corpus by the new test. Inverting it would have written
the clean-corpus assertion twice.

**The new test was shown failing before it was trusted.** One repair was reverted — `METHOD` taken
back out of `CLAUDE.md`'s comment — and the test failed, naming the citation:

```text
AssertionError: 'SECTION REF' unexpectedly found in '...
SECTION REF  tasks/T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md has no section 3.2; 1 reference(s) name it
```

**`check` on this repository, after the repair — no `SECTION REF` line:**

```text
OK - 195 task(s), 975 field value(s), 3287 front-matter value(s), 654 reference(s), 24 dependency
edge(s), 297 declared output(s), 1 index file(s), 182 closed record(s), 227 document(s), 2473
link(s), 4085 table row(s), 2 template(s), 10 template field value(s), 5 vocabulary row(s), 2974
section reference(s)
Scope  68 document(s) not read: a clone would not receive them
Scope  1933 of 2974 section reference(s) resolved against nothing: no document is named beside them
```

**The suite, and the tier-1 figure:**

```text
307 passed, 8 subtests passed in 57.74s
tier 1 6380 chars under by 1474 (bound 7854, reference/TASK-WORKFLOW.md)
```

**The bound moved and tier 1 did not.** `tests/test_budget.py` measures tier 1 against the length of
`reference/TASK-WORKFLOW.md`, and step 4 edited that file — so the bound went 7,846 → 7,854 and the
margin 1,466 → 1,474. Tier 1 itself is 6,380 characters before and after, because the only tier-1
edit is inside a block comment and the harness strips those before injecting
([T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md)). Eight characters of slack is
noise against a 1,474 margin, but it is slack bought by editing the measuring stick, and it is
recorded here rather than left for someone to find in a diff.

**Outputs produced**
- `plugin/skills/taskmd/docs/METHOD.md`
- `reference/TASK-WORKFLOW.md`
- `CLAUDE.md`
- `tasks/T-027-give-the-design-rule-one-home.md`
- `tasks/T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md`
- `tests/test_cli.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `taskmd check` on this repository prints no `SECTION REF` line, shown as output | met | The run is quoted in §3. Seven lines before, none after |
| **No rule is copied.** If `METHOD.md` gains headings, their bodies point at where the rule lives and do not restate it — checked by reading them against `CLAUDE.md`'s text | met | Read side by side rather than intended. §3.1's body is *not stated here*, why it cannot be here, and two pointers; §3.3's is the same shape. Neither contains any imperative from `CLAUDE.md`'s two rules — no *do the phase that was asked for*, no *raise it as a question now*. The section's opening paragraph now states the test explicitly, so the next editor meets it |
| Tier 1's character count is unchanged, from `tests/test_budget.py` | met | 6,380 characters before and after. The one tier-1 edit is inside a block comment, which the test does not count |
| Each of the seven says which repair it got and why, so a reader can tell a corrected citation from a corrected document | met | §3's table, one row each, naming the site. Two got the document, five the citation |
| A test holds the result, so the seven cannot come back unnoticed | met | `ChecksThisRepository.test_no_citation_names_a_section_this_repository_does_not_print`, **shown failing** with one repair reverted (§3) rather than asserted to work |

Five criteria, five met, no child raised.

**What this unblocks and does not do.** Promoting `SECTION REF` from advisory to problem is now
available and is deliberately **not** taken here — §1 puts it out of scope and
[T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3 names it as its own decision.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | All five criteria met, no child raised. **Authorisation (METHOD §3.1):** the owner's grant of 2026-08-19 to work T-194, T-189, T-148, T-131 and T-181 through their full lifecycle. `specify` needed no new agreement — its one question was answered by the same owner in the question round earlier that day. **The interesting half was not the two headings but the five citations**: two of them were not wrong at all, they were unreadable to the adjacency rule, one because a *phase value* named `review` sat beside the mark and one because a task id did. Both now name what they mean. **The repair falsified one of T-093's own tests**, which asserted this repository still had the two misses — removed rather than inverted, with a comment naming where its guarantee went. Worth carrying: editing `reference/TASK-WORKFLOW.md` moves the tier-1 **bound**, since `test_budget` measures against that file's length — 7,846 → 7,854, tier 1 unchanged at 6,380. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round.** `METHOD.md` gains pointer headings for 3.1 and 3.3; the 210 citations stay as they are. The question in §1 is struck through with what was rejected and why. **No phase was started on this answer** — an answer settles a question and is not authorisation to run one ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) raised it. **It does not answer §1's question**, which asks whether a numbered heading in `METHOD.md` weakens what [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) achieved — a judgement about the project's most carefully guarded rule, and the owner's. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-093](T-093-decide-whether-check-resolves-a-section-reference.md)'s review, from what the new class reports on this repository. Not fixed there: §1 of that task puts renumbering out of scope, and a finding is never repaired where it is found (METHOD §5). `s` in effort and `medium` in value — the work is small, and what it unblocks is promoting the class to a problem, which is where its worth actually is. |
