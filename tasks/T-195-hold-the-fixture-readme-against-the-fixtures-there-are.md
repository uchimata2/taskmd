---
id: T-195
title: Hold the fixture README against the fixtures there are
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-134, T-139, T-188]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-19
updated: 2026-08-19
adopter_visible: no
deliverables: [tests/test_publishing.py, tests/fixtures/README.md]
---

# T-195 — Hold the fixture README against the fixtures there are

## 1. Specify

**Outcome**
`tests/fixtures/README.md` names every fixture the directory holds, and a test fails when it stops
doing so.

**Why this one**
Found while reconciling after a session that added two fixtures. The README names neither, and it
already named neither of four others:

```text
abandoned-slot  label-shaped-value  malformed-date
migrated-away   section-reference   wide-table-row
```

Six unnamed, and the four oldest of them predate this session by days. **This is
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md)'s class in
the one place nobody looked**: the document a contributor reads before adding a fixture, describing a
set the tests own, with nothing comparing the two.

**And it has already drifted in the way that is hardest to see.** `planned-deliverable` and
`nested-at-root` are **both** called *the third positive case*. An ordinal is a count of the set as
it stood when the sentence was written, which is exactly what
[T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) ruled on hours earlier —
so half this task is already decided, and by a rule rather than by taste.

**Requirements served**
R-16 in spirit; `docs/SCOPE.md` §5's *humanized* constraint, since this is the document a stranger
reads to understand how the fixtures work.

**Scope**
- In: naming the six, dropping the ordinals per T-188's ruling, and a test holding the result
- In: the shape of the guard — whether the README is a marked region like the others, or whether the
  directory listing is enough on its own
- Out: writing a fixture. Every one named already exists
- Out: re-describing the fixtures that are named. Their prose is not in question
- Out: extending the guard to any other document. If the same shape exists elsewhere, that is its
  own finding

**Inputs**
- `tests/fixtures/README.md` — the document, and the collided ordinals
- `tests/fixtures/` — the set, which is the authority
- [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and
  [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  marked-region mechanism and its stated boundary
- [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) — the ordinal rule

**Acceptance criteria**
- [ ] Every directory under `tests/fixtures/` is named in the README
- [ ] A test **derives** the set from the directory, never from a list in the test, and fails when a
      fixture is added without a mention — shown failing before it is fixed
- [ ] The test fails in **both** directions: a name in the README that no directory answers is a
      failure too, or the guard cannot see a fixture that was deleted
- [ ] The collided ordinals are gone, per
      [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md)'s ruling, and no
      new ordinal replaces them
- [ ] The six added descriptions say what each fixture is **for**, not what it contains — the
      existing prose's register, and the reason the document is worth having

**Open questions**
- None. The set is the directory, the ordinal question is settled by
  [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md), and the guard's
  shape is a `plan` decision rather than an owner's.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write the guard, deriving the set from the directory and reading names out of the README | `tests/test_publishing.py` |
| 2 | Show it failing on the six | The failing run, in §3 |
| 3 | Describe the six, in the register the document already uses | `tests/fixtures/README.md` |
| 4 | Remove the two collided ordinals and the sequence that produced them | The same file |
| 5 | Run the suite | The output, in §3 |

**Decisions taken at `plan`**

- **No marked region.** The other guarded lists need one because the document mixes members with
  prose that merely mentions them; here the whole document is about the set, and a backticked
  directory name is unambiguous. *Rejected: a `taskmd:fixtures` region*, which would put markers
  around the entire file and add a mechanism to carry no distinction. — 2026-08-19
- **The guard lives in `tests/test_publishing.py`**, beside the other document guards, rather than in
  `test_cli.py` with the fixtures themselves. What it protects is a document, not behaviour.
  — 2026-08-19

**Outputs this task will produce**

- tests/test_publishing.py
- tests/fixtures/README.md

## 3. Implement

### Steps 1–2 — the guard, failing first

Three tests in `tests/test_publishing.py`, beside the other document guards. Run before the README
was touched:

```text
FAIL: test_every_fixture_is_named
tests/fixtures/README.md names no fixture called abandoned-slot, label-shaped-value,
malformed-date, migrated-away, section-reference, wide-table-row
FAIL: test_no_fixture_is_given_an_ordinal
AssertionError: [] != ['second', 'third', 'fourth', 'third']
Ran 3 tests ... FAILED (failures=2)
```

**The ordinal test's output is the finding in one line**: `second, third, fourth, third`. Two
fixtures were the third positive case, and the sequence had been hand-maintained across four
paragraphs written weeks apart.

The third test passed, and it is the one asserting the other direction — a name in the README that
no directory answers. That is a must-not-fire case which has never fired, and this record says so
rather than counting it as evidence
([`implement`](../plugin/skills/taskmd/docs/method/implement.md), *Verification*).

### Steps 3–4 — the six, and the ordinals

The six are described in one paragraph plus a list, and the paragraph says what makes them a
different shape from the `broken-*` set: **each carries its must-not-fire cases in the same
project**, which is the rule
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) wrote into the method
earlier the same day. The `broken-*` table is untouched, and the document still says of it that each
holds exactly one defect — the two claims are about different sets and both are true.

The four ordinals are gone. `alt-project` keeps a position, as *the first of the positive cases*,
because being first is a fact about it rather than a count of the set: nothing added later changes it.

### Step 5 — verification

```text
Ran 307 tests in 43.945s
OK
```

**The run before that one reported eight failures, and none of them was a defect.** The suite was
run after `T-195`'s own file was created and before `taskmd index`, so `check` reported a stale
index and every assertion about this repository's cleanliness failed behind it. That is
[T-025](T-025-let-check-notice-a-stale-generated-index.md) working: a forgotten `index` is no longer silent,
and it announces itself as eight failures rather than as one. Worth recording because the first
reading of that output was *something broke*, and it was the opposite.

**Decisions & assumptions**

- Both `plan` decisions held. — 2026-08-19
- **The reverse-direction test judges only names that look like a fixture**, because the document
  backticks plenty of other things — field values, file names, statuses. The alternative is judging
  every lowercase token, which would fail on the first paragraph that mentions `status`. The list it
  uses is a hand-kept set, and that is admitted rather than hidden: it is a **filter** on what to
  judge, not the set being judged, so it going stale weakens the reverse direction and can never
  produce a false alarm. — 2026-08-19

**Outputs produced**
- tests/test_publishing.py — `TheFixtureReadmeNamesTheFixturesThereAre`
- tests/fixtures/README.md — six descriptions, four ordinals removed

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every directory under `tests/fixtures/` is named | **met** | `test_every_fixture_is_named` passes, and it failed on six before the descriptions were written |
| A test derives the set from the directory and fails when one is added without a mention | **met** | `os.listdir` on the fixtures folder. No list of fixtures exists in the test |
| It fails in both directions | **partly met** | The reverse test exists and passes, and it has **never been made to fire**. §3 records that rather than counting it, and the filter it depends on is described in the decisions above |
| The collided ordinals are gone and nothing replaces them | **met** | `test_no_fixture_is_given_an_ordinal` holds it. `alt-project` keeps *first*, which is a fact about it and not a count |
| The six say what each is for, not what it contains | **met** | The paragraph leads with what makes them a different shape — each carries its must-not-fire cases — and the list gives each one's purpose in a sentence |

**Four met, one partly.** The partly-met row is the honest one: a must-not-fire case that has never
fired is a guard rather than evidence, which is precisely the distinction
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) ruled on hours earlier. It
is not carried to a child task because deleting a fixture to watch the test fire is a thing whoever
next deletes one can do in passing, and
[T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) already exists to
sweep for exactly this shape across the suite.

**Open questions, re-read before closing** (procedure step 5)

§1 records none and none arose. Nothing here is addressed to anyone else.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session, under the owner's extension of the eight-task grant to what the eight raise. The fixture README now names every fixture, held by a test that reads the **directory** rather than a list. It was six behind, four of them for days, and it had drifted in the way that is hardest to see: `planned-deliverable` and `nested-at-root` were **both** the third positive case, a hand-maintained sequence across four paragraphs written weeks apart. The ordinals are gone under [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md)'s ruling of the same day. **Closed with one criterion partly met and said so**: the reverse-direction test has never been made to fire, which makes it a guard and not yet evidence. |
| 2026-08-19 | → proposed | Raised during the reconcile sweep after the eight-task run, under the owner's extension of that grant to what the eight raise. Not fixed in passing: adding the two fixtures this session created would have left the four older ones and the collided ordinals, which is papering rather than repairing. `s` and `medium` — small work, and it is the document a contributor reads before touching any of it. |
