---
id: T-059
title: Audit the whole project after the plugin restructure
type: audit
status: done
phase: review
parent: null
blocked_by: []
related: [T-026, T-006, T-053, T-047, T-004]
work_package: M1
owner: maintainer
business_value: high
effort: l
created: 2026-08-09
updated: 2026-08-09
deliverables: []
---

# T-059 — Audit the whole project after the plugin restructure

## 1. Specify

**Outcome**
A recorded examination of every tracked file in this repository, plus the gitignored working
material and the session memory, with each finding written down at a stated severity **and a stated
effort**, so the maintainer can decide which to carry before any of them is fixed.

**Requested by the maintainer, 2026-08-09**, verbatim, because the wording is the scope:

> Perform a thorough audit on the project files, including memory, all tasks, open questions and
> answered decisions, the deliverables, everything, and check inconsistencies, deprecated info,
> contradictions, inefficiencies, anti-patterns, anything that you think better change, simplify, or
> remove. Create a report in the umbrella task, and evaluate the findings based on effort and
> severity.

**Why now**
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) examined 79 in-scope files on
2026-08-06. Since then the repository has taken its largest structural change —
[T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) moved `docs/`, `taskmd/` and
the launchers into a `plugin/` subtree — and gained an entry point
([T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md)), a second platform
([T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md)) and a real install
([T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md)). A structural move is the
expensive kind of change for the same reason an amendment is: every statement that named a path is a
candidate for having quietly become false, and the ones that are not Markdown links are invisible to
`check`. The tracked tree also grew from 84 files to 130.

**Requirements served**
None directly — an audit examines conformance rather than adding to it. Its findings cite them.

**The finding threshold — inherited, not re-decided**

`audit.md` step 2 requires the threshold to be fixed **before looking**. It was not re-decided for
this audit and it was not invented after the fact: it is taken **unchanged** from
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) §1, where the maintainer set it
on 2026-08-06 before any file was opened. Stated plainly because the honest sequencing matters — this
session examined files before writing this section, so the only thing that makes the threshold
binding is that it predates the session entirely.

1. **A statement that is false or stale** — including one that was true when written.
2. **Two places that must be updated together** — a fact with more than one home, drifted or not.
3. **A consequence that contradicts a stated goal** — `docs/SCOPE.md` §1's three properties, its
   requirements, or `CLAUDE.md`'s constraints.
4. **A cost paid on every turn** — tokens, an always-loaded file, a step someone must remember.
5. **Weight the purpose does not need** — the finding must show the cost and name the cheaper thing.
   A preference with no cost attached is not a clause-5 finding.

Below the line: style and wording preference, and feature ideas nobody asked for.

**Scope**
- In: every tracked file — 130 at examination time.
- In: `control/LOCAL-CONTEXT.md`, which is gitignored and was out of T-026's denominator. It is
  resumption context, so a false statement in it costs a later session real work.
- In: the session memory at the harness's project memory path, which the request names explicitly.
  Twenty-three memory files plus their index.
- In: the open tasks' own `specify` sections, judged as live claims about current code — an open
  task's premise is not a dated record, it is what the next session will act on.
- Out: **fixing anything.** METHOD §5 and [`audit`](../plugin/skills/taskmd/docs/method/audit.md).
- ~~Out: **raising the child tasks.**~~ **Back in scope, 2026-08-09.** Deferred at first at the
  maintainer's request — *"we will decide together which one to care about"* — and returned by their
  answer, *"let's make them all"*, given after reading the sixteen findings and the triage. So
  [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 4 is performed after all, one turn later than
  usual, with the finding set approved rather than assumed. The deferral is struck through rather
  than deleted: it is the reason the children were raised in a second pass, and a reader of the
  triage table should be able to see that the ordering was agreed before the tasks existed.
- Out: `reference/`, prior art from another project, on T-026's precedent. Examined for whether
  anything in the live tree depends on it — see N-5.
- Out: closed task records as *copies*. A dated account of a decision is not a live claim to keep in
  step; this is T-026's own ruling and it is not reopened.

**Inputs**
[`audit.md`](../plugin/skills/taskmd/docs/method/audit.md); `docs/SCOPE.md`; `CLAUDE.md`;
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) for the threshold and the
deduplication baseline; `taskmd list --json` for the graph.

**Acceptance criteria**
- [ ] Every finding cites the threshold clause it meets
- [ ] Every finding carries **both** a severity and an effort, on the schema's own vocabularies, so
      a child task can carry them unchanged
- [ ] Every finding that asserts a defect in behaviour is **proven by running something**, not by
      reading code — `CLAUDE.md` *Verifying*
- [ ] Every area in scope is recorded as examined, including areas that produced no finding
- [ ] Nothing is fixed in place — falsified by any change outside this task's own record and the
      regenerated index
- [ ] Findings already carried by an open task are deduped rather than re-raised, and the dedupe is
      recorded
- [ ] The pre-publish check prints nothing, and prints exactly the five fixture lines without its
      exclusion — run **after** this record is written, with no matched line quoted into it

**Open questions**
- ~~**Which findings become child tasks?**~~ **Answered by the maintainer on 2026-08-09: all
  sixteen.** Given after the findings and the triage were put to them, so the approval is of a set
  they had seen rather than of a promise. One shape offered in the triage table was **not** taken:
  folding F-11…F-16 into a single housekeeping task. Sixteen findings therefore became sixteen
  tasks, one to one, which is what [`audit.md`](../plugin/skills/taskmd/docs/method/audit.md) step 4 asks for and
  what keeps each finding traceable to its own fix. The two that will almost certainly be worked
  together — [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) and
  [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md), same function — carry a soft edge
  saying so rather than being merged.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Build the coverage denominator from `git ls-files` before looking at anything | The §3 coverage table |
| 2 | Read the live spine: `CLAUDE.md`, `docs/`, `plugin/docs/`, the skill, the config | Observations |
| 3 | Read the code and run it — every behavioural claim tested against the tool rather than the source | Observations, each with the command's real output |
| 4 | Read the tracker content: 58 task files, both templates, the generated index | Observations |
| 5 | Read the two areas T-026 never covered: `control/`, and the session memory | Observations |
| 6 | Cross-cutting sweeps no single-file reading can see: references escaping the plugin boundary, facts with more than one home, the always-loaded budget | Observations |
| 7 | Classify — clause, severity, effort — and dedupe against the eleven open tasks | The findings table |
| 8 | Validate: `check`, `index`, the suite under both runners, then the pre-publish check last | The §3 transcripts |

**Sequencing.** Step 3 is where the yield is, and it is placed after step 2 for one reason: a
behavioural test is only a finding when a document claims otherwise, so the claims have to be in hand
first. Step 6 is last of the reading steps because the boundary sweep needs the whole tree.

**Severity says who pays and when**, unchanged from T-026: **High** — costs work now, or costs a
release if it survives into [T-006](T-006-package-document-and-publish.md); **Medium** — will cost
work, at a time not of anyone's choosing; **Low** — costs work only when someone next touches that
file.

**Effort is the schema's own `effort` vocabulary** (`xs`…`xl`), so a finding promoted to a child task
carries its estimate unchanged instead of being re-estimated by whoever writes the task. That is the
one thing this audit does that T-026's did not, and it is the maintainer's request.

## 3. Implement

Worked in plan order. Nothing was reordered.

### Decisions & assumptions

- **The threshold was inherited rather than re-decided** — 2026-08-09. Re-deciding it after looking
  would have produced a threshold shaped to the findings, which is the failure `audit.md` step 2
  names. Inheriting T-026's is the only option that keeps it prior to the examination. The cost is
  that this audit cannot claim a threshold tuned to what changed since; it is the same instrument
  pointed at a larger tree.
- **An open task's `specify` section is judged as a live claim, a closed one's is not** — 2026-08-09.
  T-026 excluded task records from the duplication findings because a record is a dated account. That
  reasoning covers *closed* tasks. An open task's premise is what the next session will act on, so a
  premise the code has since falsified costs real work — which is F-9, and it would have been
  invisible under the wider reading.
- **Child tasks were not raised.** The maintainer asked to decide the set together. Recorded as a
  scope deviation above rather than absorbed silently.
- **Nothing was fixed.** The only tracked files this task changes are its own record and the
  regenerated `tasks/README.md`. Every probe was built in the session scratchpad, outside the
  repository, and the one temporary edit made to `tasks/README.md` while reproducing N-2 was reverted
  and confirmed by `git status` before anything else ran.

### Step 1 — coverage

Every tracked file from `git ls-files`, assigned to exactly one area. **130 tracked files**; 5 are
`reference/`, out of scope, leaving **125 in scope**. Two areas outside the tracked tree are added
because the request names them.

| Area | # | Examined | Findings |
| :--- | ---: | :---: | :--- |
| Root config + `CLAUDE.md` (`.gitignore`, `.gitattributes`, `LICENSE`, `.claude/settings.json`, `.claude-plugin/marketplace.json`, `.handoff/config.md`, `CLAUDE.md`) | 7 | yes | F-6, F-12, F-15 — N-9 |
| `docs/` — `SCOPE.md`, `BRIEF.md` | 2 | yes | none |
| `plugin/docs/` — `METHOD.md`, `BINDING.md` | 2 | yes | F-1 |
| `plugin/docs/method/` | 7 | yes | none — N-10 |
| `plugin/docs/bindings/` | 2 | yes | F-4, F-16 |
| `plugin/skills/taskmd/` — `SKILL.md`, `adopt.md` | 2 | yes | F-14 |
| `plugin/taskmd/` — the code | 5 | yes | F-1, F-5, F-7, F-8 |
| `plugin/taskmd/defaults/config.md` | 1 | yes | F-1, F-5, F-8 |
| `plugin/` — `taskmd.sh`, `taskmd.ps1`, `plugin.json` | 3 | yes | F-3 |
| `plugin/bin/` | 2 | yes | F-3, F-10 |
| `tests/` — four suites | 4 | yes | F-10, F-11 |
| `tests/fixtures/` | 27 | yes | F-7 — N-6 |
| `tasks/` — 58 task files | 58 | yes | F-9 — N-7 |
| `tasks/_templates/` | 2 | yes | F-2 |
| `tasks/README.md` — generated | 1 | yes | none — N-11 |
| **In scope, tracked** | **125** | | |
| Out of scope | `reference/` — 5 | no | prior art — N-5 |
| **Tracked total** | **130** | | |
| *Added by the request* — `control/LOCAL-CONTEXT.md` (gitignored) | 1 | yes | F-13 |
| *Added by the request* — session memory, 23 files + index | 24 | yes | none — N-8 |

Untracked-but-not-ignored files a push would send: **none**. `.pytest_cache/` self-excludes through
its own generated ignore file, so this repository's protection does not depend on a global excludes
file — the negative finding recorded in `control/LOCAL-CONTEXT.md` about a sibling plugin does not
apply here.

### Steps 2–7 — findings

Every row cites the clause it meets. Severity is defined in §2; effort is the schema's vocabulary.

| # | Area | Clause | Finding | Sev | Effort |
| :-- | :--- | :---: | :--- | :---: | :---: |
| **F-1** | Plugin boundary | 1, 3 | **The plugin ships prose citing documents it does not ship.** Inside `plugin/`: 19 `R-NN` citations, 5 references to `docs/SCOPE.md`, 4 to a numbered non-goal, and one to `../CLAUDE.md` — none of which an adopter receives. `plugin/docs/BINDING.md:193`'s `../CLAUDE.md` is broken **inside this repository too**: from `plugin/docs/` it resolves to `plugin/CLAUDE.md`, which has never existed. The worst carrier is `plugin/taskmd/defaults/config.md`, which `adopt.md` step 2 tells every adopter to **copy** into their own project — so five dangling citations are copied forward on adoption. T-053's replacement criterion swept `plugin/` for **links** that escape; every one of these is backticked prose, so the referential-closure claim is narrower than it reads and was never false. | High | m |
| **F-2** | Templates | 1 | **Both task templates point at paths that stopped existing at T-053.** `task-template.md:20-21` names `docs/METHOD.md` and `taskmd/defaults/config.md`; `audit-umbrella-template.md:28` names `docs/METHOD.md`. `docs/` now holds only `SCOPE.md` and `BRIEF.md`. Templates are copied into every new task, so this propagates. `check` cannot see it twice over: the references are prose inside an HTML comment rather than links, and `load_tasks` skips `_`-prefixed folders. Not covered by [T-032](T-032-repair-the-audit-template-and-validate-templates.md), which predates the move and whose scope is the *audit* template's schema defects — this also hits `task-template.md`. | High | xs |
| **F-3** | Launchers | 1, 3 | **`plugin/taskmd.sh` fails whenever `PYTHONPATH` is already set to anything that is not a POSIX-absolute path.** Proven by running it under five environments: unset, a POSIX-absolute path, and a `/c/…`-style path all print the normal `check` output; a **relative** value and a **Windows-style** value both produce `No module named taskmd` and exit 1, with an error naming the user's Python executable rather than taskmd. Cause: the launcher hardcodes `:` as the separator and hands Python a POSIX `$here`, which only works because the Windows shell layer rewrites the whole variable — and it abandons the rewrite as soon as one element is not POSIX-absolute. `taskmd.ps1` uses `[IO.Path]::PathSeparator` and is unaffected; `plugin/bin/taskmd` delegates to `taskmd.sh` and inherits it. Hidden by `test_the_shell_launcher_produces_what_the_module_produces`, which runs the launcher under whatever environment the runner happens to have. R-18's "thin launcher" and R-20's identical behaviour both bite here, and `CLAUDE.md` itself tells a reader that `python -m taskmd` needs `PYTHONPATH` set — advice that, followed and left in place, breaks the launcher. | High | s |
| **F-4** | Binding vs code | 1, 3 | **`check` silently drops one of two tasks that claim the same id.** Proven on a three-file project: `OK - 2 task(s)`, exit 0, and `list` shows only the file that sorted last. `load_tasks` assigns into a dict keyed by id, so walk order decides which task exists; the loser vanishes from the index, from `list`, and from every derived edge with no signal anywhere. `plugin/docs/bindings/local-markdown.md` *find* states the opposite in terms: *"two files claiming one id are a conflict rather than a coin toss"*. This is also the answer the implementation currently gives to [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md)'s open merge-conflict question — silent data loss — and two branches picking the same number is the predicted route to it. `check` has no duplicate-id class. | High | s |
| **F-5** | Schema config | 1 | **Pass-through fields are carried but displayed by no documented command.** `plugin/taskmd/defaults/config.md` says a field the schema does not name is *"carried and **displayed**, never interpreted. That is what lets a project adopt taskmd without first rewriting its task files."* Proven: a task carrying two unknown fields shows them in **none** of `context`, `index`, `list` or `list --json`. The only code that prints them is `taskmd.schema`'s `main()`, which is undocumented and which [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) has already decided to remove — so the claim is true today only through a doorway nobody is told about, and false outright once T-030 lands. The adoption argument rests on this sentence. The accurate statement is cheap and already works: carried, and **displayable** by naming the field in `context_fields` or `index_columns`. | Medium | xs |
| **F-6** | Tier 1 | 1, 4 | **`CLAUDE.md`'s tier-1 rule names a measurement that cannot see the member the rule just added.** The file declares tier 1 to be *"this file **plus the taskmd `description`**"*, then states that both sides are counted by `wc -l CLAUDE.md reference/TASK-WORKFLOW.md` — which counts the file alone. Measured now: **164 against 173**, so 9 lines of margin by the named command; the description is a further 397 characters, ≈5 lines at this file's 83-character average, leaving ≈4. [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) owes tier 1 a further 26 lines. Deduped: T-047 owns the move and the cut. What is new is that the rule's own check is blind to a declared member, and that tier 1 has grown **153 → 164** since T-047's last recorded measurement on 2026-08-08 — widening its gap from six lines to roughly seventeen, which changes what that task has to find room for. | High | s |
| **F-7** | Tool | 1, 3 | **`check`'s nested-project exclusion does not apply one directory below the root.** Proven: a project at `<root>/inner` holding its own tasks folder had its broken link reported as the host project's. `markdown_files()` guards with `base != root`, so at the top level of the walk a nested project is never skipped. `tests/fixtures/README.md` states the exclusion with no depth caveat — *"`check` skips a nested project … so the host repository does not report the defects these exist to hold"* — and it has never shown here because every fixture sits two levels down. It bites an adopter whose repository holds a sub-project at the top level. | Medium | s |
| **F-8** | Tool + config | 4, 5 | **`work_package` is a column of dashes in every view, on all 58 tasks.** The shipped default names it in both `context_fields` and `index_columns`; every task in this repository carries `work_package: none`, so the generated index holds a 58-row column of `-` and every `context` call prints `work_package -` in its header. `index_block()` already implements the opposite rule and states it: *"a project with no hierarchy should not read a column of dashes"* — and applies it to **edge** columns only. Same principle, half applied. Cheaper thing: derive field columns from the data as edge columns already are, or drop the key from the shipped defaults. Paid on every `context` and by every reader of the index. | Medium | s |
| **F-9** | Open tasks | 1 | **Two open tasks rest on a symptom that T-011 removed.** [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) exists to stop config errors printing an absolute install path, and [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) cites the same string on the success path. Proven on an external project with no config: the error reads `CONFIG ERROR  taskmd/defaults/config.md: …` and the schema entry point prints `schema   taskmd/defaults/config.md` — machine-independent, no absolute path. `_display()` landed in commit 580d22b (T-011), after both tasks were raised. So T-023's criterion 1 is already met, its criterion 4 (*shown failing on a fixture*) cannot be met because nothing fails, and what actually remains is the maintainer's 2026-08-07 wording choice — `<shipped default>` — which their answer preferred over precisely the string the code now prints. T-030's decision to remove the entry point is unaffected; only its evidence is stale. | Medium | xs |
| **F-10** | Tests | 3 | **The adopter's entry point is covered by no test.** `plugin/bin/taskmd` and `plugin/bin/taskmd.cmd` are what T-053 raised as `critical` — *"the adoption path not working at all"* — and what the skill names. The `Launchers` class covers `taskmd.sh` and `taskmd.ps1` only, and so does the no-logic assertion. The one test that reaches `bin/taskmd` checks its recorded mode bit and nothing else. Renaming or deleting either file leaves the suite green and every adopter broken; F-3 already reaches `bin/taskmd` through the delegation and no test saw it. | Medium | s |
| **F-11** | Tests | 1 | **`test_no_command_explains_the_three` asserts three of the four commands.** Name and body both predate `list` (T-022): the loop covers `context`, `index`, `check`. A regression that dropped `list` from the usage line passes. The sibling test that pins the *name* the usage line prints (T-055) reads it out of `SKILL.md` rather than hardcoding it — the same treatment applied here would read the command set from `cli.COMMANDS`. | Low | xs |
| **F-12** | Packaging | 2 | **The product description and the version each have more than one home.** `description` is byte-identical in `.claude-plugin/marketplace.json`'s plugin entry and `plugin/.claude-plugin/plugin.json`; a third, differently-worded copy sits in the same marketplace file's `metadata.description` and a fourth in `plugin/taskmd/__init__.py`. `version: 0.1.0` is written in both manifests and must move together at every release — the first release is [T-006](T-006-package-document-and-publish.md). Whether the marketplace entry may omit either field is a harness question to **check** rather than assume, which is why this is small rather than trivial. | Low | xs |
| **F-13** | Local context | 1 | **`control/LOCAL-CONTEXT.md` still says non-goal 11 keeps the CLI to three commands.** Stale since the 2026-08-05 amendment (T-022) that carved out `list`. The identical sentence was corrected in `CLAUDE.md` and `.handoff/config.md` at the time and this copy was missed because the file is gitignored and outside every sweep. No publishing risk; it is resumption context, and it is the only file in the tree that still states the superseded surface. | Low | xs |
| **F-14** | Skill | 2 | **`SKILL.md` and `local-markdown.md` carry the same sentence verbatim** — *"taskmd never writes a task file, so the edit that made the index stale is one it never saw"* — two lines after `SKILL.md` points the reader at the binding for exactly this. R-22 says the skill points at the tool rather than restating what it enforces, and this is the one place it does not. Both are shipped, so the two copies travel together to every adopter. | Low | xs |
| **F-15** | Packaging | 3 | **The marketplace source has never been exercised by any route but a local directory.** `.claude-plugin/marketplace.json` declares `"source": "./plugin"`. T-053 **D4** recorded `git-subdir` as the mechanism that makes a subtree installable for anyone who is not the maintainer, and the manifest declares no such source. The only install ever performed is the maintainer's local-directory one (T-053's log). Deduped against T-006 criterion 4, *"installs from a clean clone on a machine that has never seen it"*, which owns the verification — recorded here so that criterion knows the specific thing to run rather than discovering it at publication. **Verify first; it may need no fix.** | Medium | s |
| **F-16** | Binding vs code | 1 | **`id_width` is not enforced when tasks are read.** `Schema.is_id` matches `<prefix>` plus any run of digits, so a task carrying an over-wide id is accepted under `id_width: 3` — proven alongside F-4. `local-markdown.md` *enumerate* says to keep the files *"whose `id` field matches the configured prefix **and width**"*. The consequence is mild on its own, and it is in the same function and the same fix as F-4, which is the reason to record it rather than to leave it for a later reader to rediscover separately. | Low | xs |

### Triage — by severity, then effort

The order the maintainer asked for. Within a severity band, cheapest first.

| Order | Finding | Sev | Effort | One-line reason to do it in this position |
| :--: | :--- | :---: | :---: | :--- |
| 1 | **F-2** templates name dead paths | High | xs | Cheapest High in the set, and it propagates into every task created before it is fixed |
| 2 | **F-3** launcher breaks on an inherited `PYTHONPATH` | High | s | The only finding that makes the tool fail outright, for the reader most likely to have a `PYTHONPATH` — a Python developer |
| 3 | **F-4** duplicate ids silently drop a task | High | s | Silent data loss, and it answers T-004's open merge question in the worst way |
| 4 | **F-6** tier-1 rule cannot see its own member | High | s | Blocks T-047 from being sized against anything real |
| 5 | **F-1** plugin cites what it does not ship | High | m | Costs a release if it survives into T-006; the largest of the High set |
| 6 | **F-5** pass-through fields never displayed | Medium | xs | One sentence, and the adoption argument rests on it |
| 7 | **F-9** two open tasks rest on a removed symptom | Medium | xs | Two `specify` sections; cheap, and it stops a session hunting a defect that is gone |
| 8 | **F-15** git install route unproven | Medium | s | Verify before fixing — it may cost nothing, and T-006 needs the answer either way |
| 9 | **F-10** adopter entry point untested | Medium | s | Would have caught F-3 |
| 10 | **F-7** nested-project exclusion misses depth 1 | Medium | s | Real for a monorepo adopter, invisible here |
| 11 | **F-8** `work_package` column of dashes | Medium | s | Paid on every turn, but it is a design call rather than a defect |
| 12–16 | **F-11, F-12, F-13, F-14, F-16** | Low | xs | Five one-line fixes; sensible to carry as a single housekeeping task if the maintainer prefers |

Two observations about the shape of this list, offered because they are the parts a table cannot say:

- **Five of the sixteen findings are consequences of one event.** F-1, F-2 and F-9 all exist because
  the T-053 restructure moved files that non-link prose still names, and F-15 because the packaging
  it produced has only been installed one way. The restructure was verified thoroughly by the one
  instrument that could see it — `check`, which failed four times on the way — and every escape it
  could not see is prose. That is the generalisable finding underneath: **this project's validator
  reads links, and its documents cite by backtick.**
- **Three findings are the same defect at different altitudes**: F-3, F-10 and F-11 are all "the
  thing an adopter runs is the thing least covered by the suite". Fixing F-10 first would have found
  F-3 for free.

### Examined, no action

The evidence that an area was looked at. Without these a reader cannot tell "checked and clean" from
"not looked at" ([`audit.md`](../plugin/skills/taskmd/docs/method/audit.md)).

| # | Observation | Why no action |
| :-- | :--- | :--- |
| **N-1** | No `README.md` at the repository root, though R-15 and §9 both say the measured saving is *"stated in the README"*. | Owned by [T-006](T-006-package-document-and-publish.md) and deliberately deferred there. Unchanged since T-026 recorded the same row. |
| **N-2** | `check` does not notice a stale generated index. **Re-proven today** rather than assumed: a hand-edited title inside the generated block left `check` reporting OK and exiting 0. The working tree was restored and confirmed clean before anything else ran. | Already [T-025](T-025-let-check-notice-a-stale-generated-index.md). Re-raising it would double-count; the reproduction is recorded because a two-day-old failure claim is worth re-running when it is this cheap. |
| **N-3** | `tasks_dir` naming a **file** still reports *"the project root has no such folder"* and advises creating a name already taken. Reproduced today. | Already [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md). |
| **N-4** | `check`, `index` and `context` still discard unknown arguments in silence — `taskmd check nonsense` exits 0. Reproduced today. `--help` still exits 2, which T-029 has in scope. | Already [T-029](T-029-reject-unknown-arguments-on-every-command.md). |
| **N-5** | `reference/` — 5 files. Out of scope by T-026's precedent. One dependency noted: `reference/TASK-WORKFLOW.md` is the **denominator of the tier-1 budget**, so pruning `reference/` before publication would delete the bound `CLAUDE.md` measures against. | Not raised. No prune is planned, and [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) with T-028 own the budget. Recorded so that a later decision to drop `reference/` meets this fact rather than discovering it. |
| **N-6** | `tests/fixtures/` — 27 files. Each `broken-*` still holds exactly one defect; spot-checked against the README table. The suite is **116 passed** under `pytest` and **116 OK** under the documented `python -m unittest discover -s tests`. | Examined, clean. The two runners agree, which is worth stating because both appear in the project's own records. |
| **N-7** | [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) is `done` with an entirely empty `## 2. Plan` table — the only closed task carrying an untouched template section. This is exactly the gap `local-markdown.md` names: `check` returns OK on a `done` task whose sections are still the template. | **No action.** The record of what happened is that the decision was taken without a written plan; back-filling one now would fabricate history, which is worse than the gap. One instance in 39 closed tasks is not a systemic failure. Recorded so the next audit finds this was decided rather than missed. |
| **N-8** | Session memory — 23 files, index consistent at 23/23, nothing stale. Two overlap: `an-interpreter-on-path-may-not-run` restates the substance of `powershell-5-1-drops-empty-string-arguments` before linking to it. | Below the line. A memory that carries the trap inline is what makes it useful at the moment someone is writing a launcher, and the summary-is-a-copy rule is aimed at documents that drift, not at two lessons learned in the same hour. Separately: F-3 is a new instance of `git-bash-converts-argv-paths-not-embedded-ones` at the environment-variable level, and is worth a memory **after** F-3 is fixed, not before. |
| **N-9** | `.gitignore`, `.gitattributes`, `LICENSE`, `.claude/settings.json`. | Examined, no finding. `.gitattributes` still pins `eol=lf`, which is what makes the byte-identical claim meaningful; `.claude/settings.json` carries a relative marketplace path and no machine data (T-052). |
| **N-10** | `plugin/docs/METHOD.md` and `plugin/docs/method/` — 8 files. Every internal link resolves, the spine names no project file, and §3's split between rules that bind before task work and rules that do not is intact. | Examined, no finding. The escaping citations are in `BINDING.md` and the code, not here — which is F-1's boundary, correctly drawn. |
| **N-11** | `tasks/README.md` regenerated: no diff. The index is current. | Examined, clean. |

### Step 8 — validation

```
python -m pytest tests -q
116 passed in 1.41s

python -m unittest discover -s tests
Ran 116 tests in 1.206s
OK

taskmd check
OK - 58 task(s), vocabulary valid, references resolve, no broken links

taskmd index
Wrote tasks/README.md - 19 active, 39 closed
```

**Four findings were proven by making something fail**, per `CLAUDE.md` *Verifying*, on projects built
in the session scratchpad outside this repository:

```
F-3   PYTHONPATH unset            OK - 58 task(s), ...              exit 0
      PYTHONPATH=<relative>       ...: No module named taskmd       exit 1
      PYTHONPATH=<posix abs>      OK - 58 task(s), ...              exit 0
      PYTHONPATH=<windows abs>    ...: No module named taskmd       exit 1

F-4   three task files, two claiming one id
      taskmd check                OK - 2 task(s), ...               exit 0
      taskmd list                 shows only the file that sorted last

F-5   a task carrying two fields the schema does not name
      context / index / list / list --json   none of the four printed either field

F-7   a project holding its own tasks folder one level below the root
      taskmd check   BROKEN LINK   inner/tasks/T-001-b.md -> ./nope.md    exit 1
```

The F-3 lines are transcribed with the path values described rather than reproduced: the failing
output names a Python executable under a home directory, and quoting it would put a real absolute
path into this record — the mistake T-013 and T-018 each made once.

**Escalated, not absorbed.** Nothing was found after the findings table was written. The one thing
that changed during the run is recorded above rather than smoothed over: N-2's reproduction required
a temporary edit to a tracked generated file, which was reverted and verified clean before the record
was written.

### Step 9 — the child tasks, added 2026-08-09 after approval

One task per finding, sixteen in all, each carrying `parent: T-059`, the finding id it comes from,
the threshold clause it met, and the severity and effort **unchanged** from the table above — which
is the whole point of estimating them here: nobody re-estimates on the way into a task.

**Ids were assigned in triage order.** The ordering rule sorts on effective value, then effort, then
id, so the id tiebreak makes `list` reproduce the agreed triage instead of an arbitrary permutation
of the ties. Run over the children, unmodified:

```
taskmd list --parent T-059 --open
T-060   proposed  -  specify  Point the task templates at paths that exist
T-061   proposed  -  specify  Stop an inherited PYTHONPATH breaking the shell launcher
T-062   proposed  -  specify  Report two tasks claiming one id instead of dropping one
T-063   proposed  -  specify  Measure the tier-1 member the rule declares
T-064   proposed  -  specify  Stop the plugin citing documents it does not ship
T-065   proposed  -  specify  Say what happens to a field the schema does not name
T-066   proposed  -  specify  Reconcile two open tasks with the fix that already landed
T-067   proposed  -  specify  Prove the install route an adopter actually takes
T-068   proposed  -  specify  Cover the entry point an adopter runs
T-069   proposed  -  specify  Skip a nested project at any depth, not below the first
T-070   proposed  -  specify  Decide whether an unused field column is shown at all
T-071   proposed  -  specify  Let the usage test assert every command there is
T-072   proposed  -  specify  Give the plugin's description and version one home each
T-073   proposed  -  specify  Correct the command surface local context still states
T-074   proposed  -  specify  Let the skill point where it currently restates
T-075   proposed  -  specify  Enforce id width when a task file is read
```

**The rule reproduced the triage exactly**, which is a weaker result than it looks and is worth saying
so: with ids assigned in triage order, agreement was arranged rather than discovered. What it does
show is that the severity-and-effort estimates and the hand triage do not *contradict* each other —
had they, the ranks would have reordered the ids regardless. T-026's step 9 recorded the same rule
producing a genuinely unprompted answer on tasks nobody had sorted; this run cannot make that claim
and does not.

**Three findings were carried without being fixed on the way past.** F-9's whole content is that two
open tasks state something false about the code — the temptation to correct those two sentences while
raising [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) was the inline fix METHOD
§5 forbids, and it was not taken. T-023 and T-030 still read exactly as they did.

**Outputs produced**
- `tasks/T-059-…md` — this record: the coverage table, sixteen findings, a triage ordering, eleven
  no-action rows and the transcripts
- `tasks/T-060` … `tasks/T-075` — one task per finding
- `tasks/README.md` — regenerated

The `deliverables:` field stays empty. The only outputs are this record and a generated file;
declaring the record inside itself adds a self-reference that nothing reads, which is the reason
T-026 left it empty too.

## 4. Review

Done 2026-08-09, in the session that also worked all sixteen children through their own lifecycles.
The criterion this phase was waiting on — that each actionable finding has its own child task — is
answerable now: the set exists, and every one of the sixteen is `done`.

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every finding cites the threshold clause it meets | met | All sixteen rows in §3 carry a clause. The threshold was inherited from T-026 rather than re-decided, which is what makes it prior to the examination — recorded in §1 rather than claimed |
| Every finding carries **both** a severity and an effort, on the schema's own vocabularies | met | And it paid off exactly as intended: all sixteen child tasks took both estimates unchanged, so nobody re-estimated on the way into a task |
| Every finding that asserts a defect in behaviour is **proven by running something** | met | Four proven by making something fail, on scratch projects outside the repository. Each was **re-run** by its child task before any fix — F-3, F-4, F-5 and F-7 all reproduced independently, and none had gone stale |
| Every area in scope is recorded as examined, including areas that produced no finding | met | The §3 step 1 coverage table: 125 in-scope tracked files, plus `control/` and 24 memory files, plus eleven no-action rows |
| Nothing is fixed in place | met | Falsifiable and not falsified: the only tracked files this task changed are its own record and the regenerated index. T-023 and T-030 still stated F-9's falsehood when this audit closed, and were corrected later by T-066, which is the task raised for it |
| Findings already carried by an open task are deduped rather than re-raised, and the dedupe is recorded | met | Four dedupes recorded — N-1 to T-006, N-2 to T-025, N-3 to T-024, N-4 to T-029 — plus F-6 against T-047 and F-15 against T-006 within the findings themselves |
| The pre-publish check prints nothing, and prints exactly the five fixture lines without its exclusion | met | At close, and re-run after every child task since: silent with the exclusion, exactly five lines without |

**What the child tasks changed about the audit's own conclusions**, recorded because a review that
only ticked its criteria would lose it:

- **F-6 understated the problem.** It reported tier 1 as passing with a blind measurement.
  [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) measured both units and found the
  rule **fails** — 12,203 characters against 7,919 — because a line count flatters a dense document.
  The audit's finding was right that the check was blind; it did not know the answer was on the
  other side of the bound.
- **F-1 undercounted.** Nineteen requirement citations at examination time, twenty-one by the time
  [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) swept — three arrived from
  this same session's earlier tasks. That is the strongest argument for the sweep being a test, and
  it came from the fix rather than from the finding.
- **F-15 resolved to "no change needed."** The manifest installs by the git route exactly as
  written; what [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) found instead is
  that the *directory* route accumulates files that are in no clone.

**Child fix tasks raised**
- Sixteen, all `done`. Three further tasks were raised **by** the children rather than by this
  audit, under METHOD §3.3: [T-076](T-076-decide-what-a-template-s-links-resolve-against.md),
  [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) and
  [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md). They are not this umbrella's children — an
  audit's children are its findings, and these are discoveries from the work of fixing them.

**Child fix tasks raised**
- Sixteen, one per finding, listed with their findings in §3 step 9:
  [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) (F-2),
  [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) (F-3),
  [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) (F-4),
  [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) (F-6),
  [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) (F-1),
  [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) (F-5),
  [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) (F-9),
  [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) (F-15),
  [T-068](T-068-cover-the-entry-point-an-adopter-runs.md) (F-10),
  [T-069](T-069-skip-a-nested-project-at-any-depth.md) (F-7),
  [T-070](T-070-decide-whether-an-unused-field-column-is-shown.md) (F-8),
  [T-071](T-071-let-the-usage-test-assert-every-command-there-is.md) (F-11),
  [T-072](T-072-give-the-description-and-version-one-home-each.md) (F-12),
  [T-073](T-073-correct-the-command-surface-local-context-states.md) (F-13),
  [T-074](T-074-let-the-skill-point-where-it-currently-restates.md) (F-14),
  [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) (F-16).

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-09 | (no status change) | Retyped `analysis` -> `audit`, now that the shipped vocabulary has the word (T-088). `analysis` was a substitute reached for because no better value existed, and this repository never noticed it was one -- which is half of T-088's evidence. Retyped rather than left: `type` says what a task is, nothing branches on it, and leaving the workaround in place in the repository that removed it would be the clearest possible way to lose the lesson. The Log is where the history lives. |
| 2026-08-09 | → done | `review` completed and the umbrella closed, in the session that worked all sixteen children through their own lifecycles. All seven criteria met. Three of them could only be judged now: *each actionable finding has its own child task* needed the set to exist, *nothing is fixed in place* is only falsifiable once the fixes have happened elsewhere, and the four behavioural findings were each **re-run** by their own child task before being fixed — none had gone stale. What the review records beyond the ticks is where the children corrected the audit: F-6 understated the problem (tier 1 does not merely have a blind check, it **fails** the bound once measured in characters), F-1 undercounted by three because this same session added citations to the files it was about, and F-15 resolved to *no change needed* while turning up that the directory install route accumulates files no clone contains. Three tasks raised **by** the children under METHOD §3.3 — T-076, T-077, T-078 — are deliberately not children of this umbrella: an audit's children are its findings. |
| 2026-08-09 | (no status change) | **All sixteen findings approved by the maintainer and raised as T-060…T-075**, one per finding, each carrying its severity and effort from the findings table unchanged — which is what estimating them in the umbrella was for. The one shape offered and not taken was folding the five `low`/`xs` rows into a single housekeeping task; one-to-one keeps each finding traceable to its own fix, and the two that will be worked together (T-062 and T-075, same function) carry a soft edge instead of being merged. Ids were assigned in triage order so the ordering rule reproduces the agreed sequence through its id tiebreak — recorded in §3 step 9 as a *weaker* result than T-026's step 9, because agreement arranged this way is not agreement discovered. Nothing was fixed on the way past: T-023 and T-030 still state the falsehood F-9 is about, since correcting them here is the inline fix METHOD §5 forbids and T-066 is the task that does it. `specify` §Scope's deferral is struck through rather than deleted, so a reader can see the triage was agreed before the tasks existed. The umbrella stays open at `review` with sixteen children `proposed`. |
| 2026-08-09 | → review | Audited 125 in-scope tracked files, plus `control/LOCAL-CONTEXT.md` and 24 memory files the request added and T-026's denominator never held. Sixteen findings, five High, and eleven no-action rows. The threshold was **inherited unchanged** from T-026 rather than re-decided, because this session had already read files before the write-up and only a threshold that predates the session can be prior to the examination. Four findings were proven by making something fail on scratch projects outside the repository: an inherited `PYTHONPATH` makes the shell launcher unable to find its own package; two files claiming one id leave `check` reporting OK while one task silently disappears; a field the schema does not name is displayed by none of the four commands, against a config that says it is; and `check` reports a nested project's defects as its own when that project sits one directory below the root. The structural finding underneath five of the sixteen is that **the validator reads links and the documents cite by backtick** — every escape T-053's restructure left behind is prose, which is precisely the class `check` was never built to see. Child tasks were **not** raised: the maintainer asked to choose the set together, so this umbrella stops one step short of `audit.md` step 4 and stays open. Nothing was fixed; the only tracked changes are this record and the regenerated index. |
