---
id: T-098
title: Decide who checks the links in a document only a successor reads
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-002, T-034, T-080, T-094, T-095]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-10
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/fixtures/README.md, README.md]
---

# T-098 — Decide who checks the links in a document only a successor reads

## 1. Specify

**Outcome**
A project is told what validates the pointers in its machine-local working state — resumption notes,
scratch plans, anything gitignored that a *later session* reads — or is told plainly that nothing
does, so the gap is a decision rather than an accident.

**Why this one**
[T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) excluded gitignored
documents from `check` on the argument that a dead link inside something no reader can reach is a
promise to nobody. **That argument has a hole, and this repository walked straight into it within the
hour.** The live handoff is gitignored, so writing one on 2026-08-10 moved the skipped count from 31
to 32 and its ten links went unvalidated. They had to be resolved by hand.

**The walk that is now bypassed exists precisely for this document.** `markdown_files` walks
dot-directories rather than globbing, and both its docstring and `tests/fixtures/README.md` give the
same reason: `glob`'s `**` skips dot-directories, *"which is how a broken link in a live handoff
pointer stayed invisible"*. The fixture `broken-link` puts its defect in `.notes/` to pin that. So the
project paid for a deliberate walk to reach this exact case, and T-094 has now put the case back out
of reach for a different and individually sound reason.

**Two decisions, each defensible, that contradict on one document.** T-094's population is "whoever
clones the repository", and for a handoff that population is empty. The population that actually reads
a handoff is the next session, for whom the pointer is the whole artefact — a dead one there is not a
cosmetic defect, it is the resumption failing. Neither decision is wrong; nothing reconciles them.

**What is actually excluded, measured rather than assumed (2026-08-10).** The count is now 37, and
the set is not one kind of thing:

| Documents | What they are | Who reads them |
| :--- | :--- | :--- |
| 32 | `.handoff/processed_*`, consumed handoff archives | nobody, ever again |
| 3 | `.pytest_cache/README.md`, in three places | nobody; a tool wrote them |
| 2 | `control/`, machine-local working state | the next session |

Plus the live handoff when one exists. So **fewer than one in ten excluded documents has a reader at
all**, and the pile grows by one every time a handoff is written — 31 at T-094's close, 32 an hour
later, 37 now. Two consequences the decision has to survive. A blanket "read everything ignored"
would be wrong about 35 of 37 and would grow more wrong with use; and any selection rule that works
by *directory* must not swallow `.handoff/processed_*`, which sits in the same folder as the one
document that matters.

**Requirements served**
R-16.

**Scope**
- In: whether `check` gains a way to validate documents it currently excludes, and what selects them
  — a flag, a config key naming paths to read regardless, or nothing.
- In: whether the answer is instead that this is not `check`'s job, in which case say whose it is.
  The handoff skill writes the document and could resolve its own pointers; that is a real answer and
  should be rejected explicitly rather than by omission.
- In: what happens to `broken-link` and the dot-directory rationale, which currently justify a walk
  by a case the tool no longer reaches. If the answer is "nothing does", that fixture's stated reason
  is stale and must be rewritten rather than left to read as coverage.
- Out: the document-side rule itself. T-094 decided it on evidence and this task does not reopen it;
  the question is what covers what it excluded.
- Out: the target side, which is [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md).

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `markdown_files` and `check_links` — the docstring of the
  first states the reason the second now bypasses.
- `tests/fixtures/README.md`, the `broken-link` paragraph.
- [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) §3, for the argument this
  finds the boundary of, and its §4 second row for why the evidence could not be a committed fixture.

**Acceptance criteria**
- [ ] The decision is recorded with its rejected alternative, whichever way it goes
- [ ] If something covers the excluded documents: a dead link in a document this repository's own git
      would not publish is reported, shown failing first, and the archives and tool-written files in
      the table above are still **not** read
- [ ] If nothing does: `broken-link`'s stated reason and `markdown_files`' docstring no longer claim
      a case the tool does not reach, and the adopter-facing text says what is unvalidated
- [ ] Whichever way it goes, a run still reports what it did **not** examine, and a reader of that
      output can tell why the document count moved

**A committed fixture cannot carry this case**, and the second criterion is worded to allow for it.
The document has to be one git declines to publish, so committing it is the contradiction; a fixture
project's own `.gitignore` is honoured by the *host* repository's git, which means the file never
enters the tree a clone receives. T-094 hit this and built the project inside the test instead — its
§4 second row records why, and the same route is open here.

**Open questions**
- **Whose job it is.** The maintainer's, and it stays open past this phase deliberately — the
  criteria above are judgeable either way, so `specify` does not need the answer and `plan` cannot
  start without it. Answer it as plan step 1 and record it with its rejections in §3, which is the
  route [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) took through the
  same shape. Note the trap before answering: the cheap reading is "add `--all` and move on", but a
  flag nobody remembers to pass is the same silence with a feature attached — which is the failure
  mode T-095 and T-080 were both raised for.

**Authorization**
The maintainer, on 2026-08-10, authorised working every open `v0.2` task through its full lifecycle —
specify, plan, implement, review, fix, commit and push — one task at a time. It covers that set and
nothing outside it, and it includes deciding the owner-question above rather than returning it.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Answer the open question, and record every rejected alternative with the price that rejected it | Decisions in §3 below |
| 2 | Establish by running, not by reading, that the shipped `broken-link` fixture still catches the class it names — its document is tracked, so the document-side filter never reaches it | The run quoted in §3 Evidence |
| 3 | Rewrite `markdown_files`' docstring to justify the walk by a case the tool still reaches, and to name where the filter that took the old one away now lives | `plugin/skills/taskmd/taskmd/cli.py` |
| 4 | Rewrite `broken-link`'s paragraph so it states what the fixture proves rather than the case that motivated it | `tests/fixtures/README.md` |
| 5 | Say adopter-facing which pointers nothing validates and whose job they are, beside the rule T-094 already states there | `README.md` |
| 6 | Re-run `check`, `index` and the suite, and confirm the excluded count and the fixture behave as §3 records | Evidence in §3 |

**Shape of the deliverable, and what was rejected.** This answer changes no behaviour, so its
deliverable is prose in three places and **no new test**. Rejected: adding a case that asserts a
dead link in a gitignored document goes unreported. T-094's `CheckAnswersTheQuestionAFreshCloneWouldAsk`
already proves it in four — the document skipped and counted, the same project without git reading
everything and saying so, the target-side pointer still resolving, and the `Scope` line surviving a
failing run. A second copy of a proven fact is what this project's one design rule forbids, and it
would drift from the first the moment either moved.

Step 2 sits at the front because it is the assumption that would invalidate steps 3–5: if the
fixture's document were *not* tracked, the walk would have lost its last live justification and the
answer would have to be a different one.

## 3. Implement

**Decisions & assumptions**

- **Nothing in `check` covers a document a clone would not receive, and the tool says so** —
  2026-08-10. taskmd's reach ends at the tree a clone receives; the pointers inside machine-local
  working state belong to whatever writes that state. The gap is now a decision with a name on it
  rather than an accident, which is what the outcome asked for. What changes is only that the
  repository stops claiming a coverage it does not have.
- **Rejected: a config key naming paths read regardless of git** — 2026-08-10, and it was the
  strongest rival right up to the moment its price was read. The shipped schema's own *Adding a key
  to this file is a breaking change* composes three rules already in force — a config **replaces**
  the defaults rather than merging, so every key must be written, so a **missing** key is an error
  naming it. A new key therefore fails every project that wrote a config, on its next upgrade, with
  an error naming a key nobody there has heard of, in a project that changed nothing. Three projects
  run this plugin. That is the price; what it buys is reading two documents in *this* repository and
  possibly none in theirs.
- **Rejected: `--all` or `--include-ignored`** — 2026-08-10. The cheap reading, and the one the
  specify phase warned about: a flag has to be remembered on every run, so it is the present silence
  with a feature attached. T-080 and T-095 were both raised against exactly that shape.
- **Rejected: read everything and downgrade a finding in an unpublished document to a note** —
  2026-08-10. It needs no configuration and it would have covered the live handoff. It also re-admits
  35 of the 37 excluded documents — 32 consumed archives and 3 files a test runner wrote — and that
  set grows by one every time a handoff is written. A report with an unbounded and mostly worthless
  denominator is one people stop reading, which returns the silence by a longer road.
- **Rejected: derive it — read an ignored document that a published one points at** — 2026-08-10.
  Configuration-free, and it is this project's own design rule applied to the question, so it was
  the most attractive of the four. It fails on the case that raised the task: nothing published
  Markdown-links to the live handoff, so the one document that matters is exactly the one it does not
  reach. It also makes this answer depend on
  [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md), which
  the scope puts out.
- **The distinction is not derivable, which is what settles it.** No signal in the tree separates
  `.handoff/HANDOFF.md` from `.handoff/processed_*`: same folder, same shape, same ignore rule, and
  neither is pointed at. Git cannot tell them apart and neither can reachability. Only a declaration
  could — and the paragraph above is what a declaration costs here.
- **The walk into dot-directories stays, and its stated reason changes** — 2026-08-10. Its docstring
  and the fixture index both justify it by the live-handoff case, which the document-side filter now
  removes. The walk still earns its keep on *tracked* documents in dot-directories, of which this
  repository has several, and the fixture proves that rather than the case that motivated it.
- **No new test** — 2026-08-10, carried from the plan and confirmed once the existing one was read.
  T-094's `CheckAnswersTheQuestionAFreshCloneWouldAsk` already asserts all four behaviours this
  answer commits to. Asserting them again would be a second copy of one fact.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `markdown_files`' docstring
- `tests/fixtures/README.md` — the `broken-link` paragraph
- `README.md` — what nothing validates, and whose job it is

**Evidence**

The excluded set, listed rather than counted — this is what made the decision, and no run reports it,
which is why it is written here once:

| Documents | What they are | Who reads them |
| :--- | :--- | :--- |
| 32 | `.handoff/processed_*` | nobody, ever again |
| 3 | `.pytest_cache/README.md`, in three places | nobody; a test runner wrote them |
| 2 | `control/` | the next session |

The fixture still catches its class, run on the shipped project — so the walk keeps its job while
losing its old reason:

```
BROKEN LINK   .notes/scratch.md -> gone.md

1 problem(s) - 1 task(s), ..., 2 document(s), 1 link(s), ...
Scope  0 document(s) not read: a clone would not receive them
```

`0 document(s) not read` is the load-bearing part: the fixture's `.notes/scratch.md` is **tracked**,
so the document-side filter never reaches it and the report is the walk's doing.

This repository, after:

```
OK - 114 task(s), ..., 142 document(s), 1098 link(s), ...
Scope  37 document(s) not read: a clone would not receive them
```

**The suite: 4 failed, 183 passed, 2 subtests passed.** All four are in `tests/test_runtime.py` and
none is this change — the identical four fail with the working tree stashed, checked rather than
assumed:

```
FAILED tests/test_runtime.py::Launchers::test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has
SUBFAILED(entry='skills/taskmd/taskmd.sh') ...::test_every_entry_point_produces_what_the_module_produces
SUBFAILED(entry='bin/taskmd') ...::test_every_entry_point_produces_what_the_module_produces
FAILED tests/test_runtime.py::Launchers::test_the_shell_launcher_produces_what_the_module_produces
4 failed, 25 passed, 2 subtests passed in 5.26s
```

Three are the machine's two `bash` interpreters ([T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md))
and the fourth is the cross-platform link defect annotated onto
[T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md).

**What was not verified, and could not be.** The decision's own subject — that a dead pointer in a
machine-local document goes unreported — is asserted by T-094's four cases, not re-run here. The
thing this task actually changes is prose, and prose has no mechanical check; the smallest real use
available was to read each rewritten passage against the run above and confirm it claims exactly what
the run shows. That is weaker than use by a stranger, and `review` should judge it as such.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The decision is recorded with its rejected alternative, whichever way it goes | met | Four rejections in §3, each with the price that rejected it rather than a reason it was disliked. The one that mattered is the config key: it is priced by a rule already written in the shipped schema, so the rejection can be checked by a reader who disagrees with it. |
| If something covers the excluded documents: … | n/a | The branch not taken. Its condition is false by §3's first decision, and the criterion was written conditionally in `specify` so that either answer could be judged. |
| If nothing does: `broken-link`'s stated reason and `markdown_files`' docstring no longer claim a case the tool does not reach, and the adopter-facing text says what is unvalidated | met | All three rewritten. Both the fixture prose and the docstring now say what they *do* cover and name T-098 for what they do not, so neither reads as coverage. `README.md` states plainly that machine-local pointers are validated by nothing, whose job they are, and where to reopen it. |
| Whichever way it goes, a run still reports what it did **not** examine, and a reader of that output can tell why the document count moved | met | `Scope  37 document(s) not read: a clone would not receive them`, unchanged and printing on both branches. The count did not move, which is the honest outcome of an answer that changes no behaviour — and the second clause is satisfied trivially rather than by design, which is worth saying. |

**Judged as weaker than it looks.** `implement` recorded that this deliverable is prose with no
mechanical check, and that the substitute used was reading each passage against the run. That is
below the standard the method sets for verification, and it is carried here rather than dressed up:
the risk it leaves is a rewritten paragraph that is internally plausible and still wrong about the
tool. It is bounded by the three passages being short and by each naming a run that contradicts it if
it drifts.

**Child fix tasks raised**
- none. Nothing was found that this task's criteria do not cover; the one gap is the verification
  standard above, which is a property of the deliverable rather than a defect to fix.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | (no change) | **`type` fix → decision**, by [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md)'s sweep of all 123 tasks. The test it settled reads a task's **stated outcome**: an answer someone else could act on is a `decision`, whatever the task also changes. A classification corrected, not a reopening — status, body and every other field are untouched. |
| 2026-08-10 | → done | Three criteria met, one not applicable by the branch taken. The answer is that nothing covers a document a clone would not receive, and the work was removing three claims that it did. Worth knowing for the next task that reaches for configuration: the cost of a new config key here is not the code but the schema's replace-don't-merge rule, which turns any addition into a failure for every project that wrote a config. That priced out the only rival that would have closed the gap. |
| 2026-08-10 | → planned | Six steps, and the one that mattered was reading the config schema's own *Adding a key to this file is a breaking change* before planning a key. A config replaces the shipped defaults rather than merging, every key must be written, and a missing key is an error naming it — so the obvious answer would have failed all three adopting projects on their next upgrade, on a key none of them asked for. That priced the strongest rival out before a line was written. No new test: T-094 already proves all four behaviours this answer asserts. |
| 2026-08-10 | → specified | Criteria sharpened by measuring the excluded set instead of arguing about it: 37 documents, of which 35 are consumed handoff archives and files a test runner wrote, and 2 are the machine-local state a successor actually reads. That kills "read everything ignored" before `plan` starts, and it rules out selecting by directory, since the one document that matters shares a folder with the 32 that do not. Second criterion reworded — it asked for a *fixture*, which cannot exist: a document git declines to publish cannot also be committed, and T-094 met the same criterion with a project built inside the test. The owner-question is deliberately still open; it changes the plan, not the criteria. |
| 2026-08-10 | → proposed | Found by writing a handoff an hour after closing T-094: the skipped count went 31 to 32 and the document that disappeared was the one whose invisibility had justified walking dot-directories in the first place. Not found by review, and not findable by one — `check` exits 0 either way, which is the whole point. `high` because the project has now twice paid for a check that read fewer files than anyone believed (T-034, T-080) and this is the same shape arriving through a change made deliberately; `s` because the mechanism is a line, and only the rule is hard. |
