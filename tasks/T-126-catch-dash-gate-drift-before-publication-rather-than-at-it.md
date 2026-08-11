---
id: T-126
title: Catch dash-gate drift before publication rather than at it
type: fix
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-079, T-081, T-115, T-125]
work_package: v0.5
owner: maintainer
business_value: medium
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: []
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
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: v0.5`, through all four phases — including a task raised into v0.5 *by* that work, which is a v0.5 task and not a fresh grant. It **does not generalise** to `v0.6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a v0.5 task would then need its own permission, and asking seven times is not continuous work.
| 2026-08-11 | → specified | Answered by the maintainer: **a test in the suite**, on `test_budget.py`'s precedent. Both rivals are recorded in §1 with what they lose. The hook was the interesting one and it fails on a fact rather than on a preference: a hook fires on taskmd's own writes, and this drift arrives through a README edit taskmd never sees. **The answer settles the cheaper half.** Criterion 2 is now the work: the gate is a proxy, so a green test must say what it does not prove, or it converts an honest absence of evidence into a passing assertion and hides the drift better than the manual command did. |
| 2026-08-11 | → proposed | Raised from T-125, which ran the gate before deciding anything and found it red — and then found, from the three existing tags, that it had been red for two releases. Not fixed inside T-125 (METHOD rule 4): that task's job is to ship this tree through the gate, and making the gate run at a different moment is a different outcome with its own cost. Filed `v0.3` by `tasks/README.md`'s rule — it is new enforcement rather than a correction, so it is outside the standing `v0.2` authorization and is not started here. `medium` because the thing it protects is the one document a stranger reads before installing, and the failure mode is silence. |
