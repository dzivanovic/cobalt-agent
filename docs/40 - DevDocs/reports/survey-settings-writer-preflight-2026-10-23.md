# Survey prompt 1017 — preflight (read-only), main d1e735b3

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read the launch line of 1017; `bare-guard.py:992-1031` (`prod_read`), `:161` PROD | Allowed: `Read Grep Write`, the two `COBALT_ENV=production uv run cobalt db query --side user\|system --prod *` strings, `ls grep tail cut sort uniq wc date`, `git -C … log\|show\|grep`. `PROD_READ` words `COBALT_ENV=production uv run cobalt db query` + exactly one `--prod` + `--side` in {user,system} (`:992-993,1013-1023`) = the two strings, and the P1-P3 form `… --side X --prod --format json "<sql>"` passes (no `--prod=`, no `cobalt_brain`, no brace words, no `\`-newline). No db write, `settings load`, migrate, lock script, `rm`; `awk`, `git commit*`, `git push*`, `cobalt settings*`, migrate, pytest and the lock script are disallowed | OK |
| 2 | `db_query.py:209-215` flags; `:20-28` refused words/functions; grep for `%` in P1-P3 | Flags used: `--side`, `--prod`, `--format json` (all accepted; `--limit` unused). P1-P3 are one SELECT each (`:98-103`), no refused word (`AT TIME ZONE`, `IN`, `strpos` are not on the list), no `;`, no `%` | OK |
| 3 | `git diff --stat main` on cited paths (empty) + `git grep` on main | Proved: `0001_trader_settings.sql:29,45`; `store.py:60,91,96-98,106`; `cli.py:76,100,104,113,207,237,317`; `card.py:61,67,296-303,322,324-325`; `web.py:1328,1343,1365-1368`; `notes.py:724,737,747-749`; `runner.py:320`; `0004_radar_pool.sql:74`; `models.py:54,232,236-247`; `env.py:38,44,78`; `db_query.py:98-103,156-158,209-215`; `bare-guard.py:996-1031`; `radar.err:90820` (log, first hit) | OK |
| 4 | Q1-Q4 against allowed reads | Q1 = P1+P3; Q2 = P2 + `Grep`/`git grep` + `grep`/`cut` on logs + `Read` of reports; Q3 = `Read` of `ops/desk/*.sh` (all five exist) + the two reports; Q4 = P1 + `grep` of `replay.log`. None needs a write | OK |
| 5 | `Write` scope; last line | The prompt says `Write` touches the report only (path named, absent today). Last line `SURVEYED · cause: … · decisions: <n>` or `FAILED: <reason>` | OK |
| 6 | `ls -a .env` only; prompt text | `.env` exists; the prompt forbids opening it and no allowed read targets it | OK |
| 7 | prompt text | No restore, fix or launch; the restore is stated as text only, "run nothing" | OK |

## ISSUES
- NOTE: the replay error quoted in FACTS ("`radar.benchmark top_n missing`") is not the missing-row text (`models.py:240`); a row that is a mapping without `top_n` raises the `invalid radar.benchmark` pydantic error (`:253`). The seat should read P1's `vtype`/`raw` before it assumes the row is absent.
- NOTE: `Write` and `grep *` cannot be path-scoped in `--allowedTools`; the report-only and no-`.env` limits rest on the prompt text and guard G3.
- NOTE: P1 prints the raw `radar.cards_enabled` and `radar.benchmark` values; the prompt asks for that and routes it to §0.

Blocks the launch: nothing.

PREFLIGHT DONE · prompt: 1017 · checks: 7 · fails: 0 · ready: YES
