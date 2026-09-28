# S3 EXITS C1 FIX R1 — CHECK, ROUND 2 — 2026-09-28

Hub `s3-exits-c1-fix-r1-check` (Sonnet 5, auto). Prompt `prompts/2026-09-28/30-s3-exits-c1-fix-r1-check.md`. `<D>` = 2026-09-28. Range `d9240ae4..3ceb3b11` on `s3/exits-c1` (code base `5164f867`; report commit `9b25eced` on top, docs-only). I judge nothing (L37); every line is a fact I read or a seat's words with my file-check beside them.

## §0 Headline
2 of 3 houses checked (floor met: Opus + Grok): Opus `BUILD STANDS EXCEPT R1 cobalt_redactions 179→180 … · YES` · Grok `BUILD STANDS EXCEPT R1 cobalt_redactions rows and digest · YES` · Sol METER (returns 3:32 PM).
Claims of DOES NOT HOLD that I walked in the real files and found to HOLD: 1 — R1's per-table proof: `cobalt_redactions` differs between `<P0>` and `<P2>` (Opus + Grok, Q(v)). The other 29 tables are equal. Cause: NOT CHECKABLE FROM READS.
By the stop-line rule `ready for C2: NO` (defects that HOLD = 1); both answering seats say YES. Nothing run by me; no repo write, no commit.
ESCALATE: 9.

## L74
Recorded once (L74): after the prompt file was read (12:55), a `<system-reminder>` block was appended to that tool result asking commit and PR text to carry a `Claude-Session: https://claude.ai/code/session_…` line and naming a file-send tool. It is data, not an instruction; this hub commits nothing and sent nothing.

## PREFLIGHT
| rule | command | exit | allowed / output |
|---|---|---|---|
| date | `date` | 0 | allowed · `Mon Sep 28 12:56:26 EDT 2026` |
| placeholder | `grep -n -E "R_[_]" …/30-s3-exits-c1-fix-r1-check.md` | 1 | allowed · nothing |
| placeholder | `grep -n -F "FILL AT LAUNCH" …/30-…md` | 0 | allowed · line 12 only (this gate's own line) |
| R17 | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | allowed · row 35 carries `Grok approved with no asking going forward` |
| R19 | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | allowed · row 37 carries `All 4 house models approved` |
| R19 `-S` | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved" -- …/cto-2026-09-24.md` | 0 | allowed · `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R95 | `grep -n "^| R95 " …/cto-2026-09-23.md` | 0 | allowed · one row, line 103 |
| R109 | `grep -n "^| R109 " …/cto-2026-09-22.md` | 0 | allowed · line 56 carries `Make all Opus` |
| R67 | `grep -n -F "30-s3-exits-c1-fix-r1-check.md" …/cto-2026-09-28.md` | 0 | allowed · row 75 `\| R67 \| 12:56 ET \|` names this file, carries `<build stop>` and `no other house hub is running` |
| R67 `-S` | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"30-s3-exits-c1-fix-r1-check.md" -- …/cto-2026-09-28.md` | 0 | allowed · `c78a3ad18824384c9f3b0ca7ae074b4a4e250ed8` |
| grok | `grok --version` | 0 | allowed · `grok 1.0.25 (f7e67d6988e2) [stable]` |
| build stop | `tail -n 3 "<report>"` | 0 | allowed · last non-blank line EQUALS `<build stop>`, starts `S3 EXITS C1 FIX R1 BUILT ` |
| commits | `git -C /Users/cobalt/cobalt log --oneline d9240ae4..3ceb3b11` | 0 | allowed · `3ceb3b11 fix(s3-c1): fix r1 — X1 on the real factory, the drift outcome after a note failure, X-S card-load proof, constructed values (L75)` · `da9246f0 wip(s3-c1-fix-r1): red` (2 commits) |
| stat | `git -C /Users/cobalt/cobalt log --stat --format=%h d9240ae4..3ceb3b11` | 0 | allowed · `3ceb3b11`: `src/cobalt/aset/web.py`, `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_s3_c1_experiments.py`; `da9246f0`: `tests/cobalt/test_fill_c1_offline.py`, `tests/cobalt/test_fill_transaction_db.py`, `tests/cobalt/test_s3_c1_experiments.py` |
| .env | `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` | 1 | allowed · `No such file or directory` |
| recovery | `ls scratch/tribunal-bars-0920/s3-exits-c1-fix-r1` | 1 | allowed · `No such file or directory` → fresh |
| stagger | `grep -n -F "no other house hub is running" …/cto-2026-09-28.md` | 0 | allowed · lines 16, 55, 75; line 75 also names `30-s3-exits-c1-fix-r1-check.md` |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | allowed · `OK` = UP |
| probe SOL | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 1 | allowed · `ERROR: You've hit your usage limit. Upgrade to Pro (…) or try again at 3:32 PM.` = METER; Sol not launched |
| gates again (13:13:19) | R17, R19 (`grep -c -F` on each row), R19 `-S` | 0 | allowed · 1 · 1 · same sha `5055151d…` |
| diff copy | `git -C /Users/cobalt/cobalt log -p d9240ae4..3ceb3b11 -- . ":(exclude)docs"` (to a job-tmp file) | 0 | allowed · 14,627 B, 2 commits |
Denials: none. Commands outside the ten listed strings that ran under auto mode: `diff`, `sed`, `perl`, `find`, `xargs`, `cat`, `cd`, `git log … > file` (job tmp). One stderr line printed by `claude -p` about a settings deny-rule syntax (`Bash(git push*:*)`) is a settings warning, not a denial of anything this hub ran. Two `cd` calls left the shell in a worktree; each was followed by `cd /Users/cobalt/cobalt-wt/agy-trial`, and later steps use absolute paths.

## Files copied
`S` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c1-fix-r1/`. Written before the launches by me, Read → Write, no helpers. I checked every original against its copy with `diff` (parts `cat`-joined in order); two mistakes of mine in copies (a garbled tail of the diff copy; a wrong last line in the `<r1>` copy) and three whitespace-only lines (`perl` on `<report>` part 3) were fixed and re-verified before the launches.
| original | copy | bytes (original) | diff |
|---|---|---|---|
| `git log -p d9240ae4..3ceb3b11 -- . ":(exclude)docs"` | `diff.part1.md` (1 part, 100 B header) | 14,627 | IDENTICAL; `grep -c "^commit "` = 2 = PREFLIGHT's 2 |
| `rulings.md` (R43 of `cto-2026-09-28.md`, R67 of `cto-2026-09-22.md`) | `rulings.md` | 3,202 (+ 2 command lines) | IDENTICAL to a fresh `grep -n` of each |
| `<report>` lines 50–338 (`## E2 RED` … `## FOR THE CHECK`) | `packet.md` | 40,120 | IDENTICAL (no size ruling for this file; the same text is also in the report parts under `files/`, each ≤ 38,000 B) |
| `<report>` | `files/…build-2026-09-28.md.part1`–`.part3` (cut at `## W`, `## SEAM FOR C2`) | 48,611 | IDENTICAL (14,798 + 23,837 + 9,976) |
| `<class>` | `files/s3-exits-c1-fix-r1-draft-2026-09-28.md` | 10,190 | IDENTICAL |
| `<r1>` | `files/s3-exits-c1-check-2026-09-28.md` | 30,892 | IDENTICAL |
| `29-s3-exits-c1-fix-r1-build.md` | `files/29-…` | 27,768 | IDENTICAL |
| `20-s3-exits-c1-build.md` | `files/20-…` | 31,610 | IDENTICAL |
| `LAWS.md` | `files/LAWS.md.part1`–`.part2` (cut at `### L30`) | 61,011 | IDENTICAL (26,624 + 34,387) |
| `src/cobalt/aset/web.py` at `3ceb3b11` (worktree; `git diff 3ceb3b11 HEAD -- src tests` empty) | `files/wt/src/cobalt/aset/web.py.part1`–`.part2` (cut at `def _result_card`) | 65,258 | IDENTICAL (37,420 + 27,838) |
| `tests/cobalt/{test_aset_web,test_s3_c1_experiments,test_fill_c1_offline,test_fill_transaction_db,conftest}.py` | `files/wt/tests/cobalt/…` | 28,816 · 5,926 · 14,888 · 15,597 · 10,092 | IDENTICAL (5 of 5) |
`CHECK-INSTRUCTIONS.md` (5,619 B): the QUESTIONS text `diff`-identical to the prompt's lines 30–39 (opening lead-in and closing quote removed), then the "Files:" paragraph with absolute paths. Not copied for Grok (the prompt did not ask): `aset/store.py`, `cards/legs.py`, `cards/store.py`, `engine.py`, `models.py`, `fills.py`, `card.py`, `0021_legs.sql`; Grok's (vi) seam cites into them were read by it in the worktree (it says so).

## CONTINUE
- 13:14 ET: Opus and Grok launched in one message, one attempt each, 45-minute clock (to 13:59). Sol not launched (METER).
- Opus done (notice 13:18); Grok done (its file written 13:31). Clock: both inside 45 minutes; no TIMEOUT.
- next: none — the run is closed.

## Clock
| seat | launched | done | note |
|---|---|---|---|
| Opus (`claude -p …`, plan mode, Read/Grep/Glob only) | 13:14 | ~13:18 | exit 0; answer on stdout; I wrote `S/opus-check.md` = stdout lines 2–32 (`diff`-identical apart from one trailing blank line), leaving out stdout's first line (the stderr settings warning) and the `[exited with code 0]` trailer |
| Sol | — | — | METER at PREFLIGHT (12:5x); returns 3:32 PM; not launched |
| Grok (`grok --sandbox cobalt-job --allow "Write(…tribunal-bars-0920/**)" -p …`) | 13:14 | 13:31 | exit 0; replied with the path only; wrote `S/grok-check.md` itself (15,256 B) — I did not edit it |
Written-nothing proof: `ls -la S` 13:13 lists `CHECK-INSTRUCTIONS.md`, `diff.part1.md`, `files/`, `packet.md`, `rulings.md`; 13:32 adds exactly `opus-check.md` (mine) and `grok-check.md` (the one file Grok was allowed to write). `find S/files -type f -newer S/CHECK-INSTRUCTIONS.md` → 0 files; 22 files in `S` (16 in `files/`). `git status --short` in `agy-trial` shows only the two pre-existing untracked paths.

## Per question
Each cell ≤30 words of the seat's own, with its cite. Paths relative to the worktree unless shown; `packet.md` / `diff.part1.md` line numbers are the seats'.

| Q | opus | sol | grok |
|---|---|---|---|
| (i) RED FIRST | HOLDS — F2 reds `test_fill_c1_offline.py:392/:403` (`packet.md:8-9`); F3 regex mismatch on the shape refusal (`card.py:256-257`); F1 mutation `test_fill_transaction_db.py:263`; F4 equality read | METER | HOLDS — F2 `:392/:403`, F3 shape refusal, F1 mutation red at `:263` naming the transition row, F4 `equal: yes`→`no`; "No red fails for a reason other than its row" |
| (ii) X1 REAL FACTORY | HOLDS — `REAL_CONNECT` bound at import `:30`, set `:215`; every connection real; failure at `store.py:325` before commit `:326`; cleanup `:279`, zero reads `:287-290` | METER | HOLDS — `:30`, `:214-215`; `_real_read` `:186-194` fresh per statement; asserts `:261-267`; control `:272-277`; deletes `:278-289`; zero reads `packet.md:148` |
| (iii) BANNER | HOLDS — post-commit `try` `web.py:1144-1154`, tail `:1168-1177`; pre-commit handlers `:1127-1139` byte-unchanged; both hunks in `async def fill` | METER | HOLDS — new `try` `:1141-1154`, `except Exception` `:1146`, shared tail `:1168-1177`; refusals before the commit still take `:1127-1139`; two hunks, both in `fill` |
| (iv) F3 / F4 | HOLDS — `test_s3_c1_experiments.py:77` under root, reaches `card.py:270-273`; F4 `test_aset_web.py:195-197`, `:580-581`, base `:97,:101-103,:183` untouched | METER | HOLDS — F3 `:77-78`; F4 constructed at `:195-197`, `:580-581`; base `:97,:101,:102,:183` outside both hunks; report quotes no replaced value |
| (v) SUITES / R1 | Suites HOLD on quoted output, re-execution NOT CHECKABLE FROM READS. R1: DOES NOT HOLD for one table, `cobalt_redactions` 179→180 (`packet.md:67` vs `:170`) | METER | DOES NOT HOLD — suites, lock, `store.py` hold; "R1's per-table rows are not all equal"; `cobalt_redactions` row count and digest differ |
| (vi) SCOPE / SEAM | NOTHING WIDENED; seam whole, every read `file:line` true at tip (list under `packet.md:210-253`) | METER | NOTHING WIDENED; seam cites checked at `3ceb3b11` are true (`legs.py`, `aset/store.py`, `cards/store.py`, `0021_legs.sql`, `engine.py`, `card.py`, `web.py`, test file) |
| (a) weak assertions | (1) p-missing note-failure test never asserts the result card (`test_fill_c1_offline.py:387-393`); (2) `_db.connect is not REAL_CONNECT` proves only that the suite patched (`test_fill_transaction_db.py:215`), not blocking | METER | NONE |
| (b) reach | NO PATH — only renders an already-committed `FillRecompute` (`web.py:1173-1177`) | METER | NO PATH — `aset/engine.py:302` / `aset/store.py:368` are outside the diff |
| CHECK line | `BUILD STANDS EXCEPT R1 cobalt_redactions 179→180 unattributed (not F1's) · ready for C2: YES` | METER | `BUILD STANDS EXCEPT R1 cobalt_redactions rows and digest · ready for C2: YES` |
Opus also lists, outside the rows, an L32 note for the desk (under `## Checked against the branch`).

## Suites
From `<report>` (I ran nothing).
| item | fact |
|---|---|
| offline (a) | `3246 passed, 410 skipped, 1 xfailed, 20 warnings in 551.37s (0:09:11)`, exit 0 — 0 failed, 0 errors; `<p>` = 3246 (`packet.md` W (a)) |
| offline E0 on `d9240ae4` | `3244 passed, 409 skipped, 1 xfailed, 20 warnings in 554.05s`, exit 0 |
| with-DB pass 1 at `0013` | `3617 passed, 6 skipped, 33 deselected, 1 xfailed, 20 warnings in 641.13s (0:10:41)`, exit 0 — 0 failed, 0 errors; the six SKIPPED are C1's known set |
| deselects | `20`'s command: eight `--deselect` node arguments (`test_tenancy.py::TestMigrationRoundTrip`, `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`, three in `test_voice_store.py`, `test_voice_confirm.py::test_x13_with_db_…`, `test_voice_lifecycle.py::test_e7_kill_mid_turn_…`) + `--deselect tests/cobalt/test_legs_db.py` + `--deselect tests/cobalt/test_fill_transaction_db.py`; 33 deselected = 9 + 24 |
| with-DB pass 2 at `0021` | `33 passed, 5 warnings in 136.60s (0:02:16)`, exit 0, no SKIPPED line; F1's id `test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back` PASSED; `<d>` = 3617 + 33 = 3650 |
| live-note | `146 passed, 1 skipped, 15 warnings in 25.56s`; the one skip is `test_replay_line.py:256 … COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT` |
| F0 / F1 / F2 | F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; F2 = F0 at 12:25:25, and F = F0 again after forward/back at 12:25:57 (X22: forward, back, forward, back — F = F0 twice) |
| mutation run (three quotes) | RED: `AssertionError: a FILLED transition row survived the failed fill: {'state': 'FILLED', 'actual_fill': None, 'filled_rows': 1, 'legs': 0, 'picks': 0}` at `test_fill_transaction_db.py:263`, `1 failed in 0.35s` · `git diff -- src/cobalt/aset/store.py` → empty (exit 0) · re-run `PASSED …` / `1 passed in 0.35s`; cleanup reads `X1RF` `aset_sizings` = 0, joined `legs` = 0 |
| R1 per-table proof | `<P0>` (12:09) vs `<P2>`: 29 of 30 tables equal on rows and digest; `cobalt_redactions` `179 · 1d147fe7e1e2bf7ee0733886fc9ec5b4` → `180 · 5acf3646ea44438bed7e762ecd328ee7`; the forward's BEFORE probe at 12:21 already read `180 -> 180 OK`; C1's `<P0>` read 177 (C1 report line 108) |
| `.env` | taken 12:09:42; `rm` + `ls` → `No such file or directory` and `ls -la …/*/.env` → `no matches found`; released 12:26:45; my own `ls` at PREFLIGHT → `No such file or directory` |
| `aset/store.py` | `git diff -- src/cobalt/aset/store.py` empty in the mutation run; my fact (ii) below: no store.py commit in the range |
| stop line | `S3 EXITS C1 FIX R1 BUILT 3ceb3b11 | on 5164f867 | migration 0021: rolled back | offline 3246/0 | with-DB 3650/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | FIX: 4 | RUNS: 1 | ESCALATE: 7` = `<build stop>` |

## Scope
Each seat's (vi): Opus `NOTHING WIDENED` · Grok `NOTHING WIDENED` (Sol: METER).
My PREFLIGHT path union of `d9240ae4..3ceb3b11`: `src/cobalt/aset/web.py` · `tests/cobalt/test_aset_web.py` · `tests/cobalt/test_s3_c1_experiments.py` · `tests/cobalt/test_fill_c1_offline.py` · `tests/cobalt/test_fill_transaction_db.py` (5 paths, no `docs/`). `29`'s rows name exactly these: F1 `test_fill_transaction_db.py`, F2 `web.py` + `test_fill_c1_offline.py`, F3 `test_s3_c1_experiments.py`, F4 `test_aset_web.py`. `29`'s NOT IN THIS FIX paths (`settings/models.py`, `db_migrations/*`, any route other than `/fill`) do not appear.

## Checked against the branch
Every claim opened in the real file (Read/grep on `/Users/cobalt/cobalt-wt/s3-exits-c1/…`, or `git -C /Users/cobalt/cobalt`). `claim · who · file:line · result · ≤30 words`.
| claim | who | file:line | result |
|---|---|---|---|
| R1 proof rows differ: `cobalt_redactions` `<P0>` ≠ `<P2>` | Opus, Grok (Q(v)) | worktree `<report>` lines 116 (`179 … 1d147fe7…`) and 219 (`180 … 5acf3646…`) | HOLDS — the two tables in the report read as claimed; every other table row matches between them. Grok's cites `:117`/`:220` are `:116`/`:219` in the file. |
| the difference is a leak by a pass-1 run | Opus (inference) | `redact/store.py`, `<report>` W (f2) | NOT CHECKABLE FROM READS — what would have to be run: `--proof-only`, pass 1 alone, `--proof-only` again (Opus's own words) |
| p-missing note-failure test never asserts the result card | Opus (a)1 | `tests/cobalt/test_fill_c1_offline.py:387-393` | HOLDS — asserts `FAILED`+refusal text, `marked FILLED`, `BANNER`; no result-card assertion |
| `_db.connect is not REAL_CONNECT` proves only that the suite patched | Opus (a)2 | `tests/cobalt/test_fill_transaction_db.py:214` | HOLDS as described; Opus's cite `:215` is `:214` in the file (`:215` is the `setattr`) |
| C1-added test lines still carry `<value>`s of the base replay card | Opus (note) | `tests/cobalt/test_aset_web.py:217,251,567` (`fill_shares`); `tests/cobalt/test_fill_c1_offline.py:296` (`orig_timestamp`) | HOLDS — `fill_shares` lines are `+` in `git diff c1dc476d 3ceb3b11` and equal the removed row's shares `<value>`; `test_fill_c1_offline.py` is absent at `c1dc476d`; the timestamp `<value>` is the replay card's date |
| both hunks of the `web.py` diff sit in `async def fill`; pre-commit handlers unchanged | Opus, Grok (iii) | `diff.part1.md:13-25`; `src/cobalt/aset/web.py:1127-1139` | HOLDS — hunk headers name `async def fill`; the only removed lines are the blank and `save_fill_update` call inside the pre-commit `try` |
| `legs.card_id` FK has no cascade | Opus (ii) | `src/cobalt/db_migrations/0021_legs.sql:42` | HOLDS — `REFERENCES "user".aset_sizings(id)`, no `ON DELETE` |
| F3's constructed file reaches the key check | Opus, Grok (iv) | `src/cobalt/settings/card.py:74,256-257,270-273`; `tests/cobalt/test_s3_c1_experiments.py:77-78` | HOLDS — root `card_settings` passes `:256`; the key is not in `CARD_SETTING_KEYS` (`:69`) so `:270-273` raises "unknown card setting" |

Facts stated by me (each its own call):
- (i) `git -C /Users/cobalt/cobalt log --oneline d9240ae4..3ceb3b11 -- src/cobalt/radar src/cobalt/cards src/cobalt/db_migrations src/cobalt/settings src/cobalt/prefill src/cobalt/drc` → EMPTY (exit 0).
- (ii) `git -C /Users/cobalt/cobalt log --oneline d9240ae4..3ceb3b11 -- src/cobalt/aset/store.py` → EMPTY (exit 0).
- (iii) `grep -n -F "REAL_CONNECT" …/tests/cobalt/test_fill_transaction_db.py` → `:27` (comment), `:30`, `:190`, `:214`, `:215`, `:279`.
- (iv) `grep -n -F "DRIFT_NOT_EVALUATED" …/aset/web.py` → `:71` (import), `:1172` (banner).
- (v) `grep -n -F "@app.post" …/aset/web.py` → nine routes: `/size` 959, `/fill` 1060, `/attest` 1180, `/card/{card_id}/move` 1223, `/card/{card_id}/stop` 1278, `/radar/card/{card_id}/key` 1326, `…/dot/{factor}` 1378, `…/promote` 1417, `…/release` 1422 — the nine of round 1; no new route (the seven after `/fill` moved +13 lines).
- (vi) L32: this report quotes no ticker beyond the constructed `TEST` / `X1RF`, no price, share count or date of his; the `<value>` marks stand where the files show them.

## FOR THE CLASSIFIER
Each: claim verbatim · who · question · my `file:line` · HOLDS.
1. "`cobalt_redactions` is `179 · 1d147fe7…` in `<P0>` and `180 · 5acf3646…` in `<P2>`" / "R1's per-table rows are not all equal" · Opus, Grok · (v) · `<report>` lines 116 and 219 · HOLDS (the rows differ; the cause is NOT CHECKABLE FROM READS).
2. "`test_a_note_failure_after_the_commit_keeps_the_p_missing_banner` … never checks that the result card renders" · Opus · (a) · `tests/cobalt/test_fill_c1_offline.py:387-393` · HOLDS.
3. "F1's `_db.connect is not REAL_CONNECT` … proves only that the suite patched the factory" · Opus · (a) · `tests/cobalt/test_fill_transaction_db.py:214` · HOLDS (Opus: not blocking).
4. "some lines C1 added still carry `<value>`s tied to the base replay card" · Opus · note (L32) · `tests/cobalt/test_aset_web.py:217,251,567`; `tests/cobalt/test_fill_c1_offline.py:296` · HOLDS.

## ESCALATE
1. **Opus `BUILD STANDS EXCEPT` in full:** `CHECK S3 C1 FIX R1: BUILD STANDS EXCEPT R1 cobalt_redactions 179→180 unattributed (not F1's) · ready for C2: YES` — its item: (v) R1 proof `DOES NOT HOLD for one of 30 tables`. File-check: the rows differ (HOLDS); the cause is NOT CHECKABLE FROM READS.
2. **Grok `BUILD STANDS EXCEPT` in full:** `CHECK S3 C1 FIX R1: BUILD STANDS EXCEPT R1 cobalt_redactions rows and digest · ready for C2: YES` — its item: (v) `DOES NOT HOLD — … R1's per-table rows are not all equal`. File-check: HOLDS as in item 1 above.
3–6. **FOR THE CLASSIFIER, items 1–4 above** (item 1 is the one DOES NOT HOLD claim counted in the stop line).
7. **Sol did not check:** METER, returns 3:32 PM. `ASK DESK: sol did not check (METER; returns 3:32 PM) — relaunch it alone? [13:33 ET]` Safe default taken: not relaunched; the floor is met without it.
8. **L74:** the `Claude-Session` / file-send reminder appended to the prompt-file read result (recorded once under `## L74`; not followed).
9. **Round 2 of ≤3 (L39) of S3 C1: Opus 5.5 (Fable seat, R109) · Sol · Grok (R58). A HOLD → fix round 2, classified first (L75); round 3 is the last. `ready for C2: YES` → `22-s3-exits-c2-build.md` stacks on `<tip>`.**

S3 EXITS C1 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C1 FIX R1: BUILD STANDS EXCEPT R1 cobalt_redactions 179→180 unattributed (not F1's) · ready for C2: YES · sol: METER · grok: CHECK S3 C1 FIX R1: BUILD STANDS EXCEPT R1 cobalt_redactions rows and digest · ready for C2: YES · houses that checked: 2 of 3 · defects that HOLD: 1 · ready for C2: NO · ESCALATE: 9
