---
id: T-137
title: Decide what taskmd does about a grouping label that can be read as a version
type: decision
status: specified
phase: specify
parent: null
blocked_by: []
related: [T-004, T-082, T-087, T-088, T-100, T-106, T-136]
work_package: v0.6
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
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-12 | → specified | Both questions answered by the project owner: an advisory `check` line keyed on value shape with no new config key, and ship the wording fix alongside it. Their rivals are recorded beside them. **Authorisation (METHOD §3.1):** *full lifecycle on T-136 and T-137*, from the project owner on 2026-08-12, given with the answers. It covers this task end to end — specify through review — and nothing beyond the two tasks it names. The build the answer licenses is **not** covered: this task's scope puts it out, so it is raised rather than run. |
| 2026-08-12 | → proposed | Raised when a second project using this plugin hit the defect this repository has been carrying since it grouped its backlog, and the maintainer asked for a remedy that reaches adopters rather than only this tree. Kept separate from [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) because the mechanism question here is genuinely open and would otherwise hold a rename whose evidence is already in hand. **Typed `decision` on the shipped test**: the outcome is an answer someone else could act on, and the change cannot be named until it is given — both obvious mechanisms are closed by recorded decisions, so what is left is a choice rather than a build. |
