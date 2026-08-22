---
id: T-002
title: The same defect under a field name no schema mentions
status: proposed
milestone: 2.1
shipped_in: 0.4.0  # quiet: LABEL SHAPE - a real three-part version, which is the thing a grouping label must not be confused with
days: 1.5  # quiet: LABEL SHAPE - a quantity in an estimate field the rule exempts by name
targets: [3.0, 1.4.2, keep-me]  # quiet: LABEL SHAPE 1.4.2, keep-me - a real three-part version inside a list, beside a value that reads as no version at all
---

# T-002 - The same defect under a field name no schema mentions

`milestone` is not a key taskmd knows. `shipped_in` holds a real version and must stay silent.
`days` holds a quantity and must stay silent. `targets` is a **list**, because a field
the schema does not name arrives as one when a task writes one — and a check that only ever met
scalars crashed on the first real project it was pointed at.
