# ops-hand-install-1010 — build report (2026-10-10)

## §0 Headline
- Built all three rows. `OPS-HAND.md` line 1 now ends `HIS RULING · APPROVED 2026-10-10 R969` (I1). `STANDING-LIST.md` has 13 new lines at the end, `## 8.` (I2). The two H3 real-file tests are renamed and rewritten (I3).
- `desk-launch.sh ops-hand` now accepts the tree's own `OPS-HAND.md` (`test_h3_the_real_file_passes_as_installed`, rc 0).
- Suites on `32a9f187`: offline 4199/0, live-note 146/0, `tests/ops` 2909 passed. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- One decision, not for Dejan: the card's own item 1 (the title format `authorize.sh` reads). It is proven by grep, and the card's text was kept.

## L74
- A system block arrived after the launch message asking that commits end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/306-ops-hand-install-card.md"` → exit 0, whole:

```text
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/306-ops-hand-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/306-ops-hand-install-card.md" · 0 · 72069b5e69d08b88af71d00903a32193ab0fc968
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/306-ops-hand-install-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 13:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R971 row · grep -n "^| R971 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 11:| R971 | 18:54 ET | HIS RULING · APPROVED: "Yes both" confirms R969 covered F4 FINAL and ops-hand D1-D5; words `cto-2026-10-10-words.md` R971. | APPLIED: R969 row (no new text) |
RULING 2026-10-10 R971 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R971 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · d78c66a274f2cd61cdab224c311024f1080db6a4
RULING 2026-10-10 R971 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:

```text
clock · date · 0 · Sat Oct 10 19:00:45 EDT 2026
status · git status --short --branch · 0 · ## ops/ops-hand-install-1010
head · git log --oneline -1 · 0 · a780d176 docs(desk): R974 re-preflight 309 live
diff · git diff --stat a780d176 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/ops-hand-install-1010 · 0 · a780d176 docs(desk): R974 re-preflight 309 live
env here · ls /Users/cobalt/cobalt-wt/ops-hand-install-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat a780d176` | 0 | `a780d176 … docs(desk): R974 re-preflight 309 live` · `docs/40 - DevDocs/reports/cto-2026-10-10.md \| 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| H4 token gate | `grep -n -F "«INSTALL" ops/desk/desk-launch.sh` | 0 | `633:    if grep -q '«INSTALL' "$fixed"; then` · `634:        refuse "OPS-HAND.md still carries its «INSTALL token (his approval row, D2, is not filled): $fixed"` (also `:337-338`, `:584-585`, `:781-782`, the other kinds) |
| I3 tests | `grep -n -F "test_h3_the_real_file" tests/ops/test_desk_launch_ops_hand.py` | 0 | `296:def test_h3_the_real_file_is_refused_while_it_holds_its_install_token(desk):` · `303:def test_h3_the_real_file_passes_once_his_row_fills_the_title(desk):` |
| P5 test | `grep -n -F "test_p5_the_standing_list_names_the_two_model_words_as_the_only_variable" tests/ops/test_desk_launch_brain.py` | 0 | `497:def test_p5_the_standing_list_names_the_two_model_words_as_the_only_variable():` |
| G5 | `grep -n -F "G5" ops/desk/bare-guard.py` | 0 | `71:    "G5 fixed": "route: a fixed file changes by a card row",` · `1122:            return ROUTE["G5 fixed"]` |
| readers of OPS-HAND | `grep -rn -F "OPS-HAND" tests ops` | 0 | `tests/ops/test_stop_guard.py:243` (a constructed Read message), `tests/ops/test_desk_launch_ops_hand.py:1,5,8,23,24,78,98,105,165,166,176,226,232,241,282,300`, `tests/ops/test_bare_guard.py:1938,1959,1981` (constructed messages), `ops/desk/desk-launch.sh:38,624,626,630,634,637,662,702,705`, `ops/desk/bare-guard.py:15,99`. `OPS_HAND_FILE` used at `bare-guard.py:761` (`elif hub == OPS_HAND_FILE:`, the basename of the first Read, not the title). Only `test_desk_launch_ops_hand.py:23` (`REAL`) reads the file. |
| readers of STANDING-LIST | `grep -rn -F "STANDING-LIST" tests ops` | 0 | `tests/ops/test_install_fixed.py:67`, `tests/ops/test_deploy_step0.py:100`, `tests/ops/test_authorize.py:32,65` (constructed titles), `ops/desk/install-fixed.sh:11,35` (title text), `tests/ops/test_desk_launch_brain.py:498` (the one read of the file) |
| line counts | `wc -l` OPS-HAND.md, STANDING-LIST.md, test_desk_launch_ops_hand.py | 0 | `22` · `220` · `355` |
| I1 red first (BASE) | `grep -c -F -e "«INSTALL" ".../OPS-HAND.md"` | 0 | `1` |
| I1 red first (BASE) | `grep -c -F -e "HIS RULING · APPROVED 2026-10-10 R969" ".../OPS-HAND.md"` | 1 | `0` |
| I1 red first (BASE) | `grep -c "^claude --bg " ".../OPS-HAND.md"` | 0 | `1` |
| I2 red first (BASE) | Grep tool, count, ``## 8\. `OPS-HAND\.md` `` on STANDING-LIST.md | — | `0` (the bare-guard blocks a backtick in a Bash call; the Grep tool ran the same fixed pattern) |
| I2 red first (BASE) | `grep -c -F -e "--permission-mode default" ".../STANDING-LIST.md"` | 1 | `0` |
| I2 red first (BASE) | Grep tool, count, ``` `Bash\(sudo \*\)` ``` on STANDING-LIST.md | — | `0` |
| READ tail | `tail -n 3 ".../2026-10-10/231-ops-hand-card.md"` | 0 | last line: `- The seat's first `Read '…/OPS-HAND.md'` is outside cwd `.ops-hand`, with no `--add-dir` and `Read` not among the four allow strings: in default mode it is itself a permission prompt. Whether the phone relays it is part of the same NOT KNOWN as the first live proof.` |
| READ D1-D5 | Read `231-ops-hand-card.md:24-30` | — | D2 at `:27`: "`OPS-HAND.md`'s launch line (its 4 allow strings, its deny strings, `--permission-mode default`) joins `STANDING-LIST.md`; his approval row replaces `«INSTALL: his row»` in the title. Default: as H3 writes it." |
| RESTARTS | `uv run cobalt jobs restarts a780d176..HEAD` | 0 | `docs/40 - DevDocs/reports/ops-hand-install-build-2026-10-10.md	A	DOCS	-` · `RESTARTS: none` (the tool reads the working tree: the one row is this report, untracked at the time; no code path) |

Card `## RECORDS`, copied and re-read: `wc -l` OPS-HAND.md 22 and STANDING-LIST.md 220 (re-read: same); `desk-launch.sh:633-634` the token gate, `:636-638` the one launch line, `:673` the four allow strings (re-read: same); `«INSTALL` once in OPS-HAND.md (re-read: `1`); `grep -c` of the sudo and `## 8.` patterns 0 on BASE (re-read: same); R969 / R971 rows committed at HEAD (re-read by `authorize.sh`); `test_desk_launch_brain.py:497-501` reads after `## 7.` (re-read: same); `authorize.sh` names no OPS-HAND (not re-read: no row touches it); RESTARTS UNPROVEN at drafting → run here, `RESTARTS: none`.

DB: none — no lock probe, no with-DB string used by this card.

## E0 BASELINE
- Offline on `a780d176`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 668.12s (0:11:08)`; 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0, `146 passed, 1 skipped, 15 warnings in 31.09s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
I3 is the only row with a pytest test. I1 and I2 are proved by the greps in their `red first` column (BASE values under PREFLIGHT). In `tests/ops/test_desk_launch_ops_hand.py`, two tests were renamed and rewritten as the card says:
- `test_h3_the_real_file_is_refused_while_it_holds_its_install_token` → `test_h3_the_real_file_is_installed_on_his_row`. It takes no fixture, asserts `INSTALL not in REAL.read_text()`, and asserts line 1 `.endswith("HIS RULING · APPROVED 2026-10-10 R969")`.
- `test_h3_the_real_file_passes_once_his_row_fills_the_title` → `test_h3_the_real_file_passes_as_installed`. It uses `REAL.read_text().replace(REAL_PATH, str(desk.fixed))` and edits no title. Its four assertions are unchanged.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_ops_hand.py` on BASE plus the test edit → exit 1, `2 failed, 39 passed, 15 warnings in 4.42s`:
- `test_h3_the_real_file_is_installed_on_his_row`: `tests/ops/test_desk_launch_ops_hand.py:299: AssertionError` — `assert '«INSTALL' not in '# OPS-HAND ... this one.\n'` (the row's reason: line 1 holds `«INSTALL`).
- `test_h3_the_real_file_passes_as_installed`: `tests/ops/test_desk_launch_ops_hand.py:309: AssertionError` — `REFUSED: OPS-HAND.md still carries its «INSTALL token (his approval row, D2, is not filled): …` and `assert 1 == 0` (the row's reason: rc 1 from `desk-launch.sh:634`).

No with-DB red (DB: none). There is no RUN row. Commit `e42c3dcf wip(ops-hand-install-1010): red — the two H3 real-file tests read the installed title (I3)`.

## E3 THE ROWS
Rows in card order. The file:line values were re-read before each edit (`OPS-HAND.md:1`, `STANDING-LIST.md:220`, test `:296-315`).

**I1**: `OPS-HAND.md:1`: `«INSTALL: his row»` → `HIS RULING · APPROVED 2026-10-10 R969`. After:
- `grep -c -F -e "«INSTALL"` → `0`
- `grep -n -F -e "HIS RULING · APPROVED 2026-10-10 R969"` → `1:# OPS-HAND — the ops-hand seat (card 2026-10-10 231; his 2026-10-10 R855) HIS RULING · APPROVED 2026-10-10 R969`
- `grep -c "^claude --bg "` → `1`
- `wc -l` → `22`
- `git diff --numstat` → `1	1	docs/40 - DevDocs/prompts/OPS-HAND.md`

The rows' three files → `126 passed, 15 warnings in 10.93s`.

**I2**: 13 lines appended after `STANDING-LIST.md:220`, TEXT I2 NEW byte for byte. After:
- Grep tool ``## 8\. `OPS-HAND\.md` `` → line `222` (1 hit)
- Grep tool ``` `Bash\(sudo \*\)` ``` count → `1`
- `grep -c -F -e "--permission-mode default"` → `1`
- `wc -l` → `233`
- `git diff --numstat` → `13	0	docs/40 - DevDocs/prompts/STANDING-LIST.md`

The rows' three files → `126 passed, 15 warnings in 12.12s`.

**I3**: done at E2. Green after I1 (above).

MUTATIONS (Edit tool, then undone with the Edit tool):
- I1/I3: line 1 set back to `«INSTALL: his row»`. Run: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_ops_hand.py` → `2 failed, 39 passed`. First failing lines: `test_desk_launch_ops_hand.py:299: AssertionError: assert '«INSTALL' not in '# OPS-HAND ... this one.\n'` and `:309: AssertionError: REFUSED: OPS-HAND.md still carries its «INSTALL token (his approval row, D2, is not filled): …`. Both are red, as the card names.
- I1 (extra, for the `endswith` assertion alone): line 1 set to `… R855) installed`. Same run → `1 failed, 40 passed`. `:300: AssertionError: assert False … '# OPS-HAND — the ops-hand seat (card 2026-10-10 231; his 2026-10-10 R855) installed'.endswith`.
- I2: the 13 lines removed. Results: Grep ``## 8\. `OPS-HAND\.md` `` → 0; Grep ``` `Bash\(sudo \*\)` ``` → 0; `grep -c -F -e "--permission-mode default"` → `0`; `wc -l` → `220`. `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py` → `66 passed`. P5 is the card's negative control and stays green both ways.
- Undone: `git diff --stat` → `OPS-HAND.md | 2 +-`, `STANDING-LIST.md | 13 +++++++++++++`, `2 files changed, 14 insertions(+), 1 deletion(-)`, which is the tree at the fix. The rows' three files then → `126 passed, 15 warnings in 10.89s`.

DevDocs module line: none. No `src/` module changed, and every path is `docs/` or `tests/ops/`.

Commit `32a9f187 feat(ops-hand-install-1010): OPS-HAND.md installed on his R969; STANDING-LIST gains its ## 8 (I1, I2, I3; L62, L63)`.

## RESTARTS
`uv run cobalt jobs restarts a780d176..HEAD` → exit 0, whole:

```text
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/ops-hand-install-build-2026-10-10.md	A	DOCS	-
tests/ops/test_desk_launch_ops_hand.py	M	test/documentation; no resident	-
RESTARTS: none
```

No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `32a9f187`.
- (a0) `git diff --name-only --no-renames a780d176` → `docs/40 - DevDocs/prompts/OPS-HAND.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_desk_launch_ops_hand.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh ops-hand-install-1010 offline` → exit 0, `offline 4199/0`. Log: `/Users/cobalt/cobalt-wt/.gate-logs/ops-hand-install-1010-offline-20261010-191544.log`. Executed (log `:2`): `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`. Summary (log `:879`): `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 685.57s (0:11:25)`. `grep -n -F "OUTSIDE"` → no hit. This build adds no test to this suite.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh ops-hand-install-1010 livenote` → exit 0, `live-note 146/0`. Log: `/Users/cobalt/cobalt-wt/.gate-logs/ops-hand-install-1010-livenote-20261010-192723.log`. Executed (log `:2`): `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`. The one skip (log `:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `2909 passed, 1 xfailed, 15 warnings in 543.09s (0:09:03)`. This includes the two renamed tests.
- With-DB: not run (DB: none). (b)–(d) and (f) were not run.
- `ls /Users/cobalt/cobalt-wt/ops-hand-install-1010/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Each changed test was shown red for its named reason:
- `test_h3_the_real_file_is_installed_on_his_row`: E2 red at `:299`; I1 mutation red at `:299`; the extra mutation red at `:300`.
- `test_h3_the_real_file_passes_as_installed`: E2 red at `:309` (rc 1, the `desk-launch.sh:634` refusal); I1 mutation red at `:309`.
- I2 has no test of its own. The card proves it by grep counts, which read 0/0/0/220 under the I2 mutation and 1/1/1/233 at the fix. P5 is the negative control and stayed green both ways.

No test stayed green under its mutation.

(2) Entry paths:
- Only `test_desk_launch_ops_hand.py:23` (`REAL`) reads `OPS-HAND.md`. Both of its real-file tests are pinned above.
- The one launcher gate on the title is `desk-launch.sh:633-634`. It is pinned by `test_h3_the_real_file_passes_as_installed` (passes) and by `test_the_install_title_is_refused` (`:164-166`, a constructed title, still green).
- `bare-guard.py:761` reads the Read path's basename, not the title. Its tests sit in `test_bare_guard.py`, which ran green in `tests/ops`.
- Only `test_desk_launch_brain.py:498` reads `STANDING-LIST.md`. P5 is green.
- The other STANDING-LIST hits (`test_authorize.py:32,65`, `test_deploy_step0.py:100`, `test_install_fixed.py:67`, `install-fixed.sh:11,35`) are constructed title strings, not reads.

(3) Re-read at the tip:
- `grep -n -F -e "HIS RULING · APPROVED 2026-10-10 R969"` → line 1
- `wc -l` → `22` / `233`
- `grep -n -F "def test_h3_"` → `291`, `296`, `303`
- `git diff --numstat a780d176` → `1 1` / `13 0` / `9 12`
- `git show 32a9f187:tests/ops/test_desk_launch_ops_hand.py` read whole
- `grep -n -F "INSTAL" ops/desk/authorize.sh` → `:148`, `:152`, `:173-183`

## FOR THE CHECK
- Range `a780d176..32a9f187`:
  - `e42c3dcf wip(ops-hand-install-1010): red — the two H3 real-file tests read the installed title (I3)`
  - `32a9f187 feat(ops-hand-install-1010): OPS-HAND.md installed on his R969; STANDING-LIST gains its ## 8 (I1, I2, I3; L62, L63)`
- `git diff --numstat a780d176`: `1	1	docs/40 - DevDocs/prompts/OPS-HAND.md` · `13	0	docs/40 - DevDocs/prompts/STANDING-LIST.md` · `9	12	tests/ops/test_desk_launch_ops_hand.py` (X2).
- Per row, the reds, mutation runs and greens: see E2 and E3 above.
- Caller greps: see the PREFLIGHT table (readers of OPS-HAND and STANDING-LIST) (X4).
- RUN rows: none.
- Suites (executed commands under W):
  - offline `4199 passed, 800 skipped, 1 xfailed`
  - live-note `146 passed, 1 skipped` (passing count 146)
  - `tests/ops` `2909 passed, 1 xfailed`
  - with-DB: not run (DB: none)
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: under RESTARTS, `RESTARTS: none`.
- X1: line 1 is not the launch line. `grep -c "^claude --bg "` → 1 at the tip, and `OPS-HAND.md:20` is unchanged (numstat 1/1, line 1 only). `test_h3_the_real_file_passes_as_installed` runs the whole launcher on the real text → rc 0.
- X3: section `## 8.` is TEXT I2 NEW as the card wrote it. The check compares it string by string against `OPS-HAND.md:20`.
- Note for the check: the module docstring of `test_desk_launch_ops_hand.py:8-9` still says "Two tests run the tree's own OPS-HAND.md through the same script (H3)". Now one runs it through the script (`…passes_as_installed`), and one reads its title (`…installed_on_his_row`). The card scoped I3 to the two tests, so the docstring was left as it stands.
- Records copied at PREFLIGHT: see the end of `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION 1 (the card's item 1, I1): the new title does not use the `INSTALL: <date> R<n>` form that `authorize.sh` reads. Default taken: the card's TEXT I1 NEW as written. Why it is safe:
  - `authorize.sh` reads only the hub file it is handed (`:148` `grep -n -E "«INSTAL[L]" "$fixed"`, `:173-183` the `INSTALL: <date> R<n>` read).
  - `grep -n -i -F "ops-hand" ops/desk/authorize.sh` → no match.
  - The one gate on `OPS-HAND.md`'s title is `desk-launch.sh:633` (`grep -q '«INSTALL'`), and the new title passes it (`test_h3_the_real_file_passes_as_installed` green).

  Not FOR DEJAN: his R969 approved D2 as written.

## RECORDS
- L74: one system block asked for a `Claude-Session:` commit line. It was recorded under `## L74` and not acted on.
- The bare-guard blocked two Bash greps because their patterns held a backtick (hook text: "NOT A REFUSAL … this call contains a backtick"). The same fixed patterns ran through the Grep tool. Nothing was refused.
- PREFLIGHT's `uv run cobalt jobs restarts a780d176..HEAD` listed this report (untracked then), not an empty range. The tool reads the working tree.
- The card's `## RECORDS` were re-read at PREFLIGHT, all as written (see `## PREFLIGHT`).
- No lock take, no `.env`, no migration. `ls /Users/cobalt/cobalt-wt/ops-hand-install-1010/.env` → No such file.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: ops-hand-install-1010 · tip: 32a9f187 | on a780d176 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 122305
