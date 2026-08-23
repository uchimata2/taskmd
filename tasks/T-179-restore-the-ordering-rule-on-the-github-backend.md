---
id: T-179
title: Restore the what-next ordering rule on the GitHub backend
type: deliverable
status: done
phase: review
parent: null
blocked_by: []
related: [T-022, T-108, T-178]
work_package: M6
owner: maintainer
business_value: medium
effort: s
created: 2026-08-18
updated: 2026-08-19
adopter_visible: yes
deliverables: [plugin/skills/taskmd/docs/bindings/github-issues.md]
---

# T-179 — Restore the what-next ordering rule on the GitHub backend

## 1. Specify

**Outcome**
A procedure in the GitHub Issues binding that answers *what should I work on next* by the project's
own stated ordering rule, so a migrated project keeps the question rather than handing it back to a
person.

**Why this one**
**The binding currently records this as a loss and stops there**: `list --open --limit 1` answered
what to work on next "by a stated rule — blocked last, then effective value, then effort, then id",
and GitHub "sorts by number, recency or whatever a saved filter says. The question does not
disappear; it goes back to a person."

**But the rule is stated, and every input it needs is already in the binding's own `enumerate`
output.** That command returns labels, `blockedBy` and the body, and the body carries the property
block verbatim — so effective value, effort and blocked-ness are all there. Nothing is missing but
the sorting, which is why this is a document and not a feature.

**It matters more than it looks, because of what the ordering rule is for.** `docs/SCOPE.md` non-goal
11 records why the filtered listing was let in at all: not convenience, but token efficiency — an
agent that must read every task to find the next one has already spent what the tool exists to save.
A migrated project reading its whole issue list to choose is in exactly that position, and it is the
position §1 is written against.

**Scope**
- In: the ordering rule, restated as something an agent runs against `enumerate`'s output
- In: what the rule cannot reproduce here, stated rather than glossed
- Out: a command, a flag, or anything in the core. Non-goals 5 and 11
- Out: changing the ordering rule itself. It is the local backend's and this task carries it across
  unchanged; if it is wrong, that is a different task about
  [T-022](T-022-filtered-task-listing-for-scripts.md)

**Inputs**
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — *Operations*, `enumerate`, and the
  *What is gone* item this task would make partly false
- [T-022](T-022-filtered-task-listing-for-scripts.md) — the ordering rule and why the listing exists
- `plugin/skills/taskmd/taskmd/cli.py` — `is_blocked` and the ordering it feeds, which is the
  authority on what the rule actually is

**Acceptance criteria**
- [ ] The binding carries a procedure that produces the same order as the local rule, stated as
      steps somebody can run against *enumerate*'s output
- [ ] It reads the **four keys in the right order**, and the ranking is taken from the project's own
      config row rather than from a number written here — a second table mapping value to number is
      the duplication `## Ordering` refuses by name
- [ ] What the procedure **cannot** reproduce is named, item by item, rather than covered by a
      general caveat
- [ ] The *What is gone* item that says the ordering has no replacement no longer says something the
      document now contradicts, and what it said before stays legible
- [ ] The `list` row of the replacement table agrees with both
- [ ] The rule itself is unchanged — the local backend's four keys, carried across, not improved

**Open questions**
- ~~**Is a restated rule a second home for it?** The rule lives in the tool's code and would now
  also be described in a binding, which is the duplication `CLAUDE.md`'s one design rule exists to
  stop. The counter is that a binding is a mapping document and describing the local behaviour is
  what every other operation in it already does. **The maintainer decides**, because it is a
  judgement about the rule this project is most careful with.~~ **Answered by the owner on
  2026-08-19: describe it in the binding** — see the Log row of that date, which also records the
  amendment to the design rule that came with the answer and left as
  [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md).

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the rule from its one home, the config's `## Ordering`, and the code that implements it, and confirm the two agree before restating either | The four keys, confirmed in §3 |
| 2 | Check each key against what *enumerate* actually returns, so the procedure is not written against fields this backend does not have | The input map, in §3 |
| 3 | Write the procedure into *Operations*, beside the other five | The edited binding |
| 4 | Name what the procedure cannot reproduce, from what step 2 exposed rather than from imagination | The limits, in the same section |
| 5 | Reconcile the two places that say the ordering is lost — the *What is gone* item and the `list` row | The edited items |
| 6 | Run `check`, `index` and the suite, and read the diff to confirm nothing else in the document moved | The output and the diff verdict, in §3 |

**Decisions taken at `plan`**

- **The procedure is a new operation, `order`, and not a paragraph inside `enumerate`.** The
  binding's contract is a set of named operations, and a rule the skill has to find is worth a name.
  *Rejected: extending `enumerate`'s description*, which buries the one thing this task exists to
  restore inside the operation it depends on. — 2026-08-19
- **The ranking is read from the reader's own config row, never written out here.** `## Ordering`
  refuses a second table mapping a value to a number by name, and this document copying one would be
  that table. *Rejected: listing `critical > high > medium > low`*, which is shorter to read and is
  the exact duplication the rule names. — 2026-08-19
- **The *What is gone* item is corrected in place with its old text quoted**, the same shape
  [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) used the same
  day: it is a live claim about the backend, and it is also a record of what was believed when the
  document shipped. — 2026-08-19

**Outputs this task will produce**

- plugin/skills/taskmd/docs/bindings/github-issues.md

## 3. Implement

### Step 1 — the rule, from its one home

`## Ordering` in the schema config states it and says the code implements it without restating it.
`cli.py`'s `order` agrees key for key:

```python
return (is_blocked(schema, tasks, task), values[task.id], effort, task.id)
```

Blocked last, then effective value, then effort, then id. **Effective value is the interesting one**
and the config says why: it is the best value among the task *and everything it transitively
unblocks*, which is what pulls a cheap blocker ahead of the valuable work waiting on it.

### Step 2 — each key against what `enumerate` returns

| Key | Local input | On this backend |
| :--- | :--- | :--- |
| blocked | an open dependency edge | `blockedBy`, filtered to issues still open |
| effective value | the value field, improved through the derived inverse | the value label, improved through `blocking` |
| effort | the effort field | the effort label |
| id | the task id | the issue number |

**Every key is present, which is what makes this a document rather than a feature** — and the check
was worth running rather than assuming: the inverse edge is what effective value walks, and on the
local backend it is *derived*, so the question was whether this backend has it at all. It does,
under `blocking`, and *enumerate* already asks for it.

**Read the label, not the body.** The body carries the property block verbatim and that was the
tempting source, since §1 names it. It is a rendering: the binding's rule 2 makes the label the fact,
and a procedure reading the body would disagree with every other operation the first time somebody
edited one.

### Step 3–4 — the procedure, and its limits

Written into *Operations* as **order**, after *enumerate* and before *After any write*. The three
limits are named individually rather than as a caveat, and each came out of step 2:

- a `blockedBy` cycle, which the local command tolerates only because `check` reports it separately;
- a stale `blockedBy`, because both directions are GitHub's here and nothing reconciles them;
- an absent label, which the local backend's validator would have reported.

### Step 5 — the two places that said it was lost

*What is gone* item 2 becomes **No ordering *command***, keeping its original sentences and gaining
a dated correction that points at the new operation. The `list` row of the replacement table said
*the ordering does not survive*; it now says the enumeration and the ordering both do, as a procedure
rather than a command.

### Step 6 — verification

```text
Wrote tasks/README.md
OK - ... task(s) ...
Ran 288 tests ... OK
```

The document's diff is **three hunks**: the new operation, the `list` row, and the *What is gone*
item. Nothing else in the file moved, checked by reading the diff rather than by intending not to.

**Decisions & assumptions**

- All three `plan` decisions held. — 2026-08-19
- **The rule is carried across unchanged, including the parts that look improvable.** Reading it
  closely raised two temptations — hiding blocked issues, and treating a missing estimate as the
  cheapest rather than the dearest — and §1 puts both out of scope: they are the local rule's, and
  changing them here would fork the behaviour rather than mirror it. — 2026-08-19
- **Assumption, recorded as one**: the procedure has not been run against a live issues-backed
  repository. It is written from *enumerate*'s documented output, and the field names come from the
  command in this document rather than from a response. Standing verification of this binding is
  [T-178](T-178-give-the-github-binding-a-standing-verification.md) and a live run is
  [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md). — 2026-08-19

**Outputs produced**
- plugin/skills/taskmd/docs/bindings/github-issues.md — the `order` operation, the `list` row, and
  the corrected *What is gone* item

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A runnable procedure producing the same order | **met** | *order*, in *Operations*. Four numbered keys against *enumerate*'s output, in the local rule's order |
| Four keys in the right order, ranking from the reader's own config row | **met** | §2's second decision. `critical` outranks `high` *because it is written first*, and no value-to-number table is copied |
| What it cannot reproduce is named item by item | **met** | Three limits, each traced in §3 to what step 2 exposed rather than to a general worry |
| The *What is gone* item no longer contradicts the document, and its old text stays legible | **met** | Item 2 is now *No ordering command*, with the original sentences kept and a dated correction under them |
| The `list` row agrees with both | **met** | It now reads *enumerate above, then order*, and says the ordering survives as a procedure |
| The rule itself is unchanged | **met** | §3's second decision names the two changes that were tempting and refused, and why each would be a fork rather than a mirror |

**Open questions, re-read before closing** (procedure step 5)

§1's only question was answered by the owner on 2026-08-19 and is struck through there. The second
instruction that came with that answer — amending the one design rule — was already routed to
[T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) and is not this task's.
Nothing else here is addressed to anyone else.

**The assumption above is the honest gap and `review` names it rather than the record hiding it.**
This procedure is written from a documented command's output, not from a response, and nobody has
run it. That is what [T-178](T-178-give-the-github-binding-a-standing-verification.md), the next task
in this session's order, exists to make impossible to leave unnoticed.

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-19 | → done | `specify` through `review` in one session under the eight-task grant, this being number 5 of the eight. The binding gains an **order** operation: the local backend's four keys — blocked last, effective value, effort, issue number — run against `enumerate`'s output, which already returns every input they need. The check that mattered was whether `blocking` is there, because effective value walks the inverse edge and on the local backend that edge is *derived*; it is, and `enumerate` already asks for it. The ranking is read from the reader's own config row and never copied as a value-to-number table, which `## Ordering` refuses by name. Two places said the ordering was lost and both are reconciled, the *What is gone* item keeping its original text under a dated correction. **The honest gap is named in §4**: this is written from a documented command's output and nobody has run it against a live repository. |
| 2026-08-19 | (no change) | **The owner authorised the whole lifecycle for this task** — `specify` → `plan` → `implement` → `review` — on 2026-08-19, as the subject of a handoff written the same day. The grant names **eight tasks, run in a fixed order**: T-184, T-170, T-174, T-151, T-179, T-178, T-185, T-093; this is **number 5 of the eight**. It covers **these eight and nothing any of them raises**, matching the two grants before it. **It is explicitly unattended**, with one instruction attached in the owner's own words: where a question or trouble arises, record it in the task it belongs to and move to the next task rather than stopping. So a blocked phase ends in a written question here, not in a halted batch — and a question recorded under this grant is **not** answered by it. Recorded in this record as well as in the handoff, because a handoff is consumed once and renamed (METHOD §3.1, and [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) which settled where this goes). |
| 2026-08-19 | (no change) | **The open question is answered by the owner: describe the rule in the binding.** Asked in the backlog-wide round of 2026-08-19. The reason is the one §1 already carried — a binding is a mapping document, and describing local behaviour is what every other operation in it already does. *Rejected: pointing at the code instead*, which is the strictest reading of the design rule and leaves whoever implements this backend reading Python to learn the one behaviour that decides what people work on. **The owner attached a second instruction, and it is not this task's to carry**: the design rule itself is to be amended to say that single source of truth is the *goal* — its purpose being to minimise inconsistency and unnecessary administration — and that a system configuration or a comparable limitation is grounds to deviate from it. That amendment lands in the rule's own home and changes every design decision in the project rather than this binding, so it is raised as [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) rather than widened into here. This task does not wait on it: the answer above stands on the binding's own precedent. This row is the answer, not authorisation to start. |
| 2026-08-18 | → proposed | Raised 2026-08-18 from a maintainer's question about what survives a migration. Of the three losses that document lists, this is the one whose inputs are all still present — the rule is stated and `enumerate` already returns everything it needs, so the loss is of the sorting and not of the information. `medium` rather than `high`: it costs a person a decision each time, where [T-178](T-178-give-the-github-binding-a-standing-verification.md) costs them data. **Not covered by any standing authorisation.** |
