"""The dash gate, run by the suite instead of remembered at publication (T-126).

`docs/PUBLISHING.md` §5 has always held this rule, and holding it was the problem: it is a manual
command in a document read only at publication, and publication is when there is most pressure not
to stop. Measured on the three existing tags, the README carried 0 offending lines at `v0.1.0`, 6 at
`v0.2.0` and 13 at `v0.3.0` — two releases went out with the gate red and nothing said so.

`test_budget.py` is the precedent: a rule nobody runs is a rule nobody keeps, so the suite runs it.

**The covered set and the two characters are not written here.** They are read out of the fenced
command in `docs/PUBLISHING.md` §5, which stays their one home; if they cannot be read, that is a
failure and not a skip, because a gate the suite can no longer parse has drifted.
"""

import os
import re
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHING = os.path.join(ROOT, "docs", "PUBLISHING.md")

# The pathspec, as arguments to `git ls-files`, and the characters `grep` is given. Both are
# captured from the one command rather than restated, so adding a covered document to §5 arms this
# test with nothing edited here.
PATHSPEC_RE = re.compile(r"--exclude-standard\s+((?:'[^']+'\s*)+)\)")
DASH_RE = re.compile(r"-e\s+'([^']+)'")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def gate_from_the_document():
    """The pathspec and the characters, lifted from `docs/PUBLISHING.md` §5.

    Deliberately strict. A shape this cannot parse means the documented gate and the enforced one
    have come apart, which is the state this module exists to make impossible.
    """
    text = read(PUBLISHING)
    section = text.split("## 5. The gate", 1)
    if len(section) != 2:
        raise AssertionError("docs/PUBLISHING.md has no '## 5. The gate' - the gate has moved, and "
                             "this test reads it from there rather than restating it")
    body = section[1].split("\n## ", 1)[0]
    paths = PATHSPEC_RE.search(body)
    dashes = DASH_RE.findall(body)
    if not paths:
        raise AssertionError("could not read the pathspec out of docs/PUBLISHING.md section 5; the "
                             "command's shape changed, so the documented gate and this test are no "
                             "longer the same rule")
    if not dashes:
        raise AssertionError("could not read the -e characters out of docs/PUBLISHING.md section 5")
    return [p.strip("'") for p in paths.group(1).split()], dashes


def covered_files(pathspec):
    listed = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"] + pathspec,
        cwd=ROOT).decode("utf-8")
    return [line for line in listed.splitlines() if line]


def git_is_available():
    try:
        done = subprocess.Popen(["git", "--version"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        done.communicate()
    except OSError:
        return False
    return done.returncode == 0


GIT = git_is_available()


@unittest.skipUnless(GIT, "no git: the covered set is a git pathspec, so there is nothing to resolve")
class ThePassingDashGateProvesOnlyThatOnePatternIsAbsent(unittest.TestCase):
    """Named for what a pass does **not** mean, because that is the half most likely to be forgotten.

    Pattern 14 is the only part of `docs/PUBLISHING.md` §2 a script can judge. Failing here proves
    the humanizer rewrite did not happen; passing proves only that one pattern is absent. The rewrite
    is a judgement and needs the skill and an agent.
    """

    def test_the_pathspec_resolves_to_files(self):
        """The gate's exit 2, kept. A run that covers nothing prints nothing, which is also what
        success looks like - this project has hit that three times (T-034, T-080, and §5's own
        exit 2)."""
        pathspec, _ = gate_from_the_document()
        self.assertTrue(pathspec, "section 5's pathspec is empty")
        self.assertTrue(covered_files(pathspec),
                        "the pathspec in docs/PUBLISHING.md section 5 covers 0 files - the gate is "
                        "broken, not the tree")

    def test_no_covered_document_carries_an_em_or_en_dash(self):
        pathspec, dashes = gate_from_the_document()
        offenders = []
        for where in covered_files(pathspec):
            for number, line in enumerate(read(os.path.join(ROOT, where)).splitlines(), 1):
                if any(dash in line for dash in dashes):
                    offenders.append("%s:%d" % (where, number))
        self.assertEqual([], offenders,
                         "%d covered line(s) carry a dash the humanizer removes; run the rewrite in "
                         "docs/PUBLISHING.md section 2, not a find-and-replace:\n%s"
                         % (len(offenders), "\n".join(offenders)))

    def test_the_scan_reports_a_dash_when_one_is_present(self):
        """A clean tree proves nothing on its own. The same characters, the same containment test,
        over text that must be caught - so the assertion above is known to be capable of failing."""
        _, dashes = gate_from_the_document()
        self.assertIn("—", dashes, "the em dash is no longer one of the characters section 5 "
                                        "greps for")
        self.assertIn("–", dashes, "the en dash is no longer one of the characters section 5 "
                                        "greps for")
        drifted = ["A line that reads fine — until you look at the dash.",
                   "And an en dash – the same problem."]
        caught = [line for line in drifted if any(dash in line for dash in dashes)]
        self.assertEqual(drifted, caught)


BEGIN_COMMANDS = "<!-- taskmd:commands -->"
END_COMMANDS = "<!-- taskmd:end-commands -->"

# Which document, and how a command name is written in it. The pattern is what stops a table of
# purposes and a block of invocations needing two checks: both write `taskmd <name>`, so one
# expression reads both.
MARKED = ("README.md", os.path.join("plugin", "skills", "taskmd", "taskmd", "cli.py"))
COMMAND_RE = re.compile(r"taskmd\s+([a-z][a-z0-9-]*)")


def marked_commands(path):
    """The command names inside a document's `taskmd:commands` region, or None if it has none.

    Opt-in by marker rather than by guessing which documents are lists (T-134 Q1). A heuristic —
    "any document naming every current command is a list" — needs no markup and stops checking a
    document the moment one name drops out of it, which is the failure being guarded.
    """
    text = read(path)
    start = text.find(BEGIN_COMMANDS)
    if start == -1:
        return None
    end = text.find(END_COMMANDS, start)
    if end == -1:
        raise AssertionError("%s opens a taskmd:commands region and never closes it" % path)
    return set(COMMAND_RE.findall(text[start + len(BEGIN_COMMANDS):end]))


class EveryMarkedListNamesTheCommandsThereAre(unittest.TestCase):
    """T-134. T-117 let `README.md` and `cli.py` both list the four, because they say different
    things about them - purposes against flags. That holds only while the two agree about *which*
    commands exist, and nothing checked it: `usage_line` is derived from `COMMANDS`, but these two
    are prose. T-073 is this project carrying a document that named a three-command CLI for four
    days after it was four."""

    def commands(self):
        import sys
        sys.path.insert(0, os.path.join(ROOT, "plugin", "skills", "taskmd"))
        from taskmd import cli
        return set(cli.COMMANDS)

    def test_the_marked_regions_exist(self):
        """Without this, every assertion below passes on a tree where the markers were deleted."""
        for where in MARKED:
            self.assertIsNotNone(marked_commands(os.path.join(ROOT, where)),
                                 "%s carries no taskmd:commands region, so nothing checks the list "
                                 "in it" % where)

    def test_each_marked_list_names_exactly_the_commands_that_exist(self):
        expected = self.commands()
        for where in MARKED:
            listed = marked_commands(os.path.join(ROOT, where))
            self.assertEqual(expected, listed,
                             "%s is behind: it does not name %s, and it names %s which do not exist"
                             % (where, sorted(expected - listed) or "nothing missing",
                                sorted(listed - expected) or "nothing extra"))

    def test_a_command_mentioned_in_a_sentence_is_not_a_list(self):
        """Criterion 3, on the real tree. `README.md` names commands in prose outside the region -
        an FAQ row, a paragraph about filters - and none of that is checked, because the region is
        what declares an intent to be complete."""
        readme = read(os.path.join(ROOT, "README.md"))
        outside = readme[:readme.find(BEGIN_COMMANDS)] + readme[readme.find(END_COMMANDS):]
        self.assertTrue(COMMAND_RE.findall(outside),
                        "this test is vacuous unless README.md mentions a command outside the "
                        "region; it no longer does, so the case is untested")
        self.assertNotEqual(self.commands(), set(COMMAND_RE.findall(outside)) & self.commands(),
                            "every command now appears outside the region too, so this test can no "
                            "longer distinguish a mention from a list")


if __name__ == "__main__":
    unittest.main()
