# `src/cobalt/modelaccess/__init__.py`

## What it does
The public surface of the new core's ONE model-access module (voice v3
seam S1): `call`, `call_sync`, `ModelRequest`, `ModelMessage`,
`ModelResult`, `ModelCallError`, `load_routes`. Nothing else is exported.

## Why one module
Before voice V1 the new core made no model call at all. V1 needs one, and
the routing lane will need many; the seam document
(`docs/30 - Design/VOICE-v3-SEAM-S1-2026-09-23.md`) settles that every
later caller goes through THIS package and the routing build extends it —
never a second copy (L3). No other new-core module imports `litellm`,
talks to a model endpoint, or opens an HTTP connection to a model server;
the V1 close greps for it.

## What a caller sees
A route NAME in, a `ModelResult` or a typed `ModelCallError` out. Never a
URL, a key, a provider or a model file.
