---
id: T-133
title: Decide what to do about a published release note that breaks the rule
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-079, T-081, T-125, T-126, T-127, T-135]
work_package: v0.5
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [docs/PUBLISHING.md]
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
- None. **Q1 — edit the published body, or leave it? — answered by the maintainer on 2026-08-11:
  leave it, and record why.** A release note is a dated record of what was said at the time, and
  rewriting one after the rule changed is the same class of act as rewriting a task record's past,
  which METHOD rule 5 forbids. *Rejected: editing the four characters out* — the rule is now written
  and this is the only covered page that breaks it, so the cost of leaving it is a standing exception
  that has to be written down instead of removed. That is what §3 does.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Record the exception where a reader of the rule will meet it | `docs/PUBLISHING.md` §1 |
| 2 | Re-run the measurement so the figure in the record is current rather than remembered | §3 |

## 3. Implement

### Step 2 — the figure, re-measured at close

```text
tag messages      v0.1.0  em 0   v0.2.0  em 0   v0.3.0  em 0   v0.4.0  em 0
release bodies    v0.1.0  em 0   v0.2.0  em 4   v0.4.0  em 0        (v0.3.0 has no release)
```

Unchanged. One page, four characters, and nothing else in breach.

### Step 1 — where the exception is written

`docs/PUBLISHING.md` §1, in the paragraph that adopted the rule, because that is where a reader meets
the rule and therefore where they would otherwise meet a contradiction: a stated rule and a published
page that breaks it, with nothing saying which is wrong.

**Decisions & assumptions**

- **The exception names the page and the date, not just the fact.** An unexplained exception is
  indistinguishable from an oversight, and the next person to run the check would file this again. —
  2026-08-11
- **`v0.3.0` having no release is left alone.** It is deliberate and `v0.4.0`'s notes explain it; this
  task is about a body that exists and breaks the rule, not about one that does not exist. —
  2026-08-11

**Outputs produced**
- `docs/PUBLISHING.md` — §1, the recorded exception

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The `v0.2.0` release body either passes the dash rule, or the decision to leave it is recorded with its reason | met | Left, by the maintainer's answer, and recorded in `docs/PUBLISHING.md` §1 rather than only here — a reader meets the rule there, so that is where the exception has to be. |
| Whichever way it goes, the check is re-run afterwards and the figure recorded | met | Re-run at close: 4 em dashes in `v0.2.0`'s body, 0 everywhere else, all four tag messages clean. |
| If editing is chosen, nothing else in the body changes | n/a | Editing was not chosen. |

**Child fix tasks raised**
- none. The related report that arrived the same day — `v0.4.0`'s note omitting
  [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) — is a
  different defect in a different note and is
  [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md).

**Verdict.** All applicable criteria met. The rule now has one written exception instead of one
silent contradiction.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | **Left as published, by the maintainer's answer of 2026-08-11**, and the reason written into `docs/PUBLISHING.md` §1 rather than only here: a reader meets the rule there, so an unexplained exception would read as an oversight and be re-filed. The measurement was re-run at close rather than quoted from memory and is unchanged — 4 em dashes in `v0.2.0`'s body, 0 everywhere else, all four tag messages clean. The rejected reading is recorded with its cost: the rule now carries one written exception instead of one silent contradiction. | 
| 2026-08-11 | → proposed | Raised by [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md)'s criterion 3, which is the reason it exists: *check the existing notes rather than assume them*. The check refuted two things at once — T-127's own claim that the published notes were clean, and the assumption that a tag message and a release body are the same text. **Not worked under the standing v0.5 authorization**, which grants phases and not the right to modify public content; Q1 goes to the maintainer. `low` and `xs`: one page, four characters, on a version bump. |
