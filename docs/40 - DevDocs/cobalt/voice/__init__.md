# `src/cobalt/voice/__init__.py`

## What it is
The package docstring of voice V1 — the first end-to-end conversation of
the voice v3 FINAL: a press (or typed text) → local speech-to-text → ONE
local Plan call through `cobalt.modelaccess` → code resolves → a read
answered by code, or ONE confirmed act (a card stop) → the reply shown and
spoken on the device.

## What the module owns
Exactly two side effects (L40): its own `"user".voice_turns` rows and its
own scratch audio files. Card state belongs to `CardStore` (reached through
`cobalt.aset.card_stop.set_card_stop`); nothing in V1 writes the vault.
