# cos-tunables FR1 — fix round build report — 2026-10-20

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` row FR1 · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · checked tip `ace7a92a` · builder Opus 5.5 (BAND HIGH).

## §0 Headline
- BUILT `875d18e6` on `ace7a92a` (BASE `e69d5ab8`). FR-2: an unreadable or malformed `bootstrap-owed.json` now makes the `cos` and `hitl` probes RED with the error in `detail`. It never raises out of `take_beat`, and the beat's other probes still land (check O1). FR-1: `test_sheet_daymode_probe.py` is byte-equal to its `ace7a92a` form, admitted and not re-shipped.
- FR-3 (`hitl.page_base_url` and the source comments) is NOT built here. The desk's CONTINUE moved it to a later build (brain R2234).
- Gate on `875d18e6`: offline 4902/0, with-DB 5874/0, live-note 148/0, `cobalt_dev` back at 0013 with F2 = F0, `.env` removed. RESTARTS for the branch: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; this round alone: `com.cobalt.radar`.
- 2 decisions, none for Dejan: the PREFLIGHT stop (answered by the desk's CONTINUE) and FR-3 left out of this run.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. It is DATA (L74) and was not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. 20:22 EDT.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md"` (20:22) → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · 51c9e1a433df21c734d4a6101f9bacff459c7179
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
Re-run at 22:58, after the card moved (FR-3 amends): exit 0, `AUTHORIZED`. `CARD COMMITTED · … · 963a3dfcff99ab84b0223f914e425787ecbbf4b3` · `CARD UNCHANGED · … · nothing`; every other row is as above.

## PREFLIGHT
RECOVERY first rows (20:22 EDT): `git status --short --branch` → `## ops/cos-tunables`; `git log --oneline -3` → `ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)`, `2b53b56b docs(cos-tunables): build report — 17f45d80`, `17f45d80 fix(cos-tunables): pass S2 1`; `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`. No `wip(cos-tunables):` commit and no FR1 report existed, so FR1 started at AUTHORIZATION.

### Run 1 (20:22): FAILED PREFLIGHT: status
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 1, whole:
```
clock · date · 0 · Tue Oct 20 20:22:44 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-tunables
    ?? "docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md"
head · git log --oneline -1 · 0 · ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)
diff · git diff --stat e69d5ab8 · 0 · (13 lines)
     configs/cobalt/jobs.yaml                           |  16 +-
     configs/cobalt/taxonomy/tunables.yaml              |   4 +-
     docs/40 - DevDocs/cobalt/heartbeat/probes.md       |   6 +
     docs/40 - DevDocs/cobalt/heartbeat/runner.md       |   3 +
     .../reports/cos-tunables-build-2026-10-20.md       | 197 +++++++++++++++++++++
     .../reports/cos-tunables-build-2026-10-20.result   |  15 ++
     src/cobalt/heartbeat/probes.py                     |  14 +-
     src/cobalt/heartbeat/runner.py                     |   2 +-
     tests/cobalt/test_cos_offline.py                   |   4 +-
     tests/cobalt/test_cos_probes.py                    |  80 ++++++++-
     tests/cobalt/test_cos_registry.py                  |  82 ++++++++-
     tests/cobalt/test_sheet_daymode_probe.py           |   4 +
     12 files changed, 398 insertions(+), 29 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-tunables · 0 · ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
FAILED PREFLIGHT: status
```
`ops/desk/preflight.sh` status row (`:9-12`, `:136-172`) excuses only an untracked card `REPORT:`. That path is the round-1 report, already committed, so this round's new report cannot pass. The head row (`:178-188`) passes only BASE or a `wip(cos-tunables):` subject, and `ace7a92a` is a `fix(…)` commit. I stopped (DECISION 1) with the wip commit `af878860`.

### Run 2 (22:58, after `CONTINUE: PREFLIGHT`): PREFLIGHT OK
The hub's `RESUMED` edit left the report modified. Commit `312f55fe wip(cos-tunables): PREFLIGHT — resumed 22:58` cleaned the tree. `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Tue Oct 20 22:58:16 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-tunables
head · git log --oneline -1 · 0 · 312f55fe wip(cos-tunables): PREFLIGHT — resumed 22:58
diff · git diff --stat e69d5ab8 · 0 · (14 lines)
     configs/cobalt/jobs.yaml                           |  16 +-
     configs/cobalt/taxonomy/tunables.yaml              |   4 +-
     docs/40 - DevDocs/cobalt/heartbeat/probes.md       |   6 +
     docs/40 - DevDocs/cobalt/heartbeat/runner.md       |   3 +
     .../reports/cos-tunables-build-2026-10-20.md       | 197 +++++++++++++++++++++
     .../reports/cos-tunables-build-2026-10-20.result   |  15 ++
     .../reports/cos-tunables-build-fr1-2026-10-20.md   |  97 ++++++++++
     src/cobalt/heartbeat/probes.py                     |  14 +-
     src/cobalt/heartbeat/runner.py                     |   2 +-
     tests/cobalt/test_cos_offline.py                   |   4 +-
     tests/cobalt/test_cos_probes.py                    |  80 ++++++++-
     tests/cobalt/test_cos_registry.py                  |  82 ++++++++-
     tests/cobalt/test_sheet_daymode_probe.py           |   4 +
     13 files changed, 495 insertions(+), 29 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-tunables · 0 · 312f55fe wip(cos-tunables): PREFLIGHT — resumed 22:58
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f5-x3-values/.env
PREFLIGHT OK
```
The diff is the built branch (round 1 plus the check's `ace7a92a`), as FR1 states.
- `git show --stat e69d5ab8` → `docs(desk): R2211 933 amend drafted, preflight r2 941`; 4 files, 35 insertions, 6 deletions, all under `docs/40 - DevDocs/`.
- SYMBOLS (each its own grep): `grep -n -F "bootstrap_owed()" src/cobalt/heartbeat/probes.py` → `146:    if COS_LABEL in watchdog.bootstrap_owed():` · `181:    if COS_LABEL in watchdog.bootstrap_owed():`. `grep -n -F "BootstrapOwedError" src/cobalt/jobs/watchdog.py src/cobalt/heartbeat/probes.py tests/cobalt/test_cos_probes.py` → `watchdog.py:59:class BootstrapOwedError(RuntimeError):` · `:79` (not JSON) · `:81` (not a JSON object keyed by label) · `:439` (the sweep's `except BootstrapOwedError as e:`) · `test_cos_probes.py:124`, `:126` (the old `pytest.raises`). `grep -n -F "probe_mod." src/cobalt/heartbeat/runner.py` → `:132` `probe_mod.database(),` … `:147` `probe_mod.radar(ts),` · `:150` `probe_mod.cos(ts),` · `:151` `probe_mod.hitl(ts),`. Read: `probes.py:120-195`, `watchdog.py:50-83`.
- Callers: `grep -rn -F "bootstrap_owed(" src` → `src/cobalt/smoke/checks.py:435`, `src/cobalt/heartbeat/probes.py:146`, `:181`, `src/cobalt/jobs/watchdog.py:63` (def), `:437`. FR-2 touches only the two `probes.py` calls. `probes.cos`/`probes.hitl` are called by `runner.py:150-151` and by the tests.
- `wc -l`: `probes.py` 942 · `test_cos_probes.py` 139 · `test_sheet_daymode_probe.py` 202 · `heartbeat/probes.md` 152.
- `tail` of a report `## READ` names: none for FR1. The check report's FINDING O1 (`cos-tunables-check-2026-10-20.md:88-114`) was read as the model for the `take_beat` part of the test, and its `## OPEN` (`:229-233`) for the held ids.
- RESTARTS on an empty range: `e69d5ab8..HEAD` holds the built branch on a fix round. This round's own range, `uv run cobalt jobs restarts ace7a92a..HEAD` → `docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md	A	DOCS	-` · `RESTARTS: none`.
- The card's `## RECORDS` (`:64-79`), copied by reference. FR1's anchors were re-read above (`probes.py:146`, `:181`; `runner.py:127`, `:150-151`; `watchdog.py:59`, `:63-82`; the old test `:117`) and all matched. The FR-3 records (`:72-73`, `:75-79`) belong to FR-3, which is not in this run.
- No lock probe (BUILD-HUB PREFLIGHT). FR1 adds no with-DB test.

## E0 BASELINE
On `312f55fe` (the code of `ace7a92a`; the two wip commits are report-only):
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `4901 passed, 878 skipped, 4 xfailed, 36 warnings in 739.18s (0:12:19)`. The skips are with-DB (`Postgres env settings not available`) or `COBALT_LIVE_VAULT_ROOT not set` (the live-note run covers those).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.12s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`tests/cobalt/test_cos_probes.py`: `test_an_unreadable_owed_file_raises_through_both_probes` (`:117-127`) is REPLACED by `test_an_unreadable_owed_file_is_a_red_probe_never_a_raise`, parametrized `unreadable` (`{not json`) and `malformed` (`[]`), one `tmp_path` file each, with `watchdog.BOOTSTRAP_OWED_PATH` monkeypatched. It asserts:
- `probes.cos(NOW, enabled=True, …)` and `probes.hitl(NOW, enabled=True, …)` → `ok is False`, `"unreadable"` and the file path (the error text) in `detail`.
- Through `runner.take_beat(now=NOW, probe=False)` with the 12 other probes faked, `sweep` faked and `probes._cos_enabled` → True: `"database"` is in the beat, and `cos` and `hitl` are `ok is False` with the path in `detail`.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py` → `2 failed, 6 passed in 0.33s`. First lines of the reds:
- `[unreadable]`: `src/cobalt/heartbeat/probes.py:146: in cos` → `E           cobalt.jobs.watchdog.BootstrapOwedError: /private/var/folders/…/test_an_unreadable_owed_file_i0/bootstrap-owed.json: not JSON (Expecting property name enclosed in double quotes: line 1 column 2 (char 1))`
- `[malformed]`: `src/cobalt/heartbeat/probes.py:146: in cos` → `E           cobalt.jobs.watchdog.BootstrapOwedError: /private/var/folders/…/test_an_unreadable_owed_file_i1/bootstrap-owed.json: not a JSON object keyed by label`
Both fail for the row's reason: the probes raise `BootstrapOwedError` at `probes.py:146`. No with-DB red and no lock take. Commit `4f6c6472 wip(cos-tunables): fr1 red` (test file only).

## E3 THE ROWS
- FR-1: nothing re-shipped. PROOF: `git diff ace7a92a 875d18e6 -- tests/cobalt/test_sheet_daymode_probe.py` → empty (byte-equal at this round's tip).
- FR-2, `src/cobalt/heartbeat/probes.py` (only the two owed calls, now `:146-151` and `:185-190`): `try: owed = watchdog.bootstrap_owed()` / `except watchdog.BootstrapOwedError as e: return Probe("cos", False, f"bootstrap-owed.json unreadable: {e}")` (the same for `"hitl"`), then `if COS_LABEL in owed:`. Only `BootstrapOwedError` is caught. `runner.py` is untouched, and its `:127` docstring stands.
- DevDocs: `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, one dated section `## 2026-10-20 — cos-tunables fr1` after the check section. It says the probes are now red with the error and that the "`BootstrapOwedError` is not caught" line is superseded.
- Row tests: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py tests/cobalt/test_sheet_daymode_probe.py` → `18 passed in 5.33s`.
- Card suites: `uv run pytest -q -p no:cacheprovider tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probes.py tests/cobalt/test_sheet_daymode_probe.py` → `46 passed in 7.19s`. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_smoke.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_heartbeat*.py` → `259 passed, 19 skipped in 183.42s (0:03:03)`; all 19 skips `Postgres env settings not available` (`grep -c -F` → 19).
- THE MUTATIONS (Edit tool, each undone with the Edit tool; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_cos_probes.py`):
  - M1, the cos catch re-raises (`except …: raise`) → `2 failed, 6 passed in 0.27s`, first failing line `cobalt.jobs.watchdog.BootstrapOwedError: …/test_an_unreadable_owed_file_i0/bootstrap-owed.json: not JSON (Expecting property name enclosed in double quotes: line 1 column 2 (char 1))`.
  - M2, the hitl catch re-raises (cos restored) → `2 failed, 6 passed in 0.27s`, the same `BootstrapOwedError` first line (raised through `probes.hitl`; the direct `cos` assert had passed).
  - M3, a silent green (`Probe("cos", True, …)` in the catch) → `2 failed, 6 passed in 0.26s`, first line `AssertionError: assert (True is False)` / `where True = Probe(name='cos', ok=True, detail='bootstrap-owed.json unreadable: …', unknown=False).ok` (`test_cos_probes.py:128`).
  - After the undo, `git diff` showed only the two FR-2 hunks of `probes.py` (and this report).
- Commit `875d18e6 fix(cos-tunables): an unreadable owed file is a red cos/hitl probe, never a raise out of take_beat (FR1 FR-2, check O1; L1)`: `2 files changed, 13 insertions(+), 2 deletions(-)` (`probes.py`, `heartbeat/probes.md`).
- FR-3: not built (desk's CONTINUE, DECISION 2). `tunables.yaml`, `test_cos_offline.py` and `hitl/README.md` are untouched (`git diff --stat ace7a92a 875d18e6` below).

## RESTARTS
`uv run cobalt jobs restarts e69d5ab8..875d18e6` (tip named; the `..HEAD` form also counts the working-tree report), whole:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md	A	DOCS	-
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
This round alone, `uv run cobalt jobs restarts ace7a92a..875d18e6` → `docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-` · `docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md	A	DOCS	-` · `src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar` · `tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-` · `RESTARTS: com.cobalt.radar`. No UNCLASSIFIED path. The branch line matches round 1's; cos is skipped by the hub as not loaded (card 869).

## W THE THREE SUITES
`<tip>` = `875d18e6`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy` (23:15–23:48) → exit 0, verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4902/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5874/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-231537.log
```
- (a) `offline 4902/0` = E0's 4901 − the replaced test + its 2 parametrized cases. `tests/ops: skipped (no ops paths)`.
- (b) `lock taken: cos-tunables` (log `:963`), `lock: waited 0 min`; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:974`); `LEVEL 0013`.
- (c) `pass 1: whole (deploy)` (`:1030`); the executed command is the gate-lists PASS 1 command, as quoted in round 1's report (log `:1032`). `grep -n -F "OUTSIDE the allowed set"` on the log → no hit. Every SKIPPED line is quoted above.
- (c2) `dev forward: APPLIED 23:43:13` (`:1202`); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1286`). (c3) pass 2 → `with-DB 5874/0`. This build adds no with-DB test. (c3r) `stray rows: not read (no --tickers given)`: no ticker is written.
- (e) `live-note 148/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2256`) = F0 → `cobalt_dev: 0013 — F2 = F0`; `lock released` (`:2312`); `.env: removed`. `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` (23:48) → `No such file or directory`.
- No migration (`migration: none`).

## PRE-STOP SELF-CHECK
(1) BACKED. The one added test (both cases) is red on the tip for the row's reason (E2: `BootstrapOwedError` at `probes.py:146`). It is red under M1 (cos catch), M2 (hitl catch) and M3 (silent green) in E3. None stayed green; none rewritten. `test_sheet_daymode_probe.py` is unchanged (FR-1 admits it; no new assertion).
(2) BACKED. Callers: `bootstrap_owed(` in `probes.py:146`, `:181` (the two changed calls) are pinned by the new test, both the direct calls and through `take_beat`. `runner.py:150-151` is pinned by the `take_beat` part. `checks.py:435` and `watchdog.py:437` are not touched, and the sweep already reds the same error (`watchdog.py:439`). Input edges: not JSON, and JSON but not an object (both `BootstrapOwedError` raises, `watchdog.py:79`, `:81`). A missing or empty file is unchanged: it lists nothing (`watchdog.py:72-75`), and the owed and not-owed branches stay pinned by `test_cos_probe_is_unknown_green_while_owed` and `test_the_runner_path_reads_the_real_row_then_the_owed_file` (green, 46 passed).
(3) BACKED. Re-run at the tip: `grep -n -F "bootstrap-owed.json unreadable" src/cobalt/heartbeat/probes.py` → `149:`, `188:`; `grep -n -F "def test_an_unreadable_owed_file" tests/cobalt/test_cos_probes.py` → `118:`; `git log --oneline ace7a92a..HEAD` → `875d18e6`, `4f6c6472`, `312f55fe`, `af878860`; `git diff --stat ace7a92a 875d18e6` → `heartbeat/probes.md | 3 +` · this report `| 97 ++++` · `src/cobalt/heartbeat/probes.py | 12 ++-` · `tests/cobalt/test_cos_probes.py | 28 +++++--` · `4 files changed, 131 insertions(+), 9 deletions(-)`; the gate log lines by `grep -n -F` as cited in W.

## FOR THE CHECK
- `ace7a92a..875d18e6`: `af878860 wip(cos-tunables): PREFLIGHT — preflight.sh status/head rows fail on the same-branch fix round` · `312f55fe wip(cos-tunables): PREFLIGHT — resumed 22:58` · `4f6c6472 wip(cos-tunables): fr1 red` · `875d18e6 fix(cos-tunables): an unreadable owed file is a red cos/hitl probe, never a raise out of take_beat (FR1 FR-2, check O1; L1)`. Full range `e69d5ab8..875d18e6`: round 1's commits (`e3f05089`, `2a8b0315`, `17f45d80`, `2b53b56b`), the check's `ace7a92a`, then the four above.
- The card's FR1 CHECK ASK: an unreadable and a malformed owed file → red `cos` and red `hitl` with the error (file path and reason) in `detail`, `database` and the other faked probes present in `take_beat` (E2/E3 test). `test_sheet_daymode_probe.py` byte-equal to `ace7a92a` (E3 PROOF).
- Reds, mutations, greens: E2 and E3. Caller greps: PREFLIGHT. RUN rows: none.
- Suites: W (offline 4902/0, with-DB 5874/0, live-note 148/0), log `/Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-231537.log`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 = F0. Lock taken and released inside the one gate call (23:15 start, 23:48 end, `lock: waited 0 min`).
- RESTARTS: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- Detail shape: the card's `Probe("cos", False, "bootstrap-owed.json unreadable: <error>")`, where `<error>` is `str(BootstrapOwedError)`, which carries the path and reason. `Probe.unknown` stays at its default (`False`), as the card's shape gives no `unknown` argument.

FIXED: O1 — tests/cobalt/test_cos_probes.py::test_an_unreadable_owed_file_is_a_red_probe_never_a_raise
FIXED: O3 — tests/cobalt/test_sheet_daymode_probe.py::TestItIsWiredIntoTheBeat::test_the_runner_asks_it_right_after_sheet_http
FIXED: A1 — tests/cobalt/test_sheet_daymode_probe.py::TestItIsWiredIntoTheBeat::test_the_runner_asks_it_right_after_sheet_http

(O3 and A1 are settled by FR-1's admission of the path into the card's files: nothing re-shipped, byte-equal to `ace7a92a`. A2 is REJECTED in the check and settled by nothing; FR-2's dated DevDocs line is written.)

## CONTINUE
next: none (BUILT) — the desk verifies; FR-3 is a separate build (brain R2234).

## DECISIONS
1. ASK DESK (PREFLIGHT on a same-branch fix round) [20:23], ANSWERED by the desk's `CONTINUE: PREFLIGHT` [22:58]: `preflight.sh build` failed on the checked tip `ace7a92a`. Its status row rejects an untracked report that is not the card's `REPORT:`, and its head row rejects a `fix(cos-tunables):` HEAD. Default taken: stop with the wip commit. The rerun on the wip commits passed. Tool polish for the desk (R1863): `preflight.sh` has no fix-round form, and the hub's `RESUMED` write itself dirties the tree before the rerun (a second wip commit, `312f55fe`, was needed).
2. FR-3 not built: card FR1 (amended at `963a3dfc`) holds FR-3 (`hitl.page_base_url`, the two source comments, `test_the_shipped_hitl_page_base_url`, `hitl/README.md`). The desk's CONTINUE says "FR-3 is NOT part of this run: a fresh build at the step FIX ROUND row FR-3 does it afterwards (brain R2234)". Default taken: FR-1 and FR-2 only. `tunables.yaml` still holds the two `DEFAULT (brain; his word may change it)` comments and `hitl.page_base_url: null`, so the card's DEPLOY PROOF markers (`DEFAULT` after 0; the URL after 1) do not hold until FR-3 lands. Do not deploy this tip against the amended DEPLOY PROOF before the FR-3 build.

## RECORDS
- Session launched with `CONTINUE: FR1`; `date` → Tue Oct 20 20:22:24 EDT 2026. RECOVERY reads under `## PREFLIGHT`.
- Report path: no `REPORT:` line names an FR1 report. I took `cos-tunables-build-fr1-2026-10-20.md` (the shape of `deploy-freeze-build-fr1-2026-10-15.md`), which leaves the round-1 report untouched. The desk's CONTINUE named the same path.
- Stopped 20:23 EDT (`FAILED PREFLIGHT: status`, wip `af878860`).
- CONTINUED at PREFLIGHT 22:58 (`date`): the `cto-desk` message `CONTINUE: PREFLIGHT`. Fact verified: HEAD was `af878860 wip(cos-tunables): …` (`git log --oneline -1`); the tree held only the `RESUMED` edit. The message narrows the run to FR-1 and FR-2 (DECISION 2); it adds nothing and grants nothing.
- AUTHORIZATION re-run at 22:58 (the card moved to `963a3dfc`): `AUTHORIZED`.
- Extra lock takes: none; the one take was inside the gate. `REFUSED, not needed`: none.
- `.env`: removed, proven gone (gate (f); `ls -la` → No such file, 23:48).
- `cobalt_dev` held by `f5-x3-values` at PREFLIGHT (`siblings holding .env`); the gate's take waited 0 min.
- L74: one `Claude-Session:` reminder, recorded under `## L74`.
- Card records re-read at PREFLIGHT: `## PREFLIGHT`.
- `tokens`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 33c513b9-1e04-43e8-be12-288268e06a90` → `context 185819 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-tunables · tip: 875d18e6 | on e69d5ab8 | migration: none | offline 4902/0 | with-DB 5874/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (FR1: FR-1, FR-2; FR-3 deferred by the desk) | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 185819
