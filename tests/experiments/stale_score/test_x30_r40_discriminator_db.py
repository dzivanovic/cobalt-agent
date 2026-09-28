"""X30 (R40's mechanism, run BEFORE any R40 code, L70; `cobalt_dev`, rows
constructed inside the rollback): can the STORED data identify "an
`htf_level_proximity` tap graded on a stale price BEFORE this fix" by X25's
own predicate, bounded to pre-fix rows by a discriminator already stored?

Constructed rows (one card, one pool, taps written as the store writes
them, `engine_grade_at_tap` set by the test where a pre-fix grade is being
modelled):
  A  pre-fix, FRESH run, graded tap            → must NOT be matched
  B  pre-fix, STALE run, graded tap            → must be matched
  C  post-fix (this code's version), STALE run, graded tap → must NOT be matched
  D  pre-fix, DAILY-missing `input_stale` run (W3's second meaning), graded
     tap → printed: matched = over-exclusion, named
The decision table (never judgement): a sound join AND a stored pre-fix
discriminator → (A) build `0015`; else (B) ASK DESK."""

from __future__ import annotations

from datetime import timedelta

import radar_p2_support as sup
import stale_db_support as sds
from stale_predicates import PRE_FIX_VERSIONS, X25_TAPS, X30_TAPS

pytestmark = sds.requires_db

HTF_AVOID = {"expr": "RangeBreak(HTF).day_count == 1"}


def _set_version(world, run_id: int, version: str) -> None:
    with world.radar._connect() as conn:
        conn.execute("UPDATE radar_score_run SET evaluator_version = %s WHERE id = %s", (version, run_id))


def _graded_tap(world, card_id: int, at) -> int:
    from cobalt.session import session_clock

    with world.cards._connect() as conn:
        return conn.execute(
            "INSERT INTO card_dot_taps (card_id, factor, grade, engine_grade_at_tap, at, session) "
            "VALUES (%s, %s, 6, 5, %s, %s) RETURNING id",
            (card_id, sds.HTF, at, session_clock().session(at).value),
        ).fetchone()[0]


def _evaluation(world, run_id: int) -> str:
    with world.radar._connect() as conn:
        return conn.execute(
            "SELECT evaluation FROM radar_score WHERE run_id = %s AND membership_id = %s",
            (run_id, world.member_id),
        ).fetchone()[0]


def test_x30_the_stored_data_bounds_r40s_exclusion():
    from cobalt.radar.evaluate import EVALUATOR_VERSION

    world = sds.DevWorld(ticker="ZZX30", pool="stale_x30")
    card_id = world.formed_card()
    run_fresh = world.radar.latest_run_id("stale_x30")
    a = _graded_tap(world, card_id, sds.SCAN0 + timedelta(seconds=10))

    kept = sds.bars_before(sds.SCAN0)
    stale_at = sds.stale_as_of(kept)
    run_stale = world.scan(stale_at).run_id
    b = _graded_tap(world, card_id, stale_at + timedelta(seconds=5))
    for run_id in (run_fresh, run_stale):
        _set_version(world, run_id, PRE_FIX_VERSIONS[-1])

    back_at = stale_at + timedelta(seconds=sds.SCAN)
    world.feed(back_at)
    world.scan(back_at)
    stale2_at = sds.stale_as_of(sds.bars_before(back_at))
    run_post = world.scan(stale2_at).run_id
    c = _graded_tap(world, card_id, stale2_at + timedelta(seconds=5))

    daily_at = stale2_at + timedelta(seconds=sds.SCAN)
    world.feed(daily_at)
    world.daily_fails = True
    world.defs = [sup.loaded(sup.anatomy_def(avoid=[{"expr": "NOT Extension.instantiated"}, HTF_AVOID]))]
    run_daily = world.scan(daily_at).run_id
    _set_version(world, run_daily, PRE_FIX_VERSIONS[-1])
    d = _graded_tap(world, card_id, daily_at + timedelta(seconds=5))

    with world.cards._connect() as conn:
        x25 = {r[0] for r in conn.execute(X25_TAPS).fetchall()}
        x30 = {r[0] for r in conn.execute(X30_TAPS).fetchall()}
    labels = {name: _evaluation(world, run) for name, run in
              (("A", run_fresh), ("B", run_stale), ("C", run_post), ("D", run_daily))}
    matched = {name: tap in x30 for name, tap in (("A", a), ("B", b), ("C", c), ("D", d))}
    sound = matched["B"] and not matched["A"] and not matched["C"]
    print(f"X30: seam_labels={labels} x25_matched={sorted(n for n, t in (('A', a), ('B', b), ('C', c), ('D', d)) if t in x25)} "
          f"x30_matched={sorted(n for n, m in matched.items() if m)} post_fix_version={EVALUATOR_VERSION} "
          f"pre_fix_versions={list(PRE_FIX_VERSIONS)} post_fix_never_matched={not matched['C']} "
          f"daily_missing_over_excluded={matched['D']} decision={'A' if sound else 'B'}")
    assert labels["A"] == "formed" and labels["B"] == "input_stale" and labels["C"] == "input_stale"
    assert EVALUATOR_VERSION not in PRE_FIX_VERSIONS
