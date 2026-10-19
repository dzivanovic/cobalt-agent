## CHECKS

Edit state: committed in `ee414e79` (`git diff HEAD -- <card>` prints nothing for all three, HEAD has moved on; the proof is `git show --stat ee414e79`: +1 line in each card, 0 deleted).

| # | card | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | 855 | `grep -c "^| W |" <card>` | `1` | OK |
| 1 | 718 | same | `1` | OK |
| 1 | 719 | same | `1` | OK |
| 2 | all | `grep -h "^| W |" <3 cards> \| sort \| uniq -c` | one line, count `3` (identical text) | OK |
| 3 | 855 | placement | last table row, after B (`:28`); no row-order text on the card | OK |
| 3 | 718 | placement | last table row, after F (`:34`); no row-order text | OK |
| 3 | 719 | placement | last table row, after D1 (`:36`); WHY line `Rows M1, T1, C1-C4, W1, D1 in order` (`:24`) untouched, does not list W (cosmetic) | OK |
| 4 | 855 | `git show 8f4bbe28:ops/desk/gate-lists.md` | `## OFFLINE` `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; PASS 1 and PASS 2 tails end `…test_f15_p2_replay_db.py tests/cobalt/test_radar_price_floor_db.py tests/cobalt/test_strike_detector_db.py tests/cobalt/test_strike_stream_db.py tests/cobalt/test_strike_ack_db.py`; no `## OFFLINE OPS`; ROLLBACK `--down-to 0013`. Equals the drafter's table | OK |
| 4 | 718 | `git show 50b0cd87:ops/desk/gate-lists.md` | same OFFLINE; tails end `…test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py` (no price_floor, no strike); no `## OFFLINE OPS`. Equals the table | OK |
| 4 | 719 | `git show e4586978:ops/desk/gate-lists.md` | same OFFLINE; tails end `…test_f15_p2_replay_db.py tests/cobalt/test_radar_price_floor_db.py` (no strike); no `## OFFLINE OPS`. Equals the table | OK |
| 5 | 855 | `grep -n -i "placeholder\|<BASE>\|TBD\|XXXX"` | `BASE: 8f4bbe28` (`:5`); only hit is test text `placeholder object` (`:26`) and the row's literal `<BASE>`; `TIP:` empty, as on 718/719 | OK |
| 6 | 718, 719 | `git show --stat ee414e79` | +1 / 0 deleted each: BASE, JOB, BRANCH, WORKTREE, CHECK REPORT cannot have changed | OK |
| 7 | all | SHADOW-HUB read: `:45`, `:67` (W is BUILD-HUB `## W`), no `gate.sh` call in the hub body except `:67` | the row does not contradict SHADOW-HUB; see ISSUES 1 | OK |
| 8 | 719 | row vs. the card's own W1 (`:34`) | BASE PASS 1 does NOT deselect `test_strike_detector_db.py` (W1 adds it on the branch); the row runs the BASE's lines, so PASS 1 at 0013 collects that with-DB test (needs `0022`, `W1` text `:34`) | FAIL |

## ISSUES

1. SHADOW-HUB still calls `gate.sh` unconditionally, by reference: `SHADOW-HUB.md:67` (`BUILD-HUB ## RESTARTS and ## W as they stand (gate.sh <worktree> all --deploy …)`) and `:45`. The call itself is `BUILD-HUB.md:83` (`gate.sh <WORKTREE> all --deploy`, every command "read from THIS worktree's gate-lists.md"); `gate.sh:191` parses `OFFLINE OPS` from that file, which is why 855 ended `FAILED: W`. Main's file has it (count 1); the three BASEs do not. Can the hub follow the row? Yes on permissions: its allow line holds `uv run pytest *`, `COBALT_ENV=dev uv run pytest *`, `COBALT_ENV=dev uv run cobalt db *`, the `.env` cp/rm, `sh /Users/cobalt/cobalt/ops/desk/*` (lock scripts). But the row says only "exactly as then": it does not give the order (OFFLINE, PROOF ONLY, PASS 1, FORWARD, PASS 2, STRAY ROWS, LIVE-NOTE, ROLLBACK, FINGERPRINT), the by-hand lock/`.env` handling (BUILD-HUB `:36`), or the ALLOWED SKIPS check. The card governs, but the hub has to improvise those; the drafter's DECISION 1 default (which sections are "suite commands") is the unwritten part. Not blocking by itself.
2. BLOCKS 719 (check 8): the row runs the BASE's lines, and 719's W1 exists because `test_strike_detector_db.py` needs a level above 0013 (`0022`). The BASE's PASS 1 has no `--deselect` for it and its PASS 2 has no id, so PASS 1 (`tests/cobalt … --db-only`) will collect it at 0013 and go red. 855 and 718 are not hit (855's BASE already deselects the strike tests; 718 adds offline tests only). Fix: on 719 the row (or W1) says the BASE's lines plus W1's branch additions at the end of PASS 1 and PASS 2.
3. Cosmetic: 719 WHY line `Rows M1, T1, C1-C4, W1, D1 in order` does not mention the new `W`.

PREFLIGHT DONE · cards: 855 718 719 · checks: 13 · fails: 1 · ready: NO
