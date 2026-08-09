# Publishing — what has to be true of text a stranger reads

Read this when publishing anything, or when writing something that will be published. It is **not**
always-loaded: `../CLAUDE.md` carries a one-line pointer to it, because this rule binds at
publication rather than on every turn, and a rule paid for on every turn of every session is a rule
charged for a moment that happens rarely. Decided in
[T-079](../tasks/T-079-humanize-the-human-facing-documents-before-publishing.md).

`../CLAUDE.md` *Publishing constraints* holds the other publish-time rule — the pre-publish leak
check — and is not restated here. The two eventually belong together; consolidating them is a
tier-1 restructure owned by [T-047](../tasks/T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md),
not something to do in passing.

---

## 1. What is covered

**The test: text a stranger reads before they have installed anything.** That is the rule. It is
deliberately not a list of files — a list goes stale the first time a document is added, and it goes
stale silently, which this project has already paid for once in `.handoff/config.md`'s
`reconcile_targets`.

Applying the test today gives `README.md`, the GitHub repository description, the plugin manifest's
`description` and the marketplace manifest's `metadata.description`. A document written next month
is covered or not by the same test, with nothing here to edit.

**What is excluded, and why** — the maintainer's reason, 2026-08-09: *keep them efficient for AI
parsing.*

- **Commit messages.** Read by people, but after they have arrived, and they are the audit trail.
- **The plugin's agent-facing instructions** — `plugin/skills/`, `plugin/docs/`, the schema config.
  The compression that reads as machine-written is the feature there, and `SKILL.md`'s `description`
  is served to every session unasked, where characters are the budget.
- **Task files.** An audit trail of work already done. Rewriting their prose edits the history
  rather than the product.
- **This document**, by its own test: nobody reads it before installing. It is written in the house
  style, em dashes included, and that is not an oversight.

## 2. How

Run the `humanizer` skill (`humanizer@humanizer`, from the `blader/humanizer` marketplace) over the
covered text in its **file mode**, which rewrites in place and leaves code blocks, front-matter and
link targets alone.

**The exception, from the maintainer, verbatim:**

> When humanizing docs: preserve tables, code blocks, heading hierarchy, and **Label:** value
> bullets. Skip patterns 15, 16, 18. Apply the rest.

The three skipped patterns are numbered sections of the skill, and they are **named here as well as
numbered**, because a bare number pointing into a third-party document breaks silently when that
document is renumbered. In version 2.9.1 they are **15 Overuse of Boldface**, **16 Inline-Header
Vertical Lists** and **18 Emojis**. Each is load-bearing in a technical document: this project
carries its decisions in bolded labels and its rules in inline-header lists, so stripping them would
flatten the structure that makes a document skimmable rather than remove a tell.

**Two escapes in the skill are deliberately not taken.** Both would let this project keep its em
dashes, and the maintainer's answer on 2026-08-09 was to apply pattern 14 and cut them:

1. *Voice Calibration* says a supplied writing sample outranks §14, so handing over this tree's
   existing prose as a sample would preserve them at their current frequency.
2. *Detection guidance* lists "em dashes alone" under what not to flag.

Anyone reading the skill will find both. They are foreclosed for covered text, not overlooked.

## 3. Order

The leak check in `../CLAUDE.md` runs **after** any rewrite, never before. A rewrite is new text, and
new text is exactly what that check exists to read.

## 4. Where the repository description lives

One home, and it is not this file:
[T-079](../tasks/T-079-humanize-the-human-facing-documents-before-publishing.md) §3, which holds the
drafted text along with the before and the audit that produced it. It is set on the repository at
publication ([T-006](../tasks/T-006-package-document-and-publish.md) §2 step 7).
