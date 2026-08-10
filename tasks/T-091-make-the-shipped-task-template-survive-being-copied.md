---
id: T-091
title: Make the shipped task template survive being copied into another project
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-032, T-051, T-060, T-076, T-097, T-112, T-114]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-10
deliverables: [tasks/_task-template.md, tasks/_audit-umbrella-template.md, plugin/skills/taskmd/adopt.md, tests/test_cli.py]
---

# T-091 — Make the shipped task template survive being copied into another project

## 1. Specify

**Outcome**
An adopting project can take taskmd's task template and get a task file whose links resolve and
whose instructions name commands that exist there. Today it gets two broken links and a command
path that only works inside this repository.

**Why this one**
Found on 2026-08-09 while onboarding three projects onto taskmd. Copying
`tasks/_task-template.md` into a project and running `check` produced, immediately:

```
BROKEN LINK   tasks/_task-template.md -> ../plugin/skills/taskmd/docs/METHOD.md
BROKEN LINK   tasks/_task-template.md -> ../plugin/skills/taskmd/taskmd/defaults/config.md

2 problem(s) over 7 task(s)
```

Three things in the template's comment block are repository-local, not adopter-local:

1. the link to `../plugin/skills/taskmd/docs/METHOD.md` — in an adopter the method arrives with the
   installed plugin and is at no such path;
2. the link to `../plugin/skills/taskmd/taskmd/defaults/config.md` — an adopter's schema is its own
   `.taskmd/config.md`, and pointing at taskmd's default is pointing at the wrong file even when the
   path happens to resolve;
3. `./plugin/bin/taskmd index` — the by-path invocation this repository needs because of T-054's
   truncated shell snapshot. An adopter types `taskmd`.

**The workaround already exists and is the wrong shape.** The three onboarded projects were given a
hand-edited template with an adopter-appropriate comment block. That is three copies of a file this
repository also has, diverging from the day they were written — precisely the duplication the design
rule exists to prevent.

**Why this was not caught.** [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) pointed
the templates at paths that exist, and [T-076](T-076-decide-what-a-template-s-links-resolve-against.md)
decided links resolve against the template's own location so they survive *the copy that makes a
task*. Both are about the template inside this repository. Neither asked what happens when the
template crosses a project boundary, and nothing tests it — the first adopting project brought its
own templates and never took ours.

**Requirements served**
R-10 and R-11 — a clone must work unedited, and what a project configures is its own. R-20, the
out-of-the-box constraint, which this fails for the one file an adopter is most likely to copy first.

**Scope**
- In: what the template's comment block may reference, given it will be read in a project that is
  not this one.
- In: whether the template ships from `plugin/skills/taskmd/` — where an adopter can find it — rather
  than only existing as this repository's own `tasks/_task-template.md`.
- In: the audit-umbrella template, which has the same shape and the same exposure
  ([T-032](T-032-repair-the-audit-template-and-validate-templates.md)).
- Out: what an adopter's own template says once they have edited it. Theirs is theirs.
- Out: [T-032](T-032-repair-the-audit-template-and-validate-templates.md)'s other three defects and
  its mechanical template validation, which is the thing that would have caught this and is already
  specified there.

**Inputs**
- `tasks/_task-template.md`, the comment block.
- [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) for what links resolve against,
  and [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) for why they were last touched.
- The adopter template written by hand during the 2026-08-09 onboarding, as evidence of what an
  adopter actually needs it to say.

**Acceptance criteria**
- [ ] The template, copied unchanged into a project that is not this one, produces no `BROKEN LINK`
      — shown by copying it into a fixture and running `check`, not by reading the paths
- [ ] The command the template names is the one an adopter types, and this repository's by-path
      invocation is not what ships
- [ ] There is one template, not one per project — falsified by any adopting project needing a
      hand-edited copy to validate
- [ ] The same is true of the audit-umbrella template, or T-032 is explicitly the place it is fixed

**Authorization**
The maintainer asked on 2026-08-10 for every open `v0.2` task to be run through its whole lifecycle —
specify, plan, implement, review, commit and push — one task at a time. It covers this task end to
end and nothing outside the `v0.2` set.

**Open questions** — both answered here on 2026-08-10 under the standing authorization to decide an
owner-question rather than block on it. Each is cheap to reverse: one is a comment block, the other
is a file that does not exist.

- **Whether a template may contain a link at all.** Every path it names is either this repository's
  or the adopter's, and it cannot know which it is in. Naming documents without linking them makes
  the template portable at the cost of the convenience T-060 added deliberately. The maintainer's,
  because it trades an adopter's first experience against this repository's own.

  **Answered: no — a template names documents and does not link them.** The rule already exists in
  this project, written for exactly this reason, in the shipped schema's *Vocabularies* section:
  *"Named rather than linked, like every other pointer in this file: it is copied into your project
  as `.taskmd/config.md`, and a relative link would resolve from there and not from here."* A
  template is the same class of file as that one — the tool's copy of it is not where it gets read —
  so the same rule applies with nothing new to decide. What T-060 added is not lost so much as
  relocated: the comment block is deleted by whoever fills the template in, so its links were read
  once per task and never again, and the reader is an agent that has `SKILL.md` and the binding open
  already. *Rejected:* keeping the links and leaving the template repository-local, which preserves
  one click and keeps three hand-edited adopter copies diverging — the defect this task exists to
  remove.

- **Whether a second template ships from `plugin/skills/taskmd/`.** In scope above, and it has to be
  decided before the criteria can be judged.

  **Answered: no — `tasks/_task-template.md` stays the one template, made portable.** A template
  under `plugin/` would sit outside `tasks_dir`, where `check` neither link-checks it nor reads its
  front-matter; T-032 exists because a template nothing validates rots in silence, and shipping a
  second one would re-create that blindness in the copy an adopter actually receives. Keeping both
  is two copies of one file, which the design rule forbids outright. What an adopter is missing is
  not a file but a sentence — `adopt.md` never mentions templates at all — so the gap is closed
  there. *Rejected:* shipping a template from the skill folder (unvalidated, and duplicated if this
  repository keeps its own); generating one from the config, which two projects suggested and which
  non-goal 11 refuses, holding the CLI at four commands.

## 2. Plan

The order matters in one place only: step 4 is the proof, and it cannot pass until steps 1 and 2
have landed. Everything else is independent.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Rewrite `tasks/_task-template.md`'s comment block to name its documents instead of linking them, and to name the command an adopter types | the comment block in `tasks/_task-template.md` |
| 2 | The same for the audit umbrella, which carries two links and the same by-path command | the comment block in `tasks/_audit-umbrella-template.md` |
| 3 | Replace the task template's `work_package` menu — `WP<n> \| final \| none` names groupings no project has — with the placeholder the audit template already uses | the `work_package` line in `tasks/_task-template.md` |
| 4 | Move `test_a_task_built_from_each_shipped_template_passes` out of this repository and into a temp project with no `plugin/`, which is the case its own docstring says it cannot cover | `tests/test_cli.py` |
| 5 | Give `adopt.md` the step it has never had: where a project's template lives, that writing one is optional, and that `check` holds it to the same rules as a task | `plugin/skills/taskmd/adopt.md` |
| 6 | Run the suite, `check`, `index` and the leak check | the evidence recorded in §3 |

## 3. Implement

**Decisions & assumptions**
- *A template names its documents and does not link them* — 2026-08-10. The reasoning and the
  rejected alternative are in §1, where the question was asked.
- *No template ships from `plugin/skills/taskmd/`; `adopt.md` gains a step instead* — 2026-08-10,
  likewise recorded in §1.
- *`adopt.md` points an adopter at this repository's template as a worked example* — 2026-08-10.
  That is an instance of the question
  [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md)'s neighbour
  [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md) is
  open on: a published document referring to something no install receives. It is named rather than
  linked and the surrounding text works without it, so if T-097 rules against the form, deleting one
  clause is the whole of the change.

**Verification** — the fix reproduced the reported failure first, then removed it. Restoring the old
comment block and running the moved test produced the adopter's report, plus two lines their report
could not contain because they only copied the template and never made a task from it:

```
AssertionError: 1 != 0 : _task-template.md produced:
BROKEN LINK   tasks/T-999-trial.md -> ../plugin/skills/taskmd/docs/METHOD.md
BROKEN LINK   tasks/T-999-trial.md -> ../plugin/skills/taskmd/taskmd/defaults/config.md
BROKEN LINK   tasks/_task-template.md -> ../plugin/skills/taskmd/docs/METHOD.md
BROKEN LINK   tasks/_task-template.md -> ../plugin/skills/taskmd/taskmd/defaults/config.md
```

With the fix in place the same test passes for both templates, and this repository is unaffected:

```
python tests/test_cli.py   -> Ran 84 tests   OK
python tests/test_list.py  -> Ran 29 tests   OK
python tests/test_schema.py-> Ran 45 tests   OK
taskmd check -> OK - 113 task(s) ... 2 template(s), 10 template field value(s)
```

**`tests/test_runtime.py` fails four of its 27, and none of them is this change's** — the identical
four fail at `e0005ca` with the working tree stashed, which is how that was established rather than
assumed. Three are this machine: `shutil.which("bash")` resolves to **WSL** rather than Git Bash in
this session, and WSL cannot execute a script named by a Windows path, so the launcher exits 127.
The fourth is not environmental and is written up on
[T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md), which it turns
out to be evidence for. Raised for the first:
[T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md).

**Outputs produced**
- `tasks/_task-template.md` — comment block, and the `work_package` menu
- `tasks/_audit-umbrella-template.md` — comment block
- `plugin/skills/taskmd/adopt.md` — new step 5
- `tests/test_cli.py` — `test_a_task_built_from_each_shipped_template_passes`, moved out of this
  repository into a temp project

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Copied unchanged into a project that is not this one, produces no `BROKEN LINK` — shown by copying it into a fixture and running `check` | met | Stronger than asked: a temp project, not a fixture in this tree, so nothing of this repository is reachable from it. Both templates, and the task made from each. Shown failing first. |
| The command the template names is the one an adopter types, and the by-path invocation is not what ships | met | Both templates now name `taskmd index`. `test_every_usage_line_names_the_command_the_skill_names` already pinned the same property for the CLI's own output. |
| One template, not one per project — falsified by any adopting project needing a hand-edited copy to validate | met, and only testable by an adopter | Nothing here can falsify it; what can be said is that the two things that forced hand-editing — the links and the by-path command — are gone, and the `work_package` menu that named groupings no project has went with them. The next project to adopt is the test. |
| The same is true of the audit-umbrella template, or T-032 is explicitly the place it is fixed | met | Fixed here, not deferred. The moved test loops over every `_`-prefixed file in `tasks/`, so a third template would be covered without the test being edited. |

**Child fix tasks raised**
- [T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md) — not a defect in this outcome,
  but found by verifying it and not fixable where it was found (METHOD §3.3).

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Whole lifecycle in one session under the authorization in §1. Both open questions decided rather than escalated, with the rejections recorded beside them. The second defect the 2026-08-09 note below raised — the `work_package` menu — is fixed here rather than left, because a menu naming groupings no project has is the same boundary crossing as the links and it made no sense to fix half of one file. Their better idea, generating the template from the config, is refused by non-goal 11 rather than by preference. Verifying it turned up two things in the same run that are not this task's: T-114, raised, and a correction written onto T-112 that raises what that task is worth. |
| 2026-08-09 | (no status change) | Independent confirmation from the deck-building sibling, and a second defect in the same file: the shipped template's `work_package` placeholder offers `WP<n>`, `final` or `none` as alternatives, which cannot be right for a project that enumerates its own values in `.taskmd/config.md` — as two of the projects onboarded on 2026-08-09 now do. Their framing is worth keeping: a template *generated from the config* could not drift, whereas a template that restates the schema always eventually does. That is this repository's own design rule pointed at its own template, and it may be a better answer than repairing the placeholders by hand. |
| 2026-08-09 | → proposed | Raised from real use rather than from reading: onboarding three sibling projects onto taskmd, the very first `check` after copying the template reported two broken links, and the command it names is this repository's by-path invocation rather than the one an adopter types. Worked around at the time with a hand-edited adopter template, which is three diverging copies and is why this is `high` despite being `s` — the workaround is worse than the defect. T-060 and T-076 both touched these links and both were reasoning about the template inside this repository; the boundary crossing was never the question, and T-032's mechanical template validation is the thing that would have caught it. |
