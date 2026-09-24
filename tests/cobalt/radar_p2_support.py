"""Shared test support for the S2-P2 S5 evaluate tests (not a test module).

REAL SHAPE, NOT INVENTED (L45). Bars, daily bars and trader settings come
from the hub-cut fixtures under `tests/fixtures/radar/`, read as they are.
The trade_def is the ONE synthetic anatomy-only def the repo ships
(`configs/cobalt/taxonomy/examples/example_trade_def.md`), with its
preconditions/avoids/trigger/stop swapped for the Extension-reversal
anatomy the S2 detectors serve — anatomy vocabulary only, no trade name,
no user data (L31/L32). The live strategy note is never copied here; the
`requires_vault` test reads it from its live path.

The fake stores hold rows in memory with the two properties the real
stores guarantee and the tests lean on: one OPEN radar card per
(member, def slug, direction) — a second insert is a conflict, not a
second card — and receipts that cannot be edited.
"""

from __future__ import annotations

import csv
import json
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from cobalt.archiver.models import Bar, Interval
from cobalt.cards.models import TERMINAL, CardState
from cobalt.radar.anatomy.daily import DailyBar, DailySeries
from cobalt.radar.evaluate import LoadedDef, OpenRadarCard
from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH, load_defaults, load_tunables
from cobalt.taxonomy.trade_def import TradeDef

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"
TRADE_DATE = date(2026, 1, 6)
FORMED_AT = datetime(2026, 1, 6, 16, 40, tzinfo=timezone.utc)  # 11:40 ET, path A per the fixture


def fixture_bars(ticker: str, filename: str = "bars-rubberband.real-shape.json") -> list[Bar]:
    rows = json.loads((FIXTURES / filename).read_text())
    return [
        Bar(ticker=r["ticker"], interval=Interval(r["interval"]), ts=datetime.fromisoformat(r["ts"]),
            open=Decimal(r["open"]), high=Decimal(r["high"]), low=Decimal(r["low"]),
            close=Decimal(r["close"]), volume=int(r["volume"]))
        for r in rows if r["ticker"] == ticker
    ]


def fixture_daily(ticker: str, fetched_at: datetime | None = None,
                  filename: str = "daily-bars.real-shape.csv") -> DailySeries:
    with (FIXTURES / filename).open() as f:
        rows = [r for r in csv.DictReader(f) if r["Ticker"] == ticker]
    return DailySeries(
        ticker=ticker,
        bars=tuple(
            DailyBar(session_date=date.fromisoformat(r["Date"]), open=Decimal(r["Open"]), high=Decimal(r["High"]),
                     low=Decimal(r["Low"]), close=Decimal(r["Close"]), volume=int(r["Volume"]))
            for r in rows
        ),
        fetched_at=fetched_at, source="cache-hit",
    )


def fixture_settings_rows(**card: Any) -> dict[str, Any]:
    rows = {row["key"]: row["value"] for row in json.loads((FIXTURES / "card-settings.real-shape.json").read_text())}
    rows.update(card)
    return rows


ANATOMY_FACTORS = [
    {"name": "atrs_from_open", "source": "cobalt", "tier": "deterministic"},
    {"name": "rvol", "source": "cobalt", "tier": "deterministic"},
    {"name": "Extension.leg_count", "source": "cobalt", "tier": "deterministic"},
    {"name": "htf_level_proximity", "source": "cobalt", "tier": "deterministic"},
    {"name": "trail_fit", "source": "cobalt", "tier": "deterministic"},
    "tape_absorption_at_bound",
    "setup_relation",
    "market_alignment",
    "sector_alignment",
]


def anatomy_def(**overrides: Any) -> TradeDef:
    text = EXAMPLE_NOTE_PATH.read_text()
    mapping = yaml.safe_load(text.split("```yaml\n", 1)[1].split("\n```", 1)[0])["trade_def"]
    mapping.update(
        valid_setups=[{"setup_ref": "overextension", "relation": "countertrend"}],
        tf_ceiling=15,
        entry_mode="backside",
        preconditions=[{"expr": "Extension.state == culminating"}],
        avoid=[{"expr": "NOT Extension.instantiated"}, {"text": "human-only context read"}],
        trigger={"type": "bar_break", "params": {"bars_cleared": 2, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=ANATOMY_FACTORS,
        preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: 09:45-15:30",
    )
    mapping["stop"]["placement"]["ref"] = "snapback_candle"
    mapping.update(overrides)
    return TradeDef.from_unit(mapping, slug="example-anatomy-reversal", name="Example Anatomy Reversal")


def loaded(td: TradeDef | None = None, md5: str = "0123456789abcdef0123456789abcdef") -> LoadedDef:
    return LoadedDef(slug=(td or anatomy_def()).id, md5=md5, definition=td or anatomy_def())


def engine_tunables() -> dict:
    return load_tunables().by_key


def defaults():
    return load_defaults()


# ---------------------------------------------------------------------
# In-memory stores
# ---------------------------------------------------------------------


class Gate:
    def __init__(self):
        self.labels: list[str] = []
        self.drop_at: str | None = None

    def __call__(self, label: str):
        def check():
            self.labels.append(label)
            if self.drop_at == label:
                from cobalt.radar.runner import StageDropped

                raise StageDropped(f"dropped at {label}")
        return check


class FakeRadarStore:
    """SYSTEM side: membership, bars, runs and seam rows."""

    def __init__(self, members: list[dict], bars: dict[str, list[Bar]]):
        self.members = members
        self.bars = bars
        self.runs: dict[int, dict] = {}
        self.scores: dict[int, dict] = {}
        self.writes: list[str] = []
        self.fail_on: str | None = None

    def admitted_members(self, pool_key):
        return [m for m in self.members if m.get("entered_at") and not m.get("left_at")]

    def memberships(self, ids):
        return [m for m in self.members if m["id"] in set(ids)]

    def i1_bars(self, ticker, start, end):
        return [b for b in self.bars.get(ticker, []) if start <= b.ts < end]

    def latest_run_id(self, pool_key):
        ids = [i for i, r in self.runs.items() if r["pool_key"] == pool_key]
        return max(ids) if ids else None

    def abandon_running_runs(self, pool_key, *, now, before_commit):
        before_commit()
        abandoned = [i for i, r in self.runs.items() if r["pool_key"] == pool_key and r["status"] == "running"]
        for i in abandoned:
            self.runs[i].update(status="failed", finished_at=now,
                                failed_detail="abandoned: the run never published (crash or market_reset)")
        return abandoned

    def open_score_run(self, row, *, before_commit):
        before_commit()
        run_id = len(self.runs) + 1
        self.runs[run_id] = {**row, "id": run_id, "status": "running", "finished_at": None}
        self.writes.append("run")
        return run_id

    def put_scores(self, run_id, rows, *, before_commit):
        if self.fail_on == "scores":
            raise RuntimeError("synthetic seam failure")
        before_commit()
        out = {}
        for row in rows:
            score_id = len(self.scores) + 1
            self.scores[score_id] = {**row, "id": score_id, "run_id": run_id,
                                     "proximity": None, "conviction": None, "card_score": None,
                                     "suppressed_reason": None}
            out[(row["membership_id"], row["trade_def_md5"])] = score_id
        self.writes.append("scores")
        return out

    def copy_card_values(self, copies, *, before_commit):
        before_commit()
        for copy in copies:
            self.scores[copy["score_id"]].update(
                proximity=copy["proximity"], conviction=copy["conviction"],
                card_score=copy["card_score"], suppressed_reason=copy["suppressed_reason"],
            )
        self.writes.append("copy")

    def finish_run(self, run_id, *, status, finished_at, detail, before_commit):
        before_commit()
        self.runs[run_id].update(status=status, finished_at=finished_at, failed_detail=detail)
        self.writes.append(f"finish:{status}")

    def board(self, pool_key):
        complete = [r for r in self.runs.values() if r["pool_key"] == pool_key and r["status"] == "complete"]
        if not complete:
            return []
        latest = max(complete, key=lambda r: (r["started_at"], r["id"]))
        return [s for s in self.scores.values() if s["run_id"] == latest["id"]]


class FakeCardStore:
    """USER side: radar cards, dots, taps and receipts."""

    OPEN = {s.value for s in CardState if s not in TERMINAL}

    def __init__(self):
        self.cards: dict[int, dict] = {}
        self.receipts: list[dict] = []
        self.transitions: list[dict] = []
        self.taps: list[dict] = []
        self.fail_on: str | None = None

    def open_radar_cards(self):
        out = []
        for card in self.cards.values():
            if card["state"] not in self.OPEN:
                continue
            out.append(OpenRadarCard(
                card_id=card["id"], pool_member_id=card["pool_member_id"], ticker=card["ticker"],
                direction=card["direction"], state=card["state"], trade_def_slug=card["trade_def_slug"],
                trade_def_md5=card["trade_def_md5"], trigger_price=card["trigger_price"],
                structural_stop=card["structural_stop"], entry=card["entry"], stop=card["stop"],
                formed_at=card["formed_at"], expires_at=card["expires_at"], promoted_at=card.get("promoted_at"),
                health=card.get("health"), dots=card["dots"],
                taps=[{"id": t["id"], "factor": t["factor"], "grade": t["grade"]} for t in self.taps
                      if t["card_id"] == card["id"]],
            ))
        return out

    def formation_consumed(self, ticker, slug, direction, formed_at):
        return any(
            c["ticker"] == ticker and c["trade_def_slug"] == slug and c["direction"] == direction
            and c["formed_at"] == formed_at
            for c in self.cards.values()
        )

    def create_radar_card(self, spec, *, now, before_commit):
        if self.fail_on == "create":
            raise RuntimeError("synthetic account mode unresolved")
        for c in self.cards.values():
            if (c["state"] in self.OPEN and c["pool_member_id"] == spec.pool_member_id
                    and c["trade_def_slug"] == spec.trade_def_slug and c["direction"] == spec.direction):
                return None
        before_commit()
        card_id = len(self.cards) + 1
        self.cards[card_id] = {
            "id": card_id, "state": "WATCH", "origin": "radar", "entry": spec.entry, "stop": spec.stop,
            **spec.model_dump(exclude={"dots"}), "dots": list(spec.dots), "grade": None,
            "risk_budget": None, "shares": None, "used_risk": None, "health": None,
        }
        self.transitions.append({"card_id": card_id, "from": None, "to": "WATCH", "actor": "cobalt",
                                 "evidence": spec.evidence})
        return card_id

    def refresh_radar_card(self, update, *, now, before_commit):
        before_commit()
        card = self.cards[update.card_id]
        card.update(proximity=update.proximity, conviction=update.conviction, card_score=update.card_score,
                    score_suppressed=update.score_suppressed, proposed_key=update.proposed_key,
                    dots=list(update.dots), health=update.health, radar_score_id=update.radar_score_id)
        return True

    def expire_radar_card(self, card_id, expiry, *, run_id, now, before_commit):
        before_commit()
        card = self.cards[card_id]
        if card["state"] not in {"WATCH", "ARMED", "TRIGGERED"}:
            return False
        self.transitions.append({"card_id": card_id, "from": card["state"], "to": "EXPIRED", "actor": "cobalt",
                                 "evidence": {**expiry.evidence, "run_id": run_id}})
        card["state"] = "EXPIRED"
        return True

    def write_receipt(self, row, *, before_commit):
        if self.fail_on == "receipt":
            raise RuntimeError("synthetic receipt failure")
        before_commit()
        receipt_id = len(self.receipts) + 1
        self.receipts.append(json.loads(json.dumps({**row, "id": receipt_id}, default=str)))
        return receipt_id

    def receipts_for_day(self, pool_key, trade_date):
        return [r for r in self.receipts
                if r["pool_key"] == pool_key and r["observations"]["trade_date"] == trade_date.isoformat()]

    def tap(self, card_id, factor, grade):
        tap_id = len(self.taps) + 1
        self.taps.append({"id": tap_id, "card_id": card_id, "factor": factor, "grade": grade})
        card = self.cards[card_id]
        card["dots"] = [d.model_copy(update={"trader_grade": grade}) if d.factor == factor else d
                        for d in card["dots"]]


def members(*tickers: str, entered=True, left=None) -> list[dict]:
    at = datetime(2026, 1, 6, 14, 35, tzinfo=timezone.utc)
    return [
        {"id": 100 + i, "ticker": t, "trade_date": TRADE_DATE, "entered_at": at if entered else None,
         "left_at": left, "last_rank": i + 1}
        for i, t in enumerate(tickers)
    ]


def scan_times(start: datetime, stop: datetime, interval: int = 100):
    t = start
    while t <= stop:
        yield t
        t += timedelta(seconds=interval)
