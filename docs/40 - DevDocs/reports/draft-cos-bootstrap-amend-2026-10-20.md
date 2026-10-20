# Amend: cos bootstrap card 929 — 2026-10-20

## §0 Headline
- Card 929 amended in place for the brain's rulings 4, 8, 9 and the `WAITS:` line.
- Items 1, 5, 6, 7 already stood as ruled; changed nothing there.
- Beyond the brief: smoke read 5 relabelled `cos turn failures`, X2 reworded (both said the smoke proves LaunchAgent auth); the brain's FOR THE CHECK line added as X6.
- Not launched, nothing committed.

## DECISIONS

## RECORDS
- `date` → `Tue Oct 20 17:43:42 EDT 2026` (start); report written after.
- Read: card 929 (whole), `reports/cos-bootstrap-decisions-2026-10-20.md` (whole), `reports/draft-cos-bootstrap-2026-10-20.md` (whole), `topics/writing-rules.md` (whole), prompt 934 (whole).
- Proved at `main` (`git show main:src/cobalt/cos/run.py`, `git grep -n`): `run.py:105` `turns.ensure_schema()`, `:109` `hitl.ensure_schema()`, `:150` `store.register(spec)`, `:155` `store.mark_running`. Only these lines are new on the card.
- Item 1 (no overlap), 5 (`enabled: true` is the tunables card's), 6 (`--owed-clear` after green smoke (s)), 7 (`«FILL: his …»`): card already says so (NOT IN THIS JOB, PREREQUISITE, ORDER, GATE RESULTS).
- Edits: `WAITS:` line under the header; X18 line `median 28.5 s; the max, 641 s, was F5's migration deploy (0029, card 909)`; smoke read 5 and X2 per item 4; `MIGRATIONS:` line in `## RECORDS`; X6 added.

DRAFTED · decisions: 0
