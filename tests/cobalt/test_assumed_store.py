"""STEP-2 of the setups one build — the assumed store (FINAL §8 [R2F-07],
[R2F-09]; R2-3 = B by X20, with migration 0013; §7 B).

- `TunableSource.ASSUMED`;
- the dedicated reader `load_assumed_tunables` of `1 - Trading/Assumed
  Defaults.md` (unit `tunables:assumed`), appended to
  `VaultTradeDefs.user_tunables` — an absent note is no rows;
- the strategy-note reader refuses `source: assumed`;
- `merge_tunables` hole-fill, B's R2-3.2 predicate, as a truth table (X19);
- F1 WIDENED by R48 (fix r3 F2): a `per_indicator(...)` assumed row fills only
  an engine hole of that same scope; any other is refused;
- the writer (an L28 command over the existing `VaultWriter`) proven on a
  `tmp_path` vault with its unified diff, and X23;
- the read-only dry-run `cobalt taxonomy tunables --assumed`.

Every value here is a literal of this file's own choosing (L32, L69).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml

from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH, TaxonomyConfigError, load_tunables, merge_tunables
from cobalt.taxonomy.tunables import TunableRow, TunableSource
from cobalt.taxonomy.vault_loader import STRATEGIES_DIR, VaultTaxonomyError, load_vault_trade_defs

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: needs cobalt_dev",
)

EXAMPLE_SLUG = "example-range-break"


def _vault(root: Path, assumed_rows: list[dict] | None) -> Path:
    strategies = root / STRATEGIES_DIR
    strategies.mkdir(parents=True, exist_ok=True)
    (strategies / "Example Range Break.md").write_text(EXAMPLE_NOTE_PATH.read_text(encoding="utf-8"))
    if assumed_rows is not None:
        from cobalt.taxonomy.cli import assumed_note_text

        (root / "1 - Trading" / "Assumed Defaults.md").write_text(assumed_note_text(assumed_rows))
    return root


def _row(key="range.wick_ratio_max", value=0.5, unit="ratio", scope="global", source="assumed", **kw):
    return {"key": key, "value": value, "unit": unit, "scope": scope, "dynamic": True,
            "status": "proposed", "source": source, "consumers": ["a detector"], **kw}


def test_tunable_source_has_assumed():
    assert TunableSource("assumed") is TunableSource.ASSUMED


# ---------------------------------------------------------------------
# The dedicated reader
# ---------------------------------------------------------------------


def test_an_absent_assumed_note_is_no_rows_not_an_error(tmp_path):
    from cobalt.taxonomy.vault_loader import load_assumed_tunables

    root = _vault(tmp_path, None)
    assert load_assumed_tunables(root, loaded_slugs={EXAMPLE_SLUG}) == []
    assert [t.key for t in load_vault_trade_defs(vault_root=root).user_tunables] == [
        "example_range_break.range_duration_band"]


def test_the_reader_appends_global_and_per_trade_rows_to_user_tunables(tmp_path):
    root = _vault(tmp_path, [_row(), _row(key="example_range_break.probe", value=3, unit="count",
                                          scope="per_trade(example_range_break)", source="ruling")])
    result = load_vault_trade_defs(vault_root=root)
    by_key = {t.key: t for t in result.user_tunables}
    assert by_key["range.wick_ratio_max"].slug is None
    assert by_key["range.wick_ratio_max"].row.source is TunableSource.ASSUMED
    assert by_key["example_range_break.probe"].slug == EXAMPLE_SLUG
    assert by_key["range.wick_ratio_max"].note_path == "1 - Trading/Assumed Defaults.md"


@pytest.mark.parametrize(("row", "match"), [
    # fix r3 F2 (R48, F1 WIDENED): a per_indicator row fills only an engine hole of the SAME scope —
    # was scope `per_indicator(ema9)` (now accepted, `test_setups_fix_r3.py`); a mismatched scope stays refused
    (_row(scope="per_indicator(vwap)", key="flat_threshold.ema9"), "per_indicator"),
    (_row(scope="per_trade(example_not_loaded)", key="example_not_loaded.x"), "example_not_loaded"),
    (_row(source="sheet"), "source"),
    (_row(source="dwv"), "source"),
])
def test_the_reader_refuses_a_row_outside_its_contract(tmp_path, row, match):
    root = _vault(tmp_path, [row])
    with pytest.raises(VaultTaxonomyError, match=match):
        load_vault_trade_defs(vault_root=root)


def test_a_strategy_note_row_marked_assumed_is_refused(tmp_path):
    root = _vault(tmp_path, None)
    note = root / STRATEGIES_DIR / "Example Range Break.md"
    note.write_text(note.read_text().replace("    source: ruling\n", "    source: assumed\n"))
    with pytest.raises(VaultTaxonomyError, match="assumed"):
        load_vault_trade_defs(vault_root=root)


# ---------------------------------------------------------------------
# merge_tunables hole-fill — X19, one test per clause
# ---------------------------------------------------------------------


def _engine(key="range.wick_ratio_max", **update):
    row = load_tunables().by_key[key]
    return {key: row.model_copy(update=update) if update else row}


def _user(**kw) -> dict[str, TunableRow]:
    row = TunableRow(**_row(**kw))
    return {row.key: row}


def test_x19_hole_fill_fills_a_null_engine_row_with_value_and_source_only():
    engine = _engine()
    merged = merge_tunables(engine, _user(value=0.5, source="assumed"))
    row = merged["range.wick_ratio_max"]
    assert row.value == 0.5 and row.source is TunableSource.ASSUMED
    expected = engine["range.wick_ratio_max"]
    assert (row.key, row.unit, row.scope, row.dynamic, row.consumers) == (
        expected.key, expected.unit, expected.scope, expected.dynamic, expected.consumers)


def test_x19_a_ruling_row_fills_too():
    assert merge_tunables(_engine(), _user(source="ruling"))["range.wick_ratio_max"].source is TunableSource.RULING


@pytest.mark.parametrize(("engine_update", "user_kw", "why"), [
    ({"value": 0.7}, {}, "engine value is no longer null"),
    ({}, {"source": "sheet"}, "user source not assumed/ruling"),
    ({}, {"source": "dwv"}, "user source not assumed/ruling"),
    ({}, {"scope": "per_trade(example_range_break)"}, "a per-trade row never fills a global key"),
    ({}, {"unit": "atr"}, "unit differs"),
])
def test_x19_every_other_collision_stays_loud(engine_update, user_kw, why):
    with pytest.raises(TaxonomyConfigError):
        merge_tunables(_engine(**engine_update), _user(**user_kw))


def test_x19_a_strategy_note_row_never_fills_an_engine_key(tmp_path):
    """A strategy-note row is forced to `per_trade(<own slug>)` and no engine
    row is per_trade, so scope equality refuses it."""
    root = _vault(tmp_path, None)
    note = root / STRATEGIES_DIR / "Example Range Break.md"
    note.write_text(note.read_text().replace(
        "  - key: example_range_break.range_duration_band",
        "  - key: range.wick_ratio_max\n    value: 0.5\n    unit: ratio\n"
        "    scope: per_trade(example_range_break)\n    dynamic: true\n    status: proposed\n"
        "    source: ruling\n  - key: example_range_break.range_duration_band"))
    with pytest.raises(VaultTaxonomyError, match="shadow engine keys"):
        load_vault_trade_defs(vault_root=root)


def test_x19_duplicate_suppliers_are_refused(tmp_path):
    root = _vault(tmp_path, [_row(), _row(value=0.6)])
    with pytest.raises(VaultTaxonomyError, match="duplicate"):
        load_vault_trade_defs(vault_root=root)


# ---------------------------------------------------------------------
# The writer (L28, the existing VaultWriter) and X23 — tmp_path vault
# ---------------------------------------------------------------------


@requires_db
def test_the_writer_creates_the_note_and_upserts_the_unit_with_its_diff(tmp_path):
    from cobalt.taxonomy.cli import write_assumed
    from cobalt.vaultwrite.store import VaultWriteStore

    root = _vault(tmp_path, None)
    rows = tmp_path / "rows.yaml"
    rows.write_text(yaml.safe_dump({"tunables": [_row()]}, sort_keys=False))
    results = write_assumed(root, rows, store=VaultWriteStore("cobalt_dev"))
    assert [r.action for r in results] == ["created", "updated"]
    assert "+- key: range.wick_ratio_max" in results[1].diff
    print("DIFF 1:\n" + "\n".join(r.diff for r in results))
    note = root / "1 - Trading" / "Assumed Defaults.md"
    assert note.exists()
    loaded = load_vault_trade_defs(vault_root=root)
    assert {t.key for t in loaded.user_tunables} >= {"range.wick_ratio_max"}


@requires_db
def test_x23_a_hand_edit_survives_a_second_write_of_another_row(tmp_path):
    from cobalt.taxonomy.cli import write_assumed
    from cobalt.vaultwrite.store import VaultWriteStore

    root = _vault(tmp_path, None)
    store = VaultWriteStore("cobalt_dev")
    first = [_row(), _row(key="range_break.failed_trap_bars", value=1, unit="bars")]
    rows = tmp_path / "rows.yaml"
    rows.write_text(yaml.safe_dump({"tunables": first}, sort_keys=False))
    write_assumed(root, rows, store=store)
    note = root / "1 - Trading" / "Assumed Defaults.md"
    text = note.read_text()
    # the owner rules ONE row by hand: its `source` reads ruling
    head, tail = text.split("- key: range_break.failed_trap_bars", 1)
    note.write_text(head.replace("source: assumed", "source: ruling") + "- key: range_break.failed_trap_bars" + tail)
    second = [_row(value=0.55), _row(key="range_break.failed_trap_bars", value=2, unit="bars")]
    rows.write_text(yaml.safe_dump({"tunables": second}, sort_keys=False))
    results = write_assumed(root, rows, store=store)
    print("X23 DIFF:\n" + "\n".join(r.diff for r in results))
    rows_now = {t.key: t.row for t in load_vault_trade_defs(vault_root=root).user_tunables}
    assert rows_now["range.wick_ratio_max"].source is TunableSource.RULING  # the hand edit was not reverted
    assert rows_now["range_break.failed_trap_bars"].value == 2              # the second write landed


# ---------------------------------------------------------------------
# The dry-run (L10; FINAL §7 point 3)
# ---------------------------------------------------------------------


def test_the_assumed_dry_run_lists_assumed_rows_and_every_null_engine_hole(tmp_path):
    from cobalt.taxonomy.cli import assumed_report

    root = _vault(tmp_path, [_row()])
    lines = assumed_report(load_tunables().by_key, load_vault_trade_defs(vault_root=root))
    by_key = {line.key: line for line in lines}
    assert by_key["range.wick_ratio_max"].state == "assumed"
    assert by_key["range.wick_ratio_max"].source_page == ""
    holes = {line.key for line in lines if line.state == "hole"}
    assert {"flat_threshold.ema9", "flat_threshold.vwap", "dist.k.vwap", "range_break.failed_trap_bars"} <= holes
    assert "range.wick_ratio_max" not in holes
    assert all(line.unit and line.scope for line in lines)


# ---------------------------------------------------------------------
# The migration (R2-3 = B, X20) — 0013, inside the rollback transaction
# ---------------------------------------------------------------------


def test_0013_is_registered_forward_and_reverse():
    from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE

    assert MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql" in FORWARD
    assert MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql" in REVERSE
    assert FORWARD[-1].name == "0013_tunables_slug_nullable.sql"
    assert REVERSE[0].name == "0013_tunables_slug_nullable.rollback.sql"


@requires_db
def test_0013_lets_a_global_assumed_row_sync_and_its_rollback_refuses_while_one_exists(tmp_path):
    import psycopg

    from cobalt import db
    from cobalt.db_migrations import MIGRATIONS_DIR
    from cobalt.taxonomy.store import TradeDefStore

    store = TradeDefStore("cobalt_dev")
    store.ensure_schema()
    with db.connect("cobalt_dev", side=db.Side.USER) as conn:
        conn.execute("DELETE FROM tunables")
        conn.execute("DELETE FROM trade_defs")
    # The suite's one rollback connection, on the table owner's side: the
    # DDL, the sync and the reads share a session and nothing commits.
    with db.connect("cobalt_dev", side=db.Side.USER) as conn:
        conn.execute((MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql").read_text())
        conn.execute((MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql").read_text())  # idempotent
    root = _vault(tmp_path, [_row()])
    store.sync(load_vault_trade_defs(vault_root=root))
    with db.connect("cobalt_dev", side=db.Side.USER) as conn:
        slug = conn.execute("SELECT slug FROM tunables WHERE key = 'range.wick_ratio_max'").fetchone()
    assert slug == (None,)
    with db.connect("cobalt_dev", side=db.Side.USER) as conn:
        conn.execute("SAVEPOINT refuse_probe")
        with pytest.raises(psycopg.errors.RaiseException, match="REFUSING 0013 reverse"):
            conn.execute((MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql").read_text())
        conn.execute("ROLLBACK TO SAVEPOINT refuse_probe")
    with db.connect("cobalt_dev", side=db.Side.USER) as conn:
        conn.execute("DELETE FROM tunables WHERE slug IS NULL")
        conn.execute((MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql").read_text())
        nullable = conn.execute(
            "SELECT is_nullable FROM information_schema.columns WHERE table_schema = 'user' "
            "AND table_name = 'tunables' AND column_name = 'slug'").fetchone()
    assert nullable == ("NO",)
