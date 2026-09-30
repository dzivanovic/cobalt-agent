"""DRC D3 fix round 1 — the OFFLINE rows (`prompts/2026-09-29/08-drc-d3-fix-r1-build.md`
`## THE FIX ROWS`, L75): F-1, F-3, F-4, F-5, F-6 red first on `a8c622ca`,
and the two RUNs (L70: stated as a `UserWarning`, never asserted).

Each row is backed by a `09-28/11` HOLD (`reports/drc-d3-check-2026-09-25.md`
`## Checked against the branch`). The harness is `test_drc_build.py`'s,
BY IMPORT (its `_Store` double, `_record`, `_deps`, `_vault`, the helpers) —
never a copy. Constructed 2001 dates, symbols and strategy titles only
(L32 / L45 / L69); every note in a `tmp_path` vault.
"""

from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path

import pytest

# ---------------------------------------------------------------------
# F-1 — a dry run never regenerates the rules file (L10)
# ---------------------------------------------------------------------


def test_f1_the_dry_run_never_regenerates_the_rules_file(tmp_path, capsys, monkeypatch):
    """F-1 (`drc-d3-check-2026-09-25.md:102`; `09-28/10` D3-4 "`--dry-run`
    writes nothing"): `cobalt drc build --dry-run` on deps whose
    `rules_block` is the REAL one (`prefill.drc.rules_checkbox_block`) must
    never reach `regenerate_rules_config` — that call writes the generated
    rules file (`rules_gen._write_rules_yaml`)."""
    from cobalt.drc import cli as drc_cli
    from cobalt.prefill.drc import rules_checkbox_block

    from test_drc_build import D, _deps, _note, _record, _Store, _vault

    def spy(*args, **kwargs):
        raise AssertionError("regenerate_rules_config called on a dry run")

    monkeypatch.setattr("cobalt.prefill.rules_gen.regenerate_rules_config", spy)
    store = _Store()
    root = _vault(tmp_path)
    _record(store)
    args = argparse.Namespace(date=D, dry_run=True, no_trades=False)
    drc_cli.cmd_build(args, deps=_deps(store, root, rules_block=rules_checkbox_block))
    out = capsys.readouterr().out
    assert "DRY RUN" in out
    assert "rules: not regenerated on a dry run — the build re-reads Rules.md" in out
    assert not _note(root).exists() and store.recorded == []


# ---------------------------------------------------------------------
# F-3 — an unmatched trade's stop under a partial stats file (L1, R17 (5))
# ---------------------------------------------------------------------


def _stop_lines(block: list[str]) -> list[str]:
    return [line for line in block if line.startswith("  - stop:")]


def test_f3_an_unmatched_trade_under_a_partial_stats_file_reads_not_computed_for_its_stop(tmp_path):
    """F-3 (`drc-d3-check-2026-09-25.md:104`; 09-23 R17 (5)): a PARTIAL
    stats file that lacks a match column leaves every trade unmatched; its
    stop reads `not computed — missing: <that column>` like every other
    stats-fed value of the block — never `not given`."""
    from cobalt.drc import build
    from cobalt.drc.stats_log import OPEN_TIME

    from test_drc_build import STATS, _deps, _drop_column, _note, _record, _Store, _trade_id, _unit_body, _vault

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store, stats=_drop_column(STATS.read_bytes(), OPEN_TIME))
    assert event.partial == {"2": [OPEN_TIME]}
    build.run_drc_build(event, deps=_deps(store, root))
    block = _unit_body(_note(root), "drc-trades", f"trade-{_trade_id('AAA', store)}")
    assert any(f"net not computed — missing: {OPEN_TIME}" in line for line in block), block
    assert _stop_lines(block) == [f"  - stop: not computed — missing: {OPEN_TIME}"]


def test_f3_pin_a_matched_row_with_no_stop_reads_not_given_and_a_constructed_stop_as_is(tmp_path):
    """F-3 PINS (green before and after; R17 (4)): a matched stats row whose
    `stop` is `None` → `stop: not given`; a constructed stop → as-is."""
    from cobalt.drc import build

    from test_drc_build import D, _deps, _note, _record, _Store, _trade_id, _unit_body, _vault

    store = _Store()
    root = _vault(tmp_path)
    build.run_drc_build(_record(store), deps=_deps(store, root))
    for trade in store.views[D]["trades"]:
        assert _stop_lines(_unit_body(_note(root), "drc-trades", f"trade-{trade}")) == ["  - stop: not given"]

    def with_stop(derived):
        if derived["symbol"] == "CCC" and derived.get("stats"):
            derived["stats"]["stop"] = "79.95"

    store2 = _Store()
    root2 = _vault(tmp_path / "second")
    build.run_drc_build(_record(store2, edit_trade=with_stop), deps=_deps(store2, root2))
    block = _unit_body(_note(root2), "drc-trades", f"trade-{_trade_id('CCC', store2)}")
    assert _stop_lines(block) == ["  - stop: 79.95"]


# ---------------------------------------------------------------------
# F-4 — the risk facts above his risk paragraph (v2 §13 A9)
# ---------------------------------------------------------------------


def test_f4_the_risk_facts_sit_above_his_risk_paragraph(tmp_path):
    """F-4 (`drc-d3-check-2026-09-25.md:105`; v2 §13 A9 "PRE · facts above
    his paragraph"): `facts` is the unit of its OWN section
    `drc-risk-facts`, directly under `### How I managed risk:` and above
    his first line below it; `drc-risk` (pnl, risk_parameters) stays under
    `### PnL on the day:`. Built twice: the second build changes nothing."""
    from cobalt.drc import build
    from cobalt.vaultwrite.markers import find_section

    from test_drc_build import _deps, _record, _Store, _unit_body, _vault

    store = _Store()
    root = _vault(tmp_path)
    event = _record(store)
    deps = _deps(store, root)
    path = Path(build.run_drc_build(event, deps=deps))
    first = path.read_text()
    lines = first.split("\n")
    heading = lines.index("### How I managed risk:")
    facts = find_section(lines, "drc-risk-facts")
    assert facts is not None, "no drc-risk-facts section"
    his_next = next(i for i in range(facts.close_line + 1, len(lines)) if lines[i].strip())
    assert heading < facts.open_line < his_next
    assert facts.open_line == heading + 1
    assert lines[his_next] == "shape line 47"
    assert "facts" in facts.units and list(facts.units) == ["facts"]
    risk = find_section(lines, "drc-risk")
    pnl_heading = next(i for i, line in enumerate(lines) if line.startswith("### PnL on the day:"))
    assert risk is not None and risk.open_line == pnl_heading + 1
    assert list(risk.units) == ["pnl", "risk_parameters"]
    assert _unit_body(path, "drc-risk-facts", "facts")[0].startswith("daily stop: ")
    build.run_drc_build(event, deps=deps)
    assert path.read_text() == first


# ---------------------------------------------------------------------
# F-5 — a strategy note that is not UTF-8 is unmapped (D3-2b (4))
# ---------------------------------------------------------------------


def test_f5_a_strategy_note_that_is_not_utf8_is_unmapped_never_a_build_failure(tmp_path):
    """F-5 (`drc-d3-check-2026-09-25.md:106`; `09-28/10` D3-2b (4)
    "NEITHER a build failure"): a strategy note holding a non-UTF-8 byte
    lands in the read's errors; its name resolves `unmapped: <name> — note
    <title>: <the error text>`, counted; the other names map; the build
    over it is done."""
    from cobalt.drc import build
    from cobalt.drc.playbooks import read_strategies, resolve

    from test_drc_build import STRATEGIES, _deps, _note, _record, _Store, _unit_body, _vault

    root = _vault(tmp_path)
    (root / STRATEGIES / "Gamma Setup.md").write_bytes(b"---\ntrade_def: example-gamma-setup\n---\n\xff\n")
    strategies = read_strategies(root)
    assert strategies.readable and "Gamma Setup" in strategies.errors
    (gamma, alpha) = resolve(["Gamma Setup Long", "Alpha Setup Long"], strategies)
    assert gamma.text.startswith("unmapped: Gamma Setup Long — note Gamma Setup: 'utf-8' codec can't decode"), gamma.text
    assert alpha.text == "Alpha Setup Long → example-alpha-setup"
    store = _Store()
    path = build.run_drc_build(_record(store), deps=_deps(store, root))
    assert Path(path) == _note(root)
    summary = _unit_body(Path(path), "drc-summary", "summary")
    assert "unmapped playbooks: 2" in summary


# ---------------------------------------------------------------------
# F-6 — the template fixture: no attribution (L45), his seven U+00A0
# ---------------------------------------------------------------------


def _fixture_lines() -> list[str]:
    from test_drc_build import SHAPE

    return SHAPE.read_text(encoding="utf-8").split("\n")


def test_f6_the_template_fixture_carries_no_personal_attribution():
    """F-6 (a) (`drc-d3-check-2026-09-25.md:107`; L45 "personal attribution
    … stripped"): the fixture's first heading is a constructed name."""
    assert _fixture_lines()[4].rstrip() == "# Example Trader DRC"


def test_f6_the_template_fixture_carries_the_seven_nbsp_positions():
    """F-6 (b) (`drc-d3-check-2026-09-25.md:107`; L45 "real shape"): his
    template's U+00A0 sits on lines 5, 49, 128, 134, 156, 173 and 175
    (1-based), one on each, seven in all."""
    lines = _fixture_lines()
    assert [n for n, line in enumerate(lines, start=1) if " " in line] == [5, 49, 128, 134, 156, 173, 175]
    assert [lines[n - 1].count(" ") for n in (5, 49, 128, 134, 156, 173, 175)] == [1] * 7
    assert sum(line.count(" ") for line in lines) == 7


# ---------------------------------------------------------------------
# RUN-1 / RUN-2 (L70) — stated, never asserted
# ---------------------------------------------------------------------


def test_run1_a_day_ending_with_an_open_position(tmp_path):
    """RUN-1 (`drc-d3-check-2026-09-25.md:114`, NOT CHECKABLE): `units.money(
    gross_pnl)` (`build.py:608`–`:609`) on a day that ends with an open
    position — D1's `trading_log_carry_day1.csv` through the offline
    harness. The result is STATED; a raise is caught and stated."""
    from cobalt.drc import build

    from test_drc_build import DAY1, _deps, _note, _record, _Store, _unit_body, _vault

    store = _Store()
    root = _vault(tmp_path)
    try:
        event = _record(store, trading=DAY1.read_bytes())
        build.run_drc_build(event, deps=_deps(store, root))
        opens = [r["derived"] for r in store.krows[event.date] if r["kind"] == "trade"
                 and r["derived"].get("status") != "closed"]
        parts = []
        for t in opens:
            block = _unit_body(_note(root), "drc-trades", f"trade-{t['trade_id']}")
            line = next((l for l in block if l.startswith("  - P&L:")), "(no P&L line)")
            parts.append(f"open trade status={t.get('status')}; gross_pnl={t.get('gross_pnl')!r}; P&L line={line.strip()}")
        message = "RUN-1: " + (" | ".join(parts) if parts else "no open trade on the day")
    except Exception as e:  # noqa: BLE001 — the RUN states a raise, never fixes it (L70)
        message = f"RUN-1: raised {type(e).__name__}: {e}"
    warnings.warn(message, UserWarning)


def test_run2_the_miss_line_blob_through_the_job_rows_json():
    """RUN-2 (`drc-d3-check-2026-09-25.md:115`, NOT CHECKABLE): E6's blob,
    filled by the runner's absent-note path, taken through `job_result()`
    then `json.loads(json.dumps(…))` (what the JSONB row returns) →
    `render_stored`, against the in-memory render. STATED."""
    from cobalt.replay.line import render_stored
    from cobalt.replay.runner import run_nightly

    from test_replay_runner import DAY, fake_deps

    try:
        deps, _ = fake_deps(drc_missing=True)
        result = run_nightly(DAY, dry_run=False, deps=deps)
        (printed,) = [line for line in deps.printed if line.startswith("line: pending (no DRC) — ")]
        in_memory = printed.removeprefix("line: pending (no DRC) — ")
        stored = json.loads(json.dumps(result.job_result()))["line_inputs"]
        again = render_stored(stored)
        equal = again == in_memory
        first = "none"
        if not equal:
            i = next((k for k, (a, b) in enumerate(zip(again, in_memory)) if a != b), min(len(again), len(in_memory)))
            first = f"at char {i}: stored {again[i:i + 40]!r} vs in-memory {in_memory[i:i + 40]!r}"
        message = f"RUN-2: re-render after the job row's JSON equals the in-memory render = {equal}; first difference = {first}"
    except Exception as e:  # noqa: BLE001 — the RUN states a raise, never fixes it (L70)
        message = f"RUN-2: raised {type(e).__name__}: {e}"
    warnings.warn(message, UserWarning)
