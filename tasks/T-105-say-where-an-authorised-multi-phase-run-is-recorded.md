---
id: T-105
title: Say where an authorised multi-phase run is recorded
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-005, T-036, T-047, T-063]
work_package: M3
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/docs/METHOD.md]
---

# T-105 — Say where an authorised multi-phase run is recorded

## 1. Specify

**Outcome**
When the owner waives *one phase per request* for particular tasks, the method says where that
authorisation is written — so two projects record it the same way and a later session can neither
miss it nor over-apply it.

**Why this one**
Raised as **R-7** by the first adopting project (`control/LOCAL-CONTEXT.md`), which calls it the
least of its seven and recommends nothing structural. METHOD §3.1 is the right default and that
project holds to it. It was also explicitly waived once, by the owner, for four small tasks. Nothing
in a task file can carry that, so the authorisation lived in a handoff document and in Log rows on
the tasks — and it had to say, in prose, which tasks it covered and that it did not generalise.

**The failure it leaves is two-sided.** An authorisation recorded outside the tracker can be missed —
the next session re-asks for permission already given — or applied to a task it never covered, which
is §3.1's rule silently disabled. Neither is visible.

**A waiver is state, and §3.1 is a rule about requests.** That tension is the whole of the question,
and it is why the answer is a sentence rather than a field: the rule says a pointer is context and
not authorization, and a waiver written into a file is precisely a pointer that later claims to be
authorization. Wherever it is recorded has to survive that reading.

**One constraint on the size of the answer.**
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) moves §3.1 into the
always-loaded tier. Anything added to it is then paid on **every turn of every session**, against a
budget that already does not pass. So this is one sentence in §3.1 if it must be there, or a
paragraph in a phase file if it need not be — and which of those it is, is the decision.

**Requirements served**
R-6 (`docs/SCOPE.md`) — a phase is worked only when it was requested, which is the rule being waived.
R-8, since an authorisation is exactly the kind of thing that must leave a trace.

**Scope**
- In: one sentence or paragraph saying where a waiver is recorded — the task's own log, naming who
  gave it and what it covers.
- In: whether it belongs in METHOD §3.1 itself or in a phase file, given the tier-1 cost above.
- In: whether a waiver may cover more than one task, and how that is written without becoming a
  standing permission.
- Out: a front-matter field for waivers. That stores an authorisation as task state, and the whole
  point of §3.1 is that state is not a request.
- Out: reopening the rule. It is right and this does not touch it.

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §3.1 and `docs/method/rationale.md`.
- [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md), for the budget any
  addition to §3.1 is charged against.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`, for what a task's log is here.

**Acceptance criteria**
- [ ] The method says where a waiver is recorded, in one place
- [ ] It says what the record must name — who gave it and which tasks it covers — so it cannot be
      read as general
- [ ] If it lands in §3.1, the tier-1 measurement in `CLAUDE.md` is re-run and the cost is stated
- [ ] `check` is clean on this repository

**Open questions**
- None. **Q1 — §3.1 or a phase file? — decided 2026-08-10 under the standing authorization: §3.1.**
  The waiver is met at the moment the rule is, and a reader carrying only tier 1 is exactly the
  reader who needs it — a rule that forbids something without saying what permits it sends that
  reader to a document they have not loaded. *Rejected: a paragraph in `method/implement.md`* — free
  for the always-loaded tier, and not read until after the moment it was needed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure tier 1 and `METHOD.md` before the edit, so the cost is a difference and not an estimate | Recorded figures in §3 |
| 2 | Write the two sentences into §3.1 | `plugin/skills/taskmd/docs/METHOD.md` |
| 3 | Re-measure, and state what the addition costs now and what it will cost once T-047 lands | Recorded figures |
| 4 | Reconcile the sentence already published in `README.md` with the rule now written in METHOD | A decision, and the two shown to agree |
| 5 | `index`, `check`, suite, pre-publish check | Recorded output |

Step 4 exists because this task's own log found that half the answer was **already published**: the
README's worked-examples table says asking for the whole lifecycle is what authorizes it, while
METHOD — the document that states the rule — said nothing about granting or recording one. A task
that writes the missing half without looking at the published half produces two statements of one
fact, which is what this method exists to prevent.

**Shape decisions.**

**D1 — Two sentences, in the paragraph that already says what is *not* authorization.** §3.1's
existing text is entirely negative: a pointer, a resumption note, an unfinished checklist, the rhythm
of the last three tasks — none of these is a request. It never says what one *is*. The addition is
the positive counterpart in the same place, which is why it reads as a completion rather than an
appendix. *Rejected: a subsection of its own* — a heading costs more than the text under it and
implies a procedure where there is a sentence.

**D2 — METHOD says "the task's own record", never "the log".** *Record* is a role (§6); which
artifact plays it is the binding's to say, and the local-Markdown binding already assigns it — the
task file, and its log in particular. Naming the log here would put a backend word in the
backend-neutral document and would be a second copy of an assignment that already exists. *Rejected:
adding a matching line to the binding* — nothing to add; the mapping is already there.

**D3 — It says what the record must name, and does not say "it does not generalise".** Requiring the
record to name *what it covers* carries that, and the third clause would be a third sentence in the
one place this project pays for every turn.

**Planned outputs**
- `plugin/skills/taskmd/docs/METHOD.md` — §3.1

## 3. Implement

### Steps 1–3 — the edit, and what it costs

```text
                     before    after
tier 1               12736     12736      the flat alternative it must stay under: 7919
METHOD.md             8078      8382      +304 characters
```

**Tier 1 does not move today, and the reason matters more than the number.** §3.1 lives in
`METHOD.md`, which is tier 2 — the always-loaded set is `CLAUDE.md` plus the served skill's
`description`, and neither changed. What
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) will do is move §3.1
into tier 1, and **at that point these 304 characters are billed on every turn of every session**,
against a budget that already fails by 4817. So the cost is real, deferred, and known in advance
rather than discovered by T-047 — which is why criterion 3 asked for the measurement rather than for
a promise to keep it short.

### Step 4 — the half that was already published

`README.md`'s worked-examples table has carried this since it was written:

> *Take T-014 through to done* — Asking for the whole lifecycle is what authorizes it: specify, plan,
> implement, review, in that order.

Checked against the new text, and the two agree: a request for the whole lifecycle authorizes it, and
the phases still run in order. **The README row stays.** It is an *example* — the table's whole shape
is "what you say" against "what happens" — and its authority is now §3.1 rather than nothing. The
alternative was to cut it down to a pointer at METHOD; rejected, because the README is read by
someone who has installed nothing, and a front door that answers a question with a citation to a
document the reader cannot open has not answered it.

What the README does **not** say, and should not, is where the authorization is written down. That is
an instruction to whoever is doing the work, not a description of what the user gets.

### Step 5 — this repository

```text
Ran 167 tests in 6.525s                                                                      OK
```

No test was added or removed: this task changed one document and no behaviour.

**The rule was in use before it was written.** Four waivers were given in this session — one covering
[T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) and
[T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) together, then one each for
[T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md),
[T-101](T-101-report-a-template-the-create-path-cannot-see.md) and
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) — and each was recorded in the shape
the report recommended, naming who gave it, which tasks it covered, and that it did not generalise.
Five task records carry such a row. So what §3.1 now says is not a proposal: it is a description of
something that ran five times and was legible enough to cite from a sixth task, which is the only
evidence a rule about record-keeping can have.

**Decisions & assumptions**

- **No guard test.** — [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) added one for
  a constraint that leaves no evidence anywhere, so its documentation vanishing would be silent. This
  is the opposite: every waiver leaves a row in a task record, so a rule that quietly disappeared
  would be contradicted by the tree itself. Considered and not done rather than not considered. —
  2026-08-10
- **Nothing structural, exactly as the report recommended.** — No field, no status, no command. A
  waiver is an authorization about a *request*, and storing it as task state would make it a pointer
  — which is the thing §3.1's own first paragraph says is not authorization. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/docs/METHOD.md` — §3.1, two sentences

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The method says where a waiver is recorded, in one place | met | §3.1, in the paragraph that already said what is *not* authorization. **D2**: it says *the task's own record*, a role, leaving the artifact to the binding that already assigns it. |
| It says what the record must name — who gave it and which tasks it covers — so it cannot be read as general | met | Both named. **D3** records why "it does not generalise" is not a third clause: naming what it covers carries it, and §3.1 is the one text billed on every turn once T-047 lands. |
| If it lands in §3.1, the tier-1 measurement in `CLAUDE.md` is re-run and the cost is stated | met | §3 steps 1–3: re-run, **unchanged at 12736** — because §3.1 is tier 2 until T-047 moves it — and the deferred cost stated as the +304 characters T-047 will inherit, against a budget already failing by 4817. |
| `check` is clean on this repository | met | §3 step 5, and the suite unchanged at 167. |

**Child fix tasks raised**
- none. Step 4's finding was reconciled inside this task rather than raised, because the README
  sentence is this task's own subject rather than a separate defect — it is *the answer, published in
  the wrong place*, and leaving it to a child would have meant closing this one while the duplication
  it exists to resolve was still open.

**Verdict.** All four criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-10 | → done | Reviewed against the four criteria as written; **all four met, none carried**, so the task closes. Criterion 3 is the interesting one: the tier-1 measurement was re-run and is **unchanged at 12736**, because §3.1 lives in `METHOD.md` which is tier 2 until [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) moves it — so the honest answer is not "it cost nothing" but "+304 characters that T-047 will inherit, on a budget already failing by 4817". Stated that way so T-047 meets a known figure rather than a surprise. No child raised, and the reason is recorded: the README sentence step 4 found is this task's own subject rather than a separate defect, so leaving it to a child would have closed this task with the duplication it exists to resolve still open. `deliverables` names the one file. Pre-publish check run last, after this record was written: **193 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken. **The rule was in use before it was written**, which is the strongest thing this record has: four waivers were given in this session and each was recorded in the shape R-7 recommended, before §3.1 said anything about it — five task records carry such a row, and they were legible enough to cite from this task. So what landed is a description of something that ran, not a proposal. Step 4 was the plan's own addition and it earned its place: half the answer was already published in `README.md`'s worked-examples table, and a task writing the missing half without looking would have produced two statements of one fact. Checked, they agree; the README row **stays**, because it is an example and its reader has installed nothing, so answering them with a citation to a document they cannot open is not an answer. **D2** keeps METHOD saying *the task's own record* rather than *the log* — record is a role, and the local-Markdown binding already assigns it, so naming the log here would put a backend word in the backend-neutral document. A guard test was considered and deliberately not added: unlike T-106's constraint, every waiver leaves a row in a task record, so a rule that quietly vanished would be contradicted by the tree itself. |
| 2026-08-10 | → planned | Plan written; Q1 answered under the standing authorization — **§3.1**, because the waiver is met at the moment the rule is, and a reader carrying only tier 1 who is told what is forbidden without being told what permits it has been sent to a document they have not loaded. Rejected: `method/implement.md`, free for the always-loaded tier and not read until after the moment it was needed. **D1** puts the text in the paragraph that already lists what is *not* authorization — §3.1's existing text is entirely negative and never says what a request *is*, so this reads as the completion of that paragraph rather than as an appendix. **D3** leaves out "it does not generalise" as a third clause: requiring the record to name what it covers already carries it. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"keep going with T-105, full lifecycle"*. It covers this task alone and **does not generalise**; the fifth such waiver in this session, and the last one given before the rule about recording them existed. |
| 2026-08-10 | (no change) | **Two things this task did not have when it was raised, both found the same day and neither actioned here.** First, it now has live specimens rather than a second-hand report: the maintainer waived §3.1 for [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) and [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) — *"move on in the suggested order. Full lifecycle."* — and each task carries a log row naming who gave it, which tasks it covers and that it does not generalise. That is R-7's own recommended shape, applied once, so `specify` can judge a real record instead of a proposal. Second, **part of the answer is already published and in the wrong place**: `README.md`'s worked-examples table says *"Asking for the whole lifecycle is what authorizes it: specify, plan, implement, review, in that order."* So the front door already tells a reader how a waiver is granted, while METHOD — the document that states the rule — says nothing about granting or recording one. That is a fact for `specify` to reconcile, and it narrows the task: the question is now where the existing sentence's other half belongs, not whether to invent one. Surfaced under METHOD §3.3 rather than fixed, since fixing it here is the phase this task has not reached. |
| 2026-08-10 | → proposed | Raised as R-7 from the first adopting project's recommendations, which ranks it last of seven and asks for nothing structural. `medium` because the failure is silent in both directions — a later session can miss a permission already given, or apply it to a task it never covered — and `xs` because the whole work is a sentence and where to put it. Two things recorded here rather than left to `specify`: a waiver is *state* while §3.1 is a rule about *requests*, which is why the rule's own "a pointer is context, not authorization" line has to survive whatever is written; and T-047 moves §3.1 into the always-loaded tier, so anything added there is billed on every turn against a budget that already does not pass. That is the constraint on the size of the answer, and it is what makes the placement a decision rather than a formality. |
