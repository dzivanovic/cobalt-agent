"""Deterministic, re-runnable cut of the S2-P3 panel fixtures (plan §3,
L45 real-shape rule) from production JSON reads saved under the hub's
scratch directory. Never reads the live DB itself, never invents a row.

Inputs (raw `cobalt db query --format json` output, paths given via env
so the raw prod JSON is never committed):
  RADAR_FIXTURE_RAW_POOL        radar_pool row (1)
  RADAR_FIXTURE_RAW_MEMBERSHIP  radar_membership rows for one trade_date
  RADAR_FIXTURE_RAW_POOL_BLOCK  trader_settings 'radar.pool' row (1)
  RADAR_FIXTURE_RAW_SIZING      one aset_sizings row (column-shape template only)

Outputs, written under this file's own directory:
  panel-pool.real-shape.json
  panel-pool-block.real-shape.json
  panel-cards.contract.json
"""

from __future__ import annotations

import json
import os
import re
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent

# The one trade_date the membership rows were queried for, and the fixed
# synthetic day everything is shifted to. Chosen to never match the
# `2026-09-1*` pattern the L45 leak scan checks for.
#
# [amended 09-15, Astra R2-2 fixup] The pool row's own `last_scan_at` and
# the membership rows' `trade_date` must be the SAME ET calendar day for
# the fixture to be internally consistent (an intraday snapshot: the pool
# is still scanning "today"). v1 queried membership for the day BEFORE the
# pool read (both real 2026-09-14), which no longer matched once the pool
# was re-read a day later; v2 re-queries both same-session so
# `radar_pool.members` (50) exactly equals the admitted+open membership
# count (entered_at IS NOT NULL AND left_at IS NULL) — verified before
# writing (see report §Fixtures v2).
REAL_ANCHOR_DATE = date(2026, 9, 15)
SYNTHETIC_ANCHOR_DATE = date(2026, 1, 5)
DELTA_DAYS = (SYNTHETIC_ANCHOR_DATE - REAL_ANCHOR_DATE).days
DELTA_MS = DELTA_DAYS * 86_400_000

_DATETIME_RE = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})([ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:\+00:00)?)$"
)
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_HEX12_SUFFIX_RE = re.compile(r"@[0-9a-f]{12}\b")

_SCAN_ID_KEYS = {"last_scan_id", "opened_scan_id", "closed_scan_id"}
_HASH_ZERO_KEYS = {"note_sha256", "block_sha256"}


def _shift_datetime_str(value: str) -> str:
    m = _DATETIME_RE.match(value)
    if not m:
        return value
    year, month, day, rest = m.groups()
    d = date(int(year), int(month), int(day)) + timedelta(days=DELTA_DAYS)
    return f"{d.isoformat()}{rest}"


def _shift_date_str(value: str) -> str:
    if not _DATE_RE.match(value):
        return value
    d = date.fromisoformat(value) + timedelta(days=DELTA_DAYS)
    return d.isoformat()


def _zero_hex_suffix(value: str) -> str:
    return _HEX12_SUFFIX_RE.sub("@" + "0" * 12, value)


def _transform_value(key: str | None, value):
    if isinstance(value, dict):
        return {k: _transform_value(k, v) for k, v in value.items()}
    if isinstance(value, list):
        return [_transform_value(key, v) for v in value]
    if isinstance(value, str):
        if key in _HASH_ZERO_KEYS:
            return "0" * len(value)
        shifted = _shift_datetime_str(value)
        if shifted != value:
            return _zero_hex_suffix(shifted)
        shifted = _shift_date_str(value)
        if shifted != value:
            return shifted
        return _zero_hex_suffix(value)
    if isinstance(value, int) and key in _SCAN_ID_KEYS:
        return value + DELTA_MS
    return value


def transform_row(row: dict) -> dict:
    return {k: _transform_value(k, v) for k, v in row.items()}


def _load(env_key: str) -> list[dict]:
    path = os.environ[env_key]
    with open(path) as f:
        return json.load(f)


def cut_pool_and_membership() -> None:
    pool_rows = _load("RADAR_FIXTURE_RAW_POOL")
    membership_rows = _load("RADAR_FIXTURE_RAW_MEMBERSHIP")
    assert len(pool_rows) == 1, "expected exactly one radar_pool row"

    membership = [transform_row(r) for r in membership_rows]

    # [amended 09-15 per Astra R1-1 follow-up, found in Sol's build
    # verification] A single partial trading day (today, still mid-RTH at
    # cut time) has too little churn to contain a real same-ticker
    # exclusion -> promotion -> departure -> re-entry sequence within one
    # day (only 1 ticker in 359 rows reaches 3 episodes; 0 qualify). A
    # second, real, already-COMPLETED trading day (RADAR_FIXTURE_RAW_
    # MEMBERSHIP_PRIOR, one calendar day before the primary anchor —
    # confirmed by the shared DELTA_DAYS shift, never a second synthetic
    # date picked independently) is merged in to give the real-shape
    # fixture that richness. Real membership `id`s are globally
    # auto-incrementing and confirmed disjoint between the two real reads
    # (no collision). This is additive only: `pool` and its ET
    # `last_scan_at`/`members` consistency (established after the Sol
    # ESCALATE-2 fixup) describe ONLY the primary day; the real
    # `RadarStore.members_for_day` filters by `trade_date` in SQL, so a
    # live invocation still sees only the primary day's rows — the extra
    # historical slice is additional real-shape texture for fixture-level
    # assertions (e.g. episode-identity), not something any pool-view
    # render depends on.
    prior_path = os.environ.get("RADAR_FIXTURE_RAW_MEMBERSHIP_PRIOR")
    if prior_path:
        with open(prior_path) as f:
            prior_rows = json.load(f)
        prior_ids = {r["id"] for r in prior_rows}
        primary_ids = {r["id"] for r in membership_rows}
        assert not (prior_ids & primary_ids), "prior-day and primary-day membership ids collide"
        # Drop any prior-day ticker that also appears in the primary day:
        # a fixture consumer that groups raw rows by ticker alone (no
        # trade_date filter — e.g. an episode-identity assertion) must
        # never see a group mixing a still-open primary-day episode with
        # completed prior-day ones; that reads as a same-day re-entry
        # pattern but isn't one. Keeping the two days' ticker sets
        # disjoint keeps every such group single-day-coherent.
        primary_tickers = {r["ticker"] for r in membership_rows}
        prior_rows = [r for r in prior_rows if r["ticker"] not in primary_tickers]
        # Primary day stays FIRST: `_small_snapshot()` (used by most
        # `_build()`-default tests) picks `admitted[0]`/`excluded[0]` from
        # this same array and pairs them with a pool_row whose
        # `last_scan_at` is hardcoded to the primary synthetic day — those
        # picked rows must carry the primary day's `trade_date`, or the
        # builder's own pool/day scope guard (radar_panel.py:467) rejects
        # them. The prior (richer) day is appended after.
        membership = membership + [transform_row(r) for r in prior_rows]

    out = {
        "pool": transform_row(pool_rows[0]),
        "membership": membership,
    }
    dest = HERE / "panel-pool.real-shape.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(out['membership'])} membership rows)")


def cut_pool_block() -> None:
    block_rows = _load("RADAR_FIXTURE_RAW_POOL_BLOCK")
    assert len(block_rows) == 1, "expected exactly one trader_settings row"
    out = [transform_row(r) for r in block_rows]
    dest = HERE / "panel-pool-block.real-shape.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest}")


# One synthetic card per state the plan (§3) requires. Built on the real
# aset_sizings column shape (from RADAR_FIXTURE_RAW_SIZING), never a
# literal copy of the real row's own trade — every ticker/price/id below
# is fabricated to exercise each state, per L45's companion ruling
# (fixture policy = real-shape, not verbatim).
_CONTRACT_STATES = [
    # (state, ticker, origin, entry, stop, last, owner_note)
    ("WATCH", "AMD", "radar", "180.00", "177.50", "179.40", None),
    ("ARMED", "MSFT", "radar", "420.00", "417.00", "419.10", None),
    ("TRIGGERED", "NVDA", "radar", "132.00", "129.80", "132.15", None),
    ("FILLED", "TSLA", "radar", "255.00", "251.00", "256.20", None),  # displays IN-TRADE
    ("CLOSED", "AAPL", "radar", "228.00", "225.50", "230.10", None),
    ("PASSED", "META", "radar", "512.00", "507.00", "508.00", None),
    ("EXPIRED", "GOOGL", "radar", "168.00", "165.50", "166.00", None),
    ("MISSED", "AMZN", "radar", "195.00", "192.00", "196.50", None),
    ("WATCH", "SMCI", "manual", "42.00", "40.50", "41.80", "N/A MANUAL"),  # manual stop, no radar owner
]

_BASE_SYNTHETIC_AT = f"{SYNTHETIC_ANCHOR_DATE.isoformat()}T14:30:00.000000+00:00"


def _target_1r_2r(entry: str, stop: str, direction: str) -> tuple[str, str]:
    e, s = float(entry), float(stop)
    distance = abs(e - s)
    sign = 1 if direction == "long" else -1
    r1 = e + sign * distance
    r2 = e + sign * 2 * distance
    return f"{r1:.4f}", f"{r2:.4f}"


# R2's four health classes (plan §R Rulings), cycled ok/warn/bad across the
# 9 cards so the fixture exercises every pill status at least once.
_HEALTH_CLASSES = [
    ("Participation", "RVOL vs entry"),
    ("Cost", "spread vs entry"),
    ("Graded dot", "dot delta"),
    ("Structural", "level/MA/market/sector"),
]
_HEALTH_STATUS_CYCLE = ["ok", "ok", "warn", "bad"]


def _health_for(idx: int) -> list[dict]:
    return [
        {
            "label": label,
            "status": _HEALTH_STATUS_CYCLE[(idx + i) % len(_HEALTH_STATUS_CYCLE)],
            "note": f"{note} — contract sample {idx}",
        }
        for i, (label, note) in enumerate(_HEALTH_CLASSES)
    ]


def _dots_for(idx: int) -> list[dict]:
    return [
        {"label": "Catalyst", "score": idx % 3, "grade": 3 + (idx % 8), "why": f"catalyst why {idx}"},
        {"label": "Spread", "score": (idx + 1) % 3, "grade": 4 + (idx % 7), "why": f"spread why {idx}"},
        {"label": "Level", "score": (idx + 2) % 3, "grade": 5 + (idx % 6), "why": f"level why {idx}"},
        # Judgment dot (L11 human-only variable): score is always null.
        {"label": "Tape", "score": None, "grade": 1 + (idx % 10), "why": f"tape why {idx}"},
    ]


def cut_cards_contract() -> None:
    sizing_rows = _load("RADAR_FIXTURE_RAW_SIZING")
    assert len(sizing_rows) == 1, "expected exactly one aset_sizings row (shape template)"
    template = transform_row(sizing_rows[0])
    template_keys = set(template.keys())

    cards = []
    for idx, (state, ticker, origin, entry, stop, last, owner_note) in enumerate(_CONTRACT_STATES, start=1):
        direction = "long" if idx % 2 else "short"
        target_1r, target_2r = _target_1r_2r(entry, stop, direction)
        setup = "gap-go" if direction == "long" else "gap-fade"
        trade = "orb-long" if direction == "long" else "orb-short"
        card = {k: None for k in template_keys}
        card.update(
            {
                "id": 9000 + idx,
                "created_at": _BASE_SYNTHETIC_AT,
                "ticker": ticker,
                "grade": "B",
                "direction": direction,
                "sheet_mode": "half",
                "entry": entry,
                "stop": stop,
                "last_price": last,
                "shares": 100,
                "state": state,
                "state_at": _BASE_SYNTHETIC_AT,
                "session": "rth",
                "origin": origin,
                "account_mode": "live",
                "user_id": 1,
                "pool_member_id": None,
                # Contract-only presentation fields (card-spec §6 + R1-4/R2-3
                # additions). No real artifact exists until S2-P2 wires the
                # card adapter — these are the `**presentation` kwargs
                # `CardView.from_contract` requires alongside the row.
                "card_score": 60 + idx,
                "conviction": round(0.5 + 0.03 * idx, 2),
                "proximity": round(0.6 + 0.02 * idx, 2),
                "pool_position": idx,
                "target_1r": target_1r,
                "target_2r": target_2r,
                "owner": owner_note or ("COBALT" if origin == "radar" else "YOU"),
                "degraded": idx == 1,  # one degraded case, per §4 Ladder row
                "setup": setup,
                "trade": trade,
                "why": f"{setup} → {trade}, contract sample {idx} (no numbers, per card-spec §3)",
                "dots": _dots_for(idx),
                "health": _health_for(idx),
                "trails": ["1-bar", "structure"] if state in ("TRIGGERED", "FILLED") else [],
                "default_trail": "1-bar" if state in ("TRIGGERED", "FILLED") else None,
                "trail_why": ["1-bar: fastest confirmed exit on this setup"] if state in ("TRIGGERED", "FILLED") else [],
                "attempt": 1,
                "attempt_max": 2,
                # R3: news/notes are labelled empty slots in P3 (no embed).
                "news": "",
                "notes": "",
                "_contract": "card-spec §6 — no real artifact until S2-P2; P2 replaces",
            }
        )
        cards.append(card)

    dest = HERE / "panel-cards.contract.json"
    dest.write_text(json.dumps(cards, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(cards)} cards, states: {[c['state'] for c in cards]})")


def main() -> None:
    cut_pool_and_membership()
    cut_pool_block()
    cut_cards_contract()


if __name__ == "__main__":
    main()
