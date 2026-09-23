"""Voice V1 — one press-to-talk widget, one conversational turn (voice v3 FINAL).

press (or type) → local STT → ONE local Plan call (through
`cobalt.modelaccess`) → code resolves → a read answered by code, or ONE
confirmed act (a card stop, through `set_card_stop` → `CardStore`) → the
reply shown and spoken on the device. See
`docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md` §9 V1.

The voice module owns exactly two side effects (L40): its own
`"user".voice_turns` rows and its own scratch audio files. Everything
else is an ASK to the expert that owns it.
"""
