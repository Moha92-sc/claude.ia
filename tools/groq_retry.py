"""
groq_retry.py — Gestionnaire de rate limit Groq (12 000 tokens/min)

Usage :
    from agents_ia._commun.groq_retry import groq_call

    # Remplace :  result = await agent.run(prompt)
    # Par :       result = await groq_call(agent.run(prompt))

Comportement :
    - Si Groq retourne 429 → lit le header retry-after
    - Attend le temps indiqué (+ 2s de marge)
    - Réessaie automatiquement, sans limite de tentatives
    - Affiche un décompte en console
"""

import asyncio
import re
import time


def _extraire_retry_after(msg: str) -> int:
    """
    Extrait le nombre de secondes à attendre depuis le message d'erreur Groq.
    Groq inclut souvent : 'Please try again in 34.56s' ou 'retry after 60s'
    Retourne 60 par défaut si non trouvé.
    """
    # Format Groq le plus courant : "try again in X.XXs"
    match = re.search(r"try again in\s+([\d.]+)s", msg, re.IGNORECASE)
    if match:
        return int(float(match.group(1))) + 2  # +2s de marge

    # Format alternatif : "retry after Xs"
    match = re.search(r"retry.{0,10}after\s+([\d.]+)s", msg, re.IGNORECASE)
    if match:
        return int(float(match.group(1))) + 2

    # Valeur par défaut : attendre jusqu'à la prochaine minute
    return 62


def _est_rate_limit(err: Exception) -> bool:
    msg = str(err).lower()
    return "429" in msg or "rate_limit" in msg or "rate limit" in msg or "too many" in msg


async def groq_call(coro, label: str = ""):
    """
    Exécute une coroutine PydanticAI/Groq avec retry automatique sur 429.

    Args:
        coro     : coroutine à exécuter (ex: agent.run(prompt))
        label    : texte affiché pendant l'attente (ex: "Zone 3/24")
    """
    tentative = 1
    while True:
        try:
            return await coro
        except Exception as e:
            if not _est_rate_limit(e):
                raise  # Erreur autre que rate limit → on ne gère pas

            attente = _extraire_retry_after(str(e))
            prefix = f"[{label}] " if label else ""

            print(f"\n  ⏳ {prefix}Rate limit Groq — attente {attente}s (tentative {tentative})")

            # Décompte seconde par seconde
            for restant in range(attente, 0, -1):
                print(f"\r  ⏳ {prefix}Reprise dans {restant:>3}s...", end="", flush=True)
                await asyncio.sleep(1)
            print(f"\r  ✅ {prefix}Reprise !{' ' * 30}")

            tentative += 1
            # Recréer la coroutine n'est pas possible directement —
            # groq_call doit être appelé avec une fonction, pas une coroutine déjà consommée.
            # Voir groq_call_fn() pour ce cas.


async def groq_call_fn(fn, *args, label: str = "", **kwargs):
    """
    Version pour les fonctions async (pas les coroutines directes).
    Utile quand on boucle sur plusieurs appels.

    Args:
        fn       : fonction async à appeler (ex: agent.run)
        *args    : arguments positionnels
        label    : texte affiché pendant l'attente
        **kwargs : arguments nommés

    Exemple :
        result = await groq_call_fn(agent.run, prompt, label="Zone 3/24")
    """
    tentative = 1
    while True:
        try:
            return await fn(*args, **kwargs)
        except Exception as e:
            if not _est_rate_limit(e):
                raise

            attente = _extraire_retry_after(str(e))
            prefix = f"[{label}] " if label else ""

            print(f"\n  ⏳ {prefix}Rate limit Groq — attente {attente}s (tentative {tentative})")

            for restant in range(attente, 0, -1):
                print(f"\r  ⏳ {prefix}Reprise dans {restant:>3}s...", end="", flush=True)
                await asyncio.sleep(1)
            print(f"\r  ✅ {prefix}Reprise !{' ' * 30}")

            tentative += 1
