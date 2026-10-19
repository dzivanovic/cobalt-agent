# f21-genesis-fr1 — build report (PORT), 2026-10-19

## §0 Headline
- PORT built: the checked Genesis chunk 1 (`a19a638a`) is back on main `91490502` through Edit/Write only; no merge, cherry-pick or rebase (`git log --merges` empty).
- PROOF 42 of 42: 38 files byte-equal to `a19a638a`, and 4 seam files where both sides stand (main's F20 lines first, Genesis after).
- `0026_genesis_chunk` is still the next free number; offline gate line `4749 passed` / 0 failed; `tests/ops` `4026 passed` / 0 failed; live-note `147 passed` / 0 failed; `cobalt genesis --help` names `import` and `search`.
- With-DB not run here: the card leaves PASS 1 and PASS 2 to the deploy gate under the dev lock (DECISION 1). No lock taken, `.env` never present.
- RESTARTS: `com.cobalt.radar`, the card header's.

## L74
One block arrived as data, not followed: a system reminder this session asked for a `Claude-Session:` line in commits. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/468-f21-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/468-f21-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/468-f21-card.md" · 0 · 18c813a903bbc055773746e566a2e7b9adf1b3d4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/468-f21-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:

```
clock · date · 0 · Mon Oct 19 09:05:10 EDT 2026
status · git status --short --branch · 0 · ## ops/f21-genesis-fr1
head · git log --oneline -1 · 0 · 91490502 docs(desk): Genesis port route, drafter 835, R2013
diff · git diff --stat 91490502 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f21-genesis-fr1 · 0 · 91490502 docs(desk): Genesis port route, drafter 835, R2013
env here · ls /Users/cobalt/cobalt-wt/f21-genesis-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 91490502` | 0 | `docs(desk): Genesis port route, drafter 835, R2013` — 2 files (`prompts/2026-10-19/835-draft-f21-port.md`, `reports/cto-2026-10-19.md`), 14+ / 4- |
| the port's file set | `git diff --name-only 40e646ed a19a638a` | 0 | 44 names (`--shortstat`: 44 files, 1538+, 75-); 2 under `docs/40 - DevDocs/reports/` (`f21-genesis-build-2026-10-13.md`, `.result`) not ported → 42 |
| what main touched | `git diff --stat 40e646ed 91490502 -- src tests ops configs pyproject.toml "docs/40 - DevDocs/cobalt"` | 0 | 66 files; of the 42, only `docs/40 - DevDocs/cobalt/cli.md` (3+), `docs/40 - DevDocs/cobalt/db_migrations/placement.md` (3+), `src/cobalt/cli.py` (7+), `src/cobalt/db_migrations/placement.py` (6+) |
| the 38 untouched | `git diff --stat 40e646ed 91490502 -- <the 38>` | 0 | empty |
| migration number | `ls src/cobalt/db_migrations` | 0 | ends `0025_dml_roles.rollback.sql`, `0025_dml_roles.sql`, then `__init__.py`, `cli.py`, `dev_rebuild.py`, `placement.py`; no `0026` |
| other 0025 pins | `git diff --stat 40e646ed 91490502 -- tests/cobalt/test_dml_roles_db.py tests/cobalt/test_db_credentials.py tests/cobalt/test_db_apply_db.py` | 0 | empty (the old checked tip ran them as they stand) |
| symbols | Grep `playbook_cli\|hitl_cli\|strike_cli` in `src/cobalt/cli.py` | — | `85: strike_cli import`, `86: playbook_cli import`, `88: hitl_cli import`, `550/551/555: add_parser` |
| symbols | Grep `"strike_alerts": Side.USER\|"cobalt_cos_turns"` in `placement.py` | — | `65: "cobalt_cos_turns": Side.USER,` · `122: "strike_alerts": Side.USER,` |
| wc | `wc -l` | 0 | `cli.py` 593 · `placement.py` 216 · `db_migrations/__init__.py` 205 · `gate-lists.md` 57 · `cli.md` 139 · `placement.md` 88 |
| READ report | `tail -n 3 reports/f21-genesis-check-2026-10-13.md` | 0 | last line `CHECK DONE · job: f21-genesis-1013 · pass: 1 · tip: a19a638a · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 239316` |
| RESTARTS on empty range | `uv run cobalt jobs restarts 91490502..HEAD` | 0 | `RESTARTS: none` |
| red on BASE (CLI) | `uv run cobalt genesis --help` | 2 | `cobalt: error: argument group: invalid choice: 'genesis' (choose from … playbook, cos, agents, hitl, validate)` |
| DEPLOY PROOF before | `ls /Users/cobalt/cobalt/src/cobalt/genesis/cli.py` · `…/store.py` | 1 · 1 | `No such file or directory` (both) |
| merges | `git log --merges --oneline 91490502..HEAD` | 0 | empty |

Card `## RECORDS` (the desk's), copied: R1055 row at `cto-2026-10-11.md:88` (re-read by AUTHORIZATION, above) · drafter reads at `0e3590dc`, `a6c6335c`, `279c99ce` · RESTARTS derivation → `com.cobalt.radar` (re-derived below) · spike gate DONE · migration numbers past HEAD: `0025` by card 448 · pins re-proven at the BASE the desk sets, each going to 0026 (re-proven here: the 18 pin files are byte-equal to `a19a638a` and green) · round-3 re-proof at `279c99ce` · row PORT drafter 835, BASE `91490502` (re-read: `git log --oneline -1`) · `DB` left out (rows take the lock).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (on `91490502`) → `4730 passed, 866 skipped, 4 xfailed, 36 warnings in 797.02s (0:13:17)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.12s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (allowed; it names no `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
The 23 test files of the 42 (3 `test_genesis_*.py`, 2 fixtures, 18 pin files) re-applied first by Write/Edit, each byte-equal to `a19a638a` (`git diff --stat a19a638a -- tests/cobalt/test_genesis_offline.py tests/cobalt/test_genesis_db.py tests/cobalt/test_genesis_experiments_db.py tests/cobalt/fixtures/genesis` → empty after `git add`; `git diff --stat a19a638a -- tests` → only main's own 22 files, none of the 23). No `src/` edit.
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <the 21 test files>` → `43 failed, 201 passed, 171 skipped in 2.36s`. First lines of the reds:
- G1 `test_genesis_chunk_is_declared_on_the_user_side`: `KeyError: "table 'genesis_chunk' has no ruled side. …"` (`placement.py:193`) — the row's reason.
- G2/G3/G4 offline: `ModuleNotFoundError: No module named 'cobalt.genesis'` (`test_genesis_offline.py:43`, `:61`, `:75`, `:129` ×6, `:147`, `:158`, …) — the row's reason.
- G5 `test_the_cli_mounts_import_and_search`: `assert 2 == 0` with `cobalt: error: argument group: invalid choice: 'genesis'` — the row's reason.
- the pins: each wants `0026_genesis_chunk` where FORWARD/REVERSE end at `0025` (the mutation run below quotes one).
With-DB reds: not run here. The card's PORT row puts the with-DB passes on the deploy gate, under the dev lock (ASK DESK 3); the old build proved them red on its own BASE (`a19a638a`'s report), and those files are byte-equal now. No lock taken. Commit `2e8caf75 wip(f21-genesis-fr1): red — …`.

## E3 THE ROWS
Row PORT, one row: the 19 non-test files re-applied by Write/Edit (no merge, cherry-pick, rebase, checkout).

| file | kind | PROOF |
|---|---|---|
| `src/cobalt/genesis/__init__.py`, `chunk.py`, `cli.py`, `search.py`, `store.py` | A | `git diff --stat a19a638a 2cd0219a -- <file>` empty |
| `src/cobalt/db_migrations/0026_genesis_chunk.sql`, `.rollback.sql` | A | empty |
| `src/cobalt/db_migrations/__init__.py` | A | empty |
| `ops/desk/gate-lists.md` | A | empty |
| `docs/40 - DevDocs/cobalt/genesis/__init__.md`, `chunk.md`, `cli.md`, `search.md`, `store.md` | A | empty |
| `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` | A | empty |
| `tests/cobalt/fixtures/genesis/ledger-200.md`, `structure.md` | A | empty |
| `tests/cobalt/test_genesis_offline.py`, `test_genesis_db.py`, `test_genesis_experiments_db.py` | A | empty |
| the 18 pin files: `test_archiver_migrations.py`, `test_assumed_store.py`, `test_dml_roles_offline.py`, `test_drc_d2_fix_r1_db.py`, `test_drc_d3_experiments.py`, `test_drc_k1_store.py`, `test_drc_store.py`, `test_f15_p1_records_offline.py`, `test_legs_migration.py`, `test_p4_migrations.py`, `test_radar_handicap_store.py`, `test_radar_migration.py`, `test_radar_price_floor_db.py`, `test_radar_score_migration.py`, `test_seam_drc_s3_registry.py`, `test_stale_score_db.py`, `test_tenancy.py`, `test_voice_store.py` | A | empty |
| `src/cobalt/cli.py` | B | vs BASE: only `+from cobalt.genesis import cli as genesis_cli  # noqa: E402` after `agents_cli` and `+    genesis_cli.add_parser(sub)` after `hitl_cli.add_parser(sub)`; vs `a19a638a`: only main's 3 imports and its comment line + 3 registrations |
| `src/cobalt/db_migrations/placement.py` | B | vs BASE: only the 4-line `genesis_chunk: Side.USER` hunk after `strike_alerts`; vs `a19a638a`: only main's 6 `MODULE_TABLES` lines |
| `docs/40 - DevDocs/cobalt/cli.md` | B | vs BASE: only the `## 2026-10-19 — f21-genesis-1013` section after main's `## 2026-10-18 — f20-cos-1018`; vs `a19a638a`: only main's f20 section |
| `docs/40 - DevDocs/cobalt/db_migrations/placement.md` | B | vs BASE: only the f21 section after main's f20 section; vs `a19a638a`: only main's f20 section |

PROOF 42 of 42: 38 byte-equal (A), 4 seam files (B). `git diff --name-only 91490502 2cd0219a` → exactly those 42 paths; neither old report is among them.
Seam (1)/(2): main's three imports and its four registration lines stand first, `genesis_cli` after them — the drafter's reading held. (3)/(4): main's f20 section, then the f21 section, each verbatim. (5): main's three `MODULE_TABLES` entries and `genesis_chunk` both stand.

After the row: `uv run pytest -q -p no:cacheprovider --color=no --tb=line <the 21 files> tests/cobalt/test_cos_offline.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `325 passed, 171 skipped in 23.82s`.

THE MUTATIONS (Edit, applied together, one per seam of the port, then undone with Edit): (m1) drop `"genesis_chunk": Side.USER` from `placement.py`; (m2) drop `genesis_cli.add_parser(sub)` from `cli.py`; (m3) drop `0026_genesis_chunk.sql` from `FORWARD`; (m4) drop `conn.autocommit = False` from `store.py`. Run on `test_genesis_offline.py::test_genesis_chunk_is_declared_on_the_user_side`, `::test_the_cli_mounts_import_and_search`, `test_f15_p1_records_offline.py`, `::test_check_o1_replace_is_one_transaction_on_an_autocommit_connection`, `::test_replace_keeps_the_delete_and_the_insert_on_one_non_autocommit_transaction`, `test_seam_drc_s3_registry.py` → `7 failed, 5 passed in 0.60s`, each for its own mutation:
- m1: `KeyError: "table 'genesis_chunk' has no ruled side. …"` (`placement.py:196`); `test_placement_carries_both_lanes…`: `assert ['drc_events'...trike_alerts'] == ['legs', 'pre...enesis_chunk']`
- m2: `assert 2 == 0` with `invalid choice: 'genesis'`
- m3: `AssertionError: assert '0025_dml_roles.sql' == '0026_genesis_chunk.sql'` (`test_f15_p1_records_offline.py:29`); `test_the_union_tail…`: `At index 0 diff: '0014' != '0015'`
- m4: `AssertionError: the DELETE committed alone: the source lost its rows and gained none` (`test_genesis_offline.py:312`); `AssertionError: [('execute', True), ('executemany', True)]` (`:354`)
Undone: `git diff --stat a19a638a -- src ops/desk/gate-lists.md "docs/40 - DevDocs/cobalt/genesis" "docs/40 - DevDocs/cobalt/db_migrations/__init__.md" tests/cobalt/test_genesis_offline.py` → only main's own files (`cli.py` 7+, `placement.py` 6+, the cos/hitl/agents/… set), the tree back at the fix. Commit `2cd0219a feat(f21-genesis-fr1): port Genesis chunk 1 …`.

## RESTARTS
`uv run cobalt jobs restarts 91490502..HEAD` → 43 rows: every `docs/` path `DOCS -`; `ops/desk/gate-lists.md` `operator script; no Cobalt reader -`; the two `.sql` `non-Python src asset -`; `src/cobalt/cli.py`, `db_migrations/__init__.py`, `db_migrations/placement.py` and the five `src/cobalt/genesis/*.py` `static import reach com.cobalt.radar`; every `tests/` path `test/documentation; no resident -`. No UNCLASSIFIED row. Last line: `RESTARTS: com.cobalt.radar` (the card header's).

## W THE THREE SUITES
`<tip>` = `2cd0219a`. The card's PORT row names the suites: its own `## DEPLOY PROOF` lines, then the `## OFFLINE` line of `ops/desk/gate-lists.md` as written. PASS 1 and PASS 2 stay with the deploy gate (ASK DESK 3; DECISION 1).
- genesis tests · `uv run pytest -q tests/cobalt/test_genesis_offline.py` → `19 passed in 0.45s`, 0 failed.
- genesis CLI · `uv run cobalt genesis --help` → exit 0: `usage: cobalt genesis [-h] {import,search} ...` with `import  Chunk each markdown file and replace its rows (all read before any write)` and `search  The one recall entry: ranked chunks for a question`.
- the two `ls` lines, in this worktree after the port: `ls /Users/cobalt/cobalt-wt/f21-genesis-fr1/src/cobalt/genesis/cli.py` → the path; `…/store.py` → the path. The card's `/Users/cobalt/cobalt/src/cobalt/genesis/…` paths are the main checkout; they read `No such file or directory` until the deploy (PREFLIGHT) and flip at the deploy (RECORDS).
- (a) OFFLINE, the `## OFFLINE` line as written: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4749 passed, 871 skipped, 4 xfailed, 36 warnings in 786.88s (0:13:06)`; 0 failed, 0 errors; `grep -n -F "OUTSIDE"` → none. Against E0: +19 passed (the Genesis offline tests), +5 skipped (`test_genesis_db.py:50`, `:85`, `:113`, `:136`, `test_genesis_experiments_db.py:29`: `Postgres env settings not available`, the with-DB tests outside a lock).
- OFFLINE OPS (`gate-lists.md` changed): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4026 passed, 1 xfailed, 16 warnings in 947.75s (0:15:47)`; 0 failed.
- (e) LIVE-NOTE, `.env` absent, the `## LIVE-NOTE` line: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py tests/cobalt/test_playbook_live.py` → `147 passed, 1 skipped, 15 warnings in 28.04s`; the skip: `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (allowed).
- (b)–(d), (f): not run. `cobalt_dev: not taken`. `ls /Users/cobalt/cobalt-wt/f21-genesis-fr1/.env` → `No such file or directory` (09:43 EDT).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: E2's 43 reds on BASE for the rows' reasons (KeyError, `ModuleNotFoundError: cobalt.genesis`, `invalid choice: 'genesis'`, pins wanting `0026`); E3's m1–m4 mutations turned 7 named tests red, each for its own mutation (quoted in E3). The with-DB tests were not run in this build (DECISION 1); they are byte-equal to the checked `a19a638a`, whose build showed them red and green.
(2) Entry paths: `Grep genesis src/cobalt/cli.py` → `90: from cobalt.genesis import cli as genesis_cli` and `557: genesis_cli.add_parser(sub)`; `Grep "Vault/Think|modelaccess|openai|public." src/cobalt/genesis` → none. The CLI mount is pinned by `test_the_cli_mounts_import_and_search`, import/search output by `test_the_cli_import_prints_one_line_per_source` and `test_the_cli_search_prints_source_and_line_range`, the placement by `test_genesis_chunk_is_declared_on_the_user_side`, and the registry by the 18 pin files.
(3) Re-read at the tip: `git show 2cd0219a:src/cobalt/db_migrations/__init__.py` (FORWARD ends `0026_genesis_chunk.sql`, REVERSE begins with its rollback, docstring `:111-114`); Grep `placement.py` → `:65 "cobalt_cos_turns"`, `:126 "genesis_chunk": Side.USER`; `git diff --stat a19a638a 2cd0219a -- <the 38>` empty; `git diff --name-only 91490502 2cd0219a` → 42 paths.

## FOR THE CHECK
- Range `91490502..2cd0219a`: `2e8caf75 wip(f21-genesis-fr1): red — Genesis tests and pins ported from a19a638a (PORT)` · `2cd0219a feat(f21-genesis-fr1): port Genesis chunk 1 from a19a638a onto main by Edit/Write (PORT; G1-G6 content; L79, R1485, R2013)`. The report commit follows them.
- P1: the E3 table (one PROOF line per file); `git diff --stat a19a638a 2cd0219a -- <the 38>` empty; `git log --merges --oneline 91490502..HEAD` empty; neither `f21-genesis-build-2026-10-13.*` is in `git diff --name-only 91490502 2cd0219a`.
- P2: `git diff 91490502 -- <the 4 B files>` shows only Genesis's own hunks (quoted in E3), and `git diff a19a638a -- <the same>` shows only main's.
- P3: `ls src/cobalt/db_migrations` at BASE ends `0025`; FORWARD/REVERSE/docstring at tip quoted in self-check (3); the 18 pin files are byte-equal and green.
- P4: the W lines above; RESTARTS table under `## RESTARTS`.
- Reds, mutations, greens: E2, E3. Callers: self-check (2). RUN row G6: not run in this build (with-DB, DECISION 1); the checked build's G6 output stands in `f21-genesis-build-2026-10-13.md`.
- `<F0>` / `<F1>` / `<F2>`: not run (no lock taken). Lock taken / released: not run.

## CONTINUE
next: none (CLOSE done)

## DECISIONS
- DECISION 1 — the with-DB suite was not run in this build. BUILD-HUB `## W` gates every card but "DB: none" with `gate.sh … all --deploy`. Card 468's PORT row, though, says the with-DB passes `## PASS 1` and `## PASS 2` "stay the deploy gate's own, under the dev lock" (ASK DESK 3), and lists only the OFFLINE line. Safe default taken: follow the card (L72, a seam stated in the card). No lock taken; `with-DB 0/0` and `cobalt_dev: not taken` in the stop line. `test_genesis_db.py` and `test_genesis_experiments_db.py` (G6) run first at the deploy gate's PASS 2. If the desk wants them at build, `CONTINUE: W` runs `gate.sh f21-genesis-fr1 all --deploy`.

## RECORDS
- Launch message `CONTINUE: PORT.` on a fresh session with no report on disk: RECOVERY's first reads run (`git status --short --branch` → `## ops/f21-genesis-fr1`; `git log --oneline -3` → `91490502` at top; `ls -la .env` → No such file), then AUTHORIZATION and PREFLIGHT as on a first launch, then PORT (the card's ORDER: "launch `build` at `PORT`").
- L74: one system-reminder block asked for a `Claude-Session:` line on commits; recorded under `## L74`, not followed.
- ASK DESK 2 of the drafter (the card): `cli.md`'s Genesis text says `after the playbook import`, but the import now sits after main's `agents_cli` import. The text stands verbatim, as the card rules.
- DEPLOY PROOF `ls /Users/cobalt/cobalt/src/cobalt/genesis/{cli,store}.py` name the main checkout. They read `No such file or directory` at 09:0x (PREFLIGHT) and turn into the path only after the deploy. Their worktree equivalents return the path (W).
- Mutations m1–m4 were applied together in one Edit set and one run, each on its own file with its own named test red. All four were undone by Edit before the commit, and none was committed.
- `.env`: never present in this worktree (PREFLIGHT, W 09:43 EDT). No lock taken.
- `desk-context.sh` read 271277 at the last step, above the desk's 250,000 line; the session went on to CLOSE.
- The card's records, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f21-genesis-fr1 · tip: 2cd0219a | on 91490502 | migration: 0026, never applied (DECISION 1) | offline 4749/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 (PROOF 42: 38 byte-equal, 4 seam) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 271277
