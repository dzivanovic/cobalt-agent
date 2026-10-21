"""F5 — market-context checkpoints, offline (card 731, F5 FINAL F5-1, split A).

Every new name is imported INSIDE each test (`CheckpointsConfig`,
`cobalt.prefill.checkpoints`), never at module top, so each test is red on
BASE on its own (the F4 file's rule, `test_prefill_refresh.py:4-6`).

Every vault is a `tmp_path` vault (L28) built by F4's `vault` fixture;
Finviz, the radar plan, the model and the DM are fakes at the module seam
(no network); `vault_writes` is F4's `MemoryStore` and `market_checkpoints`
is `MemoryCheckpoints` below. The Groups body is the SYNTHETIC-shape
fixture of card DECISION 2 (`fixtures/checkpoints/groups_sector_v140.csv`,
X2's real capture owed before load). Constructed figures and notes only
(L32); the sector names are Finviz's public eleven.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow
from cobalt.radar import notes as radar_notes
from cobalt.session.clock import ET
from cobalt.vaultwrite.markers import find_section

from test_prefill_refresh import MemoryStore, finviz, plan, vault  # noqa: F401 — F4's fixtures

FIXTURES = Path(__file__).parent / "fixtures" / "checkpoints"
DAY = date(2026, 9, 3)
SECTION = "market_context"
SECTORS = (
    "Basic Materials", "Communication Services", "Consumer Cyclical", "Consumer Defensive", "Energy",
    "Financial", "Healthcare", "Industrials", "Real Estate", "Technology", "Utilities",
)

NOTE = """---
date: constructed
---
## Today's Plan
### Trading
| constructed table |

### Market Context:
- my read: constructed words he typed
a second constructed line of his

### Market Calendar:
constructed calendar text
"""


def at(hh: int, mm: int, day: date = DAY) -> datetime:
    return datetime(day.year, day.month, day.day, hh, mm, tzinfo=ET)


def groups_csv() -> str:
    """The synthetic fixture, its one `#` marker line dropped."""
    text = (FIXTURES / "groups_sector_v140.csv").read_text(encoding="utf-8")
    return "\n".join(line for line in text.split("\n") if not line.startswith("#"))


def sector_figures(changes: dict[str, str]) -> dict:
    return {n: {"change": c, "rel_volume": "1.00", "perf_week": "0.50"} for n, c in changes.items()}


def figures(indices: dict[str, tuple[str, str]] | None, sectors: dict[str, str] | None) -> dict:
    return {
        "indices": None if indices is None else {t: {"price": p, "change_pct": c} for t, (p, c) in indices.items()},
        "sectors": None if sectors is None else sector_figures(sectors),
    }


BASE_SECTORS = {n: f"{i / 10:.2f}" for i, n in enumerate(SECTORS)}  # Basic Materials 0.00 … Utilities 1.00


def unit_body(path: Path, unit: str) -> str | None:
    lines = path.read_text(encoding="utf-8").split("\n")
    block = find_section(lines, SECTION)
    if block is None or unit not in block.units:
        return None
    return "\n".join(block.units[unit].body(lines))


def without_section(text: str) -> str:
    lines = text.split("\n")
    block = find_section(lines, SECTION)
    if block is None:
        return text
    return "\n".join(lines[: block.open_line] + lines[block.close_line + 1:])


# ---------------------------------------------------------------------------
# Fakes: the checkpoint store, the sources, the model, the DM
# ---------------------------------------------------------------------------


class MemoryCheckpoints:
    """`CheckpointStore`'s surface, in memory: upsert by (trade_date, slot)."""

    def __init__(self):
        self.rows: dict[tuple, dict] = {}
        self.next_id = 1

    def get(self, trade_date, slot):
        row = self.rows.get((trade_date, slot))
        return None if row is None else json.loads(json.dumps(row))

    def slots_on(self, trade_date):
        return {s for (d, s) in self.rows if d == trade_date}

    def upsert(self, trade_date, slot, **fields):
        row = self.rows.get((trade_date, slot))
        if row is None:
            row = {"id": self.next_id, "trade_date": str(trade_date), "slot": slot}
            self.next_id += 1
            self.rows[(trade_date, slot)] = row
        row.update(json.loads(json.dumps(fields, default=str)))
        return row["id"]

    def update(self, trade_date, slot, **fields):
        self.rows[(trade_date, slot)].update(json.loads(json.dumps(fields, default=str)))


def reply(*lines) -> str:
    return json.dumps({"lines": [{"phrase_id": p, "refs": list(r)} for p, r in lines]})


@pytest.fixture
def cp(monkeypatch, vault, plan):  # noqa: F811
    """The checkpoint world: a constructed note on disk, every seam faked."""
    from cobalt.prefill import checkpoints

    vault.write_text(NOTE, encoding="utf-8")
    state = SimpleNamespace(
        gets=0, index_dead=None, groups_dead=None,
        indices={"SPY": ("500.00", "0.10"), "QQQ": ("400.00", "0.20"), "IWM": ("200.00", "0.30")},
        sectors=dict(BASE_SECTORS),
        reply=None, error=None, calls=[], on_call=None,
        dms=[], rpm=10.0, rpm_error=None,
        store=MemoryCheckpoints(), vstore=MemoryStore(), note=vault,
    )

    async def market(tickers=None):
        state.gets += 1
        if state.index_dead:
            raise PrefillFetchError(state.index_dead)
        return [MarketRow(ticker=t, price=Decimal(p), change_pct=Decimal(c)) for t, (p, c) in state.indices.items()]

    async def groups(params):
        state.gets += 1
        if state.groups_dead:
            raise PrefillFetchError(state.groups_dead)
        return sector_figures(state.sectors)

    def model(req, *, config=None):
        state.calls.append(req)
        if state.on_call is not None:
            state.on_call(req)
        if state.error is not None:
            from cobalt.modelaccess import ModelCallError

            raise ModelCallError(state.error, route=req.route, caller=req.caller, request_id=req.request_id,
                                 detail="fixture")
        from datetime import timezone

        from cobalt.modelaccess.models import ModelResult, Usage

        content = state.reply
        if content is None:  # the default model names the leader line it was sent, else the first line
            sent = json.loads(req.messages[-1].content)
            pick = next((e for e in sent if e["phrase"] == "leader"), sent[0])
            content = reply((pick["phrase"], [pick["ref"]]))
        return ModelResult(route=req.route, caller=req.caller, request_id=req.request_id, lane="local",
                           kind="openai_compatible", model_returned="constructed-model", content=content,
                           think_block="absent", finish_reason="stop", usage=Usage(), latency_ms=1,
                           at=datetime(2026, 9, 3, 12, 0, tzinfo=timezone.utc))

    def planned_rpm():
        if state.rpm_error is not None:
            raise state.rpm_error
        return state.rpm

    def dm(message, **kw):
        from cobalt.notify.result import SendResult

        state.dms.append(message)
        return SendResult(True, "fixture DM")

    monkeypatch.setattr(checkpoints, "fetch_market_table", market)
    monkeypatch.setattr(checkpoints, "fetch_groups", groups)
    monkeypatch.setattr(checkpoints, "call_sync", model)
    monkeypatch.setattr(checkpoints, "radar_planned_rpm", planned_rpm)
    monkeypatch.setattr(checkpoints, "send_dm", dm)
    return state


def run(cp, slot: str, when: datetime, *, dry_run: bool = False, calendar=None):
    from cobalt.prefill.checkpoints import run_checkpoint

    return run_checkpoint(slot, when, dry_run=dry_run, store=cp.store, vault_store=cp.vstore, calendar=calendar)


# ===========================================================================
# K1 — the config (FINAL §4 Config, [F-09]; L10)
# ===========================================================================

GOOD_BLOCK = {
    "slots": ["07:15", "07:45", "08:15", "08:45"],
    "source": "ruling",
    "indices": ["SPY", "QQQ", "IWM"],
    "groups": {"g": "sector", "v": 140},
    "route": "checkpoint.narrative",
    "narrative_max_lines": 3,
    "section": "market_context",
    "heading": "### Market Context:",
}


def _cfg_file(tmp_path, block) -> Path:
    import yaml

    path = tmp_path / "prefill.yaml"
    path.write_text(yaml.safe_dump({"checkpoints": block}))
    return path


class TestConfig:
    def test_config_loads_the_committed_block(self):
        from cobalt.prefill.config import CheckpointsConfig, load_checkpoints_config

        cfg = load_checkpoints_config()
        assert isinstance(cfg, CheckpointsConfig)
        assert cfg.model_dump() == GOOD_BLOCK

    @pytest.mark.parametrize(
        "change",
        ["unknown:grace_min", *(f"missing:{k}" for k in GOOD_BLOCK)],
    )
    def test_unknown_key_and_missing_key_crash(self, tmp_path, change):
        from cobalt.prefill.config import PrefillConfigError, load_checkpoints_config

        kind, key = change.split(":")
        block = dict(GOOD_BLOCK)
        if kind == "unknown":
            block[key] = 30
        else:
            del block[key]
        with pytest.raises(PrefillConfigError):
            load_checkpoints_config(_cfg_file(tmp_path, block))

    def test_prefill_block_is_untouched(self):
        from cobalt.prefill.config import CheckpointsConfig, load_prefill_paths  # noqa: F401 — red on BASE

        assert load_prefill_paths().model_dump() == {
            "trades_dir": "1 - Trading/2 - Trades",
            "review_dir": "1 - Trading/5 - Review",
            "drc_filename_pattern": "DRC-%Y-%m-%d.md",
            "trade_filename_pattern": "Trade-%Y-%m-%d %H-%M-%S -{ticker}.md",
            "drc_template": "5 - Templates/DRC.md",
        }


# ===========================================================================
# K2 — the numbers (FINAL §2.2, [F-03]; L3, L9)
# ===========================================================================


class _FakeResponse:
    def __init__(self, text: str, status_code: int = 200):
        self.text, self.status_code = text, status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            request = httpx.Request("GET", "https://elite.finviz.com/export/groups")
            raise httpx.HTTPStatusError("error", request=request,
                                        response=httpx.Response(self.status_code, request=request))


def _fake_client(text: str, seen: list):
    class _Client:
        def __init__(self, *a, **kw):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def get(self, url, params=None):
            seen.append((url, dict(params or {})))
            return _FakeResponse(text)

    return _Client


@pytest.fixture
def groups_http(monkeypatch):
    """`httpx` faked at the module seam; the token is a constructed string."""
    from cobalt.prefill import checkpoints

    async def token():
        return "constructed-token"

    seen: list = []
    state = SimpleNamespace(seen=seen, body=groups_csv())
    monkeypatch.setattr(checkpoints, "resolve_token", token)
    monkeypatch.setattr(httpx, "AsyncClient", lambda *a, **kw: _fake_client(state.body, seen)())
    return state


def _cfg():
    from cobalt.prefill.config import load_checkpoints_config

    return load_checkpoints_config()


class TestNumbers:
    def test_eleven_sector_rows_parse(self, groups_http):
        import asyncio

        from cobalt.prefill.checkpoints import fetch_groups

        sectors = asyncio.run(fetch_groups(_cfg().groups))
        assert sorted(sectors) == sorted(SECTORS)
        assert sectors["Energy"] == {"change": "1.20", "rel_volume": "1.25", "perf_week": "2.30"}
        assert sectors["Utilities"]["change"] == "0.00"
        [(url, params)] = groups_http.seen
        assert url == "https://elite.finviz.com/export/groups"
        assert params == {"g": "sector", "v": "140", "auth": "constructed-token"}

    def test_keep_gets_the_body_before_the_parse(self, groups_http):
        """f5-probe G1: `keep` sees the body as sent, before the parse; the
        result is the no-`keep` call's."""
        import asyncio

        from cobalt.prefill.checkpoints import fetch_groups

        kept: list = []
        with_keep = asyncio.run(fetch_groups(_cfg().groups, keep=kept.append))
        assert kept == [groups_http.body]
        assert with_keep == asyncio.run(fetch_groups(_cfg().groups))
        groups_http.body = "\n".join(line for line in groups_csv().split("\n") if '"Utilities"' not in line)
        with pytest.raises(PrefillFetchError, match="11 sector"):
            asyncio.run(fetch_groups(_cfg().groups, keep=kept.append))
        assert kept[-1] == groups_http.body, "a body the parse refuses still reached keep first"

    def test_ten_row_body_is_a_degraded_groups_source(self, groups_http):
        import asyncio

        from cobalt.prefill.checkpoints import fetch_groups

        groups_http.body = "\n".join(line for line in groups_csv().split("\n") if '"Utilities"' not in line)
        with pytest.raises(PrefillFetchError, match="11 sector"):
            asyncio.run(fetch_groups(_cfg().groups))

    def test_missing_change_is_degraded(self, groups_http):
        import asyncio

        from cobalt.prefill.checkpoints import fetch_groups

        groups_http.body = groups_csv().replace('"1.15","0.90%"', '"1.15",""')
        with pytest.raises(PrefillFetchError, match="Change"):
            asyncio.run(fetch_groups(_cfg().groups))

    def test_index_fetch_dead_sectors_still_render(self, groups_http, monkeypatch):
        from cobalt.prefill import checkpoints

        async def dead(tickers=None):
            raise PrefillFetchError("Finviz screener fetch failed: constructed outage")

        monkeypatch.setattr(checkpoints, "fetch_market_table", dead)
        figs, status = checkpoints.fetch_figures(_cfg())
        assert figs["indices"] is None and sorted(figs["sectors"]) == sorted(SECTORS)
        body = checkpoints.render_body(at(7, 45), figs, status, checkpoints.compute_delta(figs, None), None)
        assert "degraded: finviz-screener — Finviz screener fetch failed: constructed outage" in body
        assert "Energy +1.20%" in body
        assert body.split("\n")[0].endswith(" cobalt-degraded")

    def test_groups_dead_indices_still_render(self, groups_http, monkeypatch):
        from cobalt.prefill import checkpoints

        async def market(tickers=None):
            return [MarketRow(ticker=t, price=Decimal("100.00"), change_pct=Decimal("0.50")) for t in tickers]

        groups_http.body = ""
        monkeypatch.setattr(checkpoints, "fetch_market_table", market)
        figs, status = checkpoints.fetch_figures(_cfg())
        assert figs["sectors"] is None and list(figs["indices"]) == ["SPY", "QQQ", "IWM"]
        body = checkpoints.render_body(at(7, 45), figs, status, checkpoints.compute_delta(figs, None), None)
        assert "degraded: finviz-groups — " in body
        assert "SPY 100.00 +0.50%" in body
        assert body.strip()


# ===========================================================================
# K3 — the delta (FINAL §2.4, [F-15], [F-06])
# ===========================================================================

IDX_0745 = {"SPY": ("500.00", "0.10"), "QQQ": ("400.00", "0.20"), "IWM": ("200.00", "0.30")}
IDX_0815 = {"SPY": ("501.00", "0.30"), "QQQ": ("399.50", "0.08"), "IWM": ("200.00", "0.30")}


def _texts(delta, phrase):
    return [line["text"] for line in delta["lines"] if line["phrase"] == phrase]


class TestDelta:
    def test_rank_moves_0745_to_0815(self):
        from cobalt.prefill.checkpoints import compute_delta

        later = dict(BASE_SECTORS, **{"Basic Materials": "1.50"})  # last (rank 11) → first (rank 1)
        delta = compute_delta(figures(IDX_0815, later), figures(IDX_0745, BASE_SECTORS))
        moves = _texts(delta, "rank_move")
        assert "Basic Materials rank 11 → 1" in moves
        assert "Utilities rank 1 → 2" in moves
        assert len(moves) == 11  # every other name drops one place
        assert _texts(delta, "index_move")[0] == "SPY 500.00 → 501.00 (+1.00), change +0.10% → +0.30%"
        assert "IWM 200.00 → 200.00 (+0.00), change +0.30% → +0.30%" in _texts(delta, "index_move")

    def test_competition_rank_tie_shares_the_lower_rank(self):
        from cobalt.prefill.checkpoints import competition_rank

        ranks = competition_rank({"A": Decimal("1.0"), "B": Decimal("2.0"), "C": Decimal("2.0"), "D": Decimal("0.5")})
        assert ranks == {"B": 1, "C": 1, "A": 3, "D": 4}

    def test_tie_is_not_a_single_leader(self):
        from cobalt.prefill.checkpoints import compute_delta

        tied = dict(BASE_SECTORS, **{"Energy": "1.00"})  # Energy ties Utilities at the top
        delta = compute_delta(figures(IDX_0815, tied), figures(IDX_0745, BASE_SECTORS))
        assert _texts(delta, "leader") == ["leader: Energy, Utilities (+1.00%)"]
        assert _texts(delta, "laggard") == ["laggard: Basic Materials (+0.00%)"]

    def test_name_dropped_at_0815_fails_groups(self):
        from cobalt.prefill.checkpoints import compute_delta

        dropped = {n: c for n, c in BASE_SECTORS.items() if n != "Energy"}
        delta = compute_delta(figures(IDX_0815, dropped), figures(IDX_0745, BASE_SECTORS))
        assert "Energy" in delta["groups_failed"]
        assert not [x for x in delta["lines"] if x["phrase"] in ("rank_move", "leader", "laggard")]
        assert _texts(delta, "index_move"), "the index lines stand alone"

    def test_0715_has_no_rank_move(self):
        from cobalt.prefill.checkpoints import compute_delta

        delta = compute_delta(figures(IDX_0745, BASE_SECTORS), None)
        assert _texts(delta, "rank_move") == []
        assert _texts(delta, "prior_close") == ["SPY 500.00 (+0.10% vs prior close)",
                                                "QQQ 400.00 (+0.20% vs prior close)",
                                                "IWM 200.00 (+0.30% vs prior close)"]
        assert _texts(delta, "leader") == ["leader: Utilities (+1.00%)"]

    def test_no_crossing_field(self):
        from cobalt.prefill.checkpoints import compute_delta

        delta = compute_delta(figures(IDX_0815, BASE_SECTORS), figures(IDX_0745, BASE_SECTORS))
        assert set(delta) == {"lines", "groups_failed"}
        assert {x["phrase"] for x in delta["lines"]} <= {"prior_close", "index_move", "leader", "laggard", "rank_move"}
        assert not any("cross" in json.dumps(x) for x in delta["lines"])

    def test_render_0815_cites_delta_since_0745(self):
        from cobalt.prefill.checkpoints import compute_delta, render_body

        figs = figures(IDX_0815, BASE_SECTORS)
        status = {"finviz-screener": "ok", "finviz-groups": "ok"}
        body = render_body(at(8, 15), figs, status, compute_delta(figs, figures(IDX_0745, BASE_SECTORS)), "07:45")
        lines = body.split("\n")
        start = lines.index("Δ since 07:45:")
        assert lines[start + 1] == "- SPY 500.00 → 501.00 (+1.00), change +0.10% → +0.30%"


# ===========================================================================
# K4 — the narrative (FINAL §2.5, [F-08], D1; L25)
# ===========================================================================

ENTRIES = [
    {"phrase": "index_move", "text": "SPY 500.00 → 501.00 (+1.00), change +0.10% → +0.30%"},
    {"phrase": "leader", "text": "leader: Utilities (+1.00%)"},
]


def _narrate(monkeypatch, content=None, error=None):
    from cobalt.prefill import checkpoints

    calls = []

    def model(req, *, config=None):
        calls.append(req)
        if error is not None:
            from cobalt.modelaccess import ModelCallError

            raise ModelCallError(error, route=req.route, caller=req.caller, request_id=req.request_id, detail="x")
        from datetime import timezone

        from cobalt.modelaccess.models import ModelResult, Usage

        return ModelResult(route=req.route, caller=req.caller, request_id=req.request_id, lane="local",
                           kind="openai_compatible", model_returned="constructed-model", content=content,
                           think_block="absent", finish_reason="stop", usage=Usage(), latency_ms=1,
                           at=datetime(2026, 9, 3, 12, 0, tzinfo=timezone.utc))

    monkeypatch.setattr(checkpoints, "call_sync", model)
    narrative = checkpoints.narrate(_cfg(), ENTRIES, request_id="2026-09-03-0815")
    return narrative, calls


class TestNarrative:
    def test_valid_phrases_render_only_stored_figures(self, monkeypatch):
        narrative, calls = _narrate(monkeypatch, reply(("index_move", [0]), ("leader", [1])))
        assert narrative.status == "ok"
        assert narrative.lines == ["indices moved: " + ENTRIES[0]["text"], "leading: " + ENTRIES[1]["text"]]
        [req] = calls
        assert req.route == "checkpoint.narrative"
        sent = json.loads(req.messages[-1].content)
        assert sent == [{"ref": i, **e} for i, e in enumerate(ENTRIES)], "the input is the delta list only"
        assert narrative.input == sent and len(narrative.prompt_sha256) == 64

    def test_digit_in_model_string_degrades(self, monkeypatch):
        from cobalt.prefill.checkpoints import UnsourcedFigure, validate_reply

        bad = json.dumps({"lines": [{"phrase_id": "leader", "refs": [1], "note": "up 2"}]})
        narrative, _ = _narrate(monkeypatch, bad)
        assert narrative.status == "degraded (unsourced figure)" and narrative.lines == []
        narrative, _ = _narrate(monkeypatch, json.dumps({"lines": [{"phrase_id": "leader2", "refs": [1]}]}))
        assert narrative.status == "degraded (unsourced figure)"
        # The digit rule itself, before the schema reads the reply (a figure never reaches a renderer).
        for content in (bad, json.dumps({"lines": [{"phrase_id": "leader 2%", "refs": [1]}]})):
            with pytest.raises(UnsourcedFigure, match="a digit in a model string"):
                validate_reply(content, ENTRIES, 3)

    def test_out_of_range_ref_degrades(self, monkeypatch):
        narrative, _ = _narrate(monkeypatch, reply(("leader", [2])))
        assert narrative.status == "degraded (unsourced figure)"
        # A ref to a line of another phrase is a wrong ref (CHECK ASKS X2).
        narrative, _ = _narrate(monkeypatch, reply(("leader", [0])))
        assert narrative.status == "degraded (unsourced figure)"

    def test_bad_phrase_id_degrades(self, monkeypatch):
        narrative, _ = _narrate(monkeypatch, reply(("two_percent", [0])))
        assert narrative.status == "degraded (unsourced figure)"

    @pytest.mark.parametrize("content", ["not json", json.dumps({"lines": "x"}), json.dumps({"lines": [{"refs": [0]}]}),
                                         reply(("leader", [0]), ("laggard", [1]), ("index_move", [0]), ("leader", [1]))])
    def test_schema_failure_degrades(self, monkeypatch, content):
        narrative, _ = _narrate(monkeypatch, content)
        assert narrative.status == "degraded (unsourced figure)"

    @pytest.mark.parametrize("kind", ["timeout", "think_leak", "empty"])
    def test_timeout_think_leak_empty_each_degrade_with_numbers_exit_0(self, cp, kind):
        cp.error = kind
        result = run(cp, "0745", at(7, 45))
        assert result.exit_code == 0
        body = unit_body(cp.note, "checkpoint_0745")
        assert f"narrative: degraded ({kind})" in body
        assert "SPY 500.00 +0.10%" in body
        assert len(cp.calls) == 1, "no retry, no second lane"
        assert cp.store.get(DAY, "07:45")["narrative_status"] == f"degraded ({kind})"

    def test_route_is_loaded_and_local(self):
        from cobalt.modelaccess import load_routes

        route = load_routes().routes["checkpoint.narrative"]
        assert route.lane == "local" and route.model == "mainframe"
        assert route.timeout_s != 15, "never the voice route's 15 s"

    def test_route_budgets_are_measured(self):
        from cobalt.jobs.config import load_job_registry
        from cobalt.modelaccess import load_routes
        from cobalt.modelaccess.config import CONFIG_PATH

        routes = load_routes().routes
        route = routes["checkpoint.narrative"]
        plan = routes["local.plan"]
        # Route.timeout_s is a float field; the file token is the integer.
        lines = CONFIG_PATH.read_text().splitlines()
        start = lines.index("  checkpoint.narrative:")
        block_lines = []
        for line in lines[start:]:
            if block_lines and line and not line.startswith((" ", "#")):
                break
            block_lines.append(line)
        timeout_raw = next(
            ln.split(":", 1)[1].strip() for ln in block_lines if ln.strip().startswith("timeout_s:")
        )
        assert timeout_raw.isdigit()
        timeout_s = int(timeout_raw)
        assert type(timeout_s) is int and timeout_s > 0 and timeout_s % 5 == 0
        assert route.timeout_s == timeout_s
        assert route.timeout_s != plan.timeout_s
        assert type(route.max_output_tokens) is int and route.max_output_tokens % 64 == 0
        for label in (
            "com.cobalt.checkpoint-0715",
            "com.cobalt.checkpoint-0745",
            "com.cobalt.checkpoint-0815",
            "com.cobalt.checkpoint-0845",
        ):
            assert load_job_registry().spec(label).timeout_s > route.timeout_s + 60
        assert "UNMEASURED" not in "\n".join(block_lines)
        source = "# source: X3 reports/f5-x3-measure-2026-10-20.md"
        assert len([ln for ln in block_lines if source in ln]) == 2


# ===========================================================================
# K5 — the unit body (FINAL §2.6, [F-13] need 3)
# ===========================================================================


class TestUnitBody:
    def test_body_stamp_is_the_slot_instant(self, cp):
        run(cp, "0745", at(7, 52))  # the run starts late; the stamp is the slot's
        body = unit_body(cp.note, "checkpoint_0745")
        assert body.split("\n")[0] == "as of 07:45 ET cobalt"

    def test_degraded_source_flags_cobalt_degraded(self, cp):
        cp.groups_dead = "Finviz groups fetch failed: constructed outage"
        result = run(cp, "0745", at(7, 45))
        body = unit_body(cp.note, "checkpoint_0745")
        assert body.split("\n")[0] == "as of 07:45 ET cobalt-degraded"
        assert "degraded: finviz-groups — Finviz groups fetch failed: constructed outage" in body
        assert result.exit_code == 1
        assert "human" not in body.split("\n")[0]

    def test_body_has_no_heading_line(self, cp):
        run(cp, "0715", at(7, 15))
        run(cp, "0745", at(7, 45))
        for unit in ("checkpoint_0715", "checkpoint_0745"):
            assert not [x for x in unit_body(cp.note, unit).split("\n") if x.lstrip().startswith("#")]


# ===========================================================================
# K6 — the table (FINAL §4 Table, [F-04])
# ===========================================================================


class TestTable:
    def test_forward_and_reverse_name_the_new_pair(self):
        from cobalt.db_migrations import FORWARD, REVERSE, MIGRATIONS_DIR

        # F5 card 731 K6: 0029 last, after 0028 (next free at BASE; 469's 0028 is FORWARD[-2] / REVERSE[1]).
        assert [p.name for p in FORWARD[-3:]] == [
            "0026_genesis_chunk.sql", "0028_genesis_vectors.sql", "0029_market_checkpoints.sql"]
        assert [p.name for p in REVERSE[:3]] == [
            "0029_market_checkpoints.rollback.sql", "0028_genesis_vectors.rollback.sql",
            "0026_genesis_chunk.rollback.sql"]
        sql = (MIGRATIONS_DIR / "0029_market_checkpoints.sql").read_text()
        assert "CREATE TABLE IF NOT EXISTS system.market_checkpoints" in sql
        assert "UNIQUE (trade_date, slot)" in sql
        assert "REFERENCES" not in sql, "vault_write_id has no foreign key (vault_writes is purged at 30 days)"
        # CARD.md migration checklist item 4: the apply role's DML and sequence grants, in the same file.
        assert "GRANT SELECT, INSERT, UPDATE, DELETE ON system.market_checkpoints TO cobalt_apply_system;" in sql
        assert "GRANT USAGE ON SEQUENCE system.market_checkpoints_id_seq TO cobalt_apply_system;" in sql
        rollback = (MIGRATIONS_DIR / "0029_market_checkpoints.rollback.sql").read_text()
        assert [x for x in rollback.split("\n") if x and not x.startswith("--")] == [
            "DROP TABLE IF EXISTS system.market_checkpoints;"]

    def test_market_checkpoints_is_system_side(self):
        from cobalt.db import Side
        from cobalt.db_migrations.placement import CREATED_TABLES, side_of
        from cobalt.prefill.checkpoints import CheckpointStore

        assert side_of("market_checkpoints") is Side.SYSTEM
        assert CREATED_TABLES["market_checkpoints"] is Side.SYSTEM
        assert CheckpointStore.SIDE is Side.SYSTEM


# ===========================================================================
# K7 — one run (FINAL §2.7, §2.9–§2.13; split A)
# ===========================================================================


def _holiday_calendar(day: date):
    from cobalt.session.calendar import CalendarDay, CalendarYear, TradingCalendar

    year = CalendarYear(year=day.year, holidays=[CalendarDay(date=day, name="Constructed holiday")])
    return TradingCalendar({day.year: year}, Path("constructed"))


class TestOneRun:
    def test_closed_day_writes_nothing_exit_0(self, cp):
        monday = date(2026, 9, 7)
        assert monday.weekday() == 0
        before = cp.note.read_bytes()
        result = run(cp, "0715", at(7, 15, monday), calendar=_holiday_calendar(monday))
        assert result.exit_code == 0 and result.action == "closed"
        assert cp.gets == 0 and cp.store.rows == {} and cp.vstore.rows == []
        assert cp.note.read_bytes() == before

    def test_0745_at_0820_is_refused_exit_2(self, cp):
        before = cp.note.read_bytes()
        result = run(cp, "0745", at(8, 20))
        assert result.exit_code == 2
        assert "REFUSED: slot 07:45 window closed at 08:15" in result.report()
        assert cp.gets == 0 and cp.store.rows == {} and cp.note.read_bytes() == before

    def test_dry_run_ignores_the_window(self, cp):
        before = cp.note.read_bytes()
        result = run(cp, "0745", at(8, 20), dry_run=True)
        assert result.exit_code == 0 and result.action == "dry_run"
        assert cp.note.read_bytes() == before and cp.store.rows == {} and cp.vstore.rows == []
        assert "checkpoint_0745" in result.report()

    def test_gate_refusal_no_get_exit_1(self, cp, plan):
        from cobalt.prefill.checkpoints import demand_consumer

        plan.ceiling = 50
        cp.rpm = 49.0
        radar_notes.check_total_demand([demand_consumer("07:45")], subject="checkpoint", ceiling=50)  # alone: passes
        result = run(cp, "0745", at(7, 45))
        assert cp.gets == 0, "a refused gate sends no GET"
        assert result.exit_code == 1
        body = unit_body(cp.note, "checkpoint_0745")
        assert "degraded: finviz — demand ceiling" in body
        cp.rpm, cp.rpm_error = None, RuntimeError("radar notes unreadable (fixture)")
        assert run(cp, "0745", at(7, 46)).exit_code == 1 and cp.gets == 0

    def test_missed_0745_unit_and_one_dm(self, cp):
        run(cp, "0715", at(7, 15))
        assert cp.dms == []
        result = run(cp, "0815", at(8, 15))
        assert unit_body(cp.note, "checkpoint_0745") == "MISSED 07:45 — no run recorded"
        assert len(cp.dms) == 1 and "07:45" in cp.dms[0] and "07:15" not in cp.dms[0]
        assert "DM sent" in result.report()
        lines = cp.note.read_text().split("\n")
        units = list(find_section(lines, SECTION).units)
        assert units == ["checkpoint_0715", "checkpoint_0745", "checkpoint_0815"]
        run(cp, "0845", at(8, 45))
        assert len(cp.dms) == 1, "a MISSED unit already on disk is not DM'd again"

    def test_numbers_unit_on_disk_before_the_model_call(self, cp):
        seen = []

        def on_call(req):
            body = unit_body(cp.note, "checkpoint_0745")
            seen.append(body)
            assert body.split("\n")[-1] == "narrative: pending"
            assert "SPY 500.00 +0.10%" in body
            row = cp.store.get(DAY, "07:45")
            assert row["vault_write_id"] is None and row["figures"]["indices"]["SPY"]["price"] == "500.00"

        cp.on_call = on_call
        run(cp, "0745", at(7, 45))
        assert len(seen) == 1
        final = unit_body(cp.note, "checkpoint_0745")
        assert final.split("\n")[-2:] == ["Narrative:", "- leading: leader: Utilities (+1.00%)"]
        assert cp.store.get(DAY, "07:45")["vault_write_id"] is not None

    def test_model_timeout_leaves_the_numbers_unit(self, cp):
        cp.error = "timeout"
        assert run(cp, "0745", at(7, 45)).exit_code == 0
        body = unit_body(cp.note, "checkpoint_0745")
        assert "SPY 500.00 +0.10%" in body and body.split("\n")[-1] == "narrative: degraded (timeout)"

    def test_his_text_under_the_heading_is_byte_identical_after_four_slots(self, cp):
        for slot, (hh, mm) in (("0715", (7, 15)), ("0745", (7, 45)), ("0815", (8, 15)), ("0845", (8, 45))):
            cp.indices["SPY"] = (f"{500 + mm / 100:.2f}", "0.10")
            assert run(cp, slot, at(hh, mm)).exit_code == 0
        text = cp.note.read_text()
        assert without_section(text) == NOTE, "everything outside the section is byte-identical"
        lines = text.split("\n")
        heading = lines.index("### Market Context:")
        block = find_section(lines, SECTION)
        assert block.open_line == heading + 1, "side A: the section sits directly under the heading"
        assert lines[block.close_line + 1] == "- my read: constructed words he typed"
        assert list(block.units) == ["checkpoint_0715", "checkpoint_0745", "checkpoint_0815", "checkpoint_0845"]
        assert {r["section"] for r in cp.vstore.rows} == {SECTION}

    def test_no_heading_appends_at_end_nothing_above_touched(self, cp):
        headless = NOTE.replace("### Market Context:\n", "")
        cp.note.write_text(headless, encoding="utf-8")
        result = run(cp, "0715", at(7, 15))
        assert result.exit_code == 0
        text = cp.note.read_text()
        assert text.startswith(headless.rstrip("\n"))
        assert find_section(text.split("\n"), SECTION).open_line > len(headless.split("\n")) - 2
        assert any("anchor not found" in n for w in result.writes for n in w.notes)

    def test_rerun_same_slot_same_figures_is_zero_diff(self, cp):
        run(cp, "0745", at(7, 45))
        before, rows = cp.note.read_bytes(), len(cp.vstore.rows)
        result = run(cp, "0745", at(7, 50))
        assert result.exit_code == 0
        assert cp.note.read_bytes() == before
        assert len(cp.vstore.rows) == rows, "no vault_writes row: nothing changed"
        assert len(cp.store.rows) == 1

    def test_unwritable_note_failed_dm_exit_1(self, cp, monkeypatch):
        from cobalt.prefill import checkpoints
        from cobalt.vaultwrite import VaultWriteError

        def refuse(*a, **kw):
            raise VaultWriteError("constructed refusal")

        monkeypatch.setattr(checkpoints.VaultWriter, "upsert_unit", refuse)
        result = run(cp, "0745", at(7, 45))
        assert result.exit_code == 1
        assert cp.store.get(DAY, "07:45")["write_status"] == "FAILED"
        assert len(cp.dms) == 1 and "FAILED" in cp.dms[0]
        assert cp.calls == [], "no model call after a failed numbers write"


# ===========================================================================
# K8 — the command (FINAL §2.1, [F-13] need 8; L10)
# ===========================================================================


def _main(monkeypatch, *argv):
    import cobalt.cli

    monkeypatch.setattr("sys.argv", ["cobalt", *argv])
    with pytest.raises(SystemExit) as exc:
        cobalt.cli.main()
        raise SystemExit(0)
    return exc.value.code


class TestCommand:
    def test_the_cli_mounts_checkpoint_run(self, monkeypatch, capsys):
        assert _main(monkeypatch, "checkpoint", "run", "--help") == 0
        out = capsys.readouterr().out
        assert "--slot" in out and "--dry-run" in out

    @pytest.mark.parametrize("slot", ["0800", "745", "07:45", "2515"])
    def test_a_bad_slot_is_refused(self, monkeypatch, capsys, slot):
        assert _main(monkeypatch, "checkpoint", "run", "--slot", slot) != 0
        err = capsys.readouterr().err
        assert "slot" in err

    def test_dead_source_records_exit_1_in_as_job(self, cp, monkeypatch, capsys):
        from cobalt.prefill import checkpoints
        from cobalt.session import clock as clock_mod

        seen = []

        @contextmanager
        def fake_as_job(label, *, skip=False, store=None):
            handle = SimpleNamespace(result=None)
            try:
                yield handle
            except BaseException as e:
                seen.append((label, skip, "exit 1", type(e).__name__))
                raise
            seen.append((label, skip, "exit 0", None))

        monkeypatch.setattr(checkpoints, "as_job", fake_as_job)
        monkeypatch.setattr(checkpoints, "default_stores", lambda: (cp.store, cp.vstore))
        monkeypatch.setattr(clock_mod, "now_utc", lambda: at(7, 45))
        cp.index_dead = "Finviz screener fetch failed: constructed outage"
        assert _main(monkeypatch, "checkpoint", "run", "--slot", "0745") == 1
        assert seen == [("com.cobalt.checkpoint-0745", False, "exit 1", "CheckpointNotClean")]
        assert "degraded: finviz-screener" in capsys.readouterr().out


# ===========================================================================
# K11 — the seam tests (seam §6; F4-FINAL `## SEAM` §6)
# ===========================================================================


def _refresh(when, store):
    from cobalt.prefill.daily import run_daily_refresh

    return run_daily_refresh(when, store=store)


def _section_text(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").split("\n")
    block = find_section(lines, SECTION)
    return "\n".join(lines[block.open_line: block.close_line + 1])


class TestSeam:
    def test_f4_refresh_leaves_market_context_byte_identical(self, cp, finviz):  # noqa: F811
        cp.note.unlink()
        assert _refresh(at(5, 15), cp.vstore).action == "created"  # F4's create path renders the template
        run(cp, "0715", at(7, 15))
        run(cp, "0745", at(7, 45))
        section = _section_text(cp.note)
        finviz.set(SPY=("555.00", "0.90"))
        assert _refresh(at(8, 0), cp.vstore).exit_code == 0
        assert "555.00" in cp.note.read_text(), "the refresh did write its own unit"
        assert _section_text(cp.note) == section

    def test_same_minute_refresh_and_checkpoint_touch_different_units(self, cp, finviz, monkeypatch):  # noqa: F811
        from cobalt.prefill import checkpoints

        cp.note.unlink()
        _refresh(at(5, 15), cp.vstore)
        real = checkpoints.VaultWriter
        state = {"fired": 0, "every": False}

        def hook(path):
            if state["fired"] == 0 or state["every"]:
                state["fired"] += 1
                finviz.set(SPY=(f"{559 + state['fired']}.00", "0.20"))  # a new value each time: a real change
                _refresh(at(7, 45), cp.vstore)  # F4 lands inside the checkpoint's commit window

        def factory(*a, **kw):
            kw["precommit_hook"] = hook
            return real(*a, **kw)

        monkeypatch.setattr(checkpoints, "VaultWriter", factory)
        result = run(cp, "0745", at(7, 45))
        assert result.exit_code == 0 and state["fired"] == 1, "one abort, one retry on the real writer"
        assert "$560.00" in cp.note.read_text() and unit_body(cp.note, "checkpoint_0745") is not None

        state["every"] = True  # a second collision on the retry raises
        result = run(cp, "0815", at(8, 15))
        assert result.exit_code == 1
        assert cp.store.get(DAY, "08:15")["write_status"] == "FAILED"
        assert any("FAILED" in m for m in cp.dms)


# ===========================================================================
# K10 — the Finviz inventory is pinned in test_finviz_consumers.py; this pins
# that the request module is the one CONSUMERS names.
# ===========================================================================


def test_the_groups_request_lives_in_the_inventoried_module():
    from cobalt.prefill import checkpoints

    assert re.search(r"elite\.finviz\.com", Path(checkpoints.__file__).read_text())


# ===========================================================================
# Check O1 (card 731 PORT seam with 469): an embeddings route is a config error
# ===========================================================================


def test_check_o1_an_embeddings_route_is_a_config_error_before_any_fetch(cp, monkeypatch):
    from cobalt.prefill import checkpoints
    from cobalt.prefill.config import PrefillConfigError, load_checkpoints_config

    cfg = load_checkpoints_config().model_copy(update={"route": "local.embed"})
    monkeypatch.setattr(checkpoints, "load_checkpoints_config", lambda *a, **kw: cfg)
    with pytest.raises(PrefillConfigError):
        run(cp, "0745", at(7, 45))
    assert cp.gets == 0
