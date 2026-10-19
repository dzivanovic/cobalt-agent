# Card 731 `f5-checkpoints-1018` — preflight round 6 (2026-10-19)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE `40e646ed`, TIP empty (the desk's), REPORT, CHECK REPORT, HOUSE B, BAND, RULINGS, RESTARTS, BOOTSTRAP present, column 0 | OK |
| 2 | `git -C /Users/cobalt/cobalt diff HEAD -- <card>` | empty | OK |
| 3 | `git log --oneline -3 -- <card>` | `cccdd69f` (renumber to 0027), `13e1c7e9`, `1bd7766b`: the amend is committed | OK |
| 4 | `git rev-parse HEAD 40e646ed ops/f21-genesis-1013` | HEAD `cccdd69f…`; BASE `40e646edf726…`; Genesis branch `817a07c3…` | OK |
| 5 | placeholder scan `grep -o -n -E "<[A-Za-z_]+>\|«…»\|ASK DESK\|TBD\|TODO"` | `<BASE>`, `<tip>` (desk's), `<NNNN>` (K6/RECORDS, resolved to `0027` in K0/K6), `<reason>`, `<kind>` (runtime message strings); no `«FILL`, `ASK DESK`, `TBD`, `TODO` | OK |
| 6 | `grep -n -e launchctl -e --add-dir -e --allowedTools -e "claude --bg" -e desk-launch <card>` (R411, R412) | one hit, line 48 `## NOT IN THIS JOB`: a prohibition; no command string added to a launch line | OK |
| 7 | `grep -n -e 0025 -e 0026 -e 0027 <card>` | K0 (23), K6 (29), FOR THE CHECK (68), DECISION 3 (89), RECORDS (100, 103) all consistent: K6 and its files `0027`; Genesis `0026`; BASE facts `0025` | OK |
| 8 | K0 reads `0027`, `FORWARD` ending `0026_genesis_chunk.sql` proves it, `0025_dml_roles.sql` → `FAILED: K0 — Genesis (card 468) not merged` | present on card line 23 | OK |
| 9 | K6 RED text | `FORWARD[-1].name == "0026_genesis_chunk.sql"`; `KeyError` in `side_of` | OK |
| 10 | head-pin greps `grep -rn -e "0025" -e "0026" tests` and the moved-line comment | K6 names the grep and the comment `# F5 card 731 K6: 0027 after Genesis 0026` (count 1 in the card, in K6) | OK |
| 11 | DECISION 3 | `0027`; Genesis BUILT, deploys first; K0 re-proves `FORWARD` ends `0026_genesis_chunk.sql` | OK |
| 12 | FOR THE CHECK line about the lower number (card line 68) | "If Genesis's check fails and F5 would ship first, the desk takes the lower number (0026) back (brain 2026-10-19)" | OK |
| 13 | `git show ops/f21-genesis-1013:src/cobalt/db_migrations/__init__.py` | `FORWARD` tail `0026_genesis_chunk.sql`; `REVERSE` head `0026_genesis_chunk.rollback.sql` | OK |
| 14 | `git show ops/f21-genesis-1013:tests/cobalt/test_dml_roles_offline.py` | `FORWARD[-2].name == "0025_dml_roles.sql"`, `REVERSE[1].name == "0025_dml_roles.rollback.sql"` | OK |
| 15 | `git show ops/f21-genesis-1013:src/cobalt/db_migrations/placement.py` | `CREATED_TABLES` ends `"genesis_chunk": Side.USER` (so `"market_checkpoints"` goes after it) | OK |
| 16 | `git diff 40e646ed ops/f21-genesis-1013 --stat` vs K6's 18 pin files + `gate-lists.md` | all 18 named files are in the stat (archiver_migrations, assumed_store, dml_roles_offline, drc_d2_fix_r1_db, drc_d3_experiments, drc_k1_store, drc_store, f15_p1_records_offline, legs_migration, p4_migrations, radar_handicap_store, radar_migration, radar_price_floor_db, radar_score_migration, seam_drc_s3_registry, stale_score_db, tenancy, voice_store); `ops/desk/gate-lists.md` `--deselect` tails gain `test_genesis_db.py`, `test_genesis_experiments_db.py` | OK |
| 17 | K6's example moves vs Genesis diff | `f15_p1` `[-1]/[0]` at `0026` ✓; `tenancy` `[:15]`→`[:16]` ✓; `archiver_migrations` `range(13, 27)` ✓, `[:16]` ✓; `radar_migration`, `radar_score_migration` `[:16]` ✓; `seam_drc_s3` tail `…"0026"`, `names[-4:]` ✓ | OK |
| 18 | K0 at BASE: `git grep` for `def ensure_daily_note`, `def format_stamp`, `daily_refresh` | `daily.py:856`, `:705`, `prefill.yaml:24` | OK |
| 19 | K0 at BASE: `git grep -n "label: com.cobalt.prefill-refresh"` | `jobs.yaml:214` | OK |
| 20 | `ls src/cobalt/db_migrations` (main working tree) | ends `0025_dml_roles.*`; no `0026` file → K0 would stop today: `FAILED: K0 — Genesis (card 468) not merged` | OK (NOTE) |
| 21 | K4 pin exists: `grep -n "list(cfg.routes)" tests/cobalt/test_modelaccess_config.py` | `51: assert list(cfg.routes) == ["local.plan"]`; K4 files cell names the test; card says `["local.plan", "checkpoint.narrative"]` | OK |
| 22 | K9 pin exists: `grep -n "entry.readers ==" tests/cobalt/test_prefill_refresh.py` | `391: assert entry.readers == ["com.cobalt.prefill-daily", self.LABEL]`; K9 and `## NOT IN THIS JOB` allow only that line | OK |
| 23 | round-5 checks 1–21 re-run (header, DECISION 2 synthetic fixture + UNMEASURED `60` / `512`, B0 X2/X3, CHECK ASKS, K4/K9 files cells) | unchanged from r5; all hold on the amended card | OK |

## ISSUES
- NOTE · checks 8, 20 · BASE `40e646ed` is still `FORWARD` ending `0025`: K0 stops with `FAILED: K0 — Genesis (card 468) not merged` until Genesis merges. For the desk: BASE refreshes after Genesis merges, then K0 is re-proved before launch.
- NOTE · check 4 · the card names Genesis tip `66439da6`; `ops/f21-genesis-1013` is now at `817a07c3` (a docs commit, the build report, on top; `66439da6` is an ancestor). Same migration facts at both. Harmless.
- NOTE · check 5 · `<NNNN>` is K0's resolved `0027`; `<reason>`, `<kind>` are runtime message templates; `<tip>` a command argument. TIP is empty by design (the desk's).
- NOTE · carried from r5 · K6 does not name the `GRANT SELECT, INSERT, UPDATE, DELETE ON system.market_checkpoints TO cobalt_apply_system` and sequence `GRANT USAGE` (`CARD.md` migration checklist item 4); `test_dml_roles_db.py` G1b would catch it. The desk may add it before launch.
- NOTE · the merged-state pin list is traced from Genesis's diff, not a merged tree (drafter's ASK DESK 2); the card tells the builder to re-find each by content.
- NOTE · header `CLASS`, `INSTALL` are not CARD.md keys (as r1–r5).

PREFLIGHT DONE · card: f5-checkpoints-1018 · checks: 23 · fails: 0 · ready: YES
