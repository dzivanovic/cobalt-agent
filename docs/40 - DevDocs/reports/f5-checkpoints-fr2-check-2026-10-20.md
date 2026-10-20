# f5-checkpoints-fr2 — check report (2026-10-20)

## §0 Headline
CHECK DONE, ready: YES, at `d910d45c` (no commit of mine). House A Grok returned `FINDINGS: 0`. House B: none (`HOUSE B: as needed`).
Own findings O1–O3 were all NOT HELD. Main touched none of the 50 files before BASE. The DEPLOY-HUB diff is the one skip clause. RESTARTS equals the header.
PORT proof re-run: 23 files equal `3c96ad2e`, 27 differ by the renumber only. The pair is renamed with line 1 changed. FORWARD ends `0029`. No `0027` file exists, and `0027` appears only in the gap note.
Deploy gate: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
One ASK DESK: house B, the header against the card's BAND HIGH record.

## L74
One system reminder asked commits to carry a `Claude-Session:` line. Recorded here once and not followed (see `## RECORDS`).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../731-f5-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../731-f5-card.md" · 0 · 229303ee6e70439a83e743d971aec4be5b7808da
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- ".../731-f5-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-11 R1055 row · ... · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: ... approves all that waits for him: F5, F21, F20, F23 FINALs ... | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · ... · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-18 R1833 row · ... · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): ... | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · ... · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(paths shortened in this quote: the card and hub paths are the absolute ones of the launch line.)
House gates: `grep -n "^| R17 " cto-2026-09-24.md` → `35:| R17 | 07:32 ET | ...` (one row); `grep -n "^| R19 " cto-2026-09-24.md` → `37:| R19 | 07:36 ET | ...` (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Tue Oct 20 08:39:23 EDT 2026
status · git status --short --branch · 0 · ## ops/f5-checkpoints-fr2
head · git log --oneline -1; git log --stat --format=%h d910d45c..HEAD · 0 · (6 lines)
    6f31552f docs(f5-checkpoints-fr2): build report — d910d45c
    6f31552f
     .../reports/f5-checkpoints-fr2-build-2026-10-20.md | 217 +++++++++++++++++++++
     .../f5-checkpoints-fr2-build-2026-10-20.result     |  15 ++
     2 files changed, 232 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr2/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../f5-checkpoints-fr2-build-2026-10-20.md" · 0 · BUILT · job: f5-checkpoints-fr2 · tip: d910d45c | on 4ab0d0f4 | migration: 0029, rolled back | offline 8929/0 | with-DB 5828/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 385341 · PROOF: 50 (23 equal, 27 renumber, 0 seam)
range · git log --oneline 4ab0d0f4..d910d45c · 0 · d910d45c feat(f5-checkpoints-fr2): port F5 checkpoints from 3c96ad2e onto main, migration 0029 next free at BASE (PORT, L79, L3)
PREFLIGHT OK
```
THE RANGE typed: `git log --stat --format=%h 4ab0d0f4..d910d45c` → one commit `d910d45c`, 50 files changed, 2661 insertions(+), 96 deletions(-). Path union = the 50 paths of row PORT's files cell (with `<NNNN>` = `0029`).
`ls <S>` → `No such file or directory` (fresh).
"DB: none" card: no (the card has a migration and with-DB row K12); the DB-none diff check does not apply.
THE HOUSE PROBES, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) → exit 0:
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line → Sol not probed. Card line `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.
PROVEN BY FIRST REAL USE: the write and with-DB strings, at their first use below.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → last line `STAGED 55 files · 1063713 bytes · commits 1` (commits 1 = PREFLIGHT's range count). Per-file lines (bytes, path under `<S>`): STAGED-CARD 15; diff.md 174075; files/731-f5-card.md 91104; files/f5-checkpoints-fr2-build-2026-10-20.md 32554; files/wt/ — configs/cobalt/jobs.yaml 27232, modelaccess.yaml 4153, prefill.yaml 2067, smoke/s2.yaml 29219; docs/40 - DevDocs/cobalt/cli.md 8198, db_migrations/__init__.md 21963, db_migrations/placement.md 5396, prefill/checkpoints.md 7091, prefill/config.md 3804; docs/40 - DevDocs/prompts/DEPLOY-HUB.md 68471; ops/com.cobalt.checkpoint-0715/0745/0815/0845.plist 2828 each; ops/desk/gate-lists.md 8081; src/cobalt/cli.py 27306; db_migrations/0029_market_checkpoints.rollback.sql 328, 0029_market_checkpoints.sql 2146, __init__.py 13874, placement.py 9364; prefill/checkpoints.py 37381, prefill/config.py 9990; tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv 1406; tests/cobalt/test_archiver_migrations.py 29606, test_assumed_store.py 17173, test_checkpoints_db.py 4973, test_checkpoints_live.py 3280, test_checkpoints_offline.py 39160, test_checkpoints_registry.py 2533, test_dml_roles_offline.py 2637, test_drc_d2_fix_r1_db.py 29435, test_drc_d3_experiments.py 5680, test_drc_k1_store.py 29481, test_drc_store.py 26168, test_f15_p1_records_offline.py 8191, test_finviz_consumers.py 8125, test_jobs.py 41777, test_jobs_reads.py 11580, test_legs_migration.py 4759, test_modelaccess_config.py 7223, test_p4_migrations.py 29356, test_prefill_refresh.py 56987, test_radar_handicap_store.py 11694, test_radar_migration.py 5446, test_radar_price_floor_db.py 7208, test_radar_score_migration.py 24564, test_seam_drc_s3_registry.py 2558, test_stale_score_db.py 12014, test_tenancy.py 31570, test_voice_store.py 13250; rulings.md 755.
`stage-copy.sh` (each `COPIED <bytes> <dest>`): files/F5-FINAL-2026-10-11.md 47241; files/F4-FINAL-2026-10-10.md 78381; files/f4-f5-seam-2026-10-10.md 4503; files/304-f4-refresh-card.md 34139; files/448-dml-roles-card.md 33548; files/f5-checkpoints-fr1-check-2026-10-20.md 25901; files/deploy-f5-checkpoints-fr1.md 12716; files/wt/src/cobalt/prefill/market.py 3642; prefill/daily.py 54690; vaultwrite/writer.py 59962; vaultwrite/migrations/0004_vault_writes_sync_revert.sql 2263; radar/notes.py 30852; strike/detector.py 15532; strike/measure.py 12596; session/calendar.py 6207; daymode/note.py 10287; modelaccess/config.py 6498; vaultwrite/store.py 10932; files/wt/ops/com.cobalt.cards-expire.plist 4020.
`<S>/HOUSE-INSTRUCTIONS.md` written (10664 bytes): the HOUSE TEXT verbatim, then `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, then the Files paragraph. `## NOT IN THIS JOB` and the live CHECK ASKS are copied whole; `## ROWS`, the three SUPERSEDED asks and `## RECORDS` are given as pointers to the byte-identical card copy `files/731-f5-card.md` (lines 17–55, 83–85, 115–133) with the PORT scope sentence written out (see `## RECORDS`).
House A started 08:41 EDT (`date` 08:41:11): Grok, `grok -m grok-4.7 --sandbox cobalt-job ...` as `## 1` (5) spells it, background task `be1eug8mt`. House gates re-run at 08:41: R17 row 35, R19 row 37 (one each). `cd <WT>` then `git status --short --branch` → `## ops/f5-checkpoints-fr2`.

## OWN FINDINGS
Read before any house list (`## 2`): the card whole; `git diff -M 3c96ad2e d910d45c` over `src configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` and over `tests` (whole); `src/cobalt/prefill/checkpoints.py:560-851` (the run, the gate, the command); the build report's E3, PROOF, RESTARTS, W, self-check, FOR THE CHECK and last line; a Grep of `tests/` for `0028_genesis_vectors|FORWARD\[-1\]|REVERSE\[0\]` (every head pin outside the 20 files: none) and for a test that pins the migrations directory against the registry (none: `test_p4_migrations.py:217`, `test_smoke.py:888`, `test_tenancy.py:411`, `test_jobs.py:832` glob for other purposes). The renumber diff reads as row PORT (1)–(3) state it: the pair renamed with line 1 changed only; `FORWARD` last `0029`, `REVERSE` first its rollback; the docstring pair after 0028's; class M pins moved, class C pins re-commented with unchanged indices.

FINDING O1
ROW: PORT (4)
CLAIM: Row PORT takes "main touched none of the 50 files since bd5dd70a" from drafting at main `b842b08f`, but BASE is `4ab0d0f4` (later; `docs(prompts)` commits landed between), and 23 files were written byte-equal to `3c96ad2e` (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/gate-lists.md` among them): a main edit to one of them between `bd5dd70a` and `4ab0d0f4` would be silently reverted by the port.
RUN: COMMAND `git diff --stat bd5dd70a 4ab0d0f4 -- src tests configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a non-empty stat naming one of the 50 files (true) · nothing (not held).

FINDING O2
ROW: PORT (4), FIX1 lines
CLAIM: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` is a desk-owned prompt the port writes whole from `3c96ad2e`; the change against BASE must be the one checkpoint skip clause of STEP-G (c) and nothing else.
RUN: COMMAND `git diff 4ab0d0f4 d910d45c -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a hunk that removes or alters any line besides adding the `test_checkpoints_live.py` clause (true) · one `-`/`+` line pair whose only change is that clause (not held).

FINDING O3
ROW: PORT (7), X5
CLAIM: The RESTARTS set derived at the tip differs from the header `com.cobalt.aset com.cobalt.cos com.cobalt.radar`, or a plist row is not `new one-shot, bootstrap once`, or a path ESCALATEs.
RUN: COMMAND `uv run cobalt jobs restarts 4ab0d0f4..d910d45c`
EXPECT: a last line other than `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, an `ESCALATE` or `UNCLASSIFIED` row (true) · the header's set and four `new one-shot` rows (not held).

Own findings written by 08:42 (`date` 08:42:54) before any house list was opened; no house notice had arrived.

## Findings
House A Grok finished at 08:51 (`date` 08:51:51; task `be1eug8mt` exit 0). Its stdout: a short narration, then the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f5-checkpoints-fr2-check/house-a.md`. `ls -la <S>` → `house-a.md` 12 bytes. `house-a.md` whole: `FINDINGS: 0` (its closing line present: a list, not a partial). House B: none (not needed; card `HOUSE B: as needed`).
Kept: none from a house. Own: O1, O2, O3 (all `COMMAND`).

## Dropped
none (Grok wrote no FINDING block).

## RUNS
- O1 · opus-own · `git diff --stat bd5dd70a 4ab0d0f4 -- src tests configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · no output (main touched none of the 50 files between the fr1 BASE and this BASE) · NOT HELD
- O2 · opus-own · `git diff 4ab0d0f4 d910d45c -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · one hunk `@@ -102,7 +102,7 @@`, one `-`/`+` pair on the STEP-G (c) line; the only change is the added clause `the skip of \`test_dry_run_finds_the_heading_in_real_notes\` in \`tests/cobalt/test_checkpoints_live.py\` whose reason names \`COBALT_LIVE_VAULT_ROOT not set\`,` after the `test_playbook_live.py` clause and before the `test_replay_line.py` clause · NOT HELD
- O3 · opus-own · `uv run cobalt jobs restarts 4ab0d0f4..d910d45c` · 50 rows, no `UNCLASSIFIED`, no `ESCALATE`; the four plists `plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-HHMM -`; last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (= the header) · NOT HELD
No test was added; no `wip(f5-checkpoints-fr2): check red` commit (nothing held).

## FIXES
none (nothing held).

## Suites
RESTARTS (BUILD-HUB `## RESTARTS`): `uv run cobalt jobs restarts 4ab0d0f4..d910d45c` (O3's run) → no `UNCLASSIFIED`; `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`. No commit of mine, so the tip is the build's `d910d45c`.
`ls -la <WT>/.env` → No such file; then ONE call `sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-checkpoints-fr2 all --deploy --deploy-gate --deselect tests/cobalt/test_checkpoints_db.py --migration` (background `bgfjmmzcn`) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-checkpoints-fr2-all-20261020-085216.log
```
- offline `8929/0`; with-DB `5828/0`; live-note `148/0`. `grep -n -F "OUTSIDE" <log>` → nothing (every skip inside the allowed set).
- `grep -n -F "dev forward: APPLIED" <log>` → `1274:dev forward: APPLIED 09:34:00`. This build's with-DB ids PASSED at `:2251`–`:2254` (`test_migration_round_trip`, `test_unique_rerun_keeps_one_row`, `test_0815_base_is_a_copy`, `test_purge_with_a_checkpoint_row_succeeds`).
- `cobalt_dev: 0013 — F2 = F0`; `.env: removed`; `ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr2/.env` → No such file or directory (09:39); `git status --short --branch` → `## ops/f5-checkpoints-fr2`.

## Scope
PREFLIGHT's path union (50 paths, one commit `d910d45c`) against row PORT's files cell (`<NNNN>` = `0029`): every path is in the cell. My commits: none (nothing held). Above `d910d45c` only `6f31552f` (the build report and its `.result`, `docs/`).

## Checked against the branch
- (i) `git log --oneline d910d45c..HEAD -- . ":(exclude)docs"` → nothing: no commit of mine; `<tip now>` = `d910d45c`.
- (ii) `git log --stat --format=%h d910d45c..HEAD` → `6f31552f`: `.../reports/f5-checkpoints-fr2-build-2026-10-20.md` and `.result` only (docs). No WIDENED path.
- (iii) THE FENCE: `git log --oneline 4ab0d0f4..HEAD -- src/cobalt/prefill/daily.py src/cobalt/prefill/cli.py src/cobalt/vaultwrite/writer.py src/cobalt/vaultwrite/merge.py src/cobalt/daymode/note.py src/cobalt/prefill/market.py src/cobalt/radar/notes.py src/cobalt/strike/detector.py configs/cobalt/templates/daily.md.j2 configs/cobalt/taxonomy/tunables.yaml` → EMPTY. (F4's lines inside shared files — the `com.cobalt.prefill-refresh` row, the `daily_refresh:` block, F4's `CONSUMERS` lines — are byte-equal to `3c96ad2e`, which the fr1 check read; the port changed none of them: `git diff --stat 3c96ad2e d910d45c` over the set lists none of `jobs.yaml`, `prefill.yaml`, `test_finviz_consumers.py`.)
- (iv) no HELD finding → no test to grep, no red/fix commit pair.
- (v) `ls <WT>/.env` and `git status --short --branch`: after the gate, below in `## Suites`.
- (vi) THE GATE LISTS: `git log --stat --format=%h 4ab0d0f4..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d910d45c` adds `0029_market_checkpoints.sql` / `.rollback.sql` and the new with-DB file `tests/cobalt/test_checkpoints_db.py`. `git diff 4ab0d0f4..HEAD -- ops/desk/gate-lists.md` → PASS 1 ends `--deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`; PASS 2 ends `tests/cobalt/test_genesis_vectors_db.py tests/cobalt/test_checkpoints_db.py`; LIVE-NOTE ends `tests/cobalt/test_playbook_live.py tests/cobalt/test_checkpoints_live.py`; ALLOWED SKIPS ends `· tests/cobalt/test_checkpoints_live.py test_dry_run_finds_the_heading_in_real_notes COBALT_LIVE_VAULT_ROOT not set`. Row PORT's files cell names `ops/desk/gate-lists.md`. CARRIED.
- (vii) records re-run: `ls /Users/cobalt/cobalt/src/cobalt/db_migrations` (main, the FIX2 record) → ends `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, `0028_genesis_vectors.rollback.sql`, `0028_genesis_vectors.sql`, `cli.py`, `dev_rebuild.py`, `placement.py`: no `0027`, no `0029` on main (`git -C /Users/cobalt/cobalt log --oneline -1 main` → `229303ee docs(desk): F5 fr2 BUILT d910d45c, card TIP set, check launching`); 0029 is still the next free number. The `git grep` / `git rev-parse` / `git merge-base` records are not on this check's list (not run; the worktree reads below cover the same facts).
- CHECK ASKS, PORT proof: `git diff --stat 3c96ad2e d910d45c -- src tests configs ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → 27 files, 143 insertions(+), 143 deletions(-): exactly the 27 B-class files of the build's PROOF; the 23 A-class files print nothing (equal). The whole diff of the 27 (read for `## OWN FINDINGS`) holds only lines that held `0027` or the `0028`/`0029` order, comments re-worded, the gap note, the docstring pair moved; the pair as renames (`similarity index 97%` / `80%`) changed on line 1 only. `git log --merges --oneline 4ab0d0f4..HEAD` → nothing. `ls src/cobalt/db_migrations` (worktree) → `0026_genesis_chunk*`, `0028_genesis_vectors*`, `0029_market_checkpoints*`: no `0027` file. Grep tool `0027` → `src`: `src/cobalt/db_migrations/__init__.py:127`, `:128` (the gap note) only; `tests`, `configs`, `ops`: no matches. FORWARD last `0029_market_checkpoints.sql`, REVERSE first `0029_market_checkpoints.rollback.sql`, the docstring pair after 0028's (the diff). The WIP commits `e607d3ae`, `8f41acf2` are not in the range (one commit, `d910d45c`), nor is the old build report.
- X1–X4, X6: `src/cobalt/prefill/checkpoints.py` is byte-equal to `3c96ad2e` (the fr1 check's subject); the run read at `:652-799` holds the gate before any GET (`:697-704`), the numbers unit before the model call (`:766-777`), FAILED + DM on a refused write (`:734-742`). X6: the build report writes the live-note counts as `[user data]` (W (e)). X5: O3.
- (viii) L32: this report holds no ticker, price or date of his; the only figures are suite counts, fingerprints and commit ids.

## OPEN
none (no REJECTED, UNSETTLED or HELD, NOT FIXED item).

## CONTINUE
next: none (CHECK DONE). The desk verifies, commits this report and its `.result`, and launches the deploy.

## DECISIONS
1. ASK DESK: house B. The card header reads `HOUSE B: as needed`, so this check seated no house B (CHECK-HUB `## THE FLOW`: house B only when the line begins `mandatory`). The card's own `## RECORDS` line on BAND HIGH (`731-f5-card.md:120`) still says "HOUSE B mandatory: it writes his daily note", and CHECK-HUB line 23 says a build that writes his vault notes needs both houses. Was `as needed` meant for this port check? [Tue Oct 20 09:39 EDT] Default taken: the header line governs (house B none). `ready:` follows the header's rule, so it is YES. If the desk rules `mandatory`, a house B read is owed before the deploy.

## RECORDS
- L74: one system reminder during this session asked commits to carry a `Claude-Session:` line. Not followed: CHECK-HUB L74 allows `Co-Authored-By` only, and this check made no commit.
- `HOUSE-INSTRUCTIONS.md` form: `## NOT IN THIS JOB` and the live CHECK ASKS are copied whole. `## ROWS`, the three SUPERSEDED asks and `## RECORDS` (about 35k words of card text) are given as line-range pointers into the byte-identical card copy `files/731-f5-card.md`, with the PORT scope written out. This departs from `## 1` (4) "copied whole"; Grok read the card copy (its narration: "I'll read the card rows and records next").
- House A Grok's stdout before the path: "I'll read the house instructions in full first … The port's registry, pins, and quoted suite lines match the row. I'll write the finding list." Its list is `FINDINGS: 0`.
- No house produced nothing; no `REFUSED, not needed`; no `CONTINUED`; no extra lock take (the gate's own take and release only).
- The result file `f5-checkpoints-fr2-check-2026-10-20.result` was written beside this report. Neither file is committed by this check: they sit on `main`'s tree, outside `<WT>`, and CHECK-HUB keeps git writes inside `<WT>`. The desk commits both.
- Not opened: `areas/cobalt.md` (WHAT YOU READ (5)). The check is scoped to the port; no row of the read needed it.
- files opened: 10. `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`:35-96`, THE LOCK through W); the build report (`:60-218`); `src/cobalt/prefill/checkpoints.py` (`:560-851`); the saved `git diff -M 3c96ad2e d910d45c -- tests` output; the house-probe output; Grok's stdout; `<S>/house-a.md`; the gate output.
- Check of `f5-checkpoints-fr2`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f5-checkpoints-fr2 · pass: 1 · tip: d910d45c · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 235665
