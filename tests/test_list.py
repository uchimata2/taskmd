#!/usr/bin/env python
"""Proof for T-022: the fourth command, and the ordering rule shown to matter.

The ordering tests are the point. "Highest value, lowest effort, dependencies first" has two
readings, and the cheap one is wrong in a way that only shows on a case where the two disagree —
so `tests/fixtures/ordering/` is built precisely so they do, and the test asserts the reading the
owner chose rather than whichever one the code happens to implement.

  python tests/test_list.py
"""

import io
import json
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
    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        code = cli.main(list(argv))
    finally:
        sys.stdout = stdout
    return code, buffer.getvalue()


def ids(out):
    """The first tab-separated field of every line — the ids, in the order printed."""
    return [line.split("\t")[0] for line in out.splitlines() if line.strip()]


class OrdersByTheRule(unittest.TestCase):
    """`tests/fixtures/ordering/` — four tasks built so the two readings disagree.

    T-001  low / xs, blocks T-002      T-003  high / s
    T-002  critical / l, blocked       T-004  no estimates at all
    """

    FIXTURE = os.path.join(FIXTURES, "ordering")

    def test_a_cheap_blocker_is_pulled_ahead_by_what_it_releases(self):
        code, out = run("list", "--root", self.FIXTURE)
        self.assertEqual(code, 0, out)
        self.assertEqual(ids(out)[0], "T-001",
                         "T-001 is the cheapest, least valuable task in the project; it comes "
                         "first only because it releases T-002. Got:\n" + out)

    def test_the_plain_reading_would_have_answered_differently(self):
        """The guard on the test above: if effective value were dropped and each task ranked on
        its own, T-003 would lead. A change that silently reverts the rule fails here."""
        code, out = run("list", "--root", self.FIXTURE)
        self.assertNotEqual(ids(out)[0], "T-003", out)

    def test_blocked_tasks_are_listed_but_sort_last(self):
        code, out = run("list", "--root", self.FIXTURE)
        self.assertIn("T-002", out, "a blocked task must still be listed")
        self.assertEqual(ids(out)[-1], "T-002", out)

    def test_a_task_with_no_estimates_is_still_listed(self):
        code, out = run("list", "--root", self.FIXTURE)
        order = ids(out)
        self.assertIn("T-004", order)
        self.assertGreater(order.index("T-004"), order.index("T-003"),
                           "an unestimated task sorts after estimated ones, not before")

    def test_the_whole_order_is_the_documented_one(self):
        code, out = run("list", "--root", self.FIXTURE)
        self.assertEqual(ids(out), ["T-001", "T-003", "T-004", "T-002"], out)

    def test_limit_one_is_the_next_task(self):
        code, out = run("list", "--limit", "1", "--root", self.FIXTURE)
        self.assertEqual(code, 0, out)
        self.assertEqual(ids(out), ["T-001"], out)

    def test_the_answer_is_reproducible(self):
        first = run("list", "--root", self.FIXTURE)[1]
        second = run("list", "--root", self.FIXTURE)[1]
        self.assertEqual(first, second)


class WorksWithoutEstimates(unittest.TestCase):
    """Both keys `none`: the tool must still list, and must not invent a ranking."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        src = os.path.join(FIXTURES, "ordering")
        for name in os.listdir(src):
            s, d = os.path.join(src, name), os.path.join(self.dir, name)
            shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)
        config = os.path.join(self.dir, ".taskmd", "config.md")
        with open(config, encoding="utf-8") as fh:
            text = fh.read()
        text = text.replace("value_field: business_value", "value_field: none")
        text = text.replace("effort_field: effort", "effort_field: none")
        with open(config, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_ordering_degrades_to_blocked_last_then_id(self):
        code, out = run("list", "--root", self.dir)
        self.assertEqual(code, 0, out)
        self.assertEqual(ids(out), ["T-001", "T-003", "T-004", "T-002"], out)

    def test_no_error_is_raised(self):
        code, out = run("check", "--root", self.dir)
        self.assertEqual(code, 0, out)


class UsesTheProjectsOwnVocabulary(unittest.TestCase):
    """`alt-project` renames the effort field to `size` and declares no value field at all.

    Nothing in the filter or the ordering may know the words `effort`, `business_value`, `xs` or
    `critical` — they are one project's vocabulary, and T-002 criterion 7 forbids a built-in list.
    """

    FIXTURE = os.path.join(FIXTURES, "alt-project")

    def test_it_lists_and_orders_on_the_renamed_field(self):
        code, out = run("list", "--root", self.FIXTURE)
        self.assertEqual(code, 0, out)
        self.assertTrue(ids(out), out)

    def test_a_filter_takes_this_projects_status_word(self):
        code, out = run("list", "--state", "todo", "--root", self.FIXTURE)
        self.assertEqual(code, 0, out)
        for line in out.splitlines():
            if line.strip():
                self.assertIn("todo", line)

    def test_the_default_vocabulary_is_not_accepted_here(self):
        code, out = run("list", "--state", "proposed", "--root", self.FIXTURE)
        self.assertEqual(code, 2, out)
        self.assertIn("todo", out, "the error must name what this project does accept")


class RejectsWhatItCannotAnswer(unittest.TestCase):

    def test_an_unknown_filter_value_names_what_is_accepted(self):
        code, out = run("list", "--status", "nonsense", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("proposed", out)

    def test_an_unknown_filter_name_is_reported(self):
        code, out = run("list", "--wat", "x", "--root", ROOT)
        self.assertEqual(code, 2, out)

    def test_nothing_is_printed_before_the_error(self):
        code, out = run("list", "--status", "nonsense", "--root", ROOT)
        self.assertNotIn("\t", out, "the error must arrive before any listing output")


class RendersBothForms(unittest.TestCase):

    def test_the_line_form_is_tab_separated(self):
        code, out = run("list", "--limit", "1", "--root", ROOT)
        self.assertEqual(code, 0, out)
        self.assertGreaterEqual(len(out.splitlines()[0].split("\t")), 4, out)

    def test_json_parses_and_carries_the_same_ids(self):
        code, out = run("list", "--json", "--root", ROOT)
        self.assertEqual(code, 0, out)
        data = json.loads(out)
        line = run("list", "--root", ROOT)[1]
        self.assertEqual([t["id"] for t in data], ids(line))


class WritesNothing(unittest.TestCase):
    """`docs/SCOPE.md` §1 Invisibility, and T-022's no-cache constraint: listing is a read."""

    def snapshot(self, folder):
        out = {}
        for base, dirs, files in os.walk(folder):
            for name in files:
                path = os.path.join(base, name)
                with open(path, "rb") as fh:
                    out[os.path.relpath(path, folder)] = fh.read()
        return out

    def test_the_tree_is_byte_identical_afterwards(self):
        folder = os.path.join(FIXTURES, "ordering")
        before = self.snapshot(folder)
        run("list", "--root", folder)
        run("list", "--json", "--root", folder)
        run("list", "--limit", "1", "--root", folder)
        self.assertEqual(self.snapshot(folder), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
