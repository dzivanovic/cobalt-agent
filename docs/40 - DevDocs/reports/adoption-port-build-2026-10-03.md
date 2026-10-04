# adoption-port — build report 2026-10-03

## §0 Headline
- All three rows are built on `a8d8a848`. P1: 54 chain files are byte-equal to `9694a679`, proven by `git diff` against the chain's blobs, and the red `test_migrate_level.py` is committed (red on BASE offline and with-DB, F0 = F0 after). P3: both sides stand. P2: `02b`'s three lines, every chain hunk and the four ruled sentences are in, each grep is one hit.
- STOPPED at E3. The card's rows contradict each other. P2 (8) extends the deploy flag; P1 keeps `tests/ops/test_hub_lines.py` byte-equal and needs `tests/ops` green; that test pins the flag's ending. Two reds; the other 751 pass.
- The desk amends the card (DECISION E3: A or B), then `CONTINUE: E3`. Lock released, `.env` gone, `cobalt_dev` untouched (F0 = F0).

## L74
- 21:47 ET: a system block in this session asks commits to carry a `Claude-Session:` line. DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Sat Oct  3 21:47:08 EDT 2026`

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (none) |
| card placeholder | `grep -n -E "«FIL[L]" "<card>"` | 1 | (none) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` | 0 | `a65902d34e87d11bd39d69b86019eb0a11593e84` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (none) |
| STANDING R60 (09-30) | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | line 46, `**HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (10-02) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | line 54, `HIS RULING (direction row 10; L73 over L67 house A) … | HIS RULING · APPROVED |` |
| R47 committed | `git … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 (10-02) | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | line 161, `HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock … | HIS RULING · APPROVED |` |
| R154 committed | `git … log -1 --format=%H -S"| R154 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 (10-02) | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | line 164, `HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included … | HIS RULING · APPROVED |` |
| R157 committed | `git … log -1 --format=%H -S"| R157 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R3 (10-03) | `grep -n "^| R3 " ".../cto-2026-10-03.md"` | 0 | line 9, `HIS RULING: every Grok seat runs grok-4.7 … | HIS RULING · APPROVED — pending fold |` |
| R3 committed | `git … log -1 --format=%H -S"| R3 |" -- ".../cto-2026-10-03.md"` | 0 | `3727a00454268f485f97fdeccb8f9cc428e86113` |

All match. Laws read: this hub, the card, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down.

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Sat Oct  3 21:47:08 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-port-1003` + `?? "docs/40 - DevDocs/reports/adoption-port-build-2026-10-03.md"` (this report, the hub's first Write; no other line) |
| base | `git log --oneline -1` | 0 | `a8d8a848 Merge branch 'main' into deploy/set2d-1003` |
| branch from main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 ops/adoption-port-1003` | 0 | `a8d8a848 Merge branch 'main' into deploy/set2d-1003` |
| diff vs base | `git diff --stat a8d8a848` | 0 | (none) |
| base stat | `git show --stat a8d8a848` | 0 | `Merge: 7f0b2efa ffd0b1be` · `docs/40 - DevDocs/reports/deploy-set2d-1003.md | 133 +++` · `1 file changed, 133 insertions(+)` |
| .env here | `ls /Users/cobalt/cobalt-wt/adoption-port-1003/.env` | 1 | `ls: …/adoption-port-1003/.env: No such file or directory` |
| .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| chain files | `git diff --name-status a09f0862..9694a679` | 0 | 56 paths: 45 `M`, 11 `A` (`adoption-hubs-build`, `adoption-scripts-b2-build`, `adoption-scripts-build` reports, `ops/desk/desk-list.sh`, `ops/desk/gate-lists.md`, `tests/cobalt/test_migrate_level.py`, `tests/ops/test_desk_context.py`, `test_desk_launch_recut.py`, `test_desk_list.py`, `test_hub_lines.py`, `test_locale.py`); **no `D`** — nothing to delete |
| main since a09f0862 | `git diff --name-only a09f0862..a8d8a848` | 0 | 66 paths; the two that are also chain paths: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (matches the card's P2/P3) |
| chain head | `git show --stat 9694a679` | 0 | `docs(adoption-scripts-b): build report — b7eeb80c` |
| chain base | `git log --oneline -1 a09f0862` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| `restarts.py:38` | `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` · `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| `restarts.py:225`, `:245` | Read 220–249 | — | `225: if not rule and (path.startswith("docs/") or path in ROOT_DOCS):` → `DOCS`; `245: if not rule and path.startswith("tests/"):` → `246: rule = "test/documentation; no resident"` |
| `03`'s RESTARTS for cli.py | `git show "9694a679:docs/40 - DevDocs/reports/adoption-scripts-build-2026-10-03.md"` (the file is a chain file, absent at BASE: the plain `grep -n -F "cli.py" "<that path>"` exit 2 `No such file or directory`), Grep of the output | 0 | line 165: ``src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar``. … `Last line: RESTARTS: com.cobalt.radar.` |
| sizes | `wc -l ".../DEPLOY-HUB.md" ".../CTO-DESK-WAKEUP.md"` | 0 | `186` · `49` (the other edited paths are whole-file ports; their sizes are `git diff --stat=200 a09f0862..9694a679`: 56 files, 2714 insertions(+), 311 deletions(-)) |
| READ tail | `tail -n 3 ".../adoption-hubs-decisions-2026-10-03.md"` | 0 | last: `FOR THE CHECK (card 02 ## RECORDS): Build decisions 1–11 answered (…): 2, 3, 4, 9 are card 03c's rows; A3 amended (--deploy call; the equal-tree clause only with a with-DB count above 0); rows A7 (no hold to the stop line) and A8 (P1 (v) re-read at STEP-R) added; 1, 8, 10, 11 KEEP; 7 is not his.` |
| READ tail | `tail -n 3 ".../deploy-hub-text-decisions-2026-10-03.md"` | 0 | last: `FOR THE CHECK (card 02b ## RECORDS): Grok's 8 findings answered (…): 1–4 fixed in the P7, STEP-T and STEP-C sentences; T2–T5 cut from this card and carried to 03d; the card is the P7/T/C fix only.` |
| READ tail | `tail -n 3 ".../adoption-scripts-b-check-2026-10-03.md"` | 0 | last: `CHECK DONE · job: adoption-scripts-b · pass: 1 · tip: b7eeb80c · … · ready: YES · decisions: 3 · for Dejan: 0` |
| READ | `13b-slot-guard-port-card.md` | — | read whole (port shape: Write from `git show`, byte-equality proof, settled files by hand) |
| RESTARTS empty | `uv run cobalt jobs restarts a8d8a848..HEAD` | 0 | one row, this untracked report `DOCS -`; `RESTARTS: none` |

Card `## RECORDS` copied: (1) judge 10-03 21:39 ET — set 3 = `03d`, `11b`, `07b`, `05`, `10`; Grok read of the `DEPLOY-HUB.md` part after the check. (2) the chain's three checks stand for the byte-equal files. (3) RESTARTS homes — `ops/desk/*` → `OPS_DESK_PREFIX` (re-read: `restarts.py:38`, `:230`); tests → `:245` (re-read); `docs/**` → `:225` (re-read); `cli.py` → `static import reach com.cobalt.radar` (re-read, `03`'s report line 165). (4) desk preflight `03d-card-preflight-2026-10-03.md` issues answered by the card's edits (not re-read: a desk file).

PROVEN BY FIRST REAL USE: the table in the hub, unchanged.

The `<FP>` string, copied whole before the first run:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
- Offline on `a8d8a848`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 578.52s (0:09:38)`, exit 0. 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.47s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).
- tests/ops on BASE (the card's P1 names it): `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 239.84s (0:03:59)`.

## E2 RED
- Written: `tests/cobalt/test_migrate_level.py` from `git show 9694a679:tests/cobalt/test_migrate_level.py` (Write). After the commit, `git diff --stat 9694a679 HEAD -- tests/cobalt/test_migrate_level.py` → nothing (the blobs are equal).
- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_migrate_level.py` → `11 failed, 1 passed, 1 skipped in 0.08s`. Each red is P1's reason (the LEVEL lines are absent on BASE): `AttributeError: module 'cobalt.db_migrations.cli' has no attribute '_tables_line'` (6 tests), `… '_table_creators'` (4), `… 'FINGERPRINT_SQL'` (1). Negative control `test_src_prints_no_level_word_and_no_0013` PASSES on BASE. Skip: `tests/cobalt/test_migrate_level.py:188: Postgres env settings not available` (the with-DB test, run below).
- With-DB, ONE lock take: `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh adoption-port-1003 90` → `lock taken: adoption-port-1003` exit 0 (22:04:03 ET); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `…/adoption-port-1003/.env`. `<FP>` → **F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`**. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed; every 0014+ table (`drc_*`, `legs`, `prediction_records`, `voice_turns`) `-`; `NOTHING WAS APPLIED`; `code: a8d8a848 (DIRTY: 2 path(s))` — BASE's proof-only prints no level line (that is the red); the table picture is `0013`. No forward. `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_migrate_level.py` → `12 failed, 1 passed in 7.33s`; the with-DB red: `test_migrate_level.py:193: ValueError: not enough values to unpack (expected 1, got 0)` — no `TABLES ` line in BASE's proof-only output. `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh adoption-port-1003` → `lock released`; `ls …/adoption-port-1003/.env` → `No such file or directory` (22:04:53 ET).
- Commit `4a60ab02 wip(adoption-port): red — test_migrate_level.py from 9694a679 (P1)`.

## E3 THE ROWS
**P1 — THE PORT** (built; not yet committed — in the wip commit). 56 chain paths (`git diff --name-status a09f0862..9694a679`), none deleted; the 54 that `main` did not touch since `a09f0862` were written to `9694a679`'s bytes: modified files by Edit, hunk by hunk from `git diff a09f0862 9694a679 -- <path>` (the worktree file equals `a09f0862` for these paths), or written whole from `git show 9694a679:<path>` (`gate.sh`, `test_gate.py`, `test_pass1_db_only.py`, `BUILD-HUB.md`, `CHECK-HUB.md`); added files written whole from `git show`. The proof of each pair is `git diff 9694a679 -- <path>` → nothing (modified, worktree against the chain blob) or `git add <path>` then `git diff --cached 9694a679 -- <path>` → nothing (added) — the card's `git hash-object`/`git rev-parse` pair is on no listed string (ASK DESK 1). Results, each `(none)`:
- `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `prompts/CARD.md`, `prompts/DEVFIX-HUB.md`, `prompts/STANDING-LIST.md` (mine); `prompts/BUILD-HUB.md`, `prompts/CHECK-HUB.md` (a sub-agent of this session); the 24 modified `ops/desk/*.sh` and the added `ops/desk/desk-list.sh`, `ops/desk/gate-lists.md` (a sub-agent); the 11 modified and 5 added `tests/ops/*` (a sub-agent); the three added `reports/adoption-*-build-2026-10-03.md` (a sub-agent). `tests/cobalt/test_migrate_level.py`: `git diff --stat 9694a679 HEAD -- …` → nothing (E2's commit).
- `git diff --stat 9694a679 -- ops/desk` lists only `main`'s own `deploy-outage.sh`, `deploy-smoke.sh`, `deploy-step0.sh` (not chain paths); `git diff --stat 9694a679 -- tests/ops` lists only `main`'s `conftest.py`, `test_conftest_guard.py`, `test_deploy_outage.py`, `test_deploy_smoke.py`, `test_deploy_step0.py`. No mode change shown.
- `git status --short` → 55 changed chain paths (45 ` M`, 10 `A `; the 56th, `test_migrate_level.py`, is E2's commit) plus this report `??`.

**P3 — `CTO-DESK-WAKEUP.md`** (built). Edit adds the chain's `--append-system-prompt "…"` flag to the LAUNCH line. `git diff a8d8a848 -- <path>` → one hunk, the LAUNCH line only (the chain's line). `git diff 9694a679 -- <path>` → two hunks, STEP 0 item 2 (the stuck-REFRESH sentences) and READ item 7 (`A record only (his 10-03 R78)`), `main`'s lines only. `grep -c -F "A call the hook blocks is NOT A REFUSAL: resend it as single calls." <path>` → `1`; `grep -c -F "A record only (his 10-03 R78)" <path>` → `1`.

**P2 — `DEPLOY-HUB.md`** (built). The chain's hunks applied by Edit onto `main`'s text; `main`'s P7, STEP-T and STEP-C lines are untouched by the chain, so no sentence overlaps. Before the four ruled sentences: `git diff --stat 9694a679 -- <path>` → `3 insertions(+), 3 deletions(-)` and `git diff -U0 9694a679 -- <path>` → exactly lines 63 (P7), 83 (STEP-T bullet), 87 (STEP-C) — `02b`'s words; `git diff --stat a8d8a848 -- <path>` → `22 insertions(+), 26 deletions(-)` (the chain's own stat for this file was 48 lines). Then the four ruled sentences:
- (5) line 102, THE GATE, ONE CALL (exits 4, 5, 6, 1): the bullet now ends `…; 1 → a red, below; the release is \`gate.sh\`'s trap on every exit; verify \`<GATE>/.env\` gone and the lock dir absent, then the FAILED line.` — `grep -n -F` → one hit, line 102.
- (6) THE EQUAL-TREE CLAUSE: the card's sentence verbatim; `grep -c -F "AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole (\`--deploy\`)"` → `1`. Kept from the chain: `quote them from the check report with its path and skip (a)–(f)` and `The clause applies only when …` (ASK DESK 2).
- (7) P1 (v): the card's sentence verbatim; `grep -c -F` of `AND an empty derived restart set, provisional at P1; STEP-R re-reads the SET and fails \`window (v) does not hold: <labels>\` when it is not empty and P1 was outside (i)–(iv)` → `1`. Kept from the chain: `any hour (his 2026-10-02 ruling, row 9; …)` and the `provisional` sentence (ASK DESK 2).
- (8) the launch line's flag now ends `… resend it as single calls. Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5."` — `grep -c -F` → `1`.
- `grep -c -F "MIGRATIONS_DIR / \"00" <path>` → `0`.

**Row tests**: `uv run pytest -q -p no:cacheprovider --color=no tests/ops tests/cobalt/test_migrate_level.py tests/cobalt/test_migrate_proof.py` → **`2 failed, 751 passed, 22 skipped, 1 xfailed, 15 warnings in 260.17s (0:04:20)`**:
- `FAILED tests/ops/test_hub_lines.py::test_each_line_carries_the_flag_once[DEPLOY-HUB.md]` — `tests/ops/test_hub_lines.py:95: AssertionError` … `assert 0 == 1` where `0 = …count('--append-system-prompt "ONE bare command per Bash call: … resend it as single calls."')`
- `FAILED tests/ops/test_hub_lines.py::test_a_dry_launch_of_each_kind_prints_a_line_holding_the_flag[deploy]` — `tests/ops/test_hub_lines.py:228: AssertionError`, the same `assert 0 == 1`.
- `tests/ops/test_locale.py` alone (57 passed) — `main`'s three new `ops/desk/` scripts pass the chain's `LC_ALL=C` test.
The cause is in the card, not in the port: `test_hub_lines.py` (a chain file P1 holds byte-equal) pins `FLAG_SRC` = the flag WITH its closing quote right after `single calls.` on every hub line, and P2 (8) appends a sentence inside that quote on the deploy line. P1 (`tests/ops` green, the file byte-equal) and P2 (8) cannot both hold; the test is in no row's `files`. STOPPED here (UNATTENDED RULES (b)): DECISION E3 below.

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E3 — the row tests again after the desk's card change (DECISION E3), then the MUTATIONS, the module DevDocs lines (the port's `cli.md` line is the chain's own, already in place) and the `fix(adoption-port):` commit. P1, P2, P3 are built and sit in the wip commit; nothing is to be redone.

## DECISIONS
- **DECISION E3 (blocks the next step; the card's two rows contradict):** P2's ruled sentence (8) puts `Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5.` INSIDE the deploy line's `--append-system-prompt "…"`. P1 holds `tests/ops/test_hub_lines.py` byte-equal to `9694a679` and requires `tests/ops` green; that test's `FLAG_SRC` ends `single calls."` and is asserted once on every hub line, so two tests go red (E3, quoted). Not settled here: the test is in no row's `files`, and moving sentence (8) out of the flag re-decides a ruled sentence (L72, THE ROWS). The two ways the desk can amend the card, either one then `CONTINUE: E3`: (A) add `tests/ops/test_hub_lines.py` to P2's `files` with the one change "the deploy line's flag is `FLAG` plus sentence (8)" (P1's byte-equality then excludes that file, as it does `DEPLOY-HUB.md`); or (B) rule that sentence (8) sits outside the flag (e.g. a sentence after the launch line). Safe default taken: stop with every row built and the two reds left visible; nothing is weakened. Not his unless the desk reads (B) as changing his ruled text.
- ASK DESK 1 [22:17 ET]: P1 names `git hash-object <path>` = `git rev-parse 9694a679:<path>`; neither is a listed string. Default taken: the listed equivalent — `git diff 9694a679 -- <path>` (worktree against the chain's blob) or `git diff --cached 9694a679 -- <path>` (added, staged) printing nothing; after the commit, `git diff --stat 9694a679 HEAD -- <paths>` printing nothing compares blob ids. The commands were not tried (each a refusal under dontAsk).
- ASK DESK 2 [22:17 ET]: two glue phrases in neither parent, to keep the chain's sentences beside ruled sentences (6) and (7) without changing the ruled words: (6) `When the clause holds: ` before the chain's `quote them from the check report with its path and skip (a)–(f).`, and `; his 2026-10-02 ruling, row 8` moved into the clause's heading parenthesis; (7) `Under (v) ` before the chain's `any hour (his 2026-10-02 ruling, row 9; …)`. Default taken: keep both chain sentences with that glue (dropping them would lose chain text, X2). The check reads them.

## RECORDS
- `.env: removed, proven gone (E2)`.
- REFUSED, not needed: `git grep -n -F "resend it as single calls" 9694a679 -- ops tests docs/40*prompts` — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` Read instead with the Grep tool over the `adoption-scripts-b2-1003` worktree and `git show 9694a679:tests/ops/test_hub_lines.py`.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/adoption-scripts-b2-1003 log --oneline -1` — the same dontAsk refusal. Not needed: every chain file is read by `git show 9694a679:<path>`.

FAILED: E3 — P2 (8) and P1 contradict — tests/ops/test_hub_lines.py:95 and :228 `assert 0 == 1` (FLAG_SRC on the DEPLOY-HUB.md line); the test is in no row's files · decisions: 3 · for Dejan: 0
