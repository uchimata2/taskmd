---
id: T-151
title: Decide whether a check needs a case that must not fire
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-100, T-141, T-150]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-15
deliverables: []
---

# T-151 — Decide whether a check needs a case that must not fire

## 1. Specify

**Outcome**
The project has an answer, written where the rule it amends is written, to whether a validator is
proven by a case it must catch alone or also needs a case it must **not** catch — and if the answer
is yes, the rule says so in one place instead of being a habit three fixtures happen to follow.

**Why this one**
Recommended by the deck-building sibling on `github.com/uchimata2/taskmd/issues/1`, 2026-08-14, in
their own words: their specimen passed while their scanner was scoring 3,150 false positives, because
it had a positive case for both checks and a negative case for only one. Their conclusion is that
noise is what gets a gate switched off, so a check moving the exit status has no tolerance for it.

**The rule this repository writes down is the positive direction only.** `CLAUDE.md` says a validator
is proven when it has been shown to **fail** on a case it is supposed to catch, and that a clean-tree
pass proves nothing. Both halves are about catching. Nothing states the other half, and the reporter's
observation is that the next person to extend a check will reach for one more positive case because
that is the only direction the rule names.

**In practice this project already does it, which is what makes the question a decision.**
`tests/fixtures/wide-table-row/` is two files, one of which exists entirely to stay quiet — five
classes that must not fire, with the test asserting an exact count so a new alarm breaks it. T-100's
*legal states do not fail* is the same idea arriving from a different direction, and it **is** written
down. So the candidate answer is that the rule exists and is scattered, rather than that it is absent.

**Evidence gathered while triaging, kept here because it is this task's subject.** A specimen carrying
all three of the reporter's traps was run against `check` on 2026-08-15:

```
skills/nested/guide.md   front matter with two `|`-separated menus   -> no alarm
skills/nested/guide.md   three table rows containing code spans      -> no alarm
skills/nested/guide.md   a ```bash run named mid-sentence            -> no alarm, and the
                                                                        table after it was scanned
examples/sample.md       a genuine wide row                          -> WIDE ROW
skills/nested/guide.md   a genuine wide row                          -> WIDE ROW
                         3 problem(s) - 4 document(s), 7 table row(s)
```

None of the three traps can arise here: `check_wide_rows` does no span detection at all, by T-141's
decision that backticks do not protect a pipe; a header is only a header when a delimiter row follows
it, which no front-matter line does; and a fence opener must start its line, so backticks named
mid-sentence open nothing. `without_code`'s `CODE_SPAN` already matches **runs** with a backreference,
which is the repair the reporter describes reaching.

**The same run corrects something they believe about us**, and it is the more useful half of this row:
`check` reads every Markdown document a clone would receive, not only tasks and the documents those
resolve. Their `skills/` and `examples/` trees are covered, so the condition they recorded as the one
that would reverse their refusal to build a checker cannot occur. The exclusions are nested taskmd
projects and anything a clone would not receive.

**Requirements served**
R-16 (`docs/SCOPE.md`); `CLAUDE.md` *Verifying*, which is the text a yes would amend.

**Scope**
- In: whether the negative case is required, recommended, or left to judgement.
- In: where a yes is written. `CLAUDE.md` *Verifying* is one candidate and is tier 1, so it is paid on
  every turn of every session; `plugin/skills/taskmd/docs/METHOD.md` and the phase files are the other,
  and they are not.
- In: whether T-100's *legal states do not fail* is the same rule under another name, in which case
  the outcome may be one home rather than a new sentence.
- Out: adding the missing negative case to the wide-row fixture, which is
  [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) and does not wait on
  this answer.
- Out: auditing every existing check for a negative case. If the answer is yes that is a real piece of
  work, and it is its own task raised from this one.

**Inputs**
- The 2026-08-14 comment on `github.com/uchimata2/taskmd/issues/1`, third section.
- `CLAUDE.md` *Verifying* — the rule as written.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) — *legal states
  do not fail*, and whether it already says this.
- `tests/fixtures/wide-table-row/tasks/T-002-three-rows-that-lose-nothing.md` — the habit, unwritten.

**Acceptance criteria**
- [ ] The answer is recorded with its rejected alternative, so the next reporter of this finds a
      decision rather than silence
- [ ] If yes, the rule has exactly one home, and the choice of tier is argued rather than assumed —
      `CLAUDE.md` charges every session for it and the method files do not
- [ ] If yes, whether the existing checks satisfy it is either answered or raised as its own task,
      not left implied
- [ ] The reporter is told what the specimen found, including the correction about coverage, since
      that changes a decision they have already taken

**Open questions**
- **Is this T-100's rule arriving from the other side?** *Legal states do not fail* is about what a
  check must not report; a negative fixture case is about proving it does not. If they are one rule,
  the outcome is a pointer and not a new sentence — and the project owner decides, because the two
  live at different tiers and the cheaper answer is the one that adds no tier-1 characters.

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
| 2026-08-18 | — | **The habit gained a fourth member, and this one followed the rule on purpose** — [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) shipped `check_abandoned_slots` with **two** must-not-fire cases in `tests/fixtures/abandoned-slot/`, and read this task at `plan` specifically to find out what the convention was. It found this record still `proposed`, so it built the negative cases against §1's *candidate answer* rather than against a decision. That is worth carrying because it is the first datum on the question's cost: following the unwritten rule took one extra fixture file and caught nothing, while **not** following it would have shipped a rule whose fenced-quotation behaviour nothing asserted. §1 is otherwise unchanged and the decision is untouched — what moved is that the practice is now four fixtures rather than three, and one of them exists because a session went looking for this task. **Not a status change.** |
| 2026-08-15 | → proposed | Raised from triaging the newest comment on issue #1, the third of its three findings and the only one that asks anything of this project. The other two are answered and need no task: their zero first run is a confirmed negative about their tree, and their three traps were run here as a specimen and none can arise — the result is in §1 because this is the task it belongs to. Filed as a `decision` rather than a fix because the practice already exists and the question is whether it earns writing down and at which tier, which is `CLAUDE.md`'s own *what earns a place here* test and the owner's to apply. `medium` because the reporter reached it by losing a specimen to exactly this gap, which is stronger evidence than an argument. |
