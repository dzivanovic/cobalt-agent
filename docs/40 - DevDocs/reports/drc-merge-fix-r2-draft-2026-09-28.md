# DRC merge fix r2 — classification and prompts 2026-09-28 — seat `drc-merge-fix-r2-draft-0928`

## §0 Headline
- `17`'s 3 with-DB reds on `4fc270c7` → FIX. U1 is a registry position pin → G1, tests only. U2 and `test_stale_score_db.py:180` have one cause → G2, one `src/` row: the three `drc_rows` statements in the `0018` rollback wrapped in `0013`'s `DO $migration$` / `to_regclass` guard.
- A test-only setup cannot fix U2: its own `:190` and `:180` both repeat the reverse after `drc_rows` is gone. `0016`/`0017` rollbacks are already `IF EXISTS`, so no further row.
- Written: `prompts/2026-09-28/32-drc-merge-fix-r2-build.md` (34,243 B) and `prompts/2026-09-28/33-drc-merge-fix-r2-check.md` (40,525 B; supersedes `18`). New rule strings: 0.
- ESCALATE: 1.

## L74
A block arrived appended to the Bash tool result that printed `31-draft-drc-merge-fix-r2.md`. It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed. This seat commits nothing.

## Authorization
`grep -n -F "31-draft-drc-merge-fix-r2.md" ".../cto-2026-09-28.md"` → `:76` `| R68 | 12:57 ET | — DESK LAUNCH ROW: \`31-draft-drc-merge-fix-r2.md\` …` `| LAUNCHED |`. Read Mon Sep 28 12:58:01 EDT 2026.

## Classification
Source file: `B` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md` (committed in `0e75e46d`). Code lines are at `4fc270c7` (`git log 4fc270c7..0e75e46d -- src tests configs` empty). Merged order at `4fc270c7:src/cobalt/db_migrations/__init__.py:107–125`: FORWARD tail `0013, 0014, 0015, 0016, 0017, 0018` = `[-6]`…`[-1]`; REVERSE `:128–` head `0018, 0017, 0016, 0015, 0014, 0013` = `[0]`…`[5]`. `_rollback_paths(n)` = REVERSE entries numbered above `n` (`cli.py:774–784`); `_apply` runs whole files in one transaction (`cli.py:475–486`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | U1 `test_stale_score_db.py:159` `FORWARD[-2]` = 0015; at the tip `FORWARD[-2]` is 0017 (same test `:160–162` pins `REVERSE[1]`, `FORWARD[-4]`, `REVERSE[3]`) | `B:338–340` | FIX | R38 (1); r1 U1 (`drc-merge-fix-r1-draft-2026-09-28.md:31`); `17` W (c1) | G1, tests only: `FORWARD[-4]` / `REVERSE[3]` = 0015's pair, `FORWARD[-6]` / `REVERSE[5]` = 0013's. Verified against `__init__.py:119–124`, `:129–134`. Intent: 0015 after 0013 and reversed before it. Four pins kept, none added. |
| 2 | U2 `test_radar_handicap_store.py:187` `_apply(conn, _rollback_paths("0013"))` → `UndefinedTable "user.drc_rows"` at `0018_drc_stated_books.rollback.sql` LINE 7; 0016 never applied in that test (`:174` applies FORWARD < 14) | `B:328–336` | FIX | r1 U2 (`…fix-r1-draft…:32`); `17` W (c1); L45 | G2, one `src/` row: `0018_drc_stated_books.rollback.sql:7–10` wrapped in `DO $migration$ … IF to_regclass('"user".drc_rows') IS NULL THEN RETURN; END IF; … END $migration$;`. The idiom is main's own (`0013_tunables_slug_nullable.rollback.sql:4–8`). The comment `:1–5` and `:11` `DROP TABLE IF EXISTS "user".drc_stated_books;` are unchanged. |
| 3 | `test_stale_score_db.py:180` `_apply(conn, _rollback_paths("0013"))  # a repeated reverse is a no-op` → same `UndefinedTable`, after `:178` had reversed 0016 | `B:342–351` | FIX (= row 2's G2) | `17` ESCALATE 1 (`B:409`); `__init__.py:106` "every file idempotent" | Cleared by G2 with no test edit. A test-only setup cannot reach it: `:180` reverses a tree where 0016 is already gone. U2's own `:190` repeats the reverse the same way, so a test setup would leave U2 red too. |
| 4 | `17` ESCALATE 1: W (c1) red, 3 tests; ASK DESK 1 of r1 (test setup vs `to_regclass` guard) | `B:409` | FIX (= rows 1–3) | R66; L75 | Built as G1–G2, not counted twice. The houses settled it (L67): the guard keeps `:180`'s and `:190`'s contract. `33` (vi) puts it to them. |
| 5 | `17` ESCALATE 2: `--proof-only` prints no numeric level; `0013` read from one extra catalog query | `B:410` | OUT OF SCOPE — RECORD | L35; L76 | Not a code finding. `32` types that read as `<LV>` (0014's three columns absent, 0013's `slug` nullable), on the listed `cobalt db query *` prefix. |

Rollbacks from `0013` up at `4fc270c7` (step (5)); how each stays a no-op on absent objects:
- `0013_tunables_slug_nullable.rollback.sql:4–8`: `DO $migration$` / `IF to_regclass('"user".tunables') IS NULL THEN RETURN;`. This is the only `to_regclass` guard under `db_migrations/`.
- `0014_radar_handicap.rollback.sql:7–10`: `DROP COLUMN IF EXISTS` ×3.
- `0015_shadow_agreement_stale.rollback.sql:4`: `CREATE OR REPLACE VIEW` (`:3` "idempotent").
- `0016_drc.rollback.sql:6–8`: `DROP TABLE IF EXISTS` ×3. Not the unguarded shape, so no row.
- `0017_voice_turns.rollback.sql:5`: `DROP TABLE IF EXISTS`.
- `0018_drc_stated_books.rollback.sql:7–10`: unguarded. `:11` is `IF EXISTS`.

With the tables present, G2 runs the same three statements in the same order in the same `_apply` transaction. These with-DB tests prove it and were green in `17`'s (c1): `test_drc_k1_store.py:213` (the CHECK restored by name), `test_drc_k1_store.py:221` (deletes `seed`/`book_close`, drops the table, restores the CHECK) and `test_drc_k1_experiments.py:359`. `32` T re-runs all three after G2. No offline test pins the file's statements: `test_drc_k1_store.py:140` reads only the COST lines, which G2 keeps.

## RECORDS
- `32`'s order: the lock is taken once at `LOCK` (`17`'s W (a)–(b) plus `<LV>`) and held through R0, the rows, T, the fix commit and W. O runs after W (f) step 3 because an offline run needs `.env` gone. See ESCALATE 1.
- `32` W (f) adds step 2: the same `--rollback --down-to 0013` a second time on the real `cobalt_dev`, `<F3>` = `<F2>`. It uses the string already on the line.
- `32` expects O `3547 passed · 525 skipped` (unchanged from `17`) and W (c1) `4057 passed` (`17`'s 4054 + the 3). Pass 2 is `9 passed`.
- `32`'s PREFLIGHT tip is `0e75e46d` (`17`'s wip report commit) over `4fc270c7`. It was read at 13:01 EDT, with main at `20139f3d`.
- `33` checks `10163d51..<r2 tip>`: 12 resolutions, F1–F8, G1–G2, and `32`'s suites. It adds question (vi) (the rollback guard) and stages every rollback from 0013 up, plus the 0018 rollback as it stood at `4fc270c7`.
- Placeholders: `grep -c -F` of the launch-row token = 1 line in each prompt (the AUTHORIZATION row gate). The `FILL AT LAUNCH` tokens are `32:3` (tip read) and `33:43` (built line) and `33:66` (ceiling), plus each file's gate line and `33:1`'s definition.

## OWNER ITEMS
NONE.

## FOR DEJAN
New strings: NONE. `32`'s line 5 = `17`'s line 5 with only the path and `drc-merge-fix-r2-build` changed (`diff` after substitution: identical). `comm` of quoted Bash tokens: 26 common, 0 either side. `33`'s launch line = `18`'s with only the path and `drc-merge-fix-r2-check` changed (identical). `comm`: 15 common, 0 either side.

## ESCALATE
1. ASK DESK: `31` lists O before W and puts R0 and W under one lock. An offline run needs `.env` gone, so both cannot hold. Should `32` release and retake the lock around O? [13:06 EDT] Safe default taken: one lock from `LOCK` to W (f) step 3, and O after W. A red O then comes after `cobalt_dev` is already restored.

## CONTINUE
For the desk: commit this report, `32` and `33`. Answer ASK DESK 1 if the order should change (that would be an L19 re-issue of `32`). Fill each prompt's launch-row placeholder and its FILL AT LAUNCH values. Launch `32` (acceptEdits) only while the lock is free. Launch `33` once `32` is BUILT. `18` is never launched.

DRC MERGE FIX R2 DRAFTED · FIX: 3 · NOT REAL: 0 · UNPROVEN: 0 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · code change: src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql, tests/cobalt/test_stale_score_db.py · prompts: 2 · new rule strings: 0 · ESCALATE: 1
