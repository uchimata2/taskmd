---
id: T-244
title: Audit everything 0.6.0 ships before 1.0.0, and review the audit method while using it
type: audit
status: proposed
phase: specify
parent: null
blocked_by: [T-243, T-245]
related: [T-223, T-231, T-152]
work_package: M7
owner: the project owner
business_value: critical
effort: xl
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-244 — Audit everything 0.6.0 ships before 1.0.0, and review the audit method while using it

## 1. Specify

**Outcome**
Everything an adopter receives at `v0.6.0` has been examined, every item in scope ends in exactly one
of the three states [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) §2
names, and the findings are ranked and raised. Second, a recorded judgement on **the audit method
itself**, which has never been run.

**Why this one**
The owner asked for it on 2026-08-23, immediately after `v0.6.0` was published, and set the frame:

- **`0.6.0` is a beta, or a release candidate.** It is published and it is the latest release on
  GitHub, which the owner chose on 2026-08-23 over flagging it a prerelease, because that would show
  `v0.5.0` as latest and point a visitor at older software. The beta framing lives here and in the
  backlog rather than on the release page.
- **`1.0.0` follows this audit and the application of its findings**, and is carried by
  [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md), which is blocked by this record.
- **The audit machinery is under review at the same time as the subject.** This is its first run.
  [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) shipped
  `pre-release-audit.md` to every adopter on the strength of one project's practice and no execution,
  so the document is currently a claim. This record is the case that tests it.

**Two things this repository already knows about auditing itself, and neither is optional here**

- **A finding is never fixed where it is found** ([`METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md)
  §5). The temptation is highest in an audit whose findings are small.
- **Coverage is a partition, and it fails** (§2 of the method). An item in none of the three states is
  a gap in the audit, not a clean item. A summary that merges denominators re-creates the blindness
  it was built to show, so each cycle reports its own.

**Scope**
- In: everything inside `plugin/`, which is exactly what an install copies
  ([T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md)), graded per §1 of the
  method rather than trimmed
- In: `README.md`, the repository description and both manifests, which are what a stranger reads
  before installing
- In: **a judgement on the method document itself** — which of its six rules earned their place on a
  real run, which were dead weight, and which were missing. Recorded either way, including *it worked
  as written*
- In: the §6 grading pass, run **after** the remedies exist rather than at ranking time
- Out: applying the findings. Each becomes its own record, per METHOD §5
- Out: cutting `1.0.0`. That is [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md)
- Out: this repository's own tests, backlog and instruction files, except where a finding about the
  shipped product traces back into them

**Inputs**
- [`pre-release-audit`](../plugin/skills/taskmd/docs/method/pre-release-audit.md) — the six rules, and
  the subject of the second half of this record
- [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — the ordinary procedure the above extends
- [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) — the last audit this
  project ran, for what its findings looked like and how they were raised

**Acceptance criteria**
- [ ] The scope is graded, the aspects are named in the plan, and every item in scope ends in exactly
      one of §2's three states
- [ ] Each cycle reports its own coverage, and no cycle's denominator is merged into another's
- [ ] Every actionable finding has a severity that obliges something, and a record of its own
- [ ] The §6 grading pass has been run after the remedies exist, and names at least one prediction
      that was wrong or says honestly that none was
- [ ] The record says which of the method's six rules earned their place, which did not, and what was
      missing — including *nothing was missing*, stated plainly
- [ ] Any change the method needs is a separate task, not an edit made here

**Open questions**
- **How many cycles, and which subjects?** — whoever plans this. Not answerable before §1's grading
  is done, and the method says to pick the aspects in the plan rather than in advance.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none yet

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **Blocked by [T-243](T-243-key-the-release-note-rule-on-what-the-release-ships-not-on-a-milestone-label.md) and [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md), on the owner's instruction of 2026-08-23 that both land before the audit.** **Recorded as edges rather than as a sentence**, which is this project's own lesson twice over: the ordering that put the release before its note lived in prose and was invisible to every view until somebody ran the rule. Both change something this record would audit — §7's release-note rule and the task template — so auditing first would judge a shape about to change and re-find what is already known. **This is a sequencing edge, not a scope change**: §1 is untouched, and the record is still `proposed` for the owner to start. |
| 2026-08-23 | → proposed | **Raised on the owner's instruction of 2026-08-23**, given as a survey answer minutes after `v0.6.0` was published: raise the task, do not start it. The standing rule that a session starts no audit is unchanged, and this record is deliberately left at `proposed` for the owner to start. **Three things came with the instruction and are recorded in §1 rather than here**: `0.6.0` is to be read as a beta, `1.0.0` follows the audit and its fixes, and **the audit feature itself is under review** because it has never been run. The last is the reason this is not an ordinary audit umbrella: [T-223](T-223-ship-the-pre-release-audit-as-a-method-document.md) shipped the method to every adopter without it having been executed once, so the subject and the instrument are both on trial. **The owner also chose not to flag the published release as a prerelease** on the same exchange, because GitHub would then show `v0.5.0` as latest and point a visitor at older software. |
