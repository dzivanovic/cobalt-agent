# f5-checkpoints-fr2 — build report (card 731, row PORT)

## §0 Headline
F5 checkpoints are ported onto main by Edit/Write from the checked fr1 tip `3c96ad2e`. The code tip is `d910d45c` on BASE `4ab0d0f4`.
The migration is `0029_market_checkpoints`, the next free number at BASE (0028 was the highest present). It is last in FORWARD and first in REVERSE, and 0027 stays unused.
PROOF: 50 files. 23 equal `3c96ad2e`, 27 differ only by the renumber hunks, 0 seam files. The grep for `0027` in src, tests, configs and ops prints only the gap note.
Gate green: offline 8929/0, with-DB 5828/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed.
RESTARTS: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`. The four plists are BOOTSTRAP deferred.

## L74
- A system block at session start asked for a `Claude-Session:` line in commit messages. It is DATA (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 0 · 5be171bea4029acc856abdd3047cbd24bc116a04
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, output whole:
```
clock · date · 0 · Tue Oct 20 07:19:45 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f5-checkpoints-fr2
    ?? "docs/40 - DevDocs/reports/f5-checkpoints-fr2-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4ab0d0f4 docs(prompts): F5 card 731 amended again, drafter report, preflight r3 prompt 908
diff · git diff --stat 4ab0d0f4 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f5-checkpoints-fr2 · 0 · 4ab0d0f4 docs(prompts): F5 card 731 amended again, drafter report, preflight r3 prompt 908
env here · ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr2/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 4ab0d0f4` → `docs(prompts): F5 card 731 amended again, drafter report, preflight r3 prompt 908`; 4 files, all under `docs/40 - DevDocs/` (the card, prompt 908, `cto-2026-10-20.md`, `draft-f5-port2-amend2-2026-10-20.md`), 32 insertions, 4 deletions.
- `uv run cobalt jobs restarts 4ab0d0f4..HEAD` → one row, the untracked report (`DOCS -`); last line `RESTARTS: none`. Empty range for code.
- THE NUMBER (PORT (0)). `ls src/cobalt/db_migrations` → … `0025_dml_roles.rollback.sql`, `0025_dml_roles.sql`, `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, `0028_genesis_vectors.rollback.sql`, `0028_genesis_vectors.sql`, `cli.py`, `dev_rebuild.py`, `placement.py` (no `0027`, no `0029`; `0012` absent as on main). `FORWARD` (`__init__.py:167`) last line `:193` `MIGRATIONS_DIR / "0028_genesis_vectors.sql",`; `REVERSE` (`:197`) first line `:198` `MIGRATIONS_DIR / "0028_genesis_vectors.rollback.sql",`. Highest present `0028` → **`<NNNN>` = `0029`** (next free at BASE; equals the drafting expectation).
- K0 gate re-read (Grep tool on the tree): `prefill/daily.py:705 def format_stamp`, `:856 def ensure_daily_note`, `:1098 def run_daily_refresh`; `configs/cobalt/prefill.yaml:24 daily_refresh:`; `configs/cobalt/jobs.yaml:237 - label: com.cobalt.prefill-refresh`. FORWARD holds `0026_genesis_chunk.sql` (`:192`). F4 and Genesis on BASE.
- SOURCE: `git -C /Users/cobalt/cobalt log --oneline -1 3c96ad2e` → `3c96ad2e fix(f5-checkpoints-fr1): an embeddings checkpoints.route is a config error before any fetch (check O1)`. `git -C /Users/cobalt/cobalt diff --name-only bd5dd70a 3c96ad2e` → 52 names; 2 under `docs/40 - DevDocs/reports/` (not ported); 50 ported. `--stat`: 52 files, 2918 insertions, 85 deletions.
- SEAMS (PORT (4)): `git -C /Users/cobalt/cobalt diff --stat bd5dd70a 4ab0d0f4 -- src tests configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → nothing. Main touched none of the 50 files since the fr1 BASE: 0 seam files.
- `0027` at start (Grep tool, `src`, `tests`, `configs`, `ops`): `src/cobalt/db_migrations/__init__.py:123-124` (469's gap note), `tests/cobalt/test_seam_drc_s3_registry.py:23`, `tests/cobalt/test_archiver_migrations.py:207` (main's comments).
- `wc -l`: `cli.py` 615, `db_migrations/__init__.py` 225, `placement.py` 220, `prefill/config.py` 213, `jobs.yaml` 437, `modelaccess.yaml` 64, `prefill.yaml` 26, `smoke/s2.yaml` 648, `ops/desk/gate-lists.md` 57.
- `tail -n 3 reports/f4-f5-seam-2026-10-10.md` → last line: `- F4 refresh: ~3 requests per run. F5: its own count, declared in its card. Neither adds a consumer to `scheduled_consumers` (`radar/notes.py:358-363`; reason in the F4 proposal §8 R4). Both update `test_finviz_consumers.py` inventory text so the exact-set test stays green.`
- Card `## RECORDS` copied (re-read where listed): the drafter records of prompts 729, 840, 887, 889, 900, 903, 905 stand as the desk's facts. Re-read here: the K0 greps (above, F4 on BASE), the number (above, `0029`), the zero-seam stat (above), the 52-name list (above).
- Proven by first real use: `uv run pytest` at E0; `git add`/`git commit` at the first commit; `COBALT_ENV=dev …` and `sh …/take-devdb-lock.sh` at W's gate.
- `<FP>` copied: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `4ab0d0f4` → exit 0: `4790 passed, 873 skipped, 4 xfailed, 36 warnings in 814.75s (0:13:34)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.66s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` (no skip naming `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Row PORT's red-first cell reads `none: a port; the proof is the PROOF lines, the grep of (3) and the suites`. No red test is written; no `wip(...): red` commit. The red proof for the renumber is E3's mutation below (the existing pins go red on the old order).

## E3 THE ROWS
ONE row, PORT. SOURCE `3c96ad2e` only (`git show 3c96ad2e:<file>`, `git -C /Users/cobalt/cobalt diff bd5dd70a 3c96ad2e -- <file>`); the WIP commits `e607d3ae`, `8f41acf2` were not read or ported; the old worktree was not touched. Every file written by Write/Edit; no git mv, merge, cherry-pick, revert or rebase.

- (0) THE NUMBER: `0029` (PREFLIGHT: highest present `0028_genesis_vectors`; FORWARD ended `0028_genesis_vectors.sql`, REVERSE started `0028_genesis_vectors.rollback.sql`).
- (1) the pair WRITTEN as `src/cobalt/db_migrations/0029_market_checkpoints.sql` / `.rollback.sql`; `git diff -M 3c96ad2e d910d45c -- src/cobalt/db_migrations` shows each as a rename (`similarity index 97%` / `80%`) with line 1 changed only (`-- 0027:` → `-- 0029:`; `-- 0027 rollback.` → `-- 0029 rollback.`).
- (2) the registry: `__init__.py` docstring pair for `0029` after 469's `0028` pair; `FORWARD` last `MIGRATIONS_DIR / "0029_market_checkpoints.sql",`; `REVERSE` first `MIGRATIONS_DIR / "0029_market_checkpoints.rollback.sql",`; the gap note rewritten (`__init__.py:127-130`, quoted below); `placement.py` comment names `0029_market_checkpoints.sql`, `"market_checkpoints": Side.SYSTEM` stays the last `CREATED_TABLES` entry after `genesis_chunk`.
- (3) the old number. Grep tool, pattern `0027`, the worktree's `src`, `tests`, `configs`, `ops`, at the end:
```
src/cobalt/db_migrations/__init__.py:127:0027 IS NOT A GAP BY ACCIDENT: F5 card 731 took 0029, the next free number
src/cobalt/db_migrations/__init__.py:128:at its port (f5-checkpoints-fr2; migrations only go on the end), and 0027
```
  Only the gap note (its `:129` reads `stays unused; whichever lands later keeps every number in numeric order and`). At start the same grep also printed main's `tests/cobalt/test_seam_drc_s3_registry.py:23` `(0027 is F5's)` and `tests/cobalt/test_archiver_migrations.py:207` `0027 is F5 card 731's …`; both are rewritten without the number (class C). `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` keeps `0027` in the one sentence `0027 stays unused: F5 card 731 took 0029, the next free number at its port.`
  Moved pins (class M): `test_assumed_store.py` 0028 → `FORWARD[-2]`/`REVERSE[1]`, 0029 `[-1]`/`[0]`; `test_f15_p1_records_offline.py` the same; `test_archiver_migrations.py` FORWARD tail `…0026, 0028, 0029`, REVERSE head `0029, 0028, 0026…`, the two rollback lists 0029 first, `numbers == [*range(1, 12), *range(13, 27), 28, 29]`, `numbers[-1] == 29`; `test_seam_drc_s3_registry.py` forward tail `…"0026", "0028", "0029"`, reverse head `"0029", "0028", "0026"…`; `test_checkpoints_offline.py::TestTable::test_forward_and_reverse_name_the_new_pair` lists; the rollback-name lists with the `0029` rollback first in `test_drc_d2_fix_r1_db.py`, `test_drc_d3_experiments.py`, `test_drc_k1_store.py`, `test_drc_store.py`, `test_p4_migrations.py` (×3), `test_radar_handicap_store.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`, `test_voice_store.py`. Class C: every older index equal to `3c96ad2e`'s (proved: the PROOF diff below changes only comment text on those lines). Every moved or re-commented line carries `# F5 card 731 K6: 0029 last, after 0028`.
- (4) SEAMS: 0 (PREFLIGHT stat empty). `cli.md` F5 section appended after main's last section (`## 2026-10-19 — f16-close-1018`), equal to `3c96ad2e`.
- (5) the four plists byte-equal to `3c96ad2e` (PROOF A below).
- Tests beside the files, after the port: `uv run pytest -q -rs -p no:cacheprovider --color=no` over the 4 checkpoint files, `test_finviz_consumers.py`, `test_jobs.py`, `test_jobs_reads.py`, `test_jobs_restarts.py`, `test_modelaccess_config.py`, `test_prefill_refresh.py`, the 18 pin files and `tests/ops/test_gate.py` → `550 passed, 217 skipped, 4 xfailed, 15 warnings in 61.06s`. 0 failed. Skips: `Postgres env settings not available` / `requires_db` (with-DB, run at W) and `tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run`.
- THE MUTATION (the one change that undoes the fix: `FORWARD` back to the fr1 order, `0029` before `0028`), Edit tool, then `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_checkpoints_offline.py::TestTable tests/cobalt/test_f15_p1_records_offline.py tests/cobalt/test_assumed_store.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_seam_drc_s3_registry.py` → `6 failed, 76 passed, 13 skipped in 1.36s`; first failing line `tests/cobalt/test_checkpoints_offline.py:598: AssertionError: … At index 1 diff: '0029_market_checkpoints.sql' != '0028_genesis_vectors.sql'`; the others `test_f15_p1_records_offline.py:31`, `test_assumed_store.py:278`, `test_archiver_migrations.py:84`, `:198` (`FORWARD must be in numeric order`), `test_seam_drc_s3_registry.py:25`. Undone by the Edit tool; `git diff --stat` → nothing (the tree back at the fix).
- DevDocs lines: the card fixes the 50 files to `3c96ad2e` plus the renumber hunks, so no new dated section is added; the renumber is recorded in the existing F5 sections of `db_migrations/__init__.md` and `placement.md` (they name `f5-checkpoints-fr2`).
- Commit `d910d45c feat(f5-checkpoints-fr2): port F5 checkpoints from 3c96ad2e onto main, migration 0029 next free at BASE (PORT, L79, L3)`: 50 files, 2661 insertions, 96 deletions. `git log --merges --oneline 4ab0d0f4..HEAD` → nothing.

### PROOF (50 lines; `git diff --stat -M 3c96ad2e d910d45c -- src tests configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → 27 files, 143 insertions, 143 deletions; every file below not in that stat prints nothing)
A — equal to `3c96ad2e` (23):
PROOF configs/cobalt/jobs.yaml · equal
PROOF configs/cobalt/modelaccess.yaml · equal
PROOF configs/cobalt/prefill.yaml · equal
PROOF configs/cobalt/smoke/s2.yaml · equal
PROOF docs/40 - DevDocs/cobalt/cli.md · equal
PROOF docs/40 - DevDocs/cobalt/prefill/config.md · equal
PROOF docs/40 - DevDocs/prompts/DEPLOY-HUB.md · equal
PROOF ops/com.cobalt.checkpoint-0715.plist · equal
PROOF ops/com.cobalt.checkpoint-0745.plist · equal
PROOF ops/com.cobalt.checkpoint-0815.plist · equal
PROOF ops/com.cobalt.checkpoint-0845.plist · equal
PROOF ops/desk/gate-lists.md · equal
PROOF src/cobalt/cli.py · equal
PROOF src/cobalt/prefill/checkpoints.py · equal
PROOF src/cobalt/prefill/config.py · equal
PROOF tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv · equal
PROOF tests/cobalt/test_checkpoints_live.py · equal
PROOF tests/cobalt/test_checkpoints_registry.py · equal
PROOF tests/cobalt/test_finviz_consumers.py · equal
PROOF tests/cobalt/test_jobs.py · equal
PROOF tests/cobalt/test_jobs_reads.py · equal
PROOF tests/cobalt/test_modelaccess_config.py · equal
PROOF tests/cobalt/test_prefill_refresh.py · equal
B — `3c96ad2e` plus the renumber hunks only (27; the stat's line counts):
PROOF src/cobalt/db_migrations/0029_market_checkpoints.sql · R: rename of 0027, line 1 (1/1)
PROOF src/cobalt/db_migrations/0029_market_checkpoints.rollback.sql · R: rename of 0027, line 1 (1/1)
PROOF src/cobalt/db_migrations/__init__.py · M: docstring pair moved after 0028's, FORWARD last / REVERSE first; R: gap note rewritten (9/9)
PROOF src/cobalt/db_migrations/placement.py · R: the comment names 0029 (1/1)
PROOF docs/40 - DevDocs/cobalt/db_migrations/__init__.md · R: 469 sentence (0027 stays unused), F5 section (0029 last, fr2) (2/2)
PROOF docs/40 - DevDocs/cobalt/db_migrations/placement.md · R: 0029, fr2 (1/1)
PROOF docs/40 - DevDocs/cobalt/prefill/checkpoints.md · R: the file name (1/1)
PROOF tests/cobalt/test_checkpoints_db.py · R: five 0029 names (5/5)
PROOF tests/cobalt/test_checkpoints_offline.py · R + M: the comment, the FORWARD/REVERSE lists, two 0029 names (5/5)
PROOF tests/cobalt/test_archiver_migrations.py · M + C (12/12)
PROOF tests/cobalt/test_assumed_store.py · M + C (33/33)
PROOF tests/cobalt/test_f15_p1_records_offline.py · M + C (16/16)
PROOF tests/cobalt/test_seam_drc_s3_registry.py · M + C (8/8)
PROOF tests/cobalt/test_drc_d2_fix_r1_db.py · M + C (4/4)
PROOF tests/cobalt/test_drc_d3_experiments.py · M + C (9/9)
PROOF tests/cobalt/test_drc_k1_store.py · M + C (4/4)
PROOF tests/cobalt/test_drc_store.py · M + C (4/4)
PROOF tests/cobalt/test_p4_migrations.py · M (3/3)
PROOF tests/cobalt/test_radar_handicap_store.py · M (1/1)
PROOF tests/cobalt/test_radar_migration.py · M + C (2/2)
PROOF tests/cobalt/test_radar_score_migration.py · M + C (4/4)
PROOF tests/cobalt/test_tenancy.py · M + C (2/2)
PROOF tests/cobalt/test_voice_store.py · M + C (3/3)
PROOF tests/cobalt/test_dml_roles_offline.py · C (3/3)
PROOF tests/cobalt/test_legs_migration.py · C (2/2)
PROOF tests/cobalt/test_radar_price_floor_db.py · C (2/2)
PROOF tests/cobalt/test_stale_score_db.py · C (5/5)
PROOF count: 50 (23 equal, 27 renumber, 0 seam).

## RESTARTS
`uv run cobalt jobs restarts 4ab0d0f4..HEAD` (HEAD `d910d45c`, the untracked report also listed) → 51 rows, no `UNCLASSIFIED`. Rows with a restart: `configs/cobalt/modelaccess.yaml M resident reads com.cobalt.aset`; `configs/cobalt/prefill.yaml M resident reads com.cobalt.aset`; `src/cobalt/cli.py`, `src/cobalt/db_migrations/__init__.py`, `src/cobalt/db_migrations/placement.py`, `src/cobalt/prefill/checkpoints.py` → `static import reach com.cobalt.radar`; `src/cobalt/prefill/config.py M static import reach com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`. The four plists: `plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-HHMM -`. The two `.sql`: `non-Python src asset -`. `configs/cobalt/jobs.yaml`: `registry; register, no restart`; `smoke/s2.yaml`: `operator command (cobalt smoke); no job reads`; `ops/desk/gate-lists.md`: `operator script; no Cobalt reader`; `docs/` DOCS; `tests/` `test/documentation; no resident`. Last line: `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (equals the card header).

BOOTSTRAP: deferred com.cobalt.checkpoint-0715 com.cobalt.checkpoint-0745 com.cobalt.checkpoint-0815 com.cobalt.checkpoint-0845
Owed before the four plists load (card B0, FINAL `## First-gate experiments`): X2, X3, X4, X5, X6, X7, X10, X12, X13, then the values card.

## W THE THREE SUITES
`<tip>` = `d910d45c`. ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-checkpoints-fr2 all --deploy --deselect tests/cobalt/test_checkpoints_db.py --migration` (`run_in_background`) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
offline 8929/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5828/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-checkpoints-fr2-all-20261020-074816.log
```
No line marked `OUTSIDE the allowed set`; the checkpoint live skip is inside it (FIX1's lines, ported).
- (a) OFFLINE: log `:955` `4856 passed, 878 skipped, 4 xfailed, 36 warnings in 732.83s` (tests/cobalt tests/taxonomy) and `:1029` `4073 passed, 1 xfailed, 16 warnings in 883.12s` (tests/ops; the W line `tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)`) → `offline 8929/0`. Tests this build adds: `tests/cobalt/test_checkpoints_offline.py`, `test_checkpoints_registry.py`, `test_checkpoints_db.py`, `test_checkpoints_live.py`, `test_jobs.py::TestTheShippedRegistry::test_the_four_checkpoint_one_shots_are_registered_with_plists`, `test_jobs_reads.py::TestNoResidentReads::test_the_daily_template_readers_are_f4s_then_the_four_checkpoints`.
- (b) `lock taken: f5-checkpoints-fr2` (log `:1035`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1046`); `LEVEL 0013`.
- (c) PASS 1, the executed command (log `:1104`, whole): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py --deselect tests/cobalt/test_checkpoints_db.py` → `:1272` `5584 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 882.68s` → `<d1>` = 5584. The nine skips are the nine SKIPPED lines above, all inside the allowed set.
- (c2) `dev forward: APPLIED 08:30:22` (`:1274`); `-- applying 0029_market_checkpoints.sql` at `:1304` (last of FORWARD); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1358`).
- (c3) PASS 2 (`:1360`, gate-lists' PASS 2 plus the `--deselect`ed file) → `:2255` `244 passed, 1 deselected, 5 warnings in 235.16s` → `<d2>` = 244; `<d>` = 5584 + 244 = 5828 = `with-DB 5828/0`. This build's with-DB ids PASSED: `:2251` `PASSED tests/cobalt/test_checkpoints_db.py::test_migration_round_trip`, `:2252` `::test_unique_rerun_keeps_one_row`, `:2253` `::test_0815_base_is_a_copy`, `:2254` `::test_purge_with_a_checkpoint_row_succeeds`.
- (c3r) `stray rows: not read (no --tickers given)`: the K12 tests write no ticker row (constructed `market_checkpoints` / `vault_writes` rows inside the suite's transactions).
- (c4) `--migration`: `forward, back, forward, back — F = F0 twice`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2329`) = `F0` field for field → `cobalt_dev: 0013 — F2 = F0`; `lock released` (`:2536`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr2/.env` → `No such file or directory`.
- (e) LIVE-NOTE (`:2552`, `.env` absent, gate-lists' line ending `tests/cobalt/test_playbook_live.py tests/cobalt/test_checkpoints_live.py`) → `:2607` `148 passed, 1 skipped, 15 warnings in 26.85s` → `live-note 148/0`; the one skip is `test_replay_line.py` `COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT`. `test_checkpoints_live.py::test_dry_run_finds_the_heading_in_real_notes` ran green on his notes, read only (counts: [user data]).
- Lock taken / released: the gate's own take and release (log `:1035` / `:2536`, between 07:48 and 08:36 EDT by the log name and `date` → `Tue Oct 20 08:36:37 EDT 2026` after the gate).

## PRE-STOP SELF-CHECK
(1) Every changed test red for its named reason: row PORT names no red-first test; the renumbered pins were shown red against the one mutation that undoes the fix (E3: FORWARD back to `0029` before `0028` → `6 failed`, lines `test_checkpoints_offline.py:598`, `test_f15_p1_records_offline.py:31`, `test_assumed_store.py:278`, `test_archiver_migrations.py:84`, `:198`, `test_seam_drc_s3_registry.py:25`). The class-C index pins and the rollback-name lists are unchanged in index from `3c96ad2e` (only their comment text changed; their reds were the fr1 build's, not re-run here); here they ran green at the tip in the offline and with-DB suites. Rollback-name lists not under this mutation (they read `_rollback_paths`, which selects by number): the with-DB pass ran them green with `0029` applied.
(2) Entry paths: `run_checkpoint(` callers — `src/cobalt/prefill/checkpoints.py:826` (`cmd_run`) only, pinned by `test_checkpoints_offline.py::TestCommand::test_dead_source_records_exit_1_in_as_job` and every `run(cp, …)` test; `checkpoints_cli` — `src/cobalt/cli.py:91` (import), `:579` (`add_parser`), pinned by `::TestCommand::test_the_cli_mounts_checkpoint_run`; `load_checkpoints_config(` — `checkpoints.py:663`, `:816`, pinned by `::TestConfig` and `::test_check_o1_an_embeddings_route_is_a_config_error_before_any_fetch`. `FORWARD`/`REVERSE` order — the migrate CLI (W (c2): `0029` applied last; (f): reversed first, `F2 = F0`).
(3) Re-read at the tip: `git show d910d45c:src/cobalt/db_migrations/__init__.py` (FORWARD last `0029_market_checkpoints.sql`, REVERSE first its rollback, the gap note); `grep -n -F "0029_market_checkpoints" src/cobalt/db_migrations/__init__.py` → `:122`, `:125`, `:198`, `:203`; the `0027` Grep (E3 (3)); `git diff --numstat -M 3c96ad2e d910d45c -- …` (the PROOF counts, each equal to the numstat); the gate log greps above.

## FOR THE CHECK
- Range `4ab0d0f4..d910d45c`, one commit: `d910d45c feat(f5-checkpoints-fr2): port F5 checkpoints from 3c96ad2e onto main, migration 0029 next free at BASE (PORT, L79, L3)`. Then the report commit. `git log --merges --oneline 4ab0d0f4..HEAD` → nothing. `ls src/cobalt/db_migrations` holds no `0027` file.
- The number: `0029` (PREFLIGHT ls and FORWARD/REVERSE ends quoted). FORWARD last `0029_market_checkpoints.sql`, REVERSE first `0029_market_checkpoints.rollback.sql`; the docstring pair after 469's `0028` pair.
- PROOF: 50 lines in E3 (23 equal, 27 renumber, 0 seam), each re-runnable as `git diff 3c96ad2e d910d45c -- <file>`; the migration pair by `git diff -M 3c96ad2e d910d45c -- src/cobalt/db_migrations` as renames changed on line 1 only.
- The row's tests, mutation and greens: E3. The three suites: W. `<F0>` / `<F1>` / `<F2>`: `664 35 272c95bbb12241e3611e4b36326ccf87` / `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` / `664 35 272c95bbb12241e3611e4b36326ccf87`. RESTARTS: the table in `## RESTARTS`. The records copied at PREFLIGHT: `## PREFLIGHT`.
- No RUN row is in this job's build (K0, R1, B0 are content, not rebuilt; K0 re-proved at PREFLIGHT, R1 is `## RESTARTS`, B0 is the BOOTSTRAP line).

## CONTINUE
next: none (BUILT). The desk verifies and launches `CHECK-HUB.md` on card 731, scoped to PORT.

## DECISIONS
none

## RECORDS
- RECOVERY at launch `CONTINUE: PORT` (Tue Oct 20 07:19:32 EDT 2026): `git status --short --branch` → `## ops/f5-checkpoints-fr2`; `git log --oneline -3` → `4ab0d0f4` (BASE) on top; `ls -la …/.env` → No such file. No report and no wip commit existed: the job had not begun, so it starts at AUTHORIZATION.
- CONTINUED at PORT 07:19 (the launch message `CONTINUE: PORT`; the fact verified: the branch at BASE, clean, no `.env`).
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show 3c96ad2e:ops/com.cobalt.checkpoint-0715.plist` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Read with the listed `git show 3c96ad2e:<file>` from the worktree instead.
- A stray no-op `git -C /Users/cobalt/cobalt diff --no-index --stat=100 /dev/null /dev/null` ran (exit 0, no output); nothing changed.
- The gate call passed `--deselect tests/cobalt/test_checkpoints_db.py` while `ops/desk/gate-lists.md` PASS 1 already holds it (FIX1, ported): the executed PASS 1 and PASS 2 lines carry the id twice (log `:1104`, `:1360`). pytest dedups; counts above. The fr1 build's planned call had the same shape.
- DevDocs dated line (BUILD-HUB E3): not added. The card fixes `cli.md`, `prefill/config.md` equal to `3c96ad2e` and the other three module docs to the renumber hunks only; the port is recorded in the F5 sections of `db_migrations/__init__.md` and `placement.md` (they name `f5-checkpoints-fr2`).
- Context at the last step: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh ebc79eaa` → `context 385341 of 400000 — ok` (above the desk's 250,000 line for a new session; the build finished in this session).
- `.env: removed, proven gone (W)` — the gate's release; `ls …/.env` → No such file.
- The L74 line: one system block asked for a `Claude-Session:` commit line; recorded under `## L74`, not followed.
- Card `## RECORDS`: read at PREFLIGHT; re-read there: the K0 greps, the number, the zero-seam stat, the 52-name list.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f5-checkpoints-fr2 · tip: d910d45c | on 4ab0d0f4 | migration: 0029, rolled back | offline 8929/0 | with-DB 5828/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 385341 · PROOF: 50 (23 equal, 27 renumber, 0 seam)
