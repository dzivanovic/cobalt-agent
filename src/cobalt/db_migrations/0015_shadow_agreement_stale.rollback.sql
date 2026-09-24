-- 0015 rollback — `"user".shadow_agreement_v` exactly as 0007 defines it
-- (every tap with an engine grade is a pair again). Bounded: this view and
-- nothing else; idempotent.
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
     GROUP BY t.user_id, t.factor, (t.at AT TIME ZONE 'America/New_York')::date;

ALTER VIEW "user".shadow_agreement_v OWNER TO cobalt_user;
