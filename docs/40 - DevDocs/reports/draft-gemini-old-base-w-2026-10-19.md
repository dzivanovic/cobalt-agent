## §0 Headline
- Row `W` added, identical text, to cards 855, 718, 719 (each as its last table row; no card had a `W`-for-this row).
- No BASE of the three has `## OFFLINE OPS` in its gate-lists; `294457a8` is not an ancestor of `8f4bbe28`.
- Every BASE's gate-lists names suite lines (table below): no `ASK DESK` for a missing list.
- 3 decisions, none blocking. Nothing committed; no header changed.

## DECISIONS
- ASK DESK: which gate-lists sections are "the suite commands". Default: `## OFFLINE`, `## PASS 1`, `## PASS 2` are the suites; `## PROOF ONLY`, `## FORWARD`, `## ROLLBACK`, `## FINGERPRINT` are the with-DB step's migration frame, run in gate.sh's order under the cobalt_dev lock. The row says "the lines that gate-lists of that date names" and does not list them. [13:20]
- ASK DESK: placement. 855 and 718 hold no W rows (A, B / A–F, F is the RUN row), so `W` is the last table row of each. 719 already has `W1` (its gate-lists edit, unrelated), so the new `W` sits after `D1`, last row, and the WHY line "Rows M1, T1, C1-C4, W1, D1 in order" is untouched. Default: as placed. [13:20]
- ASK DESK: 719's own `W1` edits `ops/desk/gate-lists.md` on the branch; the new row reads the BASE's file (`git show <BASE>:`), not the branch's. Default: no conflict; as written. [13:20]

Per-BASE lines (`git -C /Users/cobalt/cobalt show <BASE>:ops/desk/gate-lists.md`; `OFFLINE OPS` count 0 in each, read whole):

| card · BASE | OFFLINE | PASS 1 / PASS 2 | frame |
|---|---|---|---|
| 855 · `8f4bbe28` | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` | `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect …` / `…tests/cobalt/test_tenancy.py::TestMigrationRoundTrip …`; deselect and PASS 2 tails end `test_f15_p2_replay_db.py tests/cobalt/test_radar_price_floor_db.py tests/cobalt/test_strike_detector_db.py tests/cobalt/test_strike_stream_db.py tests/cobalt/test_strike_ack_db.py` | PROOF ONLY, FORWARD, ROLLBACK `--down-to 0013`, FINGERPRINT as in the file |
| 718 · `50b0cd87` | same | same, tails end `test_drc_d5_db.py tests/cobalt/test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py` (no price_floor, no strike) | same |
| 719 · `e4586978` | same | same, tails end `…test_f15_p2_replay_db.py tests/cobalt/test_radar_price_floor_db.py` (no strike) | same |

The PASS 1 / PASS 2 lines are ~2 KB each; the gate seat quotes them verbatim from `git show`, as the row says. The three BASEs differ only by those tails.

## RECORDS
- Read: the prompt 863; cards 855, 718, 719 whole; `topics/writing-rules.md`; precedent `prompts/2026-10-19/857-draft-717-step0.md`.
- `git show <BASE>:ops/desk/gate-lists.md` read whole for `8f4bbe28`, `50b0cd87`, `e4586978`: no `## OFFLINE OPS` heading in any (the file's headings: OFFLINE, PROOF ONLY, PASS 1, FORWARD, PASS 2, STRAY ROWS, LIVE-NOTE, ROLLBACK, FINGERPRINT, ALLOWED SKIPS, LEVEL 0013).
- `git log -S"## OFFLINE OPS" -- ops/desk/gate-lists.md` → `294457a8 2026-10-15` only; `git merge-base --is-ancestor 294457a8 8f4bbe28` → exit 1 (not an ancestor). Not run for the other two BASEs (older cards; whole-file read stands).
- Main's file has `OFFLINE OPS` (Grep count 1).
- Edits: 855 after row B; 718 after row F; 719 after row D1. Time `date`: 2026-10-19 13:11.

DRAFTED · decisions: 3
