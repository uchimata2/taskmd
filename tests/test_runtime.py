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
import re
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


def python_on_path():
    """The interpreter these fixtures name in a config, as a **bare name** (T-057).

    `sys.executable` cannot be used, for two reasons that are both properties of the resolver rather
    than accidents: it runs the declared line through `shlex.split`, which is POSIX-mode and eats
    the backslashes of a Windows path, and it treats a program containing a separator as a file
    *inside the project*, which an interpreter is not. A bare name goes through `shutil.which`,
    which is the route a real project's hook takes.

    The running interpreter's own basename is tried first, so the hook is the same Python as the
    suite. `python3` and `python` follow because an interpreter can be launched from a directory
    that is not on PATH. Both are needed: Ubuntu ships no `python` at all, which is the whole of
    T-057, and Windows usually has no `python3` that runs.
    """
    for name in (os.path.basename(sys.executable), "python3", "python"):
        if name and shutil.which(name):
            return name
    return None


PYTHON = python_on_path()
PYTHON_HOOK = "%s hooks/after-write.py" % PYTHON   # one fact; five call sites read it


class RunsTheProjectsHook(Sandbox):
    """Criteria 3 and 4: a declared hook runs, in any language, and its failure surfaces."""

    def setUp(self):
        if not PYTHON:
            self.skipTest("no Python resolves under any name a config could name; these tests "
                          "would be reporting on the machine rather than on the hook mechanism")
        Sandbox.setUp(self)

    def python_hook(self, folder, exit_code=0, says="hook ran"):
        cli.write(os.path.join(folder, "hooks", "after-write.py"),
                  "import sys\nprint(%r)\nsys.exit(%d)\n" % (says, exit_code))
        return PYTHON_HOOK

    def test_a_declared_hook_runs_after_the_write_and_its_output_is_shown(self):
        base = self.project(after_write=PYTHON_HOOK)
        self.python_hook(base)
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertIn("Wrote", out)
        self.assertIn("hook ran", out)
        self.assertLess(out.index("Wrote"), out.index("hook ran"),
                        "the hook is an *after*-write hook:\n%s" % out)

    def test_a_hook_that_fails_fails_the_command(self):
        base = self.project(after_write=PYTHON_HOOK)
        self.python_hook(base, exit_code=3, says="this project is inconsistent")
        os.chdir(base)
        code, out = run("index")
        self.assertEqual(code, 1, out)
        self.assertIn("this project is inconsistent", out)
        self.assertIn("3", out)

    def test_the_write_still_happened_when_the_hook_failed(self):
        """The hook runs after the write, so failing it reports a problem rather than undoing one.
        A reader who saw the command fail must not be left guessing whether the file was written."""
        base = self.project(after_write=PYTHON_HOOK)
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
        base = self.project(after_write=PYTHON_HOOK)
        cli.write(os.path.join(base, "hooks", "after-write.py"),
                  "import os\nprint('cwd-has-tasks:', os.path.isdir('tasks'))\n")
        os.chdir(self.subdir(base, "somewhere", "else"))
        code, out = run("index")
        self.assertEqual(code, 0, out)
        self.assertIn("cwd-has-tasks: True", out)

    def test_a_command_that_writes_nothing_does_not_run_the_hook(self):
        base = self.project(after_write=PYTHON_HOOK)
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

class ThePluginShipsWhatItCites(unittest.TestCase):
    """T-064. Nothing under `plugin/` may send a reader to something an adopter does not receive.

    This is the sweep the boundary never had. T-053 drew the boundary and closed on a sweep for
    **links** that escape the subtree, which was honest and returned none — every escape it left
    behind was backticked prose or a code comment, and a link checker cannot see one. So this
    reads *references*: the requirement numbers, the repository's own papers by name, and any
    relative path that climbs out of `plugin/`.

    It lives here rather than in the always-loaded conventions because it has to run without
    anybody remembering to run it, which is the property the last sweep lacked.
    """

    #: What a reader inside the plugin cannot follow. `R-NN` and the numbered non-goals are
    #: `docs/SCOPE.md`'s numbering; SCOPE, BRIEF and CLAUDE are this repository's own papers,
    #: deliberately left outside the plugin. None of the four ships.
    ESCAPES = re.compile(r"\bR-\d+\b|\bnon-goal\b|\bSCOPE\.md\b|\bBRIEF\.md\b|\bCLAUDE\.md\b")

    SUBTREE = PKG  # the plugin root: exactly what an install receives

    def plugin_files(self):
        for base, dirs, files in os.walk(self.SUBTREE):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for name in sorted(files):
                if name.endswith((".pyc", ".png", ".gif")):
                    continue
                yield os.path.join(base, name)

    def test_no_file_in_the_plugin_cites_something_it_does_not_ship(self):
        offenders = []
        for path in self.plugin_files():
            try:
                text = cli.read(path)
            except (OSError, UnicodeDecodeError):
                continue
            for number, line in enumerate(text.splitlines(), 1):
                found = self.ESCAPES.search(line)
                if found:
                    offenders.append("%s:%d cites %r"
                                     % (os.path.relpath(path, ROOT).replace("\\", "/"),
                                        number, found.group(0)))
        self.assertEqual([], offenders, "\n".join(offenders))

    def test_no_relative_path_in_the_plugin_climbs_out_of_it(self):
        """The other half, and the one T-053 did sweep — kept so the two cannot drift apart."""
        offenders = []
        subtree = os.path.abspath(self.SUBTREE)
        for path in self.plugin_files():
            if not path.endswith(".md"):
                continue
            base = os.path.dirname(path)
            for target in cli.LINK.findall(cli.read(path)):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = os.path.abspath(os.path.join(base, target))
                if os.path.commonpath([resolved, subtree]) != subtree:
                    offenders.append("%s -> %s"
                                     % (os.path.relpath(path, ROOT).replace("\\", "/"), target))
        self.assertEqual([], offenders, "\n".join(offenders))


class Launchers(unittest.TestCase):
    """Criterion 2: the launchers carry no logic, so removing one changes nothing but the way in."""

    #: Comment markers, by extension. A launcher's *body* is what carries logic; its prose is
    #: allowed to say anything, and does.
    COMMENT = {".ps1": ("#",), ".cmd": ("rem", "@"), ".sh": ("#",), "": ("#",)}

    def entry_points(self):
        """Every file a user can invoke, **derived from the tree** rather than written down here.

        Two places, and they are two audiences: the plugin root is what a contributor with a clone
        types (`./plugin/taskmd.sh`), and `bin/` is what the harness puts on an adopter's PATH.
        Deriving it is the point — a written pair is correct only until someone adds a third entry
        point, and the day that happens is exactly the day nobody remembers to extend the list
        (T-068).
        """
        found = [os.path.join(PKG, n) for n in sorted(os.listdir(PKG))
                 if n.startswith("taskmd.") and os.path.isfile(os.path.join(PKG, n))]
        bindir = os.path.join(PKG, "bin")
        found += [os.path.join(bindir, n) for n in sorted(os.listdir(bindir))]
        return found

    def how_to_run(self, path):
        """The argv prefix that runs one entry point here, or None if this platform cannot.

        None is a real answer and the caller must report it: a `.cmd` on a POSIX machine cannot be
        run, and a test that quietly returned green for it would be worse than no test at all.
        """
        name = os.path.basename(path)
        if name.endswith(".cmd"):
            if os.name != "nt":
                return None
            return [os.environ.get("COMSPEC", "cmd.exe"), "/c", path]
        if name.endswith(".ps1"):
            shell = shutil.which("pwsh") or shutil.which("powershell")
            return [shell, "-NoProfile", "-File", path] if shell else None
        shell = shutil.which("bash") or shutil.which("sh")
        return [shell, path] if shell else None

    def test_every_entry_point_exists_where_the_one_who_runs_it_will_look(self):
        """Derived, so this cannot pass by describing a tree that has moved on."""
        found = [os.path.relpath(p, PKG).replace("\\", "/") for p in self.entry_points()]
        self.assertIn("taskmd.sh", found)
        self.assertIn("taskmd.ps1", found)
        self.assertIn("bin/taskmd", found)
        self.assertIn("bin/taskmd.cmd", found)

    def test_no_entry_point_names_a_command_a_flag_or_a_field(self):
        """What 'no logic' means, made checkable: an entry point that knew a command name would
        have to be edited whenever the tool grew one, which is the drift this criterion is about.

        Now over `bin/` too. Both files there are delegates, and a delegate that learned a command
        name would be a second launcher wearing a thin coat."""
        for path in self.entry_points():
            name = os.path.relpath(path, PKG).replace("\\", "/")
            markers = self.COMMENT[os.path.splitext(path)[1]]
            body = "\n".join(ln for ln in cli.read(path).splitlines()
                             if ln.strip() and not ln.strip().lower().startswith(markers))
            for word in sorted(cli.COMMANDS) + ["--root", "tasks_dir", "status"]:
                self.assertNotIn(word, body, "%s mentions %r" % (name, word))

    def test_every_entry_point_produces_what_the_module_produces(self):
        """T-068. The adopter's own command, run — not inspected, and not verified by hand once.

        The environment is **set by this test**. `bin/taskmd` reaches `taskmd.sh` by delegation, so
        it inherited T-061's defect in full and no test saw it; an assertion that borrows the
        runner's environment cannot see the case it is closest to.
        """
        expected = subprocess.run([sys.executable, "-m", "taskmd", "check"], cwd=ROOT,
                                  env=dict(os.environ, PYTHONPATH=PKG),
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ran = []
        for path in self.entry_points():
            name = os.path.relpath(path, PKG).replace("\\", "/")
            with self.subTest(entry=name):
                argv = self.how_to_run(path)
                if argv is None:
                    self.skipTest("%s cannot be run on this platform" % name)
                got = subprocess.run(argv + ["check"], cwd=ROOT,
                                     env=dict(os.environ, PYTHONPATH="relative/dir"),
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.assertEqual(expected.returncode, got.returncode,
                                 "%s exited %d: %s" % (name, got.returncode, got.stdout))
                self.assertEqual(expected.stdout.strip(), got.stdout.strip(), name)
                ran.append(name)
        self.assertTrue(ran, "no entry point was runnable here; this test proved nothing")

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

    # A drive-lettered value, assembled rather than written out. The pre-publish leak check in
    # CLAUDE.md matches exactly this shape, and a literal here would be indistinguishable from a
    # real machine path that leaked into the tree. Fabricated, and it deliberately does not exist.
    DRIVE_PATH = "C:" + "\\" + "opt" + "\\" + "lib"

    #: The three shapes an adopter's environment may already hold. The first two are what broke
    #: taskmd.sh: it appended them to its own POSIX path with a hardcoded ':', and the Windows
    #: shell layer then declined to rewrite the variable at all, so Python got a string it could
    #: not read and reported taskmd missing. The third always worked and is kept as the control.
    HOSTILE = ("relative/dir", DRIVE_PATH, "/tmp/nowhere")

    def available_launchers(self):
        """Every launcher this machine can actually run, as (label, argv-prefix)."""
        found = []
        if shutil.which("bash"):
            found.append(("taskmd.sh", ["bash", os.path.join(PKG, "taskmd.sh")]))
        for shell in ("pwsh", "powershell"):
            if shutil.which(shell):
                found.append(("taskmd.ps1",
                              [shell, "-NoProfile", "-File", os.path.join(PKG, "taskmd.ps1")]))
                break
        return found

    def test_a_launcher_ignores_whatever_pythonpath_the_caller_already_has(self):
        """T-061. The environment is **set by this test**, never inherited.

        That is the whole point, and it is why the defect this closes stayed invisible: the sibling
        test above runs the launcher under whatever the runner happens to have, so on a machine
        with no PYTHONPATH it passed while the launcher was broken for everyone who had one — which
        is to say, for a Python developer, the likeliest adopter. An assertion that inherits the
        environment cannot see the case it is closest to.
        """
        launchers = self.available_launchers()
        if not launchers:
            self.skipTest("neither bash nor PowerShell on this machine")
        for label, argv in launchers:
            for value in self.HOSTILE:
                env = dict(os.environ, PYTHONPATH=value)
                run = subprocess.run(argv + ["check"], cwd=ROOT, env=env,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                where = "%s with PYTHONPATH=%r" % (label, value)
                self.assertEqual(0, run.returncode,
                                 "%s exited %d: %s" % (where, run.returncode, run.stdout))
                self.assertTrue(run.stdout.startswith(b"OK -"), "%s: %s" % (where, run.stdout))

    def test_every_posix_shell_script_is_recorded_executable(self):
        """T-056. A shell script has no `python -m` equivalent: a `#!/bin/sh` file exists to be run
        by path, so a clone must receive it with the bit set. The Python files in this tree also
        carry shebangs and are all documented to run *through* the interpreter, which is why the
        subject is derived from the shebang rather than from a list someone maintains.

        Read out of git's index, never the filesystem. `core.fileMode` is false on Windows, so the
        working tree's bits are not what a clone receives — and Windows is where this defect is
        invisible and would therefore recur."""
        listing = subprocess.run(["git", "ls-files", "-s", "-z"], cwd=ROOT,
                                 stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if listing.returncode != 0:
            self.skipTest("not a git work tree; the recorded mode is what this asserts")
        offenders = []
        for entry in listing.stdout.split(b"\0"):
            if not entry:
                continue
            meta, _, path = entry.partition(b"\t")
            mode = meta.split(b" ")[0].decode()
            name = path.decode("utf-8")
            try:
                with open(os.path.join(ROOT, name), "rb") as handle:
                    shebang = handle.readline().decode("utf-8", "replace").strip()
            except OSError:
                continue
            if not shebang.startswith("#!"):
                continue
            words = re.split(r"[\s/]+", shebang[2:])
            if not any(word in ("sh", "bash", "dash", "zsh", "ksh") for word in words):
                continue
            if mode != "100755":
                offenders.append("%s is recorded %s" % (name, mode))
        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main(verbosity=2)
