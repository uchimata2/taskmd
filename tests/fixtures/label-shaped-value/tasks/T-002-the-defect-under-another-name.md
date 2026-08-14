---
id: T-002
title: The same defect under a field name no schema mentions
status: proposed
milestone: 2.1
shipped_in: 0.4.0
days: 1.5
targets: [3.0, 1.4.2, keep-me]
---

# T-002 - The same defect under a field name no schema mentions

`milestone` is not a key taskmd knows. `shipped_in` holds a real version and must stay silent.
`days` holds a quantity and must stay silent. `targets` is a **list**, because a field
the schema does not name arrives as one when a task writes one — and a check that only ever met
scalars crashed on the first real project it was pointed at.
