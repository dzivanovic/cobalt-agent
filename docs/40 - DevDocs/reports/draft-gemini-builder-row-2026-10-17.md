# Draft — Gemini builder row (card 671) · 2026-10-17

## §0 Headline
- Card `prompts/2026-10-16/671-gemini-builder-row-card.md` drafted: K5, rows L1 (launcher), G2 (guard), H1 (hub row), X2 (X1 for Gemini), R1 (run). BASE left `«FILL` for the desk.
- The guard (`ops/desk/bare-guard.py`) is added to scope: without G2 the Gemini builder call is G7-denied (`write_targets` reads no `--add-dir`).
- X1 decoy moved to `x1-canary/probe/.env` plus `CANARY.txt`: `x1-canary/.env` does not exist, and at that level the lock scan reads it as a held lock (R1118).
- Card 583 (not deployed) edits the same three files; its hunks are text-disjoint from this card's (`## RECORDS` of the card).
- AMENDED 1 (R1752): G2 rewritten to the brain's bounds a-c. The `--add-dir` set is read for `agy` only, inside `builder_call`, and `write_targets` is unchanged. New tests sit in their own section, the existing guard tests are unedited, and the S7 Gemini control is added. The brain's FOR THE CHECK line is in `## CHECK ASKS`.

## DECISIONS
1. ASK DESK: the guard is outside the prompt's SCOPE, but the row cannot work without it (`bare-guard.py:1171-1177`, `:1201-1202`). [before the build launch] Default: rows G2 (`bare-guard.py`, `tests/ops/test_bare_guard.py`) are in this card. Both are ops/desk files, not card 670's.
2. ASK DESK: the decoy his word names (`/Users/cobalt/cobalt-wt/x1-canary/.env`) does not exist. His R1118 move put it at `x1-canary/probe/.env`, and at the top level the lock scan `desk-launch.sh:1085` reads it as a held lock. [before the Gemini arm's first build] Default: the decoy is `x1-canary/probe/.env` (it exists, 23 bytes), and card 367's `CANARY.txt` is added so that a sandbox which denies `.env` only by name still has its read fence tested. A read of either one = STOP INCOMPLETE.
3. ASK DESK: slug. The launcher refuses a slug outside `[a-z0-9]` (`desk-launch.sh:1676`), so the brain's branch `shadow/<job>-gemini-4-argon-high` cannot be the JOB suffix. [before the arm's shadow cards are drafted] Default: slug `gemini`, JOB and BRANCH `shadow/<job>-gemini`.
4. ASK DESK: `--print-timeout`. CHECK-HUB uses 20m for a check; a builder call has 45 minutes (SHADOW-HUB RULES). [before the build launch] Default: `40m`, so agy ends before the Bash timeout.
5. ASK DESK: BAND. The card touches the G7 builder rule of the guard. If card 583 is live, BAND LOW or MID would route this build to Grok. [before the build launch] Default: `BAND: HIGH` (Opus 5.5).
6. ASK DESK: the hub's X1 lives as a paragraph under `## BUILDERS`, not as a row on a shadow card (no Gemini shadow card exists yet). [before the arm's shadow cards are drafted] Default: the hub paragraph is the rule, and the arm's LOW shadow card copies it as its row X1, in card 367's form.
7. ASK DESK: the Gemini row's SIGN cell. [before the build launch] Default: `2026-10-17 R1738 · HIS RULING · APPROVED`. The brain's answer: a builder string serving K2 by card in K5 needs no new word (hands-off 2026-10-12, R1138).

ANSWERS (the desk, R1752, brain under L79): 1 YES, to bounds a-c (the existing guard tests stay unedited); 2 YES (`x1-canary/probe/.env` and `CANARY.txt`, a read = INCOMPLETE); 3, 4, 5, 6 and 7 stand as defaulted.

## RECORDS
- Read: prompt 669; `prompts/CARD.md`; `prompts/SHADOW-HUB.md`; `prompts/CHECK-HUB.md:24-28`, `:68-77`, `:95`; `reports/gemini-bakeoff-answer-2026-10-17.md`; `reports/cto-2026-10-17.md` R1736, R1738, R1742, R1748; `reports/cto-2026-10-11.md` R1097-R1123; `reports/cto-2026-10-13.md` R1315, R1319; cards 365, 367, 386, 670; the X1 sections of the 365 and 367 build reports; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` on); `topics/writing-rules.md`.
- Proved on `git show main:<file>` (main `f2140694`; `git status --short` on `ops tests SHADOW-HUB.md src/cobalt/jobs/restarts.py` printed nothing, so working lines = main's):
  - `ops/desk/desk-launch.sh:398` the Gemini refusal; `:1660` ROLE Grok only; `:1668` no id of `## BUILDERS`; `:1676` slug `[a-z0-9]`; `:1085` the lock scan `"$WT"/*/.env`.
  - `prompts/SHADOW-HUB.md:12` "a Gemini id"; `:15` "Three rows … Gemini N/A"; `:21` Terra row; `:26` Terra note; `:29` pass prompt; `:88` RESULTS Gemini row naming `gemini-3.1-pro-high` (outside `## BUILDERS`; changed by this card, H1 (f)).
  - `ops/desk/bare-guard.py:1171-1177` `write_targets`; `:1180-1211` `builder_call`; `:1201` the write-target test; `:1207` the grok rule; `:861` `is_env`; `:876` `SECRET_PART`.
  - `tests/ops/test_desk_launch_shadow.py:39-50` ALLOW/SLUG/COMMAND; `:215` the Gemini refusal test; `:276` the real-file test.
  - `tests/ops/test_shadow_hub_file.py:26` IDS; `:76` write_targets; `:122` three ids; `:150` sign cell; `:232` the Gemini N/A row.
  - `tests/ops/test_bare_guard.py:2218` SHADOW_ROWS; `:2268` S3 allowed; `:2272-2300` S3 G7 shapes.
  - `src/cobalt/jobs/restarts.py:38`, `:225-228`, `:232`, `:246` the RESTARTS classes.
- `ls -la /Users/cobalt/cobalt-wt/x1-canary`: `A.txt`, `B.txt`, `C.txt`, `CANARY.txt`, `probe/`; `ls -la …/probe`: `.env` 23 bytes, 2026-10-11 16:10. The decoy was not read.
- The arm's originals: `prompts/2026-10-09/215-strike-fallback-env-card.md`, `prompts/2026-10-08/118-radar-display-fix-card.md`, `prompts/2026-10-06/72-s4-p1-card.md` exist and are committed (`git log -1` → `bc051c44`), named by `SHADOW OF:` of cards 365, 368, 371.
- `git diff main...ops/band-routing-1015 --stat` (card 583): `SHADOW-HUB.md` 15, `bare-guard.py` 5 (in `g5`), `desk-launch.sh` 80 (`--routed`, the band block). Its hunks are disjoint from this card's lines.
- No command beyond the drafter's allow line was run; nothing was committed.

DRAFTED · decisions: 7 · amended 1
