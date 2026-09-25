"""DRC D2 — THE ONE IMPORT PLACE (v2 §2–§3; v3 §2b, §5, `[F-17]`).

Every file he gives Cobalt for a day's DRC arrives through `place()`:
the `/drc` upload, and — through `scan_folder()` — the files he drops BY
HAND into `1 - Trading/5 - Review/_imports/drc/<date>/` (09-23 R17 (2)).
One parse path (L3): the same classifier, parsers, row writer, state,
event and `[F-17]` route behind both doors; the ONE difference is that a
hand-dropped file is never written again (the bytes writer runs for an
upload only).

WHAT A FILE IS (R114): its HEADER, through D1's ONE classifier
(`detect.detect_set` / `detect_kind`) — never its name, its extension or
a kind the request names (there is no kind field). His name is kept, any
extension. A header matching neither kind → `ignored`, listed, nothing
stored; two files of one kind → the WHOLE drop refused, both named. A
`partial` file (R17 (5)) is stored and parsed and counts as placed, loud.

THE DATE (R17 (3)): the trading log's rows take the drop's `date` (the
upload's field, or the `<date>` folder) — `detect.import_folder_date` is
the one date rule.

BOTH-PLACED (R91; L2 — deterministic, in the request, no poller, no
LLM): a `parsed`/`partial` trading log AND a `parsed`/`partial` stats log
→ READY; a trading log with ZERO executions is the no-trade DAY (no stats
log needed). Either fires the event on the day's CURRENT trading-log
import row (L18: pending → running → done | failed), then THE `[F-17]`
ROUTE as K1 / K2 built it — `seed_for` → `build_day` → `record_day` —
never a pairing, seed or statement of its own (L72), then D3's ONE build
entry, `cobalt.drc.build.run_drc_build(event)`. Until D3 exists that
import fails and the event lands `failed: build not built (D3)` — loud,
never `done` (L1).

THE NO-TRADE ACTION (R93 as v3 `[F-05]`): `no_trade()` writes his
`no_trade` statement through the ONE writer (`record_stated_book`,
`via = "drc_page"`) and rebuilds EXACTLY as the CLI's trigger does
(AMENDED C7). A FILE-LESS no-trade day has no event row in the ruled
schema (X-NT, the build report's ESCALATE): its build is not called.

MARKET RESET (R102): every door refuses 20:00–21:00 ET before anything
is read or written, with the reason.

`DrcStore` is the one writer of every `drc_*` row (L40); nothing here
writes SQL.
"""

from __future__ import annotations

import hashlib
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Iterable, Literal, Optional

from loguru import logger
from pydantic import BaseModel, Field

from cobalt.session import SessionBlocked, assert_writable
from cobalt.vault import DRC_IMPORTS_REL, resolve_vault_path
from cobalt.vaultwrite.store import VaultWriteStore
from cobalt.vaultwrite.writer import VaultWriteError, VaultWriter

from .detect import detect_kind, detect_set, import_folder_date
from .models import (
    OPENING_NOT_STATED,
    Detection,
    Kind,
    Outcome,
    PairingError,
    ParsedStatsLog,
    ParsedTradingLog,
    missing_of,
)
from .pairing import build_day
from .stats_log import StatsLogSource
from .store import DrcStore
from .trading_log import TradingLogSource

#: R102's refusal, the same words on every door.
RESET_REFUSAL = "refused: market reset 20:00–21:00 — drop again after 21:00"
WAITING_TRADING = "waiting for: trading log"
WAITING_STATS = "waiting for: stats log"
READY = "READY"
NO_TRADE = "no-trade"
#: v3 §2c / seam (2): a day recorded with no book stated.
UNPAIRED = "not computed — opening book not stated · state your opening book for {day}"
#: X-NT (the build report's ESCALATE): a file-less no-trade day's event has no row.
NO_TRADE_WAITS = "no-trade day recorded — its DRC build waits on the no-trade event home (ESCALATE X-NT)"
BUILD_NOT_BUILT = "build not built (D3)"
SCREENSHOT_NOT_BUILT = (
    "screenshot binding not built: no store path writes a screenshot row (drc_imports.kind = "
    "'screenshot' with its trade_key) on this tree — ESCALATE; nothing stored, nothing bound"
)

_PLACED = (Outcome.PARSED.value, Outcome.PARTIAL.value)
_PNG = b"\x89PNG\r\n\x1a\n"
_JPEG = b"\xff\xd8\xff"
_TRADE_ID = re.compile(r"^(.+?)-(long|short)-")

Status = Literal["parsed", "partial", "failed", "ignored", "already imported", "ambiguous"]
#: The models below have a FIELD named `date`; annotating it `date` would
#: resolve to the field's own default inside the class body.
_Date = date


class BuildNotBuilt(RuntimeError):
    """D3's build entry does not exist on this tree."""


class FileLine(BaseModel):
    """One file's line on the page."""

    name: str
    kind: Optional[str] = None
    status: Status
    reason: str = ""
    line: Optional[int] = None
    import_id: Optional[int] = None

    def text(self) -> str:
        if self.status == "parsed":
            return f"✓ {self.name} — {self.kind} parsed"
        if self.status == "partial":
            return f"{self.name} — {self.kind} {self.reason}"
        if self.status == "failed":
            return f"FAILED: {self.name} — {self.reason}"
        if self.status == "already imported":
            return f"already imported: {self.name}"
        return self.reason  # ignored / ambiguous: the classifier's own words


class DrcInputsPlaced(BaseModel):
    """THE event (v2 §3, L57): what D3's build is built from — the ids and
    sha256s of the stored rows, never a second copy of them. `partial`
    names each partial file's missing columns (R17 (5)); `orphaned` each
    screenshot binding a superseding trading log left behind (X13)."""

    date: _Date
    import_id: int
    stats_import_id: Optional[int] = None
    screenshot_import_ids: list[int] = Field(default_factory=list)
    sha256s: dict[str, str] = Field(default_factory=dict)
    partial: dict[str, list[str]] = Field(default_factory=dict)
    kind: Literal["trades", "no_trade"]
    orphaned: list[str] = Field(default_factory=list)


class PlaceResult(BaseModel):
    """What one action did: the per-file lines, the day's state after it,
    the status line, the event it fired (if any)."""

    date: Optional[_Date] = None
    refused: Optional[str] = None
    message: Optional[str] = None
    files: list[FileLine] = Field(default_factory=list)
    state: str = ""
    status_line: str = ""
    event: Optional[DrcInputsPlaced] = None
    orphaned: list[str] = Field(default_factory=list)
    note_path: Optional[str] = None


class DayView(BaseModel):
    """Everything `GET /drc` shows for a date — READ ONLY (it writes
    nothing: every value is a store read or a folder listing)."""

    date: _Date
    morning: list[str] = Field(default_factory=list)
    stated_difference: Optional[str] = None
    unpaired: Optional[str] = None
    notes: list[str] = Field(default_factory=list)
    files: list[FileLine] = Field(default_factory=list)
    orphaned: list[str] = Field(default_factory=list)
    folder_pending: list[str] = Field(default_factory=list)
    counts: dict[str, Any] = Field(default_factory=dict)
    trades: list[str] = Field(default_factory=list)
    state: str = ""
    status_line: str = ""
    event_line: Optional[str] = None


# ---------------------------------------------------------------------
# small reads
# ---------------------------------------------------------------------


def is_trading_day(day: date) -> bool:
    """THE one trading-day rule, `daymode.propose.prior_trading_day`'s
    calendar (L3): `day` is a trading day when it is the trading day
    before the next one."""
    from cobalt.daymode.propose import prior_trading_day

    return prior_trading_day(day + timedelta(days=1)) == day


def _prior(day: date) -> date:
    from cobalt.daymode.propose import prior_trading_day

    return prior_trading_day(day)


def _root(vault_root: Optional[Path]) -> Path:
    return Path(vault_root) if vault_root is not None else resolve_vault_path()


def _folder(root: Path, day: date) -> Path:
    return root / DRC_IMPORTS_REL / day.isoformat()


def _current(view: dict, kind: str) -> Optional[dict]:
    rows = [r for r in view["imports"] if r["current"] and r["kind"] == kind]
    return rows[-1] if rows else None


def _placed(row: Optional[dict]) -> bool:
    return row is not None and row["parse_status"] in _PLACED


def _state(view: dict) -> str:
    """The date's STATE, deterministic (L2), from the stored rows."""
    trading, stats = _current(view, Kind.TRADING_LOG.value), _current(view, Kind.STATS_LOG.value)
    if not _placed(trading):
        return WAITING_TRADING
    if trading["fills"] == 0:
        return NO_TRADE
    return READY if _placed(stats) else WAITING_STATS


def _computed(view: dict) -> bool:
    day = view["day"]
    return day is not None and "pairing" not in day["derived"].get("not_computed", {})


def _orphans(view: dict) -> list[str]:
    """X13: a bound screenshot whose trade the CURRENT trading log no
    longer carries — listed, never re-bound, never deleted."""
    if not _computed(view):
        return []
    trades = set(view["trades"])
    return [
        f"orphaned: {r['name']} — trade {r['trade_key']} not in the current trading log"
        for r in view["imports"]
        if r["current"] and r["kind"] == "screenshot" and r["trade_key"] not in trades
    ]


def _event(day: date, view: dict, orphaned: list[str]) -> DrcInputsPlaced:
    """The event, built from the stored rows (L57)."""
    trading = _current(view, Kind.TRADING_LOG.value)
    stats = _current(view, Kind.STATS_LOG.value)
    stats = stats if _placed(stats) else None
    shots = [r for r in view["imports"] if r["current"] and r["kind"] == "screenshot"]
    rows = [r for r in (trading, stats, *shots) if r is not None]
    return DrcInputsPlaced(
        date=day,
        import_id=trading["id"],
        stats_import_id=None if stats is None else stats["id"],
        screenshot_import_ids=[r["id"] for r in shots],
        sha256s={str(r["id"]): r["sha256"] for r in rows},
        partial={
            str(r["id"]): missing_of(Outcome.PARTIAL, r["reason"])
            for r in (trading, stats)
            if r is not None and r["parse_status"] == Outcome.PARTIAL.value
        },
        kind="no_trade" if trading["fills"] == 0 else "trades",
        orphaned=orphaned,
    )


def _line(result, import_id: Optional[int]) -> FileLine:
    """A stored file's line, from its parse result."""
    reason = result.reason
    if result.outcome is Outcome.FAILED and reason.startswith(f"{result.name}: "):
        reason = reason[len(result.name) + 2:]
    return FileLine(
        name=result.name, kind=result.kind.value, status=result.outcome.value, reason=reason,
        line=result.line, import_id=import_id,
    )


def _parse(kind: Kind, data: bytes, day: date, detection: Detection):
    """D1's sources, the trading log with `import_date = day` (L9)."""
    if kind is Kind.TRADING_LOG:
        return TradingLogSource().parse(data, day, detection)
    return StatsLogSource().parse(data, detection)


# ---------------------------------------------------------------------
# the one pipeline
# ---------------------------------------------------------------------


def place(
    day: date,
    files: Iterable[tuple[str, bytes]],
    trade_key: Optional[str] = None,
    *,
    from_folder: bool = False,
    now: Optional[datetime] = None,
    vault_root: Optional[Path] = None,
) -> PlaceResult:
    """Place one drop for `day`. `from_folder` = the files already sit in
    the day's folder (`scan_folder`): their bytes are NOT written again.
    With a `trade_key` the files are screenshots for that trade."""
    files = list(files)
    try:
        assert_writable("drc.import", target=day.isoformat(), now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    if trade_key is not None:
        return _screenshots(day, files)

    verdict = detect_set(files)
    detections = [detect_kind(name, data) for name, data in files]
    if verdict.status == "failed":
        # Two files of one kind: the WHOLE drop is refused, nothing stored.
        return PlaceResult(
            date=day,
            refused=verdict.reason,
            files=[FileLine(name=d.name, kind=None if d.kind is None else d.kind.value, status="ambiguous",
                            reason=verdict.reason) for d in detections],
        )
    lines: list[FileLine] = []
    chosen: dict[Kind, tuple[str, bytes, Detection]] = {}
    for (name, data), det in zip(files, detections):
        if det.outcome is Outcome.IGNORED:
            lines.append(FileLine(name=name, status="ignored", reason=det.reason))
        elif det.outcome is Outcome.FAILED:
            lines.append(FileLine(
                name=name, kind=None if det.kind is None else det.kind.value, status="failed",
                reason=det.reason.split(" — ", 1)[-1],
            ))
        else:
            chosen[det.kind] = (name, data, det)

    root = _root(vault_root)
    writer = None if from_folder else VaultWriter("drc.import", store=VaultWriteStore())
    store = DrcStore()
    this_drop: dict[int, object] = {}
    for kind in (Kind.TRADING_LOG, Kind.STATS_LOG):
        if kind not in chosen:
            continue
        name, data, det = chosen[kind]
        if writer is not None:
            try:
                written = writer.write_import_bytes(root, f"{DRC_IMPORTS_REL}/{day.isoformat()}/{name}", data)
            except SessionBlocked:
                return PlaceResult(date=day, refused=RESET_REFUSAL, files=lines)
            except VaultWriteError as e:
                lines.append(FileLine(name=name, kind=kind.value, status="failed", reason=f"not written: {e}"))
                continue
            if written.name != name:
                name, det = written.name, detect_kind(written.name, data)
        parsed = _parse(kind, data, day, det)
        executions = parsed.executions if kind is Kind.TRADING_LOG else ()
        import_id = store.record_import(day, parsed.result, data, executions)
        this_drop[import_id] = parsed
        lines.append(_line(parsed.result, import_id))
    return _after(day, store, lines, this_drop, root)


def _screenshots(day: date, files: list[tuple[str, bytes]]) -> PlaceResult:
    """A per-trade drop (v2 `[F-07]`): its image header decides. The
    binding itself has no store path on this tree (the report's
    ESCALATE): every screenshot is refused, nothing stored or written."""
    lines = []
    for name, data in files:
        if not data:
            reason = "an empty file is not an image"
        elif not (data.startswith(_PNG) or data.startswith(_JPEG)):
            reason = "not a PNG / JPEG header"
        else:
            reason = SCREENSHOT_NOT_BUILT
        lines.append(FileLine(name=name, kind="screenshot", status="failed", reason=reason))
    return PlaceResult(date=day, files=lines)


def _after(day: date, store: DrcStore, lines: list[FileLine], this_drop: dict, root: Path) -> PlaceResult:
    """Recompute the date's state from the stored rows; on READY or the
    no-trade day, fire the event and run the `[F-17]` route."""
    view = store.event_for(day)
    state = _state(view)
    result = PlaceResult(date=day, files=lines, state=state, status_line=state)
    if state not in (READY, NO_TRADE):
        return result
    return _fire(day, store, view, this_drop, root, result)


class _LoadError(ValueError):
    pass


def _load(day: date, row: dict, kind: Kind, this_drop: dict, root: Path):
    """The parse of a CURRENT stored file: this drop's own, or — for a
    file placed by an earlier drop — its stored bytes re-read from the
    day's folder, sha256-checked against its row, through the same
    classifier and parser (one parse path, L3). Missing or changed bytes
    FAIL; nothing is assumed."""
    if row["id"] in this_drop:
        return this_drop[row["id"]]
    path = _folder(root, day) / row["name"]
    if not path.is_file():
        raise _LoadError(f"{row['name']}: the stored file is not in {DRC_IMPORTS_REL}/{day} — nothing assumed")
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != row["sha256"]:
        raise _LoadError(f"{row['name']}: its bytes changed since import #{row['id']} — nothing assumed")
    det = detect_kind(row["name"], data)
    if det.kind is not kind:
        raise _LoadError(f"{row['name']}: its header no longer reads as {kind.value} — nothing assumed")
    return _parse(kind, data, day, det)


def _fire(day: date, store: DrcStore, view: dict, this_drop: dict, root: Path, result: PlaceResult) -> PlaceResult:
    trading = _current(view, Kind.TRADING_LOG.value)
    stats = _current(view, Kind.STATS_LOG.value)
    stats = stats if _placed(stats) else None
    import_id = trading["id"]
    store.mark_event(import_id, "pending")
    result.event = _event(day, view, [])

    def fail(step: str, reason: str) -> PlaceResult:
        store.mark_event(import_id, "failed", reason)
        result.status_line = f"DRC build FAILED: {step} — {reason}"
        logger.error(f"DRC {day}: event on import #{import_id} failed at {step}: {reason}")
        return result

    try:
        t_parsed: ParsedTradingLog = _load(day, trading, Kind.TRADING_LOG, this_drop, root)
        s_parsed: Optional[ParsedStatsLog] = (
            None if stats is None else _load(day, stats, Kind.STATS_LOG, this_drop, root)
        )
    except _LoadError as e:
        return fail("inputs", str(e))
    ids = {Kind.TRADING_LOG: trading["id"]}
    if stats is not None:
        ids[Kind.STATS_LOG] = stats["id"]

    # THE [F-17] ROUTE (seam (1)–(3)) — K1 / K2's, called, never re-implemented.
    try:
        book = store.seed_for(day)
    except PairingError as e:
        return fail("seed", str(e))  # verbatim, loud; the files stay stored
    try:
        if book is None:
            pairing = build_day(t_parsed, s_parsed, seed=None)
            store.record_day(pairing, ids, None)
        else:
            pairing = build_day(t_parsed, s_parsed, seed=book.positions, resolves=book.resolves)
            store.record_day(pairing, ids, book)
    except (PairingError, ValueError) as e:
        return fail("record", str(e))  # `drc_rows` unchanged ([F-25])

    after = store.event_for(day)
    result.orphaned = _orphans(after)
    result.event = _event(day, after, result.orphaned)
    unpaired = pairing.not_computed.get("pairing") == OPENING_NOT_STATED
    store.mark_event(import_id, "running")
    try:
        note = _run_build(result.event)
    except Exception as e:  # noqa: BLE001 — any exception is `failed`, never `done` (L1)
        reason = str(e) if isinstance(e, BuildNotBuilt) else f"{type(e).__name__}: {e}"
        fail("build", reason)
        if unpaired:
            result.status_line = UNPAIRED.format(day=day.isoformat())
        return result
    store.mark_event(import_id, "done")
    result.note_path = str(note)
    if unpaired:
        result.status_line = UNPAIRED.format(day=day.isoformat())
    elif result.event.kind == "no_trade":
        result.status_line = f"no-trade day recorded → DRC built: {note}"
    else:
        result.status_line = f"READY → DRC built: {note}"
    return result


def _run_build(event: DrcInputsPlaced):
    """D3's ONE registered entry (v2 `[F-08]`: in the request)."""
    try:
        from cobalt.drc.build import run_drc_build
    except ModuleNotFoundError as e:
        if e.name != "cobalt.drc.build":
            raise
        raise BuildNotBuilt(BUILD_NOT_BUILT) from None
    return run_drc_build(event)


# ---------------------------------------------------------------------
# D2-3b — the files he drops by hand
# ---------------------------------------------------------------------


def scan_folder(
    day_text: str | date,
    *,
    now: Optional[datetime] = None,
    vault_root: Optional[Path] = None,
) -> PlaceResult:
    """Import the TOP-LEVEL files of `_imports/drc/<date>/` through
    `place()` (R17 (2)). A file whose name AND sha256 already sit on a row
    for the date is `already imported`; nothing in the folder is written,
    renamed, moved or deleted. Triggered by the page's action only — no
    poller, no job, no watcher."""
    day = day_text if isinstance(day_text, date) else import_folder_date(str(day_text))
    if day is None:
        return PlaceResult(refused=f"FAILED: {str(day_text)!r} is not a YYYY-MM-DD import folder — nothing read")
    try:
        assert_writable("drc.scan", target=day.isoformat(), now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    root = _root(vault_root)
    folder = _folder(root, day)
    store = DrcStore()
    view = store.event_for(day)
    if not folder.is_dir():
        return PlaceResult(date=day, message=f"no folder {DRC_IMPORTS_REL}/{day}", state=_state(view),
                           status_line=_state(view))
    known = {(r["name"], r["sha256"]) for r in view["imports"]}
    already: list[FileLine] = []
    new: list[tuple[str, bytes]] = []
    for path in sorted(p for p in folder.iterdir() if p.is_file() and not p.name.startswith(".")):
        data = path.read_bytes()
        if (path.name, hashlib.sha256(data).hexdigest()) in known:
            already.append(FileLine(name=path.name, status="already imported"))
        else:
            new.append((path.name, data))
    if not new:
        return PlaceResult(date=day, files=already, state=_state(view), status_line=_state(view))
    result = place(day, new, from_folder=True, now=now, vault_root=root)
    result.files = already + result.files
    return result


# ---------------------------------------------------------------------
# D2-3c — "No trades today"
# ---------------------------------------------------------------------


def no_trade(day: date, *, now: Optional[datetime] = None) -> PlaceResult:
    """His no-trade DRC for `day` (R93, v3 `[F-05]`): one `no_trade`
    statement through the ONE writer, then AMENDED C7's rebuild trigger."""
    try:
        assert_writable("drc.no_trade", target=day.isoformat(), now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    if not is_trading_day(day):
        return PlaceResult(date=day, refused=f"refused: {day} is not a market trading day")
    store = DrcStore()
    trading = _current(store.event_for(day), Kind.TRADING_LOG.value)
    if trading is not None and trading["fills"] > 0:
        return PlaceResult(
            date=day,
            refused=f"refused: {day} has a trading log with {trading['fills']} executions — not a no-trade day",
        )
    try:
        store.record_stated_book(day, "no_trade", [], via="drc_page", now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    except ValueError as e:
        return PlaceResult(date=day, refused=str(e))  # the store's words, verbatim
    if store.has_current_import(day, Kind.TRADING_LOG) or store.has_chain_through(day):
        try:
            store.rebuild(store.effect_day(day, None))
        except (PairingError, ValueError) as e:
            return PlaceResult(date=day, message=f"not rebuilt: {e}")  # the statement is kept
        # A zero-execution trading log's event sits on its import row (D2-3).
        return PlaceResult(date=day, message=NO_TRADE_WAITS if trading is None else "no-trade day recorded")
    return PlaceResult(date=day, message=f"stated; {day} has no import yet")


# ---------------------------------------------------------------------
# D2-4 — what the page shows (reads only)
# ---------------------------------------------------------------------


def _morning(store: DrcStore, day: date) -> list[str]:
    """THE MORNING LINE (v3 §2b step 4, §5): the book `day` starts from,
    read before any drop."""
    try:
        book = store.seed_for(day)
    except PairingError as e:
        lines = [str(e)]
        if "has no import and no no-trade record" in str(e):
            lines.append(
                f"No prior DRC for {_prior(day)} — import it, record its no-trade DRC, or state your book"
            )
        return lines
    if book is None:
        return [
            f"state your opening book for {day} — until the form ships: "
            f"cobalt drc state-book --opening {day} …"
        ]
    symbols = ", ".join(p.symbol for p in book.positions) or "flat"
    n = len(book.positions)
    head = (
        f"Starting book from DRC {book.from_day}: {n} open ({symbols})"
        if book.from_day is not None
        else f"Starting book stated for {day} (statement #{book.stated_book_id}): {n} open ({symbols})"
    )
    return [head] + [
        f"{p.symbol} {p.direction.value} {p.held_shares} · opened: {p.opened_on or 'not stated'}"
        for p in book.positions
    ]


def folder_pending(day: date, view: dict, root: Path) -> list[str]:
    """The folder's top-level files not on a row for the date (by name
    and sha256) — a read of names and bytes, nothing stored."""
    folder = _folder(root, day)
    if not folder.is_dir():
        return []
    known = {(r["name"], r["sha256"]) for r in view["imports"]}
    return [
        p.name
        for p in sorted(folder.iterdir())
        if p.is_file() and not p.name.startswith(".")
        and (p.name, hashlib.sha256(p.read_bytes()).hexdigest()) not in known
    ]


def _symbol(trade_id: str) -> str:
    m = _TRADE_ID.match(trade_id)
    return m.group(1) if m else trade_id


def day_view(day: date, *, cards: Optional[list[dict]] = None, vault_root: Optional[Path] = None) -> DayView:
    """The page's content for `day`. READS ONLY."""
    store = DrcStore()
    view = store.event_for(day)
    out = DayView(date=day, morning=_morning(store, day), stated_difference=store.stated_difference(day))
    out.files = [
        FileLine(
            name=r["name"], kind=r["kind"], status=r["parse_status"],
            reason=r["reason"] if r["parse_status"] != "failed" else r["reason"].removeprefix(f"{r['name']}: "),
            line=r["failed_line"], import_id=r["id"],
        )
        for r in view["imports"]
        if r["current"] and r["kind"] != "screenshot"
    ]
    derived = view["day"]["derived"] if view["day"] else {}
    inputs = view["day"]["inputs"] if view["day"] else {}
    pairing_nc = derived.get("not_computed", {}).get("pairing")
    if pairing_nc == OPENING_NOT_STATED:
        out.unpaired = UNPAIRED.format(day=day.isoformat())
    elif pairing_nc:
        out.notes.append(f"pairing {pairing_nc}")
    if derived.get("book_stale"):
        stale = derived["book_stale"]
        out.notes.append(f"book stale (root {stale['root']}): {stale['reason']}")
    for item in derived.get("not_repaired", []):
        out.notes.append(f"not re-paired: {item['day']} — {item['reason']}")
    out.orphaned = _orphans(view)
    out.trades = list(view["trades"])
    try:
        out.folder_pending = folder_pending(day, view, _root(vault_root))
    except Exception as e:  # noqa: BLE001 — an unresolved vault is shown, never hidden
        out.notes.append(f"FAILED: the imports folder is unreadable — {type(e).__name__}: {e}")

    trading = _current(view, Kind.TRADING_LOG.value)
    shots = [r for r in view["imports"] if r["current"] and r["kind"] == "screenshot"]
    bound = {r["trade_key"] for r in shots} & set(view["trades"])
    rows = view["rows"]
    unmatched = int(derived.get("unmatched", 0))
    symbols = {_symbol(t) for t in view["trades"]}
    out.counts = {
        "executions": None if trading is None else trading["fills"],
        "trades": rows["trade"],
        "open positions": rows["open_position"],
        "stats rows matched": rows["stats_row"] - unmatched,
        "stats rows unmatched": unmatched,
        "screenshots bound / trades": f"{len(bound)} / {rows['trade']}",
        "trades without a screenshot": rows["trade"] - len(bound),
        "cards with no trade": None if cards is None else sum(
            1 for c in cards if str(c.get("ticker", "")).upper() not in symbols
        ),
    }

    out.state = _state(view)
    ev_state, ev_error = view["state"], view["error"]
    if ev_state is not None:
        out.event_line = f"event: {ev_state}" + (f" — {ev_error}" if ev_error else "")
    if out.unpaired:
        out.status_line = out.unpaired
    elif trading is None and inputs.get("no_trade_id") is not None:
        out.status_line = NO_TRADE_WAITS
    elif out.state in (READY, NO_TRADE) and ev_state == "done":
        prefix = "no-trade day recorded" if out.state == NO_TRADE else "READY"
        out.status_line = f"{prefix} → DRC built: (the note path is returned on the drop; not stored — D3)"
    elif out.state in (READY, NO_TRADE) and ev_state == "failed":
        out.status_line = f"DRC build FAILED: event — {ev_error}"
    elif out.state in (READY, NO_TRADE) and ev_state in ("pending", "running"):
        out.status_line = (
            f"DRC build FAILED: event — left {ev_state} at {view['updated_at']}, no build returned "
            "(a dead request is failed, never done — L1)"
        )
    else:
        out.status_line = out.state
    return out


def render_status(view: DayView) -> str:
    """The page's status line — exactly one line."""
    return view.status_line


__all__ = [
    "BUILD_NOT_BUILT",
    "NO_TRADE_WAITS",
    "RESET_REFUSAL",
    "UNPAIRED",
    "DayView",
    "DrcInputsPlaced",
    "FileLine",
    "PlaceResult",
    "day_view",
    "folder_pending",
    "is_trading_day",
    "no_trade",
    "place",
    "render_status",
    "scan_folder",
]
