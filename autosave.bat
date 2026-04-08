@echo off
:: ============================================================
:: autosave.bat — Sauvegarde automatique toutes les 30 min
:: Lancer en début de session, minimiser, laisser tourner
:: Fermer la fenêtre pour arrêter
:: ============================================================

echo.
echo ===================================
echo   AUTOSAVE ACTIVE
echo   Sauvegarde toutes les 30 minutes
echo   Fermez cette fenetre pour arreter
echo ===================================
echo.

:boucle
:: Attendre 30 minutes (1800 secondes)
timeout /t 1800 /nobreak

:: Vérifier s'il y a des changements
git diff --quiet && git diff --cached --quiet
if errorlevel 1 (
    echo [%time%] Modifications detectees, sauvegarde...
    git add .
    git commit -m "Autosave %date% %time%"
    git push origin master
    echo [%time%] Sauvegarde effectuee.
) else (
    echo [%time%] Aucune modification, rien a sauvegarder.
)

goto boucle
