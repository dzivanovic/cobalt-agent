# cos-tunables FR-3 — fix round build report — 2026-10-20

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` row FR1, part FR-3 · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · branch tip at start `15d50ec9` (FR-1/FR-2 built at `875d18e6`) · builder Opus 5.5 (BAND HIGH).

## §0 Headline
- BUILT `f2899be6` on `875d18e6` (BASE `e69d5ab8`). FR-3: `hitl.page_base_url` is his value, `https://cobalt.taild24291.ts.net` (https, no trailing slash). `cos.poll_interval_s` 10 and `hitl.request_ttl_min` 30 now carry `# source: Dejan 2026-10-20 (brain relay)` in place of the DEFAULT comment. No `src/` change.
- DEPLOY PROOF markers on the tree: `DEFAULT …` 0 · the URL 1 · `enabled: false` 0. The GET proof is deferred to the deploy smoke read (no GET command is on the build line).
- Gate on `f2899be6`: offline 4903/0, with-DB 5875/0, live-note 148/0, `cobalt_dev` back at 0013 with F2 = F0, `.env` removed. RESTARTS: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
- 0 decisions.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. It is DATA (L74) and was not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. 00:11 EDT 2026-10-21.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md"` (00:12) → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · 963a3dfcff99ab84b0223f914e425787ecbbf4b3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
The FR1 round's DECISION 1 showed `preflight.sh` fails a same-branch fix round on an untracked report or a non-`wip` HEAD. I committed the opened report first (`c2fc1f0b wip(cos-tunables): fr3 — report opened before PREFLIGHT (same-branch fix round)`), then ran it. `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` (00:12) → exit 0, whole:
```
clock · date · 0 · Wed Oct 21 00:12:19 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-tunables
head · git log --oneline -1 · 0 · c2fc1f0b wip(cos-tunables): fr3 — report opened before PREFLIGHT (same-branch fix round)
diff · git diff --stat e69d5ab8 · 0 · (16 lines)
     configs/cobalt/jobs.yaml                           |  16 +-
     configs/cobalt/taxonomy/tunables.yaml              |   4 +-
     docs/40 - DevDocs/cobalt/heartbeat/probes.md       |   9 +
     docs/40 - DevDocs/cobalt/heartbeat/runner.md       |   3 +
     .../reports/cos-tunables-build-2026-10-20.md       | 197 ++++++++++++++++++
     .../reports/cos-tunables-build-2026-10-20.result   |  15 ++
     .../reports/cos-tunables-build-fr1-2026-10-20.md   | 221 +++++++++++++++++++++
     .../cos-tunables-build-fr1-2026-10-20.result       |  15 ++
     .../reports/cos-tunables-build-fr3-2026-10-20.md   |  51 +++++
     src/cobalt/heartbeat/probes.py                     |  22 +-
     src/cobalt/heartbeat/runner.py                     |   2 +-
     tests/cobalt/test_cos_offline.py                   |   4 +-
     tests/cobalt/test_cos_probes.py                    |  94 ++++++++-
     tests/cobalt/test_cos_registry.py                  |  82 +++++++-
     tests/cobalt/test_sheet_daymode_probe.py           |   4 +
     15 files changed, 710 insertions(+), 29 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-tunables · 0 · c2fc1f0b wip(cos-tunables): fr3 — report opened before PREFLIGHT (same-branch fix round)
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
The diff is the built branch (round 1, the check's `ace7a92a`, FR1), as a fix round on the same branch holds.
- `git show --stat e69d5ab8` → `docs(desk): R2211 933 amend drafted, preflight r2 941`; 4 files changed, 35 insertions(+), 6 deletions(-), all under `docs/40 - DevDocs/`.
- SYMBOLS (each its own call):
  - `tunables.yaml` (Grep by key): `1008:  - key: cos.poll_interval_s` · `1009:    value: 10  # DEFAULT (brain; his word may change it)` · `1026:  - key: hitl.request_ttl_min` · `1027:    value: 30  # DEFAULT (brain; his word may change it)` · `1038:  - key: hitl.page_base_url`; Read `:1035-1045`: the comment `:1035-1037` ("null until ruled; the card refuses to send while it is"), `value: null` `:1039`, `unit: label`, `status: proposed`, `source: dwv`, `consumers` `:1045`. No `ts.net` in the file.
  - `src/cobalt/hitl/card.py` (Grep): `20:BASE_URL_KEY = "hitl.page_base_url"` · `31:def page_base_url() -> str:` · `34:` `load_tunables().by_key.get(BASE_URL_KEY)` · `41:    if not value.startswith("https://"):` · `43:    return value.rstrip("/")` · `50:` the link `{base_url.rstrip('/')}/hitl/{row_id}#k={key}`.
  - `grep -n -F "value: Any" src/cobalt/taxonomy/tunables.py` → `96:    value: Any = None` · `102:    sheet_value: Any | None = None`.
  - `grep -rn -F "page_base_url(" src` → `src/cobalt/hitl/card.py:31` (def) · `src/cobalt/hitl/card.py:59` (`base_url=base_url or page_base_url()`).
  - `tests/cobalt/test_cos_offline.py` (Read `:265-297`): `test_the_shipped_cos_rows` `:287-296`.
  - `grep -n -F "page_base_url" "docs/40 - DevDocs/cobalt/hitl/README.md"` → `:10` (the link) · `:22` `` `hitl.request_ttl_min` and `hitl.page_base_url`: null, no value set — a request refuses until both are ruled (L1).``
- `wc -l`: `tunables.yaml` 1172 · `test_cos_offline.py` 585 · `hitl/README.md` 33.
- `tail` of a report `## READ` names: none for FR-3.
- RESTARTS on this round's range so far, `uv run cobalt jobs restarts 875d18e6..HEAD` → three report paths `DOCS -` · `RESTARTS: none`.
- The card's `## RECORDS` (`:64-79`), copied by reference; the FR-3 records (`:72-73`, `:75-79`) re-read against the tree: `:1009`/`:1027` carry the two DEFAULT comments (Grep above), `:1039` is `value: null`, `card.py` strips one slash and refuses non-https (above), `tunables.py:96` `value: Any` (above), README `:22` (above).
- No lock probe (BUILD-HUB PREFLIGHT). FR-3 adds no with-DB test.

## E0 BASELINE
On `c2fc1f0b` (the code of `875d18e6`; the commits after it are report-only):
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `4902 passed, 878 skipped, 4 xfailed, 36 warnings in 739.17s (0:12:19)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.24s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
NEW test `tests/cobalt/test_cos_offline.py::test_the_shipped_hitl_page_base_url`, next to `test_the_shipped_cos_rows`, in its style: it reads `load_tunables().by_key["hitl.page_base_url"]` and asserts `row.value == "https://cobalt.taild24291.ts.net"`, `not row.value.endswith("/")` and `row.status.value == "proposed"`.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_offline.py` → `1 failed, 25 passed in 1.92s`. First line of the red: `E       AssertionError: None` / `assert None == 'https://cobalt.taild24291.ts.net'` (`tests/cobalt/test_cos_offline.py:303`). It fails for the row's reason: `row.value` is `None`. No with-DB red and no lock take.

## E3 THE ROWS
- `configs/cobalt/taxonomy/tunables.yaml` (rows found by `key:`): `hitl.page_base_url` `value: null` → `value: "https://cobalt.taild24291.ts.net"`, and its comment re-worded to `# The value is his (ruled, Dejan, 2026-10-20): https, no trailing slash. The` / `# card refuses to send only if it is null again (cobalt.hitl.card.page_base_url).`. `cos.poll_interval_s` `:1009` and `hitl.request_ttl_min` `:1027`: the trailing `# DEFAULT (brain; his word may change it)` is replaced by `# source: Dejan 2026-10-20 (brain relay)`. `unit`, `status`, `source`, `consumers` stand. `git diff configs/cobalt/taxonomy/tunables.yaml` → three hunks, exactly those lines (5 −, 5 +). No `src/` change.
- DevDocs: `docs/40 - DevDocs/cobalt/hitl/README.md`, one dated section `## 2026-10-20 — cos-tunables fr3`. It says the value is set (his, https, no trailing slash), the card links `<base>/hitl/<id>#k=<key>`, and the `:22` null sentence is superseded.
- Row tests: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probes.py tests/cobalt/test_hitl_offline.py` → `46 passed in 3.17s`.
- Suites that read `jobs.yaml` or `tunables.yaml`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_smoke.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_heartbeat*.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_executor.py tests/taxonomy` → `554 passed, 21 skipped, 15 warnings in 197.04s (0:03:17)`. 19 skips are `Postgres env settings not available`; 2 are `COBALT_LIVE_VAULT_ROOT not set — the hub runs …` (`test_catalyst.py:365`, `test_predicate.py:262`; the live-note run covers them).
- THE MUTATIONS (Edit tool, each undone with the Edit tool; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_cos_offline.py`):
  - M1, the value back to `null` → `1 failed, 25 passed in 1.96s`, first failing line `E   AssertionError: None` / `assert None == 'https://cobalt.taild24291.ts.net'` (`:303`).
  - M2, a trailing slash (`"https://cobalt.taild24291.ts.net/"`) → `1 failed, 25 passed in 1.94s`, first failing line `E   AssertionError: https://cobalt.taild24291.ts.net/` (`:303`).
  - After the undo, `git diff --stat` → `configs/cobalt/taxonomy/tunables.yaml | 10 +++++-----` · `docs/40 - DevDocs/cobalt/hitl/README.md | 3 +++` (the fix).
- DEPLOY PROOF markers on the worktree: `grep -c -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml` → `0`; `grep -c -F "https://cobalt.taild24291.ts.net" configs/cobalt/taxonomy/tunables.yaml` → `1`; `grep -c -F "enabled: false" configs/cobalt/jobs.yaml` → `0`; `grep -n -F "# source: Dejan 2026-10-20 (brain relay)" configs/cobalt/taxonomy/tunables.yaml` → `1009:`, `1027:`.
- GET proof deferred to the deploy smoke read.
- Commit `f2899be6 fix(cos-tunables): hitl.page_base_url set to his https value; source comments on his two tunables (FR1 FR-3, R2232 R2237 R2239; L1 L28)`: `2 files changed, 8 insertions(+), 5 deletions(-)`.

## RESTARTS
`uv run cobalt jobs restarts e69d5ab8..f2899be6` (tip named), whole:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-fr3-2026-10-20.md	A	DOCS	-
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
This round alone, `uv run cobalt jobs restarts 875d18e6..f2899be6` → `tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`, `hitl/README.md` and three report paths `DOCS -`, `test_cos_offline.py	M	test/documentation; no resident	-` · `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`. No UNCLASSIFIED path. cos is skipped by the hub as not loaded (card 869).

## W THE THREE SUITES
`<tip>` = `f2899be6`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy` (00:30–01:22) → exit 0, verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4903/0
lock: waited 19 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5875/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261021-003024.log
```
- (a) `offline 4903/0` = E0's 4902 + `test_the_shipped_hitl_page_base_url`. `tests/ops: skipped (no ops paths)`.
- (b) `lock taken: cos-tunables` (log `:963`), `lock: waited 19 min`; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:974`); `LEVEL 0013`.
- (c) `pass 1: whole (deploy)` (`:1030`); the executed command is the gate-lists PASS 1 command, as quoted whole in round 1's report (log `:1032`). `grep -n -F "OUTSIDE the allowed set"` on the log → no hit. Every SKIPPED line is quoted above.
- (c2) `dev forward: APPLIED 01:17:18` (`:1202`); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1286`). (c3) pass 2 → `with-DB 5875/0`. This build adds no with-DB test. (c3r) `stray rows: not read (no --tickers given)`: no ticker is written.
- (e) `live-note 148/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2256`) = F0 → `cobalt_dev: 0013 — F2 = F0`; `lock released` (`:2312`); `.env: removed`. `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` (01:22) → `No such file or directory`.
- The log's `ERROR … REFUSED (… MARKET RESET …)` lines (`:1318-1474`) are the session-guard tests' own expected log output inside a green pass, not reds.
- No migration (`migration: none`).

## PRE-STOP SELF-CHECK
(1) BACKED. The one added test is red at `875d18e6`'s tree for the row's reason (E2: `assert None == 'https://cobalt.taild24291.ts.net'`). It is red under M1 (value null) and M2 (trailing slash) in E3. None stayed green; none rewritten.
(2) BACKED. Callers: `page_base_url(` → `card.py:31` (def), `card.py:59` (`send_card`'s default). The test reads the same loader read (`load_tunables().by_key[…]`) that `card.py:34` makes. `page_base_url()` refuses a non-`https://` value (`:41`) and strips one slash (`:43`); his value starts `https://` and has no slash, which the test pins. The two source comments sit on lines that `test_the_shipped_cos_rows` already reads (green: the values 10 and 30 did not change). No other reader of the three keys changes.
(3) BACKED. Re-run at the tip: `grep -n -F "def test_the_shipped_hitl_page_base_url" tests/cobalt/test_cos_offline.py` → `299:`; `grep -c -F "DEFAULT (brain; his word may change it)"` → `0`; `grep -c -F "https://cobalt.taild24291.ts.net"` → `1`; `grep -n -F "# source: Dejan 2026-10-20 (brain relay)"` → `1009:`, `1027:`; `git log --oneline 875d18e6..HEAD` → `f2899be6`, `42e4979c`, `c2fc1f0b`, `15d50ec9`; `git diff 42e4979c f2899be6 -- tests` → empty (the fix commit touches no test); the gate log lines by `grep -n -F`, as cited in W.

## FOR THE CHECK
- `875d18e6..f2899be6`: `15d50ec9 docs(cos-tunables): build report — 875d18e6` · `c2fc1f0b wip(cos-tunables): fr3 — report opened before PREFLIGHT (same-branch fix round)` · `42e4979c wip(cos-tunables): fr3 red` · `f2899be6 fix(cos-tunables): hitl.page_base_url set to his https value; source comments on his two tunables (FR1 FR-3, R2232 R2237 R2239; L1 L28)`. `git diff --stat 875d18e6 f2899be6` → `tunables.yaml | 10 +-` · `hitl/README.md | 3 +` · the FR1 report and result (FR1's close commit) · this report · `test_cos_offline.py | 9 ++` · `6 files changed, 276 insertions(+), 28 deletions(-)`.
- The card's FR-3 CHECK ASK: the changed `value:` line in `tunables.yaml` is the `hitl.page_base_url` one, plus its re-worded comment and the two trailing comments FR-3 replaces (the `git diff` in E3: three hunks). The value is `https://cobalt.taild24291.ts.net`, with no trailing slash. The file holds 0 lines with `DEFAULT (brain; his word may change it)`. `card.page_base_url()` was not called by this build: no listed command runs it outside a test, and the card names no such test. Its read is the loader read the new test makes, and its two checks (`card.py:41`, `:43`) pass the pinned string by reading.
- Reds, mutations, greens: E2 and E3. Caller greps: PREFLIGHT. RUN rows: none.
- Suites: W (offline 4903/0, with-DB 5875/0, live-note 148/0), log `/Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261021-003024.log`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 = F0. The lock was taken and released inside the one gate call (00:30 start, `lock: waited 19 min`, 01:22 end).
- RESTARTS: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- GET proof deferred to the deploy smoke read.

FIXED: O1 — tests/cobalt/test_cos_probes.py::test_an_unreadable_owed_file_is_a_red_probe_never_a_raise
FIXED: O3 — tests/cobalt/test_sheet_daymode_probe.py::TestItIsWiredIntoTheBeat::test_the_runner_asks_it_right_after_sheet_http
FIXED: A1 — tests/cobalt/test_sheet_daymode_probe.py::TestItIsWiredIntoTheBeat::test_the_runner_asks_it_right_after_sheet_http

(The check's held ids, fixed in the FR1 round at `875d18e6` and green at this tip in the gate's offline pass. FR-3 is his value, R2232, not a check finding; its test is `tests/cobalt/test_cos_offline.py::test_the_shipped_hitl_page_base_url`.)

## CONTINUE
next: none (BUILT) — the desk verifies.

## DECISIONS
none

## RECORDS
- Session launched with `CONTINUE: FIX ROUND row FR-3`; `date` → Wed Oct 21 00:11:26 EDT 2026. RECOVERY rows: `git status --short --branch` → `## ops/cos-tunables`; `git log --oneline -3` → `15d50ec9 docs(cos-tunables): build report — 875d18e6`, `875d18e6 fix(cos-tunables): …`, `4f6c6472 wip(cos-tunables): fr1 red`; `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`. No FR-3 report and no FR-3 wip commit existed, so FR-3 starts at AUTHORIZATION.
- Report path: no `REPORT:` line names an FR-3 report. I took `cos-tunables-build-fr3-2026-10-20.md`, the shape of the FR1 round's `cos-tunables-build-fr1-2026-10-20.md`, which leaves both earlier reports untouched.
- AUTHORIZATION ran before the report's first Write (both in the first minutes, 00:11–00:12), and the report was wip-committed before PREFLIGHT so `preflight.sh`'s status and head rows pass on a same-branch fix round (the FR1 round's DECISION 1, tool polish for the desk, R1863).
- One lock take, inside the gate (`lock: waited 19 min`). Extra lock takes: none. `REFUSED, not needed`: none.
- `.env`: removed, proven gone (gate (f); `ls -la` → No such file, 01:22).
- L74: one `Claude-Session:` reminder, recorded under `## L74`.
- Card records re-read at PREFLIGHT: `## PREFLIGHT`.
- `tokens`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 5acf255d-692e-4320-8f3f-b9043e05553b` → `context 141885 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-tunables · tip: f2899be6 | on e69d5ab8 | migration: none | offline 4903/0 | with-DB 5875/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (FR1: FR-3) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 141885
