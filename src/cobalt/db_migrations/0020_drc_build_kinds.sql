-- 0020_drc_build_kinds — DRC D3: the DRC build's derived rows (L57).
--
-- The build (`cobalt.drc.build`) stores every number it computes — the
-- card match, the summary / PnL / risk figures, the playbook resolutions —
-- in `"user".drc_rows` with its inputs and `fn_version` (`drc.build/1`),
-- through ONE writer, `DrcStore.record_build`, in two new kinds:
--   build_trade  one per trade, `ref` = the trade id
--   build_day    one per day,   `ref` = 'build'
-- X-K (`tests/cobalt/test_drc_d3_experiments.py`) proved `0018`'s CHECK
-- refuses them. No table is created; the CHECK is widened in place, under
-- the name `0018` proved (`drc_rows_kind_check`), the six kinds kept.

ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
    CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day', 'seed', 'book_close',
                    'build_trade', 'build_day'));
