---
id: T-079
title: Humanize the human-facing documents before publishing
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: []
work_package: M1
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: [docs/PUBLISHING.md]
---

# T-079 — Humanize the human-facing documents before publishing

## 1. Specify

**Outcome**
A standing rule, at a home that publication reaches, saying which text gets humanized and under what
exception — plus one use of it on real text, because a rule nobody has run is a claim. **The rule is
the deliverable, not a pass over today's tree.** That is what the maintainer asked for on 2026-08-09,
and it is also the only shape that works: the README this task most needs to cover does not exist yet
([T-006](T-006-package-document-and-publish.md) step 5 writes it), so a task scoped to *documents*
would have to stay open until then, and every document written after it closed would be uncovered.

**Why this one**
Every document here was drafted in an agent session, and the tell is uniform prose rather than any
one sentence. A reader who bounces off the README never reaches the tool. Scoping this to the rule
rather than to a sweep also fixes the ordering problem it started with: T-006 step 5 writes a README
that this task would otherwise rewrite, which is one document written twice.

**The exception, as given by the maintainer on 2026-08-09 — verbatim**

> When humanizing docs: preserve tables, code blocks, heading hierarchy, and **Label:** value
> bullets. Skip patterns 15, 16, 18. Apply the rest.

The three skipped patterns are numbered sections of the skill, and they are named here as well as
numbered so the instruction survives the skill being renumbered — in `humanizer@humanizer` **2.9.1**
they are **15 Overuse of Boldface**, **16 Inline-Header Vertical Lists** and **18 Emojis**. Each is
load-bearing in a technical document: this project's prose carries its decisions in bolded labels
and its rules in inline-header lists, and stripping them would flatten the structure that makes a
document skimmable rather than remove a tell.

**Requirements served**
R-23 is not this — that is the leak check. This task serves `docs/SCOPE.md` §1 by way of the README
being the first thing anyone reads; it adds no requirement and changes none.

**Scope**
- In: the rule, written where publication reaches it.
- In: what the rule covers, named by the maintainer — `README.md`, and any repository or marketplace
  description a stranger reads before they have installed anything.
- In: one application of the rule to text that exists today, as the evidence it works.
- Out: the README itself, which T-006 step 5 writes and which the rule then covers. Writing it here
  would be doing another task's work.
- Out: **commit messages and the plugin's agent-facing instructions** — `SKILL.md`, `adopt.md`,
  `plugin/docs/`, the schema config. The maintainer's words: keep them efficient for AI parsing. The
  compression that reads as machine-written is the feature there, and `SKILL.md`'s `description` is
  served to every session unasked, where characters are the budget.
- Out: task files. Sixty-odd records of work already done are an audit trail; rewriting their prose
  edits the history rather than the product.
- Out: anything the humanizer would have to invent a fact to improve. Its rule 3 and this project's
  are the same rule.

**Inputs**
- The installed skill: `humanizer@humanizer` 2.9.1, from the `blader/humanizer` marketplace.
- `CLAUDE.md` *Publishing constraints*, which is where the other publish-time rule already lives.
- The maintainer's answers of 2026-08-09, recorded under *Open questions* below.

**Acceptance criteria**
- [ ] The rule exists in one home, states what it covers and what it excludes, and carries the
      exception verbatim
- [ ] The always-loaded tier gains a pointer to it and not the rule itself, so the cost is paid at
      publication rather than on every turn
- [ ] The rule has been **used** on real text, with the before and after both recorded — not merely
      written down
- [ ] The rule's covered set is stated as a test a future document can be held against, not as a
      list of today's files
- [ ] Nothing agent-facing is rewritten, and the pre-publish check still passes

**Open questions**
- ~~**Which documents count as human-facing?**~~ **Answered by the maintainer, 2026-08-09: the README
  definitely, and any GitHub repository description.** Commit logs and plugin instructions are
  explicitly out, and the reason given is that they should stay efficient for AI parsing. So the
  covered set is not "documents this project happens to have" but *what a stranger reads before they
  have installed anything*, which is the form the rule is written in.
- ~~**Does pattern 14 apply to this tree?**~~ **Answered by the maintainer, 2026-08-09: yes, apply it.**
  Worth recording that the skill itself offers an escape and it is not being taken: its *Voice
  Calibration* section says a supplied writing sample outranks §14, so this project's existing prose
  could have been handed over as a sample to keep its em dashes. The answer forecloses that, and the
  rule says so, because the next person to read §14 will find that escape too.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Settle where the rule lives, against the tier-1 bound this project is already over. | The decision and its rejections, in §3 |
| 2 | Write the rule: the covered set as a test, the exclusions with the maintainer's reason, the exception verbatim, and the two escapes in the skill that are not being taken. | `docs/PUBLISHING.md` |
| 3 | Add the pointer from the always-loaded tier, and measure what it costs there. | The edited `CLAUDE.md` section, and the character count before and after |
| 4 | Use the rule on real text: draft the repository description a stranger reads, run the skill's own draft, audit, final loop on it, and record all three. | The before, the audit answers, and the final text, in §3 |
| 5 | Check the descriptions that already exist against the rule and report the verdict rather than assuming it. | A verdict per description, with the one home each is stored in named |
| 6 | Point T-006's publication step at where the drafted description lives, so it is found at the moment it is needed. | The edited T-006 step 7 |
| 7 | Run `index`, `check` and the pre-publish check both ways. | The output of each |

**Step 4 is the step that makes this a task rather than a note.** A rule written and never run is
the unverified claim this project exists to avoid, and the method puts verification in `implement`
for exactly this reason. The repository description is the one piece of covered text that exists
today, so it is what the rule gets used on.

**Decisions — shape**

- **The rule is written as a test, not as a list of files.** A list goes stale the first time a
  document is added, and it would go stale silently. *Rejected: enumerating `README.md` and the
  description*, which is the same failure `.handoff/config.md` already records for
  `reconcile_targets` and which cost this project a contradiction that a human caught.

**Not in this plan:** rewriting `README.md`, which does not exist and is T-006's; and consolidating
the pre-publish leak check into the new document, which is a tier-1 restructure owned by
[T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md).

## 3. Implement

Worked in plan order. Nothing was reordered.

**Decisions & assumptions**

- **D1 — the rule lives in `docs/PUBLISHING.md`, and tier 1 gets a pointer** — 2026-08-09. Measured
  rather than argued: tier 1 stood at **12,199** characters against a bound of **7,919**, so it is
  already 54% over. The pointer cost **168**; the rule itself is roughly two thousand. *Rejected:
  the full rule in `CLAUDE.md`*, which charges every turn of every session for a rule that binds at
  publication. *Rejected: no pointer at all*, leaving the rule in a file nothing routes to — the
  failure T-073 already recorded for `control/`, where a correction sat unread for four days.
  *Accepted cost:* publishing rules now sit in two files. `docs/PUBLISHING.md` says so and points at
  the other; consolidating them is T-047's tier-1 restructure, and doing it here would be a second
  task's work.

- **D2 — the skill was applied by reading it, not by invoking it** — 2026-08-09. It was installed
  during this session, and the harness fixes its skill list at session start, so `humanizer` is not
  invocable until the next one. The loop below is the skill's own *Process and Output* — draft, the
  two audit questions, final, then a scan for `—` and `–` — run against its numbered patterns as
  written in version 2.9.1. Recorded because it is a real difference: a later session invoking the
  skill is the stronger evidence, and this is what was available.

### Steps 2 and 3 — the rule, and what the pointer cost

`docs/PUBLISHING.md` states the covered set as a test rather than a list, carries the exception
verbatim with its three patterns named as well as numbered, and records the two escapes in the skill
that are not being taken. `CLAUDE.md` gains one bullet of two lines.

```
tier 1 before   12199
tier 1 after    12367      +168
bound            7919
```

The bound is unchanged and still failed. This task made it worse by 168 characters and says so;
T-047 and T-063 own the failure itself.

### Step 4 — the rule used on real text

**Before** — `docs/SCOPE.md` §1, the project's own description of itself, which is what a repository
description would otherwise be cut down from:

> A lightweight, token-efficient, local-first task tracker for Claude Code — Markdown files, a
> generated index, real dependency links, and a validator — usable for any kind of work, not only
> software.

**Audit, the skill's two questions.**

*What makes it obviously AI generated?* Three tells, clustered, which is the skill's own bar rather
than any one of them alone: a stacked triple adjective (**10**, rule of three) doing the work an
actual claim should do; a pair of em dashes used as parentheses (**14**); and a tailing negation
(**9**), "not only software", which states the point by denying its opposite. "Lightweight" is also
promotional (**4**) and measures nothing.

*Does the rewrite state any fact, name, number, date or citation not in the source?* No. "Research
and writing" replaces "any kind of work" and comes from R-9 in the same document, which names
research, a deck, a training course and an ops runbook. The skill permits a specific drawn from the
source; it would forbid inventing one.

**Final** — the repository description, 267 characters, within GitHub's 350:

> Task tracking in plain Markdown files, one per task, for Claude Code. The index and the far end of
> every link are generated from those files, so neither can drift. Ships a validator. Runs from a
> clone with no dependencies, on any kind of work including research and writing.

Scanned for `—` and `–` per §14: none. This is the text T-006 step 7 sets at publication.

### Step 5 — the descriptions that already exist, checked rather than assumed

Both are covered by the rule, and both are already clean. Their homes are T-072's, unchanged here.

| Description | Home | Verdict |
| :--- | :--- | :---: |
| the plugin's | `plugin/.claude-plugin/plugin.json` | clean |
| the marketplace's | `.claude-plugin/marketplace.json`, `metadata.description` | clean |

No em dashes, no emoji, no curly quotes, no promotional vocabulary in either. The marketplace one
enumerates three features, which is pattern 10's shape and not its substance: the skill's own
detection guidance asks for **clusters** of tells rather than isolated ones, and there is no second
tell in a twenty-word sentence. Neither was rewritten, so T-072's one-home-each result stands.

**Outputs produced**
- `docs/PUBLISHING.md` — the rule
- `CLAUDE.md` — one pointer bullet, +168 characters
- The repository description, above, and the pointer to it from T-006 step 7

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The rule exists in one home, states what it covers and what it excludes, and carries the exception verbatim | met | `docs/PUBLISHING.md` §1 and §2. The exception is quoted, and its three patterns are named as well as numbered so the reference survives the skill being renumbered |
| The always-loaded tier gains a pointer and not the rule itself | met | §3 step 3: two lines, **+168** characters measured on the command `CLAUDE.md` itself defines, against roughly two thousand for the rule |
| The rule has been **used** on real text, before and after both recorded | met | §3 step 4. The before is `SCOPE.md` §1, the audit names three clustered tells with their pattern numbers, and the final is scanned for `—` and `–` as §14 requires. Weakened by D2 and stated there: the skill was applied by reading it, because a skill installed mid-session is not invocable until the next one |
| The covered set is stated as a test, not a list of today's files | met | `docs/PUBLISHING.md` §1: *text a stranger reads before they have installed anything*, with today's four files shown as what the test currently returns rather than as the rule |
| Nothing agent-facing is rewritten, and the pre-publish check still passes | met | `plugin/` is untouched apart from nothing at all; `check` OK on 79 tasks; the leak check silent with its exclusion and exactly five fixture lines without it |

**The unplanned finding is a negative one.** Step 5 expected to rewrite at least one of the two
existing descriptions and rewrote neither: both were already clean, and the marketplace one's
three-item list is pattern 10's shape without its substance, which the skill's own *clusters* rule
settles. Recorded because "checked and found clean" and "not checked" look identical afterwards.

**What this task does not claim.** The README is not humanized, because it does not exist. That is
not a gap in the work: after this task, it is covered by a rule rather than by an open task, which is
what the maintainer asked for and why T-006 can close it out under `docs/PUBLISHING.md` instead of
waiting on a second pass here.

**Child fix tasks raised**
- **[T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md)** — step 7 tripped it. A
  leftover `cd tests` from running the suite made the pre-publish check print its own five-line
  fixture as though the tree had leaked: the exclusion is a git pathspec and resolves against the
  working directory, while `git ls-files` does not. Nothing leaked, and the check run from the root
  is silent. Raised rather than fixed here.

  **That last sentence is wrong, and T-080 §1 carries the correction rather than this record being
  rewritten.** `git ls-files` lists the *subtree*: from `tests/` the check read 37 files of 159. The
  claim is left standing because it is what was believed when the task was raised, and because the
  successor measured it.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | All five criteria met, and the task closes the same day it was raised because its outcome turned out to be a rule rather than a sweep. `docs/PUBLISHING.md` carries it; `CLAUDE.md` gains a two-line pointer costing **168** characters, measured, against roughly two thousand for the rule itself, on a tier that is already 54% over its bound and is T-047's to fix. The rule was used rather than only written: `SCOPE.md` §1 through the skill's own draft, audit, final loop, producing the 267-character repository description T-006 step 7 will set. Two things are recorded as weaker than they look. The skill was applied **by reading it**, because one installed mid-session is not invocable until the next one, so a later session invoking it is the stronger evidence. And step 5 rewrote neither existing description: both were already clean, which is a negative finding worth writing down because checked-and-clean is indistinguishable from unchecked afterwards. Publishing rules now live in two files, which is an accepted cost stated in the new document rather than absorbed. |
| 2026-08-09 | → planned | Seven steps, with the rule's home settled first because it is the one choice the tier-1 bound can veto. Step 4 is the load-bearing one: the rule gets used on the repository description, which is the only covered text that exists before T-006 writes the README, and without it this task ships a claim. One shape decision: the covered set is a test rather than a list, on the precedent of `reconcile_targets` in `.handoff/config.md`, where an enumeration went stale the moment a document was added and left two files contradicting each other. |
| 2026-08-09 | → specified | Both questions answered, and the second answer **changes the outcome**: the maintainer asked for the rule to be recorded so the task need not stay open, which is also the only shape that works, because the README this task most needs to cover is written by T-006 step 5 and does not exist yet. So the deliverable is the rule plus one use of it, and the covered set is written as a test — what a stranger reads before installing anything — rather than as a list of today's files, which would be stale the first time a document is added. Em dashes are cut: the skill offers an escape in *Voice Calibration*, where a supplied writing sample outranks §14, and the answer forecloses it. Commit messages and everything agent-facing are explicitly out, on the maintainer's reason that they stay efficient to parse. |
| 2026-08-09 | → proposed | Created at the maintainer's request, and made a publication blocker on T-006 rather than a follow-up: after publishing, the first impression has been made, and T-006 step 5 writes the README this task would rewrite. The exception is quoted verbatim and its three pattern numbers are also named, because a number pointing into a third-party skill is a reference that breaks silently when that skill is renumbered. Two questions are left open rather than assumed: which documents are human-facing at all — the agent-facing ones are on a token budget, where compression is the feature — and whether pattern 14, cutting em dashes, applies to a tree that uses them deliberately. Acceptance criteria wait on both, because either answer changes what is being judged. |
