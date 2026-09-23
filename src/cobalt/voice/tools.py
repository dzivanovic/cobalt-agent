"""The voice tools: READ tools answered by code templates, the ONE act's
dry run, the figures check and the HARD REFUSALS (FINAL §2.4, §3).

TOOLS FETCH, CODE RENDERS. A read tool returns stored data and the reply
is a CODE TEMPLATE over it: `cards.open` / `cards.numbers` read
`CardStore().open_cards()` (the sheet's own read); `radar.pool` calls the
`/api/radar/pool` route function itself — never a second query path. No
tool calls `/size` or the sizer, or computes a score, rank, grade or size.

THE FIGURES CHECK [F-05]. A numeric token (maximal run of digits with at
most one decimal point) in the model's `say` that is not a numeric token of
the tool's rendered result drops `say`; the template is spoken alone.

HARD REFUSALS, WHATEVER THE PLAN SAYS. An order / platform request →
`refuse` with ONE fixed sentence (no such tool exists). A settings / rules
/ strategy request, or a registry tool marked `trading_logic: true` →
`unsupported` naming the owner's command ([R3F-11]; V5 builds the draft
tool). Anything else the Plan calls unsupported → "I can't do that yet."

THE ACT'S DRY RUN [F-09]. `stop_dry_run` computes the exact change (card,
from → to, card state) for the read-back WITHOUT writing, and the two
hashes the confirm must match: `target_sha256 = sha256(card id ‖
from_stop ‖ to_stop ‖ card state)` and `diff_sha256` of the change itself.
X-X5's guard: a parsed stop ≥ 10× or ≤ 0.1× the card's current stop
clarifies — the engine writes "four fifty" as `450`.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any, Optional

from .models import PendingAction, Plan
from .registry import KNOWN_TOOLS, AgentSpec

REFUSE_SENTENCE = ("I can't place, change or cancel orders or touch a trading platform — "
                   "that stays with you.")
LOGIC_SENTENCE = ("That changes your trading rules, and voice can't do that yet. The owner's command is: "
                  "cobalt settings load --card <file> --sha256 <hash> --apply")
UNSUPPORTED_SENTENCE = "I can't do that yet."

#: X-X5: a parsed stop this far from the card's current stop clarifies.
STOP_RATIO_GUARD = Decimal(10)

_ORDER = re.compile(
    r"\b(buy|buying|sell|selling|cover|covering|flatten|execute|at market|market order|limit order|"
    r"stop order|place (an? )?(\w+ )?order|(cancel|modify|change|send) (my |the |an? )?(\w+ )?orders?)\b",
    re.I)
_LOGIC = re.compile(
    r"\b(max(imum)? risk|risk budget|risk per trade|daily stop|settings?|rules?|strateg(y|ies)|"
    r"thresholds?|playbooks?)\b"
    r"|\b(enable|disable|turn (on|off))\b.*\b(grades?|filters?|rules?|setups?|settings?)\b",
    re.I)
_NUM = re.compile(r"\d+(?:\.\d+)?")


class ToolReadFailed(RuntimeError):
    """A read tool's store could not be read — named, never an empty answer."""


class Clarify(RuntimeError):
    """The act cannot be read back as asked; `str()` is the spoken question."""


@dataclass(frozen=True)
class Refusal:
    kind: str       # "refuse" | "unsupported"
    reply: str
    reason: str     # "order" | "refuse" | "trading_logic" | "unsupported"


def code_refusal(transcript: str, plan: Plan, agent: AgentSpec) -> Optional[Refusal]:
    if _ORDER.search(transcript):
        return Refusal("refuse", REFUSE_SENTENCE, "order")
    if plan.tool is not None and plan.tool in agent.tools and agent.tools[plan.tool].trading_logic:
        return Refusal("unsupported", LOGIC_SENTENCE, "trading_logic")
    if _LOGIC.search(transcript):
        return Refusal("unsupported", LOGIC_SENTENCE, "trading_logic")
    if plan.kind == "refuse":
        return Refusal("refuse", REFUSE_SENTENCE, "refuse")
    if plan.kind == "unsupported":
        return Refusal("unsupported", UNSUPPORTED_SENTENCE, "unsupported")
    return None


# --- numbers as text -------------------------------------------------------------


def fmt_price(value: Any) -> str:
    """4.4000 → '4.40'; 4.405 → '4.405'; at least two decimals."""
    s = f"{Decimal(str(value)):.4f}".rstrip("0")
    whole, _, frac = s.partition(".")
    return f"{whole}.{frac.ljust(2, '0')}"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def figures_ok(say: Optional[str], result_text: str) -> bool:
    if not say:
        return True
    allowed = set(_NUM.findall(result_text))
    return all(tok in allowed for tok in _NUM.findall(say))


def compose_reply(say: Optional[str], template: str) -> str:
    if say and say.strip() and figures_ok(say, template):
        return f"{say.strip()} {template}"
    return template


# --- read tools --------------------------------------------------------------------


def _card_phrase(c: dict) -> str:
    return f"{c['ticker']} {c['direction']}, {c['state']}, stop {fmt_price(c['stop'])}"


def render_open_cards(rows: list[dict]) -> str:
    if not rows:
        return "You have no open cards."
    noun = "card" if len(rows) == 1 else "cards"
    return f"You have {len(rows)} open {noun}: " + "; ".join(_card_phrase(c) for c in rows) + "."


def render_numbers(c: dict) -> str:
    shares = f"{c['shares']} shares" if c.get("shares") is not None else "unsized"
    return (f"{c['ticker']} {c['direction']}, card {c['id']}, {c['state']}: entry {fmt_price(c['entry'])}, "
            f"stop {fmt_price(c['stop'])}, {shares}, grade {c['grade']}.")


def render_pool(payload: dict) -> str:
    pool = payload["pool"]
    names = [r["ticker"] for r in sorted(pool.get("current") or [], key=lambda r: (r.get("position") is None, r.get("position") or 0))]
    if not names:
        return "The radar pool is empty."
    stale = " (STALE)" if pool.get("stale") else ""
    noun = "name" if len(names) == 1 else "names"
    shown = ", ".join(names[:10])
    more = f", and {len(names) - 10} more" if len(names) > 10 else ""
    return f"Radar pool{stale}: {len(names)} {noun} — {shown}{more}."


def read_open_cards() -> list[dict]:
    """The sheet's own read, through the same store class the sheet uses."""
    from cobalt.aset import web as aset_web

    try:
        return aset_web.CardStore().open_cards()
    except Exception as e:  # noqa: BLE001 - named, never an empty answer
        raise ToolReadFailed(f"open cards unreadable ({type(e).__name__})") from None


def read_pool() -> dict:
    """THE route's own function — the same read `/api/radar/pool` makes."""
    from fastapi.responses import JSONResponse

    from cobalt.aset import web as aset_web

    out = aset_web.api_radar_pool(since=None)
    if isinstance(out, JSONResponse):
        try:
            err = json.loads(out.body).get("error", "unknown")
        except ValueError:
            err = "unknown"
        raise ToolReadFailed(f"the radar could not be read: {err}")
    return out


READ_TOOLS = {"cards.open", "radar.pool", "cards.numbers"}
ACT_TOOLS = {"cards.set_stop"}
assert READ_TOOLS | ACT_TOOLS == KNOWN_TOOLS, "voice tools and registry.KNOWN_TOOLS disagree"


# --- the act ---------------------------------------------------------------------------


def stop_dry_run(card: dict, to_stop: Decimal, *, ttl_s: float, now: datetime) -> PendingAction:
    """The exact change, computed, never written."""
    from_s, to_s = fmt_price(card["stop"]), fmt_price(to_stop)
    if Decimal(from_s) == Decimal(to_s):
        raise Clarify(f"The stop on {card['ticker']} is already {from_s}. What should it be?")
    cur = Decimal(str(card["stop"]))
    if cur > 0:
        ratio = Decimal(to_s) / cur
        if ratio >= STOP_RATIO_GUARD or ratio <= 1 / STOP_RATIO_GUARD:
            raise Clarify(
                f"I heard {to_s} for {card['ticker']}, whose stop is {from_s}. "
                "Say the price with 'point' — like four point five zero.")
    state = str(card["state"])
    return PendingAction(
        tool="cards.set_stop", card_id=int(card["id"]), ticker=str(card["ticker"]), card_state=state,
        from_stop=from_s, to_stop=to_s,
        readback=f"Stop on {card['ticker']} {card['direction']}, card {card['id']}: from {from_s} to {to_s}. "
                 "Say yes, or tap Confirm.",
        diff_sha256=sha256_text(f"cards.set_stop|{card['id']}|stop|{from_s}->{to_s}"),
        target_sha256=sha256_text(f"{card['id']}|{from_s}|{to_s}|{state}"),
        expires_at=now + timedelta(seconds=ttl_s),
    )


class TargetChanged(RuntimeError):
    """The card moved between the read-back and the confirm ([F-09]):
    REFUSED; `new` is the fresh before → after to read aloud and re-confirm."""

    def __init__(self, new: PendingAction):
        self.new = new
        super().__init__(f"the card changed — {new.readback}")


def execute_stop(pending: PendingAction, *, now: datetime | None = None, ttl_s: float = 60):
    """After HIS confirmation only. Re-read the card, RE-COMPUTE the dry run
    and require the same `diff_sha256` AND `target_sha256`; then the ONE
    card-stop function (`set_card_stop` → `CardStore.record_stop_edit`, the
    expert — L40). Returns the expert's `StopEdit` (its row id is the
    turn's write reference)."""
    from datetime import timezone

    from cobalt.aset.card_stop import set_card_stop
    from cobalt.cards import CardStateError

    current = next((c for c in read_open_cards() if c["id"] == pending.card_id), None)
    if current is None:
        raise CardStateError(f"card {pending.card_id} is not open — its stop is settled.")
    fresh = stop_dry_run(current, Decimal(pending.to_stop), ttl_s=ttl_s,
                         now=now or datetime.now(timezone.utc))
    if fresh.diff_sha256 != pending.diff_sha256 or fresh.target_sha256 != pending.target_sha256:
        raise TargetChanged(fresh)
    return set_card_stop(pending.card_id, pending.to_stop)


__all__ = [
    "ACT_TOOLS", "Clarify", "TargetChanged", "execute_stop", "LOGIC_SENTENCE", "READ_TOOLS", "REFUSE_SENTENCE", "Refusal",
    "STOP_RATIO_GUARD", "ToolReadFailed", "UNSUPPORTED_SENTENCE", "code_refusal", "compose_reply",
    "figures_ok", "fmt_price", "read_open_cards", "read_pool", "render_numbers", "render_open_cards",
    "render_pool", "sha256_text", "stop_dry_run",
]
