"""Slice 2 — DRC & Daily prefill engine (pre-beta increment 2).

Cobalt fills the grunt data; Dejan's critical thinking is the only
manual input. All vault writes go through cobalt.vault's ONE resolver
and shared safety gate. Never modify existing note content — create-if-
absent from a Jinja template, otherwise append a clearly fenced
"Cobalt prefill" block.
"""
