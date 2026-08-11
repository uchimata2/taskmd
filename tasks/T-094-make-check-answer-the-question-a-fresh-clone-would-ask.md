---
id: T-094
title: Make check answer the question a fresh clone would ask
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-013, T-034, T-092, T-095]
work_package: v0.2
owner: maintainer
business_value: high
effort: s
created: 2026-08-09
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py, README.md]
---

# T-094 — Make check answer the question a fresh clone would ask

## 1. Specify

**Outcome**
`check` states which question it is answering about a broken link — *"is this file here?"* or
*"would someone who cloned this repository find it?"* — and behaves consistently with the answer, so
a project that keeps machine-local documents is not given failures it cannot fix.

**Why this one**
Reported by the deck-building sibling (`control/LOCAL-CONTEXT.md`), and reproduced here on a
throwaway project: a `.gitignore` containing `private/`, and a gitignored document holding a dead
link, produces

```
BROKEN LINK   private/notes.md -> ../nope.md

1 problem(s) over 1 task(s)
```

`markdown_files` walks everything except `SKIP_DIRS` — `.git`, `node_modules`, `__pycache__`,
`.venv` — and nested projects. `.gitignore` is not consulted on either side: not for the documents
scanned, and not for the targets a link points at.

**This repository is exposed to it and has not noticed.** `control/` is gitignored and holds
`LOCAL-CONTEXT.md`, which is prose full of references; a live `.handoff/HANDOFF.md` is resumption
state. Neither is in a clone. A dead link inside either is not a broken promise to any reader,
because no reader can reach the document making it.

**The inconsistency is inside this project's own tooling.** `CLAUDE.md`'s pre-publish check is built
on `git ls-files --cached --others --exclude-standard` **precisely** so it sees what a push would
send — that flag combination is argued for at length there, and
[T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) exists because getting it wrong
was silent. `check` answers a different question from the leak check standing next to it, and nothing
says which is intended.

**Requirements served**
R-16. R-23, since the quarantine of local-only material is the reason gitignored documents exist here
at all.

**Scope**
- In: whether `check` consults `.gitignore`, on the document side, the target side, or both.
- In: what it prints about what it skipped — a count at minimum, so the exclusion cannot quietly
  grow. That is [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)'s argument
  arriving here first.
- In: what a project with no git at all gets. One of the projects onboarded on 2026-08-09 has no
  version control, so "consult `.gitignore`" must degrade to something rather than fail.
- Out: the pre-publish leak check, which already answers this correctly and is not taskmd's code.
- Out: `SKIP_DIRS`, which is a different mechanism and is not at issue.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py`, `markdown_files` and `check_links`.
- `CLAUDE.md` *The pre-publish check*, for the argument about what `git ls-files` with those three
  flags buys and why the shorter form was rejected.
- [T-013](T-013-quarantine-local-only-information-behind-gitignore.md), for why local-only material is
  quarantined rather than deleted.

**Acceptance criteria**
- [ ] The question `check` answers is written down in one place, and the behaviour matches it
- [ ] A fixture with a gitignored document holding a dead link behaves as decided, shown by running
      it both ways
- [ ] A project with no `.git` still works, shown on a fixture rather than reasoned about
- [ ] Whatever is skipped is counted in the output

**Open questions**
- ~~**Which question is the right one.**~~ **Answered 2026-08-10 (§3).** Both, on different sides —
  documents are judged by what a clone would receive, targets by what is on disk.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Answer the open question and record the rejected alternative where the decision is | §3 below |
| 2 | Ask git what a push would send, with the flag combination `CLAUDE.md` already argues for; return *nothing* rather than an empty set where there is no git | `clone_would_receive` in `cli.py` |
| 3 | Filter the document side of the link walk through it, leaving `markdown_files` a plain walk so the T-095 narrowing test still has something to narrow | `check_links` in `cli.py` |
| 4 | Print what was **not** read, on both the passing and the failing branch | the `Scope` line from `cmd_check` |
| 5 | Prove all three behaviours on throwaway projects — ignored document skipped, no-git project unchanged, published-to-ignored pointer still resolving | `CheckAnswersTheQuestionAFreshCloneWouldAsk` in `tests/test_cli.py` |
| 6 | State the question adopter-facing, and refresh the sample run the change falsifies | `README.md` |

## 3. Implement

**Decisions & assumptions**

- **The document side answers "would someone who cloned this find it?"; the target side keeps
  answering "is this file here?"** — 2026-08-10. The asymmetry is the decision, and it is not a
  compromise between the two options: the sides fail differently. A gitignored *document* is
  unreachable, so a dead link inside it is a promise to nobody. A gitignored *target* is material a
  published document deliberately points at, which is what quarantining local-only information
  behind `.gitignore` (T-013) requires — the tracked tree refers to that material by name, and a
  check that called those pointers broken would make the convention unrepresentable.
- **Rejected: the strict reading, where a gitignored target is also a failure** — 2026-08-10. It is
  the honest application of "would a clone find it", and it catches a real class: a published README
  naming a file that is not in the repository. It was rejected because it collides head-on with the
  quarantine above, and because it is a *new problem class* rather than a scoping change, which is
  not what an `s` was estimated for. Raised instead as [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md).

  > *2026-08-11 — the first of these two decisions was **reversed**, and the second taken, by the
  > maintainer at [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md).
  > Both are left as written, because they are what was decided here and rule 5 says annotate the
  > past rather than rewrite it. What changed is not the argument but its premise: the collision with
  > the quarantine convention was measured and does not occur. Every reference to this project's own
  > quarantined file is a **bare path in prose**, never a Markdown link, and T-092 had already put
  > that class out of scope — so no pointer the convention actually uses was ever at risk. Across 151
  > published documents the strict rule raised zero file-level alarms and twelve links to
  > directories, which are exempt because git lists no directory. The target side now asks both
  > questions, and reports `IGNORED LINK`. The estimate stands as a fair reason not to have done it
  > here: it was a new problem class, and it took one.*

- **Rejected: "is it here?" on both sides, i.e. leaving the walk alone and documenting it** —
  2026-08-10. Cheapest, and defensible right up to the point where the reporting project cannot fix
  what it is told about. It also leaves two checks in one repository answering different questions
  about the same tree with nothing saying which, which is the finding, not the symptom.
- **`git ls-files -z --cached --others --exclude-standard`, one invocation per run** — 2026-08-10.
  The same flag combination `CLAUDE.md` argues for at length, so the two checks now agree by
  construction rather than by coincidence. `--cached` alone is what T-034 caught being silently
  blind to files a session had just created; the test asserts both halves by staging and re-running.
- **No git returns `None`, never an empty set** — 2026-08-10. "Nothing here would be published" and
  "there is nothing to ask" are different answers and only the first is an exclusion. Conflating
  them would have made a project without version control scan zero documents and print `OK`.
- **The skipped count is a `Scope` line, not a denominator** — 2026-08-10. A document that was not
  read was not examined, and reporting it among the examined counts is precisely the claim T-095
  removed. It prints on the failing branch too, because an exclusion hides behind an unrelated
  problem exactly as well as behind a pass.
- **`markdown_files` was left a plain walk and the filter put in `check_links`** — 2026-08-10. Two
  concerns, and T-095's narrowing test monkey-patches `markdown_files` by name to prove a shrinking
  denominator is visible; folding the filter into it would have made that test narrow the thing it
  was measuring.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `clone_would_receive`, the filtered `check_links`, the
  `Scope` line in `cmd_check`
- `tests/test_cli.py` — `CheckAnswersTheQuestionAFreshCloneWouldAsk`, four cases
- `README.md` — *Which documents `check` reads, and which pointers in them*, and a refreshed sample

**Evidence**

On this repository, before and after, same tree:

```
OK - 96 task(s), ..., 155 document(s), 1160 link(s)

OK - 96 task(s), ..., 124 document(s), 947 link(s)
Scope  31 document(s) not read: a clone would not receive them
```

The 31 are this project's own quarantined material and its live handoff state — documents no clone
has ever contained, which `check` had been reading and reporting on since it was written.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The question `check` answers is written down in one place, and the behaviour matches it | met | `README.md` states it adopter-facing; the docstring next to the code states the *mechanism* and points at the README for the question, so the two are not two copies of one fact. Behaviour matched by the four tests below rather than by reading. |
| A fixture with a gitignored document holding a dead link behaves as decided, shown by running it both ways | met | A throwaway project rather than a committed fixture, and that is load-bearing: a fixture inside this repository is governed by *this* repository's ignore rules, which is the thing under test. Both ways: `git init` alone → skipped and counted; no git → the same dead link reported. |
| A project with no `.git` still works, shown on a fixture rather than reasoned about | met | Same project, git never initialised: exit 1, the dead link named, and `no git here, so .gitignore was not consulted` on the `Scope` line. Degrading to the previous behaviour is the degradation; going silent would not have been. |
| Whatever is skipped is counted in the output | met | `Scope  31 document(s) not read`, on both branches. The no-git case says the mechanism was not consulted rather than reporting `0`, which would have been true and misleading. |

**Child fix tasks raised**
- [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md) — the
  rejected strict reading, kept as a question rather than dropped. It is a new problem class, and it
  has to be reconciled with the quarantine before it can be answered either way.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → done | Every criterion met. The decision that mattered was not which of the two questions to pick but that the sides are separable, which neither the report nor the spec had considered: answering one question on documents and the other on targets is what let the quarantine survive a check aimed at exactly the material it quarantines. Bundled into one release with [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) and the manifest bump, because a version string that does not move reaches none of the installs. |
| 2026-08-10 | → specified | Answered by separating the two sides rather than choosing between the two questions. The strict target-side reading is a real class and was pushed to T-097 rather than absorbed, since a new problem class is not a scoping change. |
| 2026-08-09 | → proposed | Raised from the deck-building sibling's migration report and reproduced here in a throwaway project. `high` and `s`: the fix is small and the argument is already written down in this repository for a different check — the pre-publish grep is built on `git ls-files --cached --others --exclude-standard` so that it sees exactly what a push would send, while `check` standing next to it walks everything. Two checks in one project answering different questions about the same tree, with neither saying which. |
