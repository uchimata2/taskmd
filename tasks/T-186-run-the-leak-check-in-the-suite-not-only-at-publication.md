---
id: T-186
title: Run the leak check in the suite, not only at publication
type: fix
status: done
phase: review
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
deliverables: [docs/PUBLISHING.md, tests/test_publishing.py]
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

  **Answered by the owner on 2026-08-18: the set.**

  What §6 had to gain is smaller than expected: a fenced `# accepted` block of `<path> <lines>`
  rows. **It could not have been a set of matched *strings***, and that is the constraint the
  question did not see — §6's own rule forbids pasting a matched line into a document, so the
  accepted set can only ever name **locations**, never contents. Naming a path and a count is
  therefore not a compromise between the two options; it is the only machine-readable form the
  document's own rules permit.

  The prose that used to say *two lines from that one file is a pass* now points at the block instead,
  so the number has one home and changing what is accepted is one edit.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Give §6 a machine-readable accepted set, and make the prose point at it rather than restate the number | The edited docs/PUBLISHING.md |
| 2 | Write the test so that the pattern, the exclusion and the accepted set are all **lifted** from §6 and none is restated | The edited tests/test_publishing.py |
| 3 | Derive the known-positive set from the fixture's own markers rather than writing a count | Part of step 2, checked in §3 |
| 4 | **Make it fail**, in both of its failure modes, then restore the tree | The two runs, in §3 |
| 5 | Recover the two shapes repaired on 2026-08-18 from git and check the pattern against them | The before/after counts, in §3 |

**Decisions taken at `plan`**

- **Nothing about the rule is written in the test.** — T-126's reason applies, and a second one that
  is specific to this check and stronger: **the check reads the test file too.** A restated pattern
  would be a tripping literal in a tracked document, so the test would fail on its own source.
  Lifting is not tidiness here, it is what makes the test possible. — 2026-08-18
- **The known positives come from the fixture, not from the test.** — `tests/fixtures/leak-check/samples.txt`
  marks its own lines, so the test reads the markers and writes no count.
  *Rejected: asserting the documented five*, which is a number in a second home and would need
  editing whenever a class is added. — 2026-08-18

**Outputs this task will produce**

- docs/PUBLISHING.md — the accepted block, and the prose pointing at it
- tests/test_publishing.py — the lifted check and its three assertions

## 3. Implement

### A hazard hit while building the guard for it

Measuring the pattern in Python first gave **3** fixture lines where the documented command gives
**5** — the drive and UNC classes missing, which is to say both classes containing backslashes. It is
not a difference between POSIX ERE and Python: the pattern had **crossed a shell** on its way into a
probe, and arrived short. §6 warns about exactly this, one paragraph above the fixture it happened
to, and this session had already been bitten once the same day.

Lifting the pattern out of the document and compiling it in Python gives 5, identical to the
documented run. **So the finding is an argument for the design rather than an obstacle to it**: a
restated pattern is not merely a second home, it is a second home that can silently differ from the
first, and the difference presents as a class that quietly stops firing.

### Steps 1–3 — the shape

§6 gained a fenced `# accepted` block naming a path and a line count; its prose now points there
instead of repeating the number. The test lifts three things from §6 — the `grep -nIE` pattern, the
`':!...'` exclusion and that block — and raises rather than skips on any shape it cannot read, which
is `gate_from_the_document`'s rule applied to the neighbouring section.

The known positives are read from the fixture's own markers, `<- must be caught` and
`<- must be ignored`, so no count is written in `tests/`. The fixture currently marks 5 and 4.

### Step 4 — made to fail, both ways

```text
baseline                        exit=0  3 passed
case 1: new tripping file       exit=1  1 failed, 2 passed
case 2: extra hit in T-085      exit=1  1 failed, 2 passed
restored                        exit=0  3 passed
```

**Case 2 is the one that justifies the earlier design decision.** A pathspec exclusion for T-085 —
the obvious way to quiet the check, rejected in
[T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md) — would have
made that case pass silently, because the file would not have been read at all. The accepted set
catches it because it holds a count per file rather than a list of files to ignore.

The specimen was written to disk by a script and never passed as a shell argument, for the reason the
first paragraph of this section records. The home-directory class was used because it carries no
backslash at all.

### Step 5 — would it have caught the four?

Recovering the two repaired on 2026-08-18 from `01f0a4c`, the commit before the repair:

```text
T-129-release-v0-5.md                                    before=1  after=0
T-142-stop-the-entry-point-stating-the-path-mechanism…   before=1  after=0
```

Both would have appeared as a file the accepted set does not name, and failed
`test_every_hit_is_one_the_document_accepts`. **T-013 and T-018 are not checked here**: they predate
the fixture and §6's present shape, and §6 already counts them itself — an honest gap rather than a
claim of four out of four.

**Decisions & assumptions**
- Both `plan` decisions held. — 2026-08-18
- **Assumption, recorded as one**: Python's `re` and the documented `grep -nIE` agree on this
  pattern. Checked on the fixture — 5 and 5, the same lines — rather than assumed, and the check is
  in the suite as `test_the_fixture_still_proves_the_pattern_can_fire`. A pattern using a construct
  the two read differently would break that test, which is where it should break. — 2026-08-18
- Binary files are skipped, matching `grep -I` in the documented command. — 2026-08-18

**Outputs produced**
- docs/PUBLISHING.md
- tests/test_publishing.py

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Fails when a new tripping line is added to a tracked document, shown by adding one | **met** | §3 step 4, case 1, and case 2 goes further — an extra hit **inside** the accepted file also fails, which is the case a pathspec exclusion would have missed |
| Reads the command, exclusion and accepted set from the document; an unparsable shape is a failure, not a skip | **met** | Three `AssertionError`s, one per part, each naming what drifted. `skipUnless` is used only for a missing `git`, matching the neighbouring gate |
| Both of §6's runs asserted | **met, differently than written** | The two runs are asserted as two tests rather than two invocations: the accepted set over the scanned tree, and the fixture's marked lines over the pattern. Same two contracts, and the second no longer needs the exclusion dropped to prove the pattern fires |
| Editing §6's accepted set alone makes the test agree, nothing edited in `tests/` | **met** | The block is the only place a path or a count appears; the test parses it. Demonstrated in reverse by case 2, where the tree changed and the block did not, and the test failed |
| Behaviour without `git` matches the neighbouring gate test | **met** | Same `@unittest.skipUnless(GIT, …)` and the same reason in the message |
| The historical shapes would have been caught | **met, with a stated gap** | The two from 2026-08-18 recovered from git: 1 hit each before, 0 after. T-013 and T-018 predate the fixture and are not checked — said plainly rather than counted as four of four |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner and the answer turned out to be narrower than either
option: §6's own no-pasting rule means an accepted set can name locations and never contents, so
*path plus count* was the only permitted machine-readable form. That constraint is recorded in §1
because it will bind anyone who later wants to accept a hit that is not a whole line.

**Child fix tasks raised**
- none

## Log


| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-18 | → done | `specify` through `review` in one session. The owner chose the **set**, and the form turned out narrower than the question imagined: §6 forbids pasting a matched line into a document, so an accepted set can name **locations and never contents** — *path plus count* is the only machine-readable form its own rules permit, not a compromise. Nothing about the rule is written in `tests/`, for T-126's reason and a stronger one specific to this check: **the check reads the test file too**, so a restated pattern would be a tripping literal that fails the test on its own source. **A hazard was hit while building the guard for it** — the pattern measured 3 fixture lines in Python against the documented 5, both backslash classes missing, because it had crossed a shell; lifting it from the document gives 5, which turns the incident into an argument for the design. Made to fail two ways and restored, and case 2 — an extra hit *inside* the accepted file — is the one a pathspec exclusion would have passed silently, which retrospectively justifies T-183's refusal to use one. Both 2026-08-18 shapes recovered from git would have been caught; T-013 and T-018 predate the fixture and are stated as a gap rather than counted. |
| 2026-08-18 | → proposed | Raised at the owner's request, from a residue recorded in [T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md)'s review rather than left to die there with the closing task. **The request was for a guard on §6's two remedies and the investigation reframed it**: the check already detects both, which is how all four instances were found, so the gap is that nothing runs it. That makes this T-126 applied one section later, and T-126 is why the shape is known to work. Only reachable at all because T-183 turned §6's unreachable *must print nothing* into a countable condition. One genuinely open question — count or set — which is the owner's because it decides how machine-readable §6 must stay. |
