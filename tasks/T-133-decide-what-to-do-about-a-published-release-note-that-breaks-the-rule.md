---
id: T-133
title: Decide what to do about a published release note that breaks the rule
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-079, T-081, T-125, T-126, T-127]
work_package: v0.5
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: []
---

# T-133 — Decide what to do about a published release note that breaks the rule

## 1. Specify

**Outcome**
The `v0.2.0` release body on GitHub either carries no em dashes, or the project records that a
published note is left as it was written and says why.

**Why this one**
Found by [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md)'s criterion 3,
which asked for the existing notes to be checked against the answer rather than assumed to comply.
Measured 2026-08-11, after the maintainer ruled release notes **covered**:

```text
tag messages      v0.1.0  em 0   v0.2.0  em 0   v0.3.0  em 0   v0.4.0  em 0
release bodies    v0.1.0  em 0   v0.2.0  em 4   v0.4.0  em 0        (v0.3.0 has no release)
```

**Two things this refutes.** T-127's own §1 said *"the three published release notes carry no em
dashes"* — true of the tag messages, and false of what is on the release pages. And the tag message
and the release body turn out to be **different texts**: `v0.2.0`'s tag message is 936 characters and
its body 2591. Whoever checked, checked the reachable one.

**Why `low`.** One page, four characters, on a version bump rather than a milestone. It is filed
because the rule now exists and this is the one thing known to breach it, not because anything is
harmed.

**Requirements served**
R-21 (`docs/SCOPE.md`).

**Scope**
- In: the `v0.2.0` release body, and whether a published note may be edited after the fact.
- Out: the tag message, which is clean, and rewriting any tag.
- Out: whether release notes are covered at all. Settled in T-127.
- Out: automating the check. The body is on GitHub and needs the network, which `docs/SCOPE.md` §5's
  dependency-free constraint keeps out of the suite; T-127 records that in `docs/PUBLISHING.md` §1.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §1, as amended by T-127.
- The measurement above, reproducible with `gh release view v0.2.0 --json body -q .body`.

**Acceptance criteria**
- [ ] The `v0.2.0` release body either passes the dash rule, or the decision to leave it is recorded
      with its reason
- [ ] Whichever way it goes, the check is re-run afterwards and the figure recorded
- [ ] If editing is chosen, nothing else in the body changes — a humanizer rewrite of a shipped note
      is a different act from removing four characters

**Open questions**
- **Q1 — edit the published body, or leave it? — for the maintainer.** Editing public content is not
  something a session does on a standing authorization, and the two readings are both defensible.
  *Edit*: the rule is now written, and a covered page that breaks it is the only such page there is.
  *Leave*: a release note is a dated record of what was said at the time, and quietly rewriting one
  is the same class of act as rewriting a task record's past, which METHOD rule 5 forbids. The
  recommendation is **leave it and record why**, because the rule was adopted on 2026-08-11 and this
  page was written before it.

## 2. Plan

_Not planned. Q1 is the whole of the work and it is the maintainer's._

## 3. Implement

_Not started._

## 4. Review

_Not started._

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → proposed | Raised by [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md)'s criterion 3, which is the reason it exists: *check the existing notes rather than assume them*. The check refuted two things at once — T-127's own claim that the published notes were clean, and the assumption that a tag message and a release body are the same text. **Not worked under the standing v0.5 authorization**, which grants phases and not the right to modify public content; Q1 goes to the maintainer. `low` and `xs`: one page, four characters, on a version bump. |
