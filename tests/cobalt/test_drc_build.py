"""DRC D3 — THE BUILD AND THE NOTE, OFFLINE half (`prompts/2026-09-28/
10-drc-d3-build.md` `## E2`).

What runs here without a database:
- the build (`cobalt.drc.build`) over a CONSTRUCTED ROW SET: `_Store`, an
  in-memory double of the three `DrcStore` calls the build makes
  (`event_for`, `rows_for`, `record_build`). Its `drc_rows` are the rows
  the real store writes — `DrcStore._rows`, the store's own static row
  builder, over D1's fixtures paired by `pairing.build_day` — so no row
  shape here is invented. The real rows and the real event are proven
  WITH-DB in `test_drc_build_db.py`.
- every note in a `tmp_path` vault whose template is
  `tests/fixtures/drc/template_shape.md` (his template's SHAPE, L32 / L45);
  the audit rows in `test_replay_line.py`'s `MemoryWriteStore`.
- his strategies folder: constructed titles and slugs only (L32 / L45).

E3 / E6 / E8 are written here RED FIRST (the build does not exist at E2).
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Optional

import pytest

from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Kind, SeedBook
from cobalt.drc.pairing import FN_VERSION as PAIRING_FN, book_sha256, build_day
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

from test_drc_k2_experiments import _drop_column
from test_drc_store import D, D_NEXT, DAY1, E1, STATS
from test_replay_line import MemoryWriteStore

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
SHAPE = FIXTURES / "template_shape.md"
TEN_ET = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
REVIEW = "1 - Trading/5 - Review"
STRATEGIES = "1 - Trading/4 - Strategies"
DAILY = "1 - Trading/1- Daily Notes"
#: `daymode/drc.py`'s two headline regexes (`:116`, `:117`) — `[F-23]`:
#: no unit ever writes a line either one reads.
GRADE_RE = re.compile(r"^\s*[-*]?\s*(?:\*\*)?Grade(?:\*\*)?\s*[:|]\s*(.+)$")
GOAL_RE = re.compile(r"^\s*[-*]?\s*(?:\*\*)?Goal(?:\*\*)?\s*[:|]\s*(.+)$")
#: Constructed strategy titles (none is his): title -> `trade_def:` slug
#: (`example-…`, the repo's names rule, L31 / ADR-0008 D5).
TITLES = {"Alpha Setup": "example-alpha-setup", "Beta Setup": "example-beta-setup", "Omega Setup": "example-omega-setup"}


# ---------------------------------------------------------------------
# the constructed row set
# ---------------------------------------------------------------------


def _json(value):
    return json.loads(json.dumps(value, default=str))


class _Store:
    """The three `DrcStore` calls the build makes, in memory."""

    def __init__(self):
        self.views: dict[date, dict] = {}
        self.krows: dict[date, list[dict]] = {}
        self.build: dict[date, list[dict]] = {}
        self.recorded: list[date] = []

    def event_for(self, day):
        return copy.deepcopy(self.views[day])

    def rows_for(self, day):
        return copy.deepcopy([*self.krows.get(day, []), *self.build.get(day, [])])

    def record_build(self, day, rows):
        kinds = {r["kind"] for r in rows}
        assert kinds <= {"build_trade", "build_day"}, kinds
        self.build[day] = copy.deepcopy(list(rows))
        self.recorded.append(day)
        return len(rows)


def _import_row(i, kind, name, data, parsed, fills=0, trade_key=None):
    return dict(
        id=i, kind=kind, name=name, sha256=hashlib.sha256(data).hexdigest(), trade_key=trade_key,
        parse_status=parsed.result.outcome.value if parsed else "parsed",
        reason=parsed.result.reason if parsed else "", failed_line=None, supersedes=None, current=True,
        fills=fills,
    )


def _record(
    store: _Store,
    day: date = D,
    trading: Optional[bytes] = None,
    stats: Optional[bytes] = None,
    *,
    flat: bool = True,
    no_stats: bool = False,
    extra: Optional[dict] = None,
    shots: tuple[tuple[str, str], ...] = (),
    edit_trade=None,
):
    """Record `day` in `store` exactly as `DrcStore._rows` would, and return
    D2's event for it (`imports._event`, the one builder)."""
    from cobalt.drc import imports

    trading = E1.read_bytes() if trading is None else trading
    stats = None if no_stats else (STATS.read_bytes() if stats is None else stats)
    t = TradingLogSource().parse(trading, day, detect_kind("t.md", trading))
    s = None if stats is None else StatsLogSource().parse(stats, detect_kind("s.md", stats))
    seed = (
        SeedBook(source="stated", positions=[], stated_book_id=1, from_book_sha256=book_sha256([]))
        if flat else None
    )
    pairing = build_day(t, s, seed=[] if flat else None)
    ids = {Kind.TRADING_LOG: 1, **({Kind.STATS_LOG: 2} if s is not None else {})}
    krows = [
        dict(kind=k, ref=r, inputs=_json(i), derived=_json(dv), fn_version=PAIRING_FN)
        for k, r, i, dv in DrcStore._rows(pairing, ids, seed, None, extra or {})
    ]
    if edit_trade is not None:
        for row in krows:
            if row["kind"] == "trade":
                edit_trade(row["derived"])
    imports_ = [_import_row(1, "trading_log", "t.md", trading, t, fills=len(t.executions))]
    if s is not None:
        imports_.append(_import_row(2, "stats_log", "s.md", stats, s))
    for n, (name, key) in enumerate(shots, start=3):
        imports_.append(_import_row(n, "screenshot", name, name.encode(), None, trade_key=key))
    day_row = next(r for r in krows if r["kind"] == "day")
    seed_row = next((r for r in krows if r["kind"] == "seed"), None)
    trades = sorted(r["ref"] for r in krows if r["kind"] == "trade")
    store.views[day] = dict(
        import_id=1, event_id=10 + len(store.views), source="import", state="running", updated_at=None,
        error=None, note_path=None, stated_book_id=None, stated_book_sha256=None,
        seed=None if seed_row is None else {k: seed_row["inputs"].get(k) for k in (
            "source", "from_day", "from_book_sha256", "stated_book_id", "no_trade_id")},
        imports=imports_, day={"inputs": day_row["inputs"], "derived": day_row["derived"]}, trades=trades,
        rows={k: sum(1 for r in krows if r["kind"] == k) for k in ("trade", "open_position", "stats_row")},
    )
    store.krows[day] = krows
    return imports._event(day, store.views[day], imports._orphans(store.views[day]))


def _record_file_less(store: _Store, day: date = D_NEXT, *, statement: int = 5):
    """A FILE-LESS no-trade day (his `no_trade` statement, no file): the
    day row `DrcStore._rows` writes for it, and D2's event."""
    from cobalt.drc import imports
    from cobalt.drc.models import ImportResult, Outcome, ParsedTradingLog

    parsed = ParsedTradingLog(
        result=ImportResult(name="no-trade DRC", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED),
        import_date=day, executions=[],
    )
    seed = SeedBook(source="stated", positions=[], stated_book_id=1, from_book_sha256=book_sha256([]))
    pairing = build_day(parsed, None, seed=[])
    krows = [
        dict(kind=k, ref=r, inputs=_json(i), derived=_json(dv), fn_version=PAIRING_FN)
        for k, r, i, dv in DrcStore._rows(pairing, {}, seed, statement, {})
    ]
    day_row = next(r for r in krows if r["kind"] == "day")
    store.views[day] = dict(
        import_id=None, event_id=90, source="stated_book", state="running", updated_at=None, error=None,
        note_path=None, stated_book_id=statement, stated_book_sha256="a" * 64,
        seed={"source": "stated", "from_day": None, "from_book_sha256": book_sha256([]),
              "stated_book_id": 1, "no_trade_id": None},
        imports=[], day={"inputs": day_row["inputs"], "derived": day_row["derived"]}, trades=[],
        rows={"trade": 0, "open_position": 0, "stats_row": 0},
    )
    store.krows[day] = krows
    return imports._event(day, store.views[day], [])


# ---------------------------------------------------------------------
# the vault and the deps
# ---------------------------------------------------------------------


def _vault(tmp_path: Path, *, template: Optional[str] = None, titles: Optional[dict] = None) -> Path:
    root = tmp_path / "vault"
    for rel in ("5 - Templates", REVIEW, STRATEGIES, DAILY):
        (root / rel).mkdir(parents=True, exist_ok=True)
    (root / "5 - Templates" / "DRC.md").write_text(SHAPE.read_text() if template is None else template)
    for title, slug in (TITLES if titles is None else titles).items():
        _strategy(root, title, slug)
    return root


def _strategy(root: Path, title: str, slug: str) -> None:
    (root / STRATEGIES / f"{title}.md").write_text(f"---\ntrade_def: {slug}\nname: {title}\n---\nconstructed\n")


class _Settings:
    """`load_drc_settings`'s shape for the keys D3 reads."""

    def __init__(self, window=None, windows=None):
        from cobalt.settings.models import DrcGoalSettings, DrcLimitsSettings, DrcWindowsSettings

        self.limits = DrcLimitsSettings(card_match_window_minutes=window)
        self.windows = windows or DrcWindowsSettings()
        self.goal = DrcGoalSettings()


def _deps(store: _Store, root: Path, **over):
    from cobalt.drc import build

    cards = over.pop("cards", [])
    window = over.pop("window", None)
    values = dict(
        store=store,
        vault_root=root,
        cards=lambda day: list(cards),
        card_counts=lambda day: (len(cards), sum(1 for c in cards if c.get("status") == "FILLED")),
        drc_settings=lambda: _Settings(window),
        daily_stop=lambda: {"full": None, "half": None},
        risk_parameters=lambda cards: "no sheet-mode cards today",
        rules_block=lambda: "- [ ] constructed rule one #process",
        daily_note=lambda day: None,
        replay_result=lambda: None,
        write_store=MemoryWriteStore(),
        now=lambda: TEN_ET,
    )
    values.update(over)
    return build.BuildDeps(**values)


def _note(root: Path, day: date = D) -> Path:
    return root / REVIEW / f"DRC-{day.isoformat()}.md"


def _lines(path: Path) -> list[str]:
    return path.read_text().split("\n")


def _unit_body(path: Path, section: str, unit: str) -> list[str]:
    from cobalt.vaultwrite.markers import find_section

    lines = _lines(path)
    sec = find_section(lines, section)
    assert sec is not None, f"section {section} absent"
    assert unit in sec.units, f"unit {section}/{unit} absent: {list(sec.units)}"
    return sec.units[unit].body(lines)


def _outside_sections(text: str) -> list[str]:
    """Every line of the note that sits outside every Cobalt section."""
    from cobalt.vaultwrite.markers import all_sections

    lines = text.split("\n")
    inside: set[int] = set()
    for sec in all_sections(lines):
        inside |= set(range(sec.open_line, sec.close_line + 1))
    return [line for i, line in enumerate(lines) if i not in inside]


def _trade_id(symbol: str, store: _Store, day: date = D) -> str:
    return next(r["ref"] for r in store.krows[day] if r["kind"] == "trade" and r["ref"].startswith(f"{symbol}-"))


# ---------------------------------------------------------------------
# E3 — his template, every unit under its heading, twice
# ---------------------------------------------------------------------


def test_e3_every_unit_sits_under_its_heading_and_his_lines_stay_byte_identical_twice(tmp_path):
    """E3 (v2 `:193`): "his template with only the date token substituted,
    then the existing placements plus summary, reconcile, open-position,
    and voice units — every unit under its heading, no other `{{` token,
    his non-unit lines byte-identical". Built TWICE: the second build is
    idempotent (every write `unchanged`)."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store)
    deps = _deps(store, root)
    path = build.run_drc_build(event, deps=deps)
    assert Path(path) == _note(root)
    first = Path(path).read_text()
    assert "{{" not in first
    expected = SHAPE.read_text().replace("{{date:YYYY-MM-DD}}", D.isoformat()).split("\n")
    outside = _outside_sections(first)
    # His lines, byte-identical and in order; after them only the writer's
    # own two blank lines: the separator L28's end placement puts before the
    # appended `drc-rules` section (`writer.py:737`) and the file's final
    # newline (`_ensure_trailing_newline`).
    assert outside[: len(expected)] == expected
    assert outside[len(expected):] == ["", ""]
    lines = first.split("\n")

    def opens(section):
        return lines.index(f"<!-- cobalt:section {section} -->")

    assert opens("drc-summary") == lines.index(f"### {D.isoformat()}") + 1
    assert opens("drc-day") == lines.index("<!-- /cobalt:section drc-summary -->") + 1
    assert opens("drc-risk") == next(i for i, l in enumerate(lines) if l.startswith("### PnL on the day:")) + 1
    assert opens("drc-trades") == lines.index("### Catalyst + Set Up + Trades") + 1
    assert opens("drc-rules") > next(i for i, l in enumerate(lines) if l.startswith("###  Take all"))
    for section, unit in (
        ("drc-summary", "summary"), ("drc-day", "premarket"), ("drc-risk", "pnl"), ("drc-risk", "facts"),
        ("drc-risk", "risk_parameters"), ("drc-trades", "tickers"), ("drc-trades", "reconcile"),
        ("drc-rules", "rules_check"),
    ):
        _unit_body(Path(path), section, unit)
    for trade in store.views[D]["trades"]:
        _unit_body(Path(path), "drc-trades", f"trade-{trade}")
        assert _unit_body(Path(path), "drc-trades", f"voice-{trade}") == []

    again = build.run_drc_build(event, deps=deps)
    assert Path(again).read_text() == first


def test_a_template_line_with_another_token_fails_naming_the_line(tmp_path):
    """`[F-20]`: any `{{` other than the date token FAILS the build naming
    the line; nothing is written."""
    from cobalt.drc import build, template

    mutated = SHAPE.read_text().replace("shape line 130", "{{time}}")
    store = _Store()
    root = _vault(tmp_path, template=mutated)
    event = _record(store)
    with pytest.raises(template.TemplateError, match=r"line 130"):
        build.run_drc_build(event, deps=_deps(store, root))
    assert not _note(root).exists() and store.recorded == []


def test_the_template_date_token_is_the_only_substitution():
    from cobalt.drc import template

    text = "### {{date:YYYY-MM-DD}}\n![[x/{{date:YYYY-MM-DD}}#y]]\nplain {{ not }}\n"
    with pytest.raises(template.TemplateError, match="line 3"):
        template.render_template(text, D)
    assert template.render_template(text.replace("plain {{ not }}\n", ""), D) == (
        f"### {D.isoformat()}\n![[x/{D.isoformat()}#y]]\n"
    )


def test_the_placements_match_his_no_break_spaces():
    """His template carries U+00A0 in the PnL heading (`day:` U+00A0 U+0020
    `$XXXX`); the fixture carries U+0020 there (X-T note). The placement
    matches both."""
    from cobalt.drc import units

    for heading in ("### PnL on the day:  $XXXX", "### PnL on the day:  $XXXX"):
        assert units.PNL_PLACEMENT.locate(["x", heading, "y"]) == (2, 2)


# ---------------------------------------------------------------------
# the units' content
# ---------------------------------------------------------------------


def test_the_summary_and_the_pnl_unit_carry_gross_and_net(tmp_path):
    """R103 (O21) both gross and net on the summary line; R102 (O16) the
    PnL unit under `### PnL on the day:`. E1's four trades: gross
    −4.0 + 44.86 + 16.0 − 6.0 = 50.86 (the pairing's own figures); net
    −4.15 + 43.66 + 15.5 − 6.3 = 48.71 (the stats log's)."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    summary = "\n".join(_unit_body(_note(root), "drc-summary", "summary"))
    pnl = "\n".join(_unit_body(_note(root), "drc-risk", "pnl"))
    for text in (summary, pnl):
        assert "gross $50.86" in text and "net $48.71" in text, text
    assert "W/L: 2/2 (4 closed)" in summary
    assert "trades: 4" in summary
    assert "screenshots bound / trades: 0 / 4" in summary
    assert "rules" not in summary.lower()  # R101: no rules line


def test_no_unit_writes_a_line_the_0900_reader_reads(tmp_path):
    """`[F-23]`: no unit ever writes a line beginning `Grade:` or `Goal:`
    (the 09:00 reader's two regexes, `daymode/drc.py:116`–`:117`); the
    template's own lines are his and are not a unit's."""
    from cobalt.drc import build
    from cobalt.vaultwrite.markers import all_sections

    store = _Store()
    root = _vault(tmp_path)
    cards = [_card("AAA", "long", created=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc))]
    build.run_drc_build(_record(store), deps=_deps(store, root, cards=cards, window=30,
                                                   daily_note=lambda d: "Sleep: 7\n1% goal: size down\n"))
    lines = _lines(_note(root))
    for sec in all_sections(lines):
        for line in sec.body(lines):
            assert not GRADE_RE.match(line) and not GOAL_RE.match(line), line


def test_the_premarket_block_reads_the_four_keys_and_nothing_else(tmp_path):
    """R102 (O11): `Sleep:` / `Readiness:` / `RHR:` / `1% goal:` from the
    daily note; meditated / tone / hotkey render `not given`; a key he left
    blank renders `not given` (A25)."""
    from cobalt.drc import build

    daily = "Sleep: 7h\nReadiness: 81\nRHR:\n1% goal: one clean A setup\nMeditated: yes\n"
    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root, daily_note=lambda d: daily))
    (line,) = _unit_body(_note(root), "drc-day", "premarket")
    assert line == (
        "premarket — sleep: 7h · readiness: 81 · RHR: not given · 1% goal: one clean A setup · "
        "meditated: not given · tone: not given · hotkey: not given"
    )


def test_a_rebuild_upserts_keeps_his_voice_text_and_lets_his_edit_win(tmp_path):
    """v2 `:82` / T6 / R99: a re-build upserts every Cobalt unit in place;
    his text in a voice unit is never rewritten (create-once); a Cobalt
    line he changed WINS and is recorded as an override (L28)."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store)
    deps = _deps(store, root)
    build.run_drc_build(event, deps=deps)
    path = _note(root)
    trade = _trade_id("AAA", store)
    voice = f"<!-- cobalt:unit voice-{trade} -->"
    text = path.read_text().replace(voice, voice + "\nmy read: patient entry")
    text = text.replace("trades: 4", "trades: 4 (his note)")
    path.write_text(text)
    build.run_drc_build(event, deps=deps)
    after = path.read_text()
    assert _unit_body(path, "drc-trades", f"voice-{trade}") == ["my read: patient entry"]
    assert "trades: 4 (his note)" in after
    assert deps.write_store.overrides, "his edit to a Cobalt line is an override row"


def test_a_file_less_no_trade_day_gets_the_no_trade_unit_and_his_blank_unit(tmp_path):
    """R93: the no-trade event → `drc-day/no_trade` (date, "no trades",
    cards written that day) and HIS blank `drc-day/voice-no-trades` under
    `### Why no trades today:`, directly under the summary; no trade
    block. Created once: a re-build never rewrites his text."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record_file_less(store)
    assert event.kind == "no_trade" and event.stated_book_id == 5
    cards = [_card("ZZZ", "long", created=datetime(2001, 1, 3, 15, 0, tzinfo=timezone.utc))]
    deps = _deps(store, root, cards=cards)
    path = Path(build.run_drc_build(event, deps=deps))
    assert path == _note(root, D_NEXT)
    body = _unit_body(path, "drc-day", "no_trade")
    assert body == [f"no trades — {D_NEXT.isoformat()} · cards written: 1", "### Why no trades today:"]
    assert _unit_body(path, "drc-day", "voice-no-trades") == []
    lines = _lines(path)
    assert lines.index("<!-- cobalt:section drc-day -->") == lines.index("<!-- /cobalt:section drc-summary -->") + 1
    trades = _unit_body(path, "drc-trades", "tickers")
    assert trades == ["trades: 0 — a no-trade day"]
    marker = "<!-- cobalt:unit voice-no-trades -->"
    path.write_text(path.read_text().replace(marker, marker + "\nquiet tape, nothing met the plan"))
    build.run_drc_build(event, deps=deps)
    assert _unit_body(path, "drc-day", "voice-no-trades") == ["quiet tape, nothing met the plan"]


def test_the_first_check_refuses_an_event_that_does_not_match_the_day_row(tmp_path):
    """D3-2's first check: a file-less event whose `stated_book_id` is not
    the day row's `inputs.no_trade_id` FAILS and writes nothing."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record_file_less(store)
    wrong = event.model_copy(update={"stated_book_id": 6})
    with pytest.raises(build.BuildError, match="no_trade_id"):
        build.run_drc_build(wrong, deps=_deps(store, root))
    assert not _note(root, D_NEXT).exists() and store.recorded == []


def test_an_unpaired_day_says_pairing_not_computed_and_never_no_trades(tmp_path):
    """L1: a day whose `day` row carries `not_computed.pairing` → the
    summary says `pairing not computed — <the stored reason>`, every
    trade-derived unit renders `not computed — <reason>`; nothing reads
    the empty trade list as "no trades"."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store, flat=False)
    build.run_drc_build(event, deps=_deps(store, root))
    path = _note(root)
    summary = _unit_body(path, "drc-summary", "summary")
    assert "pairing not computed — opening book not stated" in summary
    assert _unit_body(path, "drc-trades", "tickers") == ["trades: not computed — opening book not stated"]
    assert _unit_body(path, "drc-risk", "pnl") == ["PnL: not computed — opening book not stated"]
    text = path.read_text()
    assert "no trades" not in text and "trades: 0" not in text


def test_every_row_the_note_renders_is_stored_with_its_inputs_and_fn_version(tmp_path):
    """L57: `record_build` stores `build_trade` (one per trade id) and
    `build_day` rows with `inputs` + `derived` + `fn_version` =
    `drc.build/1`; the card snapshot is in the inputs (`[F-19]`)."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    card = _card("AAA", "long", created=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc))
    build.run_drc_build(_record(store), deps=_deps(store, root, cards=[card], window=30))
    rows = store.build[D]
    assert build.FN_VERSION == "drc.build/1"
    assert {r["fn_version"] for r in rows} == {"drc.build/1"}
    assert sorted(r["ref"] for r in rows if r["kind"] == "build_trade") == store.views[D]["trades"]
    (day_row,) = [r for r in rows if r["kind"] == "build_day"]
    assert day_row["ref"] == "build"
    aaa = next(r for r in rows if r["ref"] == _trade_id("AAA", store))
    assert aaa["inputs"]["card"]["id"] == card["id"] and aaa["inputs"]["card"]["stop"] == "49.9"
    assert aaa["inputs"]["window_minutes"] == 30
    assert aaa["derived"]["card"]["card_id"] == card["id"]
    assert "strategy_titles" in aaa["inputs"]


# ---------------------------------------------------------------------
# card match (D4's window)
# ---------------------------------------------------------------------


def _card(ticker, direction, *, created, cid=41, stop="49.9", sheet="full", status="FILLED"):
    return dict(
        id=cid, created_at=created, session="rth", account_mode="live", ticker=ticker, grade="A",
        direction=direction, sheet_mode=sheet, risk_budget=Decimal("60"), entry=Decimal("50.2"),
        stop=Decimal(stop), per_share_risk=Decimal("0.3"), shares=200, used_risk=Decimal("60"),
        state="FILLED", state_at=created, status=status, filled_at=None, actual_fill=None,
        recomputed_shares=None, recomputed_used_risk=None, share_delta=None, distance_change_pct=None,
    )


def test_an_unset_window_matches_no_card_loudly(tmp_path):
    """D4's `limits.card_match_window_minutes` unset → every trade
    `card: not matched (window not given)` — never a guessed window."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    card = _card("AAA", "long", created=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc))
    build.run_drc_build(_record(store), deps=_deps(store, root, cards=[card]))
    block = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('AAA', store)}")
    assert "  - card: not matched (window not given)" in block


def test_the_nearest_prior_card_inside_the_window_is_the_trades_card(tmp_path):
    """Same ticker + direction, created at or before the first fill,
    within the window; the nearest one wins; a later card is not it."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    early = _card("AAA", "long", created=datetime(2001, 1, 2, 14, 50, tzinfo=timezone.utc), cid=40)
    near = _card("AAA", "long", created=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc), cid=41)
    later = _card("AAA", "long", created=datetime(2001, 1, 2, 15, 20, tzinfo=timezone.utc), cid=42)
    short = _card("AAA", "short", created=datetime(2001, 1, 2, 15, 14, tzinfo=timezone.utc), cid=43)
    build.run_drc_build(_record(store), deps=_deps(store, root, cards=[early, near, later, short], window=30))
    block = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('AAA', store)}")
    assert any(line.startswith("  - card: #41 A long · sheet full") for line in block), block
    ccc = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('CCC', store)}")
    assert "  - card: none" in ccc


def test_the_card_snapshot_survives_a_later_card_edit(tmp_path):
    """`[F-19]`: the card fields a figure used are snapshotted into the
    row's inputs at build time; a later edit of the card (a re-read of
    `aset_sizings`) does not move the stored figure."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    card = _card("AAA", "long", created=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc))
    build.run_drc_build(_record(store), deps=_deps(store, root, cards=[card], window=30))
    stored = copy.deepcopy(store.build[D])
    card["stop"] = Decimal("48.0")
    assert store.build[D] == stored


# ---------------------------------------------------------------------
# E8 — a vanished trade: its block goes, his voice unit stays `orphaned`
# ---------------------------------------------------------------------


def test_e8_a_vanished_trades_voice_unit_stays_with_one_orphaned_line(tmp_path):
    """E8 (v2 `:198`): "Two builds, a trade removed, text in
    `drc-trades/voice-<trade_id>`. Pass: the voice unit still there with
    `orphaned`, derived block gone." CCC is dropped from the second file."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    path = _note(root)
    ccc = _trade_id("CCC", store)
    voice = f"<!-- cobalt:unit voice-{ccc} -->"
    path.write_text(path.read_text().replace(voice, voice + "\nmy CCC answer"))
    without = b"\n".join(l for l in E1.read_bytes().split(b"\n") if b",CCC," not in l)
    stats = b"\n".join(l for l in STATS.read_bytes().split(b"\n") if b",CCC," not in l)
    event = _record(store, trading=without, stats=stats)
    assert ccc not in store.views[D]["trades"]
    build.run_drc_build(event, deps=_deps(store, root))
    assert _unit_body(path, "drc-trades", f"voice-{ccc}") == ["my CCC answer"]
    assert _unit_body(path, "drc-trades", f"trade-{ccc}") == [
        f"orphaned — trade {ccc} is not in the current trading log"]
    lines = _lines(path)
    at = lines.index(voice)
    assert lines[at - 2] == f"orphaned — trade {ccc} is not in the current trading log"


# ---------------------------------------------------------------------
# D3-2r — the re-paired days
# ---------------------------------------------------------------------


def test_every_re_paired_date_is_rebuilt_in_date_order(tmp_path):
    """v3 `[F-03]` note half: after the event's day, each date in its
    `derived.repaired` is built again, in date order, with the SAME
    function; his voice units untouched."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    later = date(2001, 1, 4)
    _record(store, D_NEXT, trading=DAY1.read_bytes(), no_stats=True)
    _record(store, later, trading=DAY1.read_bytes(), no_stats=True)
    event = _record(store, D, extra={"repaired": [later.isoformat(), D_NEXT.isoformat()]})
    build.run_drc_build(event, deps=_deps(store, root))
    assert store.recorded == [D, D_NEXT, later]
    assert _note(root, D_NEXT).exists() and _note(root, later).exists()


def test_a_note_failure_on_a_re_paired_date_fails_naming_it_and_stops(tmp_path, monkeypatch):
    """D3-2r: a note failure on the first re-paired date → the build
    raises naming the note and the date, the later date NOT attempted
    and named `not rebuilt: <dates>` — the database stays as K2 left it."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    later = date(2001, 1, 4)
    _record(store, D_NEXT, trading=DAY1.read_bytes(), no_stats=True)
    _record(store, later, trading=DAY1.read_bytes(), no_stats=True)
    event = _record(store, D, extra={"repaired": [D_NEXT.isoformat(), later.isoformat()]})
    blocker = _note(root, D_NEXT)
    blocker.mkdir()  # a directory where the note would be: its write fails
    with pytest.raises(build.BuildError) as failed:
        build.run_drc_build(event, deps=_deps(store, root))
    text = str(failed.value)
    assert D_NEXT.isoformat() in text and str(blocker) in text
    assert f"not rebuilt: {later.isoformat()}" in text
    assert store.recorded[:1] == [D] and later not in store.recorded
    assert not _note(root, later).exists()


def test_a_not_re_paired_date_is_named_in_the_summary_and_its_note_untouched(tmp_path):
    """D3-2r: a date in `derived.not_repaired` is NOT rebuilt; the event
    day's summary names it with the stored reason."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    reason = f"{D} has pairing not computed — its open positions are unknown"
    event = _record(store, D, extra={"repaired": [], "not_repaired": [{"day": D_NEXT.isoformat(), "reason": reason}]})
    build.run_drc_build(event, deps=_deps(store, root))
    summary = _unit_body(_note(root), "drc-summary", "summary")
    assert f"not re-paired: {D_NEXT.isoformat()} — {reason}" in summary
    assert store.recorded == [D] and not _note(root, D_NEXT).exists()


# ---------------------------------------------------------------------
# D3-2b — playbook → setup, one-to-one (R116 / R117, 09-23 R17 (1))
# ---------------------------------------------------------------------


def _resolved(names, root):
    from cobalt.drc.playbooks import resolve_playbooks

    return [r.text for r in resolve_playbooks(names, root)]


@pytest.mark.parametrize("name", ["Alpha Setup Long", "Alpha Setup short", "Alpha Setup LONG", "Alpha Setup"])
def test_a_name_equal_to_a_title_after_one_side_strip_is_that_setup(tmp_path, name):
    assert _resolved([name], _vault(tmp_path)) == [f"{name} → example-alpha-setup"]


def test_the_side_is_stripped_once_and_only_as_a_whole_word(tmp_path):
    root = _vault(tmp_path)
    assert _resolved(["Alpha Setup Long Long"], root) == ["unmapped: Alpha Setup Long Long"]
    _strategy(root, "Alpha Setup Long", "example-alpha-setup-long")
    assert _resolved(["Alpha Setup Long Long"], root) == ["Alpha Setup Long Long → example-alpha-setup-long"]
    assert _resolved(["Alpha SetupLong", "Alpha Setup Longer", "Alpha Setp Long"], root) == [
        "unmapped: Alpha SetupLong", "unmapped: Alpha Setup Longer", "unmapped: Alpha Setp Long"]


def test_a_case_only_difference_is_unmapped(tmp_path):
    """09-23 R17 (1): EXACT, case-sensitive title equality."""
    assert _resolved(["alpha setup Long"], _vault(tmp_path)) == ["unmapped: alpha setup Long"]


def test_two_names_on_one_trade_render_both_in_order(tmp_path):
    """R114: every name, in D1's order; nothing picks one. E1's AAA row
    carries two constructed names."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    block = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('AAA', store)}")
    assert "  - playbooks: Alpha Setup Long → example-alpha-setup, Beta Setup Long → example-beta-setup" in block
    omega = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('BBB', store)}")
    summary = _unit_body(_note(root), "drc-summary", "summary")
    assert any(l.startswith("  - playbooks: ") for l in omega)
    # Gamma Setup Long + Delta Pattern Short have no title: 2 unmapped names.
    assert "unmapped playbooks: 2" in summary


def test_a_bad_trade_def_is_unmapped_with_the_slug_error_text(tmp_path):
    from cobalt.taxonomy.slug import SlugError, validate_slug

    root = _vault(tmp_path, titles={"Gamma Setup": "Bad_Slug"})
    with pytest.raises(SlugError) as err:
        validate_slug("Bad_Slug", where=str(root / STRATEGIES / "Gamma Setup.md"))
    assert _resolved(["Gamma Setup Long"], root) == [f"unmapped: Gamma Setup Long — note Gamma Setup: {err.value}"]


def test_an_unreadable_strategies_folder_unmaps_every_name_and_the_build_is_done(tmp_path):
    from cobalt.drc import build

    root = _vault(tmp_path)
    for p in (root / STRATEGIES).iterdir():
        p.unlink()
    (root / STRATEGIES).rmdir()
    assert _resolved(["Alpha Setup Long"], root) == [
        "unmapped: Alpha Setup Long — strategies folder not readable"]
    store = _Store()
    path = build.run_drc_build(_record(store), deps=_deps(store, root))
    summary = _unit_body(Path(path), "drc-summary", "summary")
    assert "unmapped playbooks: 5 — strategies folder not readable" in summary


def test_a_title_added_between_two_builds_maps_on_the_second(tmp_path):
    """The titles are read AT BUILD TIME (L32 / L45): no code change."""
    root = _vault(tmp_path, titles={})
    assert _resolved(["Alpha Setup Long"], root) == ["unmapped: Alpha Setup Long"]
    _strategy(root, "Alpha Setup", "example-alpha-setup")
    assert _resolved(["Alpha Setup Long"], root) == ["Alpha Setup Long → example-alpha-setup"]


def test_only_top_level_md_files_are_titles(tmp_path):
    root = _vault(tmp_path, titles={})
    nested = root / STRATEGIES / "sub"
    nested.mkdir()
    (nested / "Alpha Setup.md").write_text("---\ntrade_def: example-alpha-setup\n---\n")
    (root / STRATEGIES / "Alpha Setup.txt").write_text("---\ntrade_def: example-alpha-setup\n---\n")
    assert _resolved(["Alpha Setup"], root) == ["unmapped: Alpha Setup"]


def test_no_constructed_title_is_in_the_code():
    """No mapping table, no committed list (L2 / L32): the constructed
    titles appear nowhere under `src/cobalt/drc`."""
    src = Path(__file__).resolve().parents[2] / "src" / "cobalt" / "drc"
    hits = [p for p in src.rglob("*.py") for t in [*TITLES, "Gamma Setup", "Delta Pattern"] if t in p.read_text()]
    assert hits == []


# ---------------------------------------------------------------------
# 09-23 R17 (4) the stop; R17 (5) the partial file
# ---------------------------------------------------------------------


def test_the_stop_is_the_stats_rows_stop_or_not_given(tmp_path):
    """R17 (4): ONE `stop:` line = the stats row's `stop`, never computed
    from the dollar-risk column, prices or shares; `None` → `stop: not
    given`. E1 carries no stop column (every row `None`, its `Trade Risk`
    column set) — then a constructed stop renders as-is."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    for trade in store.views[D]["trades"]:
        block = _unit_body(_note(root), "drc-trades", f"trade-{trade}")
        assert [l for l in block if l.startswith("  - stop:")] == ["  - stop: not given"]

    def with_stop(derived):
        if derived["symbol"] == "CCC" and derived.get("stats"):
            derived["stats"]["stop"] = "79.95"

    store2 = _Store()
    root2 = _vault(tmp_path / "second")
    build.run_drc_build(_record(store2, edit_trade=with_stop), deps=_deps(store2, root2))
    block = _unit_body(_note(root2), "drc-trades", f"trade-{_trade_id('CCC', store2)}")
    assert [l for l in block if l.startswith("  - stop:")] == ["  - stop: 79.95"]


def test_a_partial_stats_log_is_named_first_and_its_values_are_not_computed(tmp_path):
    """R17 (5): the DRC is built; the summary's FIRST line is `PARTIAL —
    missing: Net P&L · stats_log file s.md`; every value that column feeds
    reads `not computed — missing: Net P&L` (never 0, never blank)."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store, stats=_drop_column(STATS.read_bytes(), "Net P&L"))
    assert event.partial == {"2": ["Net P&L"]}
    build.run_drc_build(event, deps=_deps(store, root))
    summary = _unit_body(_note(root), "drc-summary", "summary")
    assert summary[0] == "PARTIAL — missing: Net P&L · stats_log file s.md"
    assert "net not computed — missing: Net P&L" in "\n".join(summary)
    block = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('AAA', store)}")
    assert any("net not computed — missing: Net P&L" in l for l in block), block


def test_a_partial_trading_log_is_named_first(tmp_path):
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store, trading=_drop_column(E1.read_bytes(), "Route"))
    assert event.partial == {"1": ["Route"]}
    build.run_drc_build(event, deps=_deps(store, root))
    summary = _unit_body(_note(root), "drc-summary", "summary")
    assert summary[0] == "PARTIAL — missing: Route · trading_log file t.md"


def test_no_partial_file_no_partial_line(tmp_path):
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    assert not any(l.startswith("PARTIAL") for l in _lines(_note(root)))


# ---------------------------------------------------------------------
# the vault root, the CLI, the retirement
# ---------------------------------------------------------------------


def test_the_default_vault_root_is_the_dev_vault_never_his(monkeypatch):
    """THE DEV LANE: with no override the build's root is
    `resolve_vault_path()` → `configs/dev/vault.yaml` → the dev vault (a
    read; nothing is written)."""
    from cobalt.drc import build
    from cobalt.vault import resolve_vault_path

    monkeypatch.delenv("COBALT_VAULT_PATH", raising=False)
    monkeypatch.setenv("COBALT_ENV", "dev")
    root = build.default_vault_root()
    assert root == resolve_vault_path() == Path("~/dev-vault-cobalt").expanduser().resolve()
    assert root != Path("/Users/cobalt/Vault/Think")


def test_cobalt_drc_build_joins_k1s_group_and_prefill_drc_is_gone(monkeypatch, capsys):
    """D3-4 / seam (6): `build` is a subcommand of K1's ONE `drc` group
    (L3); `prefill drc` is retired with its job constant (F39)."""
    from cobalt.drc import cli as drc_cli
    from cobalt.prefill import cli as prefill_cli

    parser = argparse.ArgumentParser(prog="cobalt")
    sub = parser.add_subparsers(dest="group")
    drc_cli.add_parser(sub)
    group = sub.choices["drc"]
    commands = next(a for a in group._actions if isinstance(a, argparse._SubParsersAction))
    assert sorted(commands.choices) == ["build", "state-book"]
    args = parser.parse_args(["drc", "build", "--date", "2001-01-02", "--dry-run"])
    assert (args.date, args.dry_run, args.no_trades) == (D, True, False)
    assert not hasattr(prefill_cli, "DRC_JOB") and not hasattr(prefill_cli, "_run_drc")
    monkeypatch.setattr("sys.argv", ["prefill", "drc"])
    with pytest.raises(SystemExit) as out:
        prefill_cli.main()
    assert out.value.code == 2 and "invalid choice: 'drc'" in capsys.readouterr().err


def test_the_cli_dry_run_writes_nothing_and_prints_the_units_and_rows(tmp_path, capsys):
    from cobalt.drc import cli as drc_cli

    store = _Store()
    root = _vault(tmp_path)
    _record(store)
    args = argparse.Namespace(date=D, dry_run=True, no_trades=False)
    drc_cli.cmd_build(args, deps=_deps(store, root))
    out = capsys.readouterr().out
    assert "DRY RUN" in out and "drc-summary/summary" in out and "build_day build" in out
    assert not _note(root).exists() and store.recorded == []


def test_the_retired_files_are_gone():
    """`[F-22]` / `[F-28]`: the 15:40 plist and the repo template left git
    in THIS deploy; the job row and its reader label left `jobs.yaml`."""
    repo = Path(__file__).resolve().parents[2]
    assert not (repo / "ops" / "com.cobalt.prefill-drc.plist").exists()
    assert not (repo / "configs" / "cobalt" / "templates" / "drc.md.j2").exists()
    assert "com.cobalt.prefill-drc" not in (repo / "configs" / "cobalt" / "jobs.yaml").read_text()


# ---------------------------------------------------------------------
# D3-3 — the 21:10 miss line when the note is absent; E6
# ---------------------------------------------------------------------


def test_an_absent_note_at_2110_stores_the_line_inputs_and_ends_green():
    """`[F-24]`: note absent at 21:10 → `line_step` does not raise and
    creates nothing: it stores the exact `render_line` arguments on the
    replay run (`job.result.line_inputs`), records `line: pending (no
    DRC)`, and the run ends green."""
    from cobalt.replay.runner import run_nightly

    from test_replay_runner import DAY, fake_deps

    deps, calls = fake_deps(drc_missing=True)
    result = run_nightly(DAY, dry_run=False, deps=deps)
    assert result.line_action == "pending (no DRC)"
    assert result.failed_step is None and "line" in result.steps_done
    assert not any(c.startswith("writer") for c in calls) and not deps.drc.exists()
    blob = result.job_result()["line_inputs"]
    assert blob["trade_date"] == DAY.isoformat()
    assert set(blob) >= {"card_rows", "mover_rows", "settings", "formation_replay", "input_stale",
                         "formation_rows", "formation_suppressed", "formation_input_stale", "formation_cut"}


def test_e6_the_stored_blob_re_renders_the_in_memory_line_byte_for_byte():
    """E6 (v2 `:196`, grok): "After a 21:10 run with no note, re-render
    `render_line` from the stored argument blob only. Same bytes as that
    run's in-memory render: T3 holds." The blob goes through JSON exactly
    as `job.result` is stored."""
    from cobalt.replay.line import render_stored
    from cobalt.replay.runner import run_nightly

    from test_replay_runner import DAY, fake_deps

    deps, _ = fake_deps(drc_missing=True)
    result = run_nightly(DAY, dry_run=False, deps=deps)
    (printed,) = [line for line in deps.printed if line.startswith("line: pending (no DRC) — ")]
    in_memory = printed.removeprefix("line: pending (no DRC) — ")
    stored = json.loads(json.dumps(result.job_result()))["line_inputs"]
    assert render_stored(stored) == in_memory


def test_the_build_writes_the_pending_miss_line_from_the_stored_blob(tmp_path):
    """The build, after `drc-rules` exists, is the ONLY later caller of
    `render_line` + `write_miss_line` for the stored blob (writer identity
    `replay.nightly`); a blob for another date, or none → the summary says
    `miss line: pending (replay inputs not stored)` and no unit is written."""
    from cobalt.drc import build
    from cobalt.replay.line import render_stored

    blob = {
        "trade_date": D.isoformat(), "card_rows": [{"excluded_by": "unarmed", "cf_r": "-1.0"}],
        "mover_rows": [], "settings": {"top_n": 20, "min_move_pct": "10"}, "formation_replay": "unavailable",
        "input_stale": 0, "formation_rows": [], "formation_suppressed": 0, "formation_input_stale": 0,
        "formation_cut": None,
    }
    store = _Store()
    root = _vault(tmp_path)
    replay = {"trade_date": D.isoformat(), "line_action": "pending (no DRC)", "line_inputs": blob}
    deps = _deps(store, root, replay_result=lambda: replay)
    build.run_drc_build(_record(store), deps=deps)
    assert _unit_body(_note(root), "drc-misses", "miss_line") == [render_stored(blob)]
    lines = _lines(_note(root))
    assert lines.index("<!-- cobalt:section drc-misses -->") == lines.index("<!-- /cobalt:section drc-rules -->") + 1
    assert any(r.get("writer") == "replay.nightly" and r.get("section") == "drc-misses" for r in deps.write_store.rows)

    other = _Store()
    root2 = _vault(tmp_path / "other")
    stale = {**replay, "trade_date": "2000-12-29", "line_inputs": {**blob, "trade_date": "2000-12-29"}}
    build.run_drc_build(_record(other), deps=_deps(other, root2, replay_result=lambda: stale))
    assert "miss line: pending (replay inputs not stored)" in _unit_body(_note(root2), "drc-summary", "summary")
    assert "<!-- cobalt:section drc-misses -->" not in _note(root2).read_text()


# ---------------------------------------------------------------------
# D3-6 — the S2 smoke's DRC rows are conditional on the event
# ---------------------------------------------------------------------


def _smoke_ctx():
    from test_smoke import ctx

    return ctx()


@pytest.mark.parametrize(
    "state, note, expected",
    [(None, False, "KNOWN"), ("failed", True, "FAIL"), ("done", False, "FAIL"), ("done", True, "PASS")],
)
def test_the_miss_line_smoke_row_is_pending_fail_or_pass_by_the_event(tmp_path, state, note, expected):
    """`[F-25]` (R103 O18): K10.1 → pending (KNOWN) when no DRC event
    exists for the date; FAIL when the event is `failed`, or `done`
    without the note and its `drc-misses` markers; PASS when `done` and
    both are present. Nothing requires 15:41."""
    from cobalt.smoke import checks
    from cobalt.smoke.config import SUITES_DIR, load_suite

    from test_smoke import deps as smoke_deps
    from test_smoke import rows

    check = {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}["K10.1"]
    path = tmp_path / "DRC.md"
    if note:
        path.write_text("<!-- cobalt:section drc-misses -->\n<!-- cobalt:unit miss_line -->\nMisses\n"
                        "<!-- /cobalt:unit miss_line -->\n<!-- /cobalt:section drc-misses -->\n")
    answer = rows(["event_state", "event_error"], *([] if state is None else [[state, "x" if state == "failed" else None]]))
    present = rows(["present"], [True])  # D3-9: the `user.drc_events` guard answers first
    out = checks.evaluate(check, _smoke_ctx(), smoke_deps(
        read_rows=lambda statement, side: present if "to_regclass" in statement else answer,
        drc_note_path=lambda day: path,
        read_text=lambda p: Path(p).read_text()))
    assert out.verdict.value == expected, out.detail


@pytest.mark.parametrize(
    "state, writes, expected",
    [(None, 0, "KNOWN"), ("failed", 0, "FAIL"), ("done", 0, "FAIL"), ("done", 1, "PASS")],
)
def test_the_miss_line_write_smoke_row_is_conditional_too(state, writes, expected):
    from cobalt.smoke import checks
    from cobalt.smoke.config import SUITES_DIR, load_suite

    from test_smoke import deps as smoke_deps
    from test_smoke import rows

    check = {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}["K10.2"]
    answer = rows(["event_state", "writes"], [state, writes])
    present = rows(["present"], [True])  # D3-9: the `user.drc_events` guard answers first
    out = checks.evaluate(check, _smoke_ctx(), smoke_deps(
        read_rows=lambda statement, side: present if "to_regclass" in statement else answer))
    assert out.verdict.value == expected, out.detail


def test_the_prefill_drc_smoke_row_is_gone():
    from cobalt.smoke.config import SUITES_DIR, load_suite

    suite = load_suite(SUITES_DIR / "s2.yaml")
    assert "K12.2" not in {c.id for c in suite.checks}
    assert "com.cobalt.prefill-drc" not in (SUITES_DIR / "s2.yaml").read_text()
