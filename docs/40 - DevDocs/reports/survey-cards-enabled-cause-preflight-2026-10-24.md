# Survey prompt 1038 — preflight (read-only), main ef71bc52

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log` + `git diff --stat main` on 1038; `Read` of 1038 line 1; `desk-launch.sh:738-850` rules (grep) | 1038 committed in `ef71bc52`, diff vs `main` empty. One launch line, read by absolute path, `--permission-mode auto`, `--remote-control`+`--name`, `AskUserQuestion`,`EnterWorktree` denied, cwd `/Users/cobalt/cobalt` named. `--allowedTools` holds exactly one production string `Bash(COBALT_ENV=production uv run cobalt db query *)` (the one string `desk-launch.sh:815` passes). Every other `COBALT_ENV=`, `awk`, `git commit`, `settings`, `take-devdb-lock.sh` sits in `--disallowedTools` only. Allow list has no `shasum`, `awk`, `git add/commit/merge`, `Bash(git *)`, `launchctl`, `$`, backtick or `\`. `^RULINGS:` count = 1, line 2 `RULINGS: 2026-10-08 R686`; `main:reports/cto-2026-10-08.md:39` is `\| R686 \| … HIS RULING … APPROVED · HIS RULING` naming production reads | OK |
| 2 | `Read` + `git grep` on `main`; `git diff --stat main` on the 7 source files | Empty diff for `notes.py`, `runner.py`, `web.py`, `radar_panel.py`, `card.py`, `cli.py`, `guard.py`. Proved: `card.py:149` `cards_enabled: bool`, `:170` `from_rows`, `:196` `invalid card settings`, `:198` `rows`, `:201` writes the bool, `:236-237` `current()`, `:240-276` `load_card_file`; `notes.py:711-720` tombstone, `:724` `mirror_sources`, `:732-733` market_reset refusal, `:736-745` `unchanged`; `runner.py:320` `mirror_sources(`; `web.py:903-913` `/radar`; `radar_panel.py:949-975` `build_radar_panel`; `cli.py:76` `apply_settings`; `reports/prodwrite-restore-cards-enabled.md:74,78-80,85,86` match the prompt; `session/guard.py` exists. `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml` present (ignored, named as such); packet copy named untracked by the prompt | OK |
| 3 | Q1-Q5 against the allowed reads | Q1 = P1. Q2 = `Read` of the backup yaml. Q3 = `Read`/`Grep`/`git log`. Q4 = `grep`/`tail` on `logs/`, `Read`. Q5 = synthesis. None needs a write, a load or a hash command. P1 is one SELECT with no `%`; its words (`SELECT AS FROM WHERE IN ORDER BY AT TIME ZONE`, `jsonb_typeof`) are none of `REFUSED_WORDS`/`REFUSED_FUNCTIONS` (`db_query.py:20-28`). The only `%` in 1038 is the rule text "No `%` in a query string" (line 1). The only `awk` is "Never `awk`". No `shasum` anywhere in 1038 | OK |
| 4 | `Read` 1038 lines 1, 5, 40; `ls` | `Write` touches the report only (`reports/survey-cards-enabled-cause-2026-10-24.md`, absent: `ls` exit 1). Stop line is `SURVEYED · cause: <code\|data> · decisions: <n>` or `FAILED: <reason>` | OK |
| 5 | prompt text | "Never read or print a secret; never open `.env`"; no allowed read targets `.env`. P1 selects only `radar.cards_enabled` and `radar.benchmark` | OK |
| 6 | prompt text | "no database write, no `settings load`, no migrate, no code, no git write, no launch (L36)"; the loader and any hashing command are named as never run; restores and loads nothing | OK |

## ISSUES
- NOTE: `web.py:903-913` and `radar_panel.py:949-975` show no `CardSettings` read; the call that raises `CardSettingsError` on `/radar` is not on the cited lines (`web.py:1817` `CardSettingsReader().current()` is a POST `/radar/card/{id}/dot/{factor}` route, not `/radar`). Q3 already tells the seat to trace it; the seat needs `Grep`, which is allowed.
- NOTE: `Write`, `grep *`, `cut *` cannot be path-scoped in `--allowedTools`; the report-only and no-`.env` limits rest on the prompt text, as in 1022.
- NOTE: the survey must read P1 whole in one `db query`; the guard (`bare-guard.py`) refused one of my own non-prompt commands that named production in text, so the seat should type P1 exactly as written.

Blocks the launch: nothing.

PREFLIGHT DONE · prompt: 1038 · checks: 6 · fails: 0 · ready: YES
