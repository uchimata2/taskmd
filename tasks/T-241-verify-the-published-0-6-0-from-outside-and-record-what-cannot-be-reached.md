---
id: T-241
title: Verify the published 0.6.0 from outside, and record what cannot be reached
type: audit
status: done
phase: review
parent: null
blocked_by: [T-231]
related: [T-085, T-231, T-253]
work_package: M6
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
deliverables: []
adopter_visible: no
---

# T-241 — Verify the published 0.6.0 from outside, and record what cannot be reached

## 1. Specify

**Outcome**

The `0.6.0` artifact is checked from outside this working tree — installed the way an adopter
installs it, and exercised — with every part that **cannot** be reached from any machine here named
rather than left as an implied pass.

**Where this came from**

The owner answered [T-231](T-231-cut-the-next-release.md)'s first question **yes** on 2026-08-23: a
verification-from-outside task follows the release.
[T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) is why. `0.5.0`
had such a task and `0.4.0` did not, and the difference is the whole of what T-085 records — a
release verified only by the tree that produced it has been verified by the one party that cannot
see its own gaps.

**And T-085's other half is the reason this record exists rather than a checklist.** It found that
**half of that verification was unreachable from any machine here**, and closed with half proven and
half not. Repeating the reachable half is cheap; the value of this task is that it says, again and
in the open, which half was not — because an audit that quietly drops what it could not do reads
exactly like one that found nothing wrong.

**Scope**

- In: installing the published `0.6.0` as an adopter does, from the published artifact rather than
  from this tree, and exercising what an install is supposed to give them
- In: naming every part that cannot be reached from any machine available, with the reason — T-085's
  unreachable half re-checked rather than assumed still unreachable
- In: whether anything shipped in `0.6.0` that should not have — the pre-release audit document, the
  new `check --classes` flag, the two repaired bindings and the reader protocol all went in on
  2026-08-23
- Out: the release itself, which is [T-231](T-231-cut-the-next-release.md)
- Out: the release note, which is
  [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md)
- Out: repairing anything found. A finding here is its own task — this is an audit and
  [`audit`](../plugin/skills/taskmd/docs/method/audit.md)'s no-inline-fix rule applies

**Inputs**

- [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) — what was
  proven for `0.5.0`, what could not be, and why
- [T-231](T-231-cut-the-next-release.md) — the release this verifies, and the three answers that
  shaped it
- the published `0.6.0` artifact, once it exists

**Acceptance criteria**

- [ ] The plugin is installed from the **published** artifact, not from this working tree, and the
      route used is stated
- [ ] What an adopter gets is exercised rather than inspected — at least one command run and one
      skill reached from the install
- [ ] Every part that could not be reached is **named**, with the reason, and T-085's unreachable
      half is re-checked rather than carried forward as still-unreachable
- [ ] Anything shipped that should not have been is named; if nothing, that is stated as a checked
      result rather than left silent
- [ ] Every finding becomes its own task; none is repaired here

**Open questions**
- **None.** The shape is T-085's and the owner has already said this follows the release.

## 2. Plan

**What counts as a finding, stated before looking** — [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
step 2, and the reason it is here rather than in §1 is that the threshold is part of how *this*
subject is examined:

- a statement an adopter would act on that the installed `0.6.0` contradicts;
- a file the install carries that should not ship, or lacks that the project promises;
- a documented route that does not run when followed as written.

**Not a finding:** prose that could be worded better; a gap already carried by an open task; a
difference between the install and this working tree that is explained by commits made after the
tag. The third exclusion is the one that will do work — the tree is 23 commits ahead of `v0.6.0`,
so *the install is missing something the tree has* is the expected state and not a defect.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Establish what the published artifact **is** — tag, release, and whether it carries built assets or is source-only — and prove the installed copy on this machine came from **there** rather than from this tree. A cache directory named for a version is a claim, not provenance. | A stated route and the evidence that the install is not this tree |
| 2 | Inventory the install against `plugin/` **at the tag**, not at `HEAD`, since the tree has moved. Anything in the install and not at the tag, or the reverse, is examined. | A file-level comparison, and the answer to criterion 4 either way |
| 3 | Exercise it: run a command **from the install** and reach a skill **from the install**. Neither may resolve back into this working tree — check what the command actually loads, not only that it exits 0. | Captured output, plus proof of which copy answered |
| 4 | Re-check T-085's unreachable half rather than inherit it: is `claude plugin marketplace add` / `claude plugin install` runnable from any machine available now? Answer it by trying, and record what stops it if anything does. | A dated answer, with the command and its result |
| 5 | Check the four things `0.6.0` newly shipped are in the install: the pre-release audit document, `check --classes`, the two repaired bindings, and the reader protocol. | Present or absent, per item |
| 6 | Record every finding in this record with a severity, including the ones needing no action, and raise a child task per finding that needs one. Nothing is repaired here. | The findings table, and the child tasks |

**Decisions taken here**

- **The subject is the install, not a fresh never-seen-it machine** — 2026-08-23. §1's criteria ask
  for *the published artifact rather than this tree*, which is a different and weaker condition than
  T-085's *a machine that has never held any of this*. Conflating them is what would make this record
  unrunnable for the same reason T-085 was. *Rejected: waiting for a clean machine*, which
  [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) already recorded
  as a decision whose premise had weakened, and which is that record's to revisit and not this one's.

- **Step 1 proves provenance rather than assuming it** — 2026-08-23. A directory called `0.6.0` under
  a cache is a name somebody wrote; what makes it the published artifact is where it was fetched
  from. This is the step most likely to turn the whole audit vacuous if skipped, which is why it is
  first — a comparison against a copy of this tree would report *no differences* and mean nothing.

- **Step 2 compares against the tag, not `HEAD`** — 2026-08-23. The tree is 23 commits ahead, several
  of them written today, so comparing against `HEAD` would generate a finding per commit and bury a
  real one. The exclusion is written into the threshold above rather than applied silently while
  reading the results.

## 3. Implement

**Decisions & assumptions**

- **Step 1 justified itself immediately, and this is the decision the whole audit rests on** —
  2026-08-23. The machine carries `~/.claude/plugins/cache/taskmd/taskmd/0.6.0`, which reads as an
  installed release. The host's own registry says otherwise: `known_marketplaces.json`'s entry for
  `taskmd` gives its `source` as **`directory`**, and the `path` beside it is this repository's own
  checkout. *The path itself is not quoted here, deliberately* — `docs/PUBLISHING.md` §6 warns that
  the text most likely to trip the leak check is the write-up of a task about a matched line, and
  quoting it did trip the gate before this sentence replaced it.

  **So it is a directory install of this working tree.** Auditing it would have compared the tree
  against itself, found no differences and reported a pass — the vacuous outcome the plan named. The
  subject was therefore taken as a fresh clone of the published tag, `cb0702c` / `v0.6.0`, fetched
  from `github.com/uchimata2/taskmd`. *Rejected: the cache*, for the reason above.

- **The plugin install route was not run, on the owner's decision of 2026-08-23** — see *What could
  not be reached*, below. It is recorded as unreachable with today's reason, not with T-085's.

- **My own exercise polluted the measurement, and the number it produced is a known trap** —
  2026-08-23. Running the published launcher inside the clone created six `.pyc` files, taking a
  filesystem count of `plugin/skills/taskmd/` from 25 to **31**. That is exactly the number
  [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) predicted *an
  adopter's own `ls` would show after they run the tool once*. Recorded rather than quietly
  discounted, because 31 is the figure a reader arrives at independently and it is not evidence of
  anything shipping.

**Outputs produced**

This is an audit; its deliverable is the findings below, and nothing was repaired.

### What was examined, and with what

| Step | Done with | Result |
| :--- | :--- | :--- |
| 1. Provenance | `known_marketplaces.json`; `git clone --branch v0.6.0` | The local install is **not** the release. Subject re-taken as the published clone, `cb0702c` |
| 2. Inventory vs the tag | `git ls-files plugin/` against the cache | Published `plugin/` is **28 files**; the cache is **40**. Nothing published is missing from the cache |
| 3. Exercise | the **published** launcher, on a fresh empty project outside both trees | `check exit=0`; `check --classes exit=0` listing the class names |
| 4. T-085's unreachable half | see below | Re-checked. Still not run, for a **different** reason than T-085's |
| 5. What `0.6.0` newly shipped | file presence in the clone | All present: `pre-release-audit.md`, `classes.py` and the `--classes` flag, both repaired bindings, `uninvolved-reader.md` |
| 6. Host's own validator | `claude plugin validate` on the clone | Passes, with one warning: `plugin.json` names no `author` |

### Findings

| # | Finding | Severity | Action |
| :-- | :--- | :---: | :--- |
| 1 | **`README.md` says `plugin/skills/taskmd/` is "21 files". The published `0.6.0` has 25.** A copied-skill adopter uses that number to check the copy is complete, and it is now wrong by four. [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) verified it as **true** for `0.5.0` and recorded it as *"a claim nobody had checked from outside"* — so it was right when written and the folder grew past it | Medium | Child task — [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md) |
| 2 | The published artifact carries nothing it should not: no `control/`, no live handoff, no local scratch, and the cache's 11 extra `.pyc` files are absent from it | — | No action. Checked, and it is the answer criterion 4 asks be stated rather than left silent |
| 3 | The README's quoted empty-project `check` output is **byte-identical** to what the published tool prints — compared with `diff`, not by eye | — | No action. Recorded because a quoted output is the kind of claim that reads as evidence and is never re-run |
| 4 | `plugin.json` names no `author`; the host's own validator warns on every validate of the published plugin | — | **No action, and the threshold is why.** It is not a statement an adopter acts on, not a missing promise, and not a route that fails. Raising it would be lowering the bar after looking, which is the thing step 2 of [`audit`](../plugin/skills/taskmd/docs/method/audit.md) exists to stop. Recorded so the owner can decide, not so a session can |
| 5 | This machine's `0.6.0` install is a **directory** install of the working tree, so every session served the plugin here is served the tree | — | No action **here**. It is a fact about this machine, not about the release, and the boundary it turns on is already settled in [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md). It is written up because it is what made step 1 necessary, and because anything reading that cache as "the release" is wrong |

### What could not be reached

**The plugin install route — `claude plugin marketplace add` then `claude plugin install` — was not
run, and the reason has changed since T-085.**

T-085 could not run it because the candidate profile had no Node, no `claude` CLI, and installing one
ended in an interactive sign-in. **Both halves of that are now false**: `claude` 2.1.241 is on this
machine's `PATH` and authenticated. So the re-check the third criterion asks for produced a real
answer rather than an inherited one — *unreachable in August was a fact about the machines of that
week*, and it no longer holds.

**What stops it today is different and is a decision, not an obstacle.** The marketplace named
`taskmd` on this machine points at the working directory. Running the route means removing that
entry, adding the GitHub one, installing, and restoring — with a restart needed before the
maintainer's setup behaves as before, and a hand repair if it fails partway. **The owner was asked on
2026-08-23 and chose not to**, on the grounds that an audit which breaks the maintainer's development
loop to prove a route costs more than the answer is worth.

**So the honest statement of coverage is:** the published artifact was fetched, inventoried,
exercised and validated from outside this tree; the *host's own install mechanism* applied to the
*published* source was not exercised, and no machine available today is free of that cost. What is
proven is that the artifact is complete and runs. What is not is that `claude plugin install` fetches
and lands it correctly — which is a claim about the host, exercised for `0.5.0` no more than for
`0.6.0`.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The plugin is installed from the **published** artifact, not from this working tree, and the route used is stated | met for one route, **not for the other, and both are stated** | The published tag was fetched from `github.com/uchimata2/taskmd` at `cb0702c` and used as the subject — which is the *plain skill* route the README documents, followed as written. The **plugin** route was not run; that half is the third criterion's business and is carried onward by [T-253](T-253-exercise-the-plugin-install-route-against-a-published-release.md) |
| What an adopter gets is exercised rather than inspected — at least one command run and one skill reached from the install | met | `check` and `check --classes` both run from the **published** launcher against a fresh project outside both trees, `exit=0` each. The skill's own documents were reached by pointing `check --root` at the copied skill folder: 17 documents, 119 links, all resolving |
| Every part that could not be reached is **named**, with the reason, and T-085's unreachable half is re-checked rather than carried forward as still-unreachable | met | §3 *What could not be reached*. **The re-check produced a different answer, which is the point of asking for one**: T-085's reason — no Node, no `claude` CLI, interactive sign-in — is now false. What blocks it today is a decision the owner took on 2026-08-23, and it is written as a decision with its date |
| Anything shipped that should not have been is named; if nothing, that is stated as a checked result rather than left silent | met | Stated, not left silent: the published artifact carries no `control/`, no live handoff and no local scratch, and the 11 `.pyc` files in this machine's cache are **absent** from it. The cache-versus-release difference is finding 5, and it is about the machine rather than the release |
| Every finding becomes its own task; none is repaired here | met | One finding needed action and became [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md), now closed. Four needed none and are recorded with reasons, including one held **below** the threshold rather than quietly promoted. Nothing in the audited artifact was repaired here |

**Adopter-visible?** no. This record examined `0.6.0`; it changed nothing an adopter receives. The
change that reached them came from its child [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md),
which carries `adopter_visible: yes` on its own record — which is the field working as
`docs/PUBLISHING.md` §7 intends, the judgement sitting on the task that did the thing rather than on
the one that noticed it.

**Child fix tasks raised**
- [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md) — finding 1, the README's
  file count. **Closed**, so this umbrella may close: [`audit`](../plugin/skills/taskmd/docs/method/audit.md)
  step 5 and METHOD §4.

**One task raised as a soft link, and why it is not a child.**
[T-253](T-253-exercise-the-plugin-install-route-against-a-published-release.md) carries the plugin
install route. It is **not** a child, because this record's outcome is complete — the artifact was
fetched, inventoried, exercised and validated, and what could not be reached is named, which is
exactly what §1 asks for. T-253 asks for something *beyond* that outcome and waits on a decision
nobody here controls, so a hierarchy edge would hold a finished audit open indefinitely. That is
METHOD §4's residual case, and getting it wrong is the error that section names.

**It was raised because nothing open carried the route.** Measured while writing this review: a
`grep` over the backlog for `plugin install` / `marketplace add` returned this record and nothing
else, and [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) is
`done`. One more closure and the obligation would have left every view the project has.

**One defect in this record was caught by the project's own gate and repaired here.** §3 originally
quoted the marketplace entry verbatim, absolute local path included, and
`test_every_hit_is_one_the_document_accepts` went red naming this file. That is not an inline fix of
the audited artifact — it is a leak in the audit's own write-up, and `docs/PUBLISHING.md` §6 predicts
exactly it: *"the text most likely to trip it is the write-up of a task about the check"*. The path
is now described rather than quoted.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | → done | **`review` done and the umbrella closed**, under the grant below. Five criteria: four met, one **met for the plain-skill route and not for the plugin route, with both stated** rather than averaged into a pass. Its child [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md) closed first, which is what lets this close at all. **One task was raised as a soft link, not a child** — [T-253](T-253-exercise-the-plugin-install-route-against-a-published-release.md), the plugin install route: this record's outcome is complete and T-253 asks for something beyond it, so a hierarchy edge would hold a finished audit open on a decision nobody here controls. It was raised because a grep found **nothing open** carrying that route and T-085 had already closed over it once. **The project's own leak gate caught a defect in this write-up** and it was repaired here: §3 quoted an absolute local path, which `docs/PUBLISHING.md` §6 names as the likeliest way a task about a check re-creates what it catches. |
| 2026-08-23 | → in_progress | **`implement` done — the audit ran**, under the grant below. **Step 1 paid for itself**: this machine's `0.6.0` is a *directory* install of the working tree, per the host's own registry, so auditing the cache would have compared the tree against itself and reported a pass. The subject was re-taken as a fresh clone of the tag, `cb0702c`. **Five findings, one needing action** — [T-252](T-252-correct-the-readme-s-file-count-for-the-copied-skill.md), the README's "21 files" against the artifact's 25. **T-085's unreachable half was re-checked and its reason is now false** — `claude` is installed and authenticated here; what stops the route today is that running it would replace the maintainer's directory install, and the owner chose on 2026-08-23 not to. |
| 2026-08-23 | → planned | **`specify` closed and `plan` written**, under the grant below, re-stated by the owner the same day on resuming: *"continue with T-241, full lifecycle, commit and push."* `specify` needed nothing — its open questions were already none, and no criterion moved. The plan carries the two things [`audit`](../plugin/skills/taskmd/docs/method/audit.md) says belong there rather than in a standing checklist: **the finding threshold, stated before looking**, and how this subject in particular is examined. **This record now carries the `adopter_visible` prompt** and still no field, which is [T-251](T-251-give-the-open-records-the-adopter-visible-prompt-they-predate.md) working as intended — the prompt asks at close, the field is written when it is answered. |
| 2026-08-23 | (no change) | **The owner authorises the full lifecycle on this record, with commit and push** — given 2026-08-23 in these words: *"Work T-250, T-241, full lifecycle, commit and push, including anything raised during the work of these tasks."* Recorded here rather than only in the handoff, because an authorisation kept anywhere else is one a later session can miss or stretch to a record it never covered. **What it covers:** this record's `specify` through `review`, committing and pushing, and the same for any task raised *by this work*. **What it does not:** any other task in the backlog — T-244, T-246, T-247, T-248 and T-240 are untouched by it. |
| 2026-08-23 | → proposed | Raised on the **project owner's** answer of 2026-08-23 to [T-231](T-231-cut-the-next-release.md)'s first question. **Raised now rather than at tag time**, and that is the point of raising it at all: an answer recorded only inside a struck-through question is invisible to every view, which is the defect [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) recorded when its own wait lived in a Log row. `blocked_by` names T-231, so the ordering rule reports this held until the release exists rather than a session having to remember a sentence. **`audit` by type and by the rule that follows from it**: its findings become their own tasks and none is repaired here. **Not part of the unattended grant** — that grant excluded the release and anything scheduled after it, and this is scheduled after it. Whoever picks it up is acting on the owner's answer above, not on that grant. **The half T-085 could not reach is in scope as a re-check, not as an inherited excuse**: unreachable in August is a fact about the machines of that week, and carrying it forward untested is how an audit comes to report what its author already expected. |
