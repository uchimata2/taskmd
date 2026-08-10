---
id: T-103
title: Say whether a closed task's declared output may be repointed when the file moves
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-053, T-076, T-083, T-089, T-090, T-092]
work_package: v0.3
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/docs/METHOD.md, plugin/skills/taskmd/docs/bindings/local-markdown.md]
---

# T-103 — Say whether a closed task's declared output may be repointed when the file moves

## 1. Specify

**Outcome**
A project reorganising its files knows, from a document rather than from first principles, whether
editing a closed task's declared path preserves its record or falsifies it.

**Why this one**
Raised as **R-5** by the first adopting project (`control/LOCAL-CONTEXT.md`). `check` reports a
declared deliverable path that does not exist, including on a `done` task — correctly, since
`deliverables` asserts production. The consequence is that anything a closed task declared is
**frozen in place**: move it and the project owns a permanent `MISSING OUTPUT`; leave it and the
project cannot reorganise. The only third option is editing a closed record, and nothing says whether
that is allowed.

That project met the choice twice. Complying with the template-location rule meant moving two files
that three closed tasks declared, and it had already refused the same trade once, leaving two
superseded tools on disk rather than invalidate a closed record. It settled on *updating the path
preserves the record, because the file still exists and the task still produced it* — the declaration
names an artefact, not a location in amber. That reasoning is sound and it is **theirs**, derived
under time pressure, with nothing to lean on.

**This is the third case of one question and the only one with no home.**
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) settled what an
**open** task's declared outputs assert;
[T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) is open for the **cancelled**
case. The closed-and-moved case is neither, and it is the one every project reaches the first time it
reorganises — which is also the moment it is least willing to stop and think.

**The record-integrity rule is what makes it a real question.** A closed task is evidence; the
project's own habit is to annotate rather than rewrite, and a reconcile sweep that edits a stale
statement can destroy the thing an audit produced. Whether a path is a *statement about the past* or a
*pointer to a present artefact* is precisely what has to be decided.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, which is the question: whether the closed record or the
filesystem is the home of where an artefact lives. R-16, since whatever is decided is what `check`'s
`MISSING OUTPUT` is then claiming.

**Scope**
- In: whether a closed task's `deliverables` may be edited to follow a moved file, and what the edit
  owes — a log row, nothing, or a rule about which fields may move after closing.
- In: which document says it. The field name is the binding's, the principle is the method's.
- In: what a project does when the artefact is genuinely gone rather than moved, since that is the
  case the frozen reading is protecting.
- Out: changing what `check` reports. It reports a declared path that is missing, and that is right
  under either answer.
- Out: the cancelled case — [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md).
- Out: the open case, settled by
  [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md).

**Inputs**
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, the closing-conditions paragraph — the one
  place that already says `deliverables` asserts production.
- `plugin/skills/taskmd/docs/METHOD.md` §1 rule 5 and §6.
- [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), for the argument
  already made about what the field asserts and when.

**Acceptance criteria**
- [ ] The answer is written in exactly one document, with the rejected alternative recorded
- [ ] It covers a moved artefact and a deleted one, since the two look identical to `check`
- [ ] An adopter meets it where the question arises — reading it should not require knowing the
      answer exists
- [ ] Nothing else in the tree states a second version of it, checked against the whole tree rather
      than the file that was edited
- [ ] `check` is clean on this repository, and the suite still passes if any code changed

**Open questions**
- None. Both settled 2026-08-10 under the standing authorization, and the second changed the first.

  **Q2 — is the answer yes? — yes for a move, and *no* for a deletion.** The two are one question in
  the specify because `check` cannot tell them apart; they are two answers because a project can. A
  move leaves the assertion true and changes only how it is written; a deletion makes it false, and a
  closed task whose outcome no longer exists is a thing to know rather than a message to clear.
  *Rejected: closed records are immutable* — see §3, where this repository turns out to have answered
  the move case twice already, at scale.

  **Q1 — which document? — METHOD §1 rule 5 for the principle, the binding for the application; and
  the recommendation's §6 was the wrong half of METHOD.** §6 is about where a fact *lives*. This is
  about whether a closed record may be *edited*, which rule 5 already half-answers with the words
  *its record is current* — it just never says that *current* keeps binding after closing, which is
  precisely the doubt. So the clause goes there. *Rejected: the binding alone* — the adopting
  project's question was whether a closed task may be edited at all, which is method-level and would
  be answered again, differently, by the next backend.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Find out what this repository already does, since it has reorganised twice since tasks started closing | Recorded evidence in §3 — and it may settle Q2 |
| 2 | Write the principle where rule 5 already half-states it | `plugin/skills/taskmd/docs/METHOD.md` §1 rule 5 |
| 3 | Write the application, including the deletion case, in the binding that owns the field and the validator | `plugin/skills/taskmd/docs/bindings/local-markdown.md` |
| 4 | Check the **whole tree** for a second statement of the rule, not the two files just edited | A recorded grep |
| 5 | Suite, `index`, `check`, pre-publish check | Recorded output |

Step 1 is first because a decision task whose answer is already this project's unwritten practice is
a **ratification**, and one that contradicts it is a change — and those are different tasks with
different obligations. Step 4 is separate from step 3 because the criterion is about the tree and a
claim about a whole artefact is not answered by the part just edited.

**Shape decisions.**

**D1 — The line is what resolves the pointer, and it is a line this project has already drawn.**
[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) decided that a Markdown link is
a reference and a path in prose is not, on the ground that a task record is *a dated statement, not a
promise*. `deliverables` sits on the checked side of that line — `check` resolves it — so it is a
live pointer, and the body sits on the other side and stays as written. The answer therefore costs no
new principle: it applies an existing one to a field nobody had asked about.

**D2 — The deletion case is stated as loudly as the move case.** Without it the rule reads as
*repoint until check is quiet*, which would turn a closed task's outcome vanishing into a
bookkeeping step. §1's scope asked for it; **D1** is why it is not simply the same answer.

**Planned outputs**
- `plugin/skills/taskmd/docs/METHOD.md` — §1 rule 5
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the closing-conditions section

## 3. Implement

### Step 1 — this repository has answered the move case twice, and never wrote it down

[T-002](T-002-implement-the-core-cli-context-index-check.md) closed on **2026-08-05**, declaring the
CLI it built. Its `deliverables` today read `plugin/skills/taskmd/taskmd/cli.py` — a path that did
not exist until [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) made
`plugin/` a subtree, and was rewritten again by
[T-083](T-083-make-the-skill-directory-self-contained.md). The file's history shows both:

```text
7bc7742 Close T-083: one copied folder is a working skill
7fed526 T-053: the plugin becomes a subtree, and the boundary becomes structural
```

So a closed task's declared outputs have been repointed here, twice, at scale — T-053's own record
counts 26 `MISSING OUTPUT` lines from `deliverables:` front-matter that it had not planned for.

**And the same operation deliberately left the bodies alone.** T-053's log: *"Left alone: ~646
backticked prose mentions of old paths inside closed records, which break nothing and would be a mass
edit of closed evidence."* Two other closed tasks say the same thing in their own words —
[T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) and
[T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) both record refusing to edit a
closed task's evidence to match a later fact.

That is **D1**'s line, already being walked: front-matter followed the files, prose did not. The
practice was consistent across three tasks and four months of work, and no document said it — which
is why the adopting project had to derive it twice from first principles and could reasonably have
derived the opposite.

### Steps 2–3 — where it is written

METHOD rule 5 gains one clause: *current* keeps binding after a task closes — correct what the record
says about the present, never rewrite what it says about the past, annotate that instead. That is the
whole of the method-level answer, and it is a completion of a sentence rule 5 already started.

The binding says what it means here, in the section that already assigns rule 5's closing conditions:
declared outputs follow the artefact, the implement section does not, and a **deletion** is not a
move and must not be repaired as one.

### Step 4 — the whole tree, not the two files

```text
grep -rnE "follow the artefact|dated statement|closed record" plugin/ README.md docs/ CLAUDE.md
  plugin/skills/taskmd/docs/bindings/local-markdown.md:58  the new rule
  plugin/skills/taskmd/docs/bindings/local-markdown.md:62  the new rule
  README.md:106                                            T-092, on bare paths in prose
```

One statement of the rule. The README line is the *same principle answering a different question* —
whether a bare path in prose is a reference — and the binding cites T-092 by name so the relationship
is visible rather than coincidental.

### Step 5 — the suite and this repository

```text
Ran 167 tests in 6.543s                                                                      OK
```

Unchanged, and expected to be: no behaviour moved. `check` is clean, which it already was — this task
does not stop a `MISSING OUTPUT` being reported, it says what to do when one appears.

**Decisions & assumptions**

- **Nothing about `check` changed, and the task never proposed to.** — It reports a declared path
  that is missing, which is right under both halves of the answer. What was missing was a project
  knowing which half it was in. — 2026-08-10
- **The ratification is stated as one.** — Writing this as a fresh decision would have hidden that
  the project had already chosen, twice, and that the choice survived two reorganisations. A rule
  with that provenance is stronger than one argued from scratch, and the provenance is now findable.
  — 2026-08-10
- **Assumption, recorded as one: the GitHub binding needs no matching paragraph.** — Nothing there
  resolves a declared path, so the *live pointer* half has no mechanism to attach to; rule 5's clause
  governs it regardless. If that binding ever gains a validator, this is the paragraph it will need.
  — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/docs/METHOD.md` — §1 rule 5, one clause
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — two paragraphs

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is written in exactly one document, with the rejected alternative recorded | met | The answer — may a closed task's declared output be repointed — is in the binding, once. METHOD gains the *principle* it rests on, which is a broader fact and not a second copy: change either and the other stays true. Rejections in Q1 and Q2. |
| It covers a moved artefact and a deleted one, since the two look identical to `check` | met | Two paragraphs, and **D2** records why the second is stated as loudly as the first: without it the rule reads as *repoint until check is quiet*. |
| An adopter meets it where the question arises — reading it should not require knowing the answer exists | met | The binding paragraph sits in the section that assigns rule 5's closing conditions, which is where `deliverables` is defined and where a reader chasing a `MISSING OUTPUT` lands. |
| Nothing else in the tree states a second version of it, checked against the whole tree rather than the file that was edited | met | §3 step 4, the grep and its three hits. The one outside the new text is T-092's answer to a different question, and the binding names T-092 so the two read as one line rather than two rules. |
| `check` is clean on this repository, and the suite still passes if any code changed | met | `Ran 167 tests … OK`, unchanged because no code moved. |

**Child fix tasks raised**
- none.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. Criterion 1's "exactly one document" is met and the reading is stated rather than assumed: the *answer* is in the binding, once, and METHOD gains the broader *principle* it rests on — change either and the other stays true, so they are not two copies. Criterion 4 was checked over the whole tree rather than the two files edited, and its one outside hit is T-092 answering a different question with the same principle, which the binding now names so the two read as one line. No children. `deliverables` names the two documents. Pre-publish check run last, after this record was written: **193 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken, and **step 1 turned the task from a decision into a ratification**. T-002 closed on 2026-08-05 and its `deliverables` today read `plugin/skills/taskmd/taskmd/cli.py` — a path that did not exist until T-053, and that was rewritten again by T-083. So a closed task's declared outputs have been repointed here twice, at scale; T-053 counted 26 `MISSING OUTPUT` lines from front-matter it had not planned for. **The same operation deliberately left the prose alone** — T-053's log records ~646 backticked path mentions inside closed records left untouched as "a mass edit of closed evidence", and T-049 and T-050 each independently refused to edit a closed task's evidence to match a later fact. That is exactly D1's line, walked consistently across three tasks and never written down, which is why the adopting project derived it twice from first principles and could as easily have derived the opposite. Q2's answer splits: **yes for a move, no for a deletion** — `check` cannot tell them apart but a project can, and repointing a deleted output would turn a closed task's outcome vanishing into a bookkeeping step. Nothing about `check` changed; the suite is unchanged at 167 because no behaviour moved. |
| 2026-08-10 | → planned | Plan written; both open questions settled under the standing authorization, and **the second changed the first**. Q1's recommendation had named METHOD §6, which is about where a fact *lives*; the question is whether a closed record may be *edited*, and rule 5 already half-answers it with the words *its record is current* — it simply never says that *current* keeps binding after closing, which is the whole of the doubt. So the clause lands in rule 5 and §6 is untouched. **D1** is the plan's own finding: T-092 already drew the line this needs, between a Markdown link and a path in prose, on the ground that a task record is a dated statement rather than a promise — and `deliverables` sits on the checked side of it. The answer therefore costs no new principle. Step 1 was placed first because a decision that ratifies existing practice and one that overturns it are different tasks with different obligations, and nothing said which this was. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"Keep going with T-103, full lifecycle"*. It covers this task alone and **does not generalise**. The first waiver recorded under the rule [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) wrote into §3.1 rather than ahead of it. |
| 2026-08-10 | → proposed | Raised as R-5 from the first adopting project's recommendations, where it arrived twice and was answered from first principles both times with nothing to lean on. `high` because it is the first question a reorganising project hits and the two live projects have already answered it differently — one leaving superseded files on disk to protect a closed record, then updating paths in the other direction; `s` because the work is a paragraph and a rejected alternative, not code. Placed in v0.3 with the other method-settling items rather than v0.2, which is about the tool holding up in another project. Recorded so `specify` does not re-derive it: this is the third case of one question — T-089 settled the open case, T-090 carries the cancelled one — and it is the only one with no home. |
