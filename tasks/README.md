# Task index — taskmd

Generated from each task's front-matter. **Do not hand-edit** between the markers below.

```
./plugin/taskmd.sh index          # regenerate this file
./plugin/taskmd.sh context T-001  # everything needed to start a task
./plugin/taskmd.sh check          # validate
```

Working method: [`../CLAUDE.md`](../CLAUDE.md). Scope and requirements:
[`../docs/SCOPE.md`](../docs/SCOPE.md). Problem evidence: [`../docs/BRIEF.md`](../docs/BRIEF.md).

<!-- taskmd:index - generated, do not edit by hand -->

## Active

| ID | Title | Status | Phase | Parent | Children | Blocked By | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) | Align with the handoff tracker-binding contract | `specified` | `specify` | - | - | T-009 | - | T-002, T-007, T-009, T-033 |
| [T-006](T-006-package-document-and-publish.md) | Package, document and publish | `in_progress` | `implement` | - | - | T-002, T-003, T-004, T-008, T-009, T-010, T-011, T-018, T-079, T-083 | T-037 | T-013, T-019, T-020, T-023, T-026, T-034, T-049, T-050, T-052, T-053, T-054, T-059, T-064, T-067, T-072 |
| [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) | Confirm byte-identical output on macOS and Linux | `specified` | `specify` | T-002 | - | - | - | T-006, T-023, T-030 |
| [T-021](T-021-settle-what-the-context-closing-line-may-say.md) | Settle what the context closing line may say | `specified` | `specify` | T-002 | - | - | - | T-003, T-022 |
| [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) | Stop config errors printing an absolute install path | `specified` | `specify` | - | - | - | - | T-006, T-019, T-020, T-024, T-030, T-066 |
| [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) | Say so when tasks_dir names something that is not a folder | `proposed` | `specify` | - | - | - | - | T-019, T-023, T-078 |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | Let check notice a stale generated index | `specified` | `specify` | - | - | - | - | T-002, T-009, T-011, T-019, T-026, T-039 |
| [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) | Audit the whole project before the remaining build | `review` | `review` | - | T-027, T-028, T-029, T-030, T-031, T-032, T-033, T-034 | - | - | T-003, T-006, T-010, T-025, T-036, T-059 |
| [T-029](T-029-reject-unknown-arguments-on-every-command.md) | Reject unknown arguments on every command | `specified` | `specify` | T-026 | - | - | - | T-002, T-022, T-055 |
| [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) | Settle the schema module's own entry point | `specified` | `specify` | T-026 | - | - | - | T-020, T-023, T-065, T-066 |
| [T-031](T-031-give-the-list-rationale-one-home.md) | Give the list rationale one home | `specified` | `specify` | T-026 | - | - | - | T-022, T-027 |
| [T-032](T-032-repair-the-audit-template-and-validate-templates.md) | Repair the audit template, and validate templates at all | `specified` | `specify` | T-026 | - | - | - | T-003, T-022, T-036, T-060, T-076 |
| [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) | Resolve the F1 reference inside this repository | `proposed` | `specify` | T-026 | - | - | - | T-005, T-013 |
| [T-035](T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) | Warn that a fabricated specimen must not cross a shell | `proposed` | `specify` | - | - | - | - | T-013, T-018, T-034, T-058 |
| [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md) | Say where a plan is revised, and that reviewing one is not an audit | `specified` | `specify` | - | - | - | - | T-026, T-032 |
| [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) | Move the conduct rules that bind before task work into tier 1 | `specified` | `specify` | - | - | T-003 | - | T-015, T-028, T-059, T-063 |
| [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) | Say what a tasks_dir of dot means | `specified` | `specify` | - | - | - | - | T-019, T-024, T-069 |
| [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md) | Let id_width say that the backend allocates the ids | `proposed` | `specify` | T-004 | - | - | - | T-010, T-075 |

## Closed

| ID | Title | Status | Phase | Parent | Children | Blocked By | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) | Decide how the front-matter schema is configured | `done` | `review` | - | - | - | T-002, T-004 | T-012, T-051, T-065, T-070 |
| [T-002](T-002-implement-the-core-cli-context-index-check.md) | Implement the core CLI: context, index, check | `done` | `review` | - | T-019, T-020, T-021 | T-001 | T-003, T-006, T-011 | T-004, T-005, T-007, T-008, T-025, T-029 |
| [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) | Write the skill that teaches the agent to use the CLI | `done` | `review` | - | T-050 | T-002, T-008 | T-006, T-047 | T-008, T-017, T-019, T-021, T-022, T-026, T-028, T-032, T-048, T-051, T-052, T-053, T-054, T-074 |
| [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) | Settle the id scheme and the claimed scale ceiling | `done` | `review` | - | T-082 | T-001 | T-006 | T-002, T-007, T-010, T-043, T-059, T-062, T-075 |
| [T-007](T-007-define-the-project-scope-goals-and-requirements.md) | Define the project scope, goals and requirements | `done` | `review` | - | - | - | T-008 | T-002, T-004, T-005, T-022 |
| [T-008](T-008-write-the-backend-neutral-method-document.md) | Write the backend-neutral method document | `done` | `review` | - | T-014, T-015, T-016, T-017 | T-007 | T-003, T-006, T-009 | T-002, T-003, T-013 |
| [T-009](T-009-define-the-backend-binding-contract.md) | Define the backend binding contract and write the local-Markdown binding | `done` | `review` | - | - | T-008 | T-005, T-006, T-010 | T-005, T-010, T-012, T-025, T-038, T-040, T-043, T-074 |
| [T-010](T-010-write-the-github-issues-binding.md) | Write the GitHub Issues binding | `done` | `review` | - | - | T-009 | T-006 | T-004, T-009, T-026, T-037, T-038, T-039, T-040, T-041, T-042, T-043, T-044, T-082 |
| [T-011](T-011-runtime-discovery-and-project-hook-commands.md) | Runtime auto-discovery and project hook commands | `done` | `review` | - | T-049 | T-002 | T-006 | T-013, T-025, T-056, T-057, T-066, T-069 |
| [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) | Decide whether soft edges are symmetric | `done` | `review` | - | - | - | - | T-001, T-009 |
| [T-013](T-013-quarantine-local-only-information-behind-gitignore.md) | Quarantine local-only information behind .gitignore | `done` | `review` | - | - | - | - | T-006, T-008, T-011, T-018, T-033, T-034, T-035, T-073 |
| [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) | Stop stating each phase exit criterion twice | `done` | `review` | T-008 | - | - | - | T-015 |
| [T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) | Bring the method spine under the always-load threshold | `done` | `review` | T-008 | - | - | - | T-014, T-028, T-047 |
| [T-016](T-016-remove-the-id-format-placeholders-from-the-method.md) | Remove the id-format placeholders from the method | `done` | `review` | T-008 | - | - | - | - |
| [T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) | Settle the overlap between SCOPE requirements and the method rules | `done` | `review` | T-008 | - | - | - | T-003, T-027, T-045 |
| [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) | Stop the pre-publish fixture tripping its own check | `done` | `review` | - | - | - | T-006 | T-013, T-034, T-035, T-058, T-080 |
| [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) | Report a tasks_dir that does not exist at setup | `done` | `review` | T-002 | - | - | - | T-003, T-006, T-023, T-024, T-025, T-078 |
| [T-022](T-022-filtered-task-listing-for-scripts.md) | Filtered task listing for scripts | `done` | `review` | - | - | - | - | T-003, T-007, T-021, T-029, T-031, T-032, T-070, T-071, T-073 |
| [T-027](T-027-give-the-design-rule-one-home.md) | Give the design rule one home | `done` | `review` | T-026 | - | - | T-028 | T-017, T-031, T-045, T-046 |
| [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) | Budget the whole always-loaded context, not one file | `done` | `review` | T-026 | - | T-027 | - | T-003, T-015, T-040, T-046, T-047, T-048, T-063 |
| [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) | Let the pre-publish check see files not yet tracked | `done` | `review` | T-026 | - | - | - | T-006, T-013, T-018, T-035, T-058, T-080 |
| [T-037](T-037-delete-the-throwaway-proof-repository.md) | Delete the throwaway repository the GitHub binding was proven on | `done` | `review` | - | - | T-006 | - | T-010, T-041, T-077 |
| [T-038](T-038-reconcile-bindings-worked-example-with-the-real-binding.md) | Reconcile BINDING section 5's worked example with the binding it predicted | `done` | `review` | - | - | - | - | T-009, T-010 |
| [T-039](T-039-let-a-plan-name-a-deliverable-that-does-not-exist-yet.md) | Let a plan name a deliverable that does not exist yet | `done` | `review` | - | - | - | - | T-010, T-025 |
| [T-040](T-040-make-the-thirty-second-assumptions-check-real.md) | Make the thirty-second assumptions check real, or change the number | `done` | `review` | - | - | - | - | T-009, T-010, T-028, T-043 |
| [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) | Prove the GitHub binding's body-rewrite rule by making it fail | `done` | `review` | - | - | - | - | T-010, T-037, T-042 |
| [T-042](T-042-make-the-github-bindings-update-preserve-what-it-did-not-touch.md) | Make the GitHub binding's update preserve what it did not touch | `done` | `review` | - | - | - | - | T-010, T-041, T-044 |
| [T-043](T-043-make-every-assumption-a-claim-about-the-adopting-project.md) | Make every assumption a claim about the adopting project | `done` | `review` | - | - | - | - | T-004, T-009, T-010, T-040 |
| [T-044](T-044-state-the-gh-version-the-github-binding-requires.md) | State the gh version the GitHub binding requires | `done` | `review` | - | - | - | - | T-010, T-042 |
| [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) | Decide whether SCOPE §2 principles may state the rule they name | `done` | `review` | - | - | - | - | T-017, T-027 |
| [T-046](T-046-reconcile-the-done-condition-claude-md-restates.md) | Reconcile the done-condition CLAUDE.md restates from the method | `done` | `review` | - | - | - | - | T-027, T-028 |
| [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md) | Say what "always-loaded" means in R-21, before the skill is built against it | `done` | `review` | - | - | - | - | T-003, T-028 |
| [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) | Demonstrate a clone running on a second platform | `done` | `review` | T-011 | T-057, T-058 | - | - | T-006, T-054, T-056, T-057, T-058, T-061 |
| [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) | Measure the skill's tiers on a session that was handed it | `done` | `review` | T-003 | - | - | - | T-006, T-052, T-053 |
| [T-051](T-051-say-where-a-project-s-task-template-lives.md) | Say where a project's task template lives | `done` | `review` | - | - | - | - | T-001, T-003, T-060, T-076 |
| [T-052](T-052-decide-what-of-claude-a-published-clone-carries.md) | Decide what of .claude a published clone carries, and ignore the rest | `done` | `review` | - | - | - | - | T-003, T-006, T-050, T-053, T-067 |
| [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) | Decide the plugin's boundary, and what its skill may point at | `done` | `review` | - | - | - | - | T-003, T-006, T-050, T-052, T-054, T-059, T-064, T-067, T-072, T-083 |
| [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) | Give an adopter a way to run the commands the skill names | `done` | `review` | - | T-055, T-056 | - | - | T-003, T-006, T-049, T-053, T-055, T-056, T-067, T-068, T-083 |
| [T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) | Settle what the tool calls itself when it prints its own usage | `done` | `review` | T-054 | - | - | - | T-029, T-054, T-071 |
| [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md) | Make the shell launcher executable in a Unix clone | `done` | `review` | T-054 | - | - | - | T-011, T-049, T-054, T-061 |
| [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) | Let the hook tests name an interpreter that exists on the platform | `done` | `review` | T-049 | - | - | - | T-011, T-049 |
| [T-058](T-058-say-that-a-four-part-version-trips-the-leak-check.md) | Say that a four-part version number trips the leak check | `done` | `review` | T-049 | - | - | - | T-018, T-034, T-035, T-049, T-080 |
| [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) | Audit the whole project after the plugin restructure | `done` | `review` | - | T-060, T-061, T-062, T-063, T-064, T-065, T-066, T-067, T-068, T-069, T-070, T-071, T-072, T-073, T-074, T-075 | - | - | T-004, T-006, T-026, T-047, T-053 |
| [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) | Point the task templates at paths that exist | `done` | `review` | T-059 | - | - | - | T-032, T-051, T-076 |
| [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) | Stop an inherited PYTHONPATH breaking the shell launcher | `done` | `review` | T-059 | - | - | - | T-049, T-056, T-068 |
| [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) | Report two tasks claiming one id instead of dropping one | `done` | `review` | T-059 | - | - | - | T-004, T-075 |
| [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) | Measure the tier-1 member the rule declares | `done` | `review` | T-059 | - | - | - | T-028, T-047 |
| [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) | Stop the plugin citing documents it does not ship | `done` | `review` | T-059 | - | - | - | T-006, T-053, T-083 |
| [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) | Say what happens to a field the schema does not name | `done` | `review` | T-059 | - | - | - | T-001, T-030 |
| [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) | Reconcile two open tasks with the fix that already landed | `done` | `review` | T-059 | - | - | - | T-011, T-023, T-030 |
| [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) | Prove the install route an adopter actually takes | `done` | `review` | T-059 | - | - | - | T-006, T-052, T-053, T-054, T-077 |
| [T-068](T-068-cover-the-entry-point-an-adopter-runs.md) | Cover the entry point an adopter runs | `done` | `review` | T-059 | - | - | - | T-054, T-061 |
| [T-069](T-069-skip-a-nested-project-at-any-depth.md) | Skip a nested project at any depth, not below the first | `done` | `review` | T-059 | - | - | - | T-011, T-078 |
| [T-070](T-070-decide-whether-an-unused-field-column-is-shown.md) | Decide whether an unused field column is shown at all | `done` | `review` | T-059 | - | - | - | T-001, T-022 |
| [T-071](T-071-let-the-usage-test-assert-every-command-there-is.md) | Let the usage test assert every command there is | `done` | `review` | T-059 | - | - | - | T-022, T-055 |
| [T-072](T-072-give-the-description-and-version-one-home-each.md) | Give the plugin's description and version one home each | `done` | `review` | T-059 | - | - | - | T-006, T-053 |
| [T-073](T-073-correct-the-command-surface-local-context-states.md) | Correct the command surface local context still states | `done` | `review` | T-059 | - | - | - | T-013, T-022 |
| [T-074](T-074-let-the-skill-point-where-it-currently-restates.md) | Let the skill point where it currently restates | `done` | `review` | T-059 | - | - | - | T-003, T-009 |
| [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) | Enforce id width when a task file is read | `done` | `review` | T-059 | - | - | - | T-004, T-062, T-082 |
| [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) | Decide what a template's links resolve against | `done` | `review` | - | - | - | - | T-032, T-051, T-060 |
| [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) | Delete the rehearsal repository T-067 installed from | `done` | `review` | - | - | - | - | T-037, T-067 |
| [T-079](T-079-humanize-the-human-facing-documents-before-publishing.md) | Humanize the human-facing documents before publishing | `done` | `review` | - | - | - | T-006 | T-081 |
| [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) | Stop the pre-publish check reporting its own fixture from a subdirectory | `done` | `review` | - | - | - | - | T-018, T-034, T-058, T-081 |
| [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md) | Gate every deployment on the humanizer pass, not just the next one | `done` | `review` | - | - | - | - | T-079, T-080 |
| [T-083](T-083-make-the-skill-directory-self-contained.md) | Make the skill directory self-contained | `done` | `review` | - | - | - | T-006 | T-053, T-054, T-064 |

<!-- taskmd:end -->
