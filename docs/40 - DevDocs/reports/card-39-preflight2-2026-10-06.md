# card 39 preflight, round 2 — 2026-10-06 (read-only)

Card: `prompts/2026-10-06/39-drc-d5-o1-b2-card.md` (amended). Round 1 failed 3f and 5d.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 0 | `git diff 24a37ef9 HEAD -- <card>` | Only two hunks: B2 row `reconcile.py:361` → `:362`; new `- LOCK:` bullet in `## RECORDS` (L76). Nothing else changed | OK |
| 3f | B2 cite `reconcile.py:362` | `362:        "running_after": None if applied is None else d["running"],` | OK |
| 5d | L76 named for the with-DB step | `- LOCK: the with-DB test in test_drc_d5_db.py runs under LAWS L76 (cobalt_dev one owner, one lock, no migration left applied)…`; `LAWS.md:376: ### L76 One owner, one lock for cobalt_dev` | OK |
| 1a | `merge-base --is-ancestor 4d9e451c main` | exit 0, no output | OK |
| 1b | `rev-parse --verify ops/drc-d5-o1-b2-1006` | `fatal: Needed a single revision` (branch absent) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/drc-d5-o1-b2-1006` | `No such file or directory` | OK |
| 1d | TIP, CHECK REPORT, HOUSE B empty; DB line | Card lines 6, 8, 9 empty. No `DB:` line: CARD.md:22 makes `DB` optional, `none` only when all files sit under ops/tests-ops/docs, and the key is left out otherwise; this card touches `src/`, so omission is correct | OK |
| 1e | `git log --oneline 4d9e451c..main -- src tests configs` | empty | OK |
| 2 | `grep -n "^| R326 " reports/cto-2026-10-03.md` | `332:\| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three … \| HIS RULING · APPROVED \|`; file clean vs HEAD | OK |
| 3a | `store.py:934`–`:935` (K2 delete) at BASE | `934: for d, out in [(pairing.day, rows), *writes]:` / `935: conn.execute(f"DELETE FROM drc_rows … AND day = %s", (d,))` | OK |
| 3b | `store.py:944`–`:949` (stale mark) | `944: for d in stale:` … `946: "UPDATE drc_rows SET derived = derived \|\| %s …"` … `948: (Jsonb({"book_stale": stale_mark}), d)` `949: )` | OK |
| 3c | `store.py:1455`–`:1474`, `:1460`–`:1461` | `1455: def record_build`; `1460–1461` docstring "(K2's `record_day` deletes EVERY kind of a day it re-pairs, these two with them; D3-2r)"; `1472–1474` the build-kinds DELETE | OK |
| 3d | `build.py` `:470`–`:498`, `:483`–`:484`, `:485`–`:493`, `:919`–`:922`, `:945` | `470 def _unresolved`; `483 earlier = next(… "build_day")`; `484 same_day = …["unresolved"]`; `485–493` stale/resolved; `498 return items, read`; `919 if check and plan.reconcile:` … `921 applied = … reconcile.apply`; `945 build_date(d, …, check=False)` | OK |
| 3e | `reconcile.py` `:308`–`:320`, `:310`–`:312`, `:428`–`:431` | `308 def _status`; `310 if applied["written"]:` `311 ids = …` `312 return f"adjusted to DAS: {len(…)} rows ({ids})"`; `314 nothing written — {text}`; `428 def reconciled_cards` | OK |
| 3g | `units.py:249`, `:270`–`:271` | `249: history, then what was written (`adjusted to DAS: <k> rows (<ids>)`) or`; `270 if r.get("running_after") is not None:` `271 lines.append(f"  running after: …")` | OK |
| 3h | tests: xfail strict `:580`–`:593`, `:590`, `_Legs :65`–`:69`, `:266`, `:380`; db `:65`, `:190`–`:209`, `:219`–`:224` | `580 @pytest.mark.xfail(strict=True…`; `590 store.build.pop(D)`; `593 assert f"unresolved: card 42 — …"`; `65 class _Legs`, `69 def __init__(…, refuse=None)`; `266 test_d5_2_the_event_day_build_writes…`; `380 def _x11`; db `65 def d5_lane`, `190 test_d5_3_with_db_x11…`, `219–224` resolve + D keeps record | OK |
| 4a | O1 red on BASE: store `DELETE` at 935 drops every kind; `build_day` gone so `_unresolved` `:483`–`:484` finds no `same_day`; re-pair build is `check=False` (`:945`), so `apply` (`:919`) never runs; strict xfail at `:580` asserts the item line | Reasons hold. New with-DB test red for the same reason, X11 shape at db `:190`–`:209` is the base of it | OK |
| 4b | O1 controls green | db `:219`–`:224` resolve clears `D_NEXT`, `:224` D keeps record: path touches only `resolved` (`build.py:485`–`:493`) and the unchanged `record_build` | OK |
| 4c | B2 red/control + text | `_status` `:310`–`:312` ends at `({ids})`, so a `— then refused: …` line is red on BASE. Text equals `adjusted to DAS: <k> rows (<ids>) — then refused: <text>`. Control `:266`–`:275` asserts `"  adjusted to DAS: 1 rows (#900)" in body`, written with no refusal, unchanged. `EEE_CARD = 41` (`:40`); `_Legs refuse=` at `:69`; leg 102 exists (`:148`) | OK |
| 5a | no migration, table or command (R411, R412) | Card: "No new table, no migration, no new `drc_rows` kind"; `## NOT IN THIS JOB` fences them (`FAILED: O1 — migration needed`) | OK |
| 5b | files listed are the only ones touched | Rows list: `store.py`, `build.py`, `reconcile.py`, `units.py` (docstring), `test_drc_d5.py`, `test_drc_d5_db.py`, `docs/40 - DevDocs/cobalt/drc/`. `test_drc_d5_db.py` is whole in `ops/desk/gate-lists.md:24` (deselect) and `:30` (run); no gate-lists edit needed | OK |
| 5c | RESTARTS class home per path (K10) | `## RECORDS`: `drc/{build,reconcile,units}.py` → `com.cobalt.aset com.cobalt.radar`; `store.py` the same `drc/*` class; tests none; DevDocs DOCS. One home each | OK |
| 6a | `grep -n "FILL" <card>` | empty | OK |
| 6b | `git diff HEAD --stat -- <card> <draft report>` | empty (both clean vs HEAD) | OK |
| 6c | amend scope vs HEAD (`git diff 24a37ef9 HEAD`) | see row 0, matches the amend report's claim | OK |

## ISSUES
None. Round-1 FAILs 3f and 5d are fixed; no other FAIL.

PREFLIGHT DONE · card: drc-d5-o1-b2-39 · checks: 25 · fails: 0 · ready: YES
