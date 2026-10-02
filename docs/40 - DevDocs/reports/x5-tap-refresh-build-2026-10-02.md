# x5-tap-refresh — build report (2026-10-02)

## §0 Headline
Built 09:36 EDT on `53a85f27`, tip `2a5fa102` (card `prompts/2026-10-02/22-x5-tap-refresh-card.md`, started 08:11). `refresh_radar_card` now reads the newest tap id in its own statement after the row lock. A tap that commits while the refresh waits keeps its conviction and key.
X5 was red on BASE (B returned `True` and the stage's numbers overwrote the tap). It is green on the fix and red again when the subquery goes back into the locking SELECT. X5n (the negative control) is green on BASE and on the fix, and red under `taps_moved = True`.
T1: both hubs' pass-1 and pass-2 lines carry the new file (4 lines). Suites: offline 3783/0 · with-DB 4382 + 173 = 4555/0 · live-note 146/0. `cobalt_dev` is back at `0013` (F2 = F0).
One stop (E2, 08:25, the lock was held by `ops-glob-1002`), continued by the desk at 09:03. Decisions: 0.

## L74
- A system block in this session asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/22-x5-tap-refresh-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/22-x5-tap-refresh-card.md"` | 0 | `c858b0c86ad676e192c566c5e7650ee44e4ae69a` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R52 | `grep -n "^| R52 " ".../reports/cto-2026-10-02.md"` | 0 | `59:\| R52 \| 08:00 ET \| HIS RULING (FOR DEJAN 11 = A): X5 gets a fix card now … \| HIS RULING · APPROVED \|` |
| R52 committed | `git -C … log -1 --format=%H -S"\| R52 \|" -- ".../cto-2026-10-02.md"` | 0 | `e9a94c19ccf236eb26752e3bc64da90e8db9a243` |
| R41 | `grep -n "^| R41 " ".../reports/cto-2026-10-02.md"` | 0 | `48:\| R41 \| 07:57 ET \| HIS RULING (direction row 4): under an order the judge seat … answers a held finding or fence question inside the feature … \| HIS RULING · APPROVED \|` |
| R41 committed | `git -C … log -1 --format=%H -S"\| R41 \|" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 08:11:17 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/x5-tap-refresh-1002` + `?? "docs/40 - DevDocs/reports/x5-tap-refresh-build-2026-10-02.md"` (this report, created by the hub's FIRST Write before PREFLIGHT; nothing else) |
| base | `git log --oneline -1` | 0 | `53a85f27 docs(desk): 10-02 prompt 04 renamed (launcher refuses -card.md prompts)` |
| branch from main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 s3/x5-tap-refresh-1002` | 0 | `53a85f27 …` (same) |
| diff vs base | `git diff --stat 53a85f27` | 0 | (nothing) |
| base commit | `git show --stat 53a85f27` | 0 | `.../prompts/2026-10-02/{04-draft-x5-fix-card.md => 04-draft-x5-fix.md} \| 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` | 1 | `No such file or directory` |
| no lock anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| caller | `grep -rn -F "refresh_radar_card(" src` | 0 | `src/cobalt/cards/store.py:1177: def refresh_radar_card(…)` · `src/cobalt/radar/evaluate.py:1933: self.card_store.refresh_radar_card(update, run_id=run_id, now=instant,` |
| tap writer | `grep -rn -F "INSERT INTO card_dot_taps" src` | 0 | `src/cobalt/cards/store.py:1440` |
| subquery | `grep -n -F "coalesce(max(id), 0) FROM card_dot_taps" src/cobalt/cards/store.py` | 0 | `1203: "SELECT state, (SELECT coalesce(max(id), 0) FROM card_dot_taps WHERE card_id = %s), "` |
| taps_moved | `grep -n -F "taps_moved = " src/cobalt/cards/store.py` | 0 | `1217: taps_moved = int(locked[1]) != update.tap_version` |
| write_record imports | `grep -n -F "from .predictions import write_record" src/cobalt/cards/store.py` | 0 | `1116`, `1194`, `1408` |
| `_write_tx` | `grep -n -F "def _write_tx" …store.py` | 0 | `970` |
| `tap_dot` | `grep -n -F "def tap_dot" …store.py` | 0 | `1388` |
| `write_record` | `grep -n -F "def write_record" src/cobalt/cards/predictions.py` | 0 | `177` |
| `card_score` | `grep -n -F "def card_score" src/cobalt/cards/scoring.py` | 0 | `287: def card_score(conv, prox, suppressed) -> int \| None:` |
| store page | `grep -n -F "## 2026-09-30 — f15-p1" ".../cobalt/cards/store.md"` | 0 | `155` |
| sizes | `wc -l` store.py / store.md / BUILD-HUB.md / DEPLOY-HUB.md | 0 | `1528` / `156` / `111` / `184` |
| READ tail | `tail -n 3 .../f15-p1-decisions-2026-09-30.md` | 0 | last line `F15 P1 DECISIONS ANSWERED · answered: 13 of 13 · for Dejan: 0` |
| READ tail | `tail -n 3 .../f15-p1-build-2026-09-30.md` | 0 | last line `BUILT · job: f15-p1 · tip: 28d9364f \| on 97720c92 \| migration: 0022, rolled back \| … \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 8 of 8 \| self-check: 3 of 3 \| decisions: 13 · for Dejan: 1` |
| READ lines | Read `f15-p1-decisions` :18, `f15-p1-build` :352 | — | DECISION 4 and DECISION X5 as the card quotes them (tap 0.7 / 35 / B; final row None/None/None) |
| restarts | `uv run cobalt jobs restarts 53a85f27..HEAD` | 0 | `docs/40 - DevDocs/reports/x5-tap-refresh-build-2026-10-02.md A DOCS -` · `RESTARTS: none` (empty commit range; the tool counts this untracked report) |
| lock (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| lock (b) | `cp /Users/cobalt/cobalt/.env …/x5-tap-refresh-1002/.env` then `ls -la …/*/.env` | 0 | one line: `-rw------- 1 cobalt staff 2186 Oct 2 08:12 /Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` |
| `<FP>` | (the fingerprint string, below) | 0 | `<Fp>` = cols `664` · rels `35` · views_md5 `272c95bbb12241e3611e4b36326ccf87` |
| level | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | 36 tables probed; `legs`, `drc_*`, `prediction_records`, `voice_turns` absent (`-`): level `0013`; no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 53a85f27 (DIRTY: 1 path(s))` (this report) |
| lock (d) | `rm …/.env` then `ls …/.env` | 0 / 1 | `No such file or directory` — `.env: removed, proven gone (PREFLIGHT)` 08:12 EDT |

`<FP>` as typed:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

The card's `## RECORDS`, copied and re-read:
- main tip `53a85f27` (drafter, 08:03) → re-read `git -C /Users/cobalt/cobalt log -1 --format=%h main` → `9be57c62` now (desk commits after the card; the card itself is `c858b0c8`). The branch base is `53a85f27` as the card says.
- X5 experiment on main → re-read: `7e2fff95 wip(f15-p1): red — … X5, X9, X12, X13`. Same.
- subquery at `store.py:1203`, `taps_moved` at `:1217` → re-read, same.
- isolation: `grep -n -i -F` of `isolation`, `serializable`, `repeatable` over `store.py` and `db.py` → nothing each; `_write_tx` `:970-985` sets `autocommit = False` only (Read). READ COMMITTED holds.
- `write_record` imported at call time `:1116`, `:1194`, `:1408` → re-read, same.
- RESTARTS class homes → the build's own table answers (RESTARTS).
- THE RED'S LEVEL / R41 answer → followed at E2 and E3 (top-level lock takes, each a `## RECORDS` line).

## E0 BASELINE
- Offline, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0): `3783 passed, 673 skipped, 1 xfailed, 25 warnings in 610.70s (0:10:10)` — 0 failed, 0 errors (`.env` absent: the with-DB tests skip offline).
- Live-note, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`: `146 passed, 1 skipped, 15 warnings in 27.47s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
- Written: `tests/cobalt/test_x5_tap_refresh_db.py` — `test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers` (X5) and `test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers` (X5n, the negative control). No `src/` edit.
- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_x5_tap_refresh_db.py` → `2 skipped in 0.02s` (`:277`, `:319`: `Postgres env settings not available`).
- With-DB (top level, R41 shape): lock (a) at 08:25 EDT, `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw------- 1 cobalt staff 2186 Oct 2 08:25 /Users/cobalt/cobalt-wt/ops-glob-1002/.env`. THE LOCK IS HELD by `ops-glob-1002`; nothing taken, nothing run on `cobalt_dev`. Stopped here under UNATTENDED RULES (b).
- CONTINUED 09:03 EDT. E2 with-DB take (R41, the top level): lock (a) `no matches found`; (b) one line, this worktree's (09:03); `<F0>` = cols `664` · rels `35` · views_md5 `272c95bbb12241e3611e4b36326ccf87`; `--proof-only` → `0013` (no 0014+ table), `NOTHING WAS APPLIED`; `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001`…`0013`, `0014`…`0022` applied, `content UNCHANGED on every table` — **dev forward: APPLIED 09:04 EDT**.
- Run 1, `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_x5_tap_refresh_db.py` → `2 failed in 10.48s`:
  - X5: `:305: AssertionError: the refresh did not see the tap that committed while it waited` / `assert True is False` — the row's reason.
  - X5n: `:341: AssertionError: B never waited` / `{'b_waited': False, 'b_wrote_all': True}` — NOT the row's reason: the factory's connection autocommits, so the holder's `FOR UPDATE` lock ended with its SELECT. **Rewritten** (the holder takes `autocommit = False` before the SELECT).
- Run 2 (same command, same take) → `1 failed, 1 passed in 0.29s`:
  - `FAILED …::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers` — `:305: AssertionError: the refresh did not see the tap that committed while it waited` / `assert True is False`. RED on BASE for the row's reason: B waited (the `B never waited` assert above it passed) and returned `True`.
  - `PASSED …::test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers` — the negative control is green on BASE.
- (c3r): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('ZZX5R') GROUP BY ticker"` → header only, no rows.
- `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` reversed, newest first, `content UNCHANGED on every table`. `<F2>` = 664 / 35 / `272c95bbb12241e3611e4b36326ccf87` = `<F0>` → **cobalt_dev: 0013 — F2 = F0**. Lock (d): `rm`, `ls` → `No such file or directory`; `.env: removed, proven gone (E2)` 09:05 EDT.

## E3 THE ROWS
**X5** — `src/cobalt/cards/store.py`, `refresh_radar_card`'s `work` (re-read `:1201-1217` before the edit: unchanged from PREFLIGHT). The subquery is gone from the locking SELECT, which now reads `state, conviction, score_suppressed, proposed_key … FOR UPDATE` with `(update.card_id,)`. `SELECT coalesce(max(id), 0) FROM card_dot_taps WHERE card_id = %s` is its own statement on the same `conn`, right after the `locked is None` refusal. `taps_moved = int(tap_version) != update.tap_version`. The `locked[...]` reads in the taps-moved arm shift by one (`[2]→[1]`, `[3]→[2]`, `[4]→[3]`), as the card's row says. Nothing else moved: the run-row read, both UPDATE statements, the dot upsert, the record call and the return value are byte-identical (`git diff -- src/cobalt/cards/store.py`, quoted under `## FOR THE CHECK`).
- DevDocs: `docs/40 - DevDocs/cobalt/cards/store.md` gains `## 2026-10-02 — x5-tap-refresh` (one dated entry).

**T1** — `docs/40 - DevDocs/prompts/BUILD-HUB.md` `## W` (c) and (c3) and `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (c) `:105` and (c3) `:109`. Pass 1 ends with ` --deselect tests/cobalt/test_x5_tap_refresh_db.py`. Pass 2 adds `tests/cobalt/test_x5_tap_refresh_db.py` inside its `-rA` span, right after `tests/cobalt/test_f15_p1_records_db.py`. The (a0) list, the allowed-skip set and the level `0013` are untouched. W's executed commands are these lines byte for byte; the diff is quoted under `## FOR THE CHECK`.

E3 with-DB lock take (R41, top level, take 2), `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_x5_tap_refresh_db.py` each time:
- GREEN on the fix → `PASSED …::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers` · `PASSED …::test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers` · `2 passed in 0.33s`.
- MUTATION 1 (the subquery put back into the locking SELECT, `tap_version = locked[4]`; Edit tool) → `1 failed, 1 passed in 0.40s`; `FAILED …::test_x5_…` — first failing line `:305: AssertionError: the refresh did not see the tap that committed while it waited` / `assert True is False`; X5n PASSED. Undone with Edit; `git diff --stat` → the tree back at the fix (`src/cobalt/cards/store.py | 23 +++++++++++++---------`, as before the mutation).
- MUTATION 2 (`taps_moved = True`; Edit tool) → `1 failed, 1 passed in 0.45s`; `FAILED …::test_x5n_…` — first failing line `:345: assert False is True` (`out["b_wrote_all"] is True`); X5 PASSED. Undone with Edit; `git diff --stat` → the same tree as after mutation 1's undo.
- GREEN again → `2 passed in 0.40s`.
- (c3r) for `'ZZX5R'` → no rows. Rollback `--down-to 0013` (foreground) → `0022`…`0014` reversed, `content UNCHANGED on every table`; `<F2>` = 664 / 35 / `272c95bbb12241e3611e4b36326ccf87` = `<F0>` → **cobalt_dev: 0013 — F2 = F0**. Lock (d): `rm`, `ls` → `No such file or directory`; `.env: removed, proven gone (E3)` 09:07 EDT.
- The neighbour file `tests/cobalt/test_f15_p1_records_db.py` (x6a, bar_ts) runs in W pass 2. R41 sets the E3 runs to this one file.

## RESTARTS
`uv run cobalt jobs restarts 53a85f27..HEAD` (HEAD `2a5fa102`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cards/store.md	M	DOCS	-
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/x5-tap-refresh-build-2026-10-02.md	M	DOCS	-
src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_x5_tap_refresh_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row; no `configs/cobalt/jobs.yaml` entry owed (the card's record said the same).

## W THE THREE SUITES
`<tip>` = `2a5fa102`.
- (a) OFFLINE, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3783 passed, 675 skipped, 1 xfailed, 25 warnings in 587.31s (0:09:47)` — 0 failed, 0 errors → `<p>` = 3783. Tests this build adds: `tests/cobalt/test_x5_tap_refresh_db.py::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers`, `::test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers` (offline: `SKIPPED … :277` / `:319: Postgres env settings not available` — the two extra skips over E0's 673).
- (b) lock (a) `no matches found`; (b) one line, this worktree's, 09:18 EDT. `<F0>` = 664 / 35 / `272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → `0013` (no 0014+ table), `NOTHING WAS APPLIED`, `code: 2a5fa102`.
- (c) PASS 1, executed WHOLE (the hub's pass-1 line as T1 left it; this build's one deselect is its last item, `--deselect tests/cobalt/test_x5_tap_refresh_db.py` — both its tests need `0022`):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py`
  Result (background, exit 0): `4382 passed, 7 skipped, 67 deselected, 3 xfailed, 31 warnings in 703.63s (0:11:43)`. 0 failed, 0 errors. Every SKIPPED line:
  `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` → `<d1>` = 4382.
- (c2) FORWARD, `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001`…`0013` re-applied idempotently, then `0014_radar_handicap` … `0022_prediction_records` in order; no `CHANGED`; `content UNCHANGED on every table` (`cobalt_redactions` 225 → 225; it read 224 at the (b) proof — one row added by pass 1). This build adds no migration. **dev forward: APPLIED 09:31 EDT**. `<F1>` = cols `893` · rels `44` · views_md5 `126f2d6983fa59f9d0eaaff7da7dd29c`.
- (e) LIVE-NOTE (`.env` absent, run at 09:08 before this take): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.85s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- (c3) PASS 2, executed WHOLE (the hub's pass-2 line as T1 left it; this build's file sits in the `-rA` span right after `test_f15_p1_records_db.py`):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  Result (background, exit 0): `173 passed, 1 deselected, 5 warnings in 220.88s (0:03:40)` — 0 failed, 0 errors. This build's ids in the `-rA` lines: `:358 PASSED tests/cobalt/test_x5_tap_refresh_db.py::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers` · `:359 PASSED tests/cobalt/test_x5_tap_refresh_db.py::test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers`. The K25 pins: `:350 PASSED …test_f15_p1_records_db.py::test_last_price_bar_ts_is_the_evaluations_bar_start_in_both_arms_and_null_keeps_it` · `:351 PASSED …::test_x6a_a_tap_between_the_stage_read_and_the_refresh_records_the_locked_triple`. (`grep -c -F "FAILED"` on the output gives 11. All of them are captured page / log text, such as `radar panel FAILED: … pool 'primary' is missing` and the U3 banner HTML, not test outcomes.) → `<d2>` = 173; `<d>` = 4382 + 173 = 4555.
- (c3r) `ls -la …/x5-tap-refresh-1002/.env` (listed), then `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('ZZX5R') GROUP BY ticker"` → `ticker	count`, no rows.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022_prediction_records.rollback.sql` … `0014_radar_handicap.rollback.sql` reversed newest first, `content UNCHANGED on every table`. `<F2>` = cols `664` · rels `35` · views_md5 `272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**. Lock (d): `rm …/.env`; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` — `.env: removed, proven gone (W)` 09:35 EDT. Lock taken 09:18, released 09:35.
- (c4) not owed: this build adds no migration.
- TREE STATE (T1): the executed (c) and (c3) are the hub lines byte for byte. `git diff 53a85f27 -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → four `-`/`+` line pairs: BUILD-HUB `## W` (c) and (c3) (hunk `@@ -81,11 +81,11 @@`), and DEPLOY-HUB (c) and (c3) (hunk `@@ -102,11 +102,11 @@`). Each pass-1 line gains only ` --deselect tests/cobalt/test_x5_tap_refresh_db.py` at its end. Each pass-2 line gains only `tests/cobalt/test_x5_tap_refresh_db.py ` between `test_f15_p1_records_db.py` and `test_radar_cards_db.py`. No other line in either file changed. The level `0013`, the `--down-to` string, the (a0) list and the allowed-skip set are untouched.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. X5: red on BASE (E2 run 2, `:305: AssertionError: the refresh did not see the tap that committed while it waited` / `assert True is False`), and red under MUTATION 1, the subquery back in the locking SELECT (same line, E3). X5n: green on BASE (E2 run 2, `PASSED`) and red under MUTATION 2, `taps_moved = True` (E3, `:345: assert False is True`). X5n's first E2 run went red for a reason that was not the row's (`B never waited`: the holder connection autocommits). It was rewritten and that is said under E2. — HOLDS.
(2) Every entry path is pinned. The one caller, `src/cobalt/radar/evaluate.py:1933` (`grep -rn -F "refresh_radar_card(" src`, PREFLIGHT and again at the tip), is the stage's path, and X5/X5n drive `refresh_radar_card` directly with the stage's `CardUpdate`. The one tap writer, `tap_dot` (`grep -rn -F "INSERT INTO card_dot_taps" src` → `store.py:1440` at BASE, `:1445` at the tip), is session A in X5. Tap-before-refresh in sequence is `test_x6a_a_tap_between_the_stage_read_and_the_refresh_records_the_locked_triple`, and no tap is `test_last_price_bar_ts_is_the_evaluations_bar_start_in_both_arms_and_null_keeps_it`; both PASSED in pass 2. The NULL-proximity arm (`suppressed = update.score_suppressed`) is pinned by `test_stale_score_db.py`, which also PASSED in pass 2 (one deselect, the r40 test, as in the hub). — HOLDS.
(3) Every `file:line` was re-read at the tip from tool output: `grep -n -F "coalesce(max(id), 0) FROM card_dot_taps" src/cobalt/cards/store.py` → `1213`; `grep -n -F "taps_moved = "` → `1222: taps_moved = int(tap_version) != update.tap_version`; `grep -rn -F "refresh_radar_card("` → `store.py:1177`, `evaluate.py:1933`; `grep -rn -F "INSERT INTO card_dot_taps"` → `store.py:1445`; `git diff -- src/cobalt/cards/store.py` (quoted below); `git diff 53a85f27 --` the two hubs. — HOLDS.

## FOR THE CHECK
- Range `53a85f27..2a5fa102` (`<tip>` = `2a5fa102`, the tree the suites ran on). Commits:
  - `e074e73a wip(x5-tap-refresh): E2 — cobalt_dev lock held by ops-glob-1002`
  - `ed345d56 wip(x5-tap-refresh): red — X5 red on BASE, X5n green (two real sessions, top level)`
  - `2a5fa102 fix(x5-tap-refresh): the refresh reads the tap version after the lock, so a tap that commits while it waits is kept (X5, T1; L1, L3, L45, L76)`
  - then this report's commit.
- The `src/` diff (`git diff -- src/cobalt/cards/store.py`, taken before the fix commit), in short:
  - The locking SELECT drops the subquery and reads `"SELECT state, conviction, score_suppressed, proposed_key "` with `(update.card_id,)`.
  - Three comment lines plus `tap_version = conn.execute("SELECT coalesce(max(id), 0) FROM card_dot_taps WHERE card_id = %s", (update.card_id,)).fetchone()[0]`, right after the `locked is None` refusal.
  - `taps_moved = int(tap_version) != update.tap_version`.
  - In the taps-moved arm, `locked[3]→[2]` (suppressed), `locked[2]→[1]` (conviction, in `card_score` and in `wrote` / `held`) and `locked[4]→[3]` (proposed_key).
  - Nothing else: `23 +++++++++++++---------`.
- Per row:
  - **X5 / X5n**: reds, mutations and greens as quoted under E2, E3 and self-check (1).
  - **T1**: a RUN row; the executed commands and the hub diff are under W.
  - **K25**: self-check above.
- Caller greps: PREFLIGHT rows `caller` and `tap writer`; re-run at the tip (self-check (3)).
- RUN row output: T1 — the (c)/(c3) commands as executed, WHOLE, above; it asserts nothing and showed nothing to decide.
- Suites: offline `3783/0` (`<p>`); with-DB pass 1 `4382/0` + pass 2 `173/0` (`<d>` = 4555); live-note `146/0` (`<l>`).
- Fingerprints by lock take:
  - PREFLIGHT `<Fp>` 664/35/`272c95bb…`.
  - E2: `<F0>` = `<F2>` = 664/35/`272c95bb…`.
  - E3: `<F0>` = `<F2>` = 664/35/`272c95bb…`.
  - W: `<F0>` 664/35/`272c95bbb12241e3611e4b36326ccf87`, `<F1>` 893/44/`126f2d6983fa59f9d0eaaff7da7dd29c`, `<F2>` 664/35/`272c95bbb12241e3611e4b36326ccf87`.
- Lock times: PREFLIGHT 08:12 (taken and released); E2 09:03–09:05; E3 09:06–09:07; W 09:18–09:35.
- RESTARTS table: under `## RESTARTS` (`RESTARTS: com.cobalt.aset com.cobalt.radar`).
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — CLOSE done; the desk verifies and launches the check (`CHECK-HUB.md`).

## DECISIONS
none.

## RECORDS
- Stopped at E2, 08:25 EDT: `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/ops-glob-1002/.env`. `.env` of this worktree: never copied at E2. No migration applied by this build. Wip commit holds the test file and this report (`e074e73a`).
- CONTINUED at E2 09:03 EDT — the desk (`cto-desk`) said the lock is free; verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. (The desk's message named the holder as dev-rebuild; the file I saw at 08:25 was `ops-glob-1002`'s — either way none is left.) Its pointer to the card's R41 record (`c858b0c8`) is the card I read at start; nothing widened.
- E2 lock take (R41, top level): `.env` copied 09:03 EDT; `<F0>` = 664 / 35 / `272c95bbb12241e3611e4b36326ccf87`; `--proof-only` at `0013`. **dev forward: APPLIED 09:04 EDT** (0014-0022, `content UNCHANGED on every table`); rolled back 09:05, `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (E2)`. (Lock take 1 of the R41 extra takes.)
- E3 lock take (R41, the top level, take 2): `.env` copied 09:06 EDT; `<F0>` = 664 / 35 / `272c95bbb12241e3611e4b36326ccf87`; `--proof-only` at `0013`. **dev forward: APPLIED 09:06 EDT**; green, two mutations, green; rolled back 09:07, `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (E3)`.
- W lock take 09:18–09:35: `.env: removed, proven gone (W)`. No migration is left applied; `cobalt_dev: 0013 — F2 = F0`.
- `cobalt_redactions` on `cobalt_dev` read 222 rows at PREFLIGHT, 224 at E2 and 225 after W pass 1. The fingerprint does not see rows, and (c3r) covers only `ZZX5R`; this build writes no redaction. It is recorded as a fact and is not a decision (L70).
- The fix's `locked[...]` index shift in the taps-moved arm (`store.py` around `:1225-1237`) is the card's own instruction ("the `locked[...]` reads at `:1217-1232` shift by one"). It is the only edit outside `:1201-1217`; no SQL there changed.
- Cleanup owed: none. Every row of the real-factory tests was deleted by id and counted zero in-test, (c3r) found no `ZZX5R` rows, and no `.env` is left.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: x5-tap-refresh · tip: 2a5fa102 | on 53a85f27 | migration: none | offline 3783/0 | with-DB 4555/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
