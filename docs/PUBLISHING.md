# Publishing — what has to be true of text a stranger reads

Read this when publishing anything, or when writing something that will be published. It is **not**
always-loaded: `../CLAUDE.md` carries a one-line pointer to it, because this rule binds at
publication rather than on every turn, and a rule paid for on every turn of every session is a rule
charged for a moment that happens rarely. Decided in
[T-079](../tasks/T-079-humanize-the-human-facing-documents-before-publishing.md).

**The pre-publish leak check now lives here too** (§6), moved out of `../CLAUDE.md` by
[T-047](../tasks/T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) for the same
reason this file exists: it binds at publication, and a rule paid for on every turn is charged for a
moment that happens rarely. It was the single largest block in tier 1, for something needed once.
`../CLAUDE.md` keeps the constraints themselves — what may not be written down — and points here for
the check that enforces them.

---

## 1. What is covered

**The test: text a stranger reads before they have installed anything.** That is the rule. It is
deliberately not a list of files — a list goes stale the first time a document is added, and it goes
stale silently, which this project has already paid for once in `.handoff/config.md`'s
`reconcile_targets`.

Applying the test today gives `README.md`, the GitHub repository description, the plugin manifest's
`description` and the marketplace manifest's `metadata.description`. A document written next month
is covered or not by the same test, with nothing here to edit.

**A tag message and its GitHub release are covered, and nothing enforces it.** The maintainer's
answer, 2026-08-11
([T-127](../tasks/T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md)). A release page is
the second thing someone evaluating the plugin opens after the README, so §1's test catches it on the
literal reading; the rival was excluding it on the same grounds as a commit message, which keeps the
covered set to things a script can read and loses the reader the test is about. A stated rule nobody
enforces beats an unwritten one.

**One published page breaks this rule and is deliberately left alone.** `v0.2.0`'s release body
carries four em dashes; every other release body and all four tag messages are clean. The
maintainer's answer, 2026-08-11
([T-133](../tasks/T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md)):
the page was written before the rule was adopted, and rewriting a dated public record after the fact
is the act METHOD rule 5 forbids for a task record. Named here rather than left as a contradiction
somebody re-files.

**Two texts, not one, and only one of them is even reachable.** The annotated tag message and the
GitHub release body are separate: measured on 2026-08-11, `v0.2.0`'s tag message is 936 characters
and its release body 2591, and they say different things. A tag message can at least be listed with
`git for-each-ref`; a release body lives on GitHub and needs the network, which this project's
dependency-free and offline constraints put out of the suite's reach. So the §5 gate reaches neither —
its pathspec lists files, and neither of these is a file — and **both are written by eye, to the same
rule as the README.** That is the residue §5 names, arriving for the first time with a name.

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

**The suite runs this rule too, and reads it from here.** `tests/test_publishing.py` lifts the
pathspec and the two characters out of the command above rather than restating them, so a covered
document added to that line arms the test with nothing edited anywhere else — and a shape the test
cannot parse is a failure, not a skip. It exists because this gate was red for two releases and
nobody had disobeyed it; nobody had run it
([T-126](../tasks/T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md)). The command
here stays, because a person publishing wants to see the lines rather than a test name, and because
it is the rule's one home.

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

**One covered text is now known to be beyond it, by name**: the tag message and the GitHub release
body, neither of which is a file. §1 says so and says nothing enforces them.

---

## 6. The pre-publish check

Run over every file a push would send. It must print nothing; every hit is either a leak or a label
that needs adding to `control/LOCAL-CONTEXT.md`.

```bash
( cd "$(git rev-parse --show-toplevel)" && git ls-files -z --cached --others --exclude-standard ':!tests/fixtures/leak-check/' | xargs -0 grep -nIE '\b[A-Za-z]:[\\/][A-Za-z0-9._-]+[\\/]|/(home|Users)/|[\\]{2}[A-Za-z0-9._-]+[\\]|[0-9]{1,3}(\.[0-9]{1,3}){3}' )
```

Four classes: Windows drive paths, home directories, UNC paths, IP addresses. `git ls-files` is what
makes it meaningful, but **only with those three flags**: on its own it lists what git already
*tracks*, which silently omits every file the session just created. `--cached --others
--exclude-standard` is tracked files **plus** untracked-but-not-ignored ones — so it sees exactly
what a push would send, and anything gitignored is still out of scope by construction. Do not
shorten it to `-co`: the point of the line is that a reader can see what it covers. The omission was
silent for as long as it existed — a check that reads none of the files it was aimed at prints
nothing, which is also what success looks like ([T-034](../tasks/T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md),
which measured it and proved the fix by making it catch a leak in an untracked file).

**The `cd` is not decoration.** `ls-files` lists the subtree you are standing in, and the exclusion
is a pathspec resolved against the same place — so run from a subdirectory the unanchored command
read a quarter of the tree *and* printed its own fixture as five leaks. Both halves are invisible:
the alarm hides the under-scan, and anchoring only the exclusion silences the alarm while leaving the
blindness (T-080, which measured both and rejected that smaller fix for exactly this reason). Judge a
run by the file count, not by its silence.

**Run it last, after the task record is written — not before.** The check reads files, so it cannot
see one that does not exist yet, and the text most likely to trip it is the write-up of a task
*about* the check: quoting a matched line into a task record re-creates the leak. This has now
happened twice, in T-013 and again in T-018 while fixing T-013. Describe the result and point at the
fixture; never paste the lines.

**The excluded path is the check's own fixture, and dropping the exclusion is how the check is
proven.** `tests/fixtures/leak-check/samples.txt` holds nine deliberately-fabricated lines: five that
must be caught, one per class, and four safe forms that must not be. So there are two runs of one
command — with the exclusion, the tree must print **nothing**; without it, the output must be
**exactly those five lines and nothing else**. The second run is what a clean tree can never prove
on its own, and keeping it in the same command is what stops the proof drifting from the check. The
exclusion is one pathspec, not a second contract: any leak outside that one file is still caught, and
the file's only content is the fixture.

**A fabricated specimen must not reach the file through a shell.** The fixture above crosses none, so
this bites only where a run needs a specimen the fixture does not hold — an untracked file, a one-off
reproduction, a class being added. Sent through a command line, such a line can arrive one backslash
short and stop being the form it was meant to be. **Quoting is not the escape:** the byte is gone
before any shell construct sees the text, so a quoted heredoc — the device whose entire purpose is to
be literal — loses it too, and so does escaping the escape. Write the specimen with something that
never puts it on a command line. Two of the five must-catch lines carry backslashes, and the UNC one
is where this was first hit
([T-035](../tasks/T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) reproduced all
three shell routes failing and the direct write surviving).

**So make the specimen prove itself before it judges anything.** Damaged text is indistinguishable
from intended text by reading, which is the whole difficulty: match the pattern against the specimen
file first and confirm every class fires, and compare the stored bytes against the text as written —
that comparison is what identified it originally
([T-034](../tasks/T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md)). Until it passes, a
class that stays quiet is a transport failure and not a finding. This matters because the damage
presents as a **false negative attributed to the pattern**: a run catching every class but one reads
as a hole in the branch that did not fire, and the repair it invites is loosening a branch that was
already correct.

**Three limits, all deliberate.** A drive path is only matched with **two or more segments** after the
letter; a single-segment one is let through, because that form collides with ordinary text such as a
`d:\n` escape inside a code string — and a check that cries wolf gets ignored, which is worse than a
narrow one. (Do not write an example drive path here to illustrate that: the check reads this file
too, and an illustration is indistinguishable from a leak.) Second, **a dotted four-part version
number fires the IP branch** — a kernel or build string in a task record will trip it, and nothing
has leaked when it does; elide a component and move on. Requiring valid octets does not fix it,
because a version's parts are under 256 too, and it triples the branch (T-058). And third, **a
real name or a client project is not mechanically detectable at all**: that half is the label
discipline in `../CLAUDE.md`, and it holds only if every new identity goes into
`control/LOCAL-CONTEXT.md` rather than into a task.

The pattern was verified by being made to fail, and the fixture that did it is the one named above
rather than a transcript pasted into a task — which is what T-018 was raised to fix, after the pasted
copy left a real drive path in the tracked tree and made the documented "prints nothing" unreachable.
Two earlier drafts were wrong: one matched `http://` and a `d:\n` escape, and one ended a branch in
`\\`, which grep read as an escaped `|` and which silently swallowed the entire IP branch. Both bugs
were invisible on a clean tree.
