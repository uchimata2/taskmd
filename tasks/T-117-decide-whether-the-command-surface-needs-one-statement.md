---
id: T-117
title: Decide whether the command surface needs one statement
type: decision
status: done
phase: review
parent: null
blocked_by: []
related: [T-030, T-031, T-064, T-073]
work_package: M5
owner: maintainer
business_value: low
effort: xs
created: 2026-08-11
updated: 2026-08-11
deliverables: [plugin/skills/taskmd/taskmd/cli.py]
---

# T-117 — Decide whether the command surface needs one statement

## 1. Specify

**Outcome**
A decision, recorded with its rejected alternative: either what taskmd's command surface is gets one
home and the other places point at it, or the several statements are confirmed as different registers
that legitimately each say it.

**Why this one**
Raised from [T-030](T-030-settle-the-schema-module-s-own-entry-point.md)'s review. That task's first
acceptance criterion asks for *"exactly one statement of what taskmd's command surface is, and it is
true"*. Its falsifier — no runnable entry point the surface does not name — is met. Its first clause
is not, and was not on the day it was written. Four places say what the surface is:

| Where | What it says |
| :--- | :--- |
| `README.md` | A table of the four commands, one row each, with what each is for |
| `plugin/skills/taskmd/taskmd/cli.py` | The module docstring opens *"The four commands"* and lists their invocations |
| `docs/SCOPE.md` | *"CLI at four commands"*, inside the decision that fixed the number |
| `CLAUDE.md` | Points at `README.md` for the list rather than repeating it — already the shape the others might take |

**This is a decision and not a fix**, which is why T-030 did not absorb it. The four are not obviously
one fact repeated: `README.md`'s table is a front door for someone who has not installed anything,
`cli.py`'s docstring answers *what is this file* for someone reading the source, and `docs/SCOPE.md`
records a bounded decision rather than describing a tool. The T-026 threshold's clause 2 asks whether
they would all have to be revised together — a fifth command would touch all four, which is what
makes the question worth asking rather than answering here.

**One of them cannot point at another**, and the answer must survive it: `cli.py` is inside `plugin/`,
and T-064 forbids anything there from naming `README.md`'s neighbours — `SCOPE.md`, `BRIEF.md`,
`CLAUDE.md`, an `R-NN` or a non-goal. Whatever home is chosen, the shipped docstring can point at it
only if it ships too. [T-031](T-031-give-the-list-rationale-one-home.md) hit exactly this and settled
for naming the task rather than the document.

**Requirements served**
R-1, R-18 (`docs/SCOPE.md`); the design rule — one home per fact.

**Scope**
- In: the four statements above, and whether the count of commands is one fact or several.
- Out: what the surface *is*. Four commands, settled by `docs/SCOPE.md` non-goal 11's amendment.
- Out: T-030's removal, which is done and which this does not reopen.

**Inputs**
`README.md`, `plugin/skills/taskmd/taskmd/cli.py` module docstring, `docs/SCOPE.md`, `CLAUDE.md`;
[T-030](T-030-settle-the-schema-module-s-own-entry-point.md) §4;
[T-031](T-031-give-the-list-rationale-one-home.md) §3, for what the plugin boundary costs a pointer.

**Acceptance criteria**
- [ ] One of two outcomes is chosen and recorded with what it rejects: the surface gets one home and
      the others point at it, or the statements are confirmed as distinct registers
- [ ] If one home is chosen, it is stated how `cli.py`'s docstring reaches it without breaking T-064
- [ ] If distinct registers is chosen, it is stated what would have to be true for the answer to
      change — so the next reader who notices the repetition finds the reasoning and not just the fact

**Open questions**
- None. **Q1 — one home, or distinct registers? — decided 2026-08-11 under the standing delegation:
  distinct registers, no change.** The reasoning is in §3, because the count of statements the
  question assumes turned out to be wrong when it was read rather than listed. *Rejected: one home,
  the others point at it* — the design rule applied literally, and it would have caught nothing here:
  no statement of the surface was wrong when T-030 found the fifth entry point; what was wrong was
  the entry point.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the four statements rather than trusting §1's table, and say what each actually asserts | The corrected table in §3 |
| 2 | Answer Q1 against what was read, with the rejected alternative | §3, and the front-matter status |
| 3 | Make the answer findable from where the repetition is visible, within T-064's limit | `plugin/skills/taskmd/taskmd/cli.py` docstring |
| 4 | State the falsifier — what would have to be true for the answer to change — and raise anything it makes actionable | §3, criterion 3, and any task |
| 5 | Suite, `index`, `check` | §3 |

Step 1 is not ceremony. §1's table is a claim about four documents written from memory of them, and
this task's whole subject is whether those four say the same thing; taking the table's word for it
would answer a question about the tree by reading a summary of the tree.

## 3. Implement

### Step 1 — what the four actually say

| Where | What it asserts | Register |
| :--- | :--- | :--- |
| `README.md` §*The commands* | Four rows: the invocation and **what each is for** | A stranger deciding whether to install |
| `plugin/skills/taskmd/taskmd/cli.py` | Four lines: the invocation **with its flags**, plus why the fourth exists | Someone reading the source |
| `docs/SCOPE.md` non-goal 11 | *"holds the CLI at four commands"* — **and names none of them** | A bound on a future change |
| `CLAUDE.md` | How to invoke them **in this repository** — `./plugin/bin/taskmd <cmd>` | A session working here |

**Two of the four are not statements of the command surface at all.** `docs/SCOPE.md` states a
*bound*: the number is capped, and which commands they are is not written there. `CLAUDE.md` states
an *invocation route* peculiar to this checkout, because the shell snapshot drops the `PATH` entry an
adopter gets. Neither would be corrected by a fifth command; one would be **decided** by it, which is
what a non-goal is for.

So the real question is narrower than §1 framed it: `README.md` and `cli.py` both list the four, in
different vocabularies — purposes against flags — and neither is derivable from the other.

### Step 2 — the answer

**Distinct registers. Nothing moves.** Three reasons, in order of weight:

1. **Neither of the two real statements contains the other.** README says what `check` is *for*;
   `cli.py` says what arguments it takes. Collapsing them means one of the two readers loses the half
   addressed to them, and a pointer does not help the one who has not installed anything.
2. **The plugin boundary makes the literal fix impossible in the direction that matters.** T-064
   forbids anything in `plugin/` from naming `README.md`'s neighbours, so `cli.py` cannot point at a
   home outside the subtree. [T-031](T-031-give-the-list-rationale-one-home.md) met this and settled
   for naming the task. One home would therefore be one home plus an exception, which is two homes
   with extra words.
3. **The repetition is a list of four short names, not an argument.** T-031 moved the `list`
   rationale because a second copy of *reasoning* drifts into disagreement. Four names drift into
   being wrong, which is a different failure and has a different remedy — step 4.

*Rejected: one home, the others point at it.* Recorded in §1 with what it loses.

### Step 3 — findable from where the repetition is

One clause in `cli.py`'s docstring says the README lists the same four for a different reader and
that this is deliberate, naming T-117. It names a task and no document, which is the form
T-031 established for a pointer that has to cross the plugin boundary.

### Step 4 — the falsifier, and what it makes actionable

**What would have to be true for this answer to change:** a third document starts listing the
commands *with their purposes* — README's register, duplicated — or the two existing lists come to
disagree about which commands exist.

The second is not hypothetical here.
[T-073](T-073-correct-the-command-surface-local-context-states.md) is this project stating the
wrong command surface in a document for four days. "Distinct registers" is only safe if the registers
agree about the set, and nothing checks that they do: `usage_line` is derived from `COMMANDS`, but
README's table and `cli.py`'s docstring are prose. Raised as
[T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) rather
than built here — this task is a decision, and adding a guard is a different outcome (METHOD rule 4).

**Decisions & assumptions**

- **The decision was taken under the standing delegation, not referred.** §1 carried a recommendation
  and its rival, which is the shape the maintainer has said to decide from; the rejection is recorded
  where the decision is. — 2026-08-11
- **§1's table is left as written and corrected in §3, not edited.** It is what the task believed
  when it was raised, and rewriting it would delete the finding that reading the four changed the
  question (METHOD rule 5). — 2026-08-11

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — one clause in the module docstring

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| One of two outcomes is chosen and recorded with what it rejects | met | **Distinct registers**, with the rejected alternative in §1 and the three reasons in §3 step 2. The strongest is that reading the four narrowed the question: only two of them state the surface at all. |
| If one home is chosen, it is stated how `cli.py`'s docstring reaches it without breaking T-064 | n/a | One home was rejected, and the T-064 limit is **part of why** — a home outside `plugin/` is unreachable from `cli.py`, so "one home" would have been one home plus a permanent exception. |
| If distinct registers is chosen, it is stated what would have to be true for the answer to change | met | §3 step 4, and it is not left as prose: the second falsifier — the two lists disagreeing — has already happened once in this project (T-073), so it is raised as [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md). |

**Child fix tasks raised**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — a
  guard that the prose lists name the commands that exist. It is what makes this answer safe rather
  than merely argued.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-11 | → done | **Distinct registers. Nothing moves.** Decided under the standing delegation, with the rejection recorded in §1. The step that mattered was step 1: reading the four rather than trusting §1's table narrowed the question, because **two of them are not statements of the command surface at all** — `docs/SCOPE.md` non-goal 11 states a *bound* and names no command, and `CLAUDE.md` states an invocation route peculiar to this checkout. Of the two that remain, neither contains the other (purposes against flags) and one of them is inside `plugin/`, where [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) forbids pointing at a home outside the subtree — so "one home" would have been one home plus a permanent exception. Criterion 3's falsifier is not left as prose: the two lists disagreeing has already happened here ([T-073](T-073-correct-the-command-surface-local-context-states.md), four days), so it is raised as [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md), which is what makes this answer safe rather than merely argued. |
| 2026-08-11 | → in_progress | Five steps. One clause added to `cli.py`'s docstring so the decision is findable from where the repetition is visible, naming the task and no document — the form [T-031](T-031-give-the-list-rationale-one-home.md) established for a pointer crossing the plugin boundary. §1's table is deliberately **not** edited: it is what the task believed when raised, and correcting it in place would delete the finding that reading the four changed the question. |
| 2026-08-11 | → specified | Q1 answered under the standing delegation rather than referred, since §1 already carried a recommendation and its rival. Criteria unchanged. |
| 2026-08-11 | (no change) | **METHOD §3.1 waived by the maintainer, 2026-08-11** — *"continuous work on all v0.5 tasks is authorized, with full lifecycle."* It covers every task carrying `work_package: M5`, through all four phases — including a task raised into M5 *by* that work, which is a M5 task and not a fresh grant. It **does not generalise** to `M6` or to unlabelled work. *Rejected: reading it as the seven open on the day* — a fix task raised by a M5 task would then need its own permission, and asking seven times is not continuous work. |
| 2026-08-11 | → proposed | Raised from T-030's review. Not a finding T-030 could absorb: its criterion asks for one statement, four exist, and collapsing them is outside a task scoped to `schema.py`'s `main()`. Typed `decision` because the answer may legitimately be "leave them" — three address different readers and the fourth is already a pointer. Put in `M3` rather than `M2`: nothing is wrong today, and the clause it comes from was already unmet when it was written. |
