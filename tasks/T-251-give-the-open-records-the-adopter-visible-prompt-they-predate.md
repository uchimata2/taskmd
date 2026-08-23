---
id: T-251
title: Give the open records the adopter_visible prompt they predate
type: fix
status: proposed
phase: specify
parent: null
blocked_by: []
related: [T-245, T-248, T-242]
work_package: M7
owner: the project owner
business_value: medium
effort: xs
created: 2026-08-23
updated: 2026-08-23
adopter_visible: no
deliverables: []
---

# T-251 — Give the open records the adopter_visible prompt they predate

## 1. Specify

**Outcome**
Every open record carries the `## 4. Review` prompt for `adopter_visible`, so none of them can close
without the judgement `docs/PUBLISHING.md` §7 reads.

**Why this one**
[T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) put the prompt in
the templates on 2026-08-23 and measured what that does to the **closed** backlog: nothing, because
those records contain no line to match. It did not measure the **open** backlog, and that is the gap.

Measured 2026-08-23, while writing a handoff, and **re-measured on 2026-08-23 across the whole open
set** while working this record's `specify`: the backlog holds **eight** open records, of which
**six predate the template change and carry no prompt.** Two of those six carry no `adopter_visible`
field either.

**The first measurement said "all six open records", and that was the wrong denominator** — six is
how many lack the prompt, not how many are open. The two it omitted are the two that already carry
the prompt, so the in-set was right and only the sentence was false. The table below is therefore
**every open record**, not only the hits, so the counts sum: a filter that lists only what it matched
cannot report what it did not see.

| Record | Has the prompt | Has the field |
| :--- | :---: | :---: |
| [T-244](T-244-audit-everything-0-6-0-ships-before-1-0-0-and-review-the-audit-method-while-using-it.md) | no | yes |
| [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) | no | **no** |
| [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md) | no | yes |
| [T-247](T-247-decide-whether-taskmd-validates-a-finding-field-against-a-register.md) | no | yes |
| [T-240](T-240-the-competition-rig-does-not-reproduce-the-silence-it-was-built-to-explain.md) | no | **no** |
| [T-246](T-246-cut-1-0-0-once-the-audit-s-findings-are-applied.md) | no | yes |
| [T-250](T-250-give-the-context-registers-the-permitted-shape-for-history.md) | **yes** | yes |
| T-251 — this record | **yes** | yes |

The last two were created after
[T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) landed, so they
were copied from the fixed template and need nothing. Both prompt lines were compared byte for byte
against the template's with `cat -A` and match, trailing whitespace and line ending included.

`check` is silent on all six and correctly so — an open record has not reached `## 4. Review`, which
is the gate that keeps the rule from being 77% noise. The consequence is only visible later: each
closes with nothing having asked, and §7 blocks on it. That is the wall `0.6.0` met, arriving through
the open backlog rather than the closed one.

**Scope**
- In: the six open records above, and any opened before this lands
- In: the two missing `adopter_visible` fields
- Out: **closed records.** They contain no line to match and METHOD rule 5 forbids rewriting them.
  The three the rule already reports are
  [T-248](T-248-judge-adopter-visible-on-the-three-records-the-new-rule-reports-unmarked.md)
- Out: judging the value on the six. Adding the prompt is not answering it — the judgement is made
  when the work is understood, which is what §7 says and what the prompt exists to ask for

**Inputs**
- [`tasks/_task-template.md`](_task-template.md) — the prompt's wording, which is what must match
- [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) §3 — why the
  prompt is a body slot and not a front-matter field, and why it carries no code spans

**Acceptance criteria**
- [ ] Every open record carries the prompt, byte-identical to the template's line — a near-miss is a
      slot `check` cannot match
- [ ] The two records missing `adopter_visible` have the field, unjudged is not an option once closed
- [ ] Closing one of them without answering the prompt is reported, shown by making `check` fail on
      a real case rather than by a clean tree
- [ ] `taskmd check` still exits 0 on the tree, since all six remain open

**Open questions**
- **Does the second acceptance criterion survive? It asks for a field whose presence nothing can
  observe, and the scope forbids giving it a value.** Raised 2026-08-23 while working this
  `specify`; it changes what this record produces, so per METHOD §3.2 it is answered before the
  phase ends. The measurements, all taken 2026-08-23:
  - **`docs/PUBLISHING.md` §7 cannot tell absent from empty.** Its command reads
    `av=$(... adopter_visible ...)` and prints `${av:-UNMARKED}`, and a shell parameter default
    fires on unset *and* on empty. So T-241 today and T-241 with a valueless field both print
    `UNMARKED <id>`, which is the state §7 wants — *absent means nobody judged it* — reached either
    way.
  - **`taskmd context` cannot either.** Run on T-241, it prints `adopter_visible -`; the dash is how
    a value that is not there renders, and an empty one has none to render.
  - **`check` cannot either**, because the field is not in this project's schema vocabulary — it
    appears in `.taskmd/config.md` only in `context_fields`, which selects what `context` shows and
    validates nothing.
  - **A named unjudged value would be worse than either.** `adopter_visible: unjudged` makes §7
    print `unjudged <id>`, and §7's three counts are `grep -c` on `^yes `, `^no ` and `^UNMARKED `,
    which must **sum** to the printed lines. A fourth value breaks that sum — the one check §7 has
    that reports what it failed to see. So this option is rejected on measurement, not on taste.
  - **The obligation the criterion is reaching for is already carried by the first one.** T-245's §3
    named this exact gap and left it open deliberately: *"The check sees an unfilled slot, not an
    unfilled field."* The prompt line is what bites at close; the field is written when the prompt is
    answered.
  - **Recommendation: drop it**, and take the two `no` cells in the table above as a statement of
    where the value is not yet written rather than as work. The alternative — add the field with an
    empty value on T-240 and T-241 — costs one line each and buys nothing any of the three readers
    above can see, while putting a field on a record whose §7 meaning is *nobody judged this*, which
    is what its absence already says.
  - **Cost if the recommendation is wrong:** two records keep a shape the owner wanted uniform, and
    the repair is two lines. **Cost if the alternative is wrong:** two records carry a field that
    reads as judged-and-blank rather than unasked, in the one place §7 is relied on not to default
    quietly.

## 2. Plan

| # | Step | Output |
| :-- | :--- | :--- |
| 1 |  |  |

## 3. Implement

**Decisions & assumptions**
- <decision — rationale — date>

**Outputs produced**
- none yet

## 4. Review

| Acceptance criterion | Result | Note |
| :--- | :---: | :--- |
|  |  |  |

**Adopter-visible?** <yes or no - then set adopter_visible in the front matter, per the test in docs/PUBLISHING.md section 7>

**Child fix tasks raised**
- none

## Log

| Date | Status change | Note |
| :--- | :--- | :--- |
| 2026-08-23 | (no change) | **`specify` worked under the grant below and stopped at one question**, which is why the phase is not closed. Two things changed in §1 and neither widens the outcome. **The denominator was corrected**: the record said *all six open records* when six is how many lack the prompt and eight are open, and the table now carries every open record so the counts sum. The in-set was right, so nothing about the work changed. **The second acceptance criterion was challenged, not removed** — it asks for a field whose presence `docs/PUBLISHING.md` §7, `taskmd context` and `check` were each measured unable to observe, while the scope forbids giving it a value. It stands until the owner answers. |
| 2026-08-23 | (no change) | **The owner brought this record inside the grant**, given 2026-08-23: *"Add T-251 to the handoff too."* **The row below is not corrected**, because it was true when written — the earlier grant did not reach here, and this is a second instruction rather than a re-reading of the first. **What it covers:** this record's `specify` through `review`, committing and pushing, and anything raised by that work. **What it does not:** the rest of the backlog. **It is worked first of the three**, and the reason is in this record's §1: [T-241](T-241-verify-the-published-0-6-0-from-outside-and-record-what-cannot-be-reached.md) carries no `adopter_visible` field at all, so closing it before this lands closes it unjudged and `docs/PUBLISHING.md` §7 blocks on it at the next release note — which is the failure this record exists to stop, caused by the order it was worked in. |
| 2026-08-23 | → proposed | **Found by the reconcile sweep while writing a handoff**, 2026-08-23. [T-245](T-245-prompt-the-adopter-visible-judgement-at-the-moment-a-record-closes.md) stated what its fix does to the closed backlog and was not asked about the open one; the sweep asked. **The owner's full-lifecycle grant of 2026-08-23 does not reach this record** — it covers T-250, T-241 and anything raised *by their work*, and this was raised by the handoff, not by either of them. |
