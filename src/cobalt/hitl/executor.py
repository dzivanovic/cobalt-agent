"""The deterministic executor and the sweeper (F20 FINAL §3 steps 6-7; F-08, F-15; L37, L40).

RUNS ONLY INSIDE THE CoS RESIDENT (`cos/run.py`), never in the aset web
process: the sheet he trades beside holds no executor and restarts for none.

ONE ROW PER CALL, claimed with `FOR UPDATE SKIP LOCKED` (`HitlStore.claim_next`).
The kill switch is checked before the claim and again on the claimed row;
while it is active nothing is executed and nothing is marked `failed`.

EVERY ENDING LEAVES ONE OF THREE STATES ON DISK: no file, the approved bytes,
or the untouched prior file.

* `agents.create` writes `rendered` verbatim, create-if-absent (`O_EXCL`).
  The target already holding exactly the approved bytes is a recovery (the
  previous run died between the write and the UPDATE): `executed`, logged
  loud. Any other existing file: `failed`, never overwritten.
* `agents.deactivate` writes the after-bytes only when the file still holds
  the before-bytes he reviewed; else `failed`.

No retry after `failed`. `expired` and `denied` are never runnable.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Callable, Optional

from loguru import logger

from cobalt.agents.registry import AGENTS_DIR

from .card import outcome_line


class _Held(Exception):
    """The kill switch engaged after the claim: roll the claim back."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _kill_active() -> bool:
    from cobalt.jobs import killswitch

    return killswitch.is_active()


def _create(row: dict, target: Path) -> tuple[str, dict, Optional[str]]:
    rendered = bytes(row["rendered"])
    if _sha(rendered) != row["sha256"]:
        return "failed", None, "the stored bytes do not hash to the approved sha256"
    try:
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError:
        on_disk = target.read_bytes()
        if _sha(on_disk) == row["sha256"]:
            logger.error("HITL {}: {} already holds the approved bytes — RECOVERED as executed "
                         "(a previous run wrote it and died before the UPDATE)", row["short_id"], target)
            return "executed", {"path": str(target), "recovered": True}, None
        return "failed", None, f"{target.name} exists with other bytes — not overwritten"
    except BaseException:
        # O_EXCL: the file did not exist before this call, so anything the
        # failed open left is ours — no file is the ending (X3).
        target.unlink(missing_ok=True)
        raise
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(rendered)
    except BaseException:
        # A short or failed write leaves no partial file (X3).
        target.unlink(missing_ok=True)
        raise
    return "executed", {"path": str(target), "recovered": False}, None


def _deactivate(row: dict, target: Path) -> tuple[str, dict, Optional[str]]:
    after = bytes(row["rendered"])
    if not target.exists():
        return "failed", None, f"{target.name} is gone — nothing deactivated"
    on_disk = target.read_bytes()
    if on_disk == after and _sha(after) == row["sha256"]:
        logger.error("HITL {}: {} already holds the after-bytes — RECOVERED as executed",
                     row["short_id"], target)
        return "executed", {"path": str(target), "recovered": True}, None
    before = row.get("before_bytes")
    if before is None or on_disk != bytes(before):
        return "failed", None, f"{target.name} moved since the card was made — not changed"
    # The after-bytes go to a sibling first and replace the file in one rename:
    # a failed write leaves the untouched prior file (X3; check r2 A1).
    staged = target.with_name(f".{target.name}.hitl-{row['short_id']}")
    try:
        staged.write_bytes(after)
        os.replace(staged, target)
    except BaseException:
        staged.unlink(missing_ok=True)
        raise
    return "executed", {"path": str(target), "recovered": False}, None


def run_one(
    *,
    store=None,
    agents_dir: Path = AGENTS_DIR,
    kill_active: Optional[Callable[[], bool]] = None,
) -> Optional[tuple[dict, str]]:
    """Claim and run one approved row. `(row, executed|failed)`, or None
    when nothing is approved or the kill switch holds the queue."""
    kill_active = kill_active or _kill_active
    if kill_active():
        logger.error("HITL executor: the kill switch is active — nothing executed, nothing failed")
        return None
    if store is None:
        from .store import HitlStore

        store = HitlStore()

    def handler(row: dict) -> tuple[str, Optional[dict], Optional[str]]:
        if kill_active():
            raise _Held()
        target = Path(agents_dir) / f"{row['payload']['target']}.yaml"
        try:
            if row["action"] == "agents.create":
                return _create(row, target)
            if row["action"] == "agents.deactivate":
                return _deactivate(row, target)
            return "failed", None, f"no executor for {row['action']!r}"
        except Exception as e:  # noqa: BLE001 - an executor exception fails the row, no retry
            return "failed", None, f"{type(e).__name__}: {e}"

    try:
        out = store.claim_next(handler)
    except _Held:
        logger.error("HITL executor: the kill switch engaged on a claimed row — held, not failed")
        return None
    if out is not None:
        row, status = out
        logger.info("HITL {} {}", row["short_id"], status)
    return out


def sweep(*, store=None) -> list[dict]:
    """`pending` past `expires_at` -> `expired` (F-15). The outcome DM is
    `report_outcomes`'; an approved row is never expired."""
    if store is None:
        from .store import HitlStore

        store = HitlStore()
    return store.expire_pending()


def report_outcomes(*, store=None, send: Optional[Callable[[str, str], object]] = None) -> list[str]:
    """DM each unreported terminal outcome once and return its session line,
    `HITL <id> executed|denied|expired|failed` (FINAL §3 step 6)."""
    if store is None:
        from .store import HitlStore

        store = HitlStore()
    if send is None:
        from .card import send_outcome as send
    lines = []
    for row in store.unreported():
        send(row["short_id"], row["status"])
        store.mark_reported(row["id"])
        lines.append(outcome_line(row["short_id"], row["status"]))
    return lines


__all__ = ["report_outcomes", "run_one", "sweep"]
