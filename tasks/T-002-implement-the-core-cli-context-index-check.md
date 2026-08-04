---
id: T-002
title: Implement the core CLI: context, index, check
type: deliverable
status: review
phase: implement
parent: null
blocked_by: [T-001]
related: [T-008, T-004]
work_package: none
owner: maintainer
created: 2026-08-04
updated: 2026-08-05
deliverables:
  - taskmd/cli.py
  - taskmd/__main__.py
  - taskmd/schema.py
  - taskmd/defaults/config.md
  - tests/test_cli.py
  - tests/fixtures/README.md
  - tests/fixtures/broken-vocabulary
  - tests/fixtures/broken-dangling
  - tests/fixtures/broken-missing-blocker
  - tests/fixtures/broken-cycle
  - tests/fixtures/broken-link
  - tests/fixtures/broken-derived-field
  - tests/fixtures/broken-deliverable
  - tests/fixtures/broken-config
---

# T-002 — Implement the core CLI: context, index, check

## 1. Specify

**Outcome**
A dependency-free CLI providing `context`, `index` and `check`, driven by the schema decision from T-001.

**Why this one**
These three carry the plugin's whole thesis: `context` is the token saving, `index` is the derived view that removes drift, `check` validates what is left hand-made. `reference/task.py` proves the behaviour — it is evidence, not code to lift.

**Requirements served**
R-12, R-15, R-16, R-17, R-20 (`docs/SCOPE.md`).

**Inputs**
`taskmd/schema.py` and `taskmd/defaults/config.md` (the schema, settled in T-001);
`docs/METHOD.md` §2 and §4 (phase/status independence, the three edge kinds);
`reference/task.py` and `tools/tasks/task.py` as evidence of behaviour that already works.

**Acceptance criteria**
- [ ] Runs on a clone with no configuration and no dependencies
- [ ] `index` regenerates without touching hand-written regions
- [ ] `check` proven **failing** on every class in *What `check` claims to catch*, below
- [ ] Output byte-identical across Windows, macOS and Linux (`newline` set explicitly)
- [ ] Console output survives a cp1252 terminal
- [ ] **Configuration problems are reported when the config is read, not mid-command** (R-17) — a
      bad key, a missing file or an unresolvable reference fails at setup, never inside a task the
      user is trying to finish
- [ ] Reads the schema through `taskmd/schema.py`, holding no field name or status value of its own
- [ ] **The id format comes from config** (`id_prefix`, `id_width`) and is never hardcoded, so the
      defaults and the scale ceiling remain T-004's to settle without reopening this task
- [ ] **`context`'s `NEXT:` hint reads phase *and* status** (R-3) — proven on a task whose status has
      moved past its phase, where the current tool tells you to redo the phase you just finished
- [ ] **The `context` saving is measured on a real case** and the before/after byte counts recorded
      in `## 3. Implement` (R-15). Stating the number in the README is T-006's.

**What `check` claims to catch**

Enumerated here so the criterion above is falsifiable before implementation starts: an
implementation cannot quietly shrink the claim to whatever proved easy. Each must be demonstrated
failing on a fixture that contains it.

| # | Class | The case that must fail |
| :-- | :--- | :--- |
| 1 | Bad enumerated value | A field carries a value outside its vocabulary row |
| 2 | Dangling reference | An edge points at an id that does not exist |
| 3 | Missing blocker | A task is `blocked` with an empty dependency list |
| 4 | Dependency cycle | A depends on B depends on A |
| 5 | Broken link | A Markdown link resolves to no file, including inside dot-directories |
| 6 | Stale stored-derived field | A task stores a field the tool derives (e.g. `children`) |
| 7 | Missing deliverable | A task declares a deliverable path that no longer exists |
| 8 | Config error at setup | An unknown key, a missing file, an unresolvable reference (R-17) |

Class 5's dot-directory case is not hypothetical: `glob`'s `**` skips them, which hid the live
handoff pointer — the one file where a broken link costs most.

**Consequence of class 7, carried into implementation.** `check` must not learn the field name
`deliverables`, which the criteria above forbid. So the schema needs a key naming which field holds
deliverable paths — the field is currently carried and displayed but not interpreted
(`taskmd/defaults/config.md`). That is one added config key, within T-001's settled design rather
than a change to it; it is recorded here so it is not discovered mid-implementation.

**Not in this task**
- Interpreter and repository-root discovery, and project hook commands — **T-011**.
- The default id prefix and width, merge-conflict behaviour, and the measured scale ceiling —
  **T-004**. This task consumes whatever config says.
- Stating the measured saving in the README — **T-006**.
- `decisions` and `deliverables` as commands — **not built**; see *Resolved*, below.

**Resolved**
- ~~Are `decisions` and `deliverables` core commands or config-declared derived views?~~ —
  **neither.** `docs/SCOPE.md` non-goal 11 (decided later, in T-007) keeps the surface at three
  commands. The one behaviour worth keeping from them — `deliverables` caught a declared file that
  had been deleted (`docs/BRIEF.md`) — becomes class 7 above rather than being dropped.

**What this replaces**
`tools/tasks/task.py` is the interim self-hosting copy, kept so the project could use its own
method from the first session. It predates `taskmd/schema.py` and carries its own hardcoded schema,
so it **does not** implement symmetric soft links (T-012) — its `context` shows only the `related`
values a task literally stores, missing the ones derived from the other end. That is a known
limitation of the interim tool, not a defect to chase; this task removes it by building on
`taskmd/schema.py`. Delete `tools/tasks/task.py` when this lands, or it becomes a second
implementation with its own idea of the schema.

**Second known limitation — the `NEXT:` hint collapses phase and status.** The interim tool derives
its closing hint from `phase` alone:

```
NEXT: read the file above, then work the '%s' phase." % t.phase
```

`docs/METHOD.md` §2 makes phase and status independent — phase says where the work got to, status
says whether it can move. So a task that has *finished* a phase and is waiting for the next one to
be requested (status `review`, phase `implement`) is told to work the phase it just completed.
Observed 2026-08-04 on T-008 at exactly that state. The hint should read both, and say what the task
is waiting for rather than naming its phase back at the reader — which is the only part of `context`
that gives an instruction rather than a fact, so getting it wrong actively misleads.

Note the interaction with R-6: a hint that names the next phase is the kind of "next step pointer"
the method explicitly says is context, not authorization. Whatever it prints should not read as
permission to proceed.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Fix the R-15 baseline before any of it exists.** Name what a session must read to start one task with no tool, and count the bytes. Doing this first is the point: a denominator chosen after the numerator is known is not a measurement. | The baseline — what was counted, why that set, and the byte total — recorded in `## 3. Implement` |
| 2 | Add the config key naming the deliverables field (the consequence recorded in `## 1. Specify`), with its setup-time validation. | `taskmd/defaults/config.md` gains the key and its annotation; `taskmd/schema.py` exposes it; `tests/test_schema.py` covers a valid and a malformed declaration |
| 3 | **Build the eight failure fixtures before `check` exists** — one miniature project per class in *What `check` claims to catch*. Writing them first is what stops the claim shrinking to whatever proved easy. | `tests/fixtures/broken-<class>/` × 8, each a project the real CLI can be pointed at |
| 4 | Implement `check` and the entry point, then run it against every fixture and confirm each reports its own class and nothing else. | `taskmd/__main__.py`, `taskmd/cli.py`; `tests/test_cli.py` asserting one named failure per fixture, plus a clean pass on this repo |
| 5 | Implement `index`, including the generated-region markers and the migration of the existing index from the interim tool's marker to the new one. | `index` in `taskmd/cli.py`; a test that regenerating twice is a no-op and that text above the marker survives |
| 6 | Implement `context`, including the `NEXT:` line that reads status **and** phase. | `context` in `taskmd/cli.py`; a test over a task whose status has moved past its phase, asserting the line does not name that phase back |
| 7 | Run `context` on a real task and count its bytes against step 1's baseline. | The measured saving — both counts, the task used, and the ratio — recorded in `## 3. Implement` |
| 8 | Prove the portability criteria: bytes written contain no `\r\n`, console output survives cp1252, and the CLI runs on a copy of the tree with no `.taskmd/` present. | Three recorded results in `## 3. Implement`; the byte and no-config checks as tests |
| 9 | Switch this project onto the new CLI and delete `tools/tasks/task.py`, so there is one implementation rather than two schemas. | `tasks/_templates/task-template.md` and the index's command block updated; `tools/` gone; `check` clean afterwards |

Steps 5–8 are independent of each other and depend only on 2–4. Step 9 is last because it removes
the tool this project currently runs on.

**Shape decisions**

- **Entry point is `python -m taskmd`**, via `taskmd/__main__.py` dispatching to `taskmd/cli.py`.
  *Rejected:* a top-level `taskmd.py` script, which would have to re-find the package it sits beside,
  and would leave T-011's thin launchers wrapping a file path rather than a module.
- **The three commands share one module**, `taskmd/cli.py`. *Rejected:* a module per command — they
  share a loader and a renderer, which would then need a fourth module, and the reference does five
  commands in 458 lines. Revisit only if one command outgrows the other two together.
- **The `NEXT:` line says what the task is waiting for, never what to do.** *Rejected:* keeping the
  interim wording and adding status to it. The imperative *is* the defect — R-6 says a next-step
  pointer is context, not authorization, so a line that reads as permission is wrong even when the
  phase it names is right.
- **Fixtures are whole miniature projects, not broken text inside a test.** *Rejected:* constructing
  bad front-matter inline. A fixture the real CLI can be pointed at is also the reproduction case a
  later session needs when the class regresses.

**Assumption, recorded because it limits step 8.** Only one platform is available here, so
byte-identity across three is verified by its *mechanism* — explicit `newline="\n"` on every write,
no `os.linesep`, and separators normalised to `/` in anything printed — rather than by three runs.
That is weaker than the criterion's wording, and a run on macOS or Linux is what would close the
gap.

**Outputs this task produces**

- `taskmd/__main__.py`, `taskmd/cli.py`
- `taskmd/defaults/config.md` (one added key), `taskmd/schema.py` (exposing it)
- `tests/test_cli.py`, `tests/fixtures/broken-<class>/` × 8
- `tasks/_templates/task-template.md`, `tasks/README.md` (command block and marker)
- Deleted: `tools/tasks/task.py`
- Recorded in this file: the baseline, the measured saving, and the three portability results

## 3. Implement

### Step 1 — the R-15 baseline, fixed before the numerator existed

Measured 2026-08-05, on this repository, before a line of the CLI was written. Three candidate
baselines, because "what a session would otherwise read" has three defensible readings and picking
one after seeing the result is the failure this step exists to prevent:

| Baseline | What it counts | Bytes |
| :--- | :--- | ---: |
| **A — headline** | The task file plus the generated index: `T-002` + `tasks/README.md` | **16,113** |
| B — link-following | The task file plus every task it links to (6 of them) | 53,630 |
| C — no derived views at all | Every file in `tasks/` — what you must read when nothing is computed for you, because `blocks` and the far end of a soft link are written nowhere | 119,998 |

**A is the headline, and it is the least flattering of the three on purpose.** It credits `index`
for the graph work and asks `context` to beat only what is left, which is the honest comparison
inside a project that already runs taskmd. B and C are recorded because they are the real cost when
there is no index — C is what `docs/BRIEF.md`'s 37,909-byte figure was measuring on the source
project — but quoting either as the saving would be choosing a denominator to suit the answer.

Step 7 measures `context T-002` against A.

### Decisions taken while implementing

- **`blocked_status` became a config key** (2026-08-05). Class 3 says "a task is `blocked` with an
  empty dependency list", and there is no general way to implement it: the schema knows the status
  *vocabulary* but not which value asserts "held up". Same shape as `deliverables_field` — required,
  nullable, named by the project. *Rejected:* the literal string `blocked`, which is one project's
  word and would have made the check silently do nothing for every other project.
- **`check` skips nested projects** (2026-08-05) — a directory holding its own `.taskmd/` or its own
  tasks folder is validated on its own, never by its host. *Rejected:* a hardcoded `tests/fixtures/`
  exclusion, which would put this repository's layout inside the shipped tool. The rule is what lets
  deliberately-broken fixtures live in the tree at all.
- **The index omits an edge column no task uses** (2026-08-05), derived from the data rather than
  configured. A project with no hierarchy should not read a column of dashes, and one that starts
  using hierarchy should not have to remember to switch a column on. *Rejected:* an `index_edges`
  config key — configuration for something the data already answers.
- **The closing line of `context` carries only derived state** — open/closed, and which blockers are
  open. *Rejected:* repeating the header's fields in the footer, which is what the first draft did
  and which put one fact on screen twice.
- **The CLI prints no path to a method document** (2026-08-05). The interim tool ended with
  `Method: docs/METHOD.md`; that is a fact about *this* project, and general code cannot hold it.
  Pointing the agent at the method is T-003's job.
- **The index marker was migrated by hand, once.** The tool recognises its own marker and appends a
  region when it finds none; it does **not** know the interim tool's marker. *Rejected:* teaching the
  shipped tool to recognise a retired private marker, which would be permanent migration debt for a
  one-line one-time edit.

### Escalated rather than absorbed

- **`waiting` in the alternate fixture is not "blocked".** Setting `blocked_status: waiting` there
  made `check` report an epic as blocked with nothing blocking it — correctly: it waits on its
  *children*, which is hierarchy, not dependency (`docs/METHOD.md` §4). One status value cannot
  stand for both edges. The fixture now declares no blocked status and says why; the configurable
  name is proven by a purpose-built project in `tests/test_cli.py` instead.
- **T-008 declared a deliverable that step 9 deleted.** `check`'s missing-output class fired on its
  first real run, on `tools/tasks/task.py`. Removed from T-008's front-matter with a log entry.
  This is the class earning its place: nothing else in the repository would have noticed.

### A criterion that could not be met as literally worded — for `review` to judge

The criterion reads *"`context`'s `NEXT:` hint reads phase **and** status"*. It cannot, in a general
tool: `phase` is one project's vocabulary field, and the tool cannot know that status `planned`
means the `plan` phase is finished — that mapping is the method's, not the schema's.

What was built instead: the header line prints every `context_fields` value, so both axes are on
screen; the closing line carries only what is derived and **names no phase at all**. The defect the
criterion was written against — being told to redo the phase you just finished — is gone, because
nothing instructs. Whether that satisfies the criterion as written is `review`'s call, not this
phase's.

Both tools on T-002 at `status planned | phase plan`, i.e. planning finished:

```
interim  NEXT: read the file above, then work the 'plan' phase.
new      STATE  open, no blocker outstanding
```

### Verification — by use

**`check` made to fail, one fixture per class** (R-16). Each reports its own class and no other;
asserted in `tests/test_cli.py::CheckFailsOnEveryClassItClaims`:

```
broken-vocabulary       VOCABULARY    T-001.status is 'in-progres'; allowed: proposed, ...
broken-dangling         DANGLING      T-001.blocked_by -> T-404 does not exist
broken-missing-blocker  NO BLOCKER    T-001 is 'blocked' with nothing in blocked_by
broken-cycle            CYCLE         dependency loop: T-001 -> T-002 -> T-001
broken-link             BROKEN LINK   .notes/scratch.md -> gone.md
broken-derived-field    STORED DERIVED T-001 stores 'children:', which is computed from 'parent'
broken-deliverable      MISSING OUTPUT T-001 declares 'out/report.md', which does not exist
broken-config           CONFIG ERROR  ...: unknown config key(s): id_witdh          (exit 2)
```

The config case exits **before any command runs** (R-17), and names the key.

**Used on this repository**, which is the real case rather than a fixture:

```
OK - 18 task(s), vocabulary valid, references resolve, no broken links
71 passed in 0.23s
```

**Used on a project sharing no vocabulary with the default** — `tests/fixtures/alt-project`, whose
id prefix, status field, folder, edge names and derived names are all different. `context` printed
`state doing`, `EPIC`, `DEPENDS ON`, `SEE ALSO` and `ISSUE-0002`, and none of the default names
appeared anywhere in the output.

**Step 7 — the measured saving** (R-15), against baseline A above:

| | Bytes |
| :--- | ---: |
| Baseline A, as fixed in step 1 | 16,113 |
| `python -m taskmd context T-002` | **1,001** |
| | **6.2% — 16× smaller** |

Recomputing A at the moment of measurement gives 18,120 (5.5%), because T-002's own file grew by
this record while the work was done. The step-1 figure is the one quoted: it is the less flattering
of the two, and it is the one that was fixed before the numerator existed.

**Step 8 — portability.** Three results:

- *Bytes.* The generated index contains **0** carriage returns and 17 line feeds; non-ASCII content
  survives the round trip. Asserted in `tests/test_cli.py::WritesTheSameBytesEverywhere`.
- *cp1252.* Run with `PYTHONIOENCODING=cp1252` against a task titled with an em dash, curly quotes
  and an arrow, the output was byte-for-byte the same as on a UTF-8 terminal and exited 0 — the
  startup reconfigure overrides the terminal codec rather than depending on it.
- *No configuration.* A bare folder containing one task file and no `.taskmd/` runs all three
  commands successfully.

**The assumption from the plan still stands, unclosed.** Byte-identity was verified by mechanism on
one platform, not by three runs. A run on macOS or Linux is what would close it.

**Outputs produced**
- `taskmd/cli.py`, `taskmd/__main__.py`
- `taskmd/defaults/config.md` — two added keys (`deliverables_field`, `blocked_status`)
- `taskmd/schema.py` — both keys exposed and validated at config-read time
- `tests/test_cli.py`, `tests/fixtures/README.md`, `tests/fixtures/broken-*/` × 8
- `tests/test_schema.py`, `tests/fixtures/alt-project/` — extended for the new keys
- `tasks/README.md`, `tasks/_templates/task-template.md` — switched to `python -m taskmd`
- Deleted: `tools/tasks/task.py`

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Seeded from `docs/BRIEF.md` when the project folder was prepared. |
| 2026-08-04 | (no change) | Second interim-tool limitation recorded: the `NEXT:` hint derives from `phase` alone and contradicts R-3. Found while working T-008, which also gave the CLI its new footer target. `related` gained T-008. |
| 2026-08-05 | → specified | Specify agreed by the owner. The open question is closed by `docs/SCOPE.md` non-goal 11 — three commands, and the deliverable-existence behaviour survives as a `check` class rather than being dropped. `check`'s eight failure classes enumerated so R-16's criterion is falsifiable before implementation. R-15 gained a criterion (measure here, state in README in T-006). Id format pinned to config, which makes T-004 independent rather than a prerequisite; `related` gained T-004. |
| 2026-08-05 | → review | Implement worked, nine steps in order. Six decisions recorded, two of them adding config keys — `blocked_status` because "blocked with no blocker" cannot be checked without the project naming its own held-up value. Two discoveries escalated rather than absorbed: `waiting` in the alternate fixture is hierarchy not dependency, and T-008 declared a deliverable step 9 deleted — caught by `check`'s own missing-output class on its first real run. `check` shown failing on all eight classes; measured saving 1,001 bytes against the step-1 baseline of 16,113 (6.2%). One criterion could not be met as literally worded and is flagged for review rather than quietly reinterpreted. Phase stays `implement`; the §4 verdict is review's (R-6). |
| 2026-08-05 | → planned | Nine steps. The R-15 baseline is fixed in step 1, before anything that could flatter it exists; the eight failure fixtures are built in step 3, before `check` does. Four shape decisions recorded with what they reject. One assumption recorded against step 8: byte-identity across three platforms is verified by mechanism, not by three runs. |
