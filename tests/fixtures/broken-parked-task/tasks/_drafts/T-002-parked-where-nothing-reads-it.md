---
id: T-002
title: A complete task in a folder enumerate skips
type: deliverable
status: proposed
phase: specify
---

# T-002 - A complete task in a folder enumerate skips

Body. Nothing is wrong with this file. It carries a schema-valid id and would load as a task from
`tasks/` - it is here, one folder down, under a name beginning with `_`, so the walk never reaches
it. Before T-107 that cost exit 0 and a task in no view and on no edge.
