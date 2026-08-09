@echo off
rem taskmd entry point for cmd and PowerShell - the Windows twin of bin/taskmd, and as empty.
rem
rem Two files rather than one because no single name is typeable on both platforms: an
rem extensionless POSIX script is not executable through a PATH lookup here, and .cmd is in the
rem default PATHEXT where .sh and .ps1 are not.
rem
rem It delegates to taskmd.ps1 one directory up rather than repeating interpreter discovery.
rem -NoProfile keeps a user's profile out of it; -ExecutionPolicy Bypass is scoped to this one
rem process and is what lets an adopter on the default Restricted policy run it at all.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\skills\taskmd\taskmd.ps1" %*
exit /b %ERRORLEVEL%
