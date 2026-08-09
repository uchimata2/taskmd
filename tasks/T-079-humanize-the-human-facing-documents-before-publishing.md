---
id: T-079
title: Humanize the human-facing documents before publishing
type: deliverable
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-006]
work_package: none
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-079 — Humanize the human-facing documents before publishing

## 1. Specify

**Outcome**
The documents a stranger reads — the GitHub README first, and the other human-facing prose in the
published tree — have been through the `humanizer` skill under the exception recorded below, so what
is published reads as written rather than as generated.

**Why this one**
Every document in this repository was drafted in an agent session, and the tell is uniform prose
rather than any single sentence. A reader who bounces off the README never reaches the tool. It
blocks [T-006](T-006-package-document-and-publish.md) because after publication the first impression
has already been made, and because T-006 step 5 writes the README this task would then rewrite —
running them in the other order is one document written twice.

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
- In: `README.md` (once T-006 step 5 has written it), and whichever other human-facing documents the
  first step names.
- Out: task files. Sixty-odd records of work already done are an audit trail, and rewriting their
  prose would edit the history rather than the product.
- Out: the schema config, the bindings and `plugin/docs/METHOD.md` as *reference* material — see the
  open question, which is what decides whether the method document is in or out.
- Out: anything the humanizer would have to invent a fact to improve. The skill's own rule and this
  project's are the same one: a claim that was not measured does not enter a document.

**Inputs**
- The installed skill: `humanizer@humanizer` 2.9.1, from the `blader/humanizer` marketplace.
- `CLAUDE.md` *Publishing constraints* — the pre-publish check runs after any rewrite, not before.
- [T-006](T-006-package-document-and-publish.md) §2 step 5, which produces the README this rewrites.

**Acceptance criteria**
- [ ] <written when the open questions below are answered>

**Open questions**
- **Which documents count as human-facing?** The README is certain. `docs/SCOPE.md`, `docs/BRIEF.md`,
  `plugin/docs/METHOD.md`, the two bindings and `plugin/skills/taskmd/` are each read by someone, but
  the last two are read by an *agent* on a token budget, where the compression that reads as
  machine-written is the feature. — maintainer.
- **Does pattern 14 apply to this tree?** "Em dashes: cut them" is not in the skipped set, and this
  project's prose uses them heavily and deliberately. Applying it is a large, irreversible-by-hand
  rewrite of voice; skipping it silently would be a fourth exception nobody wrote down. — maintainer.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → proposed | Created at the maintainer's request, and made a publication blocker on T-006 rather than a follow-up: after publishing, the first impression has been made, and T-006 step 5 writes the README this task would rewrite. The exception is quoted verbatim and its three pattern numbers are also named, because a number pointing into a third-party skill is a reference that breaks silently when that skill is renumbered. Two questions are left open rather than assumed: which documents are human-facing at all — the agent-facing ones are on a token budget, where compression is the feature — and whether pattern 14, cutting em dashes, applies to a tree that uses them deliberately. Acceptance criteria wait on both, because either answer changes what is being judged. |
