# X5 fix card — the judge seat's answers (brain `776c834d`, 2026-10-02, under his R41)

Read: `reports/x5-fix-draft-2026-10-02.md` `## DECISIONS`; card `prompts/2026-10-02/22-x5-tap-refresh-card.md`; `BUILD-HUB.md` `## E2`, `## E3`, `## W`, THE LOCK; `reports/f15-p1-build-2026-09-30.md` (how F15 P1's with-DB tests held at `0013`); the hub hunks of `ops/devdb-lock-1001`.

## §0 Headline
- Three answered, none for Dejan. The card launches once the desk makes the two card edits below and commits it.
- DECISION 1 = (a), in W's own shape: the X5 file's with-DB runs at E2 and E3 go forward and roll back inside their own lock take. W is unchanged.
- DECISIONS 2 and 3 = the drafter's defaults, with one condition added to 2.
- One fact for the desk: row T1 and card `16` both edit `BUILD-HUB.md` and `DEPLOY-HUB.md`; the changed lines do not touch, so the base stays `53a85f27`.

## ANSWERS
1. DECISION 1 — (a). The red needs two real committed sessions and the `0022` column, so it cannot run inside a rolled-back transaction as F15 P1's with-DB tests do (their fixture applies `0022` in-transaction and holds at `0013`). Option (b) would put Edit mutations of `src/` inside the gate's take and would leave E2 with no red; (a) keeps the gate untouched and shows the real defect on `BASE`. It drops no law step: L76 asks that a migration be rolled back before the take releases, and it is; both migrate strings are on the build line; nothing new is granted. It sets aside one sentence of a fixed file ("NO forward", `BUILD-HUB.md` `## E2`) for this card's X5 runs only. That is a desk-level decision (R41, 09-30 R127); he sees it at DONE and may veto.
2. DECISION 2 — yes, the two tests replace `cobalt.cards.predictions.write_record` with a capture. A committed record is immutable and pins its card, so a real record would leave `ZZX5R` on `cobalt_dev` for good and turn the stray-row read red. The defect is in the row update, not in the record; the record path stays pinned by `test_f15_p1_records_db.py`. CONDITION: the capture binds its arguments against the real function's signature (`inspect.signature(write_record).bind(...)`), so a renamed or dropped parameter fails the test instead of passing silently. L45 does not bar this: no fixture is invented, and the sessions, the lock and the rows are real.
3. DECISION 3 — yes, a new file `tests/cobalt/test_x5_tap_refresh_db.py`; the F15 P1 experiment stays untouched. T1 carries it as written (deselected in pass 1, added to pass 2).

## THE TWO CARD EDITS — the desk's, then commit and launch
(i) `RULINGS:` becomes `2026-10-02 R52, 2026-10-02 R41`.
(ii) In `## RECORDS`, the last bullet (`THE RED'S LEVEL: …`): replace its closing placeholder (from the guillemet that opens it to the guillemet that closes it) with this text, byte for byte:

THE JUDGE SEAT'S ANSWER TO DECISION 1 (2026-10-02 R41, `reports/x5-fix-decisions-2026-10-02.md`): for this card the with-DB runs of `tests/cobalt/test_x5_tap_refresh_db.py` at E2 (the BASE red and the negative control) and at E3 (the two mutations and the green) run at the TOP level, each group inside its own lock take, in W's shape and under W's rules: THE LOCK (a)–(b); `<FP>` → `<F0>`; `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `0013`; `COBALT_ENV=dev uv run cobalt db migrate` in the FOREGROUND, with `dev forward: APPLIED <time>` recorded at once; the file alone, `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_x5_tap_refresh_db.py`; the (c3r) read for `ZZX5R` → no rows; then ALWAYS `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013`, `<FP>` equal to `<F0>` field for field, and the lock's (d). The sentence "NO forward" of `BUILD-HUB.md` `## E2` is set aside for these runs and for nothing else. Each such take is one `## RECORDS` line. W is unchanged. The capture that replaces `write_record` binds its arguments against the real function's signature, so a changed parameter fails the test (DECISION 2).

## RECORDS
- Merge with tonight's set: `ops/devdb-lock-1001` changes `BUILD-HUB.md` lines 8, 12, 14, 32, 36, 39, 51, 55, 59, 93, 106 and `DEPLOY-HUB.md` lines 8, 11, 13, 15, 35, 42–43, 55, 62, 74, 101, 111–113, 180 (`git diff -U0 093028d0 aeefb6df`). T1 edits `BUILD-HUB.md` 84 and 88 and `DEPLOY-HUB.md` 105 and 109. The nearest pair is `DEPLOY-HUB.md` 109 and 111, with one unchanged line between: no shared line. A conflict at the gate's STEP-T would still be possible in principle (UNPROVEN until the merge runs); if it happens, X5 drops from tonight's set, named, and ships tomorrow on a base that holds card `16`.
- `HOUSE B: as needed` is right for the check: the fix writes no vault note and changes no sizing. The check runs the normal flow with an outside house (the script program's overrule, R47, does not cover product code).
- Each extra take commits one forward and one rollback of `0021` + `0022` on `cobalt_dev` (about 4 column slots of `aset_sizings` each); after this morning's rebuild the table stands at 54 of 1600.

X5 DECISIONS ANSWERED · 3 of 3 · for Dejan: 0 · card edits: 2
