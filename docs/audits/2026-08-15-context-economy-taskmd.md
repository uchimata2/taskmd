# Context economy — taskmd's own report

**`ecoctx` phase 1, steps 1–11, run 2026-08-15 on this repository. Report only.** Nothing was raised
on the board; step 11's child work is listed here as a proposal for the owner's review, which is the
only moment the method allows it to be raised.

The findings any project can act on are in
[the portable half](2026-08-15-context-economy-portable.md). **One numbering space across both
documents; each finding is stated in full in exactly one of them.** The ranked table below lists
every id wherever it is stated — an audit about redundancy that prints its findings twice has
answered its own question.

**Steps 1–4 are measured. Steps 7–9 are estimated.** Every band is an estimate. Every inventory
figure is a measurement with a date.

**Token conversion: bytes ÷ 4, an estimate**, applied uniformly and never used to separate two
findings a byte count does not already separate.

---

## The ranked list

Gain per unit of effort, **with risk as a veto rather than as a term**.

| Rank | id | Surface | Family | Gain | Effort | Controller | Stated in | One line |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [E-12](#e-12) | B | F1/F4 | `L` per occurrence, `M` expected | XS | project | here | Tier 1 names a 36,393-char index file; a command answers the same question in 95 |
| 2 | [E-10](2026-08-15-context-economy-portable.md#e-10) | A | F3 | `S`, exact | XS | project | portable | Block HTML comments are stripped before injection — free maintainer notes |
| 3 | [E-16](#e-16) | B | F1 | `M` expected | S | project | here | The binding is 31.9% of the non-task read path and read-only phases do not need it |
| 4 | [E-13](#e-13) | A | F1 | `M` | S to test, M to carry | project | here | 36.3% of tier 1 is prose about tier 1; a path-scoped rule could now hold it |
| 5 | [E-01](2026-08-15-context-economy-portable.md#e-01) | A | F1 | `enabler` | XS | project | portable | A passing budget covers 12.3% of the observed load path; say so in the rule |
| 6 | [E-11](2026-08-15-context-economy-portable.md#e-11) | A/E | F5 | `bimodal` | S | project | portable | A general-purpose subagent pays CLAUDE.md again |
| 7 | [E-08](2026-08-15-context-economy-portable.md#e-08) | E | F5 | `enabler` | XS | project | portable | Screen every figure on source and on where the effect concentrates |
| 8 | [E-09](2026-08-15-context-economy-portable.md#e-09) | A | F1 | `enabler` | XS | project | portable | `@path` imports load at launch; a split is not a deferral |
| 9 | [E-04](2026-08-15-context-economy-portable.md#e-04) | A | F3 | `enabler` | XS | project | portable | Instruction count is the binding limit and the byte budget cannot see it |
| 10 | [E-20](2026-08-15-context-economy-portable.md#e-20) | A | F3 | `enabler` | n/a | project | portable | Attention is unpriced, and it is why rank 4's remedy must be measured |
| — | [E-02](2026-08-15-context-economy-portable.md#e-02) | A | F1 | `L` (user) / `S`→0 (project) | S | **user** | portable | The catalogue is ~31,100 chars and 1.3% of it is ours |
| — | [E-05](2026-08-15-context-economy-portable.md#e-05) | B | F1/F4 | `L` / `M` | XS | project | portable | The portable statement of rank 1 |
| — | [E-07](2026-08-15-context-economy-portable.md#e-07) | C | F5 | `L` elsewhere, **zero here** | S | user | portable | Output caps: measured not to apply |

**Rank 4 and rank 5 share one policy question** — *what is tier 1 for, and whose tier 1 does the
budget govern* — and specifying them independently produces inconsistent answers. **E-01 settles it
and E-13 cites it.** If only one is ever taken, take E-01.

**Ranks 1 and 3 are independent** and can be taken in either order.

---

## Findings stated here

### E-12 — Tier 1 names the generated index, which is 24× the command that replaces it {#e-12}

| Field | Value |
| :--- | :--- |
| Surface | B |
| Family | F1 / F4 |
| Finding | [`CLAUDE.md`](../../CLAUDE.md) states "`tasks/README.md` is the generated backlog." Measured 2026-08-15: [`tasks/README.md`](../../tasks/README.md) is **36,393 characters ≈ 9,100 tokens**. `taskmd list --open` printed **1,473 characters** and `taskmd list --open --limit 1` printed **95**. A session that follows the sentence pays about 9,100 tokens for what a command gives for about 370 — or 24. The plugin's own [`SKILL.md`](../../plugin/skills/taskmd/SKILL.md) already says the opposite: "run a command, do not read the folder, and never maintain a list." Tier 1 and tier 2 disagree, and tier 1 is read first. |
| Change | Drop the file's name from tier 1, or replace it with the command. **Hypothesis** — the owner may want a human-facing pointer to survive, in which case the sentence needs to say *for humans*. |
| Gain | `L` on the read path each time a session opens the file. `M` in expectation: it fires only when a session reads rather than runs. |
| Effort | XS |
| Risk | **none.** The file keeps being generated and keeps serving readers on GitHub. Only the pointer's audience changes. No fact loses its home. |
| Applies to | this project |
| Controller | project |
| Source | this audit |

**Already open.** [T-143 — *Decide whether tier 1 names the generated index at all*](../../tasks/T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) is `proposed`, phase `specify`, work package M6. **Nothing to raise.** What this audit adds to it is the measurement: 36,393 against 1,473 against 95, on 2026-08-15.

### E-13 — 36.3% of the project's tier 1 is prose about the instruction file itself {#e-13}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F1 |
| Finding | [`CLAUDE.md`](../../CLAUDE.md) is **6,571 characters**, partitioned to within +5. *Working method* is **4,157 (63.3%)**, and within it: **2,384 characters (36.3% of the file)** is prose about the file — the three tiers, the budget relation, and what earns a place in tier 1. The remaining **1,776 (27.0%)** is the two rules that must bind before any task exists, and those are correctly in tier 1: [`METHOD.md`](../../plugin/skills/taskmd/docs/METHOD.md) §3 explicitly refuses to state them, naming this file as their single home. **This is not F2 duplication.** The 2,384-character block binds during one activity — editing this file — which the file itself argues nobody announces. |
| Change | Move the meta-rules to `.claude/rules/` with `paths:` front matter matching `CLAUDE.md`, so they load when the file is read and not otherwise. **Hypothesis, unverified.** |
| Gain | `M` on the load path — 2,384 characters ≈ 600 tokens per turn, 34% of the project's own tier 1. **Carve-out estimate: about 400–600 characters of the block are operative for the agent rather than the human maintainer** (the tier definitions themselves, which an agent needs when told to move something between tiers), so the realistic extraction is ~1,800–2,000, not 2,384. A size names a region; the region is not the change. |
| Effort | S to test, M to carry |
| Risk | **Three.** (1) Path-scoped rules are documented as **not re-injected after compaction** — a long session that compacts and then edits this file would not have the rule. (2) It re-opens a decision the project recorded with a reason: T-118 settled that an unannounced activity is the exception that keeps a rule in tier 1. Evidence licenses re-opening, **not reversing**. (3) `.claude/rules/` is a harness-specific mechanism; this repository ships a plugin meant to work for any project, and a rule directory is not portable in the way `CLAUDE.md` is. |
| Applies to | this project |
| Controller | project |
| Source | harness documentation, via the portable [E-03](2026-08-15-context-economy-portable.md#e-03) |

**The cheaper alternative, and it needs no restart.** [E-10](2026-08-15-context-economy-portable.md#e-10) — block-level HTML comments are stripped before injection. The half of the 2,384 characters that is *justification addressed to a maintainer* can move into a comment inside the same file, at zero per-turn cost and with zero relocation risk. It saves less than the rule split and it cannot fail. **Shape refused, still worth doing** is an outcome this record is built to hold.

### E-14 — The budget's comparison set is closed, and this is a result rather than a finding {#e-14}

`python tests/test_budget.py`, run 2026-08-15:

```
tier 1 6968 chars under by 878 (bound 7846, reference/TASK-WORKFLOW.md) from: CLAUDE.md, plugin/skills/taskmd/SKILL.md
Ran 5 tests in 0.035s
OK
```

The relation is bound against a document whose membership changes only by a deliberate act, not
against *the smallest document tier 1 defers to* — which would ratchet down with every remedy it
prompts and become unsatisfiable by the one action it exists to cause. The unit is characters. The
check has been shown to fail on a tree it is supposed to catch, and its own header records that
counting bytes reversed the verdict on the real repository once.

**Family with no finding, reported as one.** This is the closed comparison set the method asks for,
already implemented.

### E-15 — Spine plus one branch is implemented; 13,905 characters are present and not paid {#e-15}

[`docs/bindings/local-markdown.md`](../../plugin/skills/taskmd/docs/bindings/local-markdown.md) is
14,425 bytes and
[`docs/bindings/github-issues.md`](../../plugin/skills/taskmd/docs/bindings/github-issues.md) is
13,905. [`SKILL.md`](../../plugin/skills/taskmd/SKILL.md) directs a session to *this project's
binding* — one. **Result, not a finding.**

### E-16 — The binding is the largest item on the read path, and read-only phases do not need it {#e-16}

| Field | Value |
| :--- | :--- |
| Surface | B |
| Family | F1 |
| Finding | **Representative unit, chosen before the audit and named here: one phase of one task, taken as the `specify` phase of [T-144](../../tasks/T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md)** — the most recently closed non-trivial task, whose whole lifecycle is in git (`+325 −19` lines across 3 commits touching its own file). Measured read path, 2026-08-15: `SKILL.md` 3,007 + `METHOD.md` 7,443 + phase file 3,363 (`specify`; the range across 7 phase files is 3,237–5,844, mean 4,306) + binding 14,425 + `taskmd context T-144` **972** + the task file **25,347** = **54,557 characters ≈ 13,600 tokens**. Against the corpus mean task file (16,205) it is 45,415 ≈ 11,400 tokens. **The binding is 14,425 of the 29,210 non-task characters — 49.4%**, and the largest single item on the whole path apart from the task file. |
| Change | `SKILL.md` already scopes the binding to "before creating or changing any task". Make that scoping load-bearing: a phase that only reads — the reading half of `specify`, and `review` — does not load it. **Hypothesis.** |
| Gain | `M` in expectation. `L` on the read path for a read-only phase; `none` for a writing phase, and most phases write. |
| Effort | S |
| Risk | A session that discovers mid-phase that it must write now has an unloaded binding. The rule has to say *load it then*, and a rule that fires mid-phase is exactly the kind that gets missed. This risk is real enough that the change may not be worth it — **the finding stands regardless of the remedy's fate.** |
| Applies to | this project |
| Controller | project |
| Source | this audit + precedent pattern P6 |

**External support, and it is the strongest independently-sourced item in the catalogue.** A study
of 55,315 published skills found **over 60% of body content non-actionable**, and a tool that
compressed descriptions 48% and bodies 39% **improved functional quality by 2.8%** — a measured
less-is-more effect. That is evidence about skill bodies in general, not about this binding, and it
is offered as a reason to test rather than as a reason to cut.

### E-17 — `Log` is 16.6% of the task corpus, and the F3 finding is rejected {#e-17}

Partition of all 151 task files, 2026-08-15 — **2,430,672 characters, partition summing to
2,431,428, delta +756 (0.03%)**, reported rather than hidden:

| Section | Characters | Share |
| :--- | ---: | ---: |
| 1. Specify | 703,445 | 28.9% |
| 3. Implement | 667,705 | 27.5% |
| **Log** | **402,398** | **16.6%** |
| 2. Plan | 296,909 | 12.2% |
| 4. Review | 296,145 | 12.2% |
| front matter | 54,582 | 2.2% |
| preamble / title | 10,244 | 0.4% |

By status: **`done` is 2,306,195 characters — 94.9% of the corpus.**

**Recorded as rejected under F3's guard rail.** F3's test is not *is this justification* but *does
it decide anything future*, and **a finding that cannot name what the prose would stop deciding is
not a finding**. The log decides what a later audit can check, which is exactly what
[`METHOD.md`](../../plugin/skills/taskmd/docs/METHOD.md) §1.5 means by *undocumented progress did
not happen*. I cannot name what it would stop deciding, so it is not a finding.

The read-path exposure is also smaller than the share suggests: `taskmd context` returns a
**pointer**, not a body — 740, 972 and 1,727 characters for T-145, T-144 and T-026, whose files are
7,590, 25,347 and 48,768 bytes. The tool already declines to pay this.

### E-18 — 858 bytes of payload per byte of tier-1 description {#e-18}

The served snapshot is **39 files, 340,592 bytes**. Its tier-1 cost is the **397-character**
description in `SKILL.md`'s front matter. Progressive disclosure is doing what it is for.

**Family with no finding, reported as one.**

### E-19 — Tool output on a green run is ~2,400 characters for a whole unit of work {#e-19}

Measured 2026-08-15, each captured to a file and measured without printing:

| Command | Characters | Lines | Exit |
| :--- | ---: | ---: | ---: |
| `taskmd list --open --limit 1` | 95 | 1 | 0 |
| `taskmd list --open` | 1,473 | 17 | 0 |
| `taskmd list` | 11,693 | 151 | 0 |
| `taskmd context T-145` | 740 | 13 | 0 |
| `taskmd context T-144` | 972 | 19 | 0 |
| `taskmd context T-026` | 1,727 | 29 | 0 |
| `taskmd check` | 412 | 3 | 0 |
| `taskmd index` | 46 | 1 | 0 |
| `pytest -q` | 355 | 4 | 0 |

`pytest -q` tail: `260 passed, 3 skipped, 6 subtests passed in 32.08s`.

A unit of work runs `list --open --limit 1`, `context`, `check`, `index` and the suite: **about
2,400 characters.** **F5 finds nothing on surface C**, and the external technique with the largest
reported saving — a global tool-output cap — would never fire here. That zero is measured, not
assumed.

### Write volume — surface D {#surface-d}

Across all 151 tasks, **36,633 lines added under `tasks/T-*`, mean 242 per task.** The
representative unit, T-144, is `+325 −19` across 3 commits. The largest are T-006 (+573, 15
commits), T-026 (+542, 9) and T-050 (+500, 7). **No finding.** Surface D is paid twice — once
written, once read as surface B — and the read half is already governed by `context` returning a
pointer.

---

## Families with no finding

| Family | Result on this repository |
| :--- | :--- |
| **F2 — redundancy and contradiction** | **No finding.** The one candidate is the two conduct rules carried in `CLAUDE.md`, and `METHOD.md` §3 declares that file the single home and states why. F2's first question — *which document should have had it* — is already answered in the governing document, which is the case the method describes as the one that usually fails. Nothing else restated a rule. |
| **F4 — model work that should be deterministic** | **One finding**, E-12: reading a generated file where a command exists. No second instance. The validator, index and listing are all programs already. |
| **F5 — tool and workflow economics** | **No finding on surface C** (E-19). One finding on surface A/E, [E-11](2026-08-15-context-economy-portable.md#e-11), and it is not this project's to fix alone. |

---

## The load path as measured

All figures 2026-08-15. **The item that cannot be changed is still in the inventory, marked.**
Membership was established **by observation** — what this session was handed before its first tool
call — not from any file's claim about when it loads.

| Item | Size | Controller | Note |
| :--- | ---: | :--- | :--- |
| Harness system prompt, tool schemas, MCP instructions, environment block | not measurable from here | **harness** | The vendor's own illustrative figures put the system prompt near 4,200 tokens and the environment block near 280. This audit did not measure it and does not band it. |
| Capability catalogue | **67 entries observed**; 7 measured at 3,245 chars, mean 464; **~31,100 estimated** | **harness / user** | Largest single item. See [E-02](2026-08-15-context-economy-portable.md#e-02) |
| Auto-memory index | 10,252 B | user | Loaded to 200 lines or 25 KB, whichever comes first |
| Output style | 4,732 B | user | Injected into the system prompt |
| Personal instruction file | 3,561 B | user | |
| **`CLAUDE.md` (this repository)** | **6,571 chars** | **project** | |
| **`SKILL.md` description (this repository)** | **397 chars** | **project** | 1.3% of the catalogue estimate |
| **Project-controlled tier 1** | **6,968 chars** | | Bound 7,846; under by 878 |
| **Observed tier 1, all controllers** | **~56,600 chars ≈ 14,200 tokens** | | Excludes the harness items above |

**The repository controls 12.3% of the tier 1 it can see.** Its budget passes. Both are true, and
[E-01](2026-08-15-context-economy-portable.md#e-01) exists so the first is never read as the second.

---

## Upstream — components this project uses but does not own

**Written to be handed over, and not implemented locally.** A handed-over item carries the sender's
labels: these are observations, not priorities, and where they land is the receiving project's call.

**Prove which component failed before filing.** Nothing here is a defect claim. Neither entry
asserts that a component failed; both report an observation and name what would turn it into a
claim.

### U-01 — Per-project control of the capability catalogue

**Upstream: the Claude Code harness.**

**Their backlog was read.** Two things already exist upstream and this entry is an **adoption, not a
proposal**: `disableBundledSkills` ships and hides built-in skills from the model, and
`disable-model-invocation: true` removes an individual skill's description from context while
keeping it invocable by name. Both are **user- or skill-scope**. What was not found is a *project*
scope — a way for a repository to say which of the 67 catalogue entries are relevant to it, so that
a clone inherits the setting. `claudeMdExcludes` does this for instruction files; there is no
equivalent for the catalogue.

**Observation, not a request:** the catalogue was the largest item on this session's load path at an
estimated ~31,100 characters, and the repository could reach 403 of them.

### U-02 — `disabledTools`: a figure in circulation, attached to a mechanism that may not exist

**Upstream: the Claude Code harness.**

**Their backlog was read**, and this is why the entry exists. A widely-repeated third-party figure
says roughly 30 built-in tools cost about 16,000 tokens — 8% of a 200k window — and attaches a
`disabledTools` setting in `settings.json` as the remedy. The primary source located for that
setting is an **open feature request**, not documentation.

**What survives is the boundary, recorded so the next reader does not re-run the search:** the
figure may be accurate and the lever may not ship. This audit did not verify either. Anyone
depending on the figure should measure it against their own session with `/context` rather than
inherit it from here.

---

## Byproduct register

**Never ranked, never banded, never a finding id.** Checking every file for one thing means seeing
other things. What an observation is worth is the receiving project's call, not the reporter's, so
everything noticed is recorded.

| # | Where | What was seen | Owner |
| :--- | :--- | :--- | :--- |
| B-1 | `.github/workflows/tests.yml` | The job runs each test module separately and deliberately does not stop at the first failure. Its own header records that a green run proves **Linux only**, and that four Windows failures are open and invisible to it. A reader of a green badge would not know that. The header says so; nothing the badge links to does. | this project |
| B-2 | `plugin/skills/taskmd/SKILL.md` | "`taskmd context <id>` … returns everything needed to start that one task, and is the only read of it you need." Measured, `context T-145` returns **740 characters** and does **not** include the task body; the file is 7,590 bytes. The sentence is true for orientation and not for the specification. Observation, not a defect claim — whether the sentence should change is the owner's call. | this project |
| B-3 | repository root | There is **no `.taskmd/config.md`**; the project runs on the shipped defaults (22,974 bytes) and declares **no `after_write` command**, though `CLAUDE.md` describes the mechanism. The mechanism is exercised only by test fixtures. Worth knowing before anyone reads the absence of hook output as a hook that ran. | this project |
| B-4 | the served plugin snapshot | It contains **five `__pycache__/*.pyc` files**, copied by the local-directory install route, which copies and does not prune. They are not in `git ls-files`, so an adopter installing from GitHub does not receive them. No context cost — a `.pyc` never enters a context window. Recorded because the served snapshot is what "an adopter receives" is usually reasoned about. | this project |
| B-5 | the plugin cache | **Five version directories** for this plugin (0.1.0, 0.1.1, 0.3.0, 0.4.0, 0.5.0, 1.6 MB total); the registry serves 0.5.0. Disk only, no context cost. The same pattern holds for another installed plugin at 30 MB across six versions. | harness / user |
| B-6 | personal skills directory | Two directories with near-identical names are present, one of 1 file and one of 15; the session catalogue served one entry. Likely a stale copy. Outside this repository entirely — recorded because it was seen while establishing the catalogue, and because a stale skill directory is the kind of thing that costs a description in tier 1 without anyone deciding to pay it. | user |
| B-7 | plugin registry vs. MCP | One plugin is installed with `enabledPlugins` set to `false`; its skills did **not** appear in the session catalogue, and its MCP tool names **did** appear on the deferred tool list. Two mechanisms, one disabled and one not. Not a defect — the MCP server is configured separately — but it is a place where "I turned that off" and "it is not loaded" come apart. | user |

**The register has a home for an owner with no section.** B-5, B-6 and B-7 belong to the person
running the agent rather than to this repository or to its upstream, and there is no other place in
this report for them.

---

## Step 11 — child work, proposed and not raised

**Nothing was raised.** The method raises child work *at the owner's review, not before*, and this
run was asked to report only. Listed here for that review:

| Proposed | Covers | Note |
| :--- | :--- | :--- |
| *(none — already open)* | [E-12](#e-12) | [T-143](../../tasks/T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) already asks the question. What this audit adds is the measurement. |
| One task, to settle the tier-1 scope question | [E-01](2026-08-15-context-economy-portable.md#e-01) **and** [E-13](#e-13) | They share one policy question. Specifying them independently produces inconsistent answers. E-01 settles it and E-13 cites it. |
| One task | [E-16](#e-16) | Independent of the others. |
| One task | [E-10](2026-08-15-context-economy-portable.md#e-10) | Cheapest in the audit and cannot fail. Could fold into the E-01/E-13 task. |
| **Phase 2 of this audit** | all of the above | **Blocked on the repairs above.** A phase that runs once, later, on a trigger nobody watches is a phase that does not run. It grades every band against what the change actually bought, and it cannot be faked from this document. |

**Re-measure every inventory figure when the work starts, not from this table.** Subjects grow
between ranking and implementation. In the one fully graded prior run, three of thirteen figures
moved before their task began — one board grew 33,676 → 36,559, one share fell 45% → 37.9% **while
the section it named had grown**, and one went 61% → 69.0% by the day it was cut.

**What each closure owes is one line**: the measured outcome, written in the record that already
exists, on the day it is known. Reconstructing thirteen outcomes afterwards cost 80,721 bytes across
fourteen closed records and was the most expensive step in the method.

---

## How this was measured, and what it cannot see

Measurement ran as a throwaway program **outside this repository**. Sizes came off the filesystem;
command output was captured to files whose lengths were measured without printing them. Opening a
file to find out how big it is spends the exact budget under audit.

Every partition was made to sum, and the residual is printed rather than hidden: the task corpus
partition summed to +756 on 2,430,672 (0.03%); the four document partitions summed within +3 to +11
characters each.

**The method measures artifacts, not sessions** — a file size is what a session *could* pay.
**It cannot separate operative prose from narrative mechanically**; every such split here was made
by reading, and [E-13](#e-13)'s carve-out estimate says so explicitly. **It does not price
attention** — see [E-20](2026-08-15-context-economy-portable.md#e-20), which is the reason
[E-13](#e-13)'s remedy is a hypothesis and not an instruction. And the screening partition in the
portable half **says nothing about the catalogue's completeness**: it sums, and summing is not
coverage. The search record is the only guard, and it is weaker than the partition.
