# F4 card 304 — preflight round 2, 2026-10-10

§0 Card `304-f4-refresh-card.md` (job `f4-refresh-1010`, BASE `d78c66a2`) passes. Round 1's FAIL 20 and NOTE 1-7 are each resolved in the amended card (table below). No FAIL. Two new NOTEs (8, 9), neither blocks. About 120 anchors read at HEAD `3ec87ff8`; 0 miss. Reads are on the working tree, equal to HEAD (checks 1-2).

## ROUND 1 RESOLVED
| round 1 | resolved in | how |
|---|---|---|
| FAIL 20 | RESTARTS paragraph | names a class for every path: plist; `prefill.yaml`, `tunables.yaml` (resident reads); `prefill/config.py`, `daymode/note.py` (static import reach); `writer.py`, `merge.py`; `jobs.yaml` (`registry; register, no restart`); `daily.md.j2` (`no resident reads (one-shot…)`, C2 adds the label as a reader); `smoke/s2.yaml` (operator command); `daily.py`, `market.py` (static import reach, the `drc.py:78` edge traced to aset and radar); `cli.py` (no module imports it); G1's new `strike.detector` edge left to R1; tests, docs |
| NOTE 1 | `## RECORDS` | LADDER and PRECEDENT bullets carry command and time (19:07 EDT); amend bullet carries 19:05-19:07 |
| NOTE 2 | row G1 | `DemandConsumer(... basis="<non-empty string>")`, `min_length=1` at `:215` |
| NOTE 3 | row G1 | `read_plan()` / `DemandPlan` named (`strike/detector.py:313-319`, `:80`); import edge left to R1; no edit of `strike/detector.py` |
| NOTE 4 | row W1 | X12 leg is the commit-window race (A paused after `os.replace`, `_commit` `writer.py:556`); the `NoteChangedOnDisk` retry leg is X4's |
| NOTE 5 | card WHY | the new test file imports the new names inside each test function; red on BASE per test |
| NOTE 6 | row E1 | X16 hand-typed-table leg `@pytest.mark.xfail(strict=True, reason=…)`; build report lists the red |
| NOTE 7 | row W1 | `body_fn(snapshot)` only; closure over `writer` calls `writer._baseline(path, section, unit_id)` (`:836-839`) each call |

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log -1 --format=%h %s -- <card>` · `git diff HEAD --stat -- <card>` | `3ec87ff8 docs(desk): F4 card 304 amended, preflight2 prompt 312`; diff empty | OK |
| 2 | `git diff HEAD --stat -- src configs ops tests` · `git diff --stat d78c66a2 HEAD -- src configs ops tests` | both empty | OK |
| 3 | `grep -n "«FILL"` over the card | none; BASE `d78c66a2` filled, TIP, CHECK REPORT, HOUSE B empty | OK |
| 4 | RULINGS form + `grep -n -E "^\| (R849\|R969\|R971) "` over `cto-2026-10-10.md` | `2026-10-10 R849, 2026-10-10 R969`; R849 `:135`, R969 `:16`, R971 `:14`, each `HIS RULING · APPROVED` | OK |
| 5 | `grep -n "cto-2026-10-10"` over the card | one hit, line 2, row id R849 only; no line cite | OK |
| 6 | round 1 FAIL 20 + NOTE 1-7 | all 8 resolved, table above | OK |
| 7 | anchors, MOVES/DO NOT HOLD (10) | `daily.py:479` `datetime.now().astimezone()`, `:575-577`; `jobs/config.py:198`; `radar/notes.py:357-363`; `aset/web.py:35-37`; `config.py:130-139`; `rules_gen.py:111-125`, `:128-159`; `store.py:91-98`; `daymode/note.py:163`, `:252`: all real at HEAD | OK |
| 8 | anchors, seam lines | `writer.py:556,559,564-581,650-669,663,718,722-741,735,753,795,836-839,844,886-919`; `merge.py:15,100,141-159`; `daily.py:297,313,328-355,435,463-473,578-582`; each read; each holds | OK |
| 9 | anchors, sampled (≈120) | `daily.py` 18 · `writer.py` 16 · `merge.py` 4 · `store.py` 4 · `prefill/config.py` 6 · `cli.py` 5 · `radar/notes.py` 14 · `strike/detector.py` 6 · `jobs/config.py` 6 · `wrapper.py` 3 · `restarts.py` 10 · `jobs.yaml` 9 · `daily.md.j2` 8 · `tunables.yaml` 3 · `s2.yaml` 1 · `clock.py` 1 · `daymode/note.py` 4 · `aset/daily_note.py` 3 · `market.py` 1 · `rules_gen.py` 2 · `aset/web.py` 5 · `heartbeat/runner.py` 1 · `drc/*`, `cli.py:68` 6 · `pyproject.toml:68` · tests 5: 0 miss | OK |
| 10 | `## RECORDS` | HOUSE B, writer gate, cite re-proof (18:58), PRECEDENT and LADDER with time, RESTARTS amend with times | OK |
| 11 | rows cover FINAL `## CHUNKS` F4-1 | A1 C1 C2 M1 W1 O1 O2 S1 D1 G1 E1 U1 K1 R1 DOC; stub, gate, stamp, template, plist, smoke row, docs all present | OK |
| 12 | T1-T14, T2b, T3b, T15-T17 | T1-T4, T2b, T9, T15-T17 → O1/O2; T3b → M1; T5 → D1; T6 → C1+S1; T7 → U1; T8, T11, T12 → E1; T10 → C2; T13 → S1; T14 → G1 | OK |
| 13 | X1-X16 | X1 A1/O1, X2 O1/M1, X3 O2, X4 W1, X5 D1, X6/X16 A1/E1, X7 S1, X11 O1, X12 W1, X13/X14 G1; X8, X9, X10, X15 owed live in `## RECORDS`; X17 in A1 (4) as data; X18 moot | OK |
| 14 | red first per test | each row names RED (`ImportError`, `KeyError`, `TypeError`, or the M1 order) or `RUN`/text only; `upsert_unit` (`writer.py:673-682`) has no `body_fn` → `TypeError`; M1 reads `:156`, `:159` `pending` after the block | OK |
| 15 | form B for R2-4 | G1: plan unreadable or `headroom_rpm` ≤ 0 → no gate call, no GET; else `check_scheduled_demand("prefill-refresh", radar_rpm=planned_rpm, extra=[DemandConsumer(... basis=...)])`; refusal → D1 path; not in `scheduled_consumers` (`:329-381`). X13: 49.95 + 0.1 = 50.05 > 50 refused (`check_total_demand` `:276-284`). Form A only as A1 (4) data | OK |
| 16 | `DB:` per D1 | key omitted; CARD.md `DB` row allows `none` only under `ops/`, `tests/ops/`, `docs/`; the card changes `src/` | OK |
| 17 | RESTARTS class home per path | see round-1 row FAIL 20; `jobs.yaml` has no resident `reads` naming `jobs.yaml` (`grep -n "jobs.yaml"` over it: none); `prefill.yaml` aset `:81`; `tunables.yaml` aset `:69`, radar `:200`; `daily.md.j2` `no_resident_reads` `:330-335`; `drc` chain `aset/web.py:2114` → `drc/imports.py:640,808` → `drc/build.py:72,178` → `prefill/drc.py:78` → `daily.py`; radar `jobs.yaml:203` → `cli.py:68` → `drc/cli.py:261-262`; `restarts.py:120,133,198-206,211-214,215-222,223-224,251-256` | OK |
| 18 | no new command (R411, R412) | card names `uv run cobalt jobs restarts` (R1), pytest and the product subcommand `prefill refresh`; no desk script added | OK |
| 19 | `HOUSE B: mandatory — vault notes`, house A Grok, no OpenAI (R920) | HOUSE B line in `## RECORDS` (`:67`), header field empty per CARD.md `:21`; `grep -n -E "OpenAI\|Codex\|Grok\|house A"` over the card: none | OK |
| 20 | D2, D3, D4 defaults consistent | D2 bootstrap held (NOT IN THIS JOB, RECORDS writer gate); D3 RULINGS kept, R931/R771 via FINAL; D4 A1 (3) runs it on BASE, E1 builds as folded, red reported not fixed. Re-derived D4: `writer.py:733-735` `merge3(seed, seed, cobalt_lines)` with `merge.py:15` → Cobalt wins. True | OK |
| 21 | writer stays unloaded | NOT IN THIS JOB: no loading, bootstrapping or running the plist, no `uv run prefill`, no Finviz call | OK |
| 22 | write path in tests | `assert_write_target` (`writer.py:181-226`): a `tmp_path` is outside the repo and the prod vault, so allowed when `COBALT_ENV` is not production; `dev_db_tx` is autouse (`conftest.py:262-263`) | OK (NOTE 9) |
| 23 | numbers | 05:45-15:45 step 30 = 21 firings × 5 weekdays = 105; 08:45 included; 3 / 30 = 0.1 rpm | OK |

## ISSUES
- NOTE 8: the with-DB tests write through the real clock: `VaultWriter._session_gate` (`writer.py:416-445`) refuses inside `market_reset` (20:00-21:00 ET), and `VaultWriter` takes `clock` and `now` (`:388-389`). The card does not say to pass `now`, so a test run in that hour fails. The builder passes `now` in the fixture writer.
- NOTE 9: `pytest.mark.usefixtures("dev_db_tx")` is redundant (the fixture is autouse, `conftest.py:262`); `test_vaultwrite.py:54` also carries `requires_db` and `requires_dev_vault`, and the card takes only the fixture, correct for `tmp_path`. No change needed.

PREFLIGHT DONE · card: f4-refresh-1010 · checks: 23 · fails: 0 · ready: YES
