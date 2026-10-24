# K3 restore cards 1029 and 1030 — preflight (read-only, 2026-10-24)

## CHECKS

| # | card | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | 1029, 1030 | read both cards; `ls` both REPORT paths; `git rev-parse 1ef351db HEAD`; `git diff --stat 1ef351db HEAD -- . ':(exclude)docs'`; `grep FILL` | TAG empty, CLASS K3, BRANCH main, WORKTREE none, BASE `1ef351db` (8 hex, ancestor of HEAD `433b2e10`), diff outside docs/ empty; both `prodwrite-restore-*.md` REPORTs absent (ls: no such file); WRITE RULING `2026-10-24 R2412` (one row); no resume step; no FILL token | OK |
| 2 | 1029, 1030 | `grep -n "^| R2412 "` on `reports/cto-2026-10-24.md`; `git log -1 -S"R2412" -- <file>` | line 7: `HIS RULING · APPROVED …`, 1 row; committed in `1ef351db` | OK |
| 3 | 1029 | `## ROWS` | one data row, 7 cells (9 awk fields); command starts `COBALT_ENV=production uv run cobalt settings load`, has `--apply`, sha256 `5993c57f54db17101cf22704508801cef8b7fcee9c832b08ac12f63936fbfc17` = survey Q5 digest in full; none of the refused characters; verb `settings load`, not db migrate/query/dev-rebuild/backup | OK |
| 3 | 1030 | `## ROWS` | one data row, 7 cells; command as above with `--optional`, sha256 `10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880` = survey Q5 digest in full; no refused characters | OK |
| 4 | 1029 | table, count read, expected, backup, inverse | table `user.trader_settings`, named whole in the read (`'user.trader_settings'`); read is `db query --side user --prod`, no `%` `$` backtick; expected `1`; backup exactly `COBALT_ENV=production uv run cobalt backup run`; inverse `none` | OK |
| 4 | 1030 | same | same shape; key `radar.benchmark`, `strpos(source, 'optional:radar-benchmark.yaml') = 1`; expected `1`; backup exact; inverse `none` | OK |
| 5 | 1029 | `ls` of the htf file | `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml` exists; card says "no dry run" and has no `--dry-run` | OK |
| 5 | 1030 | `ls` of the benchmark file | `data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml` exists; no `--dry-run` | OK |
| 6 | 1029, 1030 | read | 1029 writes only `radar.cards_enabled`; 1030 writes only `radar.benchmark`; one write each, no card restores both | OK |
| 7 | 1029, 1030 | read RECORDS | each says the write is refused 20:00–21:00 ET (`src/cobalt/session/guard.py:67`); nothing claims the window away | OK |
| 8 | 1029, 1030 | read | the card text runs only the one `--apply`; the count read and backup are the hub's steps; no launch, db migrate or other write | OK |

## ISSUES
- NOTE: not read, for speed: `reports/draft-restore-cards-2026-10-24.md` (the 8 decisions). Nothing in the card text conflicts with them.
- NOTE: not re-hashed (no hashing command allowed). The write's `--sha256` check refuses a file whose bytes hash differently, so a wrong file writes nothing.
- NOTE: the `source` and `key` columns the count reads use exist (`src/cobalt/settings/store.py:48,96`). The source labels match the code (`card.py:324`, `cli.py:218`).
- NOTE: at launch the launcher also refuses if a deploy-hub- or prodwrite- session is live. Run 1029 first, then 1030 after it ends `WRITTEN`. Launch outside 20:00–21:00 ET.
- NOTE: the working tree has uncommitted changes. They are all under docs/ or `.claude/`, and the launcher excludes docs/ from the BASE check. 1029 and 1030 themselves are committed.
- Blocks the launch: nothing.

PREFLIGHT DONE · cards: 1029, 1030 · checks: 11 · fails: 0 · ready: YES
