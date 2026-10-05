"""THE DRC RECONCILE — the export against Cobalt's legs (DRC D5; v2 §3 `:80`
steps 1–6, S-C1 / S-C2 `:96`, `[F-19]` `:117`, §6 `:140`; R67, R90).

    LegsGateway()                          the build's ONE door to `cards.legs`
    diff(trade, position, history)         per leg seq: the export vs the card's current legs (pure)
    writes_for(diff)                       the writes a diff asks for (pure)
    apply(work, *, legs, now)              those writes, through C2's writer only
    for_trade(...)                         one matched trade's stored keys
    unresolved(...)                        the day's open refusals (R90)

WHAT IT READS. The matched card's legs through `cards.legs.read_position` (the
current legs, THE running read, `realized_r`) and every `legs` row of the
card (his taps and held-count statements, listed as history, v2 `:140`).

WHAT IT WRITES. Nothing but through `cards.legs.record_correction` and
`cards.legs.record_exit`, each with `source = 'trading_log'` and
`source_import_id` = the trade's trading-log `drc_imports` row (S-C2; L3,
L40, L57). A correction per mismatched leg; a new exit leg per export exit
Cobalt never recorded, its time set by one correction (`## RECORDS` D5-b).
His rows stay — the table is append-only. `apply` runs on the event day's
build only (`build.build_date(check=True)`), never inside `plan_note`, never
for a carried trade or a re-paired date (D5-d).

THE GAPS, named, never written around: a card with no legs gets no entry leg
(the entry writer carries no import id — D5-a); a Cobalt leg with no export
execution has no writer that removes it (D5-c, an unresolved item).

A REFUSAL (R90). A `LegRefused` is never forced, never retried in another
shape and never fails the build: the card's writes stop there and the
refusal — card id, leg ids, the export rows, its text and `code` verbatim —
is stored as an unresolved item on the day's `build_day.derived`, rendered,
and carried to every later DRC until a later reconcile of that card
succeeds or a current `resolve` row names that trade (K3-7's RESOLVE).
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Optional

from cobalt.cards import legs as card_legs
from cobalt.cards.store import CardStateError
from cobalt.session.clock import ET

#: The trading-log source (`cards.legs.TRADING_LOG`, S-C1).
TRADING_LOG = card_legs.TRADING_LOG
#: `legs.price` is NUMERIC(14, 4): the export's price is compared and written at it.
PRICE_PLACES = Decimal("0.0001")

ENTRY_NOT_WRITTEN = "entry leg: not written — the entry writer carries no import id"  # D5-a
NO_WRITER = "no writer removes a leg"  # D5-c
NOT_WRITTEN_CARRIED = "adjustment not written — carried trade"  # D5-d
NOT_WRITTEN_REPAIRED = "adjustment not written — re-paired date"  # D5-d
NOT_WRITTEN_DRY = "adjustment not written — dry run (plan only)"
MATCHED = "legs match the export — nothing to adjust"
NO_READER = "legs: not read — the build has no legs reader"
NOTHING_MATCHED = "no trade matched a card — nothing to reconcile"


class LegsGateway:
    """The build's one door to `cards.legs` (L3, L40): its reads and C2's
    two writers, nothing else. A test hands the build its own door."""

    def position(self, card_id: int) -> card_legs.Position:
        return card_legs.read_position(card_id)

    def history(self, card_id: int) -> list[dict[str, Any]]:
        """Every `legs` row of the card, oldest first — a READ."""
        from cobalt import db, env

        conn = db.connect(env.resolve_db_name(), side=db.Side.USER)
        try:
            cur = conn.execute("SELECT * FROM legs WHERE card_id = %s ORDER BY id", (card_id,))
            return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]
        finally:
            conn.close()

    def record_correction(self, leg_id: int, **kw) -> card_legs.CorrectionResult:
        return card_legs.record_correction(leg_id, **kw)

    def record_exit(self, card_id: int, **kw) -> card_legs.ExitResult:
        return card_legs.record_exit(card_id, **kw)


# ---------------------------------------------------------------------
# small values
# ---------------------------------------------------------------------


def _dec(value: Any) -> Optional[Decimal]:
    if value is None or value == "":
        return None
    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None


def _price(value: Any) -> Optional[str]:
    d = _dec(value)
    return None if d is None else str(d.quantize(PRICE_PLACES))


def _when(value: Any) -> Optional[datetime]:
    if value is None or value == "":
        return None
    return value if isinstance(value, datetime) else datetime.fromisoformat(str(value))


def _et(value: Any) -> Optional[str]:
    """An instant as ET ISO text (the trading log's own zone) — what is stored."""
    at = _when(value)
    return None if at is None else at.astimezone(ET).isoformat()


# ---------------------------------------------------------------------
# D5-1 — THE DIFF (pure)
# ---------------------------------------------------------------------


def _export_rows(trade: dict) -> list[dict]:
    """The export's side by leg seq: seq 0 the entries together (shares, the
    average entry, the first entry's time); seq k the k-th exit execution.
    `held_after` = the position after that leg."""
    entries, exits = trade.get("entries") or [], trade.get("legs") or []
    rows: list[dict] = []
    held = 0
    if entries:
        held = sum(int(e["shares"]) for e in entries)
        rows.append({
            "seq": card_legs.ENTRY_SEQ, "kind": "entry", "shares": held, "price": _price(trade.get("avg_entry")),
            "time": trade.get("entry_time") or next((e.get("time") for e in entries if e.get("time")), None),
            "lines": [e.get("line") for e in entries], "held_after": held,
        })
    for seq, x in enumerate(exits, start=1):
        held -= int(x["shares"])
        rows.append({"seq": seq, "kind": "exit", "shares": int(x["shares"]), "price": _price(x.get("price")),
                     "time": x.get("time"), "lines": [x.get("line")], "held_after": held})
    return rows


def _cobalt_rows(position: Optional[card_legs.Position]) -> list[dict]:
    if position is None:
        return []
    held = position.running.base_shares
    rows = []
    for leg in sorted(position.legs, key=lambda l: l["seq"]):
        if leg["kind"] == "exit":
            held -= int(leg["shares"])
        rows.append({
            "seq": int(leg["seq"]), "kind": leg["kind"], "leg_id": int(leg["id"]), "shares": int(leg["shares"]),
            "price": _price(leg["price"]), "at": _et(leg["at"]), "flag": leg["flag"], "source": leg["source"],
            "held_after": held,
        })
    return rows


def _fields(exp: dict, cob: dict) -> list[str]:
    out = []
    if exp["shares"] != cob["shares"]:
        out.append("shares")
    if exp["price"] is not None and _dec(exp["price"]) != _dec(cob["price"]):
        out.append("price")
    exp_at, cob_at = _when(exp["time"]), _when(cob["at"])
    if exp_at is not None and exp_at.replace(microsecond=0) != cob_at.replace(microsecond=0):
        out.append("time")
    return out


def _history(rows: list[dict]) -> list[dict]:
    """His taps and held-count statements (every row not from the trading
    log), as history (v2 `:140`)."""
    return [
        {"leg_id": int(r["id"]), "seq": int(r["seq"]), "kind": r["kind"], "shares": int(r["shares"]),
         "price": _price(r["price"]), "at": _et(r["at"]), "source": r["source"], "flag": r["flag"],
         "held_stated": r.get("held_stated"), "corrects": r.get("corrects")}
        for r in rows if r["source"] != TRADING_LOG
    ]


def diff(trade: dict, position: Optional[card_legs.Position]) -> dict:
    """D5-1 (v2 `:80` steps 1–3): per leg seq, the export against the card's
    current legs — shares, price, time; export exits with no Cobalt leg;
    Cobalt legs with no export execution; the held count after each leg on
    both sides. Pure; JSON-safe."""
    exp = {r["seq"]: r for r in _export_rows(trade)}
    cob = {r["seq"]: r for r in _cobalt_rows(position)}
    rows = []
    for seq in sorted(set(exp) | set(cob)):
        d, c = exp.get(seq), cob.get(seq)
        if d is not None and c is not None:
            fields = _fields(d, c)
            state = "mismatch" if fields else "match"
        elif d is not None:
            fields, state = [], "entry_not_written" if d["kind"] == "entry" else "export_only"
        else:
            fields, state = [], "cobalt_only"
        rows.append({"seq": seq, "kind": (d or c)["kind"], "state": state, "fields": fields, "export": d,
                     "cobalt": c})
    return {
        "basis": None if position is None else position.running.basis,
        "running": None if position is None else position.running.shares,
        "export_held": int(trade.get("held_shares") or 0),
        "rows": rows,
    }


def differs(d: dict) -> bool:
    return any(r["state"] != "match" for r in d["rows"])


def writes_for(d: dict) -> list[dict]:
    """The writes a diff asks for, in seq order (S-C2): a correction of each
    mismatched leg (only its differing fields), a new exit per export exit
    Cobalt never recorded. No entry leg (D5-a); nothing for a Cobalt leg
    with no export execution (D5-c)."""
    out = []
    for r in d["rows"]:
        exp, cob = r["export"], r["cobalt"]
        if r["state"] == "mismatch":
            w: dict[str, Any] = {"op": "correction", "seq": r["seq"], "leg_id": cob["leg_id"]}
            if "shares" in r["fields"]:
                w["shares"] = exp["shares"]
            if "price" in r["fields"]:
                w["price"] = exp["price"]
            if "time" in r["fields"]:
                w["at"] = exp["time"]
            out.append(w)
        elif r["state"] == "export_only":
            out.append({"op": "exit", "seq": r["seq"], "shares": exp["shares"], "price": exp["price"],
                        "at": exp["time"]})
    return out


# ---------------------------------------------------------------------
# D5-2 — THE WRITES, through C2's writer only
# ---------------------------------------------------------------------


def _item(work: dict, code: str, refusal: str) -> dict:
    """One unresolved item (R90): card id, the leg ids read, the export rows,
    the refusal and its code verbatim."""
    return {
        "card_id": work["card_id"], "trade_id": work["trade_id"], "since": work["day"], "code": code,
        "refusal": refusal, "leg_ids": list(work["leg_ids"]),
        "export_rows": [r["export"] for r in work["diff"]["rows"] if r["export"] is not None],
    }


def apply(work: dict, *, legs, now: datetime) -> dict:
    """The event day's writes for ONE matched trade (`work` from `for_trade`):
    `writes_for` through `legs` (THE gateway — C2's writer), each with
    `source = 'trading_log'` and the trade's import id. The first
    `LegRefused` stops this card's writes and is returned as an unresolved
    item, never forced (R90). A Cobalt leg with no export execution is an
    unresolved item, no write tried (D5-c)."""
    written: list[int] = []
    items: list[dict] = []
    refused = None
    stamp = {"source": TRADING_LOG, "source_import_id": work["import_id"], "now": now}
    if work.get("read_refused") is not None:
        refused = work["read_refused"]
        items.append(_item(work, refused["code"], refused["text"]))
    for w in [] if refused else writes_for(work["diff"]):
        try:
            if w["op"] == "correction":
                kw: dict[str, Any] = {}
                if "shares" in w:
                    kw["shares"] = w["shares"]
                if "price" in w:
                    kw["price"], kw["price_source"] = Decimal(w["price"]), TRADING_LOG
                if "at" in w:
                    kw["at"] = _when(w["at"])
                written.append(legs.record_correction(w["leg_id"], **kw, flag="confirmed", **stamp).leg_id)
            else:
                running = legs.position(work["card_id"]).running.shares
                leg = legs.record_exit(
                    work["card_id"], preset="typed", shares=w["shares"], price=Decimal(w["price"]),
                    price_source=TRADING_LOG, price_asof=None, flag="confirmed", source=TRADING_LOG,
                    running_before=running, now=now, source_import_id=work["import_id"],
                )
                written.append(leg.leg_id)
                at = _when(w["at"])
                if at is not None and at != now:
                    # D5-b: `record_exit` stamps `now`; the export's time is set
                    # by one correction through the same writer.
                    written.append(legs.record_correction(leg.leg_id, at=at, **stamp).leg_id)
        except card_legs.LegRefused as e:
            refused = {"seq": w["seq"], "op": w["op"], "code": e.code, "text": str(e)}
            items.append(_item(work, e.code, str(e)))
            break
    for r in work["diff"]["rows"]:
        if r["state"] == "cobalt_only":
            c = r["cobalt"]
            items.append(_item(work, "no_writer", f"{NO_WRITER} — Cobalt leg #{c['leg_id']} (seq {r['seq']}) "
                                                  "has no DAS execution"))
    return {"card_id": work["card_id"], "trade_id": work["trade_id"], "before": work["diff"]["rows"],
            "written": written, "refused": refused, "items": items}


# ---------------------------------------------------------------------
# one matched trade: the stored keys (L57)
# ---------------------------------------------------------------------


def _status(d: dict, *, writes: Optional[str], applied: Optional[dict]) -> str:
    if applied is not None:
        if applied["written"]:
            ids = ", ".join(f"#{i}" for i in applied["written"])
            return f"adjusted to DAS: {len(applied['written'])} rows ({ids})"
        if applied["refused"] is not None:
            return f"nothing written — {applied['refused']['text']}"
        if applied["items"]:
            return f"nothing written — {NO_WRITER} (unresolved)"
        return MATCHED
    if not differs(d):
        return MATCHED
    return writes or NOT_WRITTEN_DRY


def for_trade(trade: dict, inputs: dict, card: Optional[dict], *, legs, check: bool,
              applied: Optional[dict], day: date) -> Optional[dict]:
    """One matched trade (`card` is D3's match): its stored `reconcile` key,
    its inputs, the `realized_r` position, and — on the event day's build of
    a trade with no `carried_from` — the work `apply` takes. `None` when no
    card matched."""
    if card is None:
        return None
    card_id = int(card["id"])
    import_id = inputs.get("trading_log_import_id")
    carried = bool(inputs.get("carried_from"))
    writes = NOT_WRITTEN_CARRIED if carried else (None if check else NOT_WRITTEN_REPAIRED)
    if legs is None:
        return {"card_id": card_id, "derived": {"card_id": card_id, "status": NO_READER, "before": [],
                                                 "history": [], "written": [], "refused": None},
                "inputs": {"import_id": import_id, "leg_ids": []}, "position": None, "work": None}
    position, read_refused = None, None
    try:
        position = legs.position(card_id)
        history = legs.history(card_id)
    except CardStateError as e:
        # `LegRefused` (a card holding no position) or the card row gone:
        # named, stored, never a failed build (R90, L1).
        read_refused = {"seq": None, "op": "read", "code": getattr(e, "code", "card_state"), "text": str(e)}
        history = []
    d = diff(trade, position)
    leg_ids = [r["cobalt"]["leg_id"] for r in d["rows"] if r["cobalt"] is not None]
    has_entry = any(r["kind"] == "entry" and r["cobalt"] is not None for r in d["rows"])
    derived = {
        "card_id": card_id,
        "basis": d["basis"],
        "entry_leg": None if has_entry or position is None else ENTRY_NOT_WRITTEN,
        "read_refused": None if read_refused is None else read_refused["text"],
        "before": d["rows"] if applied is None else applied["before"],
        "after": None if applied is None else d["rows"],
        "history": _history(history),
        "status": _status(d, writes=writes, applied=applied),
        "written": [] if applied is None else applied["written"],
        "refused": None if applied is None else applied["refused"],
        "running_after": None if applied is None else d["running"],
        "export_held": d["export_held"],
    }
    work = None
    if check and not carried:
        work = {"card_id": card_id, "trade_id": trade["trade_id"], "day": day.isoformat(), "import_id": import_id,
                "diff": d, "leg_ids": leg_ids, "read_refused": read_refused}
    read_before = [r["cobalt"]["leg_id"] for r in derived["before"] if r["cobalt"] is not None]
    return {
        "card_id": card_id, "derived": derived, "position": position, "work": work,
        "inputs": {"import_id": import_id, "leg_ids": read_before,
                   "leg_ids_after": None if applied is None else leg_ids,
                   "history_ids": [h["leg_id"] for h in derived["history"]],
                   "writes": check and not carried, "carried_from": inputs.get("carried_from")},
    }


def realized(card: Optional[dict], rec: Optional[dict], refused_cards: set[int]) -> tuple[dict, dict]:
    """D5-4 (`[F-19]`): `cards.legs.realized_r` over the current legs read
    after the reconcile — as `read_position` returns it (never restated, L3),
    stored with its function id and inputs; `not computed — <reason>` with no
    matched card, a card with no legs, or a refused reconcile."""
    fn = card_legs.REALIZED_R_ID

    def nc(reason: str, legs_read=()) -> tuple[dict, dict]:
        return ({"function_id": fn, "value": None, "provisional": False, "r_unit": None, "reason": reason},
                {"fn_version": fn, "card": None if card is None else card.get("id"), "legs": list(legs_read)})

    if card is None or rec is None:
        return nc("not computed — no matched card")
    if rec["derived"]["status"] == NO_READER:
        return nc("not computed — legs not read")
    position = rec["position"]
    snapshot = [] if position is None else [
        {"id": int(l["id"]), "seq": int(l["seq"]), "kind": l["kind"], "shares": int(l["shares"]),
         "price": _price(l["price"]), "stop_in_force": _price(l["stop_in_force"]), "flag": l["flag"]}
        for l in sorted(position.legs, key=lambda l: l["seq"])
    ]
    if int(card["id"]) in refused_cards:
        return nc(f"not computed — the reconcile was refused (card {card['id']})", snapshot)
    if position is None or not position.legs:
        return nc("not computed — the card has no legs", snapshot)
    r = position.realized
    return ({"function_id": r.function_id, "value": None if r.value is None else str(r.value),
             "provisional": r.provisional, "r_unit": None if r.r_unit is None else str(r.r_unit),
             "reason": r.reason},
            {"fn_version": fn, "card": {"id": int(card["id"]), "direction": str(position.card["direction"])},
             "legs": snapshot})


def realized_text(r: dict) -> str:
    if r["value"] is None:
        return r["reason"]
    value = Decimal(r["value"]).quantize(Decimal("0.01"))
    return f"{value}R ({r['function_id']}{', provisional' if r['provisional'] else ''})"


# ---------------------------------------------------------------------
# D5-3 — the day's unresolved items (R90)
# ---------------------------------------------------------------------


def _key(item: dict) -> tuple:
    return item["card_id"], item["trade_id"], item["code"], item["refusal"]


def reconciled_cards(applied: dict[str, dict]) -> set[int]:
    """The cards this build's reconcile SUCCEEDED for: applied with no
    refusal (D5-3: a refused reconcile resolves nothing)."""
    return {a["card_id"] for a in applied.values() if a["refused"] is None}


def unresolved(day: date, *, carried_in: list[dict], same_day: list[dict], applied: dict[str, dict],
               resolved_trades: set[str]) -> list[dict]:
    """The items open after this build: this build's (its writes' refusals
    and D5-c) first; then the ones the prior DRC carried in and the ones this
    day's earlier build stored — each dropped when this build's reconcile
    of its card SUCCEEDED (no refusal: a later reconcile replaces it) or a
    current `resolve` row of this day names its trade (this build's items
    too). One item per (card, trade, code, refusal); the earliest `since`
    kept."""
    reconciled = reconciled_cards(applied)
    out: list[dict] = [i for a in applied.values() for i in a["items"] if i["trade_id"] not in resolved_trades]
    for item in [*carried_in, *same_day]:
        if item["card_id"] in reconciled or item["trade_id"] in resolved_trades:
            continue
        key = _key(item)
        known = next((o for o in out if _key(o) == key), None)
        if known is None:
            out.append(dict(item))
        elif item["since"] < known["since"]:
            known["since"] = item["since"]
    return out


__all__ = [
    "ENTRY_NOT_WRITTEN", "LegsGateway", "MATCHED", "NOTHING_MATCHED", "NOT_WRITTEN_CARRIED", "NOT_WRITTEN_DRY",
    "NOT_WRITTEN_REPAIRED", "NO_READER", "NO_WRITER", "TRADING_LOG", "apply", "diff", "differs", "for_trade",
    "realized", "realized_text", "reconciled_cards", "unresolved", "writes_for",
]
