---
id: T-002
title: Three rows that lose nothing
status: proposed
---

# T-002 - Three rows that lose nothing

Every table below is quiet, and each is quiet for its own reason.

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
