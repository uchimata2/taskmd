---
id: T-026
title: Audit the whole project before the remaining build
type: audit
status: review
phase: review
parent: null
blocked_by: []
related: [T-003, T-006, T-010, T-025]
work_package: v0.2
owner: maintainer
business_value: high
effort: l
created: 2026-08-05
updated: 2026-08-06
deliverables: []
---

# T-026 — Audit the whole project before the remaining build

## 1. Specify

**Outcome**
A recorded examination of every tracked file in this repository, with each finding written down at a
stated severity and each actionable one carried by its own child task — so the work that remains
(T-003, T-006, T-010) is built on a base that has been looked at rather than assumed.

**Requested by the maintainer, 2026-08-05**, verbatim, because the wording is the scope until
`specify` narrows it:

> a thorough audit on all project files, looking for stale info, potential inconsistency generating
> methods, contradictory feature, unnecessary complexity, performance issues, technical challenges,
> duplication, inefficient token usage, better out-of-the-box ideas for a feature, anything.

**Why now**
Three sessions have added a backend contract, a fourth command, two schema fields and two amendments
to `docs/SCOPE.md`'s non-goals. Amendments are the expensive kind of change: each one licenses
something a previous decision forbade, and every document that cited the old wording is a candidate
for having quietly become false. Two such drifts were already caught by hand this session — a
`.handoff/config.md` and a `CLAUDE.md` still claiming three commands — which is evidence that the
sweep is worth doing deliberately rather than opportunistically.

The project is also close to the point where auditing gets harder: T-003 writes the skill and T-006
publishes. A finding raised after publication costs a release.

**Requirements served**
None directly — an audit examines conformance to the requirements rather than adding to them. Its
findings will cite them.

**Scope**
- In: every tracked file. Documents (`CLAUDE.md`, `docs/`, `tasks/`), code (`taskmd/`), tests and
  fixtures (`tests/`), configuration, and the generated index.
- In: the seven concerns the maintainer named, plus "anything" — which is deliberately open, and is
  why the finding threshold below matters more than usual.
- Out: **fixing anything**. METHOD §5 and [`audit`](../plugin/skills/taskmd/docs/method/audit.md) — a finding is never
  fixed where it is found, and the one exception is a finding that makes continuing impossible.
- Out: `reference/`, which is prior art from another project and is not this repository's to
  correct.
- Out: re-litigating settled decisions **as preference**. "I would have decided differently" is not a
  finding. What *is* in — and this is wider than it was when the task was raised — is a decision,
  requirement or non-goal whose **consequence costs weight the purpose does not need**: see the
  threshold's clause 5 below and the maintainer's amendment recorded with it. So `docs/SCOPE.md` §6's
  assumptions, its amendments to non-goals 1 and 11, and the requirements themselves are all
  examinable, on the condition that the finding shows the cost rather than asserting a preference.

  **This overrides `docs/SCOPE.md` §6's "no session should re-raise them", for this audit only.** The
  override is the maintainer's, given 2026-08-06 when the threshold was set. It is recorded here
  rather than edited into `docs/SCOPE.md`, because changing that sentence is a fix and this task
  fixes nothing — if the audit finds §6's wording should soften permanently, that is a child task
  like any other finding.

**Inputs**
- [`docs/method/audit.md`](../plugin/skills/taskmd/docs/method/audit.md) — the procedure, including why the
  no-inline-fix rule is the whole product
- `docs/SCOPE.md` — the requirements findings will cite, the non-goals, and §1's three properties
- `CLAUDE.md` — the publishing, portability and verification constraints
- `python -m taskmd list --json` — the whole graph, in one call, without reading 26 files

**The finding threshold — decided by the maintainer, 2026-08-06, before looking**

A finding is **anything that would cost a later reader or session real work.** Five clauses, numbered
so every finding can cite the one it meets:

1. **A statement that is false or stale** — including one that was true when written.
2. **Two places that must be updated together** — a fact with more than one home, whether or not the
   copies have drifted yet.
3. **A consequence that contradicts a stated goal** — `docs/SCOPE.md` §1's three properties, its
   requirements, or `CLAUDE.md`'s constraints.
4. **A cost paid on every turn** — tokens, an always-loaded file, a step someone must remember.
5. **Weight the purpose does not need.** *Added by the maintainer with the decision:* the purpose is
   **an efficient, lightweight, Markdown-focused task tracker for agentic coding**, and a finding may
   derail from a stated requirement, a settled decision or a non-goal where doing so **simplifies or
   makes more sense**. The finding must show the weight — what it costs, and what the simpler thing
   would be. A preference with no cost attached is not a clause-5 finding, which is the whole
   difference between this clause and re-litigation.

**Below the line:** style and wording preference, and feature ideas nobody asked for — *except* where
the idea is **cheaper than what exists**, which is a clause-5 simplification rather than a proposal.

Clause 5 is the one that will be argued with, so its test is stated rather than left to judgement:
**would a reader who accepts the purpose in §1 of `docs/SCOPE.md` agree the current design costs more
than it returns?** If the answer needs the auditor's taste to come out yes, it is below the line.

**Acceptance criteria**
- [x] The finding threshold is written down **before** looking, and every finding is judged against
      it — without one, an audit reports whatever its author happens to dislike and cannot be
      compared to the next one. **Met at `specify`**: the five clauses above, decided by the
      maintainer before any file was examined
- [ ] **Every finding cites the threshold clause it meets.** Falsified by a finding whose presence in
      the list can only be justified by the auditor being asked — which is the state clause 5 makes
      easiest to reach and hardest to notice
- [ ] **A clause-5 finding shows the weight, not the preference** — what the current design costs and
      what the cheaper thing is. Falsified by any finding that would evaporate if the reader simply
      disagreed about taste
- [ ] Every area in scope is recorded as examined, including the areas that produced **no** finding
      — that half is what distinguishes "checked and clean" from "not looked at"
- [ ] Each finding carries a severity and enough detail for someone who was not present to act on it
- [ ] Each actionable finding has its own child task pointing back here; each non-actionable one
      stays recorded with the reason it needs no action
- [ ] Nothing is fixed in place — falsified by any commit from this task that changes behaviour or
      wording outside this task's own record
- [ ] The umbrella closes only when every child is resolved or dropped with a reason
- [ ] **The umbrella reports the child tasks in the order `python -m taskmd list` computes**, and
      states whether that order is one a person would actually work in. Both outcomes count as met —
      an order that reads sanely is evidence the ordering rule works on tasks nobody hand-sorted, and
      one that does not is itself a finding against the rule. Falsified only by the order not being
      run, or by being run and quietly reordered by hand

**Open questions**
- ~~What is the finding threshold?~~ **Answered by the maintainer 2026-08-06:** the recommendation,
  taken with an amendment that widened it — **clause 5**, above. The maintainer's words: go with the
  recommendation *"but not blindly, feel free to derail from the original requirements if it
  simplifies or makes more sense. Step back, understand the purpose of such plugin, and make
  reasonable decisions to have an efficient, lightweight, md focused track management system for
  agentic coding."* The narrower option — falsity and per-turn cost only — was **not** taken; nor was
  the broader one that would have admitted feature proposals on their own merits. What the amendment
  changes about this task: the out-list's third bullet, above, no longer shields settled decisions
  from examination, only from preference.
- ~~Does the audit rank findings by the project's own ordering rule?~~ **Answered by the maintainer
  2026-08-06: yes**, and it is now the last acceptance criterion. This is the first use of `list` on
  tasks nobody has hand-sorted, so the ordering rule is under examination at the same time as the
  files are — which is the reason a bad order counts as a met criterion rather than a failed one.

## 2. Plan

**The sequencing rule, stated because it is the plan's one real choice.** Clause 5 asks whether the
design costs more than it returns — a judgement that is worthless without the cost in hand. So the
mechanical clauses run first and the purpose pass runs **last**, over evidence rather than over
impressions. A plan that opened with "is the lifecycle too heavy?" would be answering from taste,
which is exactly what the threshold's own test forbids.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Build the coverage denominator before looking at anything.** Enumerate every tracked file from `git ls-files`, assign each to an area, and mark `reference/` out of scope. Coverage cannot be claimed without a set to claim it over. | The coverage table in §3 — one row per area, listing its files and, later, the finding ids raised against it. Every tracked file appears in exactly one row |
| 2 | **Run the two cross-cutting checks, which no single-file reading can see.** Clause 2 — every fact asserted in more than one file, whether or not the copies have drifted. Clause 4 — every file loaded on every turn, measured against whatever budget it states, and every budget that is stated nowhere. | A table of raw observations in §3, each with `file:line` and the clause it is a candidate for. Not yet findings — classification is step 7 |
| 3 | **Examine the tool** — `taskmd/`, `tests/`, `tests/fixtures/`. Most objective area: the code either does what the documents claim or it does not, and running it settles which. This is also where the cost evidence for step 6 is collected. | Observations appended to the §3 table, plus the actual output of any command run to settle a question |
| 4 | **Examine the documents** — `docs/` in full (`SCOPE`, `BRIEF`, `METHOD`, `BINDING`, `method/`, `bindings/`), `CLAUDE.md`, `.handoff/config.md`, `LICENSE`, `.gitignore`, `.gitattributes`. Judged against clauses 1 and 3; clause-5 candidates are noted and deferred to step 6. | Observations appended to the §3 table |
| 5 | **Examine the tracker content** — the 26 task files, both templates in `tasks/_templates/`, and the generated `tasks/README.md`. The templates are the highest-yield part: they are copied forward, so a defect in one propagates into every task made from it. | Observations appended to the §3 table |
| 6 | **The purpose pass — clause 5 only, once, over everything steps 2–5 gathered.** The question is the maintainer's: does this design cost more than it returns for *an efficient, lightweight, Markdown-focused tracker for agentic coding*? Requirements, non-goals and the §6 assumptions are all in range here and nowhere else in the plan. Each candidate must name the cost and the cheaper thing, or be dropped. | The clause-5 findings, each carrying its cost and its proposed simplification, in the §3 table |
| 7 | **Classify: clause, severity, and dedupe against work already raised.** Every observation from steps 2–6 becomes a finding with a cited clause and a severity, or is dropped with the reason it fell below the line. Dedupe is a real step, not hygiene — T-025 is already raised for the stale-index gap, and T-021, T-023 and T-024 are open against known defects; a finding that restates one of them is not a new child task | The completed findings table in §3, every row carrying a clause, a severity and an action |
| 8 | **Raise one child task per actionable finding**, each with `parent: T-026`, citing the finding id. Non-actionable findings stay in the table with the reason they need no action. | One new file per actionable finding in `tasks/`, and the child-task column of the §3 table filled in |
| 9 | **Run the project's own ordering over the children and report it** — `python -m taskmd list --open`, plus the children specifically. State whether the order is one a person would actually work in, and if not, that is a finding against the ordering rule rather than a reason to reorder by hand. | The command's actual output in §3, with a one-paragraph judgement of it |
| 10 | **Validate and prove nothing leaked.** `check`, `index`, the suite, and the `CLAUDE.md` pre-publish check — the last of these run **after** the record is written, per `CLAUDE.md`, and never with a matched line quoted back into the record. | The actual output of all four in §3 |

**Do not plan past step 6.** Steps 7–9 are shaped by what step 6 returns: a clause-5 finding large
enough to question the lifecycle or the command surface would change what the child tasks *are*, and
possibly whether some findings should wait on a decision rather than become tasks. If that happens,
it is raised as a question rather than absorbed into the step-8 list.

**Dependencies — checked, none needed.** The audit reads; it waits on nothing. T-025 overlaps its
subject matter but does not gate it, and T-003, T-006 and T-010 are what the audit exists to protect
rather than things it needs. All four are already recorded as `related`, which is the correct edge
([`../plugin/skills/taskmd/docs/METHOD.md`](../plugin/skills/taskmd/docs/METHOD.md) §4) — a dependency edge here would falsely say the audit
cannot proceed.

**Deliverable shape — decided here.**

**The findings live in T-026's own record, not in the audit umbrella template.** *Rejected:*
`tasks/_templates/audit-umbrella-template.md`, which exists and looks like the obvious home. It
cannot be adopted as it stands, and correcting it first would be a fix — the one thing this task may
not do. Its condition is in scope for step 5 and will be recorded as a finding like anything else.
The consequence is deliberate: this audit shows what the template *should* have been, and the
template is then corrected by a child task rather than by the auditor.

**One table, one row per finding**, carrying: id (`F-n`), area, the threshold clause cited, the
finding, severity, and the action — a child task id, or "no action" with the reason. *Rejected:*
separate tables for actionable and non-actionable findings, which would let a reader consume one
without the other. The no-action rows are the evidence an area was examined, and
[`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) makes them worth as much as the rest; splitting them off is how
they get skipped.

**Severity says who pays and when**, so that a reader who was not present can triage without asking:
**High** — costs work now, or would cost a release if it survived into T-006; **Medium** — will cost
work, at a time not of anyone's choosing; **Low** — costs work only when someone next touches that
file. *Rejected:* inventing a numeric scale, which would need a rubric nobody would read.

**Output paths**

- `tasks/T-026-audit-the-whole-project-before-the-remaining-build.md` — §3, carrying the coverage
  table, the findings table, the ordering output and the validation transcript
- `tasks/T-NNN-*.md` — one new file per actionable finding; the count is not knowable until step 7
- `tasks/README.md` — regenerated, because raising child tasks changes it

The `deliverables:` field stays empty until step 10, for the reason
[T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) recorded: `check` validates that
every declared path exists.

## 3. Implement

Worked in plan order. Steps 2–6 were executed as planned; nothing was reordered.

### Decisions & assumptions

- **A finding's severity is judged on cost, not on how wrong it feels** — 2026-08-06, step 7. Two
  findings that read as embarrassing (the design rule written three times; the audit template that
  cannot make a valid task) are High because they are paid for every turn and at every audit
  respectively, not because of how they read. Conversely F-7 stays Medium despite being a dangling
  reference in a contract document, because a reader who ignores the label loses one citation.
- **Task records were excluded from the duplication findings** — 2026-08-06, step 5. A task record
  is a dated account of a decision, not a live claim to keep in step. Counting T-002's and T-022's
  statements of the `list` rationale as copies would have made F-5 look twice as large and would
  have implied rewriting history to match a later document, which destroys the record the method
  exists to keep. Stated here because the opposite choice would have been defensible and would have
  changed the finding count.
- **Clause 5 produced one finding and one deliberate refusal** — 2026-08-06, step 6. F-2 is the
  clause-5 finding, and it names its cost in lines. The four-phase lifecycle was examined under the
  maintainer's explicit licence to derail from settled decisions and was **dropped** — see N-5. That
  refusal is the threshold doing its job, and it is recorded rather than omitted because an audit
  that only reports what it found cannot be told apart from one that only looked where it expected.
- **Nothing was fixed.** The only files this task changed outside its own record are the seven new
  child tasks and the regenerated index. The temporary project built to prove F-6 was made outside
  the repository and deleted.

### Step 1 — coverage

Every tracked file, from `git ls-files`, assigned to exactly one area. **84 tracked files at the time
of examination**; 5 are `reference/`, which `specify` put out of scope, leaving **79 in scope**. The
eight child tasks this audit produced are its output, not its subject, and are not in the denominator.

*(Corrected at `review`: this table first read "82 tracked files; 8 are `reference/`". Both counts
were wrong, and criterion 4 rests on this denominator being right. The recount is below and the
per-area figures now sum to it — the correction is recorded rather than made silently, because a
coverage claim whose arithmetic was quietly repaired is worth no more than one that was never
checked.)*

| Area | Files | # | Examined | Findings |
| :--- | :--- | ---: | :---: | :--- |
| Root documents | `CLAUDE.md` | 1 | yes | F-1, F-2, F-8 |
| Repository config | `.gitignore`, `.gitattributes`, `LICENSE` | 3 | yes | none — N-10 |
| Handoff config | `.handoff/config.md` | 1 | yes | none |
| Scope & brief | `docs/SCOPE.md`, `docs/BRIEF.md` | 2 | yes | F-2, F-5, F-7 |
| Method | `docs/METHOD.md`, `docs/method/` (7) | 8 | yes | F-1, F-2 |
| Backend contract | `docs/BINDING.md`, `docs/bindings/local-markdown.md` | 2 | yes | F-7 |
| Tool — code | `cli.py`, `schema.py`, `__init__.py`, `__main__.py` | 4 | yes | F-3, F-4, F-5 |
| Tool — schema config | `taskmd/defaults/config.md` | 1 | yes | none |
| Tests | `test_cli.py`, `test_schema.py`, `test_list.py` | 3 | yes | none — N-7 |
| Fixtures | `tests/fixtures/` (incl. its `README.md`) | 25 | yes | none — N-7 |
| Task files | `tasks/T-001` … `tasks/T-026` | 26 | yes | F-7 |
| Templates | `tasks/_templates/` | 2 | yes | F-6 |
| Generated index | `tasks/README.md` | 1 | yes | none |
| **In scope** | | **79** | | |
| **Out of scope** | `reference/` | 5 | no | prior art from another project (`specify`) |
| **Tracked total** | | **84** | | |

### Steps 2–6 — findings

Every row cites the threshold clause it meets. Severity is defined in §2.

| # | Area | Clause | Finding | Severity | Action |
| :-- | :--- | :---: | :--- | :---: | :--- |
| **F-1** | Root, method, scope | 2, 4 | The design rule and its *compels the second write* qualification are written out in full in `CLAUDE.md`, `docs/SCOPE.md` §2 and `docs/METHOD.md` §4. The SCOPE↔METHOD pair is sanctioned by SCOPE §3 (T-017); the third is not, and `CLAUDE.md` itself says *"if you find it written out somewhere else, that copy is the defect"*. It is loaded every turn. | High | [T-027](T-027-give-the-design-rule-one-home.md) |
| **F-2** | Root, method | 3, 4 | The 150-line spine budget governs `docs/METHOD.md` alone. Measured always-loaded cost is `CLAUDE.md` 139 + `METHOD.md` 147 = **286 lines**, against the 173-line flat alternative the limit is justified against — so by the budget's own stated test the split has inverted its point, and the budget cannot see it. METHOD.md is at 147/150, so the constraint binds on the wrong file. | High | [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) |
| **F-3** | Tool | 3 | `check`, `index` and `context` discard unknown arguments in silence. `index nonsense --wat` **wrote the index and exited 0**. `list` rejects before printing anything (T-022); the other three never got it. R-17's reasoning applied at the command layer. | High | [T-029](T-029-reject-unknown-arguments-on-every-command.md) |
| **F-4** | Tool | 1, 3 | `python -m taskmd.schema` is a runnable fifth entry point, named only in its own module docstring, taking a positional directory where everything else takes `--root`. It prints the absolute install path on the **success** path — which R-20 forbids and which `_check_tasks_dir`'s docstring in the same file names as the reason it avoids doing so. Deduped against T-023, whose scope is error messages only. | Medium | [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) |
| **F-5** | Scope, brief, tool | 2 | The "grep cannot see a derived edge" argument is written in four live homes — `docs/SCOPE.md:152`, `docs/BRIEF.md:89`, `taskmd/cli.py:12`, `taskmd/cli.py:477` — two of them in one file. | Medium | [T-031](T-031-give-the-list-rationale-one-home.md) |
| **F-6** | Templates | 1, 3 | `tasks/_templates/audit-umbrella-template.md` cannot produce a valid task. Proven: `check` reports `VOCABULARY type is 'audit'` and `STORED DERIVED stores 'children:'`, exit 1. Two further defects it cannot see — no `related`/`business_value`/`effort` (T-022's backfill missed this template), and a body that is not the four mandatory phases (R-3). Invisible because `load_tasks` skips `_`-prefixed folders, so templates are never validated. | High | [T-032](T-032-repair-the-audit-template-and-validate-templates.md) |
| **F-7** | Brief, contract, tasks | 1, 3 | "F1" is used as a load-bearing reference in `docs/BRIEF.md`, `docs/BINDING.md` §4 and `tasks/T-005` — where it is **acceptance criterion 1** — and is defined nowhere reachable. `control/LOCAL-CONTEXT.md` was checked and does not define it, so this is not the label discipline working. BINDING §4's strongest rule rests on it. | Medium | [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) |
| **F-8** | Root documents | 1, 3 | The pre-publish check reads `git ls-files`, which lists **tracked** files — so a file created but not yet staged is invisible to it, contradicting `CLAUDE.md`'s *"it sees exactly what a push would send"*. Measured mid-run: 83 files seen, 90 a push would send, with all seven new task files in the gap. The blind spot coincides with the known failure mode — both prior leaks (T-013, T-018) were in a task write-up, the newest file class. Found in this audit's own step 10. | High | [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) |

### Examined, no action

These are the evidence that an area was looked at. Without them a reader cannot tell "checked and
clean" from "not looked at" ([`audit.md`](../plugin/skills/taskmd/docs/method/audit.md)).

| # | Observation | Why no action |
| :-- | :--- | :--- |
| **N-1** | No `README.md` at the repository root, though R-15 and §9 both say the measured saving is *"stated in the README"*. | Owned by [T-006](T-006-package-document-and-publish.md) and deliberately deferred: *"A README written before the thing works becomes the unverified claim the whole project warns about."* Not a finding — a dated plan. |
| **N-2** | `check` does not notice a stale generated index. | Already raised as [T-025](T-025-let-check-notice-a-stale-generated-index.md). Re-raising it would double-count. |
| **N-3** | Every `SchemaError` against the shipped default is prefixed with an absolute install path. | Already raised as [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md). F-4 covers only what T-023's out-list leaves. |
| **N-4** | `read()` is defined identically in `taskmd/cli.py` and `taskmd/schema.py`, which already imports from the latter. | Below the threshold. Three lines with no update-together obligation in practice, and clause 5 cuts the other way — an import to save three lines is not cheaper than what exists. Recorded so the next audit does not re-discover it and reach a different answer without knowing this one was taken. |
| **N-5** | **The four mandatory phases, examined under the maintainer's licence to derail from settled decisions.** | **Dropped.** Clause 5 requires the cost *and* the cheaper thing. The audit found no cost evidence: the lifecycle is A2 in `docs/SCOPE.md` §6, R-3 is written to be falsifiable, and this audit's own three phases each produced something the next used — `specify` fixed the threshold that made step 7 decidable, `plan` fixed the sequencing that kept clause 5 honest. The case against it is that four phases *feel* heavy for small work, which is taste, and the threshold's own test excludes it. Recorded because a refusal is worth as much as a finding. |
| **N-6** | `docs/METHOD.md` is at 147 lines against its stated 150-line limit. | Within budget. The finding is F-2's — about what the budget measures, not about this file breaching it. |
| **N-7** | `tests/` — 92 tests, 92 pass. Each `broken-*` fixture holds exactly one defect, as `tests/fixtures/README.md` documents. | Examined, clean. Spot-checked the claim that each fixture holds one defect by reading the table against the fixture files. |
| **N-8** | `docs/method/` (7 files), `docs/BINDING.md`, `docs/bindings/local-markdown.md`, `tests/fixtures/README.md`, `taskmd/defaults/config.md`. | Examined, no finding. The binding's six assumptions and BINDING §3's derived-view rules were checked against what the code actually does and agree with it. |
| **N-9** | `reference/` — 8 files. | Out of scope by `specify`: prior art from another project, not this repository's to correct. |
| **N-10** | `.gitignore`, `.gitattributes`, `LICENSE`, `taskmd/__init__.py`, `taskmd/__main__.py`, `.handoff/config.md`. | Examined, no finding. `.gitattributes` enforces `eol=lf`, which is what makes the byte-identical claim meaningful. |
| **N-11** | **The ordering rule separated the four `high`/`s` children by id alone** — see step 9. With a 4-value × 5-effort vocabulary, eight real tasks collapsed to four ranks. | Not a defect: `taskmd/defaults/config.md` §*Ordering* documents the id tiebreak as deliberate and total. Not raised as a proposal either, because clause 5 needs a *cheaper* alternative and there is none obvious — finer vocabularies buy resolution by demanding more estimation, which fails `docs/SCOPE.md` §1 *Invisibility*. Recorded so that the next audit finds this was considered rather than missed, and so the limit is visible to [T-006](T-006-package-document-and-publish.md) before the README claims anything about ordering. |

### Step 9 — the project's own ordering, run over the children

The first use of `list` on tasks nobody hand-sorted. Criterion says a bad order is a finding, not a
reason to reorder by hand.

```
python -m taskmd list --parent T-026
T-034   proposed        -       specify Let the pre-publish check see files not yet tracked
T-027   proposed        -       specify Give the design rule one home
T-028   proposed        -       specify Budget the whole always-loaded context, not one file
T-029   proposed        -       specify Reject unknown arguments on every command
T-032   proposed        -       specify Repair the audit template, and validate templates at all
T-031   proposed        -       specify Give the list rationale one home
T-033   proposed        -       specify Resolve the F1 reference inside this repository
T-030   proposed        -       specify Settle the schema module's own entry point
```

**The head of the list is right and the middle of it is arbitrary.** Eight tasks produced **four**
distinct ranks: `high`/`xs` (T-034), `high`/`s` (four tasks), `medium`/`xs` (two), `medium`/`s` (one).
Nothing was reordered by hand.

T-034 leading is a genuinely good answer, and not one that was obvious while writing the findings up:
it is the cheapest task in the set *and* the one guarding the last check before publication, and the
rule surfaced it without being asked to. That is the ordering earning its keep on tasks nobody sorted.

The middle is where it runs out. The four `high`/`s` tasks tie on both sort keys and are separated by
**id alone**, which is why T-032 sits fourth — a person would put it first, since it is the only
finding that leaves a whole task type unusable and
[T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) will ship that template. The
rule is behaving exactly as `taskmd/defaults/config.md` §*Ordering* documents — *"a tie broken by id
is stated rather than arbitrary"* — so this is not a defect and is not raised as one. Recorded as
N-11, with the reason it is not being turned into work.

**An earlier run of this same command is the reason both halves are stated.** Before F-8 was found,
the list had seven tasks and three ranks, and the head *was* arbitrary; the eighth task changed the
answer. A criterion answered once, early, would have recorded the wrong conclusion about the rule.

Two limits of this run, stated so the evidence is not read as stronger than it is:

- **No child blocks another**, so effective value never diverged from plain value. The mechanism
  `tests/fixtures/ordering/` exists to prove — a cheap blocker pulled ahead by what it releases — was
  not exercised here at all.
- **The estimates are the auditor's own**, assigned in the same session as the findings. The run
  shows the rule is reproducible on tasks nobody hand-sorted; it does not show the estimates are
  right.

### Step 10 — validation

```
python -m unittest discover -s tests
Ran 92 tests in 0.245s
OK

python -m taskmd check
OK - 33 task(s), vocabulary valid, references resolve, no broken links

python -m taskmd index
Wrote tasks/README.md - 19 active, 14 closed
```

**F-6 was proven by making `check` fail**, per `CLAUDE.md` *Verifying* — a task built from the audit
template, placeholders filled in, nothing else changed:

```
VOCABULARY    T-001.type is 'audit'; allowed: analysis, decision, deliverable, research, fix, admin
STORED DERIVED T-001 stores 'children:', which is computed from 'parent'; remove it

2 problem(s) over 1 task(s)
exit=1
```

**F-3 was proven by running the commands**, output quoted in
[T-029](T-029-reject-unknown-arguments-on-every-command.md) §1 rather than duplicated here.

**The pre-publish check prints nothing** — in both forms. Run last, after this record was written,
per `CLAUDE.md`, and no matched line is quoted anywhere in this task, which is the mistake T-013 and
T-018 both made.

**Running it is what produced F-8.** The documented command printed nothing over 83 tracked files
while this task's eight new task files were untracked and therefore unread; re-run with
`--others --exclude-standard` it printed nothing over all 90, which is the result that actually
covers this session's output. Both runs are clean; only the second one means anything. The step-10
plan said "prove nothing leaked", and the honest answer was that the documented command could not
have told me either way.

### Escalated, not absorbed

**F-8 was found after the findings table was written.** METHOD §3.3 leaves two options — raise it or
let it change the current task — and dropping it because the table looked finished is the failure the
rule exists to name. It was added as a row and as [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md),
and this paragraph records that the table is not in discovery order. Nothing else was reopened.

### Outputs produced

- `tasks/T-026-…md` — this record: the coverage table, eight findings, eleven no-action rows
- `tasks/T-027` … `tasks/T-034` — one child task per actionable finding
- `tasks/README.md` — regenerated

## 4. Review

Judged against the criteria as `specify` agreed them, not against what the audit turned out to be
good at ([`review`](../plugin/skills/taskmd/docs/method/review.md) step 1).

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The finding threshold is written down **before** looking, and every finding is judged against it | met | Decided by the maintainer on 2026-08-06 before any file was opened, as five numbered clauses. The evidence it was binding rather than decorative is N-5 and N-4: two observations that survived to the write-up and were **dropped** against it. A threshold that excluded nothing would not have been one. |
| **Every finding cites the threshold clause it meets** | met | All eight rows carry a clause column; no row cites none. Checked the harder direction too — that no finding's justification is really "the auditor disliked it": each row states a fact (a line count, a command's exit code, a grep result, a `check` failure) that survives the reader disagreeing with me. |
| **A clause-5 finding shows the weight, not the preference** | met, with a stated residual | F-2 is the only clause-5 finding. Weight: 286 always-loaded lines against the 173-line flat alternative the budget is justified against — arithmetic, so it passes the falsification test decisively (it does not evaporate if a reader disagrees about taste). **Residual:** the criterion also asks for "what the cheaper thing is", and F-2 names the cheaper *measure* (budget the set, not one file) while T-028 deliberately puts choosing what to cut out of scope. If the owner reads clause 5 as requiring the cut to be named too, this is the row to re-open — flagged rather than resolved in my own favour. |
| Every area in scope is recorded as examined, including the areas that produced **no** finding | met, after correction | 14 areas, 79 in-scope files, every one assigned to exactly one area and the per-area figures summing to the tracked total. **The denominator was wrong when `implement` closed** — it read 82 files and 8 in `reference/`, against a real 84 and 5. Found here, corrected in §3 with the correction recorded in place. Eleven no-action rows carry the other half of this criterion. |
| Each finding carries a severity and enough detail for someone who was not present to act on it | met | Every row has a severity, and severity is defined in §2 by who pays and when rather than left to feel. The "someone not present" half is tested by the child tasks: each restates the evidence in full — F-6's `check` output, F-3's three transcripts, F-8's two file counts — so a reader who never sees this umbrella can still act. F-4 and F-7 additionally record the dedupe reasoning, which is what a later reader would otherwise have to redo. |
| Each actionable finding has its own child task pointing back here; each non-actionable one stays recorded with the reason | met | `python -m taskmd list --parent T-026` returns **8**, one per finding, and the count is derived from the `parent` edge rather than from a list I maintained. Eleven no-action rows each carry a reason, including the two deduped against existing tasks (N-2 → T-025, N-3 → T-023) and the two dropped against the threshold (N-4, N-5). |
| Nothing is fixed in place — falsified by any commit from this task that changes behaviour or wording outside this task's own record | met | Two tracked files modified: `tasks/T-026…md` (this record) and `tasks/README.md` (generated). No source file, no document, and **no other task file** was touched. The index diff is the strongest evidence: 11 existing rows changed while zero existing task files were edited — the soft links written on the new tasks derived onto the far ends, which is the project's own design rule producing the proof for its own audit. The temporary project built to falsify F-6 was created outside the repository and deleted. |
| The umbrella closes only when every child is resolved or dropped with a reason | **upheld — the umbrella stays open** | Not a criterion this review can tick: it governs closure, and it is satisfied by *not closing*. All eight children are `proposed`. T-026 therefore remains open at `phase: review` with the audit itself complete. Recorded plainly because an umbrella closed over open children erases the link between the examination and its consequences ([`audit`](../plugin/skills/taskmd/docs/method/audit.md) step 5), and that is the one failure this criterion exists to prevent. |
| **The umbrella reports the child tasks in the order `python -m taskmd list` computes**, and states whether that order is one a person would actually work in | met | Run and reported in §3 step 9, unmodified. The answer is split and both halves are recorded: the head is a good answer the rule produced unprompted (T-034 — cheapest task *and* the one guarding publication), the middle four tie on both sort keys and break on id, which puts T-032 fourth where a person would put it first. The criterion admitted both outcomes as met; the honest result was one of each. |

**What the review changed.** One thing, and it is the coverage denominator — wrong in `implement`,
corrected here, correction left visible. That is the second time this task's own arithmetic has been
falsified by running something rather than re-reading it: step 9 also overturned a written-up
expectation about the ordering, twice. Both are recorded rather than smoothed over, because a review
that only confirms is indistinguishable from one that did not look.

**What the review did not do.** It raised no new findings. Two candidates were considered and
declined as out of this phase's remit ([`review`](../plugin/skills/taskmd/docs/method/review.md) — *not an audit*): that
the status vocabulary has no value for "reviewed, awaiting children", and that an umbrella's blocked
state is derivable from its open children rather than needing a `blocked_by` written by hand. Neither
was examined during `implement`, so promoting either now would be auditing under a review heading —
and the second is a feature proposal that clause 5 would ask for a cost on. Recorded here so the next
audit finds they were considered rather than missed.

**Child fix tasks raised**
- Eight, one per finding — [T-027](T-027-give-the-design-rule-one-home.md),
  [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md),
  [T-029](T-029-reject-unknown-arguments-on-every-command.md),
  [T-030](T-030-settle-the-schema-module-s-own-entry-point.md),
  [T-031](T-031-give-the-list-rationale-one-home.md),
  [T-032](T-032-repair-the-audit-template-and-validate-templates.md),
  [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md),
  [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md).
- None raised by the review itself: every criterion is met or, in criterion 8's case, upheld by the
  task staying open.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | (no status change) | Retyped `analysis` -> `audit`, now that the shipped vocabulary has the word (T-088). `analysis` was a substitute reached for because no better value existed, and this repository never noticed it was one -- which is half of T-088's evidence. Retyped rather than left: `type` says what a task is, nothing branches on it, and leaving the workaround in place in the repository that removed it would be the clearest possible way to lose the lesson. The Log is where the history lives. |
| 2026-08-06 | (no status change) | Reviewed. Eight of the nine criteria met; the ninth — the umbrella closes only when its children resolve — is upheld by **not** closing, so the task stays open at `phase: review` with all eight children `proposed`. Status deliberately unchanged: the audit is finished, the umbrella is not, and closing it now would erase the link between the examination and its consequences (audit step 5). Review changed one thing, the coverage denominator, which was wrong in `implement` (82/8 against a real 84/5) and is corrected with the correction left visible — criterion 4 rests on it. One residual flagged for the owner rather than resolved in my own favour: F-2 names the cheaper *measure* but not the cut, and if clause 5 is read as requiring both, that row re-opens. No new findings; two candidates were declined as review-is-not-an-audit and recorded so the next audit knows they were considered. |
| 2026-08-06 | → review | Ten steps worked in order, nothing reordered. Eight findings, eleven no-action rows, eight child tasks (T-027…T-034). The eighth arrived in step 10 and is recorded as escalated rather than folded in silently: running the pre-publish check over this audit's own output showed the documented command reads only tracked files, so it had not read any of them. Two findings were proven by being made to fail rather than asserted: F-6 by building a task from the audit template and watching `check` report two classes, F-3 by running the three commands, one of which wrote the index and exited 0 on a mistyped invocation. The heaviest finding is F-2, and it is the clause-5 one: the always-loaded budget measures 147 of the 286 lines it exists to protect. Clause 5 also produced a deliberate refusal — the four-phase lifecycle was examined under the maintainer's licence to derail and dropped for lack of cost evidence (N-5). Step 9 falsified my own written-up expectation twice: the ordering put T-032 fourth rather than first, and then the eighth task changed the head of the list entirely. Both runs are recorded, because a criterion answered once and early would have concluded the wrong thing about the rule. The rule behaves as documented, so N-11 rather than a finding — the head is a good answer it produced unprompted, the middle is an id tiebreak. |
| 2026-08-06 | → planned | Ten steps. The plan's one real choice is the sequencing: the mechanical clauses run first and the purpose pass runs last, because clause 5 asks whether a design costs more than it returns and that cannot be judged before the cost is in hand — a plan opening with "is the lifecycle too heavy?" would answer from taste, which the threshold's own test forbids. Planning deliberately stops at step 6, since a large clause-5 finding would change what the child tasks are. The findings live in this task's record rather than in `tasks/_templates/audit-umbrella-template.md`: the template cannot be used as it stands, and correcting it first would be the inline fix this task may not make — so its condition is a step-5 finding and a child task corrects it. Dependencies checked: none needed, the four related tasks are correctly soft links, since a dependency edge would falsely claim the audit cannot proceed. |
| 2026-08-06 | → specified | Both open questions answered by the maintainer in one turn, so `specify` closes without a second round. The threshold is the recommendation plus a fifth clause the maintainer added: weight the purpose does not need is a finding, and a finding may derail from a stated requirement or a settled decision where that simplifies. That widened the task's own out-list — settled decisions are now examinable for cost, not shielded — and it overrides `docs/SCOPE.md` §6's "no session should re-raise them" for this audit, recorded here rather than edited there, because editing it would be a fix. Clause 5 carries its own test, since it is the clause that makes preference look like a finding. The umbrella will also report the `list` order, which puts the ordering rule under examination alongside the files; a bad order is a finding, not a failed criterion. |
| 2026-08-05 | → proposed | Requested by the maintainer for the next session. Raised as an umbrella task rather than carried in the handoff, because an audit is a task type (METHOD §5) and its scope is durable content — a handoff points, it does not store. The request's wording is quoted intact so `specify` narrows it deliberately rather than by paraphrase, and the threshold it lacks is the first open question. |
