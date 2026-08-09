---
id: T-074
title: Let the skill point where it currently restates
type: fix
status: done
phase: review
parent: T-059
blocked_by: []
related: [T-003, T-009]
work_package: v0.1
owner: maintainer
business_value: low
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-074 — Let the skill point where it currently restates

## 1. Specify

**Outcome**
`SKILL.md` carries no sentence that also exists in the binding it points at, so R-22's *point at the
tool, do not restate it* is true of the skill as written.

**Why this one**
Raised as **F-14** by [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md),
threshold clause 2. One sentence, verbatim in two shipped files:

```
plugin/skills/taskmd/SKILL.md:41
plugin/docs/bindings/local-markdown.md:121
    ... taskmd never writes a task file, so the edit that made the index stale is one it never saw ...
```

`SKILL.md` reaches this sentence **two lines after** telling the reader to load the binding *"before
creating or changing any task"* and that *"a write is not finished until the binding's after any write
step has run"*. So the pointer and the copy sit in the same paragraph, which is the shape
`docs/BRIEF.md` warns about in terms — *"a skill that describes what the CLI already enforces is a
second copy that will drift"*.

**Both copies ship**, so the pair travels to every adopter and either can be edited without the other.

**The counter-argument, recorded rather than dismissed.** The sentence is doing real work where it
sits: it explains *why* the reader must run `index` themselves rather than trusting the tool, at the
exact moment the instruction is given, and a reader who does not follow the pointer will not otherwise
learn it. That is a genuine reason a summary exists, and it is the reason this is `low` rather than
being obviously wrong. What decides it is that the same reasoning would justify any restatement, and
R-22 exists because this project chose the other side of that trade.

**Requirements served**
R-22 (`docs/SCOPE.md`) — the skill points at the tool rather than restating what it enforces; R-1;
§2 principle 3.

**Scope**
- In: the duplicated sentence, and which of the two files keeps it.
- In: one sweep of `SKILL.md` and `adopt.md` for any other sentence that also exists in the method,
  the binding or the config — done once rather than one line at a time.
- Out: the binding's *After any write* section, which is where the fact belongs and is not in
  question.
- Out: the skill's structure and its load table, settled in
  [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md).
- Out: anything about what the tool does. This is about where a true sentence lives.

**Inputs**
`plugin/skills/taskmd/SKILL.md`, `plugin/skills/taskmd/adopt.md`,
`plugin/docs/bindings/local-markdown.md` *After any write*, `docs/SCOPE.md` R-22,
[T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) F-14.

**Acceptance criteria**
- [ ] The sentence exists in one of the two files; a grep for its distinctive phrasing returns one
      hit under `plugin/`
- [ ] The grep pattern tolerates the files' own emphasis and line wrapping — a literal search that
      returns zero looks exactly like success
- [ ] `SKILL.md` still tells its reader that running `index` is theirs to do, without carrying the
      explanation
- [ ] The sweep result is recorded, including "nothing else found" if that is the answer

**Open questions**
- None. Which file keeps the sentence follows from R-22 and from the binding already owning *After
  any write*; the sweep may turn up more, which is `plan`'s to size.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide which file keeps the sentence | §3 D1 |
| 2 | Rewrite the skill's line so it still tells the reader the step is theirs, without carrying the reason | `plugin/skills/taskmd/SKILL.md` |
| 3 | Build the grep first and make it find **two**, so that finding one afterwards means something | Both counts |
| 4 | Sweep the two skill files against the method, the binding and the config for any other shared sentence, and record the result even if it is nothing | The sweep output |

**Why step 3 builds the grep before the edit.** A literal search for a wrapped, emphasised sentence
returns zero, and zero looks exactly like success. The pattern has to be shown finding the
duplication before it can be trusted to show the duplication gone.

## 3. Implement

**Decisions & assumptions**

- **D1 - the binding keeps it, the skill points** - 2026-08-09. The binding owns *After any write*,
  and the sentence is the reason that step cannot be delegated to `after_write` - it belongs in the
  paragraph that makes the distinction. R-22 says the skill points at the tool rather than restating
  what it enforces, and this was the one place it did not. The skill's line now reads: *"A write is
  not finished until the binding's after any write step has run, and it is yours to run - the
  binding says why the tool cannot do it for you."* The obligation stays; the explanation moves to
  its one home.

- **D2 - the third occurrence of the clause is not a copy** - 2026-08-09. `taskmd/defaults/config.md`
  also says *"taskmd never writes a task file"*, in a sentence about pass-through fields being
  carried unaltered - written earlier this session by
  [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md). It is the same **premise**
  supporting a different claim, and removing it would leave that sentence incomplete. A shared
  premise is not a duplicated fact; what F-14 found was a duplicated *conclusion*.

### Step 3 - the grep, shown finding two before it is used to show one

The pattern allows a line break or emphasis between any two words, which a literal search does not:

```
edit[[:space:]*_]+that[[:space:]*_]+made[[:space:]*_]+the[[:space:]*_]+index[[:space:]*_]+stale

before   plugin/skills/taskmd/SKILL.md            1
         plugin/docs/bindings/local-markdown.md   1
after    plugin/docs/bindings/local-markdown.md   1
```

### Step 4 - the sweep, and its answer

Every sentence of eight words or more in `SKILL.md` and `adopt.md`, normalised for markup and
compared against every `.md` under `plugin/` outside the skill:

```
nothing else found - no sentence of 8+ words is shared between the skill and the
method, the binding or the config
```

Recorded because "nothing" is a result: the skill restated exactly one thing, and F-14 found it.

**Outputs produced**
- `plugin/skills/taskmd/SKILL.md` - two lines where three were

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The sentence exists in one of the two files; a grep for its distinctive phrasing returns one hit under `plugin/` | met | One hit, in the binding. The skill keeps the obligation and drops the reason |
| The grep pattern tolerates the files' own emphasis and line wrapping | met | Built before the edit and shown returning **two**, which is what licenses reading one afterwards as success rather than as a broken pattern |
| `SKILL.md` still tells its reader that running `index` is theirs to do, without carrying the explanation | met | *"it is yours to run - the binding says why the tool cannot do it for you"* |
| The sweep result is recorded, including "nothing else found" if that is the answer | met | That is the answer, and it is recorded. Plus D2, which is the near-miss the sweep surfaced and which is a shared premise rather than a copy |

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All four criteria met. The binding keeps the sentence because it owns *After any write* and the sentence is the reason that step cannot be delegated to `after_write`; the skill keeps the obligation and drops the explanation, which is R-22. The method point is criterion 2: the grep was **built before the edit and shown returning two**, because a literal search for a wrapped, emphasised sentence returns zero and zero looks exactly like success. The sweep for other shared sentences found nothing, which is recorded as a result rather than omitted. One near-miss is recorded as a decision: `config.md` uses the same clause as a **premise** for a different claim about pass-through fields, and a shared premise is not a duplicated conclusion. |
| 2026-08-09 | → in_progress | Plan decides which file keeps the sentence before touching either, since the answer follows from R-22 and from the binding already owning the section rather than from whichever is easier to edit. |
| 2026-08-09 | → specified | Criteria stand as raised; no open question, as recorded. |
| 2026-08-09 | → proposed | Raised as F-14 from the T-059 audit, clause 2. Located by a phrase sweep across live documents: one sentence, verbatim, in two shipped files, two lines after the skill points at the file that holds the other copy. `low`/`xs`. The counter-argument is recorded in §1 rather than left out — the copy does real work where it sits, and R-22 is the reason it loses anyway. |
