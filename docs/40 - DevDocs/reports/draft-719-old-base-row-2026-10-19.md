## §0 Headline
- Card 719 `W` row amended in place: W1's two additions, the one-line order, the WHY line.
- BASE `e4586978` PASS 1 lacks `--deselect tests/cobalt/test_strike_detector_db.py`; PASS 2 lacks its id. Both appended.
- Header, BASE, JOB, BRANCH untouched. Nothing committed.

## DECISIONS
- D1 Additions proven: `git show e4586978:ops/desk/gate-lists.md` PASS 1 ends `--deselect tests/cobalt/test_radar_price_floor_db.py`, PASS 2 ends `tests/cobalt/test_radar_price_floor_db.py`; neither names `test_strike_detector_db.py`. Card W1 (`:34`) states: its `--deselect` at the end of PASS 1, its id at the end of PASS 2. Added: PASS 1 ` --deselect tests/cobalt/test_strike_detector_db.py`, PASS 2 ` tests/cobalt/test_strike_detector_db.py`.
- D2 Order line uses the BASE's sections: OFFLINE, PROOF ONLY, PASS 1, FORWARD, PASS 2, STRAY ROWS, LIVE-NOTE, ROLLBACK, FINGERPRINT, then ALLOWED SKIPS check. Lock taken before PROOF ONLY, released after FINGERPRINT (my choice; the gate-lists give no lock position).
- D3 Cite: the by-hand take/release text is `prompts/BUILD-HUB.md:37`; `:36` is its intro. Cited `:36-37`. The path is `docs/40 - DevDocs/prompts/BUILD-HUB.md`.
- D4 WHY line now reads `Rows M1, T1, C1-C4, W1, D1, W in order`.

## RECORDS
- Read: the prompt 865; card 719 whole; `reports/gemini-old-base-w-preflight-2026-10-19.md`; `topics/writing-rules.md`; `git show e4586978:ops/desk/gate-lists.md`; `prompts/BUILD-HUB.md:28-41`.
- Edited: card 719 (W row's first cell, WHY line) only.

DRAFTED · decisions: 4
