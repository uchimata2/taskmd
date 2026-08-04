# Rationale

> Referenced from [`../METHOD.md`](../METHOD.md) §7. **You do not need this to run a phase** — the
> rules stand on their own. Read it when a rule looks wrong, or when someone proposes changing one.

## Why the inverse of a link is never written down

Recording a link on one end and computing the other is not a storage trick; it is what makes the
rest of the method possible.

An inverse that is *written down* is a second copy of one fact, and second copies eventually
disagree. A derived one cannot: **a fact that is derived cannot go stale, so nothing has to be kept
in step.** That is why no validator is needed to keep the two ends of a link honest, and why no view
can miss a link that was recorded on the far side.

This is also why the rule is phrased as forbidding designs that *compel* a second write, rather than
forbidding the second write itself. A person who records both ends creates no drift — the two
collapse into one link. A design that requires both ends creates drift on a schedule.

## Why there is no audit phase

Lifecycles that add one turn findings into a stage the work passes through — and once an auditor is
*inside* the task being audited, the cheapest thing to do with a finding is fix it on the spot. That
leaves no record the problem existed, which is the one thing an audit is for.

Audit is a task type instead ([audit](audit.md)), which puts the finding and the fix in different
tasks by construction rather than by discipline.

## Why the method says nothing about effort, tools or which model does the work

Those are properties of whoever is doing the work, not of the work being tracked. A method that
legislated them would be wrong for the next person, wrong for a differently-resourced team, and
stale by the next release of whatever it named.

It is a real temptation, because the right answer often *is* knowable for a given phase on a given
day. But that answer belongs wherever the project records how it works, not in the standard the
project follows.

## Why verification exits `implement` rather than `review`

If "the planned outputs exist" closes `implement`, then the first contact between the work and
reality happens in `review` — at which point a failure is a review finding rather than part of
doing the work, and the person who made it has already moved on.

Putting it at the end of `implement` also puts it where the cost of a fix is lowest: the author is
still in context, the decisions are fresh, and nothing downstream has been built on the result yet.
The two changes the worked example in [implement](implement.md) records — inlining a source, and
correcting a definition — both cost minutes there and would have cost a re-open in `review`.

## Why one phase per request

The person who asked for a plan may want to read it before it is executed, and cannot if the
execution already happened. Auto-advancing quietly converts a request for judgement into a request
for output.

It also removes the natural checkpoint. Each phase boundary is a cheap place to stop, reconsider, or
hand the work to someone else; a run that crosses three boundaries unprompted has skipped three
opportunities to discover that the second one was the wrong direction.
