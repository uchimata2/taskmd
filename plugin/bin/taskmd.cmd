@echo off
rem taskmd entry point for cmd and PowerShell - the Windows twin of bin/taskmd, and as empty.
rem
rem Two files rather than one because no single name is typeable on both platforms: an
rem extensionless POSIX script is not executable through a PATH lookup here, and .cmd is in the
rem default PATHEXT where .sh and .ps1 are not.
rem
rem That was an assumption until 2026-08-22 (T-207), when the single write was attempted and
rem refused. With only the extensionless file on PATH:
rem   cmd.exe   'taskmd' is not recognized as an internal or external command   exit 1
rem   pwsh 7    resolves the file, then produces no output and no exit code
rem PATHEXT was .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL - .cmd in it, .sh and
rem .ps1 not. The PowerShell half is the worse failure of the two: it looks like a command that ran.
rem The day an extensionless script starts working through a PATH lookup here, delete this file.
rem
rem Being on PATH is the design and not a guarantee - see the twin, which carries the whole of why.
rem On Windows this is the file a reader opens when the command was not found, so it says the one
rem thing that reader needs: the way in that does not depend on PATH is in
rem ..\skills\taskmd\SKILL.md, stated once there and not copied here.
rem
rem It delegates to taskmd.ps1 one directory up rather than repeating interpreter discovery.
rem -NoProfile keeps a user's profile out of it; -ExecutionPolicy Bypass is scoped to this one
rem process and is what lets an adopter on the default Restricted policy run it at all.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\skills\taskmd\taskmd.ps1" %*
exit /b %ERRORLEVEL%
