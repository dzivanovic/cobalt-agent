# `src/cobalt/genesis/search.py`

`search(question, *, limit, form="websearch", store=None) -> list[Hit]`, THE one recall entry (F-15, L3): `websearch_to_tsquery('english', question)` (or `plainto_tsquery` with `form="plain"`, kept for X7's comparison) against `genesis_chunk.tsv`, the current trader's rows only, ranked by `ts_rank_cd`, best first, at most `limit`. `Hit(source, line_start, line_end, rank, body)`. An unknown form, an empty question or a limit below 1 raises `ValueError` before any connection. No model call.

## 2026-10-19 — f21-genesis-1013
New module (card 468 G4).
