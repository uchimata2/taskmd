---
id: T-116
title: Decide whether the published repository runs its own suite
type: decision
status: proposed
phase: specify
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
- **Whether a runner that is red on arrival is worth having at all.** The maintainer's. It is the
  question that decides between "set one up now" and "set one up after T-112 and T-114 close", and
  the two answers produce different tasks.

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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | Raised from T-115's `implement`, where the enforcement it built turned out to depend on somebody running the suite and there is no `.github/` in this repository at all. Not folded into T-115: that task's outcome is the budget, and widening it to cover how every test in the tree gets run is the quiet scope growth METHOD §3.3 exists to stop. `high` because two closed tasks carry the same expired premise — *there is no git remote at all* — which stopped being true when the repository was published on 2026-08-09, and nothing re-examined them; `s` because the work is a decision and the rejected alternative is already half-written by T-011 step 3. |
