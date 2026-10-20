# Preflight — card 918 cos-probe-fr2 (read-only), 2026-10-20 12:37 EDT (`date`)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -c -F "«FILL" <918 card>` | `0`; `authorize.sh` PLACEHOLDER row: nothing | OK |
| 2 | header read whole | JOB `cos-probe-fr2`, BRANCH `ops/cos-probe-fr2`, WORKTREE `cos-probe-fr2`, REPORT `/Users/cobalt/cobalt-wt/cos-probe-fr2/docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md`, BAND `HIGH`, `CLASS: K2`, `TIP:` empty, BASE `56abaea2` | OK |
| 3 | `git merge-base --is-ancestor 56abaea2 main` · `git diff --stat 56abaea2 main -- src tests configs ops` | exit 0 · nothing (main is `27c35e37`, ahead by desk docs commits only) | OK |
| 4 | `git diff --stat -- <card>` · `git log -1 -- <card>` · `authorize.sh build <card>` | nothing · `b6555124` · last line `AUTHORIZED` (card committed, unchanged) | OK |
| 5 | `probe.py` cites against main (`:130-137`, `:140-145`, `:166-176`, `:170-172`, `:176`, `:179-183`, `:246`, `:293-300`, `:298`, `:308-336`, `:317-322`, `:340`, `:354`, `:375`, `:413`, `:422`, `:437-461`, `:451-454`) | each found at the cited line by content; the canary cite `:311-313` holds (nonce `:311`, canary `:312-313`) | OK |
| 6 | `session.py` cites (`:54`, `:93-95`, `:105-106`, `:108`, `:118-127`, `:146` pgrep) | `ALLOWED_ENV` `:54`; `child_env` `:93-95`; `setting_sources` `:105`; `strict_mcp_config` `:106`; `"env": child_env()` `:108`; `_scrubbed_environ` `:118-127`; `pgrep` `:146` | OK |
| 7 | `test_cos_probe.py` cites (`:120`, `:143-149`, `:197-200`, `:288`, `:322`, `:412`, `:416`, `:481`) | `auth_home` `:120`; auth stub `:147-149` (stdout `constructed auth output`); `_start_planted` `:197`; `:288`, `:322`, `:412`, `:481` are the named tests | OK |
| 8 | `grep -c -F "under the scratch HOME" src/cobalt/cos/probe.py` | `1` = card `before 1` | OK |
| 9 | `grep -c -F ".claude.json" src/cobalt/cos/probe.py` | `2` (`:12` docstring, `:298` code) = card `before 2` | OK |
| 10 | `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" tests/cobalt/test_cos_probe.py` | `0` = card `before 0` | OK |
| 11 | `grep -c -F "## 2026-10-20 — cos-probe-fr2" "docs/40 - DevDocs/cobalt/cos/README.md"` | `0` = card `before 0`; last section is `## 2026-10-20 — cos-probe-fr1 (check)` (`:49`), so D0 appends | OK |
| 12 | the four `grep -c -F` proof lines against `ops/desk/deploy-smoke.sh:10-22,122-131` | form `grep -c -F "<fixed string>" <absolute path>`, no `$`, backtick or backslash in a pattern; the README path is quoted; before/after present | OK |
| 13 | the `cos probe offline · uv run pytest …` proof line against `deploy-smoke.sh` `shape()` (`:114-168`: `ls`, `grep -c -F`, `curl`, `db query` only) | `uv run pytest` is not a mapped shape (RED `no mapped shape`). Card 877 carried the same line; R2165 (`cto-2026-10-20.md:33`) records "pytest smoke line removed" at deploy. The suite is run in the build's own steps | FAIL (NOTE: the desk drops it at the deploy card; does not block the build) |
| 14 | builder commands vs `BUILD-HUB.md:14`, `:16` | card names `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` (`uv run pytest *`), `uv run cobalt jobs restarts <BASE>..HEAD`, Edit / Write. No `git mv`, `rm`, `mv` or `cp` of a tracked file; the card says "Write and Edit only" | OK |
| 15 | RESTARTS: `jobs.yaml:193,203` · `cli.py:87,575` · `cos/cli.py:23-24` · `restarts.py:178,216-220,225-228,245-246` | radar `imports: [cobalt.cli]`; `cli.py:87` imports `cobalt.cos.cli`; `cos/cli.py` `_probe` imports `.probe`; `com.cobalt.cos` `imports: [cobalt.cos.run]` (`:226`). `probe.py` M → radar by static import reach; the test file → no resident; README → DOCS. Header `RESTARTS: com.cobalt.radar` agrees. No new path, so no `jobs.yaml` edit | OK |
| 16 | migration | card: `Migrations: none`; no `migrations/` row, no DB row | OK |
| 17 | RED test first | H1 names two REDs on BASE (`under the scratch HOME`; `rig.calls == [["claude","auth","status"]]`). BASE confirmed: `probe.py:181` sets `HOME` to the scratch home and `:454` prints the old clause, so both go red. H2's rewrite is RED on BASE (factory env `HOME` is the scratch home). H3's new test is RED on BASE (clause ends `scratch HOME`). H4 is a control (GREEN on BASE) with a Edit mutation, as `BUILD-HUB.md:16` allows. ORDER puts red before green | OK |
| 18 | no credential read; writes only in the scratch cwd | H4 bars any open under the real HOME; `grep -c -F ".claude.json"` goes `2` → `0`; `security` never an argv; `AUTH_ARGV` stays `claude auth status`; the only subprocesses stay `claude auth status` and `ps`. The H4 control wraps `builtins.open`, `io.open` and `os.open`, and its mutation (`_plant` reads `Path.home()/".claude.json"`) must go red | OK |
| 19 | X-item semantics and OK rules kept | `## NOT IN THIS JOB` fences `probe.py:308-427`, the seven `PROBE_ITEMS`, the one-line stdout shape, X17 `sonnet >= opus`, X14 `cos.max_turns`. X11's OK rule is unchanged. X2 / X10's written-file check changes only by diffing the cwd before / after, so the plant is the one ignored entry | OK |
| 20 | CHECK ASKS cover the real-HOME write bound | X1 (any write outside the `cos-probe-` dir; CLI state under the real HOME stated and bounded: one cwd per run, ≤67 sessions: 1+1+1+1+3+20+40 = 67), X2 (no credential read, grep `0`, mutation red), X3 (auth first, argv, quote carries two keys), X4, X5, X6 | OK |
| 21 | RULINGS `2026-10-18 R1863` | `cto-2026-10-18.md:90` `HIS RULING · APPROVED`; `authorize.sh`: committed (`11563e82`) and at HEAD. R2177 (the design) is a DESK RECORD and is not in RULINGS | OK |
| 22 | reports the card READs (`cos-gate-run-2026-10-20.md:10-17`, `:72`; `cos-probe-fr1-check-2026-10-20.md:121,123,189-203`; `draft-cos-gate-rerun-2026-10-20.md:12`; `F20-FINAL-2026-10-11.md:84,91`; `cto-2026-10-20.md:21,22`; the drafter report) | each exists and says what the card quotes (six `FAIL auth … under the scratch HOME`; `"loggedIn": true` at `:72`; G2 HELD `:121`; G4 UNSETTLED `:123`, OPEN `:192`; X17 0/20 at `:12`; X11 `:84`; X2 / X10 `:91`). The card cites R2176 / R2177 as `:21` / `:20`; the rows sit at `:22` / `:21` | OK (off by one) |
| 23 | `ls /Users/cobalt/cobalt-wt/cos-probe-fr2` | `No such file or directory`: a fresh worktree, as the card's `## RECORDS` says | OK |
| 24 | card committed, empty diff against HEAD | `git diff HEAD --stat -- <card>` → nothing; committed at `b6555124` | OK |
| 25 | what blocks the card's own build | nothing found | OK |

## ISSUES
- NOTE (#13): the `uv run pytest` DEPLOY PROOF line is unmapped by `deploy-smoke.sh`. The desk removes it at the deploy card (R2165 precedent); no change to the card needed for the build.
- NOTE (H2): `probe.py:310` (`home, work = root / "home", …`) and `:359` (`_child_env_names(pid, root / "home" / "work")`) also name `home/work`, but the card cites only `:246` and `:451-452`. Once `_scratch` stops making `home/`, a missed `:359` makes X12's `ps` run in a missing cwd. The builder finds it by content (E3), and `test_auth_and_ps_are_spawned_with_cwd_inside_scratch` (`:481`) pins X12.
- NOTE (H2): the plant moves from user config (`F20-FINAL:84`, `:91` say "user config") to a project-scope `<cwd>/.mcp.json` (card ASK DESK item 1, default taken). X11 then proves "no tool from a project `.mcp.json`", and user-config exclusion rests on the init list alone. The card says this.
- NOTE (stale docs): `src/cobalt/cos/cli.py:8` and `:37` still say "scratch HOME" / "scratch CoS session". The file is fenced (`## NOT IN THIS JOB`), so it stays stale unless a `## DECISIONS` item moves it.
- NOTE (cites): the card puts R2176 / R2177 at `cto-2026-10-20.md:20`, `:21`; they are at `:21`, `:22`. Cosmetic.
- NOTE (process): `authorize.sh build <card>` was run by this seat (read-only). It sits outside this seat's `--allowedTools`, so the harness admitted it under auto mode.
- NOTE (X6 DONE test): X17 is `0/20` on both counts as no pass (`draft-cos-gate-rerun-2026-10-20.md:12`).

PREFLIGHT DONE · card: cos-probe-fr2 · checks: 25 · fails: 1 · ready: YES
