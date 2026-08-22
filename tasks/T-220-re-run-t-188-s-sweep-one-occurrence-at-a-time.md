---
id: T-220
title: Re-run T-188's sweep one occurrence at a time
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-188, T-212, T-139]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-22
updated: 2026-08-22
adopter_visible: no
deliverables: []
---

# T-220 — Re-run T-188's sweep one occurrence at a time

## 1. Specify

**Outcome**
Every place in the live tree that writes a count of a code-owned set into prose is judged **on its
own**, not through a verdict given to the file it sits in — so it is known whether T-188's *everything
else drops the number* left anything behind, and whatever it left is repaired.

**Why this one**
Found on 2026-08-22 by the reconcile sweep at the end of the eight-task session, while checking what
[T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) had made stale.

[T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) ruled that **a count of
a set the code owns is either dated as a measurement or not written at all**, swept for them, and
recorded the result as a table of **one row per file**. `github-issues.md` got one row — the dated
blockquote — with the verdict *dated, needs no guard*. That file held a **second** count of the same
set, undated:

```text
Seventeen checks run on the local backend. Nine land here as rows above, and four cannot occur at all.
```

The row's verdict was right about the sentence it named and licensed leaving the other, so
*Everything else drops the number. Six did* was short by one. T-212 hit that sentence on 2026-08-22
by adding a check, and applied T-188's own ruling to it — deleted, not bumped.

**The ruling was never at fault. The unit was.** A survey that classifies a **file** cannot see a
second occurrence inside it, and nothing about the finding announces that: one row per file reads as
complete.

**Scope**
- In: re-running T-188's own sweep command and judging **every hit**, one at a time
- In: stating the corpus and every exclusion, with the count each removes, so the classes sum
- In: repairing whatever the per-file verdict hid
- Out: **changing the ruling**, or adding the mechanical rule T-188 priced and rejected. This asks
  whether the ruling was applied, not whether it is right
- Out: task records. They are records of their day, and the partition below shows they hold no live
  claim — see the membership check in §3, which is why this is an exclusion rather than a hope

**Inputs**
- [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) §3 — the sweep
  command, the eight-row table, and the ruling with its two exemptions
- [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) §3 decision 5 — the missed
  occurrence, found by falsifying it

**Acceptance criteria**
- [ ] The sweep is re-run with T-188's own command, and its **corpus is reported** — how many files
      it read and how many hits it produced
- [ ] Every exclusion is named with the number of hits it removes, and the excluded and included
      counts **sum to the total**
- [ ] Every hit in the included set is classified, and the classes sum to that set
- [ ] Anything the per-file verdict hid is repaired, or the record says there was nothing
- [ ] The suite and `check` are green, and the output is quoted

**Open questions**
- **None.** The ruling is settled and is not under review here.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Re-run T-188's command over the tracked tree and count the hits. | The command and the totals in §3 |
| 2 | Partition the hits by where they sit, and check the parts sum. | The partition in §3 |
| 3 | For the one exclusion that could hide a live claim — task records — **check membership rather than trust the total**: no open task may carry a hit. | The membership check in §3 |
| 4 | Classify every hit in the included set, one at a time, into T-188's own classes. | The classification in §3, summing to the set |
| 5 | Repair whatever comes out as a live undated count. | The edits |
| 6 | Run the suite and `check`. | Their output in §3 |

**Shape decision — the corpus is `git ls-files`, which is T-188's own.** Using a different corpus
would measure a different thing and could not be compared with what that task did. **Rejected:
widening it to untracked files**, which would pull in `control/` and `.handoff/` — not shipped, and
not what the ruling is about.

**Step 3 exists because step 2 cannot do its job alone.** A partition that sums is still wrong if a
part was defined by the wrong property; the excluded 438 are excluded because a closed record states
its own day, and the thing that would break that is an **open** task carrying a hit.

**Outputs**
- tests/test_cli.py
- tests/test_publishing.py

## 3. Implement

**Step 1 — the sweep, with its corpus**

```text
$ git ls-files | wc -l
359
$ git ls-files -z | xargs -0 grep -nIE "\b(two|three|...|twenty|[0-9]+) (advisor|check|command|problem|prefix|class|option|flag|vocabular|edge kind|phase)" | wc -l
471
```

**Step 2 — the partition**

| Where | Hits | Why it is set aside |
| :--- | --: | :--- |
| `tasks/` | 438 | A record states what was true on its day; METHOD rule 5 forbids rewriting that |
| `docs/audits/` | 2 | Both dated measurements, which is the ruling's own second exemption |
| `reference/` | 1 | The pre-split standard from another project — evidence, not a shipped document |
| **live** | **30** | Judged one at a time below |

438 + 2 + 1 + 30 = 471.

**Step 3 — the membership check the total cannot do**

```text
$ for id in T-176 T-182 T-199 T-213; do <sweep> | grep "^tasks/$id"; done
(no output)
```

Those four are every open task in the project. **None carries a hit**, so the 438 set aside really
are closed records, and the exclusion drops no live claim. Without this the partition would sum
perfectly and still be wrong.

**Step 4 — the 30, classified one at a time**

| Class | Hits | What they are |
| :--- | --: | :--- |
| **Fixed by a recorded decision** | 15 | *four commands* (`docs/SCOPE.md` non-goal 11), *four phases*, *three edge kinds*, and the *three of the four commands* forms derived from them — `SCOPE.md` 184; `github-issues.md` 455, 579, 600; `local-markdown.md` 156; `cli.py` 2, 12, 1484, 1645; `schema.py` 700, 722; `test_cli.py` 1108, 1119, 1120; `test_publishing.py` 310 |
| **Not a count of a code-owned set** | 12 | The number restates a list the sentence itself names — *the two commands* being `check` and `index`, *those three flags* named beside it — or it is literal command output, or an assertion on a fixture's own output: `.handoff/config.md` 172; `CLAUDE.md` 96; `README.md` 157; `PUBLISHING.md` 224; `adopt.md` 41; `HANDOFF.md` 105; `tests/fixtures/README.md` 81; `test_cli.py` 1301, 1542, 1755, 1765, 2036 |
| **Dated measurement** | 1 | `github-issues.md` 626, the blockquote opening *measured 2026-08-18* — the row T-188's table did name |
| **Live, undated count of a code-owned set** | 2 | `tests/test_cli.py` 2 and `tests/test_publishing.py` 355 — repaired in step 5 |

15 + 12 + 1 + 2 = 30.

**Step 5 — the two repairs**

- `tests/test_cli.py`'s module docstring opened *"Proof for T-002: **the three commands**"*. The CLI
  has **four**, and this file exercises all four — `list` appears in it eight times. It read as a
  live description of what the file proves and was wrong. Now: *"Proof for T-002: the commands"*.
- `tests/test_publishing.py` line 355 said *"**three** of `list`'s **four** options across the same
  document"*. Both numbers are counts of mutable sets — how many options `list` has, and how many
  of them `README.md` happens to mention in prose. Now: *"several of `list`'s options"*.

**Decisions & assumptions**

1. **Both repairs drop the number rather than correct it** — 2026-08-22 — which is T-188's ruling
   applied rather than re-derived. Bumping *three commands* to *four* would have been correct today
   and wrong on the day a fifth arrives, which is the whole of that task's argument.
2. **Neither repair adds a note explaining the missing number** — 2026-08-22. T-188's own six
   repairs did not, and a sentence in every such place saying *the number is deliberately absent*
   would be a second copy of the ruling in six files. **Rejected** for that reason; the ruling has
   one home, in `tests/test_publishing.py`'s docstring.
3. **`cli.py` 1645's *three of the four commands take no options* is left** — 2026-08-22 — and it is
   the closest call in the table. It is a count, and it is derived from a set a recorded decision
   fixes at four; the sentence's subject is *which* commands take options, which `LIST_OPTIONS`
   being `list`-only already decides in the same module. Recorded here so the judgement is visible
   rather than looking like an oversight.
4. **`reference/` is excluded and named** — 2026-08-22 — rather than silently skipped. It is
   another project's document kept as evidence, and correcting a count in it would edit a record of
   what that project did.

**Step 6 — the gates**

```text
$ python -m pytest tests -q
336 passed, 8 subtests passed

$ ./plugin/bin/taskmd check
OK - 220 task(s), ...
EXIT=0
```

**Outputs produced**
- [`tests/test_cli.py`](../tests/test_cli.py)
- [`tests/test_publishing.py`](../tests/test_publishing.py)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The sweep is re-run with T-188's own command, and its **corpus is reported** — how many files it read and how many hits it produced | met | §3 step 1: 359 tracked files, 471 hits, with the command quoted. Same corpus as T-188, deliberately, so the two are comparable |
| Every exclusion is named with the number of hits it removes, and the excluded and included counts **sum to the total** | met | §3 step 2: 438 + 2 + 1 + 30 = 471, each exclusion with its reason |
| Every hit in the included set is classified, and the classes sum to that set | met | §3 step 4: 15 + 12 + 1 + 2 = 30, and every hit is named by file and line so the classification can be re-read rather than trusted |
| Anything the per-file verdict hid is repaired, or the record says there was nothing | met | Two, both repaired in §3 step 5. One was **wrong today** — `test_cli.py` said three commands where there are four — and it sat in the file whose job is to prove the commands |
| The suite and `check` are green, and the output is quoted | met | §3 step 6 |

**What review found beyond the table.** The two survivors are both in **test files**, and neither is
in a shipped document. That is a pattern worth naming: T-188's table has five of its eight rows in
`tests/`, and the tests are where this class hides best — a docstring is prose that no assertion
reads, sitting inside the machinery a reader assumes is self-checking.

**The count that was wrong was wrong when T-188 ran.** `list` was delivered by T-022, long before
T-188, so `test_cli.py`'s *three commands* was already false and the file-level sweep passed over it.
That is the same shape as the `github-issues.md` miss and is a second instance of it, found by the
same change of unit.

**Open questions, re-read before closing** (`review` step 5). §1 recorded none and none arose.
Decision 3 records the one judgement that could reasonably have gone the other way, so it is visible
rather than silent. Nothing is addressed to anyone else.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | → done | All five criteria met. 359 files, 471 hits, partitioned 438 / 2 / 1 / 30 with a **membership check** on the excluded task records rather than only a sum; the 30 classified one at a time into 15 / 12 / 1 / 2. **Two survivors, both in test docstrings**, both repaired by dropping the number per [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md)'s ruling — and one of them, *the three commands* in `tests/test_cli.py`, had been wrong since `list` shipped. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — this task is covered by it, and it is covered *because of how it arose*.** The **project owner** extended the grant on **2026-08-22**, at the start of the session that resumed the eight: *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it covers:** this task — raised by the reconcile sweep that closed that session's work — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed. **What it does not cover:** it authorises **phases, not answers**; a task reaching an open question belonging to the owner stops there, and §1 records that this one has none. In particular this task does **not** re-open T-188's ruling, which was the owner's to make. The grant reaches this record because the work that raised it was inside the eight, not because of any description of what needs nobody. |
| 2026-08-22 | → proposed | Raised from the reconcile sweep of the eight-task session, which found that [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md)'s catalogue carries one row per **file** where the unit is an **occurrence**, so a second count in an already-classified file was invisible. The instance that exposed it was repaired by [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md) hours earlier, which is why this asks whether any other survived rather than re-raising that one. `s` and `medium`: one sweep and a classification, on a class this repository has now met three times. |
