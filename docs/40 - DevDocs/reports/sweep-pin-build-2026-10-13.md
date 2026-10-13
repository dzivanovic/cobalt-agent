# sweep-pin-1013 — build report (2026-10-13)

CARD: `docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md` · BRANCH `ops/sweep-pin-1013` · BASE `03d8ebbe` · DB: none

## §0 Headline
- FR1 built: the stale `SWEEP_EXEMPT` entry `f4-refresh-build-2026-10-10.md` (key and two-line reason, `:55`-`:57` at BASE) is removed; nothing else in the file changed (`git diff`: 3 deletions).
- `tests/ops/test_the_rule_sweep.py`: RED at BASE (`AssertionError: ['f4-refresh-build-2026-10-10.md']`), 5 passed at the tip; the mutation (entry back) is red again.
- Suites at tip `52cb2fc9`: offline 4317/0, `tests/ops` 3543/0, live-note 146/0; with-DB not run (DB: none). RESTARTS: none.

## L74
- A system notice in this session (2026-10-13, after the card was read) asked for a `Claude-Session:` line on commits. It is the `## L74` line and was not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 0 · a73c86263fc7219dfa40df717929b0065e5b0f57
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Tue Oct 13 12:07:20 EDT 2026
status · git status --short --branch · 0 · ## ops/sweep-pin-1013
head · git log --oneline -1 · 0 · 03d8ebbe docs(desk): R1424 drafter fc9cc295 for sweep-pin-1013, old FR1 trees removed
diff · git diff --stat 03d8ebbe · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/sweep-pin-1013 · 0 · 03d8ebbe docs(desk): R1424 drafter fc9cc295 for sweep-pin-1013, old FR1 trees removed
env here · ls /Users/cobalt/cobalt-wt/sweep-pin-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 03d8ebbe` | 0 | `docs(desk): R1424 drafter fc9cc295 for sweep-pin-1013, old FR1 trees removed` · `docs/40 - DevDocs/reports/cto-2026-10-13.md \| 7 ++++---` · `1 file changed, 4 insertions(+), 3 deletions(-)` |
| symbol: exempt name | `grep -n -F "f4-refresh-build-2026-10-10.md" tests ops -r` | 0 | `tests/ops/test_the_rule_sweep.py:55:    "f4-refresh-build-2026-10-10.md":` (the one hit) |
| symbol: `SWEEP_EXEMPT` | `grep -n -F "SWEEP_EXEMPT" tests/ops/test_the_rule_sweep.py` | 0 | `13:`, `38:SWEEP_EXEMPT: dict[str, str] = {`, `127:`, `132:`, `133:`, `138:`, `139:` |
| symbol: tests | `grep -n -F "def test_" tests/ops/test_the_rule_sweep.py` | 0 | `125:def test_the_sweep_has_no_mismatch(sweep):` · `131:def test_every_exempt_entry_still_mismatches(sweep):` · `137:def test_the_exempt_reasons_name_their_shape():` · `144:def test_the_304_check_reads_o1_and_a3(rule):` · `151:def test_the_sweep_swept_what_it_pins(sweep):` |
| symbol: restarts `tests/` | `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` | 0 | `246:            rule = "test/documentation; no resident"` |
| symbol: restarts `tests/` guard | `grep -n -F "path.startswith(\"tests/\")" src/cobalt/jobs/restarts.py` | 0 | `245:        if not rule and path.startswith("tests/"):` |
| symbol: `OPS_DESK_PREFIX` | `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` · `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| size | `wc -l tests/ops/test_the_rule_sweep.py` | 0 | `153 tests/ops/test_the_rule_sweep.py` |
| READ report tail | `tail -n 3 ".../reports/f4-refresh-build-2026-10-10.md"` | 0 | last line: `BUILT · job: f4-refresh-1010 · tip: edd5c076 \| on d78c66a2 \| migration: none \| offline 4245/0 \| with-DB 5173/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 15 of 15 \| self-check: 3 of 3 \| decisions: 14 · for Dejan: 3 · tokens: 86732` |
| READ precedent | `grep -n -F "\| FR1 \|" ".../prompts/2026-10-13/446-k5-gate-card.md"` | 0 | `32:` row FR1, text identical to this card's FR1 |
| READ lines 276-286 | Read tool on `f4-refresh-build-2026-10-10.md` | — | `276:CARRIED: O1 — …`, `277:CARRIED: A3 — …`, `278`-`286`: `SETTLED: O2/O3/O4/A4/B5/B1/B2/B3/B4 — R…` (plain lines) |
| RESTARTS empty range | `uv run cobalt jobs restarts 03d8ebbe..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |
| DB | — | — | card is `DB: none`: no lock probe, no with-DB strings used |

Card records, copied and re-read:
- Drafter reads at main `80563111` — not re-read (`git rev-parse` is not a listed string); BASE `03d8ebbe` is main's commit per PREFLIGHT's `main repo` row.
- Entry key at line 55, reason 56-57 — re-read: `grep -n` → `55:` only hit; Read tool lines 55-57.
- `test_every_exempt_entry_still_mismatches` at line 131 — re-read: `131:def test_every_exempt_entry_still_mismatches(sweep):`.
- `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` → re-read: `1`.
- RESTARTS class home `restarts.py:245-246`, `OPS_DESK_PREFIX` at `:38` — re-read (rows above).
- Same feature as card 446 FR1 — re-read (row above).
- BASE is the desk's; house A Grok, HOUSE B as needed — the desk's facts, not re-readable by a listed string.

## E0 BASELINE
On BASE `03d8ebbe`:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0: `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 655.31s (0:10:55)` — 0 failed, 0 errors. (Its live-note skips, e.g. `SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`, are the offline run's by design; the live-note run below covers them.)
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.76s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
FR1's red is the existing pin `test_every_exempt_entry_still_mismatches`; the row writes no new test, so no test file was written and no `wip(sweep-pin-1013): red` commit was made (nothing to commit; `## RECORDS`).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` on BASE → exit 1:
```
>       assert not stale, stale
E       AssertionError: ['f4-refresh-build-2026-10-10.md']
E       assert not ['f4-refresh-build-2026-10-10.md']

tests/ops/test_the_rule_sweep.py:134: AssertionError
1 failed, 4 passed, 15 warnings in 1.28s
```
The red is the row's named reason. The four pins (`test_the_sweep_has_no_mismatch`, `test_the_exempt_reasons_name_their_shape`, `test_the_304_check_reads_o1_and_a3`, `test_the_sweep_swept_what_it_pins`) PASS before the change.

## E3 THE ROWS
FR1 — Edit tool: the key `"f4-refresh-build-2026-10-10.md":` and its two-line reason removed. `git diff` before the commit:
```
@@ -52,9 +52,6 @@ SWEEP_EXEMPT: dict[str, str] = {
     "s4-p1-1009-terra-check-2026-10-11.md":
         "shape: twenty-five `## RUNS` bullets ending `· HELD`, `## FIXES` prose: no NOT FIXED mark "
         "(n 25, read 0); ASK DESK 1",
-    "f4-refresh-build-2026-10-10.md":
-        "shape: `:262` a bulleted bold CARRIED line with a backticked id and a trailing sentence; read, it "
-        "would count 304's O1 twice beside row CR's plain line (`has 2 FIXED or CARRIED lines`); ASK DESK 4",
     "dev-rebuild-port-build-2026-10-03.md":
```
GREEN after: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` → `5 passed, 15 warnings in 1.08s`.
`grep -c -F "f4-refresh-build-2026-10-10.md" tests/ops/test_the_rule_sweep.py` → `0` (CHECK ASK X2; DEPLOY PROOF after-value at the branch).
MUTATION (undoes the fix): the three lines put back with the Edit tool; `git diff --stat` → empty (the tree byte-equal to BASE's file); `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_the_rule_sweep.py` → exit 1:
```
E   AssertionError: ['f4-refresh-build-2026-10-10.md']
FAILED tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches
1 failed, 4 passed, 15 warnings in 1.09s
```
Undone with the Edit tool; `git diff` → the three-line deletion above, nothing else.
DevDocs line: none — no `src/` module changed and `grep -rln -F "test_the_rule_sweep" "docs/40 - DevDocs/cobalt"` → no page holds this test file.
Commit `52cb2fc9 fix(sweep-pin-1013): the stale f4-refresh-build exemption goes (FR1, L79, L3)` — `1 file changed, 3 deletions(-)`.

R2 (RUN, asserts nothing) — `uv run cobalt jobs restarts 03d8ebbe..HEAD` at `52cb2fc9`, quoted WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/sweep-pin-build-2026-10-13.md	A	DOCS	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
(The report row is this report, then uncommitted in the worktree.) Matches the card's expectation; no DECISION.

## RESTARTS
The R2 table above, WHOLE. No `UNCLASSIFIED` row. `RESTARTS: none`.

## W THE THREE SUITES
Tip `52cb2fc9`. (a0) `git diff --name-only --no-renames 03d8ebbe` → `tests/ops/test_the_rule_sweep.py` (whole output; the one path starts with `tests/ops/`). **`cobalt_dev: not taken (DB: none — 1 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh sweep-pin-1013 offline` → exit 0: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/sweep-pin-1013-offline-20261013-121945.log`. Executed (log `:2`): `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; summary (log `:885`): `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 665.36s (0:11:05)`. This build adds no test.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3543 passed, 1 xfailed, 16 warnings in 736.55s (0:12:16)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh sweep-pin-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/sweep-pin-1013-livenote-20261013-123104.log`. Executed (log `:2`): `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`; its one skip (log `:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — does not name `COBALT_LIVE_VAULT_ROOT`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/sweep-pin-1013/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) The one changed test file's pin `test_every_exempt_entry_still_mismatches`: RED at BASE (E2) and RED under the E3 mutation, both `AssertionError: ['f4-refresh-build-2026-10-10.md']`; GREEN at the tip. No test was added. — holds.
(2) Entry paths of `SWEEP_EXEMPT`: its readers by `grep -n -F "SWEEP_EXEMPT"` → `:127` (`test_the_sweep_has_no_mismatch`), `:133` (`test_every_exempt_entry_still_mismatches`), `:139` (`test_the_exempt_reasons_name_their_shape`); all three plus `test_the_304_check_reads_o1_and_a3` and `test_the_sweep_swept_what_it_pins` GREEN at the tip (`5 passed`); the removed name has no other holder in `tests` or `ops` (PREFLIGHT grep, one hit). — holds.
(3) Re-read at the tip: `git show 52cb2fc9:tests/ops/test_the_rule_sweep.py` (six entries, `CHECKS_SWEPT: int | None = 18`, `BUILDS_SWEPT: int | None = 85` unchanged); `grep -n -F "dev-rebuild-port-build-2026-10-03.md" tests/ops/test_the_rule_sweep.py` → `55:`; `grep -c -F "f4-refresh-build-2026-10-10.md"` → `0`; the gate logs' summaries by `grep -n -F`. — holds.

## FOR THE CHECK
- `03d8ebbe..52cb2fc9`: one commit, `52cb2fc9 fix(sweep-pin-1013): the stale f4-refresh-build exemption goes (FR1, L79, L3)`.
- FR1: red (E2), mutation red and green (E3) quoted above.
- Caller greps: PREFLIGHT rows `symbol: exempt name`, `symbol: SWEEP_EXEMPT`, `symbol: tests`.
- R2 output WHOLE: `## E3 THE ROWS`.
- Suites: offline 4317/0, `tests/ops` 3543/0, live-note 146/0 with executed commands in `## W`; with-DB: not run (DB: none).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- CHECK ASKS X1: `git diff 03d8ebbe 52cb2fc9 -- tests/ops/test_the_rule_sweep.py` shows only the three-line deletion. X2: `5 passed` and `grep -c` → `0`.

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- E2 wrote no test file (FR1's red is the existing pin), so no `wip(sweep-pin-1013): red` commit exists; the red was shown on BASE's unchanged file.
- No lock take; `.env` never present (`ls` → No such file, PREFLIGHT and CLOSE).
- No `REFUSED, not needed` and no `CONTINUED` line.
- L74: one system notice asked for a `Claude-Session:` commit line (`## L74`); not acted on.
- The card's records as re-read at PREFLIGHT: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: sweep-pin-1013 · tip: 52cb2fc9 | on 03d8ebbe | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 94416
