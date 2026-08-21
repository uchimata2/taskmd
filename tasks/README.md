# Task index — taskmd

Generated from each task's front-matter. **Do not hand-edit** between the markers below.

```
./plugin/bin/taskmd index          # regenerate this file
```

The other commands, and what the tool is: [`../README.md`](../README.md). Working method:
[`../CLAUDE.md`](../CLAUDE.md). Scope and requirements: [`../docs/SCOPE.md`](../docs/SCOPE.md).
Problem evidence: [`../docs/BRIEF.md`](../docs/BRIEF.md).

## Releases

What each one is for. **Which tasks are in it is not written here.** That is each task's
`work_package`, and the **Work Package** column below is generated from it. Read a release's
membership with the tool:

```
./plugin/bin/taskmd list --work_package M5 --open
```

**A milestone label is not a version and cannot be read as one.** `M5` names a group of tasks;
`0.5.0` is what an installed copy compares itself against to decide whether to update. The digit says
which release the work is scheduled into — `M5` ships as `0.5.0`, `M6` as `0.6.0` — and exactly two
closed labels are not that: **`M2` shipped as `0.4.0`**, and `M3`'s four tasks went out inside the
`v0.3.0` batch bump rather than in a release of their own.

Those two sentences replaced a four-row mapping table on 2026-08-12
([T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md)). The table had a
row per label and was therefore a second copy of a fact each task already carried; naming only the
exceptions cannot go stale the way a membership list does. The labels were `v0.1`, `v0.2`, `v0.3`,
`v0.5` and `v0.6` until that date, and they were renamed because each one resolved to a real tag of
the same number that meant something else.

**Quoted instructions in closed task logs keep the label that was in use when they were given.** A
quotation reports the words somebody used, not the set of tasks, so renaming inside one would
misreport what was said.

`v0.2.0` and `v0.3.0` are tagged and are **not** milestones. They are batch version bumps, taken
mid-milestone so that installed projects would receive fixes: `claude plugin update` compares version
strings, so a manifest that never moves serves its old snapshot for ever. `v0.3.0` has no release
notes; what it carried is described in `v0.4.0`'s.

**Grouped by size and by what blocks what**, on the maintainer's rule of 2026-08-10: the near release
takes all dependencies plus every minor-to-moderate correction, the one after it takes the bigger
work and the new capabilities. That replaced grouping by theme. The change and what it cost are in
[T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md).

**M5 — prove what 0.4.0 published, and settle the small questions.** Two checks that the shipped
plugin works where nobody has run it, three decisions nothing waits on, and two corrections.

**M6 — the capabilities.** Moving a backlog from local files to GitHub Issues, which
[`../docs/SCOPE.md`](../docs/SCOPE.md) non-goal 8 carves out and which is the largest single piece of
work in this backlog; taskmd as a tracker binding for the handoff skill; and what `check` does with a
section reference.

**Both are done when every task grouped in them is closed.** The sentences above say what a release
is *for*; they are not its exit criterion. A criterion that lists outcomes is a second copy of the
membership the *Work Package* column already carries, and it goes stale the moment a task joins the
release without joining the list. That is measured rather than feared: the clause set this replaces
left four of nine tasks unaccounted for.

A label says which release the work is scheduled into. It never says the release happened.

<!-- taskmd:index - generated, do not edit by hand -->

## Active

| ID | Title | Work Package | Status | Phase | Parent | Children | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-176](T-176-have-an-uninvolved-reader-test-the-sourced-survivor-bullet.md) | Have an uninvolved reader test the sourced survivor bullet | `M6` | `proposed` | `specify` | T-168 | - | T-166, T-167, T-168, T-199 |
| [T-182](T-182-write-the-next-release-note-to-the-rule-and-say-what-it-caught.md) | Write the next release note to the rule and say what it caught | `M6` | `proposed` | `specify` | T-135 | - | T-125, T-127, T-133 |
| [T-191](T-191-audit-whether-each-check-class-has-a-case-it-must-not-catch.md) | Audit whether each check class has a case it must not catch | `M6` | `review` | `review` | - | T-197, T-198 | T-100, T-150, T-151 |
| [T-198](T-198-show-each-quiet-fixture-is-within-its-own-check-s-reach.md) | Show each quiet fixture is within its own check's reach | `M6` | `review` | `review` | T-191 | T-201, T-202, T-204 | T-150, T-151 |
| [T-199](T-199-have-an-uninvolved-reader-write-a-coverage-declaration-from-the-clause.md) | Have an uninvolved reader write a coverage declaration from the clause | `M6` | `proposed` | `specify` | T-192 | - | T-176 |
| [T-202](T-202-mark-a-fixture-s-quiet-cases-so-a-sweep-can-find-them.md) | Mark a fixture's quiet cases so a sweep can find them | `M6` | `proposed` | `specify` | T-198 | - | T-134, T-151, T-197, T-204 |
| [T-203](T-203-detect-an-issue-whose-state-disagrees-with-its-status-label.md) | Detect an issue whose state disagrees with its status label | `M6` | `proposed` | `specify` | - | - | T-108, T-178, T-193 |
| [T-206](T-206-test-whether-the-description-s-markdown-files-clause-turns-a-session-away.md) | Test whether the description's Markdown-files clause turns a session away | `M6` | `proposed` | `specify` | T-205 | - | T-050, T-175 |
| [T-207](T-207-test-the-platform-claims-this-repository-s-own-second-copies-rest-on.md) | Test the platform claims this repository's own second copies rest on | `M6` | `proposed` | `specify` | - | - | T-072, T-187 |
| [T-208](T-208-decide-where-the-product-wide-deviation-clause-belongs-now-that-it-exists.md) | Decide where the product-wide deviation clause belongs now that it exists | `M6` | `proposed` | `specify` | - | - | T-027, T-045, T-187 |

## Closed

| ID | Title | Work Package | Status | Phase | Parent | Children | Related |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [T-001](T-001-decide-how-the-front-matter-schema-is-configured.md) | Decide how the front-matter schema is configured | `M1` | `done` | `review` | - | - | T-012, T-051, T-065, T-070, T-088, T-100, T-106 |
| [T-002](T-002-implement-the-core-cli-context-index-check.md) | Implement the core CLI: context, index, check | `M1` | `done` | `review` | - | T-019, T-020, T-021 | T-004, T-005, T-007, T-008, T-025, T-029, T-089, T-090, T-098, T-132 |
| [T-003](T-003-write-the-skill-that-teaches-the-agent-to-use-the-cl.md) | Write the skill that teaches the agent to use the CLI | `M1` | `done` | `review` | - | T-050 | T-008, T-017, T-019, T-021, T-022, T-026, T-028, T-032, T-048, T-051, T-052, T-053, T-054, T-074 |
| [T-004](T-004-settle-the-id-scheme-and-the-claimed-scale-ceiling.md) | Settle the id scheme and the claimed scale ceiling | `M1` | `done` | `review` | - | T-082 | T-002, T-007, T-010, T-043, T-059, T-062, T-075, T-108, T-137 |
| [T-005](T-005-align-with-the-handoff-tracker-binding-contract.md) | Align with the handoff tracker-binding contract | `M6` | `done` | `review` | - | T-181 | T-002, T-007, T-009, T-033, T-105 |
| [T-006](T-006-package-document-and-publish.md) | Package, document and publish | `M1` | `done` | `review` | - | T-085 | T-013, T-019, T-020, T-023, T-026, T-034, T-049, T-050, T-052, T-053, T-054, T-059, T-064, T-067, T-072, T-084, T-086, T-125 |
| [T-007](T-007-define-the-project-scope-goals-and-requirements.md) | Define the project scope, goals and requirements | `M1` | `done` | `review` | - | - | T-002, T-004, T-005, T-022 |
| [T-008](T-008-write-the-backend-neutral-method-document.md) | Write the backend-neutral method document | `M1` | `done` | `review` | - | T-014, T-015, T-016, T-017 | T-002, T-003, T-013, T-104 |
| [T-009](T-009-define-the-backend-binding-contract.md) | Define the backend binding contract and write the local-Markdown binding | `M1` | `done` | `review` | - | - | T-005, T-010, T-012, T-025, T-038, T-040, T-043, T-074, T-108, T-192 |
| [T-010](T-010-write-the-github-issues-binding.md) | Write the GitHub Issues binding | `M1` | `done` | `review` | - | - | T-004, T-009, T-026, T-037, T-038, T-039, T-040, T-041, T-042, T-043, T-044, T-082, T-108 |
| [T-011](T-011-runtime-discovery-and-project-hook-commands.md) | Runtime auto-discovery and project hook commands | `M1` | `done` | `review` | - | T-049 | T-013, T-025, T-056, T-057, T-066, T-069, T-106, T-116 |
| [T-012](T-012-decide-whether-soft-edges-are-symmetric.md) | Decide whether soft edges are symmetric | `M1` | `done` | `review` | - | - | T-001, T-009, T-187 |
| [T-013](T-013-quarantine-local-only-information-behind-gitignore.md) | Quarantine local-only information behind .gitignore | `M1` | `done` | `review` | - | - | T-006, T-008, T-011, T-018, T-033, T-034, T-035, T-073, T-094, T-097 |
| [T-014](T-014-stop-stating-each-phase-exit-criterion-twice.md) | Stop stating each phase exit criterion twice | `M1` | `done` | `review` | T-008 | - | T-015 |
| [T-015](T-015-bring-the-method-spine-under-the-always-load-threshold.md) | Bring the method spine under the always-load threshold | `M1` | `done` | `review` | T-008 | - | T-014, T-028, T-047 |
| [T-016](T-016-remove-the-id-format-placeholders-from-the-method.md) | Remove the id-format placeholders from the method | `M1` | `done` | `review` | T-008 | - | - |
| [T-017](T-017-settle-the-overlap-between-scope-requirements-and-the-method.md) | Settle the overlap between SCOPE requirements and the method rules | `M1` | `done` | `review` | T-008 | - | T-003, T-027, T-045 |
| [T-018](T-018-stop-the-pre-publish-fixture-tripping-its-own-check.md) | Stop the pre-publish fixture tripping its own check | `M1` | `done` | `review` | - | - | T-013, T-034, T-035, T-058, T-080 |
| [T-019](T-019-report-a-tasks-dir-that-does-not-exist-at-setup.md) | Report a tasks_dir that does not exist at setup | `M1` | `done` | `review` | T-002 | - | T-003, T-006, T-023, T-024, T-025, T-078 |
| [T-020](T-020-confirm-byte-identical-output-on-macos-and-linux.md) | Confirm byte-identical output on macOS and Linux | `M5` | `done` | `review` | T-002 | T-132 | T-006, T-023, T-030, T-049, T-085, T-132 |
| [T-021](T-021-settle-what-the-context-closing-line-may-say.md) | Settle what the context closing line may say | `M2` | `done` | `review` | T-002 | - | T-003, T-022 |
| [T-022](T-022-filtered-task-listing-for-scripts.md) | Filtered task listing for scripts | `M1` | `done` | `review` | - | - | T-003, T-007, T-021, T-029, T-031, T-032, T-070, T-071, T-073, T-086, T-087, T-102, T-113, T-120, T-132, T-143, T-144, T-179 |
| [T-023](T-023-stop-config-errors-printing-an-absolute-install-path.md) | Stop config errors printing an absolute install path | `M2` | `done` | `review` | - | - | T-006, T-019, T-020, T-024, T-030, T-066, T-100, T-106 |
| [T-024](T-024-say-so-when-tasks-dir-names-something-that-is-not-a-folder.md) | Say so when tasks_dir names something that is not a folder | `M2` | `done` | `review` | - | - | T-019, T-023, T-078 |
| [T-025](T-025-let-check-notice-a-stale-generated-index.md) | Let check notice a stale generated index | `M2` | `done` | `review` | - | - | T-002, T-009, T-011, T-019, T-026, T-039, T-084, T-089, T-095, T-096, T-121, T-130, T-141 |
| [T-026](T-026-audit-the-whole-project-before-the-remaining-build.md) | Audit the whole project before the remaining build | `M2` | `done` | `review` | - | T-027, T-028, T-029, T-030, T-031, T-032, T-033, T-034 | T-003, T-006, T-010, T-025, T-036, T-059, T-086, T-088, T-110, T-118 |
| [T-027](T-027-give-the-design-rule-one-home.md) | Give the design rule one home | `M1` | `done` | `review` | T-026 | - | T-017, T-031, T-045, T-046, T-208 |
| [T-028](T-028-budget-the-whole-always-loaded-context-not-one-file.md) | Budget the whole always-loaded context, not one file | `M1` | `done` | `review` | T-026 | - | T-003, T-015, T-040, T-046, T-047, T-048, T-063, T-115, T-118, T-143, T-154, T-190, T-194 |
| [T-029](T-029-reject-unknown-arguments-on-every-command.md) | Reject unknown arguments on every command | `M2` | `done` | `review` | T-026 | - | T-002, T-022, T-055, T-087, T-113, T-144, T-145 |
| [T-030](T-030-settle-the-schema-module-s-own-entry-point.md) | Settle the schema module's own entry point | `M2` | `done` | `review` | T-026 | - | T-020, T-023, T-065, T-066, T-117, T-134 |
| [T-031](T-031-give-the-list-rationale-one-home.md) | Give the list rationale one home | `M2` | `done` | `review` | T-026 | - | T-022, T-027, T-102, T-117, T-134 |
| [T-032](T-032-repair-the-audit-template-and-validate-templates.md) | Repair the audit template, and validate templates at all | `M2` | `done` | `review` | T-026 | - | T-003, T-022, T-036, T-060, T-076, T-088, T-089, T-090, T-091, T-101, T-150, T-172 |
| [T-033](T-033-resolve-the-f1-reference-inside-this-repository.md) | Resolve the F1 reference inside this repository | `M2` | `done` | `review` | T-026 | - | T-005, T-013 |
| [T-034](T-034-let-the-pre-publish-check-see-files-not-yet-tracked.md) | Let the pre-publish check see files not yet tracked | `M1` | `done` | `review` | T-026 | - | T-006, T-013, T-018, T-035, T-058, T-080, T-092, T-094, T-095, T-097, T-098, T-183, T-186 |
| [T-035](T-035-warn-that-a-fabricated-specimen-must-not-cross-a-shell.md) | Warn that a fabricated specimen must not cross a shell | `M2` | `done` | `review` | - | - | T-013, T-018, T-034, T-047, T-058, T-118 |
| [T-036](T-036-say-where-a-plan-is-revised-and-that-it-is-not-an-audit.md) | Say where a plan is revised, and that reviewing one is not an audit | `M2` | `done` | `review` | - | - | T-026, T-032, T-105 |
| [T-037](T-037-delete-the-throwaway-proof-repository.md) | Delete the throwaway repository the GitHub binding was proven on | `M1` | `done` | `review` | - | - | T-010, T-041, T-077 |
| [T-038](T-038-reconcile-bindings-worked-example-with-the-real-binding.md) | Reconcile BINDING section 5's worked example with the binding it predicted | `M1` | `done` | `review` | - | - | T-009, T-010 |
| [T-039](T-039-let-a-plan-name-a-deliverable-that-does-not-exist-yet.md) | Let a plan name a deliverable that does not exist yet | `M1` | `done` | `review` | - | - | T-010, T-025 |
| [T-040](T-040-make-the-thirty-second-assumptions-check-real.md) | Make the thirty-second assumptions check real, or change the number | `M1` | `done` | `review` | - | - | T-009, T-010, T-028, T-043 |
| [T-041](T-041-prove-the-github-bindings-body-rewrite-rule.md) | Prove the GitHub binding's body-rewrite rule by making it fail | `M1` | `done` | `review` | - | - | T-010, T-037, T-042, T-108, T-178 |
| [T-042](T-042-make-the-github-bindings-update-preserve-what-it-did-not-touch.md) | Make the GitHub binding's update preserve what it did not touch | `M1` | `done` | `review` | - | - | T-010, T-041, T-044 |
| [T-043](T-043-make-every-assumption-a-claim-about-the-adopting-project.md) | Make every assumption a claim about the adopting project | `M1` | `done` | `review` | - | - | T-004, T-009, T-010, T-040 |
| [T-044](T-044-state-the-gh-version-the-github-binding-requires.md) | State the gh version the GitHub binding requires | `M1` | `done` | `review` | - | - | T-010, T-042 |
| [T-045](T-045-decide-whether-scope-principles-may-state-the-rule-they-name.md) | Decide whether SCOPE §2 principles may state the rule they name | `M1` | `done` | `review` | - | - | T-017, T-027, T-208 |
| [T-046](T-046-reconcile-the-done-condition-claude-md-restates.md) | Reconcile the done-condition CLAUDE.md restates from the method | `M1` | `done` | `review` | - | - | T-027, T-028 |
| [T-047](T-047-move-the-conduct-rules-that-bind-before-task-work-into-tier-1.md) | Move the conduct rules that bind before task work into tier 1 | `M2` | `done` | `review` | - | - | T-015, T-028, T-035, T-059, T-063, T-105, T-115, T-118, T-119, T-190, T-194 |
| [T-048](T-048-say-what-always-loaded-means-in-r-21-before-the-skill-is-built.md) | Say what "always-loaded" means in R-21, before the skill is built against it | `M1` | `done` | `review` | - | - | T-003, T-028 |
| [T-049](T-049-demonstrate-a-clone-running-on-a-second-platform.md) | Demonstrate a clone running on a second platform | `M1` | `done` | `review` | T-011 | T-057, T-058 | T-006, T-020, T-054, T-056, T-057, T-058, T-061, T-085, T-116, T-132 |
| [T-050](T-050-measure-the-skill-s-tiers-on-a-session-handed-it.md) | Measure the skill's tiers on a session that was handed it | `M1` | `done` | `review` | T-003 | - | T-006, T-052, T-053, T-118, T-159, T-175, T-205, T-206 |
| [T-051](T-051-say-where-a-project-s-task-template-lives.md) | Say where a project's task template lives | `M1` | `done` | `review` | - | - | T-001, T-003, T-060, T-076, T-091, T-101 |
| [T-052](T-052-decide-what-of-claude-a-published-clone-carries.md) | Decide what of .claude a published clone carries, and ignore the rest | `M1` | `done` | `review` | - | - | T-003, T-006, T-050, T-053, T-067 |
| [T-053](T-053-decide-the-plugin-s-boundary-and-what-its-skill-may-p.md) | Decide the plugin's boundary, and what its skill may point at | `M1` | `done` | `review` | - | - | T-003, T-006, T-050, T-052, T-054, T-059, T-064, T-067, T-072, T-083, T-103 |
| [T-054](T-054-give-an-adopter-a-way-to-run-the-commands-the-skill-n.md) | Give an adopter a way to run the commands the skill names | `M1` | `done` | `review` | - | T-055, T-056 | T-003, T-006, T-049, T-053, T-055, T-056, T-067, T-068, T-083, T-085, T-099, T-142, T-148 |
| [T-055](T-055-settle-what-the-tool-calls-itself-when-it-prints-its-o.md) | Settle what the tool calls itself when it prints its own usage | `M1` | `done` | `review` | T-054 | - | T-029, T-054, T-071, T-099, T-134 |
| [T-056](T-056-make-the-shell-launcher-executable-in-a-unix-clone.md) | Make the shell launcher executable in a Unix clone | `M1` | `done` | `review` | T-054 | - | T-011, T-049, T-054, T-061 |
| [T-057](T-057-let-the-hook-tests-name-an-interpreter-that-exists.md) | Let the hook tests name an interpreter that exists on the platform | `M1` | `done` | `review` | T-049 | - | T-011, T-049 |
| [T-058](T-058-say-that-a-four-part-version-trips-the-leak-check.md) | Say that a four-part version number trips the leak check | `M1` | `done` | `review` | T-049 | - | T-018, T-034, T-035, T-049, T-080, T-186 |
| [T-059](T-059-audit-the-whole-project-after-the-plugin-restructure.md) | Audit the whole project after the plugin restructure | `M1` | `done` | `review` | - | T-060, T-061, T-062, T-063, T-064, T-065, T-066, T-067, T-068, T-069, T-070, T-071, T-072, T-073, T-074, T-075 | T-004, T-006, T-026, T-047, T-053 |
| [T-060](T-060-point-the-task-templates-at-paths-that-exist.md) | Point the task templates at paths that exist | `M1` | `done` | `review` | T-059 | - | T-032, T-051, T-076, T-091 |
| [T-061](T-061-stop-an-inherited-pythonpath-breaking-the-launcher.md) | Stop an inherited PYTHONPATH breaking the shell launcher | `M1` | `done` | `review` | T-059 | - | T-049, T-056, T-068 |
| [T-062](T-062-report-two-tasks-claiming-one-id-instead-of-dropping.md) | Report two tasks claiming one id instead of dropping one | `M1` | `done` | `review` | T-059 | - | T-004, T-075, T-107, T-200 |
| [T-063](T-063-measure-the-tier-1-member-the-rule-declares.md) | Measure the tier-1 member the rule declares | `M1` | `done` | `review` | T-059 | - | T-028, T-047, T-105, T-115, T-118 |
| [T-064](T-064-stop-the-plugin-citing-documents-it-does-not-ship.md) | Stop the plugin citing documents it does not ship | `M1` | `done` | `review` | T-059 | - | T-006, T-053, T-083, T-117, T-132, T-161 |
| [T-065](T-065-say-what-happens-to-a-field-the-schema-does-not-name.md) | Say what happens to a field the schema does not name | `M1` | `done` | `review` | T-059 | - | T-001, T-030, T-146 |
| [T-066](T-066-reconcile-two-open-tasks-with-the-fix-that-landed.md) | Reconcile two open tasks with the fix that already landed | `M1` | `done` | `review` | T-059 | - | T-011, T-023, T-030 |
| [T-067](T-067-prove-the-install-route-an-adopter-actually-takes.md) | Prove the install route an adopter actually takes | `M1` | `done` | `review` | T-059 | - | T-006, T-052, T-053, T-054, T-077, T-085, T-099 |
| [T-068](T-068-cover-the-entry-point-an-adopter-runs.md) | Cover the entry point an adopter runs | `M1` | `done` | `review` | T-059 | - | T-054, T-061 |
| [T-069](T-069-skip-a-nested-project-at-any-depth.md) | Skip a nested project at any depth, not below the first | `M1` | `done` | `review` | T-059 | - | T-011, T-078, T-107 |
| [T-070](T-070-decide-whether-an-unused-field-column-is-shown.md) | Decide whether an unused field column is shown at all | `M1` | `done` | `review` | T-059 | - | T-001, T-022, T-102 |
| [T-071](T-071-let-the-usage-test-assert-every-command-there-is.md) | Let the usage test assert every command there is | `M1` | `done` | `review` | T-059 | - | T-022, T-055, T-134 |
| [T-072](T-072-give-the-description-and-version-one-home-each.md) | Give the plugin's description and version one home each | `M1` | `done` | `review` | T-059 | - | T-006, T-053, T-207 |
| [T-073](T-073-correct-the-command-surface-local-context-states.md) | Correct the command surface local context still states | `M1` | `done` | `review` | T-059 | - | T-013, T-022, T-117, T-134 |
| [T-074](T-074-let-the-skill-point-where-it-currently-restates.md) | Let the skill point where it currently restates | `M1` | `done` | `review` | T-059 | - | T-003, T-009 |
| [T-075](T-075-enforce-id-width-when-a-task-file-is-read.md) | Enforce id width when a task file is read | `M1` | `done` | `review` | T-059 | - | T-004, T-062, T-082, T-107 |
| [T-076](T-076-decide-what-a-template-s-links-resolve-against.md) | Decide what a template's links resolve against | `M1` | `done` | `review` | - | - | T-032, T-051, T-060, T-091, T-101, T-103, T-104 |
| [T-077](T-077-delete-the-rehearsal-repository-t-067-installed-from.md) | Delete the rehearsal repository T-067 installed from | `M1` | `done` | `review` | - | - | T-037, T-067 |
| [T-078](T-078-say-what-a-tasks-dir-of-dot-means.md) | Say what a tasks_dir of dot means | `M2` | `done` | `review` | - | - | T-019, T-024, T-069 |
| [T-079](T-079-humanize-the-human-facing-documents-before-publishing.md) | Humanize the human-facing documents before publishing | `M1` | `done` | `review` | - | - | T-081, T-125, T-126, T-127, T-133 |
| [T-080](T-080-stop-the-pre-publish-check-reporting-its-own-fixture.md) | Stop the pre-publish check reporting its own fixture from a subdirectory | `M1` | `done` | `review` | - | - | T-018, T-034, T-058, T-081, T-095, T-098, T-183, T-186 |
| [T-081](T-081-gate-every-deployment-on-the-humanizer-pass.md) | Gate every deployment on the humanizer pass, not just the next one | `M1` | `done` | `review` | - | - | T-079, T-080, T-125, T-126, T-127, T-133 |
| [T-082](T-082-let-id-width-say-the-backend-allocates-the-ids.md) | Let id_width say that the backend allocates the ids | `M2` | `done` | `review` | T-004 | - | T-010, T-075, T-108, T-123, T-137 |
| [T-083](T-083-make-the-skill-directory-self-contained.md) | Make the skill directory self-contained | `M1` | `done` | `review` | - | - | T-053, T-054, T-064, T-084, T-099, T-103 |
| [T-084](T-084-correct-the-generated-index-preamble-after-the-move.md) | Correct the generated index preamble after the directory move | `M1` | `done` | `review` | - | - | T-006, T-025, T-083 |
| [T-085](T-085-install-the-published-plugin-on-a-machine-that-has-never-seen-it.md) | Install the published plugin on a machine that has never seen it | `M5` | `done` | `review` | T-006 | - | T-020, T-049, T-054, T-067, T-099, T-129, T-142, T-183 |
| [T-086](T-086-group-the-backlog-into-release-milestones.md) | Group the backlog into release milestones | `M2` | `done` | `review` | - | - | T-006, T-022, T-026, T-087, T-110, T-128, T-135, T-136 |
| [T-087](T-087-let-list-filter-on-a-field-the-index-can-show.md) | Let list filter on a field the index can show | `M2` | `done` | `review` | - | - | T-022, T-029, T-086, T-102, T-124, T-137, T-143, T-144 |
| [T-088](T-088-put-audit-in-the-shipped-type-vocabulary-or-stop-calling-it-a-type.md) | Put audit in the shipped type vocabulary, or stop calling it a type | `M2` | `done` | `review` | - | - | T-001, T-026, T-032, T-100, T-104, T-109, T-131, T-137 |
| [T-089](T-089-stop-check-reporting-an-open-task-s-planned-outputs-as-missing.md) | Stop check reporting an open task's planned outputs as missing | `M2` | `done` | `review` | - | T-090 | T-002, T-025, T-032, T-103, T-146 |
| [T-090](T-090-decide-what-a-cancelled-task-s-declared-outputs-assert.md) | Decide what a cancelled task's declared outputs assert | `M2` | `done` | `review` | T-089 | - | T-002, T-032, T-103, T-109 |
| [T-091](T-091-make-the-shipped-task-template-survive-being-copied.md) | Make the shipped task template survive being copied into another project | `M2` | `done` | `review` | - | - | T-032, T-051, T-060, T-076, T-097, T-101, T-112, T-114 |
| [T-092](T-092-decide-whether-a-bare-path-in-prose-is-a-reference.md) | Decide whether a bare path in prose is a reference check must resolve | `M2` | `done` | `review` | - | - | T-034, T-093, T-094, T-095, T-097, T-103, T-112 |
| [T-093](T-093-decide-whether-check-resolves-a-section-reference.md) | Decide whether check resolves a section reference | `M6` | `done` | `review` | - | T-194 | T-092, T-095, T-109 |
| [T-094](T-094-make-check-answer-the-question-a-fresh-clone-would-ask.md) | Make check answer the question a fresh clone would ask | `M2` | `done` | `review` | - | - | T-013, T-034, T-092, T-095, T-097, T-098 |
| [T-095](T-095-report-what-check-examined-not-only-that-it-passed.md) | Report what check examined, not only that it passed | `M2` | `done` | `review` | - | T-096 | T-025, T-034, T-080, T-092, T-093, T-094, T-098, T-100, T-101, T-112, T-130, T-141, T-147, T-162, T-185 |
| [T-096](T-096-decide-whether-a-narrower-walk-of-a-counted-class-needs-its-own-number.md) | Decide whether a narrower walk of a counted class needs its own number | `M2` | `done` | `review` | T-095 | - | T-025, T-121 |
| [T-097](T-097-decide-whether-a-published-document-may-point-at-a-file-no-clone-receives.md) | Decide whether a published document may point at a file no clone receives | `M2` | `done` | `review` | - | - | T-013, T-034, T-091, T-092, T-094, T-109 |
| [T-098](T-098-decide-who-checks-the-links-in-a-document-only-a-successor-reads.md) | Decide who checks the links in a document only a successor reads | `M2` | `done` | `review` | - | - | T-002, T-034, T-080, T-094, T-095, T-109 |
| [T-099](T-099-give-an-adopter-a-command-that-runs-without-bin-on-path.md) | Give an adopter a command that runs when the plugin's bin is not on PATH | `M2` | `done` | `review` | - | - | T-054, T-055, T-067, T-083, T-085, T-140, T-142, T-148, T-161 |
| [T-100](T-100-report-a-project-config-that-has-drifted-from-the-shipped-default.md) | Report a project config that has drifted from the shipped default | `M2` | `done` | `review` | - | - | T-001, T-023, T-088, T-095, T-106, T-121, T-137, T-138, T-139, T-146, T-151, T-191 |
| [T-101](T-101-report-a-template-the-create-path-cannot-see.md) | Report a template the create path cannot see | `M2` | `done` | `review` | - | - | T-032, T-051, T-076, T-091, T-095, T-107, T-121 |
| [T-102](T-102-show-which-rows-list-has-already-worked-out-are-blocked.md) | Show which rows list has already worked out are blocked | `M2` | `done` | `review` | - | - | T-022, T-031, T-070, T-087, T-111 |
| [T-103](T-103-say-whether-a-closed-task-s-declared-output-may-be-repointed.md) | Say whether a closed task's declared output may be repointed when the file moves | `M3` | `done` | `review` | - | - | T-053, T-076, T-083, T-089, T-090, T-092, T-104, T-109 |
| [T-104](T-104-say-whether-the-method-has-an-opinion-on-where-a-decision-is-recorded.md) | Say whether the method has an opinion on where a decision is recorded | `M3` | `done` | `review` | - | - | T-008, T-076, T-088, T-103, T-109 |
| [T-105](T-105-say-where-an-authorised-multi-phase-run-is-recorded.md) | Say where an authorised multi-phase run is recorded | `M3` | `done` | `review` | - | - | T-005, T-036, T-047, T-063 |
| [T-106](T-106-say-that-the-shipped-config-cannot-gain-a-key.md) | Say that the shipped config cannot gain a key without breaking every project that wrote one | `M3` | `done` | `review` | - | - | T-001, T-011, T-023, T-100, T-137, T-138, T-146, T-184 |
| [T-107](T-107-say-so-when-a-valid-task-file-is-parked-where-nothing-reads-it.md) | Say so when a valid task file is parked where nothing reads it | `M2` | `done` | `review` | - | - | T-062, T-069, T-075, T-101, T-121, T-130, T-141 |
| [T-108](T-108-support-a-project-moving-its-tasks-from-files-to-github-issues.md) | Support a project moving its tasks from local files to GitHub Issues | `M6` | `done` | `review` | - | - | T-004, T-009, T-010, T-041, T-082, T-163, T-164, T-166, T-178, T-179, T-181, T-185, T-193, T-196, T-203 |
| [T-109](T-109-decide-whether-a-task-that-settles-a-question-must-be-typed-decision.md) | Decide whether a task that settles a question must be typed decision | `M2` | `done` | `review` | - | - | T-088, T-090, T-093, T-097, T-098, T-103, T-104, T-110, T-131 |
| [T-110](T-110-re-group-the-open-backlog-by-the-maintainers-release-rule.md) | Re-group the open backlog by the maintainer's release rule | `M2` | `done` | `review` | - | - | T-026, T-086, T-109, T-124, T-125, T-128, T-136 |
| [T-111](T-111-stop-the-index-showing-a-closed-task-as-a-live-blocker.md) | Stop the index showing a closed task as a live blocker | `M2` | `done` | `review` | - | - | T-102 |
| [T-112](T-112-stop-check-resolving-a-link-that-is-displayed-rather-than-navigable.md) | Stop check resolving a link that is displayed rather than navigable | `M2` | `done` | `review` | - | - | T-091, T-092, T-095, T-114 |
| [T-113](T-113-name-an-unknown-filter-before-complaining-it-has-no-value.md) | Name an unknown filter before complaining it has no value | `M2` | `done` | `review` | - | - | T-022, T-029, T-120, T-122, T-144, T-145, T-162 |
| [T-114](T-114-make-the-launcher-tests-say-which-bash-they-found.md) | Make the launcher tests say which bash they found | `M2` | `done` | `review` | - | - | T-091, T-112 |
| [T-115](T-115-give-the-tier-1-budget-something-that-enforces-it.md) | Give the tier 1 budget something that enforces it | `M2` | `done` | `review` | - | - | T-028, T-047, T-063, T-116, T-118, T-126 |
| [T-116](T-116-decide-whether-the-published-repository-runs-its-own-suite.md) | Decide whether the published repository runs its own suite | `M2` | `done` | `review` | - | - | T-011, T-049, T-115 |
| [T-117](T-117-decide-whether-the-command-surface-needs-one-statement.md) | Decide whether the command surface needs one statement | `M5` | `done` | `review` | - | T-134 | T-030, T-031, T-064, T-073, T-134, T-149 |
| [T-118](T-118-decide-what-leaves-tier-1-when-the-budget-binds.md) | Decide what leaves tier 1 when the budget binds | `M2` | `done` | `review` | - | - | T-026, T-028, T-035, T-047, T-050, T-063, T-115, T-119, T-143, T-152, T-155, T-169 |
| [T-119](T-119-put-the-stranded-paragraph-under-a-heading-that-owns-it.md) | Put the stranded paragraph under a heading that owns it | `M2` | `done` | `review` | - | - | T-047, T-118 |
| [T-120](T-120-echo-an-unknown-flag-as-the-caller-typed-it.md) | Echo an unknown flag as the caller typed it | `M2` | `done` | `review` | - | - | T-022, T-113, T-122, T-145 |
| [T-121](T-121-report-a-second-index-of-the-same-tasks-outside-the-markers.md) | Report a second index of the same tasks sitting outside the generated markers | `M5` | `done` | `review` | - | - | T-025, T-096, T-100, T-101, T-107, T-130, T-139, T-141, T-200 |
| [T-122](T-122-echo-the-typed-flag-in-the-rejected-value-message.md) | Echo the typed flag in the rejected-value message too | `M2` | `done` | `review` | - | - | T-113, T-120 |
| [T-123](T-123-decide-whether-a-replaced-vocabulary-row-is-drift.md) | Decide whether a replaced vocabulary row is drift or a choice | `M2` | `done` | `review` | - | - | T-082 |
| [T-124](T-124-stop-a-test-asserting-this-repository-has-open-v0-2-work.md) | Stop a test asserting this repository has open M2 work | `M2` | `done` | `review` | - | - | T-087, T-110 |
| [T-125](T-125-ship-the-completed-v0-2-work-as-0-4-0.md) | Ship the completed M2 work as 0.4.0 | `M2` | `done` | `review` | - | - | T-006, T-079, T-081, T-110, T-126, T-127, T-128, T-129, T-133, T-135, T-136, T-182 |
| [T-126](T-126-catch-dash-gate-drift-before-publication-rather-than-at-it.md) | Catch dash-gate drift before publication rather than at it | `M5` | `done` | `review` | - | - | T-079, T-081, T-115, T-125, T-127, T-129, T-133, T-134, T-186 |
| [T-127](T-127-decide-whether-a-release-note-is-text-a-stranger-reads.md) | Decide whether a release note is text a stranger reads | `M5` | `done` | `review` | - | - | T-079, T-081, T-125, T-126, T-129, T-133, T-135, T-182 |
| [T-128](T-128-make-a-milestone-name-the-release-it-ships-in.md) | Make a milestone name the release it ships in | `M5` | `done` | `review` | - | - | T-086, T-110, T-125, T-135, T-136 |
| [T-129](T-129-release-v0-5.md) | Release M5 | `M5` | `done` | `review` | - | - | T-085, T-125, T-126, T-127, T-133, T-135 |
| [T-130](T-130-report-a-question-left-live-in-a-closed-task.md) | Report a question left live in a closed task | `M6` | `done` | `review` | - | - | T-025, T-095, T-107, T-121, T-131 |
| [T-131](T-131-decide-whether-a-question-heavy-task-is-a-different-kind-of-work.md) | Decide whether a question-heavy task is a different kind of work | `M6` | `done` | `review` | - | - | T-088, T-109, T-130 |
| [T-132](T-132-give-the-console-the-same-line-ending-on-every-platform.md) | Give the console the same line ending on every platform | `M5` | `done` | `review` | T-020 | - | T-002, T-020, T-022, T-049, T-064 |
| [T-133](T-133-decide-what-to-do-about-a-published-release-note-that-breaks-the-rule.md) | Decide what to do about a published release note that breaks the rule | `M5` | `done` | `review` | - | - | T-079, T-081, T-125, T-126, T-127, T-129, T-135, T-182, T-183 |
| [T-134](T-134-check-that-every-prose-list-of-the-commands-names-the-commands-there-are.md) | Check that every prose list of the commands names the commands there are | `M5` | `done` | `review` | T-117 | - | T-030, T-031, T-055, T-071, T-073, T-117, T-126, T-139, T-147, T-149, T-188, T-195, T-202 |
| [T-135](T-135-derive-what-a-release-note-must-cover-from-the-tasks-it-ships.md) | Derive what a release note must cover from the tasks it ships | `M6` | `done` | `review` | - | T-182 | T-086, T-125, T-127, T-128, T-129, T-133 |
| [T-136](T-136-rename-the-milestone-labels-so-they-cannot-be-read-as-versions.md) | Rename the milestone labels so they cannot be read as versions | `M6` | `done` | `review` | - | - | T-086, T-110, T-125, T-128, T-137, T-138 |
| [T-137](T-137-decide-what-taskmd-does-about-a-label-read-as-a-version.md) | Decide what taskmd does about a grouping label that can be read as a version | `M6` | `done` | `review` | - | - | T-004, T-082, T-087, T-088, T-100, T-106, T-136, T-138 |
| [T-138](T-138-report-a-front-matter-value-that-reads-as-a-version.md) | Report a front-matter value that reads as a version | `M6` | `done` | `review` | - | - | T-100, T-106, T-136, T-137, T-139, T-162 |
| [T-139](T-139-check-that-the-advisory-lines-the-readme-lists-are-the-ones-there-are.md) | Check that the advisory lines the README lists are the advisory lines there are | `M6` | `done` | `review` | - | - | T-100, T-121, T-134, T-138, T-141, T-147, T-149, T-161, T-188, T-192, T-195, T-197 |
| [T-140](T-140-restore-the-log-row-a-table-cell-swallowed.md) | Restore the log row a table cell swallowed in T-099 | `M6` | `done` | `review` | - | - | T-099, T-141 |
| [T-141](T-141-report-a-table-row-with-more-cells-than-its-header.md) | Report a table row with more cells than its header | `M6` | `done` | `review` | - | - | T-025, T-095, T-107, T-121, T-139, T-140, T-147, T-150, T-151, T-162 |
| [T-142](T-142-stop-the-entry-point-stating-the-path-mechanism-as-given.md) | Stop the entry point stating the PATH mechanism as given | `M6` | `done` | `review` | - | T-161 | T-054, T-085, T-099, T-148, T-153, T-161 |
| [T-143](T-143-decide-whether-tier-1-names-the-generated-index-at-all.md) | Decide whether tier 1 names the generated index at all | `M6` | `done` | `review` | - | - | T-022, T-028, T-087, T-118, T-152, T-158 |
| [T-144](T-144-decide-whether-a-commands-own-options-can-be-discovered-from-the-cli.md) | Decide whether a command's own options can be discovered from the CLI | `M6` | `done` | `review` | - | - | T-022, T-029, T-087, T-113, T-145, T-149 |
| [T-145](T-145-stop-help-answering-for-a-command-that-does-not-exist.md) | Stop --help answering for a command that does not exist | `M6` | `done` | `review` | - | - | T-029, T-113, T-120, T-144 |
| [T-146](T-146-decide-whether-a-field-can-be-required-at-a-status.md) | Decide whether a field can be required at a status | `M6` | `done` | `review` | - | - | T-065, T-089, T-100, T-106, T-173, T-184 |
| [T-147](T-147-check-that-a-quoted-command-output-is-output-the-tool-produces.md) | Check that a quoted command output is output the tool produces | `M6` | `done` | `review` | - | - | T-095, T-134, T-139, T-141 |
| [T-148](T-148-decide-whether-a-caller-outside-a-served-skill-can-find-the-launcher.md) | Decide whether a caller outside a served skill can find the launcher | `M6` | `done` | `review` | - | - | T-054, T-099, T-142 |
| [T-149](T-149-check-that-every-prose-list-of-lists-options-names-the-options-there-are.md) | Check that every prose list of list's options names the options there are | `M6` | `done` | `review` | - | - | T-117, T-134, T-139, T-144 |
| [T-150](T-150-give-the-wide-row-fixture-a-front-matter-that-carries-pipes.md) | Give the wide-row fixture a front matter that carries pipes | `M6` | `done` | `review` | - | - | T-032, T-141, T-151, T-191, T-198, T-201 |
| [T-151](T-151-decide-whether-a-check-needs-a-case-that-must-not-fire.md) | Decide whether a check needs a case that must not fire | `M6` | `done` | `review` | - | - | T-100, T-141, T-150, T-172, T-173, T-190, T-191, T-193, T-197, T-198, T-201, T-202 |
| [T-152](T-152-audit-what-this-repository-costs-a-session-on-every-turn.md) | Audit — what this repository costs a session on every turn | `M6` | `done` | `review` | - | T-153, T-154, T-155, T-156, T-157, T-158 | T-118, T-143, T-170, T-189 |
| [T-153](T-153-e-10-move-the-maintainer-s-justification-into-comments.md) | E-10 — Move the maintainer's justification into comments the harness strips | `M6` | `done` | `review` | T-152 | T-159, T-160 | T-142, T-155, T-169 |
| [T-154](T-154-e-01-e-04-say-what-the-tier-1-budget-governs.md) | E-01/E-04 — Say what the tier-1 budget governs, and what it cannot see | `M6` | `done` | `review` | T-152 | - | T-028 |
| [T-155](T-155-e-13-test-whether-a-path-scoped-rule-can-hold-tier-1-s-prose.md) | E-13 — Test whether a path-scoped rule can hold tier 1's prose about itself | `M6` | `done` | `review` | T-152 | T-169 | T-118, T-153, T-158, T-159, T-171 |
| [T-156](T-156-e-16-decide-whether-a-read-only-phase-can-skip-the-binding.md) | E-16 — Decide whether a read-only phase can skip the binding | `M6` | `done` | `review` | T-152 | - | - |
| [T-157](T-157-b-2-settle-what-context-claims-to-be-enough-for.md) | B-2 — Settle what `taskmd context` claims to be enough for | `M6` | `done` | `review` | T-152 | - | - |
| [T-158](T-158-phase-2-grade-each-band-against-what-it-bought.md) | Phase 2 of the context-economy audit — grade each band against what it bought | `M6` | `cancelled` | `specify` | T-152 | - | T-143, T-155 |
| [T-159](T-159-observe-whether-a-block-comment-reaches-a-session.md) | Observe whether a block comment in CLAUDE.md reaches a session | `M6` | `done` | `review` | T-153 | - | T-050, T-155, T-160 |
| [T-160](T-160-retire-the-budget-check-s-unobserved-premise-warning.md) | Retire the budget check's unobserved-premise warning, now that it is observed | `M6` | `done` | `review` | T-153 | - | T-159, T-161 |
| [T-161](T-161-give-the-entry-point-comments-pointer-a-reader.md) | Give the entry-point comments' pointer a reader | `M6` | `done` | `review` | T-142 | - | T-064, T-099, T-139, T-142, T-160 |
| [T-162](T-162-decide-whether-check-reads-a-date-shaped-field-as-a-date.md) | Decide whether check reads a date-shaped field as a date | `M6` | `done` | `review` | - | T-184 | T-095, T-113, T-138, T-141 |
| [T-163](T-163-tell-a-migrated-project-what-taskmd-still-provides.md) | Tell a migrated project what taskmd still provides, without judging whether it should stay | `M6` | `done` | `review` | - | T-165 | T-108, T-164, T-166, T-167, T-177, T-180 |
| [T-164](T-164-say-something-truthful-when-a-migrated-project-runs-a-command.md) | Say something truthful when a migrated project runs one of the four commands | `M6` | `done` | `review` | - | - | T-108, T-163, T-180 |
| [T-165](T-165-have-an-uninvolved-reader-test-the-post-migration-listing.md) | Have an uninvolved reader test the post-migration listing | `M6` | `done` | `review` | T-163 | - | T-166, T-167 |
| [T-166](T-166-ground-the-post-migration-listing-s-survivor-claims.md) | Stop the post-migration listing framing toward keeping taskmd | `M6` | `done` | `review` | - | - | T-108, T-163, T-165, T-167, T-168, T-176 |
| [T-167](T-167-stop-the-listing-pricing-only-the-rival.md) | Stop the post-migration listing pricing only the rival skill | `M6` | `cancelled` | `specify` | - | - | T-163, T-165, T-166, T-168, T-176 |
| [T-168](T-168-price-what-keeping-taskmd-installed-costs-a-project-with-no-tasks.md) | Price what keeping taskmd installed costs a project that has no tasks folder | `M6` | `done` | `review` | - | T-174, T-175, T-176 | T-166, T-167, T-174, T-175, T-176, T-205 |
| [T-169](T-169-decide-whether-tier-1-s-prose-about-itself-moves-into-a-path-scoped-rule.md) | Decide whether tier 1's prose about itself moves into a path-scoped rule | `M6` | `done` | `review` | T-155 | T-171 | T-118, T-153 |
| [T-170](T-170-decide-whether-the-audit-s-upstream-rows-are-reported-to-anyone.md) | Decide whether the audit's upstream rows are reported to anyone | `M6` | `done` | `review` | - | - | T-152, T-189 |
| [T-171](T-171-test-whether-the-hook-can-see-a-path-scoped-rule.md) | Test whether the InstructionsLoaded hook can see a path-scoped rule | `M6` | `done` | `review` | T-169 | - | T-155, T-172 |
| [T-172](T-172-catch-a-template-placeholder-left-in-a-finished-record.md) | Catch a template placeholder left in a finished record | `M6` | `done` | `review` | - | - | T-032, T-151, T-171, T-173 |
| [T-173](T-173-decide-whether-check-can-know-a-phase-without-breaking-every-adopter.md) | Decide whether check can know a phase without breaking every adopter | `M6` | `done` | `review` | - | - | T-146, T-151, T-172 |
| [T-174](T-174-carry-the-command-that-produced-t-168-s-figures.md) | Carry the command that produced T-168's figures into a record that can re-run it | `M6` | `done` | `review` | T-168 | - | T-168 |
| [T-175](T-175-observe-whether-the-skill-triggers-in-a-migrated-away-project.md) | Observe whether the skill triggers in a project that has migrated its backlog away | `M6` | `done` | `review` | T-168 | T-205 | T-050, T-168, T-206 |
| [T-177](T-177-run-the-checks-that-need-no-task-folder.md) | Decide whether check runs the checks that never look at a task file | `M6` | `done` | `review` | - | T-185 | T-163, T-178, T-179, T-180 |
| [T-178](T-178-give-the-github-binding-a-standing-verification.md) | Give the GitHub binding a standing verification, not only a migration-day one | `M6` | `done` | `review` | - | T-193 | T-041, T-108, T-177, T-179, T-185, T-192, T-203 |
| [T-179](T-179-restore-the-ordering-rule-on-the-github-backend.md) | Restore the what-next ordering rule on the GitHub backend | `M6` | `done` | `review` | - | - | T-022, T-108, T-177, T-178, T-187 |
| [T-180](T-180-route-a-migrated-project-to-its-binding-not-to-adopt.md) | Route a migrated project to its binding rather than to adopt.md | `M6` | `done` | `review` | - | - | T-163, T-164, T-177 |
| [T-181](T-181-verify-the-handoff-github-recipe-on-a-live-issues-backed-project.md) | Verify the handoff GitHub recipe against a live issues-backed project | `M6` | `done` | `review` | T-005 | - | T-108, T-193 |
| [T-183](T-183-decide-what-to-do-about-a-machine-block-already-published-in-t-085.md) | Decide what to do about a machine block already published in T-085 | `M6` | `done` | `review` | - | - | T-034, T-080, T-085, T-133, T-186 |
| [T-184](T-184-report-a-date-shaped-value-that-is-not-a-date.md) | Report a date-shaped value that is not a date | `M6` | `done` | `review` | T-162 | - | T-106, T-146, T-188 |
| [T-185](T-185-run-the-document-checks-in-a-project-whose-tasks-moved.md) | Run the document checks in a project whose tasks moved | `M6` | `done` | `review` | T-177 | - | T-095, T-108, T-178 |
| [T-186](T-186-run-the-leak-check-in-the-suite-not-only-at-publication.md) | Run the leak check in the suite, not only at publication | `M6` | `done` | `review` | - | - | T-034, T-058, T-080, T-126, T-183 |
| [T-187](T-187-say-that-the-one-design-rule-yields-to-a-system-limitation.md) | Say that the one design rule yields to a system limitation | `M6` | `done` | `review` | - | - | T-012, T-179, T-207, T-208 |
| [T-188](T-188-report-a-counted-set-written-into-prose-that-the-code-owns.md) | Report a counted set written into prose that the code owns | `M6` | `done` | `review` | - | - | T-134, T-139, T-184, T-195 |
| [T-189](T-189-say-whether-the-audit-s-method-finding-reached-the-repository-that-owns-it.md) | Say whether the audit's method finding reached the repository that owns it | `M6` | `done` | `review` | - | - | T-152, T-170 |
| [T-190](T-190-decide-whether-tier-1-restates-two-verification-rules-the-method-owns.md) | Decide whether tier 1 restates two verification rules the method owns | `M6` | `done` | `review` | - | - | T-028, T-047, T-151 |
| [T-192](T-192-require-every-binding-to-declare-its-validator-coverage.md) | Require every binding to declare its validator coverage | `M6` | `done` | `review` | - | T-199 | T-009, T-139, T-178 |
| [T-193](T-193-make-the-standing-github-check-fail-before-trusting-it.md) | Make the standing GitHub check fail before trusting it | `M6` | `done` | `review` | T-178 | T-196 | T-108, T-151, T-181, T-203 |
| [T-194](T-194-print-the-two-method-sections-this-project-cites-most.md) | Print the two method sections this project cites most | `M6` | `done` | `review` | T-093 | - | T-028, T-047 |
| [T-195](T-195-hold-the-fixture-readme-against-the-fixtures-there-are.md) | Hold the fixture README against the fixtures there are | `M6` | `done` | `review` | - | - | T-134, T-139, T-188 |
| [T-196](T-196-delete-the-scratch-repository-the-standing-check-ran-against.md) | Delete the scratch repository the standing check ran against | `M6` | `done` | `review` | T-193 | - | T-108 |
| [T-197](T-197-derive-the-test-harness-s-problem-class-list-from-the-code.md) | Derive the test harness's problem-class list from the code | `M6` | `done` | `review` | T-191 | - | T-139, T-151, T-200, T-202 |
| [T-200](T-200-discount-the-ids-a-task-file-carries-even-when-it-was-not-loaded.md) | Discount the ids a task file carries even when it was not loaded | `M6` | `done` | `review` | - | - | T-062, T-121, T-197 |
| [T-201](T-201-give-the-fenced-table-case-a-row-that-could-be-reported.md) | Give the fenced-table case a row that could be reported | `M6` | `done` | `review` | T-198 | - | T-150, T-151, T-204 |
| [T-204](T-204-count-the-short-row-quiet-case-the-wide-row-audit-left-out.md) | Count the short-row quiet case the wide-row audit left out | `M6` | `done` | `review` | T-198 | - | T-201, T-202 |
| [T-205](T-205-decide-whether-a-clean-trigger-observation-is-reachable-on-this-machine.md) | Decide whether a clean trigger observation is reachable on this machine | `M6` | `done` | `review` | T-175 | T-206 | T-050, T-168 |

<!-- taskmd:end -->
