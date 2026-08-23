---
id: T-245
title: Prompt the adopter_visible judgement at the moment a record closes
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-242, T-182, T-146, T-172]
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables:
  - tasks/_task-template.md
---

# T-245 — Prompt the adopter_visible judgement at the moment a record closes

## 1. Specify

**Outcome**
A closed task that never judged `adopter_visible` is reported by `check`, so the next release does not
meet the wall `0.6.0` met. Nothing new is added to the schema and no second copy of the value exists.

**Why this one**
[T-242](T-242-judge-adopter-visible-on-the-closed-m6-tasks-the-release-note-must-cover.md) cleared 78
unfilled marks. It did not touch the reason they were unfilled, and said so in its own scope:
**nothing asks for the value at the moment `docs/PUBLISHING.md` §7 wants it judged.** The field is not
in the task template, so an author copying the template never meets it. The next release meets the
same wall with a fresh backlog, and clearing it again is not a fix.

**The obvious remedy is closed, and by this project's own decision.**
[T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) considered *a field required at a
status* — precisely *this field is set when a task closes* — and declined it. The reason is in
`.taskmd/config.md` beside the refusal: every route to it needs a new config key, and adding a key to
that file breaks every project that already wrote its own. That decision stands, and this record does
not re-open it.

**What is left is the route the same paragraph points at**: a project enforces its own convention
against its own task files. Here that costs nothing new, because the machinery already ships.

**The mechanism, and the one thing about it that has to be checked first**

`check`'s `ABANDONED SLOT` reports a closed record still carrying an unfilled slot from the project's
own template. So a slot in the template that says *judge `adopter_visible` before closing* would be
reported on exactly the records that closed without judging it, and it moves the exit status.

**But the check reads the body and not the front matter.** Measured 2026-08-23: `check_abandoned_slots`
splits the front matter off and iterates the body, and its message says *body line N*. So putting
`adopter_visible: <yes | no>` in the template's front matter would do nothing at all, which is the
version of this fix that looks right and is not. The slot has to be a **prompt in the body**, and the
value stays in the front matter where it already lives. That is also what keeps this from creating a
second home for the fact.

**Scope**
- In: a slot in `tasks/_task-template.md`'s body that prompts the judgement, and evidence that a
  closed record still holding it is reported
- In: whether this project's existing closed records are affected, since they were not copied from a
  template carrying the slot
- Out: re-opening [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)
- Out: **shipping this to adopters.** `adopter_visible` is this project's own field, not a taskmd one.
  Whether the shipped template gains anything is a separate question and probably a no
- Out: the release-note rule itself, which is
  [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_abandoned_slots`, and the docstring saying why only
  closed records are read
- `.taskmd/config.md` — the refusal of a required-at-status rule, and what it says a project does
  instead
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §7 — the rule that consumes the value, and its
  statement that the judgement is made when the work is understood

**Acceptance criteria**
- [ ] A closed record that never judged `adopter_visible` is reported by `check`, shown by making it
      fail on a real case rather than by a clean tree
- [ ] The value has exactly one home, and the slot is a prompt rather than a copy of it
- [ ] No config key was added
- [ ] What this does to the existing closed backlog is stated, either way

**Open questions**
- **Does the slot go in `## 4. Review`, or beside the front matter at the top?** — whoever implements
  it. The recommendation is **`## 4. Review`**, because that is the phase where the outcome is being
  judged against what it produced, which is when the answer is known. *Against: it is furthest from
  the field it prompts for, and a reader filling in the front matter never looks there.*

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised on the owner's answer of 2026-08-23**, chosen over re-opening [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s declined required-at-status rule, and over re-deriving the marks at every release. The rejected options and what each costs are in the survey that produced this record; the short form is that re-opening T-146 needs a config key that breaks every configured project, and re-deriving makes the mark something computed at publication, which is what §7 says the field exists not to be. **The one measurement that shapes the fix is in §1**: `ABANDONED SLOT` reads the body and not the front matter, so the version of this that adds `adopter_visible: <yes \| no>` to the template's front matter would do nothing and look right. Checked in `check_abandoned_slots` before the option was offered. |
