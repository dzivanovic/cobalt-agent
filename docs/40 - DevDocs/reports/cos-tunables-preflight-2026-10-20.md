# cos-tunables preflight · card 933 · 2026-10-20

Card `prompts/2026-10-20/933-cos-tunables-card.md`, read whole. Every code anchor read in the working tree after `git diff main --stat` over those paths printed nothing (tree = `main` = `09c4be0e`). BASE `bd7bc0c9` trails main by desk commits only (allowed).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>` and `git log --oneline -3 -- <card>` | empty diff; committed in `09c4be0e` | OK |
| 2 | header names and values vs `prompts/CARD.md` (JOB, LADDER, BRANCH, WORKTREE, BASE, TIP empty, REPORT, CHECK REPORT, HOUSE B, BAND MID for 3 rows, RESTARTS, CLASS, INSTALL) | all present and well-formed; `LADDER` R2201 is a DESK RECORD row at `reports/cto-2026-10-20.md:25` | OK |
| 3 | header `RULINGS: 2026-10-20 brain 9b07db5a (L79)` vs `ops/desk/authorize.sh:142-163` (`rulings`) and `:205-210` | tokens `brain`, `9b07db5a`, `(L79)` are not `<date> R<n>`: `unreadable token 'brain'` → `FAILED: authorization mismatch`. R2201/R2205 are DESK RECORD rows, not `HIS RULING` + `APPROVED` rows, so no `<date> R<n>` can prove them. `none` is accepted (`:207`) | FAIL |
| 4 | `tunables.yaml` rows: `grep -n` of `key:`/`value:` on main | `cos.poll_interval_s` key `:1008`, value `:1009`, row ends `:1015`; `hitl.request_ttl_min` `:1026`/`:1027`/`:1033`; both `value: null`, `status: proposed`; `cos.session_rotate_at` `:1017`, `hitl.page_base_url` `:1038` null; `cos.max_turns` 30 `:989-994` proposed | OK |
| 5 | `session.py` anchors | `POLL_KEY :51`, `tunable_int :76`, null raise `:81-82`, positive-int rule `:83-84` | OK |
| 6 | `run.py` / `actions.py` anchors | `run.py:44` `refuse_if_agent_alive`, `:95` import, `:99` `poll_s = tunable_int(POLL_KEY)`; `actions.py:33`, `:62-63`, `:66` | OK |
| 7 | `jobs.yaml` anchors | `label: com.cobalt.cos :206`, `enabled: false :214`, comment `:207-213`, `:215-216` ("no value yet"), `timeout_s: 1200 :217`; 1200 > 900 + 10 holds | OK |
| 8 | `watchdog.py` / `checks.py` anchors | disabled skip `:387-396`; unloaded → `bootstrap_owed()` `:437`, `in owed` `:441-446`; K18 `:428-438`, FAIL `:444-447`, PASS+OWED `:448-451`; `bootstrap_owed` `:63` (raises `BootstrapOwedError` on a bad file) | OK |
| 9 | `probes.py` / `runner.py` anchors | `cos :135`, no-heartbeat RED `:154-156`, `hitl :167`, `probe_counts :175-179`; `runner.py:148-149` comment | OK |
| 10 | `test_cos_offline.py` anchors | `test_each_cos_tunable_is_read_loud :270-284`, `test_the_shipped_cos_rows :287-294`, `value is None` `:294`, `:291-292` stand | OK |
| 11 | `test_cos_registry.py` anchors | docstring `:1-6`, fallback `:13-16`, test `:21`, `enabled is False :28`, invariant `:29-32` | OK |
| 12 | `test_smoke.py:1578-1603` | `_Spec`, `_k18` helper (owed file in `tmp_path`, `watchdog.BOOTSTRAP_OWED_PATH` patched) as the card describes | OK |
| 13 | rows vs brain rulings (`cos-bootstrap-decisions-2026-10-20.md` item 5, `## ORDER`) | T2 is item 5. T1 is `## ORDER` "plus his two values", which the card carries as DEFAULTs (R2201, `cto-2026-10-20.md:25`). P1 is not in the brain's ruling; it rests on the desk's DESK RECORD R2205 (`:21`: "933 keeps P1"). No row goes past what those two allow | OK |
| 14 | the two pins become invariants (L69, `LAWS.md:363`) | card's T1 invariant (`int`, not `bool`, `> 0`) and T2 invariant (`if spec.enabled: plist is_file`) read no value. But a third pin is missed (check 15) | OK |
| 15 | `grep -n probes.cos tests` → `tests/cobalt/test_cos_probes.py:37-42` `test_disabled_row_is_unknown` | calls `probes.cos(NOW)` / `probes.hitl(NOW)` with the REAL registry and asserts `"enabled: false"` in `detail`. After T2 the real row is enabled: the call takes the enabled path, builds the real `JobStore()`/`HitlStore()` (or, with the real owed file present, returns the P1 OWED text without `enabled: false`). Either way it goes RED. It pins the flag (L69 / X4), is in no row, and is not in the card's suite list (`test_heartbeat*.py` does not match it). Docstring `:4` also says `enabled: false` | FAIL |
| 16 | every builder command vs `BUILD-HUB.md:14,16` | `uv run pytest -q -p no:cacheprovider …` ← `Bash(uv run pytest *)`; `uv run cobalt jobs restarts` ← listed; `git`, `ls`, `grep`, `wc`, `date` listed. `grep -rln "…\|…"` in P1 uses `\|`, which `:26` forbids (moot: the file is `test_cos_probes.py`) | OK (NOTE 3) |
| 17 | `## DEPLOY PROOF` forms vs `ops/desk/deploy-smoke.sh` | both marker lines are `` `grep -c -F "…" <path>` · before · after `` (`:122`, `:246-256`); `value_is` reads the last output line, so `after 0` is green though grep exits 1 (`:215-216`). smoke reads: `ls <path>` + `exit 0, listed` (`:342`); `curl … 5010/` + ``exit 0, `200` `` (`:12`, `:343`) | OK |
| 18 | `befores` re-proved now | `grep -c -F "enabled: false" jobs.yaml` → `1`; `grep -c -F "DEFAULT (brain; his word may change it)" tunables.yaml` → `0`; `ls ops/com.cobalt.cos.plist` → listed | OK |
| 19 | RESTARTS homes (`restarts.py:196-224`) | `tunables.yaml` → `registry.readers_of` = aset, radar, cos (cos not loaded → skipped by hub); `jobs.yaml` → `:223` "registry; register, no restart"; `probes.py`, `runner.py` → static import reach (`cli.py:71` imports `heartbeat.cli`) → radar; tests, docs → none. Header `aset radar` matches. Not run (`uv` not on this seat's line); the builder's `cobalt jobs restarts` line is the record | OK |
| 20 | migration | none; no `db_migrations` path in any row | OK |
| 21 | RED first | T1 red on `value is None`; T2 red on a disabled row (no OWED clause); P1 red on `ok` False / raise | OK |
| 22 | K5 class (`LAWS.md:406-408`) | K5 = allow/deny strings, guard rules, launcher refusals, hub lines serving K1–K4. Card edits two product tunables, a registry flag and `src/cobalt/heartbeat/probes.py`; it serves K4 (the cos deploy). The brain named it "the K5 tunables card" (`## ORDER`), so it is taken as ruled | OK (NOTE 4) |

## ISSUES

1. FAIL (check 3) · `RULINGS: 2026-10-20 brain 9b07db5a (L79)` is not a `<date> R<n>` list. `authorize.sh build` stops with `unreadable token 'brain'`, so the build ends `FAILED: authorization mismatch`. Fix: `RULINGS: none` (R2201 and R2205 stay in `LADDER` and `## RECORDS`), or a `HIS RULING`/`APPROVED` row of his.
2. FAIL (check 15) · `tests/cobalt/test_cos_probes.py::test_disabled_row_is_unknown` pins `enabled: false` through the real registry and goes RED once T2 lands. Add it to P1's `files` and `red first`: rewrite it as an invariant (pass `enabled=` explicitly, or read `trader_settings`-free `load_job_registry().spec(COS_LABEL).enabled` and assert the matching `detail`), fix the module docstring `:4`, and add `test_cos_probes.py` to the named suites.
3. NOTE (check 16) · P1's `grep -rln "probes.cos\|probe_mod.cos" tests` carries `\|`; name `tests/cobalt/test_cos_probes.py` outright.
4. NOTE (check 22) · K5 reads "harness upkeep"; T1/T2/P1 are product config and `src/`. It stands on the brain's own label; the check should confirm it stays inside what `ORDER` names.
5. NOTE · After P1, `test_dead_session_is_red` (`test_cos_probes.py:26-34`) and `test_pending_past_ttl_and_failed_execution_are_red` (`:45-56`) call `enabled=True` and now read the REAL `data/deploy/bootstrap-owed.json`. It lists cos in `/Users/cobalt/cobalt` (OWED-green → asserts fail) and not in a worktree. Both tests must patch `cobalt.jobs.watchdog.bootstrap_owed` to `frozenset()`.
6. NOTE · The T2 CONTROL (owed file empty → FAIL) is RED on BASE too (a disabled row never fails K18); it is green only after T2. The card says "same test", so the RED-on-BASE line covers it.
7. NOTE · DEPLOY PROOF marker 1 needs zero `enabled: false` lines in `jobs.yaml` after the build: the re-worded comment `:207-216` must not spell that string. Marker 2 needs exactly 2 `DEFAULT (brain; his word may change it)` lines.
8. Blocks the card's own build: issues 1 and 2.

PREFLIGHT DONE · card: cos-tunables · checks: 22 · fails: 2 · ready: NO
