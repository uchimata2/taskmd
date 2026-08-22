# The taskmd Method

**How work is tracked — independent of where it is stored.** This document names no field, no file,
no identifier format and no command; those belong to a *binding*, which maps the method onto one
particular tracker. A project moving from local files to an issue tracker changes its binding, not
this. Nothing here assumes software either — a research question, a talk, a training course and an
operations runbook are all tracked this way, and the worked examples are not code.

**Read this spine when task work begins; load a phase file when its moment arrives.** This document
is not loaded on every turn — the project's own always-loaded conventions are, and they say when this
one arrives. Everything here governs the work; the files in §7 do not, so they are not carried around.

---

## 1. Core rules

1. **No work without a task.** Before any analysis, drafting or production, the task exists and says
   what it is for.
2. **The lifecycle is mandatory** — specify → plan → implement → review (§2). Every task passes
   through all four, however small.
3. **One home per fact.** Anything derivable is derived, never written down a second time (§4).
4. **Audit findings become their own tasks** and are never fixed where they are found (§5).
5. **Done means consistent.** A task closes when its outcome exists, its record is current, and the
   `implement` evidence is written down — undocumented progress did not happen. *Current* keeps
   binding after it closes: correct what the record says about the **present**, and never rewrite
   what it says about the **past** — annotate that instead.

---

## 2. The lifecycle

| Phase | What happens | Exit criterion | Procedure |
| :--- | :--- | :--- | :--- |
| **specify** | Establish what the outcome is and how it will be judged. | Acceptance criteria written, and agreed by whoever owns the outcome. | [specify](method/specify.md) |
| **plan** | Break the work into steps and name what each produces. | Every step names an output, and every output is named precisely enough that someone else could look for it. | [plan](method/plan.md) |
| **implement** | Do the work. Record decisions as they are taken, not afterwards. | **The outcome has been checked by being used, and the evidence is recorded.** | [implement](method/implement.md) |
| **review** | Judge the result against the acceptance criteria written in `specify`. | Every criterion is either met or carries a task that will meet it — §4 says which edge, and whether this task may then close. | [review](method/review.md) |

**Phase and status are independent, and that independence is about movement.** *Phase* says where
the work has got to; *status* whether it can move. Being stuck is not a phase — a task waiting on
someone keeps the phase it reached, and never moves backwards to record an obstacle.

**Where the two correspond, phase names the phase the work is _at_ — never the one it will do next.**
A task that has finished one phase and is waiting for the next to be asked for is still at the one it
finished. Both readings sit in the table above, and two projects have now picked different ones, so
the method says which it means. Nothing here checks it: whether a tracker can is a binding's
question, not this document's.

**Verification is `implement`'s exit criterion, not `review`'s.** "The planned outputs exist" is not
an exit criterion, because a wrong output exists just as convincingly as a right one — someone must
have *used* the outcome and said what happened ([why](method/rationale.md), [how](method/implement.md)).

---

## 3. Conduct

Three rules apply on every turn of the work, in every phase. **Two of them bind before it is clear
that there is any task work** — *one phase per request, never auto-advance*, and *surface what you
discover, never absorb it, never drop it*. This document is loaded when task work begins, which is
already too late for those two, so they are **not stated here**: they belong wherever your project's
always-loaded conventions live, and a copy here would be a second home for a rule that must have one.
[`../adopt.md`](../adopt.md) §4 carries the text to put there, and
[rationale](method/rationale.md) carries the argument behind both.

**All three are numbered below, and only one is stated**, so that a citation of any of them
resolves to a heading a reader can find. A heading that says where a rule lives is not a copy of the
rule — but the moment either of the two below says what its rule *is*, it has become the second home
this section exists to prevent.

### 3.1 One phase per request — never auto-advance

**Not stated here.** It binds before there is any task work, so a session that needs it has not
loaded this document. Its home is your project's always-loaded conventions:
[`../adopt.md`](../adopt.md) §4 carries the text to put there, and
[rationale](method/rationale.md) the argument for putting it there.

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

**Not stated here**, for the reason under 3.1. Its home is your project's always-loaded conventions:
[`../adopt.md`](../adopt.md) §4 carries the text, and [rationale](method/rationale.md) the argument.

---

## 4. Edges

Tasks relate to each other in exactly three ways. The names are the project's to choose; the set is
not, because each is a different traversal.

| Kind | Shape | Meaning |
| :--- | :--- | :--- |
| **hierarchy** | at most one, per task | This task belongs to that one. The inverse is that task's children. |
| **dependency** | a list | This task cannot proceed until those close. The inverse is what it is holding up. |
| **soft** | a list | Context worth having in both directions. It gates nothing. |

### A child holds its parent open

**A task may not close while any of its children is open.** Hierarchy says the child *belongs to*
the parent, so an open child is a part of the parent that is not finished, and a parent closed over
one claims an outcome it has not got. This is the only edge that constrains **closure**: a dependency
constrains when a task may *start*, a soft edge gates nothing, and neither says anything about when a
task may close.

**Decided on 2026-08-22, against the narrower reading that only an audit umbrella is held open** —
and the narrower reading was measured before it was rejected, not argued away. Run over a real
backlog of 218 tasks, the general rule found three closed parents with an open child and the audit
reading found none. All three turned out to be the same thing: a **finished** outcome with a residual
attached to it by the wrong edge. The narrower rule would not have permitted those three, it would
have hidden them — which is the difference between a rule that is lenient and one that is blind.

**What the general rule costs is that the choice of edge now matters**, which is what the next
section is for.

### Which edge to use

- Is the other task **part of this one's outcome**, so that this one is not finished until it is
  done? **Yes** → hierarchy — and it will hold this task open, per the section above.
- Can this task's work start and finish while the other is still open? **No** → dependency.
- Would someone working this task make a worse decision without knowing about the other?
  **Yes** → soft.
- Neither → do not link them. A graph that links everything says nothing.

**The residual is the case this gets wrong**, and it is common enough to name. Work often throws off
something that is *about* a finished task without being *part* of it: a stronger test of a result
that already stands, a use that waits on an event nobody here controls, a reader nobody can summon.
It arrives feeling like unfinished business, so it gets a hierarchy edge — and then holds a finished
task open for as long as the world takes. **That is a soft edge.** The question is not whether the
new task matters; it is whether the old one's outcome is incomplete without it.

### Store the forward edge; derive the rest

Record a relationship **once**, on the task that is constrained — the child, the blocked one, either
end of a soft link. The other direction is computed when a task is read, so both ends show it: one
write is always enough, and no view can miss a link recorded on the far side ([why](method/rationale.md)).

Recording the other side as well is allowed — it collapses into the same single link, so nobody has
to know which end "owns" it. What the rule forbids is a design that *compels* the second write.

**What the rule is for.** One home per fact is a **means**, not the end. What it buys is that nothing
can disagree with itself and that nobody has to keep two things agreeing — inconsistency and
administration are the two costs, and the rule exists to hold both near zero. Almost no second write
buys anything against either, which is why the rule reads as absolute — and the paragraph above is
not an exception to it, because nothing there *compels* the second write. **Knowing the purpose is
not itself a second way to deviate.** A rule you may set aside whenever you judge the trade worth it
is not a rule, and there is exactly one grounds, below.

**A limitation of the system you are on is grounds to deviate.** Where a tracker, a platform or a
file format offers no way to record a fact once — a field it will not derive, a configuration that
replaces a default instead of extending it, a manifest that must repeat what another already states —
write it twice. Then **say, where a reader meets the second copy, what forces it.** The rule is not
suspended; it is exchanged for the obligation to keep the constraint visible, so that the day the
system stops compelling the copy, somebody can find it and delete it.

**A limitation you assumed does not qualify — only one you were refused.** *The platform needs both*
is a claim about the platform. It is the cheapest claim here to check and among the easiest to be
wrong about, and the usual result of checking is that one of the two copies was never required. So
the test is not whether the second write **seems** unavoidable; it is whether the single write was
**attempted and refused**, with the refusal recorded beside the copy it justifies. This is the case
the clause exists to turn away, and it is the one that gets through — an untested claim about the
system has the same shape as a real limitation, where convenience and *it reads better in both
places* do not and never fooled anybody.

---

## 5. Audit

An audit is a **task type, not a phase** — requested, never automatic, and nothing passes "through"
it. It produces one umbrella task whose findings become child tasks, under one rule: **a finding is
never fixed where it is found.** Procedure: [audit](method/audit.md).

An audit whose subject is **everything a project is about to release** is the same type at a size
that needs six rules the ordinary procedure does not: [pre-release audit](method/pre-release-audit.md).

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
| [pre-release audit](method/pre-release-audit.md) | The audit is of everything about to be released, and will not fit one session |
| [where facts live](method/where-facts-live.md) | About to write something down and unsure where it belongs |
| [rationale](method/rationale.md) | A rule looks wrong, or someone proposes changing one |

Load the one you are about to use — reading the set in advance costs exactly what the single long
document cost, which is the thing this structure exists to avoid.
