# Guide Graphify — Claude Code

## C'est quoi ?
Outil qui transforme un codebase en **graphe de connaissance** (JSON + HTML).
Permet à Claude d'interroger la structure du projet sans lire tous les fichiers.
Résultat : sessions plus rapides, moins de tokens consommés.

---

## Installation

```bash
pip install graphify
# ou dans ton venv :
activate-workspace
pip install graphify
```

Vérifier : `graphify --version`

---

## Utilisation

### Générer le graphe (première fois ou après gros changements)
```bash
cd mon-projet
graphify .
# Crée : graphify-out/graph.json + graphify-out/graph.html
```

### Mettre à jour après modifications
```bash
graphify update .
```

### Interroger le graphe
```bash
graphify query "comment fonctionne le dimensionnement SSI ?" --budget 2000
```

---

## Intégration Claude Code

### 1. Ajouter dans CLAUDE.md du projet
```markdown
## Graphify
Si `graphify-out/graph.json` existe : interroger le graphe **avant** de lire des fichiers.
- Requête : `graphify query "question" --budget 2000`
- Reconstruire après modifs : `graphify update .`
```

### 2. Ajouter .claudeignore à la racine du projet
Copier `config/claudeignore_template` → `.claudeignore`
Ajouter :
```
graphify-out/
```

### 3. Hook settings.json (optionnel)
Le `config/settings_template.json` contient un hook PreToolUse qui détecte
automatiquement si un graphe existe avant chaque lecture de fichier.

---

## Workflow recommandé

```
Nouveau projet    → graphify .        (générer)
Début de session  → graphify query    (interroger)
Après refacto     → graphify update . (mettre à jour)
```

---

## Fichiers générés (ne pas versionner)
Ajouter dans `.gitignore` :
```
graphify-out/
```
