# implement

> Phase 3 of 4. Spine — including this phase's **exit criterion**:
> [`../METHOD.md`](../METHOD.md) §2.

Implement executes the plan. Its exit criterion is the strictest in the method, and deliberately so:
producing the outputs is not finishing.

## Procedure

1. **Work the steps in the planned order.** Where the order has to change, say why in the task
   before changing it — an undocumented reordering hides the discovery that caused it.

2. **Record decisions as they are taken.** Each one: what was decided, what it rules out, and why,
   dated. Written at the moment of choosing, this costs a sentence. Reconstructed at the end, it is
   guesswork wearing the clothes of a record — and the reasons that felt obvious at the time are
   exactly the ones that will be gone.

3. **Escalate what you find.** A plan meeting reality produces surprises. Each is a question or a
   new task, never a silent adjustment ([`../METHOD.md`](../METHOD.md) §3.3). The one thing that
   must not happen is the plan quietly becoming a different plan.

4. **Verify by use** — below. This is the phase's real content.

5. **Record the evidence** in the task: what was checked, how, and what the result actually was.

## Verification

**The outputs existing is not evidence.** A wrong output exists exactly as convincingly as a right
one, and the person who made it is the least able to see the difference by looking. So the exit
criterion is not "the planned outputs exist" — it is that someone put the outcome to its intended
use and recorded what happened.

Verification is therefore whatever exercises the deliverable **the way it will actually be used**:

| The deliverable | Verified by |
| :--- | :--- |
| A procedure or runbook | Someone follows it, start to finish, without the author narrating |
| A written analysis | A reader who was not involved states the conclusion back, and can say what would change it |
| A course or training material | Someone in the target audience works through it and is measured on what it claimed to teach |
| A talk or deck | Delivered to a stand-in audience, timed, questions taken |
| A decision | The people bound by it can state what it commits them to |
| Anything with a mechanical check available | Run the check — and report what it printed, not that it passed |

Two rules that hold across all of them:

- **State the result, not the verdict.** "Ran it on the four Q3 cohorts; three matched the source
  system, the fourth was 12 short and the gap is the re-opened contacts" is evidence. "Verified"
  is not. A verdict cannot be checked by the next reader; a result can.
- **A check that has only ever succeeded has not been tested.** If the point of a check is to catch
  something, it is worth exactly as much as your confidence that it *would* catch it — and the only
  way to earn that confidence is to have seen it fail on a case it should catch.

### When there is nothing to run

Most work has no mechanical check, and this is where the criterion is usually abandoned. It should
not be. The substitute is not "review it carefully" — it is **finding the smallest real use** and
performing it. The distinguishing feature of use is that it can surprise you: reading your own
analysis cannot, whereas asking someone else to act on it can.

If genuinely no use is available before the deliverable ships, that is a finding. Record it, say
what would have been checked and why it could not be, and let `review` judge an honest gap rather
than an implied assurance.

## Worked example — the research task

Step 5 produced the written answer. What satisfies the exit criterion is **not** that the document
exists:

> Gave the draft to someone outside the project with the question but not the conclusion. They read
> it and stated the direction back correctly, and named the cohort-definition change as the thing
> that would overturn it — which is the intended reading. They also asked where the Q2 figure came
> from; the source was named in a footnote they did not find, so the sourcing moved inline.
>
> Traced two figures at random back to the source system: one matched, one was 12 contacts short
> because re-opened contacts are counted once there and twice here. Definition corrected in step 1's
> record, both figures re-pulled.

That is the phase's output as much as the document is. Note that verification changed the
deliverable twice — which is the point of doing it before `review` rather than during it.

## Leaving this phase

→ [`review`](review.md), **when it is asked for** ([`../METHOD.md`](../METHOD.md) §3.1).
