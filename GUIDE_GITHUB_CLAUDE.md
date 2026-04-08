# Guide : Synchroniser ses projets Claude Code avec GitHub

## Objectif
Travailler sur un projet avec Claude Code sur PC A, le pousser sur GitHub,
puis continuer sur PC B sans rien perdre.

---

## INSTALLATION (une seule fois par PC)

### 1. Installer Git
- Télécharger : https://git-scm.com
- Installer avec les options par défaut
- Vérifier : `git --version`

### 2. Installer GitHub CLI (gh)
- Télécharger : https://cli.github.com
- Installer avec les options par défaut
- Vérifier : `gh --version`

### 3. Installer Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```
- Vérifier : `claude --version`

### 4. S'authentifier sur GitHub (une seule fois)
```bash
gh auth login
```
Répondre :
- GitHub.com
- HTTPS
- Login with a web browser
- Copier le code affiché → coller dans le navigateur → confirmer

---

## CRÉER UN NOUVEAU PROJET ET L'ENVOYER SUR GITHUB

### Étape 1 — Créer le dossier du projet
```bash
mkdir mon-projet
cd mon-projet
```

### Étape 2 — Initialiser Git
```bash
git init
```

### Étape 3 — Créer le fichier .gitignore
Créer un fichier `.gitignore` avec ce contenu :
```
# Fichiers générés (Word, Excel, PDF)
output/
*.docx
*.xlsx
*.pdf
*.xls

# Python
__pycache__/
*.pyc
*.pyo
.env
venv/

# Système
.DS_Store
Thumbs.db
```

### Étape 4 — Ajouter ses fichiers
```bash
git add .
git commit -m "Premier commit : ajout des scripts"
```

### Étape 5 — Créer le dépôt sur GitHub et pousser
```bash
gh repo create nom-du-projet --public --source=. --remote=origin --push
```
Options :
- `--public` : dépôt visible par tous (remplacer par `--private` si confidentiel)
- `--source=.` : utilise le dossier actuel
- `--push` : pousse immédiatement le premier commit

---

## CYCLE DE TRAVAIL QUOTIDIEN

### PC Principal (envoyer son travail)
```bash
cd mon-projet
git add .
git commit -m "Description de ce que j'ai fait"
git push
```

### PC Bureau (récupérer le travail)
```bash
cd mon-projet
git pull
```
Ou si c'est la première fois sur ce PC :
```bash
gh repo clone TON_USERNAME/nom-du-projet
cd nom-du-projet
claude
```

---

## TRAVAIL EN ÉQUIPE (3 personnes, 3 Claude Code)

### La personne qui crée le projet
Créer le dépôt en **privé** et inviter les collaborateurs :
```bash
gh repo create nom-projet --private --source=. --remote=origin --push
gh api repos/TON_USERNAME/nom-projet/collaborators/PRENOM_COLLEGUE -X PUT -f permission=push
```

### Chaque collaborateur (une seule fois)
```bash
gh repo clone USERNAME_PROPRIETAIRE/nom-projet
cd nom-projet
claude
```

### Règle d'or en équipe : toujours pull avant de travailler
```bash
git pull
# ... travail avec Claude Code ...
git add .
git commit -m "Ce que j'ai ajouté"
git push
```

---

## COMMANDES ESSENTIELLES À RETENIR

| Action | Commande |
|--------|----------|
| Voir l'état des fichiers | `git status` |
| Ajouter tous les fichiers | `git add .` |
| Sauvegarder localement | `git commit -m "message"` |
| Envoyer sur GitHub | `git push` |
| Récupérer depuis GitHub | `git pull` |
| Voir l'historique | `git log --oneline` |
| Cloner un projet existant | `gh repo clone USER/PROJET` |

---

## STRUCTURE RECOMMANDÉE D'UN PROJET

```
mon-projet/
├── scripts/          ← code Python, JS, etc.  ✅ sur GitHub
├── templates/        ← modèles Word/Excel      ✅ sur GitHub
├── requirements.txt  ← dépendances Python      ✅ sur GitHub
├── .gitignore        ← règles d'exclusion      ✅ sur GitHub
├── README.md         ← description du projet   ✅ sur GitHub
└── output/           ← fichiers générés        ❌ ignoré par Git
    ├── rapport.docx
    └── tableau.xlsx
```

---

## EN CAS DE PROBLÈME

### Conflit lors d'un pull
```bash
git pull
# Si conflit : Git indique les fichiers concernés
# Ouvrir le fichier, chercher <<<<<< et résoudre manuellement
git add fichier_resolu.py
git commit -m "Résolution du conflit"
```

### Voir les dépôts GitHub depuis le terminal
```bash
gh repo list
```

### Ouvrir un dépôt dans le navigateur
```bash
gh repo view --web
```
