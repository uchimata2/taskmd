---
id: T-151
title: Decide whether a check needs a case that must not fire
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-100, T-141, T-150]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-15
updated: 2026-08-19
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/method/implement.md]
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
- ~~**Is this T-100's rule arriving from the other side?** *Legal states do not fail* is about what
  a check must not report; a negative fixture case is about proving it does not. If they are one
  rule, the outcome is a pointer and not a new sentence — and the project owner decides, because the
  two live at different tiers and the cheaper answer is the one that adds no tier-1 characters.~~
  **Answered 2026-08-19 under a delegation from the owner: one rule, reached by a pointer, and the
  pointer carries a condition** — the Log row of that date holds the two findings that narrowed it
  and the home the pointer cannot assume.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read both candidate homes and say which already states the positive half, since the negative half belongs beside it rather than anywhere it would read as a new topic | The home, decided in §3 |
| 2 | Write the rule once, with the condition the Log row of 2026-08-19 attached to it | The edited method file |
| 3 | Answer criterion 3 — whether the existing checks satisfy the rule — or raise it as its own task, per §1's *Out* | An answer or a task |
| 4 | Confirm criterion 4 against the thread rather than by writing to it again | The verdict, in §3 |
| 5 | Run the suite, `check` and `index`, and the budget test in particular | The output, in §3 |

**Decisions taken at `plan`**

- **The home is [`plugin/skills/taskmd/docs/method/implement.md`](../plugin/skills/taskmd/docs/method/implement.md),
  not `CLAUDE.md`.** The negative half binds when somebody is building or extending a check, which is
  an activity a session knows it has started — and `CLAUDE.md`'s own *What earns a place here* says
  tier 1 then carries a pointer and never the thing. The method file already states the positive half
  in the same list and the same register, so this completes a paragraph rather than opening a home.
  *Rejected: `CLAUDE.md` Verifying*, which is the other candidate §1 names: it charges every turn of
  every session for a rule that binds during one phase, and `tests/test_budget.py` measures exactly
  that cost. *Rejected: a new document*, which would make three homes for one idea. — 2026-08-19
- **`CLAUDE.md` is not edited at all**, in either direction — nothing added, and the sentence it
  already carries not removed. Removing it is a defensible change and a **different** one, and it
  turns out to have a second reason behind it that this task discovered rather than assumed; see §3
  and [T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md).
  — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/docs/method/implement.md

## 3. Implement

### Step 1 — where the positive half already is, which decides the question

Both candidate homes state it, which is the fact the plan decision turns on:

| Home | Tier | What it already says |
| :--- | :--- | :--- |
| `CLAUDE.md` *Verifying* | 1, paid on every turn of every session | *a validator is only proven when it has been shown to fail on a case it is supposed to catch* |
| `plugin/skills/taskmd/docs/method/implement.md` *Verification* | 3, paid when the phase is loaded | *A check that has only ever succeeded has not been tested* |

The negative half completes the second bullet of a two-bullet list in the method file. Putting it in
`CLAUDE.md` would state one idea at two tiers and charge the more expensive one for it.

### Step 2 — the rule, as written

The list stops being introduced as *two rules* — that count is exactly the shape
[T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) was raised about, and
there was no reason to add an instance of it while adding a bullet — and gains:

> **A check also needs a case it must *not* catch, and that case has to be shown able to fire.**
> Noise is what gets a check switched off, so a check that moves an exit status has no room for it —
> and a case that stays quiet proves nothing until you know it *could* have spoken.

**The condition is the half that was argued for**, and it is there because this project has watched
the unconditioned version fail twice: [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md)
§3 shipped four tests that pass by asserting silence and calls them guards rather than evidence, and
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) §3 found the obvious
two-line negative fixture **cannot** fire at all. A rule reading only *also add a negative case*
licenses both.

### Step 3 — criterion 3, raised rather than answered

Whether the seventeen problem classes each have a must-not-fire case is a real piece of work over a
real corpus, and §1's *Out* says so in advance. Raised as
[T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md). Not answered here by
sampling: a sampled answer to *do the existing checks satisfy this* is the vacuous-pass shape the
condition above exists to refuse.

### Step 4 — criterion 4, met by the thread and not by writing to it

The reporter has already been told, in the exchange this task was raised from. The public thread
carries this project's reply naming what the specimen found and this task's id, and then the
reporter's own comment: *Correction accepted, and reproduced here before accepting it* — they
re-ran it in their tree before agreeing, and moved their reversing condition to something else. So
the criterion is satisfied by what happened, and **posting again would be a second telling of a fact
already received**, on a thread both sides have recorded as too long.

### Step 5 — verification

```text
Ran 288 tests ... OK
tier 1 6380 chars under by 1466 (bound 7846, reference/TASK-WORKFLOW.md)
Wrote tasks/README.md
OK - ... task(s) ...
```

**Tier 1 is unchanged, and that is the measurable half of the home decision** — the same 6,380
characters as before this task, because nothing was added to a file a session pays for.

**Decisions & assumptions**

- **One rule, one home, with a condition.** A check needs a case it must not catch, *and* that case
  must be shown able to fire. — 2026-08-19
- **Both `plan` decisions held.** — 2026-08-19
- **The premise §1 opens with is corrected rather than carried.** §1 reads T-100's *legal states do
  not fail* as this rule already written down. It is not: in both places it appears it is the
  rationale for one advisory line not moving the exit status. The delegation's Log row of 2026-08-19
  had already narrowed this, and the outcome follows it — the rule is written, not pointed at.
  — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/docs/method/implement.md — the *Verification* list

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The answer is recorded with its rejected alternative | **met** | §2 and §3. Rejected: a bare pointer with no condition, `CLAUDE.md` as the home, a new document, and two separate rules — the last two in the Log row of 2026-08-19 |
| The rule has exactly one home, and the tier is argued rather than assumed | **met** | `implement.md` *Verification*, argued against `CLAUDE.md`'s own *What earns a place here* test and measured: tier 1 is unchanged at 6,380 characters |
| Whether existing checks satisfy it is answered or raised, not left implied | **met** | Raised as [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), which is what §1's *Out* said it would be. §3 step 3 says why it was not sampled instead |
| The reporter is told, including the coverage correction | **met** | §3 step 4, and the evidence is the reporter's own reply accepting the correction after reproducing it. Judged against the thread rather than by writing to it a second time |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered under the owner's delegation on 2026-08-19 and is struck through
there. Nothing here is addressed to anyone else.

**One finding, outside this task's criteria and raised rather than fixed.** Choosing between the two
homes meant reading both, and both carry the positive half — and the *other* rule beside it, *state
the result not the verdict*, is in both as well. `CLAUDE.md` says it carries **exactly two** of the
method's rules, §3.1 and §3.3, and that this is *not an exception to the rule but the only way to
obey it*, because those two bind before the method loads. These two do not. So tier 1 restates two
method rules the project's own account of tier 1 does not allow for. Not touched here — §1's scope is
where the *negative* half goes, and removing text from tier 1 is a change the owner should see
argued on its own. Raised as
[T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md).

**Child fix tasks raised**
- [T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md) — tier 1 restating two rules the method owns
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) — whether the existing checks satisfy the rule this task wrote

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 4 of the eight. **Ruled: a check needs a case it must not catch, and that case has to be shown able to fire.** The condition is the part that was argued for, and it is what stops the rule licensing the two failures this project has already measured — T-100's four tests that pass by asserting silence, and T-150's negative fixture that could not fire at all. **One home, and it is tier 3**: `implement.md`'s *Verification* list, where the positive half already sits in the same register. `CLAUDE.md` gains nothing and loses nothing, and the budget test shows tier 1 unchanged at 6,380 characters — which is the home decision measured rather than asserted. Two findings raised rather than fixed: [T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md), because choosing between the homes exposed that tier 1 restates two method rules its own account says it may not, and [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), which §1 had already said would be its own task. |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 4 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered: one rule, reached by a pointer — and the pointer cannot be a bare one.** The owner delegated the call on 2026-08-19, conditional on reading the report and the rule first, with *one rule, add a pointer* as the answer if nothing further turned up. Something further did, and it survives the delegation because it narrows the outcome rather than reversing it. **Two findings.** *First, the premise that the negative half is already written down is weaker than §1 reads.* `legal states do not fail` exists in exactly two places — [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) §1/§3, and `plugin/skills/taskmd/taskmd/defaults/config.md` — and in both it is the **rationale for one advisory line not moving the exit status**, never a rule about validators. So a pointer has nothing rule-shaped to point at, and `specify` decides the home rather than assuming one exists. *Second, and the reason a bare pointer is refused:* **a negative fixture passes vacuously far more easily than a positive one, and this project has measured that twice.** T-100 §3 shipped seven tests of which four pass by asserting silence, and the record calls them "guards rather than evidence"; [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) §3 found the obvious two-line fixture *cannot* fire, because `check_wide_rows` consumes the line under its header as the delimiter. A rule that says only *also add a negative case* licenses exactly those. So the rule carries the condition that a negative case counts only once it has been shown it **can** fire. *Rejected: a bare pointer with no condition* — cheaper by a clause and it authorises the two failures above. *Rejected: two separate rules* — it doubles a tier-1 cost for one idea, which is the option the owner's answer already set aside. |
| 2026-08-18 | — | **The habit gained a fourth member, and this one followed the rule on purpose** — [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) shipped `check_abandoned_slots` with **two** must-not-fire cases in `tests/fixtures/abandoned-slot/`, and read this task at `plan` specifically to find out what the convention was. It found this record still `proposed`, so it built the negative cases against §1's *candidate answer* rather than against a decision. That is worth carrying because it is the first datum on the question's cost: following the unwritten rule took one extra fixture file and caught nothing, while **not** following it would have shipped a rule whose fenced-quotation behaviour nothing asserted. §1 is otherwise unchanged and the decision is untouched — what moved is that the practice is now four fixtures rather than three, and one of them exists because a session went looking for this task. **Not a status change.** |
| 2026-08-15 | → proposed | Raised from triaging the newest comment on issue #1, the third of its three findings and the only one that asks anything of this project. The other two are answered and need no task: their zero first run is a confirmed negative about their tree, and their three traps were run here as a specimen and none can arise — the result is in §1 because this is the task it belongs to. Filed as a `decision` rather than a fix because the practice already exists and the question is whether it earns writing down and at which tier, which is `CLAUDE.md`'s own *what earns a place here* test and the owner's to apply. `medium` because the reporter reached it by losing a specimen to exactly this gap, which is stronger evidence than an argument. |
