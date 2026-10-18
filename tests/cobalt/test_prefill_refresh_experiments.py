"""F4 card row A1 — the first-gate experiments, as DATA (L70).

RUN row: every test here PRINTS and asserts nothing. Its BASE run
(`d78c66a2`, before any `src/` edit) is the record in the F4 build
report; at the tip it runs again and still asserts nothing.

  (1) X1's expected-red control — the FINAL §3 trace: a naive repeated
      `upsert_unit` on the trading unit after his SPY edit.
  (2) X6 — `last_after` of both units after a 05:15 create, and
      `_render_template({})` with every key missing.
  (3) X16 — the stub (`stub_template` plus one cards unit): one
      `upsert_unit` of the trading unit, and the same on a stub carrying
      a hand-typed `### Trading` table.
  (4) X17 — `check_total_demand` at planned 49.95 + extra 0.05, ceiling 50.

Every vault is a `tmp_path` vault; the store is `cobalt_dev` inside the
suite's rolled-back transaction. Constructed tickers, prices and dates
only (L32).
"""

import os
from datetime import datetime

import pytest

from cobalt.aset.daily_note import CARDS_SECTION, card_unit_id, stub_template
from cobalt.prefill import daily as daily_module
from cobalt.radar.notes import DemandConsumer, DemandWindow, TotalDemandExceeded, check_total_demand
from cobalt.session.clock import ET
from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.markers import find_section

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

WHEN = datetime(2026, 9, 3, 5, 15, tzinfo=ET)


def _context(spy=("$500.00", "+0.10%"), qqq=("$400.00", "+0.20%"), iwm=("$200.00", "+0.30%")) -> dict:
    return {
        "date_str": "2026-09-03", "time_str": "05:15",
        "rules_checkbox_block": "- [ ] Card first. #process", "mantras_block": "- Tape check: one",
        "mode_hint": "", "sheet_mode_block": "**Day mode: REDUCED**", "daily_stop": "full $100 · half $50",
        "spy_col2": spy[0], "spy_col3": spy[1], "qqq_col2": qqq[0], "qqq_col3": qqq[1],
        "iwm_col2": iwm[0], "iwm_col3": iwm[1], "market_calendar_block": "- 08:30 ET — CPI",
    }


def _table(spy: str, qqq: str, iwm: str) -> str:
    return "\n".join([
        "| VIX |     |     |", "| --- | --- | --- |",
        f"| SPY | {spy} | +0.11% |", f"| QQQ | {qqq} | +0.21% |", f"| IWM | {iwm} | +0.31% |",
        "| BTC |     |     |",
    ])


def _unit(path, section, unit):
    lines = path.read_text().split("\n")
    block = find_section(lines, section)
    if block is None or unit not in block.units:
        return None
    return "\n".join(block.units[unit].body(lines))


def _spy_line(path):
    return next((line for line in path.read_text().split("\n") if line.startswith("| SPY")), None)


@pytest.fixture
def store():
    s = VaultWriteStore()
    s.ensure_schema()
    return s


@requires_db
def test_a1_1_the_section_3_trace_naive_repeated_upsert(tmp_path, store):
    path = tmp_path / "2026-09-03.md"
    writer = VaultWriter("prefill.daily", store=store)
    writer.create_if_absent(path, daily_module._render_template(_context()))
    text = path.read_text()
    his = "| SPY | $512.34 his 06:00 | +9.99% |"
    path.write_text(text.replace(next(x for x in text.split("\n") if x.startswith("| SPY")), his))
    print(f"A1-1 after his 06:00 edit: {_spy_line(path)!r}")
    for n, spy in enumerate(("$501.00", "$502.00", "$503.00"), start=1):
        result = writer.upsert_unit(
            path, "trading", "market_table", _table(spy, "$401.00", "$201.00"),
            placement=daily_module.TRADING_PLACEMENT,
        )
        print(
            f"A1-1 call {n}: action={result.action} overrides={len(result.overrides)} "
            f"SPY line={_spy_line(path)!r} his line present={his in path.read_text()}"
        )


@requires_db
def test_a1_2_x6_baselines_after_create_and_empty_render(tmp_path, store):
    path = tmp_path / "2026-09-03.md"
    VaultWriter("prefill.daily", store=store).create_if_absent(path, daily_module._render_template(_context()))
    for section, unit in (("trading", "market_table"), ("market_calendar", "market_calendar")):
        after = store.last_after(str(path), section, unit)
        print(f"A1-2 last_after({section}/{unit}) is None={after is None} equals unit on disk="
              f"{after == _unit(path, section, unit)} value={after!r}")
    empty = daily_module._render_template({})
    lines = empty.split("\n")
    trading = find_section(lines, "trading")
    print(f"A1-2 _render_template({{}}) raised nothing; {len(lines)} lines; trading unit body="
          f"{trading.units['market_table'].body(lines) if trading else None!r}")
    print(f"A1-2 _render_template({{}}) header line={lines[4]!r} daily stop line="
          f"{next((x for x in lines if x.startswith('Daily HARD Stop')), None)!r}")


@requires_db
def test_a1_3_x16_upsert_on_the_stub(tmp_path, store):
    writer = VaultWriter("aset.daily_note", store=store)
    body = _table("$501.00", "$401.00", "$201.00")

    plain = tmp_path / "stub-plain.md"
    writer.create_if_absent(plain, stub_template(WHEN))
    writer.upsert_unit(plain, CARDS_SECTION, card_unit_id(WHEN), "### 10:02:06 — ZZZQ LONG B\n```aset\nticker: ZZZQ\n```")
    before = plain.read_text()
    result = writer.upsert_unit(plain, "trading", "market_table", body, placement=daily_module.TRADING_PLACEMENT)
    after = plain.read_text()
    print(f"A1-3 plain stub: action={result.action} notes={result.notes}")
    print(f"A1-3 plain stub: unit after={_unit(plain, 'trading', 'market_table')!r}")
    print(f"A1-3 plain stub: last_after equals unit={store.last_after(str(plain), 'trading', 'market_table') == _unit(plain, 'trading', 'market_table')}")
    print(f"A1-3 plain stub: prefix bytes kept={after.startswith(before.rstrip(chr(10)))}")

    typed = tmp_path / "stub-typed.md"
    hand = "| VIX | 17.5 | his |\n| --- | --- | --- |\n| SPY | 9.99 | his |\n| BTC | 1 | his |"
    writer.create_if_absent(typed, stub_template(WHEN) + "\n### Trading\n\n" + hand + "\n")
    writer.upsert_unit(typed, CARDS_SECTION, card_unit_id(WHEN), "### 10:02:06 — ZZZQ LONG B\n```aset\nticker: ZZZQ\n```")
    result = writer.upsert_unit(typed, "trading", "market_table", body, placement=daily_module.TRADING_PLACEMENT)
    unit = _unit(typed, "trading", "market_table")
    print(f"A1-3 typed stub: action={result.action} overrides={len(result.overrides)} notes={result.notes}")
    print(f"A1-3 typed stub: unit after={unit!r}")
    print(f"A1-3 typed stub: hand-typed table bytes unchanged={hand in typed.read_text()}")


def test_a1_4_x17_the_gate_at_exactly_the_ceiling():
    window = DemandWindow.between("04:00", "20:00")
    consumers = [
        DemandConsumer(name="radar", rpm=49.95, window=window, basis="planned total (fixture)"),
        DemandConsumer(name="prefill-refresh", rpm=0.05, window=DemandWindow.between("05:45", "15:45"),
                       basis="fixture extra 0.05"),
    ]
    try:
        demand = check_total_demand(consumers, subject="prefill-refresh", ceiling=50)
        print(f"A1-4 ADMITTED: peak_rpm={demand.peak_rpm!r} (49.95 + 0.05 == 50: {49.95 + 0.05 == 50})")
    except TotalDemandExceeded as e:
        print(f"A1-4 REFUSED: {e} (49.95 + 0.05 == 50: {49.95 + 0.05 == 50})")
