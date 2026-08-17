---
id: T-003
title: Closed and quoting a slot to explain it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: []
work_package: F1
owner: the project owner
business_value: low
effort: xs
created: 2026-08-18
updated: 2026-08-18
deliverables: []
---

# T-003 — Closed and quoting a slot to explain it

## 1. Specify

**Outcome**
The second case that must stay silent, and the one that is easy to forget until it bites. This record
is closed, so the gate lets the rule read it — and it quotes a slot line on a line of its own, inside
a fence, in order to explain what an abandoned slot looks like:

```
- <decision — rationale — date>
```

A rule that did not skip fenced blocks would report the document that documents it. That failure is
not hypothetical: writing the task that produced this check is the way to create one.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Hold the quoting shape | this file |

## 3. Implement

**Decisions & assumptions**
- The fence is the whole point of the file — fixture, 2026-08-18

**Outputs produced**
- none

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The quote is silent | met | Above |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | Fixture for T-172. Closed, quoting a slot inside a fence. |
