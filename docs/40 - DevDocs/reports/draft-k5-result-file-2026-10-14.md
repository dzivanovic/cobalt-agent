# draft-k5-result-file — 2026-10-14

## §0 Headline
- Card written: `prompts/2026-10-14/548-result-file-card.md` (K5, `result-file-1014`, `ops/result-file-1014`, `DB: none`, `RULINGS: 2026-10-14 R1471`; BASE and TIP empty).
- Format `key=value`, file `<REPORT minus .md>.result`; keys are the stop line's own fields, none added; the stop line stays (L71).
- One new helper `ops/desk/result-read.sh`; three gate copies read it (`deploy-step0.sh` P2, `deploy-card.sh`, `desk-launch.sh` deploy P2); two hub sentences appended to one line each; 6 rows, each red first with a negative control.
- Nothing was run: no test executed, UNPROVEN until the build.

## DECISIONS
- ASK DESK: the launch-time readers of the build report (`card-fill.sh:66-78`, `preflight.sh:246-270`, `desk-launch.sh:1689-1698`) and the finish signal (`desk-watch.sh`, `desk-done.sh`) stay on the stop line; only the deploy gate reads the file. Default: as the card says (not built here; a later card moves them if he wants). [07:38 ET]
- ASK DESK: `tests/ops/test_build_hub_no_clutter.py:57-60` holds the whole BUILD-HUB equal to BASE `5e5fab02`; any BUILD-HUB edit turns it red, and card 523 H3 (3) repairs the same lines. RF2 rewrites that body as an ordered-subsequence check by content. Default: build this card after 523's recut lands, then RF2 edits the body 523 left; if 523 is still unbuilt, the desk sequences them, never both at once. [07:38 ET]
- ASK DESK: the held path (`held unfixed` ≥ 1) and any SHIPS literal beyond the clean pair keep the stop-line read and THE RULE untouched. Default: as written (the file carries `held_unfixed` but THE RULE reads the line). [07:38 ET]
- ASK DESK: cards 546 and 547 are not in `prompts/2026-10-14/` yet, so their line ranges are unread. Default: no overlap expected (this card's ranges are `BUILD-HUB.md:109`, `CHECK-HUB.md:125`, `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `test_build_hub_no_clutter.py:57-60`); the desk compares them when they exist. [07:38 ET]
- ASK DESK: file name `.result` beside the report (not `.json`). Default: `.result`, plain `key=value`, as the card says. [07:38 ET]

## RECORDS
- Reads (07:2x–07:38 ET, `main` HEAD `0ffb6949`): `prompts/CARD.md`, `2026-10-13/523-hub-text-card.md`, `reports/cto-2026-10-14-words.md` R1471, `reports/survey-blockers-2026-10-12.md` (row 24 is the stop-line parsing row; its grep for "stop line" found only the stop-guard note), `ops/desk/gate.sh` (whole: runs suites, parses no stop line), `deploy-step0.sh:636-735`, `deploy-card.sh:470-529`, `desk-launch.sh:1440-1502` and `:1676-1710`, `preflight.sh:160-275`, `card-fill.sh:55-94`, `BUILD-HUB.md:103-111`, `CHECK-HUB.md:118-127`, `tests/ops/test_build_hub_no_clutter.py` (whole), `test_deploy_step0.py:1-90`, `test_check_hub_gate_wording.py:34-67` (grep), `src/cobalt/jobs/restarts.py:225-246` (grep).
- `git -C /Users/cobalt/cobalt diff --stat HEAD` over every code, hub and test file the card names printed nothing: every `file:line` is HEAD's (via the working tree, which equals HEAD there; no `git show` of a file, UNPROVEN beyond that diff).
- Not read: `ops/desk/desk-launch.sh:1568`, `preflight.sh:263`, `card-fill.sh:74` are quoted from card 485's text, not re-read; `deploy-card.sh:372-373` and `desk-launch.sh:1252` are the survey's cites, not re-read.
- No launch, no git write, no test run.

DRAFTED · decisions: 5
