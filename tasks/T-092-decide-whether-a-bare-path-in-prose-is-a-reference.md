---
id: T-092
title: Decide whether a bare path in prose is a reference check must resolve
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-093, T-094, T-095, T-034]
work_package: v0.2
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-11
deliverables: [tests/test_cli.py, README.md]
---

# T-092 — Decide whether a bare path in prose is a reference check must resolve

## 1. Specify

**Outcome**
A project is told whether `check` validates a path written as prose, and if it does, the rule that
decides what counts — so a project retiring its own link checker knows what it is giving up before
it deletes anything.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`) after migrating a 61-task project
off a mature bespoke checker onto taskmd 0.1.1. Reproduced here on a two-file throwaway project: a
task naming one missing document as a Markdown link and another as a bare path in prose produces

```
BROKEN LINK   tasks/T-001-x.md -> also-gone.md

1 problem(s) over 1 task(s)
```

— one problem, not two. `LINK` matches Markdown link syntax only, so the prose path is not a
reference as far as `check` is concerned. In that project it is not an edge case: it validates
around a thousand document pointers and a large share are bare, **because tools print them into
fenced blocks**.

**Why this is an adoption hazard, not a missing feature.** The migration nearly deleted that
project's checker on the strength of the two tools' command lists matching — `context`, `index`,
`check` on both sides. The lists match and the coverage does not, and nothing says so. That framing
is the reporting project's and it is the part worth keeping: a project that adopts taskmd and retires
its own checker loses this silently.

**This repository would not have noticed.** Its own prose cites paths in backticks constantly, and
`check` has never looked at one — which is also the shape of the defect
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) found in the leak check, where
the thing that read none of the files it was aimed at printed nothing and looked like success.

**Requirements served**
R-16, and R-13 in the sense that a reference that resolves is what the validator is for.

**Scope**
- In: whether a path-shaped token in prose is a reference at all. **This is the decision**; the
  mechanism is downstream of it.
- In: if yes, the rule that separates a pointer from a path merely being discussed. The reporting
  project's rule is that the token's first segment must be a real directory in the project, kept in
  a function it named `points_into_repo`.
- In: what a false positive costs here. `CLAUDE.md` already argues, for the leak check, that a check
  which cries wolf gets ignored — quoting another project's layout in prose is the obvious class.
- Out: section references, which are [T-093](T-093-decide-whether-check-resolves-a-section-reference.md).
- Out: whether it is opt-in or always on, until the first question is answered.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `LINK` and `check_links`.
- The reporting project's `tools/docs/refcheck.py`, offered MIT as a working reference.
- `CLAUDE.md` *The pre-publish check*, for the crying-wolf argument and the three deliberate limits.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If it is in: a fixture holds a dead bare path and `check` reports it, shown failing first
- [ ] If it is in: a fixture holds a path-shaped token that must **not** be reported, so the
      false-positive boundary is proven rather than asserted
- [ ] If it is out: the adopter-facing documentation says what `check` does not look at, so the next
      project to retire its own checker is told

**Open questions**
- ~~**In or out.**~~ **Answered 2026-08-10 (§3): out**, and answered by measurement rather than by
  argument — the rule was built, run over this repository, and read.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the reporting project's rule for real — path-shaped token, first segment names a real directory here — and run it over this repository before deciding anything | a number, below |
| 2 | Read what it reported and classify it, rather than counting it | §3 *The measurement* |
| 3 | Decide, and record the rejected alternatives where the decision is | §3 |
| 4 | Pin the decision so the documentation cannot drift from the behaviour | `ABarePathInProseIsNotAReference` in `tests/test_cli.py` |
| 5 | Tell an adopter what they are giving up, on the front door rather than in a task | `README.md` |

## 3. Implement

**The measurement**

The rule was implemented, not estimated: a path-shaped token counts when its first segment names a
real directory in the project, with glob metacharacters excluded and Markdown links blanked first so
nothing is validated twice. Run over this repository, on top of [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md)
so that quarantined documents were already out of scope:

```
237 problem(s) - ..., 124 document(s), 947 link(s), 683 bare path(s)
```

**Of the 237, none was a defect.** They fall into three classes, and the first is the finding:

- **235 sat in task records that correctly described a tree that has since moved** — a July record
  naming the file it edited, before [T-083](T-083-make-the-skill-directory-self-contained.md)
  relocated the package or [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) moved the
  template. A task record is a **dated statement, not a promise**, and a tracker accumulates them
  structurally. This is not this repository being untidy; it is what a tracker is.
- Fabricated example filenames written to explain a rule — the id-width probe, the ordering example.
- The 2 outside `tasks/`: a config naming where the live handoff file *will* be, and frozen prior art
  citing its original project's layout. The second is exactly the class `CLAUDE.md` names when it
  argues the leak check must not cry wolf — another project's paths, quoted, colliding with a
  directory that happens to exist here.

**Decisions & assumptions**

- **Out: a bare path in prose is not a reference `check` resolves** — 2026-08-10. `CLAUDE.md` had
  already settled this trade for the leak check — a check that cries wolf gets ignored, which is
  worse than a narrow one — and 237 alarms with no defect among them is not a threshold question.
  The cost falls on adopters, so the gap is documented on the front door and held by a test.
- **Rejected: in, always on** — 2026-08-10. The measurement above. Note what it does *not* say: the
  rule is not badly built and the tokens are not ambiguous — 446 of the 683 resolved correctly. The
  rule works and the corpus is wrong for it, which is the more useful finding and the harder one to
  reach by reasoning.
- **Rejected: in, restricted to documents outside the task folder** — 2026-08-10. The strongest
  rival on the numbers, and it was measured rather than assumed: it takes 237 reports down to 2. Both
  survivors are still false, so the signal is zero either way — and it would exclude precisely the
  corpus that motivated the request, since the reporting project's bare paths are in fenced blocks
  inside records.
- **Rejected: in, behind a config key, default off** — 2026-08-10. It preserves the reporting
  project's coverage and answers the silence, which is the real complaint. Rejected because the
  measurement is about the rule, not about this project's taste: a key would ship a check this
  project cannot run on itself, and a feature its author never runs rots. A default-off key is also
  the same silent loss for anyone who does not read the config.
- ~~**Assumption, recorded because the work survives it being wrong**~~: that the reporting project's
  bare pointers live in documents shaped like its records rather than like `README.md`. **Verified on
  its corpus the same day — see below.** It holds, and the verification is worth more than the
  assumption was.

**Verification on the reporting project — 2026-08-10**

The same rule, run over the deck-building sibling's own tree rather than this one. It answers the
assumption above and it answers it harder than expected:

| | Here | The reporting project |
| :--- | ---: | ---: |
| Markdown links (dead) | 947 (0) | 1561 (**0**) |
| Distinct bare pointers | 683 | 481 |
| — of them in the task folder | 235 of 237 dead | 388, holding 27 of 31 dead |
| Dead bare pointers outside it | 2 | 4 |

**81% of its bare pointers are in task records, and so are 27 of its 31 dead ones — and 19 of those
27 name one file: the pre-split task tool its own T-062 retired.** That is this task's finding
reproduced on the project that reported the gap, in a corpus that had never been looked at through
it: a record naming a tool that has since been removed is a correct dated statement, and the checker
calls it broken. The remaining 8 are cache artefacts named as evidence, a bare `examples/README`
without its extension, and an id prefix written with an ellipsis.

The 4 outside the task folder do not rescue the restricted variant either: one is
`.handoff/config.md` naming where the live handoff file *will* be — **the identical false positive
this repository produced**, so that class is general rather than local — one is a research id that is
not a path at all, and two are hook scripts named in config prose. So the restricted rule scores 4
reports and at best 2 arguable defects on the very project whose loss motivated the request.

**Also worth the record: 1561 Markdown links, none dead.** Everything `check` does cover was already
clean there, which is why the coverage question felt like the whole question from that side.

**Outputs produced**
- `tests/test_cli.py` — `ABarePathInProseIsNotAReference`, three cases
- `README.md` — the coverage statement in *Which documents `check` reads, and which pointers in them*
- No change to `plugin/skills/taskmd/taskmd/cli.py`. The rule was written to be measured and then
  removed; what survives is the number and the test that the number stays true.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative, whichever way it goes | met | Three rejections in §3, two of them with their own measurement rather than a reason. |
| If it is in: a fixture holds a dead bare path and `check` reports it, shown failing first | n/a | It is out. The negative is held instead: a dead bare path in a throwaway project is asserted **not** reported, and a companion case writes the same target as a Markdown link and asserts it **is** — without that, the first test would pass equally well if link-checking had stopped working altogether. |
| If it is in: a fixture holds a path-shaped token that must not be reported, so the false-positive boundary is proven rather than asserted | met, in the form the answer allows | The boundary was proven at a scale no fixture reaches: 683 tokens over this repository's real corpus, classified rather than counted. That measurement is what decided the task, so the criterion did its job even though the branch it was written for did not happen. |
| If it is out: the adopter-facing documentation says what `check` does not look at, so the next project to retire its own checker is told | met | `README.md`, with the number, so a reader can judge the trade instead of taking the omission on trust. Asserted by a test against the shipped file — a documented gap that quietly loses its documentation is this task's own finding, one level up. |

**Child fix tasks raised**
- none. [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) was already the sibling
  question about section references and is unchanged by this; it is now the only one of the pair
  still open, and this record is the evidence it should read first.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-10 | (no change) | The one assumption this record carried was verified rather than left standing, on the reporting project's own corpus — the only place it could be. It holds: 81% of that project's bare pointers, and 27 of its 31 dead ones, are in task records, 19 of them naming the single tool its own T-062 retired. The decision does not move; what moves is that the strongest rival was rejected on two independent corpora instead of one. Its `.handoff/config.md` produces the identical false positive this repository does, which promotes that class from local quirk to general. |
| 2026-08-10 | → done | Out, and the interesting part is how it was decided: the feature was built, run, and read before the decision, which cost about an hour and produced a number that no amount of reasoning would have. The reasoning available beforehand pointed the other way — the reporting project validates a thousand pointers with this rule and it works for them. What it cannot see from there is that a taskmd corpus is mostly *dated records*, so the same rule that validates a documentation tree cries wolf over a tracker. Shipped with [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) and the manifest bump. |
| 2026-08-10 | → specified | The open question was left as posed. What changed at specify was the method for answering it: build the rule and measure it rather than weigh the two risks, because both sides of the argument were plausible and neither was checkable from the armchair. |
| 2026-08-09 | → proposed | Raised from a real migration rather than from review: the deck-building sibling moved 61 tasks off its own checker onto taskmd 0.1.1 and measured what that would cost before doing it. Reproduced here on a throwaway project — a dead bare path in prose is invisible, a dead Markdown link is caught, and `check` reports one problem where two exist. `high` because the loss is silent and the adoption path invites it: the two tools' command lists match and their coverage does not. |
