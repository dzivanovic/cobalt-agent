"""THE new core's ONE model-access module (voice v3 seam S1).

Created by voice V1 with the LOCAL lane only; the routing build EXTENDS
this package (fallback chains, metered kinds, a call ledger) and never
builds a second one (L3). No other new-core module calls a model
endpoint, imports `litellm`, or opens an HTTP connection to a model
server. A caller names a ROUTE and gets a `ModelResult` or a
`ModelCallError` — see `docs/30 - Design/VOICE-v3-SEAM-S1-2026-09-23.md`.
"""

from .client import call, call_sync, embed_sync
from .config import load_routes
from .models import EmbedResult, ModelCallError, ModelMessage, ModelRequest, ModelResult

__all__ = [
    "EmbedResult",
    "ModelCallError",
    "ModelMessage",
    "ModelRequest",
    "ModelResult",
    "call",
    "call_sync",
    "embed_sync",
    "load_routes",
]
