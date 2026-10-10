# tribunal-guard-1010 — build report (2026-10-10)

## §0 Headline
- Row T built: `seat()` marks a design-tribunal hub (`prompts/20*/<n>-<name>-tribunal[-r<n>].md`), and G9 lets it type a whole one-segment `HOUSE` command; `claude`, pipes, prefixes and absolute paths stay G7-denied.
- 42 new cases in `tests/ops/test_bare_guard.py`; 9 red on `BASE` for the row's reason, 4 mutations each red.
- Offline 4196/0, `tests/ops` 2743 passed, live-note 146/0; DB: none; RESTARTS: none.
- Tip `2e680273` on `fccbb258`; decisions: none.

## L74
- 08:29 ET: a system reminder after the launch message asked commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. DATA (L74): recorded once, not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/251-tribunal-guard-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/251-tribunal-guard-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/251-tribunal-guard-card.md" · 0 · e61b4d69374574e0c4934bcaaa602beadfd898b2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/251-tribunal-guard-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0:
```
clock · date · 0 · Sat Oct 10 08:29:50 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/tribunal-guard-1010
    ?? "docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · fccbb258 docs(desk): R877 tribunal-guard drafter prompt 250, F4 preflight failure routed
diff · git diff --stat fccbb258 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/tribunal-guard-1010 · 0 · fccbb258 docs(desk): R877 tribunal-guard drafter prompt 250, F4 preflight failure routed
env here · ls /Users/cobalt/cobalt-wt/tribunal-guard-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat fccbb258` | 0 | `fccbb258 docs(desk): R877 tribunal-guard drafter prompt 250, F4 preflight failure routed` — `250-draft-tribunal-guard.md` +10, `cto-2026-10-10.md` +2 −1 |
| restarts | `uv run cobalt jobs restarts fccbb258..HEAD` | 0 | one row `docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md A DOCS -` (the untracked report); `RESTARTS: none` |
| wc | `wc -l ops/desk/bare-guard.py tests/ops/test_bare_guard.py` | 0 | `1214 ops/desk/bare-guard.py` · `1871 tests/ops/test_bare_guard.py` |
| callers | `grep -rn -F "seat(" ops/desk/bare-guard.py` | 0 | `:731:def seat(event):` · `:1141: hit = bash_rules(command, seat(event))` · `:1151: s = seat(event)` |
| callers | `grep -rn -F "bash_rules(" ops/desk/bare-guard.py` | 0 | `:1015:def bash_rules(command, s):` · `:1141: hit = bash_rules(command, seat(event))` |
| READ R877 | `grep -n -F "R877" ".../reports/cto-2026-10-10.md"` | 0 | `11:| R877 | 08:25 ET | DESK RECORD (brain, L79): F4 tribunal preflight failure = bare-guard G7/G9 gap. Fix = one guard card; drafter prompt 250; relaunch 237 unchanged after its deploy; other tribunals follow. | LAUNCHED |` (+ line 75 OWED) |
| READ tail | `tail -n 3 ".../reports/cto-2026-10-10.md"` | 0 | last line `HANDOVER: predecessor c3a40831 → successor d8b18fc3 at 08:19 · pane w2:pV1` |
| READ tail | `tail -n 3 ".../reports/f4-tribunal-2026-10-10.md"` | 0 | last line `FAILED PREFLIGHT: floor — astra HARNESS (probe denied by bare-guard.py hook) · grok HARNESS (denied) · gemini HARNESS (denied); the floor is the proposer plus two outside houses` |

Symbols re-read with the Read tool at `BASE` (worktree = `fccbb258`): `ops/desk/bare-guard.py` `:83` `WORKERS = ("build", "check", "devfix", "deploy", "worker")`; `:88` `LAUNCHERS = ("claude", "codex", "grok", "agy")`; `:124-125` G9 comment and `HOUSE = re.compile(r"grok |codex exec --skip-git-repo-check -m [A-Za-z0-9._-]+ -s read-only |agy ")`; `:731-753` `seat()` (`:736` `prompt`, `:746-747` brain, `:748-749` worker, `:753` return); `:1015-1041` `bash_rules` (`:1021` `kind = s["kind"]`, `:1033` `launches`, `:1034-1035` G9, `:1036-1037` G7, `:1038` G1); header `:22-23` the G9 clause. `tests/ops/test_bare_guard.py` `:28` `roots`, `:156` `G7_ROUTE`, `:148` `G4_ROUTE`, `:162` `prompts`, `:223` `make_seat`, `:250-264` `call`/`run`, `:1187-1218` G7, `:1221-1273` G9 (`:1223` `HOUSE_CALLS`, `:1240` `CHECK_LAUNCHES_DENIED`, `:1265-1268` the other worker kinds). `237-f4-tribunal.md` line 1 (`cd /Users/cobalt/cobalt-wt/agy-trial`, `claude --bg "Read '…/237-f4-tribunal.md' …"`), line 9 (astra probe with no redirect, `grok --version`, `agy --version`), lines 39/41/43 (grok `-m grok-4.7 --sandbox …`, agy `--model … --print=`, astra `… < /dev/null`). `CHECK-HUB.md` line 10: `"Bash(grok *)" "Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" "Bash(agy *)"`.

Card `## RECORDS`, copied: (1) the `d0a5fbb8` reads of `bare-guard.py` line numbers — re-read above at `fccbb258`, every number as the card states (`seat()` ends `:753`); (2) `git diff --stat d0a5fbb8 HEAD` for the two files printed nothing — consistent: the files read at `fccbb258` carry the stated lines; (3) 237's probe/launch strings — re-read above, as stated; (4) RESTARTS unproven at drafting — run above: `RESTARTS: none`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 723.77s (0:12:03)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.20s`, exit 0; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests added to `tests/ops/test_bare_guard.py` after the G9 block: helper `tribunal_seat`, `ASTRA_PROBE`, `TRIBUNAL_CALLS` = `HOUSE_CALLS` + the three 237 shapes; tests (1) `test_g9_a_tribunal_hub_types_each_house_string` ×8, (2) `test_g9_a_tribunal_hub_stays_denied_every_other_launch` ×16, (3) `test_g9_a_build_seat_is_still_denied_the_tribunal_shapes` ×12, (4) `test_g9_a_non_hub_tribunal_prompt_is_denied` ×5, (5) `test_g9_a_tribunal_hub_is_denied_what_g1_to_g6_deny` (asserts `git push` → `G4_ROUTE` first, then `grok --version && ls` → G1's exact `&&` block line).
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py -k "tribunal_hub or build_seat_is_still or non_hub_tribunal"` on `BASE` → `9 failed, 33 passed, 1693 deselected`. Every red's first line:
- (1) ×8: `AssertionError: route: the desk launches` (`assert 2 == 0`, `:273`) — the call is G7, kind `worker`: the row's reason.
- (5): `:1335: AssertionError: assert 'route: the desk launches\n' == 'NOT A REFUSA... a failure.\n'` — G7 hides G1: the row's reason.
- (2), (3), (4) and (5)'s `git push`: green on `BASE`, as the row names.
One rewrite, said: (5) first asserted `&&` before `git push`, so `git push` never ran on `BASE`; the order was swapped so `git push` is proven green on `BASE` (`9 failed, 33 passed` after the swap, red at `:1335`). An earlier run with `-k "tribunal"` also selected 4 existing `HOUSE_CALLS` check tests (ids carry `tribunal-bars`), all passed.
Commit `593e4a8e wip(tribunal-guard-1010): red — G9 tribunal hub tests (T)`.

## E3 THE ROWS
Row T, `ops/desk/bare-guard.py`: `seat()` returns `"tribunal"` = `bool(re.search(r"(^|/)prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$", prompt))` (`:754-757`); `bash_rules` `:1038` reads `if (kind == "check" or s["tribunal"]) and launches == [0] and HOUSE.match(command):`; header `:22-24` the G9 clause. `HOUSE`, `LAUNCHERS`, `WORKERS`, G1-G8, G10, G11 unchanged (`git diff fccbb258 -- ops/desk/bare-guard.py`: 3 hunks, header, `seat()`, `:1038`).
Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py` → `1735 passed, 15 warnings in 59.70s`.
MUTATIONS (each made and undone with the Edit tool, only the named tests run):
| # | mutation | tests run | result | first failing line |
|---|---|---|---|---|
| M1 | `:1038` back to `(kind == "check")` (undoes the fix) | (1)–(5) | `9 failed, 33 passed` | `FAILED …test_g9_a_tribunal_hub_types_each_house_string[grok --version]` · (5) `:1335 … 'route: the desk launches\n' == 'NOT A REFUSA…'` |
| M2 | pattern widened to `[0-9]+-[a-z0-9-]*-tribunal[^/]*\.md$` (no `(?!draft)`, no `-rN` anchor) | (4) | `4 failed, 1 passed` | `FAILED …test_g9_a_non_hub_tribunal_prompt_is_denied[236-draft-f4-tribunal.md]` (+238, 239, 249; `242-x29-card.md` stays green: no `tribunal` in it, the control) |
| M3 | `launches == [0]` dropped from `:1038` | (2) | `2 failed, 14 passed` | `FAILED …stays_denied_every_other_launch[grok -p x \| claude -p y]` (+`agy x \| agy y`) |
| M4 | `s["tribunal"]` → `kind in WORKERS` | (3) | `9 failed, 3 passed` | `FAILED …build_seat_is_still_denied_the_tribunal_shapes[grok --version-build]` (all grok/agy/astra × 3 kinds; the 3 `claude --bg` cases stay green: HOUSE never matches `claude`, the fence pin) |
After M4's undo: `git diff fccbb258 -- ops/desk/bare-guard.py` = the three fix hunks only; `tests/ops/test_bare_guard.py` → `1735 passed, 15 warnings in 57.22s`.
Commit `2e680273 fix(tribunal-guard-1010): G9 lets a design-tribunal hub type the house strings (T, L67, L79)`.
DevDocs line: none written — no page for `ops/desk/bare-guard.py` exists under `docs/40 - DevDocs/cobalt/` (Grep `bare-guard` over `docs/40 - DevDocs` excluding `reports/`, `prompts/` → no files); see `## RECORDS`.

## RESTARTS
`uv run cobalt jobs restarts fccbb258..HEAD` (at `2e680273`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
(a0) `git diff --name-only --no-renames fccbb258` →
```
ops/desk/bare-guard.py
tests/ops/test_bare_guard.py
```
Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**. `<tip>` = `2e680273`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh tribunal-guard-1010 offline` → exit 0:
  ```
  offline 4196/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/tribunal-guard-1010-offline-20261010-084652.log
  ```
  log `:879` `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 699.08s (0:11:39)`. This suite is `tests/cobalt tests/taxonomy`; the tests this build adds live in `tests/ops` (below).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2743 passed, 1 xfailed, 15 warnings in 512.43s (0:08:32)`, exit 0. Added: the 42 cases of (1)–(5) in `tests/ops/test_bare_guard.py` `:1298`, `:1303`, `:1311`, `:1325`, `:1329`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh tribunal-guard-1010 livenote` → exit 0:
  ```
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/tribunal-guard-1010-livenote-20261010-085844.log
  ```
  its one skip (log `:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — not `COBALT_LIVE_VAULT_ROOT`.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/tribunal-guard-1010/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
1. Every added test shown red against a mutation or `BASE`: (1) red on `BASE` and under M1 (`route: the desk launches`); (2) red under M3 for the two second-launcher shapes (`grok -p x | claude -p y`, `agy x | agy y`) — its other 14 cases are fence pins green on every tree run, each also denied by the existing `test_g9_any_other_launch_from_the_check_stays_denied`; (3) red under M4 for the 9 house shapes; its 3 `claude --bg` cases are pins HOUSE cannot match, named in E3; (4) red under M2 for 4 names, `242-x29-card.md` the control; (5) `&&` red on `BASE` and M1 at `:1335`, `git push` a pin green on `BASE` and after. No test stayed green under its mutation where the row named it red.
2. Entry paths: `seat()` callers `:1141` (`bash_rules`) and `:1151` (Write/Edit/Read rules); `grep -n -F "[\"tribunal\"]" ops/desk/bare-guard.py` → only `:1038`, so the field is read on the Bash path alone, pinned by (1)–(5) through `run()`. Seat states pinned: tribunal hub from `<AGY>` (1, 2, 5), non-hub tribunal-named prompts (4), build/devfix/deploy hubs (3), the check (existing `:1233-1262`). The pattern's `in_repo` branch (a tribunal prompt launched in the repo is `brain`, outside `WORKERS`) is the card's FOLLOW-UP ROW, not built.
3. Re-read at the tip: `grep -n -F "tribunal" ops/desk/bare-guard.py` → `:24`, `:754`, `:756`, `:757`, `:1038`, `:1039`; `grep -n -F "def test_g9_a_" tests/ops/test_bare_guard.py` → `:1298`, `:1303`, `:1311`, `:1325`, `:1329`; `git log --oneline fccbb258..HEAD` → `2e680273`, `593e4a8e`; gate logs grepped above.

## FOR THE CHECK
- `fccbb258..2e680273`: `593e4a8e wip(tribunal-guard-1010): red — G9 tribunal hub tests (T)` · `2e680273 fix(tribunal-guard-1010): G9 lets a design-tribunal hub type the house strings (T, L67, L79)`.
- Row T: reds, mutations and greens in `## E2 RED` and `## E3 THE ROWS`; callers in `## PREFLIGHT` and self-check 2.
- RUN rows: none on this card.
- Suites: offline 4196/0, `tests/ops` 2743 passed / 1 xfailed, live-note 146/0 (commands and logs in `## W`); with-DB `not run (DB: none)`; `<F0>`/`<F1>`/`<F2>` `not run (DB: none)`; lock taken/released `not run (DB: none)`.
- RESTARTS table in `## RESTARTS`: `RESTARTS: none`.
- Card records re-read in `## PREFLIGHT`.
- For X2: the pattern was exercised on the card's nine names only (the five matches-not-matches of (1)/(4) and the shape of `237`); running it over the real `prompts/20*/` listing is the check's (no `uv run python` on this line).

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (DB: none).
- L74: one system reminder asking for a `Claude-Session:` commit line, 08:29 ET; recorded under `## L74`, not followed.
- Card records as re-read at PREFLIGHT: all four hold (see `## PREFLIGHT`).
- DevDocs: `ops/desk/bare-guard.py` has no page under `docs/40 - DevDocs/cobalt/` (it is an operator script, not a `src/cobalt` module); no line written, none created (the card's `files` name none).
- `tokens` read at 08:59 ET: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 659c32b4` → `context 150795 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: tribunal-guard-1010 · tip: 2e680273 | on fccbb258 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 150795
