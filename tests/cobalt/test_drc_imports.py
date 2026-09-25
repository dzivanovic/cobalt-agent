"""DRC D2 — the one import place, OFFLINE half (`prompts/2026-09-25/
07-drc-d2-build.md` `## E2`).

What runs here without a database:
- D2-2, the bytes writer (`VaultWriter.write_import_bytes`) against a
  `tmp_path` vault and an in-memory `vault_writes` double (`_WriteStore`);
- D2-3 / D2-3b / D2-3c and the page (D2-4) against `_Drc`, an IN-MEMORY
  DOUBLE of `DrcStore` patched in as `imports.DrcStore` — it mirrors the
  store's current-file rule and `event_for`'s shape, nothing more. The
  `[F-17]` route, the event and every real row are proven WITH-DB in
  `test_drc_imports_db.py`.

Every vault write lands in a `tmp_path` vault (never the real one).
Constructed names, dates and symbols; D1's fixtures only (L32 / L45).
"""

from __future__ import annotations

import hashlib
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

import pytest

from cobalt.drc.models import Kind, Outcome, PairingError, StatedBook
from cobalt.session import SessionBlocked
from cobalt.vaultwrite.writer import VaultWriteError, VaultWriter

from test_drc_k2_experiments import _drop_column
from test_drc_store import D, D_NEXT, DAY1, E1, STATS

DRC = "1 - Trading/5 - Review/_imports/drc"
RESET_ET = datetime(2026, 9, 4, 0, 15, tzinfo=timezone.utc)  # 20:15 ET
NOTE = b"# a note\n\nnot a log\n"
PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16


# ---------------------------------------------------------------------
# doubles
# ---------------------------------------------------------------------


class _WriteStore:
    """`VaultWriteStore`'s write half, in memory."""

    def __init__(self):
        self.rows: list[dict] = []

    @contextmanager
    def pending_write(self, **kw):
        self.rows.append(kw)
        yield len(self.rows)

    def purge_expired(self, days: int = 30) -> int:
        return 0


@dataclass
class _Drc:
    """`DrcStore`, in memory: the rows `imports` writes and reads."""

    imports: list[dict] = field(default_factory=list)
    days: dict = field(default_factory=dict)
    stated: list[StatedBook] = field(default_factory=list)
    rebuilt: list[date] = field(default_factory=list)
    writes: list[str] = field(default_factory=list)
    seed: Any = None
    seed_error: Optional[str] = None

    def _current(self, day, kind):
        superseded = {r["supersedes"] for r in self.imports if r["supersedes"]}
        rows = [r for r in self.imports if r["import_date"] == day and r["kind"] == kind and r["id"] not in superseded]
        return rows[-1] if rows else None

    def record_import(self, import_date, result, data, executions=()):
        if result.kind is None or result.outcome is Outcome.IGNORED:
            raise ValueError(f"{result.name}: an {result.outcome.value} file of no kind is listed, never stored")
        self.writes.append("record_import")
        prior = self._current(import_date, result.kind.value)
        row = dict(
            id=len(self.imports) + 1, import_date=import_date, kind=result.kind.value, name=result.name,
            sha256=hashlib.sha256(data).hexdigest(), trade_key=None, parse_status=result.outcome.value,
            reason=result.reason, failed_line=result.line, supersedes=prior["id"] if prior else None,
            executions=list(executions), event_state=None, event_error=None,
        )
        self.imports.append(row)
        return row["id"]

    def mark_event(self, import_id, state, error=None):
        self.writes.append(f"mark_event:{state}")
        row = next(r for r in self.imports if r["id"] == import_id)
        row["event_state"], row["event_error"] = state, error

    def event_for(self, day):
        superseded = {r["supersedes"] for r in self.imports if r["supersedes"]}
        rows = [
            dict(
                id=r["id"], kind=r["kind"], name=r["name"], sha256=r["sha256"], trade_key=r["trade_key"],
                parse_status=r["parse_status"], reason=r["reason"], failed_line=r["failed_line"],
                supersedes=r["supersedes"], current=r["id"] not in superseded, fills=len(r["executions"]),
            )
            for r in self.imports
            if r["import_date"] == day
        ]
        cur = self._current(day, "trading_log")
        recorded = self.days.get(day)
        pairing = recorded[0] if recorded else None
        return {
            "import_id": cur["id"] if cur else None,
            "state": cur["event_state"] if cur else None,
            "updated_at": None,
            "error": cur["event_error"] if cur else None,
            "imports": rows,
            "day": None if pairing is None else {"inputs": {}, "derived": {
                "trades": len(pairing.trades), "open_positions": len(pairing.open_positions),
                "unmatched": len(pairing.unmatched), "not_computed": dict(pairing.not_computed)}},
            "trades": [] if pairing is None else [t.trade_id for t in pairing.trades],
            "rows": {"trade": 0, "open_position": 0, "stats_row": 0} if pairing is None else {
                "trade": len(pairing.trades), "open_position": len(pairing.open_positions),
                "stats_row": sum(1 for t in pairing.trades if t.stats) + len(pairing.unmatched)},
        }

    def seed_for(self, day):
        if self.seed_error:
            raise PairingError(self.seed_error)
        return self.seed

    def record_day(self, pairing, import_ids, seed):
        self.writes.append("record_day")
        self.days[pairing.day] = (pairing, import_ids, seed)
        return 1

    def has_current_import(self, day, kind):
        row = self._current(day, kind.value)
        return row is not None

    def has_chain_through(self, day):
        return any(d <= day for d in self.days)

    def effect_day(self, day, supersedes):
        return day

    def rebuild(self, day):
        self.writes.append("rebuild")
        self.rebuilt.append(day)
        return [day]

    def stated_difference(self, day):
        return None

    def record_stated_book(self, day, kind, positions, *, via, now=None, **kw):
        from cobalt.session import assert_writable

        assert_writable("drc.record_stated_book", target=day.isoformat(), now=now)
        if any(s.day == day and s.kind == kind for s in self.stated):
            raise ValueError(f"{day} {kind}: drc_stated_books #1 ({day}) is current — a restatement names it "
                             "with supersedes; nothing written")
        self.writes.append("record_stated_book")
        row = StatedBook(id=len(self.stated) + 1, day=day, kind=kind, positions=[],
                         book_sha256="0" * 64, via=via, reason="no-trade DRC")
        self.stated.append(row)
        return row


@pytest.fixture
def world(tmp_path, monkeypatch):
    """A `tmp_path` vault, the `DrcStore` double, the bytes writer's
    audit double, a constructed weekday calendar and a build that
    returns — the offline import place."""
    import importlib
    from datetime import timedelta

    from cobalt.drc import imports
    from cobalt.session.store import SessionBlockStore

    root = tmp_path / "vault"
    (root / "1 - Trading" / "5 - Review").mkdir(parents=True)
    monkeypatch.setenv("COBALT_VAULT_PATH", str(root))
    drc = _Drc()
    wstore = _WriteStore()
    monkeypatch.setattr(imports, "DrcStore", lambda: drc)
    monkeypatch.setattr(imports, "VaultWriteStore", lambda: wstore)
    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: None)

    def _prior(day: date) -> date:
        probe = day - timedelta(days=1)
        while probe.weekday() >= 5:
            probe -= timedelta(days=1)
        return probe

    monkeypatch.setattr(importlib.import_module("cobalt.daymode.propose"), "prior_trading_day", _prior)

    @dataclass
    class World:
        root: Path
        drc: _Drc
        wstore: _WriteStore

        def folder(self, day: date = D) -> Path:
            return self.root / DRC / day.isoformat()

    return World(root, drc, wstore)


def _files(folder: Path) -> dict[str, bytes]:
    return {p.name: p.read_bytes() for p in sorted(folder.iterdir()) if p.is_file()} if folder.exists() else {}


# ---------------------------------------------------------------------
# D2-2 — the bytes writer
# ---------------------------------------------------------------------


def _writer(now=None) -> tuple[VaultWriter, _WriteStore]:
    store = _WriteStore()
    kw = {"now": now} if now else {}
    return VaultWriter("drc.import", store=store, **kw), store


@pytest.mark.parametrize(
    "rel",
    [
        f"{DRC}/2001-01-02/../escape.md",
        f"{DRC}/../escape.md",
        "/etc/escape.md",
        f"{DRC}/not-a-date/x.md",
        f"{DRC}/2001-02-30/x.md",
        f"{DRC}/_reference/x.md",
        f"{DRC}/2001-01-02/sub/x.md",
        "1 - Trading/5 - Review/x.md",
        f"{DRC}/2001-01-02/",
    ],
)
def test_the_bytes_path_is_confined_to_a_dated_drc_imports_folder(tmp_path, rel):
    (tmp_path / "1 - Trading" / "5 - Review").mkdir(parents=True)
    writer, store = _writer()
    with pytest.raises(VaultWriteError):
        writer.write_import_bytes(tmp_path, rel, b"x")
    assert store.rows == []
    assert not (tmp_path / DRC).exists() or not any((tmp_path / DRC).rglob("*.md"))


def test_a_second_drop_of_one_name_gets_the_next_free_suffix_and_the_old_bytes_stay(tmp_path):
    (tmp_path / "1 - Trading" / "5 - Review").mkdir(parents=True)
    writer, _ = _writer()
    first = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a.md", b"one")
    second = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a.md", b"two")
    third = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a.md", b"three")
    bare = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a", b"four")
    bare2 = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a", b"five")
    assert (first.name, second.name, third.name, bare.name, bare2.name) == ("a.md", "a.1.md", "a.2.md", "a", "a.1")
    folder = tmp_path / DRC / "2001-01-02"
    assert _files(folder) == {"a.md": b"one", "a.1.md": b"two", "a.2.md": b"three", "a": b"four", "a.1": b"five"}
    assert all(w.action == "created" for w in (first, second, third, bare, bare2))


def test_the_write_row_carries_the_bytes_sha256(tmp_path):
    (tmp_path / "1 - Trading" / "5 - Review").mkdir(parents=True)
    writer, store = _writer()
    data = E1.read_bytes()
    out = writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/log.md", data)
    assert out.sha256 == hashlib.sha256(data).hexdigest()
    assert len(store.rows) == 1
    assert store.rows[0]["hash_after"] == out.sha256 and store.rows[0]["hash_before"] is None
    assert store.rows[0]["note"] == str(out.path) and store.rows[0]["writer"] == "drc.import"
    assert out.write_id == 1 and out.path.read_bytes() == data


def test_the_bytes_writer_is_refused_inside_market_reset(tmp_path, monkeypatch):
    from cobalt.session.store import SessionBlockStore

    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: None)
    (tmp_path / "1 - Trading" / "5 - Review").mkdir(parents=True)
    writer, store = _writer(now=lambda: RESET_ET)
    with pytest.raises(SessionBlocked):
        writer.write_import_bytes(tmp_path, f"{DRC}/2001-01-02/a.md", b"x")
    assert store.rows == [] and not (tmp_path / DRC).exists()


def test_the_text_commit_path_is_not_the_bytes_path():
    """FC5: `_commit` stays text-only; the bytes path is its own method."""
    import inspect

    from cobalt.vaultwrite import writer as writer_mod

    assert "write_import_bytes" not in inspect.getsource(writer_mod.VaultWriter._commit)
    assert "_commit(" not in inspect.getsource(writer_mod.VaultWriter.write_import_bytes)


def test_the_vault_names_the_drc_imports_location():
    from cobalt import vault

    assert vault.DRC_IMPORTS_REL == DRC


# ---------------------------------------------------------------------
# D2-3 — the import handler (R114, R17 (3) / (5))
# ---------------------------------------------------------------------


def _kinds(world) -> dict[str, str]:
    return {r["name"]: r["kind"] for r in world.drc.imports}


@pytest.mark.parametrize("t_name,s_name", [("t.md", "s.md"), ("t.csv", "s.csv"), ("t", "s"), ("t.md", "s")])
def test_each_file_is_kept_under_its_own_name_with_the_kind_its_header_shows(world, t_name, s_name):
    from cobalt.drc import imports

    result = imports.place(D, [(s_name, STATS.read_bytes()), (t_name, E1.read_bytes())])
    assert result.refused is None
    assert _kinds(world) == {t_name: "trading_log", s_name: "stats_log"}
    assert _files(world.folder()) == {t_name: E1.read_bytes(), s_name: STATS.read_bytes()}
    assert {f.name: f.kind for f in result.files} == {t_name: "trading_log", s_name: "stats_log"}


def test_one_file_at_a_time_each_by_its_header(world):
    from cobalt.drc import imports

    first = imports.place(D, [("whatever-name", STATS.read_bytes())])
    assert first.status_line == "waiting for: trading log"
    second = imports.place(D, [("another.csv", E1.read_bytes())])
    assert _kinds(world) == {"whatever-name": "stats_log", "another.csv": "trading_log"}
    assert second.state == "READY"


def test_the_request_carries_no_kind_field():
    import inspect

    from cobalt.drc import imports

    assert "kind" not in inspect.signature(imports.place).parameters


def test_a_note_in_the_drop_is_ignored_listed_and_not_stored(world):
    from cobalt.drc import imports

    result = imports.place(D, [("note.md", NOTE), ("t.md", E1.read_bytes())])
    lines = [f.text() for f in result.files]
    assert "ignored: note.md — header matches neither kind" in lines
    assert "note.md" not in _kinds(world) and "note.md" not in _files(world.folder())
    assert _kinds(world) == {"t.md": "trading_log"}


def test_two_trading_logs_refuse_the_whole_drop_naming_both(world):
    from cobalt.drc import imports

    result = imports.place(D, [("a.md", E1.read_bytes()), ("b.md", DAY1.read_bytes()), ("s.md", STATS.read_bytes())])
    assert result.refused == "FAILED: trading_log ambiguous — a.md, b.md"
    assert world.drc.imports == [] and _files(world.folder()) == {}
    assert world.wstore.rows == []


def test_a_partial_file_is_stored_parsed_loud_and_counts_as_placed(world):
    from cobalt.drc import imports

    partial = _drop_column(STATS.read_bytes(), "Commission")
    result = imports.place(D, [("t.md", E1.read_bytes()), ("s.md", partial)])
    row = next(r for r in world.drc.imports if r["name"] == "s.md")
    assert row["parse_status"] == "partial" and row["reason"] == "PARTIAL — missing: Commission"
    assert "s.md — stats_log PARTIAL — missing: Commission" in [f.text() for f in result.files]
    assert result.state == "READY"
    assert result.event is not None and result.event.partial == {str(row["id"]): ["Commission"]}


def test_the_same_bytes_dropped_for_two_dates_carry_each_drops_date(world):
    from cobalt.drc import imports

    imports.place(D, [("t.md", E1.read_bytes())])
    imports.place(D_NEXT, [("t.md", E1.read_bytes())])
    by_date = {r["import_date"]: r for r in world.drc.imports}
    assert set(by_date) == {D, D_NEXT}
    for day, row in by_date.items():
        assert row["executions"] and {e.time.date() for e in row["executions"]} == {day}


def test_a_failed_file_is_stored_with_its_reason_and_line(world):
    from cobalt.drc import imports

    lines = E1.read_bytes().splitlines(keepends=True)
    broken = lines[0] + lines[1].replace(b",S,", b",X,", 1) + b"".join(lines[2:])
    result = imports.place(D, [("t.md", broken)])
    line = next(f for f in result.files if f.name == "t.md")
    assert line.status == "failed" and line.line == 2
    assert line.text().startswith("FAILED: t.md — ") and "line 2" in line.text()
    assert world.drc.imports[0]["parse_status"] == "failed" and world.drc.imports[0]["executions"] == []


def test_a_screenshot_is_refused_by_its_header_before_anything(world):
    from cobalt.drc import imports

    for data in (b"", b"not an image"):
        result = imports.place(D, [("shot.png", data)], trade_key="T1")
        assert result.files[0].status == "failed"
        assert result.files[0].text().startswith("FAILED: shot.png — ")
    assert world.drc.imports == [] and _files(world.folder()) == {}


def test_a_screenshot_binding_has_no_store_path_on_this_tree_and_binds_nothing(world):
    from cobalt.drc import imports

    result = imports.place(D, [("shot.png", PNG)], trade_key="T1")
    assert result.files[0].status == "failed"
    assert "screenshot binding not built" in result.files[0].text()
    assert world.drc.imports == [] and _files(world.folder()) == {}


@pytest.mark.parametrize("action", ["place", "scan_folder", "no_trade"])
def test_market_reset_refuses_every_door_and_nothing_is_stored(world, action):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    before = _files(world.folder())
    if action == "place":
        result = imports.place(D, [("u.md", STATS.read_bytes())], now=RESET_ET)
    elif action == "scan_folder":
        result = imports.scan_folder(D.isoformat(), now=RESET_ET)
    else:
        result = imports.no_trade(D, now=RESET_ET)
    assert result.refused == "refused: market reset 20:00–21:00 — drop again after 21:00"
    assert world.drc.writes == [] and world.wstore.rows == []
    assert _files(world.folder()) == before


# ---------------------------------------------------------------------
# the event and the state (offline shape; the real rows are with-DB)
# ---------------------------------------------------------------------


def test_the_state_moves_waiting_trading_then_stats_then_ready(world):
    from cobalt.drc import imports

    assert imports.day_view(D).status_line == "waiting for: trading log"
    imports.place(D, [("t.md", E1.read_bytes())])
    assert imports.day_view(D).status_line == "waiting for: stats log"
    result = imports.place(D, [("s.md", STATS.read_bytes())])
    assert result.state == "READY"


def test_an_unstated_first_day_records_unpaired_and_the_build_is_not_built(world):
    from cobalt.drc import imports

    result = imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    pairing, ids, seed = world.drc.days[D]
    assert seed is None and "pairing" in pairing.not_computed
    assert result.status_line == "not computed — opening book not stated · state your opening book for 2001-01-02"
    assert world.drc.imports[0]["event_state"] == "failed"
    assert world.drc.imports[0]["event_error"] == "build not built (D3)"
    # pending → the [F-17] route (`record_day`) → running → failed (D2-3's order).
    assert world.drc.writes[-4:] == ["mark_event:pending", "record_day", "mark_event:running", "mark_event:failed"]


def test_a_seed_for_raise_fails_the_event_verbatim_and_keeps_the_files(world):
    from cobalt.drc import imports

    world.drc.seed_error = "2001-01-02: the prior trading day 2001-01-01 has no import and no no-trade record"
    result = imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    assert world.drc.imports[0]["event_state"] == "failed"
    assert world.drc.imports[0]["event_error"] == world.drc.seed_error
    assert D not in world.drc.days and len(world.drc.imports) == 2
    assert result.status_line == f"DRC build FAILED: seed — {world.drc.seed_error}"


def test_the_event_carries_the_import_ids_and_their_sha256s(world):
    from cobalt.drc import imports

    result = imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    t, s = world.drc.imports
    ev = result.event
    assert (ev.date, ev.import_id, ev.stats_import_id, ev.kind) == (D, t["id"], s["id"], "trades")
    assert ev.sha256s == {str(t["id"]): t["sha256"], str(s["id"]): s["sha256"]}
    assert ev.partial == {} and ev.screenshot_import_ids == []


# ---------------------------------------------------------------------
# D2-3b — hand-dropped files (R17 (2))
# ---------------------------------------------------------------------


def _snapshot_folder(folder: Path):
    return sorted(
        (p.relative_to(folder).as_posix(), p.read_bytes(), p.stat().st_mtime_ns)
        for p in folder.rglob("*")
        if p.is_file()
    )


def test_a_scan_imports_the_folder_and_writes_nothing_into_it(world):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "his-own-name.md").write_bytes(E1.read_bytes())
    (world.folder() / "journal.md").write_bytes(STATS.read_bytes())
    (world.folder() / "note.md").write_bytes(NOTE)
    before = _snapshot_folder(world.folder())
    result = imports.scan_folder(D.isoformat())
    assert _snapshot_folder(world.folder()) == before
    assert world.wstore.rows == []
    assert _kinds(world) == {"his-own-name.md": "trading_log", "journal.md": "stats_log"}
    row = next(r for r in world.drc.imports if r["name"] == "his-own-name.md")
    assert row["sha256"] == hashlib.sha256(E1.read_bytes()).hexdigest()
    assert "ignored: note.md — header matches neither kind" in [f.text() for f in result.files]


def test_a_second_scan_lists_already_imported(world):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    imports.scan_folder(D.isoformat())
    again = imports.scan_folder(D.isoformat())
    assert len(world.drc.imports) == 1
    assert "already imported: t.md" in [f.text() for f in again.files]


def test_an_upload_then_a_scan_is_not_imported_again(world):
    from cobalt.drc import imports

    imports.place(D, [("t.md", E1.read_bytes())])
    again = imports.scan_folder(D.isoformat())
    assert len(world.drc.imports) == 1
    assert "already imported: t.md" in [f.text() for f in again.files]


def test_a_new_file_of_a_kind_supersedes_the_current_one(world):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    imports.scan_folder(D.isoformat())
    (world.folder() / "t2.md").write_bytes(DAY1.read_bytes())
    imports.scan_folder(D.isoformat())
    first, second = world.drc.imports
    assert second["supersedes"] == first["id"] and second["name"] == "t2.md"


def test_two_new_files_of_one_kind_in_the_folder_are_refused_both_named(world):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "a.md").write_bytes(E1.read_bytes())
    (world.folder() / "b.md").write_bytes(DAY1.read_bytes())
    result = imports.scan_folder(D.isoformat())
    assert result.refused == "FAILED: trading_log ambiguous — a.md, b.md"
    assert world.drc.imports == []


def test_reference_sub_folders_and_non_date_folders_are_never_read(world, monkeypatch):
    from cobalt.drc import imports

    drc = world.root / DRC
    (drc / "_reference").mkdir(parents=True)
    (drc / "_reference" / "t.md").write_bytes(E1.read_bytes())
    (drc / "misc").mkdir()
    (drc / "misc" / "t.md").write_bytes(E1.read_bytes())
    world.folder().mkdir()
    (world.folder() / "sub").mkdir()
    (world.folder() / "sub" / "t.md").write_bytes(E1.read_bytes())
    opened: list[str] = []
    real = Path.read_bytes

    def spy(self):
        opened.append(str(self))
        return real(self)

    monkeypatch.setattr(Path, "read_bytes", spy)
    result = imports.scan_folder(D.isoformat())
    assert world.drc.imports == [] and result.files == []
    assert not any("_reference" in p or "/misc/" in p or "/sub/" in p for p in opened), opened


@pytest.mark.parametrize("bad", ["2001-13-40", "not-a-date", "_reference", "2001-01-02/..", "../2001-01-02"])
def test_a_scan_of_a_non_date_fails_and_reads_nothing(world, monkeypatch, bad):
    from cobalt.drc import imports

    opened: list[str] = []
    monkeypatch.setattr(Path, "iterdir", lambda self: opened.append(str(self)) or iter(()))
    result = imports.scan_folder(bad)
    assert result.refused is not None and result.refused.startswith("FAILED:")
    assert opened == [] and world.drc.imports == []


def test_a_scan_reaches_the_parse_only_through_place(world, monkeypatch):
    from cobalt.drc import imports

    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    calls: list[tuple] = []
    real = imports.place

    def spy(day, files, trade_key=None, **kw):
        calls.append((day, [n for n, _ in files], trade_key, kw.get("from_folder")))
        return real(day, files, trade_key, **kw)

    monkeypatch.setattr(imports, "place", spy)
    imports.scan_folder(D.isoformat())
    assert calls == [(D, ["t.md"], None, True)]


def test_the_same_bytes_give_the_same_rows_through_either_door(tmp_path, monkeypatch, world):
    from cobalt.drc import imports

    imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    uploaded = [{k: v for k, v in r.items() if k not in ("id", "supersedes")} for r in world.drc.imports]
    other = _Drc()
    monkeypatch.setattr(imports, "DrcStore", lambda: other)
    folder = world.root / DRC / D_NEXT.isoformat()
    folder.mkdir(parents=True)
    (folder / "t.md").write_bytes(E1.read_bytes())
    (folder / "s.md").write_bytes(STATS.read_bytes())
    imports.scan_folder(D_NEXT.isoformat())
    scanned = [{k: v for k, v in r.items() if k not in ("id", "supersedes")} for r in other.imports]
    for a, b in zip(uploaded, scanned):
        assert a.pop("import_date") == D and b.pop("import_date") == D_NEXT
        a_ex, b_ex = a.pop("executions"), b.pop("executions")
        assert [e.model_dump(exclude={"time"}) for e in a_ex] == [e.model_dump(exclude={"time"}) for e in b_ex]
        assert [e.time.time() for e in a_ex] == [e.time.time() for e in b_ex]
        assert a == b
    assert len(uploaded) == len(scanned) == 2


# ---------------------------------------------------------------------
# D2-3c — the no-trade action (offline shape)
# ---------------------------------------------------------------------


def test_no_trade_on_a_weekend_is_refused(world):
    from cobalt.drc import imports

    result = imports.no_trade(date(2001, 1, 6))
    assert result.refused == "refused: 2001-01-06 is not a market trading day"
    assert world.drc.stated == []


def test_no_trade_on_a_day_with_executions_is_refused_naming_the_count(world):
    from cobalt.drc import imports

    imports.place(D, [("t.md", E1.read_bytes())])
    n = len(world.drc.imports[0]["executions"])
    result = imports.no_trade(D)
    assert result.refused == f"refused: 2001-01-02 has a trading log with {n} executions — not a no-trade day"
    assert world.drc.stated == []


def test_no_trade_with_no_import_and_no_chain_is_stated_only(world):
    from cobalt.drc import imports

    result = imports.no_trade(D)
    assert [s.via for s in world.drc.stated] == ["drc_page"]
    assert world.drc.rebuilt == []
    assert result.message == "stated; 2001-01-02 has no import yet"


def test_no_trade_with_a_chain_rebuilds_and_waits_on_the_event_home(world):
    from cobalt.drc import imports

    world.drc.days[date(2001, 1, 1)] = object()
    result = imports.no_trade(D)
    assert world.drc.rebuilt == [D]
    assert result.message == "no-trade day recorded — its DRC build waits on the no-trade event home (ESCALATE X-NT)"


def test_a_second_no_trade_shows_the_stores_refusal_verbatim(world):
    from cobalt.drc import imports

    imports.no_trade(D)
    again = imports.no_trade(D)
    assert again.refused == (
        "2001-01-02 no_trade: drc_stated_books #1 (2001-01-02) is current — a restatement names it "
        "with supersedes; nothing written"
    )


# ---------------------------------------------------------------------
# D2-4 — the page (TestClient)
# ---------------------------------------------------------------------


@pytest.fixture
def page(world, monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module

    class _Cards:
        def for_date(self, day):
            return []

    monkeypatch.setattr(web_module, "AsetStore", lambda: _Cards())
    return TestClient(web_module.app)


def test_get_drc_writes_nothing(page, world):
    response = page.get("/drc", params={"date": D.isoformat()})
    assert response.status_code == 200
    assert world.drc.writes == [] and world.wstore.rows == []
    assert "waiting for: trading log" in response.text


def test_get_drc_shows_the_morning_line_state_your_book_when_none_is_stated(page, world):
    text = page.get("/drc", params={"date": D.isoformat()}).text
    assert "state your opening book for 2001-01-02 — until the form ships: cobalt drc state-book --opening 2001-01-02" in text


def test_get_drc_shows_a_seed_raise_verbatim_with_the_remedy(page, world):
    world.drc.seed_error = (
        "2001-01-03: the prior trading day 2001-01-02 has no import and no no-trade record, while "
        "2001-01-01 does — a skipped day would carry a phantom position"
    )
    text = page.get("/drc", params={"date": D_NEXT.isoformat()}).text
    assert "the prior trading day 2001-01-02 has no import and no no-trade record" in text
    assert "No prior DRC for 2001-01-02 — import it, record its no-trade DRC, or state your book" in text


def test_the_import_route_places_the_upload_with_no_kind_field(page, world):
    response = page.post(
        "/drc/import",
        data={"date": D.isoformat()},
        files=[("files", ("t.md", E1.read_bytes(), "text/markdown")),
               ("files", ("s", STATS.read_bytes(), "application/octet-stream"))],
    )
    assert response.status_code == 200, response.text
    assert _kinds(world) == {"t.md": "trading_log", "s": "stats_log"}


def test_the_scan_route_and_the_no_trade_route_call_the_one_pipeline(page, world):
    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    page.post("/drc/scan", data={"date": D.isoformat()})
    assert _kinds(world) == {"t.md": "trading_log"}
    response = page.post("/drc/no-trade", data={"date": date(2001, 1, 6).isoformat()})
    assert "refused: 2001-01-06 is not a market trading day" in response.text


def test_the_page_lists_folder_files_not_yet_imported(page, world):
    world.folder().mkdir(parents=True)
    (world.folder() / "t.md").write_bytes(E1.read_bytes())
    (world.folder() / "n.md").write_bytes(NOTE)
    text = page.get("/drc", params={"date": D.isoformat()}).text
    assert "in the folder, not imported: 2 — n.md, t.md" in text
    assert world.drc.imports == []


def test_the_upload_route_is_refused_inside_market_reset(page, world, monkeypatch):
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(clock_mod, "now_utc", lambda: RESET_ET)
    response = page.post(
        "/drc/import", data={"date": D.isoformat()}, files=[("files", ("t.md", E1.read_bytes(), "text/plain"))]
    )
    assert "refused: market reset 20:00–21:00 — drop again after 21:00" in response.text
    assert world.drc.imports == [] and _files(world.folder()) == {}


def test_a_bad_date_on_the_page_is_failed_never_guessed(page, world):
    response = page.get("/drc", params={"date": "2001-02-30"})
    assert "FAILED" in response.text
    assert world.drc.writes == []


def test_the_r51_line_renders_as_the_store_returns_it():
    """Text nodes keep the apostrophe of "<P>'s close" (seam (8): the
    line as returned); `<` / `&` are still escaped."""
    from cobalt.aset import drc_page
    from cobalt.drc.imports import DayView

    line = "stated book for 2001-01-03 differed from 2001-01-02's close: X-long-<b>&"
    page = drc_page.render(DayView(date=D_NEXT, stated_difference=line, status_line="waiting for: trading log"))
    assert "stated book for 2001-01-03 differed from 2001-01-02's close: X-long-&lt;b&gt;&amp;" in page


def test_the_existing_routes_are_still_served():
    from cobalt.aset import web as web_module

    paths = {getattr(r, "path", None) for r in web_module.app.routes}
    for path in ("/", "/size", "/fill", "/attest", "/settings/daily", "/settings/daily/apply",
                 "/drc", "/drc/import", "/drc/no-trade", "/drc/scan"):
        assert path in paths, path
