"""F20 HITL test support: an in-memory `HitlStore` at the module seam.

The fake keeps the store's contract — the same method names, the same row
keys — so the offline tests of actions, the page and the executor exercise
the code above the store. The with-DB tests (`test_hitl_db.py`) run the
real store and the real SQL on `cobalt_dev`. Constructed values only (L32).
"""

from __future__ import annotations

import hashlib
import secrets
from datetime import datetime, timedelta, timezone

#: A constructed agent file (L32): no charter text of his.
AGENT_YAML = """agent:
  id: scout
  charter: A constructed test agent. It reads the radar pool and says so.
  chassis: {kind: sdk, auth: subscription, model: claude-sonnet-5-5}
  tools: [radar.pool]
  memory_namespace: scout
  enabled: true
"""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class FakeHitlStore:
    """Rows in a dict. `update_returning` reads the two route statements by
    their status literal and applies their WHERE clause to the row."""

    def __init__(self, now: datetime | None = None):
        self.rows: dict[int, dict] = {}
        self.next_id = 1
        self.now = now or datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
        self.calls: list[str] = []

    def ensure_schema(self):
        self.calls.append("ensure_schema")

    def insert(self, *, agent_id, action, payload, sha256, rendered, before_sha256, before_bytes,
               reason, ttl_min, approve_key_sha256):
        self.calls.append("insert")
        expires_at = self.now + timedelta(minutes=ttl_min)
        row_id = self.next_id
        self.next_id += 1
        short = secrets.token_hex(4)
        self.rows[row_id] = {
            "id": row_id, "short_id": short, "agent_id": agent_id, "action": action,
            "payload": payload, "sha256": sha256, "rendered": rendered,
            "before_sha256": before_sha256, "before_bytes": before_bytes, "reason": reason,
            "status": "pending", "created_at": self.now, "expires_at": expires_at,
            "decided_at": None, "decided_via": None, "deny_reason": None, "result": None,
            "error": None, "approve_key_sha256": approve_key_sha256, "reported_at": None,
        }
        return row_id, short

    def get(self, row_id):
        row = self.rows.get(int(row_id))
        return dict(row) if row else None

    def recent(self, limit=50):
        return [dict(r) for r in sorted(self.rows.values(), key=lambda r: -r["id"])][:limit]

    def update_returning(self, sql, params):
        self.calls.append("update_returning")
        if "status='approved'" in sql:
            row_id, sha256, key_sha = params
            row = self.rows.get(int(row_id))
            if (row and row["status"] == "pending" and row["expires_at"] > self.now
                    and row["sha256"] == sha256 and row["approve_key_sha256"] == key_sha):
                row.update(status="approved", decided_at=self.now,
                           decided_via=f"aset.hitl@sha256:{row['sha256']}")
                return [(row["id"],)]
            return []
        if "status='denied'" in sql:
            reason, row_id, key_sha = params
            row = self.rows.get(int(row_id))
            if row and row["status"] == "pending" and row["approve_key_sha256"] == key_sha:
                row.update(status="denied", decided_at=self.now, deny_reason=reason,
                           decided_via=f"aset.hitl@sha256:{row['sha256']}")
                return [(row["id"],)]
            return []
        raise AssertionError(f"unexpected statement: {sql}")

    def claim_next(self, handler):
        for row in sorted(self.rows.values(), key=lambda r: r["id"]):
            if row["status"] == "approved":
                status, result, error = handler(dict(row))
                row.update(status=status, result=result, error=error)
                return dict(row), status
        return None

    def expire_pending(self):
        out = []
        for row in self.rows.values():
            if row["status"] == "pending" and row["expires_at"] < self.now:
                row["status"] = "expired"
                out.append(dict(row))
        return out

    def unreported(self):
        return [dict(r) for r in self.rows.values()
                if r["status"] in ("executed", "failed", "denied", "expired") and r["reported_at"] is None]

    def mark_reported(self, row_id):
        self.rows[int(row_id)]["reported_at"] = self.now

    def backs_sha256(self, sha256):
        return any(r["status"] == "executed" and r["sha256"] == sha256 for r in self.rows.values())

    def probe_counts(self):
        return {
            "pending_past_ttl": sum(1 for r in self.rows.values()
                                    if r["status"] == "pending" and r["expires_at"] < self.now),
            "failed": sum(1 for r in self.rows.values() if r["status"] == "failed"),
        }

    # -- test helpers ------------------------------------------------------

    def add(self, **over):
        """A pending row the way `request_action` writes one, with its key."""
        key = over.pop("key", secrets.token_hex(16))
        rendered = over.pop("rendered", AGENT_YAML.encode())
        row_id, short = self.insert(
            agent_id="cos", action=over.pop("action", "agents.create"),
            payload=over.pop("payload", {"target": "scout"}), sha256=sha(rendered),
            rendered=rendered, before_sha256=None, before_bytes=None,
            reason=over.pop("reason", "constructed"), ttl_min=60,
            approve_key_sha256=sha(key.encode()),
        )
        self.rows[row_id].update(over)
        return row_id, key
