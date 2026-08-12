---
id: T-104
title: Say whether the method has an opinion on where a decision is recorded
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-008, T-076, T-088, T-103]
work_package: M3
owner: maintainer
business_value: medium
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/docs/method/where-facts-live.md, plugin/skills/taskmd/taskmd/defaults/config.md]
---

# T-104 — Say whether the method has an opinion on where a decision is recorded

## 1. Specify

**Outcome**
A project that keeps a decisions register is told whether taskmd considers `type: decision` the home
for a decision and the register a view of it, or whether taskmd has no opinion — so the project is
choosing rather than guessing it has missed something.

**Why this one**
Raised as **R-6** by the first adopting project (`control/LOCAL-CONTEXT.md`). The shipped `type`
vocabulary carries `decision`; `METHOD.md` never mentions decisions. That project already kept a
`tasks/DECISIONS.md` with its own generated view, and after migrating it had both — `type: decision`
tasks *and* a register — with no rule saying which holds what. `context <id>` shows the task and not
the register, so the register is read by hand.

**What it cost.** A standing exception in the project's own configuration, documenting that one
question the tool cannot answer must be looked up elsewhere. That is a second procedure to remember,
which is the thing *one home per fact* exists to prevent.

**The honest counter, which `specify` must weigh rather than skip.** The shipped schema's
*Vocabularies* section already addresses this, and names this exact value: *"These are defaults worth
having, not the set of nouns METHOD uses. `decision` is here and the method never mentions it."* So
the silence is deliberate and it is written down — **one level away from where an adopter meets the
question**, in the schema they copied on day one and are unlikely to reread. The question is not
whether taskmd has thought about it. It is whether a note in the config discharges the duty, or
whether the method owes a sentence at the place a project decides how to record decisions.

**Requirements served**
R-1 (`docs/SCOPE.md`) — one home per fact, applied to a kind of fact the method does not currently
place. R-9, since decision registers are commonest in exactly the non-software work the method claims
to serve.

**Scope**
- In: one paragraph, in METHOD §6 or `method/where-facts-live.md`, saying where a decision lives — or
  saying explicitly that taskmd has no opinion and why.
- In: if the answer is `type: decision`, whether a register is then a **view** of those tasks, and
  what that implies for a project that maintains one by hand.
- Out: a `decision` **edge kind**. The three kinds are fixed and each is a different traversal; this
  is about where a fact is recorded, not about a fourth relationship.
- Out: a command that generates a register. Non-goal 11, and a project's own view is its own to
  generate.
- Out: changing the `type` vocabulary. `decision` stays whatever the answer is.

**Inputs**
- `plugin/skills/taskmd/docs/METHOD.md` §6 and `docs/method/where-facts-live.md`.
- `plugin/skills/taskmd/taskmd/defaults/config.md` §*Vocabularies*, the paragraph that already names
  `decision` as the deliberate mismatch.
- The first adopting project's register and the standing exception it wrote, per
  `control/LOCAL-CONTEXT.md`.

**Acceptance criteria**
- [ ] The answer is written once, and an explicit silence counts as an answer if that is what it is
- [ ] It is placed where a project deciding how to record decisions will actually meet it, which the
      config note is not
- [ ] A decision recorded inside a task's `implement` section — which is how this repository does it,
      and which the template prompts for — is reconciled with the answer rather than contradicted
- [ ] Nothing else in the tree ends up stating a second version of it
- [ ] `check` is clean on this repository

**Open questions**
- None. **Q1 — does taskmd have an opinion at all? — yes, and it already had one when this task was
  raised.** Settled at `plan`, 2026-08-10, by reading the method rather than by choosing:
  `method/where-facts-live.md` has carried two decision rows all along — *a decision made while doing
  a task* lives in that task, and *a decision someone else must make before the work can proceed*
  lives wherever the project registers open ones. So the premise this task inherited is wrong, and
  §1 is corrected below rather than quietly worked around. What is genuinely missing is narrower, and
  it is what this task produces. *Rejected: an explicit no* — it was never available; the method had
  already spoken.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read what the shipped method actually says about decisions, before writing anything | §1's premise confirmed or corrected |
| 2 | Write the part that is missing, in the file that already holds the rest | `plugin/skills/taskmd/docs/method/where-facts-live.md` |
| 3 | Make it reachable from where an adopter meets the question | `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 4 | Check the whole tree for a second statement of it | A recorded grep |
| 5 | Suite, `index`, `check`, pre-publish check | Recorded output |

**Shape decisions.**

**D1 — The correction to §1, stated plainly: the method does mention decisions, twice.** The report
said it never does, and this task repeated that. `METHOD.md` — the *spine* — indeed never does, and
that is what both readings were actually looking at. The answer lives one level down, in the tier-3
file §6 points at, whose stated moment of loading is *"about to write something down and unsure where
it belongs"*. A project deciding **how to organise its records** is not in that moment, so it never
gets there. That is the real defect and it is one of reachability, not of silence.

**D2 — What is missing is the third case: a register of decisions already *taken*.** Row 18 licenses
a register for **open** decisions — correctly, since no task can carry a fact nobody has supplied
yet. Nothing says what happens when the decisions have been made, which is precisely the state the
reporting project was in: `type: decision` tasks *and* a register, with no rule. The answer is that
such a register is a **view** — nothing derives it, so it is a copy, and the tasks stay the source.

**D3 — Reachability is bought in the config, not in the spine.** The one place an adopter meets the
word `decision` is the `type` vocabulary they are copying. A pointer there costs the always-loaded
tier nothing and lands at the moment the question arises, which is what §1's third criterion asks
for. *Rejected: a line in `METHOD.md` §6* — it is read by everyone doing task work and needed by the
few setting a project up, and the spine is the one document this project pays for repeatedly.

**Planned outputs**
- `plugin/skills/taskmd/docs/method/where-facts-live.md` — the missing case
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the pointer, and one stale sentence

## 3. Implement

### Step 1 — the premise was wrong, and the way it was wrong is the finding

```text
grep -rn "decision" plugin/skills/taskmd/docs/METHOD.md plugin/skills/taskmd/docs/method/*.md
  where-facts-live.md:17  A decision made while doing a task, and why -> that task
  where-facts-live.md:18  A decision someone else must make before the work can proceed
                          -> wherever the project registers open decisions, referenced from
                             the task it blocks
```

Two rows, and between them they answer most of the question. The report's *"the method never mentions
decisions"* is true of the spine and false of the method — and the distinction is not pedantry, it is
the diagnosis. `where-facts-live.md` is tier 3, loaded when someone is about to write one thing down
and is unsure where it goes. Nobody organising a project's records is in that moment.

### Steps 2–3 — the missing case, and where it is reachable from

`where-facts-live.md` gains one short section: the two rows divide on *has it been taken*, and a
register of decisions **already taken** is a view of those tasks rather than a second home for them
— including when each decision was its own task. Nothing derives it, so it is a copy, and the section
immediately below has always said what copies do.

The shipped config points at it from the `type` vocabulary, which is the one place an adopter meets
the word. One sentence there also had to be **corrected rather than left**: it used `decision` as its
example of a value the method never mentions, which was already shaky and is now plainly false. The
example is `research` now; the point it was making — that this table is not derived from the method —
is unchanged and still has `audit` as its other half.

### Step 4 — a defect this task introduced, caught by the suite

The first draft of the pointer was a Markdown link. Eleven tests failed:

```text
BROKEN LINK   .taskmd/config.md -> ../../docs/method/where-facts-live.md
```

**The shipped config is a file whose whole purpose is to be copied**, into `.taskmd/` one directory
inside someone else's project — so a relative link in it resolves from where it lands and not from
where it lives. That is [T-076](T-076-decide-what-a-template-s-links-resolve-against.md)'s finding
about templates, arriving at the other file this project ships to be copied. Every other pointer in
that file is a **name** and not a link, which is now stated in the file as a rule rather than left as
a pattern to be noticed.

No task is raised for it: the suite catches it immediately and by name, because `ScratchProject`
copies the shipped default into every project it builds — so the guard is real, and it is the guard
that found this.

### Step 5 — the whole tree, the suite and this repository

```text
grep -rniE "decisions? (register|live|belong)|register of decisions" plugin/ README.md docs/ CLAUDE.md
  where-facts-live.md:26  the new section heading
  where-facts-live.md:32  the new rule
  config.md:215           the pointer

Ran 167 tests in 6.521s                                                                      OK
OK - 107 task(s), ... , 1044 link(s), 2 template(s), 0 vocabulary row(s)
```

One statement, one pointer. The suite is unchanged in count: no behaviour moved.

**Decisions & assumptions**

- **§1's premise is corrected in place rather than rewritten.** — The *Why this one* section argued
  from "the method never mentions decisions", which is false of the method and true of the spine. It
  stays as written with Q1 carrying the correction, because what it got wrong is the same mistake the
  reporting project made and is the reason this task exists. — 2026-08-10
- **`type: decision` is not made mandatory, and the method still names no field.** — The rule is
  *the task*, whichever task that is; whether a project marks such a task with a type value is its
  vocabulary's business, which is the line the schema's own note draws. — 2026-08-10
- **Assumption, recorded as one: an adopter reads the vocabulary table before choosing where
  decisions go.** — That is where the pointer sits. Someone who copies the config without reading it
  gets no warning, which is true of every sentence in that file. — 2026-08-10

**Outputs produced**
- `plugin/skills/taskmd/docs/method/where-facts-live.md` — *A register of decisions is a view*
- `plugin/skills/taskmd/taskmd/defaults/config.md` — the pointer, the corrected example, and the
  no-relative-links rule made explicit

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is written once, and an explicit silence counts as an answer if that is what it is | met | It is not a silence: two rows already existed and a third case is now written beside them, in one file. §3 step 5's grep is the check. |
| It is placed where a project deciding how to record decisions will actually meet it, which the config note is not | met | **D3**: the config note is now exactly that place — it is where an adopter meets the word `decision`, and it points rather than restates. The rule itself stays in the method. |
| A decision recorded inside a task's `implement` section — which is how this repository does it, and which the template prompts for — is reconciled with the answer rather than contradicted | met | It *is* the answer, and was before this task: row 17 says a decision made while doing a task lives in that task. Nothing about this repository's practice changed; what changed is that a register can no longer be read as an equal second home. |
| Nothing else in the tree ends up stating a second version of it | met | §3 step 5. The config carries a pointer and no copy. |
| `check` is clean on this repository | met | Yes, and `Ran 167 tests … OK` — after the suite caught a broken link this task introduced, which §3 step 4 records rather than quietly fixes. |

**Child fix tasks raised**
- none. The relative-link defect in §3 step 4 was introduced and fixed inside this task, and the
  suite is its standing guard.

**Verdict.** All five criteria met, none carried. The task closes.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Reviewed against the five criteria as written; **all five met, none carried**, so the task closes. Criterion 3 is met by the method as it already stood — a decision made while doing a task lives in that task, which is this repository's practice and the template's prompt — so nothing was reconciled away; what changed is that a register can no longer be read as an equal second home. No children: the relative-link defect in §3 step 4 was introduced and fixed inside this task, and the suite is its standing guard. `deliverables` names the two documents. Pre-publish check run last, after this record was written: **193 files scanned, nothing printed**, and the fixture-included run still returns exactly its five lines. |
| 2026-08-10 | → in_progress | All five steps taken, and **step 4 is the one worth reading**: the first draft of the config pointer was a Markdown link, and eleven tests failed with `BROKEN LINK .taskmd/config.md -> ../../docs/method/where-facts-live.md`. The shipped config exists to be **copied**, into `.taskmd/` one directory inside someone else's project, so a relative link in it resolves from where it lands rather than from where it lives — T-076's template finding arriving at the other file this project ships to be copied. Every other pointer in that file was already a name and not a link; that is now written in the file as a rule instead of being a pattern someone has to notice. No task raised, because `ScratchProject` copies the shipped default into every project it builds, so the suite is a real standing guard and is what caught this. One sentence in the config also had to be corrected rather than left: it used `decision` as its example of a value the method never mentions, which this task makes plainly false — the example is `research` now and the point it was making is unchanged. Suite `Ran 167 tests … OK`. |
| 2026-08-10 | → planned | Plan written, and §1's premise turned out to be **wrong** — settled by reading the method rather than by choosing. `method/where-facts-live.md` has carried two decision rows all along: one taken while doing a task lives in that task, one waiting on someone else lives wherever the project registers open decisions. The report's *"the method never mentions decisions"* is true of the **spine** and false of the method, and that distinction is the diagnosis rather than pedantry: the answer sits in a tier-3 file whose stated moment of loading is *about to write something down and unsure where it belongs*, and nobody organising a project's records is in that moment. So the defect is **reachability**, and what is genuinely missing is narrower — the third case, a register of decisions already *taken*, which row 18 does not cover and which is exactly the state the reporting project was in. **D3** buys the reachability in the shipped config rather than in `METHOD.md` §6, because the spine is read by everyone doing task work and needed here only by the few setting a project up. |
| 2026-08-10 | (no change) | **METHOD §3.1 waived for this task by the maintainer, 2026-08-10** — *"keep going with T-104, full lifecycle"*. It covers this task alone and **does not generalise**. |
| 2026-08-10 | → proposed | Raised as R-6 from the first adopting project's recommendations, which ended up running two systems — `type: decision` tasks and its own register — and wrote a standing exception into its configuration saying so. `medium` because the cost is a remembered second procedure rather than a wrong answer, and because a partial answer already exists; `s` because it is a paragraph. The partial answer is recorded here so `specify` does not present itself with a blank page: the shipped schema's *Vocabularies* section already names `decision` as a value the method never mentions and calls that deliberate. The live question is narrower than R-6 states — not *does taskmd have an opinion*, but *does a note in the config file discharge it*, given that a third practice, recording decisions inside the task that took them, is what this repository itself does. |
