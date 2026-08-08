---
id: T-058
title: Say that a four-part version number trips the leak check
type: fix
status: proposed
phase: specify
parent: T-049
blocked_by: []
related: [T-049, T-018, T-034, T-035]
work_package: none
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-058 — Say that a four-part version number trips the leak check

## 1. Specify

**Outcome**
Someone who records a version number in a task and watches the pre-publish check go off knows within
one line whether they have leaked something or hit a known limit of the pattern.

**Why this one**
Found by [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md), which recorded the
second platform's kernel as reported by `uname`. That string carries a **four-component version
number**, and the check's IP branch — `[0-9]{1,3}(\.[0-9]{1,3}){3}` — cannot tell one from an
address. The check fired on the task's own record, twice.

Nothing had leaked. But the failure mode is the expensive one: `CLAUDE.md` says the check must print
nothing and that **every hit is either a leak or a label that needs adding**, so a reader who trusts
that sentence spends their time hunting for a leak that is not there. T-049 worked around it by
eliding the patch component, which is a fix for one record rather than for the next person.

**This is the third limit, and the other two are already written down.** `CLAUDE.md` explains at
length why a single-segment drive path is deliberately let through — "a check that cries wolf gets
ignored, which is worse than a narrow one" — and why a real name is not mechanically detectable at
all. Both are honest statements of what the pattern cannot do. This one is the same kind of fact and
is simply missing, which is why the task is about **saying it**, not necessarily about changing the
pattern.

**Requirements served**
No numbered requirement — this serves `CLAUDE.md` *Publishing constraints* and the *Verifying*
discipline directly. A check whose false positives are undocumented gets its output disbelieved,
and then it is not a check.

**Scope**
- In: whether the limit is documented, narrowed, or both.
- In: what a version number should look like in a record, if the answer is "document it".
- Out: the other two limits and the fixture. They are correct and
  [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) and
  [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) settled them.
- Out: any change to what the check *scans*. T-034 settled that.

**Inputs**
- `CLAUDE.md` *The pre-publish check* — the pattern, and the two limits already stated.
- `tests/fixtures/leak-check/samples.txt` — nine lines, five that must be caught and four that must
  not. A fifth safe form belongs there if the answer is "narrow it".
- [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) §1, for the case that found it.

**Acceptance criteria**
- [ ] A reader who hits this is told, in `CLAUDE.md`, what it is and what to do — without having to
      find this task
- [ ] If the pattern is narrowed, the fixture gains a line for the new safe form **and** keeps
      catching all five it caught before — shown by running both halves of the documented check
- [ ] If the pattern is not narrowed, the record says why the false positive is cheaper than the
      alternative, in the same terms the other two limits use

**Open questions**
- **Narrow it, or only document it?** Requiring each component to be ≤ 255 would let a version whose
  third component exceeds it through, while still catching every real address — but a version *can*
  be all-low-numbered, so it narrows the false positives without removing them, and it makes the
  pattern harder to read for a gain that may be smaller than the cost. `CLAUDE.md`'s own argument
  cuts both ways here and the maintainer owns the trade-off, as they did for the drive-path limit.

  *No four-part number is written anywhere in this task, deliberately.* Quoting the specimen into the
  record of a task about the checker re-creates exactly what the checker catches — which happened in
  T-013 and again in T-018, and which `CLAUDE.md` warns about in those words. The specimen belongs in
  `tests/fixtures/leak-check/samples.txt` if the answer is "narrow it", and nowhere else.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- `deliverables/...`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Raised by T-049 under METHOD §3.3. Recording the second platform's kernel string put a four-component version into a task record, and the check's IP branch matched it twice — nothing leaked, but `CLAUDE.md` promises every hit is a leak or a missing label, so the reader is sent hunting. T-049 elided the patch component, which fixes one record and not the next one. This is the **third** limit of a pattern whose other two are already written down at length, so the task is about saying it; narrowing is an option rather than the goal. `medium`/`xs` — one paragraph in `CLAUDE.md`, possibly one fixture line, but it protects the credibility of the only mechanical guard before publication. |
