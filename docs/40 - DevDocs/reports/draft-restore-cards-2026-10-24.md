## §0 Headline
Two K3 prodwrite cards drafted: `prompts/2026-10-23/1029-restore-cards-enabled-card.md` (htf card, `radar.cards_enabled`) and `1030-restore-radar-benchmark-card.md` (optional file, `radar.benchmark`); one row each, apply only.
WRITE RULING is `2026-10-24 R2412` (HIS RULING · APPROVED, committed in HEAD), supplied by the desk during the run. BASE `1ef351db` (`main`), no code past it.
Not yet proved by a launcher run: the cards are uncommitted, as the prompt says.

## DECISIONS
1. No `--dry-run` in either card: the hub has no dry-run step and its guard passes only the card's command (`PRODWRITE-HUB.md:3,12,43`). The dry run is met by the hub's `count read` BEFORE (expect 0), the one `--apply` (which refuses a file whose sha256 differs, `src/cobalt/settings/cli.py:171-172`), and the `count read` AFTER (expect 1).
2. `TAG:` is left empty: `desk-launch.sh:2305` refuses a prodwrite card with a TAG (it marks a deploy card). The prompt listed TAG; the launcher wins.
3. `RULINGS: none`: no further ruling binds the writes beyond WRITE RULING. If the desk wants R2412 there too, it is one line. (Unproved against the launcher's `ruling_rows`; deploy cards use `none`, `CARD.md:24`.)
4. The count read names the table as a string literal `'user.trader_settings'` in the select list: the launcher requires the whole name in the read (`desk-launch.sh:2437-2446`) and `"user".trader_settings` does not contain it. `--side user` pins `search_path` to `"user"` (`src/cobalt/db.py:18,217`), so the FROM is `trader_settings`. Count reads match the source label (`card.py:324`; `settings/cli.py:218`).
5. `expected rows` = 1 each (the key's row with its new source). `inverse` none: no cobalt command restores the tombstone; the backup path is the rollback.
6. No committed prodwrite card exists as precedent (`grep -l "^CLASS: K3"` finds only build cards 392, 417, 448); the shape follows `CARD.md:155-161` and `desk-launch.sh:2301-2474`.
7. R2407's text said "only after 1020 DEPLOYED"; R2410 lifted it, so the cards carry no such gate. Order: 1029 then 1030, one seat at a time.
8. BASE moved from `148b03ef` to `1ef351db` during the run; `git diff --stat 148b03ef 1ef351db -- . ':(exclude)docs'` printed nothing.

## RECORDS
Times from `date`.
- 19:54:14 ET: read `PRODWRITE-HUB.md` (whole), `CARD.md` (whole), `ops/desk/desk-launch.sh:165-194, 455-485, 2295-2474`, `reports/survey-restore-prep-2026-10-23.md` (whole).
- `git rev-parse --short=8 main` → `148b03ef`, later `1ef351db`.
- `grep -rl "^WRITE RULING:" prompts` → nothing; Grep `WRITE RULING` → only hubs, `CARD.md`, 392/417 build cards, the 1028 prompt.
- `ls reports/prodwrite-restore-cards-enabled.md`, `…-restore-radar-benchmark.md` → both absent (19:55 ET).
- `grep -n "optional:" src/cobalt/settings/cli.py` → `:218`; `grep -n "card:" src/cobalt/settings/card.py` → `:324`; `guard.py` lines 1, 7, 67 mention market_reset / 20:00-21:00. The write is refused 20:00–21:00 ET; stated in both cards' RECORDS.
- Desk message (cross-session, from cto-desk, 19:55 ET): R2412 exists. Checked: `grep -n "^| R2412 |"` on `reports/cto-2026-10-24.md` → line 7, HIS RULING · APPROVED; `git show HEAD:…cto-2026-10-24.md` holds the same row. Both cards edited to `WRITE RULING: 2026-10-24 R2412`.
- 19:55:38 ET: BASE re-proved as above.
- Files written: the two cards and this report. Nothing committed, nothing run on production.

DRAFTED · decisions: 8
