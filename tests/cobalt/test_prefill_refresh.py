"""F4 — `prefill refresh`: the two refreshable units of the daily note,
all day, his text never touched (F4 FINAL F4-1, card f4-refresh-1010).

Every new name is imported INSIDE each test (`DailyRefreshConfig`,
`run_daily_refresh`, `format_stamp`, `ensure_daily_note`, the `body_fn`
keyword), never at module top, so each test is red on BASE on its own.

Every vault is a `tmp_path` vault (L28); Finviz is a fake in every test
(no network); the with-DB tests run on `cobalt_dev` inside the suite's
rolled-back transaction (`dev_db_tx`, as `test_vaultwrite.py:54` does);
the offline ones use `MemoryStore`, a `tmp_path`-scoped stand-in for
`VaultWriteStore` with the same five reads and the same transaction
shape. Constructed tickers, prices and dates only (L32).
"""

import hashlib
import os
import time
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest

from cobalt.aset import config as aset_config_module
from cobalt.aset.config import AsetConfig
from cobalt.aset.daily_note import CARDS_SECTION, STUB_BANNER, card_unit_id, stub_template
from cobalt.prefill import daily as daily_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.calendar import EconomicEvent
from cobalt.prefill.config import REPO_ROOT
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow
from cobalt.radar import notes as radar_notes
from cobalt.session.clock import ET
from cobalt.strike.detector import DemandPlan
from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.markers import find_section
from cobalt.vaultwrite.writer import after_pattern

import re

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

DAY = date(2026, 9, 3)
NOTE_NAME = "2026-09-03.md"
#: The real day-mode block, before the `vault` fixture swaps in its fixture
#: text (fix round, check A4).
REAL_SHEET_MODE_BLOCK = daily_module.build_sheet_mode_block
MANUAL = "n/a (manual)"


def at(hh: int, mm: int, day: date = DAY) -> datetime:
    return datetime(day.year, day.month, day.day, hh, mm, tzinfo=ET)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row(ticker: str, price: str, change: str) -> str:
    return f"| {ticker} | ${Decimal(price):.2f} | {Decimal(change):+.2f}% |"


# ---------------------------------------------------------------------------
# Fakes: Finviz, the radar plan, the store
# ---------------------------------------------------------------------------


class FakeFinviz:
    """Counts every request (one call = one GET) and serves constructed rows."""

    def __init__(self):
        self.gets = 0
        self.dead = False
        self.prices = {"SPY": ("500.00", "0.10"), "QQQ": ("400.00", "0.20"), "IWM": ("200.00", "0.30")}
        self.calendar = [EconomicEvent(event="ZZZ index", time="08:30", impact="3", expected="1.0%", prior="0.9%")]

    def set(self, **prices):
        self.prices.update(prices)

    async def market(self, *a, **kw):
        self.gets += 1
        if self.dead:
            raise PrefillFetchError("market screener fetch failed: fixture transport down")
        return [MarketRow(ticker=t, price=Decimal(p), change_pct=Decimal(c)) for t, (p, c) in self.prices.items()]

    async def economic(self, *a, **kw):
        self.gets += 1
        if self.dead:
            raise PrefillFetchError("calendar/economic fetch failed: fixture transport down")
        return list(self.calendar)

    async def earnings(self, *a, **kw):
        self.gets += 1
        if self.dead:
            raise PrefillFetchError("calendar/earnings fetch failed: fixture transport down")
        return []

    def line(self, ticker: str) -> str:
        p, c = self.prices[ticker]
        return row(ticker, p, c)


class MemoryStore:
    """`VaultWriteStore`'s surface, in memory, scoped to one test. Same
    transaction shape as `pending_write`: the row exists only if the
    caller's block (the file write) did not raise."""

    def __init__(self):
        self.rows: list[dict] = []
        self.overrides: list[dict] = []

    def ensure_schema(self):
        return None

    def purge_expired(self, days=30):
        return 0

    def last_after(self, note, section, unit):
        for r in reversed(self.rows):
            if (r["note"], r["section"], r["unit"]) == (note, section, unit) and r["unit_after"] is not None:
                return r["unit_after"]
        return None

    def recent_afters(self, note, section, unit, limit=10):
        found = [
            (r["id"], r["unit_after"]) for r in reversed(self.rows)
            if (r["note"], r["section"], r["unit"]) == (note, section, unit) and r["unit_after"] is not None
        ]
        return found[:limit]

    def get_write(self, write_id):
        return next((r for r in self.rows if r["id"] == write_id), None)

    def overrides_for(self, note):
        return [o for o in self.overrides if o["note"] == note]

    @contextmanager
    def pending_write(self, *, note, section, unit, overrides=None, **kw):
        write_id = len(self.rows) + 1
        yield write_id
        self.rows.append({"id": write_id, "ts": datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc),
                          "note": note, "section": section, "unit": unit, **kw})
        for ov in overrides or []:
            self.overrides.append({"note": note, "section": section, "unit": unit, "write_id": write_id, **ov})


def make_aset_cfg() -> AsetConfig:
    return AsetConfig(
        account_size=Decimal("10000"),
        daily_note={"daily_notes_dir": "1 - Trading/1- Daily Notes", "filename_pattern": "%Y-%m-%d.md"},
    )


class FakeSheetModes:
    def dollars_for(self, mode, grade):
        return Decimal("30")


RULES_MD = "# THE 12 RULES\n\n1. Card first. #process\n2. Grades: B = $30, A = $70. #sizing\n"


@pytest.fixture
def finviz(monkeypatch):
    fake = FakeFinviz()
    monkeypatch.setattr(daily_module, "fetch_market_table", fake.market)
    monkeypatch.setattr(daily_module, "fetch_economic_events", fake.economic)
    monkeypatch.setattr(daily_module, "fetch_earnings_events", fake.earnings)
    return fake


@pytest.fixture
def plan(monkeypatch):
    """The radar plan the strike loop reads, the ceiling and the radar's cap
    (`radar.finviz_rpm`): X15's plan, 40 rpm planned with the strike loop's
    10 of headroom, under 50 with the radar capped at 37, unless a test says
    otherwise. `state.bucket` set to an exception makes the cap unreadable."""
    state = SimpleNamespace(plan=DemandPlan(planned_rpm=40.0, headroom_rpm=10.0), ceiling=50, error=None, bucket=37)

    def _read_plan():
        if state.error is not None:
            raise state.error
        return state.plan

    def _bucket(by_key=None):
        if isinstance(state.bucket, BaseException):
            raise state.bucket
        return state.bucket

    monkeypatch.setattr(daily_module, "read_plan", _read_plan, raising=False)
    monkeypatch.setattr(daily_module, "radar_bucket_rpm", _bucket, raising=False)
    monkeypatch.setattr(radar_notes, "_ceiling", lambda: state.ceiling)
    return state


@pytest.fixture
def vault(monkeypatch, tmp_path, finviz, plan):
    root = tmp_path / "vault"
    (root / "1 - Trading" / "1- Daily Notes").mkdir(parents=True)
    (root / "1 - Trading" / "5 - Review").mkdir(parents=True)
    (root / "1 - Trading" / "5 - Review" / "Rules.md").write_text(RULES_MD, encoding="utf-8")
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: root)
    monkeypatch.setattr(aset_config_module, "load_config", make_aset_cfg)
    monkeypatch.setattr(daily_module, "load_aset_config", make_aset_cfg)
    monkeypatch.setattr(daily_module, "load_sheet_modes_config", lambda: FakeSheetModes())
    monkeypatch.setattr(daily_module, "build_sheet_mode_block", lambda *a, **kw: "**Day mode: REDUCED** (fixture)")
    monkeypatch.setattr(daily_module, "daily_risk_values",
                        lambda: SimpleNamespace(daily_stop={"full": 100, "half": 50}))

    class _NoCards:
        def __init__(self, *a, **kw):
            pass

        def for_date(self, day):
            return []

    monkeypatch.setattr(daily_module, "AsetStore", _NoCards)

    def _never(*a, **kw):
        raise AssertionError("regenerate_rules_config was called by refresh")

    monkeypatch.setattr(daily_module, "regenerate_rules_config", _never)
    return root / "1 - Trading" / "1- Daily Notes" / NOTE_NAME


@pytest.fixture
def db_store():
    s = VaultWriteStore()
    s.ensure_schema()
    return s


def refresh(when, store, *, dry_run=False):
    from cobalt.prefill.daily import run_daily_refresh

    return run_daily_refresh(when, dry_run=dry_run, store=store)


def unit_body(path: Path, section: str, unit: str):
    lines = path.read_text(encoding="utf-8").split("\n")
    block = find_section(lines, section)
    if block is None or unit not in block.units:
        return None
    return "\n".join(block.units[unit].body(lines))


def table(path: Path) -> list[str]:
    return unit_body(path, "trading", "market_table").split("\n")


def outside_units(text: str) -> str:
    """The note with the two refreshable units' bodies blanked out."""
    lines = text.split("\n")
    for section, unit in (("trading", "market_table"), ("market_calendar", "market_calendar")):
        block = find_section(lines, section)
        if block is None or unit not in block.units:
            continue
        u = block.units[unit]
        lines = lines[: u.open_line + 1] + ["<refreshable>"] + lines[u.close_line :]
    return "\n".join(lines)


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert text.count(old) == 1, f"fixture edit target not unique: {old!r}"
    path.write_text(text.replace(old, new), encoding="utf-8")


def line_of(path: Path, prefix: str) -> str:
    return next(x for x in table(path) if x.startswith(prefix))


def rows_for(store, path: Path, section: str) -> int:
    with store._connect() as conn:
        return conn.execute(
            "SELECT count(*) FROM vault_writes WHERE note = %s AND section = %s", (str(path), section)
        ).fetchone()[0]


def all_rows(store, path: Path) -> int:
    with store._connect() as conn:
        return conn.execute("SELECT count(*) FROM vault_writes WHERE note = %s", (str(path),)).fetchone()[0]


# ===========================================================================
# C1 — DailyRefreshConfig (T6, config half; offline)
# ===========================================================================

GOOD = (
    "prefill:\n  trades_dir: x\n  review_dir: y\n  drc_filename_pattern: a\n  trade_filename_pattern: b\n"
    "daily_refresh:\n  units: [trading/market_table, market_calendar/market_calendar]\n"
    "  fields: {SPY: cobalt, QQQ: cobalt, IWM: cobalt, VIX: manual, BTC: manual}\n"
)


def _cfg_file(tmp_path, text):
    path = tmp_path / "prefill.yaml"
    path.write_text(text)
    return path


class TestDailyRefreshConfig:
    def test_the_repo_file_loads(self):
        from cobalt.prefill.config import load_daily_refresh_config

        cfg = load_daily_refresh_config()
        assert cfg.units == ["trading/market_table", "market_calendar/market_calendar"]
        assert cfg.fields == {"SPY": "cobalt", "QQQ": "cobalt", "IWM": "cobalt", "VIX": "manual", "BTC": "manual"}

    def test_a_good_file_loads(self, tmp_path):
        from cobalt.prefill.config import DailyRefreshConfig, load_daily_refresh_config

        assert isinstance(load_daily_refresh_config(_cfg_file(tmp_path, GOOD)), DailyRefreshConfig)

    @pytest.mark.parametrize(
        ("old", "new", "named"),
        [
            ("IWM: cobalt, ", "", "IWM"),                                  # a missing key
            ("BTC: manual}", "BTC: manual, DIA: cobalt}", "DIA"),          # an unknown key
            ("QQQ: cobalt", "QQQ: auto", "QQQ"),                           # an owner other than cobalt|manual
            ("market_calendar/market_calendar]", "market_calendar/market_calendar, rules/rules]", "rules/rules"),
            ("VIX: manual", "VIX: cobalt", "VIX"),                         # no source capability
            ("BTC: manual", "BTC: cobalt", "BTC"),
        ],
    )
    def test_a_bad_file_refuses_naming_the_key(self, tmp_path, old, new, named):
        from cobalt.prefill.config import PrefillConfigError, load_daily_refresh_config

        assert old in GOOD
        with pytest.raises(PrefillConfigError) as exc:
            load_daily_refresh_config(_cfg_file(tmp_path, GOOD.replace(old, new)))
        assert named in str(exc.value)

    def test_an_unknown_top_level_key_refuses(self, tmp_path):
        from cobalt.prefill.config import PrefillConfigError, load_daily_refresh_config

        with pytest.raises(PrefillConfigError, match="cadence"):
            load_daily_refresh_config(_cfg_file(tmp_path, GOOD + "  cadence: 30\n"))

    def test_a_missing_block_refuses(self, tmp_path):
        from cobalt.prefill.config import PrefillConfigError, load_daily_refresh_config

        with pytest.raises(PrefillConfigError, match="daily_refresh"):
            load_daily_refresh_config(_cfg_file(tmp_path, GOOD.split("daily_refresh:")[0]))


# ===========================================================================
# C2 — the job row, the tunables, the plist (T10; offline)
# ===========================================================================


class TestTheJobRow:
    LABEL = "com.cobalt.prefill-refresh"

    def _spec(self):
        from cobalt.jobs.config import load_job_registry

        return load_job_registry().spec(self.LABEL)

    def test_the_registry_loads_the_row(self):
        spec = self._spec()
        assert spec.kind.value == "one-shot" and spec.supervisor.value == "self" and spec.timeout_s == 300
        assert spec.schedule.every_min_tunable == "prefill.refresh_interval_min"
        assert spec.schedule.window_tunable == "prefill.refresh_window"
        assert spec.schedule.weekdays == [1, 2, 3, 4, 5]

    def test_105_firings_21_a_weekday_0545_to_1545_with_0845(self):
        entries = self._spec().schedule.calendar_entries()
        assert len(entries) == 105
        for day in (1, 2, 3, 4, 5):
            times = [(e["Hour"], e["Minute"]) for e in entries if e["Weekday"] == day]
            assert len(times) == 21
            assert times[0] == (5, 45) and times[1] == (6, 15) and times[-1] == (15, 45)
            assert (8, 45) in times

    def test_the_plist_equals_the_registry_and_validate_parity_holds(self):
        """`cobalt validate`'s CROSS-CHECK 2 for a windowed interval
        (`src/cobalt/cli.py:375-399`), applied to this row: entry for entry,
        no StartInterval, COBALT_ENV=production."""
        import plistlib

        spec = self._spec()
        data = plistlib.loads(spec.plist_path.read_bytes())
        assert [dict(e) for e in data["StartCalendarInterval"]] == spec.schedule.calendar_entries()
        assert data.get("StartInterval") is None
        assert data["EnvironmentVariables"]["COBALT_ENV"] == "production"
        assert data["ProgramArguments"][-2:] == ["prefill", "refresh"]

    def test_the_template_names_both_one_shot_readers(self):
        from cobalt.jobs.config import load_job_registry

        entry = load_job_registry().no_resident_read("configs/cobalt/templates/daily.md.j2")
        assert entry.readers == ["com.cobalt.prefill-daily", self.LABEL,  # F5 card 731 K9
                                 *(f"com.cobalt.checkpoint-{s}" for s in ("0715", "0745", "0815", "0845"))]

    def test_the_tunables_are_proposed_dwv(self):
        from cobalt.taxonomy.loader import load_tunables

        rows = load_tunables().by_key
        assert rows["prefill.refresh_interval_min"].value == 30
        assert rows["prefill.refresh_window"].value == "05:45-15:45"
        for key in ("prefill.refresh_interval_min", "prefill.refresh_window"):
            assert str(rows[key].status.value if hasattr(rows[key].status, "value") else rows[key].status) == "proposed"
            assert str(rows[key].source.value if hasattr(rows[key].source, "value") else rows[key].source) == "dwv"

    def test_the_smoke_row_watches_the_job(self):
        import yaml

        raw = yaml.safe_load((REPO_ROOT / "configs" / "cobalt" / "smoke" / "s2.yaml").read_text())
        found = []

        def walk(node):
            if isinstance(node, dict):
                if node.get("label") == self.LABEL and node.get("kind") == "job_row":
                    found.append(node)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(raw)
        assert len(found) == 1


# ===========================================================================
# M1 — merge3: an untouched equal-length replace emits an insert at its anchor
# ===========================================================================


class TestMergeInsertAtAnchor:
    def test_t3b_note_lands_immediately_before_the_new_qqq_line(self):
        from cobalt.vaultwrite.merge import merge3

        base = ["| SPY | 1 |", "| QQQ | 2 |", "| IWM | 3 |"]
        human = ["| SPY | 1 |", "NOTE", "| QQQ | 2 |", "| IWM | 3 |"]
        cobalt = ["| SPY | 11 |", "| QQQ | 22 |", "| IWM | 33 |"]
        out = merge3(base, human, cobalt)
        assert out.lines == ["| SPY | 11 |", "NOTE", "| QQQ | 22 |", "| IWM | 33 |"]
        assert out.overrides == []

    def test_negative_control_unequal_spans_keep_todays_order(self):
        from cobalt.vaultwrite.merge import merge3

        base = ["a", "b", "c"]
        human = ["a", "NOTE", "b", "c"]
        cobalt = ["x", "y"]
        assert merge3(base, human, cobalt).lines == ["x", "y", "NOTE"]


# ===========================================================================
# S1 — the stamp (T13), the template, daymode (X7); offline
# ===========================================================================


class TestStamp:
    @pytest.mark.parametrize("tz", ["UTC", "America/Los_Angeles"])
    @pytest.mark.parametrize(
        ("instant", "expected"),
        [
            (datetime(2026, 9, 3, 12, 45, tzinfo=timezone.utc), "as of 08:45 ET"),
            (datetime(2026, 9, 4, 3, 30, tzinfo=timezone.utc), "as of 23:30 ET"),      # ET midnight not yet crossed
            (datetime(2026, 11, 1, 5, 30, tzinfo=timezone.utc), "as of 01:30 ET"),     # EDT, before the fall-back
            (datetime(2026, 11, 1, 6, 30, tzinfo=timezone.utc), "as of 01:30 ET"),     # EST, after it
            (datetime(2026, 3, 8, 7, 30, tzinfo=timezone.utc), "as of 03:30 ET"),      # spring-forward
        ],
    )
    def test_t13_et_under_a_foreign_host_zone(self, monkeypatch, tz, instant, expected):
        from cobalt.prefill.daily import format_stamp

        monkeypatch.setenv("TZ", tz)
        time.tzset()
        try:
            assert format_stamp(instant) == expected
        finally:
            monkeypatch.delenv("TZ")
            time.tzset()

    def test_t13_a_naive_datetime_is_refused(self):
        from cobalt.prefill.daily import format_stamp
        from cobalt.session.clock import SessionError

        with pytest.raises(SessionError, match="naive"):
            format_stamp(datetime(2026, 9, 3, 8, 45))

    def test_t13_the_note_day_is_the_et_day(self, vault):
        from cobalt.prefill.daily import refresh_note_path

        assert refresh_note_path(datetime(2026, 9, 4, 3, 30, tzinfo=timezone.utc)).name == NOTE_NAME

    @pytest.mark.parametrize("how", ["absent", "None"])
    @pytest.mark.parametrize("key", ["prefill.refresh_interval_min", "prefill.refresh_window"])
    def test_x7_a_missing_or_unmeasured_refresh_tunable_is_refused(self, vault, finviz, monkeypatch, key, how):
        """X7 (F4-FINAL :213), card 1047 T1: `refresh_demand_consumer` refuses
        a refresh tunable absent or `value: None`, before any GET."""
        from cobalt.prefill.config import PrefillConfigError
        from cobalt.taxonomy import loader

        store = MemoryStore()
        refresh(at(5, 15), store)
        before, gets = vault.read_bytes(), finviz.gets
        rows = dict(loader.load_tunables().by_key)
        if how == "absent":
            del rows[key]
        else:
            rows[key] = rows[key].model_copy(update={"value": None})
        monkeypatch.setattr(loader, "load_tunables", lambda *a, **kw: SimpleNamespace(by_key=rows))
        with pytest.raises(PrefillConfigError, match=re.escape(key)):
            refresh(at(7, 45), store)
        assert finviz.gets == gets
        assert vault.read_bytes() == before

    def test_x7_the_daymode_unit_still_starts_as_of_after_a_later_daymode_write(self, vault, finviz):
        """X7 (F4-FINAL :213, Grok's addition), card 1047 T2: after a
        refresh-created note, `daymode.note.write` replaces the unit with
        `render_body`, whose first line is the stamp — once. The config is
        `test_daymode_note._cfg()`: `load_daymode_config()` reads
        `"user".trader_settings` (`daymode/config.py:309-326`), a database."""
        from test_daymode_note import _cfg

        from cobalt.daymode import note as daymode_note

        def outside(text: str) -> str:
            lines = text.split("\n")
            u = find_section(lines, "daymode").units["sheet_mode"]
            return "\n".join(lines[: u.open_line + 1] + ["<unit>"] + lines[u.close_line:])

        store = MemoryStore()
        refresh(at(5, 15), store)
        before = vault.read_text(encoding="utf-8")
        daymode_note.write(vault, _cfg(), "reduced", stage="stage-1", store=store)
        body = unit_body(vault, "daymode", "sheet_mode").split("\n")
        assert re.match(r"^as of \d\d:\d\d ET$", body[0]), body[0]
        assert [x for x in body if x.startswith("as of ")] == [body[0]]
        assert outside(vault.read_text(encoding="utf-8")) == outside(before)


class TestTemplateShape:
    def test_t6_render_half_and_the_stamp_lines(self):
        from cobalt.prefill.daily import stamp_context

        ctx = {"date_str": "2026-09-03", "time_str": "05:15", "rules_checkbox_block": "- [ ] r #process",
               "mantras_block": "- m", "mode_hint": "", "sheet_mode_block": "dm", "daily_stop": "full $1",
               "spy_col2": "$1.00", "spy_col3": "+0.10%", "qqq_col2": "$2.00", "qqq_col3": "+0.20%",
               "iwm_col2": "$3.00", "iwm_col3": "+0.30%", "market_calendar_block": "- 08:30 ET — ZZZ"}
        rows = [MarketRow(ticker=t, price=Decimal("1"), change_pct=Decimal("0.1")) for t in ("SPY", "QQQ", "IWM")]
        ctx.update(stamp_context(at(5, 15), rows, None, None))
        text = daily_module._render_template(ctx)
        lines = text.split("\n")
        rules = find_section(lines, "rules").units["rules"].body(lines)
        assert rules[0] == "as of 05:15 ET · rules from Rules.md" and rules[1] == ""
        trading = find_section(lines, "trading").units["market_table"].body(lines)
        assert trading[0] == ("as of 05:15 ET · SPY cobalt · QQQ cobalt · IWM cobalt · "
                              "VIX n/a (manual) · BTC n/a (manual) · calendar cobalt")
        assert trading[1] == ""
        assert f"| VIX | {MANUAL} | {MANUAL} |" in trading and f"| BTC | {MANUAL} | {MANUAL} |" in trading
        calendar = find_section(lines, "market_calendar").units["market_calendar"].body(lines)
        assert calendar[0] == "as of 05:15 ET · calendar cobalt" and calendar[1] == ""
        assert lines[4] == "#### 2026-09-03 T 05:15"


# ===========================================================================
# D1 / G1 — degraded, never blank, exit 1; the shared Finviz gate (offline)
# ===========================================================================


class TestDegraded:
    def test_t5_x5_dead_source_keeps_the_0745_values(self, vault, finviz):
        store = MemoryStore()
        assert refresh(at(5, 15), store).action == "created"
        finviz.set(SPY=("501.00", "0.20"))
        ok = refresh(at(7, 45), store)
        assert ok.exit_code == 0
        spy, qqq = line_of(vault, "| SPY"), line_of(vault, "| QQQ")
        assert spy == row("SPY", "501.00", "0.20")
        finviz.dead = True
        for when in (at(8, 15), at(8, 45)):
            result = refresh(when, store)
            assert result.exit_code == 1
            assert line_of(vault, "| SPY") == spy and line_of(vault, "| QQQ") == qqq
            body = unit_body(vault, "trading", "market_table")
            assert "FAILED" not in body
            assert "SPY cobalt-degraded (finviz fetch failed; values as of 07:45)" in body.split("\n")[0]
            assert "SPY" in " ".join(result.degraded)

    def test_x5_the_exception_leaves_the_as_job_block(self, monkeypatch):
        from cobalt.prefill import cli

        seen = []

        @contextmanager
        def recording_as_job(label, *, skip=False, store=None):
            try:
                yield SimpleNamespace(result=None)
            except BaseException as e:
                seen.append((label, type(e).__name__))
                raise

        fake = SimpleNamespace(exit_code=1, report=lambda: "r", summary=lambda: "degraded: SPY",
                               action="refreshed", path=Path("/x"), degraded=["SPY"], failures=[], flags={})
        monkeypatch.setattr(cli, "as_job", recording_as_job)
        monkeypatch.setattr(cli, "run_daily_refresh", lambda when, *, dry_run: fake)
        with pytest.raises(RuntimeError):
            cli._run_refresh(False)
        assert seen and seen[0][0] == cli.REFRESH_JOB == "com.cobalt.prefill-refresh"

    def test_prefill_refresh_is_a_subcommand(self, monkeypatch):
        from cobalt.prefill import cli

        called = []
        monkeypatch.setattr(cli, "_run_refresh", lambda dry_run: called.append(dry_run))
        monkeypatch.setattr("sys.argv", ["prefill", "refresh", "--dry-run"])
        cli.main()
        assert called == [True]


class TestSharedGate:
    def _filled(self, vault, finviz):
        store = MemoryStore()
        refresh(at(5, 15), store)
        refresh(at(7, 45), store)
        return store, table(vault)

    def test_l53_refusal_extra_alone_passes_radar_plus_extra_exceeds(self, vault, finviz, plan):
        from cobalt.prefill.daily import check_refresh_demand

        store, before = self._filled(vault, finviz)
        plan.ceiling = 10
        plan.plan = DemandPlan(planned_rpm=9.95, headroom_rpm=0.05)
        extra = daily_module.refresh_demand_consumer()
        radar_notes.check_total_demand([extra], subject="prefill-refresh", ceiling=10)  # alone: passes
        with pytest.raises(radar_notes.TotalDemandExceeded):
            radar_notes.check_scheduled_demand("prefill-refresh", radar_rpm=9.95, extra=[extra])
        assert check_refresh_demand() is not None
        gets = finviz.gets
        result = refresh(at(8, 15), store)
        assert finviz.gets == gets, "a refused gate issues no GET"
        assert result.exit_code == 1
        assert [x for x in table(vault) if x.startswith("| ")] == [x for x in before if x.startswith("| ")]

    def test_x13_peak_5005_refused_radar_admission_not_refused(self, vault, finviz, plan):
        store, _ = self._filled(vault, finviz)
        plan.ceiling = 50
        plan.plan = DemandPlan(planned_rpm=49.95, headroom_rpm=0.05)
        assert daily_module.refresh_demand_consumer().rpm == pytest.approx(0.1)
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 1
        assert finviz.gets == gets
        radar = radar_notes.DemandConsumer(name="radar", rpm=49.95, window=radar_notes.DemandWindow.between("04:00", "20:00"),
                                           basis="planned total")
        others = [c for c in radar_notes.scheduled_consumers(ceiling=50, radar_rpm=49.95) if c.name != "radar"]
        radar_notes.check_total_demand([radar, *others], subject="radar", ceiling=50)  # not refused

    def test_x13_a_plan_one_under_the_ceiling_is_admitted_and_gets_three(self, vault, finviz, plan):
        store, _ = self._filled(vault, finviz)
        plan.plan = DemandPlan(planned_rpm=49.0, headroom_rpm=1.0)
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 0
        assert finviz.gets - gets == 3

    @pytest.mark.parametrize(
        "broken",
        [
            SimpleNamespace(error=RuntimeError("radar notes unreadable (fixture)"), plan=None),
            SimpleNamespace(error=None, plan=DemandPlan(planned_rpm=None, headroom_rpm=None)),
            SimpleNamespace(error=None, plan=DemandPlan(planned_rpm=50.0, headroom_rpm=0.0)),
            SimpleNamespace(error=None, plan=DemandPlan(planned_rpm=40.0, headroom_rpm=None)),
        ],
    )
    def test_x14_unreadable_plan_no_get_no_none_radar_call(self, vault, finviz, plan, monkeypatch, broken):
        store, before = self._filled(vault, finviz)
        calls = []
        real = daily_module.check_scheduled_demand

        def spy(subject, **kw):
            calls.append(kw)
            return real(subject, **kw)

        monkeypatch.setattr(daily_module, "check_scheduled_demand", spy)
        plan.error, plan.plan = broken.error, broken.plan or plan.plan
        gets = finviz.gets
        result = refresh(at(8, 15), store)
        assert finviz.gets == gets
        assert result.exit_code == 1
        assert calls == [], "the gate is never called with radar_rpm=None, nor on no headroom"
        after = table(vault)
        assert [x for x in after if x.startswith("| ")] == [x for x in before if x.startswith("| ")]
        assert "cobalt-degraded" in after[0]

    # -- his ruling C (2026-10-26, R2512): the radar cap + strike + refresh ---

    def test_c_radar_cap_strike_headroom_and_refresh_over_the_ceiling_is_refused_no_get(self, vault, finviz, plan):
        from cobalt.prefill.daily import check_refresh_demand

        store, before = self._filled(vault, finviz)
        plan.plan = DemandPlan(planned_rpm=30.0, headroom_rpm=20.0)  # 37 + 20 + 3 = 60
        refusal = check_refresh_demand()
        assert refusal is not None
        assert "radar.finviz_rpm" in refusal and "REFRESH_GETS" in refusal
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 1
        assert finviz.gets == gets, "a refused gate issues no GET"
        assert [x for x in table(vault) if x.startswith("| ")] == [x for x in before if x.startswith("| ")]

    def test_c_x15_plan_is_admitted_at_exactly_the_ceiling_and_gets_three(self, vault, finviz, plan):
        store, _ = self._filled(vault, finviz)
        plan.plan = DemandPlan(planned_rpm=40.0, headroom_rpm=10.0)  # 37 + 10 + 3 = 50
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 0
        assert finviz.gets - gets == 3

    def test_c_one_over_the_allowance_is_refused(self, vault, finviz, plan):
        store, _ = self._filled(vault, finviz)
        plan.plan = DemandPlan(planned_rpm=39.0, headroom_rpm=11.0)  # 37 + 11 + 3 = 51
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 1
        assert finviz.gets == gets

    def test_c_an_unreadable_radar_finviz_rpm_makes_no_get(self, vault, finviz, plan):
        from cobalt.prefill.daily import check_refresh_demand
        from cobalt.radar.collector import SourceFailure

        store, _ = self._filled(vault, finviz)
        plan.bucket = SourceFailure("radar.finviz_rpm = None is refused (constructed)")
        assert "radar.finviz_rpm" in (check_refresh_demand() or "")
        gets = finviz.gets
        assert refresh(at(8, 15), store).exit_code == 1
        assert finviz.gets == gets


# ===========================================================================
# T12 — refresh never regenerates rules (offline)
# ===========================================================================


def _rules_files():
    paths = [REPO_ROOT / "configs" / "cobalt" / "rules.yaml", REPO_ROOT / "configs" / "dev" / "rules.generated.yaml"]
    return {p: (sha(p) if p.exists() else None) for p in paths}


class TestNoRulesRegeneration:
    def test_t12_absent_existing_and_dry_run(self, vault):
        before = _rules_files()
        store = MemoryStore()
        refresh(at(5, 15), MemoryStore(), dry_run=True)       # absent note, dry-run
        assert not vault.exists()
        refresh(at(5, 15), store)                              # absent note
        refresh(at(6, 15), store)                              # existing note
        refresh(at(6, 45), store, dry_run=True)                # existing note, dry-run
        assert _rules_files() == before


# ===========================================================================
# W1 — upsert_unit(body_fn=...) (X4 retry leg; with-DB)
# ===========================================================================


@requires_db
class TestBodyFn:
    def test_x4_body_fn_runs_on_every_attempt_with_that_attempts_snapshot(self, tmp_path, db_store):
        path = tmp_path / NOTE_NAME
        writer0 = VaultWriter("prefill.daily", store=db_store)
        writer0.create_if_absent(path, "# n\n\n<!-- cobalt:section trading -->\n<!-- cobalt:unit market_table -->\n"
                                       "| SPY | 1 |\n<!-- /cobalt:unit market_table -->\n<!-- /cobalt:section trading -->\n")
        other = VaultWriter("heartbeat", store=db_store)
        fired = []

        def hook(p):
            if not fired:
                fired.append(1)
                other.upsert_unit(p, "heartbeat", "status", "beat (another writer)")

        calls = []

        def body_fn(snapshot):
            calls.append(snapshot.sha256)
            return "| SPY | 2 |"

        writer = VaultWriter("prefill.refresh", store=db_store, precommit_hook=hook)
        result = writer.upsert_unit(path, "trading", "market_table", "", body_fn=body_fn)
        assert len(calls) == 2 and calls[0] != calls[1]
        assert result.action == "updated" and "| SPY | 2 |" in path.read_text()
        assert "beat (another writer)" in path.read_text()

    def test_negative_control_without_body_fn_the_fixed_body_is_written(self, tmp_path, db_store):
        path = tmp_path / NOTE_NAME
        writer = VaultWriter("prefill.daily", store=db_store)
        writer.create_if_absent(path, "# n\n")
        writer.upsert_unit(path, "trading", "market_table", "| SPY | 3 |")
        assert "| SPY | 3 |" in path.read_text()


# ===========================================================================
# O1 / O2 / E1 / U1 — the refresh on the real writer and store (with-DB)
# ===========================================================================


@requires_db
class TestOwnership:
    def test_t1_charter_test(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        edit(vault, "### Game Plan:\n", "### Game Plan:\nhis plan, typed at 06:00\n")
        edit(vault, f"| VIX | {MANUAL} | {MANUAL} |", "| VIX | 17.25 | rising |")
        before = vault.read_text()
        finviz.set(SPY=("505.55", "0.55"), QQQ=("405.55", "0.66"), IWM=("205.55", "0.77"))
        result = refresh(at(8, 45), db_store)
        after = vault.read_text()
        assert outside_units(after) == outside_units(before)
        assert "| VIX | 17.25 | rising |" in table(vault)
        for t in ("SPY", "QQQ", "IWM"):
            assert finviz.line(t) in table(vault)
        trading = [w for w in result.writes if w.section == "trading"]
        assert len(trading) == 1 and trading[0].write_id is not None and trading[0].diff
        assert db_store.get_write(trading[0].write_id)["hash_after"] == sha(vault)
        assert "VIX human" in table(vault)[0]

    def test_t2_his_spy_row_survives_three_refreshes(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        his = "| SPY | $512.34 his | +9.99% |"
        edit(vault, line_of(vault, "| SPY"), his)
        for n, when in enumerate((at(6, 15), at(6, 45), at(8, 45))):
            finviz.set(SPY=(f"50{n}.00", "0.10"), QQQ=(f"40{n}.00", "0.20"), IWM=(f"20{n}.00", "0.30"))
            refresh(when, db_store)
            rows = table(vault)
            assert rows.count(his) == 1, f"his SPY row lost at refresh {n + 1}"
            assert not any(x.startswith("| SPY") and x != his for x in rows)
            assert "SPY human" in rows[0]

    @pytest.mark.xfail(
        strict=True,
        reason="F4 FINAL X1/T2b (FC14): his SPY line copied into the proposal makes SPY..IWM one touched "
        "replace in merge3 (merge.py:146-156), which keeps QQQ/IWM at base for that refresh while the "
        "stamp says `cobalt`; [F-26]/[F-27] return to him (build report DECISION T2b)",
    )
    def test_t2b_qqq_iwm_fresh_and_cobalt_at_the_first_refresh_after_his_spy_edit(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        edit(vault, line_of(vault, "| SPY"), "| SPY | $512.34 his | +9.99% |")
        finviz.set(QQQ=("411.11", "0.21"), IWM=("211.11", "0.31"))
        refresh(at(6, 15), db_store)
        rows = table(vault)
        assert "SPY human · QQQ cobalt · IWM cobalt" in rows[0]
        assert finviz.line("QQQ") in rows and finviz.line("IWM") in rows

    def test_t3_x2_an_inserted_line_survives_once_at_its_anchor(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        qqq = line_of(vault, "| QQQ")
        edit(vault, qqq, "NOTE his line\n" + qqq)
        for n, when in enumerate((at(6, 15), at(6, 45), at(8, 45))):
            finviz.set(SPY=(f"51{n}.00", "0.1"), QQQ=(f"41{n}.00", "0.2"), IWM=(f"21{n}.00", "0.3"))
            refresh(when, db_store)
            rows = table(vault)
            assert rows.count("NOTE his line") == 1
            assert rows[rows.index("NOTE his line") + 1] == finviz.line("QQQ")

    def test_t4_x3_his_calendar_is_never_written(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        body = unit_body(vault, "market_calendar", "market_calendar")
        mine = body.split("\n")[-1]
        edit(vault, mine, "- 09:45 ET — his own calendar line\n- and a second one")
        his_body = unit_body(vault, "market_calendar", "market_calendar")
        rows = rows_for(db_store, vault, "market_calendar")
        for when in (at(6, 15), at(6, 45), at(8, 45)):
            refresh(when, db_store)
            assert unit_body(vault, "market_calendar", "market_calendar") == his_body
            assert "calendar human" in table(vault)[0]
        assert rows_for(db_store, vault, "market_calendar") == rows

    def test_t9_x11_whole_unit_sync_revert_is_cobalts(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        finviz.set(SPY=("520.00", "0.1"))
        refresh(at(6, 15), db_store)
        older = unit_body(vault, "trading", "market_table")
        finviz.set(SPY=("521.00", "0.1"))
        refresh(at(6, 45), db_store)
        finviz.set(SPY=("522.00", "0.1"))
        refresh(at(7, 15), db_store)
        edit(vault, unit_body(vault, "trading", "market_table"), older)
        overrides = len(db_store.overrides_for(str(vault)))
        finviz.set(SPY=("523.00", "0.1"))
        result = refresh(at(7, 45), db_store)
        rows = table(vault)
        assert finviz.line("SPY") in rows and finviz.line("QQQ") in rows
        assert "SPY cobalt · QQQ cobalt · IWM cobalt" in rows[0]
        trading = next(w for w in result.writes if w.section == "trading")
        assert db_store.get_write(trading.write_id)["sync_revert_of"] is not None
        assert len(db_store.overrides_for(str(vault))) == overrides

    def test_t15_a_unit_on_disk_with_no_baseline_writes_nothing(self, vault, db_store):
        text = daily_module._render_template({"spy_col2": "$1.00", "spy_col3": "+0.1%"})
        vault.write_text(text, encoding="utf-8")
        before = sha(vault)
        result = refresh(at(8, 45), db_store)
        assert result.exit_code == 1
        assert "FAILED: baseline_missing" in result.report()
        assert sha(vault) == before
        assert all_rows(db_store, vault) == 0

    def test_t16a_his_stamp_edit_survives_three_refreshes(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        his = "as of 06:00 ET · his own words on the stamp"
        edit(vault, table(vault)[0], his)
        for n, when in enumerate((at(6, 15), at(6, 45), at(8, 45))):
            finviz.set(SPY=(f"53{n}.00", "0.1"))
            result = refresh(when, db_store)
            assert table(vault).count(his) == 1 and table(vault)[0] == his
            assert "as of" in result.report() and result.status_line in result.report()

    def test_t16b_a_non_pipe_line_between_rows_drops_nothing(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        spy = line_of(vault, "| SPY")
        edit(vault, spy, spy + "\nhis remark between rows")
        for n, when in enumerate((at(6, 15), at(6, 45), at(8, 45))):
            finviz.set(QQQ=(f"44{n}.00", "0.2"), IWM=(f"24{n}.00", "0.3"))
            refresh(when, db_store)
            rows = table(vault)
            assert finviz.line("QQQ") in rows and finviz.line("IWM") in rows
            assert f"| BTC | {MANUAL} | {MANUAL} |" in rows
            assert rows.count("his remark between rows") == 1

    def test_t17_vix_one_typed_one_blank_identical_through_0845(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        his = "| VIX | 17.25 |  |"
        edit(vault, f"| VIX | {MANUAL} | {MANUAL} |", his)
        for when in (at(6, 15), at(6, 45), at(8, 45)):
            refresh(when, db_store)
            assert table(vault).count(his) == 1

    def test_x2_deletion_and_rename_are_not_resurrected(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        edit(vault, line_of(vault, "| QQQ") + "\n", "")
        edit(vault, line_of(vault, "| SPY"), "| SPX | $1.00 | +0.00% |")
        for when in (at(6, 15), at(6, 45)):
            refresh(when, db_store)
            rows = table(vault)
            assert not any(x.startswith("| QQQ") for x in rows)
            assert not any(x.startswith("| SPY") for x in rows)
            assert rows.count("| SPX | $1.00 | +0.00% |") == 1
            assert any(x.startswith("| IWM") for x in rows)

    def test_x2_duplicate_and_malformed_ticker_lines_and_a_manual_blank(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        iwm = line_of(vault, "| IWM")
        edit(vault, iwm, iwm + "\n| SPY | his duplicate |")
        edit(vault, iwm, "| IWM broken by hand")
        edit(vault, f"| BTC | {MANUAL} | {MANUAL} |", "| BTC |     |     |")
        for when in (at(6, 15), at(6, 45)):
            refresh(when, db_store)
            rows = table(vault)
            assert rows.count("| SPY | his duplicate |") == 1
            assert rows.count("| IWM broken by hand") == 1
            assert rows.count("| BTC |     |     |") == 1
            assert sum(1 for x in rows if x.startswith("| SPY")) == 2


@requires_db
class TestConcurrency:
    def test_x4_two_refreshes_no_lock_the_insert_survives_the_loser_retry(self, vault, finviz, db_store, monkeypatch):
        refresh(at(5, 15), db_store)
        qqq = line_of(vault, "| QQQ")
        edit(vault, qqq, "NOTE his line\n" + qqq)
        real = daily_module.VaultWriter
        state = {"armed": True, "fired": False}

        def hook(path):
            if not state["fired"]:
                state["fired"] = True
                finviz.set(SPY=("560.00", "0.1"))
                refresh(at(8, 45), db_store)  # B lands inside A's window

        def factory(*a, **kw):
            if state["armed"]:
                state["armed"] = False
                kw["precommit_hook"] = hook
            return real(*a, **kw)

        monkeypatch.setattr(daily_module, "VaultWriter", factory)
        refresh(at(8, 45), db_store)  # A: aborts once, retries with body_fn
        assert state["fired"]
        rows = table(vault)
        assert rows.count("NOTE his line") == 1
        assert rows[rows.index("NOTE his line") + 1].startswith("| QQQ")

    def test_x12_commit_window_race_no_override_names_a_values(self, vault, finviz, db_store, monkeypatch):
        """A pauses after `os.replace` in `_commit` (`writer.py:556`) and before
        its row commits; B runs in that window and cannot see A's row (the
        Postgres visibility of an uncommitted row, simulated on the shared
        test connection by hiding exactly that row from B's reads)."""
        refresh(at(5, 15), db_store)

        class Hiding:
            def __init__(self, inner, hidden):
                self.inner, self.hidden = inner, hidden

            def __getattr__(self, name):
                return getattr(self.inner, name)

            def last_after(self, note, section, unit):
                rows = self.recent_afters(note, section, unit, limit=1)
                return rows[0][1] if rows else None

            def recent_afters(self, note, section, unit, limit=10):
                rows = self.inner.recent_afters(note, section, unit, limit=limit + 1)
                return [r for r in rows if r[0] != self.hidden][:limit]

            def overrides_for(self, note):
                return [o for o in self.inner.overrides_for(note) if o["write_id"] != self.hidden]

        from cobalt.vaultwrite import writer as writer_module

        real_commit = writer_module.VaultWriter._commit
        state = {"done": False, "a_values": None}

        def trading(text):
            lines = (text or "").split("\n")
            block = find_section(lines, "trading")
            return "\n".join(block.units["market_table"].body(lines)) if block else None

        def commit_then_b(self, path, snapshot, new_text):
            real_commit(self, path, snapshot, new_text)
            # A's TRADING commit only (A writes the calendar first).
            if state["done"] or self.writer != "prefill.refresh" or trading(snapshot.text) == trading(new_text):
                return
            state["done"] = True
            with db_store._connect() as conn:
                hidden = conn.execute("SELECT max(id) FROM vault_writes").fetchone()[0]
            state["a_values"] = [x for x in table(path) if x.startswith(("| SPY", "| QQQ", "| IWM"))]
            finviz.set(SPY=("571.00", "0.1"), QQQ=("471.00", "0.2"), IWM=("271.00", "0.3"))
            state["b"] = refresh(at(8, 45), Hiding(db_store, hidden))

        monkeypatch.setattr(writer_module.VaultWriter, "_commit", commit_then_b)
        finviz.set(SPY=("570.00", "0.1"), QQQ=("470.00", "0.2"), IWM=("270.00", "0.3"))
        refresh(at(8, 15), db_store)
        assert state["done"]
        assert state["a_values"] == [finviz_a for finviz_a in (
            row("SPY", "570.00", "0.1"), row("QQQ", "470.00", "0.2"), row("IWM", "270.00", "0.3"))]
        named = [o for o in db_store.overrides_for(str(vault))
                 if any(v in (o["human_text"] or "") for v in state["a_values"])]
        assert named == [], f"an override names A's values: {named}"
        # B wrote nothing to the unit and said so, loud (fix round, X12).
        assert state["b"].exit_code == 1 and "FAILED: write_in_flight" in state["b"].report()
        assert [x for x in table(vault) if x.startswith(("| SPY", "| QQQ", "| IWM"))] == state["a_values"]


@requires_db
class TestCreateStubDryRun:
    def test_t8_absent_note_created_through_the_shared_render(self, vault, finviz, db_store):
        result = refresh(at(5, 15), db_store)
        assert result.action == "created" and vault.exists()
        assert [w.action for w in result.writes] == ["created"]
        lines = vault.read_text().split("\n")
        rules = find_section(lines, "rules").units["rules"].body(lines)
        assert rules[0] == "as of 05:15 ET · rules from Rules.md"     # X7, the clock half
        assert "- [ ] Card first. #process" in rules
        assert finviz.line("SPY") in table(vault)

    def test_ensure_daily_note_does_not_replace_an_existing_file(self, vault, db_store):
        from cobalt.prefill.daily import ensure_daily_note

        vault.write_text("# his note, only his\n", encoding="utf-8")
        result = ensure_daily_note(VaultWriter("prefill.refresh", store=db_store), at(6, 0))
        assert result.action == "skipped_exists"
        assert vault.read_text() == "# his note, only his\n"
        with pytest.raises(Exception, match="naive"):
            ensure_daily_note(VaultWriter("prefill.refresh", store=db_store), datetime(2026, 9, 3, 6, 0))

    def _stub(self, vault, db_store, extra=""):
        writer = VaultWriter("aset.daily_note", store=db_store)
        writer.create_if_absent(vault, stub_template(at(10, 2)) + extra)
        writer.upsert_unit(vault, CARDS_SECTION, card_unit_id(at(10, 2)),
                           "### 10:02:06 — ZZZQ LONG B\n```aset\nticker: ZZZQ\n```")
        return vault.read_text()

    def test_x6_the_stub_gets_both_units_and_keeps_every_byte(self, vault, finviz, db_store):
        stub = self._stub(vault, db_store)
        result = refresh(at(10, 15), db_store)
        text = vault.read_text()
        assert text.startswith(stub.rstrip("\n"))
        assert STUB_BANNER.rstrip("\n") in text and "ticker: ZZZQ" in text
        assert find_section(text.split("\n"), "rules") is None
        assert find_section(text.split("\n"), "daymode") is None
        rows = table(vault)
        assert rows[0].startswith("as of 10:15 ET · SPY cobalt") and rows[1] == ""
        assert "| --- | --- | --- |" in rows
        assert f"| VIX | {MANUAL} | {MANUAL} |" in rows and f"| BTC | {MANUAL} | {MANUAL} |" in rows
        assert unit_body(vault, "market_calendar", "market_calendar") is not None
        assert sorted(w.section for w in result.writes) == ["market_calendar", "trading"]

    def test_x16_the_stub_twice_takes_the_ownership_path(self, vault, finviz, db_store):
        self._stub(vault, db_store)
        refresh(at(10, 15), db_store)
        assert db_store.last_after(str(vault), "trading", "market_table") == unit_body(vault, "trading", "market_table")
        finviz.set(SPY=("580.00", "0.1"))
        second = refresh(at(10, 45), db_store)
        assert second.exit_code == 0
        assert vault.read_text().count("<!-- cobalt:unit market_table -->") == 1
        assert finviz.line("SPY") in table(vault)

    def test_x16_a_hand_typed_trading_table_in_a_stub_keeps_its_bytes(self, vault, finviz, db_store):
        hand = "| VIX | 17.5 | his |\n| --- | --- | --- |\n| SPY | 9.99 | his |\n| BTC | 1 | his |"
        self._stub(vault, db_store, extra="\n### Trading\n\n" + hand + "\n")
        result = refresh(at(10, 15), db_store)
        assert hand in vault.read_text()
        assert unit_body(vault, "trading", "market_table") is None
        assert rows_for(db_store, vault, "trading") == 0
        assert "SPY human · QQQ human · IWM human" in result.status_line

    def test_o2_his_text_under_the_calendar_heading_is_not_wrapped(self, vault, finviz, db_store):
        self._stub(vault, db_store, extra="\n### Market Calendar:\n- his calendar, typed by hand\n")
        refresh(at(10, 15), db_store)
        assert unit_body(vault, "market_calendar", "market_calendar") is None
        assert "- his calendar, typed by hand" in vault.read_text()

    def test_t11_dry_run_writes_no_file_and_no_row(self, vault, finviz, db_store):
        refresh(at(5, 15), MemoryStore(), dry_run=True)
        assert not vault.exists()
        refresh(at(5, 15), db_store)
        before, rows = sha(vault), all_rows(db_store, vault)
        finviz.set(SPY=("590.00", "0.1"))
        result = refresh(at(8, 45), db_store, dry_run=True)
        assert sha(vault) == before and all_rows(db_store, vault) == rows
        assert any(w.diff for w in result.writes), "a dry run still shows the diff"


@requires_db
class TestUntouchedUnits:
    def test_t7_rules_daymode_heartbeat_and_market_context_are_byte_identical(self, vault, finviz, db_store):
        refresh(at(5, 15), db_store)
        edit(vault, "- [ ] Card first. #process", "- [x] Card first. #process")
        edit(vault, "**Day mode: REDUCED** (fixture)", "**Day mode: REDUCED** (fixture) and his note")
        other = VaultWriter("heartbeat", store=db_store)
        other.upsert_unit(vault, "heartbeat", "status", "HEARTBEAT 06:00 green (fixture)")
        ctx = VaultWriter("prefill.checkpoint", store=db_store)
        ctx.upsert_unit(vault, "market_context", "checkpoint_0715", "07:15 context (fixture)",
                        placement=after_pattern(re.compile(r"^### Market Context:"), "after Market Context"))
        lines = vault.read_text().split("\n")
        keep = {name: find_section(lines, name).text(lines) for name in ("rules", "daymode", "heartbeat", "market_context")}
        for n, when in enumerate((at(6, 15), at(6, 45), at(8, 45))):
            finviz.set(SPY=(f"59{n}.00", "0.1"))
            refresh(when, db_store)
            lines = vault.read_text().split("\n")
            for name, text in keep.items():
                assert find_section(lines, name).text(lines) == text, name
        assert "-" in vault.read_text().split("### Market Context:")[1]


# ===========================================================================
# Check findings (f4-refresh-1010 check): offline
# ===========================================================================


class TestCheckFindings:
    @pytest.mark.xfail(
        strict=True,
        reason="check O1 (HELD, NOT FIXED): with his stamp line the last success is recorded nowhere "
        "(_last_success, daily.py, reads Cobalt stamps only); needs a store for it — check report DECISIONS",
    )
    def test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line(self, vault, finviz):
        store = MemoryStore()
        refresh(at(5, 15), store)
        edit(vault, table(vault)[0], "as of 06:00 ET · his own words on the stamp")
        finviz.set(SPY=("501.00", "0.20"))
        assert refresh(at(7, 45), store).exit_code == 0
        assert line_of(vault, "| SPY") == row("SPY", "501.00", "0.20")
        finviz.dead = True
        result = refresh(at(8, 15), store)
        assert "SPY cobalt-degraded (finviz fetch failed; values as of 07:45)" in result.status_line

    @pytest.mark.xfail(
        strict=True,
        reason="check O2/B1: a refresh-created note on a dead source takes the shared create render's FAILED "
        "cells (daily.py:134-143; FINAL :100 and [F-01] keep that render); D1 forbids FAILED in the unit — "
        "returns to him (check report DECISIONS)",
    )
    def test_check_o2_a_refresh_created_note_on_a_dead_source_carries_no_failed_token(self, vault, finviz):
        store = MemoryStore()
        finviz.dead = True
        first = refresh(at(5, 45), store)
        assert first.action == "created" and first.exit_code == 1
        assert "FAILED" not in unit_body(vault, "trading", "market_table")

    def test_o1_a_manual_owned_spy_is_not_fetched_into_an_absent_note(
        self, vault, finviz, monkeypatch
    ):
        from cobalt.prefill.config import DailyRefreshConfig

        cfg = DailyRefreshConfig(
            units=["trading/market_table", "market_calendar/market_calendar"],
            fields={
                "SPY": "manual",
                "QQQ": "cobalt",
                "IWM": "cobalt",
                "VIX": "manual",
                "BTC": "manual",
            },
        )
        monkeypatch.setattr(daily_module, "load_daily_refresh_config", lambda: cfg)

        result = refresh(at(5, 15), MemoryStore())

        assert result.flags["SPY"] == MANUAL
        assert f"| SPY | {MANUAL} | {MANUAL} |" in table(vault)
        assert finviz.line("SPY") not in table(vault)

    def test_a4_the_created_day_mode_stamp_and_day_are_the_callers_when(self, vault, finviz, monkeypatch):
        """Check A4 (fix round): the create render's day-mode block takes the
        caller's aware `when` — its stamp and the day it reads — never the
        wall clock."""
        import importlib

        from cobalt.daymode import config as daymode_config
        from cobalt.daymode import note as daymode_note
        from cobalt.daymode import store as daymode_store
        from cobalt.prefill.daily import format_stamp

        # the module, not the package attribute of the same name
        daymode_propose = importlib.import_module("cobalt.daymode.propose")

        seen = {}

        class _Store:
            def ensure_schema(self):
                return None

            def for_date(self, day):
                seen["day"] = day
                return None

        def _render_body(cfg, mode, *, stage, attested=None, row=None, when):
            return f"{format_stamp(when)}\n\n**Day mode: {mode.upper()}** (fixture)"

        monkeypatch.setattr(daily_module, "build_sheet_mode_block", REAL_SHEET_MODE_BLOCK)
        monkeypatch.setattr(daymode_config, "load_daymode_config", lambda: SimpleNamespace())
        monkeypatch.setattr(daymode_store, "DayModeStore", _Store)
        monkeypatch.setattr(daymode_propose, "decided_or_stage1", lambda row, cfg: "reduced")
        monkeypatch.setattr(daymode_note, "render_body", _render_body)

        refresh(at(23, 30), MemoryStore())
        body = unit_body(vault, "daymode", "sheet_mode").split("\n")
        assert body[0] == "as of 23:30 ET"
        assert seen["day"] == DAY

    @pytest.mark.xfail(
        strict=True,
        reason="check A3 (HELD, NOT FIXED; same cause as O1): with his stamp line the last success is "
        "recorded nowhere; needs a store for it — check report DECISIONS",
    )
    def test_t5_a_human_stamp_still_retains_the_last_success_time_after_ten_writes(
        self, vault, finviz
    ):
        store = MemoryStore()
        refresh(at(5, 15), store)
        edit(vault, table(vault)[0], "as of 06:00 ET · his own stamp words")

        for n in range(11):
            minute = 15 if n % 2 == 0 else 45
            hour = 6 + n // 2
            finviz.set(SPY=(f"{510 + n}.00", "0.10"))
            assert refresh(at(hour, minute), store).exit_code == 0

        finviz.dead = True
        result = refresh(at(11, 45), store)

        assert result.exit_code == 1
        assert (
            "SPY cobalt-degraded (finviz fetch failed; values as of 11:15)"
            in result.status_line
        )


@requires_db
class TestCheckFindingsDb:
    def test_t8_an_absent_note_create_race_rereads_the_winner(
        self, vault, finviz, db_store, monkeypatch
    ):
        real_writer = daily_module.VaultWriter
        state = {"fired": False}

        def create_the_winner(path):
            if state["fired"]:
                return
            state["fired"] = True
            VaultWriter("aset.daily_note", store=db_store).create_if_absent(
                path, "# his race-winning note\n"
            )

        def writer_factory(*args, **kwargs):
            kwargs["precommit_hook"] = create_the_winner
            return real_writer(*args, **kwargs)

        monkeypatch.setattr(daily_module, "VaultWriter", writer_factory)

        result = refresh(at(5, 15), db_store)

        assert state["fired"]
        assert result.exit_code == 0
        assert "# his race-winning note" in vault.read_text(encoding="utf-8")
        assert finviz.line("SPY") in table(vault)

    def test_x2_a_human_duplicate_spy_row_makes_the_spy_flag_human(
        self, vault, finviz, db_store
    ):
        refresh(at(5, 15), db_store)
        spy = line_of(vault, "| SPY")
        edit(vault, spy, spy + "\n| SPY | his duplicate |")

        result = refresh(at(6, 15), db_store)

        assert table(vault).count("| SPY | his duplicate |") == 1
        assert result.flags["SPY"] == "human"
        assert "SPY human" in result.status_line

    def test_t5_a_calendar_source_failure_exits_nonzero_when_his_unit_is_preserved(
        self, vault, finviz, db_store, monkeypatch
    ):
        refresh(at(5, 15), db_store)
        original = unit_body(
            vault, "market_calendar", "market_calendar"
        ).splitlines()[-1]
        edit(vault, original, "- 09:45 ET — his calendar")

        async def failed_calendar(*args, **kwargs):
            raise PrefillFetchError(
                "calendar/economic fetch failed: constructed outage"
            )

        monkeypatch.setattr(
            daily_module, "fetch_economic_events", failed_calendar
        )

        result = refresh(at(6, 15), db_store)

        assert unit_body(
            vault, "market_calendar", "market_calendar"
        ).endswith("- 09:45 ET — his calendar")
        assert result.flags["calendar"] == "human"
        assert result.exit_code == 1
        assert "calendar" in result.summary()

    def test_b5_a_refresh_created_note_is_byte_identical_to_prefill_daily(
        self, vault, finviz, db_store, monkeypatch
    ):
        """Check B5 (fix round, pinned): the note refresh creates — the rules
        unit's sizing text and the daily stop included — is the one shared
        create render, byte for byte what `prefill daily` writes ([F-01])."""
        import asyncio

        from cobalt.prefill.daily import read_rules_read_only, run_daily_prefill

        refresh(at(5, 15), db_store)
        by_refresh = vault.read_text(encoding="utf-8")
        vault.unlink()
        monkeypatch.setattr(daily_module, "regenerate_rules_config", read_rules_read_only)
        result = asyncio.run(run_daily_prefill(at(5, 15)))
        assert result.action == "created"
        assert vault.read_text(encoding="utf-8") == by_refresh
        assert "half / $30 full" in by_refresh

