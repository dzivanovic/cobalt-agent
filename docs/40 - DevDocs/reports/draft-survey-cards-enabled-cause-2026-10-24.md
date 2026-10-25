## §0 Headline
Wrote `prompts/2026-10-24/1038-survey-cards-enabled-cause.md` (Opus 5.5, read-only, one production read P1, one `RULINGS: 2026-10-08 R686` line).
New lead in it: `notes.py:711-720` tombstones every `radar.*` key, `radar.cards_enabled` included, whenever the mirror re-runs; the scope fix `283389ff` was reverted by `9c7593c0`. A tombstone object matches the `Input should be a valid boolean` error, and P1's `source` and `updated_at` will show whether it re-ran after 21:04:28.
The packet copy `prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml` is untracked (`git ls-files` empty); the prompt reads the ignored `data/backups/cards-htf-2026-09-20/` file instead.

## DECISIONS
- ASK DESK: the brain's FACTS say the mirror has not re-run; I did not adopt that and set the survey to settle it from P1's `source`. Default taken: the survey tests both leads. [22:50 ET]

## RECORDS
- Read: 1022 precedent, writing-rules.md, 1037 prompt, `reports/prodwrite-restore-cards-enabled.md:68-89`, `notes.py:686-749`, `card.py:20-340`, `store.py:54-56`, `radar_panel.py:586-610, 838-891, 949-975`, `web.py:903-915, 1817`, `runner.py:300-334` — all on the working tree, matching `main` for the cited lines.
- `git grep` / `git log` (settings, notes.py): commits listed; none touch `card.py` after 2026-09-25 (`807c13ec`).
- Not found: the `/radar` path that raises `CardSettingsError`; `radar_panel.py` builds `TraderSettings._build` (`:879`) and reads no `CardSettings`. The survey is told to trace it (Q3).
- `ls` of `data/backups/cards-htf-2026-09-20/`: `p2-live-settings-htf.yaml` present.
- `grep -c "^RULINGS:"` on the new prompt: 1. `session/guard.py` exists.
- Times from `date`: 22:49:09 ET, 22:50:18 ET.
- No production string run, nothing committed, nothing else changed.

DRAFTED · decisions: 1
