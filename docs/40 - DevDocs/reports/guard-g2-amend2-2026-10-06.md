# guard-g2 card amend 2 — 2026-10-06

## §0 Headline
- Card 21 amended: R2(ii) replaced by the brain's R517 text, byte for byte, with the flag written as `--prod`.
- Reds: (c) now uses `--prod`; (e) `; ls` and `| sh` refused; (f) two `--prod` words refused. (a), (b), (d) stay.
- R1, R2(i), header (`BASE: 3c257bb9`, `RULINGS: 2026-10-06 R511`) unchanged.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md`

## DECISIONS
- ASK DESK: the card's pipe and `;` controls moved from the controls list into red (e); the card asks the builder to state which rule (G2 or G1) returns each. Default taken: no rule pinned. [now]
- ASK DESK: new controls added beyond the brain's text: the query without `--prod`, `--prod=x`, `"SELECT '--prod'"`; each denied. Default taken: kept. [now]
- ASK DESK: a mutation added: drop the exactly-one-`--prod` test. Default taken: kept. [now]

## RECORDS
- BASE `3c257bb9`; `git diff --stat 3c257bb9 --` on `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`, `src/cobalt/db_query.py` printed nothing, so each read below is BASE.
- Read `bare-guard.py`: 18-21 (G2 entry is line 20); 100-109 (`PROD` at 106: `COBALT_ENV=production`, `--prod` as a whole word, `cobalt_brain`); 846-868 (`bash_rules`: `words(x)` at 848, G2 at 856-857).
- Read `src/cobalt/db_query.py`: 154-159 (157-158 `requires --prod`); 209-214 (211 `--side` choices, 212 `--prod`).
- Earlier reads of `desk-launch.sh` and the test files stand from `reports/guard-g2-amend-2026-10-06.md`; the rows R1 cites are unchanged.
- Edited only the card and this report. No git write, no launch, no database, no production command.

GUARD G2 CARD AMENDED 2 · card: 21 · decisions: 3
