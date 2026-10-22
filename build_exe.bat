@echo off
rem Builds the Windows game into build\win_amd64\ (fantasygame.exe + assets\).
rem To test on another PC, copy that whole folder across and double-click fantasygame.exe.

cd /d "%~dp0"
set "PATH=%USERPROFILE%\.local\bin;%PATH%"

if not exist build mkdir build
uv export --frozen --no-dev --no-hashes --no-emit-project -o build\requirements.txt || goto failed
uv run python setup.py build_apps || goto failed

echo.
echo Done: %~dp0build\win_amd64\fantasygame.exe
if "%CI%"=="" pause
exit /b 0

:failed
echo.
echo The build failed - see the messages above.
if "%CI%"=="" pause
exit /b 1
