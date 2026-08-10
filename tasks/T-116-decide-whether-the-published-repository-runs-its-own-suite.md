---
id: T-116
title: Decide whether the published repository runs its own suite
type: decision
status: planned
phase: plan
parent: null
blocked_by: []
related: [T-011, T-049, T-115]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: []
---

# T-116 — Decide whether the published repository runs its own suite

## 1. Specify

**Outcome**
It is settled whether this repository runs its own test suite without being asked, now that it has a
remote — either something does and has been seen reporting a real failure, or it is written down that
the suite runs on request only, and what that costs is stated where somebody would look.

**Why this one**
Two closed tasks already weighed a CI runner and both recorded the same blocker in the same words:
**there is no git remote at all**
([T-011](T-011-runtime-discovery-and-project-hook-commands.md) step 3,
[T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)). That premise expired on
2026-08-09 when the repository was published, and neither task reopened, because a premise recorded
inside a task that closes goes out of date silently. This is the first work since then to depend on
it.

[T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md) is what makes it bite. It put the
tier 1 budget into the suite precisely so a breach would be reported without being remembered, and
was honest in its own record that this only converts *remember one command* into *run the suite*. The
margin it leaves is **two characters**, and the thing that spends it is ordinary reconcile work — so
the interval between a breach happening and anyone seeing it is exactly the interval between suite
runs, which nothing currently bounds.

**The uncomfortable half is the four failures.** `tests/test_runtime.py` fails four, three of them
this machine ([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md)) and one a real
cross-platform defect ([T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md)).
A runner that is red the day it arrives teaches everyone to stop reading it, which is worse than no
runner — so the decision cannot be taken without saying what happens to those four.

**The four are Windows-observed, and the runner will not be Windows.** Three of them are this
machine's shell rather than the code's, so the set that fails on a Linux runner is **not knowable
from here** — it could be fewer, more, or a different set entirely. "Naming the four" therefore
cannot be written into the mechanism in advance: the first real run establishes what the runner's own
baseline is, and *that* is what gets named. A workflow asserting a failure set nobody has observed
would be the same class of claim this project keeps catching in its own documents.

**Scope**
- In: whether anything runs the suite automatically, and what — a workflow on push, a hook, a
  scheduled run, or nothing with the consequence written down.
- In: what a mechanism does about the four known failures, since arriving red decides whether anyone
  keeps looking at it.
- In: which interpreters and platforms it would have to run on, given that three of the four failures
  are this machine's shell rather than the code's.
- Out: fixing those four failures. T-114 and T-112 own them, and fixing them here would be the
  finding-fixed-where-it-is-found this method refuses.
- Out: publishing, releasing and the version bump. Those are settled elsewhere and this changes
  nothing an adopter receives.

**Inputs**
- [T-011](T-011-runtime-discovery-and-project-hook-commands.md) step 3 and
  [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md), for the routes already weighed
  and the premise that expired under them.
- [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md) §3, for what the
  bundled-into-the-suite answer does and does not buy.
- `tests/`, for what a runner would have to execute and how long it takes.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative
- [ ] If something runs the suite: it has been seen reporting a **real** failure, not only a green run
- [ ] The four known failures are either excluded with a stated reason, or the mechanism is explicit
      about arriving red and says who is expected to act on it
- [ ] Whatever is decided costs an adopter nothing — it is this repository's arrangement and not part
      of what an install copies

**Open questions**
- ~~**Whether a runner that is red on arrival is worth having at all.**~~ **Answered by the
  maintainer, 2026-08-10: set one up now, red, naming the four known failures.** Against the rival of
  waiting for T-112 and T-114 to close and adding it green, which would have bought a runner nobody
  had reason to distrust on its first run — at the price of leaving a two-character budget margin
  unwatched between suite runs for however long those two take, which is the exposure T-115 closed
  everything else about.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish that the route is open at all before building anything on it: a remote exists, and the credential in use carries the scope a workflow file needs to be pushed. This is the step that could invalidate the rest, so it goes first. | A recorded fact: the route is available, or it is not and the decision changes |
| 2 | Write the workflow — the smallest thing that runs this repository's suite on push and reports. No matrix: running the same tree on a second platform to compare *output* is T-020's, and borrowing it here would settle that task's question without its criteria. | .github/workflows/tests.yml |
| 3 | Push it and let it run, then read what it actually reported — which tests failed on the runner, not which are known to fail here. | The run's real result, recorded in §3 |
| 4 | Name the baseline **from step 3's observation**, wherever a person meeting a red run would look. If the runner's failing set differs from this machine's four, that difference is the finding and is recorded rather than reconciled away. | The named baseline, and the task it belongs to if it turns out to be a new one |
| 5 | Prove the runner reports a *new* failure rather than only carrying its baseline — the criterion is that it has been seen reporting a real failure, and a red run that was already red proves only that it is red. | A second run's result, recorded in §3 |
| 6 | Run `check` and `index`, and confirm nothing about what an install copies has changed. | The commands' output, recorded in §3 |

**Deliverable shape** — a single GitHub Actions workflow at the repository root, outside `plugin/`.
Rejected: **a matrix across three operating systems**, which is T-020's question wearing a workflow's
clothes and would let this task close a criterion it never wrote; and **a scheduled run**, which
reports at a time unrelated to the edit that caused the breach — the same wrong-moment objection that
disqualified the `after_write` hook in T-115.

**Promised outputs**
- .github/workflows/tests.yml

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → specified → planned | The open question was answered the same day it was raised: **set one up now, red, naming the four known failures**, against waiting for T-112 and T-114 to close and adding it green. Whole-lifecycle authorisation carried over from T-115's entry — the maintainer's, covering each open v0.2 task through to a push, one at a time. `specify` gained one thing the raising session had not seen: the four failures are *Windows-observed*, and three of them are this machine's shell rather than the code, so what fails on a Linux runner is not knowable from here. That turns step 4 from "write down the four" into "read the run and write down what it says", and it is why the plan puts the push before the naming rather than after. Step 1 exists because everything else rests on a credential scope this session had not checked. |
| 2026-08-10 | → proposed | Raised from T-115's `implement`, where the enforcement it built turned out to depend on somebody running the suite and there is no `.github/` in this repository at all. Not folded into T-115: that task's outcome is the budget, and widening it to cover how every test in the tree gets run is the quiet scope growth METHOD §3.3 exists to stop. `high` because two closed tasks carry the same expired premise — *there is no git remote at all* — which stopped being true when the repository was published on 2026-08-09, and nothing re-examined them; `s` because the work is a decision and the rejected alternative is already half-written by T-011 step 3. |
