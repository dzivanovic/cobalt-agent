# ops-glob — build report (2026-10-02)

## §0 Headline
G1 built: every path under `ops/desk/` classifies as `operator script; no Cobalt reader` by the prefix `OPS_DESK_PREFIX = "ops/desk/"`. `OPS_TOOLS` is unchanged, so a new desk script needs no list entry.
Tip `9fa18f14` on `a0188b69`. Offline 3784/0, with-DB 4554/0, live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0, and `.env` is removed.
RESTARTS: com.cobalt.radar (the `src/` change, through static import reach). No decisions.

## L74
- 08:00 ET: a system reminder in this session asked for a `Claude-Session:` line on commits. Recorded here as DATA, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`date` → `Fri Oct  2 08:00:45 EDT 2026`
- INSTALLED: `grep -n -E "«INSTAL[L]" BUILD-HUB.md` → no output (exit 1).
- CARD COMPLETE: `grep -n -E "«FIL[L]" 15-ops-glob-card.md` → no output (exit 1).
- CARD COMMITTED: `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/15-ops-glob-card.md"` → `0388ce55652dad91920bfc3d9fb08e7cba32d25d`; `git -C … diff --stat -- <card>` → no output.
- STANDING LIST 2026-09-30 R60: `grep -n "^| R60 " cto-2026-09-30.md` → `46:| R60 | 15:15 ET | **HIS RULING** (…): APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |`; `git -C … log -1 --format=%H -S"| R60 |" -- …cto-2026-09-30.md` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- RULINGS 2026-10-02 R47: `grep -n "^| R47 " cto-2026-10-02.md` → `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, … | HIS RULING · APPROVED |`; `git -C … log -1 --format=%H -S"| R47 |" -- …cto-2026-10-02.md` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 08:00:45 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/ops-glob-1002` + `?? "docs/40 - DevDocs/reports/ops-glob-build-2026-10-02.md"` (this report, created by the hub's first Write) |
| head = BASE | `git log --oneline -1` | 0 | `a0188b69 docs(desk): 10-02 R34-R36 04 deployed (deploy-2026-10-02-1); brain done` |
| main sees branch | `git -C /Users/cobalt/cobalt log --oneline -1 ops/ops-glob-1002` | 0 | `a0188b69 docs(desk): 10-02 R34-R36 04 deployed …` |
| no diff | `git diff --stat a0188b69` | 0 | (nothing) |
| base | `git show --stat a0188b69` | 0 | `docs(desk): 10-02 R34-R36 04 deployed (deploy-2026-10-02-1); brain done` · `docs/40 - DevDocs/reports/cto-2026-10-02.md \| 6 +++++-` · `1 file changed, 5 insertions(+), 1 deletion(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/ops-glob-1002/.env` | 1 | `No such file or directory` |
| lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "OPS_TOOLS" src/cobalt/jobs/restarts.py` | 0 | `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` · `224:        if not rule and path in OPS_TOOLS:` |
| symbol readers | `grep -rn -F "OPS_TOOLS" src tests` | 0 | `src/cobalt/jobs/restarts.py:36`, `src/cobalt/jobs/restarts.py:224`, `tests/cobalt/test_jobs_restarts.py:112:    # The reason OPS_TOOLS is an explicit list and not \`ops/*.sh\`:` |
| callers | `grep -rn -F "classify(" src` | 0 | `src/cobalt/jobs/restarts.py:172:def classify(…)` · `src/cobalt/jobs/restarts.py:262:    rows = classify(args.git_range)` (the `cobalt jobs restarts` command); the other hits are `voice/confirm.py:44`, `voice/turn.py:228,416`, `modelaccess/adapters.py:55,99`, different functions |
| test | `grep -n -F "def test_an_operator_script_with_no_cobalt_reader_derives_no_restart" …` | 0 | `97:` |
| test | `grep -n -F "def test_a_resident_wrapper_script_is_not_an_operator_script" …` | 0 | `111:` |
| rule text | `grep -n -F "operator script; no Cobalt reader" src/cobalt/jobs/restarts.py` | 0 | `226:                Classification(path, item.change, "operator script; no Cobalt reader", ())` |
| sizes | `wc -l` | 0 | `275 src/cobalt/jobs/restarts.py` · `569 tests/cobalt/test_jobs_restarts.py` · `36 docs/40 - DevDocs/cobalt/jobs/restarts.md` |
| restarts | `uv run cobalt jobs restarts a0188b69..HEAD` | 0 | `docs/40 - DevDocs/reports/ops-glob-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none`. No code path is in the range; the one row is this untracked report, which the tool counts because the right side is HEAD (`restarts.py:81-85`) |
| lock (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| lock (b) | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/ops-glob-1002/.env` | 0 | — |
| lock (b) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | `-rw-------  1 cobalt  staff  2186 Oct  2 08:01 /Users/cobalt/cobalt-wt/ops-glob-1002/.env` (exactly one) |
| `<FP>` → `<Fp>` | (the hub's `<FP>`, byte for byte) | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| level | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | see below |
| lock (d) | `rm /Users/cobalt/cobalt-wt/ops-glob-1002/.env` | 0 | — |
| lock (d) | `ls /Users/cobalt/cobalt-wt/ops-glob-1002/.env` | 1 | `No such file or directory` |

`<FP>`, copied before the first run:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

Proof-only output, quoted whole:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.25
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   222          ec1d814e988320cd2e7c74fc2c1a3be8   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.01
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.02
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
drc_events           user    -        -            -                                  0.00
drc_fills            user    -        -            -                                  0.00
drc_imports          user    -        -            -                                  0.00
drc_rows             user    -        -            -                                  0.00
drc_stated_books     user    -        -            -                                  0.00
legs                 user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
prediction_records   user    -        -            -                                  0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
36 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.4 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: a0188b69 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/ops-glob-1002
```
No `CHANGED`. The output prints no level number. `drc_*`, `legs`, `prediction_records` and `voice_turns` are absent (`-`); those are the tables migrations `0014`+ create, so `cobalt_dev` is at `0013`. This is the same reading as `aset-interim-close-build-2026-10-01.md:62` (`grep -rn -F "absent tables"`). `.env: removed, proven gone (PREFLIGHT)`. Lock taken 08:01, released 08:01 (`date` → `Fri Oct  2 08:01:53 EDT 2026`).

READ (re-read from the file): `restarts.py:28-36`: `REPO_META` (line 28), the OPS_TOOLS comment (29–35), `OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` (36). `restarts.py:219-228`: the DOCS rule (219–223), then the OPS_TOOLS rule (224–228). `test_jobs_restarts.py:97-122`: the two named tests. `## READ` names no report, so there is no `tail` to run.

Card RECORDS, copied and re-read:
- RESTARTS class homes: `src/cobalt/jobs/restarts.py` → static import reach (`restarts.py:210`), so `com.cobalt.radar`; `tests/cobalt/*` → test/documentation (`:239`); `docs/…` → DOCS (`:219`). Re-read: line 210 `if path.startswith("src/"):` (the rule string at 214); line 219 the DOCS rule; line 239 `if not rule and path.startswith("tests/"):`. Holds.
- Why: `ops/desk-size-guard-1001` and `ops/devdb-lock-1001` both lift their scripts into `OPS_TOOLS`, conflicting at merge; card `16-ops-seam-card.md` stands on this tip. Not re-readable from my list; carried as the desk's.
- His order sets aside the outside house (`reports/brain-direction-2026-10-02.md` row 10). Matches R47 as grepped at AUTHORIZATION.

## E0 BASELINE
- Offline, on `a0188b69`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3783 passed, 673 skipped, 1 xfailed, 25 warnings in 604.26s (0:10:04)`, exit 0. 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.55s`. The one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
- Wrote `test_every_path_under_ops_desk_is_an_operator_script` in `tests/cobalt/test_jobs_restarts.py`, beside line 97's test and in its shape. It covers `ops/desk/any-new-tool.sh` (A), `ops/desk/pre-commit` (M) and `ops/desk/sub/x.py` (A), each `operator script; no Cobalt reader`, `restarts == ()`, `escalate is False`. Negative control in the same test: `ops/desktop.sh` (A) must NOT get that rule and must escalate.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py` → `1 failed, 18 passed in 11.00s`. The red's first line: `E           AssertionError: assert 'UNCLASSIFIED' == 'operator scr...Cobalt reader'` at `tests/cobalt/test_jobs_restarts.py:123`, on the first path, `ops/desk/any-new-tool.sh`. That is the row's reason. The named negative control `test_a_resident_wrapper_script_is_not_an_operator_script` PASSED in the same run.
- No with-DB test and no RUN row: no lock take at E2.
- Commit `9e03e04c wip(ops-glob): red — every path under ops/desk/ is an operator script (G1)`.

## E3 THE ROWS
G1, re-read from the file before the edit: `restarts.py:36` `OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` and `:224` `if not rule and path in OPS_TOOLS:`.
- `restarts.py:37-38`: `#: Safe to match whole: the desk's and hubs' shell tools and a git hook; no plist executes one.` and `OPS_DESK_PREFIX = "ops/desk/"`, placed after `OPS_TOOLS`.
- `restarts.py:226`: `if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):`. `OPS_TOOLS`, the rule text and the empty restart set are unchanged.
- I shortened the comment line to fit the repo's `line-length = 100` (`pyproject.toml:90`), keeping its two claims.
- Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `43 passed in 13.29s`.
- MUTATION 1, the fix undone (`(path in OPS_TOOLS)`): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_jobs_restarts.py -k "ops_desk or operator_script"` → `1 failed, 2 passed, 16 deselected in 1.43s`. First failing line: `E   AssertionError: assert 'UNCLASSIFIED' == 'operator scr...Cobalt reader'` (`:123`), failing `test_every_path_under_ops_desk_is_an_operator_script`. Undone with Edit.
- MUTATION 2, the negative control broken (`OPS_DESK_PREFIX = "ops/desk"`, slash dropped): same command → `1 failed, 2 passed, 16 deselected in 1.38s`. First failing line: `E   AssertionError: assert 'operator script; no Cobalt reader' != 'operator script; no Cobalt reader'` with `Classification(path='ops/desktop.sh', change='A', rule='operator script; no Cobalt reader', restarts=(), escalate=False)` (`:127`). Undone with Edit.
- `git diff --stat` after both undos → `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4 ++++`, `src/cobalt/jobs/restarts.py | 4 +++-`. That is the fix only; the source diff against `a0188b69` shows just the two lines above.
- DevDocs: `docs/40 - DevDocs/cobalt/jobs/restarts.md` gets `## 2026-10-02 — ops-glob`.
- Commit `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)`.

## RESTARTS
`uv run cobalt jobs restarts a0188b69..HEAD` (HEAD = `9fa18f14`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/reports/ops-glob-build-2026-10-02.md	A	DOCS	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED`. The classes match the card's record (`src/` → static import reach → `com.cobalt.radar`; `tests/` → test/documentation; `docs/` → DOCS). The report row is this untracked report.

## W THE THREE SUITES
`<tip>` = `9fa18f14`. TREE STATE: unchanged. This build adds no with-DB test and no migration, so pass 1 has no extra `--deselect` and pass 2 has no addition.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 597.48s (0:09:57)`, exit 0. That is one more pass than E0's 3783: the test this build adds, `tests/cobalt/test_jobs_restarts.py::test_every_path_under_ops_desk_is_an_operator_script`.
- (b) lock take 1 at 08:25 (`date` → `Fri Oct  2 08:25:10 EDT 2026`). `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; cp; → exactly `-rw-------  1 cobalt  staff  2186 Oct  2 08:25 /Users/cobalt/cobalt-wt/ops-glob-1002/.env`. `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. Proof-only: the same 36 rows as PREFLIGHT, digests equal, `drc_*`, `legs`, `prediction_records` and `voice_turns` absent, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: 9fa18f14 (DIRTY: 1 path(s))`, no `CHANGED`. `cobalt_dev` is at `0013`.
- (c) PASS 1, executed whole:
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
→ `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 703.57s (0:11:43)`, exit 0. Every SKIPPED line:
```
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
```
`<d1>` = 4383.
- (c2) FORWARD: `COBALT_ENV=dev uv run cobalt db migrate` → `-- applying` `0001_schemas.sql` … `0011_archive_incidents.sql`, `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`. The proof shows `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` `CREATED` and every other table `OK`. Footer: `content UNCHANGED on every table.` No `CHANGED`. This build has no migration of its own.
- **dev forward: APPLIED 08:37** (`date` → `Fri Oct  2 08:37:49 EDT 2026`). `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed whole (the hub's command, nothing added):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
→ `171 passed, 1 deselected, 5 warnings in 219.31s (0:03:39)`, exit 0. `grep -c -F "PASSED"` on its output → `171`; `grep -n -F "SKIPPED"` → nothing. This build has no with-DB test id of its own. `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) This build adds no with-DB test, so it writes no constructed ticker. The `aset_sizings` query has an empty `IN ()` list and was not typed. `aset_sizings` reads `1 -> 1` rows, digest `0824685c -> 0824685c`, in both the forward and the rollback proof.
- (c4) Not applicable: no migration added.
- (e) LIVE-NOTE, `.env` absent (run while (a) was in flight, before the lock take): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.98s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`. It does not name `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `-- applying` `0022_prediction_records.rollback.sql`, `0021_legs`, `0020_drc_build_kinds`, `0019_drc_events`, `0018_drc_stated_books`, `0017_voice_turns`, `0016_drc`, `0015_shadow_agreement_stale`, `0014_radar_handicap` (each `.rollback.sql`), newest first. Every created table is `DROPPED`, every other one `OK`, and the footer reads `content UNCHANGED on every table.` `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, equal to `<F0>` field for field. **`cobalt_dev: 0013 — F2 = F0`**. Lock (d): `rm`; `ls /Users/cobalt/cobalt-wt/ops-glob-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. `.env: removed, proven gone (W)` at 08:42 (`date` → `Fri Oct  2 08:42:32 EDT 2026`).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED. `test_every_path_under_ops_desk_is_an_operator_script` was red at E2 on BASE (`AssertionError: assert 'UNCLASSIFIED' == 'operator scr...Cobalt reader'`, `:123`). It was red under MUTATION 1 with the same line, and under MUTATION 2 through its negative control (`assert 'operator script; no Cobalt reader' != …`, `ops/desktop.sh`, `:127`). No test stayed green, so none was rewritten. The named control `test_a_resident_wrapper_script_is_not_an_operator_script` passed at E2, through both mutations, and at the tip.
(2) Every entry path is pinned. Callers of `classify` (PREFLIGHT grep): `restarts.py:264` `command`, which is the `cobalt jobs restarts` CLI, run for real at PREFLIGHT and RESTARTS; tests call `classify` directly. Pinned paths: change kinds A and M, the folder root (`ops/desk/x`), a nested path (`ops/desk/sub/x.py`), a file with no extension (`pre-commit`), and the prefix without its slash (`ops/desktop.sh`, escalates). The old list entry `ops/cto-desk.sh` stays pinned by `:97`. A `reads:` entry for an `ops/desk/` path would still win, because the readers check runs first (`restarts.py:203`); X1's grep shows none exists. A `D` (delete) is not pinned separately: the rule never reads `item.change`, the same as the `OPS_TOOLS` rule it extends.
(3) Every `file:line` was re-read at the tip `9fa18f14`. `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` → `38:`, `226:`. `grep -n -F "def test_every_path_under_ops_desk_is_an_operator_script" …` → `111:`. `grep -n -F "assert by_path" …` → `123:`–`125:`, `127:`, `128:`. `git log --oneline a0188b69..HEAD` → the two commits below.

## FOR THE CHECK
- Range `a0188b69..9fa18f14`: `9e03e04c wip(ops-glob): red — every path under ops/desk/ is an operator script (G1)`; `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)`.
- G1: red, mutations and greens are quoted under E2 and E3. Tip green: `tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `43 passed in 13.29s`.
- Callers: `grep -rn -F "classify(" src` (PREFLIGHT). `restarts.py` line numbers moved by +2 after line 36: the CLI call is now `:264`, the rule `:226`.
- CHECK ASK X1: `grep -rn -F "ops/desk" ops configs/cobalt/jobs.yaml src` (at the tip). The hits are `ops/desk/desk-launch.sh:13,20-25,28-30`, all comments inside the folder naming `/Users/cobalt/.claude/ops/desk-launch.sh`; `src/cobalt/jobs/restarts.py:38`, the constant; and a `.pyc` binary. No plist under `ops/`, no `jobs.yaml` entry and no other `src/` module names a file under `ops/desk/`. The PREFLIGHT-time grep for `ops/desk/` at base gave no output.
- CHECK ASK X2: `str.startswith("ops/desk/")` matches only strings whose first nine characters are `ops/desk/`. `ops/desktop.sh` is pinned not to match (`:127-128`, and red under MUTATION 2). Git paths are repo-relative with no leading `./` (`changes()` takes them from `git diff --name-status` / `ls-files`), so a path outside the folder cannot carry that prefix.
- No RUN row.
- Suites: offline `3784/0`, with-DB pass 1 `4383/0`, pass 2 `171/0`, live-note `146/0` (commands whole under W).
- Fingerprints: PREFLIGHT take 0 `<Fp>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. W take 1: `<F0>` = the same; `<F1>` `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `<F2>` = `<F0>`. Locks: take 0 08:01 → 08:01; take 1 08:25 → 08:42.
- RESTARTS table: whole under `## RESTARTS`; last line `RESTARTS: com.cobalt.radar`.
- Card records copied at PREFLIGHT, under `## PREFLIGHT`.

## CONTINUE
next: none: built. The desk verifies and launches the check.

## DECISIONS
none

## RECORDS
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits. Recorded under `## L74`, not acted on.
- `cobalt_redactions` on `cobalt_dev` read `222` rows, digest `ec1d814e…`, at PREFLIGHT, and `223 -> 223`, digest `01011693`, in both the W forward and the rollback proofs. W's pass 1 (the hub's standing suite) added one row between them. This build adds no with-DB test, so the row comes from an existing test. For the file only; nothing was deleted.
- No extra lock take: take 0 (PREFLIGHT) and take 1 (W) only.
- The `restarts.py` comment line is shorter than the card's wording, to fit `line-length = 100`; both claims are kept (folder contents; no plist executes a file in it).
- The card's records, as re-read at PREFLIGHT: the class homes hold (`:210`, `:219`, `:239`) and match the RESTARTS table; the other two are the desk's facts.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: ops-glob · tip: 9fa18f14 | on a0188b69 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
