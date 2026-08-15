#!/usr/bin/env python
"""Proof for T-002: the three commands, and `check` shown failing on every class it claims.

The negative cases are the point. A validator is worth exactly your confidence that it *would*
catch what it claims to, and the only way to earn that is to watch it fail on a case it should
catch — so every `broken-*` fixture under `tests/fixtures/` is asserted to produce its own class
and nothing else.

  python tests/test_cli.py
"""

import glob
import inspect
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")   # where the taskmd package lives (T-083)
sys.path.insert(0, PKG)

from taskmd import cli  # noqa: E402

FIXTURES = os.path.join(ROOT, "tests", "fixtures")


def run(*argv):
    """Call the CLI the way a shell does, capturing what a user would see."""
    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        code = cli.main(list(argv))
    finally:
        sys.stdout = stdout
    return code, buffer.getvalue()


class ChecksThisRepository(unittest.TestCase):
    """The real case: taskmd validating the project that is building it."""

    def test_check_is_clean_and_says_how_many_tasks(self):
        code, out = run("check", "--root", ROOT)
        self.assertEqual(code, 0, out)
        self.assertIn("OK - ", out)

    def test_a_project_directly_inside_the_root_is_still_skipped(self):
        """T-069. The exclusion used to start one directory down, so a monorepo holding a taskmd
        project at its top level had that project's defects reported as its own.

        It never showed here because every `broken-*` fixture sits two levels down — the shape of
        the fixture set was hiding the shape of the bug. `nested-at-root` is the only fixture whose
        nested project is a direct child. (This line used to say "all ten", and by the time T-025
        read it there were twelve; the set is what it is, and counting it here was a second copy of
        `ls`.)"""
        code, out = run("check", "--root", os.path.join(FIXTURES, "nested-at-root"))
        self.assertEqual(code, 0, out)
        self.assertNotIn("inner/", out)

    def test_a_task_built_from_each_shipped_template_passes(self):
        """T-032 criterion 1, and the thing `check` still cannot ask on its own: it validates a
        template's *front-matter*, but only copying one out proves the result is a task.

        **Run in a temp folder, deliberately** — the one place in this class that is not this
        repository. It used to run here because a template's relative links resolved against the
        project it was copied into, so a fresh folder with no `plugin/` broke them for a reason that
        had nothing to do with the template. T-091 removed the links, and this is what proves it:
        the failure an adopter reported was `check` on a copied template, and only a project that is
        not this one can see it. Copy the template in as well as the task made from it, because both
        are what the adopter had."""
        for template in sorted(glob.glob(os.path.join(ROOT, "tasks", "_*.md"))):
            body = cli.read(template)
            for placeholder, value in (("T-NNN", "T-999"), ("YYYY-MM-DD", "2026-01-01")):
                body = body.replace(placeholder, value)
            body = re.sub(r"^(title|owner|work_package|type|business_value|effort): .*$",
                          lambda m: "%s: %s" % (m.group(1), {
                              "title": "A trial task", "owner": "someone",
                              "work_package": "none", "type": "audit",
                              "business_value": "high", "effort": "s"}[m.group(1)]),
                          body, flags=re.M)
            elsewhere = tempfile.mkdtemp()
            try:
                tasks = os.path.join(elsewhere, "tasks")   # the whole of setup, per `adopt.md`
                os.mkdir(tasks)
                shutil.copyfile(template, os.path.join(tasks, os.path.basename(template)))
                cli.write(os.path.join(tasks, "T-999-trial.md"), body)
                run("index", "--root", elsewhere)          # or STALE INDEX is the only finding
                code, out = run("check", "--root", elsewhere)
                self.assertEqual(code, 0, "%s produced:\n%s" % (os.path.basename(template), out))
            finally:
                shutil.rmtree(elsewhere)

    def test_the_broken_fixtures_are_not_reported_as_this_projects_problems(self):
        """They are projects in their own right. If the host reported them, `check` could never
        be clean here and the fixtures would have to live outside the repository."""
        code, out = run("check", "--root", ROOT)
        self.assertEqual(code, 0)
        self.assertNotIn("broken-", out)


class CheckFailsOnEveryClassItClaims(unittest.TestCase):
    """One fixture per class. Each must report its own class, and only its own."""

    LABELS = ["VOCABULARY", "DANGLING", "NO BLOCKER", "CYCLE", "BROKEN LINK",
              "STORED DERIVED", "MISSING OUTPUT", "CONFIG ERROR", "DUPLICATE ID", "ID WIDTH",
              "STALE INDEX", "TEMPLATE UNREACHABLE", "TEMPLATE FIELD", "PARKED TASK"]

    def fails(self, fixture, label, needle, code=1):
        got, out = run("check", "--root", os.path.join(FIXTURES, fixture))
        self.assertEqual(got, code, out)
        self.assertIn(label, out)
        self.assertIn(needle, out)
        for other in self.LABELS:
            if other != label:
                self.assertNotIn(other, out, "%s also reported %s:\n%s" % (fixture, other, out))

    def test_value_outside_its_vocabulary(self):
        self.fails("broken-vocabulary", "VOCABULARY", "'in-progres'")

    def test_edge_pointing_at_a_task_that_does_not_exist(self):
        self.fails("broken-dangling", "DANGLING", "T-404")

    def test_blocked_with_nothing_blocking_it(self):
        self.fails("broken-missing-blocker", "NO BLOCKER", "blocked_by")

    def test_dependency_loop(self):
        self.fails("broken-cycle", "CYCLE", "T-001 -> T-002 -> T-001")

    def test_dead_link_inside_a_dot_directory(self):
        """`glob`'s `**` skips dot-directories. Walking is what catches this one."""
        self.fails("broken-link", "BROKEN LINK", ".notes/scratch.md")

    def test_task_storing_a_field_that_is_derived(self):
        self.fails("broken-derived-field", "STORED DERIVED", "'children:'")

    def test_template_whose_front_matter_has_rotted(self):
        """T-032. `load_tasks` reads a template and discards it on its placeholder id, so both
        shipped templates could rot in silence — and one had, naming a `type` the config did not
        have and storing a derived field. The fixture carries all three forms, because the class is
        one class and the third is the one that hides longest: a menu that has fallen behind by a
        single value, every value it still offers being legal."""
        self.fails("broken-template-field", "TEMPLATE FIELD", "'children:'")
        out = run("check", "--root", os.path.join(FIXTURES, "broken-template-field"))[1]
        self.assertIn("sets 'type' to 'nonsense'", out)
        self.assertIn("offers 'critical | high | low' for 'business_value'", out)
        # The angle-bracket slots are placeholders, not defects — a check that reported them would
        # be unusable on any real template.
        self.assertNotIn("imperative", out)

    def test_declared_deliverable_that_is_gone(self):
        """The task is `done`. T-089 made that load-bearing: the fixture used to be `proposed`, so
        it proved this class through an open task and the assertion went vacuous the moment the
        rule became "closed tasks only"."""
        self.fails("broken-deliverable", "MISSING OUTPUT", "out/report.md")

    def test_config_error_surfaces_at_setup_naming_the_key(self):
        """R-17: reported when the config is read, with exit 2 — never from inside a command."""
        self.fails("broken-config", "CONFIG ERROR", "id_witdh", code=2)

    def test_two_files_claiming_one_id(self):
        """T-062. Before this class, three task files could produce two tasks and `OK`, exit 0."""
        self.fails("broken-duplicate-id", "DUPLICATE ID", "T-001-second.md")

    def test_an_id_that_is_the_right_prefix_and_the_wrong_width(self):
        """T-075. `id_width` used to be honoured only when composing a new id, never when reading
        one, so a file no `create` could have produced was silently a task."""
        self.fails("broken-id-width", "ID WIDTH", "T-0001")

    def test_a_template_the_create_path_cannot_see(self):
        """T-101. Silent in both directions before this: the folder is skipped by the same rule that
        keeps templates out of the task set, so the listing that finds a template came back empty —
        and empty is the documented shape of a project that simply has none."""
        self.fails("broken-unreachable-template", "TEMPLATE UNREACHABLE", "_templates/")

    def test_a_valid_task_parked_where_the_walk_never_reaches_it(self):
        """T-107. Two task files, one task, `OK` and exit 0 — the parked one's only trace was the
        document count, which is the same silent-loss shape as DUPLICATE ID and ID WIDTH."""
        self.fails("broken-parked-task", "PARKED TASK", "T-002")

    def test_a_projects_own_material_in_the_same_folder_is_not_reported(self):
        """The other half of T-107, and the half that can regress unnoticed. The `_` skip is what
        lets a project keep notes beside its tasks with no exclusion list; a check that fired on
        `notes.md` would have stopped being about lost work and become one about filing."""
        _, out = run("check", "--root", os.path.join(FIXTURES, "broken-parked-task"))
        self.assertNotIn("notes.md", out)
        self.assertEqual(out.count("PARKED TASK"), 1, out)

    def test_a_generated_index_that_no_longer_matches_its_tasks(self):
        """T-025. The one class where the defect was `check` itself: the fixture's task says
        `specified`, its generated region still says `proposed`, and until this landed the run
        printed `OK - 1 task(s)` at exit 0 — which is how T-009 lost an index edit unnoticed."""
        self.fails("broken-stale-index", "STALE INDEX", "run 'taskmd index'")


class AnOpenTaskMayNameWhatItWillProduce(unittest.TestCase):
    """T-089. The other half of the deliverables rule, and the half that had never been tested.

    `check` reported every declared path that did not exist, whatever the task's status, so a project
    that fills the field when it *plans* got a permanent complaint about work it had not started.
    This repository never saw it: its own habit is to leave `deliverables` empty until `implement`,
    which is a habit rather than a rule, and it is why the case survived to publication."""

    def test_an_open_task_declaring_a_path_that_does_not_exist_passes(self):
        code, out = run("check", "--root", os.path.join(FIXTURES, "planned-deliverable"))
        self.assertEqual(code, 0, out)
        self.assertNotIn("MISSING OUTPUT", out)

    def test_the_same_declaration_fails_once_the_task_closes(self):
        """The pair is the point — one fixture open, one closed, same missing path."""
        self.assertIn("out/report.md",
                      run("check", "--root", os.path.join(FIXTURES, "broken-deliverable"))[1])

    def test_a_cancelled_task_is_reported_like_any_other_closed_one(self):
        """T-090, and it pins a decision rather than a mechanism. `cancelled` is closed but did not
        close by producing an outcome, so this looks like the false positive T-089 removed and is
        not one: `deliverables` asserts production, and a task that produced nothing must stop
        claiming it did. The report is a stale record being caught.

        Without this test the next reader meets a `MISSING OUTPUT` on an abandoned task, recognises
        T-089's shape, and 'fixes' it back — which is why the decision needed a case in the suite
        and not only a paragraph.
        """
        code, out = run("check", "--root", os.path.join(FIXTURES, "broken-cancelled-deliverable"))
        self.assertEqual(code, 1, out)
        self.assertIn("MISSING OUTPUT", out)
        self.assertIn("out/report.md", out)

    def test_clearing_the_field_is_what_makes_it_quiet(self):
        """The other side of the same decision: the remedy is the record, not a config key. A copy
        of the fixture with `deliverables: []` passes, which is what makes the paragraph in the
        shipped config an instruction someone can follow rather than an assertion."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        source = os.path.join(FIXTURES, "broken-cancelled-deliverable", "tasks", "T-001-x.md")
        with io.open(source, encoding="utf-8") as handle:
            text = handle.read()
        self.assertIn("deliverables: [out/report.md]", text)
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  text.replace("deliverables: [out/report.md]", "deliverables: []", 1))
        code, out = run("check", "--root", tmp)
        self.assertEqual(code, 0, out)
        self.assertNotIn("MISSING OUTPUT", out)


class ADuplicateIsNeverSilent(unittest.TestCase):
    """T-062's real content. `check` reporting it is half the fix; the other half is that no
    command answers over a broken project without saying so.

    The failure this closes was not that `check` was wrong — it was that **nothing** was. A task
    vanished from every view, and the only way to find out was to notice it missing."""

    DUPES = os.path.join(FIXTURES, "broken-duplicate-id")

    def test_the_file_that_loads_is_the_same_one_every_time(self):
        """Which file wins used to be `os.walk`'s answer, so it could differ between machines.
        It is a collision either way — this only means a project gives the same answer twice."""
        for _ in range(3):
            code, out = run("list", "--root", self.DUPES)
            self.assertEqual(code, 0, out)
            self.assertIn("First file alphabetically", out)

    def test_an_unrelated_command_warns_on_stderr_and_still_answers(self):
        """The open question this settles: not refusal. R-17 is explicit that a problem is never
        raised "from inside a task the user is trying to finish", and a duplicate id is task
        content, not configuration — so `list` still answers, and stdout is untouched so a script
        cutting it sees exactly what it saw before. What changes is that stderr is no longer
        empty."""
        buffer = io.StringIO()
        stderr, sys.stderr = sys.stderr, buffer
        try:
            code, out = run("list", "--root", self.DUPES)
        finally:
            sys.stderr = stderr
        self.assertEqual(code, 0, out)
        self.assertIn("run 'taskmd check'", buffer.getvalue())
        self.assertNotIn("taskmd:", out)

    def test_check_itself_does_not_also_warn(self):
        """`check` lists the detail; a stderr line pointing at `check` would be it telling the
        user to run the command they are already running."""
        buffer = io.StringIO()
        stderr, sys.stderr = sys.stderr, buffer
        try:
            run("check", "--root", self.DUPES)
        finally:
            sys.stderr = stderr
        self.assertEqual("", buffer.getvalue())


class AViewOmitsAnUnusedColumnAndAContractDoesNot(unittest.TestCase):
    """T-070. The rule `index_block` already applied to edge columns, now applied to field columns
    — and deliberately **not** applied to the two machine forms of `list`.

    The distinction is the whole decision: `index` and `context` are read by a person or an agent
    and a column of dashes costs both for nothing, while a key vanishing from `--json` the moment a
    field falls out of use is a breaking change to a caller that did nothing wrong."""

    def project(self, folder, work_packages):
        """A project on the shipped default, whose tasks carry `work_package` or do not."""
        os.makedirs(os.path.join(folder, "tasks"))
        os.makedirs(os.path.join(folder, ".taskmd"))
        shutil.copy(os.path.join(PKG, "taskmd", "defaults", "config.md"),
                    os.path.join(folder, ".taskmd", "config.md"))
        for number, package in enumerate(work_packages, 1):
            cli.write(os.path.join(folder, "tasks", "T-00%d-x.md" % number),
                      "---\nid: T-00%d\ntitle: Task %d\ntype: deliverable\nstatus: proposed\n"
                      "phase: specify\nwork_package: %s\nowner: someone\n---\n\n# T-00%d\n"
                      % (number, number, package, number))
        return folder

    def test_a_field_no_task_uses_is_absent_from_both_views(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(os.path.join(tmp, "p"), ["none", "none"])
            code, out = run("context", "T-001", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("work_package", out)
            self.assertIn("owner someone", out)          # a used field is still shown
            run("index", "--root", root)
            index = cli.read(os.path.join(root, "tasks", "README.md"))
            self.assertNotIn("Work Package", index)

    def test_one_task_using_it_brings_the_column_back_with_nothing_switched_on(self):
        """§1 *Invisibility*: nobody edits a config to make a field they started using appear."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(os.path.join(tmp, "p"), ["none", "WP1"])
            code, out = run("context", "T-001", "--root", root)
            self.assertIn("work_package", out)
            run("index", "--root", root)
            self.assertIn("Work Package", cli.read(os.path.join(root, "tasks", "README.md")))

    def test_list_emits_every_configured_column_even_when_unused(self):
        """The contract half. Asserted rather than assumed — it is the criterion added with the
        maintainer's answer, and the one a later change is most likely to break by accident."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(os.path.join(tmp, "p"), ["none", "none"])
            code, out = run("list", "--json", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertIn("work_package", json.loads(out)[0])
            code, out = run("list", "--root", root)
            self.assertEqual(len(out.splitlines()[0].split("\t")),
                             2 + len(cli.load_schema(root).index_columns))


class NothingIsHardcoded(unittest.TestCase):
    """The CLI holds no field name, status value or id format of its own — it asks the schema."""

    ALT = os.path.join(FIXTURES, "alt-project")

    def test_it_reads_a_project_that_shares_no_vocabulary_with_the_default(self):
        code, out = run("context", "ISSUE-0002", "--root", self.ALT)
        self.assertEqual(code, 0, out)
        self.assertIn("state doing", out)      # not `status`
        self.assertIn("EPIC", out)             # not `parent`
        self.assertIn("DEPENDS ON", out)       # not `blocked_by`
        self.assertIn("SEE ALSO", out)         # not `related`
        for default in ("status ", "PARENT", "BLOCKED BY", "RELATED"):
            self.assertNotIn(default, out)

    def test_the_alt_project_is_clean(self):
        self.assertEqual(run("check", "--root", self.ALT)[0], 0)

    def test_the_blocked_status_is_whatever_the_project_calls_it(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, ".taskmd", "config.md"),
                  "---\nid_field: id\nid_prefix: W\nid_width: 2\ntitle_field: title\n"
                  "tasks_dir: work\nstatus_field: state\ndeliverables_field: none\n"
                  "blocked_status: stuck\nvalue_field: none\neffort_field: none\n"
                  "after_write: none\nopen_statuses: [live, stuck]\ncontext_fields: [state]\n"
                  "index_columns: [state]\n---\n\n## Edges\n\n| Field | Kind | Derives |\n"
                  "| :--- | :--- | :--- |\n| needs | dependency | feeds |\n\n"
                  "## Vocabularies\n\n| Field | Values |\n| :--- | :--- |\n"
                  "| state | live, stuck, gone |\n")
        cli.write(os.path.join(tmp, "work", "W01-x.md"),
                  "---\nid: W01\ntitle: Stuck on nothing\nstate: stuck\n---\n\n# W01\n")
        code, out = run("check", "--root", tmp)
        self.assertEqual(code, 1)
        self.assertIn("NO BLOCKER    W01 is 'stuck' with nothing in needs", out)


class Context(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)

    def task(self, tid, title, extra=""):
        path = os.path.join(self.tmp, "tasks", "%s-x.md" % tid)
        cli.write(path, "---\nid: %s\ntitle: %s\ntype: deliverable\nstatus: proposed\n"
                        "phase: specify\n%s---\n\n# %s\n" % (tid, title, extra, title))

    def test_a_soft_link_is_shown_from_the_end_that_does_not_store_it(self):
        """The interim tool could not do this: it showed only what a task literally stored, so
        half of every soft link was invisible depending on which end you opened (T-012)."""
        self.task("T-001", "Stores nothing")
        self.task("T-002", "Stores the link", "related: [T-001]\n")
        code, out = run("context", "T-001", "--root", self.tmp)
        self.assertEqual(code, 0)
        self.assertIn("RELATED", out)
        self.assertIn("T-002", out)

    def test_the_closing_line_never_names_a_phase_to_work(self):
        """R-6 and the second interim-tool limitation. A task whose status has moved past its
        phase used to be told to redo the phase it had just finished; the closing line now
        carries only derived state and issues no instruction."""
        self.task("T-001", "Planning finished",
                  "".join([]))
        path = os.path.join(self.tmp, "tasks", "T-001-x.md")
        cli.write(path, cli.read(path).replace("status: proposed", "status: planned"))
        code, out = run("context", "T-001", "--root", self.tmp)
        self.assertEqual(code, 0)
        closing = out.strip().splitlines()[-1]
        self.assertTrue(closing.startswith("STATE"), closing)
        self.assertNotIn("phase", closing)
        for word in ("work the", "next", "then", "read the file"):
            self.assertNotIn(word, closing.lower())
        # Both axes are still on screen, on the header line where they are stored.
        self.assertIn("status planned", out)
        self.assertIn("phase specify", out)

    def test_an_open_blocker_is_named_in_the_closing_line(self):
        self.task("T-001", "The blocker")
        self.task("T-002", "The blocked", "blocked_by: [T-001]\n")
        code, out = run("context", "T-002", "--root", self.tmp)
        self.assertIn("STATE  open, waiting on T-001", out)

    def test_a_closed_task_says_so(self):
        self.task("T-001", "Finished")
        path = os.path.join(self.tmp, "tasks", "T-001-x.md")
        cli.write(path, cli.read(path).replace("status: proposed", "status: done"))
        code, out = run("context", "T-001", "--root", self.tmp)
        self.assertIn("STATE  closed", out)

    def test_an_unknown_id_is_an_error_not_an_empty_report(self):
        self.task("T-001", "The only one")
        code, out = run("context", "T-404", "--root", self.tmp)
        self.assertEqual(code, 1)
        self.assertIn("No such task", out)


class Index(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)
        cli.write(os.path.join(self.tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: One\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# One\n")
        self.path = os.path.join(self.tmp, "tasks", "README.md")

    def test_hand_written_text_above_the_marker_survives_regeneration(self):
        cli.write(self.path, "# My index\n\nHand-written preamble worth keeping.\n")
        run("index", "--root", self.tmp)
        first = cli.read(self.path)
        self.assertIn("Hand-written preamble worth keeping.", first)
        self.assertIn(cli.BEGIN, first)

    def test_regenerating_twice_changes_nothing(self):
        run("index", "--root", self.tmp)
        first = cli.read(self.path)
        run("index", "--root", self.tmp)
        self.assertEqual(first, cli.read(self.path))

    def test_a_changed_task_shows_up_and_nothing_else_moves(self):
        run("index", "--root", self.tmp)
        before = cli.read(self.path)
        task = os.path.join(self.tmp, "tasks", "T-001-x.md")
        cli.write(task, cli.read(task).replace("status: proposed", "status: done"))
        run("index", "--root", self.tmp)
        after = cli.read(self.path)
        self.assertNotEqual(before, after)
        self.assertEqual(before.split(cli.BEGIN)[0], after.split(cli.BEGIN)[0])

    def test_an_edge_no_task_uses_gets_no_column(self):
        """Derived from the data, not configured: a project with no hierarchy should not read a
        column of dashes, and one that starts using it should not have to switch a column on."""
        run("index", "--root", self.tmp)
        self.assertNotIn("Parent", cli.read(self.path))
        cli.write(os.path.join(self.tmp, "tasks", "T-002-y.md"),
                  "---\nid: T-002\ntitle: Two\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\nparent: T-001\n---\n\n# Two\n")
        run("index", "--root", self.tmp)
        text = cli.read(self.path)
        self.assertIn("Parent", text)
        self.assertIn("Children", text)

    def dependent(self, tid, title, blocked_by, status="proposed"):
        cli.write(os.path.join(self.tmp, "tasks", "%s-x.md" % tid),
                  "---\nid: %s\ntitle: %s\ntype: deliverable\nstatus: %s\n"
                  "phase: specify\nblocked_by: [%s]\n---\n\n# %s\n"
                  % (tid, title, status, ", ".join(blocked_by), title))

    def close(self, tid):
        path = os.path.join(self.tmp, "tasks", "%s-x.md" % tid)
        cli.write(path, cli.read(path).replace("status: proposed", "status: done"))

    def index_row(self, tid):
        for line in cli.read(self.path).splitlines():
            if line.startswith("| [%s]" % tid):
                return line
        self.fail("no row for %s" % tid)

    def test_a_satisfied_blocker_leaves_the_cell_rather_than_reading_as_live(self):
        """T-111. `context` resolved the far end's status and `index` did not, so one surface said
        a task was startable while the other named a blocker that had closed the day before."""
        self.dependent("T-002", "Held by one that finished", ["T-001"])
        self.close("T-001")
        run("index", "--root", self.tmp)
        self.assertNotIn("T-001", self.index_row("T-002"))
        self.assertIn("no blocker outstanding", run("context", "T-002", "--root", self.tmp)[1])

    def test_one_closed_and_one_open_blocker_leaves_only_the_open_one(self):
        cli.write(os.path.join(self.tmp, "tasks", "T-003-x.md"),
                  "---\nid: T-003\ntitle: Three\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# Three\n")
        self.dependent("T-002", "Held by two", ["T-001", "T-003"])
        self.close("T-001")
        run("index", "--root", self.tmp)
        row = self.index_row("T-002")
        self.assertIn("T-003", row)
        self.assertNotIn("T-001", row)

    def test_a_project_whose_dependencies_are_all_satisfied_loses_the_column(self):
        """The column-in-use rule has to see the filtered view. Filtering only the cells would
        leave a column of dashes — the defect T-070 removed, one edge kind over."""
        self.dependent("T-002", "Held by one that finished", ["T-001"])
        run("index", "--root", self.tmp)
        self.assertIn("Blocked By", cli.read(self.path))

        # Closing the blocker satisfies one direction and not the other: nothing is held any more,
        # but finishing T-001 still releases T-002, which is open. The two resolve independently.
        self.close("T-001")
        run("index", "--root", self.tmp)
        text = cli.read(self.path)
        self.assertNotIn("Blocked By", text)
        self.assertIn("Blocks", text)

        self.close("T-002")
        run("index", "--root", self.tmp)
        self.assertNotIn("Blocks", cli.read(self.path))

    def test_the_derived_side_is_filtered_too(self):
        """`blocks` is not a key in `schema.edges` — a membership test against it answers "not a
        dependency" for the whole derived half, and a closed downstream task keeps overstating
        what finishing this one releases."""
        self.dependent("T-002", "Downstream, and finished", ["T-001"])
        self.dependent("T-003", "Downstream, still open", ["T-001"])
        self.close("T-002")
        run("index", "--root", self.tmp)
        row = self.index_row("T-001")
        self.assertIn("T-003", row)
        self.assertNotIn("T-002", row)

    def test_a_closed_parent_is_still_a_parent(self):
        """Out of scope on purpose: hierarchy and soft edges say nothing about being held."""
        cli.write(os.path.join(self.tmp, "tasks", "T-002-y.md"),
                  "---\nid: T-002\ntitle: Two\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\nparent: T-001\nrelated: [T-001]\n---\n\n# Two\n")
        self.close("T-001")
        run("index", "--root", self.tmp)
        row = self.index_row("T-002")
        self.assertIn("T-001", row)
        self.assertIn("Parent", cli.read(self.path))
        self.assertIn("Related", cli.read(self.path))

    def test_a_blocker_no_task_claims_is_still_shown(self):
        """It cannot be resolved to closed, and `check` reports it. Dropping it here would hide a
        broken edge from the artifact people read while the validator complains about it."""
        self.dependent("T-002", "Held by a ghost", ["T-404"])
        run("index", "--root", self.tmp)
        self.assertIn("T-404", self.index_row("T-002"))


class WritesTheSameBytesEverywhere(unittest.TestCase):
    """R-20. Only one platform is available here, so this proves the *mechanism*: nothing the
    tool writes carries a platform-dependent newline or separator. A run on macOS or Linux is
    what would close the remaining gap — recorded as an assumption in T-002."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)
        cli.write(os.path.join(self.tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: One\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# One\n")

    def test_the_generated_index_contains_no_carriage_returns(self):
        run("index", "--root", self.tmp)
        with open(os.path.join(self.tmp, "tasks", "README.md"), "rb") as fh:
            self.assertNotIn(b"\r\n", fh.read())

    def test_printed_paths_use_forward_slashes(self):
        code, out = run("context", "T-001", "--root", self.tmp)
        self.assertIn("tasks/T-001-x.md", out)
        self.assertNotIn("\\", out)

    def test_what_the_commands_print_carries_no_carriage_returns(self):
        """T-132. The two tests above cover the file and the separators; nothing covered the line
        ending of what is *printed*, and T-020 measured the gap — every console capture differed
        between Windows and Linux by `\\r` alone.

        This has to spawn a real process. `run()` above swaps `sys.stdout` for an `io.StringIO`,
        which has no `reconfigure`, so the line this protects never executes in-process and an
        assertion made through the helper would pass on the unfixed code."""
        env = dict(os.environ)
        env["PYTHONPATH"] = PKG
        env["PYTHONIOENCODING"] = "utf-8"
        for argv in (["check"], ["index"], ["context", "T-001"], ["list"], ["nosuchcommand"]):
            done = subprocess.Popen([sys.executable, "-m", "taskmd"] + argv
                                    + ["--root", self.tmp],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            out, err = done.communicate()
            self.assertNotIn(b"\r", out, "stdout of 'taskmd %s'" % " ".join(argv))
            self.assertNotIn(b"\r", err, "stderr of 'taskmd %s'" % " ".join(argv))


class ReportsASecondIndexOutsideTheMarkers(unittest.TestCase):
    """T-121. An adopting project has an old index generator by definition, and while both write the
    same file neither validator can see the other's block. The reporting project ran `check` twice
    over a `README.md` holding taskmd's generated table *and* a second complete copy of the same 56
    ids, and got `OK` both times.

    Every test here is paired: one that must fire and one that must stay quiet. A rule of this shape
    is worth nothing if only its silence has been observed."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)

    def task(self, number, body="", **fields):
        front = {"id": "T-%03d" % number, "title": "Task %d" % number, "type": "deliverable",
                 "status": "proposed", "phase": "specify"}
        front.update(fields)
        cli.write(os.path.join(self.tmp, "tasks", "T-%03d-x.md" % number),
                  "---\n%s\n---\n\n# T-%03d\n\n%s\n"
                  % ("\n".join("%s: %s" % kv for kv in front.items()), number, body))

    def check(self):
        return run("check", "--root", self.tmp)

    def test_a_second_table_of_every_id_is_reported(self):
        for n in (1, 2, 3, 4):
            self.task(n)
        cli.write(os.path.join(self.tmp, "docs", "backlog.md"),
                  "# Our own backlog\n\n| id | title |\n| :-- | :-- |\n"
                  + "".join("| T-%03d | Task %d |\n" % (n, n) for n in (1, 2, 3, 4)))
        code, out = self.check()
        self.assertIn("DUPLICATE INDEX", out)
        self.assertIn("docs/backlog.md", out)
        self.assertIn("4 known task ids", out)

    def test_it_is_advisory_and_moves_neither_the_exit_status_nor_the_count(self):
        """Criterion 2. A project may legitimately quote its own table, and a validator that fails
        on a legal state is one a project starts passing flags to — `CONFIG DRIFT`'s reasoning."""
        for n in (1, 2, 3, 4):
            self.task(n)
        clean_code, clean_out = self.check()
        cli.write(os.path.join(self.tmp, "docs", "backlog.md"),
                  "".join("- T-%03d\n" % n for n in (1, 2, 3, 4)))
        code, out = self.check()
        self.assertIn("DUPLICATE INDEX", out)
        self.assertEqual(clean_code, code)
        self.assertEqual(0, code)
        self.assertNotIn("problem(s)", out)
        self.assertIn("OK - ", out)

    def test_a_document_quoting_a_handful_of_ids_stays_quiet(self):
        for n in (1, 2, 3, 4):
            self.task(n)
        cli.write(os.path.join(self.tmp, "docs", "note.md"),
                  "See T-001 and T-002 for the background.\n")
        self.assertNotIn("DUPLICATE INDEX", self.check()[1])

    def test_a_small_project_of_tasks_linking_to_neighbours_stays_quiet(self):
        """The measured case, locked in. Q1 chose a majority partly because one "cannot be reached
        by a task file linking to its neighbours" — true at 132 tasks, arithmetic at three. This is
        the shape of `tests/fixtures/alt-project`, on which the first cut of the rule fired twice."""
        self.task(1, body="Nothing here records what it unblocks; that is derived from T-002.",
                  parent="T-003")
        self.task(2, parent="T-003", related="[T-001]")
        self.task(3, body="The umbrella. It does not list its children.")
        self.assertNotIn("DUPLICATE INDEX", self.check()[1])

    def test_the_discount_does_not_blind_it_to_a_table_inside_a_task_file(self):
        """The other side of that discount: a task file is forgiven the ids it *declares*, not the
        ids it lists. Paste the index into one and it still fires."""
        for n in (1, 2, 3, 4):
            self.task(n)
        self.task(5, body="".join("- T-%03d\n" % n for n in (1, 2, 3, 4)))
        out = self.check()[1]
        self.assertIn("DUPLICATE INDEX", out)
        self.assertIn("T-005-x.md", out)

    def test_the_generated_block_itself_is_not_a_duplicate_of_itself(self):
        """The index taskmd writes names every id there is. If the marked region were scanned, the
        rule would fire on its own output in every project that has ever run `index`."""
        for n in (1, 2, 3, 4):
            self.task(n)
        run("index", "--root", self.tmp)
        self.assertNotIn("DUPLICATE INDEX", self.check()[1])

    def test_the_reported_case_exactly(self):
        """The shape the adopting project actually had: taskmd's generated block between taskmd's
        markers, and a second complete table of the same ids below them, in the same file. `check`
        ran over that state twice and said `OK`."""
        for n in (1, 2, 3, 4):
            self.task(n)
        run("index", "--root", self.tmp)
        index = os.path.join(self.tmp, "tasks", "README.md")
        with open(index, encoding="utf-8") as fh:
            generated = fh.read()
        self.assertIn(cli.END, generated)
        cli.write(index, generated + "\n## Our own table\n\n"
                  + "".join("- T-%03d Task %d\n" % (n, n) for n in (1, 2, 3, 4)))
        code, out = self.check()
        self.assertIn("DUPLICATE INDEX", out)
        self.assertIn("tasks/README.md", out)
        self.assertEqual(0, code)


class RunsOnACloneWithNoConfiguration(unittest.TestCase):
    """R-20 again, from the other side: no `.taskmd/`, no dependencies, no path editing."""

    def test_a_bare_folder_of_tasks_works(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: Only\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# Only\n")
        self.assertFalse(os.path.exists(os.path.join(tmp, ".taskmd")))
        self.assertEqual(run("check", "--root", tmp)[0], 0)
        self.assertEqual(run("index", "--root", tmp)[0], 0)
        self.assertEqual(run("context", "T-001", "--root", tmp)[0], 0)

    def test_a_task_typed_the_way_the_method_words_it_validates(self):
        """T-088. METHOD §5 opens "An audit is a **task type**, not a phase", and until this the
        shipped vocabulary had no `audit` — so writing the thing the method names failed `check`.

        Built rather than read: the point is that the word survives the round trip through a real
        project with no config, not that it appears in a table."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: Audit the whole thing\ntype: audit\nstatus: proposed\n"
                  "phase: specify\n---\n\n# Audit the whole thing\n")
        code, out = run("check", "--root", tmp)
        self.assertEqual(code, 0, out)
        self.assertNotIn("VOCABULARY", out)


class AbsentTasksDirIsReportedAtSetup(unittest.TestCase):
    """T-019: a tasks_dir that is not there is a config error, not a project with no tasks.

    Three cases share one code path — a misspelled value, a project that has not created the
    folder yet, and a folder that exists but is empty. The first two are errors however the value
    arrived; the third is legal and must stay so. The middle case has no committed fixture because
    it cannot have one: a project with neither a config nor a tasks folder is an empty directory,
    and git stores no such thing.
    """

    def all_three_commands_refuse(self, root, needle):
        for argv in (("check",), ("index",), ("context", "T-001")):
            code, out = run(*(argv + ("--root", root)))
            self.assertEqual(code, 2, "%s exited %d:\n%s" % (argv[0], code, out))
            self.assertIn("CONFIG ERROR", out)
            self.assertIn("tasks_dir", out)
            self.assertIn(needle, out)
            self.assertNotIn("No such task", out)

    def test_a_misspelled_value_beside_the_real_folder(self):
        root = os.path.join(FIXTURES, "broken-tasks-dir")
        self.all_three_commands_refuse(root, "'taks'")
        self.assertFalse(os.path.isdir(os.path.join(root, "taks")),
                         "index created the folder named by the typo")

    def test_a_project_that_has_not_created_the_folder_yet(self):
        """The shipped default names `tasks`; inheriting the value is not an excuse for it to
        be missing, or `check` would go on exiting 0 on a project it never read."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        self.all_three_commands_refuse(tmp, "shipped default")
        self.assertFalse(os.path.isdir(os.path.join(tmp, "tasks")),
                         "index created the folder instead of reporting it")

    def test_a_name_that_is_taken_by_a_file_says_so(self):
        """T-024. The neighbour case T-019's plan had not tested: `tasks` is *there*, as a file.

        The rejection was always right — this is not a usable tasks folder — but the sentence
        denied the existence of a name the reader can see and then advised creating it, which is a
        remedy that cannot be followed.
        """
        root = os.path.join(FIXTURES, "broken-tasks-dir-file")
        self.all_three_commands_refuse(root, "not a folder")
        for argv in (("check",), ("index",)):
            out = run(*(argv + ("--root", root)))[1]
            self.assertNotIn("no such folder", out)
            self.assertNotIn("Create it", out)
        self.assertTrue(os.path.isfile(os.path.join(root, "tasks")),
                        "the fixture's whole defect is that this name is a file")

    def test_the_inherited_default_gets_the_same_correction(self):
        """A project with no config of its own is the *likelier* half of this case, since it is the
        shipped `tasks` value that collides with a name already in use — so its longer hint has to
        move too, or the fix covers only the half the report happened to arrive from."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, "tasks"), "not a folder\n")
        self.all_three_commands_refuse(tmp, "not a folder")
        out = run("check", "--root", tmp)[1]
        self.assertIn("shipped default", out)
        self.assertIn("rename or remove that file", out)
        self.assertNotIn("create the folder", out)

    def test_a_tasks_dir_naming_the_project_root_is_refused(self):
        """T-078. The root is a directory, so `isdir` passed it and the damage was elsewhere:
        `is_project` asks whether `<folder>/<tasks_dir>` is a directory, which with a `tasks_dir`
        of `.` is true of every folder there is. Every subdirectory then reads as a nested project
        and `check` exits over a tree it never walked."""
        root = os.path.join(FIXTURES, "broken-tasks-dir-root")
        self.all_three_commands_refuse(root, "which is the project root")
        out = run("check", "--root", root)[1]
        self.assertNotIn("BROKEN LINK", out,
                         "the config must be refused before anything is walked")

    def test_every_spelling_of_the_root_gets_the_same_answer(self):
        """A rejection one form escapes is not a rejection, so the test is path equality rather
        than a list of spellings — including a value that reaches the root by going down and back
        up, which no enumeration of dots would have caught."""
        with io.open(os.path.join(PKG, "taskmd", "defaults", "config.md"),
                     encoding="utf-8") as handle:
            shipped = handle.read()
        for value in (".", "./", "sub/..", "<root>"):
            tmp = tempfile.mkdtemp()
            self.addCleanup(shutil.rmtree, tmp)
            os.makedirs(os.path.join(tmp, "sub"))
            written = tmp if value == "<root>" else value
            cli.write(os.path.join(tmp, ".taskmd", "config.md"),
                      shipped.replace("tasks_dir: tasks", "tasks_dir: " + written, 1))
            with self.subTest(tasks_dir=value):
                code, out = run("check", "--root", tmp)
                self.assertEqual(code, 2, out)
                self.assertIn("which is the project root", out)

    def test_a_folder_that_exists_but_is_empty_stays_legal(self):
        """A new project with nothing in it yet is not an error — the distinction is that the
        folder is absent, not that it holds no tasks."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        os.makedirs(os.path.join(tmp, "tasks"))
        self.assertEqual(run("check", "--root", tmp)[0], 0)
        self.assertEqual(run("index", "--root", tmp)[0], 0)


class Usage(unittest.TestCase):

    def test_no_command_explains_every_command_there_is(self):
        """T-071. The set is **derived** from `cli.COMMANDS`, not written here.

        It used to be the written triple `("context", "index", "check")` — the name said *the
        three* — so `list` was absent from the assertion for as long as it had existed, and a
        regression that dropped it from the usage line would have passed. Deriving it is the same
        treatment the sibling test below already gives the command *name*: two things that must
        agree, instead of three that can drift."""
        code, out = run()
        self.assertEqual(code, 2)
        self.assertTrue(cli.COMMANDS, "no commands to assert; this test would prove nothing")
        for command in sorted(cli.COMMANDS):
            self.assertIn(command, out, "usage line omits %r: %r" % (command, out))

    def test_a_root_that_does_not_exist_is_reported(self):
        code, out = run("check", "--root", os.path.join(ROOT, "no-such-folder"))
        self.assertEqual(code, 2)
        self.assertIn("No such directory", out)

    def test_every_usage_line_names_the_command_the_skill_names(self):
        """T-055. What this pins is not the word `taskmd` but the property T-054 found broken: the
        tool and the skill naming different commands, so the advice printed to someone already stuck
        is advice they cannot take. The expected name is therefore read out of SKILL.md rather than
        written here — two copies that must agree, instead of three that can drift."""
        skill = os.path.join(PKG, "SKILL.md")
        with io.open(skill, encoding="utf-8") as handle:
            block = re.search(r"```bash\n([^\n]+)\n", handle.read())
        self.assertIsNotNone(block, "SKILL.md no longer opens its first command in a bash block")
        named = block.group(1).split()[0]

        for label, out in (("no command", run()[1]),
                           ("context with no id", run("context", "--root", ROOT)[1])):
            self.assertTrue(out.startswith("usage: "), "%s: %r" % (label, out))
            self.assertEqual(named, out[len("usage: "):].split()[0], "%s: %r" % (label, out))

    def test_every_command_rejects_an_argument_it_does_not_understand(self):
        """T-029, raised as F-3 by the T-026 audit. Three of the four commands took an `args`
        parameter and never read it past the first element, so a mistyped flag was discarded in
        silence and the command reported success.

        The set is **derived** from `cli.COMMANDS` for the reason T-071 gives: a written list is one
        that stops covering a command the moment one is added. An unknown *flag* is the probe that
        is unknown to all four alike — an unknown positional would be a valid id to `context`.

        The probe carries a value because `list` used to report an unknown flag as *needing a
        value* when it had none, checking the shape before the name. T-113 reversed that, so the
        value is no longer what makes this pass — `test_a_rejection_names_no_path` below runs the
        same four commands without one. It is kept because a probe with a value is the shape the
        other three commands must refuse too, and dropping it would narrow what this asserts."""
        self.assertTrue(cli.COMMANDS, "no commands to assert; this test would prove nothing")
        for command in sorted(cli.COMMANDS):
            code, out = run(command, "--definitely-not-a-flag", "value", "--root", ROOT)
            self.assertEqual(code, 2, "%s accepted it: %r" % (command, out))
            self.assertTrue("usage:" in out or "accepts:" in out,
                            "%s refused without naming what it takes: %r" % (command, out))

    def test_index_writes_nothing_before_rejecting(self):
        """The sharp case. `index nonsense --wat` performed the write and exited 0, so a user's
        evidence that their flag had done something was the same output as if it had."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: One\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# One\n")
        path = os.path.join(tmp, "tasks", "README.md")

        code, out = run("index", "nonsense", "--wat", "--root", tmp)
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(path), "the rejected call still wrote the index")
        self.assertNotIn("Wrote", out)

        # The same invocation without the junk does write — so what the assertion above pins is the
        # rejection, not a project that could not have produced an index anyway.
        self.assertEqual(run("index", "--root", tmp)[0], 0)
        self.assertTrue(os.path.exists(path))

    def test_asking_what_the_tool_does_is_not_misuse(self):
        """It printed the right line and exited 2. The intended caller is an agent working out the
        surface, and the conventional probe told it the tool had failed."""
        for args in (("--help",), ("-h",), ("check", "--help"), ("context", "--help")):
            code, out = run(*args)
            self.assertEqual(code, 0, "%r: %r" % (args, out))
            self.assertEqual(cli.usage_line(), out.strip(), "%r" % (args,))

    def test_a_rejection_names_no_path(self):
        """R-20. The same bytes on every platform, which a path could not be — and the reader of
        this line is being told what the tool accepts, not where it is installed."""
        for command in sorted(cli.COMMANDS):
            out = run(command, "--definitely-not-a-flag", "--root", ROOT)[1]
            self.assertNotIn("\\", out)
            self.assertNotIn("/", out)


class ListSaysWhatItAccepts(unittest.TestCase):
    """T-144. `list --help` answered with the top-level usage line, so the four options that are code
    and the filters that are this project's configuration were reachable only by reading `SKILL.md`
    or this package's source. The 2026-08-07 ruling against per-command help (T-029) was narrowed to
    this one command, because it is the only one whose options that line does not state."""

    def printed(self):
        code, out = run("list", "--help", "--root", ROOT)
        self.assertEqual(code, 0, out)
        return out

    def test_every_option_it_prints_is_one_the_parser_takes(self):
        """One direction. A help line naming a flag the parser rejects is worse than no help: the
        caller it exists for cannot tell a stale document from its own mistake."""
        schema = cli.load_schema(ROOT)
        for flag in sorted(set(re.findall(r"--[a-z_][a-z_-]*", self.printed()))):
            if flag == "--root":
                continue                # `main`'s, stripped before `list` sees an argument
            # Alone rather than with a value: a switch given one answers `unexpected argument`,
            # which is a true rejection of the value and says nothing about the flag.
            problem = cli.parse_filters(schema, [flag])[1] or ""
            self.assertNotIn("unknown filter", problem, flag)

    def test_every_option_the_parser_takes_is_printed(self):
        """The other direction, and the one that rots quietly: a flag added to the parser and not to
        the help is invisible to exactly the caller this was built for. Both sources are read, since
        the options are code and the filters are the project's config."""
        out = self.printed()
        for row in cli.LIST_OPTIONS:
            self.assertIn(row[0], out)
        for name in cli.filter_names(cli.load_schema(ROOT)):
            self.assertIn("--" + name, out)

    def test_the_parser_carries_no_option_name_of_its_own(self):
        """What makes the two tests above valid. They read `LIST_OPTIONS` as if it were the parser's
        accepted set, which it is only while the parser has no flag written beside it — a branch
        added by hand would be accepted, unprinted, and invisible to both. A placeholder such as
        `--<field>` inside a sentence is not an option name and does not match."""
        source = inspect.getsource(cli.parse_filters)
        self.assertEqual([], re.findall(r"""["']--[a-z_]""", source), source)

    def test_it_adds_to_the_top_level_line_rather_than_replacing_it(self):
        """The superset rule. Three commands answer this probe with the top-level line alone, so an
        agent that probed one of them first must not have been told anything `list` contradicts."""
        self.assertIn(cli.usage_line(), self.printed())
        for command in ("check", "index", "context"):
            self.assertEqual(cli.usage_line(), run(command, "--help")[1].strip(), command)

    def test_it_answers_outside_a_project_too(self):
        """Asking a tool what it does must not become conditional on standing in the right
        directory. The filters need a config to name; the two usage lines do not."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        code, out = run("list", "--help", "--root", tmp)
        self.assertEqual(code, 0, out)
        self.assertIn(cli.usage_line(), out)
        self.assertIn("--limit N", out)

    def test_it_writes_nothing(self):
        """In a project with no index yet, so a call that wrote would leave one behind rather than
        matching a file that was already there."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: One\ntype: deliverable\nstatus: proposed\n"
                  "phase: specify\n---\n\n# One\n")

        def tree():
            return sorted((p, os.path.getsize(p))
                          for p in glob.glob(os.path.join(tmp, "**"), recursive=True))

        before = tree()
        self.assertEqual(run("list", "--help", "--root", tmp)[0], 0)
        self.assertEqual(before, tree())


class CheckReportsWhatItExamined(unittest.TestCase):
    """T-095. The summary said what passed and not what was looked at, so `no broken links` over
    zero links read exactly like `no broken links` over a thousand.

    This project had already written the rule — judge a run by the file count, not by its silence
    (T-034, T-080) — and aimed it at a command that printed no file count. The reporting sibling had
    been bitten twice: a summary reading `0 broken` while two documents the tool pointed at were
    missing, and later while six pointers had dropped out of scope."""

    NOUNS = ("task", "field value", "reference", "dependency edge", "declared output",
             "index file", "document", "link")

    def counted(self, out, noun):
        found = re.search(r"(\d+) %s\(s\)" % re.escape(noun), out)
        self.assertIsNotNone(found, "no denominator for %r in %r" % (noun, out))
        return int(found.group(1))

    def test_the_passing_summary_carries_every_denominator(self):
        code, out = run("check", "--root", ROOT)
        self.assertEqual(code, 0, out)
        for noun in self.NOUNS:
            self.counted(out, noun)

    def test_the_failing_summary_carries_them_too(self):
        """A narrowed scan hides behind an unrelated problem exactly as well as behind a pass, so
        the branch that reports problems needs the same numbers as the one that does not."""
        code, out = run("check", "--root", os.path.join(FIXTURES, "broken-link"))
        self.assertEqual(code, 1, out)
        self.assertIn("1 problem(s) - ", out)
        for noun in self.NOUNS:
            self.counted(out, noun)

    def test_a_narrowed_scan_shows_a_smaller_number(self):
        """The failure the task exists to make visible, reproduced rather than described: one scan
        narrowed on the same tree, **both runs still OK at exit 0**, and the count is the only thing
        that says anything happened. Before this landed the two lines were byte-identical.

        It runs against this repository rather than a fixture, and that is not laziness: the first
        draft used `nested-at-root`, which scans exactly one document, so halving its scan produced
        the same number and the test failed for the right reason on its first run. A test of a
        shrinking denominator needs something big enough to shrink."""
        _, wide = run("check", "--root", ROOT)
        full = cli.markdown_files
        try:
            cli.markdown_files = lambda r, s: list(full(r, s))[:1]
            _, narrow = run("check", "--root", ROOT)
        finally:
            cli.markdown_files = full

        self.assertIn("OK - ", wide)
        self.assertIn("OK - ", narrow)
        self.assertGreater(self.counted(wide, "document"), self.counted(narrow, "document"))

    def test_a_project_with_no_generated_index_says_so(self):
        """`check_stale_index` returns early when there is nothing generated, which is right —
        but reporting nothing and comparing nothing used to be the same output."""
        _, out = run("check", "--root", os.path.join(FIXTURES, "broken-dangling"))
        self.assertEqual(self.counted(out, "index file"), 0)

    def test_a_check_that_records_no_denominator_is_not_silent(self):
        """What keeps the class list derived from the checks that ran instead of hand-maintained.
        A check added without a return fails at its call site, rather than leaving the summary
        claiming a coverage the run never had — which is this task's own bug, one level up."""
        original = cli.check_vocabularies
        try:
            cli.check_vocabularies = lambda *args: None
            self.assertRaises(TypeError, run, "check", "--root", ROOT)
        finally:
            cli.check_vocabularies = original

    def test_a_narrower_walk_of_a_counted_class_has_its_own_number(self):
        """T-096. `check_cycles` first reported its dependency edges as `reference`s, on the argument
        that the wider walk would witness any narrowing. It does not: reclassifying an edge field
        from `dependency` to `soft` leaves it in `task.edges`, so the reference count holds steady
        while cycle-checking drops to nothing — and the two summaries came out byte-identical, which
        is the failure T-095 exists to remove, surviving inside T-095's own fix."""
        with tempfile.TemporaryDirectory() as tmp:
            root, config = os.path.join(tmp, "p"), None
            os.makedirs(os.path.join(root, "tasks"))
            os.makedirs(os.path.join(root, ".taskmd"))
            config = os.path.join(root, ".taskmd", "config.md")
            shutil.copy(os.path.join(PKG, "taskmd", "defaults", "config.md"), config)
            cli.write(os.path.join(root, "tasks", "T-001-x.md"),
                      "---\nid: T-001\ntitle: One\ntype: fix\nstatus: proposed\nphase: specify\n"
                      "blocked_by: []\nowner: someone\n---\n\n# T-001\n")
            cli.write(os.path.join(root, "tasks", "T-002-x.md"),
                      "---\nid: T-002\ntitle: Two\ntype: fix\nstatus: proposed\nphase: specify\n"
                      "blocked_by: [T-001]\nowner: someone\n---\n\n# T-002\n")

            _, before = run("check", "--root", root)
            with io.open(config, encoding="utf-8") as handle:
                text = handle.read()
            cli.write(config, text.replace("| blocked_by | dependency | blocks |",
                                           "| blocked_by | soft | - |"))
            _, after = run("check", "--root", root)

            self.assertEqual(self.counted(before, "reference"),
                             self.counted(after, "reference"),
                             "the edge did not leave the graph, so this must not move")
            self.assertGreater(self.counted(before, "dependency edge"),
                               self.counted(after, "dependency edge"))

    def test_the_caveat_names_what_check_cannot_decide(self):
        """A validator that passes silently is read as an endorsement. It prints on the passing
        path only — a failing run is not being read as one."""
        _, passing = run("check", "--root", ROOT)
        _, failing = run("check", "--root", os.path.join(FIXTURES, "broken-link"))
        self.assertIn("structure and references only", passing)
        self.assertNotIn("structure and references only", failing)


def git_is_available():
    try:
        done = subprocess.Popen(["git", "--version"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        done.communicate()
    except OSError:
        return False
    return done.returncode == 0


GIT = git_is_available()


class ScratchProject(unittest.TestCase):
    """A throwaway project on disk, because these two questions are about files and `.gitignore`
    rather than about task shape — a fixture committed to this repository would be governed by
    *this* repository's ignore rules, which is the thing under test."""

    def project(self, tmp, documents):
        root = os.path.join(tmp, "p")
        os.makedirs(os.path.join(root, "tasks"))
        os.makedirs(os.path.join(root, ".taskmd"))
        shutil.copy(os.path.join(PKG, "taskmd", "defaults", "config.md"),
                    os.path.join(root, ".taskmd", "config.md"))
        cli.write(os.path.join(root, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: One\ntype: fix\nstatus: proposed\nphase: specify\n"
                  "blocked_by: []\nowner: someone\n---\n\n# T-001\n")
        for name, text in sorted(documents.items()):
            cli.write(os.path.join(root, name.replace("/", os.sep)), text)
        return root

    def git(self, root, *argv):
        done = subprocess.Popen(("git",) + argv, cwd=root,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = done.communicate()[0]
        self.assertEqual(done.returncode, 0, out)

    def documents(self, out):
        found = re.search(r"(\d+) document\(s\)", out)
        self.assertIsNotNone(found, out)
        return int(found.group(1))


class CheckAnswersTheQuestionAFreshCloneWouldAsk(ScratchProject):
    """T-094. `check` walked every `.md` in the tree, while the pre-publish grep standing next to it
    in `CLAUDE.md` is built on `git ls-files --cached --others --exclude-standard` *precisely* so it
    sees what a push would send. Two checks over one tree answering different questions, with nothing
    saying which — so a project that quarantines machine-local documents (R-23) was handed failures
    no reader of the published repository could ever encounter."""

    DEAD = {".gitignore": "private/\n",
            "private/notes.md": "A [dead one](../nowhere.md) nobody can reach.\n"}

    @unittest.skipUnless(GIT, "git is not available")
    def test_a_gitignored_document_is_not_read_and_the_exclusion_is_counted(self):
        """Both halves of the flag combination, in one run each. `--others --exclude-standard` is
        what makes an uncommitted project work at all; adding `--cached` must not change the answer
        once the same files are staged. T-034 is the reason both are asserted rather than the first:
        the shorter form was silently blind to exactly the files a session had just created."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, self.DEAD)
            self.git(root, "init")
            code, staged_none = run("check", "--root", root)
            self.assertEqual(code, 0, staged_none)
            self.assertIn("1 document(s) not read: a clone would not receive them", staged_none)
            self.assertNotIn("BROKEN LINK", staged_none)

            self.git(root, "add", "-A")
            code, staged_all = run("check", "--root", root)
            self.assertEqual(code, 0, staged_all)
            self.assertEqual(self.documents(staged_none), self.documents(staged_all))

    def test_the_same_project_without_git_reads_everything_and_says_so(self):
        """The other way round, which is what makes the run above evidence rather than a tautology —
        and the answer for a project with no version control at all, of which there is one among the
        projects onboarded on 2026-08-09. Degrading to the old behaviour is the degradation; going
        silent, or failing, would not be."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, self.DEAD)
            code, out = run("check", "--root", root)
            self.assertEqual(code, 1, out)
            self.assertIn("BROKEN LINK", out)
            self.assertIn("private/notes.md", out)
            self.assertIn("no git here, so .gitignore was not consulted", out)

    @unittest.skipUnless(GIT, "git is not available")
    def test_a_published_document_pointing_at_a_gitignored_file_is_reported(self):
        """**This reverses T-094**, which decided the target side would keep answering only "is
        this file here?" on the grounds that reporting the pointer would make the quarantine
        convention unrepresentable. T-097 measured that claim over this repository: every reference
        to its own quarantined file is a bare path in prose — the class T-092 put out of scope — and
        the strict rule raised no file-level alarm anywhere. The exemption was protecting a use of
        links that nobody makes. Reversed by the maintainer on 2026-08-11.

        Not `BROKEN LINK`: the file *is* here, which is a different fact and a different fix."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {".gitignore": "private/\n",
                                      "private/local.md": "Local only.\n",
                                      "docs/guide.md": "See [the local note](../private/local.md).\n"})
            self.git(root, "init")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 1, out)
            self.assertNotIn("BROKEN LINK", out)
            self.assertIn("IGNORED LINK  docs/guide.md -> ../private/local.md is here but no clone "
                          "receives it, so the link resolves for you and 404s for every reader", out)

    @unittest.skipUnless(GIT, "git is not available")
    def test_a_link_to_a_directory_is_not_reported(self):
        """The only false-alarm shape the rule has, and the one that would have made it useless:
        `git ls-files` lists files, so **no** directory is in the visible set, published or not.
        All twelve alarms T-097's probe raised over this repository were this. A published folder
        and a gitignored one are both asserted, because exempting directories has to be the reason
        rather than the published set happening to contain the first."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {".gitignore": "private/\n",
                                      "private/local.md": "Local only.\n",
                                      "docs/here.md": "Shipped.\n",
                                      "docs/guide.md": "[Shipped folder](.) and "
                                                       "[a quarantined one](../private).\n"})
            self.git(root, "init")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("IGNORED LINK", out)

    @unittest.skipUnless(GIT, "git is not available")
    def test_an_ordinary_published_link_is_not_reported(self):
        """The rule fires on membership of a set, so a rule that had the test inverted would look
        identical on a passing tree and report every link on a real one."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {"docs/here.md": "Shipped.\n",
                                      "docs/guide.md": "See [the note](./here.md).\n"})
            self.git(root, "init")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("IGNORED LINK", out)

    def test_without_git_the_class_cannot_be_claimed_at_all(self):
        """No `--skipUnless`: this is the branch where git is absent, and it must hold on a machine
        that has none. With no visible set there is no such thing as "no clone receives it", and
        guessing would report every link in a project that simply is not in version control."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {"private/local.md": "Local only.\n",
                                      "docs/guide.md": "See [the local note](../private/local.md).\n"})
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("IGNORED LINK", out)
            self.assertIn("no git here, so .gitignore was not consulted", out)

    @unittest.skipUnless(GIT, "git is not available")
    def test_the_scope_line_is_printed_on_a_failing_run_too(self):
        """A scan narrowed by an exclusion hides behind an unrelated problem exactly as well as
        behind a pass — which is T-095's finding, arriving at the mechanism T-094 added."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, dict(self.DEAD, **{
                "docs/guide.md": "A [real problem](./gone.md).\n"}))
            self.git(root, "init")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 1, out)
            self.assertIn("1 problem(s) - ", out)
            self.assertIn("1 document(s) not read", out)


class ABarePathInProseIsNotAReference(ScratchProject):
    """T-092. Decided **out**, and this pins the decision so the documentation cannot drift away
    from the behaviour it describes.

    It was decided by measurement rather than by argument. Turned on over this repository with the
    reporting project's own rule — a token is a pointer when its first segment names a real
    directory here — `check` examined 683 bare paths and reported 237, of which 235 sat in task
    records that correctly described a tree since moved, and the remaining two were a config naming
    where the live handoff will go and frozen prior art citing its original project's layout. No
    defect among them. `CLAUDE.md` had already settled the trade for the leak check: a check that
    cries wolf gets ignored, which is worse than a narrow one."""

    def test_a_dead_path_written_as_prose_is_not_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {
                "docs/guide.md": "The generator writes tasks/gone.md, which is not there.\n"})
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("gone.md", out)

    def test_the_same_target_as_a_markdown_link_is_reported(self):
        """The boundary from the other side: nothing about the target changed, only how it was
        written. Without this the test above would pass just as well if links had stopped working."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {
                "docs/guide.md": "The generator writes [tasks/gone.md](../tasks/gone.md).\n"})
            code, out = run("check", "--root", root)
            self.assertEqual(code, 1, out)
            self.assertIn("BROKEN LINK", out)

    def test_the_readme_tells_an_adopter_what_is_not_covered(self):
        """The gap's cost falls on adopters, not here — a project retiring its own checker has to be
        able to read what it is giving up. Asserted against the shipped front door rather than
        trusted, because a documented gap that quietly loses its documentation is the silent loss
        T-092 was raised about, one level up."""
        with io.open(os.path.join(ROOT, "README.md"), encoding="utf-8") as handle:
            readme = handle.read()
        self.assertIn("Markdown link syntax", readme)
        self.assertIn("T-092", readme)


class ATemplateIsCountedRatherThanInferred(ScratchProject):
    """T-101, the half that is deliberately **not** a failure.

    *A project with no template is a normal project* — the binding says so, and that stays true. But
    before this, a project could not be told it had none; it could only find that it had none, by
    running the listing and reading nothing. The count says it, without making a legal state fail.
    """

    TEMPLATE = ("---\nid: T-NNN\ntitle: <one line>\ntype: fix\nstatus: proposed\n"
                "phase: specify\nblocked_by: []\nowner: someone\n---\n\n# T-NNN\n")

    def counted(self, out):
        found = re.search(r"(\d+) template\(s\)", out)
        self.assertIsNotNone(found, out)
        return int(found.group(1))

    def test_a_project_with_none_is_told_so_by_a_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.project(tmp, {}))
            self.assertEqual(code, 0, out)
            self.assertEqual(self.counted(out), 0)

    def test_a_compliant_template_is_counted_and_not_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {"tasks/_task-template.md": self.TEMPLATE})
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertEqual(self.counted(out), 1)
            self.assertNotIn("TEMPLATE UNREACHABLE", out)

    def test_a_file_in_a_hidden_folder_that_is_not_a_template_is_left_alone(self):
        """The rule is the placeholder id, not the folder. A project's own notes live there too,
        and reporting them would make the class the noise it was raised to remove."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {"tasks/_notes/scratch.md": "Just notes.\n"})
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertEqual(self.counted(out), 0)

    def test_this_repository_carries_reachable_templates(self):
        """The live case, and the one that would have broken if the rule keyed on the folder: both
        templates here sit directly in `tasks/` since T-076."""
        code, out = run("check", "--root", ROOT)
        self.assertEqual(code, 0, out)
        self.assertGreater(self.counted(out), 0)
        self.assertNotIn("TEMPLATE UNREACHABLE", out)


class APinnedConfigIsToldWhenTheDefaultMovesOn(ScratchProject):
    """T-100. A config replaces the shipped default rather than merging with it, so a project that
    copied one and stopped looking cannot see a value added afterwards.

    That is not hypothetical: the reporting project copied the default the day before `audit`
    joined the `type` row, could not see the change, and raised work to fix a defect that had
    already stopped existing. These tests reconstruct that file's two states.

    The half that needed deciding is what is *not* reported. A configured project differs from the
    default in every way it chose to, and reporting choices would make the line noise on its first
    run — so `test_a_choice_is_not_drift` and `test_a_deleted_row_is_left_alone` carry as much of
    the rule as the positive case does.
    """

    TYPE = "| type | analysis, decision, deliverable, research, fix, admin, audit |"
    STATUS = "| status | proposed, specified, planned, in_progress, blocked, review, done, cancelled |"
    OPEN = "open_statuses: [proposed, specified, planned, in_progress, blocked, review]"

    def edit(self, root, before, after):
        path = os.path.join(root, ".taskmd", "config.md")
        with io.open(path, encoding="utf-8") as handle:
            text = handle.read()
        self.assertIn(before, text, "the shipped default no longer contains this row")
        cli.write(path, text.replace(before, after, 1))
        return root

    def pinned(self, tmp, before=None, after=None):
        root = self.project(tmp, {})
        if before is not None:
            self.edit(root, before, after)
        return root

    def restatused(self, root, value):
        """Keep the scratch task legal when the `status` row itself is what was replaced.

        Otherwise the run reports a vocabulary problem and the drift line is being read off a
        failing check — which is the one output these tests must not be coupled to.
        """
        path = os.path.join(root, "tasks", "T-001-x.md")
        with io.open(path, encoding="utf-8") as handle:
            text = handle.read()
        cli.write(path, text.replace("status: proposed", "status: %s" % value, 1))
        return root

    def test_a_row_missing_a_shipped_value_is_named(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.pinned(tmp, self.TYPE, self.TYPE.replace(", audit", ""))
            code, out = run("check", "--root", root)
            self.assertIn("CONFIG DRIFT", out)
            self.assertIn("type:", out)
            self.assertIn("'audit'", out)

    def test_it_is_advisory_and_does_not_move_the_exit_status(self):
        """The whole of the decision: pinning is legal, so a validator that failed on it is one a
        project starts passing flags to."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.pinned(tmp, self.TYPE, self.TYPE.replace(", audit", ""))
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertIn("OK -", out)
            self.assertNotIn("problem(s)", out)

    def test_a_current_copy_says_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.pinned(tmp))
            self.assertEqual(code, 0, out)
            self.assertNotIn("CONFIG DRIFT", out)

    def test_a_choice_is_not_drift(self):
        """Extra values and extra rows are what a config exists to express."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.pinned(tmp, self.TYPE,
                               self.TYPE.replace(" |", ", chore |")
                               + "\n| work_package | WP1, WP2, none |")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("CONFIG DRIFT", out)

    def test_a_wholly_replaced_row_is_not_behind(self):
        """T-123. The commonest way to adopt: keep taskmd's field names, bring the backend's values.

        `open`/`closed` is what an issue tracker gives you, and the row shares nothing with the
        shipped one — so there is no value it can be *behind* on, and the line it used to print
        named all eight shipped statuses at a project deliberately using none of them.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = self.pinned(tmp, self.STATUS, "| status | open, closed |")
            self.edit(root, self.OPEN, "open_statuses: [open]")
            self.edit(root, "blocked_status: blocked", "blocked_status: none")
            self.restatused(root, "open")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("CONFIG DRIFT", out)

    def test_one_kept_value_is_enough_to_bring_the_reporting_back(self):
        """The boundary D1 draws, from the other side — otherwise the negative case above could be
        passing because the whole `status` row had stopped being compared."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.pinned(tmp, self.STATUS, "| status | open, closed, blocked |")
            self.edit(root, self.OPEN, "open_statuses: [open, blocked]")
            self.restatused(root, "open")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertIn("CONFIG DRIFT", out)
            self.assertIn("status:", out)
            self.assertIn("'done'", out)
            self.assertNotIn("'blocked'", out)

    def test_a_deleted_row_is_left_alone(self):
        """`delete a row to stop checking one` is documented as a choice, so it is not a lag."""
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.pinned(tmp, self.TYPE + "\n", ""))
            self.assertEqual(code, 0, out)
            self.assertNotIn("CONFIG DRIFT", out)

    def test_the_comparison_reports_its_own_reach(self):
        """T-095's rule applied to this walk: a comparison that reads nothing must not look like
        one that read everything and found nothing."""
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.pinned(tmp))
            self.assertIn("5 vocabulary row(s)", out)

    def test_a_project_with_no_config_is_not_compared(self):
        """And it cannot be behind: it is *using* the default. The count says so rather than the
        walk being silently absent."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {})
            shutil.rmtree(os.path.join(root, ".taskmd"))
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertIn("0 vocabulary row(s)", out)
            self.assertNotIn("CONFIG DRIFT", out)


class LabelThatReadsAsAVersion(unittest.TestCase):
    """T-138, deciding T-137. A grouping label named after the version it was expected to ship in
    stops being true the first time a version is bumped for some other reason — and it does not go
    stale, it resolves, to a real tag holding something else. Two projects reached it independently.

    Every assertion here is against `label-shaped-value`, which carries all four behaviours in one
    project on purpose. Three of them passed while the check still crashed on the first real tree it
    met, because the fixture declared no list-valued field; `targets` is there for that.
    """

    FIXTURE = os.path.join(FIXTURES, "label-shaped-value")

    def check(self, root=None):
        code, out = run("check", "--root", root or self.FIXTURE)
        return code, out

    def test_it_fires_on_the_defect(self):
        code, out = self.check()
        self.assertIn("LABEL SHAPE", out)
        self.assertIn("work_package: 'v0.2'", out)

    def test_one_line_per_value_and_it_counts_the_tasks(self):
        """Per task this fixture would print four lines, and the real corpus that produced this
        check would have printed 137. A warning read once and scrolled past is not a warning."""
        code, out = self.check()
        self.assertIn("work_package: 'v0.2' on 2 task(s)", out)
        self.assertEqual(out.count("LABEL SHAPE"), 3, out)

    def test_it_reads_the_shape_and_never_the_field_name(self):
        """The whole reason there is no config key: `milestone` is a field name no schema mentions,
        and a rule keyed on a name could not have seen it at all."""
        code, out = self.check()
        self.assertIn("milestone: '2.1'", out)

    def test_a_list_valued_field_is_read_too(self):
        code, out = self.check()
        self.assertIn("targets: '3.0'", out)
        self.assertNotIn("'1.4.2'", out)

    def test_a_real_version_is_left_alone(self):
        """Three or more components is a version recorded correctly."""
        code, out = self.check()
        self.assertNotIn("shipped_in", out)
        self.assertNotIn("'0.4.0'", out)

    def test_the_estimate_fields_are_exempt(self):
        """`days: 1.5` is a quantity. This was the only false positive a probe built to break the
        rule could produce, and the exemption is read from `effort_field`, not from a new key."""
        code, out = self.check()
        self.assertNotIn("days:", out)

    def test_it_is_advisory_and_does_not_move_the_exit_status(self):
        code, out = self.check()
        self.assertEqual(code, 0, out)
        self.assertNotIn("problem(s)", out)

    def test_it_reports_what_it_examined(self):
        code, out = self.check()
        self.assertIn("front-matter value(s)", out)

    def test_every_other_fixture_is_silent(self):
        """The direction a clean pass cannot prove. One of these was the corpus this check was
        measured against; the rest are projects that never had the defect."""
        for path in sorted(glob.glob(os.path.join(FIXTURES, "*"))):
            if not os.path.isdir(path) or os.path.samefile(path, self.FIXTURE):
                continue
            if not os.path.isdir(os.path.join(path, ".taskmd")):
                continue
            code, out = run("check", "--root", path)
            self.assertNotIn("LABEL SHAPE", out, os.path.basename(path))

    def test_this_repository_is_silent(self):
        """It carried 137 of these until T-136 renamed them. The check is asserted against the tree
        it was written for, so a label sneaking back in fails the suite rather than a reader."""
        code, out = run("check", "--root", ROOT)
        self.assertNotIn("LABEL SHAPE", out)


class TableRowWiderThanItsHeader(unittest.TestCase):
    """T-141, from an adopter report. Markdown drops a cell past the header count, so the text is in
    the file and absent from the page, and nothing else this project runs can see it: the instance
    that produced this check sat in a closed task for most of a week with `check` clean, the suite
    green and the pre-publish gate silent.

    Every assertion is against `wide-table-row`, which carries all six behaviours in one project —
    three the check must report and three it must ignore. A fixture proving five would let the sixth
    regress in silence, which is exactly how T-138 shipped a check that crashed on the first real
    tree it met.

    **The specimens exist only in that fixture.** A row demonstrating this fault written anywhere
    else in this repository would be an instance of the fault, so the reproduction case cannot be
    quoted into a test, a task or a document.
    """

    FIXTURE = os.path.join(FIXTURES, "wide-table-row")
    REPORTS = "T-001-three-rows-that-lose-text.md"
    IGNORES = "T-002-three-rows-that-lose-nothing.md"

    def check(self, root=None):
        return run("check", "--root", root or self.FIXTURE)

    def test_it_fires_on_the_defect(self):
        code, out = self.check()
        self.assertIn("WIDE ROW", out)
        self.assertIn(self.REPORTS, out)

    def test_it_is_a_problem_and_moves_the_exit_status(self):
        """The opposite of the three advisory lines beside it. A legal state does not fail (T-100),
        and a cell that renders nowhere is not a state any project means."""
        code, out = self.check()
        self.assertEqual(code, 1, out)
        self.assertIn("3 problem(s)", out)

    def test_it_names_the_file_the_line_and_both_widths(self):
        """A reader has to find one row in a file of hundreds, and the two counts are what say
        how much was lost rather than that something was."""
        code, out = self.check()
        self.assertRegex(out, r"WIDE ROW\s+tasks/%s:\d+ has 4 cells against a 2-column header"
                         % re.escape(self.REPORTS))

    def test_a_pipe_inside_a_code_span_is_still_a_cell_boundary(self):
        """Markdown splits cells before it parses inline spans, so backticks do not protect a pipe.
        Two authors in this repository escaped one inside a code span inside a table cell, which
        nobody does unless the backticks failed to protect it — `without_code` is the obvious helper
        to reach for here and it is the wrong one."""
        code, out = self.check()
        self.assertEqual(out.count("WIDE ROW"), 3, out)

    def test_the_three_quiet_cases_are_quiet(self):
        """Blank excess, an escaped pipe and a short row. Each is silent for its own reason, and
        one assertion covers all three because the file they are in must not appear at all."""
        code, out = self.check()
        self.assertNotIn(self.IGNORES, out)

    def test_a_fenced_block_is_not_a_table(self):
        """This project quotes taskmd's own output constantly and `index` emits a table, so reading
        fences would make the tool's output the one thing a project could not quote (T-112).

        Asserted on the count rather than on the absence of a name: the fenced pseudo-table sits in
        the file this test class otherwise expects to be silent, so a fence being read would show up
        here as a fourth row and nowhere else."""
        code, out = self.check()
        self.assertEqual(out.count("WIDE ROW"), 3, out)
        self.assertIn("12 table row(s)", out)

    def test_it_reports_what_it_examined(self):
        """A scan that reports only its hits cannot be told from one that ran on nothing — which is
        the whole reason this task proved its measuring instrument before believing its zeros."""
        code, out = self.check()
        self.assertIn("table row(s)", out)

    def test_every_other_fixture_is_silent(self):
        """The direction a clean pass cannot prove."""
        for path in sorted(glob.glob(os.path.join(FIXTURES, "*"))):
            if not os.path.isdir(path) or os.path.samefile(path, self.FIXTURE):
                continue
            if not os.path.isdir(os.path.join(path, ".taskmd")):
                continue
            code, out = run("check", "--root", path)
            self.assertNotIn("WIDE ROW", out, os.path.basename(path))

    def test_this_repository_is_silent(self):
        """It carried one of these until T-140 repaired it, in a closed task, for most of a week.
        The corpus that produced the rule is the regression test for it."""
        code, out = run("check", "--root", ROOT)
        self.assertNotIn("WIDE ROW", out)


class LinkSyntaxShownRatherThanMade(ScratchProject):
    """T-112. `check_links` ran one flat regex over the whole document, so a project that quotes
    taskmd's own output had its quoted rows resolved as if they were its own links — and `index`
    emits a Markdown link per row, so the output such a project most wants to quote is exactly the
    output it cannot.

    The negative cases come first, because this is a *false positive* being removed and the way that
    goes wrong is a blanket loosening. A fence must not become a place where real links stop being
    checked.

    This repository did not lack the case. It had one and passed anyway, because a target abridged
    to three dots resolves on Windows and does not on Linux: `check` exited 0 here and 1 on a Linux
    runner, on the same tree.
    """

    FENCED = {"notes.md": ("A [real one](nowhere-above.md) above the fence.\n"
                           "\n"
                           "```\n"
                           "taskmd index  ->  | ID | Title |\n"
                           "                  | [T-001](nowhere-inside.md) | Carries two |\n"
                           "```\n"
                           "\n"
                           "A [real one](nowhere-below.md) below the fence.\n")}

    SPANNED = {"notes.md": "Write it as `[T-001](nowhere-in-a-span.md)` and it is shown.\n"}

    # The abridgement this repository actually contained. Its target is three dots, which Windows
    # resolves and Linux does not - so a test asserting it is *not reported* passes on Windows
    # whether or not the defect is fixed. Both were written that way first and both passed against
    # the unfixed scanner; the count below is what makes the case provable on either platform,
    # because an unfollowable string was counted as a link checked regardless of where it ran.
    ABRIDGED = {"notes.md": ("```\n"
                             "taskmd index  ->  | [T-001](...) | Carries two fields ... |\n"
                             "```\n")}

    PLAIN = {"notes.md": "Nothing quoted here at all.\n"}

    def links(self, out):
        found = re.search(r"(\d+) link\(s\)", out)
        self.assertIsNotNone(found, out)
        return int(found.group(1))

    def test_a_fenced_link_is_left_alone_and_the_real_ones_around_it_are_not(self):
        """Criteria 1 and 3 in one run, deliberately: proving the fence is skipped is worth nothing
        unless the same document proves links immediately above and below it are still resolved."""
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.project(tmp, self.FENCED))
            self.assertEqual(code, 1, out)
            self.assertIn("nowhere-above.md", out)
            self.assertIn("nowhere-below.md", out)
            self.assertNotIn("nowhere-inside.md", out)
            self.assertEqual(out.count("BROKEN LINK"), 2, out)

    def test_a_link_inside_a_code_span_is_left_alone(self):
        """Criterion 2. The document count is asserted so this cannot pass by not being read."""
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.project(tmp, self.SPANNED))
            self.assertEqual(code, 0, out)
            self.assertNotIn("BROKEN LINK", out)
            self.assertEqual(self.documents(out), 3, out)

    def test_the_abridged_target_this_repository_carried_stops_being_a_link(self):
        """The regression guard for the case that was actually here, asserted on the count rather
        than on the report — see the note on ABRIDGED for why the obvious assertion is untestable
        on half the platforms this runs on."""
        with tempfile.TemporaryDirectory() as tmp:
            quiet = self.links(run("check", "--root", self.project(tmp, self.PLAIN))[1])
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run("check", "--root", self.project(tmp, self.ABRIDGED))
        self.assertEqual(code, 0, out)
        self.assertEqual(self.links(out), quiet, "an abridged target was counted as a link checked")

    def test_a_document_quoting_the_whole_generated_index_passes(self):
        """Criterion 4, and the one that matters to an adopter: `index` writes a link per row, so
        quoting what it printed is the ordinary case rather than a contrived one."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, self.PLAIN)
            code, out = run("index", "--root", root)
            self.assertEqual(code, 0, out)
            board = cli.read(os.path.join(root, "tasks", "README.md"))
            cli.write(os.path.join(root, "quoted.md"),
                      "What the board looked like:\n\n```\n" + board + "```\n")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("BROKEN LINK", out)

    def test_the_link_count_excludes_what_was_never_a_pointer(self):
        """Criterion 5. `links += 1` ran on every match with no filter in front of it, so a project
        that quoted output had its coverage figure inflated by strings no reader could follow."""
        with tempfile.TemporaryDirectory() as tmp:
            quiet = self.links(run("check", "--root", self.project(tmp, self.PLAIN))[1])
        with tempfile.TemporaryDirectory() as tmp:
            spanned = self.links(run("check", "--root", self.project(tmp, self.SPANNED))[1])
        self.assertEqual(spanned, quiet,
                         "a link shown in a code span was counted as a link checked")


if __name__ == "__main__":
    unittest.main(verbosity=2)
