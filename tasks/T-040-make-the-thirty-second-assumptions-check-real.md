---
id: T-040
title: Make the thirty-second assumptions check real, or change the number
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-009, T-010, T-028]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-07
updated: 2026-08-07
deliverables:
  - plugin/docs/BINDING.md
---

# T-040 — Make the thirty-second assumptions check real, or change the number

## 1. Specify

**Outcome**
Either both existing bindings' assumptions sections can be checked in the time `docs/BINDING.md` §4
claims, or §4 states a figure that measurement supports — with the decision resting on a measured
number rather than on how the sections feel to read.

**Why this one**
T-010's criterion 4 required its assumptions section to be "checkable in thirty seconds". Measured
at review rather than asserted:

| Binding | Words | At 250 wpm |
| :--- | ---: | ---: |
| `docs/bindings/github-issues.md` | 498 | ~120s |
| `docs/bindings/local-markdown.md` | 401 | ~96s |

Four times the budget, and three times it for the binding that predates this task. So this is not
one section that ran long — **the bar has never been met by anything, including the binding it was
written alongside**, and it went unnoticed because nobody measured it. That is the specific failure
this project exists to remove: a claim in a document that no artefact satisfies, repeated by every
new artefact that copies the shape of the old one.

The number matters more than a style rule would, because §4's whole argument is that an adopter
will actually perform this check. A section nobody finishes reading is checked by nobody, and the F1
failure §4 was written to prevent comes back — an unchecked premise is an unchecked premise whether
it is unstated or merely unread.

**Scope**
- In: deciding whether the sections shrink or the figure changes, and applying that to both existing
  bindings and to §4. Whether "check" means read-through or something stronger, since that is what
  the figure is measuring.
- Out: the content of the assumptions themselves — whether each is *correct* is its own binding's
  business. This task is about whether the set can be checked in the time claimed.

**Inputs**
- `docs/BINDING.md` §4, which sets the figure and lists the five minimum entries driving the length
- Both bindings under `docs/bindings/`
- T-028, which is doing the same kind of work for the always-loaded spine — a budget stated, then
  measured against the thing it governs. Its outcome may supply the method for this one.

**Acceptance criteria**
- [ ] The figure in §4 and the measured time for both bindings agree, and the measurement is
      recorded so the next binding can be checked the same way
- [ ] Whichever way it is resolved, the five minimum entries survive — shrinking a section by
      dropping an entry defeats the point, and §4 says a binding states its position even when the
      answer is "none"
- [ ] If the sections shrink, no assumption is lost, only compressed — shown by listing the
      assumptions before and after and pairing them off
- [ ] The check is defined well enough that two people measuring the same section get the same
      answer. "Checkable" currently names no procedure, which is why it was never tested

**Open questions**
- ~~Does "checkable in thirty seconds" mean *read* in thirty seconds, or *decide whether it applies
  to my project*?~~ — **decided during the work: the second, and it is the useful reading.** The
  question expected that to argue for changing the figure, since deciding is slower per word than
  reading. It argued the opposite once the unit was identified: what an adopter reads to decide is
  the bold claim opening each entry, not the paragraph explaining it. The prose exists for the case
  where the answer is "not sure", and charging the budget for text nobody reads on the fast path was
  the measurement error, not the figure.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Identify what an adopter actually reads to answer "is this true of my project?" — the whole entry, or the claim it opens with. The figure cannot be judged until the unit is named, which is why it was never judged. | A stated unit, in §3 |
| 2 | Measure both bindings against that unit, the same way, so the numbers are comparable to the ones that failed. | Word counts and read times for both, in §3 |
| 3 | Decide: shrink the sections, or state the unit in §4 and keep the figure. Record the rejection. | A decision in §3 |
| 4 | Write it into §4, including how to perform the check, so two people measuring get the same answer. | `docs/BINDING.md` §4, edited |
| 5 | Re-read both bindings' claim lines as an adopter would and note anything that cannot be answered — the figure is worthless if the entries are unanswerable at any speed. | A verdict in §3, and a finding if the entries do not hold up |

**Sequencing.** Step 1 precedes the measurement because measuring the wrong unit is the whole
failure being fixed here; repeating it faster would not help. Step 5 is last and deliberately looks
past this task's own question — a section that reads in fifteen seconds but cannot be answered is
worse than a slow one, and this is the only point where anyone will be looking at it.

**Shape of the deliverable — decided.** A paragraph in §4 defining the unit and the procedure,
beside the figure it governs. Rejected: a measurement script under `tests/`, which would make the
figure enforceable but turns an adopter-facing sentence into a build artefact — and non-goal 11
keeps the CLI to what it has. Rejected: dropping the number for "briefly", which removes the only
part of the claim that can ever be shown false.

**Output paths**
- `docs/BINDING.md` — §4

## 3. Implement

**Step 1 — the unit is the claim line.** Both existing bindings already have the shape: every
numbered assumption opens with one bold sentence carrying the whole claim, with explanation
underneath. An adopter deciding whether a premise is false for them reads the bold sentence; they
drop into the prose only when the answer is not obvious. So the section has two audiences at two
speeds, and the thirty seconds was being charged for both.

**Step 2 — measured against that unit**, alongside the whole-section figures that failed at review:

| Binding | Whole section | Claim lines only |
| :--- | ---: | ---: |
| `github-issues.md` | 498 words, ~120s | **65 words, ~16s** |
| `local-markdown.md` | 401 words, ~96s | **44 words, ~11s** |

Both inside the budget, with room. The figure was never the problem.

**Step 3 — decision: state the unit, keep thirty seconds.** Rejected: shrinking the sections. It
would have cost the explanations, and the explanations are what an adopter needs at precisely the
moment the check *fails* — which is the only moment the section matters. Compressing to hit a
budget that was being measured wrongly would have destroyed the useful half to satisfy an artefact
of the measurement.

**Step 5 — the verdict, and it found something.** Read as an adopter, several claim lines cannot be
confirmed or denied about *their* project, because they are not about their project:
`github-issues.md` 1 ("Ids are assigned by GitHub and cannot be chosen") and 2 (the `state`
rendering) describe the backend and the binding; `local-markdown.md` 3 ("Identity is chosen
locally") does the same. §4's second sentence already requires each entry to be a claim about the
adopting project — "not a description of the backend" — and three entries across two bindings
breach it. Out of scope here by this task's own boundary, which puts the content of the assumptions
with their bindings. Raised as **T-043**.

**Decisions & assumptions**
- **The figure stays at thirty seconds; §4 gains the unit and the procedure.** — Step 3. The number
  was defensible all along and only looked wrong because nothing said what it counted. — 2026-08-07
- **The failed measurement is written into §4, not just into this task.** — A future reader
  otherwise has a bare figure again, and the reason it survived unmeasured for so long is that a
  bare figure invites a glance and a tick. Recording that it was measured, and against what,
  is what stops the next person re-deriving it. — 2026-08-07
- **Neither binding's prose is touched.** — Nothing needed to shrink, and editing them anyway would
  have been a change made to match a conclusion rather than to fix a fault. — 2026-08-07

**Outputs produced**
- [`docs/BINDING.md`](../plugin/docs/BINDING.md) — §4 gains *What the thirty seconds measures*

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The figure and the measured time for both bindings agree, and the measurement is recorded | met | 65 words / ~16s and 44 words / ~11s against a 30s budget. Both figures and the method are in §4 itself, not only here, so the next binding is checked the same way rather than by whoever remembers this. |
| The five minimum entries survive | met | Nothing was removed from either binding — the resolution was to measure differently, not to cut. The five §4 entries are untouched, as is the requirement to state a position even when the answer is "none". |
| If the sections shrink, no assumption is lost, only compressed | n/a | They did not shrink. The criterion guarded the option that was rejected at step 3, and is recorded rather than deleted because it is what would have caught that option going wrong. |
| The check is defined well enough that two people measuring get the same answer | met | §4 now names the unit (the bold claim opening each entry), excludes the prose, and gives the procedure — read the bold leads in order, stop at the first you cannot answer. Before this, "checkable" named no procedure at all, which is why it went untested through T-009 and T-010. |

Three met, one moot. The task began as "the sections are too long" and ended as "the budget was
counting the wrong text" — and the whole-section overrun that triggered it was real, but was a
symptom of an undefined measure rather than of bloated prose.

**Child fix tasks raised**
- **T-043** — three claim lines across both bindings describe the backend rather than making a claim
  about the adopting project, which §4 already forbids. Found by step 5, out of scope here.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-07 | → done | Three criteria met, one moot. The task was raised as "the sections are too long" and resolved as "the budget counted the wrong text": what an adopter reads to decide is the bold claim opening each entry, and against that unit the two bindings measure 65 and 44 words — 16s and 11s against 30. Neither binding was edited, since nothing needed to shrink. §4 now states the unit, the procedure and the failed whole-section measurement, so the figure can be checked rather than glanced at. The last plan step looked past the question and found three claim lines that describe the backend instead of asking the adopter anything, which §4 already forbids → T-043. |
| 2026-08-07 | → proposed | Raised by T-010's review, where criterion 4 was judged **not met** on measurement. Scoped to both bindings and to §4 rather than to T-010's section alone, because the older binding misses the same bar — a fix confined to the new one would leave the claim false and the precedent intact. |
