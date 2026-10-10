# `src/cobalt/aset/__main__.py`

## What it does
The launcher: `uv run python -m cobalt.aset`. Loads config, resolves
bind host/port, prints every reachable URL (loopback always; the
detected LAN IP too when `bind: lan`), and starts uvicorn serving
`web.app`.

Sets `LOGURU_LEVEL=INFO` **before any other import**, as a targeted
mitigation for a real incident: the old tree's config loader (imported
transitively via `prefill.py` → `FinvizApiClient`) used to dump the
entire merged config — including every vault secret — at DEBUG level on
import. That specific leak has since been fixed at the source
(`cobalt_agent/config.py`, 2026-08-24), but this guard is cheap
insurance and is left in place deliberately.

## Key functions/classes
No functions — this is a script module (`if __name__ == "__main__":`
guard), not a library. Body, in order:
1. Set `LOGURU_LEVEL=INFO` (before the `uvicorn`/`cobalt` imports).
2. `load_config()` → `cfg`.
3. Resolve `host, port = cfg.server.host, cfg.server.port`.
4. Print the bind summary and the loopback URL (always).
5. If `bind == "lan"`: call `net.local_lan_ip()`, print the LAN URL if
   found (else a "check manually" note), print the unauthenticated-page
   warning. All prints use `flush=True` so they land in log order ahead
   of uvicorn's own buffered stdout.
6. `uvicorn.run("cobalt.aset.web:app", host=host, port=port)`.

## Data flow in/out
**In:** `configs/dev/aset*.yaml` via `load_config()`.
**Out:** starts a blocking uvicorn server process; prints startup
banner lines to stdout.

## Config it reads
`AsetConfig.server` (`bind`, `port`) — the rest of `AsetConfig` is read
per-request by `web.py`, not here.

## 2026-10-09 — s4-p2-1009
Before `uvicorn.run`: `strike.start_fallback_thread()` — the S4-P2 S4 phone-fallback tail, one daemon thread, synchronous, outside uvicorn's event loop (it never runs under `TestClient(web.app)`, DECISION E10).

## 2026-10-10 — strike-fallback-env-1010
Loads the repo `.env` explicitly at import (`load_dotenv(Path(__file__).resolve().parents[3] / ".env")`, `override` False, as `cli.py` does), before `start_fallback_thread()`: the thread's first pass opens Postgres, and the only other load was the cwd-relative one in `cobalt.aset.web`'s import chain, which runs after it (row A, R828).
