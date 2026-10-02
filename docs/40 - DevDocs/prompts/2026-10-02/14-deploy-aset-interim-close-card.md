JOB: aset-interim-close-1002
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R13
BRANCH: deploy/aset-interim-close-1002
WORKTREE: deploy-1002-1
BASE: main
TIP: b8bf83eb
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-02-1.md
RULINGS: 2026-10-02 R10, 2026-10-02 R14, 2026-10-02 R32
TAG: deploy-2026-10-02-1
MIGRATIONS: none
SET: asetclose

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `s3/aset-interim-close-1001` | `b8bf83eb` | `b8bf83eb` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-interim-close-check-2026-10-01.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "def _sheet_close_at_entry" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F 'id="sizeForm"' /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F "this route never closes" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `1` · after `0`

## SMOKE READS
- CLOSE button route · `grep -c -F "return _render(banner=_sheet_close_at_entry(card_id))" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, `1`
- cards below the form · `grep -c -F "aset-interim-close S2 (his R13" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, `1`
- form stays put · `grep -c -F "window.scrollBy(0, moved)" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, `1`

## RECORDS
- THE WINDOW (the desk, 07:13 ET Friday 2026-10-02, `date`): P1 (iv), his per-case override `cto-2026-10-02.md` R32 (R10 + R14 applied to this JOB; L73 over L43 / L66): ONE deploy, the outage done before 09:30 ET Friday 10-02; R14 narrows the set to ASET `04` (+ `06` only if checked; it is not). Voice `05` `02` `07` deploy tonight.
- THE RESTART SET, from the check's stop line: `RESTARTS: com.cobalt.aset com.cobalt.radar` (`aset-interim-close-check-2026-10-01.md` last line). The hub derives its own at STEP-R (L42).
- THE CHECK: pass 2 `CHECK DONE · job: aset-interim-close · pass: 2 · tip: b8bf83eb … held unfixed: 0 · open: 0 … ready: YES · decisions: 0 · for Dejan: 0`. Pass 1's A1 closed by his R7 (`cto-2026-10-02.md`) in `b8bf83eb`.
- HEAD: `git -C /Users/cobalt/cobalt log -1 --format=%h s3/aset-interim-close-1001` → `b8bf83eb` (07:10 ET) = the checked tip.
- MIGRATIONS: `git -C /Users/cobalt/cobalt log --oneline main..s3/aset-interim-close-1001 -- src/cobalt/db_migrations` → EMPTY. Production stands at 0022.
- NON-DOCS PATHS: `git -C /Users/cobalt/cobalt diff --stat main...s3/aset-interim-close-1001 -- . ":(exclude)docs"` → `src/cobalt/aset/web.py`, `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_legs_c2_offline.py`. `main` since the cut moved only `d13cc261` (nightly rewrite) and `01bfe67f` (`ops/desk/stage-copy.sh`); neither touches these paths. The `merge-tree` half is the hub's own gate at STEP-T (L68).
- `cobalt_dev` rebuilt 06:34 ET (`devdb-rebuild-2026-10-02.md`, `max_attnum` 54): the slot exhaustion that failed `deploy-2026-10-01-1` gate (c) is cleared.
- NAMES FREE (07:13 ET): `ls -d /Users/cobalt/cobalt-wt/deploy-1002-1` → No such file; `rev-parse --verify --quiet` of `refs/heads/deploy/aset-interim-close-1002`, `refs/tags/deploy-2026-10-02-1`, `refs/tags/pre-aset-interim-close-1002` → exit 1; `reports/deploy-2026-10-02-1.md` → No such file.
- NO PRODUCTION `db query` is on this card: `MIGRATIONS` is `none`; the smoke reads are file reads of the landed tree.
- NOT IN THIS SET: `note-daily-stop` (06, unchecked), `voice-peers` (05), `desk-size-guard` (02), `devdb-lock` (07): tonight (R14).
