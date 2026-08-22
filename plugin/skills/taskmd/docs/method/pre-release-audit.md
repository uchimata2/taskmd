# pre-release audit

> One kind of audit, scaled up. Type and spine: [`../METHOD.md`](../METHOD.md) §5. Procedure:
> [`audit`](audit.md).

A pre-release audit examines **everything a project is about to put in front of people**, rather than
one area of it. It is the largest audit a project runs, and the only one whose stated scope is *all of
it*.

Everything in [`audit`](audit.md) holds — one umbrella, a finding threshold stated before looking, a
child task per actionable finding, no finding fixed where it is found, and the umbrella closed only
when every child is resolved. **This file adds the six things that only start to matter at that
size**, and nothing else.

## When one runs

**Never a step in the release procedure.** That an audit is requested rather than automatic is
[`../METHOD.md`](../METHOD.md) §5's rule about every audit and is not repeated here; what this size
adds is that the request may not be wired into the sequence. An audit of everything costs several
working sessions. Wired into every release it becomes a cost the release cannot refuse, and a cost
that cannot be refused is one that gets skipped — quietly, and first under time pressure. Keep it
outside the sequence and ask for it when the release is worth it.

**When it does run, it finishes before the release checks do.** Whatever a project uses to decide it
is ready, an audit that runs afterwards invalidates that decision by changing what it decided about.

---

## 1. Scope is a grade, not a list

*Everything* is not a scope. It also cannot honestly be narrowed, because the reason for this audit is
that nobody knows where the problem is.

**Every item is examined; what differs is the brief.** Grade the subject rather than trimming it:

| Grade | Applies to | Brief |
| :--- | :--- | :--- |
| **Wide** | what people meet first, what is current, what changes fastest | the full finding threshold, plus anything the reader notices |
| **Narrow** | the settled record — closed work, superseded material, background | one question, normally: *does anything written here contradict what is true today?* |
| **Instrument only** | what cannot be read whole, or must not be | examined by measurement or by use, never by reading |

The third grade is the one people leave out and then breach. A recording, a long dataset, a rendered
artefact, a live system: reading it end to end is either impossible or forbidden by the project's own
rules. Say so in the plan, name the instrument used instead, and the audit stays honest at the point
it would otherwise quietly skip something.

**Aspects keep the cycles from all becoming "documentation".** Pick a small set in the plan — four is
usual — so that every cycle sits under one of them and two cycles never examine the same thing under
different names. **What the aspects are is this audit's design and belongs in its plan**
([`audit`](audit.md), *Procedure*): a set carried in from the last audit examines each new subject for
the last subject's problems. One project's set, as an illustration of the *shape* rather than a list
to adopt: how the work is decided and tracked; the internal record; what an outsider reads; and the
thing itself.

---

## 2. Coverage is a partition, and it fails

At this size the question stops being *what did you find* and becomes *what did you actually look at*.

**Every item in scope ends in exactly one of three states**, and the record says which:

1. **examined, and it produced a finding**;
2. **examined, and clean** — recorded, with what was checked;
3. **not examined**, with the reason.

**An item in none of the three is a gap in the audit, not a clean item.** That is the whole rule, and
it is what makes a finished audit mean something: without it, *we looked at everything* is
unfalsifiable, and the areas nobody reached are indistinguishable from the areas that were fine.

State 2 is [`audit`](audit.md) step 4's no-action finding, kept per area rather than per finding, and
it is the row a reader checks first.

---

## 3. An audit larger than one session runs in cycles

**One subject per cycle.** A cycle names what it examines, the brief for that subject, the instrument,
and what it produced. It is sized so that one working session can read it *and still judge it* — the
limit is attention, not volume, and it is reached long before the material runs out.

Four rules, each of which was a failure first:

- **A cycle ends with the record written**, including a cycle that ran out of time half way. An
  unrecorded finding is a finding lost, and the session that holds it is the one about to end.
- **Order cycles by where findings are expected, not by how the subject is filed.** An audit stopped
  early must still have been worth running, and the decision to stop is usually made after it starts.
- **Re-examine a cycle whose subject later changed.** Resolving a finding in cycle 9 can falsify what
  cycle 2 concluded, and nothing will say so.
- **Run the densest cycle twice** — once in order, and once after the last remedy has landed. Remedies
  are the largest single source of new findings, which is §5 arriving as a schedule.

A cycle is also the natural handover point: it is the unit another person, or another session, can
pick up without inheriting a half-formed conclusion.

---

## 4. Severity has to oblige something

A severity that only sorts the list is decoration. Each level names what it *requires*:

| Severity | Test | Obligation |
| :--- | :--- | :--- |
| **High** | it misleads the audience, breaks something people rely on, loses work, or makes a stated procedure unfollowable | a child task, and the release does not go out while it is open |
| **Medium** | it costs real effort every time someone meets it, or becomes High at the next change | a child task, closed or explicitly deferred with a recorded reason before the release |
| **Low** | true, small, and nothing depends on it | batched into one task, or accepted in the record with a reason and a date |

**Severity measures the audience's cost, not the fixer's effort.** A one-character error in the first
instruction a newcomer follows is High. A long-unread background document that is out of date is Low.

**Batching the Low level is deliberate.** [`audit`](audit.md) step 4 raises a child task per actionable
finding, which is right at ordinary scale and breaks at this one: sixty task records for sixty
one-line corrections is a cost the tracker pays and nobody recovers. Batching keeps every finding in
the record and stops the tracker from becoming the audit's byproduct. If most findings are Low, the
threshold from step 2 was set too low — that, and not the batch, is the thing to fix.

---

## 5. A remedy is a hypothesis

**A finding says what is wrong. What to do about it is a guess until someone tries it**, and the two
belong in different columns.

This is the rule with the sharpest evidence behind it. In the one project that has run an audit of
this shape and then measured itself: **two of thirteen findings held exactly as written, every error
was in the proposed remedy and none in the finding itself, and four remedies were refused by a
measurement taken while implementing them** — obeying the ranking as written would have deleted work
that was carrying its weight. The ranking was worth having. Following it without re-measuring would
have done damage.

So: write the remedy as a proposal, let the person implementing it measure before committing to it,
and record what the measurement said. A remedy that survives contact is worth more than one that was
never tested.

---

## 6. Grade the ranking after the remedies exist

**Run a second pass once the work is done**, not at ranking time. For each finding: what was predicted
against what it actually cost and returned, and one line on what the difference was.

It is cheap next to the audit, and it is the only thing that makes the *next* audit better rather than
merely later. An audit that never grades itself keeps whichever ranking it happened to write down,
and repeats its author's expectations indefinitely.

**A grading pass that confirms every prediction was not run honestly.** Say which prediction the
measurement refused; if genuinely none did, say that and say how it was checked.

---

## The umbrella, and when the findings move out of it

[`audit`](audit.md) step 3 records every finding **in the umbrella**, which is correct and stays
correct for most audits. At this size it stops working: an umbrella carrying sixty findings, their
evidence and their coverage ledger is no longer a task record, and the lifecycle sections disappear
underneath it.

**Then, and only then, the findings move to their own record**, under three conditions:

1. **The umbrella keeps the counts and the link**, so a reader of the task still learns what happened.
2. **The separate record is the only home for a finding's statement.** Nothing restates it; a child
   task points at it. Two copies of a finding disagree the first time either is edited.
3. **Each finding keeps a stable identifier**, never reused and never renumbered, so a child task and
   a later grading pass can name the same thing.

This is a scale exception to one step of the ordinary procedure, not a second way of doing audits.
Below that scale, the umbrella is the record.

---

## What this cannot see

Say so in the review, next to what it did see:

- **Taste.** Whether something reads well, whether it is worth its length.
- **Anything the instrument-only grade could not reach**, which is exactly where the grade was applied
  because reading was impossible.
- **A defect whose only instrument is a person**, and which therefore depends on which person.
- **What the audit itself broke.** §3's last two rules exist for this and reduce it rather than remove
  it.

---

## Worked example — a training course before its first cohort

Umbrella scoped to *"everything the first cohort will meet"*, with the threshold stated first: **a
claim we cannot support, an instruction that cannot be followed as written, or two materials that
contradict each other.** Four aspects, chosen in the plan: how the course is run, the internal
record, what participants read, and the sessions themselves.

| Cycle | Subject | Grade | Outcome |
| :-- | :--- | :--- | :--- |
| 1 | The joining instructions and the schedule | Wide | 2 findings — a room that changed, a prerequisite listed nowhere else |
| 2 | The eight participant handouts | Wide | 1 finding — two handouts give different figures for the same case study |
| 3 | The three recorded lectures | Instrument only | Watched at speed against their own outlines; 1 finding — lecture 2's outline lists a demo that was cut |
| 4 | The facilitator's notes from the pilot | Narrow | Examined and clean; the two changes it recommended are both in the current materials |
| 5 | The exercise answer keys | Wide | Examined and clean |

Cycle 3 is the grade doing its job: the lectures could not be read, so the audit says how they were
examined instead of skipping them. Cycles 4 and 5 are the partition doing its job — without those two
rows a reader cannot tell whether the notes and the keys were checked or missed. And the room change
in cycle 1 is High, not because it was hard to find, but because a participant who follows the
instruction arrives at the wrong place.
