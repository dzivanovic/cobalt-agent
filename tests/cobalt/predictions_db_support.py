"""Shared with-DB helpers for the F15 P1 record tests (not a test module).

`apply_0022` runs `0022_prediction_records.sql` INSIDE the suite's
rollback transaction (the `legs_db_support.apply_0021` precedent), so every
test that reaches a record writer holds at `0013` and at `0022` alike and
leaves nothing applied (L76). The file is idempotent, so a second apply on a
tree already at `0022` is a no-op. Every value here is constructed (L32).
"""

from __future__ import annotations

import json
from decimal import Decimal
from typing import Any


def apply_0022(store) -> None:
    from cobalt.db_migrations import MIGRATIONS_DIR

    with store._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0022_prediction_records.sql").read_text())


def rollback_0022(store) -> None:
    from cobalt.db_migrations import MIGRATIONS_DIR

    with store._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0022_prediction_records.rollback.sql").read_text())


def records_of(store, card_id: int) -> list[dict[str, Any]]:
    with store._connect() as conn:
        cur = conn.execute("SELECT * FROM prediction_records WHERE card_id = %s ORDER BY seq", (card_id,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


def record_count(store) -> int:
    with store._connect() as conn:
        return int(conn.execute("SELECT count(*) FROM prediction_records").fetchone()[0])


def card_numbers(store, card_id: int) -> dict[str, Any]:
    with store._connect() as conn:
        cur = conn.execute(
            "SELECT proximity, conviction, card_score, score_suppressed, proposed_key, last_price_bar_ts "
            "FROM aset_sizings WHERE id = %s", (card_id,),
        )
        return dict(zip([d.name for d in cur.description], cur.fetchone()))


def _dec(value) -> Decimal | None:
    return None if value is None else Decimal(str(value))


def assert_output_is_the_row(output: dict[str, Any], row: dict[str, Any]) -> None:
    """A record's `output` numbers equal the card row's (the compare is on
    Decimal values: NUMERIC(8,6) reads back padded, X7)."""
    assert _dec(output["proximity"]) == _dec(row["proximity"]), (output["proximity"], row["proximity"])
    assert _dec(output["conviction"]) == _dec(row["conviction"]), (output["conviction"], row["conviction"])
    assert output["card_score"] == row["card_score"]
    assert output["score_suppressed"] == row["score_suppressed"]
    assert output["proposed_key"] == row["proposed_key"]


def transition_ids(store, card_id: int) -> list[tuple[int, str | None, str]]:
    with store._connect() as conn:
        return [tuple(r) for r in conn.execute(
            "SELECT id, from_state, to_state FROM card_transitions WHERE card_id = %s ORDER BY id", (card_id,),
        ).fetchall()]


def insert_raw_record(conn, card_id: int, **over) -> int:
    """A raw INSERT (the DDL tests only — the store writes through
    `cobalt.cards.predictions.write_record`)."""
    transition_id = conn.execute(
        "SELECT max(id) FROM card_transitions WHERE card_id = %s", (card_id,)
    ).fetchone()[0]
    values = dict(
        card_id=card_id, seq=900, transition_id=transition_id, kind="create", at="2026-01-06T16:30:00+00:00",
        scorer_id="card_grade", scorer_version="s2p2.3", formula_sha256="a" * 64, settings_sha256="b" * 64,
        run_id=None, inputs=json.dumps({"taps_moved": False, "locked": None}), output=json.dumps({}), why="raw",
    )
    values.update(over)
    columns = list(values)
    row = conn.execute(
        f"INSERT INTO prediction_records ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))}) "
        "RETURNING id",
        [values[c] for c in columns],
    ).fetchone()
    return int(row[0])
