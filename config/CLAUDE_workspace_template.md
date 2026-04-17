# WORKSPACE — [TON NOM]
> Fichier : ton_workspace\CLAUDE.md
> Mettre à jour après chaque avancée significative.

---

## Profil
- **Formation :** [Ta formation]
- **Poste / Alternance :** [Ton employeur / domaine]
- **Objectif :** [Ce que tu veux atteindre]
- **Usage Claude :** code, analyse technique, rédaction, automatisation

---

## Structure du workspace

```
ton_workspace\
├── CLAUDE.md                  ← CE FICHIER
├── .venv\                     ← Environnement Python
├── 01_projet_a\
├── 02_projet_b\
└── 03_outils\
    ├── scripts\
    ├── agents_ia\
    │   └── _commun\           ← groq_retry.py, modele_router.py
    └── templates\
```

---

## Commandes disponibles

| Commande | Action |
|---|---|
| `activate-workspace` | Activer l'environnement Python `.venv` |
| `nouveau-projet` | Créer un projet (dossier + CLAUDE.md + Git + GitHub) |

---

## Environnement Python

```bash
activate-workspace   # active le .venv
```

**Librairies installées :**
(lister ici : pydantic-ai, python-docx, openpyxl, ezdxf, pymupdf, anthropic, streamlit, pandas...)

**Variables d'environnement :**
- `GROQ_API_KEY` — clé Groq (gratuit sur console.groq.com)
- `OPENROUTER_API_KEY` — clé OpenRouter (gratuit sur openrouter.ai)

---

## GitHub
- **Compte :** TON_USERNAME
- **Repos :** (lister ici)

---

## Règles permanentes pour Claude
1. Toujours répondre en **français** (adapter)
2. Sauvegarder tout fichier produit sur le disque immédiatement
3. Mettre à jour ce CLAUDE.md après chaque avancée significative
4. Remplir "Reprendre ici" avant la fin de chaque session
5. Chemins avec espaces : toujours `cd` dans le dossier + chemins relatifs

---

## REPRENDRE ICI — [DATE]

**État :** [Ce qui a été fait]

**Points bloquants :**
- [ ] ...

**Prochaine action :**
- Option A : ...
- Option B : ...
