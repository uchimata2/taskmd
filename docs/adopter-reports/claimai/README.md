# Adopter report — ClaimAI exam project, August 2026

Three findings from one project that ran 84 tasks through taskmd over six days.

## Where this came from

The **AI Strategy Leader** training programme, Module 7 — Ethics, Governance, Risk, Compliance,
Standards, Regulation and Law. The closing exam is a full responsible-AI assessment of a fictional
insurer deploying a claims-scoring system, delivered as nine documents and a twenty-five slide
executive board presentation. It ran from 2026-08-23 to 2026-08-28 and produced 84 task records.

The deck was built with **htmldeck**. The project itself was run on **taskmd**. Neither tool was
chosen for a trial — they were used to do real work under a deadline, and everything here is
something that work ran into.

The deck was presented and the exam is delivered. **The verdict was that the deck is good**, which is
the frame for every criticism below: these are the places where a tool that produced a good result
made reaching it harder than it needed to be.

## Why it was collected

The project's owner asked for it in these words:

> *"Everything which is fixed, mitigated, improved, adjusted in this project, but should be
> universally applied to other downstream projects, so the htmldeck and taskmd should solve it, we
> have to collect them. … taskmd should learn a lot as well."*

**taskmd held up.** 84 tasks, 227 references, 38 dependency edges, 112 declared outputs, and `check`
resolved 1,989 links across 182 documents on the final run. The method — specify, plan, implement,
review, with one phase per request — is what kept a six-day project honest, and the project's own
instruction file says so.

The three findings below are the places where it did not hold, and two of them are the same
concurrency day.

## No answer is expected

This is a one-way hand-over. The project that produced it is finished and closed; there is nobody
waiting on a reply, no thread to keep alive, and no deadline attached to any of it.

So each record is written to stand on its own: the evidence is in the record, the version it was seen
on is in the record, and nothing asks a question back. **Take what is useful and discard the rest**
— including any record you judge wrong. Several of these argue against rules that caught real faults
here, and the records say so themselves.

## How to read the set

- **Every record carries its evidence.** A command and its output, a source line, or a verdict the
  tool itself printed. The staging project's rule was that a claim about a tool's behaviour without
  one is a guess.
- **Every record carries `Version seen`.** Fourteen of these were stamped rather than re-run, so
  treat the version as provenance, not as a fresh reproduction. One uncertainty is stated in the
  index: two versions were installed within the same hour, so a record found in that hour may have
  seen the earlier one.
- **`Severity` is what it costs the author who hits it**, never how hard it is to fix.
- **The `Target` rows were the staging project's own bookkeeping** and named a local clone path with
  the maintainer's first name in it. **They were redacted here on 2026-09-03, before this set was ever
  published**, because this repository is public and forbids personal and machine data
  ([`../../SCOPE.md`](../../SCOPE.md) §5); its own leak gate named all three files and refused them.
  The reporting project's preference was to leave them verbatim, and that preference could not waive
  this repository's constraint. **Nothing else in any record was touched** — every command, output and
  verdict stands as written.

## The findings

| # | Kind | Severity | Title |
| :--- | :--- | :--- | :--- |
| [`001`](001-index-drops-a-concurrently-created-task.md) | defect | — | taskmd — `index` can drop a task written during its run, and `check` then reports OK |
| [`002`](002-the-cli-is-unreachable-when-taskmd-is-installed-as-a-plugin.md) | feature | Medium | The CLI is unreachable when taskmd is installed as a plugin, and the cache keeps every version |
| [`003`](003-nothing-allocates-a-task-id-so-two-sessions-pick-the-same-one.md) | feature | High | Nothing allocates a task id, so two sessions pick the same one |

## The one that matters most

**`003` — nothing allocates a task id.** Two sessions read the same folder an hour apart, both took
the same next free number, and both used it. The id is the reference key: every dependency edge,
every cross-link and every index row names it, so a collision does not corrupt one file, it merges
two tasks in every document pointing at either.

The staging project's only defence is a hand-written rule telling every session to *re-derive the id
immediately before writing* — which is the shape of a missing operation. And `check` passes a folder
holding two `E28`s, which is the cheap half of the fix and is independent of the rest.
