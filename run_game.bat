@echo off
rem Double-click to run the game for testing (same as: uv run python -m fantasygame).
rem The real packaged .exe comes from Phase 0, piece 4.

cd /d "%~dp0"
set "PATH=%USERPROFILE%\.local\bin;%PATH%"

uv run python -m fantasygame %*
if errorlevel 1 (
    echo.
    echo The game stopped with an error - see the messages above.
    pause
)
