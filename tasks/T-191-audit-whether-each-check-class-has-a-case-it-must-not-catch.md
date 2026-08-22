---
id: T-191
title: Audit whether each check class has a case it must not catch
type: audit
status: review
phase: review
parent: null
blocked_by: []
related: [T-151, T-150, T-100]
work_package: M6
owner: the project owner
business_value: medium
effort: m
created: 2026-08-19
updated: 2026-08-21
adopter_visible: no
deliverables: []
---

# T-191 — Audit whether each check class has a case it must not catch

## 1. Specify

**Outcome**
For every class `check` reports, a statement of whether its fixtures include a case it must **not**
catch, and whether that case has been shown able to fire. Each gap becomes its own child task; none
is filled here.

**Why this one**
[T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) ruled that a check needs
such a case and that the case counts only once it has been shown it could have spoken. It wrote the
rule and deliberately did not apply it: its own §1 *Out* said auditing the existing checks is a real
piece of work and would be raised from it.

**The rule's condition is what makes this an audit rather than a checklist.** Confirming that a
fixture *has* a quiet case is a grep. Confirming the quiet case *can* fire means breaking it on
purpose, one class at a time, and watching the alarm arrive — which is the only step that separates a
guard from evidence. This project has two measured instances of the difference:
[T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) §3's four tests
that pass by asserting silence, called guards rather than evidence in that record, and
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) §3's negative fixture
that could not fire at all because the check consumed the line under its header as a delimiter.

**Requirements served**
R-16, R-17 (`docs/SCOPE.md`).

**Scope**
- In: every class `check` reports — the problem prefixes and the advisories. The set is read from the
  code, never from a list in a document
- In: for each, whether a must-not-fire case exists, and whether it has been shown able to fire
- Out: **filling any gap.** A finding is never fixed where it is found (METHOD §5); each gap is a
  child task
- Out: re-opening [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s rule or
  its condition
- Out: classes reported by something other than `check` — the launchers' errors and the config
  loader's, which are not check classes

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — the classes, read from the code
- `tests/fixtures/` and `tests/test_cli.py` — the fixtures and what asserts about them
- [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) — the rule and its
  condition
- [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) — a worked instance
  of the condition failing

**Acceptance criteria**
- [ ] The class set is **derived from the code** and the derivation is shown, so a class added since
      cannot be missing from the audit
- [ ] Every class has a row, and the rows sum to the derived set — a class with nothing to say still
      has a row saying that
- [ ] Each *has a quiet case* claim names the fixture and the assertion, not the intention
- [ ] Each *can fire* claim quotes what happened when it was made to fire; a class whose quiet case
      was not exercised is recorded as unproven rather than as passing
- [ ] Every gap is a child task, and the audit closes only when each is resolved (`audit.md` step 5)

**Open questions**
- ~~**Do the advisories carry the same rule?**~~ **Answered 2026-08-19: yes, and every class the
  validator prints is audited, advisory or not.** Two reasons were given with the answer. **An
  advisory is a hard failure in waiting** — `SECTION REF` is already queued for promotion in
  [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) §3 — so auditing a class after
  it is promoted pays for it at the moment it starts blocking people. And **a noisy advisory trains
  a reader to skim the whole output**, the failing lines included, which is
  [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s own argument arriving
  by a different door. Limiting the audit to the classes that move the exit status was the
  alternative and was rejected. The audit is larger for this, and its condition is unchanged: each
  quiet case is still broken on purpose, one class at a time.

## 2. Plan

**What counts as a finding** (`audit.md` step 2, fixed before looking). A class is a finding if
either half of [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s rule fails
for it: **no case it must not catch**, or **a quiet case that could not be shown able to fire**. A
class with a quiet case that speaks on demand is recorded as checked and produces no work. Anything
else this audit notices about the checks — how good a class's message is, whether the class is worth
having — is outside the threshold and stays out.

**How this audit examines its subject.** Not by reading the tests, which is what makes a quiet
assertion look like evidence. Each class is **made to speak in a tree where a test asserts it is
silent**, one class at a time.

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Derive the class set from `plugin/skills/taskmd/taskmd/cli.py` — the problem prefixes from what is appended to `problems`, the advisory ones from `ADVISORY_PREFIXES` — and show the derivation. | The set, its size, and the command that produced it, in §3. |
| 2 | For each class, find the case it must **not** catch, naming the test and the fixture. Search for the assertion in every form it takes, not only a literal one. | A row per class naming its quiet case, or *none*. |
| 3 | For each class, plant its defect in a tree where a test asserts silence, run `check`, and quote what arrived. A class that stays silent there had a quiet case that could never have spoken. | The alarm line per class, quoted from the run. |
| 4 | Record every class in one table, and reconcile the table's length against step 1's derived count. | The table, and the two counts stated side by side. |
| 5 | Raise a child task per finding. Fix nothing (METHOD §5). | The child tasks. |
| 6 | Leave the umbrella open until every child resolves (`audit.md` step 5). | A stated end state, not a closure. |

**Sequencing.** Step 1 before step 2, so the row set is the code's and not the test file's — a survey
that starts from the tests can only find classes somebody remembered to test. Step 3 last of the
examining steps, because it is the expensive one and step 2 tells it where to aim.

**Decisions**

- **The examination is *make it speak*, not *read the assertion*.** T-151's condition is that a quiet
  case counts only once it has been shown it could have spoken, and reading an `assertNotIn` cannot
  show that — [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) is the
  worked case of an assertion that read correctly and could not fire. *Rejected:* a survey of the
  test file, which is the cheap version of this audit and would have passed every class.
- **The planting instrument is scratch and is not shipped.** It exists to produce the alarms quoted
  in §3; the repair of any finding is a child task's, and what that repair should be is not this
  audit's to decide.

**Outputs**

- `tasks/T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md` (§3, the table and the runs)
- one task file per finding

## 3. Implement

### Step 1 — the class set, derived from the code

```text
problem classes (17): ABANDONED SLOT, BROKEN LINK, CYCLE, DANGLING, DUPLICATE ID, ID WIDTH,
  IGNORED LINK, MALFORMED DATE, MISSING OUTPUT, NO BLOCKER, PARKED TASK, STALE INDEX,
  STORED DERIVED, TEMPLATE FIELD, TEMPLATE UNREACHABLE, VOCABULARY, WIDE ROW
advisory classes (4): CONFIG DRIFT, DUPLICATE INDEX, LABEL SHAPE, SECTION REF
TOTAL 21
```

The problem set is what is appended to `problems`; the advisory set is `ADVISORY_PREFIXES`, which the
code already keeps as one home. `CONFIG ERROR` is excluded by §1's *Out* — it is the config loader's
class and `check` does not own it.

### Step 2 — the quiet cases, and a survey that under-reported

**The first survey said nine classes had no quiet case. It was wrong, and the way it was wrong is
worth more than the answer.** It looked for `assertNotIn("CLASS"` as a literal. But
`CheckFailsOnEveryClassItClaims.fails()` asserts silence through a **loop variable** —

```python
for other in self.LABELS:
    if other != label:
        self.assertNotIn(other, out, "%s also reported %s:
%s" % (fixture, other, out))
```

— so thirteen in-scope classes have a quiet case in every fixture but their own, and none of them
matches a literal search. A survey that stopped there would have raised nine child tasks for gaps
that do not exist. **Every one of the 21 classes has a case it must not catch.**

### Step 3 — each class made to speak where a test asserts it is silent

**The instrument was wrong first, and its first result was a clean sweep.** Run 1 reported all
nineteen classes `SILENT`, which is the answer a perfect audit and a broken one both produce. The
cause: it invoked `taskmd/cli.py` directly, so every run died on
`ImportError: attempted relative import with no known parent package` and no class name could appear
in output the instrument was grepping. The guard added afterwards — *assert "Traceback" not in out* —
is what should have been there first, and is the same lesson as
[T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md)'s row 7 in a different
place: **a negative result is worth nothing until the instrument is shown to be able to produce a
positive one.**

Re-run through the shipped entry point, one class at a time:

```text
VOCABULARY    T-001.status is 'in-progres'; allowed: proposed, specified, planned, ...
DANGLING      T-007.blocked_by -> T-404 does not exist
NO BLOCKER    T-001 is 'blocked' with nothing in blocked_by
CYCLE         dependency loop: T-001 -> T-002 -> T-001
BROKEN LINK   .notes/scratch.md -> gone.md
STORED DERIVED T-001 stores 'children:', which is computed from 'parent'; remove it
MISSING OUTPUT T-001 declares 'out/report.md', which does not exist
DUPLICATE ID  T-001 is claimed by tasks/T-001-first.md and tasks/T-001-second.md ...
ID WIDTH      tasks/T-0001-over-wide.md declares 'T-0001', which is not T- plus 3 digit(s) ...
STALE INDEX   tasks/README.md no longer matches the tasks it was generated from; run 'taskmd index'
TEMPLATE UNREACHABLE tasks/_templates/task-template.md carries a placeholder id ...
TEMPLATE FIELD tasks/_task-template.md stores 'children:', which is computed from 'parent' ...
PARKED TASK   tasks/_drafts/T-002-parked-where-nothing-reads-it.md declares 'T-002', a valid id ...
ABANDONED SLOT tasks/T-001-closed-with-a-slot-nobody-filled.md body line 31 still reads '- <T-NNN or "none">'
MALFORMED DATE T-001-the-accident-that-found-this.md: updated is '2026-08-165', which is shaped like a date and is not one
WIDE ROW      tasks/T-001-three-rows-that-lose-text.md:16 has 3 cells against a 2-column header ...
LABEL SHAPE   milestone: '2.1' on 1 task(s) reads as a version; a release of that number is a different thing
SECTION REF   docs/handbook.md has no section 9; 1 reference(s) name it
CONFIG DRIFT  type: shipped default adds 'audit'; this project's row does not carry it
IGNORED LINK  docs/guide.md -> ../private/notes.md is here but no clone receives it ...
DUPLICATE INDEX tasks/OLD-INDEX.md: a second table of 5 known task ids sits outside the taskmd markers
```

**21 of 21 spoke.** Two needed the instrument corrected before they would, and both corrections were
the instrument's fault rather than the check's:

- **DANGLING** stayed silent because the planted task reused `T-001`, which the target tree already
  claimed — so `DUPLICATE ID` fired and the planted file was never loaded. Planted under a fresh id,
  it speaks.
- **DUPLICATE INDEX** stayed silent because the planted copy carried the generated block's **markers**
  along with its rows, and the check reads only what sits *outside* them. Copied without the marker
  lines, it speaks. Worth writing down: a project that duplicates the index by copying the whole file
  verbatim, markers included, is not reported — that is the check's stated design and not a defect,
  but it is not obvious from the class name.

### Step 4 — the table, reconciled against the derived count

| # | Class | Kind | Case it must not catch — test, fixture | Shown able to fire |
| :-- | :--- | :--- | :--- | :---: |
| 1 | VOCABULARY | problem | `fails()`'s loop, in all 13 other LABELS fixtures; and `test_a_task_typed_the_way_the_method_words_it_validates` | yes |
| 2 | DANGLING | problem | `fails()`'s loop | yes |
| 3 | NO BLOCKER | problem | `fails()`'s loop | yes |
| 4 | CYCLE | problem | `fails()`'s loop | yes |
| 5 | BROKEN LINK | problem | `fails()`'s loop; plus 5 named tests, including `test_a_link_inside_a_code_span_is_left_alone` | yes |
| 6 | STORED DERIVED | problem | `fails()`'s loop | yes |
| 7 | MISSING OUTPUT | problem | `fails()`'s loop; plus `test_an_open_task_declaring_a_path_that_does_not_exist_passes` (`planned-deliverable`) | yes |
| 8 | DUPLICATE ID | problem | `fails()`'s loop | yes |
| 9 | ID WIDTH | problem | `fails()`'s loop | yes |
| 10 | STALE INDEX | problem | `fails()`'s loop | yes |
| 11 | TEMPLATE UNREACHABLE | problem | `fails()`'s loop; plus `test_a_compliant_template_is_counted_and_not_reported` | yes |
| 12 | TEMPLATE FIELD | problem | `fails()`'s loop | yes |
| 13 | PARKED TASK | problem | `fails()`'s loop | yes |
| 14 | ABANDONED SLOT | problem | `test_the_slots_come_from_the_project_s_own_template` (`abandoned-slot`) | yes |
| 15 | MALFORMED DATE | problem | `test_every_other_fixture_is_silent`, `test_this_repository_is_silent` | yes |
| 16 | WIDE ROW | problem | `test_every_other_fixture_is_silent`, `test_this_repository_is_silent` (`wide-table-row`) | yes |
| 17 | IGNORED LINK | problem | `test_a_link_to_a_directory_is_not_reported`, `test_an_ordinary_published_link_is_not_reported`, `test_without_git_the_class_cannot_be_claimed_at_all` | yes |
| 18 | CONFIG DRIFT | advisory | 5 named tests, including `test_a_choice_is_not_drift` and `test_a_deleted_row_is_left_alone` (`broken-config`) | yes |
| 19 | DUPLICATE INDEX | advisory | `test_a_small_project_of_tasks_linking_to_neighbours_stays_quiet`, `test_the_generated_block_itself_is_not_a_duplicate_of_itself` | yes |
| 20 | LABEL SHAPE | advisory | `test_every_other_fixture_is_silent`, `test_this_repository_is_silent` (`label-shaped-value`) | yes |
| 21 | SECTION REF | advisory | `test_no_citation_names_a_section_this_repository_does_not_print` (`section-reference`) | yes |

**21 rows against a derived set of 21.** Every class has a case it must not catch, and every class
was made to speak. Neither half of T-151's rule fails outright for any class — which is why the two
findings below are about the *shape* of the guarantee rather than about a class that lacks one.

### Findings

**F-1 — `LABELS` is hand-kept, and covers 14 of the 21 classes.** The cross-fixture silence
assertion — the quiet case for thirteen of the classes above — loops over a list written out in
`tests/test_cli.py:128`. Nothing compares it against the code's own set, so a class added to `cli.py`
tomorrow gets no cross-fixture silence assertion and nothing reports the gap. **The mechanism for
fixing this already exists in this repository and is not applied here**: `tests/test_publishing.py`
reads `cli.ADVISORY_PREFIXES` from the module, so the advisory half of the set is derived while the
problem half is transcribed. Severity: medium — it does not make a present assertion wrong, it makes
a future one silently absent, which is the failure this audit exists to find.

**F-2 — reachability was proven per class, not per quiet fixture, and those are different claims.**
Step 3 shows each class *can* speak in a tree where a test asserts it is silent. It does not show
that **each particular quiet fixture** is within that check's reach.
[T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) is exactly this
distinction failing: `WIDE ROW` could fire perfectly well elsewhere while its own negative fixture
could not, because the check consumed the line under the header as a delimiter. A class-level
exercise cannot see that, and this audit's criteria are written per class, so this is the honest
statement of what step 3 bought and what it did not. Severity: medium.

### Recorded as examined, no action

- **Every class has a quiet case.** The first survey's nine apparent gaps were the survey's fault,
  and are recorded in step 2 rather than dropped, because the next person to grep for `assertNotIn`
  will reach the same wrong answer.
- **The duplicate-index blind spot for a verbatim whole-file copy** — step 3. It is the check's
  stated design (*outside the markers taskmd owns*), not a gap in its fixtures, so it is outside this
  audit's threshold.
- **The three rows of the GitHub Issues binding that examined nothing**, recorded in
  [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) §3 and flagged there as
  evidence this task would want. **Outside the threshold**: §1 scopes this audit to the classes
  `check` reports, and those rows are a binding's, not `check`'s. It stays in T-193's record.

**Decisions & assumptions**

- **The nine apparent gaps were re-examined instead of raised — rationale: a finding threshold
  catches defects in the subject, not defects in the instrument, and nine child tasks for gaps that
  do not exist would have been this audit's own worst output.** What made the difference was reading
  how the assertion is written rather than searching for how it is usually written — 2026-08-21.
- **F-1 and F-2 are raised as tasks rather than repaired here — METHOD §5.** Both repairs are small
  enough to be tempting; that is the argument `audit.md` answers, not an exception to it —
  2026-08-21.

**Outputs produced**

- this record
- [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md)
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md)

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The class set is **derived from the code** and the derivation is shown, so a class added since cannot be missing from the audit | met | §3 step 1 quotes the derived set — 17 problem prefixes from what is appended to `problems`, 4 from `ADVISORY_PREFIXES` — and names what it excludes and why. Nothing in the audit is read from a document that lists classes |
| Every class has a row, and the rows sum to the derived set — a class with nothing to say still has a row saying that | met | 21 rows against 21 derived, stated side by side in §3 step 4. Every row names its quiet case; none of the 21 was found without one |
| Each *has a quiet case* claim names the fixture and the assertion, not the intention | met | Each row names the test, and the fixture where the test uses one. Thirteen name `fails()`'s loop, which is the assertion the first survey could not see — recorded in step 2, because a literal search for `assertNotIn("CLASS"` reaches the wrong answer and the next person will run it |
| Each *can fire* claim quotes what happened when it was made to fire; a class whose quiet case was not exercised is recorded as unproven rather than as passing | met | 21 alarm lines quoted in §3 step 3, one per class, each from planting that class's defect in a tree where a test asserts silence. No class is recorded as unproven, because none was left unexercised |
| Every gap is a child task, and the audit closes only when each is resolved (`audit.md` step 5) | **carried** | Two findings, two child tasks: [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) for the hand-kept `LABELS` list, [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) for per-fixture reachability. Both are open, so **this umbrella stays open** — that is the criterion being met, not deferred |

**The audit's most useful output is a defect in its own instrument.** Run 1 reported all nineteen
classes `SILENT` — the answer a perfect audit and a completely broken one both produce. It had never
invoked `check` at all: every subprocess died on an `ImportError` and the instrument was grepping a
traceback for class names. The same run also produced nine apparent gaps that were the survey's fault
rather than the subject's. **Both would have become findings, and nine of them would have become
tasks.** What separated them from the two real findings was making the instrument produce a positive
result first, which is the rule this audit was run to check applied to the audit.

**Why this task does not close today.** `audit.md` step 5 and the last criterion both say an umbrella
closed over open children erases the link between the examination and its consequences. T-197 and
T-198 are open. The audit is complete — every class examined, every row filled, both findings raised
— and the task stays at `review` until they resolve. **The 2026-08-19 grant covers the full
lifecycle, and the lifecycle ends here**: closing is gated on the children, not on the grant.

**Open questions, re-read before closing.** §1's one question was answered by the owner on 2026-08-19
and is struck through; it sized the audit and the audit was run at that size. §3 raises none aimed at
anyone else. [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) carries one
of its own — whether the advisory classes join the same cross-fixture assertion — written into that
record where a view will show it, rather than left here where this task's closing would hide it.

**Child fix tasks raised**
- [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) — F-1, the hand-kept class list
- [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) — F-2, per-fixture reachability

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-22 | (no change) | **The grant was extended a third time, and this row is the one to read on what it now reaches.** The **project owner** instructed on **2026-08-22**, at the start of the session that resumed the eight, to *include the tasks you raise during the execution of this eight, where my involvement is not needed, so make them complete too*. **What it adds:** a task **raised while working the eight** is covered on the same terms as the eight themselves — carried through the full lifecycle to closure without stopping to ask for each phase, then committed and pushed — **provided it needs nothing from the owner**. **What it does not change:** it still authorises **phases, not answers**, so a task that reaches an open question belonging to the owner stops there; that limit is what *where my involvement is not needed* means, and it is the same one the row below states. **It amends exactly one clause of the row below** — *any task raised after 2026-08-22* is outside the grant no longer, when the task is raised **by this work** and needs nobody. A task raised by a later session, and any task that needs the owner, stay outside it. The eight ids below are unchanged: they are still the set given directly, and this addition is defined by **how a task arises**, not by a description of the backlog — which is the distinction the row below was written to protect. Recorded here, and in each task this work raises, for the reason that row gives. |
| 2026-08-22 | (no change) | **Multi-phase authorisation — current, and this row is the one to read.** The **project owner** granted it in three steps on **2026-08-22**: six tasks, then a seventh, then an eighth. **The set in force is eight**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). **What it covers:** this task — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each waiting on the owner for something no session can supply; and **any task raised after 2026-08-22**. **The eight ids bind, and the fact that they currently exhaust the backlog is a coincidence, not the rule.** Measured this date, the eight are exactly the open tasks that need nobody, and the four above are exactly the ones that do — 8 + 4 = 12 open, checked per id rather than by the total. That makes *everything that does not need the owner* look like a safe restatement, and it is not: the next task raised would join that description and not this grant. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **This row supersedes the *set and its bounds* in the rows below** — the grant as first given (six) and its first extension (seven). It does **not** supersede the limit specific to this task, which is stated below and still binds. |
| 2026-08-22 | (no change) | **The grant was extended to a seventh task, later the same day.** The **project owner** added [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md) to the six named in the row below, on the same terms and after reading why it was raised. **The set now in force is seven**: [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md), [T-218](T-218-give-the-rule-that-a-child-holds-its-parent-open-a-home-in-the-method.md). The row below records the instruction as first given — six ids — and its *what it does not cover* clause is amended by exactly this one addition. [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md) remains outside it, as does every task waiting on the owner. Nothing else changes: it still authorises **phases, not answers**. |
| 2026-08-22 | (no change) | **Multi-phase authorisation, and its limits.** The **project owner** instructed on **2026-08-22**, in the session that wrote the handoff carrying this work forward, that **six tasks** — [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md), [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md), [T-212](T-212-report-a-closed-parent-that-still-has-an-open-child.md), [T-214](T-214-decide-whether-the-class-set-subtraction-that-removes-nothing-needs-a-reader.md), [T-215](T-215-show-a-paired-fixture-s-quiet-case-is-in-reach-or-record-that-it-cannot-be.md), [T-216](T-216-repair-the-three-closed-parents-that-still-have-an-open-child.md) — be worked with the **full lifecycle**, and that the result be committed and pushed. **What it covers:** this task, one of the six — carried from where it now stands through the remaining phases to closure, without stopping to ask for each phase, then committed and pushed. **What it does not cover:** any other task. In particular it does **not** reach [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md), [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) or [T-213](T-213-test-whether-the-description-loses-a-competition-rather-than-turning-a-session-away.md), each of which waits on the owner for something no session can supply; nor [T-217](T-217-return-the-fields-list-can-filter-on-in-its-machine-form.md), raised the same day and after the instruction was given. **The set is six ids and not a description** — it was asked for as *all six tasks which does not need me*, and T-217 already makes that description name seven, so the ids are what bind. It authorises **phases, not answers**: a task that reaches an open question belonging to the owner stops there, because no grant of phases can answer one. Written into this record rather than kept in the session's handoff, because an authorisation kept anywhere else is one a later session can miss, or stretch to a task it never reached (`CLAUDE.md`, *one phase per request*). **Specific to this task: it cannot start until [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) closes.** That task is its open child, and a child holds its parent open — the rule the owner settled on 2026-08-22. The order inside this grant is therefore not free. |
| 2026-08-21 | → review | **Audit run under the 2026-08-19 grant; 21 classes, 21 rows, every one made to speak.** Two findings, both about the shape of the guarantee rather than a class without one: [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) (`LABELS` is hand-kept and names 14 of 21) and [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) (reachability was proven per class, not per fixture - T-150's failure). **Stays open**: `audit.md` step 5 gates closure on the children, and the grant covers the lifecycle, not the closing. The instrument's own first run reported every class silent without ever invoking `check`, which §4 records as the audit's most useful output. |
| 2026-08-19 | (no change) | **Authorisation (METHOD §3.1) recorded 2026-08-19, and not yet acted on.** The owner granted a later session the four tasks that need nobody else - T-193, T-190, T-191 and T-192 - **each through its full lifecycle, committed and pushed**. It is written here as well as in the handoff because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)), and an authorisation kept only there is one the session after next cannot find. **It reaches these four and no others**: the remaining open tasks each wait on a person, an external event, or a question still the owner's. |
| 2026-08-19 | (no change) | **Answered by the owner in a question round: the rule binds on advisories too.** Every class the validator prints is in the audit; limiting it to the exit-status classes was offered and rejected. The two reasons are in §1. This sets the audit's size, which the question said had to be settled before the rows are written. **No phase was started on this answer** ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | (no change) | **The owner extended the eight-task grant to cover what those eight raise**, on 2026-08-19: *if new tasks arise from these 8, work on the non-blocked ones too the same way*. It reaches this task because [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) raised it. **It does not answer §1's question**, which sizes the audit and is the owner's. Under the grant's own instruction, this task ends in a written question rather than a halted batch. Recorded here because a handoff is consumed once and renamed ([T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md)). |
| 2026-08-19 | → proposed | Raised by [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md)'s review, as that task's §1 said it would be. Typed `audit` rather than `fix` because it examines a body of work for a problem nobody has alleged of any particular class, and its findings become children rather than repairs (METHOD §5). `m` rather than `s`: the condition means exercising each quiet case, not grepping for one. |
