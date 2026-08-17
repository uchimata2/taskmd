---
id: T-165
title: Have an uninvolved reader test the post-migration listing
type: fix
status: proposed
phase: specify
parent: T-163
blocked_by: []
related: []
work_package: M6
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-17
updated: 2026-08-17
deliverables: []
---

# T-165 — Have an uninvolved reader test the post-migration listing

## 1. Specify

**Outcome**
The seventh acceptance criterion of
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) is judged by the test it names —
a reader who was not involved reads the listing and says what would change their decision — rather
than by the structural substitute that ran in its place.

**Why this one**
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) closed with that criterion met
by a weaker test, and the substitution is recorded in its §3 and §4. The weaker test asks whether
every claim in the listing is a measured output or a pointer; the specified test asks whether a
reader can *act* on them. **The second can fail while the first passes** — a document can be entirely
factual and still leave someone unable to say what would move them, which is the failure the criterion
was written to catch.

The reason it was not run is recorded and is not a judgement about the test: no uninvolved reader was
available in the session, and spawning an agent to be one had not been asked for.

**Scope**
- In: the reader test, on the listing as it stands.
- In: what the test finds, recorded whether or not it agrees with the structural check.
- Out: rewriting the listing. If the test fails, that is a finding and its repair is its own task —
  a fix made in the same breath as the measurement leaves no evidence the measurement happened.

**Inputs**
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — *What taskmd still gives you here*, the document under test
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 step 6 — what ran instead,
  and why it is weaker

**Acceptance criteria**
- [ ] <written at `specify`>

**Open questions**
- **Who is the uninvolved reader?** A person, or a subagent given the document and nothing else.
  A subagent is cheap and repeatable; a person is the thing the criterion actually means. **The
  maintainer answers, at `specify`.**

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → proposed | Raised as the child of [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) that carries its seventh criterion, under METHOD §2 — a criterion is met, or it carries a child task that will meet it. T-163 met it with a structural check of the same property from the other side and **recorded the substitution rather than claiming the criterion**, which is why this task exists and is small. `xs`: one reading and one recorded answer. **Not covered by the lifecycle authorisation of 2026-08-17**, which named T-108 and T-163 and excluded whatever they raise. |
