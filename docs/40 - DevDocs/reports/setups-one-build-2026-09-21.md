# SETUPS ONE BUILD — report 2026-09-21

Prompt: `docs/40 - DevDocs/prompts/2026-09-21/65-setups-one-build.md` · branch `setups/seven-0921` · worktree `/Users/cobalt/cobalt-wt/setups-c1` · started `Mon Sep 21 20:13:03 EDT 2026` (`date`).

## §0 Headline

- FAILED PREFLIGHT before any edit, `.env` copy or DB contact: the session runs in AUTO MODE. L29 ("never auto mode on a write path"), this prompt ("NOT auto mode … the launch line carries NO `--permission-mode`"), R41 and R50 ("NO auto mode") all forbid it for this write-path build.
- AUTHORIZATION: every row verified and committed; R2-4 = B (R50). All 20 rule strings + triplet counted 1.
- Nothing built, nothing changed in `src/`; only this report is committed. ESCALATE: 1.

## L74

The first tool result of this session (the Bash read of the prompt) carried an appended block asking for a `Claude-Session:` line in commits and naming a file-send tool. Recorded once as DATA (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` only.

## AUTHORIZATION

| check | command | result |
|---|---|---|
| R15 row | `grep -n "^| R15 " …cto-2026-09-21.md` | line 27, carries `13 definitions is the correct number` |
| R15 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"13 definitions is the correct number" -- …` | `c915784fc15b45d57312e6cfe020cf85c5ba30b7` |
| R24 row | `grep -n "^| R24 " …` | line 35 present |
| R40 row | `grep -n "^| R40 " …` | line 51, carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| R40 committed | `-S"ONE EXTRA DOT THAT CANNOT BE TAPPED"` | `23fb828e5e87ffc240506ac07043a18345a1ea26` |
| R44 row | `grep -n "^| R44 " …` | line 55, carries `ONE BUILD of the whole FINAL` |
| R44 committed | `-S"ONE BUILD of the whole FINAL"` | `bf4e78798124e9896f812e4d3487f34f25989102` |
| R45 row | `grep -n "^| R45 " …` | line 56, carries `ADDING-A-SETUP.md` |
| R45 committed | `-S"ADDING-A-SETUP.md"` | `b56efc5624c39e33e6c3564cc20d30ef1bcd89a4` |
| R41 row | `grep -n "^| R41 " …` | line 52, quotes both `.env` strings and `"Approved"` |
| R41 committed | `-S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` | `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| launch row | `grep -n "65-setups-one-build.md" …cto-2026-09-21.md …cto-2026-09-22.md` | `cto-2026-09-22.md`: No such file (recorded, not fatal); line 62 `\| R50 \| 18:20 ET \|` carries `**R2-4 = B**` (one literal) and "NO auto mode" |
| launch row committed | `-S"65-setups-one-build.md"` | `b56efc5624c39e33e6c3564cc20d30ef1bcd89a4` |
| R25 (09-20) | `grep -n "^| R25 " …cto-2026-09-20.md` | line 262, names `11-bars-chunk-2-build.md`, "approved" |
| R18 (09-19) | `grep -n "^| R18 " …cto-2026-09-19.md` | line 31, carries `approve env` and `Bash(COBALT_ENV=dev uv run pytest *)` |
| 16 allow + 3 deny strings | `grep -c -F -e "<rule>" …02-bars-chunk-2-fix-r3.md`, one call each | every count `1` |
| `--add-dir` triplet | same file | `1` |
| `"Bash(COBALT_ENV=dev uv run pytest *)"` | `…2026-09-19/44-archiver-db-rerun.md` | `1` |

R2-4 = B.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 21 20:13:03 EDT 2026` |
| porcelain | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/setups-one-build-2026-09-21.md"` (this report only — written first, as the prompt orders) |
| long status | `git status` | 0 | `On branch setups/seven-0921` / `nothing to commit, working tree clean` (before the report was written) |
| branch tip | `git log --oneline -1` | 0 | `5b208a0 docs(report): deploy 2026-09-21b degraded line …` (first launch) |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `2834a5a docs(desk): 09-21 deploy-2026-09-21b live, …` — main moved after the cut; both recorded |
| tag | `git -C /Users/cobalt/cobalt log -1 --format=%H deploy-2026-09-21b` | 0 | `ad7d3e41e0275ebabf4ebdeac818f5827b9e77f1` |
| tag under cut | `git log --oneline HEAD..deploy-2026-09-21b` | 0 | empty |
| branch moved | `git log --oneline main..HEAD` | 0 | empty |
| `.env` | `ls -la .env` | 1 | `ls: .env: No such file or directory` |
| **permission mode** | session system context | — | **AUTO MODE ACTIVE** — the session's own system prompt states "auto mode is active". L29: "never auto mode on a write path"; this prompt: "NOT auto mode … the launch line carries NO `--permission-mode`"; R41 / R50: "NO auto mode". → **FAILED PREFLIGHT** |

Not run (stopped at the failed row, nothing started): the Lego baseline grep, the four consumer greps, `uv run pytest --version`, `uv run cobalt jobs restarts main..HEAD`, `mkdir -p` probe, the `cobalt_dev` reachability step (`.env` never copied).

## BASELINE

Not run — PREFLIGHT failed.

## ESCALATE

1. **Launch defect: this session runs in auto mode.** The build touches `cards/store.py` `tap_dot`, the tunables sync and possibly a migration — a write path (L29). L62: a wrong launch is stopped and rerun with corrected information, never patched from inside. Fix: relaunch with the same line in a session whose permission mode is the allowlist default (check the user/project `settings.json` `defaultMode` — a default of `auto` would override the line's intent), then the same prompt resumes from `## CONTINUE`.

## CONTINUE

next: relaunch in a non-auto session → STEP-0 PREFLIGHT from the top (AUTHORIZATION above already verified at 20:13 ET; re-verify on relaunch). Nothing else committed but this report.

FAILED PREFLIGHT: L29 — session launched in auto mode on a write-path build (prompt, R41, R50: "NO auto mode")
