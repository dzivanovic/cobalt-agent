# f4-probe check card 1055 — preflight, 2026-10-26 (09:29 ET)

Read only. Subject: `prompts/2026-10-26/1055-f4-probe-check-card.md`. Tip `2e0d5f77b` read via `git show` / `git grep`, and the branch worktree for line views.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | header keys vs `CARD.md` `## THE HEADER` (check column) | JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, BAND, RULINGS all present, in table order; extra CLASS, INSTALL, RESTARTS (RESTARTS is in precedent 1041; CLASS, INSTALL are copied from 1047) | OK (NOTE N1) |
| 1b | `grep -n -E "FILL\|«"` on the card | no output | OK |
| 1c | `CHECK REPORT:` value | `reports/f4-probe-check-2026-10-26.md`, relative. `CARD.md:20` requires an absolute path under `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`; precedent 1041 line 8 is absolute | **FAIL** |
| 1d | `git rev-parse --verify 596ca32f^{commit}` | `596ca32ffcf062dcfa2a02c14a564e05b95c6046` | OK |
| 1e | `git rev-parse --verify 2e0d5f77b^{commit}` | `2e0d5f77b3ab00d2d739a46d2f49aa4724078059` | OK |
| 1f | `git merge-base --is-ancestor 596ca32f 2e0d5f77b` | exit 0 | OK |
| 2 | `git diff 596ca32f..2e0d5f77b --stat` | 7 files, 870 insertions, 0 deletions; `cli.py` +12, `refresh_probe.py` +458, `cli.md` +22, `daily.md` +3, build report +89, `test_prefill_refresh.py` +46, `test_refresh_probe.py` +240 — equals the card's set; `src/` = the two prefill files only | OK |
| 2b | `git diff 2e0d5f77b 1b25f0a1c --stat` | build report and its `.result` only (card RECORDS: "adds only the build report and its .result") | OK |
| 3a | `git grep` `refresh_probe.py` at tip | `:50 PROBE_ITEMS`, `:52 EXIT`, `:54 TOKEN`, `:56 DAY`, `:62 CONSEQUENCE`, `:67 _MAX_SPINS`, `:103 VirtualClock`, `:181 handle`, `:184 in_minute >= self.ceiling`, `:209 _probe_client`, `:236 _boundary`, `:321 _radar`, `:334 _strike`, `:338 detector.tick()`, `:343/:348 _refresh/_gated_fetch`, `:358 _clause`, `:375 if peak > ceiling or throttled:`, `:380 _x15`, `:390 ceiling != FINAL_CEILING`, `:411`/`:414 error network`, `:417-418` gate refusal, `:426 _dev_only`, `:435 _verdict`, `:437 logger.disable`, `:451 main` | OK |
| 3b | Read `refresh_probe.py:254-262` | `:255 (httpx, "AsyncClient", …)`, `:256-257` handle_async_request / handle_request → OffMock, `:258-259 resolve_token`, `:260 read_plan` | OK |
| 3c | `git grep` `cli.py` at tip | `:44`, `:59 as_job` untouched; `:77 def main`; `:96 import PROBE_ITEMS`; `:98-99 add_parser("probe")`, `choices=PROBE_ITEMS`; `:103-107 if args.command == "probe"` … `sys.exit(refresh_probe.main(args.item))` | OK |
| 3d | `git grep` `test_refresh_probe.py` / `test_prefill_refresh.py` | tests at `:85, 94, 106, 147, 165, 176, 187, 200, 208, 221, 237`; `test_prefill_refresh.py:491, 511`, `daymode_note.write(...)` `:529` | OK |
| 3e | `git grep` other anchors | `finviz_get collector.py:205`, `httpx.AsyncClient( :222`, `fetch_bars :255`; `radar TokenBucket :42`; `detector.py :80 DemandPlan, :103 poll_interval, :131 StrikeDetector, :238 tick, :313 read_plan`; `daily.py :759, :780, :800`; `note.py :83 render_body, :105 format_stamp(, :140 write`; `env.py:60 resolve_env` | OK |
| 3f | Read `daily.py:757-806` | `:767` missing / `value is None` check, `:769` raise, gate `:787-797`, `_gated_fetch :800` | OK |
| 3g | `git grep -A1 finviz_max_rpm` tunables | `:702 key: radar.finviz_max_rpm`, `:703 value: 50` | OK |
| 3h | `git grep "^\| X(7\|15) "` FINAL | `F4-FINAL-2026-10-10.md:213` X7, `:221` X15; `:221` text "A minute above 50 or a 429" matches the `:375` rule | OK |
| 3i | `_CONSUMER` ContextVar | `:68` declared; set at `:324` radar, `:335` strike, `:346` refresh; read at `:191` inside `handle` | OK |
| 3j | Read `_clause`/`_x15`/`_verdict` | `_dev_only()` is the first call in the `try` (`:439`, def `:435`); NOT RUN → `—`, exit 3; FAIL appends `CONSEQUENCE` (`:376`); clause carries counts only | OK |
| 4a | card's commands vs `CHECK-HUB.md:10` allow line | `uv run pytest`, `uv run cobalt jobs restarts`, `ls`, `grep`, `git diff/log/show`, `sh /Users/cobalt/cobalt/ops/desk/*` all listed; `DEPLOY PROOF` uses `ls` and `grep -c -F` only; no Finviz host, `COBALT_ENV=production`, `launchctl`, database or `.env` | OK |
| 4b | ORDER suite files at TIP: `ls` in `/Users/cobalt/cobalt-wt/f4-probe/tests/cobalt/` | `test_refresh_probe.py`, `test_prefill_refresh.py`, `test_finviz_consumers.py` all listed | OK |
| 5a | `RESTARTS: none` vs build report | build report `## RESTARTS`: `RESTARTS: none`, `src/` rows `static import reach · -`; `grep -rn -F refresh_probe src configs` → `prefill/cli.py` and the module only | OK |
| 5b | CLASS K2 / BAND HIGH vs `CARD.md` | BAND HIGH: valid value, copied from 1047 (`BAND` required on a card dated 2026-10-16 or later). CLASS: `CARD.md` defines no check-card `CLASS` key (K3 appears only for prodwrite) and no `K2` anywhere in CARD/CHECK-HUB/BUILD-HUB; value matches 1047 line 3 | OK (NOTE N1) |
| 6a | BUILD DECISIONS vs build report `## DECISIONS` and R2479 | (1) T2 `_cfg()` — report DECISION 1; (2) no inventory entry — report DECISION 2; (3) default FAIL peak 53/min at 08:43, 3 × 429 — report DECISION 3; R2479 row 17: "T2 _cfg pin and no inventory entry accepted" | OK (NOTE N2) |
| 6b | card 1047 `DECISION 1–3` (lines 67-69) vs card text | DECISION 1 in process, virtual clock, mock transport; 2 radar stand-in at 40 rpm via `finviz_get`; 3 BAND HIGH — all reflected in the card's WHY, X15 row and BAND | OK |
| 6c | `## NOT IN THIS JOB` | gate seat's run of `prefill probe X15` / `refresh` (line 36), strike-side reservation row (L75) and X8/X9 post-load watches (line 38), live variant, configs / plist / launchctl | OK |
| 7 | `HOUSE B: as needed` vs `CARD.md:21` | `as needed` is an allowed value | OK |
| 8 | R2463 / R2479 rows | `grep -n "^\| R2463 \|^\| R2479 "` → lines 33 and 17 of `cto-2026-10-26.md`, both present, brain 9b07db5a, L79 | OK |

checks: 28 · fails: 1

## ISSUES

- FAIL · header `CHECK REPORT` (row 1c): `reports/f4-probe-check-2026-10-26.md` is relative; `CARD.md:20` needs `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md` (precedent 1041 line 8). The card's RECORDS call it a desk-owned value, but the desk fills it in as written and the check launch would read a path that is not absolute. BLOCKS the launch: change it, commit, then launch.
- NOTE N1 · header `CLASS: K2`, `INSTALL: none`: not in `CARD.md`'s check column and absent from precedent 1041. Copied from card 1047, so consistent with the build; harmless extra keys. Not a block.
- NOTE N2 · card WHY and row P1 say `_dev_only` is called first in `_verdict`: the call is at `:439`, after `logger.disable` at `:437` (def at `:435`). Same effect; no request precedes it. Not a block.
- NOTE N3 · `git -C … log 9b07db5a` is not a commit (card RECORDS says the same); the card cites R2463 and R2479 instead. Not a block.
- NOTE: card 1055 itself and its report `.result` were not in `git status` as committed here; the hub's own committed-and-unchanged gate will check that at launch.

PREFLIGHT DONE · cards: 1055 · checks: 28 · fails: 1 · ready: NO
