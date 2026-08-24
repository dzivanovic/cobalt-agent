"""Run the ASET sheet locally: uv run python -m cobalt.aset"""

import os

# The old tree's config loader dumps the merged config INCLUDING VAULT
# SECRETS at DEBUG level (ruled KILL-blanket, TRIAGE 2.7 "secret-printing
# log sinks"; dies with the old tree). Until that KILL lands, cap loguru
# at INFO for this process so importing FinvizApiClient can't spill
# secrets into this server's console/logs. Must be set before any import
# that pulls in loguru.
os.environ.setdefault("LOGURU_LEVEL", "INFO")

import uvicorn  # noqa: E402

if __name__ == "__main__":
    uvicorn.run(
        "cobalt.aset.web:app",
        host="127.0.0.1",
        port=int(os.getenv("ASET_PORT", "5010")),
    )
