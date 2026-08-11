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
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")   # where the taskmd package lives (T-083)
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


class MarksWhatCannotBeStarted(unittest.TestCase):
    """T-102 — the sort key `order` already computes, printed instead of discarded.

    Blocked-last says a boundary exists without saying where it falls, and `list --open` is the
    view that answers *what do I work on next*. The project that reported this checked by hand and
    then had to write the answer into a handoff so the next session would not start a task that
    cannot move.

    The shape rules are `## Ordering` in the schema config; these tests assert them, and in
    particular that the title stays the last field for anyone who cuts it.
    """

    FIXTURE = os.path.join(FIXTURES, "ordering")
    UNBLOCKED = os.path.join(FIXTURES, "alt-project")

    def cells(self, out):
        return [line.split("\t") for line in out.splitlines() if line.strip()]

    def titles(self, root):
        return dict((t["id"], t["title"]) for t in json.loads(run("list", "--json",
                                                                  "--root", root)[1]))

    def test_the_blocked_row_says_so(self):
        code, out = run("list", "--root", self.FIXTURE)
        self.assertEqual(code, 0, out)
        self.assertEqual(dict((c[0], c[-1]) for c in self.cells(out))["T-002"], "blocked", out)

    def test_every_startable_row_says_it_is_not(self):
        code, out = run("list", "--root", self.FIXTURE)
        marks = dict((c[0], c[-1]) for c in self.cells(out))
        for tid in ("T-001", "T-003", "T-004"):
            self.assertEqual(marks[tid], "-", out)

    def test_the_title_is_still_the_field_before_it(self):
        """Appending after the title is what keeps this a non-breaking change: every field a
        caller already cuts stays where it was."""
        code, out = run("list", "--root", self.FIXTURE)
        titles = self.titles(self.FIXTURE)
        for row in self.cells(out):
            self.assertEqual(row[-2], titles[row[0]], out)

    def test_limit_one_has_the_same_shape(self):
        """Project-wide rather than per-call — `--limit 1` must not drop the column because the
        single row it returned happens to be startable."""
        code, out = run("list", "--limit", "1", "--root", self.FIXTURE)
        self.assertEqual(self.cells(out)[0][-1], "-", out)

    def test_a_project_with_nothing_blocked_is_unchanged(self):
        """The omit-when-unused rule under `## Views`: no blocked task, no column, so the title
        is last exactly as it was before this existed."""
        self.assertFalse(any(t["blocked"] for t in
                             json.loads(run("list", "--json", "--root", self.UNBLOCKED)[1])),
                         "this fixture is only useful while nothing in it is blocked")
        code, out = run("list", "--root", self.UNBLOCKED)
        self.assertEqual(code, 0, out)
        titles = self.titles(self.UNBLOCKED)
        for row in self.cells(out):
            self.assertEqual(row[-1], titles[row[0]], out)

    def test_the_mark_is_derived_and_not_the_status_column_echoed(self):
        """The reported case exactly: the task that could not be started was `proposed`.

        `is_blocked` is an open dependency and never a status value, so a project whose blocked
        task is marked anything at all must still see it. In `ordering/` the two coincide, which
        would let a wrong implementation pass every test above.
        """
        temp = tempfile.mkdtemp()
        try:
            for name in os.listdir(self.FIXTURE):
                s, d = os.path.join(self.FIXTURE, name), os.path.join(temp, name)
                shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)
            held = [os.path.join(temp, "tasks", n) for n in os.listdir(os.path.join(temp, "tasks"))
                    if n.startswith("T-002")][0]
            with open(held, encoding="utf-8") as fh:
                text = fh.read()
            with open(held, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text.replace("status: blocked", "status: proposed", 1))

            code, out = run("list", "--root", temp)
            self.assertEqual(code, 0, out)
            row = [c for c in self.cells(out) if c[0] == "T-002"][0]
            self.assertNotIn("blocked", row[1:-1],
                             "the fixture must no longer say blocked in any field but the mark")
            self.assertEqual(row[-1], "blocked", out)
        finally:
            shutil.rmtree(temp, ignore_errors=True)

    def test_json_carries_it_whatever_the_project_looks_like(self):
        """The contract surface does not omit — a caller should not have to know what the
        project looks like today."""
        for task in json.loads(run("list", "--json", "--root", self.UNBLOCKED)[1]):
            self.assertIn("blocked", task)


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


class FiltersOnAFieldNoVocabularyEnumerates(unittest.TestCase):
    """T-087. The schema promises that a field it does not enumerate is carried, and that naming it
    in a view surfaces it with no code change. That held for both views and broke at the filter —
    the one place a reader goes once the view is long. `work_package` was the field that found it,
    on the day this repository published.

    Every other filter test here uses a vocabulary, which is why the gap survived: the case that
    fails is the one no test had a shape for."""

    def test_a_stored_field_the_schema_does_not_enumerate_can_be_selected_on(self):
        code, out = run("list", "--work_package", "v0.2", "--open", "--root", ROOT)
        self.assertEqual(code, 0, out)
        self.assertTrue(ids(out), "no rows; the filter matched nothing at all")
        for line in out.splitlines():
            if line.strip():
                self.assertIn("v0.2", line)

    def test_a_value_nothing_carries_is_an_empty_answer_not_an_error(self):
        """The maintainer's ruling: with no list to check against, the tool cannot tell a typo from
        an empty bucket, so any error it printed would be a guess. Exit 0, no rows."""
        code, out = run("list", "--work_package", "v0.22", "--root", ROOT)
        self.assertEqual(code, 0, out)
        self.assertEqual([], ids(out))

    def test_the_field_name_is_still_checked_and_the_new_ones_are_offered(self):
        """The half that stays validated — the likelier typo — and the place a reader finds the
        spelling of the half that does not."""
        code, out = run("list", "--work_pakcage", "v0.2", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("--work_package", out)

    def test_the_accepted_set_comes_from_the_config_not_from_the_tasks(self):
        """An accepted set read off current contents would make a command's validity depend on when
        it runs. `alt-project` names its own view fields, and they are what it must offer."""
        schema = cli.load_schema(os.path.join(FIXTURES, "alt-project"))
        offered = cli.filter_names(schema)
        for name in list(schema.context_fields) + list(schema.index_columns):
            self.assertIn(name, offered, "a field this project shows but cannot filter on")


class RejectsWhatItCannotAnswer(unittest.TestCase):

    def test_an_unknown_filter_value_names_what_is_accepted(self):
        code, out = run("list", "--status", "nonsense", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("proposed", out)

    def test_an_unknown_filter_name_is_reported(self):
        code, out = run("list", "--wat", "x", "--root", ROOT)
        self.assertEqual(code, 2, out)

    def test_an_unknown_filter_name_is_reported_without_a_value(self):
        """T-113. The shape was checked before the name, so the *likelier* typing — a flag
        remembered wrongly and typed alone — was answered `--wat needs a value`, which invites the
        reader to supply one and reach the useful message by a second mistake."""
        code, out = run("list", "--wat", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("unknown filter", out)
        self.assertIn("accepts:", out)

    def test_a_known_filter_with_no_value_still_says_so(self):
        """The branch the reorder must not swallow: `--status` is real, so the missing value is the
        actual complaint. Moving the name check first must not answer this one `unknown filter`."""
        code, out = run("list", "--status", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("needs a value", out)

    def test_limit_with_no_value_still_says_so(self):
        """`--limit` is accepted but is not a filter, so it is absent from the accepted set the
        name check consults. Recognising names first would reject it as unknown unless it is
        recognised too — invisible in the two tests above, since both use real filters."""
        code, out = run("list", "--limit", "--root", ROOT)
        self.assertEqual(code, 2, out)
        self.assertIn("needs a value", out)

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
