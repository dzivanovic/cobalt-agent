# cos-tunables FR-3 — fix round build report — 2026-10-20

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` row FR1, part FR-3 · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · branch tip at start `15d50ec9` (FR-1/FR-2 built at `875d18e6`) · builder Opus 5.5 (BAND HIGH).

## §0 Headline

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

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E3

## DECISIONS

## RECORDS
- Session launched with `CONTINUE: FIX ROUND row FR-3`; `date` → Wed Oct 21 00:11:26 EDT 2026. RECOVERY rows: `git status --short --branch` → `## ops/cos-tunables`; `git log --oneline -3` → `15d50ec9 docs(cos-tunables): build report — 875d18e6`, `875d18e6 fix(cos-tunables): …`, `4f6c6472 wip(cos-tunables): fr1 red`; `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`. No FR-3 report and no FR-3 wip commit existed, so FR-3 starts at AUTHORIZATION.
- Report path: no `REPORT:` line names an FR-3 report. I took `cos-tunables-build-fr3-2026-10-20.md`, the shape of the FR1 round's `cos-tunables-build-fr1-2026-10-20.md`, which leaves both earlier reports untouched.

(run in progress — next step under ## CONTINUE)
