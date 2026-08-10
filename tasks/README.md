# Task index — taskmd

Generated from each task's front-matter. **Do not hand-edit** between the markers below.

```
./plugin/bin/taskmd index          # regenerate this file
```

The other commands, and what the tool is: [`../README.md`](../README.md). Working method:
[`../CLAUDE.md`](../CLAUDE.md). Scope and requirements: [`../docs/SCOPE.md`](../docs/SCOPE.md).
Problem evidence: [`../docs/BRIEF.md`](../docs/BRIEF.md).

## Releases

What each one is for. **Which tasks are in it is not written here** — that is each task's
`work_package`, and the **Work Package** column below is generated from it. Read a release's
membership with the tool rather than off this page:

```
./plugin/bin/taskmd list --work_package v0.2 --open
```

**v0.1 — published, 2026-08-09.** The four commands, the method document, both bindings, the skill,
the plugin and the README, at `github.com/uchimata2/taskmd`. Its content is every task that was
closed when it shipped.

**Grouped by size and by what blocks what**, on the maintainer's rule of 2026-08-10: v0.2 takes all
dependencies plus every minor-to-moderate correction, v0.3 the bigger work and the new capabilities.
That replaced grouping by theme, which is what the two headlines used to be — the change and what it
cost are in [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md).

**v0.2 — the one dependency chain, and every small correction.** **Done when every task grouped here
is closed.** One criterion, not a list: a list of outcomes here would be a second copy of the
membership the *Work Package* column already carries, and that copy is exactly what the previous
clause set turned out to be — widened twice rather than tasks being moved, and still leaving eleven
open tasks it did not require. The chain is worth naming because it is the only one: **the audit
umbrella closes because all of its findings are resolved** — its open children, in the table below.
Nothing else here waits on anything.

**v0.3 — the bigger work, and the capabilities that are not corrections.** Few enough that each is
worth naming by its outcome. Done when byte-identical output is demonstrated on
macOS and Linux, the published plugin has been installed on a machine that never held it, taskmd
works as a tracker binding for the handoff skill, what `check` does with a section reference is
settled, and a project can move its backlog from local files to GitHub Issues — the one direction
[`../docs/SCOPE.md`](../docs/SCOPE.md) non-goal 8 carves out, and the largest single piece of work
here by some way.

**The two state "done" differently on purpose.** v0.3 has a handful of outcomes worth naming; v0.2
holds everything else, whose only common property is being small, and enumerating those would rebuild
the drift the re-grouping removed. The trade is real and worth stating: grouping by size cannot claim anything
about the product, so v0.2 no longer asserts that the tool holds up elsewhere, and v0.3 no longer
asserts that the method's documents settle. Both claims were true of the sets that carried them and
are not exit criteria any more.

Neither is a version until the maintainer tags one. A milestone here is what the work is grouped
into, not a promise about a date.

<!-- taskmd:index - generated, do not edit by hand -->

## Active

| ID | Title | Work Package | Status | Phase | Parent | Children | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) | Align with the handoff tracker-binding contract | `v0.3` | `specified` | `specify` | - | - | - | T-002, T-007, T-009, T-033, T-105 |
| [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) | Confirm byte-identical output on macOS and Linux | `v0.3` | `specified` | `specify` | T-002 | - | - | T-006, T-023, T-030, T-085 |
| [T-021](T-021-settle-what-the-context-closing-line-may-say.md) | Settle what the context closing line may say | `v0.2` | `specified` | `specify` | T-002 | - | - | T-003, T-022 |
| [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) | Stop config errors printing an absolute install path | `v0.2` | `specified` | `specify` | - | - | - | T-006, T-019, T-020, T-024, T-030, T-066, T-100, T-106 |
| [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) | Say so when tasks_dir names something that is not a folder | `v0.2` | `proposed` | `specify` | - | - | - | T-019, T-023, T-078 |
| [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) | Audit the whole project before the remaining build | `v0.2` | `review` | `review` | - | T-027, T-028, T-029, T-030, T-031, T-032, T-033, T-034 | - | T-003, T-006, T-010, T-025, T-036, T-059, T-086, T-088, T-110 |
| [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) | Settle the schema module's own entry point | `v0.2` | `specified` | `specify` | T-026 | - | - | T-020, T-023, T-065, T-066 |
| [T-031](T-031-give-the-list-rationale-one-home.md) | Give the list rationale one home | `v0.2` | `specified` | `specify` | T-026 | - | - | T-022, T-027, T-102 |
| [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) | Resolve the F1 reference inside this repository | `v0.2` | `proposed` | `specify` | T-026 | - | - | T-005, T-013 |
| [T-035](T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) | Warn that a fabricated specimen must not cross a shell | `v0.2` | `proposed` | `specify` | - | - | - | T-013, T-018, T-034, T-058 |
| [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md) | Say where a plan is revised, and that reviewing one is not an audit | `v0.2` | `specified` | `specify` | - | - | - | T-026, T-032, T-105 |
| [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) | Say what a tasks_dir of dot means | `v0.2` | `specified` | `specify` | - | - | - | T-019, T-024, T-069 |
| [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md) | Let id_width say that the backend allocates the ids | `v0.2` | `proposed` | `specify` | T-004 | - | - | T-010, T-075, T-108 |
| [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) | Install the published plugin on a machine that has never seen it | `v0.3` | `proposed` | `specify` | T-006 | - | - | T-020, T-049, T-067, T-099 |
| [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) | Decide what a cancelled task's declared outputs assert | `v0.2` | `proposed` | `specify` | T-089 | - | - | T-002, T-032, T-103, T-109 |
| [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) | Decide whether check resolves a section reference | `v0.3` | `proposed` | `specify` | - | - | - | T-092, T-095, T-109 |
| [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md) | Decide whether a published document may point at a file no clone receives | `v0.2` | `proposed` | `specify` | - | - | - | T-013, T-034, T-091, T-092, T-094, T-109 |
| [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) | Support a project moving its tasks from local files to GitHub Issues | `v0.3` | `proposed` | `specify` | - | - | - | T-004, T-009, T-010, T-041, T-082 |
| [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md) | Decide whether a task that settles a question must be typed decision | `v0.2` | `proposed` | `specify` | - | - | - | T-088, T-090, T-093, T-097, T-098, T-104, T-110 |
| [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) | Stop check resolving a link that is displayed rather than navigable | `v0.2` | `proposed` | `specify` | - | - | - | T-091, T-092, T-095, T-114 |
| [T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md) | Name an unknown filter before complaining it has no value | `v0.2` | `proposed` | `specify` | - | - | - | T-022, T-029 |
| [T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md) | Make the launcher tests say which bash they found | `v0.2` | `proposed` | `specify` | - | - | - | T-091, T-112 |
| [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md) | Give the tier 1 budget something that enforces it | `v0.2` | `proposed` | `specify` | - | - | - | T-028, T-047, T-063 |

## Closed

| ID | Title | Work Package | Status | Phase | Parent | Children | Blocks | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) | Decide how the front-matter schema is configured | `v0.1` | `done` | `review` | - | - | - | T-012, T-051, T-065, T-070, T-088, T-100, T-106 |
| [T-002](T-002-implement-the-core-cli-context-index-check.md) | Implement the core CLI: context, index, check | `v0.1` | `done` | `review` | - | T-019, T-020, T-021 | - | T-004, T-005, T-007, T-008, T-025, T-029, T-089, T-090, T-098 |
| [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) | Write the skill that teaches the agent to use the CLI | `v0.1` | `done` | `review` | - | T-050 | - | T-008, T-017, T-019, T-021, T-022, T-026, T-028, T-032, T-048, T-051, T-052, T-053, T-054, T-074 |
| [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) | Settle the id scheme and the claimed scale ceiling | `v0.1` | `done` | `review` | - | T-082 | - | T-002, T-007, T-010, T-043, T-059, T-062, T-075, T-108 |
| [T-006](T-006-package-document-and-publish.md) | Package, document and publish | `v0.1` | `done` | `review` | - | T-085 | - | T-013, T-019, T-020, T-023, T-026, T-034, T-049, T-050, T-052, T-053, T-054, T-059, T-064, T-067, T-072, T-084, T-086 |
| [T-007](T-007-define-the-project-scope-goals-and-requirements.md) | Define the project scope, goals and requirements | `v0.1` | `done` | `review` | - | - | - | T-002, T-004, T-005, T-022 |
| [T-008](T-008-write-the-backend-neutral-method-document.md) | Write the backend-neutral method document | `v0.1` | `done` | `review` | - | T-014, T-015, T-016, T-017 | - | T-002, T-003, T-013, T-104 |
| [T-009](T-009-define-the-backend-binding-contract.md) | Define the backend binding contract and write the local-Markdown binding | `v0.1` | `done` | `review` | - | - | T-005 | T-005, T-010, T-012, T-025, T-038, T-040, T-043, T-074, T-108 |
| [T-010](T-010-write-the-github-issues-binding.md) | Write the GitHub Issues binding | `v0.1` | `done` | `review` | - | - | - | T-004, T-009, T-026, T-037, T-038, T-039, T-040, T-041, T-042, T-043, T-044, T-082, T-108 |
| [T-011](T-011-runtime-discovery-and-project-hook-commands.md) | Runtime auto-discovery and project hook commands | `v0.1` | `done` | `review` | - | T-049 | - | T-013, T-025, T-056, T-057, T-066, T-069, T-106 |
| [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) | Decide whether soft edges are symmetric | `v0.1` | `done` | `review` | - | - | - | T-001, T-009 |
| [T-013](T-013-quarantine-local-only-information-behind-gitignore.md) | Quarantine local-only information behind .gitignore | `v0.1` | `done` | `review` | - | - | - | T-006, T-008, T-011, T-018, T-033, T-034, T-035, T-073, T-094, T-097 |
| [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) | Stop stating each phase exit criterion twice | `v0.1` | `done` | `review` | T-008 | - | - | T-015 |
| [T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) | Bring the method spine under the always-load threshold | `v0.1` | `done` | `review` | T-008 | - | - | T-014, T-028, T-047 |
| [T-016](T-016-remove-the-id-format-placeholders-from-the-method.md) | Remove the id-format placeholders from the method | `v0.1` | `done` | `review` | T-008 | - | - | - |
| [T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) | Settle the overlap between SCOPE requirements and the method rules | `v0.1` | `done` | `review` | T-008 | - | - | T-003, T-027, T-045 |
| [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) | Stop the pre-publish fixture tripping its own check | `v0.1` | `done` | `review` | - | - | - | T-013, T-034, T-035, T-058, T-080 |
| [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) | Report a tasks_dir that does not exist at setup | `v0.1` | `done` | `review` | T-002 | - | - | T-003, T-006, T-023, T-024, T-025, T-078 |
| [T-022](T-022-filtered-task-listing-for-scripts.md) | Filtered task listing for scripts | `v0.1` | `done` | `review` | - | - | - | T-003, T-007, T-021, T-029, T-031, T-032, T-070, T-071, T-073, T-086, T-087, T-102, T-113 |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | Let check notice a stale generated index | `v0.2` | `done` | `review` | - | - | - | T-002, T-009, T-011, T-019, T-026, T-039, T-084, T-089, T-095, T-096 |
| [T-027](T-027-give-the-design-rule-one-home.md) | Give the design rule one home | `v0.1` | `done` | `review` | T-026 | - | - | T-017, T-031, T-045, T-046 |
| [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) | Budget the whole always-loaded context, not one file | `v0.1` | `done` | `review` | T-026 | - | - | T-003, T-015, T-040, T-046, T-047, T-048, T-063, T-115 |
| [T-029](T-029-reject-unknown-arguments-on-every-command.md) | Reject unknown arguments on every command | `v0.2` | `done` | `review` | T-026 | - | - | T-002, T-022, T-055, T-087, T-113 |
| [T-032](T-032-repair-the-audit-template-and-validate-templates.md) | Repair the audit template, and validate templates at all | `v0.2` | `done` | `review` | T-026 | - | - | T-003, T-022, T-036, T-060, T-076, T-088, T-089, T-090, T-091, T-101 |
| [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) | Let the pre-publish check see files not yet tracked | `v0.1` | `done` | `review` | T-026 | - | - | T-006, T-013, T-018, T-035, T-058, T-080, T-092, T-094, T-095, T-097, T-098 |
| [T-037](T-037-delete-the-throwaway-proof-repository.md) | Delete the throwaway repository the GitHub binding was proven on | `v0.1` | `done` | `review` | - | - | - | T-010, T-041, T-077 |
| [T-038](T-038-reconcile-bindings-worked-example-with-the-real-binding.md) | Reconcile BINDING section 5's worked example with the binding it predicted | `v0.1` | `done` | `review` | - | - | - | T-009, T-010 |
| [T-039](T-039-let-a-plan-name-a-deliverable-that-does-not-exist-yet.md) | Let a plan name a deliverable that does not exist yet | `v0.1` | `done` | `review` | - | - | - | T-010, T-025 |
| [T-040](T-040-make-the-thirty-second-assumptions-check-real.md) | Make the thirty-second assumptions check real, or change the number | `v0.1` | `done` | `review` | - | - | - | T-009, T-010, T-028, T-043 |
| [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) | Prove the GitHub binding's body-rewrite rule by making it fail | `v0.1` | `done` | `review` | - | - | - | T-010, T-037, T-042, T-108 |
| [T-042](T-042-make-the-github-bindings-update-preserve-what-it-did-not-touch.md) | Make the GitHub binding's update preserve what it did not touch | `v0.1` | `done` | `review` | - | - | - | T-010, T-041, T-044 |
| [T-043](T-043-make-every-assumption-a-claim-about-the-adopting-project.md) | Make every assumption a claim about the adopting project | `v0.1` | `done` | `review` | - | - | - | T-004, T-009, T-010, T-040 |
| [T-044](T-044-state-the-gh-version-the-github-binding-requires.md) | State the gh version the GitHub binding requires | `v0.1` | `done` | `review` | - | - | - | T-010, T-042 |
| [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) | Decide whether SCOPE §2 principles may state the rule they name | `v0.1` | `done` | `review` | - | - | - | T-017, T-027 |
| [T-046](T-046-reconcile-the-done-condition-claude-md-restates.md) | Reconcile the done-condition CLAUDE.md restates from the method | `v0.1` | `done` | `review` | - | - | - | T-027, T-028 |
| [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) | Move the conduct rules that bind before task work into tier 1 | `v0.2` | `done` | `review` | - | - | - | T-015, T-028, T-059, T-063, T-105, T-115 |
| [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md) | Say what "always-loaded" means in R-21, before the skill is built against it | `v0.1` | `done` | `review` | - | - | - | T-003, T-028 |
| [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) | Demonstrate a clone running on a second platform | `v0.1` | `done` | `review` | T-011 | T-057, T-058 | - | T-006, T-054, T-056, T-057, T-058, T-061, T-085 |
| [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) | Measure the skill's tiers on a session that was handed it | `v0.1` | `done` | `review` | T-003 | - | - | T-006, T-052, T-053 |
| [T-051](T-051-say-where-a-project-s-task-template-lives.md) | Say where a project's task template lives | `v0.1` | `done` | `review` | - | - | - | T-001, T-003, T-060, T-076, T-091, T-101 |
| [T-052](T-052-decide-what-of-claude-a-published-clone-carries.md) | Decide what of .claude a published clone carries, and ignore the rest | `v0.1` | `done` | `review` | - | - | - | T-003, T-006, T-050, T-053, T-067 |
| [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) | Decide the plugin's boundary, and what its skill may point at | `v0.1` | `done` | `review` | - | - | - | T-003, T-006, T-050, T-052, T-054, T-059, T-064, T-067, T-072, T-083, T-103 |
| [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) | Give an adopter a way to run the commands the skill names | `v0.1` | `done` | `review` | - | T-055, T-056 | - | T-003, T-006, T-049, T-053, T-055, T-056, T-067, T-068, T-083, T-099 |
| [T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) | Settle what the tool calls itself when it prints its own usage | `v0.1` | `done` | `review` | T-054 | - | - | T-029, T-054, T-071, T-099 |
| [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md) | Make the shell launcher executable in a Unix clone | `v0.1` | `done` | `review` | T-054 | - | - | T-011, T-049, T-054, T-061 |
| [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) | Let the hook tests name an interpreter that exists on the platform | `v0.1` | `done` | `review` | T-049 | - | - | T-011, T-049 |
| [T-058](T-058-say-that-a-four-part-version-trips-the-leak-check.md) | Say that a four-part version number trips the leak check | `v0.1` | `done` | `review` | T-049 | - | - | T-018, T-034, T-035, T-049, T-080 |
| [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) | Audit the whole project after the plugin restructure | `v0.1` | `done` | `review` | - | T-060, T-061, T-062, T-063, T-064, T-065, T-066, T-067, T-068, T-069, T-070, T-071, T-072, T-073, T-074, T-075 | - | T-004, T-006, T-026, T-047, T-053 |
| [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) | Point the task templates at paths that exist | `v0.1` | `done` | `review` | T-059 | - | - | T-032, T-051, T-076, T-091 |
| [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) | Stop an inherited PYTHONPATH breaking the shell launcher | `v0.1` | `done` | `review` | T-059 | - | - | T-049, T-056, T-068 |
| [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) | Report two tasks claiming one id instead of dropping one | `v0.1` | `done` | `review` | T-059 | - | - | T-004, T-075, T-107 |
| [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) | Measure the tier-1 member the rule declares | `v0.1` | `done` | `review` | T-059 | - | - | T-028, T-047, T-105, T-115 |
| [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) | Stop the plugin citing documents it does not ship | `v0.1` | `done` | `review` | T-059 | - | - | T-006, T-053, T-083 |
| [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) | Say what happens to a field the schema does not name | `v0.1` | `done` | `review` | T-059 | - | - | T-001, T-030 |
| [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) | Reconcile two open tasks with the fix that already landed | `v0.1` | `done` | `review` | T-059 | - | - | T-011, T-023, T-030 |
| [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) | Prove the install route an adopter actually takes | `v0.1` | `done` | `review` | T-059 | - | - | T-006, T-052, T-053, T-054, T-077, T-085, T-099 |
| [T-068](T-068-cover-the-entry-point-an-adopter-runs.md) | Cover the entry point an adopter runs | `v0.1` | `done` | `review` | T-059 | - | - | T-054, T-061 |
| [T-069](T-069-skip-a-nested-project-at-any-depth.md) | Skip a nested project at any depth, not below the first | `v0.1` | `done` | `review` | T-059 | - | - | T-011, T-078, T-107 |
| [T-070](T-070-decide-whether-an-unused-field-column-is-shown.md) | Decide whether an unused field column is shown at all | `v0.1` | `done` | `review` | T-059 | - | - | T-001, T-022, T-102 |
| [T-071](T-071-let-the-usage-test-assert-every-command-there-is.md) | Let the usage test assert every command there is | `v0.1` | `done` | `review` | T-059 | - | - | T-022, T-055 |
| [T-072](T-072-give-the-description-and-version-one-home-each.md) | Give the plugin's description and version one home each | `v0.1` | `done` | `review` | T-059 | - | - | T-006, T-053 |
| [T-073](T-073-correct-the-command-surface-local-context-states.md) | Correct the command surface local context still states | `v0.1` | `done` | `review` | T-059 | - | - | T-013, T-022 |
| [T-074](T-074-let-the-skill-point-where-it-currently-restates.md) | Let the skill point where it currently restates | `v0.1` | `done` | `review` | T-059 | - | - | T-003, T-009 |
| [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) | Enforce id width when a task file is read | `v0.1` | `done` | `review` | T-059 | - | - | T-004, T-062, T-082, T-107 |
| [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) | Decide what a template's links resolve against | `v0.1` | `done` | `review` | - | - | - | T-032, T-051, T-060, T-091, T-101, T-103, T-104 |
| [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) | Delete the rehearsal repository T-067 installed from | `v0.1` | `done` | `review` | - | - | - | T-037, T-067 |
| [T-079](T-079-humanize-the-human-facing-documents-before-publishing.md) | Humanize the human-facing documents before publishing | `v0.1` | `done` | `review` | - | - | - | T-081 |
| [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) | Stop the pre-publish check reporting its own fixture from a subdirectory | `v0.1` | `done` | `review` | - | - | - | T-018, T-034, T-058, T-081, T-095, T-098 |
| [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md) | Gate every deployment on the humanizer pass, not just the next one | `v0.1` | `done` | `review` | - | - | - | T-079, T-080 |
| [T-083](T-083-make-the-skill-directory-self-contained.md) | Make the skill directory self-contained | `v0.1` | `done` | `review` | - | - | - | T-053, T-054, T-064, T-084, T-099, T-103 |
| [T-084](T-084-correct-the-generated-index-preamble-after-the-move.md) | Correct the generated index preamble after the directory move | `v0.1` | `done` | `review` | - | - | - | T-006, T-025, T-083 |
| [T-086](T-086-group-the-backlog-into-release-milestones.md) | Group the backlog into release milestones | `v0.2` | `done` | `review` | - | - | - | T-006, T-022, T-026, T-087, T-110 |
| [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) | Let list filter on a field the index can show | `v0.2` | `done` | `review` | - | - | - | T-022, T-029, T-086, T-102 |
| [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) | Put audit in the shipped type vocabulary, or stop calling it a type | `v0.2` | `done` | `review` | - | - | - | T-001, T-026, T-032, T-100, T-104, T-109 |
| [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) | Stop check reporting an open task's planned outputs as missing | `v0.2` | `done` | `review` | - | T-090 | - | T-002, T-025, T-032, T-103 |
| [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md) | Make the shipped task template survive being copied into another project | `v0.2` | `done` | `review` | - | - | - | T-032, T-051, T-060, T-076, T-097, T-101, T-112, T-114 |
| [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) | Decide whether a bare path in prose is a reference check must resolve | `v0.2` | `done` | `review` | - | - | - | T-034, T-093, T-094, T-095, T-097, T-103, T-112 |
| [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) | Make check answer the question a fresh clone would ask | `v0.2` | `done` | `review` | - | - | - | T-013, T-034, T-092, T-095, T-097, T-098 |
| [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) | Report what check examined, not only that it passed | `v0.2` | `done` | `review` | - | T-096 | - | T-025, T-034, T-080, T-092, T-093, T-094, T-098, T-100, T-101, T-112 |
| [T-096](T-096-decide-whether-a-narrower-walk-of-a-counted-class-needs-its-own-number.md) | Decide whether a narrower walk of a counted class needs its own number | `v0.2` | `done` | `review` | T-095 | - | - | T-025 |
| [T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) | Decide who checks the links in a document only a successor reads | `v0.2` | `done` | `review` | - | - | - | T-002, T-034, T-080, T-094, T-095, T-109 |
| [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) | Give an adopter a command that runs when the plugin's bin is not on PATH | `v0.2` | `done` | `review` | - | - | - | T-054, T-055, T-067, T-083, T-085 |
| [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) | Report a project config that has drifted from the shipped default | `v0.2` | `done` | `review` | - | - | - | T-001, T-023, T-088, T-095, T-106 |
| [T-101](T-101-report-a-template-the-create-path-cannot-see.md) | Report a template the create path cannot see | `v0.2` | `done` | `review` | - | - | - | T-032, T-051, T-076, T-091, T-095, T-107 |
| [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) | Show which rows list has already worked out are blocked | `v0.2` | `done` | `review` | - | - | - | T-022, T-031, T-070, T-087, T-111 |
| [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) | Say whether a closed task's declared output may be repointed when the file moves | `v0.3` | `done` | `review` | - | - | - | T-053, T-076, T-083, T-089, T-090, T-092, T-104 |
| [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md) | Say whether the method has an opinion on where a decision is recorded | `v0.3` | `done` | `review` | - | - | - | T-008, T-076, T-088, T-103, T-109 |
| [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) | Say where an authorised multi-phase run is recorded | `v0.3` | `done` | `review` | - | - | - | T-005, T-036, T-047, T-063 |
| [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) | Say that the shipped config cannot gain a key without breaking every project that wrote one | `v0.3` | `done` | `review` | - | - | - | T-001, T-011, T-023, T-100 |
| [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) | Say so when a valid task file is parked where nothing reads it | `v0.2` | `done` | `review` | - | - | - | T-062, T-069, T-075, T-101 |
| [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md) | Re-group the open backlog by the maintainer's release rule | `v0.2` | `done` | `review` | - | - | - | T-026, T-086, T-109 |
| [T-111](T-111-stop-the-index-showing-a-closed-task-as-a-live-blocker.md) | Stop the index showing a closed task as a live blocker | `v0.2` | `done` | `review` | - | - | - | T-102 |

<!-- taskmd:end -->
