---
id: T-082
title: Let id_width say that the backend allocates the ids
type: fix
status: proposed
phase: specify
parent: T-004
blocked_by: []
related: [T-075, T-010]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-09
updated: 2026-08-10
deliverables: []
---

# T-082 — Let id_width say that the backend allocates the ids

## 1. Specify

**Outcome**
A project whose ids are allocated by its backend can write a config that describes them, and
[`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) stops claiming the identity keys
already do.

**Why this one**
Raised by [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) §3 D3, which decided
the shape and left the change here because T-004 is a `decision` task and this is code and a
document. The binding says:

> the identity keys describe the issue number rather than a chosen format. A project on this
> backend has ids like `#41`; `id_prefix` and `id_width` describe that, they do not impose it.

Since [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md), `is_id` matches the prefix plus
**exactly** `id_width` digits. No value of `id_width` describes `#7` and `#41` in one repository, so
the second half of that sentence is false and the first half is unreachable. T-075 was right for
local files — the width is what makes a mistyped id reportable there — and the two backends want
opposite things from the same key, which is why a value meaning "not applicable" is the fix rather
than a relaxation.

**Why the width check protects nothing on that backend.** An id you cannot invent cannot be
mistyped: on GitHub the number comes back from `create` and is read, never composed. So the rule
that earns its keep locally has nothing to catch there, and enforcing it costs a project the ability
to describe its own ids.

**Scope**
- In: a value of `id_width` meaning "the backend allocates these; impose no width", its effect on
  `is_id` and `format_id`, whatever `check` should say about a project configured that way, and the
  binding sentence above.
- Out: the default, which stays `T-` and 3 — decided in T-004 §3 D1 and not re-opened here. Out
  also: anything that would let a local project turn the width check off as a convenience; the value
  is for a backend that allocates, and the record should say so plainly enough that it is not read
  as an escape hatch.

**Inputs**
- [`defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md) — `none` is already this config's word
  for a key that does not apply, in `blocked_status`, `deliverables_field`, `value_field`,
  `effort_field` and `after_write`. The idiom exists; this is one more use of it.
- [`schema.py`](../plugin/skills/taskmd/taskmd/schema.py) — `is_id`, `looks_like_id`, `format_id`, and the
  `id_width < 1` rejection that a non-numeric value has to pass through.
- [`github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md) — the sentence, and assumption 1
  around it.

**Acceptance criteria**
- [ ] A config with the new value loads, and a project whose ids are the prefix plus digits of
      **mixed** widths enumerates every one of them
- [ ] The default config still rejects a wrong-width id, shown by the existing
      `tests/fixtures/broken-id-width` continuing to fail
- [ ] `format_id` either does something defined under the new value or is unreachable by a
      documented route — a padder with no width to pad to is the obvious way this breaks
- [ ] The binding sentence says what is true of the keys as they then are

**Open questions**
- Whether `looks_like_id` still means anything when width is off — the near-miss it exists to report
  is defined by the width. Answer it in `specify`; it may simply be that the two collapse.

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
| 2026-08-09 | → proposed | Raised by T-004 §3 D3, which found the contradiction while settling its own fourth criterion and decided the shape rather than the change: T-004 is a `decision` task, and a config key plus a binding sentence is neither. Not a blocker on publication — the CLI is local-markdown only, so nothing today reads a config for a GitHub-backed project; what ships broken is the instruction to write one. |
