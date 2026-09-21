# Stale marker — design proposal report (2026-09-21)

Seat: proposer `stale-marker-design-0921` · Opus 5 · read-only · started 16:08 ET, done 16:12 ET (`date`).
Proposal: `docs/30 - Design/STALE-MARKER-PROPOSAL-2026-09-21.md` (81 lines).

## §0 Headline
- Row mark and card mark both render the per-ticker state that already exists: `radar_pool.poll_failures`, which the `BARS POLL FAILED` banner already names. No new route, stored column or card field. `/api/radar/pool` JSON stays byte-identical.
- The L52 word for the card mark is **RENDERING**.
- Correction to the premise: a pool row shows no `last` at all (`radar_panel.py:822-833`). The row mark goes in the ticker cell.
- Separate finding: an open card is refreshed on stale bars, and a fully tapped card can SCORE on a stale `last` → ESCALATE 1.
- 2 chunks · evenings to live 1 (2 if the card side goes to a tribunal) · ESCALATE: 2

## Fact table (condensed; full table with every row = proposal §1)

| Claim | file:line | |
|---|---|---|
| Per-ticker staleness = `radar_pool.poll_failures` `{ticker, reason, since}` | `radar/store.py:185,194,201` | PROVEN |
| Reasons: `error` (any session), `stale` (> `radar.poll_bar_max_age_s`=180, RTH only, his 09-14 ruling) | `radar/poller.py:93,113,121-122`; `tunables.yaml:513-520` | PROVEN |
| Lives one S4 cycle; cleared on a good fetch or fresh bar; dropped when the ticker is no longer polled; S2 carries it forward | `poller.py:66-81,116,124`; `store.py:268-273`; `runner.py:356-385` | PROVEN |
| Polled = admitted members + departed tickers with an open card | `runner.py:238-267` | PROVEN |
| Panel already reads it (`PoolRecord.poll_failures`); the page renders it only when `poll_only`, and every other stage fails the page | `radar_panel.py:93,477-484,589-594` | PROVEN |
| Not carried out of `build_pool_view`: no field on `PoolView`/`PoolRow` | `radar_panel.py:148-192` | PROVEN |
| Pool row has no `last` cell | `radar_panel.py:822-833` | PROVEN |
| Card `last` shown at ARMED block + LEVELS; comes from `radar_cards_v.last_price` | `radar_panel.py:748,967,997`; `evaluate.py:803` | PROVEN |
| `build_radar_panel` holds both views → the card side can reach the set with no new query | `radar_panel.py:787-800,1134-1137` | PROVEN |
| `refreshPool` swaps the pool fragment only; the ladder is re-fetched only after a POST | `radar_panel.py:1077-1093,1114-1129` | PROVEN |
| No write path in `radar_panel.py` (L29) | `radar_panel.py:3-9` | PROVEN |
| Card does NOT form on stale bars (`input_stale`, 2×scan_interval=200 s) | `evaluate.py:529-534,598-599` | PROVEN |
| Open card IS refreshed on stale bars; tapped dots are exempt from suppression → it can score | `evaluate.py:1329-1349,776-777`; `scoring.py:247-267`; `cards/radar.py:177` | PROVEN path · production occurrence UNPROVEN |

## L52 finding: RENDERING
Evidence: the stamp's only input is the ticker set of `poll_failures` (F1). The panel already reads it (`radar_panel.py:93,472`) and already renders it in the banner (`:589-594`). `render_radar_page` passes that set to `render_ladder` from the `PoolView` it already holds (`:787-800,1137`). The build adds no field to `CardView`/`RadarCardRow`/`radar_cards_v`, no route and no column. Nothing is scored, reordered or re-queried. What changes on a card: an added `STALE` stamp in the strip (`:1030`), beside ARMED `last` (`:967`) and beside LEVELS `last` (`:997`), and nothing else.

## READING:
- `Vault/Think/6 - Permanent/Memory/LAWS.md` (full, L1–L74)
- `src/cobalt/aset/radar_panel.py` (full), `src/cobalt/radar/store.py:210-285`, `radar/runner.py:236-388`, `radar/poller.py:20-129`, `radar/evaluate.py:36-55,495-634,755-805,1300-1400`, `cards/scoring.py:240-337` + greps, `cards/radar.py` grep
- `configs/cobalt/taxonomy/tunables.yaml:467-470,500-522`
- `tests/cobalt/test_radar_panel.py` (test index only)
- `reports/page-bars-hotfix-check-2026-09-21.md` (ESCALATE, Q2 rows); `reports/cto-2026-09-21.md` R10, R11, R21, R36 + §log lines 260, 264, 266, 333
- `git log main..s2/degraded-line-0921`; `git show 88602cc -- radar_panel.py`
- NOT read: `reports/degraded-line-rebase-2026-09-21.md` (not on main; it sits on the branch as `dc24d72`, commit subject read only); `test_radar_panel_cards.py`; DevDoc `radar_panel.md`; `page-bars-hotfix-build` report (the check report quotes it). Not needed for any claim above.

## ESCALATE
1. **An open card is refreshed and can score on stale bars (his; L52 scoring, NOT part of the stamp).** `refresh_card` runs for every open card with no evaluation-state guard (`evaluate.py:1329-1349`). It takes proximity from `ev.last_price`, the last stored bar, however old (`:776-777`), and writes that price as the card's `last` (`:803`). Stale computed dots suppress `card_score` only when untapped (`scoring.py:248`). A card with every computed dot tapped therefore gets a live `card_score` from a stale price, and WATCH cards are ordered by that score (`cards/radar.py:27,177`). The code path is PROVEN. Whether it has happened in production is UNPROVEN (L70). Same item the desk logged as page-bars drafter ESCALATE 2 (`cto-2026-09-21.md:260`).
2. **"Stale" has three clocks (his, L53).** The poller uses 180 s, RTH only, plus `error`. The evaluator uses 2 × scan_interval = 200 s in every session. The pool banner uses 2 × interval since the last scan (`poller.py:121`, `evaluate.py:532`, `radar_panel.py:582`). The stamp can honestly render only the poller's clock, which the banner names. So a card the evaluator holds `input_stale` outside RTH may carry no stamp. No value is proposed here. Should the stamp cover more? That is proposal Q1.

## CONTINUE
Done. The desk's next steps: L35 on the two files; lane call for chunk 2; any build branches off main after tonight's `16` deploy.

## DIGEST FOR THE DESK
- **Row mark:** a small red `STALE` badge inside the ticker cell of each `current` pool row whose ticker is in `radar_pool.poll_failures`. The tooltip reads `<reason> since HH:MM ET`. Wording, 9 px mono and red `.badge` geometry are ASSUMED. The pool row has NO `last` cell today (`radar_panel.py:822-833`), so the row mark sits by the ticker, not by a price.
- **Card mark:** the same badge in the card strip after the ticker, beside ARMED `last` and beside LEVELS `last`. It is keyed by ticker, so a lifecycle-polled card outside the pool is marked too.
- **Hook:** `build_pool_view` derives `bars_stale_tickers` from `poll_failures`, only in the `poll_only` case. It is an in-memory `PoolView` field with `exclude=True`, so the API JSON is unchanged. `render_pool` uses it for rows. `render_radar_page` passes it to `render_ladder` for cards. The pool section carries `data-bars-stale` only when the set is non-empty.
- **Refresh:** rows follow automatically, because `refreshPool` swaps the fragment. For cards, a `mirrorStale()` sits beside tonight's `mirrorDegraded()` and toggles the strip badge in place. There is no re-sort, no re-fetch and no open/close change, so the ladder never moves (his 06:32 complaint). The two in-card `last` badges follow on reload or a card action (Q2).
- **L52 word: RENDERING.** It is a second rendering of the stored state the banner already shows. It adds no card field, route or column, computes nothing, scores nothing and reorders nothing (L3 holds).
- **L29:** no write path. `radar_panel.py` is read-only. Today's hotfix used Sonnet 5 on the same builder.
- **Chunks: 2.** (1) row mark plus the derived set. (2) card mark plus `mirrorStale`. Both are in `radar_panel.py`, its two test files and its DevDoc. They touch the same lines as `s2/degraded-line-0921`, so the build branches off main AFTER tonight's `16`.
- **RESTARTS:** `com.cobalt.aset`. This is a GUESS from today's hotfix precedent until `cobalt jobs restarts` is run.
- **Evenings to live: 1** (Tue 09-22) if chunk 2 goes straight to build and ≥3 checkers. **2** if chunk 2 takes a tribunal first.
- **His:** ESCALATE 1: an open card is refreshed and can SCORE on a stale `last` when its dots are tapped (`evaluate.py:1329-1349,776`; `scoring.py:248`). That is a scoring item. ESCALATE 2: "stale" has three clocks, and the stamp follows the poller's 180 s RTH clock only.
- **Checker questions (proposal §7):** departed rows · terminal rows · JS ticker key · exclude=True vs a JSON key.

STALE MARKER PROPOSED · row mark: red STALE badge in ticker cell · card mark: RENDERING · new route or stored field: no · card can score on stale bars: yes · chunks: 2 · evenings to live: 1 · ESCALATE: 2
