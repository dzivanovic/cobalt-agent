# cos-tunables preflight r2 · card 933 · 2026-10-20

Card read whole at HEAD `e69d5ab8`. `git diff main --stat` over `src/cobalt/{heartbeat,jobs,smoke,cos,hitl}`, `configs`, and the cos/smoke tests printed only an uncommitted `configs/cobalt/rules.yaml` (not an anchor): every anchor below is main's. BASE `bd7bc0c9` trails by desk commits (allowed); `TIP:` empty (expected). Not run: `uv`, pytest, `authorize.sh` (not on this seat's line).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff cd9affb7 HEAD -- <card>` | hunks only in T2 (adds "spells `enabled: false` nowhere … marker 1"), P1 (adds the two `bootstrap_owed` patches + `test_disabled_row_is_unknown` invariant + docstring `:4` + file named, `\|` grep gone), Suites (names `test_cos_probes.py`), DEPLOY PROOF (+1 marker line). Header, T1, NOT IN THIS JOB, READ, CHECK ASKS, RECORDS untouched. The amend changed nothing else | OK |
| 2 | `git log --oneline -4 -- <card>`; `git status` of the card | committed (`e69d5ab8`, `cd9affb7`, `09c4be0e`); no working-tree change | OK |
| 3 | header fields vs `prompts/CARD.md` (JOB, LADDER, CLASS, INSTALL, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, BAND MID, RESTARTS, RULINGS) | all present, well formed | OK |
| 4 | `RULINGS: none` vs `ops/desk/authorize.sh:205-210` | `none) ;;` at `:207` → no `rulings` call, no row; round-1 FAIL 1 cleared | OK |
| 5 | `tunables.yaml` `grep -n` | `cos.poll_interval_s` `:1008` value `:1009` null; `cos.session_rotate_at` `:1017` null; `hitl.request_ttl_min` `:1026` value `:1027` null; `hitl.page_base_url` `:1038` null; `cos.max_turns` `:989` = 30. Anchors as the card says | OK |
| 6 | `session.py` / `run.py` / `actions.py` anchors | unchanged from round 1 (tree = main) | OK |
| 7 | `jobs.yaml:206-217` (Read) | label `:206`, `enabled: false` `:214`, comment `:209-213`, `:215-216` "no value yet", `timeout_s: 1200` `:217`; reads `:218-225` each cite a loader; `test_every_cos_read_cites_a_loader` reads the block text, a re-worded comment does not touch it | OK |
| 8 | `watchdog.py` / `checks.py` anchors | `bootstrap_owed` `:63`, call `:437` (module-global lookup, so the P1 monkeypatch of `cobalt.jobs.watchdog.bootstrap_owed` takes); K18 `:428-451` | OK |
| 9 | `probes.py:125-187` (Read) | `COS_LABEL :126`, `_cos_enabled :129`, `cos :135` (enabled check `:142`, stores built `:146-153`, no-heartbeat RED `:155-156`), `hitl :167` (enabled check `:173`, `HitlStore() :178`). P1's insertion point "after the enabled check, before any store" exists in both | OK |
| 10 | `test_cos_offline.py:270-294` | as round 1; `value is None` `:294` is the pin T1 turns into an invariant | OK |
| 11 | `test_cos_registry.py` (Read whole) | `enabled is False :28`, docstring `:1-6`, name `:21`, invariant `:29-32` with `POLL_FALLBACK_S`; `:36-48` reads raw block, unaffected | OK |
| 12 | `test_cos_probes.py` (Read whole) | `:4` docstring, `:26-34` `enabled=True` (needs owed patch), `:37-42` pins `"enabled: false"` via the REAL registry (card now rewrites it), `:45-56` `enabled=True` (needs owed patch), `:59-71` fakes `probes.cos`/`probes.hitl`, never reads the owed file | OK |
| 13 | `git grep -n -E "bootstrap_owed\|COS_LABEL\|enabled: false\|BOOTSTRAP_OWED_PATH" -- tests` | cos-row hits: `test_cos_probes.py:4,41,42` and `test_cos_registry.py:3` (all in the card's rows). Others are not the cos row: `test_jobs.py:967`, `test_smoke.py:1599` patch `BOOTSTRAP_OWED_PATH` to `tmp_path`; `test_herdr_probe.py` (herdr, patched `_herdr_enabled`, asserts herdr `enabled is True`); `test_hitl_offline.py:106` (agent yaml); `test_card_settings.py`/`radar.cards_enabled` (unrelated); `test_jobs_reads.py:94` is a comment only (`len(keys) == 7` counts `reads:` lines, flag-free) | OK |
| 14 | `git grep -n "com.cobalt.cos\|\.enabled" -- tests` (enabled/readers/restarts users) | `test_jobs_reads.py:109,148,154,167`, `test_jobs_restarts.py:226` list cos as a reader regardless of the flag; `test_jobs.py:71-141` loop all specs for plist parity; sweep tests at `:433-473,696,882-1030` use constructed registries / `tmp_path` owed file; `test_smoke.py:1635` is a fake `_Spec`. None reads the real cos flag or the real owed file | OK |
| 15 | other P1 consumers of the probes | `runner.py:148-149` comment only; `test_the_runner_calls_both` fakes every probe, never reaches `bootstrap_owed` | OK |
| 16 | pins vs invariants (L69), X4 | T1 (`int`, not `bool`, `> 0`), T2 (`if spec.enabled: plist is_file`), P1 (`enabled=False` explicit + `load_job_registry().spec(COS_LABEL).enabled` branch) read no flag value / no 10 / 30. Round-1 FAIL 2 cleared | OK |
| 17 | owed-file reads after P1: `data/deploy/bootstrap-owed.json` | the two `enabled=True` tests patch `bootstrap_owed` to `frozenset()` (card P1); the new tests patch it explicitly both ways. No test depends on the desk checkout's real file | OK |
| 18 | `grep -c -F "enabled: false" configs/cobalt/jobs.yaml` | `1` (before `1`) | OK |
| 19 | `grep -c -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml` | `0` (before `0`) | OK |
| 20 | `ls ops/com.cobalt.cos.plist` | listed | OK |
| 21 | DEPLOY PROOF marker 1 and 2 are satisfiable | T2 says the new comment spells `enabled: false` nowhere (→ 0); T1 puts the string on exactly the two `value:` lines (→ 2); marker lines in `grep -c -F "…" <path>` form, `after 0` green on grep exit 1 per round 1 check 17 | OK |
| 22 | suites vs `BUILD-HUB.md` allowlist | `uv run pytest -q -p no:cacheprovider …` form; `test_cos_probes.py` now named; `\|` grep removed from P1 | OK |
| 23 | RESTARTS (X5) from `tunables.yaml:` readers aset, radar, cos (`jobs.yaml:69,200,221`); `jobs.yaml` in no `reads:`; `probes.py`/`runner.py` reach radar via `cli.py:71`; cos not loaded → hub skips | `aset radar` matches header; builder's `cobalt jobs restarts` line is the record | OK |
| 24 | X2/X3 re-derived from code | cos enabled + unloaded + owed: sweep `watchdog.py:437-449` OWED, K18 `checks.py:448-451` PASS, `probes.cos`/`probes.hitl` unknown-green via P1. Control (owed empty): sweep RED, K18 FAIL (`:444-447`), both probes RED/raise — the desk entry must stay until 929 | OK |
| 25 | migration, K5 class, RED-first for T1/T2/P1 | none; K5 on the brain's own label (round-1 notes 4, 6 non-defects); each row names its RED on BASE | OK |

## ISSUES

1. NOTE · the new tests' two BASE-RED claims for P1 rest on code read, not on a run (nothing executed on this seat); the builder's red-first run is the record.
2. NOTE · working tree carries an uncommitted `configs/cobalt/rules.yaml` change; not an anchor of this card, not touched by it.
3. Blocks the card's own build: nothing.

PREFLIGHT DONE · card: cos-tunables · checks: 25 · fails: 0 · ready: YES
