---
id: T-123
title: Decide whether a replaced vocabulary row is drift or a choice
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-082]
work_package: v0.2
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/schema.py, plugin/skills/taskmd/taskmd/defaults/config.md, tests/test_cli.py, tests/fixtures/README.md]
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
- ~~Whether a third answer is better than either: report the row as *replaced* rather than as
  *behind*, saying what the tool actually knows.~~ **Answered in `specify`, 2026-08-11: no** — see
  D2 in §2. The decision the task exists to take is D1, also in §2.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what the tool can actually distinguish, from the two rows it holds, rather than from what the message says. | Recorded in §3: what a wholly replaced row makes the current line print |
| 2 | Narrow the comparison to a row that still carries at least one of the shipped values. | `drift_from_default` in `plugin/skills/taskmd/taskmd/schema.py` |
| 3 | Say in the shipped config what *a row you still keep* means, so the code and its one description agree. | The `## When this file moves ahead of yours` paragraph in `plugin/skills/taskmd/taskmd/defaults/config.md` |
| 4 | Add the wholly-replaced row to the negative cases that already carry this rule, and show the positive case still fires. | A test in `tests/test_cli.py`'s `APinnedConfigIsToldWhenTheDefaultMovesOn` |
| 5 | Stop `tests/fixtures/README.md` deferring here, and say what the fixture now prints. | `tests/fixtures/README.md` |
| 6 | Run `check` on the fixture — criterion 1 is about a run, not about the diff. | Recorded output |
| 7 | `check`, `index` and the whole suite at the repository root. | Recorded output |

**Shape decisions.**

**D1 — A row that shares no value with the shipped one is a replacement, and is not reported.**
Drift is reported only where the project's row still carries at least one of this file's values.
That is what makes *behind* a meaningful word: a row with one foot in the shipped vocabulary can lag
it; a row with none has left it. *Rejected: leave the code and widen the config's description to
admit the shape.* It costs every issue-tracker adopter an advisory line, on every run, for a decision
they took deliberately and cannot switch off — `open`/`closed` is what a backend gives you, so this
is the commonest way to adopt, not an edge. And the paragraph that would have to be widened is the
one stating the design's own principle: reporting choices makes a configured project noisy from its
first run.

**D2 — Not a second message shape saying *replaced*.** The third answer is honest about what the tool
knows, and it still prints a line about a choice on every run of every issue-tracker project —
failing on the same ground as the rejected option above, while adding a message shape to maintain.
There is nothing for such a project to do with the line: it did not fall behind, and the values it
would be told about belong to a vocabulary it does not use.

**What D1 costs, stated where it can be checked.** A project that renamed *every* shipped value and
is genuinely behind on a new one is no longer told. The loss is smaller than it sounds and the
current output is why: the line for such a row already lists the **entire** shipped vocabulary — step
1 shows all eight statuses named — so it never distinguished the new value from the seven the project
had deliberately dropped. What is suppressed is not a signal about a ninth value; it is a dump of a
vocabulary the project stopped using. A row keeping even one shipped value still reports.

**Planned outputs**
- plugin/skills/taskmd/taskmd/schema.py
- plugin/skills/taskmd/taskmd/defaults/config.md
- tests/test_cli.py
- tests/fixtures/README.md

## 3. Implement

### Step 1 — what the line actually said

```
CONFIG DRIFT  status: shipped default adds 'proposed', 'specified', 'planned', 'in_progress',
'blocked', 'review', 'done', 'cancelled'; this project's row does not carry them
```

**All eight**, which is the whole shipped vocabulary. That is the fact the decision turns on: the
report for a wholly replaced row was never naming a value the project had fallen behind on, because
there is no value it kept to fall behind *from*. It was listing a vocabulary the project had stopped
using. So the choice was not between a signal and silence — it was between silence and a dump.

### Steps 2–3 — the code and its one description

`drift_from_default` gains one clause: a row is compared only if the project's row still carries at
least one shipped value. The shipped config's `## When this file moves ahead of yours` says what
*you still keep* means, since that sentence was already there and was already the rule — the code had
simply been reading it as *the field name survives*. The comment in `schema.py` points at the config
rather than repeating it.

### Step 4 — the boundary from both sides

Two tests, in the class that already carries this rule's negative cases:

- `test_a_wholly_replaced_row_is_not_behind` — `status: open, closed`, no drift line;
- `test_one_kept_value_is_enough_to_bring_the_reporting_back` — `status: open, closed, blocked`,
  which **does** report, names `'done'`, and does not name the `'blocked'` it kept.

**The negative case was shown to fail before it was made to pass.** With the clause reverted:

```text
FAIL: test_a_wholly_replaced_row_is_not_behind
AssertionError: 'CONFIG DRIFT' unexpectedly found in "OK - 1 task(s) … CONFIG DRIFT  status:
shipped default adds 'proposed', … ; this project's row does not carry them …"
```

The second test passes on both sides of the change, and that is its job: it is falsified by an
over-broad fix — one that stopped comparing the row at all, or keyed on "most values missing" — not
by the absence of this one. A suppression proved only by the case it suppresses cannot tell those
apart.

**Replacing a vocabulary row costs three edits, not one, and the tests had to learn that.** Setting
`status` to `open, closed` makes `open_statuses`, `blocked_status` and every task's own `status`
invalid, and `check` then exits 2 on the config before drift is ever printed. The scratch helper now
edits all of them, so the advisory is read off a **passing** run — the one output these tests must
not be coupled to. The committed fixture had this right already; the test that reached for the same
shape did not.

### Steps 6–7 — the runs

The fixture, which criterion 1 is about:

```text
OK - 3 task(s), 3 field value(s), 3 reference(s), 1 dependency edge(s), 0 declared output(s),
     0 index file(s), 4 document(s), 0 link(s), 0 template(s), 0 template field value(s),
     1 vocabulary row(s)
Scope  0 document(s) not read: a clone would not receive them
```

**No `CONFIG DRIFT` line, and `1 vocabulary row(s)` still compared** — the row was read and judged,
not dropped from the walk. A suppression that had removed it from the count would have been the
wrong fix wearing the right output.

Repository root:

```text
Wrote tasks/README.md - 13 active, 110 closed
OK - 123 task(s), 615 field value(s), 391 reference(s), 22 dependency edge(s), 205 declared
     output(s), 1 index file(s), 151 document(s), 1236 link(s), 2 template(s), 10 template field
     value(s), 0 vocabulary row(s)
```

Suite, one process per module: `test_cli` **94** OK (92 before, plus these two), `test_list` 35 OK,
`test_schema` 53 OK, `test_budget` 5 OK, `test_runtime` 27 `OK (skipped=3)` — the shell skips T-114
made legible, not failures.

**Decisions & assumptions**
- **D1 — a row sharing no value with the shipped one is a replacement and is not reported** —
  2026-08-11. Rationale and the rejected alternative are in §2, where the decision is.
- **D2 — no second message shape saying *replaced*** — 2026-08-11, §2.
- **The narrowing can only remove a line, never add one** — so no adopter tree that passes today can
  start failing on it, and it is not a third surprise class for the pending manifest bump.
- **Assumption: `check`'s exit status is unaffected.** Drift was already advisory, and the change is
  inside the advisory's own producer; `test_it_is_advisory_and_does_not_move_the_exit_status` still
  passes and covers it.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/schema.py`](../plugin/skills/taskmd/taskmd/schema.py)
- [`plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)
- [`tests/test_cli.py`](../tests/test_cli.py)
- [`tests/fixtures/README.md`](../tests/fixtures/README.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Running `check` on `tests/fixtures/backend-allocated-ids` either prints no `CONFIG DRIFT` line, or prints one the shipped config's own description covers | met | §3 step 6: no drift line, exit 0, and `1 vocabulary row(s)` still compared — judged from the run, not from the diff |
| The decision names what it costs — a project that both renamed its values and is behind on a new one, if the report is narrowed; noise on every issue-tracker project, if it is not | met | §2 states both, and the cost of the option taken is stated where it can be checked rather than asserted: step 1 quotes the line that named all eight values, which is why what is suppressed is a dump and not a signal |
| `tests/fixtures/README.md` no longer defers to this task | met | It now states the settled rule and names the fixture as its standing case; the link remains, pointing at where the reasoning lives |

**What the review turned up and kept inside the task.** The scratch-project helper could only make
one config edit, so a test replacing the `status` row produced a `CONFIG ERROR` and would have been
reading the drift line off a failing check. Fixed here rather than raised: it is this task's own test
code, and the alternative was a passing assertion resting on the wrong run.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All three criteria met, no child raised. **The decision turned on one line of output rather than on the argument.** The report for a wholly replaced row named *all eight* shipped statuses — the whole vocabulary — so narrowing it does not lose a signal about a ninth value; it removes a dump of a vocabulary the project deliberately stopped using. That is what makes the stated cost of D1 smaller than it reads, and it is quoted in §3 step 1 rather than asserted. Two things worth carrying. **The negative case was made to fail before it was made to pass**, with the clause reverted, because a suppression proved only by the case it suppresses cannot be told from one that stopped comparing the row at all — and the count `1 vocabulary row(s)` on the fixture is the other half of that, showing the row is still judged. **Replacing a vocabulary row costs three edits, not one**: `open_statuses`, `blocked_status` and every task's own `status` all become invalid, and `check` exits 2 on the config before the advisory is ever reached, so the first two attempts were reading the drift line off a failing run. The committed fixture already had this right; the test reaching for the same shape did not. |
| 2026-08-11 | → planned | **Authorisation, recorded here and not inherited from a note (METHOD §3.1).** The maintainer gave *work every open `v0.2` task through its full lifecycle — specify, plan, implement, review, fix, commit and push, one task at a time* on 2026-08-10, re-confirmed and widened on 2026-08-11 to *multiple tasks until you need to stop*, and again the same day to **the remaining tasks, full lifecycle, continuously**. It covers this task end to end and nothing outside the open `v0.2` set. `specify` needed one thing: its open question, which the task itself said to answer here. **Answered no** (D2) — the third shape is honest and still prints a line about a choice on every run, which is the ground the other option loses on. **The decision is D1**: a row sharing no value with the shipped one is a replacement rather than a lag, and is not reported. The alternative it beat is not a strawman — leaving the code and widening the shipped config's description is the smaller change, and it was rejected because the paragraph it would widen is the one stating the principle that reporting choices makes a configured project noisy from its first run. Both rejections are recorded in §2 where the decision is, per the standing rule for delegated owner-questions. |
| 2026-08-11 | → proposed | Raised from T-082, which met it while building a fixture and did not fix it there (METHOD rule 4). **Filed `v0.2` by `tasks/README.md`'s rule** — a minor-to-moderate correction, blocking nothing — and that brings it inside the standing v0.2 full-lifecycle authorization, which is a consequence of the filing rule and not a grant. The task that raised it did not start it. Worth knowing before it is worked: the evidence is already committed and passing, so nothing regresses while this waits; what waits is one advisory line that every issue-tracker adopter will see and have to ask about. |
