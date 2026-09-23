"""Confirm, cancel, expire — CODE, never the model (FINAL [F-08], [F-09], L37).

While a row is `awaiting_confirm` and younger than `confirm_ttl_s`, the
turn makes NO model call: the whole normalized transcript must EQUAL a
confirm word (`yes`) — or he taps Confirm — to execute; a cancel word
(`no`) cancels; ANY other transcript ends the pending action with nothing
executed, and that transcript is not planned in the same turn. A confirm
word inside a request's own transcript never executes (the request's turn
never reaches this module).

ONE single-flight token: `awaiting_confirm → executing` is one
`UPDATE … WHERE state = …` — the first confirm or cancel commits; a second
in-flight request finds no pending action (X-X13). Execution RE-COMPUTES
the dry run and requires the same hashes (`tools.execute_stop`); a changed
target is REFUSED and the new before → after read aloud. A crash after the
expert's write and before `done` leaves the row `executing`; the reaper
fails it and nothing retries it.

NORMALIZATION: NFKC, Unicode casefold, strip whitespace, then strip leading
/ trailing `. , ! ?` — the engine writes a spoken yes as "Yes." (X-X1 and
X-E2 were counted with this same rule). Nothing inside the word changes.
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Optional

from loguru import logger

from .models import PendingAction, TurnState
from .registry import AgentSpec
from . import tools

_EDGE = ".,!?"


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text or "").casefold().strip().strip(_EDGE).strip()


def classify(transcript: str, agent: AgentSpec) -> str:
    """'confirm' | 'cancel' | 'other' — equality on the WHOLE transcript."""
    n = normalize(transcript)
    if n in agent.confirm_words:
        return "confirm"
    if n in agent.cancel_words:
        return "cancel"
    return "other"


@dataclass(frozen=True)
class PendingOutcome:
    kind: str  # done | no_pending | expired | cancelled | target_changed | refused | failed
    reply: str
    new_pending: Optional[PendingAction] = None
    stop_edit_id: Optional[int] = None


def _pending(row: dict[str, Any]) -> PendingAction:
    return PendingAction(**row["pending_action"])


def confirm_pending(store, row: dict[str, Any], *, now: datetime,
                    execute: Callable[[PendingAction], Any] = tools.execute_stop) -> PendingOutcome:
    tid = row["turn_id"]
    pending = _pending(row)
    if pending.expires_at <= now:
        store.transition(tid, {TurnState.AWAITING_CONFIRM}, TurnState.EXPIRED, at=now)
        return PendingOutcome("expired", "That change expired, so nothing was done. Say it again.")
    if not store.transition(tid, {TurnState.AWAITING_CONFIRM}, TurnState.EXECUTING, at=now):
        return PendingOutcome("no_pending", "There is no pending change to confirm.")
    from decimal import InvalidOperation

    from cobalt.aset.web import DevEntryRefused
    from cobalt.cards import CardStateError
    from cobalt.session import SessionBlocked

    try:
        edit = execute(pending)
    except tools.TargetChanged as e:
        store.transition(tid, {TurnState.EXECUTING}, TurnState.FAILED, at=now,
                         failure_class="target_changed", failure_detail="the card changed after the read-back")
        return PendingOutcome("target_changed", f"The card changed, so nothing was done. {e.new.readback}",
                              new_pending=e.new)
    except (CardStateError, SessionBlocked, DevEntryRefused, InvalidOperation, tools.Clarify) as e:
        store.transition(tid, {TurnState.EXECUTING}, TurnState.FAILED, at=now,
                         failure_class="expert_refused", failure_detail=str(e)[:500])
        logger.error("voice act {} REFUSED by its expert: {}", tid, e)
        return PendingOutcome("refused", f"Refused: {e}")
    except Exception as e:  # noqa: BLE001 - loud, named, and the row says so
        store.transition(tid, {TurnState.EXECUTING}, TurnState.FAILED, at=now,
                         failure_class="execute_error", failure_detail=f"{type(e).__name__}: {e}"[:500])
        logger.error("voice act {} FAILED: {}: {}", tid, type(e).__name__, e)
        return PendingOutcome("failed", f"The change failed ({type(e).__name__}); nothing is assumed done.")
    reply = f"Done. The stop on {pending.ticker}, card {pending.card_id}, is now {pending.to_stop}."
    store.transition(tid, {TurnState.EXECUTING}, TurnState.DONE, at=now,
                     expert_write_kind="card_stop_edits", expert_write_id=int(edit.stop_edit_id))
    return PendingOutcome("done", reply, stop_edit_id=int(edit.stop_edit_id))


def cancel_pending(store, row: dict[str, Any], *, now: datetime, reason: str) -> PendingOutcome:
    """`no`, a tap on Cancel, or any other transcript (`reason="other"`)."""
    if not store.transition(row["turn_id"], {TurnState.AWAITING_CONFIRM}, TurnState.CANCELLED, at=now):
        return PendingOutcome("no_pending", "There is no pending change to cancel.")
    if reason == "other":
        return PendingOutcome("cancelled", "I didn't hear yes, so nothing was changed. Say the request again.")
    return PendingOutcome("cancelled", "Cancelled. Nothing was changed.")


__all__ = ["PendingOutcome", "cancel_pending", "classify", "confirm_pending", "normalize"]
