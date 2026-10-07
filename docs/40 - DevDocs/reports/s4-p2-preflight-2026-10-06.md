# S4-P2 card 73 — preflight (2026-10-06, seat s4-p2-preflight, Sonnet 5.5, read-only)

Card `prompts/2026-10-06/73-s4-p2-card.md` · draft `reports/s4-cards-draft-2026-10-06.md` · main HEAD `192f5abe`. No test was run: `pytest` is not on this seat's allow line, so "red on base" is proved by absence of the file or module, and each control by the existing test file's presence and reading.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 HEAD` | `192f5abe` | OK |
| 2 | `git log --oneline -3 --name-only -- <card> <draft>` | `192f5abe docs(desk): S4-P1 and S4-P2 cards drafted…` lists both files; `git diff --stat HEAD` on the R598 files empty | OK (card and draft committed) |
| 3 | header per `CARD.md:9-28` | `JOB: s4-p2` · `LADDER: S4-P2 · F9` · `BRANCH: ops/s4-p2-1007` · `WORKTREE: s4-p2-1007` · `BASE: «FILL: …»` (the one) · `TIP:` / `CHECK REPORT:` / `HOUSE B:` empty · `REPORT:` in the worktree · `RULINGS: 2026-10-06 R598` · no `DB:` (rows touch `src/`); plain text, no backticks | OK |
| 4 | `ls cobalt-wt` / `git rev-parse --verify ops/s4-p2-1007` | no `s4-p2-1007` dir; branch absent (exit 1) | OK (both new) |
| 5 | `## DECISIONS` heading | `desk-launch.sh` calls `section ROWS` only for build (`:885`, `:906`), no order check; `CARD.md:30-61` does not list `DECISIONS` as a body section (named only as a report item, `:55`, `:97`) | OK (launcher accepts it; format is silent) |
| 6 | `grep -n "R598" cto-2026-10-06.md` | `:86 | R598 | 19:59 ET | HIS RULING (…) | HIS RULING · APPROVED`; file unmodified vs HEAD | OK |
| 7 | `web.py:88`, `:93` | `app = FastAPI(...)`; `app.include_router(voice_web.router)` | OK |
| 8 | `web.py:1799-1815` (his tap) | `@app.post("/radar/card/{card_id}/triggered")` … `return await _card_tap(card_id, request, "aset.radar.triggered", work)`; evidence `via` = `f"{source}.triggered"`, `source` = the form's `source` or `"panel"` (`:1779`) | OK as a cite; see FAIL row 24 |
| 9 | `radar_panel.py:1605-1606` | `window.setInterval(refreshPool,interval);` `window.setInterval(tickLadder,interval);` | OK |
| 10 | `config.py:81-86`, `:128-129` | `:81 bind: Literal["loopback","lan"]`, `:82 port 5010`, `:85 def host` (0.0.0.0 for lan); `:128 def load_config`, `:129 path = LOCAL_CONFIG_PATH if … exists() else CONFIG_PATH` (local first) | OK |
| 11 | `.gitignore:50` | `configs/dev/aset.local.yaml` | OK |
| 12 | `notify/mattermost.py:130` | `def send_dm(message, *, cfg=None) -> SendResult` | OK |
| 13 | `cards/store.py:1124` | `ticker, grade, direction, sheet_mode, …` in the `aset_sizings` INSERT; `sized_grade` is a column (`0007_radar_cards.sql:44`), `shares`, `stop` in the same INSERT / SELECT | OK |
| 14 | `jobs.yaml:39-91`, `:71`, `:83`, `:90`, `:194`, `:318-325` | aset label `:39`; `:71` "the schema refuses a path in both"; `:83` stale `web.py:90`; `:90 imports: [cobalt.aset.__main__, cobalt.aset.web]`; radar `:194 imports: [cobalt.cli]`; `:318 no_resident_reads`, `:325 No resident sends a DM` | OK |
| 15 | `restarts.py` classes | `:210 resident reads`, `:220 static import reach`, `:222 non-Python src asset`, `:224 registry; register, no restart`, `:228 DOCS`, `:232 operator script; no Cobalt reader`, `:246 test/documentation; no resident`, `:258 UNCLASSIFIED CONFIG` | OK (each path's class is in `## RECORDS` of the card's RESTARTS paragraph) |
| 16 | Charter / ladder cites | Charter `:116-117`, `:120`, `:121-126`, `:54`, `:227`, `:242`, `:248-250` and ladder `:812`, `:815`, `:850-851` read and match | OK |
| 17 | A0 seam vs P1 card `72` C2 CONTRACT (P1 not on main: no `src/cobalt/strike/`, no `detector.md`) | P1 CONTRACT keys: `via, policy, entry, cross_price, bar_ts, bar_close_at, seen_at, cadence_s, def_md5, card_def_md5`; vias `strike.detector` / `strike.missed`; `strike.alert_criterion_s` in T1 — identical to card 73's list | OK (against card 72's contract; the real `detector.md` is A0's job at BASE) |
| 18 | new files absent on main: `aset/strike.py`, `tests/cobalt/test_strike_stream.py`, `configs/cobalt/strike.yaml` | `ls`: no such file (×3); `src/cobalt/strike/` absent | OK (S1/S2/S4 red = 404 / `ModuleNotFoundError`; S5, S6 and `test_strike_config.py` depend on P1's package, verified against card 72 only) |
| 19 | controls exist: `test_aset_web.py`, `test_radar_panel.py`, `test_notify_mattermost.py`, `test_jobs_reads.py`, `test_jobs_restarts.py`, `test_validate_no_db.py`, `test_placement.py`, `tests/ops/test_gate.py`, `test_tenancy.py` | all present | OK (not run) |
| 20 | scope vs ladder `## S4` P2 (`:812`, `:815`) | S1 SSE · S2 tab, notification, sound · S5 hotkey (+ three numbers in S1/S2) · S4 Mattermost DM · S6 week report. S3 (ack + `strike_alerts` record) is the support for S4 and S6, named as E4; nothing else added. No trading platform read or touched (hotkey is a label; `## NOT IN THIS JOB` says so) | OK |
| 21 | E1: any row assuming Notification over HTTP | S2 shows `NOTIFICATIONS OFF — <reason>` when `isSecureContext` is false, fires `Notification` only "when permitted" | OK |
| 22 | S4 config move: `notify.yaml` from `no_resident_reads` into aset `reads:` vs existing tests | `test_jobs_reads.py:159 test_notify_yaml_is_declared_with_one_shot_readers_only` asserts `no_resident_read(NOTIFY)` is not None → RED; its `_raw` helper (`:167-170`) puts NOTIFY in `no_resident_reads` beside aset's `reads:` → the registry refuses ("re-read by a resident"). `test_jobs_restarts.py:191-199 test_a_declared_one_shot_only_config_derives_no_restart` expects notify.yaml → no restart → RED. Row S4 lists neither file; the card calls `test_jobs_reads` "green" and gates on both | FAIL |
| 23 | E4 migration vs repo rules | next free `0023` (highest `0022`; `0012` never existed). `0009:1-5` tenancy shape OK. Registration is NOT in `db_migrations/cli.py:100-140` (that is `DIGEST_EXCLUDED_COLUMNS`); it is `db_migrations/__init__.py` `FORWARD` (`:135`) and `REVERSE` (`:160`) and `db_migrations/placement.py` `CREATED_TABLES` (`:64`, the tenancy test iterates it at `test_tenancy.py:276`). `test_tenancy.py:505-517` pins `_rollback_paths("0004")[:12]` with `0022` first, so `0023` breaks it | FAIL |
| 24 | S1 negative fixture | the card's his-tap `via` is `aset.radar.triggered`; the real value is `<source>.triggered` (`panel.triggered` / `sheet.triggered`, `web.py:1779`, `:1810-1812`); `aset.radar.triggered` is the gate name | FAIL |
| 25 | R411 / R412: no new command or argument beyond the draft's decisions | S6 adds `cobalt strike week [--from <date>] [--to <date>]`; no decision E1-E7 names the verb or its two flags (E5 names only the lag clock). No seat runs it (card: "the desk's, after the week") and no row adds a seat allow-line string | FAIL |
| 26 | gate lists W1 | `ops/desk/gate-lists.md:5-7` rule and `:10-11` header match the card; W1 gives no expected count for `grep -c -F "test_strike_"` (P1's W1 states `2`) | OK (NOTE 4) |

## ISSUES
- FAIL 22: S4 must list `tests/cobalt/test_jobs_reads.py` (replace `test_notify_yaml_is_declared_with_one_shot_readers_only` and the `_raw` helper's no-resident-reads fixture with another one-shot-only file) and `tests/cobalt/test_jobs_restarts.py:191` (a NAMED REVERSAL like DRC D3's rules.yaml at `:204-215`) in its `files` and as red-first rows; drop "green" for `test_jobs_reads`.
- FAIL 23: S3's files must name `src/cobalt/db_migrations/__init__.py` (`FORWARD`, `REVERSE`), `src/cobalt/db_migrations/placement.py` (`CREATED_TABLES`) and `tests/cobalt/test_tenancy.py` (the `:517` head pin), not `cli.py`; check the other tests that name `0022` (`test_p4_migrations.py`, `test_archiver_migrations.py`, …) for head pins.
- FAIL 24: S1's negative row should use `via` = `panel.triggered` (actor `you`), the value his tap really writes.
- FAIL 25: add a decision (E8) naming `cobalt strike week` and `--from` / `--to`, or drop the flags; per R412 a new command goes to him.
- NOTE 1 (material): the DM fallback depends on a `strike_alerts` row that S3 creates at the first SSE send. With no tab connected (the case the DM exists for) no generator tails the seam, so no row, no DM. S4 must tail the seam itself or S3 must create the row at the transition; `dm_after_s` is not said to count from the seam row's `at`. No test covers "no stream ever connected".
- NOTE 2: S3's ack write and S1's tail are said to run off the event loop only for the read; the ack's DB write is not (X2).
- NOTE 3: `BASE` is the one `«FILL` and `desk-launch.sh` refuses the card until it holds main after P1 deploys; `test_strike_config.py` (S5) and S6's `cli.py` are P1's files, checked here against card 72 only.
- NOTE 4: `test_strike_stream_db.py` needs only `0007`-level tables, so by the gate-lists rule (needs a level above `0013`) it may not need a `--deselect`; P1's W1 treats its own DB test the same way, so this is consistent but unproven.
- NOTE 5: E1 open (his); no row fails on it.

PREFLIGHT DONE · card: s4-p2-73 · checks: 26 · fails: 4 · ready: NO
