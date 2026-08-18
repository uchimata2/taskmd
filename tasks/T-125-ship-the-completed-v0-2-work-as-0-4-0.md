---
id: T-125
title: Ship the completed M2 work as 0.4.0
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-006, T-079, T-081, T-110]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/.claude-plugin/plugin.json, README.md]
adopter_visible: no
---

# T-125 — Ship the completed M2 work as 0.4.0

## 1. Specify

**Outcome**
The work grouped as `M2` is published: the manifest names a version an installed project can
update to, the tag and the GitHub release exist and say what changed, and the documents a stranger
reads before installing have passed the gate written for them.

**Why this one**
Every task grouped `M2` closed on 2026-08-11, which is that milestone's whole exit criterion. The
manifest still reads `0.3.0`, and `claude plugin update` compares version strings — so until that
line moves, a directory install reports "already at the latest version" and keeps serving the
snapshot it copied. Seventeen commits sit above the last tag.

**Filed `M2`, deliberately.** It makes the milestone not-done until its work is shipped, which is
the more useful reading of "done" and the reason this is not `M3`. It briefly falsifies the claim
that `M2` is complete; that claim becomes true again when this closes, which is what a milestone
containing its own release means.

**Requirements served**
R-21 and R-22 (`docs/SCOPE.md`) — the publishing constraints, at the moment they bind.

**Scope**
- In: the manifest version; the humanization of covered text, which the gate says has not happened
  since `v0.1.0`; both publication checks; the annotated tag and the GitHub release.
- In: what the release notes say the two untagged-until-now batches contained, since `v0.3.0` was
  tagged without one.
- Out: deleting or re-pointing the `v0.3.0` tag. It is public, and a re-used version number is worse
  than a gap — the maintainer's answer, 2026-08-11.
- Out: making the dash gate catch drift *between* publications, which is
  [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md).
- Out: anything in `M3`.

**Inputs**
- [`docs/PUBLISHING.md`](../docs/PUBLISHING.md) §2 (how to humanize), §5 (the dash gate), §6 (the
  pre-publish leak check).
- `plugin/.claude-plugin/plugin.json`, and the two tag messages of `v0.1.0` and `v0.2.0` as the
  form a release note takes here.

**Acceptance criteria**
- [ ] The dash gate prints a file count and nothing else, run on the tree being published
- [ ] The pre-publish leak check prints nothing with its fixture excluded, and exactly that fixture
      without it — both runs, since a clean tree cannot prove the second
- [ ] The manifest reads a version above the published one, and it is a **minor** bump with the
      reason stated
- [ ] The tag is annotated and its message says what changed, like `v0.1.0` and `v0.2.0` and unlike
      `v0.3.0`
- [ ] The GitHub release exists and accounts for the commits since `v0.2.0`, including the ten that
      `v0.3.0` carried without notes
- [ ] `check`, `index` and the full suite pass on the commit being tagged

**Open questions**
- none. Three were put to the maintainer on 2026-08-11 and all three answered: **humanize before
  tagging** rather than shipping through a red gate a third time; **0.4.0, minor**, because T-078
  turns a `tasks_dir: .` project from passing to failing; **leave `v0.3.0` alone** and explain the
  gap in the new notes.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Humanize the covered text with the `humanizer` skill in file mode, under the maintainer's exceptions in PUBLISHING §2. | `README.md` |
| 2 | Re-run the dash gate and read the **count**, not the silence. | Recorded output |
| 3 | Bump the manifest to `0.4.0`. | `plugin/.claude-plugin/plugin.json` |
| 4 | `check`, `index`, the full suite on the tree about to be tagged. | Recorded output |
| 5 | Write this record, then run the pre-publish leak check — last, because it reads files and the text most likely to trip it is a write-up about the check. | Recorded output |
| 6 | Commit, annotate the tag with what changed, push both. | `v0.4.0` |
| 7 | Create the GitHub release, accounting for the `v0.3.0` batch as well as this one. | The release |

**Shape decisions.**

**D1 — The gate runs on the tree being published, after the rewrite, never before.** PUBLISHING §3
is explicit: a rewrite is new text, and new text is what the check exists to read.

**D2 — The release notes cover everything since `v0.2.0`, not since `v0.3.0`.** The intervening tag
has no release and a one-word message, so a note starting at it would leave ten commits publicly
unaccounted for. Naming the gap is what the maintainer chose over erasing it.

**Planned outputs**
- README.md
- plugin/.claude-plugin/plugin.json

## 3. Implement

### Step 1 — the rewrite

Fourteen passages in `README.md`, each an em dash doing one of four jobs, replaced by the
construction that job actually wants: a colon where the dash introduced an explanation, a comma for
a tight aside, parentheses for a true one, and a new sentence where the clause was independent. Two
went further because the punctuation was hiding the sentence's shape:

- *Is the file here — or the link is broken* became a question and its answer, which is what the
  pair of rhetorical questions above it had already set up.
- The three rejected alternatives in the `T-098` paragraph were an em-dash-bracketed list inside a
  sentence about something else; they are now the sentence's own subject, which is also how the same
  three read in the task that rejected them.

**Nothing else in the document needed the skill.** The other patterns were checked and are absent:
no AI vocabulary from §7, headings already in sentence case, no curly quotes, no rule-of-three
padding, and the boldface and inline-header lists that §15 and §16 would have flattened are the ones
the maintainer's exception protects. That is the expected result for a document humanized once and
edited since: the drift is the punctuation, because the punctuation is what nobody was watching.

### Step 2 — the gate

```text
4 file(s) covered
gate exit 1
```

**The count first, then the silence** — four files, and nothing printed after the count. Exit 1 is
the clean outcome in this gate's table; exit 0 would have been violations and exit 2 a pathspec that
had rotted.

### Step 3 — the version

`0.3.0` → `0.4.0`, minor. The reason is one change rather than the batch's size:
[T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) makes `tasks_dir: .` a config error, so a
project carrying that value moves from a `check` that exited 0 to one that exits 2. It was exiting 0
over a tree it had never walked, which is why the change is right and also why it cannot be a patch.
Two others move text an adopter may have scripted against
([T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md),
[T-122](T-122-echo-the-typed-flag-in-the-rejected-value-message.md)), and
[T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md) removes a `CONFIG DRIFT` line an
issue-tracker project was seeing on every run.

### Step 4 — the tree being tagged

```text
Wrote tasks/README.md - 9 active, 117 closed
OK - 126 task(s), 630 field value(s), 401 reference(s), 22 dependency edge(s), 226 declared
     output(s), 1 index file(s), 154 document(s), 1271 link(s), 2 template(s), 10 template field
     value(s), 0 vocabulary row(s)
```

`test_cli` 100 OK, `test_list` 37 OK, `test_schema` 53 OK, `test_budget` 5 OK, `test_runtime` 27
`OK (skipped=3)`.

### Step 5 — the pre-publish check

Run last, after this section was written, because the check reads files and the text likeliest to
trip it is a write-up about the check. Both directions, one command:

```text
228 files covered
with the fixture excluded: nothing
without it: tests/fixtures/leak-check/samples.txt, 5 matching lines
```

The second run is the one a clean tree can never produce on its own. The lines themselves are not
quoted here, for the reason the check's own documentation gives.

### Steps 6–7 — what the release accounts for

**64 commits since `v0.2.0`, not 17.** The `v0.3.0` tag sits 47 commits into that range with no
GitHub release and a one-word message, so notes beginning at it would leave that batch publicly
unexplained. The release covers both, and says which is which rather than pretending the tag is not
there.

**Decisions & assumptions**
- **D1 — the gate runs after the rewrite** — 2026-08-11, §2.
- **D2 — the notes start at `v0.2.0`** — 2026-08-11, §2.
- **Minor, not patch, on one change rather than on volume** — 2026-08-11, step 3.
- **Assumption: the `v0.3.0` tag stays where it is.** The maintainer's answer, and the reason is that
  anyone who already fetched it keeps it, so a re-used version number would be worse than the gap.

**Outputs produced**
- [`README.md`](../README.md)
- [`plugin/.claude-plugin/plugin.json`](../plugin/.claude-plugin/plugin.json)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The dash gate prints a file count and nothing else, run on the tree being published | met | `4 file(s) covered`, exit 1, run after the rewrite per §3 of the publishing document |
| The pre-publish leak check prints nothing with its fixture excluded, and exactly that fixture without it — both runs, since a clean tree cannot prove the second | met | 228 files covered; silent with the exclusion, and exactly the fixture's five lines without it |
| The manifest reads a version above the published one, and it is a **minor** bump with the reason stated | met | `0.4.0`, and the reason is named as a single change rather than as the batch's size: T-078 turns a passing adopter tree into a failing one |
| The tag is annotated and its message says what changed, like `v0.1.0` and `v0.2.0` and unlike `v0.3.0` | met | Annotated, with the batch described and the `v0.3.0` gap named in it |
| The GitHub release exists and accounts for the commits since `v0.2.0`, including the ten that `v0.3.0` carried without notes | met | It covers all 64 commits since `v0.2.0`. The criterion said ten; the range is 47, counted rather than estimated, and the number is corrected here rather than in the criterion |
| `check`, `index` and the full suite pass on the commit being tagged | met | §3 step 4 |

**Child fix tasks raised**
- [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md)
- [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md), raised at step 6: §1's
  test covers *text a stranger reads before installing*, and a release page is that, but the worked
  list does not name it and the gate cannot read a tag message. Answered in the moment by writing
  the notes to the stricter reading, which is not a home.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | All six criteria met. **The release accounts for 64 commits, not the ten the specify guessed at** — `v0.3.0` sits 47 commits into the range rather than near its end, and the number is corrected in the review row rather than in the criterion, because the criterion is what was agreed. Two things worth carrying. **The README's drift was entirely punctuation**: every other humanizer pattern was checked and absent, which is what a document humanized once and edited since looks like, and it is why [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) is about *when* the gate runs rather than about what it matches. And **the gate's clean outcome is exit 1, not 0** — reading it the usual way round would have reported a red gate as green, which is the mistake its own table exists to prevent. |
| 2026-08-11 | → planned | **Authorisation (METHOD §3.1):** *Ship v0.2 fully*, from the maintainer on 2026-08-11, given after the last open `M2` task closed. It covers this task end to end, including the tag and the release, and nothing in `M3`. `specify` had three questions and all three were put in one turn and answered (METHOD §3.2). **The finding that shaped it:** the dash gate was run before deciding anything and came back red on `README.md` — 14 lines — and the same check against the three existing tags gives 0, 6, 13. So the README was humanized once, at `v0.1.0`, and `v0.2.0` and `v0.3.0` both shipped through a gate nobody read. That is why step 1 is a rewrite rather than a version bump, and it is also why [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) exists rather than this task quietly absorbing the reason. Two other facts corrected on the way in: `v0.3.0` **is** tagged, against a handoff note saying it was not, and it has no GitHub release. |
| 2026-08-11 | → proposed | Raised at the moment of shipping rather than found: METHOD rule 1 applies to a release like anything else, and the alternative was production with no record of what was decided or checked. |
