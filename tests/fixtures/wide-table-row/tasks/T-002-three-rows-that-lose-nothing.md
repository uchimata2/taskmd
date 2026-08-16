---
id: T-002
title: Three rows that lose nothing
status: proposed
type: fix | research
business_value: high | low
effort: xs | s | m | l | xl
---

# T-002 - Three rows that lose nothing

Every table below is quiet, and each is quiet for its own reason, and so is the front matter above.

The three pipe-carrying lines up there are the fourth quiet case (T-150). They are the shape of the
shipped task template — the same three fields, each a `|`-separated menu — which an adopter's own
scanner reported as the only defect in their tree: five pipes, no table. Ours does not fire, because
a header is only a header when the next line is a delimiter row and no front-matter line is. That
silence was proven by the corpus until this file, and a corpus is the weaker instrument: it changes
without anyone deciding to, and the template could stop using a menu for reasons having nothing to
do with this check.

**Three lines, and the widths ascend, because two would have proved nothing.** `check_wide_rows`
reads `lines[index + 1]` as the delimiter and starts rows at `index + 2`, so a two-line menu has no
row under it even with the guard removed — the case would sit here looking decisive and firing on
nothing. With three, removing the guard makes `type` a 2-column header, skips `business_value`, and
reads `effort` as a 5-cell row that reports. That is what makes this fixture load-bearing rather
than present.

## A trailing cell with nothing in it

Wider than the header and loses no text, so there is nothing to tell anyone.

| Date | Note |
| :--- | :--- |
| 2026-08-15 | A note | |

## An escaped pipe, which is content and not a boundary

| Name | Pattern |
| :--- | :--- |
| grep | a \| b |

## A short row, which Markdown pads

| Date | Status | Note |
| :--- | :--- | :--- |
| 2026-08-15 | done |

## A table inside a fence, which is quoted output and not a table

```
| ID | Title |
| :--- | :--- |
| T-001 | this row is wider than its header and is not read |
```

## And a real table after the fence, which is read

| Date | Note |
| :--- | :--- |
| 2026-08-15 | Read, and fine |
