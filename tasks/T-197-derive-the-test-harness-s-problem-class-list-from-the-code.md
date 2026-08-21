---
id: T-197
title: Derive the test harness's problem-class list from the code
type: fix
status: done
phase: review
parent: T-191
blocked_by: []
related: [T-151, T-139]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-21
updated: 2026-08-21
adopter_visible: no
deliverables: [tests/classes.py, tests/test_cli.py, tests/test_publishing.py]
---

# T-197 — Derive the test harness's problem-class list from the code

## 1. Specify

**Outcome**
`CheckFailsOnEveryClassItClaims.LABELS` is read from `plugin/skills/taskmd/taskmd/cli.py` rather than
transcribed into `tests/test_cli.py`, so a class added to the code is asserted silent in every
fixture but its own with nothing edited in the test file — and a class the derivation cannot see
fails a test rather than passing unnoticed.

**Why this one**
Finding **F-1** of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md).
That audit derived the class set from the code and got **21**; `LABELS` names **14**, one of which
(`CONFIG ERROR`) is not a `check` class at all. So thirteen classes get a cross-fixture silence
assertion and eight do not, and nothing anywhere compares the two lists.

**The repository already does this correctly one file over.** `tests/test_publishing.py` reads
`cli.ADVISORY_PREFIXES` from the module, which is why the advisory half of the set cannot drift.
[T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) built that home precisely so a prose list could
be checked against it. The problem half has the same need and none of the mechanism.

**The derivation this needs already exists.**
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) added `check_classes()` to
`tests/test_publishing.py` on 2026-08-21 — it reads the problem prefixes out of `cli.py`'s source and
unions them with `ADVISORY_PREFIXES`, and it is the first derivation of the problem half in the
suite. **Reuse it rather than writing a second**: two derivations of one set is the defect this task
exists to remove, arriving by the door it was watching.

**What the risk actually is.** No present assertion is wrong. The failure is in the future and is
silent: a class added to `cli.py` is never asserted absent from the other fixtures, so a check that
starts firing spuriously on an unrelated fixture is not reported by anything. That is the shape
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s rule exists to prevent.

**Scope**
- In: deriving the problem-class set in the test harness, the same way `ADVISORY_PREFIXES` is derived
- In: whether the advisory classes belong in the same cross-fixture assertion, or have their own
- Out: adding fixtures. A class with no fixture of its own is a different question, and T-191 found
  none
- Out: `CONFIG ERROR`, which is the config loader's class and not one `check` owns

**Inputs**
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) §3 — the derivation,
  the 21, and the two counts side by side
- `tests/test_cli.py` — `CheckFailsOnEveryClassItClaims`
- `tests/test_publishing.py` — `check_classes()`, the derivation to reuse, and the `ADVISORY_PREFIXES` read that is its precedent

**Acceptance criteria**
- [ ] The harness's class list is read from the code, and the derivation is the one thing a reader
      has to trust
- [ ] **The derivation is shown to fail when it should**: a class present in the code and unreachable
      by the derivation makes a test fail, demonstrated by breaking it on purpose and quoting what
      the run printed
- [ ] The count the harness uses and the count T-191 derived are stated together, and agree
- [ ] Whether the four advisory classes join the same assertion is decided, with the rejected option
      named

**Open questions**
- ~~**Should the cross-fixture assertion cover the advisory classes too?**~~ **Answered
  2026-08-21: yes, they are in.** The owner carried T-191's reasoning across — every class the
  validator prints is covered, advisory or not, because a noisy advisory trains a reader to skim the
  failing lines beside it. Covering the seventeen problem classes only was the alternative and was
  rejected. **The stated cost did not materialise and something better did**: the first run with
  advisories included failed on a false positive nobody knew about, now
  [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md).

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give the derivation one home both test files can reach, rather than importing one test module from another. | `tests/classes.py`, holding `check_classes()` moved out of `tests/test_publishing.py`. |
| 2 | Replace `CheckFailsOnEveryClassItClaims.LABELS` with that derivation, advisories included per the owner's answer. | The edited `tests/test_cli.py`. |
| 3 | Run it, and treat whatever breaks as evidence rather than as an obstacle — an advisory that legitimately fires on several fixtures is the cost the open question named. | Either a green run, or a finding. |
| 4 | Make the derivation fail on purpose: shrink what it can read and show a test says so. | The failure output, quoted. |
| 5 | State the harness's count and T-191's side by side. | Both numbers in §3. |

**Sequencing.** Step 3 before step 4, because the question the owner answered is *what happens when
advisories are in*, and the honest way to answer it is to run it rather than to reason about it.

**Decisions**

- **The derivation moves to `tests/classes.py` rather than being imported from
  `tests/test_publishing.py`.** Two test modules needing one fact is what a helper module is for; a
  test importing another test couples them by load order and breaks when either is run alone.
  *Rejected:* the import, and *rejected:* a `PROBLEM_PREFIXES` constant in `cli.py`, which is the
  truest home but changes the plugin at every append site — a change with adopter reach, and §1's
  scope puts the derivation in the test harness.

**Outputs**

- `tests/classes.py`
- `tests/test_cli.py`
- `tests/test_publishing.py`

## 3. Implement

### Steps 1–2 — one home, and a derived list

`tests/classes.py` holds `check_classes()`, moved out of `tests/test_publishing.py` where
[T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) first wrote it. Both test
modules import it. It reads the problem prefixes from `cli.py`'s source and unions them with
`ADVISORY_PREFIXES`, minus `CONFIG ERROR`, which §1 scopes out as the config loader's.

```text
$ python tests/classes.py
21 classes: ABANDONED SLOT, BROKEN LINK, CONFIG DRIFT, CYCLE, DANGLING, DUPLICATE ID,
DUPLICATE INDEX, ID WIDTH, IGNORED LINK, LABEL SHAPE, MALFORMED DATE, MISSING OUTPUT, NO BLOCKER,
PARKED TASK, SECTION REF, STALE INDEX, STORED DERIVED, TEMPLATE FIELD, TEMPLATE UNREACHABLE,
VOCABULARY, WIDE ROW
```

`LABELS` is now `sorted(check_classes())`. It was fourteen hand-typed names, one of which was not a
`check` class at all.

### Step 3 — what including the advisories cost, on the first run

**It failed immediately, and the failure was a real defect.**

```text
AssertionError: 'DUPLICATE INDEX' unexpectedly found in
  DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md ...
  DUPLICATE INDEX  tasks/T-001-second.md: a second table of 1 known task ids sits outside
  the taskmd markers
FAILED tests/test_cli.py::CheckFailsOnEveryClassItClaims::test_two_files_claiming_one_id
```

`check_duplicate_index` discounts the ids a task file is entitled to carry, and builds that discount
from `tasks`. A file that lost the duplicate-id race is not in `tasks`, so it gets no entitlement and
is judged as a document naming every known id — and with one loaded task, a majority is one. Raised
as [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md), not repaired
here (METHOD §5).

**The exception is written so that it deletes itself.** `fails()` gained an `also` argument naming
classes a fixture is known to report as well as its own — and each is asserted **present**, not
merely excused. The day T-200 lands, this test fails and the entry has to go. An exclusion that
cannot rot is the only kind worth adding to a check about exclusions.

### Step 4 — the derivation made to fail

`PROBLEM_PREFIX_RE` narrowed so it can read only one prefix. The set drops from 21 to 5, and:

```text
5 classes: CONFIG DRIFT, DUPLICATE INDEX, ID WIDTH, LABEL SHAPE, SECTION REF

AssertionError: 'DUPLICATE ID' not found in {'CONFIG DRIFT', 'LABEL SHAPE', 'SECTION REF',
  'ID WIDTH', 'DUPLICATE INDEX'} : check_classes() no longer finds 'DUPLICATE ID'
AssertionError: [] != ['plugin/skills/taskmd/docs/bindings/github-issues.md names `DUPLICATE ID`', ...]
2 failed, 182 passed
```

**Which tests failed is the part worth reading.** The cross-fixture assertions did **not** — a
shrunken `LABELS` makes them weaker, silently, exactly as a hand-typed short list did. What caught it
was the guard test held against classes the shipped bindings name, and the binding-declaration check
whose own set had not shrunk. So the derivation's failure mode is quiet by nature, and the reader
that catches it is named in `tests/classes.py`'s docstring rather than assumed.

### Step 5 — the two counts

**21 and 21.** [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) §3
derived 17 problem prefixes and 4 advisories by hand-run script; `check_classes()` derives the same
21 in the suite. The audit read `CONFIG ERROR` out by scope and so does this. Full suite: **310
passed**.

**Decisions & assumptions**

- **The advisory classes are in the cross-fixture assertion — answered by the owner on 2026-08-21**,
  on T-191's ground: a noisy advisory trains a reader to skim the failing lines beside it. Rejected:
  the seventeen problem classes only. **It paid for itself on the first run** — the one thing it
  broke was a false positive nobody knew about — 2026-08-21.
- **A known extra class is asserted present rather than skipped — rationale: an exclusion that
  passes quietly outlives the defect it was added for.** Rejected: a skip list, and rejected:
  dropping `DUPLICATE INDEX` from the derived set, which would have hidden T-200 by design —
  2026-08-21.

**Outputs produced**

- `tests/classes.py`
- `tests/test_cli.py`
- `tests/test_publishing.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The harness's class list is read from the code, and the derivation is the one thing a reader has to trust | met | `LABELS = sorted(check_classes())`, and `check_classes()` has one home in `tests/classes.py`, imported by both test modules. Its docstring says what it reads, why the two halves are read differently, and what its own failure mode is |
| **The derivation is shown to fail when it should** | met | §3 step 4: narrowed to read one prefix, the set drops 21 → 5 and two tests say so, both outputs quoted. The finding inside the finding is that the cross-fixture assertions stayed green — a shrunken set weakens them silently, which is why the guard test exists and is named in the module docstring |
| The count the harness uses and the count T-191 derived are stated together, and agree | met | **21 and 21**, in §3 step 5, from two independent derivations — the audit's hand-run script and the suite's function |
| Whether the four advisory classes join the same assertion is decided, with the rejected option named | met | **In**, by the owner on 2026-08-21; the seventeen-only option is named as rejected in §3. Recorded in `LABELS`' own comment as well, because a reader meeting the line will ask |

**This is the answer that paid for itself the same day it was given.** Including the advisories was
the option with a stated cost — an advisory firing legitimately across fixtures would make the loop
wrong rather than the fixture. That cost did not materialise. What did was
[T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md): a false positive
in `DUPLICATE INDEX` that the narrower assertion could never have seen, sitting in a fixture the
suite has run thousands of times.

**Open questions, re-read before closing.** §1's one question was the advisory one and is answered
above. §3 leaves nothing aimed at anyone else; T-200 carries the defect, and the `also=` entry
pointing at it fails the day it lands.

**Child fix tasks raised**
- [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md) — the false positive this task's answer uncovered

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-21 | → done | **Four criteria met, one child raised.** `LABELS` is now `sorted(check_classes())` from `tests/classes.py`, 21 against a hand-typed 14 - the same 21 T-191 derived independently. The owner ruled advisories in, and **the first run with them included failed on a false positive nobody knew about**, now [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md). The derivation was made to fail; the instructive part is that the cross-fixture assertions stayed green, because a shrunken set weakens them silently. |
| 2026-08-21 | → proposed | Raised as finding F-1 of [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md). `medium` and `s`: the repair is small and the mechanism already exists in `tests/test_publishing.py`, but the failure it prevents is a silently absent assertion, which is the class of defect the audit was run to find. A child of T-191 rather than a soft link, because that audit does not close until this resolves (`audit.md` step 5). |
