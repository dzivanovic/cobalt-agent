"""F20 C2 — the HITL request, offline (FINAL §3 steps 1-4, F-06 B, F-08, F-18; L37).

The store is faked at the module seam (`hitl_support.FakeHitlStore`); the
with-DB file runs the real one. Constructed values only (L32): the token in
the secret test is built here, never a real credential.
"""

from __future__ import annotations

import ast
import hashlib
import re
from pathlib import Path

import pytest

from hitl_support import AGENT_YAML, FakeHitlStore, sha

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"


@pytest.fixture
def seam(monkeypatch, tmp_path):
    """A fake store, a `tmp_path` agents dir, a recorded card, a fixed TTL."""
    from cobalt.hitl import actions

    store = FakeHitlStore()
    sent: list[dict] = []
    agents = tmp_path / "agents"
    agents.mkdir()
    monkeypatch.setattr(actions, "request_ttl_min", lambda: 60)
    # Offline: the redactor's counter row is a database write (G1); the
    # `test_redact.py` precedent stubs it — the redaction itself still runs.
    monkeypatch.setattr("cobalt.redact.guard._record", lambda *a, **kw: None)

    def send(row_id, short_id, prepared, key):
        sent.append({"row_id": row_id, "short_id": short_id, "prepared": prepared, "key": key})

    def call(action, args, reason="constructed"):
        return actions.request_action(action, args, reason, store=store, agents_dir=agents, send=send)

    return store, sent, agents, call


# ---------------------------------------------------------------------
# C2a — the table is placed
# ---------------------------------------------------------------------


def test_the_table_is_placed():
    from cobalt.db import Side
    from cobalt.db_migrations.placement import side_of

    assert side_of("cobalt_hitl_requests") is Side.USER


# ---------------------------------------------------------------------
# C2b — the request
# ---------------------------------------------------------------------


def test_unknown_action_and_bad_arg_are_refused_no_row(seam):
    store, sent, _agents, call = seam
    assert call("trades.place", {"ticker": "ZZZZ"}).startswith("refused:")
    assert call("agents.create", {"yaml": AGENT_YAML, "extra": 1}).startswith("refused:")
    assert call("agents.create", {}).startswith("refused:")
    assert call("agents.create", {"yaml": "agent: [not, a, mapping"}).startswith("refused:")
    assert store.rows == {} and sent == []


def test_secret_shaped_arg_is_refused_no_row(seam):
    store, sent, _agents, call = seam
    constructed = "sk-" + "Q" * 32  # the shape of an API key, built here (L32)
    out = call("agents.create", {"yaml": AGENT_YAML.replace("says so.", f"says {constructed}.")})
    assert out.startswith("refused:") and constructed not in out
    assert store.rows == {} and sent == []


def test_sha256_is_over_the_rendered_bytes(seam):
    from cobalt.agents.registry import parse_entry, render_entry

    store, sent, _agents, call = seam
    out = call("agents.create", {"yaml": AGENT_YAML})
    assert out.startswith("pending ")
    (row,) = store.rows.values()
    assert row["status"] == "pending"
    assert out == f"pending {row['short_id']}"
    assert row["rendered"] == render_entry(parse_entry(AGENT_YAML, where="t"))
    assert row["sha256"] == hashlib.sha256(row["rendered"]).hexdigest()
    assert row["expires_at"] > store.now
    assert len(sent) == 1 and sent[0]["row_id"] == row["id"]


def test_deactivate_voice_and_cos_refused_at_request(seam):
    store, sent, agents, call = seam
    for protected in ("voice", "cos"):
        (agents / f"{protected}.yaml").write_text("agent: {}\n")
        assert call("agents.deactivate", {"id": protected}).startswith("refused:")
    assert store.rows == {} and sent == []
    # a registry entry that is neither is a request, with before and after bytes
    (agents / "scout.yaml").write_text(AGENT_YAML)
    assert call("agents.deactivate", {"id": "scout"}).startswith("pending ")
    (row,) = store.rows.values()
    assert row["before_bytes"] == AGENT_YAML.encode()
    assert row["before_sha256"] == sha(AGENT_YAML.encode())
    assert b"enabled: false" in row["rendered"] and row["sha256"] == sha(row["rendered"])


def test_only_the_key_hash_is_stored(seam):
    store, sent, _agents, call = seam
    call("agents.create", {"yaml": AGENT_YAML})
    (row,) = store.rows.values()
    key = sent[0]["key"]
    assert re.fullmatch(r"[0-9a-f]{32}", key), "a 128-bit key, hex"
    assert row["approve_key_sha256"] == sha(key.encode())
    assert key not in repr(row), "the row holds no key"


def test_card_dm_carries_the_fragment_and_is_redacted(monkeypatch):
    from cobalt.hitl import card
    from cobalt.notify import mattermost
    from cobalt.notify.config import MattermostConfig

    seen: list[str] = []
    real_redact = mattermost.redact

    def spy(text, **kw):
        seen.append(text)
        return real_redact(text, **kw)

    monkeypatch.setattr(mattermost, "redact", spy)
    monkeypatch.setattr("cobalt.redact.guard._record", lambda *a, **kw: None)  # G1, as above
    cfg =MattermostConfig(enabled=False, dm_username="constructed")
    key = "0123456789abcdef" * 2
    constructed = "sk-" + "Q" * 32
    result = card.send_card(
        7, "a1b2c3d4", card.CardFacts("agents.create", f"create agent scout {constructed}"), key,
        base_url="https://sheet.example.invalid", cfg=cfg,
    )
    assert seen, "the card went through send_dm's redaction"
    assert "https://sheet.example.invalid/hitl/7#k=" + key in seen[0]
    assert "a1b2c3d4" in seen[0] and "agents.create" in seen[0]
    assert result.redactions, "the constructed token was redacted on the way out (T8)"


# ---------------------------------------------------------------------
# C2c — T3: no approve path outside the two routes (L37)
# ---------------------------------------------------------------------

_APPROVE_WRITE = re.compile(r"SET\s+status\s*=\s*'approved'", re.I)
_VERB = re.compile(r"approve|decide|execut", re.I)
#: The modules whose names T3 rules on: every F20 package, and the sheet.
_F20_PACKAGES = ("hitl", "cos", "agents")


def _functions(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield node


def test_no_approve_symbol_outside_the_two_routes():
    write_sites, verb_sites = [], []
    for path in sorted(SRC.rglob("*.py")):
        rel = path.relative_to(SRC).as_posix()
        tree = ast.parse(path.read_text())
        owner: dict[int, str] = {}
        for fn in _functions(tree):
            for node in ast.walk(fn):
                owner.setdefault(id(node), fn.name)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and _APPROVE_WRITE.search(node.value):
                write_sites.append((rel, owner.get(id(node), "<module>")))
        if rel.split("/")[0] in _F20_PACKAGES or rel == "aset/web.py":
            for fn in _functions(tree):
                if _VERB.search(fn.name):
                    verb_sites.append((rel, fn.name))
    assert write_sites == [("aset/web.py", "hitl_approve")], write_sites
    allowed = {("aset/web.py", "hitl_approve")}
    strays = [s for s in verb_sites if s not in allowed and s[0] != "hitl/executor.py"]
    assert strays == [], f"approve/decide/execute names outside the two routes and the executor: {strays}"
    assert not [s for s in verb_sites if s[0].startswith(("cos/", "agents/"))]
