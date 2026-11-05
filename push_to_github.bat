@echo off
cd /d "%~dp0"
title Push OmniNemotron to GitHub
echo.
echo ========================================================
echo       Pushing OmniNemotron to GitHub
echo       Repository: https://github.com/adharshraj77/OmniNemotron.git
echo       Branch: main
echo ========================================================
echo.
echo Executing git push...
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================================
    echo  SUCCESS: Code pushed to GitHub successfully!
    echo  View repository: https://github.com/adharshraj77/OmniNemotron
    echo ========================================================
) else (
    echo.
    echo If GitHub asks for authentication, sign in with your browser or Personal Access Token.
)
echo.
pause
