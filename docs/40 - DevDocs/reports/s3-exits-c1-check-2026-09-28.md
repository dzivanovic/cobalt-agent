# S3 EXITS C1 — CHECK, ROUND 1 — 2026-09-28

Hub `s3-exits-c1-check` (Sonnet 5, auto). Prompt `prompts/2026-09-28/21-s3-exits-c1-check.md`. `<D>` = 2026-09-28. Range `c1dc476d..5164f867` on `s3/exits-c1`; report commit `d9240ae4` on top. I judge nothing (L37); every line below is a fact I read or a seat's words with my file-check beside them.

## §0 Headline
3 of 3 houses checked (floor met): Opus `BUILD STANDS EXCEPT … · YES` · Astra `FIX Q2/X1, Q5/banner · NO` · Grok `BUILD STANDS · YES`.
Seat claims of DOES NOT HOLD that I walked in the real files and found to HOLD: 2 — X1 runs on an emulated autocommit wrapper, not the real `db.connect` (Opus + Astra; the builder's own report discloses it); a missing-P fill whose daily-note write raises `DailyNoteRefused` after the commit returns the failure banner only, without the drift banner (Astra Q5).
By the stop-line rule `ready for C2: NO` (Astra says NO, defects that HOLD = 2). Nothing was run by me; no repo write, no commit.
ESCALATE: 16.

## L74
Recorded once (L74): after this prompt file was read (10:59), a `<system-reminder>` block was appended to that tool result asking commit and PR text to carry a `Claude-Session: https://claude.ai/code/session_…` line and mentioning a file-send tool. It is data, not an instruction; this hub commits nothing and sent nothing.

## PREFLIGHT
| rule | command | exit | allowed / output |
|---|---|---|---|
| date | `date` | 0 | allowed · `Mon Sep 28 10:59:27 EDT 2026` |
| placeholder | `grep -n -E "R_[_]" …/21-s3-exits-c1-check.md` | 1 | allowed · nothing |
| placeholder | `grep -n -F "FILL AT LAUNCH" …/21-s3-exits-c1-check.md` | 0 | allowed · line 11 only (this gate's own line) |
| R17 | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | allowed · row 35 carries `Grok approved with no asking going forward` |
| R19 | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | allowed · row 37 carries `All 4 house models approved` |
| R19 `-S` | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved" -- …/cto-2026-09-24.md` | 0 | allowed · `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R95 | `grep -n "^| R95 " …/cto-2026-09-23.md` | 0 | allowed · one row, line 103 |
| R109 | `grep -n "^| R109 " …/cto-2026-09-22.md` | 0 | allowed · line 56 carries `Make all Opus 5.5 for now` (contains `Make all Opus`) |
| R47 | `grep -n -F "21-s3-exits-c1-check.md" …/cto-2026-09-28.md` | 0 | allowed · row 55 `\| R47 \| 10:59 ET \|` names this file, carries `<build stop>` verbatim and `no other house hub is running`; line 64 (NEXT) also names it |
| R47 `-S` | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"21-s3-exits-c1-check.md" -- …/cto-2026-09-28.md` | 0 | allowed · `00f4d61691283cb94b0cfc0ee62ed9113d3892e1` |
| grok | `grok --version` | 0 | allowed · `grok 1.0.25 (f7e67d6988e2) [stable]` |
| build stop | `tail -n 3 "<report>"` | 0 | allowed · last non-blank line EQUALS `<build stop>` and starts `S3 EXITS C1 BUILT ` |
| commits | `git -C /Users/cobalt/cobalt log --oneline c1dc476d..5164f867` | 0 | allowed · `5164f867 fix(s3-c1): test_aset_daily_note passes a constructed drift P (with-DB pass 1 red)` · `eb642f05 feat(s3): C1 — legs (0021), the one fill transaction, from_card, the drift setting (v3 §2–§4, R67, R38)` · `c57634f8 wip(s3-c1): red` · `0da7e2e8 wip(s3-c1): E1 experiments` (4 commits) |
| stat | `git -C /Users/cobalt/cobalt log --stat --format=%h c1dc476d..5164f867` | 0 | allowed · path union under `## Scope` |
| .env | `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` | 1 | allowed · `No such file or directory` (also at 11:33, after the seats) |
| recovery | `ls scratch/tribunal-bars-0920/s3-exits-c1` | 1 | allowed · `No such file or directory` → fresh |
| stagger | `grep -n -F "no other house hub is running" …/cto-2026-09-28.md` | 0 | allowed · lines 16 (R8) and 55 (R47); line 55 also names `21-s3-exits-c1-check.md` |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | allowed · `OK` = UP |
| probe ASTRA | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | allowed · `OK` = UP |
| gates again (11:13:54) | R17, R19 (`grep -c -F` on each row) and R19 `-S` | 0 | allowed · 1 · 1 · same sha `5055151d…` |
| diff copy | `git -C /Users/cobalt/cobalt log -p c1dc476d..5164f867 -- . ":(exclude)docs"` (background) | 0 | allowed · 138,547 B, 4 commits |
Denials: none. One harness-side note on a CLI stderr line printed by `claude -p`: `Permission deny rule (../../cobalt/.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax…` (a settings warning, not a denial of anything this hub ran).

## Files copied
`S` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c1/`. Written before the launches (`ls -la S` at 11:13 lists CHECK-INSTRUCTIONS.md, diff.part1–4.md, files/, rulings.md).
- `diff.part1–4.md`: I copied them Read → Write. Sizes 35,184 / 36,637 / 31,691 / 35,435 B = 138,547 B of diff + 4 × 100 B header. All ≤ 38,000 B; cut at `commit ` / `diff --git` lines. `grep -c "^commit "` over the parts = 2 + 1 + 0 + 1 = 4 = PREFLIGHT's 4. The four parts' bodies joined equal the git output byte for byte (`diff` against the saved output, IDENTICAL).
- `rulings.md` (3,179 B): the R67 and R38 lines under their command lines; each line `diff`-identical to a fresh `grep -n` of its source.
- `CHECK-INSTRUCTIONS.md` (6,269 B): the QUESTIONS text `diff`-identical to the prompt's lines 28–40 with the wrapping quote and lead-in removed, then the "Files:" paragraph with absolute paths.
- `S/files/` (44 files): the Grok-only copies were made Read → Write by eight fresh helper sub-agents I launched (the prompt does not mention helpers; disclosed), each told to write only its files. I did not rely on their reports: I checked every original against its copy with `cmp` (parts `cat`-joined in order) — table below. No copy exceeds 38,000 B.

| original | parts | bytes (original) | cmp |
|---|---|---|---|
| `<report>` (`s3-exits-c1-build-2026-09-28.md`) | 2 (cut at `## SEAM FOR C2`) | 43,508 | IDENTICAL |
| `20-s3-exits-c1-build.md` | 1 | 31,610 | IDENTICAL |
| `S3-EXITS-v3-2026-09-22.md` | 3 (cut at `## 5. STOP OVERRIDE`, `## 12. OPEN QUESTIONS`) | 78,960 | IDENTICAL |
| `LAWS.md` | 2 (cut at `### L49`) | 61,011 | IDENTICAL |
| `src/cobalt/aset/web.py` | 2 (cut at `def _result_card`) | 64,466 | IDENTICAL |
| `src/cobalt/cards/store.py` | 2 (cut at `# -- backfill`) | 63,233 | IDENTICAL |
| `src/cobalt/db_migrations/cli.py` | 2 (cut at `def _rollback_paths`) | 38,407 | IDENTICAL |
| `src/cobalt/aset/{engine,models,store}.py` | 1 each | 12,752 · 7,299 · 21,404 | IDENTICAL |
| `src/cobalt/cards/{cli,legs}.py` | 1 each | 9,358 · 3,143 | IDENTICAL |
| `src/cobalt/db_migrations/{0021_legs.rollback.sql,0021_legs.sql,__init__.py,placement.py}` | 1 each | 653 · 5,672 · 7,852 · 7,171 | IDENTICAL |
| `src/cobalt/settings/fills.py` | 1 | 2,722 | IDENTICAL |
| 20 files under `tests/cobalt/` (`legs_db_support.py` … `test_voice_store.py`) | 1 each | 4,195 – 30,875 | IDENTICAL (20 of 20) |
Total 37 originals compared, 37 IDENTICAL, 0 mismatch. The worktree `/Users/cobalt/cobalt-wt/s3-exits-c1/` is at `d9240ae4` (docs-only on top of `5164f867`); `git diff --stat 5164f867 -- src tests` there is empty, `git status --short` empty.

## CONTINUE
- 11:14 ET: Opus, Astra, Grok launched in one message, one attempt each, 45-minute clock (to 11:59).
- Opus done (notice ~11:18); Astra done (before 11:29); Grok done (before 11:33). Clock: all three inside 45 minutes; no TIMEOUT.
- next: none — the run is closed.

## Clock
| seat | launched | done | note |
|---|---|---|---|
| Opus (`claude -p …`, plan mode, Read/Grep/Glob only) | 11:14 | 11:18 | exit 0; answer on stdout; I wrote `S/opus-check.md` = stdout lines of the answer (`diff`-identical), leaving out stdout's first line (a CLI stderr settings warning, quoted under PREFLIGHT) and the harness's `[exited with code 0]` trailer |
| Astra (`codex exec … gpt-6-astra -s read-only`) | 11:14 | 11:28 | exit 0; 1,135,623-byte stream (tool traces) ending in its final message; I wrote `S/astra-check.md` = the final message after `tokens used 277,295` (`diff`-identical); it says the original absolute paths were readable, no fallback copies needed, no `-check.md` opened |
| Grok (`grok --sandbox cobalt-job --allow "Write(…tribunal-bars-0920/**)" -p …`) | 11:14 | 11:33 | exit 0; replied with the path only; wrote `S/grok-check.md` itself (20,524 B, 89 lines) — I did not edit it |
Written-nothing proof: `ls -la S` 11:13 vs 11:33 — new top-level entries are exactly `astra-check.md`, `opus-check.md` (both mine), `grok-check.md` (the one file Grok was allowed to write); `files/` untouched after 11:11 (`find` shows every copy stamped 11:09–11:11); 53 files in `S` (44 in `files/`, 4 diff parts, rulings, instructions, 3 seat files). The `agy-trial` git status shows only the two pre-existing untracked paths (`audit-house-2026-09-16.md`, `tmp/`).

## Per question
Each cell ≤30 words of the seat's own, with its cite. `path` in cells is relative to the worktree unless shown.

| Q | opus | astra | grok |
|---|---|---|---|
| (1) S-LEGS | HOLDS — cols/CHECKs `src/cobalt/db_migrations/0021_legs.sql:37-65`, indexes `:71-74`, trigger `:76-88`, view `:93-96`; `preset` CHECK written `IS NULL OR …` (`:51`), same effect | HOLDS — DDL matches S-LEGS, prohibited columns absent, preset expression "semantically equivalent" (`0021_legs.sql:37`) | HOLDS — every column with its line `0021_legs.sql:38-62`, CHECKs `:63-65`, indexes `:71-74`, trigger `:83-85`, view `:93-96`; nothing added or missing |
| (2) ONE TRANSACTION | code HOLDS (`aset/store.py:268-329`, `cards/store.py:485-553`); X1 on the real factory DOES NOT HOLD (`test_fill_transaction_db.py:103-162`); other FILLED writers: `fill()`, `transition()`, `backfill` | DOES NOT HOLD — X1 "does not use the real connection factory" (`test_fill_transaction_db.py:104`); impl one txn (`aset/store.py:267`); other writers `fill`, `transition`, `create_state`/backfill (`cards/store.py:239,592,825`) | HOLDS — `fill(conn)` commits/closes only when `owned` (`cards/store.py:485-553`); `mark_filled` one commit (`aset/store.py:267-331`); X1 `:96-176`; FILLED outside: standalone `fill`, `backfill` |
| (3) `from_card` | HOLDS — only rebuild (`aset/models.py:122`), NULL raises naming column (`:135`), `/fill` price+shares only (`web.py:1092-1124`), X10 real with-DB (`test_s3_c1_experiments.py:130-150`) | HOLDS — six columns copied, no defaults, `/fill` price and shares, X10 persists and compares (`models.py:120`, `store.py:283`, `test_s3_c1_experiments.py:129`) | HOLDS — `FROM_CARD_COLUMNS` `models.py:103-106`, raise `:135-140`, `/fill` `web.py:1093-1124`, X10 `test_s3_c1_experiments.py:136-152`; only production call `aset/store.py:283` |
| (4) REFUSALS | HOLDS — move `web.py:1223-1232`; CLI `cards/cli.py:75-84`; no price `web.py:1092-1097`, `aset/store.py:252-262`; radar `cards/store.py:511`; reset `:267` | HOLDS for fill/state writes — move `web.py:1223`, CLI `cli.py:74`, price `aset/store.py:251`, radar `cards/store.py:511`, gate `:267`; notes page render can persist a day-mode attestation (cite `web.py:510`) | HOLDS — move `web.py:1224-1233`, CLI `cli.py:75-84`, price `aset/store.py:252-257`, radar `cards/store.py:508-511`, reset test `test_fill_transaction_db.py:248-258` |
| (5) DRIFT | HOLDS — constant gone (`aset/engine.py:39-41` comment), one reader `settings/fills.py:49`, `>` `engine.py:310`, banner `web.py:1156-1159`, X-S NO, banner on every fill until loadable | DOES NOT HOLD — missing-P fill commits, then `save_fill_update` may raise `DailyNoteRefused`; failure banner returned before the drift banner (`web.py:1126, 1135, 1156`) | HOLDS — `fills.py:26-66`, `engine.py:39-41, 266-322`, `web.py:1157-1160`; `>` at `engine.py:310`; X15 27.00 both sides; X-S NO, builder escalated |
| (6) ENTRY LEG | HOLDS — `stop_in_force` = `card["stop"]` (`aset/store.py:271,318`), mismatch `:335-358`, NULL structural stop test, exit-only fields NULL (`cards/legs.py:73-76`) | HOLDS — stop under lock, mismatch cases (`aset/store.py:308,335`), manual card fills (`test_fill_transaction_db.py:185`) | HOLDS — `aset/store.py:270-324`, `legs.py:66-83`; mismatch `:335-358`; NULL-stop fill test `test_fill_transaction_db.py:187-194` |
| (7) MIGRATION + SEAMS | HOLDS — rollback `0021_legs.rollback.sql:6-15`, FORWARD/REVERSE `__init__.py:117,122`, `settings/models.py` not in diff, no route added (`web.py` ends `:1409`), `for_date` unchanged (`aset/store.py:442-456`) | HOLDS structurally — rollback `:6`, registration `__init__.py:117`, `for_date` `aset/store.py:434`; X22 "reported, not independently executed"; fingerprint counts only | HOLDS — rollback `:6-15`, `__init__.py:117,122`, no route added, file ends `web.py:1410-1412`, `for_date` list unchanged `aset/store.py:445-448`; X22 from quoted fingerprints |
| (8) SUITES | HOLDS as reported; the runs NOT CHECKABLE FROM READS; pass 2 appends `-rA` (report `:110-126`) | NOT CHECKABLE FROM READS — report records the runs and the earlier red; verification needs the logs or reruns (report `:98`) | HOLDS — quoted from report `:100, 115-127`; "Not re-run here"; first pass-1 red on `eb642f05` fixed in `5164f867` |
| (9) SCOPE | WIDENED — `db_migrations/cli.py` digest exclusions; `web.py:859` `fill_shares` input; both already ASK DESK; nothing of exits/panel; L31 clean | WIDENED — digest exclusions (`cli.py:113`), `drift_settings` parameter (`aset/store.py:210`), form control (`web.py:858`); "bounded supporting changes" | NOTHING WIDENED — names three keeps outside the row's file list (digest exclusions, `fill_shares` input, `drift_settings=None`), each an ASK DESK in the report |
| (a) weak assertions | X1 emulated factory never red for its own reason; X-S card-load `(TraderSettingsError, ValueError)` `test_s3_c1_experiments.py:76`; `test_0021_applies_twice` asserts nothing | X1 simulated autocommit + no positive pre-failure pick (`test_fill_transaction_db.py:163`); fingerprint counts only (report `:104`); banner test lacks note-failure branch (`test_fill_c1_offline.py:367`) | X1 wrapper's `autocommit` setter stores a bool (`test_fill_transaction_db.py:128-129`); X-S `:76` any ValueError; radar-refusal test does not query `legs` (`test_aset_store.py:334-339`) |
| (b) reach | NO PATH — `drift_warned` only sets warning text (`engine.py:310-311`); nothing reads `legs` | `engine.py:301` DOES — stored card risk and fill-to-stop distance determine `recomputed_shares` in the persisted fill cache; "existing arithmetic" | `engine.py:302` DOES — `recomputed_shares` written by `_update_fill_cache` (`aset/store.py:368`); nothing writes a score, rank or new grade |
| CHECK line | `BUILD STANDS EXCEPT X1 emulated factory never red for its reason; X-S card-load assertion too broad; cli.py and _result_card edits await ASK DESK; unguarded CardStore.fill(conn=None)/transition(FILLED)/backfill write FILLED without a leg · ready for C2: YES` | `FIX Q2/X1, Q5/banner · ready for C2: NO · Real connection proof missing; committed fills can lose drift banners.` | `BUILD STANDS · ready for C2: YES` |

## Suites
From `<report>` (I ran nothing). All lines read at their report line numbers.
| item | fact |
|---|---|
| offline on `eb642f05` (a) | `3244 passed, 409 skipped, 1 xfailed, 20 warnings in 551.71s (0:09:11)`, exit 0 — no failed, no errors (`:100`) |
| offline on tip `5164f867` (a′) | `3244 passed, 409 skipped, 1 xfailed, 20 warnings in 558.11s (0:09:18)`, exit 0, no `.env` present, read 10:37:32 (`:127`) |
| with-DB pass 1 run 1 on `eb642f05` | `3 failed, 3612 passed, 6 skipped, 32 deselected, 1 xfailed, 20 warnings in 640.12s` — RED: `tests/cobalt/test_aset_daily_note.py` `TypeError … 'drift_warning_pct'`; fixed test-only in `5164f867` (`:114`) |
| with-DB pass 1 run 2 on `5164f867` (at `0013`) | `3615 passed, 6 skipped, 32 deselected, 1 xfailed, 20 warnings in 639.38s (0:10:39)`, exit 0 — 0 failed, 0 errors (`:115`) |
| deselects | 9 test ids named (`TestMigrationRoundTrip` holds two) — `test_tenancy.py::TestMigrationRoundTrip`, `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`, three in `test_voice_store.py`, `test_voice_confirm.py::test_x13_with_db_…`, `test_voice_lifecycle.py::test_e7_kill_mid_turn_…` — plus `--deselect tests/cobalt/test_legs_db.py` (11) and `--deselect tests/cobalt/test_fill_transaction_db.py` (12); 32 deselected in the summary (`:111-113`) |
| with-DB pass 2 at `0021` | `32 passed, 5 warnings in 136.62s (0:02:16)`, no SKIPPED line; `<d>` = 3615 + 32 = 3647 (`:119-121`) |
| live-note | `146 passed, 1 skipped, 15 warnings in 25.54s`; the one skip is `test_replay_line.py:256 … COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT` (`:125`) |
| F0 / F1 / F2 | F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; F2 = F0 at 10:26:25 and again at 10:27:16 (`:108, 116, 123-124`); `cobalt_dev` left at `0013` |
| `.env` | taken 10:00:27; `rm` + `ls` → `No such file or directory` and `ls -la …/*/.env` → `no matches found` at 10:27:50 (`:126`); the offline re-run (a′) ran 10:28–10:37 without it; my own `ls` of it at 11:33 → `No such file or directory` |
| stop line | `S3 EXITS C1 BUILT 5164f867 | on c1dc476d | migration 0021: rolled back | X: 6 of 6 run, design-changing: 1 | offline 3244/0 | with-DB 3647/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | ESCALATE: 5` = `<build stop>` |

## Scope
Each seat's (9): Opus `WIDENED` (cli.py digest exclusions; `fill_shares` input in `_result_card`) · Astra `WIDENED` (digest exclusions, `drift_settings` parameter, share-count form control) · Grok `NOTHING WIDENED` (names the same three "keeps outside the row's file list").
My PREFLIGHT path union of `c1dc476d..5164f867` (per-commit file counts 25 / 19 / 1 / 1 over four commits; union 13 + 20 + 6 = 39 paths, `docs/` included):
- `src/` (13): `aset/{engine,models,store,web}.py` · `cards/{cli,legs,store}.py` · `db_migrations/{0021_legs.rollback.sql,0021_legs.sql,__init__.py,cli.py,placement.py}` · `settings/fills.py`
- `tests/cobalt/` (20): `legs_db_support.py` · `test_archiver_migrations.py` · `test_aset_daily_note.py` · `test_aset_engine.py` · `test_aset_store.py` · `test_aset_web.py` · `test_assumed_store.py` · `test_cards_picks.py` · `test_fill_c1_offline.py` · `test_fill_transaction_db.py` · `test_legs_db.py` · `test_legs_migration.py` · `test_p4_migrations.py` · `test_radar_handicap_store.py` · `test_radar_migration.py` · `test_radar_score_migration.py` · `test_s3_c1_experiments.py` · `test_stale_score_db.py` · `test_tenancy.py` · `test_voice_store.py`
- `docs/40 - DevDocs/cobalt/` (6): `aset/{engine,store}.md` · `cards/{legs,store}.md` · `db_migrations/__init__.md` · `settings/fills.md`
Named in the build prompt `20`'s rows: `grep -n -F "db_migrations/cli.py"` on the prompt → no match (the file `db_migrations/cli.py` is not named there); the builder's report lists it as ASK DESK (`:201`), `fill_shares` as ASK DESK (`:202`), `drift_settings` as ASK DESK (`:203`). Nothing in the diff under `radar/`, `cards/scoring.py`, `cards/radar.py`, `prefill/`, `drc/`, `settings/models.py` (my (i) below).

## Checked against the branch
Every claim opened in the real file (Read on `/Users/cobalt/cobalt-wt/s3-exits-c1/…`) or by `git -C /Users/cobalt/cobalt show`. `claim · who · file:line · result · ≤30 words`.
| claim | who | file:line | result |
|---|---|---|---|
| X1 wraps the suite's `db.connect`, not the real one | Opus, Astra (Q2/(a)), Grok (a) | `tests/cobalt/test_fill_transaction_db.py:103-162`; `tests/cobalt/conftest.py:81-130` | HOLDS — `suite_connect = db.connect` (`:103`) is the patched `_SavepointConnection` factory whose commit is `RELEASE SAVEPOINT` (`conftest.py:120-123`); the wrapper's `autocommit` setter stores a bool (`:128-129`) |
| X1 was never seen red for its own reason | Opus | report `:84` | HOLDS — E2 red was `FileNotFoundError … 0021_legs.sql` at setup for every `test_fill_transaction_db.py` case; no later red for the cache-UPDATE reason in the report |
| missing-P fill + `DailyNoteRefused` after commit returns the failure banner without the drift banner | Astra Q5 | `aset/web.py:1116-1128, 1137-1139, 1156-1159`; `aset/daily_note.py:168, 187, 199` | HOLDS — `mark_filled` commits (`aset/store.py:326`) before `save_fill_update` (`web.py:1128`); `DailyNoteRefused` is in the caught tuple (`:1137`) and `return`s at `:1139`, before `:1156`. Astra's cites `1126/1135` are `1128/1139` in the file |
| X-S card-load assertion accepts any `ValueError` | Opus, Grok | `tests/cobalt/test_s3_c1_experiments.py:76` | HOLDS — `pytest.raises((TraderSettingsError, ValueError))` with no `match`; the optional-load test matches the key (`:66`) |
| `test_0021_applies_twice` asserts nothing | Opus | `tests/cobalt/test_legs_db.py:143-145` | HOLDS — body is `apply_0021(aset)` with a comment; no assert |
| X1 zero-pick assertion has no positive pre-failure pick | Astra | `tests/cobalt/test_fill_transaction_db.py:175`, `:258` | HOLDS — `_picks` is used only at `:175` and `:258`, both `== 0` |
| schema fingerprint = counts + a view-definition hash | Astra | report `:104` | HOLDS — `cols`, `rels`, `views_md5` only |
| missing-P banner test has no note-failure branch | Astra | `tests/cobalt/test_fill_c1_offline.py` (`_FillRoute.install` stubs `save_fill_update` to return a fixed value); `grep -n DailyNoteRefused` on it and `test_aset_web.py` → no match | HOLDS |
| radar-refusal test does not query `legs` | Grok | `tests/cobalt/test_aset_store.py` (only `legs` hits: `:23`, `:48-49`) | HOLDS |
| FILLED can be written without a leg by `CardStore.fill(conn=None)`, `transition()` to FILLED, and `backfill` | Opus, Astra, Grok | `cards/store.py:239-313` (only `assert_edge`), `:518-553` (owned path commits), `:822-847` (`create_state(… FILLED)`) | HOLDS as code paths. `grep -rn "\.fill("` in `src` → one caller, `aset/store.py:287`; the other `.transition(` callers in `src` target non-FILLED states (`cards/store.py:1101`, `expire.py:203`, `cli.py:87`, `web.py:1238` after the FILLED refusal, `web.py:1325` PASSED) |
| three edits outside the row list | Opus, Astra (WIDENED); Grok names them | `db_migrations/cli.py:113-122` (diff), `aset/web.py:859`, `aset/store.py:210` | HOLDS — all three in the diff; `db_migrations/cli.py` not named in `20`; `mark_filled` carries `drift_settings=None` beyond the prompt's signature; all three are ASK DESK in the report `:201-203` |
| `engine.py:301/302` reaches the persisted `recomputed_shares` | Astra (cites `:301`), Grok (`:302`) | `aset/engine.py:302`; `aset/store.py:368, 378`; base `c1dc476d` `engine.py:292` | HOLDS — `:302` is `recomputed_shares = int(risk_budget / new_distance)` (Astra's `:301` is the line above); the same expression is at base `:292` (unchanged by C1); readers: `daily_note.py:139`, `web.py:831` (display), `aset/store.py:447` (`for_date` select), `prefill/drc.py:197` (message text). No score, rank or grade write seen |
| page render can persist a day-mode attestation on a refused write | Astra Q4 | `aset/web.py:495-496` (`store.attest_sheet`), `:388` (`_render` → `_daymode_state()`) | HOLDS as existing behaviour, not in the diff; Astra's cite `web.py:510` is a docstring line, the write is `:495-496` |
| new test rows re-type real-card values already present in the file at base | Opus | `tests/cobalt/test_aset_web.py:196`, `:581` (added); `:101`, `:183` (in base `c1dc476d`) | HOLDS — values not quoted here (L32) |
Not carried into this table (no seat claimed a defect): the (a) and (b) rows above that are `NONE` / `NO PATH`.

Facts stated by me (each its own call):
- (i) `git -C /Users/cobalt/cobalt log --oneline c1dc476d..5164f867 -- src/cobalt/radar src/cobalt/cards/scoring.py src/cobalt/cards/radar.py src/cobalt/prefill src/cobalt/drc src/cobalt/settings/models.py` → EMPTY (exit 0).
- (ii) `grep -rn "FILL_DISTANCE_WARNING_PCT" /Users/cobalt/cobalt-wt/s3-exits-c1/src` → nothing (exit 1).
- (iii) `grep -rn "INSERT INTO legs" …/src` → `src/cobalt/cards/legs.py:66` only; `grep -rn -F "INSERT INTO \"user\".legs" …/src` → nothing.
- (iv) `grep -rn "actual_fill = " …/src` → `src/cobalt/aset/store.py:367` (`_update_fill_cache`'s UPDATE, in the function `mark_filled` calls) and `src/cobalt/aset/web.py:1099` (`actual_fill = Decimal(raw_price)`, a local variable, not a database write). Not "only `mark_filled`'s UPDATE" as the prompt words it: one more hit, a local.
- (v) `grep -n -F "@app.post" …/aset/web.py` → nine routes (`/size` 959, `/fill` 1060, `/attest` 1167, `/card/{card_id}/move` 1210, `/card/{card_id}/stop` 1265, `/radar/card/{card_id}/key` 1313, `…/dot/{factor}` 1365, `…/promote` 1404, `…/release` 1409). `grep -n -E "^[+-]@app"` over the four diff parts → nothing: no route added or removed.
- (vi) L32: this report quotes no ticker or price of his, no real date or value of his; constructed values only (the stop-line figures and F-fingerprints are the build's own, `cobalt_dev`).

## FOR THE CLASSIFIER
Each: claim verbatim · who · question · my `file:line` · HOLDS.
1. "X1 does not use the real connection factory as required. It captures the already-patched suite factory, then wraps its savepoint connection in simulated autocommit." · Astra (Opus: "X1 on the real factory DOES NOT HOLD (by design choice)") · (2) · `tests/cobalt/test_fill_transaction_db.py:103-162`, `tests/cobalt/conftest.py:81-130` · HOLDS.
2. "A valid fill with missing P commits, then `save_fill_update` can raise `DailyNoteRefused`. That exception returns only the failure banner, before the required drift-not-evaluated banner is appended." · Astra · (5) · `src/cobalt/aset/web.py:1128, 1137-1139, 1156-1159` · HOLDS.
3. "`pytest.raises((TraderSettingsError, ValueError))` passes on any `ValueError`." · Opus, Grok · (a) · `tests/cobalt/test_s3_c1_experiments.py:76` · HOLDS.
4. "`test_0021_applies_twice` … only asserts that nothing raises." · Opus · (a) · `tests/cobalt/test_legs_db.py:143-145` · HOLDS.
5. "its zero-pick assertion lacks a positive pre-failure pick assertion." · Astra · (a) · `tests/cobalt/test_fill_transaction_db.py:175` · HOLDS.
6. "The schema fingerprint cannot establish complete schema identity." · Astra · (a)/(7) · `<report>` line 104 · HOLDS.
7. "The missing-P banner test misses note failure after the database commit." · Astra · (a) · `tests/cobalt/test_fill_c1_offline.py` (`_FillRoute.install`) · HOLDS.
8. "The radar-refusal test asserts state stays WATCH and `actual_fill` is NULL … and does not query `legs`." · Grok · (a) · `tests/cobalt/test_aset_store.py:334-339` (only `legs` hits `:23`, `:48-49`) · HOLDS.
9. "FILLED can still be written without a leg through `CardStore.fill()` / `transition()` or the old backfill." · Opus (Astra, Grok name the same writers) · (2) · `src/cobalt/cards/store.py:239-313, 518-553, 822-847` · HOLDS.
10. "Two edits outside the row list" / "The change also adds migration-proof digest exclusions, a `drift_settings` injection parameter and the share-count form control." · Opus, Astra (Grok: "Three keeps outside the row's file list, each an ASK DESK") · (9) · `src/cobalt/db_migrations/cli.py:113-122`, `src/cobalt/aset/web.py:859`, `src/cobalt/aset/store.py:210` · HOLDS.
11. "`engine.py:302` DOES — `recomputed_shares = int(risk_budget / new_distance)` is written to `aset_sizings.recomputed_shares`" · Grok, Astra (cites `:301`); Opus says NO PATH · (b) · `src/cobalt/aset/engine.py:302`, `src/cobalt/aset/store.py:368` (same expression at base `engine.py:292`) · HOLDS.
12. "existing page rendering can persist a daily-note sheet attestation" · Astra · (4) · `src/cobalt/aset/web.py:495-496` (Astra cites `:510`) · HOLDS (existing behaviour, not in the diff).
13. "re-types real-card values … that were already in the file at base" · Opus · (9)/L32 · `tests/cobalt/test_aset_web.py:196, 581` (base `:101, 183`) · HOLDS.

## ESCALATE
1. **Astra FIX in full:** `CHECK S3 C1: FIX Q2/X1, Q5/banner · ready for C2: NO · Real connection proof missing; committed fills can lose drift banners.` — Q2: "X1 does not use the real connection factory as required. … The injected SQL failure and rollback assertions are useful, but do not supply the requested real-connection proof." (`test_fill_transaction_db.py:104`). Q5: "A valid fill with missing P commits, then `save_fill_update` can raise `DailyNoteRefused` … before the required drift-not-evaluated banner is appended." (`web.py:1126, 1135, 1156`). File-check: both claims HOLD as code (table above); no verdict from me.
2. **Opus `BUILD STANDS EXCEPT` in full:** `X1 emulated factory never red for its reason; X-S card-load assertion too broad; cli.py and _result_card edits await ASK DESK; unguarded CardStore.fill(conn=None)/transition(FILLED)/backfill write FILLED without a leg · ready for C2: YES` — each item HOLDS as code/test (FOR THE CLASSIFIER 1, 3, 9, 10).
3–15. **FOR THE CLASSIFIER, items 1–13 above** (13 entries; items 1–2 are the two DOES NOT HOLD claims counted in the stop line).
16. **L74:** the `Claude-Session` / file-send reminder appended to the prompt-file read result (recorded once under `## L74`; not followed).
Seats that did not check: none. ASK DESK from this hub: none. The builder's own five ESCALATE items (X-S design-changing; three ASK DESK on `db_migrations/cli.py`, `fill_shares`, `drift_settings`; the tip being the fix commit) stand in `<report>` `## ESCALATE`, unchanged by this check.
**Round 1 of ≤3 (L39) of S3 C1, a NEW build: Opus 5.5 (Fable seat, R109) · Astra · Grok (L67, R95). A HOLD → a fix round classified first (L75). `ready for C2: YES` → `22-s3-exits-c2-build.md` stacks on `<tip>`.**

S3 EXITS C1 CHECK DONE · round: 1 · opus: CHECK S3 C1: BUILD STANDS EXCEPT X1 emulated factory never red for its reason; X-S card-load assertion too broad; cli.py and _result_card edits await ASK DESK; unguarded CardStore.fill(conn=None)/transition(FILLED)/backfill write FILLED without a leg · ready for C2: YES · astra: CHECK S3 C1: FIX Q2/X1, Q5/banner · ready for C2: NO · Real connection proof missing; committed fills can lose drift banners. · grok: CHECK S3 C1: BUILD STANDS · ready for C2: YES · houses that checked: 3 of 3 · defects that HOLD: 2 · ready for C2: NO · ESCALATE: 16
