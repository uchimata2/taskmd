---
id: T-137
title: Decide what taskmd does about a grouping label that can be read as a version
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-004, T-082, T-087, T-088, T-100, T-106, T-136, T-138]
work_package: M6
owner: the project owner
business_value: high
effort: l
created: 2026-08-12
updated: 2026-08-12
deliverables: []
---

# T-137 — Decide what taskmd does about a grouping label that can be read as a version

## 1. Specify

**Outcome**
An answer to whether taskmd does anything at all when a project labels its work with something a
reader will resolve as a version, and if so which of its existing surfaces carries it. The answer
names the mechanism, states what it costs every adopting project, and is decided against the two
constraints that make the obvious mechanisms unavailable. Whoever implements it after that is
building, not choosing.

**Why this one**

Two independent projects using this plugin have now shipped the same defect, and one of them is this
repository ([T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md)). Both
grouped a backlog into milestones, both named the milestones after the version they expected to ship
in, and in both the two number spaces came apart — because a release takes the next number on the
published line whatever grouping its tasks belong to, so the sequences are independent by
construction and only look coupled at the start.

**A defect two adopters reach independently is a product defect, not a backlog defect.** taskmd
teaches a project how to label work: the shipped template says
`work_package: <the release or grouping this belongs to>`, and the shipped default names
`work_package` in both views. A project follows that, picks a version number because the field says
*release*, and gets a label that resolves to a real tag and means something else. Nothing in the tool
notices, because nothing in the tool has an opinion about what a label may look like.

**The scale is what makes it worth deciding rather than tolerating.** This repository ran 135 tasks
before the cost was visible, and the cheaper remedy it took at the time — a hand-written mapping
table — is the duplication this plugin exists to remove. An adopter who reads only what taskmd ships
has no warning at all.

**What makes this a decision and not a fix.** Both obvious mechanisms are already closed by recorded
decisions in this project, and neither closure is one to overturn casually:

- **taskmd has no concept of a milestone field.** `work_package` is not a schema key. It appears only
  inside `context_fields` and `index_columns`, which take any field name at all — that is deliberate,
  and it is what lets a project adopt taskmd without rewriting its task files. So a check that reads
  *the* grouping field needs a key naming it, and
  [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) established that **the moment the
  default config gains a key, every project that wrote its own config fails on the next upgrade**,
  naming a key nobody there has heard of.
- **There is no setup command to generate anything into.** No taskmd command creates a folder and
  there is deliberately no `init`, so *automatically generate a correct schema* has no surface to
  arrive on without inventing one.

So the question is real, the cheap answers are unavailable, and the shape of the remaining answer is
what somebody is waiting on before anything can be built.

**Scope**
- In: whether taskmd ships anything, and which existing surface carries it — `check`, the shipped
  default config, the task template, the method, or nothing.
- In: what the chosen mechanism costs a project that meant its labels, since a validator that fails
  on a legal state is one projects start passing flags to
  ([T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md)).
- In: whether the answer needs a config key, and if so whether it is worth T-106's price. Deciding
  *no key* is a legitimate outcome and is the recommendation below.
- Out: building it. This task ends with an answer; the build is raised from it.
- Out: relabelling this repository, which is
  [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) and does not wait
  on this answer.
- Out: **the task id scheme** — `T-NNN`, `id_prefix`, `id_width`, and ids a backend allocates. That
  is a different schema and it is settled
  ([T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md),
  [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md)). This task is about the labels a
  project invents for its own groupings.
- Out: teaching a project how to number its releases. taskmd has no opinion about versions and is not
  acquiring one; the subject is only whether a *label* can be mistaken for one.

**Inputs**
- [`../plugin/skills/taskmd/taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)
  — *Adding a key to this file is a breaking change*, and *When this file moves ahead of yours*, which
  is the one advisory line class `check` already has.
- [`../docs/SCOPE.md`](../docs/SCOPE.md) — the numbered requirements and the explicit non-goals. Which
  requirement this serves, or that it serves none, is read from there rather than asserted here.
- [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) — the precedent
  for a `check` line that is advisory, moves no exit status, and cannot be switched off.
- [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) — what it took
  to change a shipped vocabulary once two projects had reached for the same value.
- [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) — the measured
  case, including which of five labels were true, false, and true by accident.

**Acceptance criteria**
- [ ] The answer names one mechanism and one surface, and says what a project that deliberately uses
      version-shaped labels reads on every run.
- [ ] It states whether a config key is required, and if not, how the mechanism knows what to look at
      without one.
- [ ] The rejected alternatives are recorded with what going each way costs, not with why they were
      rejected — at least the two closed by T-106 and by the absence of `init`.
- [ ] It is decided against the real corpus, not in the abstract: whatever rule is proposed is run
      over this repository's 135 tasks **and** over the shipped fixtures, and its output read. A rule
      nobody ran on real data is a guess.
- [ ] If the answer is a check, it is shown to **fail** on a project that has the defect and to stay
      silent on one that does not. A clean pass proves nothing.
- [ ] If the answer is *taskmd ships nothing*, that is written down with what an adopter is left to
      discover for themselves, so the next adopter report does not re-open it from scratch.

**Open questions**
- none. Both were put to the project owner and answered on 2026-08-12.

**Q1 — the mechanism. Answered: an advisory `check` line with no new config key**, keyed on the
shape of a front-matter value rather than on the name of a field. taskmd already reads every field
value of every task, so a two-part number where a real version has three parts is visible without
knowing which field is the milestone. It reuses the T-100 line class exactly: advisory, exit status
unmoved, no flag to silence it. *Rejected: a new config key naming the grouping field.* It is the
only mechanism with correct semantics rather than a heuristic, and it costs every project that wrote
a config a failed upgrade with an error naming a key they never chose — T-106's price, paid by
everyone, for a defect that fires once per project.

**Q2 — whether it ships at all, versus documentation alone. Answered: both** — the check, and the
template and default-config wording that pointed adopters at a version in the first place. Wording
alone is the weaker half of the pair: a project copies the default config once and then stops reading
it, which is the exact failure the drift line was written to catch. *Rejected: wording alone.* It
costs nothing, adds no false positives, and is silent for the project that has already copied the
file — which is every project by the time the label matters.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Write a throwaway detector for the candidate rule and run it over this repository's 137 tasks — the corpus known to have the defect | Recorded output, §3 |
| 2 | Run the same detector over the shipped fixtures and both templates — the corpora that should be quiet | Recorded output, §3 |
| 3 | Settle the rule's predicate from what the two runs flagged, including every exemption the data forces rather than the ones imagined | The rule, §3 |
| 4 | Price the answer: what a project that means its labels reads on every run, and what the rejected config key would have cost | §3 |
| 5 | Record the answer and raise the build it licenses | §3, a new task |

**Shape decisions.**

**D1 — the rule is built in order to decide whether to have it.** An in-or-out question about a
validator is settled by running it over the real corpus and reading its alarms, not by arguing about
its predicate in the abstract. The detector written here is a throwaway and is not the shipped one;
its only product is the numbers §3 records.

**D2 — the measurement is taken before T-136's rename, and that fixes the order of the two tasks.**
This repository *is* the corpus with the defect, and T-136 removes it. Measured afterwards, the run
would report a clean tree and prove nothing about a rule meant to catch what the tree used to
contain. So T-137 goes first, and its output becomes the before-half of T-136's own evidence.

**Planned outputs**
- §3 and §4 of this file
- one new task, for the build this answer licenses

## 3. Implement

### Steps 1 and 2 — the rule, run over both corpora

A throwaway detector reads every front-matter scalar and list item and reports any value shaped like
a dotted number, split by how many components it has. Run before T-136's rename, so this repository
is still the corpus with the defect:

```text
=== this repository: 141 file(s) ===
  TWO-PART - reads as a version      work_package: 'v0.1'  x67
  TWO-PART - reads as a version      work_package: 'v0.2'  x47
  TWO-PART - reads as a version      work_package: 'v0.3'  x4
  TWO-PART - reads as a version      work_package: 'v0.5'  x11
  TWO-PART - reads as a version      work_package: 'v0.6'  x8

=== shipped fixtures: 53 file(s) ===
  (no dotted-number value in any front matter)

=== shipped defaults: 1 file(s) ===
  (no dotted-number value in any front matter)
```

**137 hits here, 0 in 53 fixture files, 0 in the shipped default.** The signal is the whole defect
and nothing else. Note what the first run also showed: **no task front matter in this repository
carries a three-part value at all**, so the two-part / three-part distinction was untested by the
real corpus and had to be probed rather than assumed.

### The probe — what a legitimate project can put there

Three fabricated projects, written to break the rule rather than to confirm it: one estimating effort
in days, one recording the version its work shipped in, one with the defect under a field name taskmd
has never heard of.

```text
  TWO-PART - reads as a version      effort: '1.5'  x1
  TWO-PART - reads as a version      milestone: '2.1'  x1
  TWO-PART - reads as a version      work_package: 'v0.2'  x1
  3-part                             shipped_in: '0.4.0'  x1
  3-part                             target: 'v1.2.0'  x1
```

Four of the five are right. `M2` and `PH3` — the shape T-136 adopts — are silent, which they must be
or the remedy would trip the warning. `shipped_in: 0.4.0` and `target: v1.2.0` are real versions
recorded correctly and are left alone. **`milestone: 2.1` is the one that settles the config-key
question**: the rule caught the defect under a field name that appears in no schema, which is exactly
what a rule keyed on a field name could not have done without T-106's price.

**`effort: 1.5` is a genuine false positive**, and it is the only one the probe could produce. Re-run
with the two estimate fields exempt, it goes and nothing else moves:

```text
=== probe, with the estimate fields exempt: 3 file(s) ===
  TWO-PART - reads as a version      milestone: '2.1'  x1
  TWO-PART - reads as a version      work_package: 'v0.2'  x1
  3-part                             shipped_in: '0.4.0'  x1
  3-part                             target: 'v1.2.0'  x1
```

### Step 4 — what it costs

A project that means its two-part labels reads one line per distinct label, for ever, with no flag to
turn it off. Here that would be five. **It would have been 137**, which is the run above, and which is
why the line is per value and not per task — a warning that prints once per file is one a reader
scrolls past on its first appearance.

**Decisions & assumptions**
- **D1 — the predicate is a front-matter value matching `v?N.N`, exactly two components** —
  2026-08-12. Three or more is a version recorded correctly and is left alone, proven by
  `shipped_in: 0.4.0` and `target: v1.2.0` staying quiet in the probe. A two-part number is the only
  shape that is a prefix of a real version and therefore resolves to one.
- **D2 — no config key, and the field name is not read at all** — 2026-08-12. The rule looks at value
  shape, so it needs no opinion about which field is the milestone. Measured rather than argued:
  it caught `milestone: 2.1` in the probe. *Rejected: a key naming the grouping field* — correct
  semantics instead of a heuristic, at T-106's price of a failed upgrade for every project that
  wrote a config, to catch a defect that fires once in a project's life.
- **D3 — the fields named by `effort_field` and `value_field` are exempt** — 2026-08-12. Forced by
  the data: `effort: 1.5` was the single false positive the probe could produce, and both keys
  already exist, so the exemption is derived from the config rather than added to it. A dotted number
  in some other numeric field is residual risk, and it costs one advisory line.
- **D4 — one line per distinct value, not per task** — 2026-08-12, from the 137-line run above.
- **D5 — advisory, exit status unmoved, no flag to silence it** — 2026-08-12. The T-100 line class
  exactly, for the reason recorded there: a validator that fails on a legal state is one a project
  starts passing flags to. Version-shaped labels are legal.
- **Assumption: the shipped fixtures stay quiet as they are.** Proven above at 53 files, so the build
  needs a fixture of its own to prove the alarm direction and cannot reuse an existing one.

**Outputs produced**
- §3 and §4 of this file — the answer, its price, and the two runs it rests on
- [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) — the build this licenses

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Names one mechanism and one surface, and says what a project that deliberately uses version-shaped labels reads on every run | met | An advisory line on `check`, one per distinct value, unsilenceable. Here that would be five lines; §3 step 4 gives the number and why it is not 137 |
| States whether a config key is required, and if not, how the mechanism knows what to look at | met | D1–D3. It reads value shape and never a field name, so there is nothing to configure. The `milestone: 2.1` hit is the proof, not the argument |
| Rejected alternatives recorded with what going each way costs | met | D2 records the config key and T-106's price; D5 records the failing-check option and why a legal state must not fail. Q1 and Q2 in §1 carry the owner's two rejections |
| Decided against the real corpus and the shipped fixtures, and their output read | met | §3 steps 1–2: 137 hits across 141 files here, 0 across 53 fixtures, 0 in the shipped default |
| Shown to fire on a project that has the defect and stay silent on one that does not | met | Both directions, and the silent direction twice: 53 fixtures, and a probe built to break it. The probe is what found the one false positive and forced D3 |
| If the answer is *ship nothing*, that is written down | n/a | The answer is to ship |

**Child fix tasks raised**
- [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) — the build

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → done | **The measurement decided it, and it decided differently from the argument.** Three things were settled by running the rule rather than by reasoning about it. The field-free predicate looked like a compromise for dodging T-106's price and turned out to be strictly better: it caught `milestone: 2.1` under a field name no schema mentions, which a key-based rule could not have seen at all. The two-part / three-part split was **untested by the real corpus** — no task front matter here carries a three-part value — so it had to be probed, and the probe is also what produced the single false positive (`effort: 1.5`) that forced the estimate-field exemption. And the line granularity was decided by a number nobody would have guessed at: per task, this repository would print **137 lines**, which is a warning read once and scrolled past for ever. Ordered before T-136 deliberately: this tree is the corpus with the defect, and the rename removes it. |
| 2026-08-12 | → in_progress | Plan agreed under the owner's authorisation. Ordered before T-136 for the reason in D2 — measuring after the rename would report a clean tree and prove nothing about the rule under test. |
| 2026-08-12 | → specified | Both questions answered by the project owner: an advisory `check` line keyed on value shape with no new config key, and ship the wording fix alongside it. Their rivals are recorded beside them. **Authorisation (METHOD §3.1):** *full lifecycle on T-136 and T-137*, from the project owner on 2026-08-12, given with the answers. It covers this task end to end — specify through review — and nothing beyond the two tasks it names. The build the answer licenses is **not** covered: this task's scope puts it out, so it is raised rather than run. |
| 2026-08-12 | → proposed | Raised when a second project using this plugin hit the defect this repository has been carrying since it grouped its backlog, and the maintainer asked for a remedy that reaches adopters rather than only this tree. Kept separate from [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) because the mechanism question here is genuinely open and would otherwise hold a rename whose evidence is already in hand. **Typed `decision` on the shipped test**: the outcome is an answer someone else could act on, and the change cannot be named until it is given — both obvious mechanisms are closed by recorded decisions, so what is left is a choice rather than a build. |
