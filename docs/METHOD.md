# The taskmd Method

**How work is tracked — independent of where it is stored.** This document names no field, no file,
no identifier format and no command; those belong to a *binding*, which maps the method onto one
particular tracker. A project moving from local files to an issue tracker changes its binding, not
this. Nothing here assumes software either — a research question, a talk, a training course and an
operations runbook are all tracked this way, and the worked examples are not code.

**Read this spine; load a phase file when its moment arrives.** Everything in the spine governs
every turn; the files in §7 do not, so they are not carried around.

---

## 1. Core rules

1. **No work without a task.** Before any analysis, drafting or production, the task exists and says
   what it is for.
2. **The lifecycle is mandatory** — specify → plan → implement → review (§2). Every task passes
   through all four, however small.
3. **One home per fact.** Anything derivable is derived, never written down a second time (§4).
4. **Audit findings become their own tasks** and are never fixed where they are found (§5).
5. **Done means consistent.** A task closes when its outcome exists, its record is current, and the
   `implement` evidence is written down — undocumented progress did not happen.

---

## 2. The lifecycle

| Phase | What happens | Exit criterion | Procedure |
| :--- | :--- | :--- | :--- |
| **specify** | Establish what the outcome is and how it will be judged. | Acceptance criteria written, and agreed by whoever owns the outcome. | [specify](method/specify.md) |
| **plan** | Break the work into steps and name what each produces. | Every step names an output, and every output is named precisely enough that someone else could look for it. | [plan](method/plan.md) |
| **implement** | Do the work. Record decisions as they are taken, not afterwards. | **The outcome has been checked by being used, and the evidence is recorded.** | [implement](method/implement.md) |
| **review** | Judge the result against the acceptance criteria written in `specify`. | Every criterion is either met or carries a child task that will meet it. | [review](method/review.md) |

**Phase and status are independent.** *Phase* says where the work has got to; *status* whether it
can move. Being stuck is not a phase — a task waiting on someone keeps the phase it reached, and
never moves backwards to record an obstacle.

**Verification is `implement`'s exit criterion, not `review`'s.** "The planned outputs exist" is not
an exit criterion, because a wrong output exists just as convincingly as a right one — someone must
have *used* the outcome and said what happened ([why](method/rationale.md), [how](method/implement.md)).

---

## 3. Conduct

Three rules that apply on every turn, in every phase — which is why they are in the spine.

### 3.1 One phase per request — never auto-advance

Do the phase that was asked for, then stop and report. Do not continue into the next one because it
is obvious, because the plan already describes it, or because a note said it was next.

**A pointer is context, not authorization.** A "next step" line, a resumption note, an unfinished
checklist, the rhythm of the last three tasks — none of these is a request
([why](method/rationale.md)).

### 3.2 Ask to the phase's exit criterion — and batch it

The exit criterion in §2 defines how much detail is *enough*. Ask for what is still missing to reach
it, and nothing beyond it: a `specify` that cannot state how the outcome will be judged is not
finished, and a `specify` that has interrogated every downstream detail has done `plan`'s work
badly.

**Put every question in one turn.** Questions delivered one at a time make the other person hold the
whole thread open while answering piecemeal, and each answer arrives too late to inform the next
question. Work out everything you need, then ask once.

Do not guess in place of asking. An assumption is acceptable when it is *recorded as an assumption*
and the work would survive being wrong; otherwise it is a question.

### 3.3 Surface what you discover — never absorb it, never drop it

Work turns up things nobody anticipated: a better approach, a flawed premise, an unrelated defect,
a missing prerequisite. Each one goes to exactly one of two places:

- **It changes what the current task should produce** → raise it as a question now, before
  continuing. Quietly widening or narrowing the outcome substitutes your judgement for the owner's.
- **It is actionable but outside this task** → raise a new task for it. This costs one record and
  keeps the current task honest.

What must never happen is the third option: fixing it silently, or noticing it and moving on. A
silent fix makes the task's record false; a dropped observation is lost the moment the session ends.

---

## 4. Edges

Tasks relate to each other in exactly three ways. The names are the project's to choose; the set is
not, because each is a different traversal.

| Kind | Shape | Meaning |
| :--- | :--- | :--- |
| **hierarchy** | at most one, per task | This task belongs to that one. The inverse is that task's children. |
| **dependency** | a list | This task cannot proceed until those close. The inverse is what it is holding up. |
| **soft** | a list | Context worth having in both directions. It gates nothing. |

### Which edge to use

- Can this task's work start and finish while the other is still open? **No** → dependency.
- Would someone working this task make a worse decision without knowing about the other?
  **Yes** → soft.
- Neither → do not link them. A graph that links everything says nothing.

### Store the forward edge; derive the rest

Record a relationship **once**, on the task that is constrained — the child, the blocked one, either
end of a soft link. The other direction is computed when a task is read, so both ends show it: one
write is always enough, and no view can miss a link recorded on the far side ([why](method/rationale.md)).

Recording the other side as well is allowed — it collapses into the same single link, so nobody has
to know which end "owns" it. What the rule forbids is a design that *compels* the second write.

---

## 5. Audit

An audit is a **task type, not a phase** — requested, never automatic, and nothing passes "through"
it. It produces one umbrella task whose findings become child tasks, under one rule: **a finding is
never fixed where it is found.** Procedure: [audit](method/audit.md).

---

## 6. Where each kind of fact lives

Rule 3, applied: before writing anything down, find its one home —
[where facts live](method/where-facts-live.md). The homes are **roles**, not locations; the binding
says which artifact plays each role for a given tracker. Where a fact seems to belong in two homes,
it belongs in the more durable one and the other **points** at it.

---

## 7. Load on demand

| Document | Load when |
| :--- | :--- |
| [specify](method/specify.md) | Starting a task, or its outcome is not yet agreed |
| [plan](method/plan.md) | The outcome is agreed and the work needs breaking down |
| [implement](method/implement.md) | Executing a plan |
| [review](method/review.md) | Judging a finished outcome against its criteria |
| [audit](method/audit.md) | Examining a body of work, or handling findings |
| [where facts live](method/where-facts-live.md) | About to write something down and unsure where it belongs |
| [rationale](method/rationale.md) | A rule looks wrong, or someone proposes changing one |

Load the one you are about to use — reading the set in advance costs exactly what the single long
document cost, which is the thing this structure exists to avoid.
