---
id: T-109
title: Decide whether a task that settles a question must be typed decision
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-088, T-090, T-093, T-097, T-098, T-103, T-104]
work_package: M2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/defaults/config.md]
adopter_visible: no
---

# T-109 — Decide whether a task that settles a question must be typed decision

## 1. Specify

**Outcome**
`list --type decision` either answers *what is waiting on a decision* or is known not to, so nobody
reads a short answer as a complete one.

**Why this one**
Found in the project status review of 2026-08-10 and raised so it is not lost with the session. Six
open tasks have question-shaped titles; two carry `type: decision` and four carry `type: fix`:

```text
T-021  decision  Settle what the context closing line may say
T-030  decision  Settle the schema module's own entry point
T-090  fix       Decide what a cancelled task's declared outputs assert
T-093  fix       Decide whether check resolves a section reference
T-097  fix       Decide whether a published document may point at a file no clone receives
T-098  fix       Decide who checks the links in a document only a successor reads
```

So the filter returns a third of them, and the third it returns is not distinguishable by anything a
reader can see. **It was raised in the review and the maintainer did not act on it** — recorded here
as a parked question rather than pressed, because a question nobody wrote down is one the next review
finds again from scratch.

**Neither typing is obviously wrong, which is why this is a decision and not a fix.** A task whose
*outcome* is an answer is a decision; a task that will also change a file once the answer is known is
plausibly a fix. All four of the mistyped set are both. The value has no stated test.

### The maintainer's steer, 2026-08-10 — and the angle it opens

**Carrying an unanswered question does not make a task a decision.** Stated by the maintainer against
this task's own first recommendation, and it is the right correction: every task carries open
questions at `specify`, so a test that fires on "has a question" fires on nearly everything and
distinguishes nothing. Whatever test the value gets has to be about the task's *outcome*, not about
its uncertainty.

**But there is a real distinction underneath, and it is one of degree.** When a task has more
questions than answers, or when its questions could change its scope *significantly*, it is a
different kind of work from one that merely has a detail to settle — closer to a **spike** in the
agile sense: work undertaken to reduce uncertainty, whose product is knowledge rather than the thing
itself. That is worth researching from that perspective, alongside the narrow typing question.

**The research is deliberately not done here**, and is `plan`'s to carry out.

**Two constraints on it, and the second is the one that will be tempting to skip.**

- taskmd tracks **any kind of work, not only software** (R-9): the method assumes no code, no tests,
  no version control, and reads for a research question, a talk, a training course or an ops runbook.
  Software projects are welcome and supported — the maintainer's words — but they are not the case
  the vocabulary is shaped around.
- So *spike* is an input, not a candidate name. It is a software word carrying a software practice's
  assumptions, and `docs/BRIEF.md` already lists what that costs: **an imported convention carries
  its author's assumptions.** If the concept survives the research, it needs a name a training
  course would recognise. The question the research answers is whether the **distinction** is real
  and worth a vocabulary value, not whether taskmd should adopt someone else's word for it.

**It matters more since [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md).**
That task settled that a decision lives in the task it belongs to, and that a register of taken
decisions is a view of those tasks. A view nobody can build — because the tasks holding decisions are
not identifiable — is a weaker answer than it reads as.

**Requirements served**
R-1 (`docs/SCOPE.md`) — a fact with one home is only useful if the home can be found. R-11, since
whatever is decided is a statement about what a vocabulary value means, which is configuration.

**Scope**
- In: whether the `decision` value carries a test, and what it is.
- In: retyping the four, or leaving them, as the decision requires.
- In: **every task the test disagrees with, in both directions** — a task typed `fix` that the test
  makes a `decision`, *and* a task typed `decision` that the test does not. The four above were found
  by looking at question-shaped titles, which can only find one direction; a filter that returns
  something wrong under-answers exactly as badly as one that misses something. Found by a sweep whose
  reach is recorded, not by re-reading the six.
- In: **closed tasks**, on the same terms — `list --type decision` is also how the register of taken
  decisions is built ([T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md)),
  so a filter that is right only about open work answers half the question.
  [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) is what says whether
  that edit preserves a closed record or falsifies it; applying its line to `type` is this task's, not
  a re-opening of it.
- In: whether the shipped schema's `type` row gains a word about it — the vocabulary is documented
  there and currently says nothing about what any value means.
- In: **the uncertainty-reducing kind of work**, per the maintainer's steer above — whether a task
  whose questions outnumber its answers, or whose questions could move its scope, is a distinct kind
  worth naming, and whether the agile *spike* is a useful comparison or a misleading one for a method
  that is not about software. Researched at `plan`, not here.
- Out: adding a field. A task that is both a decision and a fix does not need two type values; if the
  vocabulary cannot express it, that is the answer, not a schema change.
- Out: `decision` being removed. It stays; this is about when it applies and whether it has company.
- Out: adopting *spike* as a value name. If the concept lands, its name is chosen for a reader who has
  never shipped software — the word is an input to the research, never its conclusion.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Vocabularies*, and the pointer T-104 added.
- The six tasks above.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md), the last time
  a `type` value's meaning was settled — the argument there was drift between the method's word and
  the schema's field.
- [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md), for what a closed
  record may have corrected in it and what it may not.

**Acceptance criteria**
- [ ] The test for `type: decision` is written down, or it is recorded that there is none and why
- [ ] Every task the test disagrees with is retyped, found by a sweep of **all** tasks in both
      directions whose reach is stated — how many rows were read, not how many were changed
- [ ] The second kind of work is settled either way: a value with its own test and the tasks that
      carry it, or a recorded finding that the distinction does not survive outside software, with
      what was read to decide that
- [ ] `list --type decision` is run afterwards and its answer stated, so the claim is measured rather
      than asserted
- [ ] `check` is clean on this repository

**Open questions**
- **Q1 — Does `decision` mean "the outcome is an answer"? — yes, and it wins over `fix` when a task
  is both. Settled at `specify` on 2026-08-11 under the standing delegation.** The test a reader can
  apply: **read the task's stated outcome — if it is an answer someone else could act on, the type is
  `decision`, whatever the task also changes.** Underneath it is one property: a `decision` cannot
  name what it will change until it has answered something, so the answer is the product and the edit
  is downstream; a `fix` knows the change in advance and the work is making it. All four below are
  genuinely both, and `decision` wins because the answer is what somebody is waiting on.
  *Rejected: leave the value untested and say so* — cheap and honest, and it leaves a vocabulary value
  that finds nothing, which is the defect
  [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) was raised to
  remove. The cost of the recommended answer is field edits and a sentence; the cost of the
  alternative is a filter nobody can trust, paid every time someone runs it.

  **Already rejected by the maintainer on 2026-08-10: "a task with open questions is a decision"** —
  this task's own first recommendation, and wrong, since every task has open questions at `specify`.
  The test above is about the outcome, not the uncertainty, which is what that correction asked for.
- **Is there a second kind of work here, and does it need a name?** Raised by the maintainer with the
  steer above: a task whose questions outnumber its answers, or whose questions could significantly
  move its scope, may be a different kind rather than a badly-typed one. *No recommendation yet — the
  research it needs has deliberately not been done.* Whoever plans this weighs whether the
  distinction survives outside software at all, since a training course and an ops runbook are the
  cases the vocabulary has to read for.

  **Carried out on 2026-08-11: it is now [T-131](T-131-decide-whether-a-question-heavy-task-is-a-different-kind-of-work.md).**
  This task closed with the question live, and a closed record is outside every sweep this project
  runs — so it sat here unread until a hand sweep during a handoff found it.
  [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) is the mechanism question that came
  from the same find. The bullet is left as written, because it is what was true when the task
  closed; only its destination is added.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Research Q2 — is *work whose product is knowledge* a distinct kind for a method that is not about software? Read what the vocabulary already offers (`research`, `analysis`, `decision`) against the cases R-9 names: a training course, an ops runbook, a research question. | A recorded finding in §3 — the distinction survives with a name and a test, or it does not, with what was read either way |
| 2 | Sweep **all** tasks against the Q1 test in both directions, from `list`'s own output rather than by re-reading the six. | A table in §3 of every disagreement, plus the number of rows read |
| 3 | Apply [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md)'s line to `type` and record it as a decision before editing anything closed. | A recorded decision in §3: whether retyping a closed task corrects its present or rewrites its past |
| 4 | Retype what step 2 found, closed tasks included or excluded per step 3. | Edited `type` in the front-matter of the named task files |
| 5 | Write the test where the vocabulary is documented, in the prose that already qualifies `audit` and `research`. | `plugin/skills/taskmd/taskmd/defaults/config.md`, §*Vocabularies* |
| 6 | Check the **whole tree** for a second statement of what `decision` means — the method files T-104 touched are the likely site. | A recorded grep, with its pattern and its reach |
| 7 | `list --type decision`, `index`, `check`, and the suite. | Recorded output in §3 |

Step 1 is first because it can invalidate steps 2–5: a second value means the sweep sorts into three
buckets, not two, and the vocabulary row gains a value rather than a sentence. Step 3 is separate
from step 4 because editing 108 closed records is the irreversible half, and the rule permitting it
should exist before the edits and not be inferred from them. Step 6 is separate from step 5 for the
reason T-103's step 4 was: a claim about the tree is not answered by the file just edited.

**Shape decisions.**

**D1 — The test's home is the shipped config, not the method.**
[`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) opens by saying it names no field, so it cannot
own the meaning of a field *value*; the vocabulary table's surrounding prose already carries exactly
this kind of sentence for `audit` and `research`. *Rejected: METHOD §5, beside `audit`* — that
paragraph describes a kind of **work** the method has an opinion about, and putting a `type`-value
test there would re-create the drift T-088 was raised to close.

**D2 — The sweep reads `list`, not 123 files.** `list` prints id, status, work package, phase and
title, and the Q1 test is applied to the stated outcome, which a title carries or fails to carry
visibly. Where a title is ambiguous the file is opened — the ambiguous ones are the finding, so they
are named in §3 rather than resolved silently. *Rejected: open every task file* — proportionate to
nothing, and it hides which rows were actually judged behind a claim that all of them were.

**D3 — Adding prose does not touch the row.** Step 5 writes a sentence above the vocabulary table and
leaves the `type` row's values as they are, so no adopting project's copy drifts from the shipped
default. If step 1 lands a **value**, that stops being true and the change belongs to
[T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md)'s question rather
than to this task's assumption — which is the second reason step 1 is first.

**Planned outputs**
- plugin/skills/taskmd/taskmd/defaults/config.md
- the retyped task files, named individually in §3 once step 2 has found them

## 3. Implement

### Step 1 — the second kind does not survive, and the reason is that `type` has to hold still

**Finding: no new value.** What the maintainer named — *work whose product is knowledge rather than
the thing itself* — is a real distinction, and the shipped vocabulary already draws it: `research`,
`analysis` and `decision` sit on the knowledge side, `deliverable` and `fix` on the other. The steer's
proposed test is what does not survive.

**The test offered was "questions outnumber answers, or could move the scope significantly", and that
is a measure of uncertainty, not of outcome.** Two things follow. First, it is the same shape as the
test the maintainer had already rejected on 2026-08-10 — *carrying an unanswered question does not
make a task a decision* — differing only in degree, and a threshold does not repair a test that is
measuring the wrong quantity. Second, and decisively: **uncertainty moves and `type` does not.** The
proportion of questions to answers is high at `specify` and zero at `review`, so a task carrying such
a value would be that kind on Monday and not on Friday, and every view built on it would be reporting
a state the task has left. This method already has two fields for what moves — `phase` says where the
work has got to, `status` whether it can move (METHOD §2) — and a third one wearing a type's clothes
is the duplication rule failing in the schema rather than in a document.

**The *spike*'s distinguishing feature is the one thing this method has decided not to track.** Read
as a practice rather than as a word: a spike is knowledge-work that is **timeboxed**, because a team
must commit to an estimate at the end of a sprint. Remove the timebox and what is left — *find out
before you build* — is `research`. And the timebox itself cannot come along: `plan` states that
effort, duration and sizing are not tracked by this method, so the property that separates a spike
from research is unrepresentable here by an existing decision.

**Checked against R-9's cases, which is where an imported convention usually breaks.** A course
designer who does not know what the audience already knows runs a **needs analysis**; an ops team that
does not know whether failover works runs a **test** and writes up what happened; a researcher with
more questions than answers is doing **research**. Each has a name its own field would recognise, and
each lands on a value already in the row — which is the answer to the constraint that the name had to
read for someone who has never shipped software. No case was found where a task's product is
knowledge and none of `research`, `analysis` or `decision` fits.

*Rejected: add a value for it anyway, on the ground that the maintainer saw something.* They did, and
it is recorded above rather than dismissed — but a value whose test fires on a task's state instead of
its outcome would have to be re-evaluated every time the task is touched, and a vocabulary row is the
most expensive place in this project to be wrong: it is copied into every adopting project's
`.taskmd/config.md`, where changing it later is that project's problem and not this one's.

**Consequence for the plan: D3 holds.** No value is added, so step 5 writes prose above the table and
the `type` row's values are untouched — no adopting project drifts from the shipped default, and
[T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md)'s question is not engaged.

### Step 2 — the sweep, and what it read

**Reach first.** The corpus was partitioned by running `list --type` once per value, and the counts
sum to the whole tree, so no row went unread:

```text
analysis 3   decision 22   deliverable 11   research 1   fix 81   admin 3   audit 2   = 123
```

`check` reports 123 tasks, so **123 rows were judged** — not the six the task was raised from. Titles
carried the judgement (**D2**); twelve rows whose title and outcome could disagree were opened and
their stated outcome read, and those twelve are named below rather than folded into the total.

**Thirteen disagreements.**

| Task | Now | Test says | Why |
| :--- | :--- | :--- | :--- |
| T-048 | fix | decision | The outcome is a definition of "always-loaded" that another task was then built against |
| T-052 | fix | decision | What a published clone carries could not be named until it was settled |
| T-076 | fix | decision | Same shape: the edit follows from what a template's links resolve against |
| T-078 | fix | decision | *Either told it cannot, or a walk that means something* — which branch is the product |
| T-090 | fix | decision | One of the four the task was raised from |
| T-092 | fix | decision | Whether a bare path is a reference; the validator change is downstream |
| T-093 | fix | decision | One of the four |
| T-096 | fix | decision | Whether a narrower walk needs its own number |
| T-097 | fix | decision | One of the four |
| T-098 | fix | decision | One of the four |
| T-105 | fix | decision | The outcome is a rule saying where an authorisation is written |
| T-007 | decision | deliverable | The outcome is `docs/SCOPE.md` — a document, not an answer |
| T-028 | decision | fix | The outcome is a budget that governs what is actually loaded, a state rather than an answer |

**The two rows the test saves are the ones that make it worth having.** T-055 is titled *Settle what
the tool calls itself*, and its stated outcome is *someone who mistypes a command is told how to
retype it* — a behaviour. T-088 is titled *Put audit in the vocabulary, **or** stop calling it a
type*, and its outcome is *the method and the schema agree about what an audit is* — a state. Both
read as decisions by title and neither is one by outcome, which is precisely why the test reads the
**outcome** and not the title. A title-shaped rule would have retyped them.

**The row the test answers least comfortably is T-028**, recorded rather than smoothed over. Its
title, *Budget the whole always-loaded context, not one file*, contains a real judgement about what
counts as always-loaded; its stated outcome is a mechanism that works. The outcome wins under the
test as written, so it moves to `fix` — but this is the one row where a reader might reasonably read
it the other way, and the test's answer here rests on a sentence rather than on a difference in kind.

**Nine of the eleven forward disagreements were invisible to how the four were found.** The four came
from scanning for question-shaped titles among *open* tasks; seven more (T-048, T-052, T-076, T-092,
T-096, T-105, and T-078) and both reverse-direction rows were only reachable by walking every row. The
sweep found more than three times what the sample did, which is the argument for the criterion asking
what was **read** rather than what was changed.

### Step 3 — retyping a closed task corrects its present

**Decision, 2026-08-11.** A closed task's `type` may be corrected, and doing so preserves the record
rather than falsifying it. [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md)
drew the line at whether a field is a **live pointer** or a **dated statement**, and `type` is neither
a statement about what happened nor a promise about the future: it is how a view finds the task
*today*, and a misclassification was wrong on the day it was written as much as it is now. What the
record says about the past lives in the body and the log, and neither is touched.
*Rejected: leave closed tasks as they are and let the filter be right only about open work* — that
answers half the question, since [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md)
makes this same filter the register of decisions already **taken**, which is entirely closed tasks.

**What the edit owes: one log row on each retyped task**, naming this task, so nobody meets a changed
field with no account of it. That is METHOD rule 5's *annotate the past* at the scale of one field.

### Step 4 — thirteen retyped, and the edit was made to prove itself

Applied by a throwaway script rather than by hand, and the script's value was its **assertions**: for
each file it required exactly one matching filename, exactly one `type:` line with the expected old
value, exactly one `updated:` line, and exactly one Log separator — throwing before writing anything
if any of those was not 1. The last one fired immediately: `| :--- | :--- | :--- |` appears **twice**
in T-048, because a body table shares the Log table's column shape. A hand edit, or a script that had
replaced the first match, would have inserted the row into the wrong table and left a file that still
passes `check`. The anchor became *the separator following the `## Log` heading*.

```text
T-048 T-052 T-076 T-078 T-090 T-092 T-093 T-096 T-097 T-098 T-105   fix → decision
T-007  decision → deliverable      T-028  decision → fix
```

Verified by reading a written file back rather than by trusting the exit code: `git diff` on T-007
shows three changed lines — `type`, `updated`, and the inserted log row — with the arrow and the
apostrophe intact and no line-ending churn, which is what a script writing UTF-8 through this
platform's shell most easily gets wrong.

### Step 5 — the test written where the vocabulary is documented

`plugin/skills/taskmd/taskmd/defaults/config.md`, §*Vocabularies*, as prose above the table and beside
the `audit` and register paragraphs that already qualify values there. The `type` row is unchanged
(**D3**), so nothing an adopting project copied has drifted.

### Step 6 — nothing else in the tree states what `decision` means

Scanned every `.md`, `.py`, `.ps1` and `.sh` outside `tasks/`, `reference/` and `.git` — **92 files**
— for `` `decision` ``, `type: decision`, `decision task` and `a decision is`. The only hits are the
paragraph just written and its neighbour, plus the two adopter reports in `control/`, which *ask* the
question rather than answering it. `METHOD.md` names no `type` value at all, which is **D1** holding:
there was no second home to reconcile because the method never had one.

### Step 7 — measured

```text
OK - 123 task(s), 615 field value(s), 391 reference(s), 22 dependency edge(s), 203 declared output(s),
     1 index file(s), 151 document(s), 1232 link(s), 2 template(s), 10 template field value(s),
     0 vocabulary row(s)
```

`list --type decision` returns **31**, up from 22 — arithmetic that matches the sweep exactly
(22 + 11 − 2). The number that answers the task's own outcome is the **open** one:

```text
T-109 T-123 T-093 T-078 T-117 T-090
```

**Six, where before this task the same question returned three.** The filter was not slightly
incomplete; it was answering half, and a reader had no way to see which half.

Suite, one process per module: `test_cli` 92 OK, `test_list` 35 OK, `test_schema` 53 OK, `test_budget`
OK (`tier 1 6968 chars under by 878`), `test_runtime` 27 with **4 failures, all four named**:
`test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has`,
`test_the_shell_launcher_produces_what_the_module_produces`, and
`test_every_entry_point_produces_what_the_module_produces` for `skills/taskmd/taskmd.sh` and for
`bin/taskmd` — the environmental `Launchers` set of
[T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md), with no fifth hiding in the
count.

**Decisions & assumptions**
- **The `decision` test reads the stated outcome, not the title, and beats `fix` where a task is
  both** — 2026-08-11, §1 Q1.
- **No second `type` value for uncertainty-reducing work** — 2026-08-11, step 1: `type` must hold
  still and uncertainty does not, and the timebox that distinguishes a spike from research is
  something this method has already decided not to track.
- **A closed task's `type` may be corrected, with one log row** — 2026-08-11, step 3, applying
  T-103's live-pointer line to a field that is neither a promise nor a dated statement.
- **The sweep is read from `list`, with ambiguous rows opened and named** — 2026-08-11, D2; twelve
  were opened and two of them (T-055, T-088) turned out to be the evidence that the test must read
  outcomes.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)
  §*Vocabularies*
- Thirteen retyped task files, named in step 4

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The test for `type: decision` is written down, or it is recorded that there is none and why | met | Written, in the shipped config's §*Vocabularies* — read the stated outcome, and an answer someone else could act on is a `decision`. Step 6 confirms it is the tree's only statement of it |
| Every task the test disagrees with is retyped, found by a sweep of **all** tasks in both directions whose reach is stated — how many rows were read, not how many were changed | met | 123 rows read, proven by seven `--type` buckets summing to the 123 `check` counts; 13 retyped, 11 forward and 2 reverse. The reverse pair is what shows the sweep ran in both directions, since the sample that raised this task could not have found them |
| The second kind of work is settled either way: a value with its own test, or a recorded finding that the distinction does not survive outside software, with what was read to decide that | met | Settled as **no value**, step 1, on the ground that `type` must hold still and uncertainty does not. What was read is named: the existing knowledge-side values, the spike's timebox against `plan`'s refusal to track duration, and R-9's three non-software cases |
| `list --type decision` is run afterwards and its answer stated, so the claim is measured rather than asserted | met | 31 total, and the number the outcome is about — **open** decisions — went from 3 to 6. Stated as the output, not as "the filter now works" |
| `check` is clean on this repository | met | `OK - 123 task(s) … 1232 link(s)`, index regenerated, and the suite re-run with only T-114's four named `Launchers` failures |

**The one row a later reader should look at first is T-028**, not because a criterion failed but
because the test's answer there is the least comfortable — recorded in step 2 rather than smoothed
into the tick above.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All five criteria met, no child raised. **The sweep found more than three times what the sample did** — 13 disagreements against the 4 the task was raised from — and the two it found in the reverse direction (T-007, T-028) were unreachable by the method that found the original four, which is the argument for the criterion having asked what was *read*. **The maintainer's second-kind angle was researched and declined**, with the reason recorded in step 1 rather than the conclusion alone: the offered test measures uncertainty, `type` has to hold still, and the spike's actual distinguishing feature is a timebox this method has already decided not to track. Every non-software case it was checked against landed on a value already in the row. **A vocabulary row is the most expensive place here to be wrong**, being copied into every adopting project, so the prose was written above the table and the row left alone — which also keeps [T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md)'s question untouched. Two by-products worth more than they cost: the script's assertions caught a body table sharing the Log table's column shape in T-048, where a hand edit would have written the log row into the wrong table and still passed `check`; and T-055 and T-088 read as decisions by title and are not by outcome, which is the evidence the test reads the right half of the record. |
| 2026-08-11 | → planned | Seven steps, and the ordering carries the argument. **The Q2 research is step 1 because it can invalidate steps 2–5**, not because it is the interesting part: a second value means the sweep sorts into three buckets and the vocabulary row gains a *value* rather than a sentence, and a row change is [T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md)'s live question about drift rather than something this task may assume (**D3**). **D1** puts the test in the shipped config and not in METHOD, which opens by saying it names no field and so cannot own a field *value*'s meaning; the rejected home was §5 beside `audit`, where it would re-create exactly the drift T-088 closed. **D2** reads the sweep from `list` rather than from 123 files, with ambiguous titles opened and **named in §3** — an ambiguous row is a finding about the test, so hiding it inside a claim that every file was read would lose the most useful evidence the sweep produces. Steps 3 and 4 are split because permitting an edit to 108 closed records is the irreversible half and should be a written decision before the edits, never inferred from them; steps 5 and 6 are split for T-103's reason, that a claim about the tree is not answered by the file just edited. |
| 2026-08-11 | → specified | **Authorisation, recorded here because a line in a handoff is not one (METHOD §3.1).** The maintainer gave *work every open `v0.2` task through its full lifecycle — specify, plan, implement, review, fix, commit and push, one task at a time* on 2026-08-10, re-confirmed on 2026-08-11 as *continue the lifecycles automatically* and widened the same day to *multiple tasks, until you need to stop*. It covers this task end to end and nothing outside the open `M2` set. **Q1 settled under the standing delegation to decide owner-questions and record the rejection**, not by asking: `decision` means the stated outcome is an answer, and it beats `fix` where a task is both. **Scope widened twice, and both follow from the outcome as already written rather than from a new idea.** First, the sweep runs in **both directions**: the four were found by looking for question-shaped titles, which cannot find a task typed `decision` that fails the test, and a filter returning something wrong under-answers exactly as badly as one that misses something. Second, it reaches **closed** tasks, because [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md) makes this filter the register of *taken* decisions too; [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) is the input for whether that edit preserves the record, added to `related` and `Inputs`. Acceptance criteria gained one for the second-kind research so it can be settled **either way** — a value with a test, or a recorded finding that the distinction does not survive outside software — and the sweep criterion asks for **rows read**, not rows changed, since a sweep that reports only its hits cannot be told from one that ran on nothing. Effort left at `s`: the sweep is 123 title-and-type rows the tool already prints, not 123 files to open. Q2 stays open and stays `plan`'s, per the maintainer's steer. |
| 2026-08-10 | (no change) | **Maintainer's steer, recorded and not acted on.** Two parts. First, a correction to this task's own opening recommendation: *carrying an unanswered question does not make a task a decision* — right, and for a reason the task had not weighed, since every task has open questions at `specify` and a test that fires on all of them distinguishes nothing. Q1's rejected alternative now records it. Second, a genuinely new angle: when a task's questions outnumber its answers, or could move its scope significantly, that may be **a different kind of work** rather than a mistyped one — near to an agile *spike*, work whose product is knowledge rather than the thing itself. **The research was explicitly not to be performed**, so it is recorded as `plan`'s and the scope gained an *In* item for it. Two constraints written down with it, the second being the one most likely to be skipped: taskmd tracks any kind of work and not only software (R-9), the maintainer confirming software projects are supported but not the case the vocabulary is shaped around; and *spike* is therefore an **input to the research, never a candidate name**, because an imported convention carries its author's assumptions — `docs/BRIEF.md` lists that as a lesson already paid for. Effort **xs → s**: the narrow typing answer is still a sentence, but a second candidate kind is a vocabulary question with a research step in front of it. The title still reads correctly and is deliberately not widened yet — if the second kind survives, renaming is `specify`'s call, not a guess made now. **Status unchanged**: this is input to a specify nobody has agreed, not an agreement. |
| 2026-08-10 | → proposed | Found in the project status review of 2026-08-10, surfaced to the maintainer, and **not acted on** — raised as a parked task rather than pressed, because an observation with no record is one the next review re-derives from nothing. `medium` because nothing is broken and the cost is a filter that quietly under-answers; `xs` because the work is a sentence and four field edits. Sized against the wrong reading deliberately: it looks like a typo to fix, and it is not — all four of the mistyped tasks are genuinely both a decision and a fix, and the vocabulary has never stated a test for which wins. Worth settling in the same pass as any re-grouping of `work_package`, since that touches every task's front-matter anyway. |
