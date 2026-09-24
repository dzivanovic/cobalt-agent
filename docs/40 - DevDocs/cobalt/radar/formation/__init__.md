# `cobalt.radar.formation` — the formation registries

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.2–2.5).

This package holds the five tables that formation dispatches through. Each is keyed by the definition's own data, never by a trade name:

| table | key | module |
|---|---|---|
| `TRIGGERS` | `trigger.type` | `triggers.py` |
| `STOPS` | `stop.placement.type` | `stops.py` |
| `STRUCTURAL_REFS` | a §3.6 `StructuralRef` | `stops.py` |
| `ATOMS` | atom text | `atoms.py` |
| `RELATIONS` | relation word | `atoms.py` |

`anatomy/registry.evaluability` reads these same tables, so what the dry-run calls evaluable is what the stage can form (L3). A new brick is one resolver plus one row here. The stage, the registry and the card do not change.
