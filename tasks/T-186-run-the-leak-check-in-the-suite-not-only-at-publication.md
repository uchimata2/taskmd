---
id: T-186
title: Run the leak check in the suite, not only at publication
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-034, T-058, T-080, T-126, T-183]
work_package: M6
owner: the project owner
business_value: high
effort: m
created: 2026-08-18
updated: 2026-08-18
adopter_visible: no
deliverables: []
---

# T-186 — Run the leak check in the suite, not only at publication

## 1. Specify

**Outcome**
`docs/PUBLISHING.md` §6's check runs in `tests/`, reading its command and its accepted set out of that
document, so its pass condition is asserted on every test run rather than only when somebody
remembers to publish.

**Why this one**
**The remedy is written and nobody applies it.** §6 tells a writer to elide a component of a
four-part version, and to describe a matched line rather than paste it. Four records have broken one
of those two rules: T-013 and T-018, which §6 counts itself, and
[T-129](T-129-release-v0-5.md) and
[T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md), found on 2026-08-18 by
[T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md). **Every one was
caught by a person, and two of the four by accident** — noticed while doing something else.

**The framing this task started with was wrong, and correcting it is what makes it small.** The
request was a guard for the two remedies. No such guard is needed: §6's check already detects both —
detection is how all four were found. **What is missing is that nothing runs it.** It is a command a
person types before publishing, so it runs at publication or never, and its output has to be read and
judged by whoever typed it.

**The precedent is exact and it is in this repository.** §5's dash gate had the identical shape and
[T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) fixed it: the suite now
lifts the pathspec and the characters out of §5 rather than restating them, so the document stays the
one home and a covered file added to that line arms the test with nothing edited anywhere else. That
gate had been red for two releases and nobody had disobeyed it — nobody had run it. §6 is the same
gate, one section later, still unrun.

**T-183 supplied the half that makes this testable.** §6's pass condition used to be *it must print
nothing*, which was unreachable and therefore unassertable. It is now a count — two named lines from
one named file, anything else a finding — so there is a condition a test can hold.

**Requirements served**
R-17 (`docs/SCOPE.md`) — a rule nobody enforces is a rule that is not there. R-8, in that the four
instances left no trace until a person happened to look.

**Scope**
- In: a test that runs §6's command and asserts its counted pass condition
- In: reading the command, the exclusion and the accepted set **out of `docs/PUBLISHING.md`**, so the
  document stays their one home — T-126's shape, not a second copy
- In: what the test does where `git` is unavailable, matching how the existing gate test handles it
- Out: changing §6's patterns, its command, or its pass condition. All three are settled, the last by
  [T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md)
- Out: the accepted block itself. T-183 closed that and recorded the condition that would reopen it
- Out: a guard aimed at the two remedies. The check already detects them; see *why this one*

**Inputs**
- `docs/PUBLISHING.md` §6 — the command, the exclusion, the accepted pair and the counted condition
- `tests/test_publishing.py` — `gate_from_the_document`, `covered_files`, `git_is_available` and
  `ThePassingDashGateProvesOnlyThatOnePatternIsAbsent`, which are the shape to follow
- [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) — the same fix for the
  neighbouring gate, including what it decided about a shape the test cannot parse
- `tests/fixtures/leak-check/samples.txt` — nine lines, five that must be caught and four that must
  not, and the second of §6's two runs

**Acceptance criteria**
- [ ] The test fails when a new tripping line is added to a tracked document, shown by adding one and
      watching it fail before it is removed
- [ ] The test reads the command, the exclusion and the accepted set from `docs/PUBLISHING.md`; a
      shape it cannot parse is a **failure, not a skip** — T-126's rule
- [ ] Both of §6's runs are asserted: with the fixture exclusion, only the accepted lines; without it,
      those plus exactly the fixture's five, one per class
- [ ] Editing §6's accepted set alone makes the test agree, with nothing edited in `tests/`
- [ ] The behaviour without `git` matches what the neighbouring gate test already does, rather than
      inventing a second convention
- [ ] Running the four instances' historical shapes past it shows it would have caught them — at
      least the two from 2026-08-18, which are recoverable from git history

**Open questions**
- **What exactly does the test assert — a count, or a set?** A bare count is the cheapest and is
  brittle in a way that matters: it goes red the day the accepted set legitimately changes, and the
  repair is to edit a number in `tests/`, which is the second home this whole shape exists to avoid.
  Asserting the *set* — every hit must be a line §6 names — costs parsing but keeps the document
  authoritative and fails for the right reason.
  **My lean is the set, for T-126's stated reason rather than a new one.** The owner's, because it
  decides how much §6 has to be machine-readable, and that constrains how it may be written later.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |
| 2 |  |  |

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
| 2026-08-18 | → proposed | Raised at the owner's request, from a residue recorded in [T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md)'s review rather than left to die there with the closing task. **The request was for a guard on §6's two remedies and the investigation reframed it**: the check already detects both, which is how all four instances were found, so the gap is that nothing runs it. That makes this T-126 applied one section later, and T-126 is why the shape is known to work. Only reachable at all because T-183 turned §6's unreachable *must print nothing* into a countable condition. One genuinely open question — count or set — which is the owner's because it decides how machine-readable §6 must stay. |
