---
id: T-173
title: Decide whether check can know a phase without breaking every adopter
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-172, T-151, T-146]
work_package: M6
owner: the project owner
business_value: low
effort: s
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-173 — Decide whether check can know a phase without breaking every adopter

## 1. Specify

**Outcome**
A recorded answer to whether `check` should be able to reason about a task's *phase*, and at what
price — or a recorded decision that it should not, so the next person to want it finds the reason
rather than the gap.

**Why this one**
Raised from [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md)'s `review`,
carrying the unmet half of its first acceptance criterion. `check_abandoned_slots` reports a slot left
in a **closed** record. The criterion agreed at `specify` was wider: no record carrying a slot in a
section it has **already passed**. A task sitting at `review` with an unfilled `implement` satisfies
the wider text and is not reported.

**The narrowing was a decision, not an omission**, taken by the owner during T-172's `implement` once
the price was known. Three things the tool does not know stand in the way, and they are in T-172 §3
with the evidence:

- which front-matter field carries the phase — `phase` appears nowhere in `schema.py`
- that a body heading corresponds to a phase value
- that `done` and `cancelled` differ, where `open_statuses` says only open or closed

Each is project vocabulary. Carrying them means new config keys, and `defaults/config.md` §*Adding a
key to this file is a breaking change* is unambiguous about the consequence: a config replaces the
default rather than merging, so **every project that wrote its own config fails on its next upgrade**,
naming a key nobody there has heard of. No key has been added since the schema shipped.

**Why it is Low.** The shape it would catch — a record past a section it never filled — occurs **0
times in 172 tasks** here. The value is entirely in whether the capability is wanted for other
reasons; if it is not, the honest outcome is a recorded *no* and this task closes having spent one
record.

**Scope**
- In: whether `check` gains any notion of phase at all, and if so how the vocabulary reaches it
- In: whether the `done` / `cancelled` distinction is worth a key on its own, independently of phase.
  T-172 had to treat them alike and repair two cancelled records by stating the phase was never run
- In: what a *no* is written against, so this is not re-asked. T-172's docstring and the binding both
  carry the reason today, which may already be enough
- Out: any change to `check_abandoned_slots`' current behaviour. It is verified and closed; a widening
  is this task's product, not a repair of that one
- Out: the general question of optional keys or merge-on-upgrade. That is the mechanism
  `defaults/config.md` already considered and rejected, and reopening it is a much larger task than
  this one

**Inputs**
- [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) §3 — the three unknowns,
  measured, and the 0-in-172 figure
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Adding a key to this file is a breaking change*
- `plugin/skills/taskmd/taskmd/schema.py` — `CONFIG_KEYS`, and the comment above it saying what adding
  a name to it costs
- The adopter count, in `control/LOCAL-CONTEXT.md`, which is what turns "breaking" into a number

**What `specify` measured, 2026-08-18**

The breaking-change price had been cited on both sides of this pair and never counted. It is real,
and it is larger than the *three live adopters* this record was raised with: **four sibling checkouts
of the maintainer's own projects carry their own `.taskmd/config.md`**, each a full key set — and
**this repository carries none**, running the shipped default. So all four fail on the next upgrade
if `CONFIG_KEYS` gains a name, and taskmd is the one project that would not feel it. **The repository
taking this decision is the only one structurally blind to its cost**, which is why the count is
written down instead of the adjective. Taken over the sibling checkouts on 2026-08-18; the paths stay
out of this file and the roster stays in `control/LOCAL-CONTEXT.md`, which is its home.

Recorded also because it went **against** the guess that opened it — that no adopter had written a
config, so the class the price falls on was empty. It is not empty; it is four.

**Acceptance criteria**

*Drafted by the working session on 2026-08-18, not by the owner, which is the hazard this record
named at raise: criteria written by the finder are criteria the answer passes by construction. Two
guards were applied — every criterion below is one a recorded **no** must also satisfy, and three of
the five are settled by running something rather than by reading the result back.*

- [ ] The answer states whether `check` gains any notion of phase, as **yes** or **no** — not *not
      yet*. A deferral is the one outcome this task may not produce, because a deferral is what it
      already is
- [ ] The reasoning carries both numbers as measurements with their date: how many projects would
      break, and how many instances of the target shape the corpus holds. A figure quoted with no run
      behind it fails this criterion even when it is right
- [ ] The `done` / `cancelled` distinction is answered **separately** from the phase question, and the
      answer says whether it stands on its own. A yes on one and a no on the other is a permitted
      result — T-172 had to treat the two alike and repaired two records by hand to get round it
- [ ] A **no** is written where the next person to want this looks first, and `check`'s own scope
      statement does not imply phase is covered. Which document was chosen is recorded, with why
- [ ] The decision is run against this repository's corpus **and** against at least one sibling that
      carries its own config, and both runs are quoted. For a **no** that means showing the corpus
      produces no instance and the sibling still passes — an unrun claim of zero does not meet it

**Open questions**
- ~~**Is the target class empty enough to close this unanswered?**~~ **Answered by the working session
  on 2026-08-18 under standing delegation: no — it is to be answered, not closed unanswered.** The
  class is empty here (0 in 172 at raise, 0 in 173 today), and that is an argument for the answer
  being **no**, not for there being no answer. Closing it unanswered leaves the next person to
  re-derive the four-project price from nothing, which is the one cost this record exists to pay once.

  *Rejected: close it unanswered as too small to decide.* The cheapest outcome, and it spends a record
  without producing the thing the record is for. *Rejected: treat the empty class as decisive on its
  own.* A class measured empty on one project's habits says more about the habits than about the tool
  — this record said so at raise, and it is the four-project price, not the zero, that settles it.

  **Cheap to reverse**: it fixes what §3 must write down, not what §3 may conclude.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Enumerate every route by which `check` could reach a task's phase, and test each against `CONFIG_KEYS`: does it add a name to that tuple, or not? First, because it is the one step that can invalidate the rest — a route needing no key would collapse the price this pair is being decided on. | A table in §3, one row per route, each marked *needs a key* / *no key*, with the reason read out of `schema.py` rather than assumed |
| 2 | Re-take the two figures criterion 2 asks for, each beside the command that produced it. `specify` measured the first at four; the second was 0 in 172 and the corpus is 173 today, so neither is quotable as it stands. | Two dated numbers in §3, each with its command |
| 3 | Answer the `done` / `cancelled` question on its own terms, and before the phase question, so a yes there cannot be carried by a no here. | A recorded answer in §3 saying whether it stands alone, with its rejected alternative |
| 4 | Decide the phase question. Then settle with [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) which document carries which *no*: both tasks' criteria reach for `check`'s scope statement, and two answers written into it independently is one fact written twice. | A recorded decision in §3 naming the home for each answer, with rejections |
| 5 | Write the answer into the documents step 4 named. | The edited documents |
| 6 | Run the verification criterion 5 asks for: this corpus, and one sibling carrying its own config. | Both runs quoted in §3 |

**Shape decided at `plan`: the answer is prose in documents that already exist.** *Rejected: a
document of its own.* A new file is one more thing to keep current, and both tasks' criteria ask for
the answer to sit where the next person looks first — which is, by definition, somewhere that exists
already. *Rejected: a docstring beside the check.* `check_abandoned_slots` already carries the
narrowing in its docstring and that did not stop the question being re-asked; this record **is** the
re-asking, which is the evidence against repeating the choice.

**Not planned past step 4, deliberately.** Step 1 decides whether step 5 edits one document or three,
and step 4 decides which. Cutting steps 5 to 8 in detail now would bake in whichever route turns up
first, which is the trap `plan`'s sequencing rule names.

**Outputs this task will produce** — step 4 fixes the final set:

- tasks/T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md, §3
- one or more of README.md, plugin/skills/taskmd/taskmd/defaults/config.md,
  plugin/skills/taskmd/docs/bindings/local-markdown.md

## 3. Implement

**Step 1 — every route to a phase, and what each costs.** Read out of `schema.py` and `cli.py`, not
reasoned about. `CONFIG_KEYS` is 14 names — six scalar, five nullable, three list — and `_require`
rejects an unknown key and a missing one alike, so that tuple is the whole vocabulary and adding to
it is the only way to declare something new.

| # | Route | Adds a name to `CONFIG_KEYS`? | What it costs |
| :-- | :--- | :---: | :--- |
| A | A dedicated key: `phase_field`, plus something carrying the order | **yes** | The four projects in §1, on their next upgrade |
| B | Reuse `context_fields` / `index_columns` — the shipped default already names `phase` in both | no | **Unsound.** See below |
| C | Hardcode the field name `phase` in the tool | no | One project's vocabulary inside the tool: what `BINDING.md` exists to prevent and what `CLAUDE.md`'s design rule forbids |
| D | Derive the phase from the status, through the pairing the method mandates | no | The status *names* are configurable (`open_statuses`), so the pairing is name-dependent. C at one remove |
| E | Derive the section order from the templates, as `slot_lines` already does | no | Gets the *order* free, and still cannot say which front-matter field holds the phase. Half a route |
| F | No phase; gate on `open_statuses`, which exists | no | Nothing. It is what shipped in T-172 |

**Route B looked like the answer, and measuring it is what killed it.** The shipped default carries
`context_fields: [status, phase, type, work_package, owner]` and `index_columns: [work_package,
status, phase]`, so the tool is *already* told the name `phase` with no new key. Three things rule it
out, and only the third needed a measurement:

1. They are **display** lists. `filter_names` classifies a name from them as a plain `field` only
   when nothing else enumerates it, and `schema.py`'s own `extra` docstring says the display route is
   what a project uses to *see* an uninterpreted field. Reading "show me this" as "this is the phase"
   is a second meaning for one key.
2. A project that stopped **showing** phase would stop **checking** it, with nothing saying so.
3. **One of the four adopters names no phase at all** — its `context_fields` is `[status, priority]`.
   So there the route is not merely wrong, it is silent: the check would no-op and report nothing,
   and a check cannot report its own inapplicability.

So every route that works costs a key, and every route that costs no key is unsound (B), forbidden
(C, D), or incomplete (E).

**Step 2 — the two figures, each with the command that produced it.**

*Projects that would break*, 2026-08-18: **four**. Counted by testing for `.taskmd/config.md` across
the sibling checkouts; each holds a full key set, and this repository holds none, running the shipped
default. The paths stay out of this file; the roster is in `control/LOCAL-CONTEXT.md`.

*Instances of the target shape*, 2026-08-18: **0 in 173 tasks**. Measured with the tool's own
`slot_lines`, so a slot is the shipped definition rather than a pattern invented for the measurement
— 14 slot lines derived from this project's two templates, every task carrying a recognised phase:

```
corpus                       : 173 tasks
slot lines derived from templates: 14
tasks with no recognised phase  : 0
TARGET SHAPE (open, slot in a section the phase has PASSED): 0
already caught today (slot in a CLOSED record)             : 0
```

**Both zeroes are worth nothing until the counter is shown failing**, which is this method's rule and
also the trap this pair of tasks keeps walking into. On a two-task specimen — one at `phase: review`
with an unfilled `3. Implement`, one at `phase: specify` carrying the *same* slot in the *same*
section:

```
corpus                       : 2 tasks
TARGET SHAPE (open, slot in a section the phase has PASSED): 1
    ('T-001', 3, '- <decision - rationale - date>')
```

The alarm and the silence in one run: T-001 reported, T-002 not, and the only difference between them
is the phase. The second zero above is corroborated independently — `check` prints no `ABANDONED
SLOT` on this corpus either, so that figure is the shipped check's answer and not only this script's.

The specimen stayed in a scratch directory and is **not** added to `tests/fixtures/`. Nothing is being
built, so there is no check for a fixture to protect; whether a fixture is owed for a case that must
*not* fire is [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s to rule on,
and pre-empting it here is what this project's own method forbids.

**Step 3 — `done` against `cancelled`, answered on its own terms and first.**

**No, and it stands on its own.** Telling them apart needs a name for *which closed status means
finished*; `open_statuses` splits open from closed and carries nothing further, and no other existing
key can be read for it without repeating route B's unsoundness. So it reaches route A independently
of the phase question, and is refused on the same price rather than carried by it.

*Rejected: fold it into the phase answer.* Tidier, and it would have made a yes on either impossible
to grant without the other. Criterion 3 exists to keep that door open, and it is now open and unused
rather than closed by accident.

**What a project does instead costs nothing and is already proven.** T-172 repaired T-158 and T-167
by replacing the slot with the sentence saying the phase was never run. That is a record stating its
own state, it needs no tool, and it is what this answer points a project at.

**Step 4 — the decision, and where each *no* is written.**

**`check` gains no notion of phase.** Route A is the only one that works, and it costs four projects
to catch a class with zero members here. The value was always conditional on the capability being
wanted for some other reason; nothing in steps 1 to 3 supplies one.

*Rejected: route A anyway, on the argument that a class empty today is not empty tomorrow.* True, and
the strongest case for a yes. It loses on who pays: the cost falls immediately on four projects that
asked for nothing, and the benefit is contingent and lands here first. *Rejected: defer once more.*
The one outcome criterion 1 forbids, and a deferral is what this record already was.

**One home, not two.** This task and
[T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) refuse a capability for the
*same* reason: each needs the tool to learn where a task has got to, that is project vocabulary, and
vocabulary costs a key. Writing that twice is the one thing this project's design rule forbids, so it
is written **once**, in `plugin/skills/taskmd/taskmd/defaults/config.md` §*Adding a key to this file
is a breaking change*, naming both refusals as instances of the rule already stated there.

*Rejected: the README, beside `check`'s scope statement.* That is where a reader asks *what does check
do*, not *how do I declare this* — and the second question is the one that produces a request for the
key. *Rejected: the local-markdown binding.* The constraint is the shipped config's, not one
tracker's. *Rejected: a docstring beside the check*, for the reason recorded at `plan`.

**`check`'s scope statement needed no edit, and that is a result rather than a skipped step.** It
reads, in `cli.py` and quoted in `README.md`:

```
structure and references only - it cannot tell you whether a spec or an outcome is good
```

It claims structure and references, and nothing about phase, so it does not imply the class is
covered. Editing it to deny phase specifically would turn the sentence into a list of everything
`check` is not.

**Step 5 — written.** See *Outputs produced*.

**Step 6 — the sibling runs, and the figure they corrected.**

Criterion 5 asks for this corpus **and** a sibling carrying its own config. Running `check --root`
against all four, with the edited default in place, did both jobs and falsified the shape of step 2's
number:

| Project | `check` against it | Carries a config | Validating local task files today |
| :--- | :--- | :---: | :---: |
| the deck-building sibling | `1 problem` — 176 tasks, 5 vocabulary rows | yes | **yes** |
| the diagram-modelling sibling | template problems of its own; 7 tasks read | yes | **yes** |
| one further sibling | `CONFIG ERROR: tasks_dir is 'tasks', but the project root has no such folder` | yes | no |
| one further sibling | `CONFIG ERROR` on the same line, plus `id_width is 'none'`, so a backend allocates its ids and its tasks are not local files | yes | no |

**Four carry a config; two are actually validating local task files.** The breaking claim is
unaffected — a missing key is caught by `_require` when the config is *read*, which is before any of
those later failures, so all four break on the next upgrade exactly as stated. What changes is the
sentence a reader takes away: *four projects break* and *four projects are using this* are different
claims, and step 2 quoted a number that reads as the second. Partitioned here rather than corrected
in place, because both figures are true of different sets and the useful fact is the gap between
them.

It does not move the decision. Two or four, the cost lands on projects that asked for nothing, and
the target class is still zero.

**The edited shipped default did not disturb any of them**: the two that read task files read the
same counts as before the edit, and the two config errors are pre-existing conditions of those
projects rather than anything this change introduced — the error is raised on `tasks_dir` resolution,
after the key check the edit does not touch.

**One finding that is not this task's**, surfaced rather than absorbed or fixed: the deck-building
sibling's single problem is a live `ABANDONED SLOT` in one of its own closed records — the class
T-172 shipped, catching a real instance in another project for the first time. It is that project's
record to repair, in that project, and it is outside the authorisation this pair of tasks runs under.
Reported to the maintainer in the session that found it; no task raised here, because a task here
would be this repository tracking another's backlog.

**Decisions & assumptions**
- **The plan's step 4 wording constraint was wrong, and is withdrawn** — 2026-08-18. `plan` recorded
  that the `METHOD.md` edit had to avoid em and en dashes, because `tests/test_publishing.py`
  enforces that on covered documents. Measured: `METHOD.md` carries 18 and `defaults/config.md`
  carries 48, with the gate green, because §5's pathspec covers `README.md`,
  `docs/repo-description.txt` and the plugin manifests only. The constraint was assumed at `plan` and
  never tested. Recorded rather than quietly dropped: a plan constraint that disappears without a
  reason is indistinguishable from one that was forgotten.
- **The answer is `no`, not `not yet`** — 2026-08-18, above.
- **`done` / `cancelled` refused separately, on its own grounds** — 2026-08-18, above.
- **One home for both refusals** — 2026-08-18, above.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the two refusals, as instances of the rule that
  decides them. Written with no repository task ids: this file ships inside the plugin, so a link to
  `tasks/` resolves here and nowhere an adopter can reach
- `tasks/T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md` — this section

**Evidence**

After the edit, with the index regenerated:

```
OK - 173 task(s), ... 203 document(s), 2079 link(s), ... 161 closed record(s), ...
exit=0
```

Suite: `276 passed, 8 subtests passed`. The shipped default is the file every schema is loaded from,
so the suite passing at all is the evidence that the edit did not break parsing; the four sibling
runs in step 6 are the evidence it did not break a project that wrote its own config. `check` also
reported `STALE INDEX` on the first run after the edit and named the command that fixes it, which is
the two commands backing each other up rather than one covering for the other.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is **yes** or **no**, never *not yet* | met | §3 step 4 states it as a refusal: `check` gains no notion of phase. Two rejections sit beside it, one of them the deferral this criterion forbids, so the forbidden outcome was considered and declined rather than avoided by accident |
| Both numbers carried as dated measurements, each with a run behind it | met | Four projects and 0-in-173, both 2026-08-18, each with the command that produced it. The corpus figure used the tool's own `slot_lines` rather than a pattern invented for the measurement, and the counter was shown reporting **1** on a two-task specimen before its 0 here was accepted. Step 6 then partitioned the four: all four break on a key, two are validating local task files today |
| `done` / `cancelled` answered separately, and says whether it stands alone | met | §3 step 3, answered before the phase question and on its own grounds, with the rejection of folding the two together. It stands alone, and the door it keeps open — a yes on one and a no on the other — is unused rather than foreclosed |
| A **no** where the next person looks first; `check`'s scope statement does not over-claim; the choice recorded with why | met | `plugin/skills/taskmd/taskmd/defaults/config.md` §*What this rule has already refused*, chosen over three named alternatives. The scope statement was read and deliberately left alone, recorded as a result rather than passed over |
| Run against this corpus **and** a sibling carrying its own config, both quoted; an unrun claim of zero does not count | **met, on the second attempt** | This corpus: `OK`, exit 0, zero instances. The **first** sibling run was quoted with no baseline, so *the sibling still passes* was exactly the unrun claim this criterion was written to forbid. A pristine copy of the plugin at `HEAD` was then built and both active siblings run before and after **in one command**: every field identical, counts included. Recorded rather than smoothed over, because the criterion caught its author |

Five met, none carried, no child tasks raised.

**Open questions swept before closing**, per the method's `review` step 5. §1 carries one and it is
answered in place, at `specify`, with its rejections. No question in this record is aimed at anyone
who has not answered it, and none is left implicit in prose: the two that were addressed to the owner
— whether the empty class closes this unanswered, and whether the criteria could be drafted here —
were both put and both answered, on 2026-08-18.

**One observation that belongs to nobody's criteria**, recorded because it changes how the step 6
numbers should be read: the deck-building sibling reported `6535 table row(s)` in the first run and
`6534` in the paired run minutes later, with nothing here touching its tree. Something else is
editing that project. It does not weaken the before/after comparison — both halves of that ran
back to back in a single command and agree in every field — and it is the reason the comparison was
run that way rather than against the earlier figure.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | **Answered: `check` gains no notion of phase.** Six routes were read out of `schema.py` and `cli.py`; the only one that works adds a key, and the ones that add none are unsound, forbidden, or incomplete. The route that nearly survived is the one worth remembering: the shipped default already names `phase` in `context_fields` and `index_columns`, so the name was there for free — and it is a **display** list, so a project that stopped showing the field would silently stop being checked, and one of the four adopters names no phase at all and would never be checked without the check being able to say so. Priced at four projects breaking to catch a class with **0 members in 173 tasks**, both figures measured on the day with their commands. `done` / `cancelled` was refused separately, on its own grounds. The refusal is written once, in the shipped default beside the rule that decides it, and shared with T-146 rather than written twice. Five criteria met, none carried. **Criterion 5 caught its own author**: the first sibling run was quoted with no baseline, which is the unrun claim it exists to forbid, so a pristine plugin at `HEAD` was built and both siblings run before and after in one command, identical in every field. |
| 2026-08-18 | → planned | **`specify` agreed by the owner on 2026-08-18**, which is the phase's exit criterion and the thing the draft could not supply itself: the criteria stand as written, with the pass-by-construction hazard accepted and its two guards taken as the answer to it. Planned in six steps, and **deliberately not planned past step 4** — step 1 is the one that can invalidate the rest, so it runs first and the later steps stay uncut until it reports. One shape decision is recorded with both its rejections: the answer lands in documents that already exist, and in particular not in a docstring beside the check, because that is exactly where T-172 put the narrowing and this record is the proof it did not hold. |
| 2026-08-18 | → specified | `specify` run together with [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md), under the whole-lifecycle authorisation in the row below. **The criteria were drafted by the working session, not by the owner.** This record asked for the owner at raise and the reason it gave is a real one, so the draft says so in §1 and carries two guards instead: every criterion is one a recorded *no* must also satisfy, and three of five are settled by running something. The open question is answered **no** — it is to be answered, not closed unanswered — with its rejected alternatives beside it. **The one new fact is a measurement.** The config-key price was cited by both tasks and counted by neither; it is **four** projects carrying their own config, not the three this record was raised with, and this repository is the only one of the five that carries none. It went **against** the guess that opened it, which is why it is written down rather than absorbed. Stored here and pointed at from T-146, never copied. |
| 2026-08-18 | — | **The maintainer authorised the whole lifecycle for this task and [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) worked *together*** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. It covers **those two tasks and nothing either of them raises**. Recorded here as well as in T-146, because a handoff is consumed once and renamed, and an authorisation kept only there is one the session after next cannot find (METHOD §3.1). **Together is part of the instruction, not a scheduling convenience**: both run into the same wall from opposite sides. T-146 asks whether a field can be *required at a status*; this one asks whether `check` can know a *phase*. Each would be answered by teaching the schema something about where a task has got to, and each therefore meets `defaults/config.md` §*Adding a key to this file is a breaking change*. Deciding them apart risks one paying that price and the other paying it again. The soft edge is stored on this task and derived on T-146. |
| 2026-08-18 | → proposed | Raised from [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md)'s `review`, carrying the unmet half of its first criterion so the gap is a task with an owner rather than a caveat in a closed record. Filed as a `decision` because the work is not blocked on anyone's skill — it is blocked on whether the capability is worth a breaking change to three adopters for a shape that occurs 0 times in 172 tasks. Deliberately **not** a child of T-172: it does not belong to that task, it is the question T-172 was told to stop at. `low` for the same reason the parent was, and because a recorded *no* is a legitimate and cheap outcome. |
