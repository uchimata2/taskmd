---
id: T-146
title: Decide whether a field can be required at a status
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-065, T-089, T-100, T-106]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-15
updated: 2026-08-18
deliverables: []
---

# T-146 — Decide whether a field can be required at a status

## 1. Specify

**Outcome**
It is settled whether taskmd can express *this field matters once a task reaches this point*, or
whether it cannot and says so — so a project whose convention is exactly that stops finding out by
hand which tasks broke it.

**Why this one**
Raised from the htmldeck adopter report, row `O-T6`. Three instances there, and they are not the same
shape, which is the reason the row was written as one observation rather than two:

1. A field the project requires at close. Their convention sets `shipped_in` when a task closes.
   `check` validates the *value* of a declared field and nothing ties a field's presence to a status.
   113 of 138 files carried it; three closed tasks did not, found by hand.
2. A field required from a phase onward — the same shape one step earlier.
3. **Two fields that must agree.** `status` and `phase` move together, and two sessions in that
   project chose differently on the same day: one wrote `status: specified, phase: specify`, the other
   `status: specified, phase: plan`. `check` passes both. Neither is obviously wrong, because *the
   phase just completed* and *the phase to do next* are both readable from a table that pairs them.

**The report's cross-reference is wrong, and it matters.** It names *your `T-063`* as the adjacent
case already filed — an open task at `specified` or later declaring no deliverable.
[T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) is the tier-1 budget measurement and has
nothing to do with this. Nothing in this backlog covers a field bound to a status; the nearest are
[T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), which moved in the
opposite direction, and [T-039](T-039-let-a-plan-name-a-deliverable-that-does-not-exist-yet.md). So
the general form is unraised here.

**The reporter confirmed it and audited the rest**, on 2026-08-15. Seven foreign-id citations across
their two registers — our `T-028`, `T-063`, `T-085` and `T-087`, and `#53`, `#57` and `#8` on the
other — and **one is wrong: the `T-063` above**. The other six check out against the files they name,
on title and on claim. One in seven, in the direction their own preamble did not guard: a wrong id of
ours resolves to a real task, so it reads as *already covered* and a reader who trusts it stops
looking. The `O-T6` row now cites nothing and records the class as uncovered here until this task.

**Instance 3 is closed on the reporting side, and this repository is now the only live one.** They
re-measured on the same day: 159 task files, none disagreeing, all running `specified`/`specify` →
`planned`/`plan` → `in_progress`/`implement` → `done`/`review`. The split the row recorded is gone.
What it still proves is the part that matters here — two sessions can choose differently on the same
day and nothing reports it — and not that any project is inconsistent today.

> **Annotated 2026-08-18 at `implement`, not rewritten: the paragraph above was true when written and
> is false now.** Re-measured on 2026-08-18, that project holds **176** task files and **one**
> disagreement, `T-114` at status *planned* with phase *implement*. So the split is live there again,
> three days after being repaired, and this repository is no longer the only place it occurs. The
> paragraph stays as written because what it records is the state on 2026-08-15; the drift between
> the two dates is the finding, and correcting the sentence would delete it. The measurement, and
> what it does and does not change, is §3 step 6.

**The third instance is live in this repository, and unenforced.** `METHOD.md` §2 says *phase says
where the work has got to* and pairs nothing to a status. The shipped template starts a task at
`status: proposed, phase: specify`, which reads as the phase the work is *at*. Every one of this
repository's 143 files happens to follow that reading — 131 `done`/`review`, 5 `proposed`/`specify`, 2
`specified`/`specify`, 1 `in_progress`/`implement` — and nothing in the tool would have noticed if one
had not. The consistency is a habit, not a property.

**Why the answer may well be no, and why that is still the outcome.**
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) established that the shipped config
cannot gain a key without breaking every project that has written its own, and a rule of this kind is
project vocabulary by construction: `shipped_in` is a field taskmd does not name and never interprets
([T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md)). So the general form needs
somewhere to be declared, and the one obvious place is closed. A decision that this is out of scope,
written down with that reasoning, is a real result and is what two projects hitting it are owed.

**Requirements served**
R-11 (which fields exist is configuration) and R-15, in the sense the non-goal 11 carve-out was
amended on. R-16, for whether a rule of this kind can be believed.

**Scope**
- In: whether taskmd can express a constraint that binds a field to a status or a phase, and where such
  a rule would be declared given T-106.
- In: whether *presence at a status* and *two fields agreeing* are one mechanism or two. The report
  argues the second is what makes the general form worth having, since a required-field rule cannot
  express it.
- In: whether `METHOD.md` §2 should say which phase pairs with which status, independent of any
  checking. It is a method question, and the two readings the report found are both defensible under
  the current wording.
- Out: building any check before the shape is decided.
- Out: `deliverables` in particular, and any other single field. This is the class.
- Out: reversing T-106.

**Inputs**
- The adopter report, row `O-T6`, for the three instances and their counts.
- [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) — the constraint that governs the
  answer.
- [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) — carried, never interpreted.
- `plugin/skills/taskmd/docs/METHOD.md` §2, and `tasks/_task-template.md`, for what this project's own
  pairing currently is and where it is stated.
- [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) §1 — what
  T-106's constraint actually costs, counted on 2026-08-18 rather than cited. Stored there and read
  from here: both tasks meet the same price, and writing it twice is the one thing this project's
  design rule forbids.

**Acceptance criteria**
- [ ] The decision covers both shapes — a field required at a status, and two fields that must agree —
      and says whether one mechanism serves both or the second is out
- [ ] Wherever it lands, the reasoning names T-106 and says what the rule would be declared in
- [ ] If the answer is no, one document says so and says what a project relying on such a convention
      does instead, and `check`'s scope statement does not imply it is covered
- [ ] The pairing is stated in `METHOD.md` §2. The owner ruled on 2026-08-15 that it is the method's
      to state, so *deliberately left unstated* is no longer one of the two outcomes this criterion
      may report. It is met when the sentence exists **and** reads consistently beside §2's standing
      *phase and status are independent* — which governs **movement**, where the new sentence governs
      **correspondence**. A §2 asserting both without distinguishing them fails this
- [ ] Whatever is decided is measured against this repository's own task corpus in both directions,
      with the count stated as of the run — a rule that reports nothing here is as informative as one
      that reports something. The count is deliberately **not** written into this criterion: it read
      `143` at raise and is `173` today, and a criterion carrying a figure goes stale between the
      raise that wrote it and the review that reads it

**Open questions**
- ~~**Is the status–phase pairing a method question or a schema question?**~~ **Answered by the
  project owner on 2026-08-15: a method question — `METHOD.md` states which phase pairs with which
  status.** Two projects have now read §2 differently, and the pairing is a property of the lifecycle
  the method already mandates rather than of any project's vocabulary. Stating it makes the pair
  checkable for everyone following the method, at the cost of one sentence.

  *Rejected: leave the pairing to each project.* It is what §2 does today — *phase and status are
  independent* and nothing more — and it keeps the method free of an opinion it cannot enforce, which
  is a shape this project has rejected before. What decided it against: the two readings are both
  defensible under the current wording, so silence is not neutrality, it is a coin toss written into
  every adopting backlog. A method whose lifecycle is mandatory (§1.2) already owns this.

  **This does not answer the task.** Whether anything *checks* the pair, and whether the general form
  — a field required at a status — can be expressed at all under T-106, are still `specify`'s.

- ~~**Does stating the pairing make the general form unnecessary?**~~ **Answered by the working
  session on 2026-08-18 under standing delegation: no — it removes the strongest *instance* and leaves
  the general form exactly where it stood.** Stating the pairing in `METHOD.md` makes the pair
  **stated**; it does not make it **checked**. Anything that checks it must still know which
  front-matter field carries the phase, and that is the wall
  [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) priced at
  four projects on 2026-08-18. So this task does not narrow to the method sentence alone — it narrows
  to that sentence **plus** a recorded answer on the general mechanism, and the two ship together or
  the sentence implies an enforcement that does not exist.

  *Rejected: narrow to the `METHOD.md` sentence alone.* The cheaper reading the raise anticipated, and
  it fails against the third criterion above — a method stating a pairing while `check`'s scope says
  nothing is the same silence that let two sessions choose differently on the same day. *Rejected:
  drop the sentence and decide only the mechanism.* The owner ruled on 2026-08-15 that the pairing is
  the method's to state, and that ruling is not this session's to reverse.

  **Cheap to reverse**: it sets what §3 writes, and both halves are one sentence and one paragraph.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Settle whether *a field required at a status* and *two fields that must agree* are one mechanism or two. Criterion 1 needs this either way, it depends on no other step, and getting it wrong reframes every step after it. | A recorded answer in §3, with its rejected alternative |
| 2 | Take [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) step 1's route table as an input rather than re-deriving it: which vehicle, if any, adds no config key. The soft edge stored on T-173 already carries the link, so this needs no new edge. | One statement in §3 of what T-173 concluded and what it leaves available here |
| 3 | Decide the mechanism question against that route table, naming T-106 and saying where such a rule would be declared if it existed. | A recorded decision in §3, with rejections |
| 4 | Write the pairing into `METHOD.md` §2 and reconcile it with the standing *phase and status are independent*: that sentence governs **movement**, the new one governs **correspondence**, and §2 must distinguish them rather than assert both. Owner's ruling, 2026-08-18. | The edited §2, written with no em or en dash, which `tests/test_publishing.py` enforces on every covered document |
| 5 | Write the mechanism answer into the document T-173 step 4 named, and confirm `check`'s scope statement does not imply the class is covered. | The edited document |
| 6 | Measure the decision against this repository's corpus in both directions, stating the count as of the run rather than the `143` the raise carried. | Both directions quoted in §3 |

**Shape decided at `plan`: the `METHOD.md` change is one sentence plus the distinction, not a new
subsection.** §2 already carries the independence sentence, and a reader who meets one without the
other is the exact failure this task was raised on. *Rejected: a §2.1 of its own for the pairing.* It
separates the two sentences whose whole value is being read together. *Rejected: putting the pairing
in the binding.* The owner ruled on 2026-08-15 that it is the method's to state, and a binding is
per-tracker where the lifecycle is not.

**Step 4 is independent of steps 1 to 3 and could run first.** It is placed fourth because it is the
half that is already decided, and doing the decided half first is how a task quietly becomes the
easy part of itself.

**Outputs this task will produce** — step 5's document is fixed by T-173 step 4:

- tasks/T-146-decide-whether-a-field-can-be-required-at-a-status.md, §3
- plugin/skills/taskmd/docs/METHOD.md, §2

## 3. Implement

**Step 1 — two mechanisms, not one, and the second is out.**

They are different rules and no single mechanism serves both:

- *a field required at a status* is a **presence** rule — field F must be non-empty once the task is
  in state S. It reads one field and one status;
- *two fields that must agree* is a **relation** rule — the value of A constrains the value of B. It
  reads two fields and no status at all.

A required-field rule cannot express the second, which is the report's own argument and it holds.
**The second is out**, and not because it is hard: its one live instance is the status-phase pair,
and that is answered by stating the pairing in the method (step 4) rather than by any declarable
rule. A mechanism whose motivating instance has been answered another way is a mechanism with no
case.

*Rejected: treat them as one presence-shaped mechanism with the relation as a special case.* It is
what a first design would do, and it silently narrows the second shape to the fields a status happens
to touch, which is not what either project asked for.

**Step 2 — what T-173's route table leaves available here.**

Nothing. [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) §3
step 1 enumerated six routes by which the tool could learn a fact about where a task has got to; the
only one that works adds a key, and the ones that add no key are unsound, forbidden, or incomplete.
A presence rule bound to a status needs exactly that kind of fact — *which* field, *which* statuses —
so it arrives at the same wall by the same road. Read from there rather than re-derived, which is why
the soft edge to that task exists.

**Step 3 — the mechanism question, decided.**

**No. taskmd cannot express *this field matters once a task reaches this point*, and will not be
taught to.** The reasoning is [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s and
is unchanged by anything found here: such a rule is project vocabulary by construction — `shipped_in`
is a field taskmd does not name and never interprets
([T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md)) — so it must be *declared*
somewhere, and the only place a project declares vocabulary to this tool is the config, which cannot
gain a key. Priced today rather than in the abstract: four projects carry their own config, and each
would fail on its next upgrade naming a key nobody there had heard of.

*Rejected: declare the rule in the task template instead of the config.* Templates are already read
by the tool, so it looks free. It fails on meaning — a template is an example of a record, and a rule
about *when* a field is required is not a property of any one record. *Rejected: declare it in the
binding.* A binding is per-tracker, and a project's convention about its own field is not. *Rejected:
reverse T-106.* Explicitly out of scope at `specify`, and nothing found here is evidence against it.

**Where it is written**: one home, shared with T-173, in
`plugin/skills/taskmd/taskmd/defaults/config.md` under *What this rule has already refused*. Both
refusals are instances of one rule and are written once, with what a project does instead. The
choice and its rejections are recorded in T-173 §3 step 4 rather than repeated here.

**`check`'s scope statement was read and needs no edit.** It claims *structure and references only*
and nothing about fields bound to statuses, so it does not imply the class is covered. Verified in
T-173 §3 step 4 against the same sentence.

**Step 4 — the pairing, written into `METHOD.md` §2.**

The owner ruled on 2026-08-15 that the pairing is the method's to state, and on 2026-08-18 that §2
must **distinguish** movement from correspondence rather than assert both beside each other. Written
as two paragraphs: the existing independence sentence, now labelled as being about movement, and a
second saying that phase names the phase the work is **at**, never the one it will do next.

**It names no status value, and that is a constraint rather than a stylistic choice.** `METHOD.md`
names no field and no vocabulary — those belong to a binding — so the pairing could not be written as
a table of status against phase even though that is the form the question arrived in. The
vocabulary-free form turns out to be the whole rule: *at, not next* is exactly the ambiguity the two
readings split on, and it resolves them without knowing what any project calls its statuses.

**Step 5 — done in step 3.** The mechanism answer shares T-173's home.

**Step 6 — measured in both directions, on three corpora.**

The pairing was run as if it were a checker, which is the only way to learn what stating it would
cost a project that already has a backlog. *Direction 1* is what it would report; *direction 2* is
whether any status escapes it entirely, which is how a rule reports nothing by covering nothing.

| Corpus | Tasks | Direction 1: would report | Direction 2: statuses it cannot judge |
| :--- | :---: | :---: | :---: |
| this repository | 173 | **0** | 0 |
| the deck-building sibling | 176 | **1** | 0 |
| the diagram-modelling sibling | 7 | **0** | 0 |

```
this repository        done/review 159, proposed/specify 8, specified/specify 2,
                       cancelled/specify 2, planned/plan 1, in_progress/implement 1
the deck-building sibling   done/review 161, proposed/specify 11, cancelled/specify 2,
                       cancelled/review 1, planned/implement 1  <- the one
```

**The one is `T-114`, at status *planned* with phase *implement*, in the deck-building sibling.** It
is not a defect and is recorded here as an instance rather than an error: under *at, not next* the
work has reached implementing while the status still says planned, and under the rival reading it is
correct. That is precisely the ambiguity, alive in a real backlog, with nothing reporting it.

**This falsifies a claim in §1, which is why it was worth running rather than reasoning about.** §1
records that instance 3 was repaired on the reporting side on 2026-08-15 — 159 files re-measured,
none disagreeing — and concludes the split "is no longer live anywhere but here". Measured on
2026-08-18 that project holds 176 files and one disagreement. The claim was true when written and is
false now; §1 is annotated rather than rewritten, per the method's rule 5.

**It changes the evidence, not the decision.** A pairing that drifts back within three days is the
strongest case yet for *stating* it, and no case at all for the general mechanism, which still has
nowhere to be declared. Direction 1 reporting 0 here and 1 there is also the answer to criterion 5's
demand that a rule be informative in both directions: on this corpus it is silent and the silence is
real, and the only reason to trust that silence is that the same rule spoke on another corpus.

**Decisions & assumptions**
- **Two mechanisms; the second is out** — 2026-08-18, step 1, with its rejection.
- **The mechanism answer is no** — 2026-08-18, step 3, with three rejections.
- **The `METHOD.md` sentence names no status value** — 2026-08-18, step 4. Forced by what
  `METHOD.md` is, and it improved the rule rather than constraining it.
- **§1's instance-3 claim is annotated, not corrected** — 2026-08-18, step 6. It describes what was
  true on 2026-08-15; rewriting it would destroy the observation that the pairing drifts.
- **A shell-escaping defect reached the deliverable, and nothing mechanical could see it** —
  2026-08-18. The `METHOD.md` edit was applied through a shell one-liner and two apostrophes arrived
  as `'''`. `check`, `index` and the 276-test suite were all green over the damaged sentence, because
  none of them reads prose for sense. It was found at `review` by printing the section, which means
  `implement` had not really exited: its criterion is *checked by being used*, and nobody had read
  the sentence. Repaired here rather than carried as a review finding, and **all four edited files
  were swept** for the same pattern rather than only the one spotted.
- **The plan's dash constraint on this step was withdrawn** — 2026-08-18, recorded once in T-173 §3
  where it was measured, not repeated here.

**Outputs produced**
- `plugin/skills/taskmd/docs/METHOD.md` — §2, the movement / correspondence distinction and the
  pairing
- `tasks/T-146-decide-whether-a-field-can-be-required-at-a-status.md` — this section, and the §1
  annotation
- The mechanism refusal itself is in T-173's output, `plugin/skills/taskmd/taskmd/defaults/config.md`,
  because the two tasks refuse one thing for one reason and it is written once

**Evidence**

`check` and the suite after both tasks' edits:

```
OK - 173 task(s), ... 203 document(s), ... 161 closed record(s), ...
exit=0
```

The pairing sentence is a rule for a person, so the use that exercises it is a reader applying it to
a record and getting one answer. That reading was performed against three corpora above, and it
produced a different answer on one of them from the one §1 predicted, which is what use is for.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Covers both shapes, and says whether one mechanism serves both or the second is out | met | §3 step 1: two mechanisms, presence against relation, and a required-field rule provably cannot express the second. The second is **out**, and for a stated reason rather than difficulty — its one live instance is answered by the method sentence instead. Rejection recorded |
| The reasoning names T-106 and says what the rule would be declared in | met | §3 step 3 names [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) and [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md), and answers *declared where* explicitly: the config is the only place a project declares vocabulary to this tool, and it cannot gain a key. Template, binding, and reversing T-106 are each rejected by name |
| If no: one document says so and says what a project does instead; `check`'s scope statement does not imply coverage | met | `plugin/skills/taskmd/taskmd/defaults/config.md` §*What this rule has already refused* carries the refusal and a *What a project does instead* paragraph. The scope statement was read and needs no edit, which is recorded in T-173 §3 step 4 rather than restated here |
| The pairing is stated in `METHOD.md` §2 and reads consistently beside the standing independence sentence; a §2 asserting both without distinguishing them fails | **met, after a repair** | §2 now runs as two paragraphs: independence relabelled as being about **movement**, then correspondence — *phase names the phase the work is at, never the one it will do next*. It names no status value, because `METHOD.md` names no vocabulary, and that constraint turned out to be the rule's best form. The sentence was **damaged in transit** on first write and repaired before this review; see §3 |
| Measured against this repository's corpus in both directions, with the count stated as of the run | met | §3 step 6, run on three corpora as if the pairing were a checker: **0** would-report here in 173, **1** in the deck-building sibling's 176, **0** in the diagram sibling's 7; direction 2 empty on all three, so no status escapes the rule. The silence here is trustworthy only because the same rule spoke elsewhere, which is what the criterion was asking for |

Five met, none carried, no child tasks raised.

**Open questions swept before closing**, per the method's `review` step 5. §1 carries two and both are
struck through and answered in place — the status-phase pairing by the owner on 2026-08-15, and
whether stating it makes the general form unnecessary at `specify` on 2026-08-18, each with its
rejections. Nothing in this record is waiting on anyone.

**One residue that is not a criterion and would have died at close.** This task exists because of an
adopter's `O-T6` row, and the answer it reaches is **no** — that project's convention stays
hand-swept. Their row is owed the answer and the reason, and nothing in this record or the tracker
will deliver it: a closed task leaves every view a project has. It is named here, and it was raised
with the maintainer in the session that closed this task, because deciding to tell them is not this
task's to take.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | **Answered: no — taskmd cannot express *this field matters once a task reaches this point*, and the pairing is now stated in the method instead.** Two mechanisms, not one: a presence rule cannot express *two fields must agree*, and the second is out because its one live instance is answered by `METHOD.md` §2 rather than by anything declarable. §2 now separates **movement** from **correspondence** and says phase names the phase the work is *at*, never the one it will do next — written with no status value in it, because the method names no vocabulary, and that constraint turned out to be the rule's best form. **Running the pairing as if it were a checker falsified §1**: the adopter's split, recorded on 2026-08-15 as repaired, is live again at 1 in 176 three days later. §1 is annotated, not rewritten. It changes the evidence and not the decision — a pairing that drifts back within three days is the strongest case for stating it and no case for a mechanism that still has nowhere to be declared. One residue is named in §4 and is not this task's to act on: the adopter whose row raised this is owed the answer, and a closed task reaches no view. |
| 2026-08-18 | → planned | **`specify` agreed by the owner on 2026-08-18**, together with the ruling that closes criterion 4: `METHOD.md` §2 must **distinguish** movement from correspondence, not merely gain a pairing sentence beside a contradiction. That is now step 4 of the plan and its wording constraint travels with it — §2 is a covered document, so the sentence is written without an em or en dash rather than rewritten after the gate catches it. Six steps. Step 1 runs first because it reframes the rest and depends on nothing; step 4 runs fourth **although it could run first**, because it is the half already decided and taking the decided half first is how a task becomes the easy part of itself. |
| 2026-08-18 | → specified | `specify` run together with [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md), under the whole-lifecycle authorisation in the row below. The open question this phase was told to decide is answered **no**, with its rejections: stating the pairing makes it *stated*, not *checked*, so the task narrows to the method sentence **plus** a recorded answer on the mechanism, not to the sentence alone. **Two criteria were amended rather than added.** The fourth offered two outcomes when the owner's 2026-08-15 ruling had already removed one of them, and it now also has to survive §2's standing *phase and status are independent* — that sentence governs movement where the new one governs correspondence, and §2 does not yet distinguish them, so a sentence added carelessly would make the method contradict itself. The fifth carried **143** files as a literal and the corpus is **173**, so a criterion written at raise had already gone stale before review could read it; the figure is out and the run states it instead. The price both tasks meet is measured once, in T-173 §1. |
| 2026-08-18 | — | **The maintainer authorised the whole lifecycle for this task and [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) worked *together*** — `specify` → `plan` → `implement` → `review` — on 2026-08-18, as the subject of a handoff written the same day. It covers **those two tasks and nothing either of them raises**. Recorded here as well as in T-173 for the reason METHOD §3.1 gives: a handoff is consumed once, so an authorisation kept only there is invisible to the session after next. **A new constraint arrived with it, from T-172's `implement` the same day**, and `specify` should meet it rather than discover it: a config key is not a cheap way to carry a status-or-phase fact. A config **replaces** the default rather than merging, so adding a key fails every project that wrote its own, and no key has been added since the schema shipped. That does not decide this task; it prices the option this task was most likely to reach for. |
| 2026-08-15 | (no change) | **The wrong cross-reference is confirmed, and the reporter audited the rest**: seven foreign-id citations across their two registers, one wrong, and it is the one we found. Recorded in §1 with the direction it failed in, because that is the reusable part — a wrong id of ours resolves to a real task and reads as coverage. Their instance 3 also went away in the same follow-up: 159 files re-measured, none disagreeing, so the split that argued hardest for a general mechanism is no longer live anywhere but here. Neither fact changes what this task decides; both change what evidence it is standing on, so `specify` should not go looking for a split that has been repaired. |
| 2026-08-15 | (no change) | **The status–phase pairing is the method's to state**, decided by the project owner on 2026-08-15. Recorded here rather than carried in a reply, because it changes what this task's fourth acceptance criterion can say. It authorises no phase. It also raised a second question the answer creates and the first one could not: if the method fixes the pairing, the instance that argued hardest for a general mechanism no longer needs one, so this task may narrow to a sentence in `METHOD.md`. That is in §1 and is `specify`'s. |
| 2026-08-15 | → proposed | Raised from the htmldeck adopter report, row `O-T6`. The row's cross-reference to *your T-063* is wrong and is corrected in §1: T-063 is the tier-1 budget measurement, and nothing in this backlog covers a field bound to a status. Two projects have now hit the class, which is the argument for deciding it rather than leaving it to each backlog. `medium` because both projects have a hand sweep that works and neither is blocked. `m` because the answer is probably constrained to nothing by T-106 and saying so properly is most of the work. The third instance is live here too: `METHOD.md` §2 pairs no phase to any status, and this repository's 143 files are consistent by habit rather than by anything the tool would report. |
