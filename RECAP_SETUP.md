# Récapitulatif — Setup GitHub + Claude Code
**Date de mise en place :** 2026-04-08
**Compte GitHub :** Moha92-sc

---

## Ce qui a été mis en place

### 1. Authentification GitHub
- `gh` CLI installé et authentifié
- Email anonyme configuré : `199062569+Moha92-sc@users.noreply.github.com`
- Identité Git : `Lehouali`

### 2. Alias Git (raccourcis)
```cmd
git config --global alias.save "!git add . && git commit -m"
git config --global alias.sync "!git pull && git push"
git config --global alias.etat "status"
```
| Commande | Action |
|----------|--------|
| `git save "message"` | Ajoute tout + commit |
| `git sync` | Pull + Push en une fois |
| `git etat` | Voir les fichiers modifiés |

### 3. Dépôts GitHub créés
| Dépôt | Visibilité | Contenu |
|-------|-----------|---------|
| `Moha92-sc/claude.ia` | Public | Outils, scripts, guides |
| `Moha92-sc/jumeau-numerique-pia` | Privé | Projet Jumeau Numérique PIA |

### 4. Scripts disponibles dans `claude.ia`

| Script | Rôle | Quand l'utiliser |
|--------|------|-----------------|
| `nouveau_projet.bat` | Crée projet + structure + GitHub | Début d'un nouveau projet |
| `push.bat` | Push rapide avec message | Après une modification |
| `pull.bat` | Récupère le travail depuis GitHub | Sur l'autre PC |
| `fin_session.bat` | Sauvegarde + journal de session | Avant de fermer Claude Code |
| `autosave.bat` | Sauvegarde automatique toutes les 30 min | En début de session |

### 5. Fichiers de configuration
- `template.gitignore` — à copier dans chaque nouveau projet
- `GUIDE_GITHUB_CLAUDE.md` — guide complet Git + GitHub + Claude Code

---

## Workflow quotidien

### Solo (1 PC)
```
Début    → double-clic autosave.bat (minimiser)
Travail  → Claude Code
Fin      → double-clic fin_session.bat
```

### Multi-PC
```
PC Principal  → travail → git save "..." → git push origin master
Autre PC      → git pull → travail → git save "..." → git push origin master
```

### Nouveau projet
```
double-clic nouveau_projet.bat → répond aux questions → projet créé sur GitHub
```

---

## Sur l'autre PC — Installation (une seule fois)

```cmd
:: 1. Installer git → https://git-scm.com
:: 2. Installer gh  → https://cli.github.com
:: 3. Authentification
gh auth login

:: 4. Configurer Git
git config --global user.name "Lehouali"
git config --global user.email "199062569+Moha92-sc@users.noreply.github.com"

:: 5. Alias
git config --global alias.save "!git add . && git commit -m"
git config --global alias.sync "!git pull && git push"
git config --global alias.etat "status"

:: 6. Récupérer tous les outils
gh repo clone Moha92-sc/claude.ia

:: 7. Récupérer un projet
gh repo clone Moha92-sc/jumeau-numerique-pia
```

---

## Règles importantes

1. **Toujours `--private`** pour les projets pro
2. **Jamais versionner** : `*.docx`, `*.xlsx`, `*.pdf`, `node_modules/`, fichiers BIM
3. **Toujours inclure** : `CLAUDE.md`, scripts, `.gitignore`, `README.md`
4. **Avant de fermer** : remplir "Reprendre ici" dans `CLAUDE.md` + `fin_session.bat`
5. **Nouveau projet** : `git init` + GitHub en **premier**, avant de commencer

---

## Dépôts GitHub actifs

- **claude.ia** → https://github.com/Moha92-sc/claude.ia
- **jumeau-numerique-pia** → https://github.com/Moha92-sc/jumeau-numerique-pia (privé)
