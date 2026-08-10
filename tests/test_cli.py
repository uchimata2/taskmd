#!/usr/bin/env python
"""Proof for T-002: the three commands, and `check` shown failing on every class it claims.

The negative cases are the point. A validator is worth exactly your confidence that it *would*
catch what it claims to, and the only way to earn that is to watch it fail on a case it should
catch — so every `broken-*` fixture under `tests/fixtures/` is asserted to produce its own class
and nothing else.

  python tests/test_cli.py
"""

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
              "STALE INDEX"]

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
    def test_a_published_document_may_still_point_at_a_gitignored_one(self):
        """The target side deliberately keeps answering the *other* question, "is this file here?".
        R-23 quarantines local-only material behind `.gitignore` and requires the tracked tree to
        refer to it by name; reporting that pointer would make this project's own convention
        unrepresentable. Rejected alternative, recorded in T-094 rather than only here."""
        with tempfile.TemporaryDirectory() as tmp:
            root = self.project(tmp, {".gitignore": "private/\n",
                                      "private/local.md": "Local only.\n",
                                      "docs/guide.md": "See [the local note](../private/local.md).\n"})
            self.git(root, "init")
            code, out = run("check", "--root", root)
            self.assertEqual(code, 0, out)
            self.assertNotIn("BROKEN LINK", out)

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
