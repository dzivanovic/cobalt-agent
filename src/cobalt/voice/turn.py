"""THE turn function (FINAL [F-01]): ONE `run_turn` with three callers —
`POST /voice/turn` (voice/web.py), `cobalt voice turn` (voice/cli.py) and
the tests. A text turn is the same function without the audio stages.

ONE TURN, IN ORDER (FINAL §2, §7):
1. reap stuck rows (L18); a tap goes straight to the pending action.
2. the row (`received`); for audio: `transcribing`, the clip written to
   scratch by the ONE writer, its length probed (`max_clip_s`), the
   transcript under `stt_timeout_s`, the file UNLINKED right after — and in
   `finally:` on every failure path; only sha256 / length / duration kept.
3. empty transcript → "I heard nothing", no plan, no write.
4. a live pending action in THIS widget session → NO model call: `yes`
   confirms, `no` cancels, anything else ends it; the transcript is not
   planned (FINAL [F-08]).
5. ONE Plan call (voice/agent.py, through cobalt.modelaccess) → `planned`.
6. HARD REFUSALS by code whatever the Plan says (voice/tools.py).
7. read → a code template (`answered` → `done`); act → resolve the card,
   parse the value, dry-run the exact change → `awaiting_confirm` with the
   read-back. Nothing is written by an act here; only a confirm executes.
Every failure is a named `failure_class` on the row and a line he hears
(L1, L9). `dry_run` (the CLI's) returns the Plan, the resolution and the
exact change and writes NOTHING — no row, no pending action.
"""

from __future__ import annotations

import functools
import hashlib
import re
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Literal, Optional

from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, model_validator

from cobalt import env

from . import agent as agent_mod
from . import confirm as confirm_mod
from . import scratch, tools
from .config import VoiceConfig
from .models import (CandidateRef, DegradedLine, HistoryTurn, PromptInputs, Span, TurnOutcome, TurnState)
from .registry import AgentSpec
from .resolve import Unparseable, card_candidates, parse_price, resolve_card
from .store import reap_limits
from .transcribe import SttDown, probe_duration_s, transcribe_with_timeout

CLARIFY_TEMPLATE = "I need a little more: which card, and what value?"
_SESSION = re.compile(r"^[A-Za-z0-9-]{4,64}$")


class TurnInput(BaseModel):
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    session_id: str
    source: Literal["widget", "cli", "test"]
    text: Optional[str] = None
    audio: Optional[bytes] = None
    content_type: Optional[str] = None
    tap: Optional[Literal["confirm", "cancel"]] = None
    pending_turn_id: Optional[str] = None
    dry_run: bool = False
    turn_id: Optional[str] = None

    @model_validator(mode="after")
    def _one_input(self):
        if not _SESSION.match(self.session_id or ""):
            raise ValueError("session_id must be 4-64 letters, digits or dashes")
        given = [x is not None for x in (self.text, self.audio, self.tap)]
        if sum(given) != 1:
            raise ValueError("a turn carries exactly one of text, audio or a tap")
        if self.tap and not self.pending_turn_id:
            raise ValueError("a tap names the pending turn it answers")
        if self.audio is not None and not self.content_type:
            raise ValueError("an audio turn carries its content type")
        return self


@dataclass
class TurnDeps:
    """Everything a turn touches, injected (the tests pass fakes)."""

    cfg: VoiceConfig
    agent: AgentSpec
    store: Any
    transcriber: Any
    plan: Callable
    read_cards: Callable[[], list]
    read_pool: Callable[[], dict]
    execute: Callable
    now: Callable[[], datetime]
    plan_timeout_s: float
    probe_duration: Callable[[Path], float] = probe_duration_s
    extra: dict = field(default_factory=dict)


def default_deps() -> TurnDeps:
    """The real wiring (the route, the CLI). Config errors crash (L1)."""
    from cobalt.modelaccess import load_routes
    from cobalt.session import clock as clock_mod

    from .config import load_voice_config
    from .registry import load_agent
    from .store import VoiceTurnStore
    from .transcribe import make_transcriber

    cfg = load_voice_config()
    agent = load_agent()
    return TurnDeps(
        cfg=cfg, agent=agent, store=VoiceTurnStore(), transcriber=make_transcriber(cfg),
        plan=agent_mod.plan_turn, read_cards=tools.read_open_cards, read_pool=tools.read_pool,
        execute=functools.partial(tools.execute_stop, ttl_s=cfg.confirm_ttl_s),
        now=lambda: clock_mod.now_utc(),
        plan_timeout_s=load_routes().routes[agent.route].timeout_s,
    )


def new_turn_id() -> str:
    return f"turn-{uuid.uuid4().hex}"


class _Fail(Exception):
    def __init__(self, cls: str, reply: str, *, red: bool = False, detail: str = ""):
        self.cls, self.reply, self.red, self.detail = cls, reply, red, detail or reply
        super().__init__(reply)


class _Rec:
    """The row, moved one single-flight step at a time. No-ops in a dry run."""

    def __init__(self, deps: TurnDeps, turn_id: str, dry: bool):
        self.deps, self.tid, self.dry = deps, turn_id, dry
        self.state: Optional[TurnState] = None

    def create(self, inp: TurnInput, input_kind: str, confirm_of: Optional[str] = None) -> None:
        if self.dry:
            return
        self.deps.store.create(turn_id=self.tid, session_id=inp.session_id, source=inp.source,
                               input_kind=input_kind, at=self.deps.now(), confirm_of=confirm_of)
        self.state = TurnState.RECEIVED

    def update(self, **fields) -> None:
        if not self.dry and self.state is not None and fields:
            self.deps.store.update(self.tid, **fields)

    def go(self, new: TurnState, **fields) -> None:
        if self.dry:
            return
        if not self.deps.store.transition(self.tid, {self.state}, new, at=self.deps.now(), **fields):
            raise RuntimeError(f"turn {self.tid} could not move {self.state} → {new.value}")
        self.state = new

    def fail(self, f: _Fail) -> None:
        if self.dry or self.state is None:
            return
        self.deps.store.transition(self.tid, {self.state}, TurnState.FAILED, at=self.deps.now(),
                                   failure_class=f.cls, failure_detail=f.detail[:500], reply=f.reply)
        self.state = TurnState.FAILED


def _outcome(rec: _Rec, state: TurnState, reply: str, **kw) -> TurnOutcome:
    return TurnOutcome(turn_id=rec.tid, state=state, reply=reply, **kw)


def _clock(now: datetime) -> str:
    from cobalt.session.clock import session_clock

    et = session_clock().to_et(now)
    return f"{et:%Y-%m-%d %H:%M} ET ({et:%A})"


# --- the audio stage ------------------------------------------------------------------


def _hear(inp: TurnInput, deps: TurnDeps, rec: _Rec, degraded: list[DegradedLine]) -> str:
    cfg = deps.cfg
    rec.go(TurnState.TRANSCRIBING)
    held: Optional[scratch.HeldAudio] = None
    duration_s: Optional[float] = None
    try:
        with scratch.turn_audio(cfg.scratch_dir, rec.tid, inp.audio, inp.content_type) as held:
            try:
                duration_s = deps.probe_duration(held.path)
            except SttDown as e:
                raise _Fail("voice_stt", str(e), red=True, detail=e.detail) from None
            if duration_s > cfg.max_clip_s:
                raise _Fail("clip_too_long", f"That clip is too long ({duration_s:.0f} s; the limit is "
                                             f"{cfg.max_clip_s:.0f} s). Say it again, shorter.")
            try:
                t = transcribe_with_timeout(deps.transcriber, held.path, timeout_s=cfg.stt_timeout_s)
            except SttDown as e:
                raise _Fail("voice_stt", str(e), red=True, detail=e.detail) from None
            held.unlink_now("transcribed")
    except scratch.ScratchRefused as e:
        raise _Fail("audio_refused", f"That recording could not be used: {e}") from None
    except scratch.ScratchUnlinkFailed as e:
        degraded.append(DegradedLine(level="red", text=str(e)))
        raise _Fail("scratch_unlink", "The recording could not be deleted — the turn stops here.", red=True,
                    detail=str(e)) from None
    except scratch.ScratchWriteFailed as e:
        degraded.append(DegradedLine(level="red", text=str(e)))
        raise _Fail("scratch_write", "The recording could not be saved — the turn stops here.", red=True,
                    detail=str(e)) from None
    finally:
        if held is not None:
            rec.update(audio_sha256=hashlib.sha256(inp.audio).hexdigest(), audio_bytes=held.size,
                       audio_duration_ms=int((duration_s or 0) * 1000) or None,
                       audio_deleted_at=held.deleted_at)
    rec.update(transcript=t.text, stt_engine=t.engine, stt_model=t.model, stt_revision=t.revision, stt_ms=t.stt_ms)
    return t.text


# --- the pending action ------------------------------------------------------------------


def _expired(row: dict, now: datetime) -> bool:
    from .models import PendingAction

    return PendingAction(**row["pending_action"]).expires_at <= now


def _answer_pending(inp: TurnInput, deps: TurnDeps, rec: _Rec, row: dict, transcript: str) -> TurnOutcome:
    rec.update(confirm_of=row["turn_id"])
    word = confirm_mod.classify(transcript, deps.agent)
    now = deps.now()
    if word == "confirm":
        res = confirm_mod.confirm_pending(deps.store, row, now=now, execute=deps.execute)
    else:
        res = confirm_mod.cancel_pending(deps.store, row, now=now, reason="no" if word == "cancel" else "other")
    return _after_pending(deps, rec, res)


#: A confirmed act that did not land is a RED line he sees (FINAL §7, L1):
#: it failed, or its expert refused it.
_RED_OUTCOMES = ("failed", "refused")

#: [F-02] / L37: in production an act is confirmed only by the widget.
CLI_CONFIRM_REFUSED = ("In production an act is confirmed only in the widget (a tap, or your next turn there) — "
                       "no house confirms a production act (L37, FINAL [F-02]). The change is still pending there; "
                       "nothing was done.")


def _after_pending(deps: TurnDeps, rec: _Rec, res: confirm_mod.PendingOutcome) -> TurnOutcome:
    if res.kind == "target_changed" and res.new_pending is not None:
        rec.go(TurnState.PLANNED)
        rec.go(TurnState.AWAITING_CONFIRM, pending_action=res.new_pending.model_dump(mode="json"), reply=res.reply)
        return _outcome(rec, TurnState.AWAITING_CONFIRM, res.reply, pending_turn_id=rec.tid,
                        readback=res.new_pending.readback)
    rec.go(TurnState.DONE, reply=res.reply, resolution={"pending_outcome": res.kind})
    degraded = [DegradedLine(level="red", text=res.reply)] if res.kind in _RED_OUTCOMES else []
    return _outcome(rec, TurnState.DONE, res.reply, degraded=degraded)


def _tap(inp: TurnInput, deps: TurnDeps) -> TurnOutcome:
    row = deps.store.get(inp.pending_turn_id)
    rec = _Rec(deps, inp.pending_turn_id, dry=True)  # a tap writes through confirm_mod only
    if row is None or row["session_id"] != inp.session_id or row["state"] != TurnState.AWAITING_CONFIRM.value:
        return _outcome(rec, TurnState.DONE, "There is no pending change to confirm.")
    now = deps.now()
    if inp.tap == "confirm":
        res = confirm_mod.confirm_pending(deps.store, row, now=now, execute=deps.execute)
    else:
        res = confirm_mod.cancel_pending(deps.store, row, now=now, reason="no")
    if res.kind == "target_changed" and res.new_pending is not None:
        rec2 = _Rec(deps, new_turn_id(), dry=False)
        rec2.create(inp, "text", confirm_of=row["turn_id"])
        return _after_pending(deps, rec2, res)
    state = TurnState.DONE
    return _outcome(rec, state, res.reply,
                    degraded=[DegradedLine(level="red", text=res.reply)] if res.kind in _RED_OUTCOMES else [])


# --- the Plan and what follows it ------------------------------------------------------------


def _card_by_id(cards: list[dict], card_id: int) -> dict:
    return next(c for c in cards if c["id"] == card_id)


def _plan_and_act(inp: TurnInput, deps: TurnDeps, rec: _Rec, transcript: str) -> TurnOutcome:
    cfg, agent = deps.cfg, deps.agent
    try:
        cards = deps.read_cards()
    except tools.ToolReadFailed as e:
        raise _Fail("tool_read", str(e), red=True) from None
    candidates = card_candidates(cards)
    history = [HistoryTurn(transcript=t, reply=r) for t, r in deps.store.history(inp.session_id, cfg.history_turns)]
    inputs = PromptInputs(transcript=transcript, history=history, clock=_clock(deps.now()), candidates=candidates)
    try:
        po = deps.plan(inputs, agent=agent, turn_id=rec.tid)
    except agent_mod.PlanFailed as e:
        if e.result is not None:
            rec.update(plan_route=e.result.route, model_returned=e.result.model_returned,
                       plan_latency_ms=e.result.latency_ms,
                       plan_usage=e.result.usage.model_dump())
        raise _Fail("voice_plan", f"Cobalt can't think right now ({e.kind}).", red=True,
                    detail=f"{e.kind}: {e.detail}") from None
    plan = po.plan
    rec.go(TurnState.PLANNED, plan=plan.model_dump(mode="json"), plan_route=po.result.route,
           model_returned=po.result.model_returned, plan_latency_ms=po.result.latency_ms,
           plan_usage=po.result.usage.model_dump())
    dry = {"plan": plan.model_dump(mode="json"), "resolution": None, "change": None} if inp.dry_run else None

    refusal = tools.code_refusal(transcript, plan, agent)
    if refusal is not None:
        resolution = {"refusal": refusal.reason}
        if dry is not None:
            dry["resolution"] = resolution
        if refusal.kind == "unsupported":
            rec.go(TurnState.UNSUPPORTED, reply=refusal.reply, resolution=resolution)
            return _outcome(rec, TurnState.UNSUPPORTED, refusal.reply, dry_run=dry)
        rec.go(TurnState.DONE, reply=refusal.reply, resolution=resolution)
        return _outcome(rec, TurnState.DONE, refusal.reply, dry_run=dry)

    def done(reply: str, resolution: dict) -> TurnOutcome:
        if dry is not None:
            dry["resolution"] = resolution
        rec.go(TurnState.DONE, reply=reply, resolution=resolution)
        return _outcome(rec, TurnState.DONE, reply, dry_run=dry)

    if plan.kind == "clarify":
        return done(tools.compose_reply(plan.say, CLARIFY_TEMPLATE), {"clarify": "plan"})

    if plan.kind == "answer":
        if plan.tool == "cards.open":
            template, resolution = tools.render_open_cards(cards), {"tool": "cards.open", "cards": len(cards)}
        elif plan.tool == "radar.pool":
            try:
                template = tools.render_pool(deps.read_pool())
            except tools.ToolReadFailed as e:
                raise _Fail("tool_read", str(e), red=True) from None
            resolution = {"tool": "radar.pool"}
        else:  # cards.numbers
            r = resolve_card(plan.args, transcript, candidates)
            if not r.bound:
                return done(r.clarify, {"clarify": "card"})
            template = tools.render_numbers(_card_by_id(cards, r.card_id))
            resolution = {"tool": "cards.numbers", "card_id": r.card_id}
        reply = tools.compose_reply(plan.say, template)
        if dry is not None:
            dry["resolution"] = resolution
        rec.go(TurnState.ANSWERED, reply=reply, resolution=resolution)
        rec.go(TurnState.DONE)
        return _outcome(rec, TurnState.DONE, reply, dry_run=dry)

    # plan.kind == "act" — V1's one act: cards.set_stop
    r = resolve_card(plan.args, transcript, candidates)
    if not r.bound:
        return done(r.clarify, {"clarify": "card"})
    stop_arg = plan.args.get("stop")
    if stop_arg is None:
        return done("What price should the stop be?", {"clarify": "value", "card_id": r.card_id})
    if not isinstance(stop_arg, Span):
        return done("Say the stop price, like four point five zero.", {"clarify": "value", "card_id": r.card_id})
    try:
        price = parse_price(stop_arg.span)
    except Unparseable as e:
        return done(f"I couldn't read the price ({e}). Say it with 'point', like four point five zero.",
                    {"clarify": "value", "card_id": r.card_id, "heard": stop_arg.span})
    card = _card_by_id(cards, r.card_id)
    try:
        pending = tools.stop_dry_run(card, price, ttl_s=cfg.confirm_ttl_s, now=deps.now())
    except tools.Clarify as e:
        return done(str(e), {"clarify": "value_guard", "card_id": r.card_id, "heard": stop_arg.span})
    resolution = {"tool": "cards.set_stop", "card_id": r.card_id, "to_stop": pending.to_stop}
    if dry is not None:
        dry["resolution"] = resolution
        dry["change"] = pending.model_dump(mode="json")
        return _outcome(rec, TurnState.PLANNED, pending.readback, dry_run=dry)
    rec.go(TurnState.AWAITING_CONFIRM, pending_action=pending.model_dump(mode="json"), reply=pending.readback,
           resolution=resolution)
    return _outcome(rec, TurnState.AWAITING_CONFIRM, pending.readback, pending_turn_id=rec.tid,
                    readback=pending.readback)


# --- THE turn function -------------------------------------------------------------------------


def run_turn(inp: TurnInput, deps: TurnDeps) -> TurnOutcome:
    if inp.tap:
        return _tap(inp, deps)
    if not inp.dry_run:
        deps.store.reap(now=deps.now(), limits=reap_limits(stt_timeout_s=deps.cfg.stt_timeout_s,
                                                          plan_timeout_s=deps.plan_timeout_s))
    rec = _Rec(deps, inp.turn_id or new_turn_id(), dry=inp.dry_run)
    degraded: list[DegradedLine] = []
    transcript: Optional[str] = None
    try:
        rec.create(inp, "audio" if inp.audio is not None else "text")
        if inp.audio is not None:
            transcript = _hear(inp, deps, rec, degraded)
        else:
            transcript = (inp.text or "").strip()
            rec.update(transcript=transcript or None)
        if not transcript or not transcript.strip():
            raise _Fail("empty_transcript", "I heard nothing.")
        transcript = transcript.strip()
        if not inp.dry_run:
            row = deps.store.pending_for_session(inp.session_id)
            if row is not None and inp.source != "widget" and env.is_production():
                # Refused WHOLE: nothing executed, the pending row left
                # `awaiting_confirm` for the widget ([F-02], L37).
                raise _Fail("cli_confirm_refused", CLI_CONFIRM_REFUSED, red=True,
                            detail=f"a {inp.source} turn found pending act {row['turn_id']} in production")
            if row is not None:
                if _expired(row, deps.now()):
                    deps.store.transition(row["turn_id"], {TurnState.AWAITING_CONFIRM}, TurnState.EXPIRED,
                                          at=deps.now())
                    if confirm_mod.classify(transcript, deps.agent) != "other":
                        rec.update(confirm_of=row["turn_id"])
                        reply = "That change expired, so nothing was done. Say it again."
                        rec.go(TurnState.DONE, reply=reply, resolution={"pending_outcome": "expired"})
                        return _outcome(rec, TurnState.DONE, reply, transcript=transcript)
                else:
                    out = _answer_pending(inp, deps, rec, row, transcript)
                    return out.model_copy(update={"transcript": transcript})
        out = _plan_and_act(inp, deps, rec, transcript)
        return out.model_copy(update={"transcript": transcript, "degraded": degraded + out.degraded})
    except _Fail as f:
        rec.fail(f)
        if f.red:
            degraded.append(DegradedLine(level="red", text=f.reply))
        logger.error("voice turn {} FAILED ({}): {}", rec.tid, f.cls, f.detail)
        return _outcome(rec, TurnState.FAILED, f.reply, transcript=transcript, degraded=degraded)
    except Exception as e:  # noqa: BLE001 - loud, named, on the row
        f = _Fail("turn_error", f"Something failed in this turn ({type(e).__name__}); nothing was changed.",
                  red=True, detail=f"{type(e).__name__}: {e}")
        rec.fail(f)
        logger.error("voice turn {} FAILED (turn_error): {}: {}", rec.tid, type(e).__name__, e)
        degraded.append(DegradedLine(level="red", text=f.reply))
        return _outcome(rec, TurnState.FAILED, f.reply, transcript=transcript, degraded=degraded)


__all__ = ["CLARIFY_TEMPLATE", "TurnDeps", "TurnInput", "default_deps", "new_turn_id", "run_turn"]
