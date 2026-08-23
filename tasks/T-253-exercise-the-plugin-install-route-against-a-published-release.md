---
id: T-253
title: Exercise the plugin install route against a published release, or decide it will not be
type: decision
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-241, T-085, T-067]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables: []
---

# T-253 — Exercise the plugin install route against a published release, or decide it will not be

## 1. Specify

**Outcome**

Either `claude plugin marketplace add` followed by `claude plugin install` has been run against a
published taskmd release and what it produced is recorded, or the project has decided in the open
that it will not be — with the reason, so no later release verification inherits the gap silently.

**Why this exists as a task rather than a line in an audit**

Two verification tasks have now ended with this half unproven, and **the second nearly ended with it
unowned**. [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) closed
`done` in August carrying it; [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)
re-checked it on 2026-08-23 and found **T-085's reason no longer true** — that record could not run
it for want of Node and a `claude` CLI, and this machine has `claude` 2.1.241, installed and
authenticated. Nothing open carried it at that moment: a `grep` over the backlog for the route
returned only T-241 itself. One more closure and the obligation would have left every view the
project has, which is what a soft edge from a closing audit exists to stop.

**What actually blocks it, as of 2026-08-23**

Not capability. The marketplace named `taskmd` on the maintainer's machine has its `source` set to
`directory`, pointing at the working checkout — so every session there is served the working tree
rather than a release. Running the route means removing that entry, adding the GitHub one,
installing, and restoring it, with a restart needed before the maintainer's setup behaves as before
and a hand repair if it fails partway. **The owner was asked during T-241 and chose not to**, on the
grounds that an audit which breaks the maintainer's development loop to prove a route costs more than
the answer is worth. That is a decision about one audit, not about the route forever, which is why it
is a task and not a closed question.

**Scope**
- In: running the two commands against a published release, on any machine, and recording what they
  produced — or recording the decision not to, with what it rules out
- In: naming a venue if one exists that is not the maintainer's primary checkout
- Out: verifying any particular release's *contents*. That is what a
  verify-from-outside task does, and [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)
  did it for `0.6.0` by fetching the tag directly
- Out: changing how the plugin is published or installed

**Inputs**
- [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) §3
  *What could not be reached* — the current blocker, stated as a decision with its date
- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) §3 — the
  original blocker, and why it no longer holds
- [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) — what the route was supposed
  to prove

**Acceptance criteria**
- [ ] Either the two commands have been run against a published release and their output is recorded,
      or a decision not to is recorded with its reason and what it rules out
- [ ] If it was run, what it proves is stated separately from what it does not — an install landing
      files is not the same as the skill being served
- [ ] If it was not run, the next verify-from-outside task can find this record from the route's own
      words, so the gap is inherited **with** its owner rather than silently

**Open questions**
- **Is there a venue that is not the maintainer's primary checkout?** — the project owner.
  **Recommendation: ask the question before the next release rather than during its audit**, since
  during an audit the answer is always *not now*, which is how this reached its second closure
  unowned. No recommendation on the venue itself: the sibling checkouts are on the same machine and
  share the same registry, so the honest answer may be that there is none and the decision is to
  stop asking.

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

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → proposed | **Raised from [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md)'s review**, 2026-08-23, as a **soft** link and not a child. METHOD §4's residual case: T-241's outcome is *complete* — the artifact was fetched, inventoried, exercised and validated, and the unreachable part is named, which is what its criteria ask for. This asks for something **beyond** that outcome and waits on a decision nobody here controls, so making it a child would hold a finished audit open indefinitely. **It is raised at all because nothing open carried the route** — measured during that review, and T-085 had already closed over it once. **The owner's grant of 2026-08-23 reaches this record** — its words are *"including anything raised during the work of these tasks"*, and this was raised during T-241's review. **It was not worked past `specify` anyway**, and that is a judgement rather than a limit of the grant: the outcome turns on a question only the owner can answer, and a grant removes the asking, not the deciding. |
