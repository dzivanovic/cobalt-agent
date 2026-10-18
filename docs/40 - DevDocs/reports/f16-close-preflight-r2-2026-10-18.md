# Card 790 `f16-close-1018` — preflight round 2 (read-only), 2026-10-18

Card `prompts/2026-10-18/790-f16-close-card.md`, BASE `e7ef198a`, `main` is `3deeb480`. Read-only: no test was run (no `uv` or `pytest` on this seat's allowlist), so RED/CONTROL are derived from the code.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --name-only e7ef198a main` | 22 paths, all under `docs/40 - DevDocs/` except `tests/ops/test_hub_deferred_1018.py`; no `src/` or `configs/` path, so every anchor holds at BASE and at main | OK |
| 2 | R1 FAIL 26: RECORDS RESTARTS line | names the class home of BOTH `src/cobalt/cli.py` and `src/cobalt/taxonomy/loader.py`: static import reach to `com.cobalt.radar`. `grep -n` jobs.yaml: `:193` label `com.cobalt.radar`, `:203` `imports: [cobalt.cli]`; `cli.py:146` imports `load_tunables`; `loader.py:76` `def load_tunables` | OK |
| 3 | R1 NOTE 1: `grep -n` cli.py + Read `:314-337` | Jobs (F17) print `:317-322`, `if disabled:` `:328`, last NOT LOADED line `:333`, blank `:334`, `# CROSS-CHECK 1` `:335`, `Placement…tree clean.` print `:500`. The row says insert before CROSS-CHECK 1, NOT inside `if disabled:`; RECORDS gives `:334` | OK |
| 4 | R1 NOTE 2: header `RULINGS: none`; `grep -n F16 cto-2026-10-18.md`; `grep -n F16` Charter and ladder | F16 hits in the CTO report are R1934/R1936/R1937/R1938/R1939 (desk records) and OWED/STATE lines, none a ruling of his; ladder `:70`, `:1162` and Charter `:177` are scope. `none` holds | OK |
| 5 | R1 NOTE 3: `grep -c "passed\|failed"` card | `1`: the line is the hub gate `0 failed`, `0 errors`; no pytest count in the red-first cell | OK |
| 6 | Header values: JOB `f16-close-1018`, LADDER, BRANCH `s5/f16-close-1018`, WORKTREE `f16-close-1018`, BASE `e7ef198a`, TIP/CHECK REPORT/HOUSE B empty, REPORT under the worktree, BAND `MID`; `ls /Users/cobalt/cobalt-wt` | well-formed; no `f16-close-1018` dir in `cobalt-wt` (no collision) | OK |
| 7 | `file:line` proofs: tunables.yaml `prefill.refresh_window` `:1084`, `refresh_interval_min` `:1096`; `daily.py:682` `REFRESH_GETS = 3`, `:791` `headroom_rpm <= 0`; `route.py:80` `MIN_N = 30`, `:389` `<= 2` / `<= 6`; `checkin-timer.sh:54` `PING_MAX_AGE_MIN=30`; `stop-guard.py:532` `<= 160` | all match the card | OK |
| 8 | `tunables.py` and loader anchors: `grep -n` | `TunableRow` `:92`, `extra="forbid"` `:93`, `consumers: list[str] = Field(default_factory=list)` `:103`, registry `extra="forbid"` `:118`; `loader.py:76` `load_tunables`, `TaxonomyConfigError` `:58` | OK |
| 9 | `grep -c "^  - key:"` / `grep -c "^    consumers:"` tunables.yaml | `94` / `94`, matches RECORDS and the C1 CONTROL | OK |
| 10 | F23/F4 loaders: `grep -n` playbook/config.py, prefill/config.py, prefill.yaml | `PlaybookConfigError` `:22`, `extra="forbid", strict=True` `:27`, `load_playbook_config` `:43`; `PrefillConfigError` `:33`, `VIX`/`BTC` in `NO_SOURCE_FIELDS` `:128`, `load_daily_refresh_config` `:198`; `daily_refresh:` block `prefill.yaml:24-26` with `VIX: manual` | OK |
| 11 | X2 pptx seam: `grep -rn "import pptx\|from pptx" src`; `grep -n "^import\|^from" playbook/cli.py` | `pptx` only in `playbook/deck.py:26-27`; `playbook/cli.py` imports `.config` only; V1 imports `cobalt.playbook.config` only, so `pptx` stays unloaded | OK |
| 12 | RED V1/V2/C1 (derived): V1/V2 — BASE `_cmd_validate` never loads either file (no `playbook`/`daily_refresh` in it), so `DID NOT RAISE`; C1 — `consumers` defaults to `[]` (`tunables.py:103`) and `loader.py` checks nothing more, so `DID NOT RAISE`; CONTROLs green on the real files (94/94) | consistent; not executed | OK |
| 13 | Test form: `grep -n` `tests/cobalt/test_validate_no_db.py`; `ls tests/cobalt/test_f16_close_1018.py` | autouse `_no_db_settings` `:27` removes Postgres env and stubs `cli.taxonomy_validate.main`; `_cmd_validate(argparse.Namespace(no_db=True))`; the new file does not exist yet (ONE new file, all bad files under `tmp_path`) | OK |
| 14 | L69: card text | tests build files under `tmp_path`; `no_db=True` skips the `trader_settings` reads; no test asserts a value of the real files | OK |
| 15 | C1 other homes: `grep -n consumers` `test_taxonomy_store.py`, `test_trade_defs.py` | no `consumers` in either: they build rows without one, as the card says; those rows do not go through `load_tunables` | OK |
| 16 | R411/R412: command strings the card adds | none on a launch line; `uv run pytest …`, `uv run cobalt validate --no-db` and `COBALT_ENV=production uv run cobalt validate --no-db` are report/smoke content | OK |
| 17 | DEPLOY PROOF "before" values: `grep -c -F "Playbook (F23): "` cli.py; `grep -c -F "with no consumer (F16)"` loader.py | `0` and `0`, as the card's "before" | OK |
| 18 | Card committed: `git diff HEAD --stat -- <card>`; `git diff HEAD --stat -- src configs tests` | both empty | OK |

## ISSUES

- NOTE 1 · RED/CONTROL (check 12) are derived by reading, not run; the check's PASS 1 runs the card's own pytest command on BASE (file copied onto BASE) and after.
- NOTE 2 · Build blocker: none in the card. The build takes the `cobalt_dev` lock (src change) and queues behind any deploy holding it (777 stop-guard-work was DEPLOYED at 19:55, so none is known to hold it). The desk sequences it after the F20 chain.
- NOTE 3 · Deploy blocker: none in the card. The change reaches resident `com.cobalt.radar` through `cobalt.cli` and `loader.py`, so `cobalt jobs restarts` will list a restart; the deploy card's `RESTARTS:` comes from the builder's line. F16 closes for BASE only; the repeat sweep after F5, F20, F21 stays owed.

PREFLIGHT DONE · card: f16-close-1018 · checks: 18 · fails: 0 · ready: YES
