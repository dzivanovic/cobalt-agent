# `src/cobalt/strike/delivery_config.py`

`configs/cobalt/strike.yaml`, the strike delivery numbers the ASET sheet reads (`aset/strike.py`): `DeliverySettings` (pydantic, `extra="forbid"`, defaults in the model) — `stream_tail_ms` 500, `keepalive_s` 15, `dm_after_s` 10, `hotkey_template` `"{DAYMODE}-{KEY}-{SIDE}"` (Charter §5 #4). `load_delivery_config(path)`: a missing file → the defaults and one logged line; a missing key → its default; an extra key, or a template naming a field other than DAYMODE / KEY / SIDE → `DeliveryConfigError` naming it. `hotkey(template, sheet_mode, sized_grade, direction)` fills and upper-cases the template; no `sheet_mode` or no `sized_grade` → `UNSIZED` (`n/a — unsized`), never guessed. Imports nothing of the detector.

## 2026-10-09 — s4-p2-1009
New module (S4-P2 S5).
