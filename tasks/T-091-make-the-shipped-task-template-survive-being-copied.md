---
id: T-091
title: Make the shipped task template survive being copied into another project
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-032, T-051, T-060, T-076]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-09
deliverables: []
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

**Open questions**
- **Whether a template may contain a link at all.** Every path it names is either this repository's
  or the adopter's, and it cannot know which it is in. Naming documents without linking them makes
  the template portable at the cost of the convenience T-060 added deliberately. The maintainer's,
  because it trades an adopter's first experience against this repository's own.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <path>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- <T-NNN or "none">

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | (no status change) | Independent confirmation from the deck-building sibling, and a second defect in the same file: the shipped template's `work_package` placeholder offers `WP<n>`, `final` or `none` as alternatives, which cannot be right for a project that enumerates its own values in `.taskmd/config.md` — as two of the projects onboarded on 2026-08-09 now do. Their framing is worth keeping: a template *generated from the config* could not drift, whereas a template that restates the schema always eventually does. That is this repository's own design rule pointed at its own template, and it may be a better answer than repairing the placeholders by hand. |
| 2026-08-09 | → proposed | Raised from real use rather than from reading: onboarding three sibling projects onto taskmd, the very first `check` after copying the template reported two broken links, and the command it names is this repository's by-path invocation rather than the one an adopter types. Worked around at the time with a hand-edited adopter template, which is three diverging copies and is why this is `high` despite being `s` — the workaround is worse than the defect. T-060 and T-076 both touched these links and both were reasoning about the template inside this repository; the boundary crossing was never the question, and T-032's mechanical template validation is the thing that would have caught it. |
