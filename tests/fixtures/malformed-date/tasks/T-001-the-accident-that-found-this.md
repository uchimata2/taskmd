---
id: T-001
title: The two shapes a real off-by-one produced
status: proposed
created: 2026-08-18
updated: 2026-08-165
---

# T-001 - The two shapes a real off-by-one produced

`updated` here is the value a script actually wrote on 2026-08-16 while inserting authorisation
rows: an off-by-one in its match appended the day to the year-month-day it meant. `check` reported
`OK` over it, and `index` regenerated without complaint (T-162).

`created` is a real date and must stay silent, so the fixture cannot pass by reporting everything.
