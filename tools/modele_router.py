"""
modele_router.py — Routeur automatique Groq / Ollama

Logique :
    GROQ  → tâches complexes : raisonnement normatif, analyse technique
    OLLAMA → tâches simples  : résumé, extraction, formatage, Excel IA, offline

Usage :
    from agents_ia._commun.modele_router import appeler_ia

    reponse = await appeler_ia("Résume ce texte", tache="simple")
    reponse = await appeler_ia("Analyse de conformité réglementaire", tache="groq")

Adapter MOTS_CLES_GROQ selon ton domaine métier.
"""

import os
import asyncio
import httpx
from groq import AsyncGroq

# Import groq_retry compatible selon le contexte d'exécution
try:
    from agents_ia._commun.groq_retry import groq_call_fn
except ImportError:
    from _commun.groq_retry import groq_call_fn

# ─── Configuration ───────────────────────────────────────────
GROQ_MODEL   = "llama-3.3-70b-versatile"
OLLAMA_MODEL = "mistral"
OLLAMA_URL   = "http://localhost:11434/api/chat"

# Tâches routées vers Groq (mots-clés — adapter à ton domaine)
MOTS_CLES_GROQ = [
    "analyse", "conformit", "normati", "vérifi",
    "rapport", "dimensionn", "calcul",
    # Ajouter ici tes mots-clés métier
]

# ─── Routeur ─────────────────────────────────────────────────
def choisir_modele(prompt: str, tache: str = "auto") -> str:
    """
    Retourne 'groq' ou 'ollama' selon la tâche.

    Args:
        prompt : texte de la requête
        tache  : 'groq' | 'ollama' | 'simple' | 'auto'
    """
    if tache == "groq":
        return "groq"
    if tache in ("ollama", "simple"):
        return "ollama"

    # Auto-détection par mots-clés dans le prompt
    prompt_lower = prompt.lower()
    for mot in MOTS_CLES_GROQ:
        if mot in prompt_lower:
            return "groq"

    return "ollama"  # Par défaut : local


# ─── Appel Groq ──────────────────────────────────────────────
async def _appeler_groq(prompt: str, systeme: str = "", label: str = "") -> str:
    client = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY"))

    messages = []
    if systeme:
        messages.append({"role": "system", "content": systeme})
    messages.append({"role": "user", "content": prompt})

    async def _run():
        reponse = await client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            max_tokens=2048,
        )
        return reponse.choices[0].message.content

    return await groq_call_fn(_run, label=label or "Groq")


# ─── Appel Ollama ────────────────────────────────────────────
async def _appeler_ollama(prompt: str, systeme: str = "") -> str:
    messages = []
    if systeme:
        messages.append({"role": "system", "content": systeme})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
    }

    print("  ⏳ Ollama chargement modele (30-60s premiere fois)...")
    async with httpx.AsyncClient(timeout=180) as client:
        reponse = await client.post(OLLAMA_URL, json=payload)
        reponse.raise_for_status()
        data = reponse.json()
        return data["message"]["content"]


# ─── Point d'entrée principal ────────────────────────────────
async def appeler_ia(
    prompt: str,
    systeme: str = "",
    tache: str = "auto",
    label: str = "",
    fallback: bool = True,
) -> str:
    """
    Appelle Groq ou Ollama selon la tâche, avec fallback automatique.

    Args:
        prompt   : message utilisateur
        systeme  : prompt système (optionnel)
        tache    : 'auto' | 'groq' | 'ollama' | 'simple'
        label    : affiché dans la console pendant les retries
        fallback : si True, bascule sur l'autre modèle en cas d'erreur

    Returns:
        Texte de la réponse
    """
    modele = choisir_modele(prompt, tache)
    print(f"  🔀 Router → {modele.upper()} ({tache})")

    try:
        if modele == "groq":
            return await _appeler_groq(prompt, systeme=systeme, label=label)
        else:
            return await _appeler_ollama(prompt, systeme=systeme)

    except Exception as e:
        if not fallback:
            raise

        autre = "ollama" if modele == "groq" else "groq"
        print(f"  ⚠️  {modele.upper()} échoué ({e}) → bascule sur {autre.upper()}")

        if autre == "groq":
            return await _appeler_groq(prompt, systeme=systeme, label=label)
        else:
            return await _appeler_ollama(prompt, systeme=systeme)


# ─── Test rapide ─────────────────────────────────────────────
if __name__ == "__main__":
    async def test():
        print("=== Test routeur ===")
        print("\n[1] Tâche analyse → doit router sur Groq")
        r = await appeler_ia("Analyse de conformité réglementaire du dossier", tache="auto")
        print(f"Réponse : {r[:100]}...")

        print("\n[2] Tâche simple → doit router sur Ollama")
        r = await appeler_ia("Résume en 2 phrases : Paris est la capitale de la France.", tache="simple")
        print(f"Réponse : {r[:100]}...")

    asyncio.run(test())
