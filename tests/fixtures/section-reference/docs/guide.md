# The guide that cites the handbook

**A citation that resolves.** The rule is in [`handbook.md`](handbook.md) §2, and section 2 is <!-- quiet: SECTION REF 2 - the handbook prints section 2 -->
printed there.

**A citation that does not.** The exception is in [`handbook.md`](handbook.md) §9, and the
handbook stops at 2. This is the defect the class exists to report.

**A sub-number that resolves against a list item.** [`handbook.md`](handbook.md) §1.2 is the <!-- quiet: SECTION REF 1.2 - a sub-number naming a numbered item rather than a heading, which is how most are written -->
second rule under *What this is*, and it is a numbered item rather than a heading - which is how
most sub-numbers are written and why the rule reads both.

**A mark bound to nothing.** Somewhere above, §4 was mentioned with no document beside it. <!-- quiet: SECTION REF 4 - no document is named beside it, so nothing is guessed and it is counted into the Scope line -->
Nothing binds it, so nothing is guessed: it is counted into the `Scope` line and left alone.

**Conjoined marks.** The two that matter are [`handbook.md`](handbook.md) §1 and §2, <!-- quiet: SECTION REF 1 - the second mark inherits the first's document by conjunction, and both are printed -->
where the second inherits the first's document by conjunction rather than by being near it.

**A wrong citation quoted on purpose**, which must not be resolved because it is inside a fence: <!-- quiet: SECTION REF 404 - quoted on purpose, once inside a fence and once in a code span, so neither is resolved -->

```text
handbook.md §404 is what a broken reference looks like
```

And the same inside a code span: `handbook.md §404`.
