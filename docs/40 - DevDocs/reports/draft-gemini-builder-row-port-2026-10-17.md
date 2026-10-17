## §0 Headline
- Card 671 re-headed in place as port job `gemini-builder-row-fr1`: header, `## PORT JOB`, rows PORT and FR-2, ORDER, DEPLOY ORDER, O2 gate, CHECK ASKS P1-P3, one RECORDS entry.
- BASE `13bcd579` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main`).
- Main touched three of the six ported files since `7f415a4f`: `SHADOW-HUB.md`, `ops/desk/desk-launch.sh`, `ops/desk/bare-guard.py`. The three test files are untouched, so byte-equal to `695f8bde` after the port.
- No hunk overlaps; both cards' rows stand. Nothing run but reads; nothing committed.

## DECISIONS
1. ASK DESK: the old job's two report files (`reports/gemini-builder-row-build-2026-10-17.md` and `.result`) are in `git diff --name-only 7f415a4f 695f8bde`. The card does not port them (history; the new job writes its own report). Default: not ported. [16:59]
2. ASK DESK: card 583's FR-5 text in `SHADOW-HUB.md` says `stop line BUILT · as :28` and a 583 test pins that literal. The port inserts the Gemini note and X1 paragraph before the BAND ROUTING paragraph (as on the branch), so that paragraph moves from `:28` and the cited number goes stale. Default: leave the text byte for byte; the stale number is harmless. [16:59]
3. ASK DESK: rows L1, G2, H1, X2, R1, FR-1 keep their old `file:line`s and their 'RED on BASE' and mutation lines as context; the card says so and tells the builder to find places by content. Default: as written, not rewritten. [16:59]

## RECORDS
- 2026-10-17 16:59 EDT (`date`). Read: prompt 707; card 671; card 523 (header, FR-P1, CHECK ASKS); `reports/cto-2026-10-17.md` R1804-R1808; `tests/ops/test_band_routing_1015.py:86-117`, `:462-471`, `:638-646`; `ops/desk/desk-launch.sh:370-405`; `ops/desk/bare-guard.py` (grep `:1180-1207`, `:1257`); `SHADOW-HUB.md:10-38`, `:97`; writing-rules.md.
- Git reads: `rev-parse --short=8 main` → `13bcd579`; `diff --name-only 7f415a4f 695f8bde` (8 files); `diff --stat 7f415a4f main` over the six files (hub 15, guard 5, launcher 80; the three tests empty); `diff -U0 7f415a4f main` and `diff -U0 7f415a4f 695f8bde` over hub, guard, launcher; `log --oneline 7f415a4f..main` over the six files (583's `bd9c24ac`, `c8c5ca90`, `fda2300b`); `log -3 695f8bde`; `diff --stat 695f8bde -- ops/desk/bare-guard.py` (9+/11-: main's 5 lines plus 671's hunks, as expected on main's tree).
- Seams (hunk lists in the card's PORT row and RECORDS): hub 583 after `:27`, `:44`, `:61`, `:73` vs 671 `:12`, `:15`, after `:21`, after `:26`, `:29`, `:88`; guard 583 `g5` main `:1277` vs 671 `builder_call`; launcher 583 `:379`, `:392`, `:991-999`, `:1638-1688`, `:1717`, `:1723`, `:1740`, `:1791`, `:1817`, `:2356` vs 671 after `:376`, `:398` (main `:403`).
- Not proved: that the ported tree is green (the builder's job). Card grew by one section, two rows and five lines; no read-path file edited.

DRAFTED · decisions: 3
