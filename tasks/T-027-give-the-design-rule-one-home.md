---
id: T-027
title: Give the design rule one home
type: fix
status: done
phase: review
parent: T-026
blocked_by: []
related: [T-017]
work_package: M1
owner: maintainer
business_value: high
effort: s
created: 2026-08-06
updated: 2026-08-07
adopter_visible: no
deliverables:
  - CLAUDE.md
---

# T-027 — Give the design rule one home

## 1. Specify

**Outcome**
"Store the forward edge; derive the rest" — and in particular its *compels the second write*
qualification — is written out in full in exactly one place, and the other documents point at it.

**Why this one**
Raised as **F-1** by [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md), threshold
clauses 2 and 4. The rule is currently stated in full, with its own worked qualification, in three
documents:

- `CLAUDE.md` §*The one design rule*
- `docs/SCOPE.md` §2, principles 1 and 2
- `docs/METHOD.md` §4 and its *Store the forward edge; derive the rest* subsection

with a fourth treatment in `docs/method/rationale.md` §*Why the inverse of a link is never written
down*. The near-verbatim part is the qualification: all three say that the rule forbids a design
that **compels** a second write rather than a user who makes one, and all three reach for the same
"collapses to a single entry" phrasing.

**Two of those copies are already sanctioned; the third is not.** `docs/SCOPE.md` §3 settles the
SCOPE↔METHOD overlap deliberately — a requirement states a property, the method states the rule that
gives it that property, and their agreeing is what conformance *is*
([T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md)). Nothing settles
`CLAUDE.md` carrying a third full statement, and `CLAUDE.md` itself rules it out: *"The method has
one home: `docs/METHOD.md` — ... it is not restated here; if you find it written out somewhere else,
that copy is the defect."*

**Why it costs more than an ordinary duplicate.** `CLAUDE.md` is loaded on every turn, so this copy
is paid for on every turn (clause 4), and it is the project's own thesis — delete duplication rather
than policing it — violated in the document that states the thesis.

**Requirements served**
R-1, R-21 (`docs/SCOPE.md`); §1 *Token cost*.

**Scope**
- In: `CLAUDE.md` §*The one design rule*, and whatever pointer replaces it.
- Out: the SCOPE↔METHOD overlap, which is settled in T-017 and is not a defect.
- Out: `docs/method/rationale.md`, which explains *why* the rule holds rather than restating it —
  that is the division METHOD §7 is built on.
- Out: any change to the rule itself. This is about where it lives, not what it says.

**Inputs**
`CLAUDE.md`, `docs/SCOPE.md` §2 and §3, `docs/METHOD.md` §4,
[T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md),
[T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) F-1.

**Acceptance criteria**
- [ ] The qualification is written in full in exactly one file; a grep for its distinctive phrasing
      returns one hit outside task records
- [ ] `CLAUDE.md` still tells a new session that the rule exists and where to read it — the fix is a
      pointer, not a deletion, since a spine that omits the rule entirely fails a different job
- [ ] `CLAUDE.md`'s own "if you find it written out somewhere else, that copy is the defect"
      sentence is true of the file that contains it
- [ ] `docs/SCOPE.md` §3's sanctioned overlap is left intact and is explicitly re-checked, so this
      fix does not quietly reopen T-017

**Open questions**
- Which file is the one home — `docs/METHOD.md` §4 is the obvious candidate, since METHOD is already
  declared the method's one home. Confirm rather than assume, because `docs/SCOPE.md` §2 principle 2
  states it as a *principle* the requirements apply, which is a different role. — maintainer.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Locate every statement of the rule and of its qualification outside task records, so the fix is aimed at a measured set rather than at the three files the finding named from reading. Classify each hit: the one home, a sanctioned role, or a copy. | The grep output, and a classified list |
| 2 | Decide the boundary inside `CLAUDE.md` between *naming* the rule — which criterion 2 requires it to keep — and *stating* it, which is what has to move. | A recorded decision, with what was rejected |
| 3 | Rewrite `CLAUDE.md` §*The one design rule* as a pointer to `docs/METHOD.md` §4, keeping this repository's own application of the rule. | The edited section |
| 4 | Re-run the grep and judge what remains against criterion 1 as written. Check criterion 3's sentence against the whole of `CLAUDE.md`, not only the section that changed — the sentence makes a claim about the file. | The grep output, a verdict per remaining hit, and the new line count |
| 5 | Confirm `docs/SCOPE.md` §3's sanctioned overlap is untouched and still says what T-017 decided. | A stated verdict, and a diff showing SCOPE unchanged |

**Sequencing.** Step 1 leads because it can invalidate criterion 1 before a word is written. The
finding named three files by reading them; criterion 1 is a *grep count*, so if the real set is
larger — or if a hit the scope protects carries the qualification in full — then the criterion is
unreachable by any acceptable edit, and that is much cheaper to discover before the rewrite than
during the review of it. Step 4 re-runs the same command rather than a new one, so the before and
after are comparable. Step 5 is last and deliberately negative: it proves the fix did *not* reach
into the overlap T-017 settled, which is the way this task could quietly reopen a closed decision.

**Shape of the deliverable — decided: a pointer that keeps the local application.** `CLAUDE.md`
retains the rule's name and what it comes out as *in this repository* — front-matter as the only
written home, children and dependents and the index and the deliverable map all computed — and
points at `docs/METHOD.md` §4 for the full statement and the qualification.
*Rejected: a bare pointer with no statement of the rule.* Criterion 2 rules it out in advance, and
rightly: a spine that names no design rule fails the job it has, which is to make a new session
check its next decision against something.
*Rejected: moving the local application into `docs/METHOD.md` §4 along with the qualification.* This
is the tempting one, because it would leave `CLAUDE.md` with a single line. But METHOD's opening
paragraph commits it to naming **no field, no file, no identifier format and no command** — pushing
`tasks/` front-matter and the generated index into it would buy one-home-ness for the rule by
breaking the property that makes METHOD portable, and R-13/R-14 are that property.

**Output paths**
- `CLAUDE.md` — §*The one design rule*
- This task's §3 — the two grep runs and the classification of what remains

## 3. Implement

Run on 2026-08-07. One command does steps 1 and 4, before and after, so the two are comparable:

```bash
grep -rnIE --exclude-dir=.git --exclude-dir=tasks --exclude-dir=.handoff --exclude-dir=.pytest_cache 'compels?\W+(a|the) second write' .
```

**Step 1 — four hits, not three, and the fourth changes the verdict.**

| Hit | Role | Verdict |
| :--- | :--- | :--- |
| `CLAUDE.md:44` | full qualification, near-verbatim with SCOPE's | the copy this task removes |
| `docs/METHOD.md:113` | the rule's statement | **the one home** — the maintainer's answer |
| `docs/method/rationale.md:16` | explains *why* the rule is phrased this way | a different role; scope puts it out, and it is genuinely not a statement of the rule |
| `docs/SCOPE.md:43` | principle 1's closing sentence, full qualification | **the problem** — see the finding below |

**The pattern needed markup tolerance to find anything at all.** `compels the second write` matches
nothing: every instance emphasises the keyword, so the literal phrase is broken by `**` or `*` in all
four files. Recorded because criterion 1 is *defined* as a grep count, and the first, obvious
spelling of that grep returns zero hits — which reads exactly like success.

**Steps 2 and 3 — the section rewritten.** `CLAUDE.md` §*The one design rule* now names the rule,
points at `docs/METHOD.md` §4 for the full statement and the qualification, and keeps only what is
true of *this repository* — front-matter as the sole written home, and children, dependents, the
index and the deliverable map as computed. One further sentence went with the qualification: *"Facts
that are computed cannot drift from facts that are stored, so no validator is needed to keep them
honest."* That is `rationale.md`'s point in `rationale.md`'s words, so it was a fourth copy hiding
inside the third.

**Step 4 — three hits remain, and `CLAUDE.md` is 145 → 139 lines.** The removal is six lines off the
file T-028 is budgeting, which is the whole reason that task depended on this one.

**Step 5 — the settled overlap was not touched.** `git diff --stat` over `docs/SCOPE.md`,
`docs/METHOD.md` and `docs/method/` reports **no change**; the only modified file is `CLAUDE.md`, at
6 insertions and 12 deletions. SCOPE §3's paragraph still reads as T-017 decided it.

**Decisions & assumptions**
- **The local application stays in `CLAUDE.md` rather than moving to METHOD §4.** — Taking it along
  with the qualification would have left a one-line section, but METHOD's opening commits it to
  naming no field, no file and no command; `tasks/` front-matter and the generated index would break
  exactly the portability R-13 and R-14 exist to protect. — 2026-08-07
- **Criterion 1 was judged as written and not rewritten to fit.** — It asks for one hit; the scope
  protects two of the three that remain. That is a criterion that no outcome inside this task's scope
  could satisfy, which `review.md` §*Changing a criterion* covers — but its third clause requires the
  original's owner to agree the replacement, and that is the maintainer's call, not this session's.
  Carried as unmet with a task, rather than silently narrowed. — 2026-08-07

**Findings raised, not fixed here**
- **T-045** — `docs/SCOPE.md` §2 principle 1 carries the qualification in full, and the sanction this
  task's scope relies on does not cover it.
- **T-046** — `CLAUDE.md` restates METHOD §1.5's closing condition and has already drifted from it.

**Outputs produced**
- [`CLAUDE.md`](../CLAUDE.md) — §*The one design rule*, now a pointer plus this repository's
  application of it

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The qualification is written in full in exactly one file; a grep for its distinctive phrasing returns one hit outside task records | **not met** | Four hits before, three after. Two of the three are put out of scope by this task's own *Scope* section, so no acceptable outcome could have returned one — the criterion is broader than the task it belongs to. `rationale.md`'s hit is defensible on its role; `docs/SCOPE.md:43` is not, and the sanction invoked for it does not reach it → **T-045**. Judged as written per `review.md` step 1 rather than narrowed to match the result. |
| `CLAUDE.md` still tells a new session that the rule exists and where to read it — a pointer, not a deletion | met | The section still opens with the rule by name and states this repository's application of it; what it no longer does is state the qualification, which now resolves through one link to `docs/METHOD.md` §4. |
| `CLAUDE.md`'s own "if you find it written out somewhere else, that copy is the defect" sentence is true of the file that contains it | **not met** | True of the design rule now. Not true of the file: the sentence claims the whole method — "the lifecycle and its exit criteria" — is not restated in `CLAUDE.md`, and line 59 restates METHOD §1.5's closing condition. Worse than a copy, it has drifted: METHOD requires the `implement` evidence to be written down, `CLAUDE.md` substitutes the validator passing, and a task can satisfy the second with none of the first → **T-046**. Found because the criterion says *the file*, so it was checked against the file rather than against the edited section. |
| `docs/SCOPE.md` §3's sanctioned overlap is left intact and explicitly re-checked, so this fix does not quietly reopen T-017 | met | `git diff --stat` reports no change to `docs/SCOPE.md`, `docs/METHOD.md` or `docs/method/`; `CLAUDE.md` is the only modified file. Re-read rather than only diffed: §3 still states the requirement-versus-rule division T-017 decided, and T-045 is deliberately aimed at §2 *Principles*, which that decision never covered. |

Two met, two carried. The task did the work its scope named and did it correctly — the removed copy
is gone and the pointer resolves — and both gaps are the same shape: a criterion written from a
reading of three files, checked against the tree, turning out to describe a bigger problem than the
one being fixed. Neither is repaired here (`review.md` step 4).

**Child fix tasks raised**
- **T-045** — `docs/SCOPE.md` §2 principle 1 states the qualification in full; T-017's settlement was
  about §3 *requirements* and does not reach §2 *principles*.
- **T-046** — `CLAUDE.md`'s done-condition restates METHOD §1.5 and drops its evidence clause.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **`adopter_visible: no`, judged under [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)**, 2026-08-23. Annotated rather than rewritten, per METHOD rule 5: nothing this record says about the past changes. Against `docs/PUBLISHING.md` §7's test — this record's sole output is `CLAUDE.md` §*The one design rule*, which §7 names in its own words as the `no` case: *instruction files*. An install copies `plugin/`, which this did not touch, so an adopter sees no different output, receives no different file and acts no differently. |
| 2026-08-07 | → done | Two criteria met, two carried. The maintainer answered the open question — `docs/METHOD.md` §4 is the one home — and instructed plan through fix in one turn, which is taken as `specify`'s agreement as it was for T-037 and T-042. The fix itself was small and is done: `CLAUDE.md` §*The one design rule* is now a pointer plus this repository's application, 145 → 139 lines, and a sentence that turned out to be `rationale.md`'s went with the qualification. Step 1 is what earned its place at the front — the grep found **four** hits, not the three the finding named, and only after being made tolerant of Markdown emphasis; the literal phrase matches nothing in any of the four files, so the obvious spelling of criterion 1's own check returns zero hits and reads as success. The fourth hit is `docs/SCOPE.md:43`, which carries the qualification in full: this task's scope waves it through as settled by T-017, but T-017 settled §3 *requirements* against the method and never reached §2 *Principles* — whose own header claims the principles are "listed once, here", which METHOD §4 makes false → **T-045**. Criterion 3 was checked against the file rather than the edited section, as it is written, and found `CLAUDE.md` restating METHOD §1.5 with the evidence clause swapped for a validator run → **T-046**. Criterion 1 was left as written rather than narrowed to fit: no outcome inside this task's scope could return one hit, which `review.md` §*Changing a criterion* covers, but its agreement clause belongs to the maintainer. |
| 2026-08-07 | → planned | Five steps, and step 1 leads on the possibility that it invalidates criterion 1 before any prose is written — the finding named three files by reading them, and the criterion is a grep count. Shape decided: a pointer that keeps the local application, rejecting both a bare pointer (criterion 2 forbids it) and moving the application into METHOD §4, which would buy one-home-ness by putting `tasks/` front-matter into the document that promises to name no file. No soft edge to T-028: it already records a dependency on this task, and one relationship shown under two edge kinds is noise in the graph rather than the permitted second write. |
| 2026-08-06 | → proposed | Raised as F-1 from the T-026 audit, clauses 2 and 4. Not fixed where it was found (METHOD §5). The finding is narrow on purpose: two of the three copies are settled by T-017 and are not in scope here. |
