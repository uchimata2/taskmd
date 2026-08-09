---
id: T-074
title: Let the skill point where it currently restates
type: fix
status: proposed
phase: specify
parent: T-059
blocked_by: []
related: [T-003, T-009]
work_package: none
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
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised as F-14 from the T-059 audit, clause 2. Located by a phrase sweep across live documents: one sentence, verbatim, in two shipped files, two lines after the skill points at the file that holds the other copy. `low`/`xs`. The counter-argument is recorded in §1 rather than left out — the copy does real work where it sits, and R-22 is the reason it loses anyway. |
