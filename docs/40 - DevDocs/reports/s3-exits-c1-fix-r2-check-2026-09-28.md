## §0 Headline
S3 exits C1 fix r2, round 3 of ≤3 — THE LAST. Opus and Grok checked: both `BUILD STANDS · ready for C2: YES`, 0 defects HOLD. Sol METER (return 3:32 PM), skipped, floor met (2 of 3, Grok satisfies Sol-or-Grok). `cobalt_redactions` +1 confirmed as the classification's known outside writer by both seats. Ready for C2: YES.

## L74

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date | `date` | 0 | allowed — Mon Sep 28 14:26:42 EDT 2026 |
| R17 grep | `grep -n "^\| R17 " cto-2026-09-24.md` | 0 | allowed — carries "Grok approved with no asking going forward" |
| R19 grep | `grep -n "^\| R19 " cto-2026-09-24.md` | 0 | allowed — carries "All 4 house models approved" |
| grok version | `grok --version` | 0 | allowed — grok 1.0.25 (f7e67d6988e2) [stable] |
| report tail | `tail -n 3 "<report>"` | 0 | allowed — last non-blank line EQUALS `<build stop>`, starts `S3 EXITS C1 FIX R2 BUILT ` |
| log oneline | `git -C cobalt log --oneline 9b25eced..944f632e` | 0 | allowed — one commit: 944f632e fix(s3-c1): fix r2 — C1's added test values constructed (L32, L75) |
| log stat | `git -C cobalt log --stat --format=%h 9b25eced..944f632e` | 0 | allowed — tests/cobalt/test_aset_web.py, tests/cobalt/test_fill_c1_offline.py |
| .env check | `ls .../s3-exits-c1/.env` | 1 | allowed — "No such file or directory" |
| recovery check | `ls scratch/tribunal-bars-0920/s3-exits-c1-fix-r2` | 1 | allowed — absent, fresh |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-28.md` | 0 | allowed — line 90 (R82), names 36-s3-exits-c1-fix-r2-check.md |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | allowed — OK, UP |
| probe SOL | `codex exec ... gpt-5.6-sol ...` | 1 | allowed — METER, "try again at 3:32 PM" |

Floor: 2 seats to launch (Opus, Grok); one of Sol/Grok present (Grok). Floor met.

## Files copied
`diff.part1.md`: 1 commit (`grep -c "^commit "` = 1 = PREFLIGHT's count).
| file | original B | copy B (parts summed) | match |
|---|---|---|---|
| build report | 38787 | 36139 + 2648 = 38787 | yes |
| classification draft | 10913 | 10913 | yes |
| r1-check report | 21808 | 21808 | yes |
| `35` prompt | 22346 | 22346 | yes |
| `20` prompt | 31610 | 31610 | yes |
| LAWS.md | 61011 | 30699 + 30312 = 61011 | yes |
| wt test_aset_web.py | 28816 | 28816 | yes |
| wt test_fill_c1_offline.py | 14888 | 14888 | yes |
| wt conftest.py | 10092 | 10092 | yes |
| wt test_redact.py | 19468 | 19468 | yes |
No mismatch.

## CONTINUE
next: none. This check is done; the desk reads the stop line.

## Clock
Sol: probed 14:2x, METER, return "3:32 PM" — not launched (skipped per L67/R82, no round spent). Opus: launched 14:33:50 ET, 45-min clock → 15:18:50 ET. Grok: launched 14:33:50 ET, 45-min clock → 15:18:50 ET.

## Per question
| Q | opus | sol | grok |
|---|---|---|---|
| (i) RED FIRST | HOLDS — `equal: yes` ×4 pre-fix, `equal: no` ×4 post-fix, no value quoted (`packet.md:7-14`, `:23-28`) | not launched (METER) | HOLDS — build report `:47,54-57,59` (yes×4); `:70-73,:276` (no×4), no value quoted |
| (ii) F5 | HOLDS — exactly 4 values changed (`test_aset_web.py:217,251,567`; `test_fill_c1_offline.py:296`); `75 passed in 0.62s` | not launched (METER) | HOLDS — one commit, two files, four replacements; base lines untouched; `75 passed in 0.62s` (build report `:75`) |
| (iii) SUITES | HOLDS — offline/with-DB/live-note all 0 failed, 0 errors; `cobalt_redactions` +1 explained by `test_redact.py:393` `monkeypatch.undo()` | not launched (METER) | HOLDS — same suites quoted; redactions reading confirmed via `conftest.py:188`, `test_redact.py:393,401,403` |
| (iv) SCOPE/SEAM | NOTHING WIDENED; SEAM whole, every cite re-read true in the worktree | not launched (METER) | NOTHING WIDENED; seam whole except `src/` and `test_fill_transaction_db.py` cites NOT CHECKABLE FROM READS (not copied to its folder) |
| (a) weak | NONE (one procedure note, not a defect: a `date` call between the `.env` check and the pytest call) | not launched (METER) | NONE |
| (b) score/rank/grade/size | NO PATH — test fixture values only; RESTARTS: none | not launched (METER) | NO PATH — commit doesn't touch `src` |

## Suites
From `<report>` (build report), facts:
- offline: `3246 passed, 410 skipped, 1 xfailed, 20 warnings`, exit 0 — 0 failed, 0 errors.
- with-DB pass 1: `3617 passed, 6 skipped, 33 deselected, 1 xfailed, 20 warnings`, exit 0 — deselects: `test_tenancy.py::TestMigrationRoundTrip`, `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`, `test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction`, `test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries`, `test_voice_store.py::test_single_flight_under_two_real_connections`, `test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both`, `test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped`, `test_legs_db.py`, `test_fill_transaction_db.py` (`20`'s eight + these two files' nodes = 33).
- with-DB pass 2 (at `0021`): `33 passed, 5 warnings`, exit 0, no SKIPPED line.
- Fingerprints: `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `<F1>` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `<F2>` = `<F0>` field for field, twice (rollback #1 14:22:35, rollback #2 14:23:04). `cobalt_dev: 0013 — F2 = F0`.
- X22: forward, back, forward, back — F = F0 twice; `design-changing: no`.
- live-note: `146 passed, 1 skipped, 15 warnings` — the one skip is `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set); no skip names `COBALT_LIVE_VAULT_ROOT`.
- `X1RF` reads: `aset_sizings` count `0`; joined `legs` count `0`.
- Per-table proof `<P0>` vs `<P2>`: 29 of 30 tables equal (rows + digest). `cobalt_redactions`: `182 · a2204cda0dcef1616682ab2723c9db1c` → `183 · d15f9c1f9bdde494213ee85dfae221b5` (+1; already 183 at the forward's before-probe 14:19, so it moved during pass 1 — the known outside writer, R61's OWED item, not a fix row here).
- `.env`: taken 14:07:57 (lock), removed + proven gone 14:23:44 (`ls` → "No such file"; `ls -la .../*/.env` → "no matches found").

## Scope
Opus (iv): NOTHING WIDENED; SEAM whole, every cite re-read true in the worktree (list in `opus-check.md`).
Grok (iv): NOTHING WIDENED; SEAM whole except `src/` and `tests/cobalt/test_fill_transaction_db.py` cites marked NOT CHECKABLE FROM READS (outside its confined folder; not a defect, L70).
My PREFLIGHT path union (`tests/cobalt/test_aset_web.py`, `tests/cobalt/test_fill_c1_offline.py`) against `35`'s F5 row's files (same two files, "Edit only; only the row's files"): EXACT MATCH, no widening. `35`'s NOT IN THIS FIX (`src/`, `cobalt_redactions`, `tests/cobalt/test_redact.py`, base replay lines, F1–F4) — my own greps (below) confirm none touched.
- `git -C cobalt log --oneline 9b25eced..944f632e -- src` → EMPTY.
- `git -C cobalt log --oneline 9b25eced..944f632e -- tests/cobalt/test_redact.py tests/cobalt/conftest.py` → EMPTY.
- `grep -n -F "fill_shares=" .../test_aset_web.py` → lines 217, 251, 567 (values not quoted, L32).
- `grep -n -F "monkeypatch.undo()" .../test_redact.py` → one hit: `393:        monkeypatch.undo()`.
- `grep -n -F "@app.post" .../aset/web.py` → nine routes, same lines as the round-1 check (`/size` 959, `/fill` 1060, `/attest` 1180, `/card/{card_id}/move` 1223, `/card/{card_id}/stop` 1278, `/radar/card/{card_id}/key` 1326, `…/dot/{factor}` 1378, `…/promote` 1417, `…/release` 1422) — no new route.
- L32 (vi): this report holds no ticker beyond constructed ones, no real date, share count or value of his.

## Checked against the branch
No `DOES NOT HOLD`, no `WIDENED`, no weak assertion, no L52 path from either seat — none to walk.

## FOR THE CLASSIFIER
1. F5's red/green equality shift HOLDS (Opus, Grok) — `packet.md:7-14,23-28`; build report `:47,54-59,70-73,276` — HOLDS.
2. Exactly four values changed, all other lines untouched, both files pass (Opus, Grok) — `diff.part1.md:14-52`; build report `:75` — HOLDS.
3. Three suites 0 failed/0 errors, `X1RF` zero, `.env` proven gone, 29/30 tables equal (Opus, Grok) — `packet.md` `## W THE THREE SUITES`; build report `:94,145,152,188-189,234` — HOLDS.
4. `cobalt_redactions` +1 explained by `test_redact.py:393` `monkeypatch.undo()` dropping the suite's `db.connect` patch (Opus, Grok) — `tests_cobalt_test_redact.py:393`; `tests_cobalt_conftest.py:133-134,188` — HOLDS.
5. Scope not widened; SEAM re-issued whole and true at `<tip>` (Opus, Grok) — `35-s3-exits-c1-fix-r2-build.md:26`; build report `## SEAM FOR C2` — HOLDS.

## ESCALATE
`cobalt_redactions` `182 · a2204cda…` → `183 · d15f9c1f…` (+1, during pass 1) — R61's OWED item; the desk's, not a fix row here; both checking seats confirm the classification's reading holds in the files.
Every item under `## FOR THE CLASSIFIER` above (5) — all HOLD, none contested.
Sol did not check: METER, return "3:32 PM" (probed 14:2x; the desk's R82 pre-declared Opus + Grok, floor met — no round spent, L67).
**Round 3 of ≤3 (L39) — THE LAST — of S3 C1: Opus 5.5 (Fable seat, R109) · Sol · Grok (R58). A HOLD goes to the desk and then to Dejan; there is no round 4. `ready for C2: YES` → `22-s3-exits-c2-build.md` stacks on `<tip>`.**

S3 EXITS C1 FIX R2 CHECK DONE · round: 3 · opus: CHECK S3 C1 FIX R2: BUILD STANDS · ready for C2: YES · sol: METER · grok: CHECK S3 C1 FIX R2: BUILD STANDS · ready for C2: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C2: YES · ESCALATE: 3
