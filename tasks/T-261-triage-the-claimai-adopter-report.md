---
id: T-261
title: Triage the ClaimAI adopter report and decide its three findings
type: analysis
status: proposed
phase: specify
parent: null
blocked_by: []
related: []
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-28
updated: 2026-08-28
adopter_visible: no
deliverables: []
---

# T-261 — Triage the ClaimAI adopter report and decide its three findings

## 1. Specify

**Outcome**
Each of the three findings in [`docs/adopter-reports/claimai/`](../docs/adopter-reports/claimai/README.md)
has a decision against it — accepted and raised as a fix, accepted and deferred, or rejected with a
reason. This task produces the judgement; the fixes it accepts become tasks of their own. It is
`adopter_visible: no` because triage changes nothing an adopter sees; the fixes it raises carry their
own judgement.

**Where it came from**

An outside project ran a formal training exam on taskmd — a responsible-AI assessment of a fictional
insurer, delivered as nine documents and a twenty-five slide board deck. It ran from 2026-08-23 to
2026-08-28 and closed **84 tasks**. The findings were staged as they were hit, not written up
afterwards.

**taskmd held up, and the report says so first.** On its final run `check` resolved **1,989 links
across 182 documents**, over 227 references, 38 dependency edges and 112 declared outputs. The
project's own instruction file credits the method — specify, plan, implement, review, one phase per
request — as what kept a six-day project honest under a deadline.

**Nobody is waiting for an answer.** That project is closed. There is no thread, no deadline and no
reply expected. Take what is useful and discard the rest.

**The one that matters**

[`003` — nothing allocates a task id](../docs/adopter-reports/claimai/003-nothing-allocates-a-task-id-so-two-sessions-pick-the-same-one.md).

Two sessions read the same folder an hour apart, both took the same next free number, and both used
it. **The id is the reference key** — every dependency edge, every cross-link and every generated
index row names it — so a collision does not corrupt one file, it merges two tasks in every document
that points at either.

Two details make it worse than an ordinary race:

- **`check` passes a folder holding two `E28`s.** It validates structure and references, and a
  duplicate id is a state it reports as `OK`. That half is cheap to fix and independent of everything
  else in the record.
- **The adopter's only defence is a hand-written rule** in their own instruction file, telling every
  session to *re-derive the next free id immediately before writing a new task file, never from an
  earlier reading*. A rule that says "do the unsafe thing as late as possible" is the shape of a
  missing operation. It is worth reading as a specification for whatever replaces it.

**The other two**

- [`001`](../docs/adopter-reports/claimai/001-index-drops-a-concurrently-created-task.md) — `index`
  dropped a task file that existed on disk, and `check` immediately after reported `OK`. Same two
  sessions, same day. **Already staged before this hand-over**; it is included so the set is
  complete, and because reading it beside `003` shows one concurrency story rather than two bugs.
  That project still carries a standing rule to compare the file count against the count `index`
  reports, every time.
- [`002`](../docs/adopter-reports/claimai/002-the-cli-is-unreachable-when-taskmd-is-installed-as-a-plugin.md)
  — installed as a plugin, the CLI is not on `PATH`, so every command in that project's documentation
  goes through a wrapper it had to write. The wrapper must sort cached versions **as versions**: the
  plugin cache keeps every version installed, and a first-match glob picks the oldest, which fails in
  a way that reads as *tool not found*. The same gap exists in htmldeck and is reported there too,
  which suggests it belongs wherever plugin tooling is documented rather than in either repository.

**Worth knowing before reading**

- **Every record carries its evidence** — the command and its output, or the observed sequence step by
  step. That was the staging project's standing rule.
- **Every record carries `Version seen`.** All three say `0.6.0`. `001` and `002` were stamped rather
  than re-run, so check whether either is already fixed before actioning it.
- **The `Target` rows name a local clone path.** That is the staging project's own bookkeeping, left
  verbatim rather than edited, because editing an evidence record on the way out is worse than an odd
  line in it.

**Scope**
- In: the three records; one decision each; a fix task for every accepted finding.
- Out: fixing anything here.
- Out: replying to the adopter. There is no channel and none is expected.

**Inputs**
- [`docs/adopter-reports/claimai/README.md`](../docs/adopter-reports/claimai/README.md) — the covering
  note and the index
- The three records beside it

**Acceptance criteria**
- [ ] Each of the three records carries a decision: accepted and raised, accepted and deferred, or rejected with a reason
- [ ] `001` and `003` are decided together — they are one concurrency story from one day, and a fix for either should be checked against the other
- [ ] The `check` half of `003` is decided on its own merits: whether the validator should fail a folder holding two tasks with the same id, independent of how ids come to be allocated
- [ ] Each accepted finding names the task that will do it
- [ ] Each rejected finding says why, in a sentence an adopter would accept
- [ ] `Version seen` is checked before any record is actioned — all three were stamped, not re-run

**Open questions**
- None for the adopter — the report is closed and expects nothing.

## 2. Plan

Not planned.

## 3. Implement

**Decisions & assumptions**

**Outputs produced**

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |

**Child fix tasks raised**

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-28 | → proposed | Created when the adopter report was handed over. Three findings from 84 tasks over six days, staged as they were hit. Nothing is expected in return. |
