---
id: T-032
title: Repair the audit template, and validate templates at all
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-003, T-022, T-036]
work_package: M2
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tasks/_audit-umbrella-template.md, tests/fixtures/broken-template-field/tasks/_task-template.md]
adopter_visible: yes
---

# T-032 — Repair the audit template, and validate templates at all

## 1. Specify

**Outcome**
A task created from `tasks/_audit-umbrella-template.md` passes `check`, follows the
mandatory lifecycle, and carries the fields every other task carries — and a template that stops
being valid is noticed by something other than a person reading it.

**Why this one**
Raised as **F-6** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 1 and 3. Shown, not asserted — a task built from the template, with only the placeholders
filled in, run against `check`:

```
VOCABULARY    T-001.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
STORED DERIVED T-001 stores 'children:', which is computed from 'parent'; remove it

2 problem(s) over 1 task(s)
exit=1
```

Four defects, of which `check` can see the first two:

1. **`type: audit`** is not in the `type` vocabulary. There is no audit type — audit is a task
   *type* in the method's sense (METHOD §5) but the schema never gained the value, so the template
   names one the config does not have.

   > **Resolved 2026-08-09 by [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md),
   > which carried out Q1's answer below.** The shipped `type` row now contains `audit`, so the
   > template no longer names a value the config lacks. The finding text is left as written — it is
   > an audit's product and dating its resolution beside it is the reconcile, not editing it away.
   > T-088 was raised without knowing Q1 had settled this on 2026-08-06; its record now points here
   > rather than holding a second copy of the decision. **The other three defects are untouched**,
   > and so is the criterion that templates be validated mechanically, which is the half that stops
   > this class recurring.
2. **`children: []`** is a stored derived name — the precise thing `check`'s STORED DERIVED class
   exists to catch, and the thing `tasks/_task-template.md` warns against by name.
3. **No `related`, `business_value` or `effort`.** T-022's backfill updated the other template and
   left this one, so a task made from it sorts after everything estimated and shows no soft links.
4. **The body is `1. Specify / 2. Findings / 3. Resolution`** — not the four mandatory phases (R-3),
   and its fixed *Review dimensions* checklist predates
   [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 2, which requires a finding threshold
   stated per audit instead.

**Why nobody saw it.** `load_tasks` skips folders whose name begins with `_`, so `_templates/` was
never enumerated and never validated — correctly, since a template is not a task, but the
consequence is that both templates can rot silently. `check_links` walks the whole tree, so a broken
*link* in a template is caught; nothing checks its front-matter.

> **The mechanism above changed under this task on 2026-08-09, and the conclusion did not** —
> [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) moved both templates out of
> `_templates/` and into `tasks/` as `_`-prefixed files. There is no skipped folder any more:
> `load_tasks` now **reads** each template and discards it because `id: T-NNN` is neither a valid id
> nor a near miss. Still unvalidated, still silent — but by a rule about the file's *content* rather
> than about where it sits, which is a much shorter distance to travel for this task's second
> in-scope item below. Recorded rather than rewritten, because the paragraph is why F-6 went
> unnoticed for as long as it did, and that is a fact about the past.

**Why it is High.** This is the template for the audit task type, and audit is the one task type
whose whole product is traceability. [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md)
will teach an agent to create tasks from these templates, and
[T-006](T-006-package-document-and-publish.md) ships them.

**Requirements served**
R-3, R-5, R-16 (`docs/SCOPE.md`).

**Scope**
- In: `tasks/_audit-umbrella-template.md` — its front-matter and its body structure.
- In: a way for a template's front-matter to be checked, which is what stops this recurring.
- In: whether the `type` vocabulary gains an `audit` value, or the template uses an existing one.
  [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) itself used `analysis`, which
  is evidence that it works but not a decision that it is right.
- Out: `reference/templates/audit-umbrella-template.md`, which is prior art from another project and
  is not this repository's to correct (T-026's scope).
- Out: any new command. Non-goal 11 stands; if templates are to be validated it is by `check`, which
  already walks the tree.

**Inputs**
`tasks/_audit-umbrella-template.md`, `tasks/_task-template.md`,
`taskmd/defaults/config.md` §*Vocabularies*, `taskmd/schema.py` (`load_tasks`),
`docs/method/audit.md`, [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-6.

**Acceptance criteria**
- [ ] A task created from the template, with placeholders filled in and nothing else changed, passes
      `check` — demonstrated by running it, per `CLAUDE.md` *Verifying*
- [ ] The template's body carries the four mandatory phases, and the findings table lives inside
      that structure rather than replacing it
- [ ] It carries every front-matter field `task-template.md` carries, or states why one is absent
- [ ] **The failure is caught mechanically from now on** — shown by breaking a template on purpose
      and watching the check report it, per R-16. A fix that leaves templates unvalidated has fixed
      today's instance and not the class
- [ ] Whatever the audit-type decision is, it is recorded with the alternative that was rejected —
      the template and the vocabulary must not disagree again

**Open questions**
- None. **Q1 — does `type` gain `audit`? — answered by the maintainer on 2026-08-06: yes.**

  The answer given was that an audit task runs the same pipeline as any other task. That settles the
  doubt the question was raised on rather than sidestepping it: `type` and `phase` are **orthogonal**
  fields, and every value already in the vocabulary goes through all four phases. So "it has a full
  lifecycle" is an argument *for* the value, not the reason to withhold it — `type` records what kind
  of work a task is, and audit is a kind of work.

  The deciding argument is drift. METHOD §5's first line is *"An audit is a task type, not a
  phase"*; if the schema's `type` field has no such value, the method's word and the schema's field
  name different things, which is what this plugin exists to remove. T-026 running as `analysis` is
  evidence the field tolerates the substitution, not that the substitution is right — and it makes
  audits unfindable as a class, since `list` filters on the value that is stored.

  *Rejected: keep using `analysis`.* It costs nothing today and leaves the template naming a value
  the config does not have — which is this finding, unfixed.

**Deliberately not answered here — the audit *workflow*, which is a different subject**

The answer to Q1 arrived with a fuller account of how an audit should run: `specify` carries goals
and requirements, `plan` researches and produces the audit procedure for that particular audit,
`implement` performs it and records findings; plus a separate case — a user asking for a **task's
plan** to be audited.

Most of it is already written, and where it is not, **it does not belong in this task**:

- Scope-first, threshold-before-looking, findings-in-the-umbrella and close-only-when-children-resolve
  are [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) steps 1–5. The mandatory lifecycle is METHOD
  rule 2.
- **Genuinely new:** that the audit *procedure* is designed in `plan`, per audit. That is an addition
  to `audit.md`.
- Writing any of it into the template is the defect this task exists to fix. F-6 is a template that
  had rotted into a stale second copy of the method; repairing it by copying more method into it
  reproduces the fault at a larger size.

Split out as [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md), which also
carries the plan-audit case — where the answer given is argued **against**; see that task.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Rebuild a task from the template and run `check`, before changing anything | evidence in §3 |
| 2 | The mechanical half **first**, so the repair is proved by the check rather than by reading | `check_template_fields` in `cli.py` |
| 3 | Repair whatever it reports, plus the two defects it cannot see | `tasks/_audit-umbrella-template.md` |
| 4 | A fixture holding the class, and the class in the failure set | `tests/fixtures/broken-template-field/`, `tests/test_cli.py` |
| 5 | Copy each shipped template out and check the result — the half front-matter validation cannot ask | `tests/test_cli.py` |
| 6 | Reconcile the binding, which says a template is link-checked | `docs/bindings/local-markdown.md` |

Step 2 before step 3 is the point of the ordering: writing the check first means the repair is
verified by the mechanism that has to keep verifying it, rather than by the same reading that missed
the defects for two months.

## 3. Implement

**Reproduced first.** A task built from the audit template with only its placeholders filled:

```
STORED DERIVED T-001 stores 'children:', which is computed from 'parent'; remove it
2 problem(s) - 1 task(s), ...
exit=1
```

Defect 1 is gone, as §1 records — T-088 put `audit` in the vocabulary. Defects 2, 3 and 4 stood.

**Decisions & assumptions**
- **The check was written before the repair** — 2026-08-10. Both were in scope and either order
  would have closed the task; this one makes the repair's proof mechanical. It paid immediately:
  on its first run against this repository it reported **two** defects, and only one of them was
  known. The other was `tasks/_task-template.md` offering `analysis | deliverable | research | fix |
  admin` — five of the seven types, missing `decision` and `audit`. Nobody had noticed, and criterion
  5 is exactly *the template and the vocabulary must not disagree again*.
- **A placeholder is not a defect, and a menu is held to the whole vocabulary** — 2026-08-10. Angle
  brackets are a slot and are skipped. A `|`-separated value is a menu, and it must equal the
  vocabulary rather than merely be contained in it. Membership alone would have passed the drifted
  `type` line above, which is the case that motivated the rule: a menu falling behind is the form of
  rot that lasts longest, because every value it still offers is legal and nothing a reader could
  spot distinguishes it from a correct template. Rejected: skipping any value containing `|`, which
  is simpler and would have found nothing.
- **Missing fields and body structure are repaired, not made mechanical** — 2026-08-10, and stated
  because criterion 4 is about the class. `check` does not require `business_value` of a *task*, so
  requiring it of a template would invent a rule the tool does not otherwise hold anyone to; and the
  four phases are a body convention the method deliberately does not impose as a format. So two of
  the four defects are now class-proof and two are instance repairs. What closes the gap for the
  latter is step 5 — copying each shipped template out and checking the result — which is a weaker
  guarantee than a rule and is the honest one available.
- **The trial copy is made in this repository, not a temp folder** — 2026-08-10. A template's
  relative links resolve against the project it is copied into, so a fresh folder breaks them for
  want of a `plugin/` directory rather than because the template is wrong. That is
  [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md)'s subject and was left to it.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `check_template_fields`, wired into `cmd_check`.
- `tasks/_audit-umbrella-template.md` — rewritten: `children:` gone; `related`, `business_value` and
  `effort` added; body now the four mandatory phases, with the findings table inside `implement` and
  the closing rule inside `review`. The fixed *Review dimensions* checklist is replaced by a
  **what counts as a finding** slot, per `docs/method/audit.md` step 2.
- `tasks/_task-template.md` — the `type` menu, corrected to the vocabulary.
- `tests/fixtures/broken-template-field/`, `tests/fixtures/README.md`, `tests/test_cli.py`.
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — *create* now says a template's
  front-matter is checked, and what a placeholder is.

**Evidence**

The check, on this repository, before the repair — one known defect and one nobody had found:

```
TEMPLATE FIELD tasks/_audit-umbrella-template.md stores 'children:', which is computed from
'parent'; every task copied from it starts invalid
TEMPLATE FIELD tasks/_task-template.md offers 'admin | analysis | deliverable | fix | research'
for 'type'; the schema allows analysis, decision, deliverable, research, fix, admin, audit
```

A task built from the repaired audit template, in this repository, after regenerating the index —
criterion 1, run rather than asserted:

```
OK - 114 task(s), 570 field value(s), 355 reference(s), 22 dependency edge(s), 158 declared
output(s), 1 index file(s), 142 document(s), 1086 link(s), 2 template(s), 10 template field
value(s), 0 vocabulary row(s)
```

Shown failing on the class, per R-16 — `tests/fixtures/broken-template-field`, three forms:

```
TEMPLATE FIELD tasks/_task-template.md stores 'children:', ...
TEMPLATE FIELD tasks/_task-template.md offers 'critical | high | low' for 'business_value'; the
schema allows critical, high, medium, low
TEMPLATE FIELD tasks/_task-template.md sets 'type' to 'nonsense'; allowed: ...
```

Suite **181 passed** (179 before), `check` clean on 113 tasks.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A task created from the template, placeholders filled and nothing else changed, passes `check` — demonstrated by running it | met | Run in this repository, exit 0 on 114 tasks, output above. `test_a_task_built_from_each_shipped_template_passes` does it for **both** shipped templates on every run, so it is not a one-off demonstration. |
| The body carries the four mandatory phases, findings inside that structure rather than replacing it | met | `1. Specify / 2. Plan / 3. Implement / 4. Review`; the findings table is inside `implement`, where the findings are produced, and the closing rule inside `review`. `plan` now says the audit procedure is designed there, per audit. |
| Every front-matter field `task-template.md` carries, or why one is absent | met | `related`, `business_value` and `effort` added. Every field the task template carries is now present; none is absent, so nothing needs excusing. |
| The failure is caught mechanically from now on — shown by breaking a template on purpose | met, with a stated limit | Two of the four defect classes are mechanical and have a fixture. Missing fields and body structure are not, for the reasons in §3 — `check` requires neither of a task either, so requiring them of a template would invent a rule. Step 5 covers what is left, weakly and honestly. |
| The audit-type decision is recorded with the alternative rejected — template and vocabulary must not disagree again | met | The decision and its rejected alternative were already in §1 (Q1, 2026-08-06). *Must not disagree again* is now enforced rather than intended, and it caught a live disagreement in `_task-template.md` on its first run. |

**Child fix tasks raised**
- none. The one thing found and not fixed here — a template's links breaking when it is copied into
  a project without this one's directory layout — is already
  [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md), open and in this same
  release.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Plan through review in one session, under the maintainer's `M2` whole-lifecycle authorisation of 2026-08-10 (METHOD §3.1). The check was built before the repair, and found a second, unknown defect on its first run — the shipped **task** template's `type` menu, five values of seven. So the log entry above, which recorded a second project wanting this criterion, understated it: the repository asking for the check was itself failing it. |
| 2026-08-10 | (no change) | **Independent evidence for the second in-scope item**, from the first adopting project's recommendations (`control/LOCAL-CONTEXT.md`, raised there as R-3): a `_`-prefixed Markdown file in `tasks_dir` whose front-matter fails the schema is a template that will produce a failing task, and nothing reports it. That is this task's *"a way for a template's front-matter to be checked"* reached from outside, by a project that hit the consequence rather than by an audit of this one — so the criterion is now wanted by two projects and no criterion is amended. The other half of R-3, a template the create path cannot see at all, is **not** here: it is [T-101](T-101-report-a-template-the-create-path-cannot-see.md), because the file is never opened and the silence reads as the legal "this project has no template". **Not a status change**: nothing about the four defects or the five criteria moved. |
| 2026-08-09 | (no change) | Reconciled by [T-076](T-076-decide-what-a-template-s-links-resolve-against.md), which moved both templates from `tasks/_templates/` to `tasks/` as `_`-prefixed files. Four path references updated — Outcome, defect 2, Scope *In*, Inputs — and *Why nobody saw it* annotated rather than rewritten: its mechanism is now historical, its conclusion still holds, and it is the record of why F-6 survived. **Not a status change**: nothing about this task's four defects or its criteria moved, and the second in-scope item — a way for a template's front-matter to be checked — got closer rather than different, since `load_tasks` now reads the file and rejects it on its id instead of never opening it. |
| 2026-08-06 | → specified | Q1 answered by the maintainer: `type` gains `audit`. The answer's own reasoning — that an audit runs the same pipeline as any other task — is what settles it, since `type` and `phase` are orthogonal and every existing value already runs all four phases; the deciding argument is that METHOD §5 calls audit a task type while the schema has no such value, which is the drift this plugin exists to remove. No criterion amended; criterion 5 already required the rejected alternative to be recorded and it now is. The answer also carried an account of the audit *workflow* — two method changes that would have widened this task into the thing it was raised to fix, so they are split to T-036, one agreed and one argued against there rather than here. |
| 2026-08-06 | → proposed | Raised as F-6 from the T-026 audit, clauses 1 and 3. Proven by building a task from the template and running `check`, which reported two classes; the other two defects are structural and invisible to it. The audit that found this is the one that would have been created from the template. |
