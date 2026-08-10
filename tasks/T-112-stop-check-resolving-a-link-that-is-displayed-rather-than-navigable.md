---
id: T-112
title: Stop check resolving a link that is displayed rather than navigable
type: fix
status: done
phase: review
parent: null
blocked_by: []
related: [T-092, T-095, T-091, T-114]
work_package: v0.2
owner: maintainer
business_value: critical
effort: s
created: 2026-08-10
updated: 2026-08-10
deliverables: [plugin/skills/taskmd/taskmd/cli.py, tests/test_cli.py]
---

# T-112 — Stop check resolving a link that is displayed rather than navigable

## 1. Specify

**Outcome**
A document can quote taskmd's own output without `check` resolving the quoted rows as its own
links. Link syntax inside a fenced code block or an inline code span is text being shown, not a
pointer being made, and is left alone.

**Why this one**
**[T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) already drew this boundary,
and drew it in the right place.** It separates a pointer from *a path merely being discussed*, and
ruled the second out — recorded in `cli.py` as *a decision rather than an omission*. A link inside a
fence is the same category one syntax over: it renders as literal characters, nobody can follow it,
and it cannot be broken. So the rule is settled; it is enforced for prose and not for code.

The mechanism is why. `check_links` runs `LINK.finditer` over the result of `read(md)` — one flat
regex across the whole file, with no notion of a fenced block or a code span. Nothing decided that
fenced text should be scanned; the scan simply never learned that fences exist.

**Why an adopter hits this and this repository does not.** `index` emits a Markdown link per row,
by construction. A project whose method is to paste what a command actually printed therefore puts
link syntax inside a fence the moment it quotes a board row — and its own generated index is the
thing it most wants to quote. This repository passes today because no task here happens to quote one.

> **The last sentence was wrong, found 2026-08-10 under
> [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md), and how it was wrong raises
> what this task is worth.** [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md)
> quotes an `index` row inside a fence, with the target abridged to three dots — the same
> abridgement, in the same construction, as the paste that started this. This repository does not
> pass because it lacks the case. **It passes because Windows resolves that target and Linux does
> not**: a trailing-dot path component is stripped by the filesystem layer, so the abridged target
> silently resolves to the tasks folder itself and the link is called good. Run the same tree under
> WSL and `check` exits 1 on a repository that is clean on the machine it was written on.
>
> **Reproduced on a real Linux runner, 2026-08-10, and it is larger than one test.** The CI runner
> [T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md) set up went red on its
> first run, and **every one of its seven failing assertions is this defect** — six in
> `tests/test_cli.py` and one in `tests/test_runtime.py`, all of them cases that run `check` over
> this repository and assert it is clean, all of them reporting the same
> `BROKEN LINK tasks/T-065-…`. Two things this adds to the paragraph below. It is no longer
> conditional on which `bash` a session happens to find — an ordinary `ubuntu-latest` checkout
> reproduces it. And it is what stands between this repository and a green runner: until this closes,
> the mechanism the maintainer asked for on 2026-08-10 arrives red, which is the state that teaches
> people to stop reading it.
>
> So this is not only a false positive that blocks a practice. **It is an R-20 violation** — output
> that is not byte-identical across platforms — and it is currently the reason
> `tests/test_runtime.py` fails when the `bash` a session finds happens to be a Linux one. The
> reproduction is one line each way, from the repository root: on Windows a probe for the existence
> of the tasks folder with three dots appended answers true, and under WSL the same probe answers
> false.
>
> Two consequences for the criteria below rather than for the fix, which does not change: whatever
> stops scanning fenced text removes this by construction, and after it lands the repository should
> be checked once under a Linux `bash` — because until then nothing here was ever measuring the
> thing that was broken. The criteria are not edited; this is the note that says why the fourth one
> now has a second reason to exist.

**What it cost, 2026-08-10.** An adopting project (htmldeck, `github.com/uchimata2/htmldeck`) was
writing up a separate proposal and pasted one `index` row as evidence, with the filename abridged.
`check` reported the ellipsis as a broken link. The paste was then rewritten to carry a real,
resolvable filename — **so the checker did not find a defect, it edited the evidence.** A quotation
adjusted to satisfy a link checker is no longer a quotation, and the adjustment leaves no trace.

The same project then wrote a task describing the defect and **could not write it without committing
it**: three more failures in one run, every one a link-shaped example in prose backticks. That is
also the measurement of the code-span half — it behaves exactly like the fence. The examples in that
task, and in this one, are paraphrased for that reason.

**A second consequence, on the numbers.** `links += 1` runs on every match, before nothing and after
no filter. So for a project that quotes output, the link count [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md)
added to the summary is inflated by strings no reader can follow — the denominator reports coverage
that was never navigable.

**Scope**
- In: fenced code blocks, and inline code spans, which measure the same.
- In: whether the excluded matches should be counted anywhere. Silence is defensible; so is a note,
  in the spirit of T-095. Recommended: leave them out of `links` entirely and say nothing, because
  the count means *pointers checked* and these were never pointers.
- Out: **bare paths in prose.** T-092 settled that and this proposes no change to it.
- Out: reference-style links, and any other link form — not measured here.

**Inputs**
- `plugin/skills/taskmd/taskmd/cli.py` — `LINK`, `check_links`, and the comment above `LINK`
  recording T-092's decision.
- [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) — the boundary, and its
  criterion that a false-positive boundary should be *proven rather than asserted*.

**Acceptance criteria**
- [ ] A fixture holds a fenced block containing link syntax whose target does not exist, and `check`
      does not report it — the false-positive boundary proven the way T-092 required.
- [ ] The same for an inline code span.
- [ ] A real link on the line before and the line after the fence is still reported when broken, so
      the fix cannot be a blanket loosening.
- [ ] A document quoting the full output of `taskmd index` passes.
- [ ] The reported link count excludes what was not examined.

**Open questions**
- ~~Indented (four-space) code blocks — not measured, and this task should not legislate one it has
  not seen.~~ **Measured 2026-08-10, and the answer is to leave them out.** Ten lines in this
  repository are indented four spaces and carry link syntax, and every one sampled is a **list or
  table continuation holding a real, resolvable link** — not a code block at all. Treating that
  indentation as code would stop checking ten genuine links here alone, which is precisely the
  blanket loosening criterion 3 exists to prevent. The question is answered by the corpus rather
  than by a reading of the specification, and it is answered *against* extending the fix.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Make the scan fence-aware and span-aware before matching | `cli.py` |
| 2 | Decide whether skipped matches are counted or silent | `cli.py`, this file §3 |
| 3 | Cover the five criteria, the negative cases first | `tests/test_cli.py` |

## 3. Implement

**Decisions & assumptions**

- **D1 — blank the code regions before matching, rather than filter matches after** — 2026-08-10.
  `without_code` returns the document with fences and spans replaced by spaces, character for
  character, and `LINK.finditer` runs on that. Filtering afterwards would have needed the same
  region information to decide each match, and would have left `links += 1` counting things it then
  discarded — criterion 5 is a count, not a report, so the exclusion has to happen before the match
  exists. Blanking rather than deleting keeps every other offset where it was.
- **D2 — code spans are line-scoped** — 2026-08-10. A span regex allowed to cross lines lets one
  stray backtick swallow the rest of a document and take every real link in it out of the check.
  That is a **false negative**, which is worse than the false positive being fixed and is what
  criterion 3 exists to catch. A span that genuinely wraps a line is not scanned as code; that costs
  a false positive of the kind already being removed, in a case nobody has produced.
- **D3 — indented code blocks stay out, and this is measured rather than assumed** — 2026-08-10. See
  the answered open question above: ten lines here are indented four spaces and carry link syntax,
  and every one sampled is a list or table continuation with a real link. Extending the fix to them
  would blind the checker to genuine links in this repository on the day it landed.
- **An unclosed fence runs to the end of the document**, which is what Markdown does with one. Noted
  as an assumption rather than a decision: no case in this corpus depends on it.

**The first two tests passed against the unfixed scanner, and that is worth more than the fix.**

Both were written the obvious way — a fenced link whose target is `...`, asserted not to be reported
— and both went green *before* any code changed. The reason is the defect itself: `...` resolves on
Windows, so there was nothing for the unfixed scanner to report, and the test could not tell a
working fence-skip from a filesystem that fabricates the target. **A test can be invalidated by the
very bug it is written for.** Recorded here because after the repair it leaves no trace: the tests
pass either way and nothing in the diff shows they once passed for the wrong reason.

Rewritten twice over: the fenced and span cases now use a target absent on every platform, so they
fail before the fix and pass after it *anywhere*; and the abridged `...` case is kept as its own
regression guard asserted on the **link count** rather than on the report, because the count is
wrong on Windows too — an unfollowable string was being counted as a link checked regardless of
where it ran.

**Verification**

Five tests, shown failing against the unfixed scanner first:

```
FAIL: test_a_fenced_link_is_left_alone_and_the_real_ones_around_it_are_not
  AssertionError: 'nowhere-inside.md' unexpectedly found in 'BROKEN LINK ...'
FAIL: test_a_link_inside_a_code_span_is_left_alone
  AssertionError: 1 != 0 : BROKEN LINK   notes.md -> nowhere-in-a-span.md
FAIL: test_a_document_quoting_the_whole_generated_index_passes
  AssertionError: 1 != 0 : BROKEN LINK   quoted.md -> T-001-x.md
FAIL: test_the_abridged_target_this_repository_carried_stops_being_a_link
  AssertionError: 1 != 0 : an abridged target was counted as a link checked
FAIL: test_the_link_count_excludes_what_was_never_a_pointer
  AssertionError: 1 != 0 : a link shown in a code span was counted as a link checked
Ran 5 tests in 0.240s
FAILED (failures=5)
```

and passing after it, with the rest of the suite unmoved — the four in `test_runtime.py` are
T-114's and are this machine's:

```
test_budget.py     Ran 5 tests   OK
test_cli.py        Ran 89 tests  OK
test_list.py       Ran 29 tests  OK
test_runtime.py    Ran 27 tests  FAILED (failures=4)
test_schema.py     Ran 45 tests  OK
```

`check` on this repository still exits 0, and **the link count moved from 1,137 to 1,136** — one
string that was never a pointer leaving the denominator, which is the T-065 row this task was
finally raised over. Measured across the fix alone, before this record's own links were written; the
figure a reader sees today is larger and that difference is this file, not a regression.

**Checked once under a real Linux runner, which is what this task has been owed since it was
raised.** The annotation in §1 asked for exactly this, on the grounds that nothing on the
development machine was ever measuring the thing that was broken. The CI job
[T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md) built went from seven
failing assertions to none on the commit carrying this fix:

```
Ran 5 tests    Ran 89 tests    Ran 29 tests    Ran 27 tests    Ran 45 tests
every module passed
```

All 195 pass on `ubuntu-latest`. The three `test_runtime.py` failures this machine reports are
absent there, which is T-114's whole point and is not this task's to close.

**Outputs produced**
- [`plugin/skills/taskmd/taskmd/cli.py`](../plugin/skills/taskmd/taskmd/cli.py) — `FENCE`,
  `CODE_SPAN`, `blanked`, `without_code`, and one call site in `check_links`
- [`tests/test_cli.py`](../tests/test_cli.py) — `LinkSyntaxShownRatherThanMade`, five cases

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
| A fixture holds a fenced block containing link syntax whose target does not exist, and `check` does not report it | met | `FENCED`, and it took two attempts to make it mean anything — the first target was the abridged `...`, which resolves on Windows, so the test passed before the fix. The one that ships names a file absent on every platform and was seen failing first |
| The same for an inline code span | met | `SPANNED`, and the document count is asserted alongside it so it cannot pass by the document not being read — the same trap one level down |
| A real link on the line before and the line after the fence is still reported when broken, so the fix cannot be a blanket loosening | met | Same fixture as the first, one run: two `BROKEN LINK` reports, the fenced one absent. This is also what decided D2 and D3 — a line-crossing span or an indented-block rule would each have failed this criterion on real documents |
| A document quoting the full output of `taskmd index` passes | met | Built by running `index` on a scratch project and quoting what it actually wrote, rather than a hand-made imitation of it. Fails before the fix on `quoted.md -> T-001-x.md` |
| The reported link count excludes what was not examined | met | Two projects differing only by the quoted block report the same count. On this repository, 1,137 to 1,136 |

**The criterion that was not written, and was owed.** §1's annotation asked for the repository to be
checked once under Linux, on the grounds that nothing here had ever measured the defect. Done, and
it is the strongest evidence this task produced: seven failing assertions to zero, all 195 green on
`ubuntu-latest`. Recorded as evidence rather than as a criterion invented after the fact.

**Child fix tasks raised**
- none. The `medium` this was raised at was wrong and the log below already said so; it was raised
  to `critical` by the maintainer on 2026-08-10 once the runner made the cost visible. That is a
  correction to this task, not a new one.

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → in_progress → review → done | Raised to `critical` by the maintainer and taken next, on the evidence that it was the only thing between this repository and a green runner. All five criteria met, plus the Linux check §1 asked for: **seven failing assertions to zero, 195 green on `ubuntu-latest`**. Two things are worth more than the fix, which is twenty lines. **The first two tests passed against the unfixed scanner** — written the obvious way, asserting the abridged target is not reported, they were satisfied by Windows resolving that target rather than by any fence-skipping, and after a repair such a test leaves no trace of having been vacuous. They were rewritten to fail on every platform, and the abridged case kept as its own guard asserted on the *count*, which was wrong everywhere. **And the open question was answered against extending the fix**: ten lines here are indented four spaces and carry link syntax, and every one sampled is a list continuation holding a real link, so legislating indented blocks would have blinded the checker to genuine links on the day it landed. Measured on the corpus rather than reasoned from the specification, which is the only reason it came out that way. |
| 2026-08-10 | (no status change) | Found under T-091 that this repository has carried an instance since T-065, invisibly: the abridged target resolves on Windows and not on Linux, so `check` is clean here and red under WSL on the same commit. Annotated above rather than rewritten, and `related` now carries T-091 and T-114 — the latter is the other half of the same failing run. Worth re-reading `medium` against: this is an R-20 violation in the tree, not only a blocked practice in an adopter's. |
| 2026-08-10 | → proposed | **Written by an adopting project** — htmldeck — and placed here at the maintainer's request, alongside T-111 from the same source. It is a false positive on the boundary T-092 already decided rather than a new rule, which is why it is argued from T-092 and not from the adopter's preference. `medium`/`s`: it blocks a documented practice rather than corrupting any output, and the change is a scan that knows where code starts plus its negative fixtures. Re-scope, re-estimate or reject freely. |
