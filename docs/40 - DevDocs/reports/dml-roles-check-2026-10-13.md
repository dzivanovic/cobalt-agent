# dml-roles-1013 — check report (card 448)

## §0 Headline
Checked card 448 at tip `ce3b9dc1` (build `d0ffa988` plus one check test). Four findings, 2 held, 1 fixed. **Ready: NO** — one held finding (A2) is not fixed, because its fix is a line in the build report, which this check does not write.
O2 (fixed): no test pinned the rollback's revokes. The new O4 does; it was red with the default-privilege revokes cut.
A2 (Grok, held, not fixed): the build report says R1 has 13 `test_db_apply_db.py` ids in pass 2. The module collects 11, and the log shows 11 PASSED. The suite line `with-DB 5609/0` is unaffected.
A1 (Grok, rejected, open): a `CREATE TEMP TABLE` past the allowlist commits under the apply role. TEMP is PUBLIC's database right, outside the rows. O1 (unsettled, open): FIX1's pin runs in pass 1, so it may be red on a fresh cluster.
Gate green: offline 8653/0 · with-DB 5610/0 · live-note 147/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS com.cobalt.radar.

## L74
A system notice in this session asked for a `Claude-Session:` line on commits. It is recorded here once and not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 0 · e30b6b385dda6829df2b54f65982b19f31d6980f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/448-dml-roles-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Sun Oct 18 22:25:08 EDT 2026
status · git status --short --branch · 0 · ## ops/dml-roles-1013
head · git log --oneline -1; git log --stat --format=%h d0ffa988..HEAD · 0 · (6 lines)
    10af5c76 docs(dml-roles-1013): build report — d0ffa988
    10af5c76

     .../reports/dml-roles-build-2026-10-13.md          | 65 ++++++++++++++++++----
     .../reports/dml-roles-build-2026-10-13.result      | 15 +++++
     2 files changed, 68 insertions(+), 12 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/dml-roles-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../dml-roles-build-2026-10-13.md" · 0 · BUILT · job: dml-roles-1013 · tip: d0ffa988 | on e7ef198a | migration: 0025, rolled back | offline 8652/0 | with-DB 5609/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 8 of 8 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 318534
range · git log --oneline e7ef198a..d0ffa988 · 0 · (4 lines)
    d0ffa988 fix(dml-roles-1013): cobalt_app is a member of exactly the five roles (FIX1; L1, L70)
    ad8ecbb9 wip(dml-roles-1013): W — test_db_credentials.py:211 red outside the rows
    cb115b1e feat(dml-roles-1013): DML-only apply roles 0025 and db apply SET LOCAL ROLE (M1, A1, W1, C1; L1, L42, L72, L76)
    8babdd5b wip(dml-roles-1013): red — M1 O1-O3, G1a-h, A1 T7/T10-T12, R1, C1 K1-K2
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| range | `git log --stat --format=%h e7ef198a..d0ffa988` | 0 | 4 commits. Path union: `d0ffa988` `tests/cobalt/test_db_credentials.py`; `ad8ecbb9` `docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md`; `cb115b1e` `docs/40 - DevDocs/cobalt/db_apply.md`, `docs/40 - DevDocs/cobalt/db_migrations/__init__.md`, `docs/40 - DevDocs/prompts/CARD.md`, `ops/desk/gate-lists.md`, `src/cobalt/db_apply.py`, `src/cobalt/db_migrations/0025_dml_roles.rollback.sql`, `src/cobalt/db_migrations/0025_dml_roles.sql`, `src/cobalt/db_migrations/__init__.py`, and 17 head-pin test files (`test_archiver_migrations.py`, `test_assumed_store.py`, `test_drc_d2_fix_r1_db.py`, `test_drc_d3_experiments.py`, `test_drc_k1_store.py`, `test_drc_store.py`, `test_f15_p1_records_offline.py`, `test_legs_migration.py`, `test_p4_migrations.py`, `test_radar_handicap_store.py`, `test_radar_migration.py`, `test_radar_price_floor_db.py`, `test_radar_score_migration.py`, `test_seam_drc_s3_registry.py`, `test_stale_score_db.py`, `test_tenancy.py`, `test_voice_store.py`); `8babdd5b` `tests/cobalt/test_db_apply.py`, `tests/cobalt/test_db_apply_db.py`, `tests/cobalt/test_dml_roles_db.py`, `tests/cobalt/test_dml_roles_offline.py`, `tests/ops/test_card_md_migration_checklist.py` |
| scratch | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/dml-roles-1013-check` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, no `HOUSE A:` header line | — | house A: Grok · house B: none (not needed) — the card says `HOUSE B: as needed` |
| self-check | build report last line | — | `self-check: 3 of 3` |

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, last line `STAGED 37 files · 564295 bytes · commits 3`. `commits 3` is the commit count of the range outside `docs` (`git log --oneline e7ef198a..d0ffa988 -- . ":(exclude)docs"` → `d0ffa988`, `cb115b1e`, `8babdd5b`). PREFLIGHT's fourth commit, `ad8ecbb9`, is docs-only (the build report), and the house gets that report under `files/`. Per-file lines (bytes, dest under `<S>`):
`22 STAGED-CARD` · `64688 diff.md` · `33548 files/448-dml-roles-card.md` · `29465 files/dml-roles-build-2026-10-13.md` · `3064 files/wt/docs/40 - DevDocs/cobalt/db_apply.md` · `19845 files/wt/docs/40 - DevDocs/cobalt/db_migrations/__init__.md` · `21423 files/wt/docs/40 - DevDocs/prompts/CARD.md` · `23661 files/wt/docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md` · `7578 files/wt/ops/desk/gate-lists.md` · `13536 files/wt/src/cobalt/db_apply.py` · `1899 files/wt/src/cobalt/db_migrations/0025_dml_roles.rollback.sql` · `4257 files/wt/src/cobalt/db_migrations/0025_dml_roles.sql` · `12170 files/wt/src/cobalt/db_migrations/__init__.py` · `28040 …/test_archiver_migrations.py` · `15167 …/test_assumed_store.py` · `24131 …/test_db_apply.py` · `7385 …/test_db_apply_db.py` · `11123 …/test_db_credentials.py` · `6830 …/test_dml_roles_db.py` · `1633 …/test_dml_roles_offline.py` · `28905 …/test_drc_d2_fix_r1_db.py` · `4783 …/test_drc_d3_experiments.py` · `28988 …/test_drc_k1_store.py` · `25673 …/test_drc_store.py` · `6920 …/test_f15_p1_records_offline.py` · `4414 …/test_legs_migration.py` · `28693 …/test_p4_migrations.py` · `11473 …/test_radar_handicap_store.py` · `5132 …/test_radar_migration.py` · `6867 …/test_radar_price_floor_db.py` · `23974 …/test_radar_score_migration.py` · `1952 …/test_seam_drc_s3_registry.py` · `11663 …/test_stale_score_db.py` · `31256 …/test_tenancy.py` · `12799 …/test_voice_store.py` · `982 files/wt/tests/ops/test_card_md_migration_checklist.py` · `356 rulings.md`.
`stage-copy.sh`, each `COPIED`: `6423 files/draft-dml-roles-2026-10-13.md` · `2152 files/draft-448-amend-2026-10-13.md` · `45979 files/cto-2026-10-12.md` · `66463 files/cto-2026-10-13.md` · `30236 files/db-apply-prod-check-2026-10-12.md` · `50354 files/db-apply-prod-build-2026-10-12.md` · `40740 files/deploy-s4-p2-1009.md` · `25326 files/73-s4-p2-card.md` · `14043 files/wt/src/cobalt/db.py` · `9013 files/wt/src/cobalt/db_migrations/0001_schemas.sql` · `1795 files/wt/src/cobalt/db_migrations/0024_strike_alerts.sql` · `345 files/wt/src/cobalt/db_migrations/0024_strike_alerts.rollback.sql` · `8069 files/wt/ops/cobalt_app_role_provision.py` · `1820 files/wt/tests/cobalt/migration_retry.py` · `29228 files/wt/ops/desk/gate.sh` · `12118 files/wt/src/cobalt/jobs/restarts.py`.
`HOUSE-INSTRUCTIONS.md` (Write): the HOUSE TEXT, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the `Files:` paragraph.
House A Grok started 22:28 EDT (`date` 22:28:31), background task `bp92mcqn7`; house B none (not needed). `cd` back, `git status --short --branch` → `## ops/dml-roles-1013`.

## OWN FINDINGS
Written before any house list was opened. Read: the card, the diff `e7ef198a..d0ffa988` (src, ops, CARD.md, the new and changed tests, the 17 head-pin files), `src/cobalt/db_apply.py:225-320` at the tip, `0001_schemas.sql` whole, and the build report.

FINDING O1
ROW: FIX1 (and W1)
CLAIM: FIX1's exact-five pin (`tests/cobalt/test_db_credentials.py:202-214`) runs in PASS 1 at level `0013`, because `ops/desk/gate-lists.md` does not name the file. At `0013` the two apply memberships exist only if 0025 has run on this cluster once before, so on a fresh cluster (a new docker volume) pass 1 reads three memberships and the pin is red before any forward.
RUN: COMMAND `grep -c -F "test_db_credentials.py" ops/desk/gate-lists.md`
EXPECT: `0`, so the file is neither deselected in PASS 1 nor named in PASS 2.

FINDING O2
ROW: M1 (rollback)
CLAIM: The rollback revokes the default privileges (`src/cobalt/db_migrations/0025_dml_roles.rollback.sql:13`, `:16`, `:19`, `:22`), the sequence USAGE (`:25`, `:29`) and the schema USAGE (`:26`, `:30`). No test pins these revokes. O3 (`tests/cobalt/test_dml_roles_offline.py:39-43`) checks only that `REVOKE` appears and that `DROP`, `REVOKE cobalt_apply_` and `CREATE ROLE` do not. G1g (`tests/cobalt/test_dml_roles_db.py:142-153`) checks only `UPDATE` on `"user".traders`. The gate's F2 = F0 counts columns, relations and views only. So the rollback can lose its four `ALTER DEFAULT PRIVILEGES … REVOKE` lines, or its sequence or schema revokes, with every test still green.
RUN: TEST, in `tests/cobalt/test_dml_roles_offline.py`:
```python
def test_o4_the_rollback_revokes_every_grant_the_forward_makes():
    code = _code(ROLLBACK)
    for schema, role in (('"user"', "cobalt_apply_user"), ("system", "cobalt_apply_system")):
        for want in (
            f"REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA {schema} FROM {role}",
            f"REVOKE USAGE ON ALL SEQUENCES IN SCHEMA {schema} FROM {role}",
            f"REVOKE USAGE ON SCHEMA {schema} FROM {role}",
            f"REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM {role}",
            f"REVOKE USAGE ON SEQUENCES FROM {role}",
        ):
            assert want in code, want
```
With the four `ALTER DEFAULT PRIVILEGES … REVOKE` statements cut from the rollback (a mutation, undone afterwards), the file's tests O1-O3 run.
EXPECT: under the mutation, O1-O3 stay `3 passed` and O4 fails with `AssertionError: REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM cobalt_apply_user`. At the tip, O4 passes.

Read and found right (no finding): A1's order and the `current_user` check (`db_apply.py:248-264`; T7 ×2, T10, T12); `Side(side)` normalises a `str` side before `APPLY_ROLES[side]` (`:243`); the `__all__` line, the `#:` line and the A4 docstring; the forward's grants and the four default-privilege statements, which are DML and USAGE only, own schema, no `OWNER`, `CREATE`, `TRUNCATE` or other side, and no line starts `CREATE TABLE`; the registry and its docstring lines; all 17 head-pin files (each hunk is an index move or an added `0025` line with its `# DML roles (0025)` comment, and nothing else); FIX1's two hunks (the name and docstring, and the full five-name list, no subset form); gate-lists PASS 1 and PASS 2 ends; the CARD.md section after the prodwrite section.

## Findings
House A Grok finished at 22:43 EDT (`date` 22:43:48; task exit 0, stdout `…/dml-roles-1013-check/house-a.md`). `ls -la <S>` → `house-a.md` 1257 bytes, last line `FINDINGS: 2`. House B: none (not needed). Drop check: `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: TEST — tests/cobalt/test_db_apply_db.py`, `15:RUN: COMMAND`. Each block carries a `def test_` or one `uv run pytest` line, so both are kept.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| O1 | Opus | FIX1 / W1 | FIX1's five-membership pin runs in PASS 1 at 0013 (gate-lists does not name the file), so it holds only on a cluster where 0025 already ran | COMMAND |
| O2 | Opus | M1 | No test pins the rollback's default-privilege, sequence or schema revokes; cutting them leaves every test green | TEST (+ mutation) |
| A1 | Grok | X2 | PUBLIC's database `TEMP` right survives `SET LOCAL ROLE`, so a `CREATE TEMP TABLE` past the allowlist commits under `cobalt_apply_user` | TEST |
| A2 | Grok | G1 | The build report says R1 has 13 `test_db_apply_db.py` ids in pass 2; the module collects 11 | COMMAND |

## Dropped
none (both house blocks carry a runnable RUN).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -c -F "test_db_credentials.py" ops/desk/gate-lists.md` | `0` | UNSETTLED — the output shows the file runs in PASS 1, but the red the claim predicts needs a cluster on which 0025 never ran. No listed command builds one, and on this server the memberships persist (the build's RECORDS). OPEN |
| O2 | Opus | O4 added to `tests/cobalt/test_dml_roles_offline.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dml_roles_offline.py` at the tip → `4 passed in 0.03s`; mutation (the four `ALTER DEFAULT PRIVILEGES … REVOKE` statements cut from the rollback with Edit) → `1 failed, 3 passed in 0.05s`, first failing line `AssertionError: REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM cobalt_apply_user` (`tests/cobalt/test_dml_roles_offline.py:56`); mutation undone with Edit, `git diff --stat` → only the test file | under the mutation O1-O3 stay green and O4 is red | HELD (no test pinned the revokes; the fix is the pin itself) |
| A1 | Grok | the test pasted at the end of `tests/cobalt/test_db_apply_db.py`, run with-DB in ONE lock take at `0013`, no forward (the apply roles and `cobalt_app`'s memberships exist cluster-wide since the build's gate, and `TEMP` is PUBLIC's database right, so `0013` meets the claim): `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=short tests/cobalt/test_db_apply_db.py::test_x2_create_temp_commits_under_the_apply_role` | `1 failed in 0.12s` · `AssertionError: assert 0 == 1` · captured `STATEMENT 1/1: CREATE TEMP TABLE zz_db_apply_temp (a int)` · `ROWS 1: -1` · `COMMITTED · statements: 1 · rows: 0` | REJECTED — `## NOT IN THIS JOB`: "A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here." The `TEMP` right is PUBLIC's on the database, granted by no row; M1 (3)'s NEVER list covers the grants 0025 makes. The test was removed again with Edit (a committed red would turn W's pass 2 red, since `gate.sh:13` appends a deselected id to pass 2). OPEN, `## DECISIONS` 1 |
| A2 | Grok | `uv run pytest -q -p no:cacheprovider --collect-only tests/cobalt/test_db_apply_db.py` | `11 tests collected in 0.03s` (t5, t6, `test_command_end_to_end…` [a] [b] [c], t9, the DDL test [drop] [alter] [truncate] [create], the allowed update). Cross-read: `grep -c -F "PASSED tests/cobalt/test_db_apply_db.py" <run 3 log>` → `11`; `grep -c -F "PASSED tests/cobalt/test_dml_roles_db.py" <run 3 log>` → `15` | HELD, NOT FIXED — `docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md` (its `:136` says "R1's 13 `test_db_apply_db.py` ids"; the module and the log show 11, all PASSED; the `with-DB 5609/0` line is not affected) |

## FIXES
- O2: `ce3b9dc1 wip(dml-roles-1013): check red — O2 (O4 pins the rollback's revokes; red with the default-privilege revokes cut)` (the test; its red is the mutation run in `## RUNS`), then `88d5a98d fix(dml-roles-1013): the rollback's revokes are pinned, DevDocs line (check O2)` (`docs/40 - DevDocs/cobalt/db_migrations/__init__.md`, one line under `## 2026-10-18 — dml-roles-1013`). No `src/` change: the rollback was right, and the gap was the missing pin. After: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dml_roles_offline.py tests/cobalt/test_db_apply.py tests/cobalt/test_db_apply_db.py` → `118 passed, 11 skipped in 0.48s` (`0 failed`; the 11 skips are `test_db_apply_db.py`'s with-DB tests, no `.env`).
- A2: HELD, NOT FIXED — `docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md` (the build report, not a file this check writes).

## Suites
RESTARTS first: `uv run cobalt jobs restarts e7ef198a..HEAD`. Its rows: `src/cobalt/db_apply.py` and `src/cobalt/db_migrations/__init__.py` `static import reach` `com.cobalt.radar`; the two `.sql` files `non-Python src asset`; `ops/desk/gate-lists.md` `operator script; no Cobalt reader`; every `tests/…` (`test_db_credentials.py` among them) `test/documentation; no resident`; every `docs/…` `DOCS`. No UNCLASSIFIED row. Last line `RESTARTS: com.cobalt.radar`.
The gate, one call on HEAD `88d5a98d` (code tip `ce3b9dc1`): `sh /Users/cobalt/cobalt/ops/desk/gate.sh dml-roles-1013 all --deploy --deploy-gate --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --migration` → exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8653/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5610/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/dml-roles-1013-all-20261018-224801.log
```
- offline 8653 = the build's 8652 plus O4. None of the skips is marked `OUTSIDE the allowed set`.
- pass 1 executed command: log `:1079` (`pass 1: whole (deploy)`). Pass 2 PASSED lines: `test_db_apply_db.py` ×11 (`:2142-2152`) and `test_dml_roles_db.py` ×15 (`:2153-2167`).
- `cobalt_dev: 0013 — F2 = F0`. `.env: removed`; `ls /Users/cobalt/cobalt-wt/dml-roles-1013/.env` → `No such file or directory`.
- Check's own lock take (A1): 22:45-22:47 EDT. `lock taken: dml-roles-1013`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's; `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` before and after; proof-only `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` (level 0013, no forward); `lock released`; `.env: removed, proven gone (4, A1)`.

## Scope
PREFLIGHT's path union (`## PREFLIGHT`, the range row): every non-docs path is a row's file. `0025_dml_roles.sql`, `0025_dml_roles.rollback.sql`, `__init__.py`, `test_dml_roles_offline.py` and the 17 head-pin files belong to M1; `test_dml_roles_db.py` to G1; `db_apply.py` and `test_db_apply.py` to A1; `test_db_apply_db.py` to R1; `gate-lists.md` to W1; `CARD.md` and `test_card_md_migration_checklist.py` to C1; `test_db_credentials.py` to FIX1. The check's commits: `tests/cobalt/test_dml_roles_offline.py` (M1's file, the O2 pin) and `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (the DevDocs line).

## Checked against the branch
- (i) `git log --oneline d0ffa988..HEAD -- . ":(exclude)docs"` → `ce3b9dc1 wip(dml-roles-1013): check red — O2 (…)`. `<tip now>` = `ce3b9dc1`.
- (ii) `git log --stat --format=%h d0ffa988..HEAD` → `88d5a98d` `docs/40 - DevDocs/cobalt/db_migrations/__init__.md`; `ce3b9dc1` `tests/cobalt/test_dml_roles_offline.py`; `10af5c76` the build report and its `.result` (docs). No other path: nothing WIDENED.
- (iii) `git log --oneline e7ef198a..HEAD -- src/cobalt/db.py ops/cobalt_app_role_provision.py ops/desk/desk-launch.sh ops/desk/authorize.sh src/cobalt/db_migrations/placement.py .claude/settings.json` → empty.
- (iv) `grep -n -F "def test_o4_the_rollback_revokes_every_grant_the_forward_makes" tests/cobalt/test_dml_roles_offline.py` → `46:def test_o4_…` (one line). Its `wip` commit `ce3b9dc1` sits below its `fix` commit `88d5a98d`.
- (vi) `git log --stat --format=%h e7ef198a..HEAD -- src/cobalt/db_migrations tests/cobalt` → new migration `0025_dml_roles.sql` / `.rollback.sql`; new with-DB file `tests/cobalt/test_dml_roles_db.py`; `test_db_apply_db.py` now needs `0025`. `git diff e7ef198a..HEAD -- ops/desk/gate-lists.md` → PASS 1 ends `--deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py`, and PASS 2 ends `tests/cobalt/test_db_apply_db.py tests/cobalt/test_dml_roles_db.py`. Row W1 names `ops/desk/gate-lists.md` in its `files`. GATE LISTS carried.
- (vii) card `## RECORDS` commands: `git -C /Users/cobalt/cobalt diff --stat ffd5e7a8 692ff5ae -- src tests ops configs "…/CARD.md" "…/BUILD-HUB.md"` → empty (as recorded). `grep -rn -F "D1 follow-up migration card" "…/reports"` → `db-apply-prod-check-2026-10-12.md:251`, `cto-2026-10-13.md:191` (the OWED line), and `draft-dml-roles-2026-10-13.md:20` (the drafter's own note, written after the record). `grep -rln -F "DML-only" "…/reports"` → the two cto files, the 417 check report, and files written after the record (the two drafts, the two preflights, this report). `ls -l /Users/cobalt/.claude/ops/desk-launch.sh` → `… -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh`. `git -C /Users/cobalt/cobalt-wt/f4-refresh-1010 diff --stat main...HEAD -- src/cobalt/db_migrations src/cobalt/db_apply.py ops/desk/gate-lists.md tests/cobalt/test_db_apply.py tests/cobalt/test_db_apply_db.py "…/CARD.md"` → empty (as recorded).
- (viii) L32: this report holds no ticker, price or date of his; the figures are file lines, counts and fingerprints.

## OPEN
- A2 · HELD, NOT FIXED — `docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md:136`. Settled by the fix round correcting "13" to "11", or by a desk ruling that carries it (no test path exists to close it).
- A1 · REJECTED (the fence's last line). Settled by a card that decides whether the apply roles should lose PUBLIC's database `TEMP` (e.g. `REVOKE TEMPORARY ON DATABASE … FROM PUBLIC`, which changes every role's right), or by a ruling that a temp table inside the apply transaction is acceptable (it dies with the session, which `apply_statements` closes, `db_apply.py:287-288`).
- O1 · UNSETTLED. Settled by a run on a cluster where 0025 never ran (FIX1's pin is then red in pass 1), or by moving `test_db_credentials.py::TestTheLiveFactoryAuthenticatesAsCobaltApp::test_it_is_a_member_of_exactly_the_five_roles` to PASS 2 in `gate-lists.md` (W1's file).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. A2 — HELD, NOT FIXED: the build report's pass-2 figure "R1's 13 `test_db_apply_db.py` ids" (`dml-roles-build-2026-10-13.md:136`) is 11 (collect-only `11 tests collected`; run-3 log `grep -c -F "PASSED tests/cobalt/test_db_apply_db.py"` → `11`). Every id PASSED and `with-DB 5609/0` stands; the error is in the prose only. The fix is the builder's report, a file this check does not write, so `held unfixed: 1` and `ready: NO`. Default taken: nothing changed. For the fix round or a judgment seat: correct the figure, or carry it (the deploy gate needs `FIXED:` or `CARRIED:` for A2).
2. A1 — REJECTED, open, follow-up: `CREATE TEMP TABLE zz_db_apply_temp (a int)`, passed to `apply_statements` past `check_file`, commits under `cobalt_apply_user` (`COMMITTED · statements: 1 · rows: 0`, at `0013` on `cobalt_dev`). The cause is PUBLIC's database `TEMP` right, not a grant of 0025, and the fence's last line says "never fixed here". The allowlist (A1 of card 417) still refuses the statement in a real `db apply`. Default taken: not fixed, and the test was removed from the tree (it is quoted whole in `## Findings` / house A's list).
FOR DEJAN: none.

## RECORDS
- L74: one system notice asked for a `Claude-Session:` commit line; not followed (`## L74`).
- House A Grok: `FINDINGS: 2`, both kept. House B: none (not needed; `HOUSE B: as needed`). No house failed.
- Dropped: none. REFUSED, not needed: none. CONTINUED: none.
- Extra lock take: one (step 4, A1's with-DB run, 22:45-22:47 EDT), besides the gate's own.
- Mutation for O2 done with Edit on `src/cobalt/db_migrations/0025_dml_roles.rollback.sql` and undone with Edit; `git diff --stat` afterwards showed only the test file.
- A1's test was added to `tests/cobalt/test_db_apply_db.py`, run, and removed with Edit before any commit; that file is unchanged by the check.
- Staging count: `stage-set.sh` printed `commits 3` against PREFLIGHT's 4. The fourth, `ad8ecbb9`, touches only `docs/` (the build report), which `diff.md` excludes by its `":(exclude)docs"` pathspec; `git log --oneline e7ef198a..d0ffa988 -- . ":(exclude)docs"` → 3 commits.
- Outside this branch: `cobalt_app`'s two apply memberships persist on the cluster (as the card's RECORDS say), so any other branch's gate that still carries the three-role pin (`test_db_credentials.py`, main's text) meets a red in pass 1 until `d0ffa988` reaches main. This is the build's own RECORDS line, confirmed by this check's reading; it is not this branch's defect.
- The report and its `.result` sit on `main`'s tree uncommitted. The desk commits them (this session has no `git -C … commit` string).
- CHECK ASKS: X1 — no statement runs before `SET LOCAL ROLE`, and none runs after a refused `SET` (T12) or on the side role (T10); the order is the two timeouts, the `SET LOCAL ROLE`, then the version and user reads (`db_apply.py:248-252`; T7 ×2). X2 — the forward grants DML and USAGE only (O2 of the build, G1b/c/d/h green in pass 2); `TEMP` via PUBLIC is A1. X3 — the rollback touches no role or membership (O3, G1g); `cobalt_dev: 0013 — F2 = F0` and `forward, back, forward, back — F = F0 twice`; grants and default ACLs are per database. X4 — R1's red at E2 is `0 == 1` with `COMMITTED` (build report), and pass 2 PASSED ×4 (`:2148-2151`). X5 — no new line prints a DSN, password or environment value; `tests/cobalt/test_db_apply.py` is green (in the 118-passed run). X6 — the 17 files carry index moves and `0025` lines only. X7 — `test_db_credentials.py:213-214` is the exact five-name list.
- files opened: 16 — CHECK-HUB.md, the card, the build report, the saved diff output, the probe output, `src/cobalt/db_apply.py`, `0001_schemas.sql`, BUILD-HUB.md (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`), `tests/cobalt/test_dml_roles_offline.py`, `0025_dml_roles.rollback.sql`, `tests/cobalt/test_db_apply_db.py`, the lock-take output, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), Grok's stdout, `house-a.md`, the gate output.
- Check of `dml-roles-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: dml-roles-1013 · pass: 1 · tip: ce3b9dc1 · house A: Grok FINDINGS: 2 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · house B: none available · suites: offline 8653/0 · with-DB 5610/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 255901
