# Task index — taskmd

Generated from each task's front-matter. **Do not hand-edit** between the markers below.

```
python -m taskmd index            # regenerate this file
python -m taskmd context T-001    # everything needed to start a task
python -m taskmd check            # validate
```

Working method: [`../CLAUDE.md`](../CLAUDE.md). Scope and requirements:
[`../docs/SCOPE.md`](../docs/SCOPE.md). Problem evidence: [`../docs/BRIEF.md`](../docs/BRIEF.md).

<!-- taskmd:index - generated, do not edit by hand -->

## Active

| ID | Title | Work Package | Status | Phase | Parent | Children | Blocked By | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) | Write the skill that teaches the agent to use the CLI | - | `proposed` | `specify` | - | - | T-002, T-008 | T-006 | T-008, T-017, T-019, T-021, T-022, T-026, T-032 |
| [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) | Settle the id scheme and the claimed scale ceiling | - | `proposed` | `specify` | - | - | T-001 | - | T-002, T-006, T-007, T-010 |
| [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) | Align with the handoff tracker-binding contract | - | `proposed` | `specify` | - | - | T-009 | - | T-002, T-007, T-009, T-033 |
| [T-006](T-006-package-document-and-publish.md) | Package, document and publish | - | `proposed` | `specify` | - | - | T-002, T-003, T-008, T-009, T-010, T-011, T-018 | - | T-004, T-013, T-019, T-020, T-023, T-026, T-034 |
| [T-010](T-010-write-the-github-issues-binding.md) | Write the GitHub Issues binding | - | `proposed` | `specify` | - | - | T-009 | T-006 | T-004, T-009, T-026 |
| [T-011](T-011-runtime-discovery-and-project-hook-commands.md) | Runtime auto-discovery and project hook commands | - | `proposed` | `specify` | - | - | T-002 | T-006 | T-013 |
| [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) | Confirm byte-identical output on macOS and Linux | - | `proposed` | `specify` | T-002 | - | - | - | T-006, T-023, T-030 |
| [T-021](T-021-settle-what-the-context-closing-line-may-say.md) | Settle what the context closing line may say | - | `specified` | `specify` | T-002 | - | - | - | T-003, T-022 |
| [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) | Stop config errors printing an absolute install path | - | `proposed` | `specify` | - | - | - | - | T-006, T-019, T-020, T-024, T-030 |
| [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) | Say so when tasks_dir names something that is not a folder | - | `proposed` | `specify` | - | - | - | - | T-019, T-023 |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | Let check notice a stale generated index | - | `proposed` | `specify` | - | - | - | - | T-002, T-009, T-019, T-026 |
| [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) | Audit the whole project before the remaining build | - | `review` | `review` | - | T-027, T-028, T-029, T-030, T-031, T-032, T-033, T-034 | - | - | T-003, T-006, T-010, T-025 |
| [T-027](T-027-give-the-design-rule-one-home.md) | Give the design rule one home | - | `proposed` | `specify` | T-026 | - | - | - | T-017, T-028, T-031 |
| [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) | Budget the whole always-loaded context, not one file | - | `proposed` | `specify` | T-026 | - | - | - | T-015, T-027 |
| [T-029](T-029-reject-unknown-arguments-on-every-command.md) | Reject unknown arguments on every command | - | `proposed` | `specify` | T-026 | - | - | - | T-002, T-022 |
| [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) | Settle the schema module's own entry point | - | `proposed` | `specify` | T-026 | - | - | - | T-020, T-023 |
| [T-031](T-031-give-the-list-rationale-one-home.md) | Give the list rationale one home | - | `proposed` | `specify` | T-026 | - | - | - | T-022, T-027 |
| [T-032](T-032-repair-the-audit-template-and-validate-templates.md) | Repair the audit template, and validate templates at all | - | `proposed` | `specify` | T-026 | - | - | - | T-003, T-022 |
| [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) | Resolve the F1 reference inside this repository | - | `proposed` | `specify` | T-026 | - | - | - | T-005, T-013 |
| [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) | Let the pre-publish check see files not yet tracked | - | `specified` | `specify` | T-026 | - | - | - | T-006, T-013, T-018 |

## Closed

| ID | Title | Work Package | Status | Phase | Parent | Children | Blocked By | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) | Decide how the front-matter schema is configured | - | `done` | `review` | - | - | - | T-002, T-004 | T-012 |
| [T-002](T-002-implement-the-core-cli-context-index-check.md) | Implement the core CLI: context, index, check | - | `done` | `review` | - | T-019, T-020, T-021 | T-001 | T-003, T-006, T-011 | T-004, T-005, T-007, T-008, T-025, T-029 |
| [T-007](T-007-define-the-project-scope-goals-and-requirements.md) | Define the project scope, goals and requirements | - | `done` | `review` | - | - | - | T-008 | T-002, T-004, T-005, T-022 |
| [T-008](T-008-write-the-backend-neutral-method-document.md) | Write the backend-neutral method document | - | `done` | `review` | - | T-014, T-015, T-016, T-017 | T-007 | T-003, T-006, T-009 | T-002, T-003, T-013 |
| [T-009](T-009-define-the-backend-binding-contract.md) | Define the backend binding contract and write the local-Markdown binding | - | `done` | `review` | - | - | T-008 | T-005, T-006, T-010 | T-005, T-010, T-012, T-025 |
| [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) | Decide whether soft edges are symmetric | - | `done` | `review` | - | - | - | - | T-001, T-009 |
| [T-013](T-013-quarantine-local-only-information-behind-gitignore.md) | Quarantine local-only information behind .gitignore | - | `done` | `review` | - | - | - | - | T-006, T-008, T-011, T-018, T-033, T-034 |
| [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) | Stop stating each phase exit criterion twice | - | `done` | `review` | T-008 | - | - | - | T-015 |
| [T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) | Bring the method spine under the always-load threshold | - | `done` | `review` | T-008 | - | - | - | T-014, T-028 |
| [T-016](T-016-remove-the-id-format-placeholders-from-the-method.md) | Remove the id-format placeholders from the method | - | `done` | `review` | T-008 | - | - | - | - |
| [T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) | Settle the overlap between SCOPE requirements and the method rules | - | `done` | `review` | T-008 | - | - | - | T-003, T-027 |
| [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) | Stop the pre-publish fixture tripping its own check | - | `done` | `review` | - | - | - | T-006 | T-013, T-034 |
| [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) | Report a tasks_dir that does not exist at setup | - | `done` | `review` | T-002 | - | - | - | T-003, T-006, T-023, T-024, T-025 |
| [T-022](T-022-filtered-task-listing-for-scripts.md) | Filtered task listing for scripts | - | `done` | `review` | - | - | - | - | T-003, T-007, T-021, T-029, T-031, T-032 |

<!-- taskmd:end -->
