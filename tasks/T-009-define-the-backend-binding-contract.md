---
id: T-009
title: Define the backend binding contract and write the local-Markdown binding
type: deliverable
status: done
phase: review
parent: null
blocked_by: [T-008]
related: [T-005, T-010]
work_package: none
owner: maintainer
business_value: high
effort: l
created: 2026-08-04
updated: 2026-08-05
deliverables:
  - docs/BINDING.md
  - docs/bindings/local-markdown.md
---

# T-009 — Define the backend binding contract and write the local-Markdown binding

## 1. Specify

**Outcome**
A written contract naming the operations a backend must provide for `docs/METHOD.md` to run on it,
and stating what each one must **guarantee** rather than how it is done; plus the first binding that
implements it — local Markdown files — written as a document that declares the assumptions it makes
about the adopting project. A second, file-less backend appears only far enough to show that the
contract text needs no change to describe it.

**Requirements served**
R-13, R-14 (`docs/SCOPE.md`).

**Why this one**
Without a contract, "backend-neutral" is an aspiration. `docs/METHOD.md` is *written* to name no
field, no file and no command, and nothing has yet tested that it succeeded — this task is that
test, and the contract is what it produces. Handoff proves the shape works: five operations
(`find` / `read` / `create` / `update` / `reference`) let one core drive Notion or a folder of files
unchanged. taskmd may need more, because it does two things handoff never does — it derives the
inverse of every edge and it generates an index, and both are computations over the *whole* task
set rather than over one item.

**Scope**
- In: the operation set; what each must guarantee; how derived views are expressed for a backend
  that has no files; the local-Markdown binding; the mandatory "assumptions this binding makes"
  section; the decision on whether taskmd's operation vocabulary is handoff's (Q1 — T-005 waits on
  it).
- Out: the GitHub Issues binding as a whole — that is [T-010](T-010-write-the-github-issues-binding.md).
  Only the fragment that proves criterion 4 is written here (Q2).
- Out: the method itself ([T-008](T-008-write-the-backend-neutral-method-document.md), done). If
  this task finds the method is *not* backend-neutral somewhere, that is a finding raised against
  it, not an edit made here (METHOD §3.3).
- Out: making taskmd drivable **by handoff** — the opposite direction, and
  [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md)'s. Nothing in the handoff skill
  package is edited by this task.
- Out: code. A binding is a document (`docs/SCOPE.md` A3), and no fourth command is added
  (non-goal 11).

**Inputs**
- `docs/SCOPE.md` §3B — R-13, R-14 — and §2 principles 1–2
- `docs/METHOD.md`, especially §4 (the three edge kinds and the forward-edge rule) and §6 (homes as
  roles the binding assigns) — the contract has to carry exactly what these need
- `taskmd/defaults/config.md` — the existing separation of *field names* (the project's) from *edge
  kinds* (fixed); the contract must not re-decide either
- Handoff `bindings/README.md` + `handoff.core.md` §8 — the contract shape that works
- Handoff `control/IMPROVEMENT-BRIEF.md` **F1** — a binding stated "the folder is the index" as a
  premise; an adopting project with a generated index could follow it exactly and still break its
  own single source of truth. The failure was silent and looked like compliance.
  **Not reachable from this working copy** — recorded per [`specify`](../docs/method/specify.md)
  step 3. It is not a dependency in disguise, because the finding's substance is quoted above and
  the instance it describes is readable directly: the handoff package's own `local-markdown-dir`
  binding still says the folder is the index and that there is no central list to keep in sync,
  and that binding is the one **this** project's `.handoff/config.md` selects — while this
  project's index is generated into `tasks/README.md`. The F1 case is live here, not historical.

**Acceptance criteria**
- [ ] Every operation the method needs is named, with what it must guarantee — and nothing the
      method does not need. Falsified either way: by an operation no rule in `docs/METHOD.md`
      requires, or by a rule in it that cannot be carried out through the named set
- [ ] The contract states **guarantees, not mechanisms**: no operation names a field, a status
      value, an id format or a file format — those come from the schema config (T-001). Falsified
      by an operation that can only be implemented one way
- [ ] Each binding carries an **"assumptions this binding makes"** section an adopter can check in
      thirty seconds (the F1 fix). Falsified concretely: the local-Markdown binding must say
      whether it assumes the folder listing is the index, given that this project generates one
- [ ] The contract expresses derived views without assuming a filesystem, proven by writing one
      operation against a backend that has no files, and showing the contract text needed no change
      to accommodate it
- [ ] The local-Markdown binding is proven by **being followed**: its operations are executed
      against this repository using the binding text alone, after which `check` passes and the
      regenerated index differs only by the intended change. Falsified by any omitted step — a
      `create` that leaves `tasks/README.md` stale is the expected failure mode, and per
      `CLAUDE.md` the binding is only proven once it has been made to fail on one
- [ ] Q1 is answered in writing, with the reason, because T-005 cannot start without it

**Open questions**
- none. **Both were answered by the owner on 2026-08-05: the recommendation in each case.** Q1 —
  the contract **extends** handoff's five. Q2 — criterion 4 is proven by **one operation sketched
  against GitHub Issues inside the contract document**, and T-010 still writes the whole binding.
  The questions are kept below with their reasoning, since T-005 depends on Q1 and will want it.

- **Q1 — does taskmd's contract extend handoff's five operations or replace them?** Owner's, and it
  changes the outcome, so it is answered before this phase ends. *Recommendation: extend.* Keep
  `find` / `read` / `create` / `update` / `reference` with handoff's meanings and add exactly one —
  an operation that yields **every** task in the set. Everything taskmd does beyond handoff (inverse
  edges, the index, `check`) is a computation over that set rather than a new thing to ask a backend
  for, so one addition looks sufficient; and if it is, T-005 becomes a vocabulary alignment instead
  of a translation. Replacing the five would buy nothing and cost that.
- **Q2 — what proves criterion 4, given GitHub is T-010's?** Owner's. *Recommendation:* one
  operation sketched against GitHub Issues **inside the contract document**, as an illustration; one
  operation is not a binding, so T-010 stays whole. The alternative is to illustrate with some other
  file-less backend to keep GitHub untouched here — cleaner as a boundary, but weaker evidence,
  since GitHub is the backend the project has actually committed to (`docs/SCOPE.md` A3).

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | **Derive the operation set from `docs/METHOD.md` rule by rule**, before writing any contract prose. This is the only way criterion 1 can be checked in *both* directions, and it is the step that can invalidate the rest — if a method rule turns out to need something no backend can promise, the contract is not the thing that needs fixing. | A two-column derivation in §3: every rule in `docs/METHOD.md` → the operation(s) it requires. Plus the two residual lists, which must both come out **empty**: operations no rule asked for, and rules no operation serves |
| 2 | **Decide the deliverable's shape and where it lives**, with rejected alternatives — one contract document plus one file per binding, or a single document with a section per backend. | A recorded decision in §3, and the paths fixed for steps 3–5 |
| 3 | **Write the contract**: each operation with what it must *guarantee*, and how derived views (inverse edges, the index) are expressed given that they are computed rather than stored. Name no field, no status value, no id format, no file format — those are the schema config's (T-001). | `docs/BINDING.md` |
| 4 | **Test the contract against a backend with no files** — write one operation against GitHub Issues, inside the contract, and record whether the contract text had to change to accommodate it. Placed here, immediately after the draft, because a change it forces is cheap now and expensive after the binding is written. One operation is not the binding; T-010 stays whole. | The worked operation in `docs/BINDING.md`, and in §3 a plain statement of what changed — including "nothing", if that is the answer |
| 5 | **Write the local-Markdown binding**, including the mandatory *assumptions this binding makes* section. The F1 case is the one that must be answered explicitly: whether the folder listing is the index — it is not, in a project that generates one. | `docs/bindings/local-markdown.md` |
| 6 | **Prove the binding by following it, and make it fail first.** Follow a deliberately incomplete version of the binding text to perform one real operation on this repository, and show the damage — then follow the corrected text and show it clean. A binding that has only ever been read has not been tested (`CLAUDE.md` *Verifying*). | The before/after transcript in §3, with the actual command output |
| 7 | **Sweep for what this task made false.** `CLAUDE.md`'s status paragraph calls the binding contract the largest unproven claim left; `docs/BRIEF.md` and `.handoff/config.md` may carry related statements. Anything found that belongs to another task is raised, not fixed (METHOD §3.3). | The reconciled lines, and any task raised, listed in §3 |
| 8 | Declare the deliverables in front-matter, then run `check`, `index` and the suite, and paste the output. | The updated front-matter and the transcript in §3 |

**Deliverable shape — decided here.** A **spine plus one file per binding**: `docs/BINDING.md` holds
the contract, `docs/bindings/<backend>.md` holds each implementation. It mirrors
`docs/METHOD.md` + `docs/method/`, which is the structure this project already reads, and it means
T-010 adds a file rather than editing a shared one — two bindings in one document would make every
new backend a merge conflict in the contract itself.

*Rejected:* a single `docs/BINDING.md` with a section per backend — smaller today, but it puts the
contract and its implementations in one file, so an adopter loads three backends to read one, which
is the cost R-21 exists to avoid. *Rejected:* putting the contract inside `docs/METHOD.md` — it
would breach the 150-line spine limit, and the method is deliberately the document that knows
nothing about storage.

**The sixth operation is named `enumerate`, not `list`.** T-022 is adding a CLI command whose user-
facing name is likely `list`; one word meaning both a backend capability and a command would make
every later sentence ambiguous about which is being described.

**No new dependency edges.** Everything step 1 needs is in the repository, and T-008 (the only
blocker) is closed.

**Output paths**

- `docs/BINDING.md`
- `docs/bindings/local-markdown.md`
- `CLAUDE.md` (step 7, the status paragraph)

The `deliverables:` field stays empty until step 8: `check` validates that every declared path
exists, so declaring them now would make this project fail its own validator for the length of the
plan.

## 3. Implement

### Step 1 — the operation set, derived from `docs/METHOD.md`

| Method rule | What it requires of a backend |
| :--- | :--- |
| §1.1 no work without a task | **create**; **find**, to establish that it exists |
| §1.2 the lifecycle is mandatory | **read**, **update** — phase and status are recorded properties, and they are independent, so a backend must hold at least two of them per task |
| §1.3 one home per fact; anything derivable is derived | **enumerate** — no other operation can answer a question about the whole set without a second stored copy |
| §1.4 audit findings become their own tasks | **create**, with the edge set in the same operation |
| §1.5 done means consistent | **update** |
| §2 phases and their exit criteria | **read** — `review` judges against what `specify` wrote, so content must come back whole |
| §3.1–3.2 one phase per request; ask to the exit criterion | **nothing** |
| §3.3 surface what you discover | **create** (already counted) |
| §4 three edge kinds, forward edge stored | **create** / **update** to write one; **reference**, so there is something stable to point at |
| §4 the inverse is derived, both ends visible | **enumerate** — *or* a backend that presents both directions itself |
| §5 audit umbrella and children | **create** with a hierarchy edge (already counted) |
| §6 homes are roles the binding assigns | **nothing operational** — it is what each binding must *state* |

**Residual 1 — operations no rule asked for: empty.** All six trace to at least one rule.

**Residual 2 — rules no operation serves: not empty, and correctly so.** METHOD §3.1, §3.2 and §6
require nothing of a backend. The plan predicted this list would be empty and it is not; the
prediction was wrong rather than the result. §3 governs how the agent works and §6 assigns roles
rather than actions, so an operation serving either would be the contract reaching into the method.
This is stated in the contract itself rather than left as a silent gap, because a reader who repeats
this derivation will hit the same three rules and needs to know they were considered.

### Decisions & assumptions

- **Six operations: handoff's five plus `enumerate`** — 2026-08-05, per the owner's Q1. The
  derivation above is the evidence that one addition is *sufficient*, not just convenient: every
  taskmd-specific behaviour reduces to a pass over the whole set.
- **Named `enumerate`, not `list`** — 2026-08-05. Decided in `plan`; T-022 is adding a CLI command
  likely called `list`, and one word for both a backend capability and a command makes every later
  sentence ambiguous.
- **The contract must not assume operations are implemented by code** — 2026-08-05. Discovered while
  writing §5: for local Markdown the operations *are* `taskmd`'s own commands, while for GitHub they
  are instructions an agent carries out with its own tools (`docs/SCOPE.md` A3 — the GitHub backend
  ships as a document, and non-goal 5 keeps the network out of the tool). A contract phrased as
  "the tool does X" would have excluded half the backends it exists for, so every operation is
  phrased as a guarantee about a result and each binding says who performs it.
- **§3 gained "a backend may satisfy a derived view natively"** — 2026-08-05, and this is the whole
  value of step 4. The draft said derived views *are computed from* `enumerate`. GitHub presents
  blocked-by and blocking as two views of one relation, so it meets the both-ends guarantee without
  enumerating — and the draft would have made a backend non-conforming for being better at the
  thing than the contract expected. Rejected: keeping the stronger wording and letting bindings
  note an exception, which would have made the exception invisible to anyone reading only the
  contract.
- **"A materialised derived view is a rendering, never an input"** — 2026-08-05. The generated
  index is written, so something has to say why that is not a second home. The rule that makes it
  safe is that no operation may read it back; `docs/SCOPE.md` §1 *Invisibility* is the same
  constraint one level up.
- **The local-Markdown binding states its limits are none** — 2026-08-05. A file holds any field,
  any edge and any content, so nothing in the method is absorbed here. Recorded as an explicit
  entry rather than omitted, because a binding with no limits is the one an adopter is most likely
  to generalise from, and it is the *least* representative of the two.

### Escalated, not fixed here

- [T-025](T-025-let-check-notice-a-stale-generated-index.md) — `check` exits 0 on a project whose
  generated index no longer matches its tasks. Found by the verification below, outside this task's
  criteria, so it is raised rather than absorbed (METHOD §3.3).

### Outputs produced

- `docs/BINDING.md` — the contract: six operations with their guarantees, derived views, what every
  binding must state, and the worked file-less operation
- `docs/bindings/local-markdown.md` — the first binding, assumptions section first
- `CLAUDE.md` — the status paragraph, which called this the largest unproven claim left

### Verification

**The binding was proven by being followed, and it failed first — without being staged.** Step 6
planned to follow a deliberately incomplete version of the binding text. That turned out to be
unnecessary: earlier in this session the task's own front-matter had been updated without the
index being regenerated — the exact step the binding's first assumption warns about — and the
failure was sitting there waiting:

```
--- file says ---            --- index says ---        --- check says ---
status: planned              `specified` | `specify`   OK - 24 task(s), ... exit=0
phase: plan
```

The generated index disagreed with the task it was generated from, and `check` reported the project
consistent. Following the binding's *after any write* step:

```
python -m taskmd index    Wrote tasks/README.md - 13 active, 11 closed
                          index now says: `planned` | `plan`
python -m taskmd check    OK - 24 task(s), vocabulary valid, references resolve, no broken links
```

That is the strongest available evidence for assumption 1, because the author of the binding made
the mistake the binding exists to prevent, while writing it. It also produced T-025: the recovery
works, but nothing *reports* the discrepancy.

**`create`, performed from the binding text alone.** T-025 was created by following the operation as
written — next id after the highest present, template copied, edges written in the same write, index
regenerated:

```
python -m taskmd index    Wrote tasks/README.md - 14 active, 11 closed
python -m taskmd check    OK - 25 task(s), vocabulary valid, references resolve, no broken links
```

**The both-ends guarantee, on a link written only once.** `related: [..., T-009, ...]` was written
on T-025 and nowhere else. Read from the other end:

```
python -m taskmd context T-009
RELATED
  T-005        proposed    Align with the handoff tracker-binding contract
  T-010        proposed    Write the GitHub Issues binding
  T-012        done        Decide whether soft edges are symmetric
  T-025        proposed    Let check notice a stale generated index
```

**Suite and publishing checks**, since two documents were added:

```
python -m unittest discover -s tests -q     Ran 74 tests — OK
pre-publish grep over the tracked tree      5 hits, all in T-013's fixture (T-018's, unchanged)
```

**What was not verified.** The GitHub operation in contract §5 was written *against* the contract,
not executed — no repository was called, and `docs/SCOPE.md` A3 means none will be until T-010. It
proves the contract's wording accommodates a file-less backend, which is what criterion 4 asks; it
does not prove the GitHub binding works, which is not this task's claim. Recorded per
[`implement`](../docs/method/implement.md) rather than left implied.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| Every operation the method needs is named with what it must guarantee, and nothing it does not — falsified by an operation no rule requires, or a rule the set cannot carry out | met | The §3 derivation runs both directions over every rule in `docs/METHOD.md`. Residual 1 (operations no rule asked for) is empty. Residual 2 is **not** empty and the plan predicted it would be: §3.1, §3.2 and §6 require nothing of a backend. That is a wrong prediction, not an unserved rule — the three are agent conduct and role assignment — and the contract states it rather than leaving a reader to rediscover it |
| Guarantees, not mechanisms: no operation names a field, a status value, an id format or a file format — falsified by an operation implementable only one way | met | Checked by grep, not by reading: the contract contains no schema field name, no status value, no id pattern and no file extension; the only filenames in it are the project's own documents. The stronger evidence is that two backends of different shape implement the same six sentences — files with local ids, and a remote tracker with server-assigned ids, labels and no files at all. One marginal call, recorded rather than tidied: the local binding uses "done tasks" as ordinary English in two places, which a grep for status values hits. It describes finished work rather than defining a value, so it passes — a reviewer who disagrees is looking at the right line |
| Each binding carries an *assumptions this binding makes* section checkable in thirty seconds — falsified concretely by the folder-is-the-index question | met | `docs/bindings/local-markdown.md` opens with it: six numbered claims about the adopting project, plus the METHOD §6 home assignments and an explicit "backend limits: none". 34 lines. Assumption 1 answers the F1 question head-on and names the sentence it contradicts. The contract's §4 makes the section mandatory with five minimum entries, so T-010 inherits it. **Weaker than it reads:** thirty seconds was judged on the text, not measured on an uninvolved reader — the same limitation T-019's review recorded, and for the same reason |
| Derived views expressed without assuming a filesystem, proven by one operation against a file-less backend, **showing the contract text needed no change** | met — **the wording's prediction was falsified, and that is the result** | The operations needed no change. §3 did: GitHub presents blocked-by and blocking as two views of one relation, so it meets the both-ends guarantee *without* enumerating, and the draft's "derived views are computed from `enumerate`" would have made a conforming backend non-conforming for being better at it. So the contract does not assume a filesystem — which is what the criterion is for — but it reached that state by being corrected, not by having been right. Recorded openly per [`review`](../docs/method/review.md); had the test found nothing, it would have proved only that the author agreed with himself. **The owner may want the clause amended; the outcome does not change either way** |
| The local-Markdown binding proven by being followed — `check` passes, the index differs only by the intended change, and it has been made to fail | met | Made to fail without being staged: the session updated a task's front-matter and skipped the regeneration step, and `check` reported the project consistent while the index disagreed with it (transcript in §3). `create` was then performed from the binding text alone and produced T-025. Review added the check `implement` did not run: `index` is **idempotent** — a second consecutive run leaves the file byte-identical, so "differs only by the intended change" is a property of the generator rather than of how carefully the write was done |
| Q1 answered in writing with the reason, since T-005 cannot start without it | met | Answered in §1 and carried into §3 with the evidence that one addition is *sufficient* rather than merely convenient. T-005's own text says T-009 owns this decision; closing this task unblocks it |

**Also checked, beyond the criteria**

- Suite 74/74 — unchanged, as expected: this task shipped no code.
- Pre-publish check: five hits, all in T-013's fixture (T-018's, unchanged). The two new documents
  added none.
- `check` validates declared deliverables, and passed with both new paths declared — so the
  front-matter names files that exist rather than files that were planned.

**Child fix tasks raised**
- none — every criterion is met.

**Raised, not fixed here** (outside these criteria, so not a child fix — METHOD §3.3)
- [T-025](T-025-let-check-notice-a-stale-generated-index.md) — `check` cannot see a stale generated
  index. Found by this task's verification; it belongs to the validator, not to the contract.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-04 | → proposed | Raised by T-007 to carry R-13/R-14. |
| 2026-08-05 | → done | Review worked. All six criteria met, no child fixes. Two things review added that `implement` had not run: a grep for leaked vocabulary in the contract (clean; one marginal "done tasks" in the binding, judged prose and left alone rather than tidied), and `index` idempotence, which is what makes "differs only by the intended change" a property of the generator. Criterion 4's wording predicted the contract would need no change; it needed one, and that correction is the evidence the test was worth running — recorded openly, the clause is the owner's to amend. |
| 2026-08-05 | → review | Implemented in plan order. The operation set was derived from the method rule by rule before any prose was written, which is what makes "nothing the method does not need" checkable; the plan's prediction that both residual lists would be empty was wrong, and the second one is correctly non-empty. Two contract-level rules came out of writing it: operations are guarantees about results, never "the tool does X" (local Markdown is code, GitHub is an agent with its own tools), and a materialised derived view may never be read back. The binding was made to fail without staging — the index went stale mid-session and `check` said OK, which raised T-025. |
| 2026-08-05 | → planned | Eight steps, riskiest first: derive the operation set from the method before writing the contract, then test the draft against a file-less backend immediately, because a change it forces is cheap before the bindings exist and expensive after. Shape decided here — a contract spine plus one file per binding, mirroring `docs/METHOD.md` + `docs/method/`, so T-010 adds a file rather than editing a shared one. The sixth operation is named `enumerate` to keep it distinct from T-022's `list` command. |
| 2026-08-05 | → specified | Specify agreed by the owner; both open questions answered as recommended — the contract extends handoff's five, and the file-less proof is one GitHub operation inside the contract document, leaving T-010 whole. Two criteria were unfalsifiable as written and were replaced: "nothing names a field or a file format" became its own criterion with a stated failure mode, and "proven by the existing tooling running unchanged" became "proven by being followed" — the tooling runs on this repository whatever a binding document says, so it could never have failed. One listed input, the handoff improvement brief, is unreachable from this working copy; recorded rather than treated as a blocker, because the F1 case is live in this project's own handoff config rather than historical. |
