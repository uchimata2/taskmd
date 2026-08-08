#!/usr/bin/env python
"""Proof for T-011: the project is found from the repository, and its hook is run and reported.

Two halves, and each is written so the thing it claims can fail.

*Discovery* — every other test in this suite passes `--root`, which is exactly the case T-011
exists to remove: a clone has to work when nobody names a path. So these tests change the working
directory and pass no flag, which is the only way to tell a resolved root from a lucky one.

*Hooks* — the failing hook and the missing hook are the tests that matter. A hook mechanism that
has only ever been watched succeeding proves that a command can be run, not that a project can
rely on it (R-16).

  python tests/test_runtime.py
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin")   # the plugin subtree: where the taskmd package lives
sys.path.insert(0, PKG)

from taskmd import cli  # noqa: E402

FIXTURES = os.path.join(ROOT, "tests", "fixtures")

CONFIG = """---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: %(tasks_dir)s
status_field: status
deliverables_field: none
blocked_status: none
value_field: none
effort_field: none
after_write: %(after_write)s
open_statuses: [proposed]
context_fields: [status]
index_columns: [status]
---

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | proposed, done |
"""

TASK = "---\nid: T-001\ntitle: Something to index\nstatus: proposed\n---\n\n# T-001\n"


def run(*argv):
    """Call the CLI the way a shell does, capturing what a user would see.

    A hook's output is captured by the command rather than inherited, so it lands in this buffer
    like everything else. That is a design choice being relied on, not an accident — see
    `cli.run_after_write`.
    """
    import io
    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        code = cli.main(list(argv))
    finally:
        sys.stdout = stdout
    return code, buffer.getvalue()


class Sandbox(unittest.TestCase):
    """A throwaway project, and a working directory that is always put back."""

    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.addCleanup(os.chdir, os.getcwd())

    def project(self, where=None, tasks_dir="tasks", after_write="none", config=True):
        base = os.path.join(self.tmp, where) if where else self.tmp
        if config:
            cli.write(os.path.join(base, ".taskmd", "config.md"),
                      CONFIG % {"tasks_dir": tasks_dir, "after_write": after_write})
        cli.write(os.path.join(base, tasks_dir, "T-001-x.md"), TASK)
        return base

    def subdir(self, base, *parts):
        folder = os.path.join(base, *parts)
        os.makedirs(folder)
        return folder


# ------------------------------------------------------------------------------- discovery

class FindsTheProject(Sandbox):
    """Criterion 6: the root resolves from the repository, not from the working directory."""

    def test_a_command_run_from_a_subdirectory_finds_the_project(self):
        base = self.project()
        os.chdir(self.subdir(base, "docs", "notes"))
        code, out = run("check")
        self.assertEqual(code, 0, out)
        self.assertIn("1 task(s)", out)

    def test_a_project_with_no_config_at_all_is_still_found(self):
        """The case the shipped default exists for, and the one a config-only marker would miss:
        this repository has no `.taskmd/`, so a rule keyed on it would fail on the very tree that
        has to prove the feature."""
        base = self.project(config=False)
        os.chdir(self.subdir(base, "deep", "deeper"))
        code, out = run("check")
        self.assertEqual(code, 0, out)

    def test_a_project_that_renames_its_tasks_folder_is_found_by_its_config(self):
        base = self.project(tasks_dir="issues")
        os.chdir(self.subdir(base, "sub"))
        code, out = run("check")
        self.assertEqual(code, 0, out)

    def test_outside_any_project_it_says_so_rather_than_guessing(self):
        empty = os.path.join(self.tmp, "not-a-project")
        os.makedirs(empty)
        os.chdir(empty)
        code, out = run("check")
        self.assertEqual(code, 2, out)
        self.assertIn("No taskmd project", out)
        self.assertIn(".taskmd/config.md", out)
        self.assertIn("tasks", out)

    def test_the_nearest_project_wins(self):
        """A fixture project inside a repository is a project in its own right — the same rule
        `check` already uses to keep this repository's broken fixtures out of its own report."""
        outer = self.project()
        inner = self.project(where=os.path.join("tests", "inner"), tasks_dir="issues")
        os.chdir(self.subdir(inner, "sub"))
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertTrue(os.path.isfile(os.path.join(inner, "issues", "README.md")))
        self.assertFalse(os.path.isfile(os.path.join(outer, "tasks", "README.md")))

    def test_the_root_flag_still_overrides_discovery(self):
        base = self.project()
        os.chdir(base)
        code, out = run("check", "--root", os.path.join(FIXTURES, "alt-project"))
        self.assertEqual(code, 0, out)
        self.assertIn("3 task(s)", out)

    def test_no_message_carries_an_absolute_path(self):
        """R-20 asks for identical output everywhere, which a resolved root quietly threatens:
        the moment the root stops being '.', anything printing it prints somebody's disk."""
        os.chdir(self.subdir(self.tmp, "nowhere"))
        outputs = [run("check")[1]]
        os.chdir(self.project(config=False))
        outputs.append(run("check")[1])
        outputs.append(run("context", "T-001")[1])
        for out in outputs:
            self.assertNotIn(self.tmp, out)
            self.assertNotIn(self.tmp.replace(os.sep, "/"), out)

    def test_the_config_a_command_used_is_named_relative_to_something(self):
        base = self.project(config=False)
        os.chdir(base)
        code, out = run("check", "--root", os.path.join(FIXTURES, "broken-config"))
        self.assertEqual(code, 2, out)
        self.assertIn(".taskmd/config.md", out)
        self.assertNotIn(FIXTURES, out)


# ----------------------------------------------------------------------------------- hooks

def non_python_hook(folder):
    """A hook in a language that is not Python, written for whatever shell this machine has.

    Criterion 4 is about the mechanism being language-free, so the honest test is one that picks
    the platform's own shell rather than one that skips where the shell it assumed is absent.
    """
    if shutil.which("bash"):
        cli.write(os.path.join(folder, "hooks", "after-write.sh"),
                  "#!/bin/sh\necho \"hook speaking, not python\"\n")
        return "bash hooks/after-write.sh"
    cli.write(os.path.join(folder, "hooks", "after-write.cmd"),
              "@echo off\r\necho hook speaking, not python\r\n")
    return "cmd /c hooks\\after-write.cmd"


class RunsTheProjectsHook(Sandbox):
    """Criteria 3 and 4: a declared hook runs, in any language, and its failure surfaces."""

    def python_hook(self, folder, exit_code=0, says="hook ran"):
        cli.write(os.path.join(folder, "hooks", "after-write.py"),
                  "import sys\nprint(%r)\nsys.exit(%d)\n" % (says, exit_code))
        return "python hooks/after-write.py"

    def test_a_declared_hook_runs_after_the_write_and_its_output_is_shown(self):
        base = self.project(after_write="python hooks/after-write.py")
        self.python_hook(base)
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertIn("Wrote", out)
        self.assertIn("hook ran", out)
        self.assertLess(out.index("Wrote"), out.index("hook ran"),
                        "the hook is an *after*-write hook:\n%s" % out)

    def test_a_hook_that_fails_fails_the_command(self):
        base = self.project(after_write="python hooks/after-write.py")
        self.python_hook(base, exit_code=3, says="this project is inconsistent")
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 1, out)
        self.assertIn("this project is inconsistent", out)
        self.assertIn("3", out)

    def test_the_write_still_happened_when_the_hook_failed(self):
        """The hook runs after the write, so failing it reports a problem rather than undoing one.
        A reader who saw the command fail must not be left guessing whether the file was written."""
        base = self.project(after_write="python hooks/after-write.py")
        self.python_hook(base, exit_code=1)
        os.chdir(base)
        run("index")
        self.assertTrue(os.path.isfile(os.path.join(base, "tasks", "README.md")))

    def test_a_hook_written_in_another_language_runs(self):
        base = self.project()
        command = non_python_hook(base)
        cli.write(os.path.join(base, ".taskmd", "config.md"),
                  CONFIG % {"tasks_dir": "tasks", "after_write": command})
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertIn("hook speaking, not python", out)

    def test_the_hook_runs_with_the_project_as_its_working_directory(self):
        base = self.project(after_write="python hooks/after-write.py")
        cli.write(os.path.join(base, "hooks", "after-write.py"),
                  "import os\nprint('cwd-has-tasks:', os.path.isdir('tasks'))\n")
        os.chdir(self.subdir(base, "somewhere", "else"))
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertIn("cwd-has-tasks: True", out)

    def test_a_command_that_writes_nothing_does_not_run_the_hook(self):
        base = self.project(after_write="python hooks/after-write.py")
        self.python_hook(base)
        os.chdir(base)
        for command in ("check", "list", "context"):
            args = (command, "T-001") if command == "context" else (command,)
            self.assertNotIn("hook ran", run(*args)[1], "%s ran the hook" % command)

    def test_a_project_declaring_no_hook_is_unaffected(self):
        base = self.project()
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertNotIn("Hook", out)


class ReportsAnUnrunnableHookAtSetup(unittest.TestCase):
    """Criterion 5, and R-17: reported when the config is read, never mid-command."""

    BROKEN = os.path.join(FIXTURES, "broken-hook")

    def test_every_command_refuses_before_it_starts(self):
        for args in (("check",), ("index",), ("list",), ("context", "T-001")):
            code, out = run(*(args + ("--root", self.BROKEN)))
            self.assertEqual(code, 2, out)
            self.assertIn("CONFIG ERROR", out)
            self.assertIn("after_write", out)

    def test_it_names_the_declared_command_not_a_resolved_path(self):
        code, out = run("check", "--root", self.BROKEN)
        self.assertIn("hooks/after-write.sh", out)
        self.assertNotIn(FIXTURES, out)

    def test_index_did_not_write_before_refusing(self):
        readme = os.path.join(self.BROKEN, "tasks", "README.md")
        run("index", "--root", self.BROKEN)
        self.assertFalse(os.path.isfile(readme),
                         "the config was rejected, so nothing should have been written")

    def test_a_program_that_is_not_on_path_is_caught_too(self):
        """The other half of 'unrunnable': not a path in the project, and not on PATH either."""
        tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        cli.write(os.path.join(tmp, ".taskmd", "config.md"),
                  CONFIG % {"tasks_dir": "tasks", "after_write": "definitely-not-a-program --check"})
        cli.write(os.path.join(tmp, "tasks", "T-001-x.md"), TASK)
        code, out = run("check", "--root", tmp)
        self.assertEqual(code, 2, out)
        self.assertIn("definitely-not-a-program", out)


# -------------------------------------------------------------------------------- launchers

class Launchers(unittest.TestCase):
    """Criterion 2: the launchers carry no logic, so removing one changes nothing but the way in."""

    def test_both_launchers_exist_at_the_root_where_a_clone_will_look(self):
        """The root a clone looks at is the *plugin* root, which is what an install receives —
        not this repository's root, which also holds material the plugin does not ship."""
        for name in ("taskmd.sh", "taskmd.ps1"):
            self.assertTrue(os.path.isfile(os.path.join(PKG, name)), name)

    def test_neither_launcher_names_a_command_a_flag_or_a_field(self):
        """What 'no logic' means, made checkable: a launcher that knew a command name would have
        to be edited whenever the tool grew one, which is the drift this criterion is about."""
        for name in ("taskmd.sh", "taskmd.ps1"):
            text = cli.read(os.path.join(PKG, name))
            body = "\n".join(ln for ln in text.splitlines()
                             if ln.strip() and not ln.strip().startswith("#"))
            for word in sorted(cli.COMMANDS) + ["--root", "tasks_dir", "status"]:
                self.assertNotIn(word, body, "%s mentions %r" % (name, word))

    def test_the_shell_launcher_produces_what_the_module_produces(self):
        if not shutil.which("bash"):
            self.skipTest("no bash on this machine; the PowerShell launcher covers the same claim")
        # `-m taskmd` needs the package on the path; the launcher sets that for itself, which is
        # the whole of what it does. Both run from ROOT, so both discover the same project.
        env = dict(os.environ, PYTHONPATH=PKG)
        direct = subprocess.run([sys.executable, "-m", "taskmd", "check"], cwd=ROOT, env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        viash = subprocess.run(["bash", "plugin/taskmd.sh", "check"], cwd=ROOT,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertEqual(direct.stdout, viash.stdout)
        self.assertEqual(direct.returncode, viash.returncode)


if __name__ == "__main__":
    unittest.main(verbosity=2)
