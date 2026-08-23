---
id: T-139
title: Check that the advisory lines the README lists are the advisory lines there are
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-100, T-121, T-134, T-138, T-141, T-161]
work_package: M6
owner: the project owner
business_value: medium
effort: s
created: 2026-08-12
updated: 2026-08-16
adopter_visible: yes
deliverables: []
---

# T-139 — Check that the advisory lines the README lists are the advisory lines there are

## 1. Specify

**Outcome**
A prose list of `check`'s advisory lines cannot name a set different from the one the code emits.
Adding a third advisory fails the suite until the document that enumerates them is updated, the same
way [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) made a
prose list of the commands fail.

**Why this one**
[`../README.md`](../README.md) devotes a paragraph each to `CONFIG DRIFT` and `DUPLICATE INDEX`.
[T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) added `LABEL SHAPE` and did not
add the paragraph — its scope named the task template and the shipped default, which are where an
*adopter* meets the wording, and missed the document a *stranger* reads before installing. It was
caught by the handoff reconcile sweep on 2026-08-12, by a person's grep rather than by anything in
the suite, which is the same way the command lists were caught before T-134 guarded them.

**This is T-134's class, one set over.** That task guarded the command lists and stopped there,
correctly — it was scoped to commands. Nothing generalised the guard, so the next enumerated set to
drift was the next one nobody was watching. The question worth settling here is whether the guard is
written a third time for advisories or written once for *any* marked list of a set the code owns.

**Scope**
- In: the advisory lines `check` can print, and every tracked document that enumerates them.
- In: whether the existing marker mechanism T-134 built is reused, extended, or copied.
- Out: what any advisory says or when it fires. Those belong to the tasks that added them.
- Out: the `Scope` and problem-class lines, unless the answer generalises to them for free — which is
  worth asking, since they are enumerated in prose too.

**Inputs**
- [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) — the
  marker mechanism and the reason a list is guarded rather than a sentence.
- `tests/test_publishing.py` — where the command-list assertions live.
- [`../README.md`](../README.md) — the three paragraphs as they now stand.

**Acceptance criteria**

Written at `specify`, 2026-08-16, to the owner's ruling — *any marked list of a set the code owns*.

- [x] The advisory names have **one home in the code**, and `check` prints through it. Until they do,
      there is no set to compare a document against, and this task cannot be done at all
- [x] An advisory added to the code and named in no marked list fails the suite, shown by doing it
- [x] An advisory dropped from a marked list fails too — the comparison is a **set**, both ways
- [x] Deleting a region's markers fails rather than passing vacuously
- [x] **A document that opts in is checked wherever it is** — the mechanism finds regions rather than
      reading a written list of documents. Shown by adding a third document with a wrong list
- [x] Adding a kind is one row in one table: no test names a member of any set, and none is edited

  **Half true, found by [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md)
  adding the third kind on 2026-08-16.** The *no test names a member* half held exactly as written.
  The *none is edited* half did not: `test_a_name_mentioned_in_a_sentence_is_not_a_list` located
  `README.md`'s region with `next()` and no default, so the first kind that document does not carry
  raised `StopIteration` rather than failing an assertion — and a region is a claim the carrying
  document makes about itself, so most new kinds will not be in `README.md`. T-149 fixed it in one
  line and the claim is true again. **The verdict below was reached by reading the module rather than
  by adding a kind**, which is the only way this could have been caught, and is the reason it is
  annotated here rather than corrected: what the review concluded on 2026-08-15 is what it concluded.
- [x] T-134's command lists are still guarded, both directions, shown by doing it
- [x] A name in a sentence outside a region is still not a list, shown on the real tree
- [x] Which sets are marked and which are not is decided explicitly, with the reason
- [x] The suite, `index` and `check` are green

**Open questions**
- ~~**Is the guard written a third time for advisories, or once for any marked list of a set the code
  owns?**~~ **Answered by the project owner on 2026-08-15: once, for any marked list of a set the
  code owns.** Put to them after
  [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) added a **problem**-class
  paragraph beside the three advisory ones, which is the case that makes the narrow reading
  arbitrary: the README now enumerates two different kinds of `check` line in the same register, and
  a guard covering one of them would be drawing its boundary where nothing in the document does.

  *Rejected: keep the guard to the advisory lines.* Narrower and cheaper, and it is what this task's
  title says. What decided it against: it is exactly how T-134 led here. That task guarded the
  command lists and stopped, correctly for its scope, and the next enumerated set to drift was the
  next one nobody was watching. A third instance of the same fault is evidence about the class, not
  about advisories.

  **This does not settle the mechanism.** Whether T-134's markers are reused, extended or copied is
  still `specify`'s, and so is which sets count as *owned by the code* — the scope line above already
  admits the `Scope` and problem-class lines conditionally, and that condition is now met.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Count what the code actually owns, before designing anything: how many advisory and problem classes there are, and where each name is written | The two counts in §3 |
| 2 | Give the advisory names one home and print through it, keeping the output byte-identical | `plugin/skills/taskmd/taskmd/cli.py` — `ADVISORY_PREFIXES` |
| 3 | Decide which sets are marked, on what rule | The decision in §3 |
| 4 | Generalise T-134's mechanism to a table of kinds, and discover the documents rather than list them | `tests/test_publishing.py` |
| 5 | Mark the README's advisory region | `README.md` |
| 6 | Show it firing on every case it exists to catch, each mutation reverted | The five results in §3 |
| 7 | Suite, `index`, `check` | Their output in §3 |

Step 1 is first for the sequencing rule, and it earned its place: the answer — *the code owns no
advisory set at all* — is what makes step 2 a prerequisite rather than tidying, and it would have
been discovered at step 4 otherwise, with the mechanism already built around a set that did not exist.

## 3. Implement

### Step 1 — what the code owns

`check` can print **15 problem classes** (`BROKEN LINK`, `CYCLE`, `DANGLING`, `DUPLICATE ID`,
`ID WIDTH`, `IGNORED LINK`, `MISSING OUTPUT`, `NO BLOCKER`, `PARKED TASK`, `STALE INDEX`,
`STORED DERIVED`, `TEMPLATE FIELD`, `TEMPLATE UNREACHABLE`, `VOCABULARY`, `WIDE ROW`) and **3
advisory lines**. `README.md` describes **1** of the 15 and **3** of the 3.

**Neither set had a home.** Every one of those names was a format string at its own `append` or
`print` site. `COMMANDS` is a real object, which is why T-134 could compare against it; there was
nothing to compare an advisory list *to*, and that — not the missing paragraph — is why T-138 could
ship a third advisory unnoticed.

### Step 2 — one home, and no change to the output

```python
ADVISORY_PREFIXES = ("CONFIG DRIFT", "DUPLICATE INDEX", "LABEL SHAPE")
```

`cmd_check` collects into `advisory = dict((name, []) for name in ADVISORY_PREFIXES)` and prints
through the tuple, so print order is the tuple's order and a misspelled name raises rather than
printing under a new prefix. The three prefixes are asserted 19 times across `tests/test_cli.py`, so
the refactor had a dense net under it; the suite stayed green with nothing edited.

### Step 3 — which sets are marked

**A marker is a claim of completeness, not a claim of importance.** The advisory paragraphs are
marked because the README names all three and means to. The 15 problem classes are **not**, because
it describes one of them — `WIDE ROW`, and only to contrast it with the advisories below it — and
never claims to be describing all fifteen. Marking it would make the suite demand fourteen paragraphs
nobody wants and the document does not promise.

So *a set the code owns* is necessary and not sufficient. The rule is both: **the code owns the set
in one place, and a document claims to enumerate it.** The marker is where that claim is made, which
is what T-134 already meant by *the region is what declares an intent to be complete*.

### Step 4 — the mechanism, generalised

One table. Each row is a kind: the marker token, how a member is written in prose, the set the code
owns, and the documents that must carry a region of that kind.

```python
KINDS = (
    Kind("commands",   re.compile(r"taskmd\s+([a-z][a-z0-9-]*)"), lambda cli: set(cli.COMMANDS), (...)),
    Kind("advisories", re.compile(r"`([A-Z]{3,}(?: [A-Z]+)*)`"),  lambda cli: set(cli.ADVISORY_PREFIXES), (...)),
)
```

Existing markers were **not** touched: T-134 already wrote `taskmd:commands` /
`taskmd:end-commands`, which is `taskmd:<kind>` / `taskmd:end-<kind>` read one way, so the
generalisation is free.

**`{3,}` on the advisory pattern is not decoration.** The region also contains `` `OK` ``, in the
sentence about `check` saying it twice over a duplicated index. A two-letter token would have been
read as a fourth advisory and the comparison would have failed on the real tree. Found by running it.

**The documents are discovered, not listed.** T-134's Q1 rejected *the test naming the two documents*
as a third statement of where the surface is written — and then its implementation shipped exactly
that, a module-level `MARKED` tuple, so a third document opting in would have been read by nothing.
The sweep now walks `git ls-files`. The written tuple survives for the **other** question, which no
scan can answer: which documents must have a region at all. A scan finds what has one; only a floor
notices one that was deleted.

**A marker counts only alone on its line, and that rule was written by running the sweep.** The first
run failed naming `tasks/T-134-….md` as a document behind on its command list — T-134's own record
*describes* the mechanism, quoting the marker inline in a sentence. Excluding `tasks/` would have been
an exclusion list to maintain and wrong anyway, since the next document to describe the markers would
be documentation. A real region marker sits on its own line in all three places that use one, and a
quotation inside backticks never does.

### Step 6 — firing, five ways

Each mutation applied, the suite run, the mutation reverted:

```text
1. a fourth advisory in the code, named in no document        exit 1  FAILED as intended
   AssertionError: Items in the first set but not the second:
2. an advisory dropped from the README's marked list          exit 1  FAILED as intended
   AssertionError: Items in the first set but not the second:
3. the README's advisory markers deleted                      exit 1  FAILED as intended
   AssertionError: [] is not true : no document carries a taskmd:advisories region, so this
   kind is declared and checked against nothing
4. a command dropped from the README's marked list            exit 1  FAILED as intended
   AssertionError: Items in the first set but not the second:
5. a THIRD document opts in with a wrong list                 exit 1  FAILED as intended
   AssertionError: Items in the first set but not the second:

tree restored; suite green again                              exit 0  6 passed
```

Case 3 trips **all three** tests, named individually:

```text
FAILED ...::test_a_name_mentioned_in_a_sentence_is_not_a_list
FAILED ...::test_each_marked_list_names_exactly_the_set_that_exists
FAILED ...::test_every_required_document_carries_its_region
3 failed, 3 passed
```

Case 5 is the one worth its own line: it is the gap T-134's written tuple left open, and under that
implementation it would have passed.

### Step 7

```text
264 passed, 3 skipped, 6 subtests passed
Wrote tasks/README.md - 18 active, 143 closed
OK - 161 task(s), ... 2368 front-matter value(s)          exit=0
```

**Decisions & assumptions**

- **The advisory names get a home in the code before anything is guarded** — 2026-08-16. Not part of
  the draft scope, and unavoidable: there was no set to compare against, and a test that read the
  names out of `cmd_check`'s source would have been a second parser for a fact the module could
  simply state. *Rejected:* deriving them by scanning `cli.py` for print prefixes.
- **The problem classes are not marked** — 2026-08-16, on the rule in step 3. *Rejected:* marking the
  `WIDE ROW` paragraph as a problem-class list, which is the reading the owner's ruling might invite
  and would assert a completeness the README does not have; the suite would then demand fourteen more
  paragraphs. The ruling is about the **mechanism** being general, and it now is — a third kind is one
  row.
- **The carrying documents are discovered; the required ones are still written** — 2026-08-16. Two
  different questions, and T-134 collapsed them into one tuple. *Rejected:* keeping the written tuple
  as the only source, which is the defect; *also rejected:* dropping it for pure discovery, which
  would make deleting a marker a silent pass — the vacuous case T-134's D2 exists to stop.
- **A marker is recognised only alone on its line** — 2026-08-16, forced by the first run. *Rejected:*
  excluding `tasks/` from the sweep.
- **`taskmd:commands` markers are reused unchanged** — 2026-08-16. Re-marking the two existing regions
  to a new token would have been churn in two shipped files for no behaviour.

**Outputs produced**
- `plugin/skills/taskmd/taskmd/cli.py` — `ADVISORY_PREFIXES`, and `cmd_check` printing through it.
- `tests/test_publishing.py` — `Kind`, `KINDS`, `marked_region`, `documents_carrying`, and
  `EveryMarkedListNamesTheSetTheCodeOwns` (three tests, replacing T-134's three).
- `README.md` — the `taskmd:advisories` region.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The advisory names have one home, and `check` prints through it | met | `ADVISORY_PREFIXES`, and `cmd_check`'s single print loop. The 19 existing assertions on the three prefixes passed unedited, which is what shows the output did not move. |
| An advisory added to the code and named nowhere fails | met | Case 1, run. |
| An advisory dropped from a marked list fails | met | Case 2, run. The comparison is a set difference reported both ways, so the failure names what is missing **and** what is named that does not exist. |
| Deleting a region's markers fails rather than passing vacuously | met | Case 3, and it trips all three tests, listed by name above. This is T-134's D2 carried over rather than re-argued. |
| A document that opts in is checked wherever it is | met | Case 5 — a third document, in a directory no test names, with a wrong list. **Under T-134's implementation this passed**, which is the finding this criterion existed to close. |
| Adding a kind is one row, and no test names a member | met | Read off the module: the two kinds differ only in their `Kind` row. No test mentions a command or an advisory by name; every set comes from `cli`. **Half of this was optimistic, and the first real use showed it — see the note under §1's criterion.** |
| T-134's command lists are still guarded, both directions | met | Case 4, run. The existing markers were not touched, so this is the original guard still working, not a reimplementation that happens to agree. |
| A name in a sentence outside a region is still not a list | met | On the real tree, for both kinds, and each half asserts its own premise first — it fails rather than passing if the README ever stops mentioning a member outside its regions. |
| Which sets are marked is decided explicitly, with the reason | met | Step 3. The rule is two-part — the code owns the set **and** a document claims to enumerate it — and the 15 problem classes are excluded under it, with the rejection recorded. |
| Suite, `index`, `check` green | met | `264 passed, 3 skipped`; index written; `check` exit 0. |

**Child fix tasks raised**
- none. [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md), raised by
  [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md) earlier the same day,
  asks whether it is an instance of this mechanism and is linked rather than answered here — this
  task's job was to make that question answerable, not to answer it.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-16 | (no change) | Kept current, not rewritten: §1's *adding a kind is one row* criterion and its review row both carry a note. [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md) added the third kind and found the second half of the claim false — the mechanism was sound and one test assumed `README.md` carried every kind. Nothing above is edited; the verdict of 2026-08-15 stands as what was concluded then. |
| 2026-08-16 | → done | All ten criteria met. **The title was narrower than the task and the task was narrower than the fault.** Two things had to be built before the guard could exist: the advisory names had no home in the code at all — every one was a format string at its print site — so there was nothing for a document to be compared against, which is the real reason T-138 shipped a third line unnoticed. And T-134's implementation contradicted its own rejected alternative: it named its two documents in a module-level tuple, the very *third statement of where the surface is written* its Q1 refused, so a third document opting in would have been read by nothing. Both are fixed, and case 5 of the firing evidence is that gap shown open. Two rules came out of running rather than designing: a marker counts only alone on its line, because the first sweep read T-134's own record as a command list; and `{3,}` on the advisory pattern, because the region says `OK`. The scope's conditional on the problem classes is answered **no** and the rule for it recorded — a marker is a claim of completeness, and the README makes no such claim about the fifteen. |
| 2026-08-16 | (no change) | **Authorisation (METHOD §3.1): the maintainer asked for this task's full lifecycle**, given 2026-08-16 as the subject of a handoff — *work all 4 from the list, full lifecycle*. The list is the four unblocked `fix` tasks named that day: [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md), [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md), [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) and [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md). It covers those four and **nothing else** — not the five `decision` tasks beside them on the same list, and not anything these four raise. Recorded here and not only in the handoff, which is consumed once and archived. This row records the permission, not a phase. **Note for whoever takes it**: the owner's ruling below narrowed this task to *any marked list of a set the code owns*, and `check` has gained two advisory lines since the README paragraph was written — so the instance and the guard are both live. |
| 2026-08-15 | (no change) | **The guarded set is any marked list of a set the code owns, not the advisory lines**, decided by the project owner on 2026-08-15. The occasion was [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) adding a problem-class paragraph beside the three advisory ones, so the scope line's conditional — *unless the answer generalises to them for free* — is now met rather than hypothetical. It authorises no phase, and it leaves the mechanism and the membership rule to `specify`. Recorded here rather than carried in a reply, because it changes what this task's title is about and the title is now narrower than the task. |
| 2026-08-12 | → proposed | Raised by the handoff reconcile sweep after [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) shipped a third advisory line and left `README.md` naming two. **The missing paragraph was written during the sweep and this task is the guard, not the paragraph** — fixing the instance silently would have left the class exactly as unguarded as T-138 found it. Not folded back into T-138: that task is closed and its scope was honest about where it looked, so the gap is in what nobody had generalised rather than in what it did. |
