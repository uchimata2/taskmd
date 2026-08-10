#!/usr/bin/env python
"""Proof for T-001: the schema is configuration, not code.

Three things are proven by running, not by reading:

1. A project with **no** config file works, on this repository's own real `tasks/`.
2. A second, deliberately different schema works — different id field, prefix, width, title
   field, folder, status field, vocabulary, edge names and derived names.
3. Every rule the config validator claims to enforce is shown **failing** on a case it should
   catch. A clean pass proves nothing on its own.

  python tests/test_schema.py
"""

import glob
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG = os.path.join(ROOT, "plugin", "skills", "taskmd")   # where the taskmd package lives (T-083)
sys.path.insert(0, PKG)

from taskmd.schema import (  # noqa: E402
    DEFAULT_CONFIG, SchemaError, load_schema, load_tasks, split_front_matter,
)

ALT = os.path.join(ROOT, "tests", "fixtures", "alt-project")

VALID = """---
id_field: id
id_prefix: T-
id_width: 3
title_field: title
tasks_dir: tasks
status_field: status
deliverables_field: deliverables
blocked_status: none
value_field: none
effort_field: none
after_write: none
open_statuses: [open]
context_fields: [status]
index_columns: [status]
---

## Edges

| Field | Kind | Derives |
| :--- | :--- | :--- |
| parent | hierarchy | children |
| blocked_by | dependency | blocks |
| related | soft | - |

## Vocabularies

| Field | Values |
| :--- | :--- |
| status | open, closed |
"""


def write(path, text):
    # newline="\n" so the fixture is byte-identical on every platform (carried lesson L-11).
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


class DefaultSchema(unittest.TestCase):
    """A clone with no configuration must work."""

    def test_no_config_file_falls_back_to_the_shipped_default(self):
        tmp = tempfile.mkdtemp()
        try:
            write(os.path.join(tmp, "tasks", "T-001-x.md"),
                  "---\nid: T-001\ntitle: X\nstatus: proposed\nphase: specify\n---\n")
            schema = load_schema(tmp)
            # `source` is deliberately relative to the *plugin* root, so an error message never
            # prints one machine's disk. Resolve it against PKG, not the working directory —
            # they were the same folder until the plugin became a subtree, and this assertion
            # passed on that coincidence rather than on what `_display` promises.
            self.assertEqual(os.path.abspath(os.path.join(PKG, schema.source.replace("/", os.sep))),
                             os.path.abspath(DEFAULT_CONFIG))
            self.assertEqual(len(load_tasks(tmp, schema)), 1)
        finally:
            shutil.rmtree(tmp)

    def test_the_shipped_default_passes_its_own_validator(self):
        schema = load_schema(ROOT)
        self.assertEqual(schema.id_prefix, "T-")
        self.assertEqual(schema.format_id(7), "T-007")
        self.assertEqual(schema.number_of("T-007"), 7)
        self.assertEqual(sorted(schema.edges), ["blocked_by", "parent", "related"])
        self.assertEqual(schema.edges["blocked_by"].derives, "blocks")
        self.assertEqual(schema.edges["related"].derives, "")
        self.assertTrue(schema.is_open("in_progress"))
        self.assertFalse(schema.is_open("done"))

    def test_this_repositorys_own_tasks_load_and_derive(self):
        """The real case, not a fixture: T-002 and T-004 store `blocked_by: [T-001]`,
        so T-001's `blocks` must be computed as exactly those two."""
        tasks = load_tasks(ROOT)
        self.assertIn("T-001", tasks)
        self.assertEqual(tasks["T-001"].derived["blocks"], ["T-002", "T-004"])
        self.assertEqual(tasks["T-002"].edges["blocked_by"], ["T-001"])
        self.assertEqual(tasks["T-001"].edges["blocked_by"], [])

    def test_unnamed_fields_are_carried_never_interpreted(self):
        carried = load_tasks(ROOT)["T-001"].extra
        self.assertIn("work_package", carried)
        self.assertIn("owner", carried)
        self.assertIsInstance(carried["work_package"], str)
        self.assertNotIn("status", carried)
        self.assertNotIn("blocked_by", carried)
        # `deliverables` used to be carried; the default schema now names it, so it is
        # interpreted and must have left the pass-through set.
        self.assertNotIn("deliverables", carried)

    def test_generated_views_and_templates_are_not_mistaken_for_tasks(self):
        """The index and both templates share the task folder and are not tasks.

        This used to match on the string `_templates`, and T-076 moved the templates out of
        that folder and in beside the tasks they become — so the folder skip in `load_tasks`
        no longer applies to them at all: the files are read, and discarded on their `id`.
        The old assertion did not start failing, it started passing **vacuously**, which is
        the worse outcome. Measured before replacing it, by giving a `_`-prefixed file a real
        id so it was genuinely loaded as a task: `assertFalse([])` still passed, and the form
        below caught it.

        The existence check is the same trap one level up — without it, deleting both
        templates would make this test greener rather than redder.
        """
        templates = glob.glob(os.path.join(ROOT, "tasks", "_*.md"))
        self.assertEqual(len(templates), 2, templates)
        tasks = load_tasks(ROOT)
        self.assertFalse([t for t in tasks.values() if t.name == "README.md"])
        self.assertFalse([t.name for t in tasks.values() if t.name.startswith("_")])


class AltSchema(unittest.TestCase):
    """A second schema, unlike the default in every configurable dimension."""

    def setUp(self):
        self.schema = load_schema(ALT)
        self.tasks = load_tasks(ALT, self.schema)

    def test_every_configurable_dimension_is_actually_different(self):
        s = self.schema
        self.assertEqual((s.id_field, s.id_prefix, s.id_width), ("ref", "ISSUE-", 4))
        self.assertEqual((s.title_field, s.status_field, s.tasks_dir),
                         ("name", "state", "issues"))
        self.assertEqual(s.format_id(7), "ISSUE-0007")
        self.assertEqual(sorted(s.edges), ["depends_on", "epic", "see_also"])
        self.assertEqual(sorted(s.vocabularies), ["size", "state"])
        self.assertTrue(s.is_open("waiting"))
        self.assertFalse(s.is_open("shipped"))

    def test_the_inverse_edges_are_computed_under_the_new_names(self):
        self.assertEqual(sorted(self.tasks), ["ISSUE-0001", "ISSUE-0002", "ISSUE-0003"])
        self.assertEqual(self.tasks["ISSUE-0003"].derived["stories"],
                         ["ISSUE-0001", "ISSUE-0002"])
        self.assertEqual(self.tasks["ISSUE-0001"].derived["unblocks"], ["ISSUE-0002"])
        self.assertEqual(self.tasks["ISSUE-0002"].edges["epic"], ["ISSUE-0003"])
        self.assertNotIn("stories", self.tasks["ISSUE-0003"].fields)  # derived, never stored

    def test_a_soft_edge_is_visible_from_the_end_that_does_not_store_it(self):
        """ISSUE-0002 stores `see_also: [ISSUE-0001]`. ISSUE-0001 stores nothing, and must still
        show the link — otherwise half the graph is invisible depending on which task you open."""
        self.assertEqual(self.tasks["ISSUE-0002"].edges["see_also"], ["ISSUE-0001"])
        self.assertEqual(self.tasks["ISSUE-0001"].edges["see_also"], [])
        self.assertEqual(self.tasks["ISSUE-0001"].links("see_also"), ["ISSUE-0002"])
        self.assertEqual(self.tasks["ISSUE-0002"].links("see_also"), ["ISSUE-0001"])

    def test_pass_through_survives_both_list_forms(self):
        extra = self.tasks["ISSUE-0002"].extra
        self.assertEqual(extra["area"], "exterior")
        self.assertEqual(len(extra["notes"]), 2)


class DeclaredDeliverables(unittest.TestCase):
    """The field is named by config, so nothing above the schema learns what it is called."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)

    def build(self, config, front_matter):
        write(os.path.join(self.tmp, ".taskmd", "config.md"), config)
        write(os.path.join(self.tmp, "tasks", "T-001-x.md"),
              "---\nid: T-001\ntitle: X\nstatus: open\n%s---\n" % front_matter)
        return load_tasks(self.tmp)["T-001"]

    def test_declared_paths_are_read_through_the_named_field(self):
        task = self.build(VALID, "deliverables: [docs/a.md, docs/b.md]\n")
        self.assertEqual(task.deliverables, ["docs/a.md", "docs/b.md"])

    def test_a_different_project_may_call_it_something_else(self):
        task = self.build(VALID.replace("deliverables_field: deliverables",
                                        "deliverables_field: produces"),
                          "produces: [out/report.pdf]\ndeliverables: [not-this-one.md]\n")
        self.assertEqual(task.deliverables, ["out/report.pdf"])
        self.assertIn("deliverables", task.extra)  # now just a carried field

    def test_none_means_the_project_does_not_track_them(self):
        task = self.build(VALID.replace("deliverables_field: deliverables",
                                        "deliverables_field: none"),
                          "deliverables: [docs/a.md]\n")
        self.assertEqual(task.deliverables, [])
        self.assertIn("deliverables", task.extra)

    def test_an_empty_declaration_is_not_a_path(self):
        self.assertEqual(self.build(VALID, "deliverables: []\n").deliverables, [])
        self.assertEqual(self.build(VALID, "deliverables: null\n").deliverables, [])

    def test_the_alt_project_runs_with_the_key_switched_off(self):
        self.assertEqual(load_schema(ALT).deliverables_field, "")
        self.assertEqual(load_tasks(ALT)["ISSUE-0001"].deliverables, [])


class LinksAreVisibleFromBothEnds(unittest.TestCase):
    """T-012: whichever task you open, you see every link it has — stored or derived."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)

    def build(self, *bodies):
        for i, body in enumerate(bodies, start=1):
            write(os.path.join(self.tmp, "tasks", "T-%03d-x.md" % i),
                  "---\nid: T-%03d\ntitle: Task %d\nstatus: proposed\nphase: specify\n%s---\n"
                  % (i, i, body))
        return load_tasks(self.tmp)

    def test_one_stored_side_is_enough(self):
        tasks = self.build("related: [T-002]\n", "")
        self.assertEqual(tasks["T-001"].links("related"), ["T-002"])
        self.assertEqual(tasks["T-002"].links("related"), ["T-001"])

    def test_both_sides_stored_collapses_to_one_entry(self):
        """Writing the link on both tasks is allowed — it must not show up twice."""
        tasks = self.build("related: [T-002]\n", "related: [T-001]\n")
        self.assertEqual(tasks["T-001"].links("related"), ["T-002"])
        self.assertEqual(tasks["T-002"].links("related"), ["T-001"])

    def test_named_inverses_are_reachable_through_the_same_accessor(self):
        tasks = self.build("", "parent: T-001\nblocked_by: [T-001]\n")
        self.assertEqual(tasks["T-001"].links("children"), ["T-002"])
        self.assertEqual(tasks["T-001"].links("blocks"), ["T-002"])
        self.assertEqual(tasks["T-002"].links("parent"), ["T-001"])
        self.assertEqual(tasks["T-002"].links("blocked_by"), ["T-001"])

    def test_a_self_link_is_ignored(self):
        tasks = self.build("related: [T-001]\n")
        self.assertEqual(tasks["T-001"].links("related"), [])

    def test_a_link_to_a_task_that_does_not_exist_is_ignored(self):
        tasks = self.build("related: [T-404]\n")
        self.assertEqual(tasks["T-001"].derived["related"], [])

    def test_this_repositorys_own_soft_links_resolve_both_ways(self):
        """The real case: T-010 stores `related: [T-004]`; T-004 stores nothing about T-010."""
        tasks = load_tasks(ROOT)
        self.assertNotIn("T-010", tasks["T-004"].edges["related"])  # T-004 stores nothing about it
        self.assertIn("T-010", tasks["T-004"].links("related"))     # and still sees it
        self.assertIn("T-004", tasks["T-010"].links("related"))


class ParsesTheRestrictedSubset(unittest.TestCase):

    def test_comments_are_stripped_and_nulls_normalised(self):
        fields, body = split_front_matter(
            "---\na: one  # trailing note\nb: [x, y]\nc: null\nd:\n  - p\n  - q\n---\nbody\n")
        self.assertEqual(fields["a"], "one")
        self.assertEqual(fields["b"], ["x", "y"])
        self.assertEqual(fields["c"], "")
        self.assertEqual(fields["d"], ["p", "q"])
        self.assertEqual(body, "body\n")


class RejectsBadConfig(unittest.TestCase):
    """Each case below is a rule the validator claims to enforce, shown failing."""

    def reject(self, text, expected):
        tmp = tempfile.mkdtemp()
        try:
            write(os.path.join(tmp, ".taskmd", "config.md"), text)
            with self.assertRaises(SchemaError) as caught:
                load_schema(tmp)
            self.assertIn(expected, str(caught.exception))
        finally:
            shutil.rmtree(tmp)

    def test_unknown_key(self):
        self.reject(VALID.replace("id_width: 3", "id_witdh: 3"), "unknown config key")

    def test_missing_key(self):
        self.reject(VALID.replace("tasks_dir: tasks\n", ""), "missing config key(s): tasks_dir")

    def test_the_shipped_config_warns_that_a_new_key_breaks_every_existing_one(self):
        """T-106. `test_missing_key` above is the mechanism; this is the warning that has to reach
        whoever is about to cause it.

        The constraint exists only as a conjunction — replace-not-merge, every key written, a
        missing key is an error — each documented separately and each individually right. A fact
        that is nowhere stated whole is one that gets rediscovered by being hit, which is how it
        surfaced (mid-plan, in T-100). So the sentence is asserted rather than trusted."""
        with open(DEFAULT_CONFIG, encoding="utf-8") as handle:
            shipped = handle.read()
        self.assertIn("Adding a key to this file is a breaking change", shipped)
        for premise in ("replaces", "must be **written**", "**missing** key is an error"):
            self.assertIn(premise, shipped)

    def test_id_width_not_a_number(self):
        self.reject(VALID.replace("id_width: 3", "id_width: wide"), "must be a whole number")

    def test_id_width_zero(self):
        self.reject(VALID.replace("id_width: 3", "id_width: 0"), "at least 1")

    def test_list_key_given_a_scalar(self):
        self.reject(VALID.replace("open_statuses: [open]", "open_statuses: open"),
                    "'open_statuses' must be a list")

    def test_unimplemented_edge_kind(self):
        self.reject(VALID.replace("| parent | hierarchy | children |",
                                  "| parent | contains | children |"),
                    "taskmd implements only")

    def test_soft_edge_claiming_an_inverse(self):
        self.reject(VALID.replace("| related | soft | - |", "| related | soft | siblings |"),
                    "a soft link is symmetric")

    def test_dependency_edge_deriving_nothing(self):
        self.reject(VALID.replace("| blocked_by | dependency | blocks |",
                                  "| blocked_by | dependency | - |"),
                    "must name what it derives")

    def test_derived_name_that_is_also_a_stored_field(self):
        self.reject(VALID.replace("| parent | hierarchy | children |",
                                  "| parent | hierarchy | related |"),
                    "is derived and also stored")

    def test_two_edges_deriving_the_same_name(self):
        self.reject(VALID.replace("| parent | hierarchy | children |",
                                  "| parent | hierarchy | blocks |"),
                    "two edges derive the same name")

    def test_open_status_outside_the_vocabulary(self):
        self.reject(VALID.replace("open_statuses: [open]", "open_statuses: [opne]"),
                    "not in the 'status' vocabulary")

    def test_status_field_with_no_vocabulary(self):
        self.reject(VALID.replace("status_field: status", "status_field: state"),
                    "no vocabulary declares it")

    def test_misshaped_table_header(self):
        self.reject(VALID.replace("| Field | Kind | Derives |", "| Field | Type | Derives |"),
                    "no table under '## Edges'")

    def test_short_table_row(self):
        self.reject(VALID.replace("| related | soft | - |", "| related | soft |"),
                    "expected 3")

    def test_no_front_matter(self):
        self.reject("# just prose\n", "no front-matter block")

    def test_blocked_status_absent(self):
        self.reject(VALID.replace("blocked_status: none\n", ""),
                    "missing config key(s): blocked_status")

    def test_blocked_status_outside_the_vocabulary(self):
        self.reject(VALID.replace("blocked_status: none", "blocked_status: stuck"),
                    "not in the 'status' vocabulary")

    def test_deliverables_field_absent(self):
        self.reject(VALID.replace("deliverables_field: deliverables\n", ""),
                    "missing config key(s): deliverables_field")

    def test_deliverables_field_given_a_list(self):
        self.reject(VALID.replace("deliverables_field: deliverables",
                                  "deliverables_field: [a, b]"),
                    "must be a field name or 'none'")

    def test_deliverables_field_that_is_an_edge(self):
        self.reject(VALID.replace("deliverables_field: deliverables",
                                  "deliverables_field: related"),
                    "also declared as an edge")

    def test_deliverables_field_that_is_derived(self):
        self.reject(VALID.replace("deliverables_field: deliverables",
                                  "deliverables_field: blocks"),
                    "derived from an edge")

    def test_deliverables_field_with_a_vocabulary(self):
        self.reject(VALID.replace("deliverables_field: deliverables",
                                  "deliverables_field: status"),
                    "not an enumerated value")

    def test_deliverables_field_colliding_with_the_id(self):
        self.reject(VALID.replace("deliverables_field: deliverables",
                                  "deliverables_field: id"),
                    "collides with id_field/title_field")


if __name__ == "__main__":
    unittest.main(verbosity=2)
