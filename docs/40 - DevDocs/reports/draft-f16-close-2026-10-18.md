# Draft — S5 F16 close card `f16-close-1018` (prompt 789)

## §0 Headline
- Card: `docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md`, BASE `e7ef198a`, BAND MID, 3 rows; uncommitted.
- S5 thresholds on main are already tunables rows with consumers (`prefill.refresh_window`, `prefill.refresh_interval_min`); no S5 literal stays inline in a predicate.
- Rows: V1 `cobalt validate` builds `playbook.yaml` (F23); V2 builds `daily_refresh` (F4); C1 `load_tunables` refuses a row with no consumer. Each RED on BASE (`DID NOT RAISE`).
- Rows touch `src/cobalt/cli.py` and `src/cobalt/taxonomy/loader.py`, so this is more than a tests-and-config change: residents restart, BAND MID.
- F5, F20, F21 are not on main; F16 close stays open for their sweep.

## DECISIONS
- ASK DESK: the card is a `src/` change (two files, one read by residents), not tests-and-config; take V1, V2, C1 as written? Default: take them, BAND MID, `DB` key left out, RESTARTS from the builder's `cobalt jobs restarts` line. [19:01]
- ASK DESK: F5 (card 731), F20 (card 730), F21 (cards 468, 469) are not on main at BASE. Close F16 now on main as it stands? Default: this card closes F16 for BASE; the ladder marks F16 BUILT, not DONE; a repeat sweep (the same greps, plus a validate line for each new family) is owed after the last of those three deploys. [19:01]
- ASK DESK: OFF-LADDER harness literals (`src/cobalt/classify/route.py:80` `MIN_N = 30`, `:389` band cutoffs 2/6; `ops/desk/checkin-timer.sh:54` `PING_MAX_AGE_MIN=30`; `ops/desk/stop-guard.py:532` 160) are outside F16. Default: outside (Charter `:177` scopes F16 to thresholds the MVP evaluates; `MIN_N` is L8's n, as `src/cobalt/replay/line.py:62`); recorded in the card's `## RECORDS`, no row. [19:01]

## RECORDS
- 18:52 EDT `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `e7ef198a`.
- Read: prompt 789; `prompts/CARD.md`; card 787; `docs/00 - Project/SPRINT-LADDER-v0_1.md:30-200`, `:1100-1175`; `docs/00 - Project/MVP-CHARTER-v0_2.md:175-182`; LAWS L8, L10, L69; `topics/writing-rules.md`.
- `git log --merges -40 main`; `git diff --stat` of each S5 merge's build (`db62c4b5`, `6b205122`, `862e3b1d`, `c95e7241`, `5a52b4f7`, `d12b0e1a`); `git log --since=2026-10-14 main -- src configs`.
- Full diffs read: F4 (tunables, prefill, jobs, `prefill/daily.py`, `prefill/config.py`), F23 (`src/cobalt/playbook/*`, `configs/cobalt/playbook.yaml`, jobs), JEV keyed, stop-guard; `ops/desk/checkin-timer.sh:40-60`.
- Greps on main: numeric literals in `src/cobalt/classify/`; `MIN_N`/`n < 30` in `src/cobalt`; `tunables.yaml` `- key:` 94, `consumers:` 94, none empty; `TunableRow(` and `load_tunables(` callers in `src/` and `tests/`; `_cmd_validate` (`src/cobalt/cli.py:137-500`) has no playbook or daily_refresh load.
- 19:01 EDT `date`: card and report written; nothing committed.

DRAFTED · decisions: 3
