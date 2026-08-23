---
id: T-230
title: A task gated on an external event has no field, and sorts as startable
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-182, T-199, T-087]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-23
adopter_visible: yes
deliverables: []
---

# T-230 — A task gated on an external event has no field, and sorts as startable

## 1. Specify

**Outcome**
An answer, recorded, on whether a task held up by something that is **not another task** gets a way to
say so that the ordering rule can read — and if so, what it is.

**Why this one**
[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) cannot be started. It
waits on there being a release to make, which is nobody's to schedule. That fact lives in an *Open
questions* bullet, and no view can see prose, so `list --open --limit 1` will hand it to a session as
the next thing to work.

**Neither existing mechanism reaches it, and both were checked by running.** Measured 2026-08-22:

```text
blocked_by needs a task, and a release is not one. Nothing to point the edge at.

$ ./plugin/bin/taskmd check --root tests/fixtures/broken-missing-blocker
NO BLOCKER    T-001 is 'blocked' with nothing in blocked_by
1 problem(s) - ...
exit 1
```

So marking it `blocked` is a validator failure, and the edge has no target. The task has **no field**,
and the ordering rule sorts it on value then effort then id, exactly as if it were ready.

**This is the shape a commit already fixed once, in the only case where the fix was available.**
[T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md)'s wait was a
sentence in a Log row until it was made a `blocked_by` edge, on the stated ground that *prose in a Log
row is invisible to every view*. That repair worked because the blocker was a task. Here it is an
event, so the same defect has no remedy and nobody has said so.

**Scope**
- In: whether this is worth a mechanism at all, and if so which. **A new shipped-config key is very
  nearly ruled out before this starts**: [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
  records that a config *replaces* the default rather than merging, so every key is required and adding
  one errors every existing adopter's config on upgrade. What is left is code-only or nothing —
  relaxing the *no blocker* rule so `blocked` is legal without an edge, teaching the ordering rule to
  read the status value, a convention with no tool support, or nothing
- In: the tension inside the second of those. `is_blocked` reads edges and **says why in its own
  docstring** — *"Not a status value — a task can be marked anything and still be held"*. Any
  answer that has the ordering rule read a status must overturn that sentence on the record, not
  around it
- In: whether the answer also covers *waiting on a person* — a reader nobody can summon, an owner
  question — which is the same shape and is currently carried by soft edges and prose
- Out: fixing T-182. It is the instance; if a mechanism arrives it can adopt it, and if none does then
  T-182 keeps a prose gate and that is the recorded answer
- Out: changing what `blocked_by` means. The derived flag reads edges deliberately, and `cli.py` says
  so in `is_blocked`'s own docstring

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `is_blocked`, `effective_values`, and
  `check_blocked_without_blocker`; the three places that decide what *held up* means today
- [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) *Open questions* —
  the instance, and the only one currently open
- [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) Log,
  2026-08-22 — the same defect where a remedy existed, and the argument for why prose does not do

**Acceptance criteria**
- [ ] The answer is recorded with its reason, and every candidate that was rejected is named with what
      it would have cost
- [ ] How many open tasks are in this state **today** is counted, not estimated — a mechanism for a
      class with one member is a different decision from one with eight
- [ ] If the answer is *nothing*, what a session should do when `list` hands it an unstartable task is
      stated somewhere a session reads
- [ ] Any shipped-schema change is checked against what it does to an adopter's existing config on
      upgrade

**Open questions**
- **Is this worth a mechanism, given the class may have one member?** — the project owner. The
  recommendation is to **count first and decide after**: the second criterion is deliberately ahead of
  the decision, because *ask whether the remedy's target class is empty* is the question this kind of
  proposal skips. If the count is one, *nothing, plus a stated convention* is likely right.

### The count, run 2026-08-23 — and the class is not the one this record names

**Every open task was classified individually, not filtered.** A filter here would have to key on prose
and would report its own coverage as complete; the ten were read one at a time and the groups sum, so
a member cannot be dropped invisibly.

| Task | Held up by | Does a view see it? |
| :--- | :--- | :--- |
| [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) | **a person** — only the owner can say whether the reader output still exists | no — sorts first of ten |
| T-230, this record | **a person** — it runs to this count and the decision is the owner's | no |
| [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md) | **a person** — authorised for `plan` and no further, so the next phase needs the owner's word | no — sorts sixth, at `planned`, as if ready |
| [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md) | **a person** — an unanswered owner question, and outside the grant | no |
| [T-231](T-231-cut-the-next-release.md) | **a person** (the release is the owner's act) **and a task** | partly — reports blocked, but on the task half only |
| [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | **a task *starting*** — `blocked_by: [T-231]` says *until it closes*, which overstates the gate | partly — reports blocked, for the wrong reason |
| [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) | **a task closing** | yes, correctly |
| [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md) | nothing — the owner answered on 2026-08-22 | n/a |
| [T-236](T-236-build-check-classes-and-give-the-class-derivation-one-home-in-the-package.md) | nothing — its four questions are measurements, none the owner's | n/a |
| [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md) | nothing — the scratch repository was authorised on 2026-08-22 | n/a |

**4 invisible and startable-looking + 1 person-gated but reported + 1 gated on a start + 1 correctly
reported + 3 not gated = 10**, which is every open task.

**Gated on an external event: zero.** §1's only named instance,
[T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), left the class on
2026-08-22 when its event acquired a task. **So the class this record was raised for is empty, and the
count found a different one that is not** — four tasks held up by a *person*, none of which any view
can see, all sorting as though a session could pick them up. §1 admitted that shape as a secondary
question; the count makes it the primary one.

**The defect bites exactly where nothing points.** Every task gated on another *task* already reports
blocked. Every task gated on a *person* reports nothing at all.

### What the count changes about the recommendation

**Measured, not assumed:** `list` rejects a filter on a field the project has not named —

```text
$ ./plugin/bin/taskmd list --waiting_on "the project owner" --open
unknown filter: --waiting_on. This project accepts: --adopter_visible, --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related, --status, --type,
--work_package
exit 2
```

`adopter_visible` is in that list and is **not** in the shipped schema — it is in this project's own
`context_fields`. So a project can add a field, name it in its own config, and filter on it, with **no
shipped-config key and no code change** — which is the constraint [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)
imposes and the reason the obvious candidate looked closed.

**Revised recommendation, for the owner: ship nothing; add `waiting_on` to this project's own
`context_fields`.** `list --waiting_on ...` then answers *what cannot be started* as a command, per
project, and an adopter who wants it does the same in their config. *What it does not do, stated
because it is the whole of the original complaint:* it does not change the **default ordering**, so
those four still sort as startable. Buying that would mean teaching the ordering rule to read a status
value, which overturns `is_blocked`'s own docstring — *"Not a status value — a task can be marked
anything and still be held"* — and makes *blocked* a self-declaration nothing verifies.

*Rejected: relax `NO BLOCKER` so `status: blocked` is legal with no edge* — it is the cheapest way to
move the four to the bottom, and it trades a checked state for an unchecked one in the validator that
exists to check states. *Rejected: a new shipped-config key* — T-106, every adopter's config errors on
upgrade. *Rejected: nothing at all, plus a convention* — it is what happens today, and the third
acceptance criterion would then have to put the convention somewhere a session reads, which means tier
1, which is paid on every turn of every session for a class of four.

~~**This record stops here**, as its grant row of 2026-08-22 says it should: the count is done and the
decision is the owner's.~~ **Answered 2026-08-23: the per-project `waiting_on` field.**
The record resumed the same day and is closed below.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Add `waiting_on` to this project's own `context_fields`, and to nothing shipped | the edited `.taskmd/config.md` |
| 2 | Give the field to the one open task that is genuinely gated on a person, and to no other | that task's front matter |
| 3 | Run the filter that was refused before the change | the output |
| 4 | Show the shipped default is untouched, which is the fourth criterion | a diff |

**Step 2 adopts exactly one instance, deliberately.** §1 puts *fixing T-182* out of scope with the
reason that an instance adopts a mechanism separately — so this record builds the mechanism and
proves it on the single live case rather than retro-fitting the backlog. **A mechanism proved on a
corpus with no positives has not been proved**, which is why it is one and not zero.


## 3. Implement

**Decisions & assumptions**

- **The owner chose the per-project field on 2026-08-23**, from the three the count left standing.
  *Rejected: relax `NO BLOCKER` so `status: blocked` is legal with no edge* — the cheapest way to move
  the four to the bottom of `list --open`, and it overturns `is_blocked`'s own docstring and makes
  *blocked* a self-declaration nothing verifies, inside the validator that exists to verify states.
  *Rejected: nothing, plus a stated convention* — what happens today, and the convention would have to
  live where a session reads before choosing work, which is tier 1, paid on every turn for a class of
  four.
- **What the answer does not buy is stated with it** — 2026-08-23. The default ordering is unchanged:
  a person-gated task still sorts as startable. What changes is that *which tasks cannot be started*
  becomes a **command** instead of prose no view reads. That was the trade named when the option was
  put, not discovered afterwards.
- **One instance adopted, and it is [T-231](T-231-cut-the-next-release.md)** — 2026-08-23. It is the
  live case: the release is the owner's act and no task blocks it, so nothing in any view said so.
  **Its own work is untouched and remains outside this session's scope** — one field was added to its
  front matter and nothing else. §1 puts adopting instances out of scope, so no other task was
  retro-fitted.

**Outputs produced**

- `.taskmd/config.md` — `waiting_on` added to `context_fields`
- `tasks/T-231-cut-the-next-release.md` — one field

**Verification**

**Step 3 — the same command, before and after.** Before the config change, on 2026-08-23:

```text
$ ./plugin/bin/taskmd list --waiting_on "the project owner" --open
unknown filter: --waiting_on. This project accepts: --adopter_visible, --blocked_by, --blocks,
--business_value, --children, --effort, --owner, --parent, --phase, --related, --status, --type,
--work_package
exit 2
```

After:

```text
$ ./plugin/bin/taskmd list --waiting_on "the project owner" --open
T-231   proposed   M6   specify   Cut the next release   -
```

**A refusal became an answer, and the answer is a real row rather than an empty list** — which is the
difference between a filter that is accepted and a mechanism that works.

**Step 4 — nothing shipped changed.**

```text
git diff --stat -- plugin/skills/taskmd/taskmd/defaults/config.md   ->   (empty)
```

So [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s bar is not approached: an
adopter's config gains no required key, and a clone that never adds `waiting_on` behaves exactly as
before. The field is carried and uninterpreted for anyone who does not name it, which is the shipped
schema's own rule about unnamed fields.

**Gates.** `taskmd check` exit 0; `python -m pytest tests/ -q` reports `337 passed, 8 subtests
passed`, unchanged.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded with its reason, and every candidate that was rejected is named with what it would have cost | met | Three candidates, one chosen; the two rejected are in §3 with their costs — the `NO BLOCKER` relaxation trades a checked state for an unchecked one, and *nothing* puts a convention in tier 1 for a class of four |
| How many open tasks are in this state **today** is counted, not estimated | met | Counted per item on 2026-08-23, all ten open tasks classified individually and the groups summing to ten. **The count refuted the record's premise**: zero gated on an external event, four gated on a person |
| If the answer is *nothing*, what a session should do when `list` hands it an unstartable task is stated somewhere a session reads | **n/a** | The answer is not *nothing*. Recorded as not-applicable rather than met, so a later reader can see the branch was not taken rather than not checked |
| Any shipped-schema change is checked against what it does to an adopter's existing config on upgrade | met | There is no shipped-schema change: `git diff` over `taskmd/defaults/config.md` is empty. The field is added to this project's own config only, so an adopter's config gains no required key and T-106's failure mode is not reached |

**Child fix tasks raised**
- none. Adopting the field on further instances is out of scope by §1 and needs no task: it is one
  line in a record, taken when a record is next worked.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 held one, the owner's, answered
2026-08-23 and struck through. **One residual is recorded rather than left implicit**: the default
ordering still sorts a person-gated task as startable, and that is a stated cost of the chosen option
rather than an unfinished part of it. Buying it would mean the rejected `NO BLOCKER` relaxation, which
the owner declined with the reason in §3.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed: three criteria met and one recorded n/a.** The owner chose the per-project `waiting_on` field, so the third criterion's *if the answer is nothing* branch never fired — marked **n/a** rather than met, so a reader can see it was not taken rather than not checked. **The mechanism was proved on a real positive, not on an empty filter**: `--waiting_on` went from `unknown filter … exit 2` to returning [T-231](T-231-cut-the-next-release.md), which is the live case — the release is the owner's act, no task blocks it, and until today no view said so. **One instance adopted and no more**, because §1 puts retro-fitting instances out of scope; T-231's own work is untouched. **Nothing shipped changed** — `git diff` over the default config is empty, so no adopter's config gains a required key and [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s failure mode is not reached. **The cost is recorded with the answer**: the default ordering still sorts these as startable, and buying that would need the `NO BLOCKER` relaxation the owner declined. |
| 2026-08-23 | (no change) | **The count is done and this record stops at it, exactly as its grant row says.** Phase and status are unchanged because the decision is the owner's and nothing here decides it. **The count refutes the record's own premise, which is what putting it first was for.** Tasks gated on an external event: **zero** — [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) left the class on 2026-08-22 when its event acquired a task. What the count found instead is **four open tasks held up by a *person***, invisible to every view and sorting as though a session could start them. §1 named that shape as a secondary question; it is the primary one. **The ten were classified one at a time and the groups sum to ten**, because a filter here would have to key on prose and would report its own coverage as complete. **The mechanism the recommendation now rests on was run rather than reasoned about**: `list` refuses `--waiting_on` with exit 2, and its own error names `adopter_visible`, which is in this project's `context_fields` and not in the shipped schema — so a per-project field costs no shipped key and no code, which is what [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) appeared to have closed off. **What it does not buy is the default ordering**, and that is stated with the recommendation rather than left for the owner to discover. |
| 2026-08-22 | (no change) | **The grant was extended a third time**, to [T-234](T-234-decide-whether-a-grant-s-membership-is-copied-into-every-record-or-derived.md), scoped there to finishing that record and not to building what it decides. The rows below are what the grant covered when each was written and are left as written; **T-234's own row carries the membership as it now stands**. Nothing about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The grant is extended a second time: it now reaches what the work raises.** The **project owner** instructed on **2026-08-22**, handing this batch to a new session, that it be worked **unattended, through the full lifecycle, committed and pushed, including any task raised during the execution**. **What that adds:** a task the session raises may be carried to closure under the same authority, without coming back for a phase. **What it does not add:** anything already excluded — [T-231](T-231-cut-the-next-release.md), which is the owner's act; [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md); [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md); [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md); and **any audit**, which remains the boundary the owner named. **A task raised under this extension carries the grant in its own Log, exactly as these six do.** That is the mechanism and not bookkeeping: a raised task with no grant row is not covered by the fact of having been raised. **It still authorises phases, not answers** — a raised task whose open question is the owner's stops where it stands. The same extension ran earlier today over six raised tasks: two carried no owner question and were closed, four did and were left at `specify`. |
| 2026-08-22 | (no change) | **The grant was extended, later the same day.** The owner added [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) to the unattended grant recorded below, because it became the blocker of [T-231](T-231-cut-the-next-release.md) and the release would otherwise have waited on one person. **The list in the row below is what the grant covered when it was given, and it is left as written**; T-232's own row carries the membership as it now stands. Nothing else about this record's authorisation changed. |
| 2026-08-22 | (no change) | **The class moved while this record was open, and both directions are worth the count.** [T-231](T-231-cut-the-next-release.md) was raised the same day, which gave [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) — §1's only named instance — a real task to point `blocked_by` at, so it now sorts last and reports blocked. **That is not the class shrinking to nothing; it is one member leaving by a route that was not available to it**: the event acquired a task. **And the same edge is imprecise in a way the count should notice.** `blocked_by` means *cannot proceed until those close*, while T-182's real gate is *until T-231 has started* — a shape the schema cannot say either, and a second sub-kind for §1's second criterion to distinguish. So the count runs over two questions, not one: what is gated on a non-task, and what is gated on a task **starting** rather than closing. |
| 2026-08-22 | (no change) | **Unattended authorisation, and its limits.** The **project owner** instructed on **2026-08-22** that a session work **unattended** toward a release they want soon, **stopping before the audit** that will precede it. **What it covers here:** this record, through the full lifecycle to closure, without stopping to ask for each phase. **What the grant covers in total:** [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md), [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md), [T-228](T-228-decide-whether-the-reader-s-framing-verdict-reopens-the-accepted-balance.md), [T-230](T-230-a-task-gated-on-an-external-event-has-no-field-and-sorts-as-startable.md) and [T-224](T-224-re-run-the-binding-s-github-side-measurements-or-record-that-they-cannot-be.md), and nothing else. **What it does not cover:** [T-225](T-225-have-a-second-uninvolved-reader-write-a-declaration-from-the-repaired-clause.md), which needs the owner to run an uninvolved reader and no session can supply one; [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), gated on there being a release to make, which is nobody here's to schedule; [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), which is not release work and whose own grant of the same date covered `plan` and said so; and **any audit** — no audit umbrella may be raised, and no audit started, which is the boundary the instruction names. **It authorises phases, not answers**: an open question that is the owner's stops the record where it stands. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task:** §1's second acceptance criterion — count how many open tasks are in this state today — comes **before** the decision, and the decision itself is the owner's. So this record runs to the count and stops there with a recommendation, which is the grant authorising phases and not answers. |
| 2026-08-22 | → proposed | Raised at the owner's request on 2026-08-22, after a survey of the open backlog put [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) last on a gate the tool cannot see while `list --open` put it first. **Both existing mechanisms were run rather than reasoned about**: `blocked_by` has no target when the blocker is an event, and `status: blocked` without an edge is `NO BLOCKER`, exit 1, shown on this project's own fixture. **A decision and not a fix**, by the schema's own test — the change is not known until the question is answered. **The candidate that looks obvious is nearly closed already**: [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) records that the shipped config cannot gain a key without erroring every adopter on upgrade, which was read here rather than remembered — the guessed title of that record was wrong and its real one is the sharper fact. **The second criterion is placed deliberately ahead of the decision**: a mechanism argued at size and applied to a class with one member is the failure this kind of proposal makes, so the count comes first. |
