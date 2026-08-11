# audit

> A task type, not a phase. Spine: [`../METHOD.md`](../METHOD.md).

An audit examines a body of work for problems nobody has alleged. It is requested; it never happens
automatically, and nothing "passes through" it.

## Why it is a task and not a phase

A phase is something every task goes through. Audits are not: most work does not need one, and the
work an audit examines is usually spread across many tasks rather than contained in one. Making
audit a phase would also put the auditor *inside* the task being audited — where the cheapest thing
to do with a finding is fix it on the spot, which is exactly what must not happen.

As a task type, an audit has its own outcome, its own criteria and its own lifecycle. It goes
through specify → plan → implement → review like anything else. Its deliverable is a set of
findings.

## Procedure

The five steps are what every audit does. **How this one examines its subject is not fixed here** —
an audit is a task, so it has a `plan`, and the procedure for *this* audit is researched and written
there: what will be read, in what order, and what the examination consists of. Step 2's threshold is
part of that design. A standing checklist carried by every audit would examine each new subject for
the last subject's problems, which is how an audit comes to report what its author already expected.

1. **Create one umbrella task**, scoped to what is being examined. The scope is the first thing to
   get right: "everything" produces a list nobody acts on. Name what is in, and say what is
   deliberately not being looked at.

2. **Say what counts as a finding**, before looking. Without this, an audit reports whatever its
   author happens to dislike, and its results cannot be compared to the last one.

3. **Record every finding in the umbrella**, each with a severity and enough detail that someone who
   was not present can tell what is wrong. A finding that only makes sense to its discoverer is not
   yet a finding.

4. **Raise a child task for each finding that needs action**, pointing back at the umbrella and at
   the finding it comes from. Findings that need no action stay recorded in the umbrella with the
   reason — they are the evidence that the area was examined, which is worth as much as the ones
   that produced work.

5. **Close the umbrella only when every child is resolved** — done, or dropped with a recorded
   reason. An umbrella closed over open children erases the link between the examination and its
   consequences.

## Why the no-inline-fix rule is the whole point

The rule is in [`../METHOD.md`](../METHOD.md) §5. Its cost is obvious and its benefit is not, so it
is the one most often waived — here is what waiving it destroys.

An auditor who repairs what they notice leaves: no record that the problem existed, no way to judge
whether the fix was right, no way to see that the same problem has now recurred four times, and no
way to distinguish "we examined this and it was clean" from "we examined this and quietly patched
eleven things". The fix is cheap; the traceability is the whole product.

This holds even when the fix is a single word, and even when the auditor is also the person who
would do the repair. If a fix is genuinely too small to be a task, that is a signal the finding
threshold (step 2) is set too low — not a licence to fix it inline.

The one exception is a finding that makes continuing the audit impossible. Then stop, raise it, and
say the audit is incomplete; do not repair it and carry on as though the scope were covered.

## Auditing a plan that has not been implemented

People do ask for this — "audit the plan before we start" — and it is a reasonable thing to want.
It is not an audit, and treating it as one damages the rule above.

**An audit's product is traceability over work that exists.** A plan that has not been implemented
has produced nothing: nothing patched, nothing to trace, and no way for the distinction between a
clean examination and a quiet repair to arise. **And the no-inline-fix rule cannot bite**, because
the plan is the thing still being decided — changing it *is* the work of the `plan` phase, not a fix
applied to a finished artifact. Calling the exercise an audit would therefore force an exception
into [`../METHOD.md`](../METHOD.md) rule 4 for the commonest case of all, and a rule with a
sanctioned waiver for its commonest case has stopped being a rule.

So: no umbrella task, no findings, no child tasks. The plan is revised where it lives —
[`plan`](plan.md), *Revising a written plan*, which says how and where that is recorded. What the
requester wanted is unchanged; only its name is.

## Worked example — a non-software audit

An umbrella scoped to *"the four onboarding emails, checked for claims we cannot support"*, with a
stated finding threshold: **a factual claim about the product with no source, or a commitment we do
not actually meet.**

| Finding | Severity | Action |
| :--- | :---: | :--- |
| Email 2 promises a response "within an hour"; the measured median is four | High | Child task — decide whether to fix the promise or the process |
| Email 3 cites a customer-satisfaction figure with no source | Medium | Child task — source it or remove it |
| Email 1 calls the trial "free"; it is | — | No action; recorded as checked |
| Email 4's tone differs from the other three | — | No action; outside the stated threshold |

The last two rows are why the audit is trustworthy. Without them a reader cannot tell whether emails
1 and 4 were examined or skipped — and the fourth row shows the threshold doing its job by keeping a
real but out-of-scope observation from becoming work nobody asked for.
