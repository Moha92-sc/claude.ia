# Guide Superpowers — Claude Code

## C'est quoi ?
Plugin officiel qui ajoute des **skills** (slash commands) à Claude Code :
workflows guidés pour brainstorming, debug, TDD, plans d'implémentation, revue de code, etc.

---

## Installation (une seule fois par PC)

### Activer le plugin dans settings.json
Fichier : `C:\Users\TON_USER\.claude\settings.json`

```json
{
  "enabledPlugins": {
    "superpowers@claude-plugins-official": true
  },
  "extraKnownMarketplaces": {
    "superpowers-marketplace": {
      "source": {
        "source": "github",
        "repo": "obra/superpowers-marketplace"
      }
    }
  }
}
```

Le fichier `config/settings_template.json` du repo contient déjà cette config.

---

## Skills essentiels

| Skill | Quand l'utiliser |
|---|---|
| `/brainstorming` | Avant toute création de feature |
| `/writing-plans` | Planifier une tâche multi-étapes |
| `/executing-plans` | Exécuter un plan écrit |
| `/systematic-debugging` | Face à un bug ou test qui échoue |
| `/verification-before-completion` | Avant de dire "c'est fait" |
| `/dispatching-parallel-agents` | 2+ tâches indépendantes |
| `/requesting-code-review` | Après implémentation majeure |

## Skills métier (Mohamed Lehouali)

| Skill | Domaine |
|---|---|
| `/ssi` | NF S 61-936, dimensionnement SSI |
| `/dim` | Agent dimensionneur SSI |
| `/dxf` | Génération fichiers DXF AutoCAD |
| `/rapport` | Pipeline Pandoc Word professionnel |
| `/graphify` | Graphe de connaissance codebase |

---

## Règle d'or
Claude vérifie automatiquement si un skill s'applique **avant chaque réponse**.
Ne pas chercher à contourner — les skills évitent les erreurs et accélèrent le travail.
