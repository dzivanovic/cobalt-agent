# F4 card 304 — preflight, 2026-10-10

§0 Card `304-f4-refresh-card.md` (job `f4-refresh-1010`, BASE `d78c66a2`) is sound, with one FAIL: the RESTARTS paragraph does not name a class for 6 of its paths (check 20). Fix is one sentence; nothing else blocks. About 115 anchors were read at HEAD `0acf6424` (src, configs, ops, tests are clean against HEAD, and `d78c66a2..HEAD` touches none of them). All 10 drafter MOVES/DO NOT HOLD anchors are corrected in the card. Reads were done with Read on the working tree, equal to HEAD per check 2.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log -1 -- <card>` · `git diff HEAD --stat -- <card>` | `0acf6424 docs(desk): R976 F4 card 304 drafted…`; diff empty | OK |
| 2 | `git diff HEAD --stat -- src configs ops tests` · `git diff --stat d78c66a2 HEAD -- src configs ops tests` · `merge-base --is-ancestor` | both empty; BASE is an ancestor of HEAD, `rev-parse` = `d78c66a274f2…` | OK |
| 3 | header: `grep -n "«FILL"` | none. BASE `d78c66a2` filled; TIP, CHECK REPORT, HOUSE B empty | OK |
| 4 | RULINGS form + `grep -n -E "^\| (R849\|R969\|R971) "` over `cto-2026-10-10.md` | `2026-10-10 R849, 2026-10-10 R969`; R849 `:133`, R969 `:14`, R971 `:12`, each `HIS RULING · APPROVED` | OK |
| 5 | `grep -n "cto-2026-10-10"` over the card | one hit, line 2, row id R849 only; no line-number cite | OK |
| 6 | anchors, drafter MOVES/DO NOT HOLD (10) | `daily.py:479` `:575-577`; `jobs/config.py:198`; `radar/notes.py:357-363`; `aset/web.py:35-37`; `config.py:130-139`; `rules_gen.py:111-125`, `:128-159`; `store.py:91-98` (docstring only); `daymode/note.py:163`: all real at HEAD and used so in the card. Card WHY keeps `daily.py:574-577` (574 is the `state =` line, 575-577 the skip): holds as a range | OK |
| 7 | anchors, sampled ≈115 | `daily.py` 16 · `writer.py` 14 · `merge.py` 4 · `store.py` 4 · `prefill/config.py` 5 · `cli.py` 4 · `radar/notes.py` 12 · `strike/detector.py` 5 · `jobs/config.py` 5 · `wrapper.py` 2 · `restarts.py` 5 · `jobs.yaml` 7 · `daily.md.j2` 7 · `tunables.yaml` 3 · `s2.yaml` 1 · tests 6 · `clock.py` 1 · `daymode/note.py` 7 · `aset/daily_note.py` 3 · `market.py` 2 · `calendar.py` 1 · `aset/web.py` 3 · `heartbeat/runner.py` 1: 0 miss | OK |
| 8 | seam lines (`writer.py:556,564-581,650-669,718,722-741,735,753,774-795,785-787,839,844,886-919`; `merge.py:15,100,141-159`; `daily.py:297,313,435,463-473,578-582`) | each read; each holds | OK |
| 9 | `## RECORDS` | names the cite re-proof (command, 18:58), corrections, precedent files, ladder grep, restarts; the drafter report names the reads. Times missing on 2 bullets | OK (NOTE 1) |
| 10 | rows cover FINAL `## CHUNKS` F4-1 | all of §4 + stub + gate; files match FINAL §5 (plus `test_daymode_note.py`, named for `render_body`) | OK |
| 11 | T1-T14, T2b, T3b, T15-T17 | T1-T4,T2b,T9,T15-T17 → O1/O2; T3b → M1; T5 → D1; T6 → C1+S1; T7 → U1; T8,T11,T12 → E1; T10 → C2; T13 → S1; T14 → G1. Live `--dry-run` → RECORDS (owed) | OK |
| 12 | X1-X16 | in rows: X1 O1, X2 O1/M1, X3 O2, X4 W1, X5 D1, X6/X16 A1/E1, X7 S1, X11 O1, X12 W1, X13/X14 G1. Owed live and recorded: X8, X9, X10, X15 | OK (NOTE 4) |
| 13 | red-first on BASE, every test | each row names RED (`ImportError`/`KeyError`/`TypeError`) or `RUN`. Read M1: base `SPY/QQQ/IWM`, `NOTE` before `QQQ`, all replaced → `merge.py:143-159` appends `pending` after the block, so red on BASE is real. W1: `upsert_unit` (`writer.py:673`) has no `body_fn` → `TypeError` | OK (NOTE 5) |
| 14 | form B for R2-4 | G1: `planned_rpm`/`headroom_rpm` None → no gate call, no GET; else `check_scheduled_demand("prefill-refresh", radar_rpm=planned_rpm, extra=[DemandConsumer(rate 3/interval)])`; refusal → D1 path; not in `scheduled_consumers`; X13 fixture 49.95+0.1 → peak 50.05 > 50 refused (read `check_total_demand`, `notes.py:276-284`). Form A only as A1 (4) data | OK (NOTE 2, 3) |
| 15 | `DB:` | key omitted; CARD.md `DB` row allows `none` only for `ops/`,`tests/ops/`,`docs/`; card changes `src/` → omit (D1) | OK |
| 16 | no new command (R411, R412) | only `uv run cobalt jobs restarts`, pytest, the product subcommand `prefill refresh`; no desk script added | OK |
| 17 | `HOUSE B: mandatory — vault notes` | in `## RECORDS`; header empty per CARD.md. Card names no house A and no OpenAI/Codex (grep); house A = Grok (R920/R921) stays the hub's | OK |
| 18 | D2, D3, D4 stated defaults | D2 bootstrap held (RECORDS + NOT IN THIS JOB); D3 RULINGS kept, R931/R771 via FINAL §8 R4 / SEAM §7; D4 A1 (3) runs it on BASE, E1 builds as folded, red reported not fixed. Re-derived D4 from `writer.py:733-735` + `merge.py:15`: a hand-typed table is wrapped as `seed`, `merge3(seed,seed,cobalt)` → Cobalt wins. True | OK (NOTE 6) |
| 19 | writer stays unloaded | NOT IN THIS JOB: "Loading, bootstrapping or running the plist; any `uv run prefill`…; any Finviz network call" | OK |
| 20 | RESTARTS class home for every path (by reading) | named: plist (`restarts.py:198-206`), `prefill.yaml`, `tunables.yaml` (`:207-214`), `prefill/config.py`, `daymode/note.py`, `writer.py`, `merge.py`, tests, docs. NOT named: `configs/cobalt/jobs.yaml` (`:223-224` registry; register, no restart, if no resident reads it: none in `jobs.yaml` reads), `templates/daily.md.j2` (`no_resident_reads` `jobs.yaml:330`, no restart once the label is a reader), `smoke/s2.yaml` (`restarts.py:251-256` operator command), `prefill/daily.py`, `prefill/cli.py`, `prefill/market.py` (static import reach, `:215-222`; `daily` is imported by `cli.py:25` and, lazily, `drc.py:78`; whether `drc.py` reaches a resident is not traced) | FAIL |
| 21 | `uv run cobalt jobs restarts` | not run (read-only seat); R1 owns it | OK |
| 22 | numbers | 21 firings × 5 weekdays = 105 entries (05:45..15:45 step 30 includes 08:45); 3/30 = 0.1 rpm | OK |

## ISSUES
- FAIL 20: add one line to RESTARTS: `configs/cobalt/jobs.yaml` → `registry; register, no restart` (`restarts.py:223-224`); `daily.md.j2` → `no resident reads (one-shot: …)` after the label is added; `smoke/s2.yaml` → `operator command (cobalt smoke); no job reads` (`:251-256`); `prefill/daily.py`, `cli.py`, `market.py` → `static import reach`, class as R1 prints it (the `drc.py:78` lazy import is the one edge to check).
- NOTE 1: `## RECORDS` ladder and precedent bullets carry no time (CARD.md: "each with its command and time").
- NOTE 2: G1's `DemandConsumer(name=, rpm=, window=)` omits `basis`; `DemandConsumer` requires it (`radar/notes.py:215`, `min_length=1`), so the first G1 test raises `ValidationError`. The builder adds a `basis` string; the same omission is in the FINAL.
- NOTE 3: G1 does not name the plan reader: `read_plan()` / `DemandPlan` (`strike/detector.py:313-319`, `:80`), outside the READ list (`:95-180`, `:265-285`). Importing it is no edit of `strike/detector.py`; it adds an import edge from `prefill/daily.py` that R1 will classify.
- NOTE 4: W1's `X12` leg is a `NoteChangedOnDisk` retry; the FINAL's X12 is the commit-window race (A paused after `os.replace` `writer.py:556`, B runs, no override naming A's values). Not the same window.
- NOTE 5: every test in `test_prefill_refresh.py` is red on BASE by one `ImportError` if the module imports at top; per-row red holds only with function-local imports.
- NOTE 6: E1's X16 hand-typed-table leg is red by the code (D4). A committed red test breaks the `0 failed` gate; the card does not say whether that leg is `xfail(strict=True)` or data only (A1 (3) already records it).
- NOTE 7: W1 says `body_fn(snapshot)` rebuilds "from the baseline read in the same `build`", but the signature takes only `snapshot`; how the baseline reaches `body_fn` (argument, or the closure reads `writer._baseline`) is the builder's.

PREFLIGHT DONE · card: f4-refresh-1010 · checks: 22 · fails: 1 · ready: NO
