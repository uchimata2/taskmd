---
id: T-002
title: A month and a day that do not exist
status: proposed
created: 2026-8-5
updated: 2026-13-99
reviewed_on: 2026-08-161
windows: [2026-08-01, 2026-02-30, keep-me]
---

# T-002 - A month and a day that do not exist

`updated` is the deliberate specimen from T-162: month 13, day 99, and `check` exited 0 over it.

`reviewed_on` is the second shape of the same accident, under a field name **no config mentions** -
the assertion that the rule reads no key.

`created` is `2026-8-5`, which is a real date written without zero padding. It must stay silent:
the class is *date-shaped and not a date*, and this is a date.

`windows` holds a list. `2026-02-30` is a day that does not exist in a month that does, `keep-me` is
not date-shaped at all, and `2026-08-01` is an ordinary date.
