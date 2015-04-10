@echo off
set CXB_PATH=%~d0%~p0
set PYTHONPATH=%PYTHONPATH%;%CXB_PATH%\CX\Library
cd %CXB_PATH%
git pull

cd %CXB_PATH%
::if exist "%CXB_PATH%\AutomationReport\report" rd /q/s %CXB_PATH%\AutomationReport\report
::mkdir %CXB_PATH%\AutomationReport\report
ride.py