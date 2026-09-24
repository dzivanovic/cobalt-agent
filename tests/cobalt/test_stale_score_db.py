"""STALE SCORE S2 — the two writers on `cobalt_dev` (v2 §6 S2; §2 C step 7
`[F-06]`; step 8 REPLACED by R45, Fable (i); R40 by X30 (A); `requires_db`).

Everything runs inside the suite's rolled-back `cobalt_dev` transaction
(`conftest.dev_db_tx`); `stale_db_support` builds the world (real-shape
FTFT bars fed by the test, the repo's synthetic def, a constructed
`radar.scan_interval`). The "pre-C1" card has no `assumed_formation` dot,
so its score is live when fresh (v2 §1b) — the only shape on which a stale
number can be published and these writers matter. Migration `0015` is
applied ONLY inside a rolled-back transaction, never committed (L76).
"""

from __future__ import annotations

from datetime import timedelta
from decimal import Decimal

import pytest

import stale_db_support as sds

pytestmark = [sds.requires_db, pytest.mark.integration]

TICKER = "ZZSS"
POOL = "stale_score_s2"


@pytest.fixture
def world():
    return sds.DevWorld(ticker=TICKER, pool=POOL)


def _stale_card(world):
    """A scored pre-C1 card, then one scan with no newer bar: stale."""
    card_id = sds.scored_pre_c1_card(world)
    assert world.row(card_id)["card_score"] is not None
    stale_at = sds.stale_as_of(sds.bars_before(sds.SCAN0))
    world.scan(stale_at)
    return card_id, stale_at


# ---------------------------------------------------------------------
# (i) [F-06] — a tap during staleness keeps the helper's sentence
# ---------------------------------------------------------------------


def test_a_tap_while_proximity_is_null_keeps_the_stored_sentence_and_publishes_no_score(world):
    card_id, stale_at = _stale_card(world)
    before = world.row(card_id)
    assert before["proximity"] is None and before["card_score"] is None
    assert before["score_suppressed"].startswith("bars stale — last close ")
    result = world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=5))
    after = world.row(card_id)
    assert result["card_score"] is None and after["card_score"] is None
    assert after["score_suppressed"].encode() == before["score_suppressed"].encode(), after["score_suppressed"]
    assert after["conviction"] != before["conviction"]  # the tap still moves conviction (as today)


def test_a_tap_while_proximity_is_null_and_no_sentence_is_stored_writes_proximity_unknown(world):
    from cobalt.cards.scoring import PROXIMITY_UNKNOWN

    card_id, stale_at = _stale_card(world)
    with world.cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET score_suppressed = NULL WHERE id = %s", (card_id,))
    world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=5))
    after = world.row(card_id)
    assert after["card_score"] is None and after["score_suppressed"] == PROXIMITY_UNKNOWN


# ---------------------------------------------------------------------
# (ii) taps-moved while this scan's proximity is NULL (X3)
# ---------------------------------------------------------------------


def test_taps_moved_with_a_null_proximity_writes_a_null_score_and_the_stale_reason(world):
    card_id = sds.scored_pre_c1_card(world)
    kept = sds.bars_before(sds.SCAN0)
    stale_at = sds.stale_as_of(kept)
    update = sds.update_for(world, card_id, stale_at, kept)  # the stage's read
    assert update.proximity is None and update.score_suppressed.startswith("bars stale — ")
    world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=1))  # lands before the stage's write
    wrote_all = world.cards.refresh_radar_card(update, now=stale_at + timedelta(seconds=2))
    row = world.row(card_id)
    assert wrote_all is False  # the taps-moved branch
    assert row["proximity"] is None
    assert row["card_score"] is None, f"card_score {row['card_score']} beside a NULL proximity"
    assert row["score_suppressed"] == update.score_suppressed


# ---------------------------------------------------------------------
# (iii) R45 — the FRESH-price tap race (Fable (i)), its own test
# ---------------------------------------------------------------------


def test_r45_a_tap_racing_a_fresh_scan_scores_the_taps_conviction_on_this_scans_proximity(world):
    from cobalt.cards.scoring import card_score

    card_id = sds.scored_pre_c1_card(world)
    stored = world.row(card_id)["proximity"]
    later = sds.SCAN0 + timedelta(minutes=10)
    fresh = sds.bars_before(later)
    world.feed(later)
    update = sds.update_for(world, card_id, later, fresh)  # the stage reads the card
    assert update.proximity is not None and update.proximity != stored  # a new price, a new proximity
    tapped = world.tap(card_id, "trail_fit", 3, later + timedelta(seconds=1))  # a tap lands: conviction moves
    locked = world.row(card_id)  # what the lock SELECT reads under the write
    world.cards.refresh_radar_card(update, now=later + timedelta(seconds=2))  # the stage writes
    row = world.row(card_id)
    expected = card_score(Decimal(tapped["conviction"]), update.proximity, locked["score_suppressed"])
    old_price_score = card_score(Decimal(tapped["conviction"]), stored, locked["score_suppressed"])
    assert expected is not None and expected != old_price_score  # the race is visible in the integer
    assert row["proximity"] == update.proximity
    assert row["card_score"] == expected, (
        f"card_score {row['card_score']} beside proximity {row['proximity']}: expected {expected} "
        f"(the tap's conviction on this scan's proximity)"
    )
    assert row["score_suppressed"] == locked["score_suppressed"]
    assert row["conviction"] == Decimal(tapped["conviction"])  # conviction stays the tap route's
    assert row["proposed_key"] == tapped["proposed_key"]  # and so does the proposed key


# ---------------------------------------------------------------------
# (iv) R40 — migration 0015 (X30 (A)). NEVER committed to cobalt_dev (L76):
#   * the forward / rollback shape on `connect_migration` with autocommit
#     off and `conn.rollback()` in `finally` (`test_p4_migrations.py:403`);
#   * the view's behaviour inside the suite's own rollback transaction —
#     the 0015 text executed on the user-side connection the stores share
#     (`test_assumed_store.py:258-278`'s precedent), seeded by the real stage.
# ---------------------------------------------------------------------


def _migration_conn():
    from cobalt import db, env

    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


def _viewdef(conn) -> str:
    return conn.execute("SELECT pg_get_viewdef('\"user\".shadow_agreement_v'::regclass)").fetchone()[0]


def _predicates():
    import sys
    from pathlib import Path

    folder = str(Path(__file__).resolve().parents[1] / "experiments" / "stale_score")
    if folder not in sys.path:
        sys.path.insert(0, folder)
    import stale_predicates

    return stale_predicates


def test_0015_is_registered_after_0013_and_its_rollback_first():
    from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE

    assert FORWARD[-1] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
    assert REVERSE[0] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql"
    assert FORWARD[-2].name == "0013_tunables_slug_nullable.sql"
    assert REVERSE[1].name == "0013_tunables_slug_nullable.rollback.sql"


def test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction():
    from cobalt.db_migrations import FORWARD
    from cobalt.db_migrations.cli import _apply, _rollback_paths

    conn = _migration_conn()
    try:
        _apply(conn, [p for p in FORWARD if p.name < "0015"])
        at_0013 = _viewdef(conn)
        assert "evaluator_version" not in at_0013  # 0007's view
        _apply(conn, FORWARD)
        once = _viewdef(conn)
        _apply(conn, FORWARD)  # second apply: idempotent
        assert _viewdef(conn) == once and "evaluator_version" in once and "input_stale" in once
        _apply(conn, _rollback_paths("0013"))
        assert _viewdef(conn) == at_0013  # exactly 0007's view again
        _apply(conn, _rollback_paths("0013"))  # a repeated reverse is a no-op
        assert _viewdef(conn) == at_0013
    finally:
        conn.rollback()
        conn.close()


def _apply_0015_in_the_suite_transaction(cards) -> None:
    from cobalt.db_migrations import MIGRATIONS_DIR

    with cards._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql").read_text())


def _htf_pairs(world) -> int:
    from datetime import date

    return sum(r["pairs"] for r in world.cards.shadow_agreement(None)
               if r["factor"] == sds.HTF and r["trade_date"] == date(2026, 1, 6))


def _graded_tap(world, card_id: int, at) -> int:
    """A tap row as the store writes it, with an engine grade at tap — the
    shape a PRE-fix stale-graded tap had (after the fix none can be written,
    X21)."""
    from cobalt.session import session_clock

    with world.cards._connect() as conn:
        return conn.execute(
            "INSERT INTO card_dot_taps (card_id, factor, grade, engine_grade_at_tap, at, session) "
            "VALUES (%s, %s, 6, 5, %s, %s) RETURNING id",
            (card_id, sds.HTF, at, session_clock().session(at).value),
        ).fetchone()[0]


def test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones():
    world = sds.DevWorld(ticker="ZZR40", pool="stale_r40")
    card_id = world.formed_card()
    run_fresh = world.radar.latest_run_id("stale_r40")
    fresh_tap = _graded_tap(world, card_id, sds.SCAN0 + timedelta(seconds=10))  # pre-fix, fresh-graded
    stale_at = sds.stale_as_of(sds.bars_before(sds.SCAN0))
    run_stale = world.scan(stale_at).run_id
    stale_tap = _graded_tap(world, card_id, stale_at + timedelta(seconds=5))  # pre-fix, stale-graded
    with world.radar._connect() as conn:
        conn.execute("UPDATE radar_score_run SET evaluator_version = 's2p2.2' WHERE id = ANY(%s)",
                     ([run_fresh, run_stale],))
    back_at = stale_at + timedelta(seconds=sds.SCAN)
    world.feed(back_at)
    world.scan(back_at)
    stale2_at = sds.stale_as_of(sds.bars_before(back_at))
    world.scan(stale2_at)  # this code's version, stale
    post_tap = _graded_tap(world, card_id, stale2_at + timedelta(seconds=5))
    with world.cards._connect() as conn:
        x25 = {r[0] for r in conn.execute(_predicates().X25_TAPS).fetchall()}
    before = _htf_pairs(world)  # 0007's view: all three taps are pairs
    _apply_0015_in_the_suite_transaction(world.cards)
    after = _htf_pairs(world)
    assert {fresh_tap, stale_tap, post_tap} - x25 == {fresh_tap}  # X25 names the two stale-run taps
    assert before - after == 1  # the view drops exactly the pre-fix stale-graded one
    assert after >= 2  # the fresh-graded pre-fix tap and the post-fix tap are still pairs


def test_r40_on_cobalt_dev_the_view_drops_exactly_x25s_pre_fix_count():
    from cobalt.cards.store import CardStore

    cards = CardStore("cobalt_dev")
    with cards._connect() as conn:
        x25_pre_fix = len(conn.execute(_predicates().X30_TAPS).fetchall())
    before = sum(r["pairs"] for r in cards.shadow_agreement(None))
    _apply_0015_in_the_suite_transaction(cards)
    after = sum(r["pairs"] for r in cards.shadow_agreement(None))
    print(f"R40: cobalt_dev pairs_before={before} pairs_after={after} x25_pre_fix={x25_pre_fix}")
    assert before - after == x25_pre_fix
