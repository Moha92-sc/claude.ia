@echo off
:: ============================================================
:: pull.bat — Recuperer le travail depuis GitHub
:: Copier ce fichier a la racine de chaque projet
:: Double-cliquer sur l'autre PC pour recuperer le travail
:: ============================================================

echo.
echo ===================================
echo   RECUPERATION DEPUIS GITHUB
echo ===================================
echo.

git pull origin master

echo.
echo ===================================
echo   DONE ! Projet a jour.
echo ===================================
echo.
pause
