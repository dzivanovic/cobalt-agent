# terra-pass-prompt-1011 — build report (2026-10-11)

## §0 Headline
Row T1 is built at `a790e54d`, on `ffc704da`. `SHADOW-HUB.md` changes at `:26` and `:29` only: numstat 2/2, still 103 lines.
The Terra pass prompt now allows read-only commands. Grok and Sonnet still read `Run no command.`
Suites: offline 4199/0, live-note 146/0, `tests/ops` 3135 passed. DB: none, so no lock was taken. RESTARTS: none.
One decision: one of the card's after-greps cannot hit with the text the row prescribes. The text was kept and the grep is recorded (DECISION T1).

## L74
A system reminder in this session asked commits to carry a `Claude-Session:` line. Under L74 that is data: it is recorded here once and was not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md"` (15:35 EDT), quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 0 · 89682bc0eb56d3bf4ba394cb0289525ab8d5e55c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1107 row · grep -n "^| R1107 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 10:| R1107 | 15:29 ET | HIS RULING: "Approved grok and I approve terra read" (mid-turn). Grok 365 X1 re-run approved, but my CONTINUE to `5b7147c4` was classifier-denied again: he types it there. Terra read: brain asked how (decoy .env). | APPROVED |
RULING 2026-10-11 R1107 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1107 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · e501ad3a2f473d05e732b8e03b9350c49cfd5459
RULING 2026-10-11 R1107 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, quoted whole:
```
clock · date · 0 · Sun Oct 11 15:35:11 EDT 2026
status · git status --short --branch · 0 · ## ops/terra-pass-prompt-1011
head · git log --oneline -1 · 0 · ffc704da docs(desk): card 367 X1 decoy row drafted
diff · git diff --stat ffc704da · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/terra-pass-prompt-1011 · 0 · ffc704da docs(desk): card 367 X1 decoy row drafted
env here · ls /Users/cobalt/cobalt-wt/terra-pass-prompt-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/.env
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat ffc704da` | 0 | `docs(desk): card 367 X1 decoy row drafted` · 2 files changed, 25 insertions(+), 2 deletions(-) |
| symbol `:29` | `grep -n -F "Run no command." "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` | 0 | `29:` (the template line, quoted under E2) |
| line count | `grep -c "" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` | 0 | `103` |
| `PLAIN_PROMPT` | `grep -n -F "PLAIN_PROMPT" ops/desk/bare-guard.py` | 0 | ``108:PLAIN_PROMPT = re.compile(r'"[^"\\$`]*"')`` · `1167:    if not PLAIN_PROMPT.fullmatch(command[len(prefix):len(command) - len(suffix)]):` |
| `builder_call` callers | `grep -rn -F "builder_call(" ops tests` | 0 | `ops/desk/bare-guard.py:1086` · `:1089` · `:1148` (def) |
| prompt readers (X4) | `grep -rn -F "Run no command" tests ops` | 1 | empty |
| READ `bare-guard.py:105-108`, `:1106-1122`, `:1148-1179` | Read tool | — | `WT_TOKEN` at `:105`, `PASS_PROMPT` at `:106`, `PLAIN_PROMPT` at `:108`; `builder_command` at `:1106`, `builder_call` at `:1148`. Both match the card |
| R1107 | `grep -n -F "\| R1107 " …/cto-2026-10-11.md` | 0 | `10:` … `\| APPROVED \|` (the card says `:9`; see RECORDS) |
| R1109 | `grep -n -F "\| R1109 " …/cto-2026-10-11.md` | 0 | `8:| R1109 | 15:35 ET | DESK RECORD (brain, L79) Terra read: codex may run read commands; out-of-worktree reads recorded, not STOP. …| DIRECTION |` (the card says `:7`) |
| RESTARTS | `uv run cobalt jobs restarts ffc704da..HEAD` | 0 | lists only this report (untracked, `A`, DOCS); `RESTARTS: none` |

The card's records, copied: drafter `draft-terra-pass-install` read against `ffb0e99c`. `grep -n -F "Run no command."` → `29:` only, and `grep -c ""` → 103: both re-read above and they hold. `builder_call` tests the typed prompt with `PLAIN_PROMPT` alone, and nothing in the guard reads `SHADOW-HUB.md:29`: re-read at `:1148-1179` and it holds. No test reads `Run no command`: re-read and it holds (empty). R1107 and R1109 are present, now at `:10` and `:8`.

## E0 BASELINE
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 718.25s (0:11:58)`. The two `COBALT_LIVE_VAULT_ROOT` skips are the live-note tests, which run below.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.45s`. The one skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, not `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
The card's `red first` is a set of greps, and `## NOT IN THIS JOB` fences off every test file, so no test file was written and nothing was committed at E2. Each grep below ran on `BASE`:
- `grep -c -F -e "Run no command." …` → `1`
- `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network" …` → `0`
- `grep -c -F -e "(GROK, SONNET)" …` → `0`
- `grep -c -F -e "Reads are not confined by workspace-write; accepted by HIS word 2026-10-11 (R1107)." …` → `0`
- `grep -n -F "Run <no command (GROK, SONNET) or only commands that read files; no command that writes, deletes or uses the network (TERRA)>." …` → empty
- negative control `grep -c -F -e "«SIGN" -e "«INSTALL" …` → `0`

## E3 THE ROWS
T1, Edit tool, `docs/40 - DevDocs/prompts/SHADOW-HUB.md` `:26` and `:29`. After the edit:
- `grep -c -F -e "Run no command."` → `0` ✓
- `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network"` → **`0`** (card: 1). See DECISION T1.
- `grep -c -F -e "(GROK, SONNET)"` → `1` ✓
- `grep -c -F -e "Reads are not confined by workspace-write; accepted by HIS word 2026-10-11 (R1107)."` → `1` ✓
- `grep -n -F "Run <no command (GROK, SONNET) or only … (TERRA)>."` → `29:` ✓
- `grep -c -F -e "«SIGN" -e "«INSTALL"` → `0` ✓
- `grep -c ""` → `103` ✓ · `git diff --numstat ffc704da -- …SHADOW-HUB.md` → `2	2` ✓
- `uv run pytest -q tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_authorize.py` → `1918 passed, 15 warnings in 72.55s` ✓

MUTATIONS, made and undone with the Edit tool:
- M1 put `:29` back to `Run no command.` → `grep -c -F "(GROK, SONNET)"` → `0` and `grep -c -F "Run no command."` → `1`: red. Undone.
- M2 removed the `:26` sentence → `grep -c -F "Reads are not confined …(R1107)."` → `0`: red. Undone.
- Undoing M2 also dropped the blank line `:27`. I restored it with the Edit tool. `git diff -U0 ffc704da` then showed hunks `@@ -26 +26 @@` and `@@ -29 +29 @@` only; numstat `2	2`; `grep -c ""` `103`.
- The four pytest files do not read this text (`grep -rn -F "Run no command" tests ops` is empty), so they stay green under any change to it. The greps are the row's test.

No module changed (one prompt file), so there is no DevDocs module line.
Commit `a790e54d feat(terra-pass-prompt-1011): Terra pass prompt may run read commands (T1, R1107, L72)`.

## RESTARTS
`uv run cobalt jobs restarts ffc704da..HEAD`, the table whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md	A	DOCS	-
RESTARTS: none
```

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames ffc704da` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (1 path, `docs/`). **`cobalt_dev: not taken (DB: none — 1 paths)`**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh terra-pass-prompt-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/terra-pass-prompt-1011-offline-20261011-155034.log`
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh terra-pass-prompt-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/terra-pass-prompt-1011-livenote-20261011-160232.log`
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3135 passed, 1 xfailed, 15 warnings in 632.57s (0:10:32)`
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/terra-pass-prompt-1011/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
1. Every red was shown: each card grep at E2 (on BASE), and mutations M1 and M2 at E3. No test file was added or changed.
2. Entry paths: the only reader of a pass prompt is `builder_call` (`bare-guard.py:1086`, `:1089`). It applies `PLAIN_PROMPT` to the typed prompt and never reads the template; `grep -rn -F "Run no command" tests ops` is empty. The new `:29` text has no `"`, `\`, `$` or backtick (read from the `git diff -U0` output). Whether `scan()` keeps a `;` inside double quotes is check ask X5. The guard's header says separators are seen only "OUTSIDE quotes", but no test was run for it here: the card fences off test files and no Python is listed.
3. Every count, line and quote above was re-read at `a790e54d`: `git diff -U0`, `--numstat`, `grep -c ""`, the greps, and `git log --oneline -1`.

## FOR THE CHECK
- `ffc704da..a790e54d`: `a790e54d feat(terra-pass-prompt-1011): Terra pass prompt may run read commands (T1, R1107, L72)`.
- T1: reds under E2, mutations and greens under E3. Callers: `bare-guard.py:1086`, `:1089`. Suites: offline 4199/0 (gate log above), live-note 146/0, `tests/ops` 3135 passed. With-DB: not run (DB: none). F0, F1, F2: not run (DB: none). Lock: not run (DB: none). The RESTARTS table is above.
- X3, filled: Terra → `Run only commands that read files; no command that writes, deletes or uses the network.` Grok and Sonnet → `Run no command.`
- X5: the build left this unproven (see self-check 2).

## CONTINUE
next: CLOSE (done)

## DECISIONS
- DECISION T1: the card's after-grep `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network"` → 1 cannot hold with the template text the same row prescribes. The template reads `Run <no command (GROK, SONNET) or only commands …`, so `Run` and `only` are never adjacent and the grep counts 0. That string exists only in the filled Terra prompt (X3). Safe default taken: the row's prescribed text, character for character. The grep stays 0, and every other grep holds. The check confirms the filled sentence.

## RECORDS
- The card cites R1107 at `cto-2026-10-11.md:9` and R1109 at `:7`. At HEAD they are at `:10` and `:8`: the file grew by one line. Both rows match the card's content.
- The baseline offline run created `.venv` in the worktree (uv, first run).
- An unneeded `git show a790e54d:ops/desk/bare-guard.py --stat` printed the file. It was a read and changed nothing.
- The L74 line is under `## L74`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: terra-pass-prompt-1011 · tip: a790e54d | on ffc704da | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 100980
