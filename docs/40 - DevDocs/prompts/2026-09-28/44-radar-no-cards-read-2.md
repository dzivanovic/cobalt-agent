MODEL: Sonnet 5 (`claude-sonnet-5`) · SEAT: read-only helper `radar-no-cards-2-0928`, launched by the CTO desk in the background · SESSION: fresh · auto mode (read-only, L62) · METER: Anthropic small · LADDER: `OFF-LADDER — cto-2026-09-28.md R92, R99, R102` · nobody sits at this terminal: the report is your channel; `ASK DESK: <question> [<time from date>]` under `## ESCALATE`, take the safe default, continue.

Launch (the desk's): `cd /Users/cobalt/cobalt-wt/ops-day-open`, then `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/44-radar-no-cards-read-2.md' and follow it exactly." --model claude-sonnet-5 --permission-mode auto --remote-control radar-no-cards-2-0928 --name radar-no-cards-2-0928 --allowedTools "Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(head *)" "Bash(wc *)" "Bash(date*)" "Bash(git -C /Users/cobalt/cobalt log*)" "Bash(git -C /Users/cobalt/cobalt show*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/Vault`

# WHY DID 2,107 FORMED RADAR SCORES MAKE NO CARD ON MON 2026-09-28?

AUTHORIZATION: written by the CTO desk on Dejan's "A" (R102). Verify: `grep -n "^| R102 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-28.md"` prints a row naming `44-radar-no-cards-read-2.md`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"44-radar-no-cards-read-2.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` NON-EMPTY. Else last line `FAILED: authorization mismatch`, stop.

RULES: reads only. One bare command per Bash call, exactly a listed prefix; no pipe, no redirect, no `cd …&&`; grep patterns are plain fixed strings (`grep -n -F`), one per call; or the Read tool. Never run `uv`, `cobalt`, `psql`, `docker`, `launchctl`, any database query, any `COBALT_ENV=production` command; never edit code, config or the vault. Never read `.env` or print a secret (L4, L41). Write only your report, with the Write tool. L32: no ticker, value or real file name of his in the report beyond what the cause needs. A query you need → write it verbatim under `## ESCALATE` as `ASK DESK`, take the reading the code gives, continue.

FACTS — round 1 (`reports/radar-no-cards-2026-09-28.md`, read it whole first) left two readings: (A) nothing formed, (B) `radar.cards_enabled` false. The desk's DB reads at 16:3x ET rule out both:
- `"user".trader_settings` `radar.cards_enabled` = True; `system.radar_score_run.cards_enabled` = True on run 1826.
- Today (ET): premarket 112 runs, 0 formed · rth 128 runs (09:30–15:59), 2,107 `radar_score` rows `evaluation = formed` · aftermarket 12 runs, 217 formed. Run 1826 (16:27, aftermarket, `complete`, evaluator `s2p2.3`): formed 13, `suppressed_reason` empty on all 13.
- `"user".radar_cards_v` holds 62 rows in all; `/radar` shows "No radar cards today" (`src/cobalt/aset/radar_panel.py:773`); `logs/radar.err` shows no card line and no error today.
- LIVE = `deploy-2026-09-27` `3349466f`.

STEPS — `date` first; write the report after each step:
1. Trace at `main` the code from a `formed` `radar_score` row to a card row and to `radar_cards_v` (`src/cobalt/radar/evaluate.py` from `:1882`, `propose.py`, `seam.py`, `store.py`, `runner.py`; the view's migration SQL): every condition between `formed` and a card, each `file:line`.
2. For each condition, what today's facts above make of it: HOLDS / FAILS / NOT CHECKABLE FROM READS — the exact SQL that settles it (as `ASK DESK`).
3. What changed: `git -C /Users/cobalt/cobalt log --oneline -20 -- src/cobalt/radar src/cobalt/aset/radar_panel.py src/cobalt/db_migrations` and the diffs of any commit in `deploy-2026-09-27` touching that path; the last day `radar_cards_v` shows a card is a desk query — name it as `ASK DESK`.
4. State the cause in one sentence, or the readings still open with the one query that splits them. Name the fix owner's step, never build it.

REPORT: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-no-cards-2-2026-09-28.md` — `## §0 Headline` (≤5 lines: the cause or the open readings; intended or defect) → `## Path` → `## Today` → `## What changed` → `## ESCALATE` → last line. Per `topics/writing-rules.md` (`/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`). While you run, the last non-blank line is `(run in progress)`.
STOP LINE (L71): `RADAR NO-CARDS READ 2 DONE · cause: <one line|OPEN — <n> readings> · intended: <yes|no|unknown> · ESCALATE: <n>` — or `FAILED: <step> — <reason>`. Then stop.
