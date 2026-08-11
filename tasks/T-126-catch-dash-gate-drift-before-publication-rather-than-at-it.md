---
id: T-126
title: Catch dash-gate drift before publication rather than at it
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-079, T-081, T-115, T-125, T-127, T-129]
work_package: v0.5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [tests/test_publishing.py, docs/PUBLISHING.md]
---

# T-126 — Catch dash-gate drift before publication rather than at it

## 1. Specify

**Outcome**
A covered document that has drifted out of its humanized form is reported when it drifts, rather
than at the next publication — or the project records that publication-time is the right moment and
says why the drift is acceptable in between.

**Why this one**
Measured on 2026-08-11 while preparing [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md). The
dash gate (`docs/PUBLISHING.md` §5) counts lines in covered text carrying an em or en dash:

| Tag | `README.md` lines |
| :--- | ---: |
| `v0.1.0` | 0 |
| `v0.2.0` | 6 |
| `v0.3.0` | 13 |

The README was humanized once, for the first publication, and has drifted with every edit since.
**Two releases went out with that gate red**, and nothing said so — because the gate is a manual
command in a document read only at publication, and publication is exactly when there is most
pressure not to stop.

**It is the shape this project has a fix for already.** `tests/test_budget.py` was written (T-115)
because a tier-1 budget nobody ran was a budget nobody kept, and the answer was to make the suite
fail rather than to remember a command. This is the same failure one document over, and the same
answer is available.

**Why it is not simply "add it to the suite".** The gate is a **proxy** and `docs/PUBLISHING.md` §5
says so: failing it proves the rewrite did not happen, passing it proves only that one pattern is
absent. A test that goes green on a document nobody humanized would make the drift *less* visible,
not more, by converting an honest absence of evidence into a passing assertion.

**Requirements served**
R-21 (`docs/SCOPE.md`) — humanized wherever a stranger reads it before installing, which is a
property of the tree at all times rather than at one moment.

**Scope**
- In: when the gate runs, and what makes it run.
- In: whether a green automated check would misrepresent what the gate can judge, and how to word it
  if so.
- Out: what the gate matches, and the three skipped humanizer patterns. Settled in T-079 and T-081.
- Out: the covered-set test in `docs/PUBLISHING.md` §1, which is deliberately a rule and not a list.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §5, including *What passing does not prove*.
- `tests/test_budget.py`, as the precedent for enforcing a publication-time rule from the suite.
- [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md) §3, for the measurement above.

**Acceptance criteria**
- [ ] A covered document gaining an em dash is reported without anyone choosing to run a check,
      shown by adding one and watching it fail
- [ ] Whatever reports it says what a pass does **not** prove, in its own output or its own name
- [ ] The existing gate in `docs/PUBLISHING.md` §5 and whatever is added do not become two homes for
      one rule
- [ ] A run on the tree as published at `v0.4.0` is green, so the check starts from a known state

**Open questions**
- ~~**Suite, hook, or neither.**~~ **Answered by the maintainer on 2026-08-11: a test in the suite**,
  on `test_budget.py`'s precedent. The rule becomes free to keep, and drift is caught in the commit
  that causes it instead of two releases later.

  *Rejected: a project `after_write` hook.* It is the mechanism taskmd already ships, so it would
  have doubled as dogfooding. It cannot work here: a hook fires on taskmd's own writes, and the
  drift arrives through a README edit that taskmd never sees.

  *Rejected: leave it manual.* Cheaper, and the gate does catch the problem at the one moment it
  blocks a release. That is also the reasoning that produced two red releases.

  **What the answer does not settle** is the §1 problem this task's scope excludes: a passing test
  must still say what it does not prove. Criterion 2 carries that, and it is now the harder half.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the covered pathspec and the two dash characters **out of** `docs/PUBLISHING.md` §5 rather than restating them, and fail loudly if they cannot be found | `tests/test_publishing.py` |
| 2 | Assert no covered file carries either character, in a class whose **name** says what a pass does not prove | `tests/test_publishing.py` |
| 3 | Prove it fires twice over: a fixture with a dash, and a live demonstration on the real `README.md` recorded in §3 | §3, and a test |
| 4 | Run the same scan over the tree as published at `v0.4.0` | A figure in §3 |
| 5 | Point `docs/PUBLISHING.md` §5 at the test — a pointer, never a second copy | `docs/PUBLISHING.md` |
| 6 | Suite, `index`, `check` | §3 |

**Shape decisions.**

**D1 — The test reads the pathspec out of the document; it does not restate it.** This is criterion 3
in one decision. `docs/PUBLISHING.md` §5 stays the only place the covered set and the two characters
are written; the test extracts them from the fenced command and **fails with a message saying so** if
it cannot. A gate the suite can no longer read has drifted, and that is a failure rather than a skip.
*Rejected: a second pathspec in Python* — two homes for the one thing this project's own rule forbids
having two of, and it would go stale exactly when a covered document is added.

**D2 — The limit goes in the class name.** Criterion 2 asks for it in the output or the name, and a
name is in every failure line and in every verbose run, where a docstring is not. The class is
`ThePassingDashGateProvesOnlyThatOnePatternIsAbsent`.

**D3 — Python does the scanning; the documented bash line is not shelled out.** Running the exact
command would be the strongest form of one-home, and it cannot be relied on here: `bash` is not
guaranteed on Windows, and where it exists it may resolve to WSL, which disagrees with Git Bash about
paths. A gate that skips on the maintainer's own machine is the manual gate again, which is the
defect. So the *rule* is read from the document and only the *mechanism* is reimplemented.
*Rejected: `subprocess` on the fenced command* — correct in principle and it would have been skipped
on the one platform this project is written on.

**Planned outputs**
- `tests/test_publishing.py` — new module, picked up by `unittest discover`
- `docs/PUBLISHING.md` — §5, one pointer

## 3. Implement

### Steps 1 and 2 — one home, read rather than restated

`tests/test_publishing.py` splits `docs/PUBLISHING.md` at `## 5. The gate` and lifts two things out
of the fenced command: the `git ls-files` pathspec, and the characters `grep` is given. Neither is
written in the test. What it read today:

```text
pathspec read from docs/PUBLISHING.md section 5: README.md docs/repo-description.txt
                                                 .claude-plugin/*.json */.claude-plugin/*.json
characters: — –
covers 4 file(s) in the working tree
```

Three assertions, in a class named
`ThePassingDashGateProvesOnlyThatOnePatternIsAbsent` (**D2**): the pathspec resolves to files at all —
§5's exit 2, which exists because a run covering nothing prints nothing and so does success; no
covered line carries either character; and the characters really are the two dashes, checked against
text that must be caught.

Extraction failure is an `AssertionError` with its own sentence, not a skip:

> could not read the pathspec out of docs/PUBLISHING.md section 5; the command's shape changed, so
> the documented gate and this test are no longer the same rule

### Step 3 — watching it fail

One em dash appended to `README.md`, nothing else touched:

```text
- []
+ ['README.md:260'] : 1 covered line(s) carry a dash the humanizer removes; run the rewrite in
docs/PUBLISHING.md section 2, not a find-and-replace:
README.md:260
FAILED (failures=1)
```

Reverted, and `git diff --name-only HEAD -- README.md` names nothing afterwards. The message points
at the rewrite rather than at the character, because the character is the proxy and the rewrite is
the rule.

### Step 4 — every tag, including the one this starts from

The scan is a reimplementation (**D3**), so it was run over history to see whether it agrees with the
`grep` that produced T-125's figures:

```text
v0.1.0   4 file(s) covered,  0 offending line(s)
v0.2.0   4 file(s) covered,  6 offending line(s)
v0.3.0   4 file(s) covered, 13 offending line(s)
v0.4.0   4 file(s) covered,  0 offending line(s)
```

**`v0.4.0` is green, which is criterion 4**, and the middle two rows reproduce T-125's measurement
exactly — 0, 6, 13. So the Python scan and the documented `grep` agree on three trees neither was
written against, which is the evidence D3 owed for reimplementing the mechanism.

### Step 5 — the pointer

`docs/PUBLISHING.md` §5 gains one paragraph saying the suite runs this rule and reads it from there.
**The command stays.** A person publishing wants the offending lines, not a test name, and §5 is the
rule's one home — moving it into the test would relocate the duplication rather than remove it.

### Step 6

```text
python -m unittest discover -s tests -q     Ran 233 tests     OK (skipped=3)
```

`test_publishing` is picked up by discovery, so nothing enumerates the module list.

**Decisions & assumptions**

- **A missing `git` skips the class, and that is the one skip allowed.** The covered set is a git
  pathspec, so there is nothing to resolve without it; the suite already gates on `git` this way.
  Every other failure path is a failure. — 2026-08-11
- **The test does not run the fenced bash command. D3.** Correct in principle, and on this platform
  `bash` resolves to something that cannot execute a script named the way these tests name one — the
  launcher checks already skip for exactly that reason, printing which candidate it tried. A gate
  that skips where the work happens is the manual gate again. — 2026-08-11
- **No attempt to judge humanizing.** The class name is the whole of the answer to what a pass does
  not prove; nothing here claims more than pattern 14. — 2026-08-11

**Outputs produced**
- `tests/test_publishing.py` — new module, three tests
- `docs/PUBLISHING.md` — §5, one paragraph pointing at it

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A covered document gaining an em dash is reported without anyone choosing to run a check, shown by adding one and watching it fail | met | §3 step 3 quotes the failure, naming `README.md:260`. It arrives from `unittest discover`, so nobody chooses to run it. |
| Whatever reports it says what a pass does **not** prove, in its own output or its own name | met | The class is `ThePassingDashGateProvesOnlyThatOnePatternIsAbsent`, so the limit is in every failure line and every verbose run (**D2**). |
| The existing gate in `docs/PUBLISHING.md` §5 and whatever is added do not become two homes for one rule | met | The pathspec and the characters are **read out of** §5 (**D1**). A shape the test cannot parse fails with a message saying the two have come apart, rather than skipping. |
| A run on the tree as published at `v0.4.0` is green, so the check starts from a known state | met | 4 files covered, 0 offending lines. The same scan over `v0.2.0` and `v0.3.0` returns 6 and 13, reproducing T-125's figures — so the reimplementation is calibrated against the original on trees it was not written for. |

**Child fix tasks raised**
- none.

**Verdict.** All four criteria met. The rule that was red for two releases now costs nothing to keep,
and the harder half — a proxy that does not pretend to be more — is carried by the name a reader
cannot avoid.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All four criteria met. The rule is now free to keep and it starts from a known state: `v0.4.0` scans green at 4 files and 0 offending lines. **The reimplementation was calibrated rather than trusted** — the same scan over `v0.2.0` and `v0.3.0` returns 6 and 13, reproducing [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md)'s figures on trees it was not written against, which is what **D3** owed for not shelling out to the documented command. Criterion 2 was the harder half and the answer is a name: `ThePassingDashGateProvesOnlyThatOnePatternIsAbsent` appears in every failure line, where a docstring would not. Criterion 3 is **D1**: the pathspec and the two characters are read out of §5 rather than restated, and a shape the test cannot parse is a failure with its own sentence, not a skip. |
| 2026-08-11 | → in_progress | Six steps. Firing was shown twice: a fixture, and one em dash appended to the real `README.md`, which failed naming `README.md:260` and was then reverted. The failure message points at the humanizer rewrite rather than at the character, because the character is the proxy. `docs/PUBLISHING.md` §5 keeps its command — a person publishing wants the offending lines, not a test name — and gains one paragraph pointing at the test. 233 tests through `unittest discover`, so the new module needs no enumeration anywhere. |
| 2026-08-11 | → planned | Six steps, and the plan is mostly two decisions. **D1** answers criterion 3 by reading the pathspec and the characters out of the document instead of restating them; **D3** declines to shell out to the fenced bash line, because `bash` here resolves to something that cannot run a script named the way these tests name one, and a gate that skips on the machine where the work happens is the manual gate again. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → specified | Answered by the maintainer: **a test in the suite**, on `test_budget.py`'s precedent. Both rivals are recorded in §1 with what they lose. The hook was the interesting one and it fails on a fact rather than on a preference: a hook fires on taskmd's own writes, and this drift arrives through a README edit taskmd never sees. **The answer settles the cheaper half.** Criterion 2 is now the work: the gate is a proxy, so a green test must say what it does not prove, or it converts an honest absence of evidence into a passing assertion and hides the drift better than the manual command did. |
| 2026-08-11 | → proposed | Raised from T-125, which ran the gate before deciding anything and found it red — and then found, from the three existing tags, that it had been red for two releases. Not fixed inside T-125 (METHOD rule 4): that task's job is to ship this tree through the gate, and making the gate run at a different moment is a different outcome with its own cost. Filed `v0.3` by `tasks/README.md`'s rule — it is new enforcement rather than a correction, so it is outside the standing `v0.2` authorization and is not started here. `medium` because the thing it protects is the one document a stranger reads before installing, and the failure mode is silence. |
