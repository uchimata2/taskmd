---
id: T-090
title: Decide what a cancelled task's declared outputs assert
type: decision
status: done
phase: review
parent: T-089
blocked_by: []
related: [T-002, T-032]
work_package: M2
owner: maintainer
business_value: low
effort: s
created: 2026-08-09
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/defaults/config.md, plugin/skills/taskmd/docs/bindings/local-markdown.md, tests/test_cli.py, tests/fixtures/README.md, tests/fixtures/broken-cancelled-deliverable/tasks/T-001-x.md]
adopter_visible: yes
---

# T-090 — Decide what a cancelled task's declared outputs assert

## 1. Specify

**Outcome**
`check` treats a task that was abandoned differently from one that was completed, or the project is
told plainly that abandoning a task means clearing its declared outputs. Either way the rule stops
resting on the accident that nobody's cancelled task has a missing path yet.

**Why this one**
Raised from [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md), which
settled that `deliverables` is checked once a task is **closed**, because METHOD §1 rule 5 is the one
place the method requires an outcome to exist. `cancelled` is closed and rule 5 does not apply to it:
a task that was abandoned did not close by producing its outcome. So the fixed rule reports a
cancelled task's declared paths for the same bad reason the original defect reported an open task's.

**It is not hypothetical, and it is not yet firing.** Of the four projects onboarded on 2026-08-09,
two carry a cancelled task and one of those declares two outputs. Nothing is reported today only
because both of those paths happen to exist — one deletion away from the noise T-089 removed.

**Why `low` even so.** Nobody is being cried wolf at right now, and the cheap fix has a real price:
the only clean mechanism is a config key naming the abandoned status, on the `blocked_status`
precedent, and **every key in that file is required** — a config replaces the default rather than
merging with it. That is a line every adopting project writes to settle a case none of them has hit.

**Requirements served**
R-16 — a false positive is the other half of proving a validator. R-11, since the likely answer is a
schema key rather than code.

**Scope**
- In: whether `check` should skip a task closed by abandonment, and how it would know which status
  that is.
- In: the alternative that needs no mechanism — documenting that cancelling a task means clearing
  `deliverables`, on the grounds that the field asserts production and an abandoned task produces
  nothing.
- In: what a project with no such status pays. `blocked_status` takes `none`; whatever is added here
  must too.
- Out: [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md)'s rule
  itself, which is settled and is not reopened by this.
- Out: any other use for knowing which status means abandoned. If a second use appears, that changes
  the economics and should be said here rather than assumed.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `check_deliverables`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` — `blocked_status` as the precedent for naming one
  distinguished value, and the *Deliverables* section's note that every key is required.
- [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) §1, for the rule
  and the rejected alternative.

**Acceptance criteria**
- [ ] A cancelled task declaring a path that does not exist behaves the way this task decides, shown
      on a fixture rather than argued from the config
- [ ] A project that has no abandoned status is unaffected, and pays nothing it did not already pay
- [ ] Whatever is decided, one document says it and the others point — the binding already carries
      the sentence about which of rule 5's conditions is mechanical

**Open questions**
- ~~**Mechanism or documentation.**~~ **Answered 2026-08-11: documentation** — see D1 in §2, with the
  config key priced and rejected there.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the case as a committed fixture — a `cancelled` task declaring a path that is not there — and run `check` on it, so the decision is taken against the behaviour rather than against the code. | `tests/fixtures/broken-cancelled-deliverable/`, and the output recorded in §3 |
| 2 | Say, in the one document that defines what `deliverables` means, that abandoning a task means clearing it. | The `## Deliverables` section of `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 3 | Remove the reading that would contradict it: the binding's rule-5 paragraph says `check` stays quiet until rule 5 applies, and rule 5 is exactly what does not apply to an abandoned task. | `plugin/skills/taskmd/docs/bindings/local-markdown.md` |
| 4 | Pin the behaviour with a test, so a later session cannot read the report as the defect T-089 removed and "fix" it back. | `tests/test_cli.py` |
| 5 | Give the fixture its row, and show a project with no cancelled task pays nothing. | `tests/fixtures/README.md`, recorded output |
| 6 | `check`, `index`, the suite. | Recorded output |

**Shape decisions.**

**D1 — Documented, not a config key. There is nothing to skip, because the report is true.**
`deliverables` asserts production ([T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md)).
A task closed by abandonment produced nothing, so a `deliverables` list it still carries is a claim
its own record contradicts — and `MISSING OUTPUT` on it is not a false positive but a stale record
being caught. That reframes the whole question: T-089's defect was `check` asking for an outcome
before the method required one; this is `check` reporting a claim the task itself no longer makes.
Clearing the field is part of abandoning the task, the same way the log row is.

*Rejected: a config key naming the abandoned status.* It is exact, it follows the `blocked_status`
precedent, and it is the answer the specify expected. What it costs is stated in the shipped config
itself: **adding a key is a breaking change** — a config replaces the default rather than merging, so
every existing config must gain the line or fail with a missing-key error. Three adopting projects
would pay that, none of them hits the case, and what they would buy is silence about a record that is
wrong. A key whose effect is to stop reporting a true statement is the wrong purchase at any price.

**D2 — What this answer costs, said plainly.** `check` cannot tell *you abandoned this and left the
claim behind* from *you closed this and lost the file*; both print `MISSING OUTPUT`. That is a real
loss of precision and it is bounded, because the remedy is the same in both directions — make the
record true. It is also unenforced in the other direction: a cancelled task whose declared paths
happen to exist keeps a false claim silently, exactly as the two onboarded projects do today.

**D3 — The sentence lives in the shipped config, not in the binding or the method.** The config is
where `deliverables_field` is defined and where `check`'s behaviour on it is described, and it is the
document that travels into an adopting project — so the reader who meets the report has it. The
binding says `check` stays quiet "until rule 5 actually applies", which a reader can take to promise
silence here, so it gains one clause and a pointer rather than a second copy. METHOD is not the home:
it names no field, and this is a statement about one.

**Planned outputs**
- tests/fixtures/broken-cancelled-deliverable/
- plugin/skills/taskmd/taskmd/defaults/config.md
- plugin/skills/taskmd/docs/bindings/local-markdown.md
- tests/test_cli.py
- tests/fixtures/README.md

## 3. Implement

### Step 1 — the case, and what it prints

`tests/fixtures/broken-cancelled-deliverable/` is a `cancelled` task, abandoned in `plan`, still
carrying `deliverables: [out/report.md]`:

```text
MISSING OUTPUT T-001 declares 'out/report.md', which does not exist

1 problem(s) - 1 task(s), … 1 declared output(s), …
exit 1
```

**The decision was taken against this rather than against the config**, which is what the specify
asked for — and reading it changed the answer. The line is not `check` demanding an outcome the
method has not required yet, which is T-089's defect; it is `check` reporting that a task claims to
have produced something it says elsewhere it abandoned. There is nothing to suppress.

The same task with the field cleared:

```text
OK - 1 task(s), 5 field value(s), … 0 declared output(s), …
exit 0
```

That is the remedy the shipped config now names, shown to work rather than asserted — and it is
one edit to the record, not a key in every adopter's config.

### Steps 2–3 — one home, and the reading that contradicted it

The `## Deliverables` section of the shipped config gains the paragraph: abandoning a task means
clearing the field, the report on such a task is a stale record, and there is deliberately no key
naming an abandoned status.

The binding needed one clause, because it promised the opposite by implication: *`check` stays quiet
until rule 5 actually applies to it* is exactly the sentence a reader would use to conclude that an
abandoned task is exempt, rule 5 being what does not apply to it. It now says closed includes
abandoned and points at the config, rather than restating it.

### Step 4 — pinned as behaviour

Two tests beside T-089's pair. The first asserts the report on the cancelled fixture; the second
copies that fixture with `deliverables: []` and asserts it passes. The second is the one that makes
the config's paragraph an instruction someone can follow — and the first exists because the next
reader to meet this line will recognise T-089's shape and reach for its fix.

### Step 5 — what a project without a cancelled task pays

```text
tests/fixtures/planned-deliverable   OK - … 0 declared output(s) …
tests/fixtures/alt-project           OK - 3 task(s), … 0 declared output(s) …
```

Nothing: no key was added, so no config gained a required line and no existing config can now be
missing one. `alt-project` is the second schema and is equally untouched.

### Step 6 — the runs

Suite: `test_cli` **100** OK (98 before, plus these two), `test_list` 37 OK, `test_schema` 53 OK,
`test_budget` 5 OK, `test_runtime` 27 `OK (skipped=3)`.

**Decisions & assumptions**
- **D1 — documented, not a config key; the report is true and there is nothing to skip** —
  2026-08-11, §2, with the key priced and rejected there.
- **D2 — the cost, stated: `check` cannot tell a stale claim from a lost file** — 2026-08-11, §2.
- **D3 — the sentence lives in the shipped config; the binding points** — 2026-08-11, §2.
- **Assumption: no adopter is disturbed.** Nothing about `check` changed, so no tree that passed
  yesterday can fail today; the two onboarded projects carrying a cancelled task keep passing, and
  what they gain is a documented answer the day one of their paths is deleted.

**Outputs produced**
- [`tests/fixtures/broken-cancelled-deliverable/`](../tests/fixtures/broken-cancelled-deliverable)
- [`plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)
- [`plugin/skills/taskmd/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md)
- [`tests/test_cli.py`](../tests/test_cli.py)
- [`tests/fixtures/README.md`](../tests/fixtures/README.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A cancelled task declaring a path that does not exist behaves the way this task decides, shown on a fixture rather than argued from the config | met | §3 step 1: the fixture reports `MISSING OUTPUT`, exit 1, which is what D1 decides it should do — and the fixture is committed with two tests, so the decision is met as behaviour rather than as a paragraph |
| A project that has no abandoned status is unaffected, and pays nothing it did not already pay | met | §3 step 5. Stronger than the criterion asks: **no** project pays anything, because no key was added — the alternative that would have cost every adopter a required line is the one rejected |
| Whatever is decided, one document says it and the others point — the binding already carries the sentence about which of rule 5's conditions is mechanical | met | The shipped config's *Deliverables* section is the home (D3); the binding gains a clause and a link rather than a copy, because its existing wording implied the opposite. `tests/fixtures/README.md` explains the fixture and points at this task for the reasoning |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met, no child raised. **Authorisation (METHOD §3.1):** the maintainer's standing grant to work every open `M2` task through its full lifecycle, given 2026-08-10 and widened on 2026-08-11 to *the remaining tasks, full lifecycle, continuously*. The open question was marked the maintainer's; it is answered here under the standing delegation, with the rejected option priced in §2 and cheap to reverse — the whole of it is one paragraph, one clause and a fixture. **Reading the run changed the answer.** The task was framed as choosing between a config key and a convention for suppressing a false positive; running the fixture showed there is no false positive to suppress. `deliverables` asserts production, a task closed by abandonment produced nothing, and the line reports a claim the task's own record contradicts — so the key would have bought silence about something true, at the price of a **breaking change** to every adopter's config, for a case none of the three hits. Two things worth carrying: the report has T-089's exact shape and is not T-089's defect, which is why this needed two tests and a fixture rather than a paragraph — the next reader will recognise the shape and reach for that fix; and the binding said `check` *stays quiet until rule 5 actually applies*, which promised the opposite by implication, so a decision recorded only in the config would have left a document contradicting it. |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-09 | → proposed | Raised from T-089 rather than solved inside it. T-089 keyed the deliverables check on the task being closed, which is METHOD §1 rule 5 stated mechanically; `cancelled` is closed and rule 5 does not cover it, so the same false positive survives under a different status. Carried rather than fixed because the clean mechanism is a required config key every adopter pays for, and the case fires in none of the four projects onboarded today — two of which do have a cancelled task, one declaring two outputs that happen to exist. `low` for that reason, and `s` because the whole of it is one branch and one key. |
