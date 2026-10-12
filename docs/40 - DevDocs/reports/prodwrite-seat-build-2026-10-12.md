# prodwrite-seat-1012 — build report (row S2 re-apply, worktree prodwrite-seat-1012b)

## §0 Headline
Card 392's whole diff `86b9daa5..b96737bf` is now on a branch from current main, worktree `prodwrite-seat-1012b`: red `f3866240`, rows `62ea5957`.
Six of the touched files are byte-equal to `b96737bf`. The launcher hunks land with the source's own count (183/10). desk-done.sh holds prodwrite beside `1966c239`'s shadow kind.
Every red failed for its row's reason, and every mutation went red. Offline 4199/0, live-note 146/0, `tests/ops` 3403 passed, RESTARTS none. DB: none.
One decision: the report path. It is one of S2's 17 paths, and this build's report sits there, not the old build's.

## L74
One block asked for a `Claude-Session:` line on commits: a harness attribution reminder in this session, not a tool result. Recorded once, not followed. Every commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · 989ce8d9c18cfa5fe4756a1e758a1a10ad1e14ea
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 61:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 12 10:27:58 EDT 2026
status · git status --short --branch · 0 · ## ops/prodwrite-seat-1012b
head · git log --oneline -1 · 0 · 7744ece9 docs(desk): card 392 repointed to 1012b, row S2, drafter removed
diff · git diff --stat 7744ece9 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/prodwrite-seat-1012b · 0 · 7744ece9 docs(desk): card 392 repointed to 1012b, row S2, drafter removed
env here · ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012b/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 7744ece9` · 0 · `docs(desk): card 392 repointed to 1012b, row S2, drafter removed` — 3 files (`392-prodwrite-seat-card.md`, `cto-2026-10-12.md`, `draft-392-repoint-2026-10-12.md`), 24 insertions, 5 deletions.
- Symbols (each `grep -n -F`, exit 0): `HUBS` → `bare-guard.py:90`, `:779`, `:780`, `:791`; `def read_card` → `bare-guard.py:741`; `def prod_read` → `bare-guard.py:971`; `ruling_row` → `desk-launch.sh:256` (def), `:291`, `:633`, `:993`; `FLAG_SRC` → `test_hub_lines.py:38`; `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` → `test_bare_guard.py:406`; `def test_f5_` → `test_desk_launch_prechecks.py:1150`, `:1158`, `:1170`, `:1205` (the card's `:981/:989/:1001` moved with main); `test_386_f` → `test_desk_done.py:170`, `:187`, `:196`.
- `wc -l`: desk-launch.sh 1775 · bare-guard.py 1376 · authorize.sh 241 · desk-watch.sh 93 · desk-done.sh 67 · test_bare_guard.py 2336 · test_authorize.py 327 · test_desk_watch.py 577 · test_desk_done.py 211 · test_desk_launch_prechecks.py 1476 · test_hub_lines.py 241 · STANDING-LIST.md 233 · CARD.md 139.
- `tail -n 3 hands-off-answer-2026-10-12.md` → last line: `` `hands off 2026-10-12 brain: … Cards C1 cleanup, C2 survey, C3 production-write seat, C4 NEEDS HIS HAND, C5 sheet changes.` ``
- `uv run cobalt jobs restarts 7744ece9..HEAD` · 0 → one row, the uncommitted report: `docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md	A	DOCS	-`; `RESTARTS: none`.
- Card records copied: main HEAD `6468fb5e` reads of `bare-guard.py:1074`/`:779-790`/`:965-1006`; the production strings on the hub lines; the hook entry and `INSTALL: none`; R1138 at `cto-2026-10-12.md` (authorize.sh re-read it at line 61, commit `5d6ce588`); `git diff 86b9daa5 b96737bf --stat` = 17 files, 1316 insertions, 37 deletions (re-run here: same); the four commits resolve; brain L79; the header edit.
- Divergence re-read: `git diff --stat 86b9daa5 7744ece9` on the row paths → of the 17, only `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_done.py`, `tests/ops/test_desk_launch_prechecks.py` moved on main; the other 13 are byte-equal to the source base.
- DB: none — no lock probe, no with-DB string used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · exit 0 · `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 682.03s (0:11:22)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 · `146 passed, 1 skipped, 15 warnings in 28.47s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (names no `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests re-applied from `b96737bf` (Write for the two new files, Edit for the rest). `git diff --stat b96737bf --` on the six test files that did not move on main → one line differs: `test_desk_launch_prodwrite.py` P1's docstring cites `desk-launch.sh:892` (the kind refusal's line at this BASE) where the source said `:889`. `test_desk_done.py` and `test_desk_launch_prechecks.py` (moved on main) each gain the source's +32 lines beside the base's tests (`git diff --stat 7744ece9`: 32 insertions each).

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_prodwrite_hub.py tests/ops/test_desk_launch_prodwrite.py tests/ops/test_bare_guard.py tests/ops/test_authorize.py tests/ops/test_desk_watch.py tests/ops/test_desk_done.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_hub_lines.py` · exit 1 · `67 failed, 2149 passed, 15 warnings in 235.46s (0:03:55)`. Each red, its first line:
- W1 `test_prodwrite_hub.py` (13): `FileNotFoundError: [Errno 2] No such file or directory: '…/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md'` (11); `test_prodwrite_hub.py:147: AssertionError: assert 0 == 1` (CARD.md section); `:156: AssertionError: []` (STANDING-LIST §9).
- W2 `test_desk_launch_prodwrite.py` (31: P1 ×2, P2 ×29): `AssertionError: REFUSED: kind 'prodwrite' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops` (`:163`, `:178`, `:152` ×28, `:273`). P2's negative control (other live sessions) is red on BASE by the same kind refusal (`:273`). P3 ×2 PASSED on BASE (two-sided).
- W3 `test_bare_guard.py` (13): `test_bare_guard.py:292: AssertionError: (0, '')` ×12 (Q2 ×5, Q2 two/none ×4, Q2 short second row, Q3, Q4 — the seat is kind None and passes); `:529: AssertionError: ('git -C … diff --output=…/src/x.py HEAD', 0, '')` (O3). Q1, Q5 (×12), O1 and `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` PASSED on BASE.
- W4 `test_authorize.py` (5): `:347` (R1) and `:371` ×4 (R2): `AssertionError: REFUSED: kind 'prodwrite' is none of build, check, deploy, shadow`. R3 ×4 PASSED.
- W5 `test_desk_watch.py:112` (V1): `REFUSED: unknown kind: prodwrite`; `test_desk_done.py:133` (D1): `REFUSED: unknown kind: prodwrite`. V2, D2 ×2 PASSED (two-sided); row S's `test_386_f1` ×2, `f2` ×3, `f3` PASSED.
- W6 `test_desk_launch_prechecks.py:224` ×3 (F6, O2 ×2): `AssertionError: RUN: cd …/repo` (it launches). F7 and the F5 tests PASSED.
- W7 `test_hub_lines.py`: PASSED on BASE (pins; its mutation is at E3).

## E3 THE ROWS
Re-applied with Edit (new file with Write) from `git diff 86b9daa5 b96737bf`; no merge, rebase or cherry-pick. Commit `62ea5957`.
- Byte-equal to `b96737bf` (`git diff --stat b96737bf -- <path>` prints nothing): `PRODWRITE-HUB.md`, `CARD.md`, `STANDING-LIST.md`, `authorize.sh`, `bare-guard.py`, `desk-watch.sh`.
- `desk-launch.sh` (moved on main): `git diff --numstat 7744ece9` → `183 10`, the source's own count (`git diff --numstat 86b9daa5 b96737bf` → `183 10`); every hunk landed at its anchor (the kind case now `:927-928`, the arm `:1642-1771`).
- `desk-done.sh` (row S): the prodwrite hunks sit beside `1966c239`'s shadow change, both kept — `prodwrite) done_re='^WRITTEN' ;;` beside `shadow) done_re='^SHADOW (BUILT|ROLE)'; kind=build ;;`, and the FAILED case `build|check)` (shadow reaches it as build) plus `prodwrite)` keep; header and usage name both kinds.

Greens after each row:
- W1 + W7: `tests/ops/test_prodwrite_hub.py tests/ops/test_hub_lines.py` → `43 passed, 15 warnings in 2.95s`.
- W2 + W6: `tests/ops/test_desk_launch_prodwrite.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_brain.py` → `271 passed, 15 warnings in 85.91s`.
- W3, W4, W5, S: `tests/ops/test_bare_guard.py tests/ops/test_authorize.py tests/ops/test_desk_watch.py tests/ops/test_desk_done.py` → `1968 passed, 15 warnings in 154.76s`.

THE MUTATIONS (each made with Edit, its tests run, undone with Edit):
- W1: title `INSTALL: 2026-10-12 R1138` → `R1139` → `1 failed, 12 passed`: `test_prodwrite_hub.py:123: AssertionError: … assert 'INSTALL: 2026-10-12 R1138' in '# PRODWRITE-HUB — … R1139 …'`.
- W2: the kind case `prodwrite)` → `prodwritex)` → 31 failed, 2 passed (P3 ×2): `test_desk_launch_prodwrite.py:163: AssertionError: REFUSED: kind 'prodwrite' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops, prodwrite`; each P2 case asserts its own text (e.g. `assert 'REFUSED: the write row is unnamed: ## ROWS holds 2 rows' in "REFUSED: kind 'prodwrite' is none of …"`).
- W3 (a) G2: `return None` after `named = …` in the prodwrite branch → `12 failed, 74 passed`: Q2 ×5, Q2 two/none ×4, Q2 short second row, Q4, O3 (`test_bare_guard.py:292: AssertionError: (0, '')`; `:529` for O3). (b) G5: the prodwrite fence's last `return ROUTE["G5 fence"]` → `return None` → Q3 `1 failed` (`:292: AssertionError: (0, '')`). (c) O1: `if hub in HUBS and not pw_hub:` → `if hub in HUBS:` → O1 `1 failed` (`:292`).
- W4: `if [ "$kind" = "prodwrite" ]` → `"prodwritex"` → `5 failed, 4 passed` (R1 at `test_authorize.py:351`: `assert 'WRITE RULING 2026-01-02 R2 row · ' in …AUTHORIZED`; R2 ×4 at `:370`: `assert 0 == 1`); R3 ×4 green.
- W5 + S (a): `desk-watch.sh` and `desk-done.sh` `prodwrite)` → `prodwritex)` → `2 failed, 9 passed`: `test_desk_watch.py:112` and `test_desk_done.py:133`: `REFUSED: unknown kind: prodwrite`; the 386 tests (f1 ×2, f2 ×3, f3) and V2, D2 ×2 green — row S's two changes stand together. (b) D2: the FAILED-kept `prodwrite)` → `prodwritex)` → D2 `1 failed`: `test_desk_done.py:142: AssertionError: assert 0 == 1` (it closed: `+ claude stop aaaa1111`).
- W6 (a): the awk `if (index(s, "COBALT_ENV=production")) print s` → `if (0) print s` → `2 failed, 12 passed`: F6 and O2 `"production"`, `test_desk_launch_prechecks.py:224: AssertionError: RUN: cd …/repo`; F7, F5 green. (b) the `$` refusal `*[\$\`\\]*` → `*[\`\\]*` → O2 `${x:-production}` `1 failed` (`:224`).
- W7: `"Bash(COBALT_ENV=production uv run cobalt validate)"` added to `CHECK-HUB.md`'s line → `2 failed, 12 passed`: `test_hub_lines.py:91` and `:137: AssertionError: ('CHECK-HUB.md', ['Bash(COBALT_ENV=production uv run cobalt validate)'])`. Undone: `git status --short` lists no `CHECK-HUB.md`.
- After every undo: `git diff --stat b96737bf --` on the six byte-equal files prints nothing; `git diff --numstat 7744ece9 -- ops/desk/desk-launch.sh ops/desk/desk-done.sh` → `183 10`, `9 5`.

DevDocs line: none written — no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (`grep -rl -F "desk-launch.sh" "docs/40 - DevDocs/cobalt"` → only `jobs/restarts.md`, the page of `src/cobalt/jobs/restarts.py`); the source build added none either.

## RESTARTS
`uv run cobalt jobs restarts 7744ece9..HEAD` (HEAD `62ea5957`) · exit 0 · whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/PRODWRITE-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_done.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prodwrite.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	M	test/documentation; no resident	-
tests/ops/test_hub_lines.py	M	test/documentation; no resident	-
tests/ops/test_prodwrite_hub.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. The 17 paths (the report counted, uncommitted) are row S2's 17. W8 (RUN): as card 386 L3 expected — `ops/desk/` operator script, `docs/` DOCS, `tests/` no resident.

## W THE THREE SUITES
`<tip>` = `62ea5957`.
- (a0) `git diff --name-only --no-renames 7744ece9` → whole: `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/PRODWRITE-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/authorize.sh`, `ops/desk/bare-guard.py`, `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `tests/ops/test_authorize.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_done.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_desk_launch_prodwrite.py`, `tests/ops/test_desk_watch.py`, `tests/ops/test_hub_lines.py`, `tests/ops/test_prodwrite_hub.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 16 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012b offline` · exit 0 · `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012b-offline-20261012-105748.log` (`:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 696.16s (0:11:36)`; `grep -c -F "OUTSIDE the allowed set"` → `0`). This build adds no test under `tests/cobalt` or `tests/taxonomy`; its tests are in `tests/ops` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012b livenote` · exit 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012b-livenote-20261012-105751.log`; its one skip (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, which names no `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 · `3403 passed, 1 xfailed, 16 warnings in 686.04s (0:11:26)`. It holds every test row S2 names: `test_prodwrite_hub.py`; `test_desk_launch_prodwrite.py` P1–P3; `test_bare_guard.py` Q1–Q5, O1, O3 and `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed`; `test_authorize.py` R1–R3; `test_desk_watch.py` V1, V2; `test_desk_done.py` D1, D2 and the 386 f1/f2/f3; `test_desk_launch_prechecks.py` F6, F7, O2 and the F5 tests; `test_hub_lines.py` W7 and `test_build_check_and_devfix_deny_every_production_string`.
- with-DB: not run (DB: none). (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012b/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test went RED, either against BASE (E2) or under an E3 mutation. W1: 13 red on BASE, plus the title mutation. W2: 31 red on BASE, plus the kind mutation (31 red; P3 two-sided green). W3: 13 red on BASE; mutations G2 (12), G5 (Q3) and O1. Q1 and Q5 are pins: green on BASE and after, as the row says. W4: 5 red on BASE plus the mutation (5); R3 is a pin. W5/S: V1 and D1 red on BASE, plus the kind mutation; D2's keep has its own mutation; V2, D2-build and the 386 tests stay green, both kept. W6: F6 and O2 ×2 red on BASE; mutations (a) 2 red and (b) 1 red; F7 and F5 are pins. W7 is a pin: its mutation turned 2 red. No test stayed green under its own mutation, so none was rewritten.
(2) Every entry path is pinned. `authorize.sh prodwrite` is called by the hub line `PRODWRITE-HUB.md:10` and step (0) `:26`: the hub tests pin the allow string, R1/R2 pin the script. `desk-watch.sh prodwrite` is called by the hub `:54` and by the launcher's WATCH line (`watch_line`, `desk-launch.sh:248`): P1 asserts `desk-watch.sh prodwrite "<card>"` and V1 pins the script. `desk-done.sh prodwrite`: D1 and D2. The launcher kind case `desk-launch.sh:927`: P1–P3. `bare-guard.py` prodwrite branches `:1099` (G2) and `:1281` (G5), `read_card` `:741` via `seat()`: Q1–Q4, O1, O3. The prompt kind's production refusal: F6, F7, O2. Every other hub line: W7.
(3) Every `file:line`, count and quote here was re-read at the tip: `grep -n -F "prodwrite) fixed="` → `desk-launch.sh:927`; `grep -n -F "if kind == PRODWRITE:"` → `bare-guard.py:1099`, `:1281`; the two caller greps above; `git diff --stat b96737bf --` (six files, empty) and `git diff --numstat 7744ece9` (`183 10`, `9 5`) after the last undo; the gate verdict lines from their output files; `git log --oneline -3` → `62ea5957`, `f3866240`, `7744ece9`.

## FOR THE CHECK
- Range `7744ece9..62ea5957`: `f3866240 wip(prodwrite-seat-1012): red — W1-W7 and S tests, re-applied from b96737bf (S2)`; `62ea5957 feat(prodwrite-seat-1012): the production-write seat re-applied from b96737bf onto main — PRODWRITE-HUB.md, launcher kind, guard G2/G5, authorize, watch/done beside 1966c239, prompt production refusal (W1-W7, S, S2; L29 L81 K3 K5)`. The report commit follows.
- Source: `b96737bf` (old branch `ops/prodwrite-seat-1012`, untouched), diff `86b9daa5..b96737bf`. Re-applied onto `7744ece9`. Of the 17 source paths, 16 are code, tests or prompts (the a0 list); the 17th, this report, holds this build's report (DECISIONS 1).
- Per row: reds under `## E2 RED`, mutations and greens under `## E3 THE ROWS`, quoted.
- RUN row W8: under `## RESTARTS`, whole.
- Suites: offline `gate.sh … offline` → `offline 4199/0`; live-note `gate.sh … livenote` → `live-note 146/0`; `tests/ops` → `3403 passed, 1 xfailed`. with-DB: `not run (DB: none)`.
- `<F0>`/`<F1>`/`<F2>`: `not run (DB: none)`. Lock taken / released: `not run (DB: none)`.
- RESTARTS: `RESTARTS: none` (table under `## RESTARTS`).
- Card records copied at PREFLIGHT: under `## PREFLIGHT`.
- The card's CHECK ASKS X1–X5 are answered by the source's checked code, which is byte-equal here for the guard (X1), the hub line (X2, X3) and authorize. X4 is the launcher arm: same hunks, and each P2 case asserts its own text (mutation W2). X5: `INSTALL: none` stands, since no file under `~/.claude/` is touched (`git diff --name-only` above).

## CONTINUE
next: none — CLOSE done.

## DECISIONS
1. ASK DESK [11:09 ET]: row S2 lists `docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md` among the 17 paths to re-apply, and BUILD-HUB makes that same path this build's `REPORT`. Safe default taken: the path holds THIS build's report. The old build's report stays on `b96737bf` as the checked evidence S2 names, and nothing of it was copied in as a claim of this run (L35).

## RECORDS
- Card records, as re-read at PREFLIGHT: authorize.sh re-proved R1138 at `cto-2026-10-12.md:61` (commit `5d6ce588`), not `:12` as the card's record says. `git diff 86b9daa5 b96737bf --stat` re-run: 17 files, 1316 insertions, 37 deletions, as recorded. The other records are copied under `## PREFLIGHT`.
- Card line cites that moved on main (read at the tip, not re-decided): the F5 tests sit at `test_desk_launch_prechecks.py:1150/:1158/:1170/:1205` (card `:981/:989/:1001`); the kind refusal sits at `desk-launch.sh:927-928` (card `:889`). P1's docstring cites the BASE line `:892`.
- The Edit tool dropped one trailing padding space twice, once in `test_authorize.py` (`[[], [` spacing) and once on the `install-ops` comment line of `desk-launch.sh`. Both were caught by `git diff` against `b96737bf` / the numstat count and restored before their commits.
- No DevDocs line owed: no `docs/40 - DevDocs/cobalt/` page covers an `ops/desk/` script.
- No extra lock take (DB: none). No `REFUSED, not needed` line. No `CONTINUE` message received.
- `desk-context.sh 13935c88` at the last step → `context 300326 of 400000 — ok`, which is above the desk's 250,000 line (UNATTENDED RULES (c)). It was read at CLOSE; the desk decides.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: prodwrite-seat-1012 · tip: 62ea5957 | on 7744ece9 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 300326 · re-applied from b96737bf onto 62ea5957
