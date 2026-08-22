# review

> Phase 4 of 4. Spine — including this phase's **exit criterion**:
> [`../METHOD.md`](../METHOD.md) §2.

Review judges the finished outcome against the criteria agreed in [`specify`](specify.md). It is a
verdict phase, not a working phase.

## Procedure

1. **Take the criteria as they were written.** Judge against the agreed text, not against what the
   work turned out to be good at. A criterion that now looks wrong is a finding, not a licence to
   restate it — see *Changing a criterion*, below.

2. **Judge each one separately**, and record the result with a note saying what settled it. A bare
   tick is not a review; the note is what a later reader uses to decide whether to trust the tick.

3. **For anything not met, raise a task for it.** Not a to-do line, not a caveat in the summary — a
   task, linked to this one, that someone can be given. Then the gap is visible instead of buried in
   a paragraph nobody re-reads.

   **Which edge you give it decides whether this task can close** ([`../METHOD.md`](../METHOD.md)
   §4). Where the outcome itself is incomplete, the new task is a **child**, and this one stays open
   until it closes — a task whose own outcome is missing a piece is not done, whatever the table
   says. Where the outcome is finished and the criterion asked for something **beyond** it — a
   stronger test, a use that waits on an event nobody controls, a reader nobody can summon — the new
   task is a **soft** link, and this one closes honestly.

4. **Do not fix things here.** Review that repairs what it finds destroys the record of what was
   wrong ([`../METHOD.md`](../METHOD.md) §5) and re-opens work that has already been verified,
   without re-verifying it. The fix is a child task — a repair to the outcome is part of the
   outcome, so it holds this task open (step 3) — and it runs the lifecycle like anything else.

5. **Read the task's own open questions before closing**, and route anything still live — an answer
   into the record, or a new task for what nobody here can settle. **No tool will do this for you**,
   and the reason is under *A question aimed at someone else*, below.

6. **Close the task** when every criterion is met or carried, **no child of it is open** (step 3
   and [`../METHOD.md`](../METHOD.md) §4), the record is current, and the evidence from
   [`implement`](implement.md) is in place. Closing a task whose evidence is missing is the failure
   this method exists to prevent — the outcome may well be fine, but nobody can now tell.

## A question aimed at someone else

A question addressed to somebody who is not doing the work — the owner, a specialist, whoever holds a
fact nobody here has — is the one residue a review is built to miss. It fails no criterion, so steps
2 and 3 never reach it: there is no row for it in the table and nothing to carry into a task of its own.
And the moment the task closes it leaves every view a project has, because **views read open work**.
It does not go stale; it goes invisible.

Step 5 is the only thing that catches it, and that is a measured claim rather than a preference. One
project ran four candidate detectors over its own records — 178 questions in 148 closed tasks — and
then over an older tree where one question was known to have been left live. Every rule precise
enough to be worth running missed that one, and every rule that caught it buried it about one in
twenty. The reason is structural, not a matter of a better pattern: a question and its answer are
both prose, and an answer is written wherever it belongs — beside the question, in a sibling bullet,
in a decision, or in the task raised to carry it. **No pattern can tell which answer belongs to which
question**, so a checker either reports the section or reports nothing.

The convention that would fix it — *always answer inside the bullet* — was measured too, and
rejected: most of those answers are numbered decisions, and their home is the decision list. Forcing
a copy beside the question would make the record state one fact twice, which is the failure the whole
method is built to avoid.

So this is a step in a procedure and not a class in a validator, deliberately. Whatever your tracker
validates, it is not this.

## Changing a criterion

Sometimes a criterion really was wrong — it measured the wrong thing, or the work revealed that it
could not be satisfied by any acceptable outcome. Then:

- Say so explicitly, in the task, with the reason.
- Record the original text alongside the replacement. A criterion that is silently edited to match
  the result is not a criterion; it is a description.
- Get it agreed by whoever agreed the original.

Doing this openly is legitimate and sometimes necessary. Doing it quietly makes every future review
worthless, because a reader can no longer tell which criteria predated the work.

## What review is not

- **Not the first check.** The outcome was already used and the evidence recorded in `implement`.
  Review that is discovering basic faults means the previous phase did not exit properly.
- **Not an audit.** Review judges *this* task against *its* criteria. Examining a body of work for
  problems nobody has alleged is an audit, which is a task type of its own ([`audit`](audit.md)).
- **Not a summary.** Restating what was produced belongs in the deliverable, not in the verdict.

## Worked example — the research task

| Criterion | Result | Note |
| :--- | :---: | :--- |
| Names a direction and does not hedge | met | Concludes "does not reduce contacts in month one"; direction stated in the opening line |
| Every figure traceable to a named source | met | Two traced at random during `implement`; the second exposed a definition mismatch, corrected before this review |
| Where evidence cannot settle it, said as a finding | met | Cohort 4 is excluded and the exclusion is stated, with what it would take to include it |
| An uninvolved reader can say what would change the conclusion | **not met** | The reader identified the cohort-definition risk but not the seasonal one, which is not stated anywhere → **child task: state the seasonal confounder** |

Three met, one carried — **and this task does not close yet.** The seasonal confounder is missing
from the deliverable itself, so the task raised for it is a **child**, which under
[`../METHOD.md`](../METHOD.md) §4 holds this one open. Had the criterion instead asked for something beyond the
outcome — a second reader for a conclusion that already stands — the task raised would be a soft
link and this one would close. Either way the gap is a task with an owner rather than a sentence in a
document nobody will re-read. Note that the second row's note points at what `implement` already
found — review reports it, it does not re-do it.

## Leaving this phase

The task is closed, or it is not — there is no fifth phase. If the review surfaced problems beyond
this task's criteria, that is an [`audit`](audit.md), raised separately.
