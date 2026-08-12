---
id: T-051
title: Say where a project's task template lives
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-003, T-001]
work_package: M1
owner: maintainer
business_value: medium
effort: s
created: 2026-08-07
updated: 2026-08-09
deliverables:
  - plugin/skills/taskmd/docs/bindings/local-markdown.md
---

# T-051 — Say where a project's task template lives

## 1. Specify

**Outcome**
An agent creating a task in a project it has not seen before can find that project's template, or is
told plainly that there is none and what to do instead.

**Why this one**
Found while writing the skill ([T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md))
and raised rather than absorbed, per `docs/METHOD.md` §3.3.

[`docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *create* says **"Copy the
template"**. Nothing says where the template is. The schema
([`taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md)) names every key that exists and none of
them names a template, and `check` therefore cannot report a missing one. This repository keeps its
template at `tasks/_templates/task-template.md` and that path appears in `../CLAUDE.md` — so the
convention exists here and is invisible to an adopting project, which is exactly the shape of defect
`docs/BINDING.md` §4 was written to catch: a premise about the adopting project that was never
surfaced to be checked.

**Not urgent, and worth saying why.** Nothing is broken today: creating a task without a template
still produces a file `check` accepts, because the schema is what `check` validates and the template
is only a convenience. The cost is a worse first task in every project that adopts taskmd, and one
more thing an adopter has to be told rather than shown.

**Requirements served**
R-11, R-13, R-17 (`docs/SCOPE.md`).

**Scope**
- In: where the answer belongs — the schema, the binding, or the convention the binding already
  relies on when it skips `_`-prefixed folders while enumerating.
- In: what happens when a project has no template at all, which must be a supported state rather
  than an error.
- Out: changing the template's content, and validating templates — [T-032](T-032-repair-the-audit-template-and-validate-templates.md) holds both.
- Out: adding a command. `docs/SCOPE.md` non-goal 11 still stands after its 2026-08-05 amendment.

**Inputs**
[`docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) *create* and *enumerate*,
[`taskmd/defaults/config.md`](../plugin/skills/taskmd/taskmd/defaults/config.md),
[`docs/BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §2 and §4,
[T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) — the schema-is-configuration
decision this would extend.

**Acceptance criteria**
- [ ] An agent that has read only the binding and the schema can locate a project's template, or
      knows there is none — checked by doing it on a project other than this one
- [ ] A project with no template is a supported state, and nothing reports it as a problem
- [ ] Whatever carries the answer does not become a second copy of a path this repository already
      writes down in `../CLAUDE.md`
- [ ] ~~If the answer is a new config key, it is a required key like every other one, and
      `taskmd/defaults/config.md` documents it — the schema has no optional keys, by T-001~~
      — **moot, and kept to say so.** The answer is a convention, so there is no key. The criterion
      was a conditional and its condition is now false; deleting it would hide that the key was
      considered and declined

**Open questions**
- ~~**Is a config key the right shape, or a convention the binding states?**~~ **Answered by the
  maintainer on 2026-08-09: a convention, stated in the binding.**

  The question asked what `check` could report in each case, and the answer is **nothing useful**.
  No code reads the template path: there is no `create` command and non-goal 11 keeps it that way,
  so the binding's *create* step — *"Copy the template"* — is performed by an agent following prose,
  not by the tool. A key would therefore be a required line in every adopting project's config,
  naming a file no command opens, which §1 *Invisibility* is exactly the property that rejects.

  **The convention is a rule, not a path**, which is what keeps criterion 3 satisfiable: *the
  template is an `_`-prefixed Markdown file in `tasks_dir`*. Nothing enumerates it, nothing can go
  stale, and a project with none is legal by construction because the rule describes where to look
  rather than what must exist. It also reuses a mechanism the binding already relies on —
  *enumerate* skips `_`-prefixed names — rather than introducing a second one.

  **Decide the shape with [T-076](T-076-decide-what-a-template-s-links-resolve-against.md).** That
  task's answer puts templates at the same depth as the tasks they become, as `_`-prefixed **files**
  in `tasks_dir`. The two answers are the same convention seen from opposite ends, and stating them
  independently would give one fact two homes.

  *Rejected: a config key.* It is checkable in principle, and that is its whole case. There is
  nothing to check until [T-032](T-032-repair-the-audit-template-and-validate-templates.md) makes
  templates validatable, and a key added now buys a line in every project's config against a
  validation that does not exist. If T-032 gives `check` something real to say about a template, the
  key can be argued for then, on evidence.

## 2. Plan

**This is half a plan, and the other half is [T-076](T-076-decide-what-a-template-s-links-resolve-against.md)'s.**
That task moves this repository's two templates and repairs every reference to their old location;
this one states the convention so a project that is not this one can follow it. The split is by
outcome, so neither table restates the other. **T-076 runs first** — step 3 below checks the rule
against another project, and a rule this repository does not yet obey is not worth checking.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | State the convention in the binding's *create*, where the need arises — it is *create* that says "Copy the template" and does not say which file that is. Write it as the **rule** the answer settled on, and name the mechanism that actually excludes such a file, which is assumption 6's id rule and **not** the folder skip in *enumerate*. | A paragraph in `plugin/docs/bindings/local-markdown.md` *create* |
| 2 | Say, in the same paragraph, what an agent does when the rule matches nothing — the no-template case is supported, not an error. | Same paragraph; no second home |
| 3 | Check criterion 1 from outside: on a scratch project that is not this repository, locate the template using only the binding and the schema, then repeat with the template removed. | A transcript in §3 of both outcomes — found, and correctly reported absent |
| 4 | Check criterion 2: run `check` on that scratch project with no template present, and confirm it says nothing about the absence. | Command output in §3 |
| 5 | Check criterion 3: confirm the binding names no path, so nothing it says can become a second copy of the path `../CLAUDE.md` writes down. | A grep over the new paragraph, in §3 |

**Decision on the shape, recorded here because step 1 could reasonably go elsewhere.** The convention
goes in the **binding**, not in `SKILL.md` and not in the schema. The skill already sends an agent to
the binding *before creating or changing any task*, so the binding is where an agent is standing when
the question arises; putting it in `SKILL.md` would need the skill to know a local-Markdown fact,
which is what the binding layer exists to keep out of it. *Rejected: the schema* — that is §1's
answered question, and the rejection with its cost is recorded there, not re-argued here.

**Outputs**

```
plugin/docs/bindings/local-markdown.md
```

## 3. Implement

**Steps 1–2 — the rule, written into the binding's *create*.** Two paragraphs, both under *create*
because that is the operation that says "Copy the template": *Which template*, stating the rule and
why each half of it is load-bearing, and *A project with no template is a normal project*, stating
the empty case. The mechanism named is assumption 6's id rule — the correction recorded in the log
below — and with it the two consequences an adopter would otherwise meet by surprise: a template is
link-checked like anything else in the tree, and a placeholder id made real turns the template into
a task.

**Steps 3–4 — checked on a project that is not this one.** A scratch project holding one real task,
a `_`-prefixed template beside it, and a `notes.md` at the project root for the template to link to.
Nothing was copied from this repository; the rule was applied as written.

```
=== the rule applied: _-prefixed Markdown files directly in tasks_dir ===
tasks/_task-template.md
=== check ===
OK - 1 task(s), vocabulary valid, references resolve, no broken links
=== list ===
T-001	proposed	-	specify	A real task
```

Found, and the template is not work. Then *create* performed as the binding describes — copy it out,
fill the placeholders — with the template's relative link left exactly as written:

```
OK - 2 task(s), vocabulary valid, references resolve, no broken links
```

The template's body carried one relative link, up one level to the project's notes file. It survived
the copy verbatim and `check` resolved it from the copy's location — the count going from 1 task to 2
with nothing else to report. (That line is described rather than quoted, for the reason
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md) §3 records after this record tripped
over it.) That is
[T-076](T-076-decide-what-a-template-s-links-resolve-against.md)'s half of the convention holding on
a project other than this one. Then the same project with its template deleted:

```
ls: cannot access 'tasks/_*.md': No such file or directory
(the rule matches nothing: this project has no template)
OK - 1 task(s), vocabulary valid, references resolve, no broken links
exit 0
```

Criterion 2 met by that last pair: the rule matching nothing is an answer an agent can act on, and
`check` exits 0 with nothing to say about the absence.

**Step 5 — the binding names no path.** A grep for a path-shaped string over the two new paragraphs,
and for any template filename over the whole binding, both print nothing. Criterion 3 holds by
construction rather than by care: there is no path in the binding to drift from the one
`../CLAUDE.md` writes down.

**Decisions & assumptions**
- **The convention goes in the binding, not in `SKILL.md` and not in the schema** — 2026-08-09,
  recorded in §2 with what it rules out. Unchanged by implementation.
- **The stated mechanism is assumption 6's id rule, not *enumerate*'s folder skip** — 2026-08-09.
  §1's answer said the convention reuses the skip of `_`-prefixed names; that skip is applied to
  **folders** only, and a `_`-prefixed file directly in `tasks_dir` is read and then rejected because
  its placeholder id is not the prefix plus `id_width` digits. Found in `schema.py` rather than in
  the binding, which is why it survived being answered. The decision is untouched — T-076's scratch
  evidence tested the outcome, not the reason — but a binding that named the wrong mechanism would
  mislead precisely the adopter this task is written for.
- **The no-template case says what it costs** — 2026-08-09. A project cannot be *told* it has no
  template, only discover it; that follows from there being no key and no command, and it is written
  down rather than left as an implication, because it is the one thing a config key would have
  bought and §1 rejected the key.

**Outputs produced**
- [`plugin/docs/bindings/local-markdown.md`](../plugin/skills/taskmd/docs/bindings/local-markdown.md) — *create*
  gains *Which template* and the no-template paragraph

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| An agent that has read only the binding and the schema can locate a project's template, or knows there is none — checked on a project other than this one | met | §3 steps 3–4, on a scratch project built from nothing this repository holds. The rule listed the template; with it deleted the rule matched nothing, which the agent can act on. Both directions checked, not just the found one |
| A project with no template is a supported state, and nothing reports it as a problem | met | `check` on the template-less scratch project: `OK - 1 task(s)`, exit 0, no mention of a template. Nothing to suppress, because nothing ever looked |
| Whatever carries the answer does not become a second copy of a path `../CLAUDE.md` already writes down | met | The binding names **no** path: a grep for a path-shaped string over the new paragraphs, and for any template filename over the whole binding, both print nothing. The rule is a place to look, so there is nothing that can drift |
| ~~If the answer is a new config key…~~ | moot | Struck at `specify` and kept to record that the key was considered and declined. Its condition is false: the answer is a convention, so no key exists and `taskmd/defaults/config.md` is untouched |

**Child fix tasks raised**
- none. One correction was made **inside** this task rather than raised: §1's answer named the wrong
  exclusion mechanism, which is a defect in this task's own reasoning and not a finding about
  something else. Recorded in §3 and in the log, and the binding states the mechanism that is real.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | → done | Three live criteria met, the fourth moot and struck at `specify`; no child raised. The rule went into the binding's *create* and was checked on a scratch project built from nothing this repository holds — found when present, and correctly reporting nothing when absent, with `check` exiting 0 and saying nothing about the absence. One correction was made inside the task rather than raised as a finding: §1's answer justified the convention by *enumerate*'s skip of `_`-prefixed names, which applies to **folders**, and what really excludes a `_`-prefixed file directly in `tasks_dir` is assumption 6's id rule. The decision survives — [T-076](T-076-decide-what-a-template-s-links-resolve-against.md)'s scratch evidence tested the outcome, not the reason — but the binding now names the mechanism that is real, which matters because the reader it is written for has nothing else to go on. Criterion 3 held by construction: the binding names no path at all, so there is nothing to drift from `../CLAUDE.md`. |
| 2026-08-09 | → planned | Planned **with [T-076](T-076-decide-what-a-template-s-links-resolve-against.md), as one plan split by outcome across two tables**; T-076 moves the files and runs first, this one states the rule and then checks it somewhere else. The home is decided and recorded as a plan decision: the **binding's *create***, because `SKILL.md` already sends an agent there before creating any task, and because a local-Markdown fact written into the skill is exactly what the binding layer exists to keep out of it. One correction to §1's reasoning, found by reading the code rather than the binding: the answer says the convention reuses *enumerate*'s skip of `_`-prefixed names, and that skip applies to **folders only** — a `_`-prefixed *file* is read and then rejected by assumption 6's id rule. The decision is unaffected, since the scratch-project evidence in T-076 §1 tested the outcome rather than the reason, but the paragraph step 1 writes must name the mechanism that is really doing the work. |
| 2026-08-09 | → specified | Answered: **a convention, not a config key**. The open question asked what `check` could report in each case and the answer settled it — nothing useful, because no code reads the template path: there is no `create` command, so the binding's *create* step is followed by an agent rather than executed. A required key naming a file no command opens is what §1 *Invisibility* rejects. The convention is stated as a **rule** — an `_`-prefixed Markdown file in `tasks_dir` — which is what keeps criterion 3 satisfiable, since a rule cannot become a second copy of a path. Criterion 4 is conditional on the answer being a key and is now moot; kept and marked rather than deleted. To be decided and written with T-076, whose answer is the same convention from the other end. |
| 2026-08-07 | → proposed | Raised from T-003, which needed to tell an agent how to create a task and found that the binding's *create* names a template the project has no way to locate. Not fixed there: T-003's scope puts the CLI and the schema out, and this is a premise about the adopting project rather than something T-003 made false — so METHOD §5's distinction applies and it is a finding, not reconcile debt. `medium`/`s` because nothing is broken until someone adopts taskmd, and T-006 is the task that makes that possible. |
