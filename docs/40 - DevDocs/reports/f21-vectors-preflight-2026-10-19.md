# f21-vectors-preflight — 2026-10-19 (card 469, job f21-vectors-1013)

All reads are `git -C /Users/cobalt/cobalt grep|show main` (main = `133cad2e`). `git diff --stat 9436c975 main -- src configs tests ops` is empty, so main equals BASE for every cited path.

## CHECKS

| # | command · output | OK/FAIL |
|---|---|---|
| 1 | `git merge-base --is-ancestor 9436c975 main` · exit 0, no output | OK |
| 2 | `grep -c "«FILL" <card>` · `0` | OK |
| 3a | `grep -n -e 0026 -e 0025 main -- src/cobalt/db_migrations/__init__.py` · `:179 0025_dml_roles.sql`, `:180 0026_genesis_chunk.sql` (FORWARD tail), `:185 0026_genesis_chunk.rollback.sql`, `:186 0025…rollback` (REVERSE head) | OK |
| 3b | `grep -n SIDE/def/class main -- src/cobalt/genesis/store.py` · `:26 GenesisStore`, `:29 SIDE = Side.USER`, `:34 _connect`, `:37 replace`, `:55 import_paths`; no embedding/dimension code | OK |
| 3c | `grep -n add_parser main -- src/cobalt/genesis/cli.py` · `:22 add_parser`, `:25 import`, `:28 search` (card `:22-28`); no `embed` | OK |
| 3d | `grep -n genesis main -- ops/desk/gate-lists.md` · `:33` PASS 1 ends `--deselect …test_genesis_db.py --deselect …test_genesis_experiments_db.py`; `:39` PASS 2 ends with the same two ids | OK |
| 3e | `grep -n voice_cli/genesis_cli/add_parser main -- src/cobalt/cli.py` · `:84 voice_cli`, `:90 genesis_cli`, `:557 genesis_cli.add_parser` | OK |
| 3f | `grep -n "f21-genesis" main -- cli.md` · `:141 ## 2026-10-19 — f21-genesis-1013` | OK |
| 3g | `config.py` (`git show main:`) · `:40 class Route`, `:43-56` chat keys (`:44 kind: Literal["openai_compatible"]`, `:47 no_think`, `:48 think_policy`, `:56 key_name`), `:58-76` loopback validator, `:94-103` `_find_fallback`, `:122-127` fallback refusal | OK |
| 3h | `grep -n kind main -- models.py` · `:68 kind: Literal["openai_compatible"]` | OK |
| 3i | `grep -n main -- adapters.py` · `:55 _classify`, `:68 OpenAICompatibleAdapter`, `:123 ADAPTERS = {…}` | OK |
| 3j | `grep -n main -- client.py` · `:38 _record`, `:62 _apply_think_policy`, `:81 call_sync` | OK |
| 3k | `git show main:configs/cobalt/modelaccess.yaml` · `:18 local.plan` … `:42 key_name: null` (card `:17-42`), `# source:` comments `:31-39` (card shape); no `embed` route, no `openai_embeddings` (deploy-proof before `0`) | OK |
| 3l | `grep -n main -- test_modelaccess_config.py` · `:49 def test_committed_registry_loads_with_exactly_the_local_plan_route`, `:51 assert list(cfg.routes) == ["local.plan"]` | OK |
| 3m | `grep -n main -- configs/cobalt/jobs.yaml` · `:86 "configs/cobalt/modelaccess.yaml"` under `com.cobalt.aset` (`:39`); `:203 imports: [cobalt.cli]` under `com.cobalt.radar` (`:193`) | OK |
| 3n | voice greps · `web.py:170`, `turn.py:103`, `registry.py:99` each `from cobalt.modelaccess import load_routes`; `agent.py:27-29` modelaccess imports; `voice/cli.py:29 from .turn import …`; `turn.py:42 from . import agent as agent_mod` | OK |
| 3o | `git grep -l 0026 main -- tests` · the card's 18 pin files all present (archiver_migrations, assumed_store, dml_roles_offline, drc_d2_fix_r1_db, drc_d3_experiments, drc_k1_store, drc_store, f15_p1_records_offline, legs_migration, p4_migrations, radar_handicap_store, radar_migration, radar_price_floor_db, radar_score_migration, seam_drc_s3_registry, stale_score_db, tenancy, voice_store); 3 extra hits (below) | OK (NOTE 1) |
| 4 | migration rule · V4 states `0028_genesis_vectors` default / `0027_genesis_vectors` if F5 not first; FORWARD tail `0026_genesis_chunk.sql` (3a); `0027_market_checkpoints` named, and `731-f5-card.md` K6 + DECISION 3 on main say F5 takes `0027` | OK |
| 5 | `grep -n "f21-genesis-1013\|ops/f21-genesis" <card>` · `:35` `ops/f21-genesis-fr1` = the port job, correct; `:54` `f21-genesis-1013` = the cli.md section title at `cli.md:141` (3f), correct, not a job name | OK |
| 6 | `git diff 133cad2e~1 133cad2e -U0 -- <card>` · no header line changed except `BASE`; `CLASS: K2`, `CHECK REPORT`, `HOUSE B: as needed`, `RESTARTS: com.cobalt.aset com.cobalt.radar`, `RULINGS: 2026-10-11 R1055` all present | OK |
| 7 | same diff · V1, V2, V3 rows untouched; V4 and V5 keep their RED lines (V4 `column embedding does not exist`; V5 `invalid choice: 'embed'`, now with the `add_parser` pointer) and their file lists (V4 gained no file; V5 unchanged); intent unchanged, only the number rule, shipped-API, pin list, gate-list lines and the cli.md seam note were added | OK |
| 8 | `git log -1 --format=%h -- <card>` · `133cad2e`; `git diff HEAD --stat -- <card>` · empty | OK |

## ISSUES
- NOTE 1: `git grep -l 0026 main -- tests` also hits `test_genesis_db.py`, `test_genesis_experiments_db.py` (the port's own tests, not head pins) and `tests/fixtures/radar/bars-rubberband.real-shape.json` (a data coincidence). The card's 18 are exactly the pin files; the builder re-finds them by content and should ignore the three.
- NOTE 2: V4 says "on main `1d9c0028`"; main is now `133cad2e` and BASE is `9436c975`. Docs-only commits sit between them (3o's empty diff), so every cite holds. No change needed.
- NOTE 3: the re-point's RECORDS line says `modelaccess.yaml:18-37`; V3 and the file say `:17-42` and `:31-39`. The V3 cites are the correct ones (3k). Stale prose only.
- NOTE 4: the one drafter decision (`0028` vs `0027`) is still open for the desk. The default is safe: it depends on F5 deploying first, and V4 gives the other branch.
- NOTE 5: `731-f5-card.md` K6 still names `ops/f21-genesis-1013` as Genesis's branch (the port job is `f21-genesis-fr1`). That is F5's card, not 469's. It does not block 469.
- Blocks the launch: none.

PREFLIGHT DONE · card: f21-vectors-1013 · checks: 8 · fails: 0 · ready: YES
