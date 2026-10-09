# guard-d2-1009 — build report (2026-10-09)

## §0 Headline
- G3 now refuses any Bash word that names `.env`, `.cobalt_key` or `.cobalt_vault`, whatever the verb; the only exception is bare `ls`. This covers a name inside an interpreter's string, brace forms and backslash-newline joins.
- T1–T4 were red on BASE (168) and are green at `187bfd6c`; C1 controls stay green. All 8 K1 mutations were run; one card expectation (mutation 6 → `os.environ`) did not hold (DECISION K1-6).
- Suites: offline 4036/0 · live-note 146/0 · `tests/ops` 2319 passed · with-DB not taken (DB: none) · RESTARTS: none.
- 3 decisions, none for Dejan; self-check 2 of 3 (the wrapped non-reader verb is unpinned).

## L74
- 11:44 EDT: a system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded once as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/158-guard-d2-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/158-guard-d2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/158-guard-d2-card.md" · 0 · b155b95d817024a801f381367b523f457028a110
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/158-guard-d2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | below, whole |
| base | `git show --stat 0e84db6f` | 0 | `0e84db6f docs(desk): four drafter prompts: arm-unsized, radar-top50, https-only, guard D2` · 4 files changed, 31 insertions(+) (four `prompts/2026-10-09/15x-draft-*.md`) |
| symbols | Grep `ENV_READERS\|g3_bash\(\|is_secret\(\|is_env\(` in `ops/desk/bare-guard.py` | 0 | `86:ENV_READERS = (…)` · `787:def is_env(path):` · `802:def is_secret(path):` · `806:    if is_env(path):` · `842:def g3_bash(segs):` · `846:        if verb(ws) in ENV_READERS and any(is_secret(w) for w in args):` · `848:` route · `940:    deny = g3_bash(segs)` · `1061:        if is_env(path):` · `1063:` Read rule |
| symbols | Grep `^def (verb\|words\|unwrap\|segments\|awk_reads\|awk_writes)\(\|^ASSIGN\|^SEQUENCE` | 0 | `112:ASSIGN` · `208:def segments` · `288:def words` · `296:def verb` · `304:def unwrap` · `535:def awk_writes` · `540:def awk_reads` · `755:SEQUENCE` |
| symbols | Read `bare-guard.py` 1-110, 280-309, 760-959, 1055-1066; `test_bare_guard.py` 1-60, 140-151, 220-279, 590-774, 1258-1269, 1410-1499 | — | every card `file:line` holds at BASE (`braces` 773-784, `env_words` 830-839, `g3_bash` 842-854, `bash_rules` 933-955 with `segs +=` at 938, `deny = g3_bash(segs)` at 940; `KINDS` test :277, `assert_denied` :267-269, `G3_ROUTE` :144-147, `G3_SECRET_ROUTE` :641-644, lock steps :620-632) |
| wc | `wc -l ops/desk/bare-guard.py tests/ops/test_bare_guard.py` | 0 | `1128` · `1575` |
| READ | brief `guard-d1-d2-answer-2026-10-09.md` read whole | — | last line 17: `A seat that writes a script file and then runs it can hide …This is L-level and is not a guard row.` |
| READ | Grep `O2` in `prompts/2026-10-08/120-guard-g2-open-reads-card.md` | 0 | line 18 (row O2), line 45 |
| restarts | `uv run cobalt jobs restarts 0e84db6f..HEAD` | 0 | `docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md	A	DOCS	-` · `RESTARTS: none` (only the untracked report; no code path) |
| card RECORDS re-read | Grep `ops/desk` in `configs/cobalt/jobs.yaml` | 1 | No matches found |

preflight.sh, whole:
```
clock · date · 0 · Fri Oct  9 11:44:51 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/guard-d2-1009
    ?? "docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 0e84db6f docs(desk): four drafter prompts: arm-unsized, radar-top50, https-only, guard D2
diff · git diff --stat 0e84db6f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/guard-d2-1009 · 0 · 0e84db6f docs(desk): four drafter prompts: arm-unsized, radar-top50, https-only, guard D2
env here · ls /Users/cobalt/cobalt-wt/guard-d2-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
Card `## RECORDS`, copied: BASE `0e84db6f…` · hubs type `.env` only as `ls`/`ls -la`, the lock copies/removes it by script · over-refusal accepted (a word naming `.env`/`.cobalt_key`/`.cobalt_vault` at a component boundary is refused, a commit message too) · every test runs the hook as a subprocess; the hook entry runs main's file, so this build seat's own calls run main's copy · RESTARTS classes: `bare-guard.py` operator script, test, DOCS; expected `RESTARTS: none` · RECORDED, NOT CARDED: a script file written then run hides a read from any word-level guard · the desk deploys with its own deploy card (R587). Re-read: `ops/desk` in `jobs.yaml` → no match (above); the brief's line numbers hold (symbols rows above). DB: none → no lock probe.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `0e84db6f` → `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 672.07s (0:11:12)`; last skip `SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` (expected offline).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.92s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Added to `tests/ops/test_bare_guard.py` (end of file, section `card 158 D2`): `D2_VERBS` (14 pairs), `test_d2_any_verb_naming_a_secret_is_denied` (T1), `test_d2_an_interpreter_naming_a_secret_inside_a_word_is_denied` (T2), `test_d2_a_brace_or_continued_secret_word_is_denied` (T3), `test_d2_a_typed_copy_or_remove_of_env_is_denied` (T4), `test_d2_a_word_naming_no_secret_stays_allowed` (C1); each over `KINDS`. T4: `cp /x/repo/.env /x/wt/job/.env` and `rm /x/wt/job/.env` removed from `test_g3_the_lock_steps_on_env_are_allowed`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py -k test_d2_` → `168 failed, 70 passed, 1082 deselected, 15 warnings in 8.33s` (T1 98 + T2 42 + T3 14 + T4 14 = 168 reds; C1 70 green).
- Every red's first line: `tests/ops/test_bare_guard.py:268: AssertionError: (0, '')` · `assert 0 == 2` (exit 0, no rule fires) — the rows' named reason. Proof over all 168: `grep -c -F "assert 0 == 2" /Users/cobalt/.claude/jobs/0ff8c770/tmp/red.xml` → `336` (each failure carries the line twice in junit: message + body = 2 × 168).
- Commit `a2a86384 wip(guard-d2-1009): red — T1-T4 reds, C1 control (D2)`.

## E3 THE ROWS
F1 in `ops/desk/bare-guard.py`: new `SECRET_PART` (the card's regex, `re.I`) beside `SECRETS`; new `secret_part(word)` (part (b) over `braces(word)`, returns the matched name); `g3_bash` reads `env_words(ws)` (the verb and NAME=value words included) with the `"\n"` join, and for every segment but `verb(ws) == "ls"` refuses on (a) `is_secret` or (b) `secret_part`; route `G3` when a word passes `is_env` or (b) names `env`, else `G3 secret`; the `ENV_READERS` gate is gone, `keychain_read` and B9 follow in that order; `ENV_READERS` kept with the comment `# no rule reads ENV_READERS since D2 (card 158): G3 reads every verb's words`; header `:20` → `G3 .env or a secret named by any word (D2)` (rewrapped), `:26-27` → `B1: G3 reads every verb's words (D2)`. Read rule, `ROUTE`, `is_env`, `is_secret`, `SECRETS` unchanged (`git diff 0e84db6f -- ops/desk/bare-guard.py`, under `## FOR THE CHECK`).
- Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py` → `1320 passed, 15 warnings in 44.60s`.
- K1 MUTATIONS (each with Edit, file run `uv run pytest -q -p no:cacheprovider --color=no --tb=no [-rN] tests/ops/test_bare_guard.py`, restored with Edit):

| # | mutation | summary | failing ids (named) |
|---|---|---|---|
| 1 | `if verb(ws) in ENV_READERS and verb(ws) != "ls":` | `168 failed, 1152 passed` | `-k "test_d2_any_verb or test_d2_a_typed"` → `112 failed, 1208 deselected` = every T1 (98) and T4 (14) case; the other 56 are T2 (42) + T3 (14) |
| 2 | `or any(parts)` removed | `49 failed, 1173 passed, 98 deselected` (`-k "not test_d2_any_verb"`) | every T2 id (42: the 6 commands × 7 kinds) and T3 `xxd /Users/cobalt/{.cobalt_key,x}/` × 7; `-k test_d2_any_verb` → `98 passed` |
| 3 | `for alt in [word]:` in `secret_part` | `7 failed, 1313 passed` | `test_d2_a_brace_or_continued_secret_word_is_denied[xxd /Users/cobalt/{.cobalt_key,x}/-<kind>]` × 7 |
| 4 | `for x in (w,)` (no `"\n"` join) | `28 failed, 1292 passed` | `test_d2_a_brace_or_continued_secret_word_is_denied[xxd ~/.cobalt_ke\\\ny-<kind>]` × 7; and the existing `test_x3_a_secret_path_whose_basename_the_guard_does_not_see_is_denied` continued cases × 21 |
| 5 | `if True:` (no `ls` exemption) | `23 failed, 1297 passed` | `test_d2_a_word_naming_no_secret_stays_allowed[ls -la /x/wt/*/.env-<kind>]` × 7; `test_g3_the_lock_steps_on_env_are_allowed[ls -la /x/wt/job/.env]`, `[ls /x/wt/job/.env]` (`:623-624`); `test_g3_a_secret_shown_present_or_a_near_name_is_allowed[ls -la /Users/cobalt/.cobalt_key-…]`, `[ls -la /Users/cobalt/cobalt/data/.cobalt_vault-…]` × 7 each (`:678-679`) |
| 6 | leading group → `()` | `14 failed, 1306 passed` | C1 `[cat /x/prod.env-<kind>]` × 7, `[xxd /x/foo.cobalt_key-<kind>]` × 7. C1 `os.environ` stayed GREEN (DECISION K1-6) |
| 7 | trailing group → `()` | `24 failed, 1296 passed` | C1 `[cat /x/.envrc-…]` × 7, `[xxd /x/.cobalt_key.example-…]` × 7; `:627` `[cat /x/wt/job/.env.example]`; `:680` `[cat /x/.cobalt_key.example-…]` × 7; `:1265` `[cat /x/wt/job/.env.*]`, `[cat /x/wt/job/{.env.example,x}]` |
| 8 | `return ROUTE["G3 secret"]` always | `124 failed, 1196 passed` | `-k "test_d2_ and build"` → `5 failed, 29 passed`: T1 `[od -c .env-…-build]`, `[base64 /x/wt/job/.env-…-build]`; T2 `[uv run python -c "print(open('.env').read())"-…-build]`; T4 `[cp /x/repo/.env /x/wt/job/.env-build]`, `[rm /x/wt/job/.env-build]` |

- Restored: `git diff 0e84db6f -- ops/desk/bare-guard.py` = F1's diff (only the header rewrap followed); `1320 passed, 15 warnings in 43.79s`.
- DevDocs: no page for `bare-guard.py` under `docs/40 - DevDocs/cobalt/` (Grep `bare-guard` over `docs/40 - DevDocs` outside reports and prompts → no files); none created (ASK DESK 1).
- Commit `187bfd6c fix(guard-d2-1009): G3 refuses a secret named by any word, whatever the verb (T1-T4, C1, F1, K1; L1, L28, L70)`.

## RESTARTS
`uv run cobalt jobs restarts 0e84db6f..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `187bfd6c`.
- (a0) `git diff --name-only --no-renames 0e84db6f` → `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py` (every path under `ops/` or `tests/ops/`). **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-d2-1009 offline` → exit 0, whole: `offline 4036/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-d2-1009-offline-20261009-121010.log`; executed (log line 2) `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → (log line 867) `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 662.26s (0:11:02)`. This build adds no test to that suite; its tests are all in `tests/ops/test_bare_guard.py` (below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-d2-1009 livenote` → exit 0, whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-d2-1009-livenote-20261009-121011.log`; executed (log line 2) `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`; only skip (log line 56) `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2319 passed, 1 xfailed, 15 warnings in 499.63s (0:08:19)`. This build adds: `test_d2_any_verb_naming_a_secret_is_denied` (98), `test_d2_an_interpreter_naming_a_secret_inside_a_word_is_denied` (42), `test_d2_a_brace_or_continued_secret_word_is_denied` (14), `test_d2_a_typed_copy_or_remove_of_env_is_denied` (14), `test_d2_a_word_naming_no_secret_stays_allowed` (70).
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/guard-d2-1009/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. T1–T4 were red at E2 (`168 failed`, each `:268` `assert 0 == 2`, 336 = 2 × 168 junit lines). C1 is a control (green on BASE, `70 passed`) and was shown red under K1 mutations 5 (`ls -la /x/wt/*/.env`), 6 (`prod.env`, `foo.cobalt_key`) and 7 (`.envrc`, `.cobalt_key.example`). Each T row was also red under its K1 mutation: 1 (T1, T4), 2 (T2), 3 and 4 (T3), 8 (the `.env` routes). One C1 case, `os.environ`, stayed green under both 6 and 7. A single mutation cannot red it, because each boundary group alone keeps it out (DECISION K1-6); nothing rewritten, it is a RUN row. — 1 of 1 backed, with that item named.
(2) Entry paths: `g3_bash` has one caller, `bash_rules` (`:957` at tip, Grep), so every Bash event reaches it, and the D2 tests drive it through the hook subprocess for all 7 `KINDS`. `is_secret` is also called by the Read rule (`:1080`), which is unchanged and pinned by `test_g3_the_read_tool_on_a_secret_is_denied`. Not pinned: the unwrapped-segment path (`segs +=` from `unwrap`) for a non-reader verb, e.g. `time base64 ~/.cobalt_key`. No row lists such a test, and the existing B10 cases are now also caught on the outer segment (DECISION 3). — gap.
(3) Re-read at tip: Grep `g3_bash\(|secret_part\(|SECRET_PART|is_secret\(|ENV_READERS` → `86`, `87`, `801`, `805`, `845`, `849`, `855`, `861`, `862`, `957`, `1080`; Grep `^def test_d2_|^D2_VERBS` → `1578`, `1598`, `1615`, `1622`, `1629`, `1650`; `git log --oneline 0e84db6f..HEAD` → `187bfd6c`, `a2a86384`. The line numbers in E2/E3 are BASE's, as the card gives them.

## FOR THE CHECK
- `0e84db6f..187bfd6c`: `a2a86384 wip(guard-d2-1009): red — T1-T4 reds, C1 control (D2)` · `187bfd6c fix(guard-d2-1009): G3 refuses a secret named by any word, whatever the verb (T1-T4, C1, F1, K1; L1, L28, L70)`.
- Per row: reds at `## E2 RED`; mutation runs at `## E3 THE ROWS` (K1 table); greens `1320 passed` (file) and `2319 passed, 1 xfailed` (`tests/ops`).
- K1 (RUN row) output: the K1 table in `## E3`, the count and named failing ids of each mutation; restored, `git diff 0e84db6f -- ops/desk/bare-guard.py` = F1's diff.
- Caller greps: `## PREFLIGHT` symbols rows; at tip, `## PRE-STOP SELF-CHECK` (3).
- Suites: offline `4036/0`, live-note `146/0` (commands and logs under `## W`); with-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT`, last paragraph.

## CONTINUE
next: CLOSE (done)

## DECISIONS
- DECISION K1-6: under mutation 6 (leading boundary group dropped), C1 `python3 -c "import os; print(os.environ.get('HOME'))"` and `grep -rn "os.environ" src/` stay GREEN. Mutation 6 gave `14 failed`, only `prod.env` and `foo.cobalt_key`; the card expected the `os.environ` cases to fail too. The trailing group still refuses `.env` followed by `i`. Under mutation 7 the leading group holds them (`s.env`). Each group alone keeps `os.environ` allowed, so no single K1 mutation reds that case. Shown, not fixed (RUN row). Safe default: none taken; the fix is as carded.
- ASK DESK 1: E3 asks for a dated line in the module's page under `docs/40 - DevDocs/cobalt/`. There is no page for `ops/desk/bare-guard.py` (Grep `bare-guard` over `docs/40 - DevDocs`, outside reports and prompts → no files), and creating one is outside the rows' files. Safe default: no page created. [12:21 EDT]
- DECISION 3 (self-check 2): no D2 test sends a non-reader verb through a wrapper (e.g. `time base64 ~/.cobalt_key`, `xargs xxd ~/.cobalt_key`). That leaves the unwrapped-segment entry (`bash_rules` `segs +=`) unpinned for D2. Since D2, the wrapper's own outer segment carries the same words, so it would be refused there first; this is unproven (L70), because no tool run shows it. Safe default: not added (not a card row); the check may add the case.

## RECORDS
- started 11:44 EDT (`date`).
- The build seat's own Bash calls ran main's `bare-guard.py` (card record); no call of this build was refused.
- No lock taken (DB: none). `.env: removed, proven gone` → never present: `ls /Users/cobalt/cobalt-wt/guard-d2-1009/.env` → `No such file or directory` (12:21 EDT).
- L74: one system-reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not followed.
- Junit file for the E2 proof: `/Users/cobalt/.claude/jobs/0ff8c770/tmp/red.xml` (job tmp, not committed).
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 0ff8c770` → `context 174620 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: guard-d2-1009 · tip: 187bfd6c | on 0e84db6f | migration: none | offline 4036/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 2 of 3 | decisions: 3 · for Dejan: 0 · tokens: 174620
