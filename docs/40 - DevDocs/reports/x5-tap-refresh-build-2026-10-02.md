# x5-tap-refresh — build report (2026-10-02)

## §0 Headline
Started 08:11 EDT (`date`). Card: `prompts/2026-10-02/22-x5-tap-refresh-card.md`.

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

## E3 THE ROWS

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E2 — the with-DB red (lock take at the top level: lock (a)–(b), `<FP>` → `<F0>`, `--proof-only` → `0013`, forward, the file alone, (c3r) for `ZZX5R`, rollback to `0013`, `<FP>` = `<F0>`, lock (d)); then the `wip(x5-tap-refresh): red` commit if the reds are the rows'.

## DECISIONS
none so far.

## RECORDS
- Stopped at E2, 08:25 EDT: `cobalt_dev` lock held by `/Users/cobalt/cobalt-wt/ops-glob-1002/.env`. `.env` of this worktree: never copied at E2. No migration applied by this build. Wip commit holds the test file and this report.

FAILED: E2 — cobalt_dev lock held — /Users/cobalt/cobalt-wt/ops-glob-1002/.env
