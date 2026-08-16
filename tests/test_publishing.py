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

import collections
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


def _cli():
    import sys
    sys.path.insert(0, os.path.join(ROOT, "plugin", "skills", "taskmd"))
    from taskmd import cli
    return cli


#: One marked kind of list. `name` is the marker token, so the region is
#: `<!-- taskmd:<name> -->` … `<!-- taskmd:end-<name> -->`; `pattern` reads the members out of the
#: region's prose; `owned` returns the set the code owns; `required` names the documents that must
#: carry a region of this kind.
Kind = collections.namedtuple("Kind", "name pattern owned required")

# T-139 generalised this from commands to any marked list of a set the code owns. Adding a kind is
# one row here and a pair of markers in the document - no test below is edited, and none names a
# member of any set.
#
# The patterns differ because the registers do. A command is written as an invocation in both places
# that list them (`taskmd context <id>` in a table of purposes, `python -m taskmd context T-002` in a
# block of invocations), so one expression reads both. An advisory is written as a backticked
# all-caps name. `{3,}` on the first word is not decoration: the advisory region also contains
# `` `OK` ``, in the sentence about `check` saying it twice over a duplicated index, and a two-letter
# token would have been read as a fourth advisory.
KINDS = (
    Kind("commands",
         re.compile(r"taskmd\s+([a-z][a-z0-9-]*)"),
         lambda cli: set(cli.COMMANDS),
         ("README.md", os.path.join("plugin", "skills", "taskmd", "taskmd", "cli.py"))),
    Kind("advisories",
         re.compile(r"`([A-Z]{3,}(?: [A-Z]+)*)`"),
         lambda cli: set(cli.ADVISORY_PREFIXES),
         ("README.md",)),
)


def opens(kind, line):
    """True when this line *is* the opening marker, rather than merely containing one.

    **A marker counts only alone on its line**, and that rule was written by running the sweep, not
    foreseen. Discovery below reads every tracked file, and T-134's own task record describes the
    mechanism it built - `` `<!-- taskmd:commands -->` `` inline in a sentence, inside backticks.
    The first run read that record as a document listing the commands and failed, naming a task file
    as behind. Excluding `tasks/` would have been an exclusion list to maintain, and wrong anyway:
    the next document to describe the markers would be documentation. A real region marker sits on
    its own line in all three places that use one, and a quotation never can.
    """
    return line.strip() == "<!-- taskmd:%s -->" % kind.name


def closes(kind, line):
    return line.strip() == "<!-- taskmd:end-%s -->" % kind.name


def marked_region(path, kind):
    """The names inside a document's region of this kind, or None if it carries none.

    Opt-in by marker rather than by guessing which documents are lists (T-134 Q1). A heuristic -
    "any document naming every current member is a list" - needs no markup and stops checking a
    document the moment one name drops out of it, which is the failure being guarded.
    """
    lines = read(path).splitlines()
    start = next((i for i, line in enumerate(lines) if opens(kind, line)), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if closes(kind, lines[i])), None)
    if end is None:
        raise AssertionError("%s opens a taskmd:%s region and never closes it" % (path, kind.name))
    return set(kind.pattern.findall("\n".join(lines[start + 1:end])))


def tracked_files():
    """Every file a clone receives, so a document that opts in is checked wherever it is.

    `git ls-files` for the same reason the dash gate above uses it: it is the definition of what
    ships, and it needs no exclusion list of its own to keep in step.
    """
    listed = subprocess.check_output(["git", "ls-files", "--cached", "--others",
                                      "--exclude-standard"], cwd=ROOT)
    return [p for p in listed.decode("utf-8").splitlines() if p]


def documents_carrying(kind):
    """Every tracked file with a region of this kind, discovered rather than written down."""
    found = []
    for rel in tracked_files():
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        try:
            text = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if any(opens(kind, line) for line in text.splitlines()):
            found.append(rel)
    return sorted(found)


class EveryMarkedListNamesTheSetTheCodeOwns(unittest.TestCase):
    """T-134, generalised by T-139 on the project owner's ruling of 2026-08-15: the guarded thing is
    *any* marked list of a set the code owns, not the command lists.

    T-134 guarded the commands and stopped, correctly for its scope. Nothing generalised it, so the
    next enumerated set to drift was the next one nobody was watching: T-138 shipped a third advisory
    line and left `README.md` naming two, caught four days later by a person's grep. That is the
    third instance of one fault - T-073 was the first - which is evidence about the class.

    **A marker is a claim of completeness, not a claim of importance.** It is why the fifteen problem
    prefixes are not marked: `README.md` describes one of them and never says it is describing all of
    them, so a region there would assert something the document does not mean."""

    def test_every_required_document_carries_its_region(self):
        """Without this, every assertion below passes on a tree where the markers were deleted -
        the region becomes unreadable, there is nothing to compare, and nothing fails (T-134 D2).

        This is the one place a document is named, and the naming is deliberate: discovery below
        finds what *has* a region, and no scan can tell you about a region someone removed."""
        for kind in KINDS:
            for where in kind.required:
                self.assertIsNotNone(
                    marked_region(os.path.join(ROOT, where), kind),
                    "%s carries no taskmd:%s region, so nothing checks the list in it"
                    % (where, kind.name))

    def test_each_marked_list_names_exactly_the_set_that_exists(self):
        """Both directions, over every document that opts in - **discovered**, not listed.

        T-134 rejected "the test naming the documents" as a third statement of where the surface is
        written, then shipped exactly that, so a third document opting in would have been read by
        nothing. The floor above and this sweep are different questions: which documents must have a
        region, and which documents have one."""
        cli = _cli()
        for kind in KINDS:
            carriers = documents_carrying(kind)
            self.assertTrue(carriers, "no document carries a taskmd:%s region, so this kind is "
                                      "declared and checked against nothing" % kind.name)
            expected = kind.owned(cli)
            self.assertTrue(expected, "the code owns no %s, so the comparison below is vacuous"
                                      % kind.name)
            for where in carriers:
                listed = marked_region(os.path.join(ROOT, where.replace("/", os.sep)), kind)
                self.assertEqual(expected, listed,
                                 "%s's %s list is behind: it does not name %s, and it names %s "
                                 "which do not exist"
                                 % (where, kind.name,
                                    sorted(expected - listed) or "nothing missing",
                                    sorted(listed - expected) or "nothing extra"))

    def test_a_name_mentioned_in_a_sentence_is_not_a_list(self):
        """On the real tree. `README.md` names commands in prose outside their region - an FAQ row,
        a paragraph about filters - and an advisory outside theirs, in the `WIDE ROW` paragraph that
        contrasts itself with them. None of that is checked, because the region is what declares an
        intent to be complete.

        Each half asserts its own premise first, so it fails rather than passing vacuously if the
        README stops mentioning anything outside its regions."""
        cli = _cli()
        readme = read(os.path.join(ROOT, "README.md"))
        for kind in KINDS:
            lines = readme.splitlines()
            begin = next(i for i, line in enumerate(lines) if opens(kind, line))
            end = next(i for i in range(begin + 1, len(lines)) if closes(kind, lines[i]))
            named = set(kind.pattern.findall("\n".join(lines[:begin] + lines[end + 1:])))
            self.assertTrue(named,
                            "this test is vacuous unless README.md names a %s outside the region; "
                            "it no longer does, so the case is untested" % kind.name)
            expected = kind.owned(cli)
            self.assertNotEqual(expected, named & expected,
                                "every %s now appears outside the region too, so this test can no "
                                "longer distinguish a mention from a list" % kind.name)


if __name__ == "__main__":
    unittest.main()
