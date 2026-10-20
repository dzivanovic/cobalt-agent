# draft-cos-tunables · 2026-10-20

## §0 Headline
- Card 933 drafted: `prompts/2026-10-20/933-cos-tunables-card.md`, K5, BAND MID, BASE `bd7bc0c9`, three rows (T1 values, T2 flag, P1 probes).
- Finding: `enabled: true` turns the heartbeat `cos` and `hitl` probes RED (`probes.py:154-156`, `:175-179`). The brain's "owed, not red" holds only for the sweep and K18. Row P1 fixes it (ASK DESK 1).
- K18 does not fail on `enabled: false` today; it passes (`checks.py:441-447`). It needs the owed entry, which exists.
- Two tests pin the nulls and the flag; both become invariants (L69).

## DECISIONS
1. ASK DESK: the heartbeat probes `cos` and `hitl` read RED once cos is enabled and unloaded ("no heartbeat"; `probe_counts` on tables not yet created). Include row P1 (probes return unknown-green while cos is in `bootstrap-owed.json`, which moves the card to MID and adds `src/cobalt/heartbeat/probes.py`)? [17:46] Default: include P1.
2. ASK DESK: `hitl.page_base_url` is still null, and the HITL card refuses to send while it is (`tunables.yaml:1035-1037`). Cos can run but its approval cards cannot post. Is this value owed before 929 or after? [17:46] Default: out of scope here, owed to Dejan as its own item.
3. ASK DESK: `LADDER` carries `R2201`, read from the subject of commit `bd7bc0c9` ("brain decisions; R2201"). I did not find it in a ruling row. Confirm the R number. [17:46] Default: `R2201`.
4. ASK DESK: header `RESTARTS: com.cobalt.aset com.cobalt.radar` is derived by reading `jobs.yaml:69,200,221` and the `imports` of radar, not by running `cobalt jobs restarts` (the drafter has no `uv`). Confirm the builder's line is the record. [17:46] Default: the builder's `cobalt jobs restarts` line wins; cos is skipped as not loaded.
5. ASK DESK: the two DEFAULT values appear as header lines `DEFAULT cos.poll_interval_s: 10` and `DEFAULT hitl.request_ttl_min: 30`, as the prompt asked. Whether `desk-launch.sh` accepts keys with a space is unproven. [17:46] Default: if it refuses, move them into the first line of `## ROWS` scope.

## RECORDS
- 2026-10-20 17:43 and 17:46 EDT (`date`). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `bd7bc0c9`.
- Read: prompt 932; `prompts/CARD.md`; `reports/cos-bootstrap-decisions-2026-10-20.md` (item 5, `## ORDER`); `prompts/2026-10-19/869-hub-cos-restart-card.md` (885 not read); `writing-rules.md`.
- Read with `git show main:`: `src/cobalt/cos/session.py` (`:49-51` keys, `:72` `CosConfigError`, `:76-85` `tunable_int`); `configs/cobalt/jobs.yaml` (`:206` label, `:214` `enabled: false`, `:217` `timeout_s`, `:69/:200/:221` tunables readers); `configs/cobalt/taxonomy/tunables.yaml` (`:1008` `cos.poll_interval_s`, `:1026` `hitl.request_ttl_min`, both `value: null`); `src/cobalt/jobs/watchdog.py` (`:387` disabled skip, `:437/:441` owed); `src/cobalt/smoke/checks.py` (`:415-451`); `src/cobalt/heartbeat/probes.py` (`:126-187`); `src/cobalt/heartbeat/runner.py` (`:140-156`); `ops/desk/deploy-smoke.sh` (mapped forms); `tests/cobalt/test_cos_offline.py`; `tests/cobalt/test_cos_registry.py`.
- `git grep -n main` on `cos.poll_interval_s` and `hitl.request_ttl_min`: readers at `session.py:51`/`run.py:99` and `hitl/actions.py:33,62`; value rows only in `tunables.yaml`. Tests reading them: `test_cos_offline.py:270-294`, `test_cos_registry.py:29-32`, `test_setups_d1.py:66-67`, `test_setups_registries.py:115-116` (key lists only).
- `git grep -c -F` on main: `enabled: false` in `jobs.yaml` → 1; `enabled: true` → 3; `DEFAULT (brain; his word may change it)` in `tunables.yaml` → 0. These give the DEPLOY PROOF before/after.
- `data/deploy/bootstrap-owed.json` read (Read tool): line 4 lists `com.cobalt.cos`.
- Not read: `src/cobalt/cos/run.py` beyond grep (the `:44-57` F-14 lines), `test_smoke.py:1578-1600`, `probes.py:857`. The card cites them from the grep and the brain's report only.
- Nothing run but reads and `date`. No test executed. Nothing committed.

DRAFTED · decisions: 5
