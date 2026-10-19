# `src/cobalt/genesis/store.py`

`GenesisStore` (`SIDE = Side.USER`, the `aset/strike.py` `StrikeAlertStore` shape) over `"user".genesis_chunk`. `replace(source)` deletes that `(user_id, source)`'s rows and inserts the new chunks in ONE transaction (DECISION D4); other sources are untouched.

`import_paths(paths, *, store)` reads and chunks every path before the first write, so one bad path raises `GenesisImportError` and no source of that call is written (L1). No path given is refused; there is no default path, and nothing under the vault is opened unless it is passed.

## 2026-10-19 — f21-genesis-1013
New module (card 468 G2, G3).
Check (card 820, O1/A1): `replace` sets `conn.autocommit = False` on the `autocommit=True` connection of `db.connect`, so the DELETE and the INSERTs commit together or not at all.

## 2026-10-19 — f21-vectors-1013
Card 469 V4 (FINAL F-02, X10): `column_embed_dim()` reads `embedding`'s `atttypmod`; `check_embed_dim(dim)` raises `GenesisEmbedError` when the column is absent or its dimension is not the route's `dim`; `null_chunks()` lists `(id, body)` with no vector; `set_embedding(id, vector, *, model, dim)` refuses before the check, a wrong length, an empty, zero or non-finite vector and an empty model, then writes one row (autocommit, so each vector lands on its own).
