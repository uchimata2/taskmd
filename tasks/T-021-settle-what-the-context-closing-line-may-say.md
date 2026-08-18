---
id: T-021
title: Settle what the context closing line may say
type: decision
status: done
phase: review
parent: T-002
blocked_by: []
related: [T-003, T-022]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-05
updated: 2026-08-10
deliverables: []
adopter_visible: yes
---

# T-021 — Settle what the context closing line may say

## 1. Specify

**Outcome**
A decision by the owner of T-002's criteria: either the criterion is replaced with wording a
backend-neutral tool can satisfy, or the closing line gains something it does not have.

**Why this one**
T-002's ninth criterion reads:

> **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
> moved past its phase, where the current tool tells you to redo the phase you just finished.

It was **not met as written**, and the reason is structural rather than an oversight. `phase` is one
project's vocabulary field. The tool can print its value — it does — but it cannot know that status
`planned` means the `plan` phase is *finished*, because that mapping lives in `docs/METHOD.md`, not
in the schema. A tool that inferred it would be hardcoding this project's vocabulary, which
criterion 7 forbids in the same list.

What was built: the header prints every `context_fields` value, so both axes are on screen, and the
closing line carries only derived state and names no phase at all. On T-002 at
`status planned | phase plan` — planning finished:

```
interim  NEXT: read the file above, then work the 'plan' phase.
new      STATE  open, no blocker outstanding
```

The defect the criterion was written against is gone: nothing instructs, so nothing can instruct you
to redo the phase you just finished, which also settles the R-6 concern the criterion carried. What
is unresolved is whether "gone" is what was wanted, or whether a correct hint was.

`docs/method/review.md` is explicit that a criterion which turns out to be wrong may be replaced —
openly, with the original recorded, **and agreed by whoever agreed the original**. This task is that
agreement. A reviewer cannot grant it to themselves; that is the whole point of the rule.

**Requirements served**
R-3, R-6 (`docs/SCOPE.md`).

**Scope**
- In: what the closing line of `context` may say, and the wording of T-002's criterion 9.
- Out: anything the skill says. If the answer is "the agent should be told what to do next", that is
  T-003's to carry, not the CLI's — the CLI would then keep its line unchanged.

**Inputs**
T-002 §1 criterion 9 and §3 *A criterion that could not be met as literally worded*;
`docs/METHOD.md` §2 (phase and status are independent) and §3.1 (a pointer is not authorization);
`docs/method/review.md` *Changing a criterion*.

**Acceptance criteria**
- [ ] One of three outcomes is chosen and recorded with its rejected alternatives: (a) the criterion
      is replaced, with the original text kept alongside; (b) the CLI gains a phase-aware line and a
      config key that makes the status-to-phase mapping declarable; (c) the whole concern moves to
      the skill and the CLI line is confirmed as final
- [ ] If (b), it is stated how the mapping avoids becoming a second home for the lifecycle that
      `docs/METHOD.md` already defines
- [ ] T-002's criterion row is updated to point here, so no future reader finds a bare "not met"
      with no resolution

**Open questions**
- none. ~~Is a closing line that gives no direction a loss, or exactly the R-6 behaviour?~~
  **Answered by the owner on 2026-08-05: exactly the R-6 behaviour.** The owner asked for whichever
  option causes least trouble in the long term and fits what has since been designed; that is
  **(a) with (c)** — the criterion is replaced with wording a backend-neutral tool can satisfy, the
  CLI's closing line is confirmed as final, and direction-giving belongs to the skill.

**Why (a) + (c), and not (b)**

(b) — a config key declaring which status means each phase is finished — is the expensive answer.
The lifecycle would then be written in two places, `docs/METHOD.md` and every project's config, and
the copy in the config would be the one nobody re-reads when the method changes. That is the drift
this plugin exists to remove, bought for one line of output.

What settled it is a decision taken *after* this task was raised.
[T-022](T-022-filtered-task-listing-for-scripts.md) gives taskmd a command whose entire job is to
answer "what should I work on next", ordered by business value, effort and dependencies. "What next"
therefore has a home, and it is not a hint appended to `context`. Had (b) been built, taskmd would
have shipped two answers to one question — a per-task guess from `context` and a graph-wide answer
from the listing — which is the same defect one altitude up.

So the division is: **`context` reports state, the listing answers "what next", and the skill says
what to do about it.** Each fact keeps one home.

## 2. Plan

The decision itself was taken in `specify` — (a) with (c), agreed by the owner on 2026-08-05. What
is left is landing it in the two places that still say otherwise, and checking that the half of it
given away to the skill actually arrived there.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Draft the replacement for T-002's criterion 9: wording a backend-neutral tool can be judged against, naming the case that would falsify it, and carrying (c) — that direction-giving is not the CLI's. | The replacement text and the original quoted beside it, recorded in §3 |
| 2 | Replace criterion 9 in T-002 §1 with that wording, leaving the original visible, marked replaced, dated, and naming who agreed it. | The edited criterion list in `tasks/T-002-implement-the-core-cli-context-index-check.md` §1 |
| 3 | Annotate T-002 §4's criterion-9 row: leave the 2026-08-05 verdict as written, add what the replacement settles and how the delivered line stands against it. | The edited row in `tasks/T-002-implement-the-core-cli-context-index-check.md` §4 |
| 4 | Add a Log row to T-002 recording the replacement and pointing here. | A row in `tasks/T-002-implement-the-core-cli-context-index-check.md` Log |
| 5 | Read `plugin/skills/taskmd/SKILL.md` and establish whether the skill gives the direction (c) handed it. If it does not, raise a task — do not edit the skill here, it is out of scope by §1. | A finding recorded in §3, and a new task file in `tasks/` if the answer is no |
| 6 | Run `check` and `index`, and record the literal output. | Command output in §3 |

**Inputs from outside the task.** `docs/SCOPE.md` R-3 and R-6 were read before planning: R-3 states
the lifecycle and the independence of `phase` and `status`, R-6 states that a phase is worked only
when requested. Neither mentions a hint or a closing line, so no requirement text changes and there
is no step for it — the criterion was a stricter reading of R-3 than R-3 asks for.

**Shape of the edit — decided.** The original criterion stays in T-002 §1, struck through, with the
replacement beneath it; the same house style §1's answered open question already uses. *Rejected:*
deleting the original line and preserving it only here. It reads more cleanly, and it makes T-002 §1
claim it always said the satisfiable thing — `METHOD.md` rule 5 allows correcting what a record says
about the present but not rewriting what it says about the past.

**Outputs promised**

- tasks/T-002-implement-the-core-cli-context-index-check.md
- tasks/T-021-settle-what-the-context-closing-line-may-say.md
- tasks/README.md
- one new file in tasks/, only if step 5 finds the skill silent

## 3. Implement

**Decisions & assumptions**
- **The replacement wording** — 2026-08-10. The original, kept in T-002 §1:

  > **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
  > moved past its phase, where the current tool tells you to redo the phase you just finished

  and what now stands beside it:

  > **`context`'s header carries every field the config names, and its closing line states derived
  > state only** (R-3, R-6) — so a project whose vocabulary has `phase` and `status` sees both, and
  > nothing tells the reader which phase to work next. Falsified by a closing line that names a
  > phase or an action; proven on a task whose status has moved past its phase, where the interim
  > tool tells you to redo the phase you just finished

  It names no field of its own — "every field the config names" is the mechanism, and `phase` and
  `status` appear only as this project's instance of it, which is what kept the original unmeetable.
  It stays falsifiable in both halves: a header missing a configured field fails it, and so does any
  closing line that instructs.
- **The original is struck through in place, not deleted** — 2026-08-10, as planned. A reader of
  T-002 §1 has to be able to see that the criterion changed; `METHOD.md` rule 5 permits correcting
  the present but not rewriting the past.
- **T-002 §4's verdict is left as it was judged** — 2026-08-10. The row still reads
  **not met — carried**, with the resolution annotated after it. Overwriting it with *met* would
  make the 2026-08-05 review claim it had approved wording that did not exist that day, and would
  also erase the reason T-021 exists.
- **The skill already carries the direction (c) gave it, so no task was raised** — 2026-08-10.
  Step 5's check: `plugin/skills/taskmd/SKILL.md` opens with "what to do next" among the things
  **derived by the tool**, makes `taskmd list --open --limit 1` the first command it runs and says
  it "answers what to work on next", and warns that `context` shows a plan you were not asked to
  execute, pointing at `METHOD.md` §3.1. So the division this task settled — `context` reports
  state, the listing answers "what next", the skill says what to do about it — is written where (c)
  put it, and nothing here needed to change.

**Outputs produced**
- tasks/T-002-implement-the-core-cli-context-index-check.md — §1 criterion 9 replaced with the
  original kept, §4 row annotated, Log row added
- tasks/T-021-settle-what-the-context-closing-line-may-say.md — this record
- tasks/README.md — regenerated
- No new task file: step 5's conditional output was not needed

**Evidence — the replacement judged by running the command.** `context` on a task whose status has
moved past its phase, which is this task itself at `planned | plan`:

```
status planned | phase plan | type decision | work_package M2 | owner maintainer
file   tasks/T-021-settle-what-the-context-closing-line-may-say.md
...
STATE  open, no blocker outstanding
```

Both fields in the header; the closing line names no phase and no action. The interim tool printed
`NEXT: read the file above, then work the 'plan' phase.` on this same state — the case the original
criterion was written against.

```
Wrote tasks/README.md - 21 active, 95 closed
OK - 116 task(s), 580 field value(s), 367 reference(s), 22 dependency edge(s), 179 declared output(s), 1 index file(s), 144 document(s), 1142 link(s), 2 template(s), 10 template field value(s), 0 vocabulary row(s)
```

Three links more than before the edits, which is the two new pointers to this task plus the one in
T-002's Log — the reference count is unchanged at 367 because no front-matter edge moved.

## 4. Review

Judged against the criteria as agreed on 2026-08-05. Two met, one not applicable by the choice the
first one records.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One of three outcomes chosen and recorded with its rejected alternatives | met | (a) with (c), chosen by the owner on 2026-08-05 and recorded in §1 *Open questions*; §1 *Why (a) + (c), and not (b)* carries the rejection of (b) and the argument that settled it — T-022 had since given "what next" a command, so a hint on `context` would have been a second answer to one question. The owner's choice was not re-litigated here; `plan` and `implement` only landed it. |
| If (b), it is stated how the mapping avoids a second home for the lifecycle | n/a | (b) was the rejected option. The condition is not vacuously ticked: the reason (b) was rejected *is* that no such statement exists — a status-to-phase mapping in every project's config is a second home for what `docs/METHOD.md` §2 defines, and nothing in the design removes that. |
| T-002's criterion row points here, so no future reader finds a bare "not met" with no resolution | met | T-002 §4's row keeps its 2026-08-05 verdict and now carries a linked resolution naming what replaced the criterion and how the delivered command stands against the replacement. Checked by reading it back through the tool rather than the file: `check` resolves the link (1,142 links, 0 unresolved) and the row is reachable from this task's own `context` through the parent edge. |

**On the criterion that could not be ticked.** A third of this task's criteria was conditional on the
option the owner rejected, which is the shape a `decision` task's criteria take when they are written
before the decision. It is recorded as `n/a` with the reason rather than dropped, because a reader
comparing the criteria to the outcome would otherwise have to work out for themselves whether it was
forgotten.

**Child fix tasks raised**
- none. Step 5 checked whether the skill carries the direction (c) handed it and found that it does —
  recorded in §3 with what it says, so a later reader does not have to re-check.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1). The evidence had to be gathered on this task itself: it was the only one at a state where status has moved past phase at the moment the check was run, which is exactly the case the original criterion named. Nothing raised — step 5 expected to find the skill silent about "what next" and found it saying so in its first command. |
| 2026-08-10 | → planned | Planned under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1), which covers each task in that set end to end and nothing outside it. Six steps, no dependency edge: the decision was taken in `specify`, so what remains is landing it. One step is a check rather than an edit — (c) gave direction-giving to the skill, and nothing has confirmed the skill took it. |
| 2026-08-05 | → specified | Owner chose (a) with (c): criterion 9 is replaced, the CLI's state-only closing line is final, and direction-giving is the skill's. (b) was rejected as a second home for the lifecycle. The deciding argument arrived after this task was raised — T-022 gives "what next" a command of its own, so a hint on `context` would have been a second answer to one question; soft edge added to record that. Implement is two edits: criterion 9's replacement text in T-002 §1 with the original kept, and its §4 row pointing here. |
| 2026-08-05 | → proposed | Raised by T-002's review. Flagged during `implement` rather than reinterpreted, and carried here rather than ticked — a reviewer cannot agree a criterion change with themselves. |
