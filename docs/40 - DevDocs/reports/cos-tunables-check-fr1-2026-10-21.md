# cos-tunables — check of fix round FR1 (FR-1, FR-2, FR-3) — 2026-10-21

## §0 Headline
- FR1 holds. FR-1's file is byte-equal to `ace7a92a`. FR-2 gives a red `cos` and `hitl` probe with the error text, and the beat's other probes still land. FR-3's value loads, and `card.page_base_url()` returns it. `tunables.yaml` holds 0 DEFAULT lines.
- Grok had 1 finding: the FR-2 test never checked the error text. It held and is fixed in the test only (`0b8bf093`), shown red under a mutation first.
- One open item: an owed file the OS cannot read still raises out of `take_beat`. The card says to catch `BootstrapOwedError` only, and the reader is outside the rows, so it is REJECTED and sent to follow-up (`## DECISIONS` 1).
- The deploy gate is green on `0b8bf093`: offline 8976/0, with-DB 5875/0, live-note 148/0, `cobalt_dev` back at 0013, `.env` removed. ready: YES.

## L74
A system reminder at launch asked that commits also carry a `Claude-Session:` line. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · 3b3ba624a869f58a91546ceda42c89a3f5428243
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:
```
clock · date · 0 · Wed Oct 21 01:24:50 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-tunables
head · git log --oneline -1; git log --stat --format=%h f2899be6..HEAD · 0 · (6 lines)
    8bcbc5ae docs(cos-tunables): build report — f2899be6
    8bcbc5ae
    
     .../reports/cos-tunables-build-fr3-2026-10-20.md   | 98 +++++++++++++++++++++-
     .../cos-tunables-build-fr3-2026-10-20.result       | 15 ++++
     2 files changed, 110 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-tunables/docs/40 - DevDocs/reports/cos-tunables-build-fr3-2026-10-20.md" · 0 · BUILT · job: cos-tunables · tip: f2899be6 | on e69d5ab8 | migration: none | offline 4903/0 | with-DB 5875/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (FR1: FR-3) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 141885
range · git log --oneline e69d5ab8..f2899be6 · 0 · (13 lines)
    f2899be6 fix(cos-tunables): hitl.page_base_url set to his https value; source comments on his two tunables (FR1 FR-3, R2232 R2237 R2239; L1 L28)
    42e4979c wip(cos-tunables): fr3 red
    c2fc1f0b wip(cos-tunables): fr3 — report opened before PREFLIGHT (same-branch fix round)
    15d50ec9 docs(cos-tunables): build report — 875d18e6
    875d18e6 fix(cos-tunables): an unreadable owed file is a red cos/hitl probe, never a raise out of take_beat (FR1 FR-2, check O1; L1)
    4f6c6472 wip(cos-tunables): fr1 red
    312f55fe wip(cos-tunables): PREFLIGHT — resumed 22:58
    af878860 wip(cos-tunables): PREFLIGHT — preflight.sh status/head rows fail on the same-branch fix round
    ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)
    2b53b56b docs(cos-tunables): build report — 17f45d80
    17f45d80 fix(cos-tunables): pass S2 1
    2a8b0315 feat(cos-tunables): rows
    e3f05089 wip(cos-tunables): red
PREFLIGHT OK
```
- THE RANGE typed: `git log --stat --format=%h e69d5ab8..f2899be6` → path union: `configs/cobalt/taxonomy/tunables.yaml`, `configs/cobalt/jobs.yaml`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/heartbeat/runner.py`, `tests/cobalt/test_cos_offline.py`, `tests/cobalt/test_cos_probes.py`, `tests/cobalt/test_cos_registry.py`, `tests/cobalt/test_sheet_daymode_probe.py`, `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, `docs/40 - DevDocs/cobalt/heartbeat/runner.md`, `docs/40 - DevDocs/cobalt/hitl/README.md`, and the build reports under `docs/40 - DevDocs/reports/`.
- The card has no `DB: none` line: the with-DB gate runs at `## 6`.
- `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-tunables-fr1-check` (card CHECK ASKS FR1: "runs as JOB `cos-tunables-fr1` (the scratch rule)"): absent before staging (the listing of `tribunal-bars-0920/` held `cos-tunables-check` only) = fresh.
- House probes (`house-probe.sh --card`, background, exit 0): `grok: UP` · `gemini: UP`. No `HOUSE A: OpenAI` header line → Sol not probed.
- Seats: **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.
- PROVEN BY FIRST REAL USE: the write and with-DB strings, at `## 4`–`## 6`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → output whole:
```
25 <S>/STAGED-CARD
26131 <S>/diff.md
27273 <S>/files/933-cos-tunables-card.md
23027 <S>/files/cos-tunables-build-fr3-2026-10-20.md
27165 <S>/files/wt/configs/cobalt/jobs.yaml
40130 <S>/files/wt/configs/cobalt/taxonomy/tunables.yaml
8330 <S>/files/wt/docs/40 - DevDocs/cobalt/heartbeat/probes.md
4208 <S>/files/wt/docs/40 - DevDocs/cobalt/heartbeat/runner.md
3825 <S>/files/wt/docs/40 - DevDocs/cobalt/hitl/README.md
29678 <S>/files/wt/docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md
256 <S>/files/wt/docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.result
27553 <S>/files/wt/docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md
301 <S>/files/wt/docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.result
9758 <S>/files/wt/docs/40 - DevDocs/reports/cos-tunables-build-fr3-2026-10-20.md
40292 <S>/files/wt/src/cobalt/heartbeat/probes.py
20465 <S>/files/wt/src/cobalt/heartbeat/runner.py
23641 <S>/files/wt/tests/cobalt/test_cos_offline.py
6733 <S>/files/wt/tests/cobalt/test_cos_probes.py
4593 <S>/files/wt/tests/cobalt/test_cos_registry.py
7668 <S>/files/wt/tests/cobalt/test_sheet_daymode_probe.py
386 <S>/rulings.md
STAGED 21 files · 331438 bytes · commits 8
```
(`<S>` written short here; the script printed the absolute path.) `commits 8` against PREFLIGHT's 13: the diff is `git log -p … -- . ":(exclude)docs"`, which lists only the 8 commits that touch a path outside `docs/` (`f2899be6 42e4979c 875d18e6 4f6c6472 ace7a92a 17f45d80 2a8b0315 e3f05089`); the other 5 are docs-only. `grep -c "^commit " <S>/diff.md` → `8`.
`stage-copy.sh`, each → `COPIED <bytes> <dest>`: `files/cos-bootstrap-decisions-2026-10-20.md` 4960 · `files/cos-tunables-check-2026-10-20.md` 30248 · `files/wt/src/cobalt/cos/session.py` 14955 · `files/wt/src/cobalt/cos/run.py` 6470 · `files/wt/src/cobalt/hitl/actions.py` 7022 · `files/wt/src/cobalt/hitl/card.py` 2645 · `files/wt/src/cobalt/jobs/watchdog.py` 23604 · `files/wt/src/cobalt/smoke/checks.py` 32603 · `files/wt/src/cobalt/taxonomy/tunables.py` 4920 · `files/wt/tests/cobalt/test_smoke.py` 77859 · `files/wt/tests/cobalt/test_jobs.py` 41777.
`<S>/HOUSE-INSTRUCTIONS.md` written (28370 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
House A Grok started 01:27:36 EDT (`date` before the gates), background task `bhc8fcv93`. No house B (not needed). `cd <WT>` → `git status --short --branch` → `## ops/cos-tunables`.

## OWN FINDINGS
Written before either house list was opened. Scope: FR1 (FR-1, FR-2, FR-3), per the card's FR1 CHECK ASK.

FINDING O1
ROW: FR1 (FR-2)
CLAIM: An owed file that cannot be READ (an OS error, e.g. the path is a directory or has no read permission) is not a `BootstrapOwedError`: `src/cobalt/jobs/watchdog.py:70-73` catches `FileNotFoundError` only, so the `OSError` passes the `except watchdog.BootstrapOwedError` at `src/cobalt/heartbeat/probes.py:148` and `:187` and raises out of `take_beat` (`src/cobalt/heartbeat/runner.py:150`), the one case FR-2 names "unreadable"; the test's `unreadable` id (`tests/cobalt/test_cos_probes.py:117`) is invalid JSON, not an unreadable file.
RUN: TEST — `tests/cobalt/test_cos_probes.py`
```python
def test_an_owed_path_that_cannot_be_read_is_a_red_probe_never_a_raise(monkeypatch, tmp_path):
    from cobalt.heartbeat import probes
    from cobalt.jobs import watchdog

    monkeypatch.setattr(watchdog, "BOOTSTRAP_OWED_PATH", tmp_path)  # a directory: read_text raises OSError
    cos = probes.cos(NOW, enabled=True, job_store=_never_stamped(), cos_store=_turns(None))
    assert cos.ok is False and str(tmp_path) in cos.detail
    hitl = probes.hitl(NOW, enabled=True, store=SimpleNamespace(probe_counts=_counts_raise))
    assert hitl.ok is False and str(tmp_path) in hitl.detail
```
EXPECT: on the tip, `IsADirectoryError` raised from `watchdog.py:71` through `probes.py:147`.

FINDING O2
ROW: FR1 (FR-3, CHECK ASK FR-3 "Does `card.page_base_url()` return the string through the loader?")
CLAIM: No test calls `cobalt.hitl.card.page_base_url()` (`src/cobalt/hitl/card.py:31-43`) on the shipped row; the FR-3 test (`tests/cobalt/test_cos_offline.py:299-305`) reads the loader only, so the card's own read of the ruled value is unpinned.
RUN: TEST — `tests/cobalt/test_cos_offline.py`
```python
def test_the_card_reads_the_ruled_base_url_through_the_loader():
    from cobalt.hitl import card
    from cobalt.taxonomy.loader import load_tunables

    assert card.page_base_url() == load_tunables().by_key[card.BASE_URL_KEY].value
```
EXPECT: if the claim's worry is real, a `RuntimeError` (no value / not https) or an inequality; green answers the ask YES.

FINDING O3
ROW: FR1 (FR-1, CHECK ASK FR1 "Is `test_sheet_daymode_probe.py` byte-equal to its `ace7a92a` form?")
CLAIM: FR-1 ships nothing, so `tests/cobalt/test_sheet_daymode_probe.py` must be byte-equal between `ace7a92a` and the tip.
RUN: COMMAND — `git diff ace7a92a f2899be6 -- tests/cobalt/test_sheet_daymode_probe.py`
EXPECT: a defect prints a hunk; byte-equal prints nothing.

FINDING O4
ROW: FR1 (FR-3, CHECK ASK X1 / FR-3, DEPLOY PROOF marker 2)
CLAIM: `configs/cobalt/taxonomy/tunables.yaml` must hold 0 lines with `DEFAULT (brain; his word may change it)`, and exactly the three `value:` lines (`cos.poll_interval_s`, `hitl.request_ttl_min`, `hitl.page_base_url`) plus the comment above `hitl.page_base_url` change against BASE.
RUN: COMMAND — `grep -c -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml`, then `git diff e69d5ab8..f2899be6 -- configs/cobalt/taxonomy/tunables.yaml`
EXPECT: a defect prints a count above 0, or a hunk outside those lines.

## Findings
House A Grok finished 01:41:46 EDT (`date` at the notice), exit 0; `ls -la <S>` → `house-a.md` 614 bytes, written by Grok; its stdout was the path only. Its last line: `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:"` over `house-a.md` → `4:RUN: COMMAND`, followed by one `grep` line: kept.
- A1 · Grok · FR1 (FR-2) · `test_cos_probes.py:128-130, :140-141` accept a red detail holding the word `unreadable` and the path, never the `BootstrapOwedError` reason (`not JSON`, `not a JSON object keyed by label`) · COMMAND

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py::test_an_owed_path_that_cannot_be_read_is_a_red_probe_never_a_raise` | `1 failed in 0.09s`; first failing line `src/cobalt/heartbeat/probes.py:147: in cos` → `src/cobalt/jobs/watchdog.py:71` → `E       IsADirectoryError: [Errno 21] Is a directory: '<tmp_path>'` | REJECTED — FR1 row: "Catch `BootstrapOwedError` only, at the two `bootstrap_owed()` calls"; and the reader that would wrap an `OSError` is `src/cobalt/jobs/watchdog.py:70-73`, outside the rows' files. Red for its stated reason; test removed with Edit (not committed). OPEN |
| O2 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_offline.py::test_the_card_reads_the_ruled_base_url_through_the_loader` | `1 passed in 0.12s` | NOT HELD — CHECK ASK FR-3 answered YES: `card.page_base_url()` returns the loader's value. Test removed with Edit |
| O3 | opus-own | `git diff ace7a92a f2899be6 -- tests/cobalt/test_sheet_daymode_probe.py` | (no output) | NOT HELD — byte-equal (CHECK ASK FR1, second part: YES) |
| O4 | opus-own | `grep -c -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml`; `git diff e69d5ab8..f2899be6 -- configs/cobalt/taxonomy/tunables.yaml` | `0`; three hunks only: `cos.poll_interval_s` `value: null` → `value: 10  # source: Dejan 2026-10-20 (brain relay)`, `hitl.request_ttl_min` `value: null` → `value: 30  # source: Dejan 2026-10-20 (brain relay)`, and the two comment lines above `hitl.page_base_url` plus its `value: null` → `value: "https://cobalt.taild24291.ts.net"` | NOT HELD — X1 / FR-3 answered YES |
| A1 | Grok | `grep -n -F "not JSON" tests/cobalt/test_cos_probes.py` | (no output, exit 1). Proof the gap is real: with `probes.py:149`/`:188` mutated to `f"bootstrap-owed.json unreadable: {watchdog.BOOTSTRAP_OWED_PATH}"` (the error text dropped), the old assertions at `:130` (`"unreadable"` and `str(path)` in detail) pass and only the new line fails: `tests/cobalt/test_cos_probes.py:131: AssertionError` · `assert 'not JSON' in 'bootstrap-owed.json unreadable: <tmp_path>/bootstrap-owed.json'` · `2 failed, 6 passed in 0.33s`. Mutation undone with Edit; `git diff --stat` → only `tests/cobalt/test_cos_probes.py` | HELD |

A1 was held by its COMMAND, not by a red test, so no `wip(cos-tunables): check red` commit exists: the held item is the test's own weakness, and the strengthened test is the fix; it was shown red under the mutation above before the commit.

## FIXES
- A1: `0b8bf093 fix(cos-tunables): the FR-2 probe test pins the BootstrapOwedError reason in each red detail (check A1)` — `tests/cobalt/test_cos_probes.py`: the parametrize carries `(text, reason)` (`not JSON`, `not a JSON object keyed by label`); `reason in detail` asserted for `probes.cos`, `probes.hitl` and both beat probes. One dated line `## 2026-10-21 — cos-tunables fr1 check` in `docs/40 - DevDocs/cobalt/heartbeat/probes.md`. After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_sheet_daymode_probe.py` → `47 passed in 7.12s` (0 failed). No `src/` change.

## Suites
RESTARTS first: `uv run cobalt jobs restarts e69d5ab8..HEAD` → no UNCLASSIFIED row; the last line is `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`tunables.yaml` resident reads aset, cos, radar; `probes.py` and `runner.py` static import reach radar; `jobs.yaml` registry, no restart; tests and docs no resident). X5: this matches the build's line. The header line `com.cobalt.aset com.cobalt.radar` leaves out cos, and the hub skips cos as not loaded (card record, card 869).
`sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy --deploy-gate` (01:43–02:30 EDT) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8976/0
lock: waited 0 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261021-014310.log
```
- `offline 8976/0` includes `tests/ops` (deploy gate). `grep -c -F "OUTSIDE the allowed set" <log>` → `0`.
- `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1047`) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2329`) → `cobalt_dev: 0013 — F2 = F0`.
- `.env: removed`; `ls /Users/cobalt/cobalt-wt/cos-tunables/.env` (02:30) → `No such file or directory`.

## Scope
PREFLIGHT's path union (`## PREFLIGHT`) plus my one commit `0b8bf093`: `tests/cobalt/test_cos_probes.py` (FR1's files) and `docs/40 - DevDocs/cobalt/heartbeat/probes.md` (FR1's files). Nothing outside the rows' files.

## Checked against the branch
- (i) `git log --oneline f2899be6..HEAD -- . ":(exclude)docs"` → `0b8bf093 fix(cos-tunables): the FR-2 probe test pins the BootstrapOwedError reason in each red detail (check A1)` = `<tip now>`.
- (ii) `git log --stat --format=%h f2899be6..HEAD` → `0b8bf093`: `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, `tests/cobalt/test_cos_probes.py`; `8bcbc5ae`: the build report and result (docs). No other path.
- (iii) `git log --oneline e69d5ab8..HEAD -- ops/com.cobalt.cos.plist ops/start_cos.sh src/cobalt/cos src/cobalt/hitl data/deploy/bootstrap-owed.json` → empty.
- (iv) A1: `grep -n -F "def test_an_unreadable_owed_file_is_a_red_probe_never_a_raise" tests/cobalt/test_cos_probes.py` → `120:` (one line). A1 was held by its command; there is no `wip … check red` commit (`## RUNS`). Its red is the mutation run quoted there.
- (v) `ls /Users/cobalt/cobalt-wt/cos-tunables/.env` → No such file; `git status --short --branch` → `## ops/cos-tunables` alone.
- (vi) `git log --stat --format=%h e69d5ab8..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file, and no with-DB test file (only offline test files: `test_cos_probes.py`, `test_cos_offline.py`, `test_cos_registry.py`, `test_sheet_daymode_probe.py`). The gate lists are not needed.
- (vii) The card's `## RECORDS` name `git rev-parse` and `git grep` reads, which are not on my list. They are not re-run. O3 and O4 cover the same facts at the tip.
- (viii) L32: this report holds no ticker, price or trade date of his. The URL is the card's ruled value and appears as the card writes it.
- COUNTING: findings 5 (O1–O4, A1) · dropped 0 · held 1 (A1) · fixed 1 · held unfixed 0 · open 1 (O1).

## OPEN
- O1 · REJECTED — the FR1 row says "Catch `BootstrapOwedError` only". An `OSError` while reading the owed file (a directory, no read permission) raises out of `probes.cos` / `probes.hitl` and `take_beat`. Proof: `IsADirectoryError` at `watchdog.py:71`, `## RUNS`. What would settle it: a card row that lets `src/cobalt/jobs/watchdog.py` `bootstrap_owed` turn an `OSError` other than `FileNotFoundError` into a `BootstrapOwedError`, with the O1 test as its red. FOLLOW-UP.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. O1 FOLLOW-UP (outside the card's rows): an owed file that exists but cannot be read raises out of `take_beat`. The fix is `src/cobalt/jobs/watchdog.py:70-73`, which the rows do not admit, and the card limits FR-2 to `BootstrapOwedError`. Safe default taken: not fixed, and the test is not committed. Today the owed file is a gitignored desk file that the desk scripts write. Its test text is in `## OWN FINDINGS` O1, ready to paste for the fix round or a later card.

## RECORDS
- L74: one `Claude-Session:` attribution reminder after launch, recorded under `## L74`. Not acted on.
- Scratch folder `cos-tunables-fr1-check`, from the card's CHECK ASK FR1 ("runs as JOB `cos-tunables-fr1` (the scratch rule)").
- House A Grok: `FINDINGS: 1`, written to `house-a.md` by Grok itself. House B: none, because the card's `HOUSE B` line is `as needed`. Gemini was UP and was not seated. The stop line writes `house B: none (not needed)`, as PREFLIGHT recorded it.
- Dropped findings: none. Houses that produced nothing: none. `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (the one take was inside `gate.sh`, `lock: waited 0 min`).
- O1's and O2's tests were added with Edit, run, and removed with Edit. Neither was committed.
- files opened: 15 — `CHECK-HUB.md`, the card, `BUILD-HUB.md`, `cos-tunables-build-fr3-2026-10-20.md` (from `:100`), `areas/cobalt.md` (`:20-24`, `:33-64`), `src/cobalt/jobs/watchdog.py`, `src/cobalt/hitl/card.py`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/heartbeat/runner.py`, `tests/cobalt/test_cos_probes.py`, `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, `<S>/house-a.md`, and three task output files (the house probe, Grok's stdout, the gate).
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh c726e862-248b-4c4b-b4ac-0de9cfab5c04` → `context 181651 of 400000 — ok`.
- Check of `cos-tunables`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-tunables · pass: 1 · tip: 0b8bf093 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8976/0 · with-DB 5875/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181651
