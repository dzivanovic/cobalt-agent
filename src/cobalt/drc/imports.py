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
log needed). Either fires the event of the day's CURRENT trading-log
import (L18: pending → running → done | failed, one event-home row per
source — D2 fix r1, `DRC-D2-SEAM-2026-09-25.md` §1), then THE `[F-17]`
ROUTE as K1 / K2 built it — `seed_for` → `build_day` → `record_day` —
never a pairing, seed or statement of its own (L72), then D3's ONE build
entry, `cobalt.drc.build.run_drc_build(event)`. Until D3 exists that
import fails and the event lands `failed: build not built (D3)` — loud,
never `done` (L1). ANY exception after `pending` lands the event
`failed` naming its step (D2 fix r1 F-1): no row is left `pending` or
`running` by an exception.

THE NO-TRADE ACTION (R93 as v3 `[F-05]`): `no_trade()` writes his
`no_trade` statement through the ONE writer (`record_stated_book`,
`via = "drc_page"`); a FILE-LESS no-trade day then runs `no_trade_event`
— its event's source is that statement (§1): `fire_event` → the rebuild
(AMENDED C7) → `running` → the build → `done` with its note path |
`failed`. The CLI's `state-book --no-trade --apply` calls the SAME
function (L3).

THE SCREENSHOT DROP (§2): a PNG / JPEG on a trade of the day's CURRENT
computed trading log is written by the one bytes writer and bound by
`DrcStore.record_screenshot`, the one writer of screenshot rows; a READY
day re-fires.

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
from pydantic import BaseModel, Field, model_validator

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
BUILD_NOT_BUILT = "build not built (D3)"
#: D2 fix r2 F-10: `done` needs a note path (seam §1, `0019_drc_events.sql`).
NO_NOTE_PATH = "the build returned no note path ({note!r}) — never done (L1)"

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


class _NoNotePath(RuntimeError):
    """D3's build returned no note path (`NO_NOTE_PATH`): `failed`, never `done`."""


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
    screenshot binding a superseding trading log left behind (X13).

    D2 fix r1 (`DRC-D2-SEAM-2026-09-25.md` §1): `event_id` is its row in
    the event home. Its source is EXACTLY one of `import_id` (a file
    day) and `stated_book_id` (a file-less no-trade day, with the
    statement's `stated_book_sha256`); a stated source is `no_trade` with
    no stats, no screenshots, no partial file and no file sha256s — a
    breach is a `ValidationError` (L1). `seed_from_day` /
    `seed_from_book_sha256`: the day's `seed` row, `None` without one."""

    date: _Date
    event_id: int
    import_id: Optional[int] = None
    stated_book_id: Optional[int] = None
    stated_book_sha256: Optional[str] = None
    seed_from_day: Optional[_Date] = None
    seed_from_book_sha256: Optional[str] = None
    stats_import_id: Optional[int] = None
    screenshot_import_ids: list[int] = Field(default_factory=list)
    sha256s: dict[str, str] = Field(default_factory=dict)
    partial: dict[str, list[str]] = Field(default_factory=dict)
    kind: Literal["trades", "no_trade"]
    orphaned: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _one_source(self) -> "DrcInputsPlaced":
        if (self.import_id is None) == (self.stated_book_id is None):
            raise ValueError("an event names exactly one source: import_id or stated_book_id")
        if self.stated_book_id is not None:
            breaches = [
                name
                for name, bad in (
                    ("kind is not no_trade", self.kind != "no_trade"),
                    ("a stats import", self.stats_import_id is not None),
                    ("screenshots", bool(self.screenshot_import_ids)),
                    ("a partial file", bool(self.partial)),
                    ("file sha256s", bool(self.sha256s)),
                    ("no hex-64 stated_book_sha256",
                     not (isinstance(self.stated_book_sha256, str)
                          and re.fullmatch(r"[0-9a-f]{64}", self.stated_book_sha256))),
                )
                if bad
            ]
            if breaches:
                raise ValueError(f"a file-less (stated) event carries {', '.join(breaches)}")
        return self


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
    """The date's STATE, deterministic (L2), from the stored rows. D2 fix
    r1 (§1): no current trading log but a current `no_trade` statement
    (`event_for`'s `stated_book_id`, the store's `_no_trade_id` rule) is
    the file-less no-trade day."""
    trading, stats = _current(view, Kind.TRADING_LOG.value), _current(view, Kind.STATS_LOG.value)
    if trading is None and view["stated_book_id"] is not None:
        return NO_TRADE
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
    """The event, built from the stored rows (L57) — `event_for`'s, never
    a second copy: a file day's from its current files, a file-less
    no-trade day's from its current `no_trade` statement (§1)."""
    trading = _current(view, Kind.TRADING_LOG.value)
    seed = view["seed"] or {}
    common = dict(
        date=day,
        event_id=view["event_id"],
        seed_from_day=seed.get("from_day"),
        seed_from_book_sha256=seed.get("from_book_sha256"),
        orphaned=orphaned,
    )
    if trading is None:
        return DrcInputsPlaced(
            **common,
            stated_book_id=view["stated_book_id"],
            stated_book_sha256=view["stated_book_sha256"],
            kind="no_trade",
        )
    stats = _current(view, Kind.STATS_LOG.value)
    stats = stats if _placed(stats) else None
    shots = [r for r in view["imports"] if r["current"] and r["kind"] == "screenshot"]
    rows = [r for r in (trading, stats, *shots) if r is not None]
    return DrcInputsPlaced(
        **common,
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
        return _screenshots(day, files, trade_key, _root(vault_root))

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


def _screenshots(day: date, files: list[tuple[str, bytes]], trade_key: str, root: Path) -> PlaceResult:
    """A per-trade drop (v2 `[F-07]`; D2 fix r1 S-2, `DRC-D2-SEAM-2026-09-
    25.md` §2): its image header decides; the key must be a trade of the
    day's CURRENT computed trading log, else FAILED and nothing bound or
    written; then the bytes through the ONE bytes writer and the row
    through the ONE screenshot writer (`record_screenshot`). A READY day
    re-fires (v2 `:82`); a day not yet READY only stores the binding."""
    store = DrcStore()
    trades = set(store.event_for(day)["trades"])
    writer = None
    lines: list[FileLine] = []
    for name, data in files:
        if not data:
            reason = "an empty file is not an image"
        elif not (data.startswith(_PNG) or data.startswith(_JPEG)):
            reason = "not a PNG / JPEG header"
        elif trade_key not in trades:
            reason = f"trade {trade_key} is not in the current trading log"
        else:
            writer = writer or VaultWriter("drc.import", store=VaultWriteStore())
            try:
                written = writer.write_import_bytes(root, f"{DRC_IMPORTS_REL}/{day.isoformat()}/{name}", data)
            except SessionBlocked:
                return PlaceResult(date=day, refused=RESET_REFUSAL, files=lines)
            except VaultWriteError as e:
                reason = f"not written: {e}"
            else:
                import_id = store.record_screenshot(day, written.name, data, trade_key)
                lines.append(FileLine(name=written.name, kind="screenshot", status="parsed", import_id=import_id))
                continue
        lines.append(FileLine(name=name, kind="screenshot", status="failed", reason=reason))
    if not any(line.status == "parsed" for line in lines):
        return PlaceResult(date=day, files=lines)
    view = store.event_for(day)
    state = _state(view)
    if state != READY:
        return PlaceResult(date=day, files=lines, state=state, status_line=state)
    return _after(day, store, lines, {}, root)


def _after(day: date, store: DrcStore, lines: list[FileLine], this_drop: dict, root: Path) -> PlaceResult:
    """Recompute the date's state from the stored rows; on READY or the
    no-trade day of a stored trading log, fire the event and run the
    `[F-17]` route. (A file-less no-trade day's event is `no_trade_event`'s.)"""
    view = store.event_for(day)
    state = _state(view)
    result = PlaceResult(date=day, files=lines, state=state, status_line=state)
    if state not in (READY, NO_TRADE) or _current(view, Kind.TRADING_LOG.value) is None:
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


def _failer(day: date, store: DrcStore, event_id: int, source: str, result: PlaceResult):
    """THE one `failed` path of an event (L1, L18): the row names its
    reason, the status line names the step."""

    def fail(step: str, reason: str, *, uncaught: bool = False) -> PlaceResult:
        # D2 fix r1 F-1: an exception no step names is stored with its
        # step, `<step> — <Type>: <message>` (the named ones verbatim).
        error = f"{step} — {reason}" if uncaught else reason
        store.mark_event(event_id, "failed", error)
        result.status_line = f"DRC build FAILED: {step} — {reason}"
        logger.error(f"DRC {day}: event #{event_id} ({source}) failed at {step}: {reason}")
        return result

    return fail


def _uncaught(e: Exception) -> str:
    return f"{type(e).__name__}: {e}"


def _fire(day: date, store: DrcStore, view: dict, this_drop: dict, root: Path, result: PlaceResult) -> PlaceResult:
    trading = _current(view, Kind.TRADING_LOG.value)
    stats = _current(view, Kind.STATS_LOG.value)
    stats = stats if _placed(stats) else None
    event_id = store.fire_event(day, import_id=trading["id"])
    fail = _failer(day, store, event_id, f"import #{trading['id']}", result)

    # D2 fix r1 F-1 (L18, v2 `[F-08]`): between `pending` and the terminal
    # move EVERY exception lands the event `failed` — the named ones with
    # their verbatim texts, any other as `<step> — <Type>: <message>`.
    step = "inputs"
    try:
        result.event = _event(day, store.event_for(day), [])
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
        step = "seed"
        try:
            book = store.seed_for(day)
        except PairingError as e:
            return fail("seed", str(e))  # verbatim, loud; the files stay stored
        step = "record"
        try:
            if book is None:
                pairing = build_day(t_parsed, s_parsed, seed=None)
                store.record_day(pairing, ids, None)
            else:
                pairing = build_day(t_parsed, s_parsed, seed=book.positions, resolves=book.resolves)
                store.record_day(pairing, ids, book)
        except (PairingError, ValueError) as e:
            return fail("record", str(e))  # `drc_rows` unchanged ([F-25])

        step = "build"
        after = store.event_for(day)
        result.orphaned = _orphans(after)
        result.event = _event(day, after, result.orphaned)
        unpaired = pairing.not_computed.get("pairing") == OPENING_NOT_STATED
        store.mark_event(event_id, "running")
        try:
            note = _run_build(result.event)
            if note is None or not str(note):
                raise _NoNotePath(NO_NOTE_PATH.format(note=note))
            store.mark_event(event_id, "done", note_path=str(note))
        except Exception as e:  # noqa: BLE001 — any exception is `failed`, never `done` (L1)
            fail("build", str(e) if isinstance(e, (BuildNotBuilt, _NoNotePath)) else _uncaught(e))
            if unpaired:
                result.status_line = UNPAIRED.format(day=day.isoformat())
            return result
    except Exception as e:  # noqa: BLE001 — F-1: never left pending / running
        return fail(step, _uncaught(e), uncaught=True)
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
        stated = store.record_stated_book(day, "no_trade", [], via="drc_page", now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    except ValueError as e:
        return PlaceResult(date=day, refused=str(e))  # the store's words, verbatim
    if store.has_current_import(day, Kind.TRADING_LOG) or store.has_chain_through(day):
        if trading is None:
            # D2 fix r1 S-1: the FILE-LESS day's event, its source the
            # statement just written (`DRC-D2-SEAM-2026-09-25.md` §1).
            return no_trade_event(day, stated.id, now=now)
        try:
            store.rebuild(store.effect_day(day, None))
        except (PairingError, ValueError) as e:
            return PlaceResult(date=day, message=f"not rebuilt: {e}")  # the statement is kept
        # A zero-execution trading log's event sits on its import (D2-3).
        return PlaceResult(date=day, message="no-trade day recorded")
    return PlaceResult(date=day, message=f"stated; {day} has no import yet")


def no_trade_event(day: date, stated_book_id: int, *, now: Optional[datetime] = None) -> PlaceResult:
    """THE file-less no-trade day's event (D2 fix r1 S-1, `DRC-D2-SEAM-
    2026-09-25.md` §1) — ONE path for the page's `no_trade` AND the CLI's
    `state-book --no-trade --apply` (L3): `fire_event(day, stated_book_id=
    …)` → `pending`; the rebuild (AMENDED C7, `rebuild(effect_day(day,
    None))`: a `PairingError` / `ValueError` → `failed` with its text
    verbatim, the statement kept); `event_for` → the event; `running`; D3's
    build; `done` with its note path — or `failed` on ANY exception, never
    `done` (L1, L18). Refused inside `market_reset` before anything is
    written (R102)."""
    try:
        assert_writable("drc.no_trade_event", target=day.isoformat(), now=now)
    except SessionBlocked:
        return PlaceResult(date=day, refused=RESET_REFUSAL)
    store = DrcStore()
    result = PlaceResult(date=day, state=NO_TRADE, status_line=NO_TRADE)
    event_id = store.fire_event(day, stated_book_id=stated_book_id)
    fail = _failer(day, store, event_id, f"statement #{stated_book_id}", result)
    step = "record"
    try:
        try:
            dates = store.rebuild(store.effect_day(day, None))
        except (PairingError, ValueError) as e:
            result.message = f"not rebuilt: {e}"  # the statement is kept
            return fail("record", str(e))
        result.message = f"rebuilt: {', '.join(d.isoformat() for d in dates)}"
        step = "build"
        result.event = _event(day, store.event_for(day), [])
        store.mark_event(event_id, "running")
        try:
            note = _run_build(result.event)
            if note is None or not str(note):
                raise _NoNotePath(NO_NOTE_PATH.format(note=note))
            store.mark_event(event_id, "done", note_path=str(note))
        except Exception as e:  # noqa: BLE001 — any exception is `failed`, never `done` (L1)
            return fail("build", str(e) if isinstance(e, (BuildNotBuilt, _NoNotePath)) else _uncaught(e))
    except Exception as e:  # noqa: BLE001 — F-1: never left pending / running
        return fail(step, _uncaught(e), uncaught=True)
    result.note_path = str(note)
    result.status_line = f"no-trade day recorded → DRC built: {note}"
    return result


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
    if not _computed(view):
        # D2 fix r2 F-11 (X13): `_orphans` cannot check a binding against a
        # pairing that is not computed — each current one is listed, unchecked.
        out.notes.extend(
            f"screenshot {r['name']} — trade {r['trade_key']}: not checked, pairing not computed"
            for r in view["imports"]
            if r["current"] and r["kind"] == "screenshot"
        )
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
    elif out.state in (READY, NO_TRADE) and ev_state == "done":
        # D2 fix r1 (§1): the note path the `done` event row stores.
        prefix = "no-trade day recorded" if out.state == NO_TRADE else "READY"
        out.status_line = f"{prefix} → DRC built: {view['note_path']}"
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
    "NO_NOTE_PATH",
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
    "no_trade_event",
    "place",
    "render_status",
    "scan_folder",
]
