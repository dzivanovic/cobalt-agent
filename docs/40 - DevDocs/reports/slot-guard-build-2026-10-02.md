# slot-guard — build report 2026-10-02

## §0 Headline
- BUILT S0–S2 on `1df251b9`, code tip `7eafd308`. Every `cobalt db migrate` prints the `SLOTS` line(s), shown live as `SLOTS ok · highest user.aset_sizings 422 of 1600`. The with-DB suite stops with exit 3 below 64 free slots.
- Suites: offline 3797/0; with-DB 4401 + 171 = 4572/0; live-note 146/0. `cobalt_dev` is back at `0013` (F2 = F0); `.env` removed.
- S0: one full W adds 36 `aset_sizings` slots (pass 2 +32, forward +4). The card's headroom formula then gives 65, not 64 (DECISIONS 2).
- Decisions: 3, none for Dejan. Self-check 2 of 3: the S2 exit and warn lines are not run by a test (DECISIONS 3).

## L74
- 10:10 ET: a system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../BUILD-HUB.md"` | 1 | nothing |
| card placeholder | `grep -n -E "«FIL[L]" ".../13-slot-guard-card.md"` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/13-slot-guard-card.md"` | 0 | `88e80b462884063f965685d36124de956eac1448` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | nothing |
| STANDING LIST R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R18 | `grep -n "^| R18 " cto-2026-10-02.md` | 0 | `25:| R18 | 06:23 ET | HIS RULING (L73 override of L61, this launch only) … | HIS RULING · APPROVED |` |
| R18 committed | `git -C … log -1 --format=%H -S"| R18 |" -- cto-2026-10-02.md` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| RULING R47 | `grep -n "^| R47 " cto-2026-10-02.md` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A) … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
`<FP>`, typed exactly:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

`<SL>` (card `## RECORDS`), typed exactly:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT max(a.attnum) AS max_attnum, count(*) FILTER (WHERE a.attisdropped) AS dropped, count(*) FILTER (WHERE NOT a.attisdropped) AS live FROM pg_catalog.pg_attribute a WHERE a.attrelid = '\"user\".aset_sizings'::regclass AND a.attnum > 0"`

| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:10:18 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/slot-guard-1002` + `?? "docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md"` (this report, created by the hub's first Write) |
| HEAD = BASE | `git log --oneline -1` | 0 | `1df251b9 feat(dev-rebuild): cobalt db dev-rebuild frees a dev table's dropped column slots, kept only on an equal compare (D1, D2, D3; L1, L3, L4, L76)` |
| branch tip in main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/slot-guard-1002` | 0 | `1df251b9 feat(dev-rebuild): …` (same) |
| diff vs BASE | `git diff --stat 1df251b9` | 0 | nothing |
| BASE | `git show --stat 1df251b9` | 0 | 6 files: `cli.md` +3, `dev_rebuild.md` +18, `cli.py` 203, `dev_rebuild.py` +771, `test_dev_rebuild_cli.py` 17, `test_dev_rebuild_db.py` 11; `993 insertions(+), 30 deletions(-)` |
| .env absent | `ls /Users/cobalt/cobalt-wt/slot-guard-1002/.env` | 1 | `No such file or directory` |
| no lock held | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "DEFAULT_LOCK_TIMEOUT_S" src/cobalt/db_migrations/cli.py` | 0 | `143:DEFAULT_LOCK_TIMEOUT_S = 30` (+ uses at 688, 952, 955, 980, 982, 994) |
| symbol (new) | `grep -rn -F "slot_report" src tests` | 1 | nothing — row S1 creates it |
| symbol (new) | `grep -rn -F "slot_verdict" src tests` | 1 | nothing — row S2 creates it |
| READ | `grep -n -F "def _migrate" tests/cobalt/test_tenancy.py` | 0 | `668:def _migrate(*args: str) -> str:` |
| READ | `grep -n -F "class TestMigrationRoundTrip" tests/cobalt/test_tenancy.py` | 0 | `694:class TestMigrationRoundTrip:` (test body 703–714) |
| READ | `grep -n -F "def test_card_checks_index_and_receipt_immutability_on_cobalt_dev" tests/cobalt/test_radar_score_migration.py` | 0 | `412:def test_card_checks_index_and_receipt_immutability_on_cobalt_dev():`; `:497 _apply(conn, _rollback_paths("0005"))`, `:506 _apply(conn, [SYSTEM_SQL, USER_SQL])` |
| READ | `grep -n -F "requires_db" tests/cobalt/conftest.py` | 1 | nothing: the gate in `conftest.py` is the Postgres settings check `:154 if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):` (Read tool); `requires_db` is defined per test module (e.g. `test_dev_rebuild_db.py:29`) |
| READ | `grep -n -F "DROP COLUMN" …/0004_radar_pool.rollback.sql` | 0 | `7: DROP COLUMN IF EXISTS pool_member_id,` `8: DROP COLUMN IF EXISTS account_mode;` `10: DROP COLUMN IF EXISTS account_mode;` |
| READ | `grep -n -F "DROP COLUMN" …/0007_radar_cards.rollback.sql` | 0 | lines 40–64: 25 `DROP COLUMN IF EXISTS` (promoted_at … trade_def_slug) |
| READ | `grep -n -F "DROP COLUMN" …/0021_legs.rollback.sql` | 0 | `10: DROP COLUMN IF EXISTS kind;` `13–15:` trade_note_path, drift_warning_pct, drift_warned |
| READ | `grep -n -F "DROP COLUMN" …/0022_prediction_records.rollback.sql` | 0 | `7:ALTER TABLE "user".aset_sizings DROP COLUMN IF EXISTS last_price_bar_ts;` |
| READ | `grep -n -F "## L68 GATE" deploy-2026-10-01-1.md` | 0 | `101:## L68 GATE` |
| READ last line | `tail -n 3 deploy-2026-10-01-1.md` | 0 | `FAILED: gate — G (c) — tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev (TooManyColumns: cobalt_dev "user".aset_sizings 1581/1600 column slots) · rollback: not used · decisions: 2 · for Dejan: 0` |
| callers | `grep -rn -F "cmd_migrate(" src tests` | 0 | `cli.py:609` (def); `test_migrate_proof.py:645, 667, 933, 1490, 1546, 1613, 1696, 1768, 2136`; `test_radar_migration.py:69, 108` |
| wc -l | `wc -l <the rows' files>` | 0 | `dev_rebuild.py 771` · `cli.py 1002` · `test_dev_rebuild_cli.py 212` · `test_dev_rebuild_db.py 172` · `conftest.py 290` · `dev_rebuild.md 18` · `cli.md 375` |
| RESTARTS empty | `uv run cobalt jobs restarts 1df251b9..HEAD` | 0 | `docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md A DOCS -` / `RESTARTS: none` (the untracked report only; no commit in range) |

Card `## RECORDS`, copied:
- `<SL>` as above (re-read: the deploy report's `## L68 GATE` sits at `:101`; its stop line quotes `1581/1600`).
- THE CAUSE, read from code and unproven (L70) — S0 measures it. Re-read: the four rollback files drop 2 + 25 + 3 + 1 = 31 `aset_sizings` columns (0004 `:7–8`, 0007 `:40–64`, 0021 `:13–15`, 0022 `:7`; 0004 `:10` and 0021 `:10` are other tables); `TestMigrationRoundTrip` `:703–714` runs `--rollback --down-to 0001` in a subprocess.
- RESTARTS class homes (drafter): not re-read here; RESTARTS derives them.
- Cut by the brain 09:20 ET: rows S0–S2; base = card 11's BUILT tip (`1df251b9`, re-read above); check = fresh Opus session alone (R47, re-read in AUTHORIZATION).

THE LOCK PROBE (take 0), 10:13 ET:
| rule | command | exit | output |
|---|---|---|---|
| lock (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | `-rw-------  1 cobalt  staff  2186 Oct  2 10:12 /Users/cobalt/cobalt-wt/ops-seam-1002/.env` |

The lock is held by `ops-seam-1002`. Nothing copied, nothing run on `cobalt_dev`; this worktree's `.env` was never created.

THE LOCK PROBE (take 0), resumed 10:29 ET after `CONTINUE`:
| rule | command | exit | output |
|---|---|---|---|
| lock (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| lock (b) | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/slot-guard-1002/.env` | 0 | nothing |
| lock (b) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | one line: `… Oct  2 10:29 /Users/cobalt/cobalt-wt/slot-guard-1002/.env` |
| `<FP>` → `<Fp>` | `<FP>` | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| proof-only | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | quoted whole below |
| lock (d) | `rm /Users/cobalt/cobalt-wt/slot-guard-1002/.env` | 0 | nothing |
| lock (d) | `ls /Users/cobalt/cobalt-wt/slot-guard-1002/.env` | 1 | `No such file or directory` |

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.47
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   227          762bec95002a91e77e481412c2d000fe   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
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
36 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 29 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.5 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: dd60df2b (clean) · /Users/cobalt/cobalt-wt/slot-guard-1002
```
Level: the tables `0014`+ create (`drc_*`, `legs`, `prediction_records`, `voice_turns`) are absent and every `0013`-and-below table is present → `cobalt_dev` at `0013`; no `CHANGED`. `.env: removed, proven gone (PREFLIGHT)`.

## E0 BASELINE
Code tree = `1df251b9` (HEAD `dd60df2b` adds this report only).
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3781 passed, 677 skipped, 1 xfailed, 25 warnings in 650.74s (0:10:50)`; exit 0. Skips: `Postgres env settings not available` and the two `COBALT_LIVE_VAULT_ROOT not set` (offline by design).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.58s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written (no `src/` edit):
- `tests/cobalt/test_dev_rebuild_cli.py` (offline): S1 — `test_s1_slot_report_reads_the_rows_and_the_line_is_the_warn_line_exactly` (`(user, aset_sizings, 1581, 1527, 54)` → the WARN line exactly), `test_s1_below_the_warn_mark_is_one_ok_line_naming_the_highest` (`664` → `SLOTS ok · highest user.aset_sizings 664 of 1600`), `test_s1_the_two_ends_of_the_warn_edge[1200|1199]`, `test_s1_one_warn_line_per_relation_at_or_above_the_mark`, `test_s1_a_failed_slot_read_is_named_and_undone_inside_its_savepoint`, `test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[proof-only|forward|rollback|proof-only-production]`; S2 — `test_s2_slot_verdict[1581-fail|1537-fail|1536-warn|1199-ok]`, `test_s2_slot_verdict_with_no_rows_is_ok`.
- `tests/cobalt/test_dev_rebuild_db.py` (with-DB): `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` (the card's `<SL>` verbatim, in the module's rolled-back `conn` fixture).

Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py` → `15 failed, 12 passed, 5 skipped in 0.08s`. Every red's first line:
- the 11 S1 reds (`:270`, `:278`, `:295` ×2, `:303`, `:318`, `:357` ×4): `ImportError: cannot import name 'slot_report' from 'cobalt.db_migrations.dev_rebuild'` — the row's named red.
- the 5 S2 reds (`:381` ×4, `:389`): `ImportError: cannot import name 'slot_verdict' from 'cobalt.db_migrations.dev_rebuild'` — "the name does not exist". First run named `SLOT_FAIL_HEADROOM` (import order); the import was reordered so the red names `slot_verdict`, and re-run as above.
- 12 passed = the file's existing D2 tests; 5 skipped = `test_dev_rebuild_db.py` without Postgres settings.

With-DB red, 10:43 ET: lock (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:37 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`. The lock is held; not taken.

With-DB red, resumed 11:01 ET after `CONTINUE` (lock take 1):
| rule | command | exit | output |
|---|---|---|---|
| lock (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| lock (b) | `cp …/cobalt/.env …/slot-guard-1002/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | one line, `… Oct  2 11:01 /Users/cobalt/cobalt-wt/slot-guard-1002/.env` |
| `<FP>` → `<F0>` | `<FP>` | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| proof-only | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | the PREFLIGHT table, `0014`+ tables absent → `0013`; no `CHANGED`; one difference: `cobalt_redactions 228 · 0258b01d…` (227 · 762bec95… at PREFLIGHT: append-only telemetry); last line `code: b6a3219b (clean) · /Users/cobalt/cobalt-wt/slot-guard-1002` |
| with-DB red | `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` | 1 | `1 failed, 4 passed in 0.36s`; red `test_dev_rebuild_db.py:188: ImportError: cannot import name 'slot_report' from 'cobalt.db_migrations.dev_rebuild'`; PASSED: `test_d1_rebuild_frees_every_dropped_slot_and_keeps_rows_and_catalog`, `test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept`, `test_d1_dry_run_rolls_back_after_the_compare`, `test_d3_aset_sizings_passes_the_rule_as_a_dry_run_at_0013` |
| `<FP>` again | `<FP>` | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` |
| lock (d) | `rm …/slot-guard-1002/.env`; `ls …/slot-guard-1002/.env` | 0 / 1 | `No such file or directory` |
`.env: removed, proven gone (E2)`. RUN rows: S0 runs at W (it reads during the suites).

## E3 THE ROWS
Commit `7eafd308 feat(slot-guard): every db migrate prints the SLOTS line; the with-DB suite stops below 64 free column slots (S1, S2; L1, L3, L76)`. 6 files, `153 insertions(+), 1 deletion(-)`.

S1:
- `dev_rebuild.py`: `SLOT_LIMIT = 1600`, `slot_report(conn)` (one catalog query over `system` / `"user"` tables, relkind `r` / `p`, highest `max_attnum` first), `slot_lines(rows, warn_at)`.
- `cli.py`: `SLOT_WARN_AT = 1200` beside `DEFAULT_LOCK_TIMEOUT_S`. `_slot_lines(conn)` reads under `SAVEPOINT cobalt_slots`; it is called inside the transaction after the AFTER probe (forward and rollback) and after the probe (`--proof-only`). Its lines print after the proof table and before `code:`.
- A failed read → `ROLLBACK TO SAVEPOINT` + `SLOTS UNKNOWN — <type>: <e>` (see `## DECISIONS` 1).

S2:
- `dev_rebuild.py`: `SLOT_FAIL_HEADROOM = 64`, `slot_verdict(rows, warn_at, fail_headroom)`.
- `tests/cobalt/conftest.py`: `pytest_sessionstart` runs only with `POSTGRES_HOST` and `POSTGRES_USER` set. It reads `slot_report` through `REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)`; `fail` → `pytest.exit("cobalt_dev column slots: <schema>.<table> <n> of 1600 — run a devfix (cobalt db dev-rebuild <schema>.<table>) before any with-DB gate", returncode=3)`; `warn` → the `SLOTS WARN` lines via `pytest_terminal_summary`.

DevDocs: one `## 2026-10-02 — slot-guard` line each in `db_migrations/dev_rebuild.md` and `db_migrations/cli.md`.

Greens after the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py tests/cobalt/test_migrate_proof.py tests/cobalt/test_radar_migration.py` → `74 passed, 26 skipped in 1.70s` (skips: `Postgres env settings not available`).

THE MUTATIONS (Edit tool; each run `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py`):
| # | row | mutation | summary | first failing line |
|---|---|---|---|---|
| M1 | S1 (undoes the fix) | proof-only branch: the `for line in slots: print(line)` removed | `2 failed, 25 passed` | `test_dev_rebuild_cli.py:361: AssertionError: assert ['cobalt db m...'<code line>'] == ['<proof tabl...'<code line>']` — `[proof-only]`, `[proof-only-production]` |
| M2 | S1 edge | `slot_lines`: `m >= warn_at` → `m > warn_at` | `1 failed, 26 passed` | `:299: AssertionError: … 'SLOTS ok · highest user.aset_sizings 1200 of 1600' != 'SLOTS WARN user.aset_sizings max_attnum 1200 …'` |
| M3 | S1 savepoint | `ROLLBACK TO SAVEPOINT cobalt_slots` removed from the failure path | `1 failed, 26 passed` | `:323: assert False` (`startswith('ROLLBACK TO SAVEPOINT ')`) |
| M4 | S2 fail edge | `slot_verdict`: `< fail_headroom` → `<= fail_headroom` | `1 failed, 26 passed` | `:385: AssertionError: assert 'fail' == 'warn'` (`[1536-warn]`) |
| M5 | S2 warn edge | `slot_verdict`: `>= warn_at` → `> warn_at` | first run `27 passed` — STAYED GREEN; the test gained a `(1200, "warn")` case; re-run `1 failed, 27 passed` | `:385: AssertionError: assert 'ok' == 'warn'` (`[1200-warn]`) |
Each mutation was undone with the Edit tool. `git diff --stat` then showed only the fix (cli.py 33, dev_rebuild.py 68, conftest.py 45, test_dev_rebuild_cli.py 2 = the added 1200 case), and the greens above ran on that tree.

## RESTARTS
`uv run cobalt jobs restarts 1df251b9..HEAD` (HEAD `7eafd308`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md	M	DOCS	-
docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md	M	DOCS	-
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/dev_rebuild.py	M	static import reach	com.cobalt.radar
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_dev_rebuild_cli.py	M	test/documentation; no resident	-
tests/cobalt/test_dev_rebuild_db.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row; no `configs/` path.

## W THE THREE SUITES
`<tip>` = `7eafd308`.
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3797 passed, 678 skipped, 1 xfailed, 25 warnings in 617.62s (0:10:17)`; exit 0 → `<p>` = 3797. Against E0 (3781 / 677): +16 passed = this build's 16 offline test ids; +1 skipped = `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` (with-DB). The 16 added offline ids: `test_s1_slot_report_reads_the_rows_and_the_line_is_the_warn_line_exactly`, `test_s1_below_the_warn_mark_is_one_ok_line_naming_the_highest`, `test_s1_the_two_ends_of_the_warn_edge` ×2, `test_s1_one_warn_line_per_relation_at_or_above_the_mark`, `test_s1_a_failed_slot_read_is_named_and_undone_inside_its_savepoint`, `test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table` ×4, `test_s2_slot_verdict` ×5, `test_s2_slot_verdict_with_no_rows_is_ok`.
- (b) 11:15 ET: lock (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 11:06 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`. The lock is held; not taken (stop, `## RECORDS`).
- (b) resumed 11:43 ET after `CONTINUE: W (b)` (lock take 2). Lock (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Lock (b) `cp`, then `ls -la` → one line `… Oct  2 11:43 /Users/cobalt/cobalt-wt/slot-guard-1002/.env`. `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
  - `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → the PREFLIGHT table: `0014`+ tables `-` → `0013`; no `CHANGED`; `cobalt_redactions 230 · 7c7598ce…`. Its last three lines:
    ```
    NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
    SLOTS ok · highest user.aset_sizings 422 of 1600
    code: 6d152c2b (clean) · /Users/cobalt/cobalt-wt/slot-guard-1002
    ```
    S1 on the real `cobalt_dev`: the SLOTS line prints after the proof table and before `code:`.
  - S0 `<SL>` → `422 · 368 · 54`.
- (c) PASS 1 at `0013` (background), the pass-1 command byte for byte, with no deselect added (this build's with-DB test needs no migration above `0013`):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
  → `4401 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 707.16s (0:11:47)`; exit 0 → `<d1>` = 4401. Every SKIPPED line:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`

  S2's hook: the summary carries no `SLOTS` line (verdict `ok` at 422) and the run started (no exit 3). S0 `<SL>` after (c) → `422 · 368 · 54`.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) applied `0001` … `0013` (idempotent), then `0014_radar_handicap.sql` … `0022_prediction_records.sql` in order. The proof shows `content UNCHANGED on every table.` with 8 tables `CREATED` and no `CHANGED`. Its last two lines: `SLOTS ok · highest user.aset_sizings 426 of 1600` / `code: 6d152c2b (clean) · /Users/cobalt/cobalt-wt/slot-guard-1002`.
  - **dev forward: APPLIED 11:56 ET**; from here every ending runs (f).
  - `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`. S0 `<SL>` after (c2) → `426 · 368 · 58`.
- (c3) PASS 2, the pass-2 command byte for byte (this build deselected nothing in pass 1, so nothing is added):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → `171 passed, 1 deselected, 5 warnings in 221.72s (0:03:41)`; exit 0; no SKIPPED → `<d2>` = 171. `-rA`: `PASSED tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips`. The `ERROR` lines in the output are logged refusals the tests provoke (e.g. `REFUSED (cards.transition.FILLED): … inside MARKET RESET`), not results. `<d>` = 4401 + 171 = 4572. S0 `<SL>` after (c3) → `458 · 400 · 58`.
- (c3r) This build's with-DB test only reads: `slot_report` and `<SL>` inside the rolled-back `conn` fixture. It writes no ticker, so there is no `aset_sizings` ticker to query (a query with an empty `IN ()` is not valid SQL).
- (c4) not applicable: no migration in this build.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) reversed `0022` … `0014`, newest first. The proof shows `content UNCHANGED on every table.` with 8 `DROPPED` and no `CHANGED`. Its last two lines: `SLOTS ok · highest user.aset_sizings 458 of 1600` / `code: 6d152c2b (DIRTY: 1 path(s)) · …` (the dirty path is this report's uncommitted `dev forward` line).
  - `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`**.
  - S0 `<SL>` after (f) → `458 · 404 · 54`.
  - Lock (d): `rm …/slot-guard-1002/.env`; `ls …/slot-guard-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. `.env: removed, proven gone (W)`, 12:01 ET.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.38s`; the skip: `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (not `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.

S0 — the slot read `<SL>` (`max_attnum · dropped · live`) per phase:
| after | read | Δ max_attnum |
|---|---|---|
| (b) | `422 · 368 · 54` | — |
| (c) pass 1 at `0013` | `422 · 368 · 54` | 0 |
| (c2) forward `0014`–`0022` | `426 · 368 · 58` | +4 |
| (c3) pass 2 | `458 · 400 · 58` | +32 |
| (f) rollback to `0013` | `458 · 404 · 54` | 0 (+4 dropped) |
`ADD COLUMN` count per file (`grep -c -F "ADD COLUMN"`): `0004_radar_pool.sql` 3 · `0007_radar_cards.sql` 26 · `0021_legs.sql` 4 · `0022_prediction_records.sql` 1. These are statement lines in the file, across every table each file alters. The rollback files drop 2 + 25 + 3 + 1 = 31 `aset_sizings` columns (PREFLIGHT). See `DECISION S0`.

## PRE-STOP SELF-CHECK
(1) Holds. Each added test went red for its named reason:
- Every S1 / S2 offline test was red at E2: `ImportError … 'slot_report'` (11 tests) or `ImportError … 'slot_verdict'` (5 tests).
- The with-DB S1 test was red at E2 at `0013`: `test_dev_rebuild_db.py:188: ImportError … 'slot_report'`.
- E3 mutations were red: M1 (`[proof-only]`, `[proof-only-production]`), M2 (`[1200-…]` edge), M3 (savepoint test), M4 (`[1536-warn]`), M5 (`[1200-warn]`).
- M5 stayed green on its first run. The test was rewritten (`(1200, "warn")` added) and the re-run went red.

(2) Holds with one gap (`## DECISIONS` 3). Entry paths, from callers re-grepped at the tip:
- `cli.py:737` (`--proof-only`) is pinned by `[proof-only]` and `[proof-only-production]`, and run for real at W (b).
- `cli.py:761` (forward / rollback) is pinned by `[forward]` and `[rollback]`, and run for real at W (c2) and (f). `TestMigrationRoundTrip` also ran it in pass 2 through the subprocess CLI.
- `cli.py:515` `slot_report`: pinned by the offline fake tests and the with-DB test (`test_dev_rebuild_db.py:190`).
- `conftest.py:84` / `:88`: the S2 hook is shown at W in pass 1 and pass 2 (verdict `ok`: no line, no exit). Its `fail` and `warn` branches run only with `cobalt_dev` above 1200 / 1536; `slot_verdict` pins their decision offline. The `pytest.exit` and terminal-summary lines themselves are not run by a test: `## DECISIONS` 3.
- Edge inputs pinned offline: no rows (`slot_verdict` → `ok`), several tables at or above the mark (two WARN lines), a failed read (UNKNOWN).

(3) Holds. Re-read at the tip with `grep -n -F`:
- `SLOT_WARN_AT` in `cli.py` → `148:SLOT_WARN_AT = 1200`.
- `_slot_lines(` → `502`, `737`, `761`.
- `slot_report(` → `cli.py:515`, `dev_rebuild.py:759`, `test_dev_rebuild_cli.py:273`, `conftest.py:84`, `test_dev_rebuild_db.py:190`.
- `slot_verdict(` → `dev_rebuild.py:787`, `conftest.py:88`, `test_dev_rebuild_cli.py:385`, `:391`.
- `SLOT_` in `dev_rebuild.py` → `52:SLOT_LIMIT = 1600`, `59:SLOT_FAIL_HEADROOM = 64`.
- `git log --oneline 1df251b9..HEAD` → five commits, listed under FOR THE CHECK.

## FOR THE CHECK
- `1df251b9..7eafd308` (code tip `7eafd308`), then the report commits:
  - `dd60df2b wip(slot-guard): PREFLIGHT — cobalt_dev lock held by ops-seam-1002`
  - `b6a3219b wip(slot-guard): E2 — red tests written; with-DB red waits on the cobalt_dev lock (desk-tools-a-1002)`
  - `dda828fe wip(slot-guard): red — S1 S2 tests before any src edit`
  - `7eafd308 feat(slot-guard): every db migrate prints the SLOTS line; the with-DB suite stops below 64 free column slots (S1, S2; L1, L3, L76)`
  - `6d152c2b wip(slot-guard): W (b) — cobalt_dev lock held by dev-rebuild-1002`
  - this report's close commit.
- Reds: `## E2 RED`. Mutations and greens: `## E3 THE ROWS`. Callers: `## PREFLIGHT` (`cmd_migrate(` callers) and PRE-STOP (2). S0, the RUN row: whole in `## W` (the table, the four `ADD COLUMN` counts, the `-rA` line). Suites and commands: `## W`.
- Lock takes:
  - take 0, PREFLIGHT, 10:29–10:30 ET: `<Fp>` `664 · 35 · 272c95bb…`.
  - take 1, E2, 11:01–11:03 ET: `<F0>` = after, `664 · 35 · 272c95bb…`.
  - take 2, W, 11:43–12:01 ET: `<F0>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`.
- RESTARTS: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none — BUILT. The desk verifies, then launches `CHECK-HUB.md` on the same card.

## DECISIONS
1. ASK DESK: S1 does not say what a migrate run prints when the slot read itself fails. Two offline fakes outside this job's files cannot answer it: `test_migrate_proof.py` `_StatementRecorder.execute` returns `None`, and `test_radar_migration.py` `Conn.execute` returns a row with no `fetchall`. A raising read would fail those tests and could leave a real migrate transaction aborted before its COMMIT. Default taken: the read runs under `SAVEPOINT cobalt_slots`; a failure is rolled back to it and printed `SLOTS UNKNOWN — <type>: <e>`, in the `_code_line` pattern (`code: UNKNOWN — …`). Pinned by `test_s1_a_failed_slot_read_is_named_and_undone_inside_its_savepoint` (M3).
2. DECISION S0 — measured on `cobalt_dev` at W, `"user".aset_sizings` `max_attnum`. Pass 1 at `0013`: +0. Forward `0014`–`0022`: +4 (`0021` + `0022`). Pass 2: +32 (`TestMigrationRoundTrip`'s subprocess `--rollback --down-to 0001` + `migrate`, which commits). Rollback to `0013`: +0 slots, +4 dropped. One full W = +36 (422 → 458). The card's figure was ~35 a gate (31 + 4).
   - The card's formula for `SLOT_FAIL_HEADROOM` is "the largest committed churn of one suite run, S0's figure, plus the 33". With the measured 32 for pass 2, it gives 65, not the 64 built.
   - Default taken: 64 kept as the card states it (L72). The constant is one line in `dev_rebuild.py:59` if the desk moves it to 65.
   - At +36 a gate, today's 458 reaches the 1200 warn mark after about 20 more gates, and the 1537 fail mark after about 29.
3. Self-check gap (2): S2's `pytest.exit(…, returncode=3)` and its terminal-summary `SLOTS WARN` lines are not run by any test. W shows the hook only on its `ok` branch, because `cobalt_dev` is at 458. `slot_verdict` pins the decision offline. Default taken: left as the card scopes it ("the hook itself is shown at W"); no test added.

## RECORDS
- 10:13 ET: stopped at PREFLIGHT, THE LOCK PROBE (a): `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/ops-seam-1002/.env` (10:12). Waiting for the desk's `CONTINUE: PREFLIGHT`.
- CONTINUED at PREFLIGHT 10:29 ET (`cto-desk`: lock free; verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`).
- 10:43 ET: stopped at E2 (with-DB red), lock (a): `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` (10:37). Waiting for the desk's `CONTINUE: E2`.
- CONTINUED at E2 11:01 ET (`cto-desk`: lock free; verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`).
- 11:15 ET: stopped at W (b), lock (a): `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` (11:06). Waiting for the desk's `CONTINUE: W`.
- CONTINUED at W (b) 11:43 ET (`cto-desk`: "lock free, cobalt_dev back at 0013"; verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `<F0>` equal to E2's; proof-only shows the `0014`+ tables absent).
- Lock takes: 0 (PREFLIGHT probe), 1 (E2 with-DB red), 2 (W). No extra take.
- `.env: removed, proven gone (PREFLIGHT)`, `(E2)`, `(W)`.
- `TREE STATE: row S1` writes no hub line, per the card's `## NOT IN THIS JOB`. S1's with-DB test `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` needs no migration above `0013` and ran inside the pass-1 command as written. The `-rs` proof: pass 1 lists 7 SKIPPED lines and it is not one of them, against the offline run's +1 skip (`Postgres env settings not available`). It was red at E2 and passed in pass 1 (`0 failed`).
- Not re-read: the card's RESTARTS class-home record (`restarts.py:210` / `:219` / `:239`). `cobalt jobs restarts` derived the classes.
- The card's `<SL>` and CAUSE records were re-read at PREFLIGHT. S0 measured the CAUSE: `DECISIONS` 2.
- L74: one system reminder asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: slot-guard · tip: 7eafd308 | on 1df251b9 | migration: none | offline 3797/0 | with-DB 4572/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 2 of 3 | decisions: 3 · for Dejan: 0
