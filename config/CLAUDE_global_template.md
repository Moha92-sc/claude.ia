# Environnement Claude Code — [TON NOM]
> Fichier : C:\Users\TON_USER\.claude\CLAUDE.md
> Ce fichier est chargé dans TOUTES les sessions Claude Code.

## Protocole de session — MemPalace
À chaque nouvelle session : lire les fichiers mémoire pertinents AVANT toute question.
Ne jamais demander "où en étions-nous ?" — la réponse est dans la mémoire.
- L'index est dans MEMORY.md (auto-chargé)
- Chaque projet actif a une section "REPRENDRE ICI" dans son fichier mémoire
- Lire le fichier mémoire correspondant dès que le sujet est identifié

## Règles permanentes
1. Toujours répondre en **français** (adapter à ta langue)
2. Workspace : `C:\Users\TON_USER\Documents\workspace\`
3. Venv Python : `activate-workspace` avant tout script
4. Chemins avec espaces → `cd` dans le dossier + chemins relatifs

## Graphify
Si `graphify-out/graph.json` existe : interroger le graphe **avant** de lire des fichiers.
- Requête : `graphify query "question" --budget 2000`
- Reconstruire après modifs : `graphify update .`

## Skills (slash commands — taper dans la zone de saisie)
Lister tes skills ici, ex : `/mon-skill` · `/autre-skill`

## Modèles IA
- **Groq** (`GROQ_API_KEY`) — llama-3.3-70b : raisonnement complexe, normes
- **Ollama** (`OLLAMA_HOST` localhost:11434) — mistral/deepseek : tâches simples, offline
- Retry 429 Groq → utiliser `groq_call_fn` de `_commun/groq_retry.py`

## Notes spécifiques à ton domaine
(Ajouter ici les règles, normes, outils propres à tes projets)
