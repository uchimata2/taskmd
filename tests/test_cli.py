#!/usr/bin/env python
"""Proof for T-002: the three commands, and `check` shown failing on every class it claims.

The negative cases are the point. A validator is worth exactly your confidence that it *would*
catch what it claims to, and the only way to earn that is to watch it fail on a case it should
catch — so every `broken-*` fixture under `tests/fixtures/` is asserted to produce its own class
and nothing else.

  python tests/test_cli.py
"""

import io
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin")   # the plugin subtree: where the taskmd package lives
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

    def test_the_broken_fixtures_are_not_reported_as_this_projects_problems(self):
        """They are projects in their own right. If the host reported them, `check` could never
        be clean here and the fixtures would have to live outside the repository."""
        code, out = run("check", "--root", ROOT)
        self.assertEqual(code, 0)
        self.assertNotIn("broken-", out)


class CheckFailsOnEveryClassItClaims(unittest.TestCase):
    """One fixture per class. Each must report its own class, and only its own."""

    LABELS = ["VOCABULARY", "DANGLING", "NO BLOCKER", "CYCLE", "BROKEN LINK",
              "STORED DERIVED", "MISSING OUTPUT", "CONFIG ERROR"]

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

    def test_declared_deliverable_that_is_gone(self):
        self.fails("broken-deliverable", "MISSING OUTPUT", "out/report.md")

    def test_config_error_surfaces_at_setup_naming_the_key(self):
        """R-17: reported when the config is read, with exit 2 — never from inside a command."""
        self.fails("broken-config", "CONFIG ERROR", "id_witdh", code=2)


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

    def test_a_folder_that_exists_but_is_empty_stays_legal(self):
        """A new project with nothing in it yet is not an error — the distinction is that the
        folder is absent, not that it holds no tasks."""
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        os.makedirs(os.path.join(tmp, "tasks"))
        self.assertEqual(run("check", "--root", tmp)[0], 0)
        self.assertEqual(run("index", "--root", tmp)[0], 0)


class Usage(unittest.TestCase):

    def test_no_command_explains_the_three(self):
        code, out = run()
        self.assertEqual(code, 2)
        for command in ("context", "index", "check"):
            self.assertIn(command, out)

    def test_a_root_that_does_not_exist_is_reported(self):
        code, out = run("check", "--root", os.path.join(ROOT, "no-such-folder"))
        self.assertEqual(code, 2)
        self.assertIn("No such directory", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
