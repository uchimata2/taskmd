---
id: T-081
title: Gate every deployment on the humanizer pass, not just the next one
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-079, T-080]
work_package: v0.1
owner: maintainer
business_value: high
effort: m
created: 2026-08-09
updated: 2026-08-09
deliverables: [docs/repo-description.txt]
---

# T-081 — Gate every deployment on the humanizer pass, not just the next one

## 1. Specify

**Outcome**
Publishing anything fails closed when a covered document has not been through the humanizer, and it
does so on every deployment rather than on the next one. The covered set is derived, so a document
added later is gated with nothing edited.

**Why this one**
[T-079](T-079-humanize-the-human-facing-documents-before-publishing.md) wrote the rule and routed it
into the always-loaded tier, which is the strongest routing available and is **not** enforcement. The
maintainer asked on 2026-08-09 whether deployment is forced to apply it. It is not, and three holes
were found by looking:

1. T-006's plan still says the README comes back from T-079, which closed. Nothing in that plan
   applies the rule, so the step that was supposed to exist does not.
2. No acceptance criterion on T-006 mentions it, so `review` cannot fail for skipping it.
3. `docs/PUBLISHING.md` has exactly one inbound reference in the tree — the `CLAUDE.md` bullet.

**What "automatically" can and cannot mean, stated before anything is built.** The rewrite is a
judgement and no script performs it: humanizing is the skill's work, and the skill needs an agent.
What a script can do is **refuse to let a deployment proceed** while the mechanical half of the rule
is unsatisfied. So this task builds a gate that fails closed, not a rewriter. Pattern 14 is the half
that mechanizes — no em or en dashes in covered text — and it became mandatory when the maintainer
answered on 2026-08-09. It is a proxy: passing the gate does not prove a document was humanized, and
failing it proves the document was not. That asymmetry is the honest claim and the one to write down,
because a gate believed to prove more than it does is the failure `CLAUDE.md` records for validators.

**Requirements served**
`docs/SCOPE.md` §1 *Invisibility* — no correctness may depend on someone remembering to intervene.
That is the property T-079 left unsatisfied and this task is written against.

**Scope**
- In: the gate, its covered set, and where it runs in the publish procedure.
- In: the covered set becoming **derivable** — the README and any description a stranger reads —
  rather than a list somebody maintains.
- In: giving the repository description a home a gate can read. It has none today: it lives in a
  task record, which the rule excludes and no gate should scan.
- In: reconciling T-006, both the stale plan step and the missing criterion.
- Out: rewriting anything. No document is humanized here; T-006 step 5 writes the README and the
  rule then covers it.
- Out: a `taskmd` subcommand. `docs/SCOPE.md` non-goal 11 excludes it, and the leak check is the
  standing precedent for a publish-time grep that the CLI does not own.
- Out: a git hook. Installing one is a setup step somebody has to remember, which is the property
  this task exists to stop depending on.

**Acceptance criteria**
- [ ] Shown **failing first**, on a document that carries an em dash, with the actual output
- [ ] Passing on the tree as it stands, and naming how many files it read — silence alone is not a
      pass, which is [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md)'s lesson
- [ ] The covered set is **derived from the tree**, and adding a covered document does not require
      editing the gate or the rule
- [ ] The gate is correct from any working directory, on T-080's precedent
- [ ] An empty covered set does not make the gate hang or pass vacuously — `README.md` does not exist
      yet, so this is today's real case rather than a hypothetical
- [ ] The repository description has one home in the tree, and it is not a task record
- [ ] T-006 carries a step that applies the rule and a criterion that fails if it was not applied
- [ ] `docs/PUBLISHING.md` states what the gate does **not** prove

**Open questions**
- None. The maintainer authorised all three remedies and the standing requirement on 2026-08-09;
  what is left is design, recorded as decisions in §3.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Decide how the covered set is derived, so a grep can resolve it without an enumeration to maintain. | D1 in §3 |
| 2 | Give the repository description a home a gate can read, and point its old home at it. | The file, and the edited `docs/PUBLISHING.md` §4 |
| 3 | Build the gate. Prove it by **making it fail** on a planted em dash, then prove the planted text is gone. | The failing output, and the passing one with its file count |
| 4 | Handle the empty-set case explicitly, since `README.md` does not exist yet. | The behaviour, shown |
| 5 | Write the gate and its limits into `docs/PUBLISHING.md`, including what passing does not prove. | The edited document |
| 6 | Reconcile T-006: a plan step that applies the rule, and an acceptance criterion that fails without it. | The edited T-006 |
| 7 | Run `index`, `check`, the suite, the gate, and the pre-publish check. | The output of each |

**Step 3 leads with the failure because a gate that has only ever passed is not known to gate.**
This is `CLAUDE.md`'s rule about validators, and T-080 is the fresh evidence for it: a candidate fix
that went silent looked exactly like a candidate fix that worked.

**Step 4 is a step and not a detail.** A file list that resolves to nothing is the state the tree is
in right now. Two failure modes live there — a gate that hangs waiting on stdin, and one that reports
success having read nothing, which is T-034's bug for the third time in this project.

**Not in this plan:** the README, which is T-006's; and any attempt to detect humanization itself,
which §1 rules out as unmechanizable.

## 3. Implement

**Two departures from the plan, both recorded rather than tidied.** Step 3 was worked before step 2,
so the gate was proven against a tree that did not yet contain `docs/repo-description.txt` — which
is why its counts below read two and three where a reader reproducing them today gets three and
four. And step 4's stated rationale was **disproved** by running it.

**Decisions & assumptions**

- **D1 — the covered set is a pathspec over classes, not a list of files** — 2026-08-09.
  `README.md`, `docs/repo-description.txt`, and every `.claude-plugin/*.json` anywhere in the tree.
  A second plugin manifest is gated the day it appears. *Rejected: the gate reading its covered set
  from `docs/PUBLISHING.md`*, which would give the rule and the gate one shared home and no drift at
  all; it needs a shell parsing prose for a set that changes about annually, and a parser that
  mis-reads the document fails in the direction of covering nothing. *Rejected: enumerating the
  files*, which is the `reconcile_targets` failure this project already paid for. The residue is
  real and is written into `docs/PUBLISHING.md` §5: a covered document of a **new kind** needs one
  pattern added.

- **D2 — the repository description moves out of the task record into `docs/repo-description.txt`**
  — 2026-08-09. T-079 put it in its own §3, which was a fine home until a gate had to read it: task
  files are excluded from the rule, so scanning one would mean the gate reading what the rule
  exempts. `.txt` rather than `.md` because the file's entire content is the value, so nothing has to
  be stripped before use. T-079 §3 keeps the before and the audit, which is why the text reads as it
  does and is not duplicated by the value.

- **D3 — three exit codes, because two could not tell a pass from a broken gate** — 2026-08-09.
  First form printed the count and greped; a clean tree and a pathspec matching nothing **both** came
  back exit 1, distinguishable only by a number a reader might skip. Exit 2 now means the gate itself
  is wrong. This is T-080's lesson applied before it could bite: judge a run by its count.

### Step 3 — made to fail first, then to pass

Planted an em dash in a `README.md` that does not otherwise exist:

```
3 file(s) covered
README.md:1:draft <em dash> with an em dash
exit=0        violations found
```

Plant removed, on the tree as it stands:

```
2 file(s) covered
exit=1        clean
```

And with a deliberately wrong pathspec:

```
covers 0 files - the pathspec is wrong
exit=2
```

Re-run at the end, on the finished tree, which is the number to reproduce:

```
3 file(s) covered
exit=1        clean
```

### Step 4 — the hypothesis was wrong, and the real risk is the opposite one

The plan said an empty file list risks a command that **hangs** on stdin. Run, it does not: the list
arrives through a pipe, so `grep` reaches EOF immediately and reports no match. What actually
happens is worse and quieter — **zero files scanned, no output, and a result indistinguishable from
a clean tree.** That is T-034's bug and T-080's bug for the third time in this project, which is
what D3 and the printed count exist to stop. Recorded because the plan's stated reason for the step
was wrong while the step itself was right.

### Steps 5 and 6 — where it is written down, and what it repairs

`docs/PUBLISHING.md` gains §5 with the gate, its three outcomes, the `cd` rationale carried from
T-080, an explicit statement of **what passing does not prove**, and the one thing the pathspec
cannot derive. §4 is rewritten around the new home.

T-006 gains step **5a** (humanize, then run the gate) and a **ninth acceptance criterion**. Its
"the README leaves and comes back" paragraph is corrected in place with a note saying what it used
to claim, because that sentence is the record of how the hole opened: it was true while T-079 was an
open blocker and became false the moment T-079 closed, taking the only step that referenced the rule
with it.

**Outputs produced**
- `docs/PUBLISHING.md` — §4 rewritten, §5 added
- `docs/repo-description.txt` — the description's new home
- `tasks/T-006-package-document-and-publish.md` — step 5a, criterion 9, step 7 repointed, plan
  paragraph corrected

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Shown **failing first** on a document carrying an em dash, with the actual output | met | §3 step 3: a planted `README.md`, caught by name and line |
| Passing on the tree as it stands, and naming how many files it read | met | §3 step 3: `3 file(s) covered`, exit 1, on the finished tree. The two earlier runs read two and three because the gate was built before the description file landed, which §3 states |
| The covered set is derived from the tree, and adding a covered document does not require editing the gate | **partly** | Met within the classes named: a second `.claude-plugin` manifest anywhere in the tree is gated with nothing edited. **Not met for a covered document of a new kind** — a `CONTRIBUTING.md` needs one pattern added. Stated in `docs/PUBLISHING.md` §5 rather than claimed away, and D1 records the alternative that would have closed it and why it was rejected |
| Correct from any working directory | met | The `cd "$(git rev-parse --show-toplevel)"` prefix, on T-080's precedent and for its reason |
| An empty covered set does not hang or pass vacuously | met | Exit 2 with a message, §3 step 3. The plan's reason for this criterion was wrong and §3 step 4 says so: it cannot hang, and it can pass vacuously, which is the more dangerous half |
| The repository description has one home in the tree, and it is not a task record | met | `docs/repo-description.txt` (D2). T-079 §3 keeps the audit that produced the text, not the value |
| T-006 carries a step that applies the rule and a criterion that fails without it | met | Step 5a and criterion 9 |
| `docs/PUBLISHING.md` states what the gate does not prove | met | §5 *What passing does not prove*: pattern 14 is a proxy, failing proves the rewrite did not happen, passing proves one pattern is absent |

**Eight criteria, seven met and one partly.** The partial is left partial rather than reworded: a
gate that cannot see a new *class* of document is a real limit, and the honest place for it is the
document the next person reads, not a criterion quietly softened to fit what was built.

**What this task does not achieve, restated because the request was "automatically".** No script
humanizes anything. The gate refuses a deployment while the mechanizable half of the rule is
unsatisfied, and that is the whole of the automation. A green gate on a machine-written README is
possible and always will be.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Seven criteria met, one partly and left that way. The gate is a grep in `docs/PUBLISHING.md` §5, proven in all three of its states before being written down: caught a planted em dash, ran clean on the tree at two files, and returned exit 2 on a pathspec resolving to nothing. That third state exists because the first form could not tell a clean tree from a broken gate — both came back exit 1, differing only in a number a reader might skip, which is T-080's lesson arriving one task early. The plan's reason for the empty-set step was **wrong and is recorded as wrong**: an empty list cannot hang, because it arrives through a pipe, and what it really does is scan zero files and look exactly like success. The description moved out of T-079 §3 into `docs/repo-description.txt`, because a gate that had to read it would otherwise be scanning a task file, which the rule exempts. T-006 gains step 5a and a ninth criterion, and its stale paragraph is corrected in place rather than rewritten, since that sentence is the record of how the hole opened. The partial criterion is the one that matters most: the pathspec derives over classes, so a second manifest is gated free, and a covered document of a **new kind** still needs one pattern added. That is in the document rather than argued away. |
| 2026-08-09 | → planned | Seven steps, failure-first at step 3 and the empty covered set promoted to a step of its own at step 4, because that is the tree's actual state today and it is where both of this project's recurring bugs live: a command that hangs on stdin, and one that passes having read nothing. |
| 2026-08-09 | → specified | Raised after the maintainer asked whether deployment is forced to apply T-079's rule. It is not, and three holes were found rather than assumed: T-006's plan points at a closed task for a hand-off that can no longer happen, no criterion on T-006 mentions the rule, and the rule has one inbound reference in the whole tree. The specify section says up front what "automatically" can mean, because the rewrite is a judgement no script performs: this builds a gate that fails closed, and pattern 14 is the mechanizable half. Passing does not prove a document was humanized; failing proves it was not, and that asymmetry is written into the criteria rather than left to be discovered. |
| 2026-08-09 | → proposed | Created from the maintainer's answer: all three remedies, and every future deployment gated rather than only the next one. |
