# Preflight round 2 of card 603 `jev-shadow-1015` (CHECK) — 2026-10-15

Read only. No keyed call, no key read, no git write. Anchors read in the worktree `/Users/cobalt/cobalt-wt/jev-shadow-1015`; its code equals the tip (`git diff --stat d0fdd674 f298a7bf` = the build report and its `.result` only).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <603 card>` | empty | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline -2 -- <603 card>` | `6e883218` (fix round) and `687f3a78`: committed | OK |
| 3 | `grep -n -F "FILL" <603 card>` | no output: no placeholder token | OK |
| 4 | `grep -n -E "^(JOB\|BASE\|TIP\|…):" <603 card>` | JOB, LADDER, BRANCH, WORKTREE, BASE `d601b1f6`, TIP `d0fdd674`, REPORT, CHECK REPORT, HOUSE B `as needed`, RULINGS: every CARD.md check field present (DB optional, left out) | OK |
| 5 | `git diff 687f3a78 6e883218 --stat -- <603 card>` | 5 insertions, 5 deletions: the fix round touched five rows only (X0c, X0d, X0e, P0, R2, as the drafter's report says) | OK |
| 6 | F1 fixed: card row X0c | four fixed-string greps, one per call: `write_text`, `.open(`, `mkdir`, `.write(`, no `\|` | OK |
| 7 | X0c greps run as the card types them (worktree cwd) | `write_text`: `route.py:690`, `cli.py:54`, `cli.py:105`. `.open(`: `trial.py:171`, `route.py:475`, `ledger.py:130`, `collector.py:276` (urllib opener, not a file). `mkdir`: `trial.py:170`, `route.py:474`, `route.py:689`, `ledger.py:123`, `cli.py:53`, `cli.py:104`. `.write(`: `trial.py:172`, `route.py:476`, `ledger.py:131` (and `route.py:437,447,463`, calls of `Router.write`). Every writer the card names appears; none is missing | OK |
| 8 | X0c anchors | `ledger.py:123-131` (mkdir, open, write) ✓ · `route.py:474-476` (mkdir, open, write) ✓ · `trial.py:170-172` ✓ · `cli.py:53-54`, `:104-105` ✓ · `route.py:689-690` ✓ · `route.py:745` `out_dir = … REPO_ROOT / REPORTS_DIR` ✓ | OK |
| 9 | X0c yaml quotes | `route.yaml:22` `spend_ledger: /Users/cobalt/.cobalt/classify/classify-spend.jsonl` · `:31` `routing_ledger: /Users/cobalt/.cobalt/classify/routing-ledger.jsonl` · `trial.yaml:46` the same `spend_ledger` · `trial.yaml:54` `results_dir: scratch` | OK |
| 10 | F2 fixed: X0d | throwaway pytest file under the worktree `scratch/`, run with `uv run pytest -q -rA -p no:cacheprovider --color=no <file>` (on the allow line), no `uv run python`; counts in Python; names `Router.body(router.qset, router.item(card))` | OK |
| 11 | X0d anchors | `route.py:703` is that call ✓ · `route.py:710-711` prints only bytes, tokens, projection, guard ✓ · `Router(OpenRouterClassifier)` at `route.py:414`, `body` at `collector.py:347`, `item` at `route.py:424`, `qset` at `:421` ✓ · `DROPPED_HEADERS` `route.py:77` holds the same five strings ✓ · `load_card` `route.py:354` ✓ | OK |
| 12 | F3 fixed: X0e | marked `ASK DESK`, names the off-list command, safe default is the pytest-file driver calling `cmd_route_read`, else `REFUSED, not needed` | OK |
| 13 | X0e anchors | `cmd_route_read` `route.py:739` ✓ · `load_route_config()` `:740` ✓ · `routing_ledger` read `:744` ✓ · parser `route-read` `:762` ✓ · `--out-dir` `:764` ✓ · `_batch` monkeypatch shape `test_jev_shadow_1015.py:741` (`monkeypatch.setattr(route, "load_route_config", lambda *a, **k: cfg)`) ✓ · helpers `_route_cfg` `:95`, `_classify_parser` `:197` exist | OK |
| 14 | N1 fixed: P0 | classify tree `f4e8de85 d0fdd674`; `cli.py` and `cli.md` `d601b1f6 d0fdd674`. Proof: `git diff --stat d601b1f6 d0fdd674 -- src/cobalt/cli.py "docs/40 - DevDocs/cobalt/cli.md"` → `cli.md` 11 insertions, `cli.py` 2 insertions: "+2 only" and the trial's hunk ✓ | OK |
| 15 | N4 fixed: R2 | row says run from `/Users/cobalt/cobalt-wt/jev-shadow-1015`, `uv run cobalt jobs restarts d601b1f6..<TIP>` (on the allow line), names the two `no_resident_reads` rows and the main-vs-worktree difference | OK |
| 16 | other anchors, unchanged rows | `collector.py` `:182` `except OverflowError:` · `:304` `Path(cfg.spend_ledger)` · `:307` `carried=` · `:594` `ledger.check(OVERRUN_FACTOR * projected_usd, calls=1)` (read in `git show feat/jev-shadow-1015:…collector.py`, all present; `_send` guard, check, key, transport in that order) · `route.yaml:26` `call_ceiling: 518` · `:28` `batch_wall_clock_s: 1470` (their source lines `:27`, `:29` name 147 cards) | OK |
| 17 | commands inside the allow line | Z0, X0b, X0c: `grep *`; P0, X0 cites: `git diff *`; X0a, X0d, X0e default: `uv run pytest *`; R2: `uv run cobalt jobs restarts *`; X0f: `sh /Users/cobalt/cobalt/ops/desk/*`. Off the line and marked `ASK DESK`: X0e CLI form, X2 `ls /Users/cobalt/.cobalt/classify` (R411, R412) | OK |
| 18 | `grep -n -E "uv run cobalt classify\|uv run python\|ls /Users/cobalt/.cobalt" <603 card>` | `uv run cobalt classify` appears at X0e (ASK DESK) and in `## DEPLOY PROOF` (the deploy's smoke read, not the check's); `ls /Users/cobalt/.cobalt` at X2 (ASK DESK) and DEPLOY PROOF; `uv run python` only in X0d's "no `uv run python`" | OK |
| 19 | keyed call or key read | `## NOT IN THIS JOB` and WHY forbid `--run`, `probe`, `trial --run`, `discover`, key read, vault open, `has_secret`; every run uses a stub transport or none; X0d and X0e build no keyed call (F12) | OK |
| 20 | stop-line shape | the card holds no stop line (CARD.md forbids one); it quotes only the build's `BUILT ·` line, as CHECK-HUB `## PREFLIGHT` reads it | OK |

## ISSUES

- NOTE N1 X0e driver: `cmd_route_read` also builds a `Ledger(Path(cfg.spend_ledger), …)` from the config (`route.py:742-743`), so the monkeypatched config must point `spend_ledger` at a tmp path as well as `routing_ledger`, or the read touches the host file outside the `--add-dir`s. The helper `_route_cfg(tmp_path)` (`test_jev_shadow_1015.py:95`) already builds both under `tmp_path`; the check reuses it. Does not block.
- NOTE N2 `HOUSE A: grok` is not a CARD.md key; per SEAT ORDER house A is the first house up, so it changes nothing (round 1 N2, unchanged).
- NOTE N3 X10 asks for both houses but `HOUSE B: as needed` makes house B none under CHECK-HUB (only `mandatory — vault notes|sizing` needs one). The desk accepts it or changes the header (round 1 N3, unchanged).
- NOTE N4 The drafter's two `ASK DESK` items stand as defaults: X0e's CLI run stays off the allow line; the throwaway files under the worktree's `scratch/` are written with the Write tool (`Edit(//Users/cobalt/cobalt-wt/**)` covers that path); a denied Write is `REFUSED, not needed`.
- NOTE N5 I did not re-count R1 (147 cards): the row is unchanged since round 1, which counted 147 and proved `1470` and `518`.
- Nothing blocks the check launch.

PREFLIGHT DONE · card: jev-shadow-1015-check · checks: 20 · fails: 0 · ready: YES
