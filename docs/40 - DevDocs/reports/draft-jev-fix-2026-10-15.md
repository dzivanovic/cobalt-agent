## §0 Headline
- Card 591 amended in place from preflight `## ISSUES` 1, 4, 5, 9, 10, 11 (and FAIL 18, 20).
- P0 drops the door wrapper test (brain ruling quoted byte for byte); R1 and the two `~/.cobalt` reads are `ASK DESK`; DEPLOY PROOF fixed; Z0 and F13 stop on `FAILED: DECISION <text>`.
- `BASE`, `TIP`, `HOUSE B` untouched (empty).
- Desk follow-up: preflight issue 2 done, `_classify_fixtures.md` added to P0's file list under the same PROOF.

## DECISIONS
- ASK DESK 18: row R1's `uv run cobalt classify route … --dry-run` is not on the build line. Default: the builder lists the cards by `ls` and takes the count for F1; the desk runs the dry run after the build and quotes the lines for F9's bound. [12:27]
- ASK DESK 19: `ls /Users/cobalt/.cobalt/classify` (ORDER before E2/after W; DEPLOY PROOF) is outside the builder's `--add-dir`s. Default: the desk reads it; the DEPLOY PROOF line becomes a smoke read without `· before`/`· after`. [12:27]
- ASK DESK 20: DEPLOY PROOF line 83 needs a fixed `after`; I changed the command to `grep -c -E "^spend_ledger:" …/trial.yaml` → `1` (one top-level key; the old `-F "spend_ledger"` count cannot be fixed before the build). Default: this form. [12:27]
- ASK DESK 21: F1 now also edits design `:48`; the replacement wording is the sense of R1580 (check `74` dropped, card `593` superseded, trial package ported by P0), not a text the issues give. Default: that sense. [12:27]
- ASK DESK 22: ORDER's `git diff f4e8de85 -- tests/cobalt/test_classify_*.py` clause now also allows P0's one dropped-test hunk (follows from fix 1). Default: as written. [12:27]
- Left as is: preflight issues 3, 6, 7, 8.

## RECORDS
- `date` 12:27; `main` HEAD `b8332005` (`rev-parse --short=8`); read: card 591, `reports/jev-card-preflight-2026-10-15.md`, `writing-rules.md`.
- BUILD-HUB stop line: `FAILED: <step> — <reason>` (`BUILD-HUB.md:110`), so Z0's stop is `FAILED: DECISION <text>`.
- Design `:48` proved by `Grep` ("Check `74` … runs before any new keyed call"); R1580 proved at `cto-2026-10-15.md:16`.
- Edits to the card: P0 row, Z0 row, F13 row (STOP clause; test fixture config gains `active_profile`), F2 row (`model_copy` after load), F1 row (`:48`, files), R1 row, WHY (lazy import), ORDER (STOP line, P0 hunk, `ls` reads), DEPLOY PROOF lines 83-84.
- Desk message (cto-desk): P0 row's file list gained `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md` (preflight FAIL 8, path from the preflight's check 8); ASK DESK defaults unchanged.
- Wording not read from the files: none beyond the ASK DESK items above. Nothing was run but reads.

DRAFTED · decisions: 5 · round 2
