"""Typed-classifier trial collector — the JEV hands-on trial (2026-09-23).

Plan: `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md`. OFF-LADDER; an
INPUT to the typed-classifier design tribunal, deciding nothing about
adoption.

    models.py     the neutral question schema + the per-call record (L57)
    config.py     configs/cobalt/classify/trial.yaml — the sets (L10)
    collector.py  the `Classifier` protocol + the OpenRouter door (L9)
    ledger.py     the spend ledger — TOTAL demand against his cap (L53)
    trial.py      the runner: --dry-run renders, --run calls
    cli.py        `cobalt classify discover | probe | trial`

WHAT THIS PACKAGE NEVER DOES: hold a key (the key is read inside each
keyed request and lives only in its `Authorization` header — L4, L41),
touch the network outside `openrouter.ai`, open a database, or write the
vault. Nothing here imports LiteLLM, a vendor SDK or the old tree (L15).
"""
