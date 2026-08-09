#!/bin/sh
# taskmd launcher. Finds a Python and hands over; every argument is passed through untouched.
#
# There is deliberately nothing here to read. It knows no command, no flag and no field name, so
# it never needs editing when the tool grows one - and deleting it changes nothing except the way
# in, which is how that claim is tested. The logic all lives in the Python package
# (docs: taskmd/discovery.py for how the project is found).
#
# The two lines that are not interpreter discovery: PYTHONPATH is *replaced* with this script's own
# folder so the package imports from anywhere, and the working directory is left alone so the
# project is found from where you actually are.
#
# Replaced, not extended - a caller's existing PYTHONPATH is discarded for this one process. It
# used to be appended, and that made the launcher fail outright whenever the inherited value was
# relative or drive-lettered: joining with a hardcoded `:` only ever worked because the Windows
# shell layer rewrites the whole variable for a native process, and it abandons the rewrite as
# soon as one element is not POSIX-absolute. Python then got a POSIX string it could not read and
# reported taskmd missing. taskmd imports nothing but the standard library and itself, so there is
# nothing an inherited value could usefully add - and prepending is one ordering mistake away from
# importing somebody else's `taskmd`.

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PYTHONPATH="$here"
export PYTHONPATH

# A candidate has to *run*, not merely exist. On Windows `python3` is usually a Store stub that
# is on PATH, answers `command -v`, and then exits 49 telling you to visit a shop. Asking it to
# execute nothing is the cheapest question that tells the two apart.
for interpreter in python3 python py; do
    if command -v "$interpreter" >/dev/null 2>&1 && "$interpreter" -c "" >/dev/null 2>&1; then
        exec "$interpreter" -m taskmd "$@"
    fi
done

echo "taskmd: no Python found. Looked for: python3, python, py." >&2
exit 127
