---
id: T-112
title: Stop check resolving a link that is displayed rather than navigable
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-092, T-095]
work_package: v0.2
owner: maintainer
business_value: medium
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
- Indented (four-space) code blocks — not measured, and this task should not legislate one it has
  not seen. Worth measuring while the fenced case is in hand.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 | Make the scan fence-aware and span-aware before matching | `cli.py` |
| 2 | Decide whether skipped matches are counted or silent | `cli.py`, this file §3 |
| 3 | Cover the five criteria, the negative cases first | `tests/test_cli.py` |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- <none yet>

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-10 | → proposed | **Written by an adopting project** — htmldeck — and placed here at the maintainer's request, alongside T-111 from the same source. It is a false positive on the boundary T-092 already decided rather than a new rule, which is why it is argued from T-092 and not from the adopter's preference. `medium`/`s`: it blocks a documented practice rather than corrupting any output, and the change is a scan that knows where code starts plus its negative fixtures. Re-scope, re-estimate or reject freely. |
