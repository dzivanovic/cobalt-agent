"""X25's predicate and X30's bounded form, as SQL (not a test module).

X25 (v2 §7, Fable X12): a `card_dot_taps` row for `htf_level_proximity`
with `engine_grade_at_tap IS NOT NULL` whose `at` falls inside a run whose
`radar_score` row for that card's member/def is `input_stale`. "The run the
tap falls inside" = the latest COMPLETE run of the card's pool that started
at or before the tap (`radar_score_run.started_at` is the scan instant,
`evaluate.py:1759`). The join path, every column stored:
`card_dot_taps.card_id` (`0007:144`) → `aset_sizings.pool_member_id`,
`trade_def_md5` → `radar_membership.pool_key` (`0004`) →
`radar_score_run` (`pool_key`, `started_at`, `status`, `evaluator_version`
— `0006:66-83`) → `radar_score` (`run_id`, `membership_id`,
`trade_def_md5`, `evaluation` — `0006:92-109`).

X30's bound: the run's stored `evaluator_version` is one of the strings
written BEFORE this fix — every `EVALUATOR_VERSION` value in the code's
history (`git log -G`): `s2p2.1`, `s2p2.2`.
"""

from __future__ import annotations

PRE_FIX_VERSIONS = ("s2p2.1", "s2p2.2")

_RUN_OF_TAP = (
    "JOIN \"user\".aset_sizings AS c ON c.id = t.card_id "
    "JOIN system.radar_membership AS m ON m.id = c.pool_member_id "
    "JOIN LATERAL (SELECT r2.id, r2.evaluator_version FROM system.radar_score_run AS r2 "
    "              WHERE r2.pool_key = m.pool_key AND r2.status = 'complete' AND r2.started_at <= t.at "
    "              ORDER BY r2.started_at DESC, r2.id DESC LIMIT 1) AS r ON true "
    "JOIN system.radar_score AS s ON s.run_id = r.id AND s.membership_id = c.pool_member_id "
    "     AND s.trade_def_md5 = c.trade_def_md5 "
)

#: X25: the taps its predicate names (ids), any version.
X25_TAPS = (
    'SELECT t.id FROM "user".card_dot_taps AS t ' + _RUN_OF_TAP
    + "WHERE t.factor = 'htf_level_proximity' AND t.engine_grade_at_tap IS NOT NULL "
    "AND s.evaluation = 'input_stale'"
)

#: X30: the same, bounded to runs written by a pre-fix evaluator.
X30_TAPS = X25_TAPS + " AND r.evaluator_version IN ('s2p2.1', 's2p2.2')"
