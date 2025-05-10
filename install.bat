@echo off
SET CMD_NAME=simpyq

REM Get current script directory
SET SCRIPT_DIR=%~dp0
SET CLI_PATH=%SCRIPT_DIR%cli.py

REM Remove trailing backslash from SCRIPT_DIR if exists
IF %SCRIPT_DIR:~-1%==\ SET SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

REM Target custom bin folder
SET CUSTOM_BIN=%USERPROFILE%\simpyq-cli-bin
IF NOT EXIST "%CUSTOM_BIN%" mkdir "%CUSTOM_BIN%"

REM Create the .bat launcher
ECHO @echo off > "%CUSTOM_BIN%\%CMD_NAME%.bat"
ECHO python "%CLI_PATH%" %%* >> "%CUSTOM_BIN%\%CMD_NAME%.bat"

REM Confirm PATH status
echo %PATH% | find /I "%CUSTOM_BIN%" >nul
IF ERRORLEVEL 1 (
    echo.
    echo ⚠️  You must add "%CUSTOM_BIN%" to your system PATH manually:
    echo 👉  Control Panel > System > Environment Variables > PATH
    echo    Add: %CUSTOM_BIN%
    echo.
) ELSE (
    echo ✅ '%CMD_NAME%' installed and ready to use from anywhere!
)

pause
