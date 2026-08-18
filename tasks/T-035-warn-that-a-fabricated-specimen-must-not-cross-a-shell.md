---
id: T-035
title: Warn that a fabricated specimen must not cross a shell
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-034, T-013, T-018, T-047, T-118]
work_package: M2
owner: maintainer
business_value: medium
effort: xs
created: 2026-08-06
updated: 2026-08-11
deliverables: [docs/PUBLISHING.md]
adopter_visible: no
---

# T-035 — Warn that a fabricated specimen must not cross a shell

## 1. Specify

**Outcome**
`docs/PUBLISHING.md` §6 warns that a fabricated specimen must be written by something that does not
shell-escape it, so the next author who proves the check by making it fail is not handed a false
result.

**Why this one**
Found during [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md)'s `implement`,
which had to produce exactly such a specimen. Written through the shell, the UNC line lost one
leading backslash in transit and stopped being a UNC path; a quoted heredoc did not help. The run
then reported three of the four classes caught.

**The failure mode is that this looks like a finding.** The natural reading of "three of four" is
that the pattern has a hole in its UNC branch — a defect in a regex settled in T-013 and T-018,
raised against the wrong thing, and "fixed" by loosening a branch that was already correct. The
damage is silent in both directions: the specimen looks like what was typed, and the check looks
like it failed.

`CLAUDE.md` instructs a future author to do this — *"a validator is only proven when it has been
shown to **fail** on a case it is supposed to catch"* — and says nothing about the trap. **Two** of
the four classes are backslash-bearing, drive paths and UNC, which is two of the fixture's five
must-catch lines; so it is a frequent case rather than the common one. *(Corrected at `implement` on
2026-08-11 from "three of the four … the common case", which was an overcount asserted rather than
counted: home directories and IP addresses carry no backslash. The overstatement did not change
whether the warning is worth having — the class that actually failed in T-034 is one of the two.)*

**Requirements served**
R-16 (`docs/SCOPE.md`), whose whole content is proof-by-failure, and R-20's cross-platform concern —
this is the same class as the existing `newline="\n"` note, which is already in `CLAUDE.md` for the
same reason.

**Scope**
- In: one warning in `docs/PUBLISHING.md` §6, beside the two-run proof it applies to.
- Out: `CLAUDE.md`. This task was raised against §*The pre-publish check* **there**; T-047 has since
  moved that section to `docs/PUBLISHING.md` §6, and T-118's tier-1 rule now forecloses putting the
  warning back — it binds only once a session has started proving the check, so tier 1 carries the
  pointer it already has and never the thing.
- Out: the regex, its four classes and its three limits. Settled in T-013, T-018 and T-058; this task
  exists because they are correct and were nearly re-opened on false evidence.
- Out: `tests/fixtures/leak-check/samples.txt`, which is committed and crosses no shell.
- Out: any change to the check command itself — that was T-034.

**Inputs**
`docs/PUBLISHING.md` §6 and `CLAUDE.md` §*Verifying*,
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) §3 *Found while verifying*.

**Acceptance criteria**
- [ ] `docs/PUBLISHING.md` §6 names the failure — a specimen damaged in transit — and what to do
      instead
- [ ] It says how to detect it, since the damaged text is indistinguishable from the intended text
      by reading; a byte-level check on the stored line is what identified it in T-034
- [ ] It says why it matters: the result is a *false negative attributed to the pattern*, not an
      obvious error
- [ ] No fabricated specimen or matched line is quoted into this task's record or into
      `docs/PUBLISHING.md`
- [ ] The addition does not restate the two-run proof, which already has one home

**Open questions**
- None. The one this phase raised — the home named above had ceased to exist — was decided rather
  than referred, under the standing authorization; the argument and the rejected alternative are in
  the Log.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Recover from [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) §3 what was damaged and what identified it, so the warning can name a detection method instead of telling the reader to be careful. | The mechanism and the detection method, recorded in §3 *Decisions & assumptions*. |
| 2 | Reproduce both branches **outside this repository**, in a scratch directory: write the same fabricated line through a shell argument and through a direct file write, then compare the stored bytes against the intended ones. | A recorded result naming which route preserved the line and what the byte comparison reported — counts and a verdict, never the line. |
| 3 | Fix where in `docs/PUBLISHING.md` §6 the warning goes, and list the facts that section already carries, so the warning points at them rather than restating them. | The insertion point and the do-not-restate list, in §3. |
| 4 | Write the warning. | One paragraph in `docs/PUBLISHING.md` §6. |
| 5 | Run the two-run proof §6 describes, producing the specimen the way the new warning says to. | The two runs' outcomes as counts and class names, recorded in §3 — no matched lines. |
| 6 | Run the §6 leak check over the whole tree, **last**, after this record is written — §6's own instruction, and the trap T-013 and T-018 both fell into. | Exit status and output, recorded in §3. |

Step 2 is placed before the writing because it is the only step that can invalidate the rest: if the
shell route turns out to preserve the line on this machine, the warning has no subject and the task
should be closed as unreproducible rather than written anyway.

**Deliverable shape.** A paragraph in prose, beside the two-run proof — not a fenced recipe naming a
tool. Rejected: a copy-pasteable command that writes a specimen safely. It would be the more useful
thing if it were portable, and it is not — the safe route depends on what the author is holding, and
§6 already carries one command whose correctness is load-bearing. A second command would need its own
proof, and an unproven one beside a proven one is worse than prose. Also rejected: adding a fifth
line to `tests/fixtures/leak-check/samples.txt` to exercise the transport, which is out of scope and
would not fire anyway, since the fixture is committed and crosses no shell.

**Outputs**
- docs/PUBLISHING.md
- tasks/T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md

## 3. Implement

Worked in plan order. Step 2 did not merely confirm the premise; it **sharpened the prescription**,
and the warning as written says something the plan did not know.

**Decisions & assumptions**
- **The warning tells the reader to bypass the command line, not to quote harder** — 2026-08-11.
  This is the step-2 yield. T-034 recorded that "a quoted heredoc did not help" without saying why,
  which leaves the natural next move — quote it more carefully — looking untried. It is not
  untried; it cannot work. The loss happens **upstream of the shell**, so every device the shell
  offers operates on text that is already short. Stating the reason is what stops the advice being
  re-litigated by the next person who assumes better quoting would have done it.
- **The detection method is "make the specimen prove itself", with the byte comparison behind it** —
  2026-08-11. T-034's `od -c` is what identified the damage, and it is kept; but it requires knowing
  the intended byte count, which the reader of a fresh specimen may not. Matching each class against
  the specimen file *before* the specimen is used as evidence needs no such knowledge and fails
  loudly. Rejected: leading with the byte count, which is the more precise instrument and the less
  usable one.
- **No example of a damaged or intended line anywhere** — 2026-08-11. Forced by §6's own rule that
  the check reads this file, and by criterion 4. The two paragraphs describe the shape and point at
  the fixture; nothing is quoted.
- **Placed after the two-run-proof paragraph, before *Three limits*** — 2026-08-11. That paragraph
  is what sends a reader to produce a specimen, so the warning meets them at the moment it applies.
  Rejected: the top of §6, which would greet every reader of the check with a caveat about a task
  most of them are not doing.
- **The five facts §6 already carries were checked and pointed at, not restated** — 2026-08-11: the
  two-run proof and its expected outputs, the fixture's composition, *run it last* and the
  quote-a-matched-line trap (T-013, T-018 — a **different** failure and deliberately not conflated
  with this one), the no-example rule, and *judge a run by the file count*.

**Found while verifying — one claim in this task's own `specify` was an overcount**

*Why this one* asserted that three of the four classes are backslash-bearing. Counted against the
fixture, it is two: drive paths and UNC carry backslashes; home directories and IP addresses do not.
Corrected in place with the correction annotated, per METHOD rule 5, since it is a present-tense
claim about the classes. It does not weaken the task — the UNC class is one of the two, and it is the
class that actually failed in T-034 — but "the common case" was doing rhetorical work the numbers do
not support, and this task exists because an unchecked number was read as a finding.

**Checked and found sound, so changed nothing:** §6's claim that the fixture holds nine fabricated
lines, five caught and four safe. A first count made it ten safe forms and looked like a second stale
claim; the count was wrong, not the document — it took the fixture's six comment lines for specimens.
Recorded because a near-miss that produces no edit leaves no other trace.

**Outputs produced**
- `docs/PUBLISHING.md` — §6, two paragraphs after the two-run-proof paragraph

**Verification**

*Step 2 — both branches, reproduced in a scratch directory outside the repository.* One fabricated
UNC-class line, 28 characters as intended, written four ways and then measured. No specimen text
crossed into this record or into the tree.

```
                      stored bytes    UNC branch matches
direct file write         29                 1
echo "..."                28                 0
printf '%s\n' "..."       28                 0
quoted heredoc <<'EOF'    28                 0
```

`od -c` on the first sixteen bytes shows the direct write beginning with two backslashes and the
heredoc with one. **The heredoc result is the load-bearing one**: a quoted heredoc is literal by
definition, so bash received only one backslash — the byte was already gone before bash parsed
anything. A second probe, assembling the literal inside a script file rather than in the command
string, lost it identically. The site is the transport into the shell, not the shell.

*Unplanned, and the cleanest evidence in the task.* While counting backslash-bearing fixture lines,
the count command itself was damaged in exactly this way and died with `grep: Trailing backslash` —
a two-backslash argument arrived as one. That failure was loud. The one this warning is about is the
same fault landing somewhere it produces a plausible number instead of an error, which is the whole
argument for the warning, obtained by accident rather than by construction.

*Step 5 — the two-run proof, unchanged and re-run.* Run with the pattern supplied from a file written
directly rather than typed into the command, which is the new warning's own advice applied to itself.

```
RUN 1  with the exclusion      212 files covered   -> nothing
RUN 2  without the exclusion   213 files covered   -> 5 hits, all in tests/fixtures/leak-check/
```

The two counts differ by exactly one, the fixture. Reported as counts because "prints nothing" is
also what the broken command did while reading none of them.

*And the pattern itself was damaged in transit — measured, not inferred.* The §6 regex holds ten
backslashes. Written directly it arrives with ten; sent through the command string it arrives with
**six**, because every doubled backslash collapses to one while single ones survive. **All four
losses are semantically harmless here**, since each falls inside a bracket expression, where POSIX
treats a backslash as literal and `[\\]` and `[\]` are the same class. So the damaged pattern returns
the correct five hits and is indistinguishable from the intact one by its output. That is the
clearest statement of the risk available: the transport corrupted the check's own regex in four
places during this task, changed no result, and would never have been noticed by running it.

*Step 6 — the §6 leak check over the whole tree, run last, after this record was written.* Result
below the review table.

`./plugin/bin/taskmd check` and `index` — output recorded at review.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| §6 names the failure and what to do instead | met | First paragraph. It names the failure as a line arriving one backslash short, and the instruction is *write it with something that never puts it on a command line* — a route, not a caution. It also forecloses the wrong fix explicitly, which the criterion did not ask for and the phase found necessary: T-034 left "a quoted heredoc did not help" unexplained, so the obvious next move looked untried rather than impossible. |
| It says how to detect it | met | Second paragraph, in the order the phase decided: match every class against the specimen file before the specimen judges anything, with the byte comparison behind it and T-034 cited. The criterion named only the byte check; it is kept, and led with the test that does not require knowing the intended byte count. |
| It says why it matters — a false negative attributed to the pattern | met | Second paragraph, final sentence, in those words, and it carries the consequence rather than stopping at the label: a run catching every class but one reads as a hole in the branch that stayed quiet, and invites loosening a branch that was correct. |
| No fabricated specimen or matched line quoted, here or in §6 | met | Verified mechanically, not by reading — the §6 check over the whole tree, run last and after this record was complete, covers both files. Output below. The two paragraphs describe shapes and point at the fixture; the tables in §3 carry byte counts and match counts only. |
| Does not restate the two-run proof | met | The proof stays in the paragraph above the addition and is referred to by position, not repeated. Five overlapping facts were listed at `implement` and each pointed at instead of copied; *run it last* and the quote-a-matched-line trap were the live risk, being adjacent and about the same command, and are deliberately kept distinct — they concern writing **about** the check, this concerns writing an input **to** it. |

**Not carried as a criterion, and stated rather than ticked:** the warning is scoped to this check. A
future author proving some *other* validator by fabricated specimen does not meet it here. No task
was raised, for two reasons that could both be wrong: the general rule's home is not this repository
(it is agent-level and cross-project), and the alternative homes are foreclosed or speculative —
`CLAUDE.md` by T-118's tier-1 rule, a new verifying document by there being one site today. Raised to
the maintainer at close rather than resolved, because "leave a known gap unwritten" is the owner's
call and not the reviewer's.

**Answered by the maintainer, 2026-08-11: leave the gap as it is.** No general home, no task. Written
here after close because this is where the question was asked, and a question answered somewhere else
is a question the next reader finds still open. **The premise it rests on is that the leak check is
the only place in this project needing a backslash-bearing specimen**, which is true today and is not
guaranteed to stay true — a second such validator is the event that reopens this, and nothing will
announce it, because a closed task is not read by any sweep. Stated as the expiry condition rather
than left implicit, since the decision is sound only while the premise holds.

**Step 6 — the §6 check over the whole tree, run last.**

```
files covered: 212        output: nothing
```

Run twice, once with the pattern typed into the command and once supplied from a directly-written
file; both silent, so the four collapsed backslashes change nothing here either. The two files this
task touched were then matched by name — `docs/PUBLISHING.md` 0, this record 0 — because a tree-wide
silence is what the broken command produced too, and criterion 4 is about these two files
specifically.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → in_progress → review → done | All five criteria met, none carried, one child task none. **The phase's real yield was not the paragraph but the reason behind it:** T-034 recorded that a quoted heredoc did not help and did not say why, and step 2 found the why — the byte is lost upstream of the shell, so no shell-level quoting can recover it. Without that, the advice reads as "quote it more carefully", which is the one thing that provably fails. Two things were measured rather than argued: the four write routes and their byte counts, and the check's own regex arriving with six of its ten backslashes, damaged in four places, all harmless, output identical. The second was unplanned and is the better evidence — it is this failure occurring during the task written to warn about it, invisible by running it. A third instance was pure luck: a counting command died with `grep: Trailing backslash`, which is the same fault landing where it is loud. One claim in this task's own `specify` was corrected as an overcount (three of four classes backslash-bearing; it is two), annotated rather than rewritten per METHOD rule 5. One near-miss produced no edit and is recorded anyway — §6's fixture composition looked stale and was not; the count was wrong. Two-run proof: 212 files clean, 213 files giving exactly the five fixture lines. |
| 2026-08-11 | → planned | Six steps, and the order is the whole of the design: step 2 reproduces the damage before step 4 writes about it, because a warning about a transport failure that this machine cannot actually produce is a warning about nothing. The experiment is deliberately sited **outside the repository** — the check in §6 reads untracked-but-not-ignored files by design since T-034, so fabricating a specimen inside the tree would plant the leak the task exists to warn about, and it would be found by the run in step 6 rather than by anyone thinking about it. Shape decided rather than deferred, with two alternatives rejected on the record: a copy-pasteable safe-write command, and a fifth fixture line. |
| 2026-08-11 | → specified | **The home this task named had stopped existing.** It was raised against `CLAUDE.md` §*The pre-publish check*; T-047 moved that section to `docs/PUBLISHING.md` §6 two days later, and nothing re-read this spec, so the target went stale in silence — the same class of decay the task itself is about. Decided rather than referred, under the standing authorization below, because the spec's own words settle it: *beside the two-run proof it applies to* resolves to exactly one place in the tree, and only the filename was wrong. **The rejected alternative is `CLAUDE.md` §*Verifying***, and it is not a strawman — that section still carries the instruction that creates the trap, still says nothing about it, and is quoted in *Why this one* for that reason. It loses to T-118's rule: a warning that binds only once a session has begun proving a validator is scoped to an announced activity, so tier 1 carries the pointer and never the thing. Two further consequences, both recorded rather than acted on: the residue that a future author proving some *other* validator by fabricated specimen will not meet the warning where it now sits, and the stale *two limits* in this spec's own Out list, which T-058 made three. The first is a real gap and is the one thing here worth a task if the owner disagrees with leaving it; the second was corrected in place as a present-tense fact. **Authorization, recorded here rather than in the handoff that carried it (METHOD §3.1):** the maintainer gave a standing instruction on 2026-08-10, re-confirmed since, to work each open `M2` task through its full lifecycle — specify, plan, implement, review, fix, commit and push — one task at a time, stopping before the next task when the remaining work will not fit the context. It covers the whole lifecycle of this task and nothing outside the `M2` set. |
| 2026-08-06 | → proposed | Raised from T-034's `implement`, which hit it while producing the specimen its criterion 2 demanded. Raised rather than fixed in place (METHOD §5) even though it is one paragraph: T-034's scope explicitly excludes the regex and the fixture, and this warning is about neither the command nor the pattern but about how the proof is produced. Medium value — it does not affect what the check catches, only whether the next person proving it can trust the answer. |
