---
id: T-258
title: Report a declared output a clone never receives as excluded, not missing
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-257, T-103, T-098, T-013]
work_package: M7
owner: the project owner
business_value: high
effort: s
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/taskmd/cli.py
  - plugin/skills/taskmd/docs/bindings/local-markdown.md
  - tests/test_cli.py
---

# T-258 - Report a declared output a clone never receives as excluded, not missing

## 1. Specify

**Outcome**
`check` draws the same distinction for a declared output that it already draws for a document: an
artefact that exists but that a clone would never receive is reported as **excluded**, in the `Scope`
lines, and does not take the exit code to 1. A path that is genuinely gone still fails, unchanged.

**Why this one**
**`check` already knows this distinction and applies it on one side only.** It prints
`Scope  84 document(s) not read: a clone would not receive them` - the document-side filter
[T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) put there - and
then reports a `deliverables:` path under the same condition as
`MISSING OUTPUT ... which does not exist`. Two paths, same fact about the reader, opposite verdicts.

**It is not hypothetical, and this project has now met it twice.**
[T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) was raised when the
asymmetry took CI red for a day: `control/LOCAL-CONTEXT.md` is gitignored on purpose by
[T-013](T-013-quarantine-local-only-information-behind-gitignore.md), so it exists here and in no
clone, and the working tree passed while every clone failed. The first time was the adopting
project's `R-5`, which became
[T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) - **the same file, the
same rule, a different gap in it.**

**This record is the second half of the owner's answer, and it is raised before the first half
lands.** The owner chose *unblock now, fix properly after* on 2026-08-23 and named the failure mode
of that choice in the option itself: once the gate is green, nothing is left arguing for the repair.
So T-257's plan raises this record as its step 1, ahead of the one-line edit that removes the pain.

**What the unblock cost, stated so this record can restore it.** Reading 1 removes
`control/LOCAL-CONTEXT.md` from T-250's `deliverables`, which means the project no longer records
that [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) produced that file
anywhere a command can see. The declaration is the fact; a Log row is a consolation. Closing this
task is what makes re-declaring it safe.

**Scope**
- In: how `check` decides that a declared path is excluded rather than missing, and what it prints
- In: the exit-code consequence - excluded does not fail, missing still does
- In: whether T-250's declaration is restored once this ships, since removing it was the unblock and
  not the answer
- Out: any new configuration key. The document side needed none, and a key is what
  [`.taskmd/config.md`](../.taskmd/config.md)'s *What this rule has already refused* declines twice
- Out: what `check` reports about a path that is genuinely gone. Right under any answer, and T-257
  scoped it out for the same reason

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` - the document-side filter and the `MISSING OUTPUT` check, so
  the two can be read side by side
- [T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) - the document
  side, with its alternatives already priced
- [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md) - the decision this
  implements, and the survey of the class

**Acceptance criteria**
- [ ] A tracked declared path that is deleted still fails `check`, and the run is shown failing on it.
      A rule that never fires and a rule that cannot are worth the same
- [ ] An untracked declared path is reported in `Scope` and does not move the exit code, shown on a
      case that could have fired
- [ ] Verified in a **fresh clone** and not in the working tree, which is the instrument that missed
      the original defect for a day
- [ ] T-250's declaration is restored, or the record says why it is not

**Open questions**
- **How exclusion is detected without a config key.** The document side has a mechanism already;
  whether it reaches a `deliverables:` path unchanged is a question for whoever plans this, and the
  answer decides whether this is small or not.

## 2. Plan

**The open question is answered, and by the wrong mechanism to the one §1 expected.** §1 pointed at the
document-side filter, `clone_would_receive`, which lists what a clone **would contain**. That cannot
work here: in a clone the declared file is simply **absent**, so it is missing from that set for the
same reason a deleted file is, and the two stay indistinguishable exactly where the check runs.

**`git check-ignore` answers instead, and it answers about a path that does not exist.** Measured in a
fresh clone on 2026-08-23, with `control/LOCAL-CONTEXT.md` not present:

```
git check-ignore -v control/LOCAL-CONTEXT.md
.gitignore:2:control/   control/LOCAL-CONTEXT.md          rc=0
git check-ignore -v docs/DOES-NOT-EXIST.md
                                                          rc=1
```

**Never receivable and genuinely gone are separable, in the clone, with no config key** — which is what
`§1` scoped out and what the two refusals in the config forbid. The rule that matched is named, so
the message can say *why* rather than assert it.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Add the ignore query beside `clone_would_receive`, batched over all declared paths in one call, returning `None` where there is no git so nothing changes for a project without one. | A helper in `plugin/skills/taskmd/taskmd/cli.py` |
| 2 | In the declared-output check, split the absent case: ignored → a `Scope` line naming the count, not a problem and not an exit code; not ignored → `MISSING OUTPUT`, unchanged. | The changed check |
| 3 | Show the **failing** half still fails: a genuinely deleted declared path exits 1. A rule that stopped firing would pass every other step here. | The failing run, in §3 |
| 4 | Show the **quiet** half on a case that could have fired: an ignored declared path is reported and the run exits 0, in a tree where the same path un-ignored exits 1. | Both runs, in §3 |
| 5 | Verify in a fresh clone, which is the instrument that missed the original defect for a day. | The clone's output, in §3 |
| 6 | Restore T-250's `control/LOCAL-CONTEXT.md` declaration, which was removed as T-257's unblock and is the fact this task exists to make safe again. | `tasks/T-250-...md` |
| 7 | Correct the binding paragraph T-257 wrote, which says in its own words that it is superseded when this ships. | `plugin/skills/taskmd/docs/bindings/local-markdown.md` |

**Step 7 is not optional and is easy to miss.** The paragraph names its successor, so leaving it would
make the shipped binding tell an adopter to do the thing this task just made unnecessary.

**Outputs this task will produce**

- `plugin/skills/taskmd/taskmd/cli.py`
- `plugin/skills/taskmd/docs/bindings/local-markdown.md`
- `tasks/T-250-give-the-context-registers-the-permitted-shape-for-history.md`
- `tests/test_cli.py`

## 3. Implement

**Decisions & assumptions**
- **`git check-ignore`, not `clone_would_receive`** — 2026-08-23, and §1 pointed the wrong way. That
  set lists what a clone *would contain*, so in a clone the untracked file is missing from it for the
  same reason a deleted file is, and the two stay indistinguishable exactly where the check runs.
  `check-ignore` matches the **path** rather than the filesystem, so it answers for a file that is not
  there — and names the rule that matched, so the report can say why.
- **No config key, which is what made this possible at all** — 2026-08-23. `.taskmd/config.md`
  refuses a key three times over, and this needed none: an ignore rule is git's, not the project's
  vocabulary.
- **The helper returns `{}` where there is no git, never `None`** — 2026-08-23. *Nothing is ignored*
  and *there is no git here* lead to the same behaviour for this check — judge every declared path on
  existence — so the distinction `clone_would_receive` draws would be a difference that changes
  nothing. Its docstring says so, because the neighbouring helper deliberately does the opposite.
- **`check-ignore` exit 1 is *nothing matched*, not an error** — 2026-08-23. Only a code outside
  `(0, 1)` means the query failed. Treating 1 as failure would silently disable the whole feature.

**Evidence — run in a clone, where the file is absent, which is the only place this matters**

**The case that was red.** T-250's declaration restored, in a fresh clone with the file not present:

```
file present in clone? no
check --root <clone>                                                    rc=0
Scope  1 declared output(s) not checked: an ignore rule keeps them out of every clone
```

**A genuinely deleted path still fails, in the same clone:**

```
MISSING OUTPUT T-250 declares 'docs/DELETED-BY-MISTAKE.md', which does not exist      rc=1
```

**And the quiet case was shown able to speak** — the decisive one. The **same** declared path, the
same absent file, with only the ignore rule commented out:

```
git check-ignore -q control/LOCAL-CONTEXT.md                            rc=1  (no longer ignored)
MISSING OUTPUT T-250 declares 'control/LOCAL-CONTEXT.md', which does not exist        rc=1
```

Without that run the first result is indistinguishable from a check that had simply stopped looking.

**The tests were shown to fail against the code they replace.** Reverting `cli.py` to `HEAD` and
running the four new cases: `1 failed, 3 passed`. The one that fails is
`test_an_ignored_declared_output_is_reported_and_does_not_fail` — the only one asserting new
behaviour. The other three pin behaviour the change must **not** weaken, so passing both ways is
what they are for.

Full suite: `358 passed, 8 subtests passed`. `check` on this tree: `rc=0`, with the restored
declaration in place.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `clone_would_never_receive`, and the declared-output check
  split into absent-and-ignored versus absent-and-gone
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — T-257's interim paragraph replaced by the
  settled rule; the *declare it anyway* instruction now matches what `check` does
- `tests/test_cli.py` — four cases, including the same-path-without-the-rule control
- `tasks/T-250-...md` — the declaration restored

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A tracked declared path that is deleted still fails `check`, and the run is shown failing on it | met | `MISSING OUTPUT ... docs/DELETED-BY-MISTAKE.md`, `rc=1`, in a clone. Pinned by `test_a_genuinely_deleted_declared_output_still_fails`. |
| An untracked declared path is reported in `Scope` and does not move the exit code, shown on a case that could have fired | met | Both halves. `rc=0` with the `Scope` line; then the **same path** with the ignore rule removed gives `MISSING OUTPUT`, `rc=1`. The control is the evidence, not the quiet run. |
| Verified in a **fresh clone** and not in the working tree | met | Every run above is `check --root <clone>` with the file absent. The working tree was never the instrument. |
| T-250's declaration is restored, or the record says why it is not | met | Restored. `control/LOCAL-CONTEXT.md` is back in that record's `deliverables`, and the Log row explaining its removal now reads as the history it is. |

**Adopter-visible?** yes — `check` reports a new `Scope` line and stops failing on a case it used to
fail on, and the shipped binding tells an adopter to declare a quarantined artefact rather than omit
it. That is a change to what an install does. `adopter_visible: yes` set at `specify`, unchanged.

**Child fix tasks raised**
- none.

**What this closes, beyond itself.** [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md)
took reading 1 as an unblock and recorded that reading 2 was the truer answer. Reading 2 has now
shipped, and the interim paragraph that said so has been replaced rather than left to be found.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | planned → done | All four criteria met, every run in a clone with the file absent. **The control is the finding**: the same declared path with only the ignore rule removed exits 1, which is what makes the quiet run mean something. The new tests were shown failing against the code they replace — 1 of 4, the one asserting new behaviour. T-250's declaration is restored, so the record of what that task produced is mechanical again rather than prose. |
| 2026-08-23 | proposed → planned | Seven steps. **The open question is answered in §2, and §1's suggested mechanism was wrong**: `clone_would_receive` cannot separate the two cases in a clone, because the file is absent there either way. `git check-ignore` can, and answers for a path that does not exist. **Carried under the owner's instruction of 2026-08-23**, given when asked which new records to close: T-258, on the ground that this is the half their own earlier answer flagged as the one that gets forgotten once the gate is green. |
| 2026-08-23 | → proposed | **Raised as step 1 of [T-257](T-257-decide-what-a-deliverable-a-clone-never-receives-asserts.md)'s plan, deliberately before that task's one-line unblock lands.** The owner's answer of 2026-08-23 was *unblock now, fix properly after*, and the option they chose names its own failure mode: a follow-up whose only constituency is a red gate loses it the moment the gate goes green. So the record exists first. |
