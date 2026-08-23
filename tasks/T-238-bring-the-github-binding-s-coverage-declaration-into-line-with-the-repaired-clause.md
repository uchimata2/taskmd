---
id: T-238
title: Bring the GitHub binding's coverage declaration into line with the repaired clause
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-232, T-222]
work_package: M6
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: yes
deliverables:
  - plugin/skills/taskmd/docs/bindings/github-issues.md
---

# T-238 — Bring the GitHub binding's coverage declaration into line with the repaired clause

## 1. Specify

**Outcome**

`github-issues.md`'s coverage declaration carries the heading, the level and the position that
[`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 now fixes — so the contract's own example
of a binding is not the one that breaks its newest rule.

**Where this came from**

[T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md) fixed the heading, level
and position on 2026-08-23, because two uninvolved readers had to guess all three. It measured both
shipped bindings against the result and **reported rather than repaired**, for
[T-222](T-222-repair-the-coverage-clause-against-the-eight-defects-a-stranger-found.md)'s reason: a
binding edited inside the task that changed the contract makes it impossible to see which of the two
moved. This is the repair, in its own record, so the diff shows only the binding.

| | Required | `github-issues.md` today |
| :--- | :--- | :--- |
| Heading | `What the validator cannot check here` | *What this does not cover, and why* |
| Level | `###` | `####` |
| Position | after the mapping section, before the write step | after its own *After any write*, inside the migration-verification material |

**`local-markdown.md` already matches all three**, which is how those values were chosen — they were
measured, not invented. So this record has a working example to move toward and nothing to design.

**Scope**

- In: the heading, the level and the position of that one section, and any pointer to it that moves
- Out: what the declaration **says**. Its content was judged by two readers and is not re-opened here
- Out: the marked-region markers and what they wrap, which T-232 settled
- Out: `local-markdown.md`, which complies on all three
- Out: the declaration's **content** requirements, which neither binding met and which are
  [T-239](T-239-give-both-shipped-declarations-the-content-the-repaired-clause-now-requires.md)
  — found while doing this record

**Inputs**

- [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 *Where the declaration goes* — the three
  values, and the measurement behind them
- `plugin/skills/taskmd/docs/bindings/local-markdown.md` — the compliant example
- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the section to move

**Acceptance criteria**

- [ ] The section carries the required heading at `###`, positioned after the mapping section and
      before *After any write*
- [ ] Every pointer to that section still resolves, checked by running rather than by reading
- [ ] The declaration's text is unchanged apart from the heading line
- [ ] `taskmd check` passes and `tests/test_publishing.py` still finds the region and reads every
      class it names

**Open questions**
- **None.** The three values are fixed by the contract and a compliant example exists.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Read the section whole and list every directional reference in it — *above*, *below*, *the row below* — since moving text is what falsifies those and nothing checks them | the list, and which break at the new position |
| 2 | Decide what actually moves. The contract requires the **declaration** in that position; the coverage table is the binding's own detail and says so | the split, recorded |
| 3 | Move it, rename the heading, and leave a pointer at the old location | the edited binding |
| 4 | Re-run the region tests and `check` | the outputs |

**Step 1 exists because the obvious repair breaks something silently.** The section carries *some
land above as rows*, pointing at the verification rows earlier in the document; move the whole
section to just after *Operations* and that word becomes false, with no check anywhere that would say
so.

## 3. Implement

**Decisions & assumptions**

- **The declaration moved and the coverage table stayed** — 2026-08-23, and this is step 1's finding
  rather than a preference. [`BINDING.md`](../plugin/skills/taskmd/docs/BINDING.md) §4 requires *the
  declaration* at that heading and position; the table beneath it is, in the binding's own words,
  *this binding's own detail rather than the contract's requirement*. It also carries **directional
  references** — *some land above as rows* points at the verification rows at the far end of the
  document — which moving it would have silently falsified. So the marked region and its lead moved,
  the table kept its place and its old heading, and each now points at the other.
  *Rejected: move the whole section* — one edit, and it would have left a sentence saying *above*
  about material that had become *below*, which no check in this project can see.
- **The declaration's text is byte-identical apart from the heading** — 2026-08-23, which is the third
  criterion. What the region says was **later** filled out by
  [T-239](T-239-give-both-shipped-declarations-the-content-the-repaired-clause-now-requires.md), a
  separate record for a separate requirement, so this record's diff is a move and nothing else.

**Outputs produced**

- `plugin/skills/taskmd/docs/bindings/github-issues.md` — the declaration relocated and renamed

**Verification**

**Step 1, the directional references.** Read whole, the section carries three: *some land above as
rows*, *the row below*, and *the measurement under `No validator` below*. The second is internal to
the table. The first and third point outward, and the first is the one that breaks — the verification
rows it names sit at the far end of the document, so at the new position *above* becomes false. This
is what decided step 2.

**Step 3, the result.** The structure now reads:

```text
 98  ## Mapping
140  ## Operations
272  ### What the validator cannot check here      <- the declaration, at the required heading and level
287  ### After any write
...
     #### What this does not cover, and why        <- the coverage table, where it was, pointing up
```

After the mapping section and before the write step, which is the position §4 fixes and the one
`local-markdown.md` already used.

**Step 4, the gates.**

```text
python -m pytest tests/test_publishing.py -q  ->  21 passed
taskmd check                                   ->  exit 0
```

The region test is the one that matters here: it locates the marked region in every binding and reads
every class it names, so a move that had orphaned the markers or split them would fail it. **It was
also shown able to fail during this session** — a deliberately broken pointer in `METHOD.md` produced
`check exit = 1` and a named `BROKEN LINK`, and `check` caught a real dangling reference in a task
record minutes before this run.

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| The section carries the required heading at `###`, after the mapping section and before *After any write* | met | Line 272, `### What the validator cannot check here`, between `## Operations` and `### After any write` — the same arrangement `local-markdown.md` has |
| Every pointer to that section still resolves, checked by running | met | `check` exit 0, which resolves the document's links. The one prose reference to the old name — *What this does not cover* above says which — still names the coverage table, which kept both its name and its place |
| The declaration's text is unchanged apart from the heading line | met | The moved region is byte-identical. Its content was filled out afterwards by [T-239](T-239-give-both-shipped-declarations-the-content-the-repaired-clause-now-requires.md), deliberately in a separate record so this diff is a move and nothing else |
| `taskmd check` passes and `tests/test_publishing.py` still finds the region and reads every class | met | `exit 0` and `21 passed` |

**Child fix tasks raised**
- [T-239](T-239-give-both-shipped-declarations-the-content-the-repaired-clause-now-requires.md), and
  it is a **soft edge**: this record's outcome is the section's placement, which is complete. That the
  declaration also owed content nobody had measured is a different requirement, found here and
  carried there.

**Open questions, re-read before closing**
([`review`](../plugin/skills/taskmd/docs/method/review.md) step 5). §1 holds none, and none arose.


## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | proposed → done | **Closed: four criteria, four met.** The declaration now sits at `### What the validator cannot check here`, after the mapping section and before *After any write* — the arrangement `local-markdown.md` already had. **The plan's first step was to list the section's directional references, and it earned its place**: *some land above as rows* points at verification rows near the end of the document, so moving the whole section would have turned *above* into a falsehood that nothing in this project can check. **So the declaration moved and the coverage table stayed**, which is also what the contract actually asks — the table is the binding's own detail and says so in its own words. Each now points at the other. **The moved text is byte-identical apart from the heading**; the content the repaired clause also requires was found missing while doing this and is [T-239](T-239-give-both-shipped-declarations-the-content-the-repaired-clause-now-requires.md), kept separate so this diff is a move and nothing else. |
| 2026-08-23 | → proposed | Raised from [T-232](T-232-repair-the-coverage-clause-against-what-two-readers-found.md)'s `review`, whose scope reports a non-compliant binding and does not fix it, under the **project owner's** unattended grant of **2026-08-22** as extended the same day to reach what the work raises. **What the grant covers here:** this record, through the lifecycle to closure. **What it does not cover:** [T-231](T-231-cut-the-next-release.md), [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md), and **any audit** — unchanged. **No open question**, so unlike [T-237](T-237-the-softening-clause-t-228-repaired-has-a-second-instance-and-an-idiom-behind-it.md) this record does not stop at `specify`: the contract fixes all three values and `local-markdown.md` is a working example of them. **A soft edge from T-232 and not a child**, because T-232's outcome is the contract and the contract is complete; a binding that has not caught up does not make it incomplete, and a hierarchy edge would have held the release's blocker open for an edit to something else. |
