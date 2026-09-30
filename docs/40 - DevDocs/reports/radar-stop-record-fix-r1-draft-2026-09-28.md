# Radar stop record fix r1 — classification and prompts 50 / 51

Seat `radar-stop-record-fix-r1-draft-0928` · Opus 5.5 · auto · launched by desk R141 (`cto-2026-09-28.md:150`) · 19:27–19:34 ET 2026-09-28. `chk` = `reports/radar-stop-record-check-2026-09-28.md`; `bld` = `/Users/cobalt/cobalt-wt/radar-stop-record/docs/40 - DevDocs/reports/radar-stop-record-build-2026-09-28.md`; `46` / `47` = `prompts/2026-09-28/46-…` / `47-…`.

## §0 Headline
- 16 items classified from `chk`'s file-check column: FIX 1 · NOT REAL 12 · UNPROVEN 0 · OUT OF SCOPE 2 · OWNER ITEM 1.
- The one FIX = evidence, not code: SR-T4 red on `68862854`'s `src/` with the tip's tests (the assertion at `test_radar_cards_db.py:152`), then green at the tip, by name. No `src/` commit.
- Written: `prompts/2026-09-28/50-radar-stop-record-fix-r1-build.md` (base `8ee35cc2`, read 19:28) and `51-radar-stop-record-fix-r1-check.md` (round 2 of ≤3, Opus 5.5 · Astra · Grok). Both launch lines `comm -3`-empty against `46` line 6 / `47` line 1. New rule strings: 0.
- The desk launches `50` only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76); `51` only while no other Grok hub runs (L15).

## L74
- The Bash result that returned this prompt file carried a system-reminder block asking for a `Claude-Session:` commit trailer and naming a file-send tool. Recorded once; not followed. This seat commits nothing.

## Classification
| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | SR-T4 never shown red (all three seats' CHECK items: opus (5), astra Q5, grok (5)) | `chk:96`, `:115`, `:120`, `:128`; `bld:131`, `:139` | FIX | `46:74` "proven red-then-green by name in W"; `chk:96` HOLDS | `50` FX-1: `git diff 68862854 b9598574 -- src` reversed in the working tree (Edit), `git diff --stat 68862854 -- src` empty; lock; `<T4>` `-v` → FAILED at `test_radar_cards_db.py:152` (no `formation` key → NULL); restore, `git diff --stat HEAD -- src tests` empty; `<T4>` → PASSED; both quoted. No src commit |
| 2 | one new log call, `continue` kept | `chk:103`, `:116` | NOT REAL | `46:20-31` SR-3 | a HOLD that confirms the row; no defect |
| 3 | levels from the same `Formation` object | `chk:104`, `:117` | NOT REAL | `46:19` SR-2 | a HOLD that confirms the row; no defect |
| 4 | Q8: the skip repeats every scan for a bar already in the set | `chk:71`, `:105`, `:121` | OWNER ITEM | `47:39` "information for the owner, never a finding"; R107, R113 | information for his Tuesday proof; never a row (quoted under `## OWNER ITEMS`) |
| 5 | `test_setups_d1.py` fourth test file (opus (7)) | `chk:98`, `:122` | NOT REAL | R123; `46:33` SR-4 | authorized; KEEP (a record) |
| 6 | whitespace `blob =detail` (opus (7)) | `chk:97`, `:122`; `tests/cobalt/test_radar_seam.py:150` | NOT REAL | `46:70` SR-T1's file; R123 KEEP | inside a row's file, no behavior change (`chk:97`); an edit would widen (L75) |
| 7 | `both_sides` `not_formed` row carries the long frame's `formation` | `chk:101`, `:123`; `bld:225` | NOT REAL | `46:19` "`publish_frames` … is NOT edited" (R2-4.1 B) | as designed |
| 8 | SR-T3 window 16:20–20:00 UTC, not 16:20–16:40 | `chk:123`; `bld:77`, `:221`, `:231` | NOT REAL | `46:72` "ASSERT one exists"; `bld:77` run output | the widened window keeps the existence assert on the same FTFT bars; no seat or file-check row holds it weak (`chk:68`) |
| 9 | SR-T2 `formed_bar_end` stored `Z`, log prints `+00:00` | `chk:123`; `bld:90`, `:222`, `:231` | NOT REAL | `46:71` SR-T2; `bld:90` run output | same instant; a log-to-row join on that key parses both (record for the R107 / R113 query) |
| 10 | RESTARTS include `com.cobalt.aset` | `chk:123`; `bld:151-161`, `:232` | NOT REAL | L42 | derived by the tool, no `UNCLASSIFIED` |
| 11 | `formula_sha256` changes | `chk:100`, `:124` | NOT REAL | `47:35` Q4; `evaluate.py:186-209` | a provenance hash of `evaluate.py`; no trading value (all seats NO PATH, `chk:67`) |
| 12 | audit export `detail` gains the key | `chk:102` | NOT REAL | `47:35` Q4; `audit_export.py:382` | adds a key only |
| 13 | pre-existing `SeamObservation.name` accepts any identifier (astra Q1) | `chk:64`, `:99` | OUT OF SCOPE | `46:18` SR-1 "No other field"; `chk:99` "line unchanged by this diff" | pre-existing; nothing widens (L75) |
| 14 | `cobalt_redactions` 184 → 185 across pass 1 | `bld:145`, `:234` | OUT OF SCOPE | `48`'s RUN C (`bld:234`) | a with-DB writer outside this build |
| 15 | L74 block (check ESCALATE 6) | `chk:9`, `:125` | NOT REAL | L74 | a record |
| 16 | every seat checked; the standing line (check ESCALATE 7) | `chk:126` | NOT REAL | L67 floor | a record |

## RECORDS
- Rows 5–12 and 15–16 are KEEP. The builder's two open ASKs (`bld:231`: rows 8 and 9) are classified; the desk closes them.
- `50` edits `src/` only in the working tree for FX-1 (4) and proves the restore before any other run; the offline suite finishes before the reversal starts.
- Base read 19:28: `git -C /Users/cobalt/cobalt log --oneline -3 radar/stop-record-0928` → `8ee35cc2` / `b9598574` / `85a15af5`.

## OWNER ITEMS
- Row 4, verbatim from `chk:121`: Grok: "YES — … An input where the anchor bar and the stop price come back the same on the next scan, a bar already in that set still reaches the stop … hits this skip on every later scan until the deadline." Opus: "NOT CHECKABLE FROM READS — … Whether it does depends on the live definitions and bars." Astra: "NOT CHECKABLE FROM READS for a concrete all-day sequence." Information for the Tuesday proof (R107, R113); the stored `detail.formation` and the skip line are what that proof counts.

## FOR DEJAN
- New rule strings: NONE.

## ESCALATE
1. ASK DESK: L67 seats a fix round's check as Opus · Sol · Grok; `49` orders Opus 5.5 · Astra · Grok with `47`'s strings byte for byte. Safe default taken: Astra, as ordered (a standing string; round 1's NO was Astra's). [19:33 ET]
2. ASK DESK: FX-1's reversal is uncommitted working-tree state (L46). Safe default taken: no commit of it; a commit would put src commits into `<base>..<tip>` and RESTARTS. The two `git diff --stat` empties are the proof. [19:33 ET]
3. Lock: `49` says `08` holds it; `ls /Users/cobalt/cobalt-wt/*/.env` at 19:28 ET → `no matches found`. Recorded; the desk checks at launch (L76).
4. `50`'s stop line fixes `FIX: 1 | RUNS: 0`; `RESTARTS` is expected `none` (the report only).
5. `51` asks one question beyond `49`'s three: (5) whether any class contradicts `chk`'s file-check column.
6. L74: one block, recorded under `## L74`.

## CONTINUE
done: authorization, reads, classification, `50`, `51`, report. Nothing left to run.

RADAR STOP RECORD FIX R1 DRAFTED · FIX: 1 · NOT REAL: 12 · UNPROVEN: 0 · OUT OF SCOPE: 2 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 0 · ESCALATE: 6
