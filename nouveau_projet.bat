@echo off
:: ============================================================
:: nouveau_projet.bat — Crée un nouveau projet complet
:: Double-cliquer pour créer un projet Git + GitHub en 1 clic
:: ============================================================

echo.
echo ===================================
echo   CREATION D'UN NOUVEAU PROJET
echo ===================================
echo.

:: Nom du projet
set /p NOM="Nom du projet (sans espaces, ex: r17-apsad) : "
if "%NOM%"=="" (
    echo ERREUR : nom vide. Abandon.
    pause
    exit /b 1
)

:: Description courte
set /p DESC="Description courte : "

:: Dossier parent
set /p DOSSIER="Dossier parent (ex: C:\Users\moham\Documents) : "
if "%DOSSIER%"=="" set DOSSIER=C:\Users\moham\Documents

:: Créer le dossier
mkdir "%DOSSIER%\%NOM%"
cd /d "%DOSSIER%\%NOM%"

:: Créer la structure
mkdir scripts
mkdir output
mkdir templates

:: Créer .gitignore
(
echo # Fichiers generes
echo output/
echo *.docx
echo *.xlsx
echo *.xls
echo *.pdf
echo *.pptx
echo.
echo # Python
echo __pycache__/
echo *.pyc
echo .env
echo venv/
echo.
echo # Node
echo node_modules/
echo dist/
echo.
echo # Systeme
echo Thumbs.db
echo desktop.ini
echo *.tmp
) > .gitignore

:: Créer CLAUDE.md
(
echo # %NOM%
echo.
echo ## Description
echo %DESC%
echo.
echo ## Date de création
echo %date%
echo.
echo ## Structure
echo - `scripts/` : scripts Python/JS
echo - `templates/` : modeles de documents
echo - `output/` : fichiers generés ^(ignores par Git^)
echo.
echo ## Reprendre ici
echo ^> A remplir avant chaque fin de session
echo.
echo ## Commandes utiles
echo ^> A remplir selon le projet
) > CLAUDE.md

:: Créer README.md
(
echo # %NOM%
echo.
echo %DESC%
echo.
echo ## Installation
echo ^`^`^`cmd
echo gh repo clone Moha92-sc/%NOM%
echo cd %NOM%
echo ^`^`^`
echo.
echo ## Structure
echo ^`^`^`
echo %NOM%/
echo ├── scripts/
echo ├── templates/
echo ├── output/      ^(ignore par Git^)
echo ├── CLAUDE.md
echo └── README.md
echo ^`^`^`
) > README.md

:: Copier push.bat et pull.bat depuis claude.ia
copy "C:\Users\moham\claude.ia\push.bat" push.bat >nul 2>&1
copy "C:\Users\moham\claude.ia\pull.bat" pull.bat >nul 2>&1

:: Init Git
git init
git add .
git commit -m "Init : %NOM% - %DESC%"

:: Créer dépôt GitHub privé
echo.
echo [GitHub] Creation du depot prive...
gh repo create %NOM% --private --source=. --remote=origin --push

echo.
echo ===================================
echo   PROJET CREE !
echo   Dossier : %DOSSIER%\%NOM%
echo   GitHub  : https://github.com/Moha92-sc/%NOM%
echo ===================================
echo.
pause
