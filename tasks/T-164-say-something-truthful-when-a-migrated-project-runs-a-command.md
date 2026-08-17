---
id: T-164
title: Say something truthful when a migrated project runs one of the four commands
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-163, T-108]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-17
updated: 2026-08-17
deliverables: [plugin/skills/taskmd/taskmd/schema.py, tests/fixtures/migrated-away/.taskmd/config.md, tests/test_cli.py]
---

# T-164 — Say something truthful when a migrated project runs one of the four commands

## 1. Specify

**Outcome**
A project whose tasks now live in GitHub Issues gets an accurate answer when it runs `context`,
`index`, `check` or `list`, instead of being told to create a folder it deliberately does not have.

**Why this one**
Found on 2026-08-17 while measuring for
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md), and recorded rather than fixed
there — it is outside that task's boundary and a silent fix would have made its record false. All
four commands exit 2 with:

```
CONFIG ERROR  <shipped default>: tasks_dir is 'tasks', but the project root has no such folder.
This project has no .taskmd/config.md, so taskmd is using its shipped default; create the folder,
or write a config naming a different one.
```

That is correct advice for a misconfigured project and wrong for a migrated one, where the absence of
the folder is the intended state. The message names the two repairs that do not apply and none of the
one that does.

**The shape of the fix is not obvious, which is why this is `specify` and not a one-line edit.**
taskmd has no way to know a project moved: there is nothing left behind to read, which is exactly what
[T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)'s listing says. So the candidates
differ in what they ask a project to keep — a config naming a non-local backend, a marker file, or
nothing at all and a wider message. Each buys accuracy with a different cost, and one of them is
*leave it alone*: a message that lists a third possibility no reader can act on is worse than one that
is merely incomplete.

**Scope**
- In: what the four commands say when `tasks_dir` is absent.
- Out: making any command work against GitHub Issues. The commands are local-Markdown only, and that
  is the fact [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) documents rather
  than a defect to repair.
- Out: a fifth command. Non-goal 11.

**Inputs**
- [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 — the measured output
- [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  — *What taskmd still gives you here*

**Acceptance criteria**
- [ ] The four commands **still refuse, still exit 2**. This task changes advice, not applicability —
      there is no folder, and nothing here makes one appear
- [ ] A migrated project is offered the possibility that applies to it, and the message **names what
      taskmd read to know it was possible** rather than asserting it
- [ ] A genuinely misconfigured local project — a typo, a folder that should exist — gets its
      previous message **unchanged**. Trading one misleading sentence for another is the way this
      fix fails
- [ ] Shown **failing first** on the migrated case, per `CLAUDE.md` *Verifying*
- [ ] A committed fixture carries the case, so the behaviour is protected rather than remembered
- [ ] The `CONFIG ERROR` label and exit 2 are untouched — see the decision at `plan`

**Open questions**
- **Does a migrated project keep anything taskmd can read? Yes — `id_width: none`. Answered
  2026-08-17**, under the lifecycle authorisation, and answered by reading rather than by choosing:
  the shipped config already glosses that value as *`none` if a backend allocates them*, and
  [`../plugin/skills/taskmd/docs/bindings/github-issues.md`](../plugin/skills/taskmd/docs/bindings/github-issues.md)
  **requires** a project on that backend to set it. So the marker exists, it is already mandatory,
  and this task imposes nothing new on an adopter to earn the sentence.

  *Rejected: a marker file the migration leaves behind.* It invents an artefact whose only purpose is
  to be found, and a project that deletes it silently loses the message.
  *Rejected: widen the message for everyone, with no test.* It would tell every misconfigured local
  project that its tasks might live on a backend, which is the same failure pointed the other way.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Measure what a migrated project **with its own config** sees. [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) measured the no-config case; a migrated project has a config, so the message it actually meets was never observed | The real output, recorded |
| 2 | Establish that `id_width` is normalised before the folder check runs, or the marker cannot be read there | The call order, named |
| 3 | Add the third possibility to the hint, for the missing-folder case only | The change in `schema.py` |
| 4 | Commit a fixture for the migrated case, and a test asserting the neighbour is unchanged | `tests/fixtures/migrated-away/`, two tests |
| 5 | Revert the change and run the new tests, so the failure is on record before the pass | A recorded failure |

**Decisions taken at `plan`**

- **The `CONFIG ERROR` label and exit 2 stay** — 2026-08-17. Both were arguable: the config of a
  migrated project is *coherent*, so calling it an error is itself a small lie. They stay because the
  label is one of a documented set the suite enumerates, R-17 pins config problems to exit 2, and the
  command genuinely cannot do what was asked. *Rejected: a distinct label and exit code for this
  case* — it changes a documented contract to improve a sentence, and would break a project scripting
  on exit 2. What was wrong was never the label; it was the advice.
- **The sentence is appended, not substituted** — 2026-08-17. `id_width: none` is legal on a local
  project, which the local binding says outright. So the message gains a possibility and keeps both
  existing remedies; it states, it does not diagnose. *Rejected: replacing the remedies when the
  marker is present*, which would tell a local project that set `none` there is nothing to fix.

**Outputs this task will produce**

- plugin/skills/taskmd/taskmd/schema.py
- tests/fixtures/migrated-away/.taskmd/config.md
- tests/test_cli.py

## 3. Implement

**Step 1 — the message a migrated project actually meets, measured 2026-08-17.** Fixture: the shipped
config with the GitHub binding's identity keys (`id_prefix: '#'`, `id_width: none`), no task folder.

```
CONFIG ERROR  .taskmd/config.md: tasks_dir is 'tasks', but the project root has no such folder.
Create it, or correct tasks_dir.
exit=2
```

**Worse than the no-config case [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md)
measured**, not better. That one at least explained itself — *taskmd is using its shipped default*.
This one is two bare imperatives, both wrong, addressed to a project whose config taskmd had just
read and which contained the marker saying so.

**Step 2 — the marker is readable where it is needed.** `_require` normalises `id_width` at
`schema.py:603`; `_check_tasks_dir` runs at `:611`, deliberately last. So `fields["id_width"]` is
already `None` rather than the raw string by the time the folder check fails.

**Steps 3–4 — the change and its fixture.** One appended sentence, guarded on the missing-folder
branch and on the marker. Two tests, and the second is the one that matters: it asserts
`broken-tasks-dir` — a real typo, the same shape — gains nothing.

**Step 5 — failing first.** The change stashed, the new tests run:

```
E   AssertionError: "id_width is 'none'" not found in "CONFIG ERROR  .taskmd/config.md: tasks_dir
    is 'tasks', but the project root has no such folder. Create it, or correct tasks_dir.\n"
1 failed, 1 passed
```

The neighbour test passing in that same run is not incidental — it shows the second assertion was
already true before the fix, so it can only ever fail if the fix over-reaches.

**A first attempt at this proof was vacuous and is recorded rather than quietly repeated.**
`git stash push -- <file> --quiet` put `--quiet` after `--`, so git read it as a pathspec, refused,
and **stashed nothing** — the tests then ran against the fixed tree and reported `2 passed`. That
output is indistinguishable from a real fail-first run except that it says *passed* where it should
say *failed*, and a run producing the expected shape is exactly the one nobody re-reads. The redone
attempt asserts the file is reverted before running anything.

After: `269 passed, 3 skipped` — two more than before.

**Decisions & assumptions**
- Both recorded at `plan` above and unchanged by the work: the label and exit code stay, and the
  sentence is appended rather than substituted.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/schema.py`
- `tests/fixtures/migrated-away/.taskmd/config.md`
- `tests/test_cli.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The four commands still refuse, still exit 2 | met | `all_three_commands_refuse` asserts exit 2 and the `CONFIG ERROR` label on the new fixture; `list` measured by hand alongside |
| The migrated project is offered the possibility that applies, naming what taskmd read | met | The message quotes `id_width is 'none'` — the reader can check the claim against their own config |
| A genuine misconfiguration is unchanged | met | `test_the_genuine_missing_folder_gains_nothing`, and it passed *before* the fix as well, which is what makes it a guard rather than a restatement |
| Shown failing first | met | §3 step 5, with the failure text. The first attempt at that proof was itself vacuous and is recorded |
| A committed fixture carries the case | met | `tests/fixtures/migrated-away/`, whose README-in-place says what distinguishes it from `broken-tasks-dir` |
| Label and exit code untouched | met | One appended sentence; no new exception type, no new exit path |

**The fail-first proof failed silently on its first attempt, and that is the finding worth keeping.**
A mis-placed `--quiet` made `git stash push` a no-op, so the "before" run was actually an "after" run
and printed `2 passed`. Everything about it looked like a completed check except the word. A
fail-first step that cannot show its own revert took place proves nothing, so the second attempt
asserts the file is reverted before it runs the tests.

**Child fix tasks raised**
- none.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-17 | → done | Full lifecycle in one request. **The maintainer authorised `specify` → `plan` → `implement` → `review` on this task and [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) and nothing else** — no other task, and nothing either raises. Recorded here rather than only in the chat, because an authorisation kept anywhere else is one a later session can miss (METHOD §3.1). **The open question answered itself by measurement**: a migrated project keeps `id_width: none`, the GitHub binding already requires it, and the shipped config already glosses it as *a backend allocates them* — so the marker was there all along and nothing new is imposed. Step 1 also found the case was **worse than [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) had measured**: with a config present the message drops the explanation and leaves two bare imperatives, both wrong. The label and exit code were left alone on purpose — what was wrong was the advice, and changing a documented contract to improve a sentence would break projects scripting on exit 2. **The fail-first proof was vacuous on its first attempt** and is recorded rather than repeated quietly: a misplaced `--quiet` made `git stash push` a no-op, so the "before" run was an "after" run and printed `2 passed` — the expected shape, which is the run nobody re-reads. |
| 2026-08-17 | → proposed | Raised from [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) §3 step 1, where the four commands were run against a project with no task folder to establish what stops applying after a migration. The measurement was the deliverable; **the misleading advice in the error was a by-product**, and it is recorded there and raised here rather than fixed in place. `s` because the message is one string, and `specify` rather than `fix`-and-done because the honest message depends on whether a migrated project keeps anything taskmd can read — which nothing currently requires it to. **Not covered by the lifecycle authorisation of 2026-08-17**, which named T-108 and T-163 and explicitly excluded whatever they raise. |
