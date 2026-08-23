---
id: T-245
title: Prompt the adopter_visible judgement at the moment a record closes
type: fix
status: done
phase: review
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
  - tasks/_audit-umbrella-template.md
  - tests/test_publishing.py
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
- ~~**Does the slot go in `## 4. Review`, or beside the front matter at the top?**~~ **Answered at
  implement, 2026-08-23: `## 4. Review`**, taking the recommendation. *The question as it stood, kept
  so a later reader can see what was chosen over what: — whoever implements it. The recommendation is*
  **`## 4. Review`**, *because that is the phase where the outcome is being judged against what it
  produced, which is when the answer is known. Against: it is furthest from the field it prompts for,
  and a reader filling in the front matter never looks there.* What settled it is in §3: the check
  reads **closed** records only, so a slot anywhere earlier is silent until the record closes anyway —
  the top-of-file position buys proximity and changes nothing about when the prompt bites.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Confirm what `slot_lines` treats as a slot, and where `check_abandoned_slots` looks | The mechanism in §3, read from `cli.py` rather than assumed |
| 2 | Answer §1's open question and put the slot in the templates | `tasks/_task-template.md` and `tasks/_audit-umbrella-template.md` |
| 3 | Plant the slot in a **real** closed record and run `check` | A recorded failing run, in §3 |
| 4 | Measure what the change does to the existing closed backlog | A count, in §3, either way |
| 5 | Guard the prompt itself, so it cannot vanish silently | `tests/test_publishing.py`, four cases, shown to fail |

## 3. Implement

**Decisions & assumptions**

- **The slot goes in `## 4. Review`** — 2026-08-23, answering §1's open question. *Rejected: beside
  the front matter at the top*, whose whole argument was proximity to the field. It buys nothing
  here: `check_abandoned_slots` reads **closed** records only, so a slot at the top of an open record
  is as silent as one in its last section, and the prompt bites at exactly the same moment either
  way. Review is where the outcome is judged against what it produced, which is when the answer is
  known.

- **Both templates carry it, not only `_task-template.md`** — 2026-08-23. §1 named one file, and the
  project has two: `_audit-umbrella-template.md` has its own `## 4. Review` and closes like any other
  record. Leaving it out would have met the letter of the declared deliverable and left the outcome —
  *a closed task that never judged `adopter_visible` is reported* — half true, with the gap sitting in
  exactly the record type that generates the most children. `deliverables` above was widened to say
  so rather than the second file being added quietly.

- **The slot carries no code spans, and that is a measured decision rather than a style one.**
  `check` blanks fenced and inline code *before* matching, so the first version — with the field name
  and the path in backticks — reported this:

  ```text
  ABANDONED SLOT tasks/T-231-cut-the-next-release.md body line 188 still reads
  '**Adopter-visible?** <yes or no - then set        in the front matter, per        §7>'
  ```

  The message is the thing somebody acts on, and it had holes where the instruction should be. The
  slot was rewritten without backticks and re-measured. `test_the_prompt_reports_readably` is what
  keeps them out.

- **No config key was added, and none was needed.** The mechanism is the project enforcing its own
  convention against its own task files, which is the route `.taskmd/config.md` points at where it
  declines a required-at-status rule. [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)
  is not re-opened.

- **The existing closed backlog is unaffected, and the measurement is the point of saying so.**
  `check` reports a closed record that *contains* an unfilled slot line. The 241 records that closed
  before today were copied from a template that carried no such line, so they contain nothing to
  match: `check` exits 0 on the tree with the slot added, with `ABANDONED SLOT` reported **0 times**.
  The fix is forward-looking by construction. What it does **not** do is find the records already
  unjudged — [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)
  is those, surfaced by T-243's rule rather than by this one.

- **The gap this leaves, stated rather than found later.** The check sees an *unfilled slot*, not an
  *unfilled field*. Deleting the prompt line without setting the front-matter value closes the record
  silently. Nothing here closes that, and closing it is what needs the config key T-146 declined.

**Outputs produced**

- [`tasks/_task-template.md`](_task-template.md) and
  [`tasks/_audit-umbrella-template.md`](_audit-umbrella-template.md) — one line each in `## 4. Review`,
  prompting the judgement and naming where the value goes.
- [`tests/test_publishing.py`](../tests/test_publishing.py) —
  `TheAdopterVisibleJudgementIsPromptedAtClose`, four cases. It sits beside §7 because §7 is what
  consumes the value, and it derives the template list the way the binding does rather than naming
  files, so a third template arms it with nothing edited.

**Checked by using it.** The slot was planted, unfilled, in a **real** closed record — not a fixture:

```text
check exit=1
ABANDONED SLOT tasks/T-231-cut-the-next-release.md body line 188 still reads
'**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in
docs/PUBLISHING.md section 7>'; the record is closed, so nothing is going to fill it
```

The record was then restored from a copy taken before the edit, and `check` returned to 0.

**And the guard was shown to fail.** The slot was removed from one template and turned into a
body-level `adopter_visible:` field in the other — the two ways this fix can rot:

```text
FAILED test_every_template_prompts_for_the_judgement
FAILED test_the_prompt_does_not_carry_the_value
FAILED test_the_prompt_is_a_slot_so_an_abandoned_one_is_reported
3 failed, 1 passed
```

One assertion message read wrongly in that run — it said a template *mentions* the field outside a
slot when the mention was gone entirely — and was corrected before the templates were restored.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A closed record that never judged `adopter_visible` is reported by `check`, shown by making it fail on a real case rather than by a clean tree | met | `check exit=1`, `ABANDONED SLOT` on `T-231` with the slot planted unfilled. A real record, restored afterwards |
| The value has exactly one home, and the slot is a prompt rather than a copy of it | met | The line asks for the judgement and names the front matter as where it goes. `test_the_prompt_does_not_carry_the_value` fails if a body-level `adopter_visible:` appears, and did |
| No config key was added | met | `.taskmd/config.md` is untouched. The mechanism is the project's own convention against its own files, which is the route that file points at |
| What this does to the existing closed backlog is stated, either way | met | Nothing: 241 records closed before today contain no line to match, and `check` reports `ABANDONED SLOT` 0 times on the tree with the slot added. §3 says so, and says what does find them |

**Adopter-visible?** no — this is the project's own template and its own release-note discipline. An
adopter's output, files and actions are unchanged; `adopter_visible` is not a taskmd field, which §1
puts out of scope.

**Child fix tasks raised**
- none. The three unjudged records this work sits next to are
  [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md), raised
  from [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md)
  and not by this record.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **Landed under the owner's unattended full-lifecycle grant, recorded below.** The slot went to `## 4. Review`, and to **both** templates rather than the one §1 named — the umbrella closes like any other record, and `deliverables` was widened to say so rather than the second file being added quietly. Two things were measured rather than assumed: the existing backlog is untouched, because 241 already-closed records contain no line to match; and the slot carries no backticks, because `check` blanks code spans before reporting and the first version printed gaps where the instruction should be. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, unattended, and asks that it land before the audit** — given on 2026-08-23 in these words: *"Update the handoff file to land T-243 and T-245 before the audit in the new session, full lifecycle, commit and push"*. Recorded here rather than in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, and committing and pushing the result. **What it does not:** any other task, and starting [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md), which stays the owner's to begin. |
| 2026-08-23 | → proposed | **Raised on the owner's answer of 2026-08-23**, chosen over re-opening [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s declined required-at-status rule, and over re-deriving the marks at every release. The rejected options and what each costs are in the survey that produced this record; the short form is that re-opening T-146 needs a config key that breaks every configured project, and re-deriving makes the mark something computed at publication, which is what §7 says the field exists not to be. **The one measurement that shapes the fix is in §1**: `ABANDONED SLOT` reads the body and not the front matter, so the version of this that adds `adopter_visible: <yes \| no>` to the template's front matter would do nothing and look right. Checked in `check_abandoned_slots` before the option was offered. |
