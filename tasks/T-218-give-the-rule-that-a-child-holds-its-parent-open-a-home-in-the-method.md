---
id: T-218
title: Give the rule that a child holds its parent open a home in the method
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-212, T-216, T-209]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: yes
deliverables: []
---

# T-218 — Give the rule that a child holds its parent open a home in the method

## 1. Specify

**Outcome**
The rule *a child holds its parent open — a task may not close while one of its children is open*
has one durable home in the shipped method, so it survives the closure of the task records that
currently carry it.

**Why this one**
The **project owner** settled the rule on **2026-08-22**, answering a question raised by
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md): a child holds **every** parent
open, not only an audit umbrella. **Right now that ruling exists in exactly two places, and both are
task records** — T-212 §1 and
[T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) §1.

**Both of those will close, and a premise inside a closed record expires in silence.** Views read
open work, so the day T-212 closes the rule leaves every list a session consults. It does not go
stale — it goes invisible, which is worse, because nothing reports its absence.

**What the shipped documents say today is narrower than the rule.**

- [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 5 reads *"Close the **umbrella**
  only when every child is resolved"* — an audit's umbrella, which is the reading T-212 had to put
  to the owner precisely because it does not cover an ordinary parent.
- [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4 defines the hierarchy edge — *"This task
  belongs to that one. The inverse is that task's children."* — and says nothing about closure.
- `cli.py`'s `holds_open()` states the rule in full and qualifies it to nothing, but it is code and
  the method is not derived from it.

So the method's own text has a gap that the tool and the owner have both already filled.

**And two shipped documents say the *opposite*, which this section missed when it was written.**
Found on 2026-08-22 by [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)
§3 step 2, while judging the three records the rule condemns:

- [`review.md`](../plugin/skills/taskmd/docs/method/review.md) step 3 — *"For anything not met, raise
  a **child** task"* — and step 6 — *"Close the task when every criterion is met **or carried**"*.
- [`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §2, the `review` exit criterion — *"Every
  criterion is either met or **carries a child task** that will meet it."*

Together they instruct a reviewer to attach an unmet criterion to a hierarchy child and then close —
which is exactly the state the owner ruled is a defect. **All three of the cases T-216 repaired were
produced that way**, so this is not a hypothetical clash: the method has been telling people to do
the thing it is about to forbid.

**This is a gap of a different kind from the three above, and it changes what this task must
produce.** *Narrower* text can stand beside a general rule as an application of it. *Contradictory*
text cannot: writing the rule into `METHOD.md` §4 and leaving `review.md` as it is would ship a
method that argues with itself, which defeats this task's own outcome — one durable home for the
rule is worth nothing if another home says the reverse. So the scope below is extended to cover it,
recorded here rather than absorbed silently.

**It needs no further ruling from the owner, and that is a judgement worth stating.** The owner
settled the *substance* on 2026-08-22 — a child holds every parent open. What is left is which
documents change and how, which is what the scope below already called this task's work for
`audit.md`. The reconciliation adds no new policy: it says a residual whose parent's outcome is
finished takes a **soft** edge, and that is already this project's practice —
[T-211](T-211-mark-the-quiet-cases-in-the-two-fixtures-outside-t-202-s-scope.md) raised its two that
way on 2026-08-22, and T-216 §3 applied it to three more with the reasoning per record.

**Scope**
- In: deciding where the rule belongs — `METHOD.md` §4 beside the edge it constrains, or a phase
  file — and writing it there once
- In: deciding what happens to `audit.md` step 5, which becomes either an application of the general
  rule or a pointer to it. **It must not become a second copy**
- In: **reconciling every shipped statement that contradicts the rule** — `review.md` and
  `METHOD.md` §2's `review` exit criterion, per the paragraphs above. Added 2026-08-22, mid-`specify`,
  on T-216's finding
- In: **finding that set by a survey rather than from memory**, and recording what the survey read
- Out: the `check` class that reports the state, which is
  [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md)
- Out: repairing this repository's three cases, which is
  [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)
- Out: the **open** parent case. [T-209](T-209-report-an-open-child-as-a-blocker-on-the-parent-that-cannot-close.md)
  settled that an open parent with an open child is the ordinary state and is not reported; this
  task documents when a parent may *close*, which is the other side

**Inputs**
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §1 — the question, the two
  readings, and the owner's answer with its date
- `plugin/skills/taskmd/docs/METHOD.md` §4 — the edge definition, and the *store the forward edge*
  rule that governs where a fact may be written
- `plugin/skills/taskmd/docs/method/audit.md` step 5 — the narrower statement
- `plugin/skills/taskmd/taskmd/cli.py` — `holds_open()`, which already states it
- `plugin/skills/taskmd/docs/method/review.md` — steps 3, 4, 6 and the worked example, which
  instruct the opposite
- [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) §3 step 2 — the
  finding, and the three records that were produced by following `review.md` as written

**Acceptance criteria**
- [ ] The rule is stated **once** in the method, and the decision records where and why, with the
      rejected location and its reason
- [ ] `audit.md` step 5 is left as an application or a pointer, and a reader of either place can tell
      which is the source — no second copy of the rule
- [ ] The owner's ruling is cited where the rule now lives, with its date, so a later reader can find
      the argument without opening a closed task
- [ ] **No shipped document contradicts the rule**, and the set of places that spoke about it was
      found by a survey whose command and output are recorded — not from memory. Added 2026-08-22
      mid-`specify`, with the reason in §1; the original four criteria are unchanged
- [ ] `check`, `index` and the suite are green, and the tier-1 budget test still passes

**Open questions**
- **None.** The rule is settled; where it lives is this task's work.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Survey the whole shipped subtree for every place that speaks about a child, and judge each occurrence as *states the rule* / *narrower* / *contradicts* / *unrelated*. Read the full match list, not a filtered one. | The command, the count of files it read, and a classification of every match, in §3 |
| 2 | Write the rule once, in `METHOD.md` §4, beside the edge it constrains. Record the rejected location and why. | A new subsection in `METHOD.md` §4, and a decision in §3 |
| 3 | Give `METHOD.md` §4's *Which edge to use* the hierarchy question it currently lacks, plus the residual case that is the one people get wrong. | Edited bullets in `METHOD.md` §4 |
| 4 | Reconcile `review.md` steps 3, 4, 6, its aside at *A question aimed at someone else*, and its worked example. | Edited `review.md` |
| 5 | Reconcile `METHOD.md` §2's `review` exit criterion. | One edited table cell |
| 6 | Leave `audit.md` step 5 as an **application** naming §4 as its source, keeping only what is specific to an audit. | Edited `audit.md` |
| 7 | Fix `holds_open()`'s docstring, which states the rule correctly but says *umbrella* where it means *parent* — the exact word that made the rule ambiguous in the first place. | Edited `cli.py` docstring |
| 8 | Re-run the step 1 survey and re-classify, so the *no contradiction* claim is measured rather than asserted. | The second run's output in §3 |
| 9 | Run `check`, `index`, the suite and the tier-1 budget test. | Their output in §3 |

**Shape decision — the rule goes in `METHOD.md` §4, not in a phase file.**
§4 is where the hierarchy edge is defined, and the rule is a property *of that edge*: it binds
whenever a task closes, which is not inside any one phase's procedure. **Rejected: `review.md`**,
which is where a reader most often meets the consequence — but review is one of four phases and the
rule also binds on a task closed outside review, so a phase file would be a home that does not cover
its own subject. **Rejected: a new section of its own**, which would separate the rule from the edge
it is about and give a reader two places to look for one fact. `review.md` and `audit.md` then
*apply* it and name §4 as the source, which is what keeps them from being copies.

**Step 1 reads the full match list on purpose.** A filtered survey was tried first and missed
`review.md` line 24, because that line says *child* without any of the words a closure-shaped filter
would look for. The classification is what makes the sweep honest, not the pattern.

**Outputs**
- `plugin/skills/taskmd/docs/METHOD.md`
- `plugin/skills/taskmd/docs/method/review.md`
- `plugin/skills/taskmd/docs/method/audit.md`
- `plugin/skills/taskmd/taskmd/cli.py`

## 3. Implement

**Step 1 — the survey, and every match classified**

```text
$ find plugin -type f \( -name '*.md' -o -name '*.py' -o -name '*.sh' -o -name '*.ps1' -o -name '*.json' \) | wc -l
23
$ grep -rn -i "child" plugin --include=*.md --include=*.py --include=*.sh --include=*.ps1 --include=*.json | wc -l
31
```

23 files read, 31 matches, every one classified — the whole list, not a filtered one:

| Class | Matches | Where |
| :--- | :--: | :--- |
| **States the rule** | 2 | `cli.py` 222, 225 — `holds_open()`'s docstring |
| **Narrower, or an application** | 7 | `audit.md` 38, 43, 44, 77, 89, 90; `METHOD.md` 154 (§5) — all about an audit's umbrella |
| **Contradicts the rule** | 5 | `review.md` 18, 24, 39, 88; `METHOD.md` 37 (§2's `review` exit criterion) |
| **Unrelated** | 17 | `BINDING.md` 76, 78; `github-issues.md` 353, 466; `METHOD.md` 105, 118; `cli.py` 265, 279, 297–299, 395; `defaults/config.md` 290, 396; `schema.py` 227, 832, 834 — edge mechanics, derivation, and one child *process* |

2 + 7 + 5 + 17 = 31, so nothing was dropped between the count and the classification.

**One place that had to change carries no match at all.** `review.md`'s worked example closes with
*"Three met, one carried. The task closes"* — the single sharpest contradiction in the shipped
method, and the word *child* is not in it. It was found by reading the neighbourhood of match 88,
not by the pattern. **This is why the plan reads the full list and classifies it rather than
filtering**: a filtered sweep had already missed `review.md` line 24 for the same reason, and no
better pattern would have reached this one.

**Steps 2–7 — what changed**

- **`METHOD.md` §4** gains *A child holds its parent open*, immediately under the edge table: the
  rule, why hierarchy is the only edge that constrains closure, and the owner's decision of
  2026-08-22 with the measurement that rejected the narrower reading — three cases against zero on a
  218-task backlog. It links to no task, so it survives every record closing.
- **`METHOD.md` §4's *Which edge to use*** had **no hierarchy question at all** — it asked about
  dependency and soft and stopped. It now opens with one, and closes with *the residual is the case
  this gets wrong*: work that is *about* a finished task without being *part* of it takes a soft
  edge. That paragraph is the general form of what T-216 decided three times.
- **`METHOD.md` §2**, the `review` exit criterion: *carries a **child** task* → *carries a task*,
  with §4 named for which edge and whether the task may then close.
- **`review.md` step 3** now says which edge, and what each implies: a child where the outcome itself
  is incomplete and this task stays open; a soft link where the criterion asked for something beyond
  the outcome and this task closes honestly.
- **`review.md` step 4** keeps *the fix is a child task* and says why that is the right edge — a
  repair to the outcome is part of the outcome — so it now reads as an instance of step 3 rather
  than as an exception to it.
- **`review.md` step 6** gains *no child of it is open* as a closing condition.
- **`review.md`'s worked example** now shows the task **not** closing, and names the variant that
  would have closed. It teaches both branches, which the old one could not.
- **`audit.md` step 5** is left as an **application**: it names §4 as the source, does not restate
  the rule, and keeps only what is specific to an audit — that an umbrella closed over open children
  erases the link between examination and consequence.
- **`cli.py`'s `holds_open()`** said *work on a child proceeds while its **umbrella** waits*. The
  word is exactly the ambiguity that forced T-212 to escalate. It now reads *parent*, and cites
  METHOD §4 for the *every parent, not only an audit umbrella* half.

**Decisions & assumptions**

1. **The rule lives in `METHOD.md` §4** — 2026-08-22. It is a property of the hierarchy edge and it
   binds whenever a task closes, which is not inside any one phase. **Rejected: `review.md`**, where a
   reader most often meets the consequence — but review is one phase of four and a task can be closed
   outside it, so that home would not cover its own subject. **Rejected: a section of its own**, which
   would put the rule somewhere other than the edge it constrains and give a reader two places to
   look.
2. **`audit.md` step 5 stays as an application, not a pointer alone** — 2026-08-22. §1's scope allowed
   either. An application was chosen because the audit-specific *cost* — the link from examination to
   consequence — is a real fact with nowhere else to live, and deleting the step to leave a bare
   pointer would lose it. The rule itself is not restated there, so it is not a second copy.
3. **`review.md`'s worked example changes verdict rather than its criteria** — 2026-08-22. The
   alternative was to soften the example's failing criterion so the task could still close, which
   would have made the example agree with the text by removing the case the text is about.
4. **`cli.py` was edited although no criterion names it** — 2026-08-22. §1 lists it as an input and
   says it *"states the rule in full and qualifies it to nothing"*; the word *umbrella* is a
   qualification, and leaving it would leave the exact ambiguity this task exists to end sitting in
   the one place that had it right. Comment only — no behaviour changed, and the suite is quoted
   below.
5. **Nothing was written into `CLAUDE.md`** — 2026-08-22. The rule binds when a task closes, which is
   inside work the session knows it has started, so tier 2 is reachable by then. Adding it to tier 1
   would be paid on every turn of every session for a rule only a closing task needs.

**Step 8 — the survey, re-run**

```text
$ grep -rn -i "child" plugin --include=*.md --include=*.py --include=*.sh --include=*.ps1 --include=*.json | wc -l
35
```

**31 → 35, and the four are accounted for.** `review.md` went from 4 matches to 5 (+1: step 3's new
sentence naming the child branch); `METHOD.md` went from 4 to 7 (+3: the new subsection's heading and
two lines, less the §2 cell that no longer says *child*). Re-classified, the **contradicts** column is
now **empty**: `review.md` 23, 31, 38, 96, 99 and `METHOD.md` 109, 111, 112, 119 all state or apply
the rule with §4 named as its source, and `METHOD.md` 105, 145, 181 and every other file are the
unrelated set unchanged.

**Step 9 — the tool on itself**

```text
$ ./plugin/bin/taskmd check
OK - 218 task(s), 1090 field value(s), 3673 front-matter value(s), 721 reference(s), 25 dependency edge(s), 331 declared output(s), 1 index file(s), 207 closed record(s), 250 document(s), 3293 link(s), 4723 table row(s), 2 template(s), 10 template field value(s), 5 vocabulary row(s), 3667 section reference(s)
CHECK_EXIT=0

$ python -m pytest tests -q
325 passed, 8 subtests passed in 43.77s

$ python -m pytest tests/test_budget.py -q
8 passed in 0.04s
```

**Outputs produced**
- [`plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md)
- [`plugin/skills/taskmd/docs/method/review.md`](../plugin/skills/taskmd/docs/method/review.md)
- [`plugin/skills/taskmd/docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md)
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The rule is stated **once** in the method, and the decision records where and why, with the rejected location and its reason | met | `METHOD.md` §4, *A child holds its parent open*. §3 decision 1 records two rejected homes — `review.md`, which covers one phase of four, and a section of its own, which would separate the rule from the edge |
| `audit.md` step 5 is left as an application or a pointer, and a reader of either place can tell which is the source — no second copy of the rule | met | An application: it names `METHOD.md` §4 as the source in its own text, states no version of the rule, and keeps only the audit-specific cost. §3 decision 2 says why a bare pointer was rejected |
| The owner's ruling is cited where the rule now lives, with its date, so a later reader can find the argument without opening a closed task | met | The subsection carries the date, the rejected reading, and the measurement that settled it — three cases against zero over 218 tasks. It links to no task id, which is what makes it survive `T-212` and `T-216` closing, and what keeps it valid in an adopter's clone where those records do not exist |
| **No shipped document contradicts the rule**, and the set of places that spoke about it was found by a survey whose command and output are recorded — not from memory | met | §3 steps 1 and 8: both commands quoted, 23 files read, all 31 matches classified into four classes that sum to 31, then 35 re-classified with the *contradicts* class empty. The 31→35 delta is accounted for line by line |
| `check`, `index` and the suite are green, and the tier-1 budget test still passes | met | §3 step 9. `check` exit 0, `325 passed, 8 subtests passed`, `tests/test_budget.py` `8 passed` — run separately because §3 decision 5 turns on it |

**What review found beyond the table.** The survey's most useful result is the one the table cannot
show: **the sharpest contradiction in the method carried none of the words a search for it would
use.** `review.md`'s worked example ended *"Three met, one carried. The task closes"* — no *child*,
no *parent*, no *open*. It was found by reading around a neighbouring match. A pattern-based sweep of
this rule is not merely incomplete, it is systematically blind to the place where a method states a
rule by **demonstrating** it, which is where a reader is most likely to learn the wrong thing.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none. One arose during
`specify` and is answered in place, in §1's own paragraph: whether extending the scope to
`review.md` needed a further ruling from the owner. It does not — the owner settled the substance on
2026-08-22, and what remained was which documents change, which §1 already called this task's work.
Nothing is addressed to anyone else.

**Child fix tasks raised**
- none. Every criterion is met, so nothing is carried — which is the shape §4's new text now says
  lets a task close.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All five criteria met. The rule now lives once, in `METHOD.md` §4 beside the edge it constrains, with the owner's date and the measurement that rejected the narrower reading; `audit.md` applies it, `review.md` and `METHOD.md` §2 stopped contradicting it, and `holds_open()` no longer says *umbrella* where it means *parent*. **§1 and the criteria were extended mid-`specify`** on [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md)'s finding that two shipped documents instructed the state the rule forbids — recorded there rather than absorbed, with the reason it needed no further ruling. **Worked under the multi-phase grant recorded at the top of this Log.** |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that six tasks be worked with the full lifecycle, and later the same day **added this one**, after reading why the handoff's backward sweep raised it. **The set in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through `plan` → `implement` → `review` to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task, and in particular not [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), nor [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply. **The set is seven ids and not a description.** It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: the rule gets one home and `audit.md` step 5 must not become a second copy of it.** §1 puts that in scope as a decision to take; METHOD §4's *store the forward edge* rule is what forbids writing it twice, and no grant of phases licenses an exception. |
| 2026-08-22 | → proposed | Raised by the handoff's backward sweep, not by a task: the owner's ruling of 2026-08-22 was recorded in the two task records that needed it and in no shipped document, and both of those records are destined to close. `medium` and `s` — one rule, one home, one decision about `audit.md`, but the cost of losing it is that a rule the tool enforces has no written source. `adopter_visible` because the method ships. ~~**Not covered by the multi-phase grant of 2026-08-22**, which names six tasks by id and was given before this was found.~~ **Superseded later the same day** — the owner added this task to the grant on being shown why it was raised; the row above is the authorisation and this sentence records only what was true at the moment of raising it. |
