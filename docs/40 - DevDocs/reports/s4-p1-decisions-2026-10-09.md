# S4-P1 build `d5bef4f9` · brain decisions · 2026-10-09

Build report: `/Users/cobalt/cobalt-wt/s4-p1-1009/docs/40 - DevDocs/reports/s4-p1-build-2026-10-09.md` (tip `da8a84dd`). Desk request R771.

Three items hold as built: P-1, M-1 and S-1 in part. W-1 and the rest of S-1 are fixed now by the kept builder, inside `tests/cobalt/test_strike_measure.py` and the test file that pins `runner.py`. Nothing goes to Dejan.

## W-1: neither (a) nor (b). FIX NOW by the kept builder
- I read the code. `test_strike_measure.py:188` skips on `Path("data/.cobalt_vault").exists()`, a path relative to the cwd. `resolve_token` (`archiver/collector.py:78`) calls `FinvizApiClient._resolve_vault_credentials` (`finviz_api.py:181`). That method unlocks `VaultManager` (`security/vault.py:19`, default `vault_path="data/.cobalt_vault"`) with `COBALT_MASTER_KEY` from the environment.
- (b) does not work. Every gate runs in a worktree, so the deploy gate would hit the same skip and go red again. It would also need `COBALT_MASTER_KEY` inside the gate, and secrets stay out of the gate (L41, L76, R686).
- (a) does not work either. It widens his R438 set for a test that can never run in any gate, so (f) would be a dead test.
- The fix is that the property (f) pins, "the real token path opens no database", does not need the real secret. The test runs the real `resolve_token` code against a throwaway vault. It does `monkeypatch.chdir(tmp_path)`, creates `data/.cobalt_vault` with `VaultManager().set_secret(<throwaway key>, "finviz.com::api_token", "ZZTOKEN")`, sets `COBALT_MASTER_KEY` to the throwaway key with `monkeypatch.setenv`, refuses `psycopg.connect` and `AsyncConnection.connect` as now, and asserts `token == "ZZTOKEN"` and `called == []`. The `skipif` is removed. If the config's debug `vault.master_key` can override the env, the test neutralizes that too.
- Red proof: a mutation that makes `resolve_token` call `psycopg.connect` turns the test red.
- Then W reruns: touched tests plus the deploy gate. There is no re-check (L75).

## S-1: split
- **FIX NOW:** `measure.command` (exit 2 / exit 1 wrapper) and `runner.make_strike_loop` are the code production runs. Each gets a pin with fakes and no real resource. For `measure.command`, monkeypatch `run_measure` to return each verdict class and assert the exit code. For `make_strike_loop`, use a fake detector and assert that one tick calls it and that `should_keep_running` False stops the loop. A check cannot close these, because tests a check writes are removed (CHECK-HUB `## 4`).
- **KEEP, left for the check to read:** `detector.build_detector` and `read_plan` open the real store and the real notes. Pinning them would mean a real resource in the gate.

## P-1: KEEP as committed
The edits to `test_setups_d1.py` and `test_setups_registries.py` add the four new tunables rows to the pins' added-row list. This is the R95 precedent `8b931ce5` ("as every added row"), the same feature's small fix (L75).

## M-1: KEEP as built
`NOT MET — <WINDOW> GET failed (<status>: <error>)` for a 500 or a parse error is right. It does not count a server or parse fault as THROTTLED, so the Charter's throttle verdict stays honest.

## CONTINUE for the desk to send to `d5bef4f9`
`CONTINUE: W. The real token path's DB-free property needs no real secret: run the real resolve_token against a throwaway vault in tmp_path (chdir, VaultManager().set_secret with a throwaway key, COBALT_MASTER_KEY set by monkeypatch, psycopg connects refused), drop the skipif, prove red by mutation; pin measure.command's exit codes and runner.make_strike_loop with fakes (S-1); P-1 and M-1 stand as built; build_detector and read_plan are left for the check; then rerun the touched tests and the deploy gate, and CLOSE.`

## FOR THE CHECK
`FOR THE CHECK: S4-P1 brain 10-09 — W-1 fixed in-build: (f) runs the real resolve_token on a tmp_path throwaway vault, no skip, no secret, no ALLOWED SKIPS widening; S-1 measure.command exit codes and make_strike_loop pinned with fakes, build_detector and read_plan read by the check; P-1 KEEP (R95 8b931ce5); M-1 KEEP (non-throttle failure is NOT MET with status).`
