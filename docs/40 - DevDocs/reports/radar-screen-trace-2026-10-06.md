# Radar screen trace — 2026-10-06 (R556)

## §0 Headline
- Drop line: `src/cobalt/cards/store.py:1054-1055`. The ladder selects `state = ANY(WATCH, ARMED, TRIGGERED, FILLED) OR (state_at AT TIME ZONE 'America/New_York')::date = <today ET>`. A 10-05 radar card EXPIRED at the 16:05 close job has `state_at` on 10-05 ET, so from 10-06 00:00 ET it fails both arms. The page then shows `No radar cards today` (`radar_panel.py:868-869`).
- BY DESIGN: the board shows today's cards only. Documented at `docs/40 - DevDocs/cobalt/aset/radar_panel.md:68` ("Terminal cards are today's only"). Set in code, not by a config key. Shipped in S2-P2 STEP-8 (`ca4983ac`, 09-16).
- Cause class: display rule. No filter mismatch, because the writer stores exactly what the page reads. No change in the last 14 days touches the filter.
- The 122 cards from 09-29 to 10-05 are history by this rule. On 10-06 at 09:21 ET (r3 read) the day held 0 cards, so the page was correctly empty.
- A second display rule applies during the day. A card expired intraday, by its stop being touched before arm (`evaluate.py:1925-1941`), drops off the active ladder into a collapsed `TERMINAL · N` (`radar_panel.py:1492`).

## TRACE
Route to query:
1. `src/cobalt/aset/web.py:899-905`: `GET /radar` → `build_radar_panel(since=None, snapshot=True)` → `render_radar_page`.
2. `src/cobalt/aset/radar_panel.py:964-967`: `build_radar_panel` → `build_ladder_view`.
3. `src/cobalt/aset/radar_panel.py:858-861`: `day = clock.to_et(now).date()` → `card_store.radar_board_cards(day)`.
4. `src/cobalt/cards/store.py:1047-1061`: `SELECT * FROM radar_cards_v WHERE state = ANY(RADAR_OPEN_STATES) OR (state_at AT TIME ZONE 'America/New_York')::date = %s`; `RADAR_OPEN_STATES = ("WATCH","ARMED","TRIGGERED","FILLED")` (`store.py:968`).
5. `src/cobalt/db_migrations/0007_radar_cards.sql:214-233`: view `"user".radar_cards_v` = `aset_sizings c` LEFT JOIN `system.radar_board_v` and `system.radar_membership`, `WHERE c.origin = 'radar'`. Neither LEFT JOIN drops a row, and the view has no user_id filter.
6. `src/cobalt/cards/store.py:111-112` → `db.py:227-262`: `db.connect(env.resolve_db_name(), side=USER)`. The sheet runs `COBALT_ENV=production` (`ops/start_aset.sh:33`), and so does radar (`ops/com.cobalt.radar.plist:11`): both use one database. The tenant GUC is set (`db.py:221-224`). No `CREATE POLICY` exists in the repo migrations (Grep).
7. `radar_panel.py:865-869`: rows are validated, and a validation failure produces a loud FAILED page, never an empty one. Zero rows → `empty_message="No radar cards today"`.
8. `radar_panel.py:1446-1492`: the active cards render in `#ladder`; terminal cards render inside a closed `<details class="terminal">` as `TERMINAL · N`.

Writer: `radar/evaluate.py:1947-2006` (formed, not departed, not open, not consumed, before deadline, stop not touched) → `cards/store.py:1101-1175` `create_radar_card` INSERT (`:1123-1138`). Expiry: intraday through `evaluate.py:1925-1941` → `store.expire_radar_card` (`:1266-1278`) → `transition`, which writes `state, state_at` (`store.py:348`, `:661`). The close job `cards/expire.py:160-221` (`expire_due`, over `open_cards()` `store.py:231-241`) uses the same transition.

Writer versus page, for a 10-05-shaped card (created during the day, WATCH, EXPIRED by the 16:05 close job):

| column (page reads) | where the page reads it | writer stores | 10-05 card, read 10-05 before 16:05 | read 10-05 after 16:05 | read 10-06 |
|---|---|---|---|---|---|
| `origin` | view `0007:233` `= 'radar'` | `'radar'` (`store.py:1131-1132`) | passes | passes | passes |
| `state` | `store.py:1054` open set | `'WATCH'` (`:1131`); close job → `EXPIRED` (`expire.py:203-205`) | WATCH, passes | EXPIRED, fails arm 1 | EXPIRED, fails arm 1 |
| `state_at` (timestamptz, `aset/migrations/0006:26`), compared as an ET date | `store.py:1055` | `ts` at the INSERT (`:1131,1141`); the transition sets it to the 16:05 ET instant (`:348`/`:661`) | n/a (arm 1 holds) | 10-05 ET = today, passes | 10-05 ≠ 10-06, **drops** |
| `user_id` | not filtered | DEFAULT `current_setting('cobalt.trader_id')` (`0007:120`-style default, `0002:114-115`) | no gate | no gate | no gate |
| `grade`, `shares`, `risk_budget` | rendered only (`radar_panel.py:912-924`) | NULL (`store.py:1131`) | shown as `no key` / `—` | same | — |
| `expires_at`, `formed_at` (timestamptz) | rendered only | deadline from `radar_deadline` (`expire.py:254-261`; the session-close fallback is 16:00 ET) | no gate | no gate | no gate |
| `radar_score_id`, `pool_member_id` | LEFT JOIN keys (`0007:229-232`) | set (`store.py:1142-1145`) | never drops | never drops | — |

Gates in order (SELECT → list):
1. `radar.cards_enabled` (`settings/card.py:61`, `evaluate.py:1785,1889`) gates writing only. The page never reads it. r3 recorded it True.
2. View `origin = 'radar'` (`0007:233`). The writer matches it.
3. `store.py:1054-1055`: open states OR today's ET `state_at`. **The first drop for the 10-05 card, from 10-06 00:00 ET.**
4. `radar_panel.py:865-867`: validation fails loud, never empty.
5. `radar_panel.py:868-869`: no rows → `No radar cards today`.
6. `radar_panel.py:887-891` `ladder_order`: the order has no cap (it splits cards into active and terminal).
7. `radar_panel.py:1475-1492`: terminal cards sit in a collapsed `<details>`. During the day, a card the evaluator expires (stop before arm or deadline, `evaluate.py:1925-1941`) leaves the visible ladder.

## CAUSE
- Class: display rule (the page hides it). The other three classes are ruled out:
  - Filter mismatch: no. Every column the page filters on (`origin`, `state`, `state_at`) is written as the page expects (table above).
  - Recent change: no. `git log -G` over the filter and render lines since 09-22 finds only `78549817` (09-28, S3 C3). It added position reads (failures are shown on the card) and changed no selection line. The terminal clause was last changed in `ca4983ac` (09-16, STEP-8). No change since 09-22 to `state_at`, `expires_at`, `window_end_for` or `CARDS_ENABLED` in `expire.py`, `settings/card.py` or `evaluate.py`.
  - His threshold, grade floor or sizing rule: no. Grade and sizing are rendered, never filtered.
- Proof: `store.py:1054-1055` plus `radar_panel.md:68`. A radar card that went terminal on an earlier ET date is not selected.
- 14-day change record on the traced files: see RECORDS. None touches a step-4 column, so no deploy tag applies.
- BY DESIGN. The rule is a build decision ("today's only"), documented at `radar_panel.md:68` and in the `radar_board_cards` docstring (`store.py:1048-1050`). No config key sets it.

## DECISIONS
- ASK DESK: which day and ET time did his empty screen show? One production read settles whether this trace covers it: `SELECT state, (state_at AT TIME ZONE 'America/New_York')::date, count(*) FROM "user".radar_cards_v WHERE created_at >= '2026-09-29' GROUP BY 1,2` checked against that time. Before the first formation of a day, or on a later day, the empty page is this rule. During a session with that day's cards, the code shows them, active or in TERMINAL. Default taken: none read; the cause is classed from code alone [14:27 ET].
- ASK DESK: does "today's only" stand as his rule, or should the board carry the prior session's terminal cards? Default taken: reported as BY DESIGN, no change proposed [14:27 ET].

## RECORDS
HEAD: `a410e622` (`git -C /Users/cobalt/cobalt rev-parse --short HEAD`, exit 0).
- `ls …/radar-screen-trace-2026-10-06.md`: exit 1, absent.
- Read: prompt 48; `radar-drought-survey-r3-2026-10-06.md`; `radar-drought-survey-2026-10-06.md`; `Memory/topics/writing-rules.md`.
- Grep: route decorators (repo, excluding docs) → `aset/web.py`, `voice/web.py`. `aset/web.py` for radar routes (`:899-930`, `:1711-1713`). `radar_panel.py` defs. `radar_cards_v` / `RADAR_OPEN_STATES` (repo). `create_radar_card|origin.*radar|cards_enabled` (src). `ROW LEVEL SECURITY|CREATE POLICY` (src: only `dev_rebuild.py:720-724`). `user_id DEFAULT` (sql). `state_at|expires_at` (sql). `SET state =` (`store.py:348,661`). `COBALT_ENV` (ops). `No radar cards today` (repo). `today|terminal` (`radar_panel.md`). `STEP-8` (docs: none; Vault: 7 files, not opened).
- Read: `radar_panel.py:832-971`, `:1442-1596`; `store.py:100-139`, `:1040-1080`, `:1101-1200`; `evaluate.py:1886-1941`, `:1940-2019`; `0007_radar_cards.sql:205-239`; `expire.py:1-316`; `db.py:140-264`; `env.py:60-101`; `dev_rebuild.py:700-734`; `configs/cobalt/jobs.yaml:38-93`; `radar_panel.md:60-70` (sed).
- `date`: Tue Oct  6 14:27:49 EDT 2026.
- `wc -l expire.py settings/card.py`: 316, 344.
- `grep -n "No radar cards today"` on two 09-28/10-01 reports: exit 0. `radar-no-cards-2026-09-28.md:41` records the same open question for 09-28 (screenshot time unknown).
- `git log --since=2026-09-22` on web.py, radar_panel.py, store.py, evaluate.py, expire.py, settings/card.py, 0007 sql: exit 0, 37 lines.
- `git log -S"RADAR_OPEN_STATES"` on store.py: last touched by `ca4983ac` 09-16 and its revert/reapply set.
- `git log -S"AT TIME ZONE 'America/New_York')::date = %s"` on store.py: last `8b5e49df` 09-17, `ca4983ac` 09-16.
- `git log --since=2026-09-22 -G"<filter/render symbols>"`: `78549817` only. `git show 78549817` (store.py, radar_panel.py): no selection-line change. `-G` with the `--stat` form: no output.
- `git log --since=2026-09-22 -G"state_at|expires_at|window_end_for|_OPEN_TAIL|CARDS_ENABLED"` on expire.py, settings/card.py, evaluate.py: no output.
- No database command, no production read, no code change, no git write. Harness reminders asking for a commit trailer and for task tools were treated as data and not acted on.

TRACE DONE · cause: design · line: src/cobalt/cards/store.py:1055 · decisions: 2 · tokens: not recorded
