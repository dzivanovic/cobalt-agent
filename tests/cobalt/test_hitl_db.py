"""F20 C2 — the HITL table and the acceptance path on `cobalt_dev` (T1; FINAL §6).

WITH-DB: every test runs in the suite's rollback transaction (conftest
`dev_db_tx`), so the module table `ensure_schema` creates is gone at the
end of the test and no row is left behind. The agents dir is `tmp_path`.
Constructed values only (L32).
"""

from __future__ import annotations

import os

import psycopg
import pytest

from hitl_support import AGENT_YAML, sha

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@pytest.fixture
def store():
    from cobalt.hitl.store import HitlStore

    s = HitlStore()
    s.ensure_schema()
    return s


def test_schema_and_placement(store):
    from cobalt import db, env

    with db.connect(env.resolve_db_name(), side=db.Side.USER) as conn:
        (schema,) = conn.execute(
            "SELECT table_schema FROM information_schema.tables WHERE table_name = %s",
            ("cobalt_hitl_requests",),
        ).fetchone()
        assert schema == "user"
        with pytest.raises(psycopg.errors.CheckViolation):
            with conn.transaction():
                conn.execute(
                    "INSERT INTO cobalt_hitl_requests (short_id, agent_id, action, payload, sha256, "
                    "rendered, reason, status, expires_at, approve_key_sha256) VALUES "
                    "('c0ffee00', 'cos', 'agents.create', '{}'::jsonb, 'x', '\\x00'::bytea, 'r', "
                    "'bogus', now(), 'k')"
                )


def _world(monkeypatch, tmp_path, store):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.hitl import actions
    from cobalt.jobs import killswitch

    agents = tmp_path / "agents"
    agents.mkdir()
    keys: dict[str, str] = {}
    monkeypatch.setattr(actions, "request_ttl_min", lambda: 60)
    monkeypatch.setattr(killswitch, "is_active", lambda *a, **k: False)

    def send(row_id, short_id, prepared, key):
        keys[short_id] = key

    def draft(yaml_text):
        out = actions.request_action("agents.create", {"yaml": yaml_text}, "constructed",
                                     store=store, agents_dir=agents, send=send)
        assert out.startswith("pending "), out
        short = out.split()[1]
        row = next(r for r in store.recent() if r["short_id"] == short)
        return row, keys[short]

    return TestClient(web_module.app), agents, draft


def test_draft_approve_execute_lists_the_agent(monkeypatch, tmp_path, store):
    from cobalt.agents.registry import list_agents
    from cobalt.hitl import executor

    client, agents, draft = _world(monkeypatch, tmp_path, store)

    row, key = draft(AGENT_YAML)
    assert "scout" not in {a.id for a in list_agents(agents)}
    r = client.post(f"/hitl/{row['id']}/approve", data={"sha256": row["sha256"], "k": key})
    assert "APPROVED" in r.text, r.text
    assert store.get(row["id"])["status"] == "approved"
    out = executor.run_one(store=store, agents_dir=agents, kill_active=lambda: False)
    assert out[1] == "executed"
    target = agents / "scout.yaml"
    assert sha(target.read_bytes()) == row["sha256"]
    assert "scout" in {a.id for a in list_agents(agents)}
    assert store.backs_sha256(row["sha256"])

    denied, denied_key = draft(AGENT_YAML.replace("id: scout", "id: denied_one"))
    r = client.post(f"/hitl/{denied['id']}/deny", data={"k": denied_key, "reason": "constructed"})
    assert "DENIED" in r.text
    late, _ = draft(AGENT_YAML.replace("id: scout", "id: late_one"))
    store.update_returning(
        "UPDATE cobalt_hitl_requests SET expires_at = now() - interval '1 minute' "
        "WHERE id = %s RETURNING id", (late["id"],))
    assert [x["id"] for x in executor.sweep(store=store)] == [late["id"]]
    assert executor.run_one(store=store, agents_dir=agents, kill_active=lambda: False) is None
    listed = {a.id for a in list_agents(agents)}
    assert "denied_one" not in listed and "late_one" not in listed
    assert store.get(denied["id"])["status"] == "denied"
    assert store.get(late["id"])["status"] == "expired"


def test_two_executors_claim_one_row(monkeypatch, tmp_path, store):
    """One approved row, two executor passes: one executes, the other finds
    nothing. The suite holds ONE session (conftest), so the two passes run
    in sequence; the claim statement is the SKIP LOCKED one (read below)."""
    import inspect

    from cobalt.hitl import executor
    from cobalt.hitl.store import HitlStore

    client, agents, draft = _world(monkeypatch, tmp_path, store)
    row, key = draft(AGENT_YAML)
    client.post(f"/hitl/{row['id']}/approve", data={"sha256": row["sha256"], "k": key})
    first = executor.run_one(store=store, agents_dir=agents, kill_active=lambda: False)
    second = executor.run_one(store=HitlStore(), agents_dir=agents, kill_active=lambda: False)
    assert first[1] == "executed" and second is None
    assert "FOR UPDATE SKIP LOCKED" in inspect.getsource(HitlStore.claim_next)
