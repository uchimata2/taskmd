---
id: T-184
title: Report a date-shaped value that is not a date
type: fix
status: done
phase: review
parent: T-162
blocked_by: []
related: [T-146, T-106]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-19
adopter_visible: yes
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, README.md]
---

# T-184 — Report a date-shaped value that is not a date

## 1. Specify

**Outcome**
`check` reports a front-matter value that is date-shaped and is not a date, as a problem, and a test
holds it.

**Why this one**
[T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) ruled that it should, and
deliberately did not ship the code: a ruling that arrives with its implementation cannot be reviewed,
because a reader cannot tell whether the rule was adopted for being right or for being already
written. The ruling, its three rejections and the measurements behind it are in that record and are
not repeated here.

**The design in one line**: key on the **value**, never on the field name. That is what keeps the rule
clear of [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md)'s refusal and of
[T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md)'s price — it needs no config key,
because it never asks which field is a date.

**Scope**
- In: the check class, its message, and a test that fails without it.
- In: the shape the rule matches, and what it deliberately does not match.
- Out: re-opening whether to have it. That is T-162's, and it is closed.
- Out: detecting a date that is well-formed and wrong. Undetectable, and T-162 says so.

**Inputs**
- [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) §3 — the ruling, the
  probe's behaviour, and the three-corpus measurement
- `plugin/skills/taskmd/taskmd/cli.py` — where the other check classes live
- `plugin/skills/taskmd/README.md` and the advisory list — a new class may need naming there
  ([T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md))

**Acceptance criteria**
- [ ] `check` exits non-zero and names the file, the field and the value
- [ ] A test fails without the fix and passes with it — the fixture carries a malformed date, and it
      is shown failing first
- [ ] The rule reads no config key, and that is asserted rather than assumed
- [ ] Run on this repository and at least one sibling: the count is stated, and it is zero on clean
      data
- [ ] Wherever this project lists `check`'s classes, the list gains this one — the drift
      [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) exists to catch

**Open questions**
- None. T-162 settled the ruling, the form and the rejected alternatives.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the check in `cli.py`, keyed on the value: a front-matter value matching the date shape that is not a date. Wire it into `cmd_check` beside the other value-keyed walk | The `MALFORMED DATE` class, and its line in `cmd_check` |
| 2 | Build a fixture carrying the known positives, a real date that must stay silent, and a **list-valued** field — the shape that crashed T-138's check on its first real tree | `tests/fixtures/malformed-date/` |
| 3 | Show the test failing on the tree without the check, then passing with it | The two runs, quoted in §3 |
| 4 | Assert the rule reads no config key, by firing it under a field name no schema mentions | A test in `tests/test_cli.py` |
| 5 | Run `check` on this repository and at least one sibling, and state the counts | The counts, in §3 |
| 6 | Add the class to `README.md` beside the other problem classes it is written like | The README paragraph |
| 7 | Run the suite, `check` and `index` | The output, in §3 |

**Step 3 before step 5, deliberately.** T-162 measured 0 on three corpora and the zeros only meant
something because it seeded positives first; a check written today and run on the same clean tree
would reproduce that hazard exactly ([T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md)
§3 step 4).

**Decisions taken at `plan`**

- **The class is `MALFORMED DATE`, a problem, and it joins no marked list.** — `README.md` describes
  problem classes one at a time and never claims to describe all of them, which is why the sixteen
  problem prefixes carry no `taskmd:` region while the three advisories do
  ([`tests/test_publishing.py`](../tests/test_publishing.py), `EveryMarkedListNamesTheSetTheCodeOwns`).
  *Rejected: adding a `taskmd:problems` region so the guard covers it* — that asserts a completeness
  the document does not mean, and it is a change to T-139's ruling rather than to this class. — 2026-08-19
- **The fixture carries a list-valued field.** — *Rejected: scalars only*, which is what
  `label-shaped-value` shipped first: three behaviours passed while the check crashed on the first
  real tree it met. — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/malformed-date/
- tests/test_cli.py
- README.md

## 3. Implement

### Step 3 — the test, shown failing before the check existed

The fixture and the nine tests were written first, and run against a tree with no `check_dates` in
it:

```text
FAIL: test_it_reads_the_shape_and_never_the_field_name
AssertionError: 'reviewed_on' not found in "OK - 2 task(s), 2 field value(s), ... 14 front-matter value(s)
FAIL: test_one_line_per_malformed_value
AssertionError: 0 != 4
Ran 9 tests ... FAILED (failures=5, errors=1)
```

`OK` over `updated: 2026-13-99`, which is [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md)'s
silence reproduced a third time, on a corpus written for this task. The single error is
`check_dates` not existing, which is the test that reads the function's own source.

### The check, and what the fixture prints

```text
MALFORMED DATE T-001-the-accident-that-found-this.md: updated is '2026-08-165', which is shaped like a date and is not one
MALFORMED DATE T-002-a-month-and-a-day-that-do-not-exist.md: reviewed_on is '2026-08-161', which is shaped like a date and is not one
MALFORMED DATE T-002-a-month-and-a-day-that-do-not-exist.md: updated is '2026-13-99', which is shaped like a date and is not one
MALFORMED DATE T-002-a-month-and-a-day-that-do-not-exist.md: windows is '2026-02-30', which is shaped like a date and is not one

4 problem(s) - 2 task(s), ...
EXIT=1
```

Four values, four fields, one of them a list member and one of them under `reviewed_on`, **a field
name no config in that project mentions**. Silent in the same run: `2026-08-18`, `2026-08-01`, and
`2026-8-5`, which is a real date written without zero padding.

### Step 5 — the corpora

| Corpus | Tasks | Front-matter values | `MALFORMED DATE` |
| :--- | ---: | ---: | ---: |
| this repository | 187 | 3,144 | **0** |
| the deck-building sibling | 185 | not counted | **0** |
| the diagram sibling | 7 | not counted | **0** |

The other two siblings hold no local task folder and answer `CONFIG ERROR` before any check runs, so
they are not corpora for this and are not counted as clean ones.

**The zero on this repository is only worth reading because of the seed.** `updated: 2026-08-11`
became `2026-08-115` in one real task file:

```text
MALFORMED DATE T-093-decide-whether-check-resolves-a-section-reference.md: updated is '2026-08-115', which is shaped like a date and is not one
1 problem(s) - 187 task(s), ...
EXIT=1
```

Reverted with `git checkout` immediately afterwards.

### Step 7 — the suite, `check` and `index`

```text
Ran 288 tests in 20.952s
OK
Wrote tasks/README.md - 15 active, 172 closed
OK - 187 task(s), 935 field value(s), 3144 front-matter value(s), ...
```

No skips. The handoff of 2026-08-19 said the suite reports three on this shell; it reported none, on
Python 3.12 through the Bash tool, and the line it was written on said to re-run rather than trust it.

**The suite caught two things the change broke**, which is the point of running it rather than the
new tests alone:

- `README.md`'s quoted `check` transcript no longer matched the command. `examined` merges
  denominators **in the order the checks ran**, so wiring `check_dates` in second moved
  `front-matter value(s)` up the summary line. Regenerated by running the command the test runs,
  never by editing the line.
- Two lines of the new README paragraph carried em dashes, which
  [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §2 forbids in covered text. Rewritten rather than
  substituted, as that section requires.

**Decisions & assumptions**

- **The value is validated by handing its three components to `datetime.date`, not to
  `date.fromisoformat`.** T-162's probe used `fromisoformat`, and that was right for a probe and
  wrong for shipped code: before Python 3.11 it rejects `2026-8-5` and from 3.11 it accepts it, so
  the class would mean something different on different interpreters. `datetime.date(2026, 8, 5)`
  answers the same everywhere. *Rejected: `fromisoformat`, matching the probe exactly* — it would
  make a real date fail on one interpreter and pass on another, and neither the ruling nor the class
  name claims anything about zero padding. It moves no measurement: this repository holds no unpadded
  date-shaped value, so both readings score 0 here. — 2026-08-19
- **The message names the file rather than the task id**, unlike `VOCABULARY` beside it. The
  acceptance criterion asks for the file, and it is the right half: a malformed value can sit in a
  file whose id never loaded. — 2026-08-19
- **Assumption, recorded as one**: the two sibling corpora are the same person's, so the
  false-positive evidence is no wider than T-162's was, and T-162 recorded the same limit. An
  adopter's corpus is what would widen it. — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/taskmd/cli.py
- tests/fixtures/malformed-date/.taskmd/config.md
- tests/fixtures/malformed-date/tasks/T-001-the-accident-that-found-this.md
- tests/fixtures/malformed-date/tasks/T-002-a-month-and-a-day-that-do-not-exist.md
- tests/test_cli.py
- README.md

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `check` exits non-zero and names the file, the field and the value | **met** | §3: exit 1, and each line carries all three. It names the file rather than the id, and §3 records why |
| A test fails without the fix and passes with it, the fixture carrying a malformed date, shown failing first | **met** | §3 step 3 quotes the failing run: 5 failures and 1 error on a tree with no `check_dates`. Nine pass with it |
| The rule reads no config key, asserted rather than assumed | **met** | `test_it_reads_no_config_key` reads the function's own source and fails if it touches `schema.`. The fixture also fires under `reviewed_on`, which no config names |
| Run on this repository and at least one sibling, count stated, zero on clean data | **met** | §3 step 5: 0 on 187 tasks here, 0 on 185 and 0 on 7 in two siblings. The seeded positive is what stops those zeros being vacuous |
| Wherever this project lists `check`'s classes, the list gains this one | **met** | `README.md` gains a paragraph beside `WIDE ROW` and `ABANDONED SLOT`, which is how problem classes are written there. It joins no marked region, and §2 records why: the problem prefixes carry none, because that document never claims to describe all of them |

**Open questions, re-read before closing** (procedure step 5)

§1 recorded none, and none arose. Nothing here is addressed to anyone else.

**One finding, outside this task's criteria and raised rather than fixed.**
[`tests/test_publishing.py`](../tests/test_publishing.py) line 244 says *the fifteen problem
prefixes* while arguing why they carry no marked region. There were **sixteen** before this task and
there are now **seventeen**, so the number was already wrong when it was read. The argument it
supports is untouched; the count inside it is a derived value written down. Raised as
[T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) rather than corrected
here, because a review that repairs what it finds destroys the record of what was wrong
(METHOD §5), and because the interesting half is the class and not the word.

**Child fix tasks raised**
- [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) — a counted set written into prose that the code owns

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 1 of the eight. **`check` now reports `MALFORMED DATE`**, keyed on the value exactly as [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) ruled: it reads no config key, fires under a field name no schema mentions, and reads list members as well as scalars. Written test-first and quoted failing before the check existed, which is the step that stops the zeros meaning nothing: 0 on this repository's 187 tasks and 3,144 front-matter values, 0 on two sibling corpora, and 1 the moment a real value here was corrupted. One decision diverges from T-162's probe and says so — `datetime.date` rather than `date.fromisoformat`, because the latter answers differently before and after Python 3.11. The suite caught two breakages the new tests could not: a README transcript the changed denominator order falsified, and two em dashes the publishing gate forbids. One finding raised rather than fixed: [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md). |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 1 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). The authorisation of earlier the same day, which covered this task alone, is superseded by this one rather than added to. |
| 2026-08-19 | (no change) | **The owner authorised this task to start**, on 2026-08-19, answering the backlog-wide question round the handoff of that date asked for. The authorisation covers **this task only** and nothing it raises. Recorded here rather than only in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). Nothing else changes: T-162's ruling, form and rejections stand as written, and this row is permission rather than an answer, because §1 records no open question. |
| 2026-08-18 | → proposed | Raised by [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md)'s review. The ruling is made and measured; this is the code. Kept separate on purpose — T-162 §2 records the reason as a `plan` decision rather than discovering it at close. Outside the standing grant of 2026-08-18, which covers the six named tasks and **nothing any of them raises**. |
