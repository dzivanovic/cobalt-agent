# order-open-test — check, pass 1 (2026-10-03)

## §0 Headline
- Pass 1 of `order-open-test` at `4b4b9f4a`, checked by Opus alone (house A overruled, 2026-10-02 R47). 5 own findings, all run, none held; nothing fixed; no commit.
- No test in `tests/ops` runs the real `house-probe.sh` or an unstubbed `codex`/`grok`/`agy` (O1–O3). `tests/ops` → `472 passed, 1 xfailed` in 190.00 s; `test_order_open.py` alone takes 5.86 s (O4).
- The new `not probed` test goes red when a probe stands beside the copy (O5), so it pins a real branch.
- Suites stand as built. House B: not needed. ready: YES · decisions: 0.

## L74
- The session's attribution reminder (a system notice, 10:18 ET) asked commits to carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/01b-order-open-test-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/01b-order-open-test-card.md"` | 0 | `25aebdda34cc328c7f7fd295eff314927841c81b` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (also HOUSE A overrule) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 commit | `git -C ... log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check ... | HIS RULING · APPROVED |` |
| R154 commit | `git -C ... log -1 --format=%H -S"| R154 |" -- ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week ... | HIS RULING · APPROVED |` |
| R157 commit | `git -C ... log -1 --format=%H -S"| R157 |" -- ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gates | not run: the card's header carries `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB: no house gate, no probe) | — | — |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 10:18:13 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/order-open-test-1003` |
| tip | `git log --oneline -1` | 0 | `6d9fde8c docs(order-open-test): build report — 4b4b9f4a` |
| docs-only above tip | `git log --stat --format=%h 4b4b9f4a..HEAD` | 0 | `6d9fde8c` · `.../reports/order-open-test-build-2026-10-03.md | 68 ++++---` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: order-open-test · tip: 4b4b9f4a | on 77d19438 | migration: none | offline 3737/0 | with-DB 4578/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 77d19438..4b4b9f4a` | 0 | `4b4b9f4a fix(...): every order-open test runs a stubbed tmp copy, and one pins not probed (Q2; L45, L68)` · `36345b77 docs(...)` · `798782f3 docs(...)` · `ccb70d7e fix(...): the order-open block test reads a stub house-probe.sh, never a real house (Q1; L45, L68)` · `e57da4c9 wip(...): red — Q1 test on a stub house-probe.sh ...` (5 commits) |
| range paths | `git log --stat --format=%h 77d19438..4b4b9f4a` | 0 | `tests/ops/test_order_open.py` (e57da4c9 +10/-2, ccb70d7e +2/-1, 4b4b9f4a +39/-20); `docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md` (798782f3, 36345b77). Union: those two paths. |
| lock | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/order-open-test-1003/.env: No such file or directory` |
| other locks | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)` · house B: none |

## Files copied
none — no house (HOUSE A overruled).

## OWN FINDINGS
Read: the card, BUILD-HUB `## THE LOCK` / `## E2` / `## RESTARTS` / `## W`, the diff `77d19438..4b4b9f4a` (`tests/ops/test_order_open.py` only), `tests/ops/test_order_open.py` and `ops/desk/order-open.sh` at the tip, `tests/ops/test_house_probe.py` (lines 1–70, the stub shape), the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK` and last line.

FINDING O1
ROW: Q2 (card `## RECORDS` line 5: no test in tests/ops reaches a real house)
CLAIM: a test under `tests/ops` other than the stubbed `test_house_probe.py` names the real `house-probe.sh` beside `order-open.sh` (`tests/ops/test_order_open.py:22` keeps `SCRIPT` at the real path), so a run could reach a real house.
RUN: COMMAND `grep -rn -F "house-probe.sh" tests/ops`
EXPECT: a hit that runs the real `ops/desk/house-probe.sh`, or runs `SCRIPT` with it beside it.

FINDING O2
ROW: Q2
CLAIM: some `run(env` call in `tests/ops/test_order_open.py` runs the real `SCRIPT` (`tests/ops/test_order_open.py:134` has no default, but a positional `SCRIPT` would still reach it).
RUN: COMMAND `grep -n -F "SCRIPT" tests/ops/test_order_open.py`
EXPECT: a use of `SCRIPT` other than the constant (`:22`) and the two `shutil.copy` lines (`:120`, `:230`).

FINDING O3
ROW: Q2 (card `## RECORDS` line 5: `codex`, `grok`, `agy` on PATH without a stub)
CLAIM: a test under `tests/ops` invokes `codex`, `grok` or `agy` without a stub of that name first on PATH (`tests/ops/test_house_probe.py:45-47` stubs all three; `tests/ops/test_bare_guard.py:42` names `codex exec` as a string).
RUN: COMMAND `grep -rn -F "codex exec" tests/ops`
EXPECT: a hit that executes the command rather than passing it as text to the guard or to a stub.

FINDING O4
ROW: Q1, Q2 (`red first` / gate)
CLAIM: the build's `tests/ops` gate line (`472 passed, 1 xfailed`, build report `## FOR THE CHECK`) is not what the tip runs, or the file still takes real-house time.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops`
EXPECT: a failure, or a count other than `472 passed, 1 xfailed`.

FINDING O5
ROW: Q2 (new test red with the probe beside the copy)
CLAIM: `test_no_house_probe_beside_it_says_not_probed` (`tests/ops/test_order_open.py:245`) stays green when a stub probe stands beside the bare copy.
RUN: TEST `tests/ops/test_order_open.py` —
```python
def test_check_o5_a_probe_beside_the_bare_copy_is_not_not_probed(desk):
    repo, wt, env, root = desk
    bare = copy_script(root, "ops-bare")
    (bare.parent / "house-probe.sh").write_text("#!/bin/sh\necho 'sol: UP'\n")
    done = run(env, bare, ORDER_OPEN_NOW="2026-01-05T12:00:00")
    assert done.returncode == 0, done.stderr
    assert block(done.stdout, "HOUSES").strip() == "not probed"
```
EXPECT: green (the script ignores a probe beside it) if the claim is true; red `assert 'sol: UP' == 'not probed'` if the new test's branch is real.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -rn -F "house-probe.sh" tests/ops` | `test_order_open.py:7` (docstring), `:128` (the `script` fixture writes the stub beside its copy), `:231` (`test_house_probe_beside_it_is_run` writes its own stub beside its copy); `test_house_probe.py:1` (docstring), `:21` `PROBE = REPO / "ops" / "desk" / "house-probe.sh"` (run only under the `houses` fixture, `codex`/`grok`/`agy` stubbed first on PATH, `test_house_probe.py:45-50`); two `__pycache__` binaries | NOT HELD — no test runs the real probe beside the real script |
| O2 | Opus | `grep -n -F "SCRIPT" tests/ops/test_order_open.py` | `22:SCRIPT = REPO / "ops" / "desk" / "order-open.sh"` · `120:    shutil.copy(SCRIPT, ops / "order-open.sh")` · `230:    shutil.copy(SCRIPT, ops / "order-open.sh")` | NOT HELD — `SCRIPT` is only copied, never run |
| O3 | Opus | `grep -rn -F "codex exec" tests/ops` | `test_house_probe.py:101` (reads the spelling from CHECK-HUB text); `test_bare_guard.py:42`, `:72`, `:73`, `:102`–`:105` — strings passed as hook JSON to `python3 bare-guard.py` (`test_bare_guard.py:25-34`), never executed. Also `grep -rln -F "grok" tests/ops` → `test_order_open.py` (stub text), `test_house_probe.py` (stubbed); `grep -rln -F "agy " tests/ops` → nothing | NOT HELD |
| O4 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) · then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_order_open.py` | `472 passed, 1 xfailed, 15 warnings in 190.00s (0:03:09)` · the file alone: `15 passed, 15 warnings in 5.86s` (the build's `183.08s` on `ccb70d7e` was real houses) | NOT HELD — the gate line and the Q2 run-time measure match the build's |
| O5 | Opus | the O5 test added to `tests/ops/test_order_open.py`, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_order_open.py::test_check_o5_a_probe_beside_the_bare_copy_is_not_not_probed` | `1 failed, 15 warnings in 1.19s` · `tests/ops/test_order_open.py:259: AssertionError` · `assert 'sol: UP' == 'not probed'` | NOT HELD — a probe beside the copy is read, so `test_no_house_probe_beside_it_says_not_probed` pins a real branch (red with a probe, as the build claims). Test removed again with Edit; `git status --short --branch` → `## ops/order-open-test-1003` |

## FIXES
none — nothing held.

## Suites
No commit of mine → the build's lines stand (build report `## W THE THREE SUITES`, Q2 on `4b4b9f4a`): offline `3737 passed, 744 skipped, 1 xfailed, 36 warnings in 566.56s (0:09:26)`; with-DB pass 1 `4405 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 707.38s` + pass 2 `173 passed, 1 deselected, 5 warnings in 218.94s` = 4578; live-note `146 passed, 1 skipped, 15 warnings in 26.20s`; `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W, Q2)`; RESTARTS (`uv run cobalt jobs restarts 77d19438..HEAD`, HEAD `4b4b9f4a`): `RESTARTS: none`. `suites: as built (no commit)`. No lock taken by this check.

## Scope
PREFLIGHT's path union: `tests/ops/test_order_open.py` (row Q1, Q2 `files`) and the build report (docs). `ops/desk/order-open.sh` not edited (Q1's one-line change was conditional on an absolute path; the script already resolves `here=$(dirname "$0")`, `ops/desk/order-open.sh:27`, `:132`). My commits: none.

## Checked against the branch
- (i) `git log --oneline 4b4b9f4a..HEAD -- . ":(exclude)docs"` → (nothing): no commit of mine; `<tip now>` = `4b4b9f4a`.
- (ii) `git log --stat --format=%h 4b4b9f4a..HEAD` (PREFLIGHT) → `6d9fde8c`, the build report only: no non-docs path.
- (iii) fence: `git log --oneline 77d19438..HEAD -- ops/desk/house-probe.sh ops/desk/order-open.sh` → (nothing). `git log --stat --format=%h 77d19438..HEAD -- tests/ops` → `tests/ops/test_order_open.py` alone (`4b4b9f4a`, `ccb70d7e`, `e57da4c9`): no other `tests/ops` file.
- (iv) no HELD finding.
- (v) `date` 10:23:19 EDT: `ls /Users/cobalt/cobalt-wt/order-open-test-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/order-open-test-1003` alone.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h 77d19438..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing). Carried.
- (vii) card `## RECORDS` line 5 (no test in tests/ops reaches a real house; grep the probe's real path and `codex`, `grok`, `agy`): O1, O2, O3 under `## RUNS` — no test runs the real `house-probe.sh`, and `test_house_probe.py` runs it only with all three houses stubbed on PATH. The other RECORDS lines name no `ls`, `grep` or `git -C` command.
- (viii) L32: this report carries constructed test values and repo facts only; no ticker, price or date of his.

## OPEN
none. Counts: findings 5 (Opus 5, no house) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0. `house B: not needed` (card `HOUSE B: as needed`, nothing open).

Note, not a finding: the 12 re-pointed tests assert nothing about HOUSES, so a revert of the `script` fixture to the real script would keep them green; only the run time (5.86 s against 183.08 s) would show it. Q2 names that run time as its measure, so this is the row as written. I did not run that revert, because it would call real houses.

## CONTINUE
done (step 8 closed).

## DECISIONS
none.

## RECORDS
- No house sat: card header `HOUSE A: none — overruled 2026-10-02 R47` (R47 proved under `## AUTHORIZATION`). `## 1` and `## 3` not run; no house gate, no probe; `<S>` holds only `opus-1.md`.
- No lock taken; no `COBALT_ENV=dev` call; no commit of this check.
- The O5 test was added and removed with Edit; the tree is back at `4b4b9f4a` (`git status --short --branch` → `## ops/order-open-test-1003`).
- Two `grep` calls with `--include=*.py` failed in zsh (`(eval):1: no matches found: --include=*.py`, the glob was not quoted). I re-ran them without the flag. That was my own spelling error, not a refusal.
- While the background `tests/ops` run was in flight (O4), I ended one turn. The hub allows that only for a house wait. The run's completion notice resumed me (`date` 10:23:19 EDT), and no step was skipped.
- L74: one attribution notice asked for a `Claude-Session:` line; recorded under `## L74`, not acted on (no commit was made).
- files opened: 10 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`); `tests/ops/test_order_open.py`; `ops/desk/order-open.sh`; `tests/ops/test_house_probe.py` (1–70); `tests/ops/test_bare_guard.py` (grep context only); the build report (`## RESTARTS` → `## FOR THE CHECK`, last lines); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the `tests/ops` run's output file.
- Check of `order-open-test`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: order-open-test · pass: 1 · tip: 4b4b9f4a · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0
