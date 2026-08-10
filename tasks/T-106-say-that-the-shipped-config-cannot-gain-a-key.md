---
id: T-106
title: Say that the shipped config cannot gain a key without breaking every project that wrote one
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-001, T-011, T-023, T-100]
work_package: v0.3
owner: maintainer
business_value: high
effort: xs
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/defaults/config.md, plugin/skills/taskmd/taskmd/schema.py, tests/test_schema.py]
---

# T-106 — Say that the shipped config cannot gain a key without breaking every project that wrote one

## 1. Specify

**Outcome**
The constraint that governs every future schema change is written down in one place, so the next
person proposing a config key meets it before designing around it rather than after.

**Why this one**
Found while planning [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md),
whose §1 asked whether a project could switch the new advisory off with a config key. It cannot, and
the reason is not local to that task:

- A config **replaces** the shipped default rather than merging with it.
- Therefore every key is **required to be written**, and `schema._require` raises on a missing one —
  deliberately, because a silently absent key would hand a project a schema nobody wrote.
- Therefore **adding a key to the shipped default invalidates every existing project's config the
  moment they upgrade**, with an error naming a key they have never heard of.

Each of those three is written down. **Their conjunction is not**, and it is the one that constrains
design. T-100 met it as a surprise mid-plan; the next task to propose a key will meet it the same
way unless it is stated.

**It is not a defect to fix.** Every step in the chain is a decision this project made on purpose and
would make again. What is missing is the sentence saying what they cost together.

**Requirements served**
R-11 (`docs/SCOPE.md`) — the schema is configuration, and this is the price of the rule that makes it
so. R-17, in that the failure mode is a config error appearing at the worst possible moment: on
upgrade, in a project that changed nothing.

**Scope**
- In: one paragraph, in the shipped config beside the replace-not-merge rule it follows from.
- In: whether anything can be done for a project caught by it — a named upgrade path, or the plain
  statement that a new key means every config is edited.
- Out: changing `_require`. Making a key optional is exactly what it exists to forbid, and
  [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) D2 rejected the
  carve-out already.
- Out: adding any key. This says what it would cost, not that one is wanted.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Format*, and the new *When this file moves ahead
  of yours*.
- `plugin/skills/taskmd/taskmd/schema.py` — `_require`, `CONFIG_KEYS`.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) **D2**, where
  the chain was first written out.

**Acceptance criteria**
- [ ] The three rules and their consequence are stated together, once
- [ ] It says what a project that hits it should do, rather than only that it will
- [ ] It is placed where someone *proposing a key* will read it, not only where someone debugging the
      error will
- [ ] `check` is clean on this repository

**Open questions**
- None. **Q1 — does the answer include a migration route? — decided 2026-08-10 under the standing
  authorization, and the question turned out to conflate two things.** *No mechanism*: an optional
  key, a merge on upgrade or a version marker in every config are each larger than a problem that
  has not arisen since the schema shipped, and each weakens the replace-not-merge rule that makes a
  config say exactly what a project meant. *Yes, a plain instruction*: the error already names the
  key, and the shipped config is the only description of what a key means, so *add the line from the
  shipped file* is the entire upgrade and commits this project to nothing. Criterion 2 asked for the
  second and never for the first. *Rejected: silence about what to do* — it would leave a project
  reading an error about a key it has never heard of with no next step.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Demonstrate the breakage on a real config rather than describing it | A recorded transcript in §3 |
| 2 | Write the conjunction where the three rules it follows from already live | `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 3 | Put a pointer at the line a contributor actually edits to add a key | `plugin/skills/taskmd/taskmd/schema.py`, `CONFIG_KEYS` |
| 4 | Guard the sentence, since a fact stated in only one place is one that can quietly leave | `tests/test_schema.py` |
| 5 | Suite, `index`, `check`, pre-publish check | Recorded output |

Step 1 is first because the whole task is a claim about what happens on upgrade, and this project
does not accept a claim about behaviour that has not been run.

**Shape decisions.**

**D1 — The conjunction goes in the shipped config, beside the drift section, because they are one
subject seen from two ends.** *When this file moves ahead of yours* explains what happens when a
project falls behind on a **value** — an advisory. This explains why it cannot fall behind on a
**key** — a hard failure instead. Splitting them would leave a reader who found one believing they
had the whole upgrade story. *Rejected: `docs/SCOPE.md` under R-11* — it is not shipped to adopters,
and the audience that needs this includes them.

**D2 — The pointer at `CONFIG_KEYS` is where criterion 3 is actually met.** A contributor proposing a
key edits that tuple; nothing makes them open the config document first. A three-line comment
pointing at the section is the only thing that reaches them at the moment of the change. It is a
pointer and not a copy, which is the arrangement `## Ordering` already uses.

**Planned outputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the section
- `plugin/skills/taskmd/taskmd/schema.py` — the pointer
- `tests/test_schema.py` — the guard

## 3. Implement

### Step 1 — the breakage, on a config that is not hypothetical

`after_write` was added to the schema by [T-011](T-011-runtime-discovery-and-project-hook-commands.md).
A project that had written its own config before then holds every key but that one — so the shipped
default with that single line removed **is** what such a project's file looks like, rather than a
contrived one. Against a scratch project holding it:

```text
CONFIG ERROR  .taskmd/config.md: missing config key(s): after_write. A project config replaces
              the default rather than merging with it, so every key must be present.
                                                                                       exit 2
```

Exit 2 at setup, in a project that changed nothing, naming a key nobody there has heard of. That is
the whole claim, run rather than asserted — and it is worth noticing that the message is *good*: it
names the key and the rule. What it cannot say is that this is expected and how to fix it, because
nothing said so anywhere.

### Steps 2–4 — where it is written

The shipped config gains *Adding a key to this file is a breaking change*, stating the three rules as
a numbered chain and the consequence that follows. `CONFIG_KEYS` in `schema.py` carries a pointer to
it and no copy. `tests/test_schema.py` asserts the section and its three premises are present, one
class away from `test_missing_key`, which is the mechanism the section describes.

**The guard is not decoration.** This constraint has no code that fails when the sentence goes
missing — it is true whether or not it is written down, which is exactly why it went unwritten for as
long as the three rules have existed. The precedent is the README assertion T-092 left behind: a
documented gap that quietly loses its documentation is the same silent loss one level up.

### Step 5 — the suite and this repository

```text
Ran 167 tests in 6.494s                                                                      OK
OK - 107 task(s), 535 field value(s), 331 reference(s), 22 dependency edge(s), 147 declared
     output(s), 1 index file(s), 135 document(s), 1029 link(s), 2 template(s),
     0 vocabulary row(s)
```

Figures from the run taken **after** this record was written, so a later reader can reproduce them.

**Decisions & assumptions**

- **Nothing about `_require` changed.** — The task's scope said so and the demonstration confirms why:
  the mechanism is correct and its message is good. What was missing was a reader knowing in advance
  that it is a designed cost rather than a bug in their project. — 2026-08-10
- **Assumption, recorded as one: a key will eventually be added.** — If none ever is, this section is
  three paragraphs nobody needed. It is cheap insurance against a failure that lands on every adopter
  at once, in a project they did not touch, and the work survives being wrong. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — *Adding a key to this file is a breaking change*
- `plugin/skills/taskmd/taskmd/schema.py` — the `CONFIG_KEYS` pointer
- `tests/test_schema.py` — `test_the_shipped_config_warns_that_a_new_key_breaks_every_existing_one`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The three rules and their consequence are stated together, once | met | The shipped config's new section, as a numbered chain. Once: the code carries a pointer, not a copy. |
| It says what a project that hits it should do, rather than only that it will | met | The error names the key; the shipped config is the only description of what a key means, so the line to copy is in it. Q1 records that this is an *instruction* and deliberately not a *mechanism*. |
| It is placed where someone *proposing a key* will read it, not only where someone debugging the error will | met | Two places by design, and **D2** is the one that meets this: the pointer sits on `CONFIG_KEYS`, the line a contributor edits to add a key. The section itself reaches the other audience — an adopter reading the config they are about to copy. |
| `check` is clean on this repository | met | §3 step 5, and `Ran 167 tests … OK`. |

**Child fix tasks raised**
- none.

**Verdict.** All four criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the four criteria as written; **all four met, none carried**, so the task closes. Criterion 3 is the one that shaped the work: it is met by the pointer on `CONFIG_KEYS` rather than by the section, because a contributor adding a key edits that tuple and nothing makes them open the config document first. No child tasks. `deliverables` names the three files. Pre-publish check run last, after this record was written: **193 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken. Step 1 demonstrated the breakage instead of describing it, and on a file that is not contrived: `after_write` was added by T-011, so the shipped default minus that one line **is** what a config written before then looks like. It gives `CONFIG ERROR … missing config key(s): after_write` at exit 2, in a project that changed nothing. The message turns out to be good — it names the key and the rule — which sharpened what was actually missing: not a better error, but a reader knowing in advance that this is a designed cost. Nothing about `_require` changed. The section went beside the drift section written for T-100 (**D1**), because the two are one upgrade story from opposite ends: a project may fall behind on a *value* and be advised, and cannot fall behind on a *key* because it hard-fails instead. The guard in `tests/test_schema.py` is deliberate — this constraint is true whether or not anyone writes it down, which is exactly why it stayed unwritten for as long as the three rules have existed, and no code fails when the sentence goes missing. Suite `Ran 167 tests … OK`. |
| 2026-08-10 | → planned | Plan written; Q1 answered under the standing authorization, and **the question was conflating two things**. No *mechanism* — optional keys, merge-on-upgrade or a version marker in every config are each larger than a problem that has not arisen since the schema shipped, and each weakens replace-not-merge. But yes a plain *instruction*, which is what criterion 2 asked for and all it asked for: the error names the key, and the shipped config is the only description of what a key means, so *copy the line* is the whole upgrade and commits this project to nothing. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"keep going with T-106, full lifecycle"*. It covers this task alone and **does not generalise**; it is the fourth such waiver in this session. Recorded here for the reason [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) exists. |
| 2026-08-10 | → proposed | Raised from [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md)'s plan under METHOD §3.3, and deliberately not fixed there: T-100 needed the answer to shape one decision, and the constraint governs every future one. `high` because it is a trap with no warning sign — the three rules that produce it are each documented and each individually right, and only their conjunction bites; `xs` because the whole work is a paragraph in a file that already carries the rules it follows from. Not a defect: nothing here would be decided differently, and what is missing is the sentence naming the cost. |
