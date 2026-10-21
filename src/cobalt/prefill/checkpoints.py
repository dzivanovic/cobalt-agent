"""F5 — the four market-context checkpoints (F5 FINAL F5-1, card 731).

    uv run cobalt checkpoint run --slot HHMM [--dry-run]

One command, one slot per run: the plist command and the manual trigger.
At 07:15 / 07:45 / 08:15 / 08:45 ET (Charter:50, `prefill.yaml`
`checkpoints.slots`) one run writes one unit, `checkpoint_HHMM`, into the
Cobalt section `market_context` directly under `### Market Context:`
(split A, R1055 + R1056; a note without the heading gets the section at
the end, the writer's `AT_END`). His text under the heading stays outside
the section, byte-identical.

THE ORDER OF ONE RUN ([F-12], §2.7, §2.9-§2.13), each step before the next:

1. the config (`CheckpointsConfig`, the route) — a bad block crashes here,
   before any fetch (L1, L10);
2. the calendar: a closed day writes nothing, exit 0 (`TradingCalendar`);
3. the slot window: from the slot's time to the next slot's (08:45 to
   09:00); outside it the run is REFUSED, writes nothing, exits 2 — the
   MISSED unit stands. `--dry-run` ignores the window ([F-16]);
4. the Finviz gate: ONE `check_scheduled_demand` with the radar's planned
   rpm and this run's 2 requests as `extra` ([F-14], [F-17]); a refusal or
   an unreadable plan sends no GET and is loud;
5. the fetch: indices through F4's `fetch_market_table` (unchanged), the
   eleven sectors through ONE Groups GET here. Each source fails alone,
   never blank ([F-03]);
6. the delta against the latest earlier slot's STORED figures (or the
   prior close at the day's first run), a pure function ([F-15]);
7. the row: `system.market_checkpoints`, upserted by (trade_date, slot),
   the base figures COPIED onto it ([F-04]);
8. F4's `ensure_daily_note` (never `create_if_absent` here);
9. a MISSED unit for every earlier slot of today with no row, and ONE DM
   naming the slots ([F-07]);
10. this slot's unit with the numbers and `narrative: pending`;
11. ONE model call on route `checkpoint.narrative` (no retry, no second
    lane, L25), its reply indexed phrases only ([F-08]);
12. the same unit with the narrative or its degraded line; the row's
    `vault_write_id`.

EXIT: 0 every Finviz source ok (the narrative ok or degraded); 1 a Finviz
source degraded (fetch error, the eleven-row rule, the gate) or the unit
write FAILED; 2 the slot window.

Code computes every figure; the model returns `{lines: [{phrase_id,
refs}]}` and the renderer prints only stored figure strings (L25, the
LLM-reads-validated-data rule).
"""

from __future__ import annotations

# `cobalt.cli` caps loguru at INFO before this import chain runs (it reaches
# aset.prefill, which transitively imports FinvizApiClient — prefill/cli.py's note).
import argparse
import asyncio
import csv
import hashlib
import io
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Callable, Optional

import httpx
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, StrictInt, ValidationError

from cobalt import db, env
from cobalt.aset.prefill import resolve_token, scrub
from cobalt.db import Side
from cobalt.jobs.entrypoint import as_job
from cobalt.modelaccess import ModelCallError, ModelMessage, ModelRequest, load_routes
from cobalt.modelaccess.client import call_sync
from cobalt.modelaccess.config import Route
from cobalt.notify.mattermost import send_dm
from cobalt.prefill.config import CheckpointsConfig, PrefillConfigError, load_checkpoints_config
from cobalt.prefill.daily import ensure_daily_note, format_stamp
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import fetch_market_table
from cobalt.radar.notes import DemandConsumer, DemandWindow, check_scheduled_demand
from cobalt.session import SessionClock
from cobalt.session.calendar import TradingCalendar, load_calendar
from cobalt.session.clock import ET
from cobalt.strike.measure import radar_planned_rpm
from cobalt.vaultwrite import VaultWriter, VaultWriteStore, WriteResult, after_pattern
from cobalt.vaultwrite.markers import find_section

WRITER = "prefill.checkpoint"
JOB_PREFIX = "com.cobalt.checkpoint-"
GATE_SUBJECT = "checkpoint"
#: Two requests a slot: one screener export (indices) + one Groups export.
GETS_PER_SLOT = 2
#: Charter:50 — "full view by 09:00": the last slot's window closes here.
FULL_VIEW_BY = "09:00"

SCREENER = "finviz-screener"
GROUPS = "finviz-groups"
OK = "ok"
DEMAND_CEILING = "demand ceiling"

GROUPS_URL = "https://elite.finviz.com/export/groups"
#: Finviz's eleven sector groups (DATA-SOURCE-MEMO:440-441). A body that is
#: not exactly these is a failed groups source, never a ranked partial list.
SECTORS: tuple[str, ...] = (
    "Basic Materials", "Communication Services", "Consumer Cyclical", "Consumer Defensive", "Energy",
    "Financial", "Healthcare", "Industrials", "Real Estate", "Technology", "Utilities",
)
_CHANGE, _REL_VOLUME, _PERF_WEEK = "Change", "Relative Volume", "Performance (Week)"

#: [F-08]: the only phrases a narrative line may be. Each prints its words
#: (no figure) and then the stored text of the delta lines it refers to.
PHRASES: dict[str, str] = {
    "prior_close": "vs prior close",
    "index_move": "indices moved",
    "leader": "leading",
    "laggard": "lagging",
    "rank_move": "rank moves",
}
UNSOURCED = "unsourced figure"
PENDING = "pending"

_SLOT_ARG = re.compile(r"^([01]\d|2[0-3])([0-5]\d)$")


class CheckpointError(RuntimeError):
    """A run that cannot start (a slot no config names) — crash, never guess."""


class CheckpointNotClean(RuntimeError):
    """Raised INSIDE `as_job`: the only way the job row records exit 1."""


class GroupsShapeError(PrefillFetchError):
    """The Groups body is not the eleven sectors with a Change each."""


class UnsourcedFigure(ValueError):
    """The model's reply could put a figure on the note no code computed."""


# ---------------------------------------------------------------------------
# Slots
# ---------------------------------------------------------------------------


def slot_hhmm(slot: str) -> str:
    """`0745` → `07:45`."""
    m = _SLOT_ARG.match(slot)
    if m is None:
        raise CheckpointError(f"slot {slot!r} is not HHMM")
    return f"{m.group(1)}:{m.group(2)}"


def slot_instant(day: date, hhmm: str) -> datetime:
    hh, mm = (int(x) for x in hhmm.split(":"))
    return datetime(day.year, day.month, day.day, hh, mm, tzinfo=ET)


def _window(cfg: CheckpointsConfig, hhmm: str) -> tuple[str, str]:
    i = cfg.slots.index(hhmm)
    return hhmm, (cfg.slots[i + 1] if i + 1 < len(cfg.slots) else FULL_VIEW_BY)


def window_refusal(cfg: CheckpointsConfig, hhmm: str, when: datetime) -> Optional[str]:
    """None inside the slot's window, else the REFUSED line ([F-16])."""
    et = SessionClock.to_et(when)
    opens, closes = _window(cfg, hhmm)
    if et < slot_instant(et.date(), opens):
        return f"REFUSED: slot {hhmm} window opens at {opens}"
    if et >= slot_instant(et.date(), closes):
        return f"REFUSED: slot {hhmm} window closed at {closes}"
    return None


def require_slot(cfg: CheckpointsConfig, slot: str) -> str:
    hhmm = slot_hhmm(slot)
    if hhmm not in cfg.slots:
        raise CheckpointError(f"slot {hhmm} is not one of the configured slots {cfg.slots} (prefill.yaml checkpoints)")
    return hhmm


# ---------------------------------------------------------------------------
# The numbers ([F-03])
# ---------------------------------------------------------------------------


def _decimal(raw: Optional[str], name: str, column: str) -> str:
    cleaned = (raw or "").strip().rstrip("%").strip()
    if not cleaned:
        raise GroupsShapeError(f"Finviz groups row {name!r} has no {column}")
    try:
        return str(Decimal(cleaned))
    except InvalidOperation as e:
        raise GroupsShapeError(f"Finviz groups row {name!r}: unparseable {column} {raw!r}") from e


def parse_groups(text: str) -> dict[str, dict[str, str]]:
    """The Groups `v=140` CSV → {sector: {change, rel_volume, perf_week}},
    figures as the Decimal strings Finviz gave. Exactly the eleven
    sectors, each with a Change, or `GroupsShapeError`."""
    rows = list(csv.DictReader(io.StringIO(text)))
    names = [(r.get("Name") or "").strip() for r in rows]
    if sorted(names) != sorted(SECTORS):
        missing = sorted(set(SECTORS) - set(names))
        extra = sorted(set(names) - set(SECTORS))
        raise GroupsShapeError(
            f"Finviz groups body is not the 11 sector rows: {len(names)} row(s), "
            f"missing {missing or 'none'}, unexpected {extra or 'none'}"
        )
    out: dict[str, dict[str, str]] = {}
    for name, row in zip(names, rows):
        out[name] = {
            "change": _decimal(row.get(_CHANGE), name, _CHANGE),
            # Stored, never a delta input ([F-03]).
            "rel_volume": (row.get(_REL_VOLUME) or "").strip(),
            "perf_week": (row.get(_PERF_WEEK) or "").strip().rstrip("%"),
        }
    return out


async def fetch_groups(groups, *, keep: Optional[Callable[[str], None]] = None) -> dict[str, dict[str, str]]:
    """ONE Groups GET (`g=sector&v=140`). The token and the scrub are
    aset.prefill's, as `prefill/market.py` uses them (one Finviz-auth path).
    `keep` gets the body as sent, before the parse: the probe's X6 only
    (f5-probe G1); the run path passes none."""
    token = await resolve_token()
    params = {"g": groups.g, "v": str(groups.v), "auth": token}
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(GROUPS_URL, params=params)
            response.raise_for_status()
    except Exception as e:
        raise PrefillFetchError(f"Finviz groups fetch failed: {scrub(str(e))}") from e
    if keep is not None:
        keep(response.text)
    return parse_groups(response.text)


def fetch_figures(cfg: CheckpointsConfig, *, keep: Optional[Callable[[str], None]] = None
                  ) -> tuple[dict, dict[str, str]]:
    """Both sources, each failing alone. Returns (figures, source_status).
    `keep` is passed on to `fetch_groups` (f5-probe G1)."""

    async def _both():
        groups = fetch_groups(cfg.groups) if keep is None else fetch_groups(cfg.groups, keep=keep)
        return await asyncio.gather(fetch_market_table(tuple(cfg.indices)), groups, return_exceptions=True)

    market, sectors = asyncio.run(_both())
    figures: dict[str, Any] = {"indices": None, "sectors": None}
    status = {SCREENER: OK, GROUPS: OK}
    if isinstance(market, BaseException):
        status[SCREENER] = scrub(str(market)) or type(market).__name__
    else:
        figures["indices"] = {r.ticker: {"price": str(r.price), "change_pct": str(r.change_pct)} for r in market}
    if isinstance(sectors, BaseException):
        status[GROUPS] = scrub(str(sectors)) or type(sectors).__name__
    else:
        figures["sectors"] = sectors
    return figures, status


# ---------------------------------------------------------------------------
# The delta ([F-15]) — a pure function over stored figures
# ---------------------------------------------------------------------------


def _signed(value: Decimal) -> str:
    return f"{value:+}"


def competition_rank(changes: dict[str, Decimal]) -> dict[str, int]:
    """1 + the number of names with a strictly higher Change: ties share
    the lower rank ("1224")."""
    return {n: 1 + sum(1 for v in changes.values() if v > c) for n, c in changes.items()}


def _changes(sectors: dict) -> dict[str, Decimal]:
    return {n: Decimal(f["change"]) for n, f in sectors.items()}


def _tied(changes: dict[str, Decimal], pick) -> tuple[list[str], Decimal]:
    edge = pick(changes.values())
    return sorted(n for n, c in changes.items() if c == edge), edge


def compute_delta(figures: dict, base: Optional[dict]) -> dict:
    """`figures` vs `base` (the latest earlier slot's stored figures; None =
    the day's first run, whose baseline is the prior close Finviz's change%
    already is). Returns {"lines": [{phrase, text}], "groups_failed"}; no
    crossing field ([F-15])."""
    lines: list[dict[str, str]] = []
    indices = figures.get("indices")
    base_indices = (base or {}).get("indices")
    if indices:
        for ticker, f in indices.items():
            if base is None:
                lines.append({"phrase": "prior_close",
                              "text": f"{ticker} {f['price']} ({_signed(Decimal(f['change_pct']))}% vs prior close)"})
            elif base_indices and ticker in base_indices:
                b = base_indices[ticker]
                diff = Decimal(f["price"]) - Decimal(b["price"])
                lines.append({"phrase": "index_move", "text": (
                    f"{ticker} {b['price']} → {f['price']} ({_signed(diff)}), "
                    f"change {_signed(Decimal(b['change_pct']))}% → {_signed(Decimal(f['change_pct']))}%")})

    groups_failed: Optional[str] = None
    sectors = figures.get("sectors")
    base_sectors = (base or {}).get("sectors")
    if sectors:
        if base_sectors is not None and set(base_sectors) != set(sectors):
            gone = sorted(set(base_sectors) - set(sectors))
            new = sorted(set(sectors) - set(base_sectors))
            groups_failed = f"sector names changed since the base: absent {gone or 'none'}, new {new or 'none'}"
        else:
            changes = _changes(sectors)
            ranks = competition_rank(changes)
            if base_sectors is not None:
                before = competition_rank(_changes(base_sectors))
                for name in sorted(changes, key=lambda n: (ranks[n], n)):
                    if ranks[name] != before[name]:
                        lines.append({"phrase": "rank_move", "text": f"{name} rank {before[name]} → {ranks[name]}"})
            leaders, top = _tied(changes, max)
            laggards, bottom = _tied(changes, min)
            lines.append({"phrase": "leader", "text": f"leader: {', '.join(leaders)} ({_signed(top)}%)"})
            lines.append({"phrase": "laggard", "text": f"laggard: {', '.join(laggards)} ({_signed(bottom)}%)"})
    return {"lines": lines, "groups_failed": groups_failed}


# ---------------------------------------------------------------------------
# The narrative ([F-08]; L25)
# ---------------------------------------------------------------------------


class _Line(BaseModel):
    model_config = ConfigDict(extra="forbid")

    phrase_id: str
    refs: list[StrictInt] = Field(min_length=1)


class _Reply(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lines: list[_Line] = Field(min_length=1)


@dataclass
class Narrative:
    status: str  # ok | degraded (<kind>)
    lines: list[str]
    input: list[dict]
    prompt_sha256: Optional[str]
    model_returned: Optional[str]


def _strings(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for k, v in value.items() for s in (*_strings(k), *_strings(v))]
    if isinstance(value, list):
        return [s for v in value for s in _strings(v)]
    return []


def validate_reply(content: str, entries: list[dict], max_lines: int) -> list[str]:
    """The reply → narrative lines of stored figure strings, or
    `UnsourcedFigure`: not JSON, not the schema, a digit in any string, a
    phrase outside PHRASES, a ref out of range or to a line of another
    phrase, more lines than `narrative_max_lines`."""
    try:
        data = json.loads(content)
    except ValueError as e:
        raise UnsourcedFigure(f"not JSON: {e}") from None
    digits = [s for s in _strings(data) if any(ch.isdigit() for ch in s)]
    if digits:
        raise UnsourcedFigure(f"a digit in a model string: {digits[:3]}")
    try:
        reply = _Reply.model_validate(data)
    except ValidationError as e:
        raise UnsourcedFigure(f"schema: {e.error_count()} error(s)") from None
    if len(reply.lines) > max_lines:
        raise UnsourcedFigure(f"{len(reply.lines)} lines, more than narrative_max_lines {max_lines}")
    out = []
    for line in reply.lines:
        if line.phrase_id not in PHRASES:
            raise UnsourcedFigure(f"phrase_id {line.phrase_id!r} is not a phrase")
        for ref in line.refs:
            if not 0 <= ref < len(entries):
                raise UnsourcedFigure(f"ref {ref} outside the {len(entries)}-line delta list")
            if entries[ref]["phrase"] != line.phrase_id:
                raise UnsourcedFigure(f"ref {ref} is a {entries[ref]['phrase']} line, not {line.phrase_id}")
        out.append(f"{PHRASES[line.phrase_id]}: " + "; ".join(entries[r]["text"] for r in line.refs))
    return out


def _response_schema(max_lines: int) -> dict:
    return {
        "type": "object", "additionalProperties": False, "required": ["lines"],
        "properties": {"lines": {"type": "array", "minItems": 1, "maxItems": max_lines, "items": {
            "type": "object", "additionalProperties": False, "required": ["phrase_id", "refs"],
            "properties": {"phrase_id": {"type": "string", "enum": list(PHRASES)},
                           "refs": {"type": "array", "minItems": 1, "items": {"type": "integer", "minimum": 0}}},
        }}},
    }


_SYSTEM = (
    "You pick which lines of a market checkpoint's change list matter most. Each line has a ref and a "
    "phrase. Reply with JSON only: {\"lines\": [{\"phrase_id\": <phrase>, \"refs\": [<ref>, ...]}]}, no more "
    "lines than the schema allows; every ref must be a line whose phrase equals phrase_id. Never write a "
    "number, a digit or a figure in words: the figures are printed from the list, not by you."
)


def narrate(cfg: CheckpointsConfig, entries: list[dict], *, request_id: str, config=None) -> Narrative:
    """ONE call on `cfg.route`; the input is the filtered delta list only.
    A model error kind or an unsourced reply degrades the narrative, never
    the numbers; no retry, no second lane (L25)."""
    payload = [{"ref": i, "phrase": e["phrase"], "text": e["text"]} for i, e in enumerate(entries)]
    messages = [
        ModelMessage(role="system", content=_SYSTEM),
        ModelMessage(role="user", content=json.dumps(payload, ensure_ascii=False)),
    ]
    sha = hashlib.sha256(json.dumps([m.model_dump() for m in messages], sort_keys=True).encode()).hexdigest()
    if not entries:
        return Narrative(status="degraded (empty delta)", lines=[], input=payload, prompt_sha256=sha,
                         model_returned=None)
    req = ModelRequest(route=cfg.route, caller=WRITER, request_id=request_id, messages=messages,
                       response_schema=_response_schema(cfg.narrative_max_lines))
    try:
        result = call_sync(req, config=config)
    except ModelCallError as e:
        return Narrative(status=f"degraded ({e.kind})", lines=[], input=payload, prompt_sha256=sha,
                         model_returned=None)
    try:
        lines = validate_reply(result.content, entries, cfg.narrative_max_lines)
    except UnsourcedFigure as e:
        logger.error("checkpoint {}: narrative dropped — {}", request_id, e)
        return Narrative(status=f"degraded ({UNSOURCED})", lines=[], input=payload, prompt_sha256=sha,
                         model_returned=result.model_returned)
    return Narrative(status=OK, lines=lines, input=payload, prompt_sha256=sha, model_returned=result.model_returned)


# ---------------------------------------------------------------------------
# The unit body ([F-13] need 3)
# ---------------------------------------------------------------------------


def _degraded(status: dict[str, str]) -> bool:
    return any(v != OK for v in status.values())


def render_body(at: datetime, figures: dict, status: dict[str, str], delta: dict, base_slot: Optional[str],
                narrative: Optional[Narrative] = None) -> str:
    """Line 1 `as of HH:MM ET cobalt|cobalt-degraded` from the SLOT's instant
    (F4's `format_stamp`; never `human`), the numbers, `Δ since HH:MM:` and
    the narrative. No markdown heading line: his DRC embeds the heading."""
    flag = "cobalt-degraded" if _degraded(status) or delta.get("groups_failed") else "cobalt"
    lines = [f"{format_stamp(at)} {flag}"]
    if status.get("gate", OK) != OK:
        lines.append(f"degraded: finviz — {DEMAND_CEILING}")
    else:
        if status[SCREENER] == OK:
            lines.append(" · ".join(f"{t} {f['price']} {_signed(Decimal(f['change_pct']))}%"
                                    for t, f in figures["indices"].items()))
        else:
            lines.append(f"degraded: {SCREENER} — {status[SCREENER]}")
        if status[GROUPS] == OK:
            changes = _changes(figures["sectors"])
            ranks = competition_rank(changes)
            lines.append("Sectors: " + " · ".join(f"{n} {_signed(changes[n])}%"
                                                  for n in sorted(changes, key=lambda n: (ranks[n], n))))
        else:
            lines.append(f"degraded: {GROUPS} — {status[GROUPS]}")
    if delta.get("groups_failed"):
        lines.append(f"degraded: {GROUPS} — {delta['groups_failed']}")
    lines.append(f"Δ since {base_slot}:" if base_slot else "Δ since prior close:")
    if delta["lines"]:
        lines.extend(f"- {e['text']}" for e in delta["lines"])
    else:
        lines.append("- none")
    if narrative is None:
        lines.append(f"narrative: {PENDING}")
    elif narrative.status == OK:
        lines.extend(["Narrative:", *(f"- {x}" for x in narrative.lines)])
    else:
        lines.append(f"narrative: {narrative.status}")
    return "\n".join(lines)


def missed_body(hhmm: str) -> str:
    return f"MISSED {hhmm} — no run recorded"


# ---------------------------------------------------------------------------
# The table ([F-04]) — system.market_checkpoints
# ---------------------------------------------------------------------------

_JSONB = frozenset({"figures", "source_status", "base_figures", "delta", "narrative_input", "narrative"})
_COLUMNS = frozenset({
    "figures", "source_status", "base_slot", "base_at", "base_figures", "delta", "narrative_input",
    "prompt_sha256", "narrative", "narrative_status", "model_returned", "write_status", "vault_write_id",
    "fetched_at",
})


class CheckpointStore:
    #: ADR-0008 D2: public market figures, no trader's data, no user_id.
    SIDE = Side.SYSTEM

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    @staticmethod
    def _values(fields: dict) -> tuple[list[str], list]:
        unknown = sorted(set(fields) - _COLUMNS)
        if unknown:
            raise ValueError(f"market_checkpoints has no column(s) {unknown}")
        from psycopg.types.json import Jsonb

        names = list(fields)
        return names, [Jsonb(fields[n]) if n in _JSONB and fields[n] is not None else fields[n] for n in names]

    def get(self, trade_date: date, slot: str) -> Optional[dict]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM market_checkpoints WHERE trade_date = %s AND slot = %s",
                               (trade_date, slot))
            row = cur.fetchone()
            return None if row is None else dict(zip([d.name for d in cur.description], row))

    def slots_on(self, trade_date: date) -> set[str]:
        with self._connect() as conn:
            rows = conn.execute("SELECT slot FROM market_checkpoints WHERE trade_date = %s", (trade_date,)).fetchall()
        return {r[0] for r in rows}

    def upsert(self, trade_date: date, slot: str, **fields) -> int:
        """One row per (trade_date, slot): a re-run updates it in place."""
        names, values = self._values(fields)
        cols = ", ".join(["trade_date", "slot", *names])
        marks = ", ".join(["%s"] * (2 + len(names)))
        sets = ", ".join([*(f"{n} = EXCLUDED.{n}" for n in names), "updated_at = now()"])
        with self._connect() as conn:
            row = conn.execute(
                f"INSERT INTO market_checkpoints ({cols}) VALUES ({marks}) "
                f"ON CONFLICT (trade_date, slot) DO UPDATE SET {sets} RETURNING id",
                (trade_date, slot, *values),
            ).fetchone()
        return int(row[0])

    def update(self, trade_date: date, slot: str, **fields) -> None:
        names, values = self._values(fields)
        sets = ", ".join([*(f"{n} = %s" for n in names), "updated_at = now()"])
        with self._connect() as conn:
            conn.execute(f"UPDATE market_checkpoints SET {sets} WHERE trade_date = %s AND slot = %s",
                         (*values, trade_date, slot))


def default_stores():
    """(market_checkpoints, vault_writes) — the CLI's; tests pass their own."""
    vault_store = VaultWriteStore()
    vault_store.ensure_schema()
    return CheckpointStore(), vault_store


# ---------------------------------------------------------------------------
# The Finviz gate ([F-14], [F-17]; L53)
# ---------------------------------------------------------------------------


def demand_consumer(hhmm: str) -> DemandConsumer:
    return DemandConsumer(name=GATE_SUBJECT, rpm=GETS_PER_SLOT, window=DemandWindow.from_at(hhmm, 60),
                          basis="1 screener + 1 groups request per slot")


def check_demand(hhmm: str) -> Optional[str]:
    """None = admitted. A refusal, an unreadable plan or a broken gate is a
    reason, and no GET is sent. `radar_rpm=None` (no planned rpm) makes the
    gate count the radar at the ceiling: a refusal, loud."""
    try:
        check_scheduled_demand(GATE_SUBJECT, radar_rpm=radar_planned_rpm(), extra=[demand_consumer(hhmm)])
    except Exception as e:  # noqa: BLE001 - an unreadable plan is a refusal, never a guess
        return f"{type(e).__name__}: {e}"
    return None


# ---------------------------------------------------------------------------
# One run
# ---------------------------------------------------------------------------


@dataclass
class CheckpointResult:
    slot: str
    day: date
    dry_run: bool
    path: Optional[Path] = None
    action: str = "written"  # closed | refused | written | failed | dry_run
    exit_code: int = 0
    degraded: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    writes: list[WriteResult] = field(default_factory=list)
    dm: Optional[Any] = None
    narrative_status: Optional[str] = None

    def summary(self) -> str:
        parts = [f"checkpoint {self.slot} {self.day}: {self.action}, exit {self.exit_code}"]
        parts += self.degraded + self.failures
        return " · ".join(parts)

    def report(self) -> str:
        lines = [self.summary(), *self.notes]
        if self.narrative_status:
            lines.append(f"narrative: {self.narrative_status}")
        if self.dm is not None:
            lines.append(self.dm.report())
        for w in self.writes:
            lines.append(w.report() if hasattr(w, "report") else str(w))
        return "\n".join(lines)


def _placement(cfg: CheckpointsConfig):
    hashes, _, title = cfg.heading.partition(" ")
    pattern = re.compile(rf"^{re.escape(hashes)}\s+{re.escape(title.strip())}\s*$")
    return after_pattern(pattern, f"after {cfg.heading!r}")


def _unit_id(hhmm: str) -> str:
    return f"checkpoint_{hhmm.replace(':', '')}"


def _unit_on_disk(path: Path, section: str, unit: str) -> Optional[str]:
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").split("\n")
    block = find_section(lines, section)
    if block is None or unit not in block.units:
        return None
    return "\n".join(block.units[unit].body(lines))


def _base(cfg: CheckpointsConfig, store, day: date, hhmm: str) -> Optional[dict]:
    """The latest earlier slot of today with stored figures."""
    for earlier in reversed(cfg.slots[: cfg.slots.index(hhmm)]):
        row = store.get(day, earlier)
        if row is not None and row.get("figures") is not None:
            return row
    return None


def run_checkpoint(
    slot: str,
    when: datetime,
    *,
    dry_run: bool = False,
    store=None,
    vault_store: Optional[VaultWriteStore] = None,
    calendar: Optional[TradingCalendar] = None,
) -> CheckpointResult:
    """One slot, in the module docstring's order. `store`, `vault_store` and
    `calendar` are test seams; production passes none of them."""
    cfg = load_checkpoints_config()
    routes = load_routes()
    if cfg.route not in routes.routes:
        raise PrefillConfigError(f"checkpoints.route {cfg.route!r} is not a route in configs/cobalt/modelaccess.yaml")
    # The registry also holds embeddings routes (card 469); the narrative needs a chat route.
    if not isinstance(routes.routes[cfg.route], Route):
        raise PrefillConfigError(
            f"checkpoints.route {cfg.route!r} is a {routes.routes[cfg.route].kind} route, not a chat route")
    hhmm = require_slot(cfg, slot)
    et = SessionClock.to_et(when)
    day = et.date()
    result = CheckpointResult(slot=hhmm, day=day, dry_run=dry_run)

    calendar = calendar or load_calendar()
    if not calendar.is_trading_day(day):
        logger.info("checkpoint {}: {} — nothing fetched, nothing written", hhmm, calendar.describe(day))
        result.action = "closed"
        result.notes.append(calendar.describe(day))
        return result

    refusal = window_refusal(cfg, hhmm, when)
    if refusal is not None:
        if not dry_run:
            result.action, result.exit_code = "refused", 2
            result.failures.append(refusal)
            return result
        result.notes.append(f"dry run: {refusal} (ignored)")

    if store is None or vault_store is None:
        default_checkpoints, default_writes = default_stores()
        store = store or default_checkpoints
        vault_store = vault_store or default_writes

    # The gate, then the fetch: a refusal sends no GET.
    gate = check_demand(hhmm)
    if gate is not None:
        logger.error("checkpoint {}: no Finviz request this run — {}", hhmm, gate)
        figures: dict = {"indices": None, "sectors": None}
        status = {"gate": DEMAND_CEILING, SCREENER: "not requested", GROUPS: "not requested"}
        result.degraded.append(f"degraded: finviz — {DEMAND_CEILING} ({gate})")
    else:
        figures, status = fetch_figures(cfg)
        result.degraded += [f"degraded: {s} — {status[s]}" for s in (SCREENER, GROUPS) if status[s] != OK]

    base_row = _base(cfg, store, day, hhmm)
    base_figures = None if base_row is None else json.loads(json.dumps(base_row["figures"], default=str))
    base_slot = None if base_row is None else base_row["slot"]
    delta = compute_delta(figures, base_figures)
    if delta["groups_failed"]:
        result.degraded.append(f"degraded: {GROUPS} — {delta['groups_failed']}")
    source_bad = bool(result.degraded)

    stamp_at = slot_instant(day, hhmm)
    previous = None if dry_run else store.get(day, hhmm)
    if not dry_run:
        store.upsert(
            day, hhmm, figures=figures, source_status=status, base_slot=base_slot,
            base_at=None if base_row is None else base_row.get("fetched_at"), base_figures=base_figures,
            delta=delta, narrative_input=None, prompt_sha256=None, narrative=None, narrative_status=PENDING,
            model_returned=None, write_status=PENDING, vault_write_id=None, fetched_at=when,
        )

    writer = VaultWriter(WRITER, store=vault_store, dry_run=dry_run)
    from cobalt.daymode.note import daily_note_path

    path = daily_note_path(day)
    result.path = path
    placement = _placement(cfg)
    unit = _unit_id(hhmm)
    write_ids: list[int] = []

    def _failed(error: BaseException) -> CheckpointResult:
        message = f"FAILED: checkpoint {hhmm} write — {type(error).__name__}: {error}"
        logger.error(message)
        result.action, result.exit_code = "failed", 1
        result.failures.append(message)
        if not dry_run:
            store.update(day, hhmm, write_status="FAILED")
            result.dm = send_dm(f"Cobalt {message} ({path.name})")
        return result

    try:
        ensured = ensure_daily_note(writer, when)
        result.writes.append(ensured)
        if dry_run and not path.exists():
            result.action = "dry_run"
            result.notes.append("dry run: the note does not exist yet — ensure_daily_note would create it; "
                                "nothing further computed")
            return result

        # MISSED: every earlier slot of today with no row ([F-07]).
        have = store.slots_on(day)
        missed = [s for s in cfg.slots[: cfg.slots.index(hhmm)] if s not in have]
        newly = []
        for s in missed:
            write = writer.upsert_unit(path, cfg.section, _unit_id(s), missed_body(s), placement=placement)
            result.writes.append(write)
            if write.action != "unchanged":
                newly.append(s)
        if newly and not dry_run:
            result.dm = send_dm(f"Cobalt checkpoint MISSED: {', '.join(newly)} ET — no run recorded today "
                                f"({path.name}); this run is {hhmm}")

        # The numbers on disk BEFORE the model call ([F-12]); a re-run whose
        # numbers are already there writes nothing here.
        pending = render_body(stamp_at, figures, status, delta, base_slot)
        numbers = pending.rsplit("\n", 1)[0]
        on_disk = _unit_on_disk(path, cfg.section, unit)
        if dry_run or on_disk is None or not on_disk.startswith(numbers + "\n"):
            write = writer.upsert_unit(path, cfg.section, unit, pending, placement=placement)
            result.writes.append(write)
            if write.write_id is not None:
                write_ids.append(write.write_id)
    except Exception as e:  # noqa: BLE001 - a refused write is FAILED, DM'd, exit 1 — never silent
        return _failed(e)

    narrative = narrate(cfg, delta["lines"], request_id=f"{day}-{hhmm.replace(':', '')}", config=routes)
    result.narrative_status = narrative.status
    final = render_body(stamp_at, figures, status, delta, base_slot, narrative)
    try:
        write = writer.upsert_unit(path, cfg.section, unit, final, placement=placement)
        result.writes.append(write)
        if write.write_id is not None:
            write_ids.append(write.write_id)
    except Exception as e:  # noqa: BLE001
        return _failed(e)

    if dry_run:
        result.action = "dry_run"
    else:
        kept = write_ids[-1] if write_ids else (previous or {}).get("vault_write_id")
        store.update(day, hhmm, narrative_input=narrative.input, prompt_sha256=narrative.prompt_sha256,
                     narrative={"lines": narrative.lines}, narrative_status=narrative.status,
                     model_returned=narrative.model_returned, write_status="written", vault_write_id=kept)
    if source_bad:
        result.exit_code = 1
    return result


# ---------------------------------------------------------------------------
# The command ([F-13] need 8)
# ---------------------------------------------------------------------------


def _slot_arg(raw: str) -> str:
    if not _SLOT_ARG.match(raw):
        raise argparse.ArgumentTypeError(f"slot {raw!r} is not HHMM (e.g. 0745)")
    return raw


def cmd_run(args: argparse.Namespace) -> None:
    from cobalt.session import clock as clock_mod

    cfg = load_checkpoints_config()  # a config error crashes before any fetch
    hhmm = require_slot(cfg, args.slot)
    now = clock_mod.now_utc()
    refusal = window_refusal(cfg, hhmm, now)
    if refusal is not None and not args.dry_run:
        # No job row: a refused late fire must not satisfy the watchdog's MISSED.
        print(refusal)
        sys.exit(2)
    with as_job(f"{JOB_PREFIX}{args.slot}", skip=args.dry_run) as job:
        store, vault_store = default_stores()  # read in a dry run too; the run writes nothing then
        result = run_checkpoint(args.slot, now, dry_run=args.dry_run, store=store, vault_store=vault_store)
        job.result = {"slot": result.slot, "action": result.action, "exit_code": result.exit_code,
                      "path": str(result.path) if result.path else None, "degraded": result.degraded,
                      "failures": result.failures, "narrative": result.narrative_status}
        report = result.report()
        logger.info(report)
        print(report)
        if result.exit_code == 1:
            raise CheckpointNotClean(result.summary())


def cmd_probe(args: argparse.Namespace) -> None:
    from cobalt.prefill.checkpoint_probe import main

    raise SystemExit(main(args.item, keep_groups=args.keep_groups))


PROBE_ITEMS = ("X4", "X5", "X6", "X7", "X10", "X13")


def add_parser(sub) -> None:
    checkpoint = sub.add_parser("checkpoint", help="The 07:15-08:45 market-context checkpoints (F5).")
    csub = checkpoint.add_subparsers(dest="command", required=True)
    run = csub.add_parser("run", help="Run one slot: fetch, delta, the unit, the narrative.")
    run.add_argument("--slot", required=True, type=_slot_arg, help="HHMM, one of prefill.yaml checkpoints.slots")
    run.add_argument("--dry-run", action="store_true",
                     help="Ignore the slot window; show the diff; write nothing (note, rows, DM).")
    run.set_defaults(func=cmd_run)
    probe = csub.add_parser("probe", help="Run one F5 first-gate item in dev (prints one "
                                          "PROBE <item> OK|FAIL|NOT RUN line; checkpoint_probe.py).")
    probe.add_argument("item", choices=PROBE_ITEMS)
    probe.add_argument("--keep-groups", metavar="PATH",
                       help="X6 only: keep the real Groups body (header and 11 rows) at PATH, a new file "
                            "under /Users/cobalt/cobalt-wt/.f5-probe/.")
    probe.set_defaults(func=cmd_probe)


__all__ = [
    "CheckpointError", "CheckpointNotClean", "CheckpointResult", "CheckpointStore", "GroupsShapeError",
    "PHRASES", "SECTORS", "add_parser", "check_demand", "compute_delta", "competition_rank", "demand_consumer",
    "fetch_figures", "fetch_groups", "narrate", "parse_groups", "render_body", "run_checkpoint",
    "validate_reply", "window_refusal",
]
