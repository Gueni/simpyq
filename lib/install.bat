@echo off
SET CMD_NAME=simquery

REM Get absolute path to cli.py
FOR %%I IN (cli.py) DO SET ABS_PATH=%%~fI

REM Custom bin folder
SET CUSTOM_BIN=%USERPROFILE%\simquery-cli-bin
IF NOT EXIST "%CUSTOM_BIN%" mkdir "%CUSTOM_BIN%"

REM Create the simquery.bat
ECHO @echo off > "%CUSTOM_BIN%\%CMD_NAME%.bat"
ECHO python "%ABS_PATH%" %%* >> "%CUSTOM_BIN%\%CMD_NAME%.bat"

REM Check if folder is in PATH
echo %PATH% | find /I "%CUSTOM_BIN%" >nul
IF ERRORLEVEL 1 (
    echo.
    echo ⚠️  You must add "%CUSTOM_BIN%" to your system PATH manually:
    echo 👉  Control Panel > System > Environment Variables > PATH
    echo    Add: %CUSTOM_BIN%
    echo.
) ELSE (
    echo ✅ '%CMD_NAME%' installed and ready to use.
)

pause
