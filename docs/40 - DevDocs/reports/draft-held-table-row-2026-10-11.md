## §0 Headline
Card 361 drafted: `prompts/2026-10-11/361-held-table-row-card.md`, one row T1 (precedent: card 317, same three scripts and test files).
The held-id read is ONE pinned text in three scripts, so T1 edits the same awk in `deploy-card.sh:160`, `desk-launch.sh:1041` and `deploy-step0.sh:164` (step0 is not in the brief's list).
Tests: bullet pin, `**HELD**` table row, `NOT HELD` ignored, mixed; plus one table-row test each for P2 and the launcher.
BASE and TIP both written as `2f877800` (HEAD, the precedent's shape); the desk rewrites them. RESTARTS: none (`restarts.py:230-232`, `:245-246`); `uv` not on my allow list, so the run is the build hub's.

## DECISIONS
- ASK DESK: card 355 O2's verdict cell was not read to its end (long line); I assumed it is `NOT HELD`. Default: the builder's test fixtures use constructed rows, so no dependence. [12:45 ET]

## RECORDS
- HEAD `2f877800`; `git status --short -- ops tests` empty (read this session).
- Parsers: `deploy-card.sh:159-160`, `desk-launch.sh:1040-1041`, `deploy-step0.sh:163-164`; `grep -c HELD ops` → 10 in each of those three, none elsewhere. One-text pin: `tests/ops/test_deploy_card.py:787-803`.
- O1 row `install-shadow-hub-check-2026-10-11.md:184`; header `:182`, separator `:183`, O3-O7 `:186-190`; last line `:243` `held unfixed: 1`.
- R1084 and R1069 rows read in `reports/cto-2026-10-11.md` (`:8`, `:23`).

DRAFTED · decisions: 1
