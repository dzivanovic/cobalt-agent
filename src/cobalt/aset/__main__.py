"""Run the ASET sheet locally: uv run python -m cobalt.aset

Bind host/port are config-driven (configs/dev/aset*.yaml, `server:`
section). The plain-http listener is loopback only (127.0.0.1); the
tailnet reaches the sheet through `tailscale serve` on https (L80), at the
address `configs/cobalt/voice.yaml` `https_url` names.
"""

import os

# The old tree's config loader dumps the merged config INCLUDING VAULT
# SECRETS at DEBUG level (ruled KILL-blanket, TRIAGE 2.7 "secret-printing
# log sinks"; dies with the old tree). Until that KILL lands, cap loguru
# at INFO for this process so importing FinvizApiClient can't spill
# secrets into this server's console/logs. Must be set before any import
# that pulls in loguru.
os.environ.setdefault("LOGURU_LEVEL", "INFO")

import uvicorn  # noqa: E402

from cobalt.aset.config import load_config  # noqa: E402
from cobalt.voice.config import load_voice_config  # noqa: E402

if __name__ == "__main__":
    cfg = load_config()
    host, port = cfg.server.host, cfg.server.port

    print(f"Cobalt ASET sheet — bind: {cfg.server.bind} ({host}:{port})", flush=True)
    print(f"  reachable at: http://127.0.0.1:{port}", flush=True)
    print(
        f"  reachable at: {load_voice_config().https_url}  (tailnet, through `tailscale serve`, L80)",
        flush=True,
    )

    uvicorn.run("cobalt.aset.web:app", host=host, port=port)
