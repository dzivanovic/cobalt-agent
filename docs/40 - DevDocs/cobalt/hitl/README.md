# cobalt.hitl — requested actions, his tap, a deterministic executor (F20)

## 2026-10-18 — f20-cos-1018
Built by card 730 (FINAL §3; D6 = B, the one-time key). The catalog is two actions: `agents.create`, `agents.deactivate`.

### The approval path (B)
1. The model calls `request_action{action, args, reason}` or `draft_agent{yaml, reason}` (`cos/tools.py`).
2. `actions.request_action` validates the action and its args (one schema each), refuses a secret-shaped arg (`modelaccess.guard.refuse_if_secret_shaped`), renders the exact file bytes B (`agents.registry.render_entry`) and stores `sha256(B)`. A deactivate binds the file's before-bytes too and is refused for `voice` and `cos` (F-08). A refusal goes back to the model as text; no row.
3. A 128-bit key is generated; only `approve_key_sha256` is stored. The row is `pending`, `expires_at` = the database's now() + `hitl.request_ttl_min`. The tool returns `pending <short_id>` at once.
4. `card.send_card` DMs the action, a summary, the short id and `<hitl.page_base_url>/hitl/<id>#k=<key>` through `send_dm` (F19 redaction runs; the fragment never reaches a server log).
5. His tap: `POST /hitl/{id}/approve` in `aset/web.py` — kill switch first, then ONE `UPDATE … SET status='approved'` WHERE pending, unexpired, the reviewed sha256 and `sha256(k)`; zero rows → refused, nothing written. Deny needs the key too. These two routes are the only pending → approved / denied write (L37; T3 is an AST walk).
6. `executor.run_one` (inside the CoS resident only): claim with `FOR UPDATE SKIP LOCKED`, re-check the kill switch (held, never failed), write `rendered` create-if-absent (`O_EXCL`); an existing file with the approved bytes is a recovery (`executed`), any other existing file → `failed`, never overwritten. Deactivate writes only when the file still holds the before-bytes. No retry after `failed`.
7. `executor.sweep`: `pending` past `expires_at` → `expired`; an `approved` row is never expired. `executor.report_outcomes` DMs each terminal outcome once (`reported_at`) and returns `HITL <id> executed|denied|expired|failed` for the session.

### Table
`cobalt_hitl_requests` (USER side): id, short_id, agent_id, action, payload JSONB, sha256, rendered BYTEA, before_sha256, before_bytes, reason, status (CHECK pending/approved/denied/expired/executed/failed), created_at, expires_at, decided_at, decided_via (`aset.hitl@sha256:<hash>`), deny_reason, result, error, approve_key_sha256, reported_at.

### Commands
`cobalt hitl list [--limit N]` (read only). No approve or deny subcommand.

### Tunables
`hitl.request_ttl_min` and `hitl.page_base_url`: null, no value set — a request refuses until both are ruled (L1).

### Laws
L37 (only his tap approves; no model holds an approve path), L40 (one deterministic executor per action), L1 (every missing value refuses loud).

Tests: `test_hitl_offline.py`, `test_hitl_web.py`, `test_hitl_executor.py`, `test_hitl_db.py` (with-DB, T1), `test_generated_hitl_dirs.py` (the commit path).

## 2026-10-18 — f20-cos-1018 (check)
`executor.py`: an `agents.create` whose exclusive open or write fails removes the file it made, so the ending is no file (X3). Check O8, G1.

## 2026-10-18 — f20-cos-1018 (check r2)
`executor.py`: `agents.deactivate` writes the after-bytes to a hidden sibling and renames it over the file, so a failed write leaves the untouched prior file (X3). Check r2 A1.

## 2026-10-20 — cos-tunables fr3
`hitl.page_base_url` is set to his value (ruled, Dejan, 2026-10-20): `https://cobalt.taild24291.ts.net`, https, no trailing slash; the card links `<base>/hitl/<id>#k=<key>`. `hitl.request_ttl_min` is 30 (his word, 2026-10-20). The `### Tunables` sentence above ("null, no value set — a request refuses") is superseded; the card refuses only if the value is null again.
