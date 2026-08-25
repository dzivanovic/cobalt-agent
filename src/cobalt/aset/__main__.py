"""Run the ASET sheet locally: uv run python -m cobalt.aset

Bind host/port are config-driven (configs/dev/aset*.yaml, `server:`
section) — default is loopback-only. `bind: lan` exposes the sheet on
the local network (e.g. Dejan's Windows trading PC, same home network,
NOT Tailscale) at http://<mac-lan-ip>:<port>. LAN bind serves an
UNAUTHENTICATED page to the local network — see the config comments;
an access token is a backlog item.
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
from cobalt.aset.net import local_lan_ip  # noqa: E402

if __name__ == "__main__":
    cfg = load_config()
    host, port = cfg.server.host, cfg.server.port

    print(f"Cobalt ASET sheet — bind: {cfg.server.bind} ({host}:{port})", flush=True)
    print(f"  reachable at: http://127.0.0.1:{port}", flush=True)
    if cfg.server.bind == "lan":
        lan_ip = local_lan_ip()
        if lan_ip:
            print(
                f"  reachable at: http://{lan_ip}:{port}  (LAN, e.g. the Windows trading PC)",
                flush=True,
            )
        else:
            print(
                "  LAN bind requested but no LAN IP could be detected — check manually.",
                flush=True,
            )
        print(
            "  ⚠ UNAUTHENTICATED: anyone on the local network can reach this page. "
            "Acceptable for now; an access token is a backlog item.",
            flush=True,
        )

    uvicorn.run("cobalt.aset.web:app", host=host, port=port)
