# `src/cobalt/voice/registry.py`

## What it does
Loads the voice agent's registry entry `configs/cobalt/agents/voice.yaml`
(L16 — an agent is data): `id`, `charter`, the model `route`, the tool
allowlist (each tool's `kind` read / act, `trading_logic` flag,
description and argument schema) and the confirm / cancel words.

## What it refuses
- A `route` that is not a route NAME in `configs/cobalt/modelaccess.yaml`
  (so a URL, a provider string or a bare model id can never stand there).
- A tool the voice code does not implement (`KNOWN_TOOLS`), or an argument
  type the resolver cannot bind (`card`, `price`).
- `confirm_words` other than exactly `["yes"]`, `cancel_words` other than
  exactly `["no"]` (FINAL [F-08] — widening waits on a measurement).
- A missing key.

## YAML note
The words are quoted in the file: bare YAML `yes` / `no` load as booleans.
