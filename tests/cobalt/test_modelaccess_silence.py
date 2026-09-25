"""Seam S1 §2.4 (5): no network at import, and none beyond loopback at call.

Each probe runs in a FRESH interpreter (a subprocess this test starts), so
an import already cached by the suite cannot hide a fetch. The child
replaces `socket.socket.connect` / `connect_ex` and
`socket.getaddrinfo` BEFORE the import and records every attempt whose
host is not loopback; it then prints the record as one JSON line.

Which adapter the module uses is decided by this file (seam §2.4 (5)):
`litellm` is preferred IF its import is silent with the remote cost-map
fetch disabled; otherwise the `openai` client (already pinned) is the
adapter. `test_litellm_import_is_probed` RECORDS litellm's result either
way — it asserts nothing about litellm, so the evidence is kept whatever
it reads — and `test_the_adapter_module_imports_silently` is the binding
check on what the module actually imports.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import textwrap

CHILD = textwrap.dedent(
    """
    import json, os, socket, sys
    LOOP = {"127.0.0.1", "::1", "localhost"}
    attempts = []
    _connect, _connect_ex, _gai = socket.socket.connect, socket.socket.connect_ex, socket.getaddrinfo
    def _host(addr):
        return addr[0] if isinstance(addr, tuple) else str(addr)
    def connect(self, addr):
        if self.family in (socket.AF_INET, socket.AF_INET6) and _host(addr) not in LOOP:
            attempts.append(["connect", _host(addr)])
            raise OSError("non-loopback connect blocked by test")
        return _connect(self, addr)
    def connect_ex(self, addr):
        if self.family in (socket.AF_INET, socket.AF_INET6) and _host(addr) not in LOOP:
            attempts.append(["connect_ex", _host(addr)])
            return 111
        return _connect_ex(self, addr)
    def getaddrinfo(host, *a, **k):
        if host not in LOOP and host is not None:
            attempts.append(["getaddrinfo", str(host)])
            raise socket.gaierror("non-loopback lookup blocked by test")
        return _gai(host, *a, **k)
    socket.socket.connect, socket.socket.connect_ex, socket.getaddrinfo = connect, connect_ex, getaddrinfo
    error = None
    try:
        __import__(sys.argv[1])
    except Exception as e:
        error = f"{type(e).__name__}: {e}"[:300]
    print("PROBE " + json.dumps({"module": sys.argv[1], "attempts": attempts, "error": error}))
    """
)


def _probe(module: str) -> dict:
    env = dict(os.environ)
    env["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
    env.pop("HTTP_PROXY", None)
    env.pop("HTTPS_PROXY", None)
    p = subprocess.run(
        [sys.executable, "-c", CHILD, module], capture_output=True, text=True, env=env, timeout=180
    )
    line = next((l for l in p.stdout.splitlines() if l.startswith("PROBE ")), None)
    assert line is not None, f"probe produced no result (rc={p.returncode}): {p.stderr[-600:]}"
    return json.loads(line[6:])


def test_litellm_import_is_probed(capsys):
    """Evidence only (seam §2.4 (5)): what `import litellm` attempts with
    `LITELLM_LOCAL_MODEL_COST_MAP=True`. Printed so the build report can
    quote it; the adapter choice rests on it."""
    result = _probe("litellm")
    with capsys.disabled():
        print(f"\nLITELLM IMPORT PROBE: {json.dumps(result)}")
    assert result["module"] == "litellm"


def test_the_adapter_module_imports_silently():
    """The binding check: importing the model-access package (and so its
    adapter) attempts NO non-loopback connection and no lookup."""
    result = _probe("cobalt.modelaccess")
    assert result["error"] is None, result
    assert result["attempts"] == [], result
