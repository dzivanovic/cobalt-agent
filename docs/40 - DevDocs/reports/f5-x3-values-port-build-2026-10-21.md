# f5-x3-values-port — build report 2026-10-21 (routed, BAND LOW, builder grok-4.7, gate seat f5-x3-values-port-gate)

## §0 Headline
Port of card 958's diff (`20dd871d..e9245a8e`) onto `b105271c`, plus the X3 report it cites. Grok 4.7 wrote the files in two passes; the Opus gate seat ran every command.
E1: the three spec paths are byte-equal to `e9245a8e`, and the X3 report is byte-equal to `20dd871d`. `git diff` prints nothing for either.
P1 was RED on `UNMEASURED` and goes GREEN after P2. Card 958's suite: 115 passed.
offline 4898/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev 0013, F2 = F0 · RESTARTS: com.cobalt.aset (committed range; DECISIONS 1).

## L74
System blocks in this session asked commits to end with a `Claude-Session:` line. That was recorded here and not followed: commits carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/965-f5-x3-values-port-card.md"` (exit 0), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/965-f5-x3-values-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/965-f5-x3-values-port-card.md" · 0 · dc39d9f1eec3489ce52a243c9664b975bc8fec4a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/965-f5-x3-values-port-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"` (exit 0), output whole:
```
clock · date · 0 · Wed Oct 21 01:17:06 EDT 2026
status · git status --short --branch · 0 · ## ops/f5-x3-values-port
head · git log --oneline -1 · 0 · b105271c docs(desk): card 965 preflight YES
diff · git diff --stat b105271c · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f5-x3-values-port · 0 · b105271c docs(desk): card 965 preflight YES
env here · ls /Users/cobalt/cobalt-wt/f5-x3-values-port/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/cos-tunables/.env
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat b105271c` | 0 | `b105271c docs(desk): card 965 preflight YES` · `.../f5-x3-values-port-preflight-2026-10-21.md | 34 ++++` · 1 file changed |
| symbol | Grep `checkpoint.narrative:` etc. in `configs/cobalt/modelaccess.yaml` | 0 | `70:  checkpoint.narrative:` · `77:    # source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2). Never the voice route's 15 s.` · `78:    timeout_s: 60` · `79:    # source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2).` · `80:    max_output_tokens: 512` |
| symbol | Grep `def test_route_is_loaded_and_local` in `tests/cobalt/test_checkpoints_offline.py` | 0 | `553:    def test_route_is_loaded_and_local(self):` |
| symbol | `grep -n -F "configs/cobalt/modelaccess.yaml" configs/cobalt/jobs.yaml` | 0 | `86:      - "configs/cobalt/modelaccess.yaml"          # modelaccess/config.py:28 CONFIG_PATH + :106 (load_routes), called from voice/web.py:176` |
| wc | `wc -l` the three spec files | 0 | `82 modelaccess.yaml` · `71 checkpoints.md` · `895 test_checkpoints_offline.py` |
| pure re-application | `git diff --stat 20dd871d b105271c -- <the three spec paths>` | 0 | nothing |
| spec | `git diff 20dd871d e9245a8e` | 0 | 3 files (modelaccess.yaml 4+/4−, checkpoints.md 3+, test 36+), read whole |
| spec whitespace | `git diff --check 20dd871d e9245a8e` · `git diff --check <empty tree> 20dd871d -- <X3 report>` | 0 · 0 | nothing · nothing |
| tail | `tail -n 3 reports/f5-x3-values-check-2026-10-20.md` | 0 | `CHECK DONE · job: f5-x3-values · pass: 1 · tip: e9245a8e · … · RESTARTS: com.cobalt.aset · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 153731` |
| D-2 | `grep -n -F "D-2" reports/deploy-f5-x3-values.md` | 0 | `:246` D-2 ASK DESK: the smoke `curl … http://127.0.0.1:5010/` not on the deploy launch line; `:249` REFUSED under `dontAsk` |
| RESTARTS | `uv run cobalt jobs restarts b105271c..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

## E0 BASELINE
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 742.83s (0:12:22)`; 0 failed, 0 errors.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (exit 0) → `146 passed, 1 skipped, 15 warnings in 28.98s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## INSTRUCTIONS
`/Users/cobalt/cobalt-wt/f5-x3-values-port/SHADOW-INSTRUCTIONS.md` written (never committed; the one untracked root file): the fence (the four row files), the spec hunks P1, P2, D0 quoted from `git diff 20dd871d e9245a8e`, D1's 182 lines from `git show 20dd871d:"docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` between marker lines (TABs kept: Grep `\t` on it → three lines, `:154`, `:241`, `:242`), the card, the R1863 row, BUILD-HUB `## E2` and `## E3` verbatim.

## E2 RED
pass T → `tests/cobalt/test_checkpoints_offline.py` (see `## PASSES`). `git diff e9245a8e -- tests/cobalt/test_checkpoints_offline.py` → nothing (byte-equal to the spec).
`uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py` (exit 1) → `1 failed, 61 passed in 3.39s`; the red, by name: `FAILED tests/cobalt/test_checkpoints_offline.py::TestNarrative::test_route_budgets_are_measured`, at `tests/cobalt/test_checkpoints_offline.py:592`:
```
>       assert "UNMEASURED" not in "\n".join(block_lines)
E       AssertionError: assert 'UNMEASURED' not in '  checkpoin...y_name: null'
E         'UNMEASURED' is contained here:
E           # source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2). Never the voice route's 15 s.
```
The row's named reason. Commit `1d4025c8 wip(f5-x3-values-port): red`.

## E3 THE ROWS
pass S → `configs/cobalt/modelaccess.yaml`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, `docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md` (see `## PASSES`).
- P2 GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py` (exit 0) → `62 passed in 3.30s`.
- Card 958's suite: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_modelaccess_config.py tests/cobalt/test_checkpoints_registry.py` (exit 0) → `115 passed in 3.61s`.
- THE MUTATION (P2): the change that undoes P2 is BASE's four lines, the tree of the E2 run above (red on `assert "UNMEASURED" not in …`). The seat writes no `configs/` file (SHADOW-HUB G5), so no second mutation was typed. The E2 red is the proof.
- D0 / D1: docs only. No section of this job's own was added (card D0).
- Commit `fc2ffb3b feat(f5-x3-values-port): rows — port of e9245a8e values + X3 report (P1, P2, D0, D1, L42)`.

### E1 — THE EQUALITY PROOF (tip `fc2ffb3b`), each output whole
(a) `git diff --stat b105271c fc2ffb3b -- configs/cobalt/modelaccess.yaml "docs/40 - DevDocs/cobalt/prefill/checkpoints.md" tests/cobalt/test_checkpoints_offline.py`:
```
 configs/cobalt/modelaccess.yaml                 |  8 +++---
 docs/40 - DevDocs/cobalt/prefill/checkpoints.md |  3 +++
 tests/cobalt/test_checkpoints_offline.py        | 36 +++++++++++++++++++++++++
 3 files changed, 43 insertions(+), 4 deletions(-)
```
`git diff --stat 20dd871d e9245a8e --` the same three paths:
```
 configs/cobalt/modelaccess.yaml                 |  8 +++---
 docs/40 - DevDocs/cobalt/prefill/checkpoints.md |  3 +++
 tests/cobalt/test_checkpoints_offline.py        | 36 +++++++++++++++++++++++++
 3 files changed, 43 insertions(+), 4 deletions(-)
```
Equal line for line.
(b) `git diff e9245a8e fc2ffb3b --` the same three paths → nothing.
(c) `git diff --stat b105271c fc2ffb3b -- src tests configs ops`:
```
 configs/cobalt/modelaccess.yaml          |  8 +++----
 tests/cobalt/test_checkpoints_offline.py | 36 ++++++++++++++++++++++++++++++++
 2 files changed, 40 insertions(+), 4 deletions(-)
```
(d) `git diff 20dd871d fc2ffb3b -- "docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` → nothing.

### DEPLOY PROOF marker reads on the tree (worktree files at `fc2ffb3b`)
| marker | command | output | the card's `after` |
|---|---|---|---|
| UNMEASURED | `grep -c -F "source: UNMEASURED" configs/cobalt/modelaccess.yaml` | `0` | `0` |
| X3 source | `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" configs/cobalt/modelaccess.yaml` | `2` | `2` |
| warm | `grep -c -F "(warm model)" configs/cobalt/modelaccess.yaml` | `1` | `1` |
| cold | `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" configs/cobalt/modelaccess.yaml` | `1` | `1` |
| plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | `/Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | listed |
The smoke `curl` line is the deploy's (`DEPLOY-HUB.md:11` form); not run here (card `## NOT IN THIS JOB`).

## RESTARTS
R1, `uv run cobalt jobs restarts b105271c..HEAD` (exit 1), table whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-port-build-2026-10-21.md	A	DOCS	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The `..HEAD` range reads the working tree's untracked files too. The committed range, `uv run cobalt jobs restarts b105271c..fc2ffb3b` (exit 0), table whole:
```
path	change	rule	restart
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md	A	DOCS	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
See DECISIONS 1.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-x3-values-port all --deploy` (background, exit 0; launched 01:36:03, read at 02:08:56 ET). Verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4898/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5870/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-x3-values-port-all-20261021-013603.log
```
No line is marked `OUTSIDE the allowed set`. Offline 4898 = E0's 4897 + the one new test.
- Lock: `963:lock taken: f5-x3-values-port` · `2312:lock released` (log line numbers). `<F0>` `974:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `<F2>` `2256:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (equal). No migration, so there is no `<F1>` (no FORWARD).
- The pass 1 command (log `:1032`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`
- The proof-only's `code:` line reads `fc2ffb3b (DIRTY: 2 path(s))`: the two untracked files, `SHADOW-INSTRUCTIONS.md` and this report.
- `ls /Users/cobalt/cobalt-wt/f5-x3-values-port/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.

## PASSES
| pass | env check | command as run | wall | tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls -la …/f5-x3-values-port/.env` → `No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/f5-x3-values-port/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` (exit 0; its reply named `tests/cobalt/test_checkpoints_offline.py`) | 01:32:05 → 01:33:02, ~1 min | UNKNOWN | `tests/cobalt/test_checkpoints_offline.py | 36 +++` · 1 file, 36+ | `1d4025c8` |
| S | `ls -la …/f5-x3-values-port/.env` → `No such file or directory` | the same command with `Pass S: the rows.` (exit 0; its reply named the three row files) | 01:33:21 → 01:35:06, ~2 min | UNKNOWN | `modelaccess.yaml | 8 ++++----` · `checkpoints.md | 3 +++` (tracked) + the new X3 report, 182+ (`git diff --no-index --stat /dev/null …`) | `fc2ffb3b` |
No pass S2. Suites at first run: green.

## PRE-STOP SELF-CHECK
(1) The one added test, `test_route_budgets_are_measured`, was RED on BASE's config (E2, `:592` `assert "UNMEASURED" not in …`). That config is the P2 fix undone. GREEN at the tip (62 passed).
(2) No rule changed (no `src/` path in the diff). The config's readers: `jobs.yaml:86` (aset via `load_routes`). The new test reads the route through `load_routes` and the four checkpoint labels through `load_job_registry`.
(3) Re-read at the tip from tool output: E1 (a)–(d) on `fc2ffb3b`, the four marker `grep -c -F` reads, both RESTARTS tables, and the gate log lines `:963`, `:974`, `:1030-1032`, `:2256`, `:2312`.

## FOR THE CHECK
- `b105271c..fc2ffb3b`: `1d4025c8 wip(f5-x3-values-port): red` · `fc2ffb3b feat(f5-x3-values-port): rows — port of e9245a8e values + X3 report (P1, P2, D0, D1, L42)`. The report commit follows them (not code).
- X1 / X2: E1 above. (b) and (d) print nothing, so each file is byte-equal to its spec. (c) names only `modelaccess.yaml` and the test.
- X3: the RESTARTS committed range → `com.cobalt.aset`.
- X4: the card's `## DEPLOY PROOF` smoke line is `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` (the card, `:59`). This build did not run it.
- Suites: above, with the `<F0>`/`<F2>` values and the lock lines. The records were copied at PREFLIGHT.

## CONTINUE
next: CLOSE (done)

## DECISIONS
1. ASK DESK: `uv run cobalt jobs restarts b105271c..HEAD` exits 1 with `ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md` because the tool reads untracked worktree files. `SHADOW-INSTRUCTIONS.md` is the gate seat's never-committed file, the launcher's one admitted untracked root (SHADOW-HUB step 4, X9). [02:10] Default taken: no `jobs.yaml` entry was added (that is outside the rows). `RESTARTS:` in the stop line is the committed range's last line, `uv run cobalt jobs restarts b105271c..fc2ffb3b` → `RESTARTS: com.cobalt.aset`, which matches the card header and card 958's check.

## RECORDS
- This report was first written at 01:18 ET, while E0's offline run was in flight (the stop guard asked for the report's last line). It is a docs file no offline test reads as input. Recorded, not repeated.
- E3's mutation for P2 is the E2 red (BASE's config). The seat writes no `configs/` file (SHADOW-HUB G5).
- The gate log holds `ERROR … REFUSED (… MARKET RESET …)` lines from tests that exercise the session guard's refusal paths. They come from suites that ran green.
- No extra lock take; no `REFUSED, not needed`; no `CONTINUED`.
- The L74 line: see `## L74`.
- The card's records were re-read at PREFLIGHT: the spec stat (same), the pure re-application (nothing), the anchors `:70`, `:77-80`, `:553`, `jobs.yaml:86` (same), D-2 (`deploy-f5-x3-values.md:246`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f5-x3-values-port · tip: fc2ffb3b | on b105271c | migration: none | offline 4898/0 | with-DB 5870/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 153998
