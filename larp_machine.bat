@echo off
"%~dp0python\python.exe" "%~dp0app\larp_machine.py" %*
exit /b %errorlevel%
