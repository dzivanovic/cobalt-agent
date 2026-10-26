# draft-f4-gate-run · 2026-10-26

## §0 Headline
- Drafted `prompts/2026-10-26/1045-f4-gate-run.md`: seat `f4-gate-run`, CLASS K2, LADDER `S5-P2 · F4`, RULINGS `2026-10-18 R1863`, the 970 shape, 5 `GATE RESULT` lines for `com.cobalt.prefill-refresh`.
- Runs: X7 offline pytest leg, X8 offline pytest leg, X9 `cobalt jobs restarts 5623c3ff..54feb833` plus the deploy-log bounce read (28 s). X10 and X15 run nothing.
- No item can read exactly `OK` from this hub: X7 and X9 hold a [HIS HAND] leg, X8's measurement needs the plist loaded, X10 is the desk's from DEPLOYED, X15 has no command.
- Seven ASK DESK below; the bootstrap needs the brain to rule X8, X10 and X15 (or a probe card for X15).

## DECISIONS
- ASK DESK: X10 — the three L68 suites run on a gate worktree (gate.sh), never from `/Users/cobalt/cobalt`, whose `.env` pytest loads (`tests/conftest.py:13`). May the desk write X10 from `deploy-f4-refresh-attempt2.md:263` (offline 8539/0 · with-DB 5552/0 · live-note 146/0 on `db62c4b5`), or does it need a fresh gate on today's main? Default: `NOT RUN`, as 1045 writes it. [07:55]
- ASK DESK: X8 — no command measures per-minute Finviz demand, redirects or 429s per consumer before load; FINAL `:214` measures the loaded plist (105 entries, 21 runs on one weekday). Rule it a post-load watch, or name a probe card? Default: `NOT RUN`; the plist stays unloaded. [07:55]
- ASK DESK: X15 — no command or test exists (grep of `tests/cobalt` for `x15` finds no F4 test) for 5 ARMED dev cards, radar planned 40, a refresh at the strike loop's steady state, counted per minute at the transport. FINAL `:221`: a minute above 50 or a 429 → a strike-side reservation row on the F4 card before load. A probe card is owed. Default: `NOT RUN`. [07:55]
- ASK DESK: X7 — two clauses of FINAL `:213` have no offline test today: a missing tunable refused, and the daymode unit still starting `as of` after a later `daymode.note.write` (the only test of untouched units, `test_t7_…` `test_prefill_refresh.py:1037`, is with-DB). 1045's offline leg leaves them out. Default: recorded as unproven; X7 stays `NOT RUN` until his Obsidian read and a ruling. [07:55]
- ASK DESK: pytest from this checkout opens one rolled-back `cobalt_dev` connection per test when `.env` names a Postgres host (`tests/cobalt/conftest.py:289-298`), as 970's pytest steps did. 1045 runs pytest only with the `.cobalt_dev.lock` absent. Default: run as 970 did. [07:55]
- ASK DESK: X9 — launchd firings and sleep/wake (FINAL `:215`) need the plist loaded; 1045 states them unmeasurable before load. Default: `NOT RUN` with his Sync leg. [07:55]
- ASK DESK: the card `778` `## LAUNCHD` line is `deferred` (`:21`); `deploy-step-c.sh --bootstrap-only` admits only `add` (`:176`) and reads the `GATE RESULT` lines from the card it is given (`:185`). The desk writes a bootstrap card as for cos (`2026-10-20/929-deploy-cos-bootstrap-card.md`). Default: the desk's bootstrap card. [07:55]

## RECORDS
- 07:50:42 `date`. HEAD `2649aa16` (`git rev-parse --short=8 HEAD`).
- Read whole: `prompts/2026-10-26/1043-draft-f4-gate-run.md`, `prompts/2026-10-21/970-f5-gate-run.md`, `prompts/2026-10-19/873-cos-gate-run.md`, `prompts/2026-10-18/778-deploy-f4-refresh-card.md` (`## LAUNCHD` `:20-21`), `data/deploy/bootstrap-owed.json` (`:2`), `ops/desk/deploy-step-c.sh` (`:176`, `:185-186`), `src/cobalt/prefill/cli.py` (`refresh` `:88-99`), `ops/desk/gate-lists.md` `:1-46`, `tests/conftest.py`, `topics/writing-rules.md`.
- `docs/30 - Design/F4-FINAL-2026-10-10.md`: gate table found by Grep, `## First-gate experiments (L70)` `:200`; read `:200-224` (X7 `:213`, X8 `:214`, X9 `:215`, X10 `:216`, X15 `:221`).
- `git grep HEAD` proved: `pyproject.toml:73` (`prefill` script), `src/cobalt/jobs/cli.py:194-196` (`restarts`), `src/cobalt/cli.py:554` (jobs group), `src/cobalt/jobs/restarts.py:274-276` (`ESCALATE:`, `RESTARTS:`), `src/cobalt/prefill/daily.py:794` (gate check), `:1109` (`VaultWriteStore()`), the test names of `tests/cobalt/test_prefill_refresh.py` and `@requires_db` at `:669`, `:709`, `:866`, `:955`, `:1035`, `:1181`; `tests/cobalt/test_prefill_refresh_experiments.py` (offline: only `test_a1_4_x17`), `tests/cobalt/test_finviz_consumers.py`.
- Read `tests/cobalt/test_prefill_refresh.py` `:1-75`, `:160-234` (fixtures offline), `:296-525`, `:1036-1181`; `tests/cobalt/conftest.py` `:1-80`, `:150-309`.
- `reports/deploy-f4-refresh-attempt2.md`: grep → `:6` range `5623c3ff` → `54feb833`, `:189` `<t down>` 12:42:45, `:204` `<t up>` 12:43:13 downtime 28 s, `:229` restarts `5623c3ff..54feb833` → aset radar, `:263` DEPLOYED line. The 1045 grep was run once here to prove it prints exactly `:189` and `:204`.
- `git rev-parse --short=8 deploy-2026-10-18-f4-refresh-attempt2` → `54feb833`. `ls` → the deploy report and `ops/com.cobalt.prefill-refresh.plist` exist. `ls -la /Users/cobalt/cobalt/.env` → exists (not opened).
- No test or command was run besides the reads above. Wrote `prompts/2026-10-26/1045-f4-gate-run.md` and this report; committed nothing.
- 07:54:34, 07:55:45 `date`.

## REVISION (brain R2463, 08:03)
### §0
- The seven ASK DESK above are ruled (R2463 of `cto-2026-10-26.md:13`, read by grep). Revised `1045`; drafted `prompts/2026-10-26/1047-f4-probe-card.md` (K2, BAND HIGH) and `prompts/2026-10-26/1048-deploy-prefill-refresh-bootstrap-card.md` (929 shape).
- 1045: X10 `OK` cited from `deploy-f4-refresh-attempt2.md:263`; X8 `RULED post-load watch`; X9 hub legs OK plus his Sync; X15 and X7's two new tests in a SECOND PASS after f4-probe deploys. Two strings added to the launch line: the T1/T2 pytest and `COBALT_ENV=dev uv run prefill probe X15`. Last line gains `ruled: <n>`.
- 1048 `## GATE RESULTS` carries X10 and X8 only. `deploy-step-c.sh:185` admits any non-empty result, so X7, X9 and X15 stay absent until each reads `OK`; the script refuses until then (the load rule).
- Four open ASK DESK below; the stop line counts them.

### DECISIONS
- ASK DESK: X15 likely FAILs by arithmetic. With headroom 10 and 5 ARMED names, `poll_interval` (`strike/detector.py:103-108`) gives 30 s = 10 rpm. Radar 40 + strike 10 = 50 at steady state, and the refresh's 3 GETs land in one minute: 53. If so, FINAL `:221` puts a strike-side reservation row on the F4 card before load (L75). Draft that card now, in parallel with f4-probe? Default: wait for the probe line. [08:03]
- ASK DESK: X15 runs in process on a virtual clock with a mock transport (1047 DECISION 1). A live dev run would share the production Finviz account with the running radar. Default: no live variant. [08:03]
- ASK DESK: 1047 T1 and T2 pin existing behaviour, so they are expected GREEN on BASE, not red first (`CARD.md:42`). A red on BASE is a `## DECISIONS` item there. Default: as written. [08:03]
- ASK DESK: 1048's TAG is dated 2026-10-27, and the card numbers 1047 and 1048 were free at 07:59 (`ls`). Default: the desk re-dates or renumbers at launch. [08:03]

### RECORDS
- F4 gate 1045 — X10 OK from the attempt2 deploy gate; X8 post-load watch (FINAL :214 R3); X15 load gate by probe card f4-probe (+X7 two offline tests); X7 render and X9 Sync legs his; X9 firings post-load — brain 9b07db5a 2026-10-26
- The desk's message (cross-session, cto-desk) relayed R2463; `grep -n -F "R2463" reports/cto-2026-10-26.md` → `:13` DESK RECORD (brain 9b07db5a, L79), `APPROVED — pending fold`.
- Read for 1047: `prompts/2026-10-21/973-f5-probe-card.md`, `prompts/CARD.md:9-86`, `:149-150`; `src/cobalt/strike/detector.py:60-189`, `:236-356`; `src/cobalt/strike/measure.py`; `src/cobalt/prefill/daily.py:755-806`; `src/cobalt/archiver/collector.py:205-274`; `src/cobalt/radar/collector.py:40-79`; `src/cobalt/daymode/note.py:80-189`; `tests/cobalt/test_prefill_refresh.py:75-110`; `configs/cobalt/taxonomy/tunables.yaml:700-709` (`radar.finviz_max_rpm` 50). `git grep HEAD`: `src/cobalt/cli.py` imports (no `prefill.cli`), `strike/cli.py:13`, `checkpoints.py:860`, `env.py:60`, `market.py:55`, `calendar.py:62`, `:83`, `configs/cobalt/jobs.yaml` prefill lines. `ls`: `checkpoint_probe.py`, `docs/40 - DevDocs/cobalt/prefill/`. `git rev-parse --short=8 main` → `05366873` (1047 BASE).
- Read for 1048: `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md`; `ops/com.cobalt.prefill-refresh.plist` (`RunAtLoad` false `:149-150`, logs `:151-154`); `DEPLOY-HUB.md:146` (4.6L-BO) by grep.
- Wrote: `1045` (edited), `1047`, `1048`, this section. Nothing run but reads; nothing committed.
- 08:03:06 `date`.

## REVISION (brain R2465)
### §0
- The 4 asks are ruled (R2465 of `cto-2026-10-26.md:13`, checked by grep): (a) YES, (b)–(d) KEEP. I drafted `prompts/2026-10-26/1049-f4-strike-reserve-card.md` (K2, BAND HIGH); `ls` showed 1049 free.
- 1049: inside `prefill.refresh_window` (ET), the strike loop subtracts refresh's one-minute burst (3 rpm) from its headroom and shows that burst to the gate. Outside the window its interval is unchanged. With radar 40, ceiling 50 and 5 names, the worst minute drops from 53 to 49.98 (30 s → 43 s). It launches only on `PROBE X15 FAIL`, and is dropped if X15 is `OK`.

### DECISIONS
- ASK DESK: the reservation slows the strike loop inside 05:45–15:45 ET (5 names at radar 40: 30 s → 43 s, measured against `strike.alert_criterion_s`). It also edits the existing pin `test_with_the_radar_at_30_rpm_five_names_poll_every_15_s` (`test_strike_detector.py:145`: 15 → 18 s inside the window, plus a 15 s twin outside it). Default: the brain weighs the cost when it launches 1049 on the FAIL line. [08:06]

### RECORDS
- Read: `tests/cobalt/test_strike_detector.py:1-185`; `src/cobalt/radar/notes.py:276-400`; `F4-FINAL-2026-10-10.md` lines `:67`, `:221`, `:315` by grep; `LAWS.md` L75 by grep. `git grep HEAD`: `REFRESH_GETS` `prefill/daily.py:682`, `parse_window` `jobs/config.py:34`, `DemandWindow` `radar/notes.py:173`, no `cobalt.prefill` import under `src/cobalt/strike` or `src/cobalt/radar`, the strike interval and demand tests. `ls`: `docs/40 - DevDocs/cobalt/strike/detector.md` present.
- Wrote `1049` and this section. Nothing run but reads; nothing committed.
- 08:06:38 `date`.

## REVISION (preflight)
### §0
- Fixed the two FAILs in `reports/f4-gate-preflight-2026-10-26.md` `## ISSUES`. In 1048 `## SMOKE READS`, row 1 now expects `exit 0, a count of 1 or more` and row 2 expects `` exit 0, `1` ``. In 1047 `## DEPLOY PROOF`, marker 2's pattern is now `"PROBE_ITEMS = ("`, before `0`, after `1`, as in 973:62.
- One more fix, same rule. 1048 row 2's pattern `"REFRESH_JOB = \"com.cobalt.prefill-refresh\""` had a backslash; `deploy-smoke.sh:125-127` cuts at the first quote and refuses a backslash. It is now `"REFRESH_JOB = "`, which counts `1` on `src/cobalt/prefill/cli.py` (checked with `grep -c -F`). The preflight's 5d said this row was a mapped shape.
- 1049's smoke row now expects `exit 0, a count of 1 or more`; it had `prints 1 or more`, the same unread expectation.
- NOTE 2: `grep -c -F` of the R2463 line the desk relayed gives `1` in each of 1045, 1047 and 1048, so the prompts carry exactly that line.

### RECORDS
- Read: the preflight report (`grep` of `## ISSUES` and the FAIL/NOTE rows); `ops/desk/deploy-smoke.sh:110-139` (`shape()`).
- `grep -c -F "PROBE_ITEMS = (" src/cobalt/prefill/checkpoints.py` → `1` (973's pattern still maps on main). `grep -c -F "REFRESH_JOB = " src/cobalt/prefill/cli.py` → `1`.
- Edited 1047, 1048, 1049 in place; nothing committed.
- 08:11:33 `date`.

DRAFTED PF · decisions: 0
