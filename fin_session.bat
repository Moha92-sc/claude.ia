@echo off
:: ============================================================
:: fin_session.bat — A lancer avant de fermer Claude Code
:: Sauvegarde le travail + écrit dans le journal
:: ============================================================

echo.
echo ===================================
echo   FIN DE SESSION
echo ===================================
echo.

:: Résumé de la session
set /p RESUME="Ce que tu as fait aujourd'hui : "
if "%RESUME%"=="" set RESUME=Session de travail

:: Prochaine étape
set /p SUITE="Quoi faire à la prochaine session : "
if "%SUITE%"=="" set SUITE=A definir

:: Git save + push
echo.
echo [1/2] Sauvegarde Git...
git add .
git commit -m "Session %date% : %RESUME%"
git push origin master

:: Écrire dans le journal
echo.
echo [2/2] Mise a jour du journal...
echo. >> journal.md
echo ## %date% >> journal.md
echo **Fait :** %RESUME% >> journal.md
echo **Suite :** %SUITE% >> journal.md

:: Push du journal
git add journal.md
git commit -m "Journal : %date%"
git push origin master

echo.
echo ===================================
echo   SESSION SAUVEGARDEE !
echo ===================================
echo.
pause
