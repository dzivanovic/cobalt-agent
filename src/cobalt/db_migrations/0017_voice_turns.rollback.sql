-- 0017 rollback. COST: drops every voice turn row (transcripts, Plans, the
-- expert write ids they carry). The card stop edits those rows point at live
-- in "user".card_stop_edits and are untouched. Snapshot the table first if
-- its rows must survive.
DROP TABLE IF EXISTS "user".voice_turns;
