# S4 cards draft — 2026-10-06 (drafter s4-cards-draft, prompt 70)

## §0 Headline
- Two build cards drafted: `prompts/2026-10-06/72-s4-p1-card.md` (S4-P1, measurement script + detector, 8 rows) and `73-s4-p2-card.md` (S4-P2, SSE tab + notification + DM fallback + week report, 9 rows). Each card's one `«FILL` is `BASE`.
- P1's seam is the `card_transitions` rows (`via` = `strike.detector` / `strike.missed`) with a fixed evidence CONTRACT. P2 reads that seam and nothing else (A0 proves it at BASE).
- The live measurement needs market hours and a command on no seat's allow line. The build seat builds and tests it but never runs it (D1, its run string is his to approve).
- Biggest gaps: the Finviz budget (strike 100 rpm vs his ruled 50, D2 FOR DEJAN), and browser notifications need HTTPS while the sheet is plain HTTP over Tailscale (E1 FOR DEJAN).
- 14 decisions, each with a default. 2 are FOR DEJAN and 3 are his named preconditions (F8 live; PC reaches :5010; `.htk` key labels).

## CARD
S4-P1: `JOB: s4-p1` · `LADDER: S4-P1 · F9` · `BRANCH: ops/s4-p1-1007` · `WORKTREE: s4-p1-1007` · `BASE: «FILL: main HEAD at launch, 8 hex»` · `TIP:` · `REPORT: /Users/cobalt/cobalt-wt/s4-p1-1007/docs/40 - DevDocs/reports/s4-p1-build-2026-10-07.md` · `CHECK REPORT:` · `HOUSE B:` · `RULINGS: 2026-10-06 R598`. No `DB:` key (rows touch `src/`).
S4-P2: `JOB: s4-p2` · `LADDER: S4-P2 · F9` · `BRANCH: ops/s4-p2-1007` · `WORKTREE: s4-p2-1007` · `BASE: «FILL: main HEAD at launch, 8 hex»` (main after P1 deploys) · `TIP:` · `REPORT: /Users/cobalt/cobalt-wt/s4-p2-1007/docs/40 - DevDocs/reports/s4-p2-build-2026-10-07.md` · `CHECK REPORT:` · `HOUSE B:` · `RULINGS: 2026-10-06 R598`. No `DB:` key.
Both cards carry `## DECISIONS` (the prompt's order; `CARD.md` lists no such section, so `desk-launch.sh` acceptance of the heading is the desk's to confirm).

## DECISIONS
- D1 ASK DESK (P1): the live measurement run needs market hours and a command on no seat's allow line, so the build only builds and tests it. Default: the desk launches one run from the P1 worktree on 10-08, 10 min premarket + 10 min RTH: `COBALT_ENV=dev uv run cobalt strike measure --names LULU,TSLA,NVDA,INTC,DELL --cadence 3 --minutes 20 --out …`. Its verdict fixes the criterion: HOLDS → 3 s / 5 s; THROTTLED → 10 s / ~8 s, as a config diff. The run string is his. [20:05]
- D2 ASK DESK · FOR DEJAN (P1): `radar.finviz_max_rpm` = 50 by his R17 2026-09-17. Strike at 5 × 3 s = 100 GET/min on the same account. Default: its own bucket at 100, the radar's 50 untouched, the measurement stops at the first non-200. [20:05]
- D3 ASK DESK (P1): MISSED on a WATCH cross is terminal and runs on 100 s-old stored bars. Default: build it (Charter F7). Alternative: leave it to the nightly F12 replay. [20:05]
- D4 ASK DESK (P1, L52): if more than 5 cards are ARMED, watch the five armed earliest and log the rest; no ranking. [20:05]
- D5 ASK DESK (P1): sequence triggers and steps with no policy are not watched and are logged. [20:05]
- D6 ASK DESK (P1): manual cards are not watched (they have no trade_def, so no policy). [20:05]
- D7 PRECONDITION, his (P1): F8 live. Today's radar-drought surveys (prompts 17, 19, 37) are open with the desk. [20:05]
- E1 ASK DESK · FOR DEJAN (P2): browsers allow the Notification API only on a secure origin, and the sheet is HTTP on 0.0.0.0:5010. Default: the tab ships sound, a flashing title and a loud `NOTIFICATIONS OFF — insecure origin` banner. A secure origin is his to set up: Tailscale HTTPS, or the PC browser's "treat as secure" setting. [20:05]
- E2 PRECONDITION, his (P2): the PC reaches `:5010/strike` over Tailscale. R27 says the PC is on Tailscale, but reaching the sheet from it is unproven. [20:05]
- E3 ASK DESK (P2): the alert's title is ticker + side and its body is key · shares · stop · hotkey. [20:05]
- E4 ASK DESK (P2): store the ack and DM times in a new `"user".strike_alerts` table (a migration). The alternative is a rotating JSON log. [20:05]
- E5 ASK DESK (P2): measure `intrabar` lag from `seen_at`, close-type lag from `bar_close_at`, and report the two apart. [20:05]
- E6 PRECONDITION, his (P2): the `.htk` key labels match `{DAYMODE}-{KEY}-{SIDE}`. R27 covers only the file names. The template is config. [20:05]
- E7 ASK DESK (P2): `dm_after_s` = 10. [20:05]

## RECORDS
All reads at main HEAD `2812c2ef` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`, 2026-10-06 20:05 EDT); one Bash / Read / Grep call each.
- `SPRINT-LADDER-v0_1.md`: `grep -n "^## \|^### "` → S4 at `:804`; `sed -n '1,53p;804,860p'` → glance `:33`, preconditions `:806-808`, F9 row `:812`, prompts owed `:814-815`, carried items `:850-851` (R27 Tailscale and `.htk` file names).
- `MVP-CHARTER-v0_2.md`: `grep -n` + `sed -n` → M7 `:54`, F7 `:102-105`, F9 `:114-126` (criterion `:121-124`, toast `:121`, post-MVP types `:125-126`), §5 `:224-252` (three-number `:227`, hotkey `:242`, host #10 `:248`), §6 `:269`, `:273`, §12 `:371-380`.
- `docs/30 - Design/LIVE-FEED-SPIKE.md` read whole (204 lines): scripts never committed `:11-16`, `:190-192`; lag definition `:33-36`; names `:8-9`; 10 s cadence 0 errors `:22-27`.
- `src/cobalt/cards/models.py`: `ALLOWED` `:92-110`, `MISSED` terminal `:109`, `MISSED_EDGE` `:136`, `Actor` `:76-85`. `cards/store.py`: `transition` `:248`, MISSED reason `:387-400`, `open_radar_cards` `:1017-1030`, `create_radar_card` `:1101`, `sheet_mode` column `:1124`. `cards/__init__.py:28-31` (the detector calls `store.transition`).
- `taxonomy/trade_def.py`: `ConfirmationPolicyType` `:192-196`, `ConfirmationPolicy` `:379-396`, `TriggerStep` `:632-640`, `SimpleTrigger` `:643-654`, `SequenceTrigger` `:657`. `taxonomy/store.py:91-101` (`get`). Policies in use: `intrabar` and `close_through` (Grep over `docs/30 - Design`, TRADE-DEFS-BATCH1/2).
- `replay/cards.py:14-16` (trigger = first bar at/after start with high ≥ entry), `:99-107` (WATCH/MISSED → `unarmed`).
- `radar/poller.py:48` (injectable fetch), `:98-100` (closed-bar filter); `radar/runner.py:461-472` (`run_command`, loop `:465`); `radar/config.py:192-215`; `radar/collector.py:42` (`TokenBucket`); `archiver/collector.py:78` (`resolve_token`), `:219` (`fetch_bars`).
- `tunables.yaml:666-710`: `radar.poll_interval` 100 `:684`, `radar.finviz_max_rpm` 50 `:702-709` (R17 2026-09-17).
- `aset/web.py`: `app` `:88`, `include_router` `:93`, manual TRIGGERED route `:1799`. `aset/radar_panel.py:1605-1606` (`setInterval`). There is no SSE and no `EventSource` (Grep over `src/cobalt/aset`). `aset/config.py:81-86` (bind), `:128-129` (local config first). `.gitignore:50` (`aset.local.yaml`). `git show HEAD:configs/dev/aset.local.yaml` → not in HEAD.
- `notify/mattermost.py:130` (`send_dm`). `configs/cobalt/notify.yaml` read at HEAD. `jobs.yaml`: aset `:39-91` (reads `:67-89`, tunables `:69`, imports `:90`), radar `:184-195` (imports `:194`), `no_resident_reads` notify `:319-325`, "refuses a path in both" `:71`, stale `web.py:90` comment `:83`.
- `jobs/restarts.py` read whole: `OPS_DESK_PREFIX` `:38`, `resident reads` `:207-210`, `static import reach` `:216-220`, `non-Python src asset` `:221-222`, registry `:223-224`, `DOCS` `:225-229`, ops/desk `:230-234`, tests `:245-246`, `UNCLASSIFIED CONFIG` `:257-259`.
- `BUILD-HUB.md:12`, `:14` (the allow line: no `uv run python`, no `cobalt strike`). `DEPLOY-HUB.md:92` (restart set within agent/aset/radar), `:94` (migration needs a resident down). `ops/desk/gate-lists.md:5-7`. `placement/check.py:80`. `cli.py:518`. Migrations listed: highest `0022`.
- RESTARTS classes in the cards come from `restarts.py` rules and `jobs.yaml`. `jobs restarts` itself is not on this seat's allow line, so each build proves the classes by running it (both cards, `## ROWS` RESTARTS line).

S4 CARDS DRAFTED · decisions: 14
