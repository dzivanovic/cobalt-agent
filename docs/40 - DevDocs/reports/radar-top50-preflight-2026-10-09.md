# radar-top50 preflight — 2026-10-09

Card `154-radar-top50-card.md`, read at main `1458693d`. Read-only: no test was run, so "red on BASE" is proved by reading the code.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 0a | card path vs `desk-launch.sh:687-694` | absolute, `prompts/2026-10-09/154-radar-top50-card.md` ends `-card.md`, no `..`, only `[A-Za-z0-9 ._/-]` | OK |
| 0b | `need` fields (`:722`); JOB `[a-z0-9-]` (`:733`); BRANCH plain (`:736`); WORKTREE one name (`:755`) | JOB `radar-top50-1009`, LADDER `OFF-LADDER — reports/cto-2026-10-09.md R716`, BRANCH `ops/radar-top50-1009`, WORKTREE `radar-top50-1009`, BASE, REPORT, RULINGS all set; `## ROWS` present | OK |
| 0c | build mode (`:895-911`): REPORT inside worktree, worktree absent so branch must be absent, BASE 8 hex and a commit | REPORT `/Users/cobalt/cobalt-wt/radar-top50-1009/docs/40 - DevDocs/reports/…`; `ls cobalt-wt` has no `radar-top50-1009`; BASE `0e84db6f` is 8 hex and a real commit (`diff --stat 0e84db6f HEAD -- src tests configs/cobalt/jobs.yaml` empty; main is `1458693d`) | OK |
| 0d | RULINGS `2026-10-09 R716` (`ruling_row`, `:245-272`) | the one row, `reports/cto-2026-10-09.md:9`, ends `RECORD`: "DESK RECORD (brain, from Dejan) … Queued … as a small display card". It holds neither `HIS RULING` nor `APPROVED`. The launcher refuses: `ruling 2026-10-09 R716: not HIS RULING + APPROVED` (`:267`). The file is committed (`1458693d`). | **FAIL** |
| 0e | header otherwise per `CARD.md`; `TIP`, `CHECK REPORT`, `HOUSE B` empty; `DB` left out | matches CARD.md build column; TREE STATE absent (optional) | OK |
| 1 | `file:line` cites in `radar_panel.py` | `:630-632` current_records, `:633-636` count check, `:644` `current = …`, `:641-643` order, `:1071` `<b>members</b> / cap`, `:1074` Current admitted, `:195-218` PoolView with `bars_stale_tickers` at `:213`, `:90`, `:115`, `:165`, `:502`, `:511` `position=record.last_rank`, `:532`, `:1008`, `:1018`, `:1042` — all match | OK |
| 2 | `pool.py:450-451` | `if len(admitted) > pool.cap:` / `raise AssertionError(f"pool cap violated: {len(admitted)} > {pool.cap}")` | OK |
| 3 | `store.py` cites | HOLD UPDATE in place `:114-129`; LEAVE sets `left_at` `:130-138`; `SIDE = Side.SYSTEM` `:29` | OK |
| 4 | test cites | `FakeRadarStore` `:49`, `_small_snapshot` `:96-125`, `_build` `:128-154`, mismatch test `:838-842`; pins `test_radar_panel_cards.py:480` and `:482` | OK |
| 5 | named fault vs the draft | draft §0 traces the same cause (no cap on `Current admitted`, `:630-633`, `:1074`); HOLD/LEAVE not drawn twice, same refs. The draft calls it MOST PROBABLE, the card's WHY states it as fact (see ISSUES) | OK (NOTE 1) |
| 6 | row A red on BASE | 51 deep-copied current rows, `members=51, cap=50`: BASE's count check passes (51 == 51), `current` holds 51, so `len == 50` fails for that reason. The control (row B, 50 rows, `members=50`) passes on BASE. `PoolRecord` allows `members` above `cap` (`ge=0`, `ge=1`, `:99-100`). `over_cap` does not exist on BASE; the first assert fails first. | OK |
| 7 | offline tests | rows use `FakeRadarStore`, `FakeSettingsStore`, `FakeClock`, no DB | OK |
| 8 | production read | the draft leaves it to a survey (draft `## DECISIONS` 1); card `## RECORDS` last line says "No production read at drafting. The survey read … is `## DECISIONS` 1"; the display fix does not depend on its answer | OK |
| 9 | no new command (R411, R412) | row C is `uv run cobalt jobs restarts <BASE>..HEAD`, which exists (`src/cobalt/jobs/cli.py`) | OK |
| 10 | RESTARTS class homes | `restarts.py:220` static import reach (src), `:246` test/documentation, `:225-228` DOCS; `jobs.yaml:39` `com.cobalt.aset`, `:184` `com.cobalt.radar`, `:194` `imports: [cobalt.cli]` | OK |
| 11 | committed | `git log -1 -- card` and `-- draft report` both `1458693d` "docs(desk): drafts 152 and 154 …"; `git status` lists neither as modified | OK |

## ISSUES
- FAIL (0d): RULINGS `2026-10-09 R716` is a RECORD row, not HIS RULING + APPROVED, so `desk-launch.sh build` refuses it. The desk needs Dejan's ruling row for the card (or a ruled row to cite), committed, and then RULINGS changes to it.
- NOTE 1: the card's WHY says "A pool row with `members = 51` … renders 51", stated as fact. The draft calls it most probable and leaves open the 50-names-with-a-sticky-rank-51 case. The fix is right for both causes (the cap is enforced either way), but the card does not say which cause Dejan saw. The survey read is still the desk's.
- NOTE 2: `BASE 0e84db6f` is not main HEAD (`1458693d`). `src`, `tests` and `jobs.yaml` are identical between them, so it is valid. The `diff --stat` was run from this session.
- NOTE 3: the red tests were not run (read-only seat); the proof is by reading.

PREFLIGHT DONE · card: radar-top50-1009 · checks: 16 · fails: 1 · ready: NO
