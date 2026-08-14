---
id: T-001
title: Three rows that lose text
status: proposed
---

# T-001 - Three rows that lose text

Every table below loses text. None of it renders.

## A row with one cell too many

| Date | Note |
| :--- | :--- |
| 2026-08-15 | This row is fine |
| 2026-08-15 | This row is not | and this cell is dropped, silently |

## A row several cells too wide

| Field | Value |
| :--- | :--- |
| one | two | three | four |

## A pipe inside a code span, which is still a cell boundary

Markdown splits a row into cells before it parses inline spans, so the backticks do not protect the
pipe. The row is four cells against a two-column header, and the code span is broken as well.

| Name | Pattern |
| :--- | :--- |
| grep | `a | b` |
