"""THE DRC BUILD — `run_drc_build(event)`, D2's ONE registered entry (DRC D3;
v2 §6, §8, `[F-17]` seam (5); v3 `[F-03]` note half; R93, R98, R99,
R101–R103, R114, R116, R117, 09-23 R17).

    run_drc_build(event, *, deps=None) -> Path     the note path (never empty)
    plan_note(day, *, deps, event, check)          compute + render, write nothing
    write_note(plan, *, deps)                      create-if-absent + every unit
    event_of(day, store)                           D2's event for a stored day

WHAT IT READS. The day's stored `drc_rows` as K1 / K2 recorded them through
D2's route (`DrcStore.rows_for` / `event_for`) — it pairs NOTHING: no
`build_day`, `pair_day` or `seed_for` here (`[F-17]` seam (5)). Beside them:
his template (`drc.template`), the day's cards (`AsetStore.for_date`, the
card snapshot `[F-19]`), D4's ONE readers (`load_drc_settings`,
`daily_risk_values`), the strategies folder's titles (`drc.playbooks`), the
daily note's four premarket keys (R102 O11) and the 21:10 replay row.

WHAT IT STORES (L57). Every number it computes — the card match, the
summary / PnL / risk figures, the playbook resolutions — goes into
`drc_rows` through ONE writer, `DrcStore.record_build`, as `build_trade`
(one per trade id) and `build_day` (`ref = 'build'`) rows with `inputs`,
`derived` and `fn_version` = `FN_VERSION`. The note renders ONLY what those
rows and K's rows hold (`drc.units`).

WHAT IT WRITES. The note at `load_prefill_paths()`'s path: `create_if_absent`
from his template (only the date token replaced), then ALWAYS every unit
upserted (never the old create-then-return, L1). His voice units
(`drc-trades/voice-<trade_id>`, `drc-day/voice-no-trades`) are created once
and never rewritten (R99, `upsert_unit(..., skip_if=…)`). A trade the
current rows no longer carry keeps its voice unit; its derived block
becomes ONE line, `orphaned — …`, directly above it (T6 / E8).

THE ORDER (the event's state is D2's; D3 writes none): the first check →
the rows recorded → the note written → for EACH date of the day row's
`derived.repaired`, in date order, the SAME build (v3 `[F-03]`: "Note
re-upserts run after the commit, in date order"). A note failure on a
re-paired date raises naming the note and the date, the later dates named
`not rebuilt: <dates>` — the database stays as K2 committed it.
"""

from __future__ import annotations

import functools
import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Callable, Optional

from cobalt.prefill.drc import (
    RULES_PLACEMENT,
    TRADES_PLACEMENT,
    format_card_reconcile_block,
    format_rules_check_block,
)
from cobalt.session.clock import ET
from cobalt.vault import resolve_vault_path
from cobalt.vaultwrite import VaultWriter
from cobalt.vaultwrite.markers import find_section, unit_open

from . import imports, template, units
from .models import Kind, Outcome, missing_of
from .playbooks import Strategies, read_strategies, resolve
from .stats_log import MATCH_INPUTS, PLAYBOOK, _DECIMALS as STATS_COLUMNS
from .store import DrcStore

#: The build's function id on every row it stores (L57).
FN_VERSION = "drc.build/1"
#: Its writer identity in `vault_writes`.
WRITER = "drc.build"
#: The daily-note keys the premarket block reads — nothing else (R102 O11).
PREMARKET_KEYS = ("Sleep", "Readiness", "RHR", "1% goal")
#: The regular session's open, the anchor of `windows.first_window_minutes`.
SESSION_OPEN = time(9, 30)


class BuildError(RuntimeError):
    """The build refuses (the first check), or a re-paired date's note
    failed — named, never `done` (L1)."""


# ---------------------------------------------------------------------
# what the build reads outside the DRC rows — one field each, so a test
# hands in constructed values and `default_deps` names the real readers
# ---------------------------------------------------------------------


@dataclass
class BuildDeps:
    store: Any
    vault_root: Path
    cards: Callable[[date], list[dict]]
    card_counts: Callable[[date], tuple[int, int]]
    drc_settings: Callable[[], Any]
    daily_stop: Callable[[], dict]
    risk_parameters: Callable[[list[dict]], str]
    rules_block: Callable[[], str]
    daily_note: Callable[[date], Optional[str]]
    replay_result: Callable[[], Optional[dict]]
    write_store: Any
    now: Optional[Callable[[], datetime]] = None


def default_vault_root() -> Path:
    """`cobalt.vault.resolve_vault_path()` — in dev the committed default is
    the DEV vault (`configs/dev/vault.yaml`)."""
    return resolve_vault_path()


def _cards(day: date) -> list[dict]:
    from cobalt.aset.store import AsetStore

    return AsetStore().for_date(day)


def _card_counts(day: date) -> tuple[int, int]:
    from cobalt.aset.store import AsetStore

    return AsetStore().counts_for_date(day)


def _drc_settings():
    from cobalt.settings.drc import load_drc_settings

    return load_drc_settings()


def _daily_stop() -> dict:
    from cobalt.settings.drc import daily_risk_values

    return dict(daily_risk_values().daily_stop)


def _daily_note(root: Path, day: date) -> Optional[str]:
    from cobalt.aset.config import load_config

    cfg = load_config().daily_note
    path = Path(root) / cfg.daily_notes_dir / day.strftime(cfg.filename_pattern)
    return path.read_text(encoding="utf-8") if path.is_file() else None


def _replay_result() -> Optional[dict]:
    from cobalt.jobs.store import JobStore
    from cobalt.radar.notes import REPLAY_LABEL

    row = JobStore().get(REPLAY_LABEL)
    return None if row is None else row.get("last_result")


def default_deps(vault_root: Optional[Path] = None, **over) -> BuildDeps:
    from cobalt.prefill.drc import risk_parameters_line, rules_checkbox_block
    from cobalt.vaultwrite.store import VaultWriteStore

    root = Path(vault_root) if vault_root is not None else default_vault_root()
    values: dict[str, Any] = dict(
        store=DrcStore(), vault_root=root, cards=_cards, card_counts=_card_counts,
        drc_settings=_drc_settings, daily_stop=_daily_stop, risk_parameters=risk_parameters_line,
        rules_block=rules_checkbox_block, daily_note=functools.partial(_daily_note, root),
        replay_result=_replay_result, write_store=VaultWriteStore(), now=None,
    )
    values.update(over)
    return BuildDeps(**values)


# ---------------------------------------------------------------------
# the plan: the rows and the units, computed and rendered, nothing written
# ---------------------------------------------------------------------


@dataclass
class UnitWrite:
    section: str
    unit: str
    body: str
    placement: Any = None
    create_once: bool = False


@dataclass
class BuildPlan:
    day: date
    note_path: Path
    note_text: str
    rows: list[dict]
    units: list[UnitWrite] = field(default_factory=list)
    miss_line: Optional[str] = None

    def report(self) -> str:
        out = [f"cobalt drc build {self.day} — DRY RUN: nothing written", f"note: {self.note_path}", ""]
        for u in self.units:
            out.append(f"{u.section}/{u.unit}{' (created once — his)' if u.create_once else ''}:")
            out.extend(f"    {line}" for line in (u.body.split("\n") if u.body else ["(blank)"]))
        if self.miss_line is not None:
            out += ["drc-misses/miss_line (from the stored 21:10 blob):", f"    {self.miss_line}"]
        out += ["", "drc_rows the build would record:"]
        out.extend(
            f"{r['kind']} {r['ref']}: fn_version={r['fn_version']} inputs={json.dumps(r['inputs'], sort_keys=True)} "
            f"derived={json.dumps(r['derived'], sort_keys=True)}"
            for r in self.rows
        )
        return "\n".join(out)


def _json(value: Any) -> Any:
    """A JSON-safe copy (Decimal / date / datetime as text) — what `drc_rows`
    stores, so the dry run prints exactly what would be recorded."""
    return json.loads(json.dumps(value, default=str))


def _dec(value: Any) -> Optional[Decimal]:
    if value is None or value == "":
        return None
    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None


def _at(iso: Optional[str]) -> Optional[datetime]:
    return None if not iso else datetime.fromisoformat(iso)


def _hhmm(text: str) -> time:
    hour, _, minute = str(text).partition(":")
    return time(int(hour), int(minute))


def event_of(day: date, store) -> "imports.DrcInputsPlaced":
    """D2's event for a stored day — D2's own builder (`imports._event`),
    never a second copy (L3)."""
    view = store.event_for(day)
    if view["event_id"] is None:
        raise BuildError(f"{day}: no DRC event for this date — D2's route fires it; nothing built")
    return imports._event(day, view, imports._orphans(view))


def _first_check(event, view: dict) -> None:
    """D3-2: the event is `trades` with both files `parsed` / `partial`,
    or `no_trade`; and the day's `day` row exists (recorded by D2's route).
    Anything else FAILS and writes nothing."""
    day = event.date
    if view["day"] is None:
        raise BuildError(f"{day}: no day row — D2's route records the day before the build; nothing written")
    current = {r["kind"]: r for r in view["imports"] if r["current"]}
    placed = (Outcome.PARSED.value, Outcome.PARTIAL.value)
    trading, stats = current.get(Kind.TRADING_LOG.value), current.get(Kind.STATS_LOG.value)
    if event.stated_book_id is not None:
        stored = view["day"]["inputs"].get("no_trade_id")
        if event.kind != "no_trade" or stored != event.stated_book_id:
            raise BuildError(
                f"{day}: the event names statement #{event.stated_book_id}, the day row's no_trade_id is "
                f"{stored} — nothing written"
            )
        return
    if trading is None or trading["id"] != event.import_id or trading["parse_status"] not in placed:
        raise BuildError(f"{day}: the event's trading log #{event.import_id} is not the day's current placed file")
    if event.kind == "trades" and (
        stats is None or stats["id"] != event.stats_import_id or stats["parse_status"] not in placed
    ):
        raise BuildError(f"{day}: a trades event needs the day's current placed stats log — nothing written")


def _premarket(text: Optional[str]) -> dict[str, Optional[str]]:
    out: dict[str, Optional[str]] = {}
    for key in PREMARKET_KEYS:
        m = re.search(rf"^{re.escape(key)}:[ \t]*(.*?)[ \t]*$", text or "", re.MULTILINE)
        out[key] = (m.group(1) or None) if m else None
    return out


def _windows(settings) -> list[tuple[str, time, time]]:
    w = settings.windows
    out: list[tuple[str, time, time]] = []
    if w.premarket_end:
        out.append(("premarket", time(0, 0), _hhmm(w.premarket_end)))
    if w.first_window_minutes:
        end = (datetime.combine(date(2000, 1, 3), SESSION_OPEN) + timedelta(minutes=w.first_window_minutes)).time()
        out.append(("first window", SESSION_OPEN, end))
    for name in ("prime", "dead", "second"):
        span = getattr(w, name)
        if span:
            out.append((name, _hhmm(span[0]), _hhmm(span[1])))
    return out


def _card_snapshot(card: dict) -> dict:
    """`[F-19]`: every card field a figure uses, at build time."""
    keys = ("id", "ticker", "grade", "direction", "sheet_mode", "entry", "stop", "shares", "risk_budget",
            "state", "status", "actual_fill", "recomputed_shares", "created_at", "distance_change_pct")
    return _json({k: card.get(k) for k in keys})


class _Stats:
    """What a trade's stats-fed values render as: the value, `not given`,
    or `not computed — missing: <columns>` when a PARTIAL file lacks the
    column (R17 (5)) — never 0, never blank."""

    def __init__(self, row: Optional[dict], missing: list[str], has_log: bool):
        self.row, self.missing, self.has_log = row, missing, has_log
        self.unmatched_by = [c for c in MATCH_INPUTS if c in missing]

    def text(self, field_name: str, *, as_money: bool = False) -> str:
        column = PLAYBOOK if field_name == "playbooks" else STATS_COLUMNS.get(field_name)
        if column is not None and column in self.missing:
            return f"not computed — missing: {column}"
        if self.row is None:
            if self.unmatched_by:
                return f"not computed — missing: {', '.join(self.unmatched_by)}"
            return units.NOT_GIVEN
        value = self.row.get(field_name)
        if value is None:
            return units.NOT_GIVEN
        return units.money(value) if as_money else str(value)

    def value(self, field_name: str) -> Optional[Decimal]:
        column = STATS_COLUMNS.get(field_name)
        if self.row is None or (column is not None and column in self.missing):
            return None
        return _dec(self.row.get(field_name))


def plan_note(day: date, *, deps: BuildDeps, event, check: bool = True) -> BuildPlan:
    """Everything the build would record and write for `day`, computed from
    the stored rows; nothing written."""
    root = Path(deps.vault_root)
    view = deps.store.event_for(day)
    if check:
        _first_check(event, view)
    elif view["day"] is None:
        raise BuildError(f"{day}: no day row — nothing to rebuild")
    note_path = template.note_path(root, day)
    note_text = template.render_template(template.read_template(root), day)
    stored = deps.store.rows_for(day)
    trade_rows = [r for r in stored if r["kind"] == "trade"]
    day_row = view["day"]
    derived_day = day_row["derived"]
    pairing_nc = (derived_day.get("not_computed") or {}).get("pairing")

    # the event's files: partial ones, names, screenshots (D2's event, L3)
    by_id = {r["id"]: r for r in view["imports"]}
    partial_lines = [
        f"PARTIAL — missing: {', '.join(cols)} · {by_id[int(i)]['kind']} file {by_id[int(i)]['name']}"
        for i, cols in sorted(event.partial.items(), key=lambda kv: int(kv[0]))
    ]
    stats_missing = list(event.partial.get(str(event.stats_import_id), [])) if event.stats_import_id else []
    shots = {r["trade_key"]: r["name"] for r in view["imports"] if r["id"] in set(event.screenshot_import_ids)}

    settings = deps.drc_settings()
    window = settings.limits.card_match_window_minutes
    windows = _windows(settings)
    cards = list(deps.cards(day))
    written, taken = deps.card_counts(day)
    strategies: Strategies = read_strategies(root)
    premarket = _premarket(deps.daily_note(day))
    stops = deps.daily_stop()

    # --- per trade -----------------------------------------------------
    trades = [r["derived"] for r in trade_rows]
    entry_at = {t["trade_id"]: _at(t.get("entry_time")) for t in trades}
    ordered = sorted(trades, key=lambda t: (entry_at[t["trade_id"]] is None, entry_at[t["trade_id"]] or datetime.min.replace(tzinfo=ET)))
    matched: dict[str, dict] = {}
    builds: list[dict] = []
    losses_run, last_loss_at = 0, None
    closed_sorted = sorted(
        (t for t in trades if t.get("exit_time")), key=lambda t: _at(t["exit_time"])
    )
    for seat, t in enumerate(ordered, start=1):
        tid = t["trade_id"]
        row = next(r for r in trade_rows if r["ref"] == tid)
        entry = entry_at[tid]
        stats = _Stats(t.get("stats"), stats_missing, event.stats_import_id is not None)
        # card match: nearest prior, same ticker + direction, within the window
        card = None
        if window is not None and entry is not None:
            candidates = [
                c for c in cards
                if str(c["ticker"]).upper() == t["symbol"].upper() and str(c["direction"]) == t["direction"]
                and c["created_at"] <= entry and entry - c["created_at"] <= timedelta(minutes=window)
            ]
            card = max(candidates, key=lambda c: (c["created_at"], c["id"])) if candidates else None
        if card is not None:
            matched[tid] = card
        after_fill = entry is not None and any(
            str(c["ticker"]).upper() == t["symbol"].upper() and str(c["direction"]) == t["direction"]
            and c["created_at"] > entry for c in cards
        )
        names = list((t.get("stats") or {}).get("playbooks") or [])
        resolutions = resolve(names, strategies)
        avg_entry = _dec(t.get("avg_entry"))
        planned = _dec(card["risk_budget"]) if card else None
        actual = (
            abs(avg_entry - _dec(card["stop"])) * t["shares"]
            if card is not None and avg_entry is not None and card.get("stop") is not None else None
        )
        overrun = ((actual - planned) / planned * 100).quantize(Decimal("0.1")) if actual is not None and planned else None
        prior_losses = [c for c in closed_sorted if entry is not None and _at(c["exit_time"]) <= entry]
        run = 0
        for c in reversed(prior_losses):
            g = _dec(c.get("gross_pnl"))
            if g is not None and g < 0:
                run += 1
            else:
                break
        last_loss = next((c for c in reversed(prior_losses) if (_dec(c.get("gross_pnl")) or 0) < 0), None)
        in_windows = [
            name for name, start, end in windows
            if entry is not None and start <= entry.astimezone(ET).time() < end
        ]
        derived = {
            "label": f"{t['symbol']} {t['direction']} {_clock_of(t.get('entry_time'))}",
            "card": None if card is None else {
                "card_id": card["id"],
                "lead_seconds": int((entry - card["created_at"]).total_seconds()),
            },
            "planned_risk": None if planned is None else str(planned),
            "actual_risk": None if actual is None else str(actual),
            "overrun_pct": None if overrun is None else str(overrun),
            "playbooks": [r.model_dump() for r in resolutions],
            "unmapped": sum(1 for r in resolutions if not r.mapped),
            "window": in_windows,
            "seat": seat,
            "losses_before": run,
            "minutes_since_loss": None if last_loss is None or entry is None
            else int((entry - _at(last_loss["exit_time"])).total_seconds() // 60),
            "flags": [f for f, on in (("card after fill", after_fill),
                                      ("risk overrun", overrun is not None and overrun > 0)) if on],
        }
        derived["risk_text"] = _risk_text(card, window, derived)
        derived["lines"] = _trade_lines(t, row["inputs"], derived, card, window, windows, stats, resolutions,
                                        shots.get(tid), day)
        builds.append(dict(
            kind="build_trade", ref=tid, fn_version=FN_VERSION,
            inputs=_json({
                "trade_row": {"day": day.isoformat(), "kind": "trade", "ref": tid},
                "card": None if card is None else _card_snapshot(card),
                "stats_row": t.get("stats"),
                "window_minutes": window,
                "window_bounds": [[n, s.isoformat(), e.isoformat()] for n, s, e in windows],
                "strategy_titles": strategies.listing() if strategies.readable else None,
                "screenshot": shots.get(tid),
            }),
            derived=_json(derived),
        ))

    # --- the day ------------------------------------------------------
    no_trade_day = event.kind == "no_trade"
    gross_values = [t.get("gross_pnl") for t in trades]
    literal = next((g for g in gross_values if isinstance(g, str) and g.startswith("not computed")), None)
    gross = sum((_dec(g) for g in gross_values if _dec(g) is not None), Decimal(0))
    nets = [_Stats(t.get("stats"), stats_missing, True) for t in trades]
    net_missing = next((s.text("net_pnl") for s in nets if s.value("net_pnl") is None), None)
    net = sum((s.value("net_pnl") for s in nets if s.value("net_pnl") is not None), Decimal(0))
    gross_text = literal if literal else units.money(gross)
    net_text = units.money(net) if net_missing is None else net_missing
    closed = [t for t in trades if t.get("status") == "closed" and _dec(t.get("gross_pnl")) is not None]
    wins = sum(1 for t in closed if _dec(t["gross_pnl"]) > 0)
    losses = sum(1 for t in closed if _dec(t["gross_pnl"]) < 0)
    bound = sum(1 for key in shots if key in {t["trade_id"] for t in trades})
    if pairing_nc:
        pnl_text = wl_text = tickers_text = pairing_nc
        tickers_text = f"trades: {pairing_nc}"
        shots_text = f"{pairing_nc} ({len(shots)} bound)"
    elif no_trade_day:
        pnl_text = "no trades — gross $0 · net $0"
        wl_text = "0/0 (0 closed) · trades: 0"
        tickers_text = "trades: 0 — a no-trade day"
        shots_text = "0 / 0"
    else:
        pnl_text = f"gross {gross_text} · net {net_text}"
        wl_text = f"{wins}/{losses} ({len(closed)} closed) · trades: {len(trades)}"
        tickers_text = f"trades: {len(trades)}"
        shots_text = f"{bound} / {len(trades)}"
    not_repaired: dict[str, list[str]] = {}
    for item in derived_day.get("not_repaired") or []:
        not_repaired.setdefault(item["reason"], []).append(item["day"])
    replay = deps.replay_result() or {}
    blob = replay.get("line_inputs") if replay.get("trade_date") == day.isoformat() else None
    if blob is not None and replay.get("line_action") == "pending (no DRC)":
        miss = "write"
    elif replay.get("trade_date") == day.isoformat() and replay.get("line_action") not in (None, "pending (no DRC)"):
        miss = "present"
    else:
        miss = "pending"
    matched_ids = {c["id"] for c in matched.values()}
    cards_without = [c for c in cards if c["id"] not in matched_ids]
    sheets = sorted({str(c.get("sheet_mode")) for c in matched.values() if c.get("sheet_mode")})
    day_derived = {
        "partial_lines": partial_lines,
        "pairing": pairing_nc,
        "not_repaired": [f"not re-paired: {', '.join(days)} — {reason}" for reason, days in not_repaired.items()],
        "miss_line": miss,
        "gross": None if literal or pairing_nc else str(gross),
        "net": None if net_missing or pairing_nc else str(net),
        "pnl_text": pnl_text,
        "wl_text": wl_text,
        "tickers_text": tickers_text,
        "screenshots_text": shots_text,
        "cards_written": written,
        "cards_taken": taken,
        "unmapped_playbooks": sum(b["derived"]["unmapped"] for b in builds),
        "strategies_readable": strategies.readable,
        "daily_stop_text": _daily_stop_text(stops, sheets, None if literal or pairing_nc else gross),
        "card_reconcile": format_card_reconcile_block(cards_without),
        "orphaned": [],
    }
    existing = note_path.read_text(encoding="utf-8") if note_path.is_file() else None
    current_ids = {t["trade_id"] for t in trades}
    if existing is not None:
        sec = find_section(existing.split("\n"), "drc-trades")
        for uid in (sec.units if sec else {}):
            if uid.startswith(units.VOICE_PREFIX) and uid[len(units.VOICE_PREFIX):] not in current_ids:
                day_derived["orphaned"].append(uid[len(units.VOICE_PREFIX):])
    day_build = dict(
        kind="build_day", ref="build", fn_version=FN_VERSION,
        inputs=_json({
            "day": day.isoformat(),
            "event": {"event_id": event.event_id, "import_id": event.import_id,
                      "stats_import_id": event.stats_import_id, "stated_book_id": event.stated_book_id,
                      "kind": event.kind, "partial": event.partial},
            "seed": view.get("seed"),
            "cards": [_card_snapshot(c) for c in cards],
            "card_counts": [written, taken],
            "window_minutes": window,
            "daily_stop": stops,
            "premarket": premarket,
            "strategy_titles": strategies.listing() if strategies.readable else None,
            "screenshots": shots,
            "replay": {k: replay.get(k) for k in ("replay_run_id", "trade_date", "line_action")},
        }),
        derived=_json(day_derived),
    )
    rows = [*builds, day_build]

    # --- the units, rendered from the rows ----------------------------
    plan = BuildPlan(day=day, note_path=note_path, note_text=note_text, rows=rows)
    add = plan.units.append
    add(UnitWrite(*units.SUMMARY, units.summary(day_build), units.date_line_placement(day.isoformat())))
    if no_trade_day and not pairing_nc:
        add(UnitWrite(*units.NO_TRADE, units.no_trade(day_build), units.DAY_PLACEMENT))
        add(UnitWrite(*units.VOICE_NO_TRADES, "", units.DAY_PLACEMENT, create_once=True))
    add(UnitWrite(*units.PREMARKET, units.premarket(day_build), units.DAY_PLACEMENT))
    add(UnitWrite(*units.PNL, units.pnl(day_build), units.PNL_PLACEMENT))
    add(UnitWrite(*units.FACTS, units.facts(day_build, builds), units.RISK_FACTS_PLACEMENT))
    add(UnitWrite(*units.RISK_PARAMETERS, f"Risk Parameters: {deps.risk_parameters(cards)}", units.PNL_PLACEMENT))
    add(UnitWrite(*units.TICKERS, units.tickers(day_build), TRADES_PLACEMENT))
    by_ref = {b["ref"]: b for b in builds}
    for t in ordered:
        add(UnitWrite(*units.trade_unit(t["trade_id"]), units.trade_block(t, by_ref[t["trade_id"]]), TRADES_PLACEMENT))
        add(UnitWrite(*units.voice_unit(t["trade_id"]), "", TRADES_PLACEMENT, create_once=True))
    for tid in day_derived["orphaned"]:
        add(UnitWrite(*units.trade_unit(tid), units.orphaned(tid), TRADES_PLACEMENT))
    add(UnitWrite(*units.RECONCILE, units.reconcile(day_build), TRADES_PLACEMENT))
    add(UnitWrite(*units.RULES_CHECK, format_rules_check_block({
        "rules_checkbox_block": deps.rules_block(),
        "card_reconcile_block": day_build["derived"]["card_reconcile"],
    }), RULES_PLACEMENT))
    if miss == "write":
        from cobalt.replay.line import render_stored

        plan.miss_line = render_stored(blob)
    return plan


def _clock_of(iso: Optional[str]) -> str:
    return "not given" if not iso else iso[11:19]


def _risk_text(card: Optional[dict], window: Optional[int], d: dict) -> str:
    if card is None:
        return "risk: not matched (window not given)" if window is None else "risk: no card"
    if d["actual_risk"] is None:
        return f"risk: planned {units.money(d['planned_risk'])} · actual not computed"
    text = f"risk: planned {units.money(d['planned_risk'])} · actual {units.money(d['actual_risk'])}"
    if d["overrun_pct"] is not None:
        text += f" · overrun {d['overrun_pct']}%" + (" (flag)" if Decimal(d["overrun_pct"]) > 0 else "")
    return text


def _daily_stop_text(stops: dict, sheets: list[str], gross: Optional[Decimal]) -> str:
    if all(v is None for v in stops.values()):
        return "not given"
    if len(sheets) != 1:
        return f"not computed — the day's sheet is not known ({len(sheets)} sheets on the matched cards)"
    stop = stops.get(sheets[0])
    if stop is None:
        return f"{sheets[0]}: not given"
    if gross is None:
        return f"{sheets[0]} {units.money(stop)} · distance not computed"
    return f"{sheets[0]} {units.money(stop)} · distance to the daily stop {units.money(_dec(stop) + gross)} (gross)"


def _trade_lines(t: dict, inputs: dict, d: dict, card: Optional[dict], window: Optional[int],
                 windows: list, stats: _Stats, resolutions: list, shot: Optional[str], day: date) -> list[str]:
    entries, exits = t.get("entries") or [], t.get("legs") or []
    lines = [
        f"entries: {len(entries)} · first {units._clock(t.get('entry_time'))} · avg entry "
        f"{units.given(t.get('avg_entry'))} · shares {t['shares']}",
    ]
    if t.get("status") == "closed":
        hold = t.get("hold_seconds")
        hold_text = units.NOT_GIVEN if hold is None else f"{hold // 60}m {hold % 60}s"
        lines.append(f"exits: {len(exits)} · last {units._clock(t.get('exit_time'))} · avg exit "
                     f"{units.given(t.get('avg_exit'))} · hold {hold_text}")
    else:
        lines.append(f"exits: {len(exits)} · open — held {t.get('held_shares')}")
    gross = t.get("gross_pnl")
    gross_text = gross if isinstance(gross, str) and gross.startswith("not computed") else units.money(gross)
    lines.append(f"P&L: gross {gross_text} · net {stats.text('net_pnl', as_money=True)} · "
                 f"commission {stats.text('commission', as_money=True)}")
    legs = [*entries, *exits]
    lines.append("legs: " + ("; ".join(
        f"{leg['kind']} {units._clock(leg.get('time'))} {leg['shares']}@{units.given(leg.get('price'))}"
        + (" (carried)" if leg.get("carried") else "")
        for leg in legs) or "none"))
    if card is None:
        lines.append("card: not matched (window not given)" if window is None else "card: none")
    else:
        lines.append(
            f"card: #{card['id']} {card['grade']} {card['direction']} · sheet {units.given(card.get('sheet_mode'))} · "
            f"entry {units.money(card['entry'])} · stop {units.money(card['stop'])} · shares {card['shares']} · "
            f"risk budget {units.money(card['risk_budget'])} · lead {d['card']['lead_seconds']}s"
        )
        lines.append(f"fill: card entry {units.money(card['entry'])} vs avg entry {units.given(t.get('avg_entry'))}")
    lines.append(d["risk_text"])
    lines.append(f"R: planned {stats.text('assumed_rr')} (stats log) · realized not computed (D5)")
    lines.append(
        f"target: {stats.text('target')} · MAE {stats.text('price_mae')} · MFE {stats.text('price_mfe')} · "
        f"best exit {stats.text('best_exit_price')}"
    )
    lines.append(f"stop: {stats.text('stop')}")
    if not windows:
        lines.append("window: not given")
    else:
        lines.append("window: " + (", ".join(d["window"]) or "outside the configured windows"))
    lines.append(f"seat: trade {d['seat']} of the day by entry time")
    since = d["minutes_since_loss"]
    lines.append(f"losses before: {d['losses_before']} in a row · since last loss: "
                 f"{'no loss before' if since is None else f'{since} min'}")
    lines.append("flags: " + (", ".join(d["flags"]) or "none"))
    carried = inputs.get("carried_from")
    if carried:
        lines.append(
            f"carried from: {carried['day']} ({carried['trade_id']})" if carried.get("day")
            else f"carried from: statement #{carried.get('stated_book_id')}"
        )
    playbook_missing = stats.text("playbooks")
    if playbook_missing.startswith("not computed"):
        lines.append(f"playbooks: {playbook_missing}")
    else:
        lines.append("playbooks: " + (", ".join(r.text for r in resolutions) or units.NOT_GIVEN))
    from cobalt.vault import DRC_IMPORTS_REL

    lines.append(f"chart: ![[{DRC_IMPORTS_REL}/{day.isoformat()}/{shot}]]" if shot else "chart: no screenshot bound")
    return lines


# ---------------------------------------------------------------------
# the write
# ---------------------------------------------------------------------


def _writer(name: str, deps: BuildDeps) -> VaultWriter:
    kw = {} if deps.now is None else {"now": deps.now}
    return VaultWriter(name, store=deps.write_store, **kw)


def write_note(plan: BuildPlan, *, deps: BuildDeps) -> Path:
    """`create_if_absent` from his template, then EVERY unit upserted (L1:
    never the create-then-return path); his voice units created once."""
    writer = _writer(WRITER, deps)
    writer.create_if_absent(plan.note_path, plan.note_text)
    for u in plan.units:
        skip = None
        if u.create_once:
            marker = unit_open(u.unit)
            skip = lambda text, marker=marker: marker in text.split("\n")  # noqa: E731
        writer.upsert_unit(plan.note_path, u.section, u.unit, u.body, placement=u.placement, skip_if=skip)
    if plan.miss_line is not None:
        from cobalt.replay.line import WRITER as LINE_WRITER
        from cobalt.replay.line import write_miss_line

        # One writer identity for the unit, whatever process writes it (v2 §8).
        write_miss_line(plan.note_path, plan.miss_line, writer=_writer(LINE_WRITER, deps))
    return plan.note_path


def build_date(day: date, *, deps: BuildDeps, event, check: bool) -> Path:
    """ONE date: plan (the first check when `check`), record the rows, write
    the note."""
    plan = plan_note(day, deps=deps, event=event, check=check)
    deps.store.record_build(day, plan.rows)
    return write_note(plan, deps=deps)


def run_drc_build(event, *, deps: Optional[BuildDeps] = None) -> Path:
    """D2's ONE entry: the event's day, then every re-paired date in date
    order (D3-2r). Returns the event day's note path — never empty (F-10)."""
    deps = deps if deps is not None else default_deps()
    note = build_date(event.date, deps=deps, event=event, check=True)
    day_row = deps.store.event_for(event.date)["day"]
    repaired = sorted(date.fromisoformat(d) for d in (day_row["derived"].get("repaired") or []))
    for i, d in enumerate(repaired):
        try:
            build_date(d, deps=deps, event=event_of(d, deps.store), check=False)
        except Exception as e:  # noqa: BLE001 — named, the later dates named, never done (L1)
            later = ", ".join(x.isoformat() for x in repaired[i + 1:]) or "none"
            raise BuildError(
                f"re-paired {d}: note {template.note_path(Path(deps.vault_root), d)} failed — "
                f"{type(e).__name__}: {e} · not rebuilt: {later}"
            ) from e
    return note


__all__ = [
    "FN_VERSION", "WRITER", "BuildDeps", "BuildError", "BuildPlan", "UnitWrite", "build_date", "default_deps",
    "default_vault_root", "event_of", "plan_note", "run_drc_build", "write_note",
]
