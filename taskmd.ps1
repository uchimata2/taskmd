# taskmd launcher. Finds a Python and hands over; every argument is passed through untouched.
#
# The PowerShell twin of taskmd.sh, and deliberately as empty. It knows no command, no flag and no
# field name, so it never needs editing when the tool grows one - and deleting it changes nothing
# except the way in, which is how that claim is tested. The logic all lives in the Python package
# (docs: taskmd/discovery.py for how the project is found).
#
# `py` is tried first here and last in taskmd.sh, on purpose. On Windows `py` is the official
# launcher and picks a real interpreter, while `python3` is often the Store stub that opens a
# shop instead of running anything; on everything else `python3` is the one that exists.

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:PYTHONPATH = if ($env:PYTHONPATH) {
    $here + [IO.Path]::PathSeparator + $env:PYTHONPATH
} else { $here }

# A candidate has to *run*, not merely exist: the Store stub is on PATH, answers Get-Command, and
# then exits 49 telling you to visit a shop. Asking it to execute nothing tells the two apart.
foreach ($interpreter in 'py', 'python3', 'python') {
    $found = Get-Command $interpreter -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $found) { continue }
    & $found.Source -c "" *> $null
    if ($LASTEXITCODE -eq 0) {
        & $found.Source -m taskmd @args
        exit $LASTEXITCODE
    }
}

[Console]::Error.WriteLine('taskmd: no Python found. Looked for: py, python3, python.')
exit 127
