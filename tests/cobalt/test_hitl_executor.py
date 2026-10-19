"""F20 C2d — the executor and the sweeper (FINAL §3 steps 6-7, F-08, F-15; L37, L40).

`tmp_path` agents dir, the store faked at the seam. Every ending leaves no
file, the approved bytes, or the untouched prior file (check ask X3).
"""

from __future__ import annotations

from datetime import timedelta

import pytest

from hitl_support import AGENT_YAML, FakeHitlStore, sha


@pytest.fixture
def world(tmp_path):
    agents = tmp_path / "agents"
    agents.mkdir()
    return FakeHitlStore(), agents


def _run(store, agents, *, kill=False):
    from cobalt.hitl import executor

    return executor.run_one(store=store, agents_dir=agents, kill_active=lambda: kill)


def test_create_writes_rendered_bytes_and_executes(world):
    store, agents = world
    row_id, _ = store.add(status="approved")
    out = _run(store, agents)
    assert out is not None and out[1] == "executed"
    target = agents / "scout.yaml"
    assert target.read_bytes() == store.rows[row_id]["rendered"]
    assert sha(target.read_bytes()) == store.rows[row_id]["sha256"]
    assert store.rows[row_id]["status"] == "executed"
    assert _run(store, agents) is None, "nothing approved is left"


def test_existing_same_hash_recovers_executed(world):
    """X8's shape: the executor died after the write and before the UPDATE —
    the row is still `approved`, the file holds the approved bytes; the next
    poll marks it executed and never loops or fails."""
    store, agents = world
    row_id, _ = store.add(status="approved")
    (agents / "scout.yaml").write_bytes(store.rows[row_id]["rendered"])
    out = _run(store, agents)
    assert out[1] == "executed"
    assert "recovered" in str(store.rows[row_id]["result"])


def test_existing_other_bytes_fails_no_overwrite(world):
    store, agents = world
    row_id, _ = store.add(status="approved")
    prior = b"agent:\n  id: scout\n  charter: somebody else's file\n"
    (agents / "scout.yaml").write_bytes(prior)
    out = _run(store, agents)
    assert out[1] == "failed" and store.rows[row_id]["error"]
    assert (agents / "scout.yaml").read_bytes() == prior
    assert _run(store, agents) is None, "no retry after failed"


def test_deactivate_refused_when_bytes_moved(world):
    store, agents = world
    before = AGENT_YAML.encode()
    after = before.replace(b"enabled: true", b"enabled: false")
    moved = before.replace(b"says so.", b"says more.")
    (agents / "scout.yaml").write_bytes(moved)
    row_id, _ = store.add(status="approved", action="agents.deactivate", rendered=after)
    store.rows[row_id].update(before_bytes=before, before_sha256=sha(before))
    assert _run(store, agents)[1] == "failed"
    assert (agents / "scout.yaml").read_bytes() == moved

    (agents / "scout.yaml").write_bytes(before)
    ok_id, _ = store.add(status="approved", action="agents.deactivate", rendered=after)
    store.rows[ok_id].update(before_bytes=before, before_sha256=sha(before))
    assert _run(store, agents)[1] == "executed"
    assert (agents / "scout.yaml").read_bytes() == after


def test_kill_switch_holds_without_failing(world):
    store, agents = world
    row_id, _ = store.add(status="approved")
    assert _run(store, agents, kill=True) is None
    assert store.rows[row_id]["status"] == "approved"
    assert not (agents / "scout.yaml").exists()


def test_sweeper_expires_pending_only(world):
    from cobalt.hitl import executor

    store, agents = world
    late, _ = store.add(expires_at=store.now - timedelta(minutes=1))
    fresh, _ = store.add()
    tapped, _ = store.add(status="approved", expires_at=store.now - timedelta(minutes=1))
    expired = executor.sweep(store=store)
    assert [r["id"] for r in expired] == [late]
    assert store.rows[late]["status"] == "expired"
    assert store.rows[fresh]["status"] == "pending"
    assert store.rows[tapped]["status"] == "approved", "an approved row is never expired"
    store.rows[late]["status"] = "expired"
    assert _run(store, agents)[0]["id"] == tapped, "expired is not runnable; approved is"

    sent: list[str] = []
    lines = executor.report_outcomes(store=store, send=lambda short, status: sent.append(status))
    assert sorted(sent) == ["executed", "expired"]
    assert all(line.startswith("HITL ") for line in lines)
    assert executor.report_outcomes(store=store, send=lambda *a: None) == [], "each outcome once"


# ---------------------------------------------------------------------
# check (CHECK-HUB ## 4) — findings run as written
# ---------------------------------------------------------------------


def test_check_o8_a_failed_write_leaves_no_file(world, monkeypatch):
    from cobalt.hitl import executor

    class Broken:
        def __init__(self, fd, mode):
            import os
            os.close(fd)

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def write(self, data):
            raise OSError(28, "constructed: no space left on device")

    monkeypatch.setattr(executor.os, "fdopen", Broken)
    store, agents = world
    row_id, _ = store.add(status="approved")
    out = _run(store, agents)
    assert out[1] == "failed"
    assert not (agents / "scout.yaml").exists(), "no file, the approved bytes, or the prior file"


def test_create_error_after_the_file_exists_leaves_no_partial(world, monkeypatch):
    import os

    store, agents = world
    row_id, _ = store.add(status="approved")
    rendered = bytes(store.rows[row_id]["rendered"])
    real_open = os.open

    def open_then_fail(path, flags, mode=0o777, *, dir_fd=None):
        fd = real_open(path, flags, mode)
        os.close(fd)
        raise OSError("constructed disk full")

    monkeypatch.setattr(os, "open", open_then_fail)
    out = _run(store, agents)
    target = agents / "scout.yaml"
    assert out is not None and out[1] == "failed"
    assert (not target.exists()) or target.read_bytes() == rendered


def test_deactivate_write_error_leaves_the_prior_bytes(world, monkeypatch):
    from cobalt.hitl import executor

    store, agents = world
    before = AGENT_YAML.encode()
    after = before.replace(b"enabled: true", b"enabled: false")
    target = agents / "scout.yaml"
    target.write_bytes(before)
    row_id, _ = store.add(status="approved", action="agents.deactivate", rendered=after)
    store.rows[row_id].update(before_bytes=before, before_sha256=sha(before))

    def truncate_then_fail(self, data):
        with open(self, "wb"):
            pass
        raise OSError(28, "constructed: no space left on device")

    monkeypatch.setattr(executor.Path, "write_bytes", truncate_then_fail)
    out = _run(store, agents)
    assert out is not None and out[1] == "failed"
    assert target.read_bytes() == before
