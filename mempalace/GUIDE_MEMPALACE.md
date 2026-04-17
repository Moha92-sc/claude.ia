# MemPalace — Mémoire persistante pour Claude Code

> Objectif : zéro re-contextualisation. Claude se souvient de tout entre les sessions.

---

## Principe

Claude Code dispose d'un système de mémoire basé sur des fichiers Markdown stockés localement.
Ces fichiers sont lus automatiquement à chaque session.

**Emplacement :**
```
C:\Users\TON_USER\.claude\projects\C--Users-TON_USER\memory\
├── MEMORY.md          ← Index auto-chargé (200 lignes max)
├── user_profile.md    ← Qui tu es, tes compétences
├── feedback_xxx.md    ← Ce que Claude doit/ne doit pas faire
└── project_xxx.md     ← État des projets en cours
```

---

## Types de mémoire

| Type | Contenu | Quand créer |
|------|---------|-------------|
| `user` | Profil, compétences, objectifs | Quand Claude apprend quelque chose sur toi |
| `feedback` | Règles de comportement | Quand tu corriges Claude ("ne fais plus X") |
| `project` | État des projets, décisions | Quand un projet avance ou une décision est prise |
| `reference` | Où trouver les infos externes | Linear, Slack, Grafana, NotebookLM... |

---

## Format d'un fichier mémoire

```markdown
---
name: Nom de la mémoire
description: Description courte — utilisée pour décider si pertinent
type: user | feedback | project | reference
---

Contenu de la mémoire.

**Why:** Pourquoi cette règle existe.
**How to apply:** Quand/comment l'appliquer.
```

---

## Format de MEMORY.md (index)

```markdown
# Memory Index

- [Titre](fichier.md) — description courte (max 150 chars)
- [Autre mémoire](autre.md) — description
```

**Règles MEMORY.md :**
- Max 200 lignes (tout ce qui dépasse est tronqué)
- Une ligne par mémoire : `- [Titre](fichier.md) — hook court`
- Pas de contenu directement dans MEMORY.md — uniquement des pointeurs

---

## Protocole de session (à mettre dans CLAUDE.md global)

```markdown
## Protocole de session — MemPalace
À chaque nouvelle session : lire les fichiers mémoire pertinents AVANT toute question.
Ne jamais demander "où en étions-nous ?" — la réponse est dans la mémoire.
- L'index est dans MEMORY.md (auto-chargé)
- Chaque projet actif a une section "REPRENDRE ICI" dans son fichier mémoire
- Lire le fichier mémoire correspondant dès que le sujet est identifié
```

---

## Bonne pratique : "REPRENDRE ICI"

Chaque fichier projet doit se terminer par :

```markdown
## REPRENDRE ICI — [DATE]

**État :** [Ce qui a été fait / où on en est]

**Points bloquants :**
- [ ] ...

**Prochaine action recommandée :**
- Option A : ...
- Option B : ...
```

---

## Ce qu'il NE faut PAS mettre en mémoire

- Structure du code, architecture (lire les fichiers directement)
- Historique git (utiliser `git log`)
- Solutions de debugging (le fix est dans le code)
- État temporaire de la session en cours

---

## Templates

Voir `mempalace/templates/` pour des exemples de fichiers mémoire.
