-- 0015 — R40: stale-graded `htf_level_proximity` taps leave the shadow
-- agreement numbers (cto-2026-09-22.md R40 "B"; stale-score build, X30 (A)).
--
-- A tap is excluded when ALL hold (X25's predicate, bounded by X30):
--   * factor `htf_level_proximity` with an engine grade at tap;
--   * the latest COMPLETE run of the card's pool that started at or before
--     the tap has a `radar_score` row for the card's member and formation
--     def that is `input_stale`;
--   * that run was written by an evaluator BEFORE the stale-score fix
--     (`s2p2.1`, `s2p2.2` — every EVALUATOR_VERSION in the code's history).
-- After the fix a stale `htf_level_proximity` dot carries no engine grade,
-- so a new tap records none (X21); the version bound keeps every run
-- written by this or a later evaluator out of the exclusion.
-- Named over-exclusion (accepted, it only removes rows): a pre-fix run
-- whose `input_stale` meant "daily bars missing" (W3) matches too.
-- Named under-exclusion: a card refreshed under an edited def (R2-4) has
-- its seam rows under the new md5, which this join (formation md5) misses.
--
-- The column list is 0007's, so OR REPLACE is enough; idempotent.
CREATE OR REPLACE VIEW "user".shadow_agreement_v AS
    SELECT t.user_id, t.factor, (t.at AT TIME ZONE 'America/New_York')::date AS trade_date,
           count(*) AS pairs,
           percentile_cont(0.5) WITHIN GROUP (
               ORDER BY abs(t.grade - t.engine_grade_at_tap)) AS median_abs_delta,
           avg(CASE WHEN abs(t.grade - t.engine_grade_at_tap) <= 2 THEN 1.0 ELSE 0.0 END)
               AS within2_share,
           array_agg(abs(t.grade - t.engine_grade_at_tap) ORDER BY t.id) AS deltas
      FROM "user".card_dot_taps AS t
     WHERE t.engine_grade_at_tap IS NOT NULL
       AND NOT EXISTS (
           SELECT 1
             FROM "user".aset_sizings AS c
             JOIN system.radar_membership AS m ON m.id = c.pool_member_id
             JOIN LATERAL (
                  SELECT r2.id, r2.evaluator_version
                    FROM system.radar_score_run AS r2
                   WHERE r2.pool_key = m.pool_key AND r2.status = 'complete' AND r2.started_at <= t.at
                   ORDER BY r2.started_at DESC, r2.id DESC
                   LIMIT 1) AS r ON true
             JOIN system.radar_score AS s
               ON s.run_id = r.id AND s.membership_id = c.pool_member_id AND s.trade_def_md5 = c.trade_def_md5
            WHERE c.id = t.card_id
              AND t.factor = 'htf_level_proximity'
              AND s.evaluation = 'input_stale'
              AND r.evaluator_version IN ('s2p2.1', 's2p2.2'))
     GROUP BY t.user_id, t.factor, (t.at AT TIME ZONE 'America/New_York')::date;

ALTER VIEW "user".shadow_agreement_v OWNER TO cobalt_user;
