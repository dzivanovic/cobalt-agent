# Guard D1 draft · 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/162-guard-d1-card.md` written: JOB `guard-d1-1009`, BASE `1458693d`, one seam (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`).
- Rows: T1 (10 hidden spellings), T2 (`--allow-prod`), C1 (`prod_read` the one pass), C2 (dev commands; deploy and unknown seats), F1 (G2-W), K1 (7 K25 mutations).
- Two departures from the brief, each a decision: the option test is a `prod` token, not a substring (keeps `uv run cobalt --products` green); the brief's `env COBALT_ENV=production` already fails on BASE, so T1 uses the quoted form.
- Builds after D2 deploys.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/162-guard-d1-card.md`

## DECISIONS
- D1 · ASK DESK: D1 and D2 both edit `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`. Build D1 after D2 deploys? [11:40 EDT] Default taken: yes. At launch the desk sets `BASE` to main HEAD after the D2 merge. The build rebases its tests onto D2's and re-proves each `file:line` by symbol.
- D2 · ASK DESK: the brief's option clause "starts `-` and its lower case contains `prod`" would refuse `uv run cobalt --products`, a green control at `tests/ops/test_bare_guard.py:410-413`. Narrow it? [11:40 EDT] Default taken: `PROD_OPTION` matches `prod` as a token (`--allow-prod`, `--prod=1`, `-prod`). K1 mutation (5) proves the narrowing.
- D3 · ASK DESK: the brief's `env COBALT_ENV=production …` holds the literal, so `PROD.search` already refuses it on BASE. It cannot be a red. Swap it? [11:40 EDT] Default taken: T1 uses `env COBALT_ENV="production" …` (check `:236`). The literal form stays a passing denial (`:502`).
- D4 · ASK DESK: the check's `COBALT_ENV=product\<newline>ion` needs the backslash-newline join, which the brief names only for D2. Add it to `prod_word`? [11:40 EDT] Default taken: yes (mirrors `g3_bash` `:844-845`). K1 mutation (3) pins it. The check's `COBALT_ENV=prod{uction,uction}` is not production in bash, because an assignment word is not brace-expanded. T1 uses the `env` operand form instead.
- D5 · ASK DESK: argparse lets a prefix of an option through: `db migrate --allow` reaches `cobalt_brain` and `db query --pr` reaches production, and neither contains the word `prod`. Card it? [11:40 EDT] Default taken: record it, don't card it (R707: no more variant rounds). The cause is in `src/` (`allow_abbrev`), outside this seam.
- D6 · ASK DESK: the order sets `REPORT` to a main path. `CARD.md` and card 158 put a build's report inside its worktree. Keep it? [11:40 EDT] Default taken: kept as ordered, `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md` (absent at 11:3x EDT).

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `1458693dbde5371259a29c5d502d74e3878fee3b` (11:38 EDT).
- `git -C /Users/cobalt/cobalt diff --stat 0e84db6f HEAD -- ops/desk src/cobalt tests/ops` → empty, so D2's BASE and this BASE carry the same guard.
- `git -C /Users/cobalt/cobalt show HEAD:ops/desk/bare-guard.py`, lines read: 1-125 (header `:20-21`, `ROUTE["G2"]` `:57`, `ENV_READERS` `:86`, `PROD` `:111`, `ASSIGN` `:112`), 126-200 (scanner, backslash `:167-169`), 200-345 (`segments`, `ansi_c`, `unquote_ansi_c` `:254`, `words` `:288-293`, `verb`, `unwrap` `:304`), 755-958 (`braces` `:773-784`, `is_secret` `:802`, `g3_bash` `:842-854`, `PROD_READ` `:891`, `prod_read` `:895-930`, `bash_rules` `:933`, segs `:935-938`, G2 `:943-944`). The brief's numbers hold.
- `git -C /Users/cobalt/cobalt show HEAD:tests/ops/test_bare_guard.py`, lines read: 53-66, 143, 263-280, 387-415, 462-486, 489-590 (by grep), 1156-1172.
- `src/cobalt/db_migrations/cli.py:1060-1095` (`--allow-prod` `:1078`); `src/cobalt/db_query.py:200-216` (`--prod` `:212`). Grep `allow_abbrev|--prod|--allow-prod` in `src` finds no `allow_abbrev`.
- `reports/guard-g2-open-reads-check-2026-10-08.md:165,184,230,236` (D1's spelling list and the B1 output `(0, '')`).
- `prompts/CARD.md`, `prompts/2026-10-08/120-guard-g2-open-reads-card.md`, `prompts/2026-10-09/158-guard-d2-card.md`, `reports/guard-d1-d2-answer-2026-10-09.md`, `topics/writing-rules.md`: read whole.
- `grep -n "bare-guard" /Users/cobalt/.claude/settings.json` → `:22`.
- RESTARTS classes: `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing (11:38 EDT). `ops/desk/bare-guard.py` is an operator script, `tests/ops/test_bare_guard.py` is a test, both reports are DOCS. Expected `RESTARTS: none`.
- Recorded, not carded (brief): a script file the seat writes and then runs hides a production verb from any word-level guard. The wall is structural.
- No test or mutation was run. Every red reason is read from the code (L70).

GUARD D1 CARD DRAFTED · decisions: 6
