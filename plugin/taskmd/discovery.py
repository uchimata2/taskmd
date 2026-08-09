#!/usr/bin/env python
"""Find the project a command is being run *in*, so a clone works with nothing named.

This is the one home for the rule. The CLI's `--root` is the override; everything else asks here.

The rule
--------
Starting at the working directory and walking **upwards**, the first folder that is a taskmd
project is the root. A folder is a project if either mark is present:

- `.taskmd/config.md` — the project wrote a config, whatever it calls its tasks folder; or
- a folder with the **default** `tasks_dir` name — the project wrote no config, so the shipped
  default is its schema and that default names the folder.

Nearest wins, so a project nested inside another is worked on its own — the same rule `check`
already uses to keep this repository's deliberately-broken fixtures out of its own report.

Two markers rather than one, because either alone is wrong
----------------------------------------------------------
The config alone would fail on any project that never wrote one — including this repository, which
runs on the shipped default and is the tree the feature has to be proven on. It would also mean a
clone had to write a config before the first command worked, which is precisely the "no install"
property this tool is built on: clone it and run it.

The tasks folder alone would fail on a project that renamed it, since the new name is only knowable
from the config that has not been found yet. Reading the default's name out of the shipped file
rather than repeating it here keeps that fact in one place.

`.git` is not a marker: nothing in this method assumes version control, and a project may be a
folder on a disk. An environment variable is not one either — a value somebody has to remember to
set is exactly the kind of setup this is avoiding.

Pure standard library.
"""

import os

from .schema import DEFAULT_CONFIG, PROJECT_CONFIG, read, split_front_matter


def default_tasks_dir():
    """The `tasks_dir` the shipped default declares — read, never repeated."""
    fields, _ = split_front_matter(read(DEFAULT_CONFIG))
    return fields.get("tasks_dir", "")


def is_project(folder, tasks_dir):
    """True if `folder` is a taskmd project in its own right.

    `tasks_dir` is the caller's: discovery has no schema yet and passes the default's, while
    `check` passes the resolved one so a project that renamed its folder still recognises its
    own nested projects.
    """
    return (os.path.isfile(os.path.join(folder, PROJECT_CONFIG)) or
            bool(tasks_dir) and os.path.isdir(os.path.join(folder, tasks_dir)))


def find_root(start=None):
    """The nearest project at or above `start` (default: the working directory), or None."""
    tasks_dir = default_tasks_dir()
    folder = os.path.abspath(start if start is not None else os.getcwd())
    while True:
        if is_project(folder, tasks_dir):
            return folder
        parent = os.path.dirname(folder)
        if parent == folder:
            return None
        folder = parent


def not_found_message():
    """Why no command can start, in terms of what the reader can act on.

    It names the two marks and the default folder, and **no path** — printing where the search
    started would put one machine's disk into output that has to be identical on every platform,
    and the reader already knows where they are.
    """
    return ("No taskmd project here. Looking upwards from the working directory, no folder holds "
            "%s or a '%s' folder. Run the command inside a project, or name one with --root."
            % (PROJECT_CONFIG.replace("\\", "/"), default_tasks_dir()))
