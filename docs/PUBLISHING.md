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
- **The plugin's agent-facing instructions** — `plugin/skills/`, `plugin/skills/taskmd/docs/`, the schema config.
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

**`repo-description.txt`, beside this file.** Its entire content is the value, which is why it is not
Markdown: nothing in it is prose about the description, so there is nothing to strip before using it.
It is set on the repository at publication
([T-006](../tasks/T-006-package-document-and-publish.md) §2 step 7).

It moved here from
[T-079](../tasks/T-079-humanize-the-human-facing-documents-before-publishing.md) §3, which still
holds the before and the audit that produced the text and is the reason it reads as it does. A task
record was the wrong home for a value the gate below has to read: task files are excluded from this
rule, so a gate would have had to scan what the rule exempts (T-081).

## 5. The gate

Run before publishing, and before any redeployment. It must print a file count and **nothing else**.

```bash
( cd "$(git rev-parse --show-toplevel)" && set -- $(git ls-files --cached --others --exclude-standard 'README.md' 'docs/repo-description.txt' '.claude-plugin/*.json' '*/.claude-plugin/*.json') && { [ "$#" -gt 0 ] || { echo "covers 0 files - the pathspec is wrong"; exit 2; }; } && echo "$# file(s) covered" && grep -nI -e '—' -e '–' "$@" )
```

Three outcomes, deliberately distinguishable:

| Exit | Means |
| :---: | :--- |
| 1 | Clean. The count printed, no lines after it |
| 0 | Violations. Every line is a covered document carrying an em or en dash |
| 2 | **The gate is broken**, not the tree. It resolved to no files at all |

**Read the count, not just the silence.** A run that reports zero files and prints nothing else is
the failure mode this project has hit three times now — T-034, T-080, and the reason exit 2 exists
here. The count is why the pathspec cannot rot quietly.

The `cd` is load-bearing for the same reason it is in the leak check: `git ls-files` lists the
subtree you are standing in, so an unanchored gate run from `plugin/` would cover a smaller set and
say so only in a number nobody was reading (T-080).

### What passing does **not** prove

It does not prove a document was humanized. Pattern 14 is the only part of §2 a script can judge, so
the gate is a **proxy**: failing it proves the rewrite did not happen, and passing it proves only
that one pattern is absent. The rewrite is a judgement and needs the skill and an agent. Treating a
green gate as evidence of a humanized document is the mistake `../CLAUDE.md` warns about for
validators generally, and it is written here because this gate is the one most likely to invite it.

### What it covers, and the one thing it cannot derive

The pathspec covers the README, the description above, and **every** plugin or marketplace manifest
anywhere in the tree, so a second manifest is gated the day it is added, with nothing edited. What it
cannot do is notice a covered document of a **new kind** — a `CONTRIBUTING.md`, a landing page. The
test in §1 still governs that, and adding one pattern to the line above is the whole of the work.
That residue is stated rather than hidden, because a gate believed to be exhaustive is worse than one
known to be partial.
