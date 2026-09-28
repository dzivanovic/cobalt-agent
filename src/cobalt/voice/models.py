"""Typed data of a voice turn: the Plan (FINAL §2.4), its spans, the
closed candidate lists, the pending action and the turn state machine
(FINAL §7).
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class Span(BaseModel):
    """A VERBATIM substring of the transcript — checked by code, never trusted."""

    model_config = ConfigDict(extra="forbid")

    span: str = Field(min_length=1)


class CandidateRef(BaseModel):
    """An id from a CLOSED list code built for this turn."""

    model_config = ConfigDict(extra="forbid")

    candidate: str = Field(min_length=1)


ArgValue = Union[Span, CandidateRef]

PlanKind = Literal["answer", "act", "clarify", "unsupported", "refuse"]


class Plan(BaseModel):
    """What the model may say. Nothing in it executes by itself."""

    model_config = ConfigDict(extra="forbid")

    kind: PlanKind
    tool: Optional[str] = None
    args: dict[str, ArgValue] = Field(default_factory=dict)
    #: Optional prose. Figures in it must appear in the tool's own result
    #: or it is dropped (FINAL [F-05]).
    say: Optional[str] = None


class CardCandidate(BaseModel):
    """One open card as the model sees it: an id and a code-rendered label."""

    model_config = ConfigDict(extra="forbid")

    id: str
    card_id: int
    ticker: str
    direction: str
    state: str
    label: str


class HistoryTurn(BaseModel):
    """One earlier turn of THIS widget session, read from its row (L2)."""

    model_config = ConfigDict(extra="forbid")

    transcript: str
    reply: str


class PromptInputs(BaseModel):
    """EVERYTHING the prompt builder may use (L4 / L41 whitelist)."""

    model_config = ConfigDict(extra="forbid")

    transcript: str
    history: list[HistoryTurn]
    clock: str
    candidates: list[CardCandidate]


class PendingAction(BaseModel):
    """An ACT waiting for his confirmation (FINAL §2.6, [F-09])."""

    model_config = ConfigDict(extra="forbid")

    tool: Literal["cards.set_stop"]
    card_id: int
    ticker: str
    card_state: str
    from_stop: str
    to_stop: str
    readback: str
    diff_sha256: str
    target_sha256: str
    expires_at: datetime


class TurnState(str, Enum):
    """FINAL §7: received → transcribing → planned → (answered |
    awaiting_confirm → executing) → done | failed | cancelled | expired |
    unsupported."""

    RECEIVED = "received"
    TRANSCRIBING = "transcribing"
    PLANNED = "planned"
    ANSWERED = "answered"
    AWAITING_CONFIRM = "awaiting_confirm"
    EXECUTING = "executing"
    DONE = "done"
    FAILED = "failed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    UNSUPPORTED = "unsupported"


TERMINAL_STATES = frozenset({TurnState.DONE, TurnState.FAILED, TurnState.CANCELLED,
                             TurnState.EXPIRED, TurnState.UNSUPPORTED})

#: Legal edges. `answered → done` closes a read; a text turn skips
#: `transcribing`; every non-terminal state may fail.
EDGES: dict[TurnState, frozenset[TurnState]] = {
    TurnState.RECEIVED: frozenset({TurnState.TRANSCRIBING, TurnState.PLANNED, TurnState.DONE,
                                   TurnState.FAILED}),
    TurnState.TRANSCRIBING: frozenset({TurnState.PLANNED, TurnState.DONE, TurnState.FAILED}),
    TurnState.PLANNED: frozenset({TurnState.ANSWERED, TurnState.AWAITING_CONFIRM, TurnState.UNSUPPORTED,
                                  TurnState.DONE, TurnState.FAILED}),
    TurnState.ANSWERED: frozenset({TurnState.DONE, TurnState.FAILED}),
    TurnState.AWAITING_CONFIRM: frozenset({TurnState.EXECUTING, TurnState.CANCELLED, TurnState.EXPIRED,
                                          TurnState.FAILED}),
    TurnState.EXECUTING: frozenset({TurnState.DONE, TurnState.FAILED}),
}


class DegradedLine(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: Literal["red", "amber"]
    text: str


class TurnOutcome(BaseModel):
    """What the widget / the CLI shows. `reply` is spoken on the device."""

    model_config = ConfigDict(extra="forbid")

    turn_id: str
    state: TurnState
    reply: str
    transcript: Optional[str] = None
    pending_turn_id: Optional[str] = None
    readback: Optional[str] = None
    degraded: list[DegradedLine] = Field(default_factory=list)
    #: --dry-run only: the Plan, the resolution and the exact change.
    dry_run: Optional[dict] = None


__all__ = [
    "ArgValue", "CandidateRef", "CardCandidate", "DegradedLine", "EDGES", "HistoryTurn",
    "PendingAction", "Plan", "PlanKind", "PromptInputs", "Span", "TERMINAL_STATES",
    "TurnOutcome", "TurnState",
]
