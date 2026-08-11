---
id: T-123
title: Decide whether a replaced vocabulary row is drift or a choice
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-082]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-123 — Decide whether a replaced vocabulary row is drift or a choice

## 1. Specify

**Outcome**
`check`'s `CONFIG DRIFT` line either stops firing on a vocabulary row a project has **replaced**,
or the shipped config stops claiming it only reports a lag — and whichever way it goes, the reason
is written where the next person meets the behaviour.

**Why this one**
The shipped config says the drift line reports exactly one shape: *a row you still keep, missing a
value this file has since gained*, and says why nothing else is reported — "reporting choices would
make every configured project noisy from its first run — extra values, extra rows, renamed fields
and every front-matter setting are the whole point of writing a config."

A row whose **values** are wholly replaced, under a field name that happens to match, is such a
choice and is reported anyway. Found while building `tests/fixtures/backend-allocated-ids` for
[T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md), whose `status` row is
`open, closed`:

```
CONFIG DRIFT  status: shipped default adds 'proposed', 'specified', 'planned', 'in_progress',
'blocked', 'review', 'done', 'cancelled'; this project's row does not carry them
```

`alt-project` does not hit it only because it renamed the *field* to `state`, so no row matches at
all — which means the noise arrives precisely for the project that kept taskmd's field names and
brought its own values, the commonest way to adopt. Any project on an issue tracker is that project:
`open`/`closed` is what a backend gives you.

**Why it is a decision and not a fix.** From the config alone the two cases are indistinguishable:
a project that pinned and fell behind, and a project that replaced the row, both present as a kept
field name carrying fewer values than the default. Suppressing the report when *no* default value
survives would silence the replace case, but it also silences a project that renamed every value
while genuinely being behind on a ninth. Whether that trade is worth making is the question.

**Scope**
- In: what `check` reports for a kept field name whose values are wholly replaced; the shipped
  config's paragraph describing what the line reports; whichever of the two moves.
- Out: the drift mechanism itself, and the rule that it is advisory and never changes the exit
  status — both settled and not re-opened. Out also: adding a key to switch it off, which the
  shipped config rules out for a reason that this finding does not touch.

**Inputs**
- `plugin/skills/taskmd/taskmd/defaults/config.md` — *When this file moves ahead of yours*, the
  paragraph beginning "Only one shape is reported".
- `plugin/skills/taskmd/taskmd/cli.py` — the drift comparison.
- `tests/fixtures/backend-allocated-ids/` — the case, already in the tree and already passing;
  `tests/fixtures/README.md` records the line as expected and points here.

**Acceptance criteria**
- [ ] Running `check` on `tests/fixtures/backend-allocated-ids` either prints no `CONFIG DRIFT`
      line, or prints one the shipped config's own description covers
- [ ] The decision names what it costs — a project that both renamed its values and is behind on a
      new one, if the report is narrowed; noise on every issue-tracker project, if it is not
- [ ] `tests/fixtures/README.md` no longer defers to this task

**Open questions**
- Whether a third answer is better than either: report the row as *replaced* rather than as
  *behind*, saying what the tool actually knows. Costs a second message shape; decide in `specify`.

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
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → proposed | Raised from T-082, which met it while building a fixture and did not fix it there (METHOD rule 4). **Filed `v0.2` by `tasks/README.md`'s rule** — a minor-to-moderate correction, blocking nothing — and that brings it inside the standing v0.2 full-lifecycle authorization, which is a consequence of the filing rule and not a grant. The task that raised it did not start it. Worth knowing before it is worked: the evidence is already committed and passing, so nothing regresses while this waits; what waits is one advisory line that every issue-tracker adopter will see and have to ask about. |
