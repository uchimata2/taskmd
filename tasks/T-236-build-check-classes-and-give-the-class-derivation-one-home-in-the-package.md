---
id: T-236
title: Build check --classes, and give the class derivation one home in the package
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-226, T-197, T-191, T-222]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/taskmd/classes.py
  - plugin/skills/taskmd/taskmd/cli.py
  - plugin/skills/taskmd/docs/BINDING.md
  - tests/classes.py
---

# T-236 — Build check --classes, and give the class derivation one home in the package

## 1. Specify

**Outcome**

`check --classes` prints the set of classes `check` can report, from an installed copy, and the
derivation that produces that set exists **once** — in the package, with `tests/classes.py` importing
it rather than repeating it.

**Where this came from**

[T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) put the
whether-and-what-shape question to the owner and it was answered on 2026-08-22: **yes, as
`check --classes`** rather than a fifth command, because it adds no verb to a surface this project has
held at four and it sits on the command that owns the classes. T-226 §3 answers its third criterion —
the derivation moves into the package — with the placements it rules out. **This record is the build,
which T-226's scope puts out of its own.**

**Why it matters rather than being tidiness.**
[`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 requires a binding to name the classes its
mapping makes impossible **in the validator's own names**, and tells the author to go and read
`cli.py`. That is honest and it asks somebody to read Python in order to write Markdown. T-225
measured the cost: both uninvolved readers found the answer and both reported they could not reach it
from the text.

**Scope**

- In: the flag, the move of the derivation into the package, and `tests/classes.py` reduced to an
  import so that the set has one home
- In: the four questions below, which T-226's answer does not reach and which were found by writing
  this record from it
- In: [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 *Where the class names come from*
  updated to name the command, since its current instruction is *read the source* and the whole point
  is to replace it
- Out: changing what the classes are, or adding one
- Out: a list of the classes in any document. That is the per-check coverage table §4 refuses, one
  column narrower, and it is falsified by the same event
- Out: `tests/classes.py`'s own guard readers in `tests/test_publishing.py` losing coverage — they
  must still run against the derivation wherever it ends up

**Inputs**

- [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md) §3 — the
  answer, the rejected placements, and the four gaps this record's questions come from
- `tests/classes.py` — the derivation as it exists, its guard on `CONFIG ERROR`, and the `source=`
  override that keeps the guarded line inside the run
- `plugin/skills/taskmd/taskmd/cli.py` — the 20 `problems.append` sites and `ADVISORY_PREFIXES`
- [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) — the defect a second
  derivation would re-create

**Acceptance criteria**

- [ ] `check --classes` prints the set, and is shown to do so **from an installed copy** rather than
      from this working tree
- [ ] Exactly one derivation exists: a search for the prefix pattern finds it in one place, and
      `tests/classes.py` imports rather than repeats it
- [ ] The set the flag prints is the same set the tests compare against, shown by running both
- [ ] `CONFIG ERROR` is absent from the printed set, and the guard that removes it is still exercised
      by its reader in `tests/test_publishing.py`
- [ ] [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 names the command where it currently
      says to read the source, and no list of classes is added to any document
- [ ] `taskmd check` passes and the suite passes with no bound edited

**Open questions**

*All four came out of writing this `specify` from T-226 alone, which was T-226's own verification
step. None is the owner's; each is answerable by measurement during `plan`.*

- **Does the shipped derivation keep reading `cli.py`'s source text, or do the 20 append sites gain a
  constant?** `tests/classes.py` says a constant *"would change `cli.py` at every append site, which
  is a plugin change with adopter reach and is out of T-197's scope"* — but this record **is** a
  plugin change, so the reason has expired and the question is live again. **Recommendation: keep the
  regex.** 20 sites is a large diff for robustness the guard reader already supplies, and the padding
  those literals carry is what aligns `check`'s output. *Against:* a prefix that stops matching leaves
  the set silently, and a shrunken set makes every assertion built on it **weaker** rather than
  louder — which the module's own docstring names as its cost.
- **Does a runtime source-read work from an installed copy?** The derivation opens `cli.__file__`.
  That is fine for a directory install, which is what this plugin ships as, and it is **not** fine if
  the module is ever loaded from an archive or a frozen build. Nothing anywhere has considered this,
  because until now the derivation only ever ran from a checkout. It is the first acceptance criterion
  for that reason. **Recommendation: measure it before choosing the shape above** — if it fails from
  an install, the constant stops being optional and the first question is answered for us.
- **What exactly does the flag print?** One class per line, sorted, nothing else — so the output can
  be piped and diffed — or grouped into problems and advisories, which is a distinction a binding
  author does care about, since only the problem classes move an exit code. **Recommendation: one per
  line, sorted, no grouping**, and let `check`'s own output teach the distinction. *Against:* the
  author then cannot tell from this command which names are advisory.
- **Does `check --classes` still run the checks?** **Recommendation: no — print and exit 0**, because
  a binding author running it has no project in mind and `check` would fail on whatever directory they
  happen to be in. *Against:* every other flag on `check` modifies a run rather than replacing it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Answer the second open question first — does a runtime source-read work from an installed copy? — because a *no* answers the first one for us | the run, against this machine's real install |
| 2 | Move the derivation into the package and reduce `tests/classes.py` to a re-export | the two files |
| 3 | Wire `--classes` so it answers **before** discovery, and give `check --help` the line T-144's rule now allows it | the edited `cli.py` |
| 4 | Point [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 at the command where it currently says to read the source | the edited clause |
| 5 | Test it: sorted output, the same set the tests use, no project needed, `CONFIG ERROR` absent, and the help line | the new tests |
| 6 | Run it from a copy of what an install receives, not from this tree | the run |

**Step 1 leads because it can decide step 3's shape.** If `cli.__file__` is unreadable from an
install, the regex has to become a constant at twenty sites and the build is a different size.

**Step 6 is separate from step 5 on purpose.** A test in `tests/` runs against the working tree, and
the criterion is about the copy an adopter gets — `tests/` is not in it.

## 3. Implement

**Decisions & assumptions**

- **The regex stays; the twenty append sites gain no constant** — 2026-08-23, and step 1 is why it
  could be decided rather than argued. The runtime source-read works from an installed copy, so the
  reason to change it never arose. A constant would touch twenty sites and change the padding that
  aligns `check`'s output, against robustness the guard reader already supplies.
- **`--classes` answers before discovery and exits 0** — 2026-08-23. Its caller is writing a binding
  and has no backlog in mind; running the checks first would fail on whichever directory they are
  standing in and tell them nothing about the names they came for. It sits beside `--help` in the
  argument loop for exactly that reason.
- **One class per line, sorted, no grouping** — 2026-08-23. It can be piped, diffed and read; the
  problem/advisory distinction is visible in `check`'s own output, and putting it here would make the
  command's format a second statement of something the code already shows.
- **`check --help` now prints a per-command line, and that applies T-144's rule rather than extending
  it** — 2026-08-23. That ruling permits a per-command line exactly where the top-level line's
  `[args]` hides a real option, and forbids one that would restate — which is what T-029 rejected.
  `check` had no options until today. Two existing tests asserted the old state and are updated with
  the reason written into them.
- **`tests/classes.py` is kept as a re-export rather than deleted** — 2026-08-23. Two readers in
  `test_publishing.py` import it by name; deleting it would move a shipped-code change into their
  import lines for no gain.

**Outputs produced**

- `plugin/skills/taskmd/taskmd/classes.py` — the derivation, moved
- `plugin/skills/taskmd/taskmd/cli.py` — `--classes`, and `check_help()`
- `plugin/skills/taskmd/docs/BINDING.md` — §4 names the command
- `tests/classes.py` — reduced to a re-export
- `tests/test_cli.py`, `tests/test_publishing.py` — five new tests, three repaired

**Verification**

**Step 1, and it answered the first question too.** Run against this machine's actual installed
plugin — the `0.5.0` snapshot in the plugin cache, not a copy made for the test:

```text
installed tree: True
cli loaded from: .../plugins/cache/taskmd/taskmd/0.5.0/skills/taskmd/taskmd/cli.py
prefixes read from the INSTALLED source: 14
```

**It read the installed copy's own source and got that copy's own answer** — fourteen, against
twenty-two in the working tree, because `0.5.0` predates eight of them and `ADVISORY_PREFIXES`
entirely. The mechanism works and the snapshot is older, which is the behaviour wanted: the flag
answers for the version the caller has, not for the version this record was written against.

**Steps 3 and 5 — the flag.**

```text
$ taskmd check --classes                     ->  exit 0, 22 lines, sorted
$ taskmd check --classes   (from C:\, no project anywhere above)  ->  exit 0, 22 lines
$ taskmd check --help
usage: taskmd {check,context,index,list} [args] [--root PATH]
usage: taskmd check [--classes]  print the classes check can report, and exit
```

**One derivation, two callers, checked against each other**: the re-export and the flag return
identical sets — `tests re-export: 22   flag: 22   identical: True` — which is the assertion that
would catch T-191's defect being re-created.

**The move broke a guard test, and that is the finding of this step.**
`TestTheGuardOnTheDerivedSetStillBites` empties `NOT_A_CHECK_CLASS` and asserts the class then
appears. It patched `classes.NOT_A_CHECK_CLASS` — the **re-export** — which no longer reaches the
constant `check_classes` actually reads, so the patch became a no-op and the test asserted nothing.
**It failed loudly the moment the move landed** rather than passing vacuously, which is precisely
what a guard on a guard is for. Repointed at `taskmd.classes`, with the reason written beside it.

**Step 6 — from a copy of what an install receives.** `plugin/skills/taskmd/` copied alone to a
scratch directory and run through its own shipped launcher:

```text
$ sh ./taskmd.sh check --classes
exit 0, 22 classes
```

That is the criterion: not this working tree, and not `tests/`, which an install does not receive.

**Gates.** `taskmd check` exit 0. `python -m pytest tests/ -q` reports **342 passed, 8 subtests
passed**, up from 337 by the five tests added here.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| `check --classes` prints the set, shown **from an installed copy** rather than from this working tree | met | Twice over: the derivation read this machine's real `0.5.0` install and returned that copy's own fourteen prefixes, and the flag itself ran from a fresh copy of `plugin/skills/taskmd/` through its shipped launcher, exit 0, 22 classes |
| Exactly one derivation exists; `tests/classes.py` imports rather than repeats it | met | `taskmd/classes.py` holds it; the test-side file computes nothing and re-exports three names. The two are asserted to return identical sets by a test, so a future divergence fails rather than drifts |
| The set the flag prints is the same set the tests compare against, shown by running both | met | `tests re-export: 22   flag: 22   identical: True`, and now a standing test |
| `CONFIG ERROR` is absent, and the guard that removes it is still exercised by its reader | met | Absent, and asserted. **The reader had stopped exercising it** — it patched the re-export, which the move made a no-op — and it failed rather than going quiet. Repointed at the package module |
| §4 names the command where it said to read the source, and no list of classes is added to any document | met | The clause now gives `taskmd check --classes`, says it needs no project, and says it answers for the reader's own installed version. No class is listed anywhere |
| `taskmd check` passes and the suite passes with no bound edited | met | `exit 0`; **342 passed, 8 subtests passed**, up from 337 by the five added here. `tests/test_budget.py` unedited — the change is code and a tier-3 clause, and touches no tier-1 file |

**Child fix tasks raised**
- none.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 held four, none of them the
owner's, and all four are answered in §3 with the measurement that settled each: the regex stays, the
installed-copy read works, one sorted class per line, and the flag does not run the checks.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed: six criteria, six met.** `check --classes` prints the 22 classes, sorted, one per line, needing no project — so [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 can tell a binding author to run something instead of to read Python. **The plan put the installed-copy question first because a *no* would have resized the build**, and it answered itself twice: the derivation read this machine's real `0.5.0` snapshot and returned **that copy's** fourteen prefixes rather than the working tree's twenty-two, which is the mechanism working and the snapshot being old. So the regex stays and the twenty append sites gain no constant. **The derivation now has one home in the package**, forced by `tests/` sitting outside `plugin/`, with the test-side file reduced to a re-export and a standing test asserting the two agree. **The move broke a guard test and that is the best thing in this record**: `TestTheGuardOnTheDerivedSetStillBites` patched the re-export, which stopped reaching the constant `check_classes` reads, so the patch became a no-op — and it **failed** instead of passing vacuously, which is exactly what a guard on a guard exists for. **`check --help` gains a line by applying T-144's rule**, which permits one where the top-level line hides a real option; two tests asserting the old state are updated with the reason in them. 342 passed, up from 337. |
| 2026-08-23 | → proposed | Raised from [T-226](T-226-decide-whether-taskmd-should-print-the-class-list-a-binding-author-needs.md)'s `implement`, whose scope puts building it out by name, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure, without stopping to ask for each phase. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-233](T-233-give-the-uninvolved-reader-protocol-one-home-and-settle-its-count-rule.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), and **any audit** — unchanged. **None of the four open questions above is the owner's**, so unlike [T-235](T-235-recover-or-retire-the-reader-questions-t-225-s-review-says-its-record-carries.md) this record does not stop at `specify`; each is answerable by measurement in `plan`. **This record was written from T-226 alone, deliberately and as that task's verification step** — a decision is verified when the people bound by it can state what it commits them to, so the smallest real use of the answer was to write the build's `specify` from it and keep what had to be invented. The four questions **are** that list, and the second is the one worth having: nothing had considered that a derivation reading its own module's source has only ever run from a checkout. |
