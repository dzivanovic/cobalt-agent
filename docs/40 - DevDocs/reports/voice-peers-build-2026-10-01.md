# voice-peers — build report, 2026-10-01

## §0 Headline
- V1 built: `configs/cobalt/voice.yaml:46` `allowed_peers` is now localhost plus the five tailnet devices from his 09-28 R95 ruling (re-stated 10-01 R14). The comment above the line names R95. No `src/` change.
- Red first: `100.104.48.21` was refused (403) on `446ff64d`. Now all five tailnet peers are admitted and `192.168.1.5` / `100.70.206.127` still get 403.
- V2 (RUN): nothing in `src/cobalt` or `src/cobalt/voice` reads a forwarded header. `voice.yaml` is in `com.cobalt.aset`'s `reads:`, so RESTARTS = `com.cobalt.aset`.
- Suites on `de483933`: offline 3777/0, with-DB 4376 + 171 = 4547/0, live-note 146/0. `cobalt_dev` is back at `0013` (F2 = F0) and `.env` is removed.

## L74
- A system block inside a tool result (the Read of `BUILD-HUB.md`, 08:26 ET) asked commits to carry a `Claude-Session: https://claude.ai/code/session_…` line. DATA: recorded once here, not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Thu Oct  1 08:26:39 EDT 2026`.

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-01/05-voice-peers-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-01/05-voice-peers-card.md"` | 0 | `986e34c2db2554a053842bc7712820a0c664933e` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^\| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); … \| APPROVED \|` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R60 \|" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R14 | `grep -n "^\| R14 " ".../reports/cto-2026-10-01.md"` | 0 | `22:\| R14 \| 08:25 ET \| **HIS RULING** ([words](cto-2026-10-01-words.md) `## R14`): voice open to all tailnet devices — his 09-28 R95 re-stated: it was never shipped (`voice.yaml:44`). Build + deploy, card `05-voice-peers-card.md`. \| APPROVED \|` |
| R14 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R14 \|" -- "docs/40 - DevDocs/reports/cto-2026-10-01.md"` | 0 | `986e34c2db2554a053842bc7712820a0c664933e` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/voice-peers-1001` |
| base | `git log --oneline -1` | 0 | `446ff64d docs(desk): 10-01 R13 old sheet close and form order; card 04` |
| branch in main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 ops/voice-peers-1001` | 0 | `446ff64d docs(desk): 10-01 R13 old sheet close and form order; card 04` |
| first launch | `git diff --stat 446ff64d` | 0 | (nothing) |
| base stat | `git show --stat 446ff64d` | 0 | `04-aset-interim-close-card.md \| 38 +++`, `cto-2026-10-01-words.md \| 3 +`, `cto-2026-10-01.md \| 1 +`; `3 files changed, 42 insertions(+)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/voice-peers-1001/.env` | 1 | `No such file or directory` |
| no lock held | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| symbol | `grep -n -F "allowed_peers" configs/cobalt/voice.yaml` | 0 | `44:  allowed_peers: ["127.0.0.1", "::1"]` |
| symbol | `grep -n -F "def peer_gate" src/cobalt/voice/web.py` | 0 | `70:def peer_gate(request: Request) -> None:` |
| callers | `grep -rn -F "peer_gate" src` | 0 | `web.py:70` def; `web.py:95` `/turn`; `web.py:130` `/confirm`; `web.py:135` `/cancel`; `web.py:152` `/status`; `web.py:311` `__all__` |
| symbol | `grep -n -F "_ip_literals" src/cobalt/voice/config.py` | 0 | `67:    def _ip_literals(cls, v: list[str]) -> list[str]:` (decorator `@field_validator("allowed_peers")` at `:65`, Read) |
| callers | `grep -rn -F "load_voice_config(" src` | 0 | `voice/turn.py:111`, `voice/web.py:59`, `voice/config.py:120` (def), `voice/cli.py:56` |
| wc | `wc -l configs/cobalt/voice.yaml tests/cobalt/test_voice_config.py tests/cobalt/test_voice_web.py` | 0 | `44`, `364`, `295` |
| READ | `grep -n -E "^\| R9[45] " ".../cto-2026-09-28.md"` | 0 | `102:\| R94 \| 16:23 ET \| **P-HIS — voice works from every Tailscale device: Badass, MSI, Cobalt, phone** …`; `103:\| R95 \| 16:25 ET \| **P-HIS — "yes change it as well as fedor. all tailscale machines included"** (words `## R95`): `configs/cobalt/voice.yaml` `allowed_peers` = localhost + all five tailnet devices; shipped in tonight's window (L42, L43). \| APPLIED: areas/cobalt-product-definition.md 16:28 \|` |
| READ | `grep -n -A 8 "^## R95" ".../cto-2026-09-28-words.md"` | 0 | `85-> correct listing and yes change it as well as fedor. all tailscale machines included` |
| tail | `tail -n 3 ".../cto-2026-09-28.md"` | 0 | last line `HANDOVER: predecessor f030d47a → successor e41f7813 at 22:38 ET` |
| tail | `tail -n 3 ".../cto-2026-09-28-words.md"` | 0 | last line `21:52 ET, desk chat, on R169 (A — let `60` run unwatched / B — stop it): "A"` |
| restarts | `uv run cobalt jobs restarts 446ff64d..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

Card `## RECORDS`, copied: `tailscale status`, 2026-10-01 08:2x ET: cobalt 100.70.206.126 (macOS), badass 100.73.178.42 (windows, offline 18 h), dejans-s25 100.66.219.53 (android), fedora 100.104.48.21 (linux), msi 100.82.85.27 (windows). Not re-readable by this list (`tailscale` is not a listed string); the five addresses are used exactly as the card gives them.

`<FP>`, typed exactly:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

LOCK PROBE (take 0, 08:27 ET): (a) `no matches found`; (b) `cp`, then `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 08:27 /Users/cobalt/cobalt-wt/voice-peers-1001/.env`. `<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → `36 table(s) probed on cobalt_dev`; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` absent (`-`); `aset_sizings 1 0824685c130da3c7cb7f0e76191a6819`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 446ff64d (clean)`. No `CHANGED`; the tables above `0013` absent: `0013`. (d) `rm`, `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (PREFLIGHT)`.

PROVEN BY FIRST REAL USE: `uv run pytest *`, `COBALT_LIVE_VAULT_ROOT=… uv run pytest *` (E0), `git add *` / `git commit *` (E2), `COBALT_ENV=dev uv run pytest *` and `… db migrate` (W (c), (c2)), `… --rollback --down-to 0013` (W (f)).

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3769 passed, 673 skipped, 1 xfailed, 25 warnings in 616.80s (0:10:16)`, exit 0.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.97s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, and it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written (no `src/` edit, no with-DB test):
- `tests/cobalt/test_voice_config.py:65` `test_v1_allowed_peers_are_localhost_and_the_five_tailnet_devices`: the loaded config holds each of the seven literals, equals `RULED_PEERS`, every entry parses with `ipaddress.ip_address`, and the comment line above the key carries `# source:` and `R95`.
- `tests/cobalt/test_voice_config.py:54`, the existing `test_committed_voice_config_loads_with_the_dev_defaults`: its pin `== ["127.0.0.1", "::1"]` now reads `== RULED_PEERS`. It is the same value the row rules, and leaving the old pin would make it the row's own regression.
- `tests/cobalt/test_voice_web.py:85` `test_v1_every_tailnet_device_is_an_allowed_socket_peer[<5 hosts>]`: each tailnet socket peer gets `GET /voice/status` → 200 through `peer_gate`.
- `tests/cobalt/test_voice_web.py:93` `test_v1_a_near_miss_or_lan_peer_is_still_refused[192.168.1.5, 100.70.206.127]`: the negative control, 403 `not an allowed peer`.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_voice_config.py tests/cobalt/test_voice_web.py` → `7 failed, 96 passed in 1.14s`. The first line of each red:
- `test_committed_voice_config_loads_with_the_dev_defaults`: `AssertionError: assert ['127.0.0.1', '::1'] == ['127.0.0.1',...4.48.21', ...]`
- `test_v1_allowed_peers_are_localhost_and_the_five_tailnet_devices`: `AssertionError: 100.70.206.126` / `assert '100.70.206.126' in ['127.0.0.1', '::1']`
- `test_v1_every_tailnet_device_is_an_allowed_socket_peer[100.104.48.21]`: `AssertionError: {"detail":"voice: peer '100.104.48.21' is not an allowed peer"}` / `assert 403 == 200`. This is the row's named red.
- The same `403 == 200` for `[100.70.206.126]`, `[100.73.178.42]`, `[100.66.219.53]` and `[100.82.85.27]`.
- The negative control `test_v1_a_near_miss_or_lan_peer_is_still_refused[*]` PASSES (2 of the 96).

Commit `319a25cd wip(voice-peers): red — V1 the seven ruled peers, fedora admitted, near-miss refused`.

V2 RUN (read only; it asserts nothing). The output, whole:
- `grep -rn -F "X-Forwarded-For" src/cobalt` → exit 1, no output.
- `grep -rn -i -F "forwarded" src/cobalt/voice` → exit 1, no output.
- `grep -rn -F "request.headers" src/cobalt/voice` → exit 1, no output.
- `grep -rn voice.yaml src configs` →
```
src/cobalt/voice/config.py:1:"""`configs/cobalt/voice.yaml` — schema, loader, and the FINAL §5 path refusals.
src/cobalt/voice/config.py:32:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "voice.yaml"
src/cobalt/voice/registry.py:1:"""The voice agent as a REGISTRY ENTRY (L16): `configs/cobalt/agents/voice.yaml`.
src/cobalt/voice/registry.py:23:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "agents" / "voice.yaml"
Binary file src/cobalt/voice/__pycache__/config.cpython-314.pyc matches
Binary file src/cobalt/voice/__pycache__/registry.cpython-314.pyc matches
Binary file src/cobalt/voice/__pycache__/transcribe.cpython-314.pyc matches
src/cobalt/voice/transcribe.py:5:chose (`configs/cobalt/voice.yaml`), loaded from `model_dir` with
configs/cobalt/jobs.yaml:84:      - "configs/cobalt/voice.yaml"                # voice/config.py:32 CONFIG_PATH + :120 (load_voice_config); cached per process in voice/web.py:59 _CONFIG, so a change reaches the sheet only by restart
configs/cobalt/jobs.yaml:85:      - "configs/cobalt/agents/voice.yaml"         # voice/registry.py:23 CONFIG_PATH + :85 (load_agent), called from voice/web.py:176
```
- `configs/cobalt/jobs.yaml:39` `- label: com.cobalt.aset`, `kind: resident`; that `reads:` list starts at `:67` and holds `:84`. `voice/web.py:13-16` (Read): "No header is ever read as the allow key."

What V2 shows: the headers are not read, and the deploy's restart class is `com.cobalt.aset`. That matches the RESTARTS table below. Nothing for `## DECISIONS`.

## E3 THE ROWS
V1, `configs/cobalt/voice.yaml` (re-read `:40-45` before the edit). `:44` became `:46`, with two comment lines above it: the device names, then `# source: his ruling cto-2026-09-28 R95 "…" (re-stated 2026-10-01 R14)`. No `src/` change.
- Green: `tests/cobalt/test_voice_config.py tests/cobalt/test_voice_web.py` → `103 passed in 1.08s`.
- MUTATION 1 (undoes the fix): `"100.104.48.21"` removed from the list → `3 failed, 100 passed in 1.07s`. First failing line: `tests/cobalt/test_voice_config.py:54: AssertionError: assert ['127.0.0.1',...100.82.85.27'] == ['127.0.0.1',...4.48.21', ...]`. Also red: `test_voice_config.py:75: AssertionError: 100.104.48.21` and `test_voice_web.py:89: AssertionError: {"detail":"voice: peer '100.104.48.21' is not an allowed peer"}`. Undone with Edit.
- MUTATION 2 (breaks the negative control): `"100.70.206.127"` appended → `test_voice_web.py`: `1 failed, 39 passed in 0.81s`, `test_voice_web.py:96: assert (200 == 403)`. Undone with Edit.
- `git diff --stat` → `configs/cobalt/voice.yaml | 4 +++-` (the fix alone). Green again: `103 passed in 1.00s`.
- DevDocs: `docs/40 - DevDocs/cobalt/voice/config.md` gained `## 2026-10-01 — voice-peers` with one line.
- Commit `de483933 fix(voice-peers): allowed_peers = localhost + the five tailnet devices (V1, L1 L42 L77; R95 / R14)`.

V2: RUN row, nothing built (see E2).

## RESTARTS
`uv run cobalt jobs restarts 446ff64d..HEAD` →
```
path	change	rule	restart
configs/cobalt/voice.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/voice/config.md	M	DOCS	-
docs/40 - DevDocs/reports/voice-peers-build-2026-10-01.md	A	DOCS	-
tests/cobalt/test_voice_config.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `de483933`. TREE STATE `unchanged`: the diff adds no with-DB test and no migration.
- (a) Offline (background) → `3777 passed, 673 skipped, 1 xfailed, 25 warnings in 598.85s (0:09:58)`, exit 0 → `<p>` = 3777. Added tests: 1 + 5 + 2 = 8 (3769 → 3777).
- (b) Lock take 1 at 08:50:43: (a) `no matches found`; (b) `cp`, then `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 08:50 /Users/cobalt/cobalt-wt/voice-peers-1001/.env`. **`<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.** `--proof-only` → 36 tables, with `drc_*`, `legs`, `prediction_records` and `voice_turns` `-`; `NOTHING WAS APPLIED`; no `CHANGED`; `code: de483933 (DIRTY: 1 path(s))` (this report). Level `0013`.
- (c) PASS 1, executed byte for byte as the hub's pass-1 command (no deselect added; this build has no with-DB test):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
→ `4376 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 718.27s (0:11:58)`, exit 0 → `<d1>` = 4376. The seven SKIPPED lines:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0011`, `0013`, `0014` … `0022` applied in order. `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records` and `voice_turns` are `CREATED`; every other table is `OK`; `content UNCHANGED on every table`; no `CHANGED`. **`dev forward: APPLIED 09:03:30`**. **`<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.**
- (c3) PASS 2, executed byte for byte as the hub's pass-2 command (nothing added):
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
→ `171 passed, 1 deselected, 5 warnings in 227.77s (0:03:47)`, exit 0. There are no SKIPPED lines, and `grep -c -E "^(FAILED|ERROR)"` → `0`. `<d2>` = 171; `<d>` = 4376 + 171 = **4547**. This build adds no with-DB test id.
- (c3r) `ls -la …/voice-peers-1001/.env` → listed. This build's tests write no constructed ticker, so the IN-list query has no tickers to name. Instead: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) AS aset_sizings_rows FROM aset_sizings"` → `1`, the same row count `--proof-only` showed at take 0 and at (b) (`aset_sizings 1 0824685c…`, unchanged through forward and rollback).
- (c4) Not applicable: no migration added.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` rollbacks applied, newest first. The eight tables are `DROPPED`, the rest `OK`, `content UNCHANGED on every table`. **`<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → `cobalt_dev: 0013 — F2 = F0`.** Lock (d) at 09:08:07: `rm`; `ls …/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found`. `.env: removed, proven gone (W)`.
- (e) Live-note, `.env` absent → `146 passed, 1 skipped, 15 warnings in 27.82s`. The skip is `test_replay_line.py:266 … COBALT_TEST_LIVE_DRC …`, not `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. The E2 reds on `446ff64d` are quoted above: `test_committed_…_dev_defaults`, `test_v1_allowed_peers_…` and the five `test_v1_every_tailnet_device_…`. The E3 mutation 1 reds (`:54`, `:75`, `web.py:89 [100.104.48.21]`) are quoted too. The negative control `test_v1_a_near_miss_or_lan_peer_is_still_refused` passed at E2 and went red under mutation 2 (`test_voice_web.py:96: assert (200 == 403)`). No test stayed green under its mutation.
(2) Entry paths. `peer_gate` callers (PREFLIGHT, re-run at tip): `web.py:95` `/turn`, `:130` `/confirm`, `:135` `/cancel`, `:152` `/status`. Every one is the same `Depends(peer_gate)` reading the one `get_config().allowed_peers`. Tailnet admission is pinned through `/status` (`test_v1_every_tailnet_device_…`). The existing `test_every_voice_route_is_gated` pins that `/status`, `/confirm` and `/cancel` go through the gate, and the existing `test_any_other_peer_is_a_named_403` pins it for `/turn`. Of the `load_voice_config(` callers, `voice/turn.py:111` and `voice/cli.py:56` do not read `allowed_peers`; `web.py:59` is the gate's own source, pinned. The validator `config.py:65-73` is pinned by the new test's `ipaddress.ip_address` pass and by the existing `test_allowed_peers_must_be_ip_literals`. The edge inputs are the LAN peer and the near-miss tailnet peer `100.70.206.127`, both pinned.
(3) Re-read at the tip with `git show de483933:configs/cobalt/voice.yaml` (`:44-46` as quoted), `grep -n -F "allowed_peers" configs/cobalt/voice.yaml` → `46:`, `grep -n -F "def test_v1_" …` → `test_voice_config.py:65`, `test_voice_web.py:85`, `:93`, `grep -n -F "Depends(peer_gate)" src/cobalt/voice/web.py` → `95`, `130`, `135`, `152`, and `git log --oneline 446ff64d..HEAD` → two commits.

## FOR THE CHECK
- Range `446ff64d..de483933`: `319a25cd wip(voice-peers): red — V1 the seven ruled peers, fedora admitted, near-miss refused`, then `de483933 fix(voice-peers): allowed_peers = localhost + the five tailnet devices (V1, L1 L42 L77; R95 / R14)`.
- V1: the reds are under E2, the mutation runs and greens under E3. The caller greps are under PREFLIGHT and in self-check (2).
- V2: the RUN output, whole, is under E2.
- The suites and their executed commands are under W. Offline is 3777/0, with-DB 4547/0 (pass 1 4376 + pass 2 171), live-note 146/0.
- Fingerprints: take 0 (08:27) `<Fp>` = 664 · 35 · `272c95bb…`. Take 1 (08:50:43 → 09:08:07): `<F0>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`, `<F1>` = 893 · 44 · `126f2d6983fa59f9d0eaaff7da7dd29c`, `<F2>` = `<F0>`.
- The RESTARTS table is under RESTARTS. The card's records copied at PREFLIGHT are under PREFLIGHT.

## CONTINUE
next: none (CLOSE done)

## DECISIONS
none

## RECORDS
- Lock takes: take 0 at PREFLIGHT (08:27, reads only) and take 1 at W (08:50:43–09:08:07). There was no E2 take, because no with-DB red exists, and no extra take.
- `.env: removed, proven gone (PREFLIGHT)`; `.env: removed, proven gone (W)`.
- `cobalt_redactions` on `cobalt_dev` grew from 211 rows (take 0 and W (b) `--proof-only`) to 212 at the forward's before-probe. It then held at 212 through forward and rollback (`OK`). No step of this build writes that table. Earlier reports name the same outside writer: `f15-p1-build-2026-09-30.md:375` and `s3-exits-c1-fix-r2-check-2026-09-28.md:65` ("R61's OWED item"). The fingerprint does not see rows.
- The card's `## RECORDS` (`tailscale status` 08:2x ET, the five addresses) were used as given. `tailscale` is not a listed string, so the builder could not re-read them.
- `--proof-only` prints no level number. `0013` is read off the tables of `0014`–`0022` showing `-`, as at `f15-p1-build-2026-09-30.md:76`.
- The L74 block is recorded under `## L74`. No commit carries a `Claude-Session:` line.
- No `REFUSED, not needed` line and no `CONTINUED` line.
- CLOSE's last lock check, after the report commit `3f67947a`: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 09:10 /Users/cobalt/cobalt-wt/devdb-lock-1001/.env`. That is another worktree's take at 09:10, after this build released at 09:08:07; it is not this build's file. `ls /Users/cobalt/cobalt-wt/voice-peers-1001/.env` → `No such file or directory`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: voice-peers · tip: de483933 | on 446ff64d | migration: none | offline 3777/0 | with-DB 4547/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
