# `src/cobalt/classify/__init__.py`

## What it does
Package marker and map for the JEV typed-classifier trial collector
(plan `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md`; OFF-LADDER, an
input to the typed-classifier design tribunal, deciding nothing about
adoption). Exports nothing; the docstring lists the six modules.

## What the package never does
Holds a key (read inside each keyed request, alive only in its
`Authorization` header — L4, L41), touches the network outside
`openrouter.ai`, opens a database, or writes the vault. No LiteLLM, no
vendor SDK, no old-tree import (L15).
