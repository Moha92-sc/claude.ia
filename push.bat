@echo off
:: ============================================================
:: push.bat — Synchronisation rapide vers GitHub
:: Copier ce fichier à la racine de chaque projet
:: Double-cliquer pour pusher en un clic
:: ============================================================

echo.
echo ===================================
echo   SYNCHRONISATION GITHUB
echo ===================================
echo.

:: Demander le message de commit
set /p MSG="Decrivez ce que vous avez fait : "

:: Verifier qu'un message a ete saisi
if "%MSG%"=="" (
    echo ERREUR : message vide. Abandon.
    pause
    exit /b 1
)

:: Executer git save + push
echo.
echo [1/2] Sauvegarde locale...
git add . && git commit -m "%MSG%"

echo.
echo [2/2] Envoi sur GitHub...
git push origin master

echo.
echo ===================================
echo   DONE ! Projet mis a jour.
echo ===================================
echo.
pause
