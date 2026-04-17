# claude.ia — Boîte à outils Claude Code

Optimisations, scripts, templates et guides pour maximiser Claude Code sur Windows.

---

## Structure

| Dossier | Contenu |
|---------|---------|
| `config/` | Templates CLAUDE.md, settings.json, MCP, .claudeignore |
| `tools/` | Scripts Python utilitaires (Groq retry, routeur IA) |
| `mempalace/` | Système de mémoire persistante MemPalace |
| `scripts/` | Scripts BAT pour workflow Git/GitHub |

---

## Démarrage rapide — nouveau PC

### 1. CLAUDE.md global (mémoire de Claude)
```
Copier config/CLAUDE_global_template.md → C:\Users\TON_USER\.claude\CLAUDE.md
Adapter : workspace, domaines, modèles IA
```

### 2. CLAUDE.md workspace
```
Copier config/CLAUDE_workspace_template.md → ton_workspace\CLAUDE.md
Adapter : structure, outils, commandes
```

### 3. .claudeignore (réduire le contexte de Claude)
```
Copier config/claudeignore_template → ton_workspace\.claudeignore
```

### 4. Settings Claude Code (hook Graphify + Superpowers)
```
Copier config/settings_template.json → C:\Users\TON_USER\.claude\settings.json
Adapter : chemin Python (.venv)
```

### 5. MCP servers
```
Voir config/mcp_config_template.json
Installer : claude mcp add <nom> <commande>
Ajouter les clés API dans les variables d'environnement
```

### 6. MemPalace (zéro re-contextualisation)
```
Voir mempalace/GUIDE_MEMPALACE.md
```

---

## Outils Python

| Fichier | Rôle |
|---------|------|
| `tools/groq_retry.py` | Retry automatique sur rate limit Groq 429 |
| `tools/modele_router.py` | Routeur auto Groq (complexe) / Ollama (simple/offline) |

---

## Scripts Git/GitHub

| Script | Quand l'utiliser |
|--------|-----------------|
| `scripts/nouveau_projet.bat` | Créer un nouveau projet (dossier + Git + GitHub) |
| `scripts/push.bat` | Sauvegarder et envoyer sur GitHub |
| `scripts/pull.bat` | Récupérer le travail depuis GitHub |
| `scripts/fin_session.bat` | Fin de session (sauvegarde + journal) |
| `scripts/autosave.bat` | Lancer en début de session (auto-sauvegarde 30 min) |

---

## Guides

- `GUIDE_GITHUB_CLAUDE.md` — Synchroniser projets Claude Code avec GitHub
- `RECAP_SETUP.md` — Récapitulatif setup GitHub + Claude Code
- `mempalace/GUIDE_MEMPALACE.md` — Système MemPalace (mémoire persistante)
