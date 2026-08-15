# Context economy — the portable half

**Findings that stand alone.** Every row here is stated so that a project with no knowledge of
taskmd can act on it. The half that only taskmd can act on is
[the project's own report](2026-08-15-context-economy-taskmd.md); the two share one numbering
space, and each finding is stated in full in exactly one of them.

**Method:** `ecoctx` phase 1, steps 1–11, run 2026-08-15. Steps 1–4 are measured. Steps 7–9 are
estimated, and the difference is the most important thing this document carries.

**Token conversion, stated once and applied uniformly:** bytes ÷ 4. It is an estimate. It is never
used to separate two findings that a byte count does not already separate.

---

## What this method cannot see

Said here so silence is not read as a clean bill.

- It measures **artifacts, not sessions**. A file size is what a session *could* pay, not what one
  did.
- It **cannot separate operative prose from narrative mechanically**. Every such split in this run
  was made by reading, and is marked where it was.
- It **does not price attention**. A shorter context is assumed better. Where a cut would make the
  agent guess, that is a risk field, not a measurement — see [E-20](#e-20).
- The screening partition in step 7 says nothing about **the catalogue's completeness**. It sums.
  Summing is not coverage.

---

## The four surfaces

| | Surface | Paid |
| :--- | :--- | :--- |
| **A** | Load path — what enters context unasked | every turn of every session |
| **B** | Read path — what one unit of work must open | once per session, and it grows with the project's age |
| **C** | Tool output — what commands print back | per invocation |
| **D** | Write volume — what a session produces | twice: written, then read as surface B |
| **E** | Workflow and tooling — **when** a cost is paid | cuts across all four |

**Only tier 1 gets a budget.** Tiers 2 and 3 are not paid every turn, so a size limit there measures
the wrong cost; what constrains them is the load-one-at-a-time rule. This is the visible price of
budgeting tier 1 alone, and it means tier-2 documents are allowed to grow.

**Express the budget as a relation, not a constant**, and bound it against something counted from
the same tree whose **membership changes only by a deliberate act**. A bound against *the smallest
document tier 1 defers to* ratchets down with every remedy it prompts, and becomes unsatisfiable by
the one action it exists to cause.

---

## Findings

Eleven fields each. `Change` is a **hypothesis** and is read as one; `Finding` is a measurement.
In the one fully graded prior run, eleven of thirteen bands missed and **every error was in
`Change`, none in `Finding`**. Re-measure a remedy before carrying it out, and let the measurement
refuse it.

### E-01 — A project's tier-1 budget can only govern the minority of tier 1 it ships {#e-01}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F1 |
| Finding | Measured on one repository, 2026-08-15: the repository controlled **6,968 of about 56,600 observed tier-1 characters — 12.3%**. The rest was user scope (personal instruction file, auto-memory index, output style) and harness scope (system prompt, tool schemas, capability catalogue). The repository's own budget check passed. Both statements are true at once. |
| Change | State the budget's scope inside the rule — *tier 1 **that this repository ships*** — so that a passing check is never read as a clean load path. |
| Gain | `enabler`. It saves nothing. It makes [E-02](#e-02) and [E-03](#e-03) decidable, because until the denominator is named, every share computed against it is ambiguous. |
| Effort | XS |
| Risk | none |
| Applies to | any |
| Controller | project |
| Source | this audit |

### E-02 — The capability catalogue is the largest load-path item and almost none of it is the project's {#e-02}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F1 |
| Finding | **67 catalogue entries were observed** in one session. Seven were resolvable to files on disk and measured exactly: **3,245 characters of name + description, mean 464**. Extrapolating that mean gives **about 31,100 characters ≈ 7,800 tokens** — larger than every instruction file on the load path combined. The repository under audit contributed **403 characters, 1.3%**. |
| Change | Nothing the repository can do. The reachable levers are user scope: turning off bundled skills, disabling plugins that are installed but unused, and `disable-model-invocation: true` on a per-skill basis, which keeps the skill invocable by name while removing its description from context. |
| Gain | `L` on the load path **for the person running the agent**. `S`, tending to zero, for the repository. The two are different quantities and the record says which. |
| Effort | S at user scope; not available at project scope |
| Risk | A skill whose description is removed is one the agent will not offer. That is a fact losing its only discovery path, and it ranks the change below everything that defers rather than deletes. |
| Applies to | any |
| Controller | **user** — actionable, and someone present can do it, but the change lands outside the repository and no clone inherits it |
| Source | external research (axis B, axis C) + this audit |

**The 31,100 figure is an extrapolation from a 7-of-67 sample and is labelled as one.** The measured
part is 3,245 characters. The unmeasured 60 entries are served by the account and the harness and are
not on the audited machine's disk. A reader who needs the exact number must observe it, not compute
it from here.

### E-03 — A rule that binds only while editing one file can now be scoped to that file {#e-03}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F1 |
| Finding | Instruction files accumulate prose about themselves — the tiering scheme, the budget, what may be added. It is paid on every turn and it binds during one activity: editing that file. The classic defence is that **nobody announces editing an instruction file**, so no on-demand pointer can reach the rule in time. That defence rested on a gap in the harness that no longer exists: path-scoped rules (`.claude/rules/*.md` with a `paths:` glob in front matter) load **only when the agent reads a matching file**, which makes the unannounced activity announceable. |
| Change | Move the file's meta-rules to a path-scoped rule matching the instruction file itself. **Hypothesis, unverified — see below.** |
| Gain | `M` on the load path. On the measured instance, 2,384 of 6,571 characters (36.3%) fell in scope; that is about 600 tokens per turn. |
| Effort | S to test, M to carry |
| Risk | **Two, and both are real.** (1) Path-scoped rules are documented as **not re-injected after compaction**; they reload the next time a matching file is read. A long session that compacts and then edits the instruction file would have the rule absent at exactly the moment it binds. (2) Where a project has already recorded a decision to keep the prose in tier 1, this evidence licenses **re-opening** that decision, not reversing it. |
| Applies to | any |
| Controller | project |
| Source | harness documentation (axis C) |

**Unverified, and the test is named.** This run did not write a rule, restart a session and observe
the load. The settling test is: write the rule, restart, and read the `InstructionsLoaded` hook's
log — it fires when an instruction file enters context, at session start for eager files and again
later for path-scoped ones, and it exists for exactly this kind of observability. Then compact, edit
the instruction file, and check whether it fired a second time. **Two failed attempts is the signal
to stop**, and what survives is the boundary: which loads the mechanism reached and which it did not.

### E-04 — Size is measurable; instruction count is the binding limit and is not {#e-04}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F3 |
| Finding | Practitioner guidance converges on 150–200 lines per always-loaded instruction file, and the stated reason is **adherence, not tokens**: frontier reasoning models follow roughly 150–200 instructions with consistency, and smaller or non-reasoning models fewer. One coding agent silently truncates an instruction file past a configured byte limit, so an oversized file actively loses content rather than costing extra. A byte budget sees none of this. |
| Change | None proposed. Record instruction count as a second constraint alongside the byte budget, unmeasured, and say it is unmeasured. |
| Gain | `enabler` |
| Effort | XS |
| Risk | none |
| Applies to | any |
| Controller | project |
| Source | external research (axis A) |

### E-05 — A generated index is a read-path cost the tool already avoids {#e-05}

| Field | Value |
| :--- | :--- |
| Surface | B |
| Family | F1 / F4 |
| Finding | Measured 2026-08-15 on one repository: the generated index file was **36,393 characters**; the command answering the same question printed **1,473** (all open items) or **95** (the single next item). That is 25× and 383×. Any project that both generates an index file and names that file in an always-loaded document has created a ~9,000-token read that its own tool makes unnecessary. |
| Change | Name the command in tier 1. Never name the file. |
| Gain | `L` on the read path each time it fires. `M` in expectation, because it fires only when a session opens the file rather than running the command. |
| Effort | XS |
| Risk | none — the index file keeps existing for humans; only the pointer moves |
| Applies to | any |
| Controller | project |
| Source | this audit |

### E-08 — An advertised saving and a measured one differed by 7.6× {#e-08}

| Field | Value |
| :--- | :--- |
| Surface | E |
| Family | F5 |
| Finding | A named output-compression skill advertises a 65% cut in output tokens. An independent paired benchmark over 82 tasks measured **8.5%**, and **+7%** — a net increase — on one coding benchmark. The mechanism explains the gap and is more useful than the number: agentic output is dominated by code, diffs, tool invocations and exact error strings, all of which the technique correctly leaves verbatim, so only the narration between tool calls compresses, and there is little of it. |
| Change | Screen every catalogue figure on two things: whether it is vendor-published, and **where the effect concentrates**. Concentration decides more screenings than magnitude. |
| Gain | `enabler` |
| Effort | XS |
| Risk | none |
| Applies to | any |
| Controller | project |
| Source | external research (axis B) |

### E-09 — Splitting an instruction file into imports does not reduce what loads {#e-09}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F1 |
| Finding | The harness documents that `@path` imports in an instruction file are **expanded and loaded into context at launch**, recursively to four hops. Splitting for organisation therefore changes nothing about what is paid. Three mechanisms do defer: skills, path-scoped rules, and plain markdown links that the agent must choose to follow. A project that believes it deferred by splitting may have only reorganised. |
| Change | Establish by observation which of the three a split actually used. A file's claim about its own loading is not evidence. |
| Gain | `enabler` |
| Effort | XS |
| Risk | none |
| Applies to | any |
| Controller | project |
| Source | harness documentation (axis C) |

### E-10 — Block-level HTML comments in an instruction file cost nothing {#e-10}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F3 |
| Finding | The harness strips block-level HTML comments from an instruction file **before injecting it into context**. Comments inside code blocks are preserved, and the comment is still visible when the file is opened with a read tool. A justification addressed to a human maintainer can therefore sit in the file at zero per-turn cost. |
| Change | Where an F3 candidate is *justification for a human* rather than *instruction for the agent*, wrap it in a block comment instead of deleting it or relocating it. This is the F3 outcome that destroys nothing. |
| Gain | `S`, and it is exact rather than estimated: the bytes leave the per-turn cost entirely. |
| Effort | XS |
| Risk | **The agent cannot see it.** Nothing operative may go there, and the split between *justification* and *instruction* is the same judgement F3 always demands. Getting it wrong here is silent. |
| Applies to | any |
| Controller | project |
| Source | harness documentation (axis C) |

### E-11 — A subagent pays the instruction file again {#e-11}

| Field | Value |
| :--- | :--- |
| Surface | A / E |
| Family | F5 |
| Finding | The harness documents that a spawned subagent loads the project instruction file into **its own** context window, and that the built-in exploration and planning agents skip it for a smaller context. So an always-loaded file is paid once per session **plus once per general-purpose subagent**. Delegating read-heavy exploration — a technique whose whole point is protecting surface B — multiplies the surface-A cost. |
| Change | Prefer the built-in exploration agent for read-heavy sweeps over a general-purpose one. |
| Gain | `bimodal`, and both figures are stated rather than netted. It **costs** one instruction file per general-purpose subagent on surface A, and **saves** the parent every file the subagent read on surface B. The trade is won when the delegated reading exceeds the instruction file, which is almost always, and lost when a subagent is spawned for a small lookup. |
| Effort | S |
| Risk | none |
| Applies to | any |
| Controller | project / user |
| Source | harness documentation (axis C) |

### E-20 — The largest risk on this surface is one no byte count reports {#e-20}

| Field | Value |
| :--- | :--- |
| Surface | A |
| Family | F3 |
| Finding | Independent work measures accuracy falling as input length grows **with the evidence fixed and favourably placed** — a reported fall from 0.92 to 0.68 as input grew from a few hundred to three thousand tokens on one reasoning task, and separate work finding monitor models missing 2× to 30× more often after long benign transcripts. Instruction-file guidance repeats the same finding from the other side: longer files reduce adherence. A budget expressed in characters cannot see any of it. |
| Change | None. This is the reason [E-03](#e-03)'s remedy must be measured rather than obeyed: a cut that makes the agent guess costs more than it saves, and nothing in this method would report it. |
| Gain | `enabler` |
| Effort | n/a |
| Risk | none |
| Applies to | any |
| Controller | project |
| Source | external research (axis A) |

---

## Families with no finding

**A family with no finding against it is a result and is reported as one.**

| Family | Result |
| :--- | :--- |
| **F2 — redundancy and contradiction** | No portable finding. On the audited repository the one candidate duplication was a rule carried in two documents **with the governing document explicitly declaring which copy is the home and why**. That is a declared single home, not restatement. F2's first question — *which document should have had it* — already had an answer. |
| **F4 — model work that should be deterministic** | One portable finding only, folded into [E-05](#e-05): reading a generated file where a command exists. No second instance. |

---

## The technique catalogue and its search record

**A catalogue with no search record cannot be told apart from a short one.** The screening partition
below sums; summing is arithmetic over what was gathered and is not a coverage claim.

### Search record

| Axis | What it searched | Rounds | Stopped because |
| :--- | :--- | :--- | :--- |
| **A** | ideas, articles, papers | 7 | Round 7 (*techniques cut LLM agent context tokens coding assistant survey*; *how to make instruction file loaded every turn smaller*) returned only restatements of techniques already held — progressive disclosure, the 150–200-line guidance, "point elsewhere". **This is the recorded empty round.** |
| **B** | **named tools, by name** | 9 | Rounds 1–8 each added new names, including in the last productive round *Entroly*, *Mem0*, *SkillReducer*. Round 9 (*named tool trims agent startup context skill descriptions plugin catalogue*) returned curated skill lists and restated progressive disclosure, adding no technique. **This is the recorded empty round.** |
| **C** | **the harness's own documented mechanisms** | 5 | Rounds 1–4 were the highest-yield of the whole survey. Round 5 (*documented setting or environment variable that changes what enters context at startup*) added one item, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`, and otherwise restated tool search. Stopped there; **the round was not fully empty and is recorded as it was.** |

**Axis B produced the survey's single largest correction** — [E-08](#e-08) — exactly as the method
predicts. Axis C, which is easy to skip because it is documentation rather than research, produced
[E-03](#e-03), [E-09](#e-09), [E-10](#e-10) and [E-11](#e-11): four of the eleven findings, and the
only ones with a named, testable mechanism behind them.

### Screening — adopted, rejected, deferred

The three are a partition. A technique in none of them fails the audit.

| # | Technique | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| 1 | Prompt caching / cache-stable prefix ordering | **deferred** | Harness-controlled here. Closes if a project builds its own agent. Figures: cache reads at 10% of input rate; explicit breakpoints reported taking hit rates from 7% to 74% and from single digits to 84%. |
| 2 | Compaction (`/compact`, auto-compact) | **adopted** | Already available; the audit's contribution is [E-03](#e-03)'s risk field — path-scoped rules do not survive it. |
| 3 | Just-in-time retrieval (lightweight identifiers, load on demand) | **adopted** | The core of tiering. Vendor-published as a principle, not a figure. |
| 4 | Structured note-taking / external memory | **adopted** | Present as the auto-memory index. |
| 5 | Sub-agent architectures | **adopted with a cost** | See [E-11](#e-11): a subagent returns a 1,000–2,000-token summary and pays an instruction file to do it. |
| 6 | Progressive disclosure of skills (metadata → body → bundled files) | **adopted** | ~100 tokens per idle skill; body under 5k recommended. Measured instance: 858 bytes of payload per byte of description. |
| 7 | Path-scoped rules (`paths:` front matter) | **deferred** | [E-03](#e-03). Closes on one restart-and-observe test. |
| 8 | `@path` imports for splitting | **rejected** | [E-09](#e-09): loads at launch. Organisation only. |
| 9 | Block HTML comments in instruction files | **adopted** | [E-10](#e-10). |
| 10 | `disable-model-invocation` on a skill | **deferred** | User scope; the description leaves context and the skill stays invocable by name. |
| 11 | `disableBundledSkills` | **deferred** | User scope, and it removes a set the project did not choose. |
| 12 | Disabling installed-but-unused plugins | **adopted at user scope** | [E-02](#e-02). |
| 13 | MCP tool search / deferred tool schemas | **adopted, already on** | Vendor reports 85% reduction in tool-definition overhead; an independent implementation reported 96% on tool-heavy workloads. Observed active in this session: tool names listed, schemas fetched on demand. |
| 14 | MCP gateway / dynamic tool loading | **rejected** | No MCP server is on the audited project's critical path. |
| 15 | Code execution with MCP instead of tool calls | **rejected** | Same reason. Vendor reports 50–98%; the headline 98.7% is one scenario. |
| 16 | Global tool-output cap | **adopted as a technique, rejected on measurement here** | [E-07 below]. One practitioner reports an 8,000-character cap saved more than every other change combined. Measured here, a whole unit of work printed ~2,400 characters on a green run, so the cap would never fire. |
| 17 | Per-command quiet flags / wrapper scripts that strip boilerplate | **rejected on measurement** | Same evidence. Reported 40–60% on test, build and git output elsewhere. |
| 18 | Truncation-aware tool results (`maxResultSizeChars`, 25k-token default) | **deferred** | Matters only once outputs are large. Silent truncation is the hazard, not the cap. |
| 19 | Repo packing (Repomix, gitingest, code2prompt, files-to-prompt) | **rejected** | Concatenates whole trees: 50k–500k tokens on medium repositories. The opposite of tiering. |
| 20 | Tree-sitter compression of packed output | **rejected** | ~70% off a number that should not have been paid. |
| 21 | Graph-ranked repo map (aider) | **rejected** | ~1k tokens for a whole-repo map, but it is a code-navigation instrument and the audited surfaces are prose. |
| 22 | LSP-backed semantic code tools (Serena) | **deferred** | Real for code-heavy repositories. Figures are vendor-published; the independent convergence reported is about *call count*, not tokens. |
| 23 | Vector/hybrid code search as an MCP server (Claude Context) | **rejected** | Adds a server and an embedding provider to save a surface this project does not pay. ~40% claimed on large projects. |
| 24 | AST-based chunking | **rejected** | Same. |
| 25 | Prompt compression by a small model (LLMLingua, LLMLingua-2) | **rejected** | Up to 20× claimed; it rewrites text before it reaches the model, which forfeits the exactness that instruction files exist for. |
| 26 | Selective-Context / gist tokens / token-level pruning | **rejected** | Same class, same objection. |
| 27 | Code-specific pruning (SWE-Pruner, Long-CodeZip, DietCode, SlimCode, hierarchical context pruning) | **deferred** | Research-stage; applies to code context, not instruction context. |
| 28 | Minification of code before it enters context | **rejected** | −42% input tokens reported; the audited surfaces are markdown. |
| 29 | TOON and other compact encodings for structured data | **rejected** | 30–60% on structured data, 90%+ claimed on tabular; no structured payload on these surfaces. |
| 30 | RAG over documentation | **rejected** | Adds retrieval infrastructure to a corpus a command already indexes. |
| 31 | Model routing to cheaper models | **rejected** | Changes cost, not runway. The ranking axis is runway. |
| 32 | Hierarchical / tiered summarisation of long histories | **deferred** | 59% reported on agent memory; belongs to a memory layer this project does not run. |
| 33 | Ebbinghaus-style eviction from a memory store | **deferred** | Same. |
| 34 | Hard token budgeting with priority fill | **adopted in spirit** | This is what a tier-1 budget is. The reported 75% is against unbudgeted baselines. |
| 35 | Observation masking, and masking + summarisation hybrids | **deferred** | 7–11% improvements over either alone; needs a harness hook this project does not own. |
| 36 | Automatic tool-output compression | **deferred** | 40%+ claimed at 98.3% quality retention; vendor-published. |
| 37 | Reversible tool-output compression proxies (Headroom, Entroly) | **deferred** | 47–92% and "up to 90%" — both vendor-published, both on tool output, which [E-07] shows is not this project's cost. |
| 38 | Terse-output skills (Caveman) | **rejected** | [E-08](#e-08): advertised 65%, measured 8.5%, +7% on one benchmark. |
| 39 | Real-time multi-technique proxies (TokenShift) | **deferred** | 17 techniques behind one binary; no independent figure found. |
| 40 | Graph-based codebase indexing (Graphify, CodeGraph) | **rejected** | Code navigation again. |
| 41 | Semantic tool selection by embedding index | **deferred** | 82% reduction in tool descriptions and 89% fewer selection errors, from an independent research post — the strongest independently-sourced figure in the catalogue. Superseded here by tool search, which the harness already runs. |
| 42 | Skill optimisation by compression and restructuring (SkillReducer) | **adopted as evidence, deferred as a tool** | A study of 55,315 public skills found 26.4% with no routing description and **over 60% of body content non-actionable**; the tool reports 48% description and 39% body compression **with functional quality up 2.8%** — a measured less-is-more result. It is the strongest support in the catalogue for cutting a skill body, and it is why [E-16 in the project report] is worth testing. |
| 43 | `SessionStart` hook injecting state into context | **rejected** | It **adds** to tier 1. Listed because a reader looking for context mechanisms will find it and should know which direction it points. |
| 44 | `InstructionsLoaded` hook for observability | **adopted** | Not a saving. It is the **instrument** that makes tier 1 establishable by observation instead of by a file's claim about itself, and it is what settles [E-03](#e-03). |
| 45 | `claudeMdExcludes` | **deferred** | Skips ancestor instruction files by glob. Relevant to monorepos, not here. |
| 46 | `disabledTools` to drop built-in tool schemas | **rejected — the mechanism is not established** | A third-party figure of ~16,000 tokens for ~30 built-in tools (8% of a 200k window) circulates with this setting attached. The primary source found for the setting is an **open feature request**, not documentation. The figure may be right and the lever may not exist. Recorded so the next reader does not re-run the search. |

**Null result, recorded as an output:** the research changed no *inventory* figure. It changed four
*verdicts* — 8, 16, 17 and 38 — and supplied the mechanism behind [E-03](#e-03), [E-10](#e-10) and
[E-11](#e-11), none of which were visible from inside the repository.

### E-07 — Tool-output caps beat per-command tidying, and neither applies here {#e-07}

| Field | Value |
| :--- | :--- |
| Surface | C |
| Family | F5 |
| Finding | Practitioners report a **global per-call output cap** as the single largest saving they measured, ahead of per-command quiet flags and boilerplate-stripping wrappers, with 40–60% reported on test, build and git output. Measured on the audited project 2026-08-15, a complete unit of work printed about **2,400 characters** on a green run — next item 95, task context 740, validator 412, index 46, whole suite 355. A cap set anywhere useful would never fire. |
| Change | For a project whose green output is large: set the cap first, tidy commands second. For this one: nothing. |
| Gain | `L` where output is large; **zero here, and the zero is measured, not assumed** |
| Effort | S |
| Risk | Silent truncation. A capped result the agent reasons over without knowing it was cut is worse than a long one. |
| Applies to | any |
| Controller | user / harness |
| Source | external research (axis A) + this audit |

---

## Local precedent — patterns that survived contact with real work

Structures only. Nothing was copied, and no path or machine datum crossed from the precedent.

| | Pattern | Observed | What it buys |
| :--- | :--- | :--- | :--- |
| **P1** | Stub, canon, depth | **yes** | A small always-loaded file points at one method document, which points at heavy references. The stub saves little; the layer below it is what saves. |
| **P2** | One file per lifecycle phase | **yes** | 7 phase files, 3,237–5,844 bytes, mean 4,306, against a 7,443-byte spine. A session in one phase loads one. |
| **P3** | Rationale in its own document | **yes** | 3,237 bytes, cited from the operative steps. The F3 tension resolves without deleting anything. |
| **P4** | Evidence quoted forward | **not observed as a structure** | The project records evidence in the task's `implement` section, which is the same effect by a different route. |
| **P5** | One body, thin per-agent front-ends | **not applicable** | One agent. |
| **P6** | Spine plus one branch, never both | **yes** | Two binding documents, 14,425 and 13,905 bytes; a run loads one. **13,905 bytes present and not paid.** |

**Four of six, implemented before this audit ran.** That is the most useful thing the precedent
section reports: the patterns are not proposals here, they are the reason the load path is already
small enough that the findings above are mostly about the harness rather than the repository.

---

## Where the numbers came from

All figures dated **2026-08-15**. **Record absolute bytes plus the date and derive the share** — a
share is two measurements and the denominator usually moves faster than the numerator.

Measurement was done by a throwaway program outside the audited repository. Sizes came off the
filesystem; command output was captured to files whose lengths were measured without printing them.
Opening a file to find out how big it is spends the exact budget under audit.

Two partitions were checked rather than trusted:

- The task-corpus section partition summed to 2,431,428 against a real 2,430,672 — **+756, 0.03%**,
  accounted for by heading-delimiter arithmetic and reported rather than hidden.
- The document section partitions summed within +3 to +11 characters of each file's real length.

**The unit is characters, not bytes, wherever a verdict depends on it.** On the audited repository
the two units disagree about a verdict, because one file is denser in multi-byte punctuation than
the other; counting bytes flattered tier 1 by enough to reverse the answer.
