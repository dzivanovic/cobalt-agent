# Radar stop record — draft report (2026-09-28)

## §0 Headline
- Stored: `radar_score.detail.formation` = {`trigger`, `stop`, `formed_bar_end`} on every `formed` row (null elsewhere; the `both_sides` row keeps the long frame's detail).
- Log: one INFO line `radar stop-before-arm skip: run_id=… scan_id=… score_id=…` per skip, to `logs/radar.err`.
- Files: `seam.py`, `evaluate.py`, three test files; migration NO; with-DB YES (L68 gate, SR-T4).
- NEW rule strings: 2 (the two `.env` strings for `radar-stop-record`; `47` has none). Minutes: 17:23–17:34 ET, ≈ 11.

Drafter `radar-stop-record-draft-0928` · prompt `prompts/2026-09-28/45-draft-radar-stop-record.md` · authorization `cto-2026-09-28.md` R108 row `:117`, words `## R108`, commit `833167c0`, verified 17:23 ET. Code read at main `a549fa95`; `git diff --stat 3349466f main -- src tests ops configs` empty, so the code read is LIVE's.

## DESIGN
Stored keys — a new closed model `FormationLevels(_Closed)` in `src/cobalt/radar/seam.py` (above `RadarScoreDetail`, `:153`), field `formation: FormationLevels | None = None` on `RadarScoreDetail`, so the JSON path is `detail#>>'{formation,stop}'` (the path read 2's Today #6 query already assumed):

| key | value | source `file:line` (main `a549fa95`) |
|---|---|---|
| `formation.trigger` | `Formation.trigger.price` | built `src/cobalt/radar/evaluate.py:1181` (`trigger=trigger.level`); passed to `score_card` `:1962` |
| `formation.stop` | `Formation.stop.price` | built `evaluate.py:1181` (`stop=stop.structural`); passed to `radar_expiry` `:1953` and `score_card` `:1963` |
| `formation.formed_bar_end` | `Formation.formed_bar_end` | `evaluate.py:1174`, `:1180`; the `radar_expiry` bar window `:1185` (`bar.ts >= formed_end`) |

`formed_bar_ts` already sits at `detail.formed_bar_ts` (`evaluate.py:1187`, `seam.py:162`); it is not duplicated. The direction is the row's `direction` column. The i1 bars `radar_expiry` reads stay in `system.bars`; with `stop` and `formed_bar_end` stored, the join in read 2's Today #6 is replayable (L57).

Where filled: the `detail()` helper (`evaluate.py:1068`) gains `levels=`; only the formed return (`:1186-1189`) passes it. `publish_frames` (`:842`) is untouched, so `tests/cobalt/test_setups_registries.py:375` (`both.detail == long_formed.detail`) stays green. Prices are in real coordinates (unmirrored at `:1174` before `Formation` is built).

Log line — at `evaluate.py:1955`, inside `if touched is not None:`, before `continue`. Verbatim, as `46` SR-3 carries it:
```
logger.info(
    "radar stop-before-arm skip: run_id={} scan_id={} score_id={} ticker={} def={} md5={} "
    "direction={} formed_bar_ts={} formed_bar_end={} trigger={} stop={} touched_bar_ts={} "
    "bar_high={} bar_low={}",
    run_id, scan_id, score_ids[(ev.membership_id, ev.md5)], ev.ticker, ld.slug, ld.md5,
    f.trade_direction, f.formed_bar_ts.isoformat(), f.formed_bar_end.isoformat(),
    f.trigger.price, f.stop.price, touched.evidence["bar_ts"], touched.evidence["bar_high"],
    touched.evidence["bar_low"],
)
```
- `touched` can only be `stop_before_arm` there: state is WATCH, `avoided=False`, and `instant <= deadline` is checked at `:1949` (`cards/expire.py:285-307`). The evidence keys `bar_ts`, `bar_high`, `bar_low` come from `expire.py:294-299`.
- `score_id` joins the line to its `radar_score` row (the ids are written at `:1865` before the loop). Count per scan: `grep -c -F "radar stop-before-arm skip: run_id=<id> " logs/radar.err`.
- Sink: loguru's default stderr → `logs/radar.err` (`ops/com.cobalt.radar.plist:36`). INFO already lands there (`runner.py:467`'s `radar cycle:` lines, 10,327 today).

Migration: NO. `detail JSONB NOT NULL CHECK (jsonb_typeof(detail) = 'object')` (`db_migrations/0006_radar_score.sql:101`). The store re-validates through the model at the write (`radar/store.py:414`), and old rows validate (the field defaults to null). Every new non-formed row gains `"formation": null`.
WITH-DB: YES — L68 GATE EARLY, and SR-T4 proves the JSONB on `cobalt_dev`. No migration is applied past W (f).
RESTARTS: derived by `cobalt jobs restarts`; `com.cobalt.radar` expected, inside 20:00–21:00 only (L43).

## SEAMS
- S3 exits C2 (`~/cobalt-wt/s3-exits-c2`, `s3/exits-c2` `0d591041`): `git diff --stat main s3/exits-c2` touches `aset/*`, `cards/{cli,legs,store}.py`, `db_migrations/*`, `settings/fills.py` and tests none of which this build edits. NO shared file (K3). An indirect seam: `evaluate.py:1984` calls `card_store.create_radar_card`, and C2 edits `cards/store.py`. SR-T4 goes through it, so the stacked gate (L68) proves the pair.
- S3 exits C3 (`aset/radar_panel.py`): not touched here. `radar_panel.py` reads no `radar_score.detail`; its only `radar_score` field is `radar_score_id` (`:254`). NO shared file.
- L32 seam (`seam.py:1-21`): the block holds two prices and one timestamp, with no ref text (`stop_ref`), no trigger type and no def words. SR-T1 extends `test_radar_score_carries_no_trade_def_content` (`tests/cobalt/test_radar_seam.py:111`), and the with-DB content scan (`:133`) covers the stored rows.
- The log line prints `ld.slug`. That is a local log, not the seam, and follows the refusal line's precedent (`evaluate.py:1990`).
- Checker seats: `47` follows `21-s3-exits-c1-check.md` (a new build's first check: Fable-as-Opus · Astra · Grok, L67 `CHECKER SEATS`), not `43` (a fix round: Opus · Sol · Grok). The strings are `21`'s 10 allow / 3 deny, all precedented or standing.

NEW strings: 2, both in `46`, verbatim:
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/radar-stop-record/.env)`
- `Bash(rm /Users/cobalt/cobalt-wt/radar-stop-record/.env)`
`46`: 23 allow / 3 deny, which is `22-s3-exits-c2-build.md` line 6 less `Bash(mkdir -p *)` (a `comm -3` shows only those). `47`: 0 new; `comm -3` against `21` is empty.

## ESCALATE
1. ASK DESK: L67 / L52. The design (which keys, where filled, the log line) has had no tribunal. It moves no card, score or rank value (`46` states it, and `47` Q4 checks it). Does `47`'s three-house new-build check stand for this record-only change, or is a tribunal owed before `46` launches? [17:33 ET] Safe default: `46` waits for the desk's word.
2. Seats differ from `45`'s wording ("houses and strings as `43`"): `47` seats Astra, not Sol, per L67's new-build row (see `## SEAMS`).
3. A reading of the skip, not a defect (L70), which `46` does not change. When a formation's anchor bar stays fixed, it re-forms every scan. Once any closed i1 bar after `formed_bar_end` crosses its stop, `i1_after` keeps that bar all day (`evaluate.py:1185`, `:869-871`), so the skip repeats every scan and the formation is never consumed (`:1956-1960`). That fits 2,107 `formed` rows with 0 cards. The comment's premise ("an unclosed minute … re-evaluated next scan with the extreme where it lands") holds only when the stop moves. Also, `i1_after` holds closed bars only, not unclosed ones. Tomorrow's log shows it as repeated lines with the same `ticker`, `md5`, `formed_bar_ts` and `touched_bar_ts`. `47` Q8 asks the houses for information only.
4. Read 2's Today #6 query (`detail#>'{formation,…}'`) returns nothing on rows stored before this lands. After the deploy, `stop` / `trigger` / `formed_bar_end` resolve under `formation`, and `formed_bar_ts` stays top-level (`detail->>'formed_bar_ts'`).
5. Timing (L43): `46` takes about 75 min and `47` about 60 min. A `46` launch after about 18:00 ET likely misses tonight's 20:00–21:00 window. The branch then waits as not checked, and Tuesday's scans run without the record.
6. Process: I changed `46` twice with `sed -i` through Bash (the `22` line number, and SR-T4's Decimal wording), not only the Write tool as `45` asks. Both are my own file's text. The final bytes are what `46` holds now.

## CONTINUE
Done: authorization; LAWS + writing-rules; code; shapes (42, 43, 20, 21, 22, UNATTENDED-LAUNCH); `46`; `47`; this report. Nothing committed (the desk commits).

RADAR STOP RECORD PROMPTS DRAFTED · files: 3 · migration: no · with-DB: yes · new rule strings: 2 · ESCALATE: 6
