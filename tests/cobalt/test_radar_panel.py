"""Offline contract tests for the S2-P3 read-only Trade Radar panel."""

from __future__ import annotations

import copy
import json
import os
import re
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from typing import ClassVar
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient

from cobalt.aset import radar_panel as panel
from cobalt.aset import web as web_module
from cobalt.cards import CardState
from cobalt.radar.store import RadarStore
from cobalt.session.models import Session

FIXTURES = Path(__file__).parents[1] / "fixtures" / "radar"
POOL_FIXTURE = json.loads((FIXTURES / "panel-pool.real-shape.json").read_text())
BLOCK_FIXTURE = json.loads((FIXTURES / "panel-pool-block.real-shape.json").read_text())
CARD_FIXTURE = json.loads((FIXTURES / "panel-cards.contract.json").read_text())
ET = ZoneInfo("America/New_York")
NOW = datetime(2026, 1, 5, 16, 1, tzinfo=UTC)


class FakeClock:
    def __init__(self, current: Session = Session.RTH):
        self.current = current

    def to_et(self, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("naive")
        return value.astimezone(ET)

    def session(self, _value: datetime) -> Session:
        return self.current


class FakeRadarStore:
    def __init__(self, pool_row=None, members=None, error: Exception | None = None):
        self.pool = copy.deepcopy(pool_row)
        self.members = copy.deepcopy(members or [])
        self.error = error
        self.requested_day = None

    def pool_row(self, _pool_key):
        if self.error:
            raise self.error
        return copy.deepcopy(self.pool)

    def members_for_day(self, _pool_key, trade_date):
        self.requested_day = trade_date
        return copy.deepcopy(self.members)


class FakeSettingsStore:
    def __init__(self, values=None, error: Exception | None = None):
        self._values = copy.deepcopy(values if values is not None else _block_values())
        self.error = error

    def values(self):
        if self.error:
            raise self.error
        return copy.deepcopy(self._values)


class FakeCardStore:
    def __init__(self, rows=None, error: Exception | None = None):
        self.rows = rows or []
        self.error = error

    def radar_board_cards(self, _trade_date):
        if self.error:
            raise self.error
        return copy.deepcopy(self.rows)


def _block_values():
    return copy.deepcopy({row["key"]: row["value"] for row in BLOCK_FIXTURE})


def _tunables(value=60):
    return lambda: SimpleNamespace(by_key={"radar.scan_interval": SimpleNamespace(value=value)})


def _small_snapshot():
    admitted = [row for row in POOL_FIXTURE["membership"] if row["entered_at"] is not None]
    excluded = [
        row
        for row in POOL_FIXTURE["membership"]
        if row["entered_at"] is None
        and row["left_at"] is not None
        and datetime.fromisoformat(row["left_at"]) < NOW
    ]
    current = copy.deepcopy(admitted[0])
    current["left_at"] = None
    current["closed_scan_id"] = None
    departed = copy.deepcopy(next(row for row in admitted[1:] if row["excluded_by"] is not None))
    never_admitted = copy.deepcopy(excluded[0])
    # The hub-cut fixture predates 0008. The store's query selects both
    # columns since S2-P4, and every episode scanned before the deploy
    # holds NULL in them (R1: no backfill) — that is the shape given here.
    for row in (current, departed, never_admitted):
        row.setdefault("rank_metric", None)
        row.setdefault("rank_value", None)
    pool_row = copy.deepcopy(POOL_FIXTURE["pool"])
    pool_row.update(
        members=1,
        session="premarket",
        last_scan_at="2026-01-05 16:00:00+00:00",
        updated_at="2026-01-05 16:00:00+00:00",
    )
    return pool_row, [current, departed, never_admitted]


def _build(
    *,
    since=None,
    snapshot=True,
    clock_session=Session.RTH,
    pool_row=None,
    members=None,
    settings=None,
    now=NOW,
    tunables_loader=None,
    card_store=None,
):
    default_pool, default_members = _small_snapshot()
    store = FakeRadarStore(
        pool_row or default_pool, members if members is not None else default_members
    )
    view = panel.build_radar_panel(
        since=since,
        snapshot=snapshot,
        radar_store=store,
        settings_store=FakeSettingsStore(settings),
        card_store=card_store or FakeCardStore(),
        clock=FakeClock(clock_session),
        now=now,
        tunables_loader=tunables_loader or _tunables(),
    )
    return view, store


def test_store_members_for_day_selects_every_episode_column():
    columns = [
        "id",
        "pool_key",
        "ticker",
        "trade_date",
        "first_seen_at",
        "entered_at",
        "left_at",
        "source",
        "sources",
        "rank_at_entry",
        "last_rank",
        "below_cap_streak",
        "excluded_by",
        "session",
        "opened_scan_id",
        "last_scan_id",
        "closed_scan_id",
        "rank_metric",
        "rank_value",
    ]
    rows = [tuple(range(len(columns)))]

    class Cursor:
        description: ClassVar = [SimpleNamespace(name=name) for name in columns]

        def fetchall(self):
            return rows

    class Conn:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def execute(self, sql, params):
            self.sql, self.params = sql, params
            return Cursor()

    conn = Conn()
    result = RadarStore(connect=lambda: conn).members_for_day("primary", date(2026, 1, 5))
    assert list(result[0]) == columns
    assert "left_at" in conn.sql and "entered_at" in conn.sql
    assert conn.params == ("primary", date(2026, 1, 5))


def test_pool_rows_are_rank_ordered_and_categories_are_distinct():
    view, _ = _build()
    assert [row.position for row in view.pool.current] == sorted(
        row.position for row in view.pool.current
    )
    assert all(row.entered_at is not None and row.left_at is None for row in view.pool.current)
    assert all(row.entered_at is not None and row.left_at is not None for row in view.pool.departed)
    assert all(row.entered_at is None for row in view.pool.excluded)
    assert len(view.pool.current) == view.pool.members == 1


def test_real_shape_episode_ids_distinguish_exclusion_promotion_departure_and_reentry():
    grouped = {}
    for row in POOL_FIXTURE["membership"]:
        grouped.setdefault(row["ticker"], []).append(row)
    episodes = next(
        rows
        for rows in grouped.values()
        if len(rows) >= 3
        and any(row["entered_at"] is None for row in rows)
        and sum(row["entered_at"] is not None for row in rows) >= 2
    )
    ids = [row["id"] for row in episodes]
    assert len(ids) == len(set(ids))
    assert any(row["entered_at"] is None and row["left_at"] is not None for row in episodes)
    assert (
        sum(row["entered_at"] is not None and row["left_at"] is not None for row in episodes) >= 2
    )


def test_pre_deploy_null_value_renders_dash():
    view, _ = _build()
    row = view.pool.current[0]
    assert (row.rank_metric, row.rank_value) == (None, None)
    rendered = panel.render_pool(view.pool)
    cell = re.search(
        rf'<tr data-episode-id="{row.episode_id}"[^>]*>(.*?)</tr>', rendered
    ).group(1)
    assert '<td class="mono rank-value">—</td>' in cell


def test_pool_view_shows_value_beside_metric_name():
    """R1-19: query row -> MembershipRecord -> PoolRow -> HTML, with the
    per-row metric name (a screen override's name, not the session's)."""
    pool_row, members = _small_snapshot()
    members[0].update(rank_metric="volume", rank_value=Decimal("1234567.000000"))
    members[1].update(rank_metric="rvol", rank_value=Decimal("3.250000"))
    view, _ = _build(pool_row=pool_row, members=members)
    assert view.pool.rank_metric == "volume"  # the stored premarket session metric
    current, departed = view.pool.current[0], view.pool.departed[0]
    assert (current.rank_metric, current.rank_value) == ("volume", Decimal("1234567.000000"))
    assert (departed.rank_metric, departed.rank_value) == ("rvol", Decimal("3.250000"))
    rendered = panel.render_pool(view.pool)
    assert '<td class="mono rank-value">volume 1234567</td>' in rendered
    assert '<td class="mono rank-value">rvol 3.25</td>' in rendered
    assert "<th>value</th>" in rendered


def test_membership_row_without_the_value_columns_fails_loud():
    """The columns are selected on every read; a row missing them is a
    store that forgot them, not a pre-deploy NULL."""
    pool_row, members = _small_snapshot()
    del members[0]["rank_value"]
    with pytest.raises(panel.RadarPanelError, match="invalid radar membership row"):
        _build(pool_row=pool_row, members=members)


def test_departed_rows_render_left_time_reason_and_episode_id():
    view, _ = _build()
    row = view.pool.departed[0]
    rendered = panel.render_pool(view.pool)
    assert f'data-episode-id="{row.episode_id}"' in rendered
    assert row.left_at.isoformat(timespec="seconds") in rendered
    assert row.excluded_by and row.excluded_by in rendered


def test_initial_snapshot_has_no_churn_and_embeds_observed_watermark():
    view, _ = _build()
    assert view.pool.churn is None
    rendered = panel.render_pool(view.pool)
    assert 'id="churn"' not in rendered
    assert view.pool.observed_watermark.isoformat() in rendered


def test_churn_is_strictly_after_since_and_counts_admitted_transitions_only():
    pool_row, members = _small_snapshot()
    entered = datetime.fromisoformat(members[0]["entered_at"])
    view, _ = _build(
        since=entered - timedelta(microseconds=1),
        snapshot=False,
        pool_row=pool_row,
        members=members,
    )
    assert members[0]["id"] in view.pool.churn.entered_episode_ids
    assert members[2]["id"] not in view.pool.churn.entered_episode_ids
    equal, _ = _build(
        since=entered,
        snapshot=False,
        pool_row=pool_row,
        members=members,
    )
    assert members[0]["id"] not in equal.pool.churn.entered_episode_ids


def test_delayed_commit_cursor_is_observed_data_not_http_response_time_and_retries():
    pool_row, members = _small_snapshot()
    since = datetime.fromisoformat(members[0]["entered_at"]) - timedelta(seconds=1)
    first, _ = _build(since=since, snapshot=False, pool_row=pool_row, members=members, now=NOW)
    retry, _ = _build(
        since=since,
        snapshot=False,
        pool_row=pool_row,
        members=members,
        now=NOW + timedelta(seconds=30),
    )
    assert first.pool.churn == retry.pool.churn
    assert first.pool.observed_watermark < NOW


@pytest.mark.parametrize(
    "clock_session",
    [Session.PREMARKET, Session.RTH, Session.AFTERMARKET, Session.MARKET_RESET, Session.OVERNIGHT],
)
def test_clock_session_boundaries_do_not_drive_stored_metric(clock_session):
    view, _ = _build(clock_session=clock_session)
    assert view.pool.clock_session is clock_session
    assert view.pool.rank_metric == "volume"


@pytest.mark.parametrize(
    ("scan_session", "metric"),
    [("premarket", "volume"), ("rth", "rvol"), ("aftermarket", "volume")],
)
def test_metric_name_comes_from_stored_scan_session(scan_session, metric):
    pool_row, members = _small_snapshot()
    pool_row["session"] = scan_session
    view, _ = _build(pool_row=pool_row, members=members)
    assert view.pool.rank_metric == metric
    assert "day_scan first from 10:00" in view.pool.override_labels


def test_membership_day_is_derived_from_last_scan_et_date():
    pool_row, members = _small_snapshot()
    view, store = _build(pool_row=pool_row, members=members)
    assert store.requested_day == date(2026, 1, 5)
    assert view.pool.data_date == date(2026, 1, 5)


def test_midnight_retains_and_labels_prior_trading_day():
    pool_row, members = _small_snapshot()
    now = datetime(2026, 1, 6, 5, 5, tzinfo=UTC)
    view, store = _build(
        pool_row=pool_row, members=members, now=now, clock_session=Session.OVERNIGHT
    )
    assert store.requested_day == date(2026, 1, 5)
    assert view.pool.retained_prior_day
    assert "RETAINED PRIOR-DAY DATA" in panel.render_pool(view.pool)


def test_stale_threshold_and_refresh_interval_are_config_driven():
    pool_row, members = _small_snapshot()
    now = datetime.fromisoformat(pool_row["last_scan_at"]) + timedelta(seconds=121)
    view, _ = _build(pool_row=pool_row, members=members, now=now, tunables_loader=_tunables(60))
    assert view.pool.stale and view.pool.scan_interval == 60
    assert "older than 120 seconds" in panel.render_pool(view.pool)


def test_degraded_banner_names_sources_and_escapes_them():
    pool_row, members = _small_snapshot()
    pool_row["degraded"] = True
    pool_row["degraded_sources"] = [
        {"source": "<bad>&", "reason": "down", "since": pool_row["last_scan_at"]}
    ]
    view, _ = _build(pool_row=pool_row, members=members)
    rendered = panel.render_pool(view.pool)
    assert "DEGRADED" in rendered and "&lt;bad&gt;&amp;" in rendered
    assert "<bad>" not in rendered


@pytest.mark.parametrize(
    "case",
    ["missing_pool", "failed_stage", "missing_setting", "bad_block", "bad_status", "missing_scan"],
)
def test_required_pool_inputs_fail_loud_independently(case):
    pool_row, members = _small_snapshot()
    settings = _block_values()
    if case == "missing_pool":
        pool_row = None
    elif case == "failed_stage":
        pool_row["failed_stage"] = "bars"
        pool_row["failed_detail"] = "poll broke"
    elif case == "missing_setting":
        settings = {}
    elif case == "bad_block":
        settings["radar.pool"]["block"]["cap"] = 0
    elif case == "bad_status":
        settings["radar.pool"]["status"] = "parse_failed"
        settings["radar.pool"]["error"] = "bad note"
    elif case == "missing_scan":
        pool_row["last_scan_at"] = None
    with pytest.raises(panel.RadarPanelError, match="FAILED"):
        panel.build_pool_view(
            since=None,
            snapshot=True,
            radar_store=FakeRadarStore(pool_row, members),
            settings_store=FakeSettingsStore(settings),
            clock=FakeClock(),
            now=NOW,
            tunables_loader=_tunables(),
        )


@pytest.mark.parametrize(
    ("radar_store", "settings_store", "tunables_loader", "message"),
    [
        (
            FakeRadarStore(error=RuntimeError("pool boom")),
            FakeSettingsStore(),
            _tunables(),
            "pool read",
        ),
        (
            FakeRadarStore(*_small_snapshot()),
            FakeSettingsStore(error=RuntimeError("settings boom")),
            _tunables(),
            "settings read",
        ),
        (
            FakeRadarStore(*_small_snapshot()),
            FakeSettingsStore(),
            lambda: (_ for _ in ()).throw(RuntimeError("config boom")),
            "tunables read",
        ),
    ],
)
def test_read_and_config_exceptions_fail_loud(
    radar_store, settings_store, tunables_loader, message
):
    with pytest.raises(panel.RadarPanelError, match=message):
        panel.build_pool_view(
            since=None,
            snapshot=True,
            radar_store=radar_store,
            settings_store=settings_store,
            clock=FakeClock(),
            now=NOW,
            tunables_loader=tunables_loader,
        )


def test_pool_member_count_mismatch_fails_instead_of_rendering_empty():
    pool_row, members = _small_snapshot()
    pool_row["members"] = 50
    with pytest.raises(panel.RadarPanelError, match="open admitted"):
        _build(pool_row=pool_row, members=members)


def test_hub_cut_pool_and_past_day_slice_fail_loud_as_an_inconsistent_snapshot():
    pool_row = copy.deepcopy(POOL_FIXTURE["pool"])
    with pytest.raises(panel.RadarPanelError, match="open admitted"):
        panel.build_pool_view(
            since=None,
            snapshot=True,
            radar_store=FakeRadarStore(pool_row, []),
            settings_store=FakeSettingsStore(),
            clock=FakeClock(Session.PREMARKET),
            now=datetime(2026, 1, 6, 13, 0, tzinfo=UTC),
            tunables_loader=_tunables(),
        )


@pytest.mark.parametrize(
    "value", ["", "not-a-date", "2026-01-05T12:00:00", "2026-01-07T12:00:00+00:00"]
)
def test_parse_since_rejects_missing_malformed_naive_and_future(value):
    with pytest.raises(panel.RadarPanelError):
        panel.parse_since(value, now=NOW)


# The card-shell tests that ran against `panel-cards.contract.json`
# through `CardView.from_contract` moved to `test_radar_panel_cards.py`
# (S2-P2 STEP-8): the adapter is gone and the ladder is specified against
# `"user".radar_cards_v` rows the evaluator produces from the hub-cut bars.


def test_failed_page_escapes_the_error():
    failed = panel.render_failed_page('<failure data-x="bad">')
    assert '<failure data-x="bad">' not in failed and "&lt;failure" in failed


def test_card_source_empty_and_failure_cases():
    assert (
        panel.build_ladder_view(card_store=FakeCardStore(), clock=FakeClock(), now=NOW).empty_message
        == "No radar cards today"
    )
    with pytest.raises(panel.RadarPanelError, match="card read failed"):
        panel.build_ladder_view(
            card_store=FakeCardStore(error=RuntimeError("offline")), clock=FakeClock(), now=NOW
        )
    with pytest.raises(panel.RadarPanelError, match="invalid radar card row"):
        panel.build_ladder_view(card_store=FakeCardStore([{"origin": "radar"}]), clock=FakeClock(), now=NOW)


def test_css_has_exact_responsive_contract_and_phone_frame():
    assert "@media (max-width:1149px)" in panel.PANEL_CSS
    assert "@media (max-width:1150px)" not in panel.PANEL_CSS
    assert "@media (max-width:430px)" in panel.PANEL_CSS
    assert "width:366px" in panel.PANEL_CSS
    view, _ = _build()
    assert 'class="phone-frame"' in panel.render_radar_page(view, phone_frame=True)


def test_refresh_javascript_preserves_ladder_state_and_cursor_on_failure():
    source = panel.PANEL_JS
    assert "oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark" in source
    assert "refresh-failed','stale-data" in source
    assert "REFRESH FAILED" in source
    assert "classList.toggle('open'" in source
    assert "collapseAll" in source and "topTwo" in source
    assert "cursor=" not in source[source.index("catch(error)") :]


@pytest.fixture
def route_view():
    return _build()[0]


def test_routes_use_builder_directly_and_never_sheet_write_helpers(monkeypatch, route_view):
    calls = []
    monkeypatch.setattr(
        web_module, "build_radar_panel", lambda **kwargs: calls.append(kwargs) or route_view
    )
    for name in ("_render", "_daymode_state", "_open_cards_section"):
        monkeypatch.setattr(
            web_module,
            name,
            lambda *args, _name=name, **kwargs: (_ for _ in ()).throw(AssertionError(_name)),
        )
    client = TestClient(web_module.app)
    response = client.get("/radar")
    assert response.status_code == 200 and "POOL VIEW" in response.text
    assert calls == [{"since": None, "snapshot": True}]


def test_routes_are_get_only_on_exact_paths(monkeypatch, route_view):
    monkeypatch.setattr(web_module, "build_radar_panel", lambda **_kwargs: route_view)
    monkeypatch.setattr(web_module, "now_utc", lambda: NOW)
    client = TestClient(web_module.app)
    assert client.post("/radar").status_code == 405
    assert client.post("/api/radar/pool?since=2026-01-05T15:00:00%2B00:00").status_code == 405


def test_api_rejects_missing_malformed_naive_and_future_before_builder(monkeypatch):
    monkeypatch.setattr(web_module, "now_utc", lambda: NOW)
    monkeypatch.setattr(
        web_module,
        "build_radar_panel",
        lambda **_kwargs: (_ for _ in ()).throw(AssertionError("builder called")),
    )
    client = TestClient(web_module.app)
    for query in (
        "",
        "?since=nope",
        "?since=2026-01-05T12:00:00",
        "?since=2027-01-05T12:00:00%2B00:00",
    ):
        assert client.get("/api/radar/pool" + query).status_code == 422


def test_api_json_and_html_are_from_same_builder_output(monkeypatch, route_view):
    monkeypatch.setattr(web_module, "now_utc", lambda: NOW)
    monkeypatch.setattr(web_module, "build_radar_panel", lambda **_kwargs: route_view)
    client = TestClient(web_module.app)
    response = client.get("/api/radar/pool?since=2026-01-05T15:00:00%2B00:00")
    assert response.status_code == 200
    assert response.json() == panel.pool_api_payload(route_view.pool)


def test_panel_has_no_write_or_focus_stealing_markup(monkeypatch, route_view):
    monkeypatch.setattr(web_module, "build_radar_panel", lambda **_kwargs: route_view)
    rendered = TestClient(web_module.app).get("/radar").text.lower()
    for forbidden in (
        "<form",
        'method="post"',
        "alert(",
        "prompt(",
        "confirm(",
        ".focus(",
        "autofocus",
        'http-equiv="refresh"',
    ):
        assert forbidden not in rendered


def test_sheet_header_links_to_radar():
    source = Path(web_module.__file__).read_text()
    assert '<a href="/radar">Trade Radar</a>' in source


def _walk_strings(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from _walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_strings(item)
    elif isinstance(value, str):
        yield value


def test_panel_json_fixtures_are_fully_redacted_and_shifted():
    for fixture in (POOL_FIXTURE, BLOCK_FIXTURE, CARD_FIXTURE):
        for value in _walk_strings(fixture):
            assert not re.search(r"@[0-9a-f]{12}\b", value) or "@000000000000" in value
            assert "2026-09-1" not in value


def test_rendered_panel_contains_no_screen_filter_token():
    view, _ = _build()
    rendered = panel.render_radar_page(view)
    assert not re.search(r"\bf=[a-z0-9_,.-]+", rendered)


requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: radar read-layer integration needs cobalt_dev",
)


@pytest.mark.integration
@pytest.mark.usefixtures("dev_db_tx")
@requires_db
def test_members_for_day_db_returns_both_open_and_left_and_scopes_pool_and_day():
    store = RadarStore("cobalt_dev")
    target_day = date(2040, 1, 3)
    with store._connect() as conn:
        conn.execute(
            "INSERT INTO radar_pool (pool_key,state,session,cap,members) VALUES (%s,'scanning','rth',2,1)",
            ("panel_test",),
        )
        for ticker, day, left_at, scan_id in (
            ("OPEN", target_day, None, 9400001),
            ("LEFT", target_day, datetime(2040, 1, 3, 15, 1, tzinfo=UTC), 9400002),
            ("OTHERDAY", date(2040, 1, 4), None, 9400003),
        ):
            conn.execute(
                "INSERT INTO radar_membership (pool_key,ticker,trade_date,first_seen_at,entered_at,left_at,source,sources,rank_at_entry,last_rank,excluded_by,session,opened_scan_id,last_scan_id,closed_scan_id) "
                "VALUES (%s,%s,%s,%s,%s,%s,'test','[\"test\"]'::jsonb,1,1,%s,'rth',%s,%s,%s)",
                (
                    "panel_test",
                    ticker,
                    day,
                    datetime(2040, 1, 3, 15, 0, tzinfo=UTC),
                    datetime(2040, 1, 3, 15, 0, tzinfo=UTC),
                    left_at,
                    "config_cap" if left_at else None,
                    scan_id,
                    scan_id,
                    scan_id if left_at else None,
                ),
            )
    rows = store.members_for_day("panel_test", target_day)
    assert {row["ticker"] for row in rows} == {"OPEN", "LEFT"}
    assert any(row["left_at"] is None for row in rows)
    assert any(row["left_at"] is not None for row in rows)
