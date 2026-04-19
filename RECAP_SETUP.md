# Récapitulatif — Setup GitHub + Claude Code
**Date de mise en place :** 2026-04-08 (mis à jour 2026-04-19)
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
| `Moha92-sc/workspace` | Privé | Workspace complet |
| `Moha92-sc/SSI_DUBERNARD` | Privé | Projets SSI Dubernard |
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
- `config/CLAUDE_global_template.md` → copier dans `~/.claude/CLAUDE.md`
- `config/CLAUDE_workspace_template.md` → copier dans chaque projet
- `config/settings_template.json` → copier dans `~/.claude/settings.json`
- `config/mcp_config_template.json` → référence pour les MCP servers
- `config/claudeignore_template` → copier en `.claudeignore` dans chaque projet
- `template.gitignore` → copier en `.gitignore` dans chaque projet

### 6. Guides outils avancés
- `tools/GUIDE_SUPERPOWERS.md` — skills Claude Code (brainstorming, debug, TDD...)
- `tools/GUIDE_GRAPHIFY.md` — graphe de connaissance codebase
- `mempalace/GUIDE_MEMPALACE.md` — mémoire persistante entre sessions

---

## Sur l'autre PC — Installation complète (une seule fois)

```cmd
:: === ÉTAPE 1 : Outils de base ===
:: Installer git    → https://git-scm.com
:: Installer gh     → https://cli.github.com
:: Installer Node   → https://nodejs.org
:: Installer Python → https://python.org

:: === ÉTAPE 2 : Authentification ===
gh auth login

:: === ÉTAPE 3 : Configurer Git ===
git config --global user.name "Lehouali"
git config --global user.email "199062569+Moha92-sc@users.noreply.github.com"
git config --global alias.save "!git add . && git commit -m"
git config --global alias.sync "!git pull && git push"
git config --global alias.etat "status"

:: === ÉTAPE 4 : Installer Claude Code ===
npm install -g @anthropic-ai/claude-code

:: === ÉTAPE 5 : Récupérer les outils ===
gh repo clone Moha92-sc/claude.ia

:: === ÉTAPE 6 : Copier la config Claude ===
:: config/settings_template.json  → C:\Users\TON_USER\.claude\settings.json
:: config/CLAUDE_global_template.md → C:\Users\TON_USER\.claude\CLAUDE.md
:: (Adapter TON_USER et les chemins workspace)

:: === ÉTAPE 7 : Superpowers (déjà dans settings_template.json) ===
:: Lire tools/GUIDE_SUPERPOWERS.md pour les détails

:: === ÉTAPE 8 : Graphify ===
pip install graphify

:: === ÉTAPE 9 : MCP Servers ===
claude mcp add filesystem npx -- -y @modelcontextprotocol/server-filesystem C:\Users\TON_USER\Documents\workspace
claude mcp add github npx -- -y @modelcontextprotocol/server-github
claude mcp add context7 npx -- -y @upstash/context7-mcp
claude mcp add notebooklm npx notebooklm-mcp@latest
claude mcp add sequential-thinking npx -- -y @modelcontextprotocol/server-sequential-thinking
claude mcp add playwright npx -- -y @playwright/mcp
claude mcp add memory npx -- -y @modelcontextprotocol/server-memory

:: === ÉTAPE 10 : Récupérer les projets ===
gh repo clone Moha92-sc/workspace
gh repo clone Moha92-sc/SSI_DUBERNARD
```

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

## Règles importantes

1. **Toujours `--private`** pour les projets pro
2. **Jamais versionner** : `*.docx`, `*.xlsx`, `*.pdf`, `node_modules/`, fichiers BIM, `graphify-out/`
3. **Toujours inclure** : `CLAUDE.md`, scripts, `.gitignore`, `.claudeignore`, `README.md`
4. **Avant de fermer** : remplir "Reprendre ici" dans `CLAUDE.md` + `fin_session.bat`
5. **Nouveau projet** : `git init` + GitHub en **premier**, avant de commencer
6. **Superpowers** : laisser Claude vérifier les skills avant chaque tâche
7. **Graphify** : générer le graphe au début de chaque nouveau projet

---

## Dépôts GitHub actifs

- **claude.ia** → https://github.com/Moha92-sc/claude.ia
- **workspace** → privé
- **SSI_DUBERNARD** → privé
- **jumeau-numerique-pia** → privé
