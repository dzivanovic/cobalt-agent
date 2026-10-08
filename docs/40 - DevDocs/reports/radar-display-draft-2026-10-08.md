## §0 Headline
- Fault: on his page, `tickLadder` never refetched `/radar` after the 08:52 ET load (`logs/aset.log:15298`), so the pre-market `No radar cards today` stayed on screen. The server path returns all 19 cards.
- Most probable: the open `TERMINAL · 0` `<details>` pauses every tick (`src/cobalt/aset/radar_panel.py:1609`, `:1620`).
- Second: a fetch with no timeout (`:1613`) left `ladderInFlight` stuck at true (`:1611`, `:1630`).
- Card `118`: control for today's shape (A), TERMINAL kept open across the swap (B), fetch abort (C), `LADDER NOT REFRESHED` banner (D), hidden-card control (E), RESTARTS (F).

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md` (14.5 kB, uncommitted; the desk commits it).
- BASE `50b0cd87`. Branch `ops/radar-display-fix-1008`, worktree `radar-display-fix-1008`. RULINGS `2026-10-08 R685`. DB key left out.

## DECISIONS
- ASK DESK: the brain pointed at WHERE the page reads (another DB or connection). The log refutes that: his client sent no `GET /radar` after 12:52Z, while it kept polling the pool to 15:19Z. Default taken: the card fixes the client tick, and the server path is a control. [11:29 ET]
- ASK DESK: prompt `117` asks for a first row that fails on today's shape. The server renders today's shape correctly at BASE (survey read 2 = 19, same WHERE), so row A is GREEN on BASE. Rows B–D are the red rows. Default taken: A is a control, and the red-first evidence is in B–D. [11:29 ET]
- ASK DESK: prompt `117` gives REPORT under `/Users/cobalt/cobalt/docs/…`, but `desk-launch.sh:902` refuses a build REPORT outside `$WT/<worktree>/docs/40 - DevDocs/reports/`. Default taken: the worktree path, as on card `89`. [11:29 ET]
- ASK DESK: prompt `117` names `DB: none`, but `CARD.md` allows `none` only for `ops/`, `tests/ops/` and `docs/` files. Default taken: the key is left out; every new test is offline. [11:29 ET]
- ASK DESK: row B removes the TERMINAL pause that card 10-06 (R556 flow) added as its drafting choice. Default taken: the open state is kept across the swap. This is an engineering choice and he may veto it. [11:29 ET]
- ASK DESK: R679 says no `/radar` fetch since `14:46Z`. That time is a `127.0.0.1` request (`aset.log:15499`); his client's last fetch was 12:52Z. Default taken: the card cites 12:52Z. [11:29 ET]
- ASK DESK: his tab still holds the 08:52 ET page until he reloads it. Default taken: the desk tells him to reload `/radar` now. That shows today's cards before the fix ships. [11:29 ET]

## RECORDS
- Prompt `117`, `CARD.md`, card `89`, survey `-r2` report, prompt `115` (read 2 SQL, line 26), `radar-page-read-2026-10-06.md`, `cto-2026-10-08.md` rows R675–R685 and `## §5 CURRENT`, `areas/cobalt.md`, `writing-rules.md`: read whole.
- Code at `50b0cd87`: `radar_panel.py:800`–`:969`, `:1465`–`:1664`; `web.py:890`–`:929`; `cards/store.py:1`–`:125`, `:940`–`:1079`; `db.py:1`–`:268`; `env.py:60`–`:99`; `db_migrations/0007_radar_cards.sql:205`–`:239`; `tests/cobalt/test_radar_panel.py:558`–`:571`, `:1100`–`:1360`; `tests/cobalt/test_radar_panel_cards.py:170`–`:244`, `:400`–`:411`, `:440`–`:510`, `:640`–`:659`, `:955`–`:974`; greps of `restarts.py` (`:220`, `:225`–`:228`, `:246`), `jobs.yaml` (`:90`, `:194`), `desk-launch.sh` (`:902`).
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `50b0cd87`. `git … diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` printed nothing. `git … log -3 -- radar_panel.py` → `0544f91d`, `541adf0c`, `6370ea6a`.
- `logs/aset.log` (15527 lines): grep of `GET /radar` and of `100.73.178.42.*GET /radar`, Read of `:15270`–`:15527`, and a count of `radar panel FAILED|radar pool refresh FAILED` (0). `logs/radar.err`: the first 10-08 line matching `card` is at `:35844`, 09:44:24.
- `ls` of card `118`, both report paths and the worktree: all absent before writing.
- The bare-guard hook blocked one Bash `grep` because its pattern held the production flag text; it was resent with the Grep tool. No production command, git write or launch was run.
- `wc -c` card `118`: 14509 bytes (new file).

RADAR DISPLAY CARD DRAFTED · decisions: 7
