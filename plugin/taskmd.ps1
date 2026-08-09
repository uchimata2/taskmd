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

# PYTHONPATH is replaced, not extended, exactly as in taskmd.sh - a caller's existing value is
# discarded for this one process. This launcher never had the bug that made taskmd.sh replace it
# (it joined with the platform's own separator and a native path, and passed all four values it
# was tested against). It is written the same way regardless, because R-20 says the two behave
# identically, and two launchers that differ only in what they do with an inherited variable is
# the kind of difference nobody discovers until it matters.
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:PYTHONPATH = $here

# A candidate has to *run*, not merely exist: the Store stub is on PATH, answers Get-Command, and
# then exits 49 telling you to visit a shop. Asking it to execute nothing tells the two apart.
#
# The no-op is `pass` and not the empty string, which is what taskmd.sh can afford to use. Windows
# PowerShell 5.1 drops an empty-string argument on its way to a native command, so `-c ""` arrives
# as a bare `-c`; Python then answers "Argument expected for the -c option" and exits 2, and every
# interpreter on the machine is reported missing. PowerShell 7 passes it through, which is why the
# form survived here for as long as it did - this project drives the launcher from 7, and 5.1 is
# what an adopter has by default.
foreach ($interpreter in 'py', 'python3', 'python') {
    $found = Get-Command $interpreter -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $found) { continue }
    & $found.Source -c "pass" *> $null
    if ($LASTEXITCODE -eq 0) {
        & $found.Source -m taskmd @args
        exit $LASTEXITCODE
    }
}

[Console]::Error.WriteLine('taskmd: no Python found. Looked for: py, python3, python.')
exit 127
