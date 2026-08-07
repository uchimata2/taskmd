# plan

> Phase 2 of 4. Spine — including this phase's **exit criterion**:
> [`../METHOD.md`](../METHOD.md) §2.

Plan turns an agreed outcome into an ordered set of steps that produce it. It does not produce the
outcome, and it does not revisit whether the outcome is right — that was settled in
[`specify`](specify.md).

## Procedure

1. **Break the outcome into steps.** Each step is one movement of the work with one result. A step
   that produces nothing is not a step; it is either preparation belonging to the step that needs
   it, or it is missing its output.

2. **Name each step's output.** Not "write it up" but the thing that will exist: a comparison
   table, a decision recorded in the task, a section of the deliverable. The test is whether a
   second person, handed only the plan, could go and check whether that output exists yet.

3. **Say what each step needs.** Where an input comes from outside the task, name it. Where it comes
   from an earlier step, the order is the dependency and needs no further ceremony.

4. **Record real dependencies as edges, not as prose.** If another task must close first, that is a
   dependency edge on this task ([`../METHOD.md`](../METHOD.md) §4). A sentence in the plan saying
   "this needs the contact-volume extract first" is invisible to every view that matters.

5. **Decide the shape of the deliverable, and record it as a decision.** Where the output could
   reasonably take more than one form, choose, and write down what was rejected and why. A rejected
   alternative with its reason is the single most useful thing a later reader finds — without it,
   the next person re-litigates the choice from scratch, or worse, quietly reverses it.

6. **Collect the output paths in one place** at the end of the plan, so the set of things this task
   will produce can be read without reconstructing it from the steps. **Write them as plain paths,
   never as links** — at `plan` the file does not exist yet, and a link to a file that is not there
   is a broken link like any other. For the same reason, the field that records a task's *produced*
   outputs stays empty until they exist: a plan lists what is promised, and those are two different
   facts that happen to look alike.

## Sequencing

Order by dependency first, then by what reduces uncertainty soonest. A step that could invalidate
the rest of the plan belongs near the front, where discovering it is cheap. A plan that saves its
riskiest assumption for step nine is optimistic, not efficient.

Do not plan past the horizon you can actually see. If step 4's result determines whether steps 5–8
are the right steps at all, say so in the plan rather than inventing detail that will be discarded.

## What does not belong in a plan

- **Acceptance criteria.** They live in `specify` and are judged in `review`. Restating them here
  creates a second copy that will drift from the first.
- **Effort, duration or sizing.** Not tracked by this method.
- **The work itself.** A plan step that contains its own answer means the work happened during
  planning, unreviewed and unrequested.

## Worked example — the research task from `specify`

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what "support contact" has meant across the window; the definition changed once. | A stated definition, and the date it changed, recorded in the task |
| 2 | Pull first-month contact volumes per cohort, split at each onboarding revision. | A table, one row per cohort, with its source named |
| 3 | Check whether anything else changed at those dates that would move the same number. | A list of confounders, each kept or discarded with a reason |
| 4 | Decide whether the evidence can carry a conclusion at all, before writing one. | A recorded decision: answerable, or not, and on what basis |
| 5 | Write the answer, its evidence, and what would change it. | The deliverable |

Step 1 exists because the earlier definition change would silently corrupt every later figure —
that is the "reduces uncertainty soonest" rule doing its work. Step 4 is a deliberate stopping
point: it is where the plan admits that "cannot be determined" is a real result, and it is placed
*before* the writing so that conclusion is available rather than embarrassing.

## Leaving this phase

→ [`implement`](implement.md), **when it is asked for** ([`../METHOD.md`](../METHOD.md) §3.1).
