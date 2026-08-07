---
id: T-046
title: Reconcile the done-condition CLAUDE.md restates from the method
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-027, T-028]
work_package: none
owner: maintainer
business_value: high
effort: xs
created: 2026-08-07
updated: 2026-08-07
deliverables: []
---

# T-046 — Reconcile the done-condition CLAUDE.md restates from the method

## 1. Specify

**Outcome**
`CLAUDE.md` states no closing condition of its own. Either it points at `docs/METHOD.md` §1 rule 5,
or it states only the part that is genuinely local — and its own sentence saying the method is not
restated there becomes true of the file.

**Why this one**
Raised by [T-027](T-027-give-the-design-rule-one-home.md)'s review, against its criterion 3: *"`CLAUDE.md`'s
own 'if you find it written out somewhere else, that copy is the defect' sentence is true of the file
that contains it."* Checked against the file rather than against the section T-027 edited, it is not:

| Document | The closing condition |
| :--- | :--- |
| `docs/METHOD.md` §1 rule 5 | outcome exists, record is current, **the `implement` evidence is written down** |
| `CLAUDE.md` §*Working method* | deliverables exist, log is current, **the validator passes** |

**It is not a copy, it is a copy that has already drifted** — which is the more expensive kind. Two
of the three slots are the local nouns for METHOD's, and that much is what a binding legitimately
does. The third is a different condition: METHOD requires recorded evidence that the outcome was
used, `CLAUDE.md` requires a tool run. A task can pass `python -m taskmd check` with `## 3. Implement`
left as the template placeholder, so the local version can be satisfied with none of what the method
asks for. The rule this project claims most loudly is the one it restated and lost a clause from.

**The framing around it is right for the other three bullets.** The list is introduced as *"What this
project adds on top, because the method is deliberately storage-agnostic"* — and the tasks folder,
the schema file and the generated index are genuine additions. This one is not an addition; it is
METHOD §1 rule 5 with local nouns and a substituted clause, sitting under a heading that says it is
not.

**Requirements served**
R-1, R-4 (`docs/SCOPE.md`).

**Scope**
- In: `CLAUDE.md` §*Working method*, the `done` bullet, and whatever replaces it.
- In: whether the local mapping belongs in `docs/bindings/local-markdown.md` instead — it is the
  document whose job is saying which artifact plays which role, and it does not currently carry this.
- Out: `docs/METHOD.md` §1 rule 5 itself, which is the one home and is correct as written.
- Out: the other three bullets in that list, which are additions and not restatements.
- Out: making `check` enforce the evidence clause. That is a tool change and a separate argument;
  this task is about a document saying something the method does not.

**Inputs**
`CLAUDE.md` §*Working method*, `docs/METHOD.md` §1 rule 5 and §2 *implement*,
`docs/bindings/local-markdown.md`, [T-027](T-027-give-the-design-rule-one-home.md) §4.

**Acceptance criteria**
- [ ] `CLAUDE.md` no longer states a closing condition that differs from `docs/METHOD.md` §1 rule 5
- [ ] The `implement`-evidence clause is reachable from `CLAUDE.md` in one link, or is stated there
      correctly — losing it silently is the defect, so a fix that drops the sentence without
      replacing the route to it does not count
- [ ] `CLAUDE.md`'s "it is not restated here; if you find it written out somewhere else, that copy is
      the defect" sentence is true of the whole file, checked by re-reading the file and not only the
      edited line
- [ ] If the local mapping moves to `docs/bindings/local-markdown.md`, that binding says it once and
      `CLAUDE.md` points there

**Open questions**
- None blocking `specify`. Which of the two homes takes the local mapping — `CLAUDE.md` as a pointer,
  or the local-markdown binding — is `plan`'s to choose against criterion 4.

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
| 2026-08-07 | → proposed | Raised by T-027's review and not fixed there (METHOD §5), because T-027's scope was one section of `CLAUDE.md` and this is a different one. Found only because criterion 3 makes a claim about *the file*, so it was checked against the file. `business_value: high` and `effort: xs`: one bullet, and what it currently licenses is closing a task with `## 3. Implement` still holding the template placeholder, which is the failure R-4 exists to prevent. |
