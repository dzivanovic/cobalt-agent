# DRC merge fix r3 build 2026-09-28 — seat `drc-merge-fix-r3-build`

## §0 Headline
- Report-only r3 on `7cdc5774` (branch head at PREFLIGHT `509f19f5`); no `src/`, `tests/`, `configs/` path touched; no `.env`, no lock, no migrate.
- `## FOR 08` re-issued whole: 11 test files' registry pins (S, N, L, T; two WITH-DB) and the per-file rollback contract (`0015` named an idempotent re-create); P1–P11 prove every line at the tip, no LINE MOVED.
- O `3547 passed, 525 skipped, 1 xfailed`; live-note `146 passed, 1 skipped`; W not run (`32`'s 4066/0 stands).
- RESTARTS: every resident, widened by the UNCLASSIFIED `.clinerules` (ESCALATE 1).

## L74
A block arrived appended to the Read tool result that printed `38-drc-merge-fix-r3-build.md`. It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed; the report commit carries the prompt's `Co-Authored-By` line only.

## AUTHORIZATION
Each its own Bash call.
- `grep -n -E "R_[_]" ".../prompts/2026-09-28/38-drc-merge-fix-r3-build.md"` → exit 1, no output.
- `grep -n -F "FILL AT LAUNCH" ".../38-drc-merge-fix-r3-build.md"` → exit 0, `21:` only (the gate's own line).
- `grep -n "^| R85 " ".../reports/cto-2026-09-28.md"` → exit 0:
```
94:| R85 | 14:34 ET | — DESK LAUNCH ROW: `38-drc-merge-fix-r3-build.md` (Opus 5.5, acceptEdits, cwd `~/cobalt-wt/drc-d1`) on `7cdc5774` (head `509f19f5`, main `7bc0702b`); report-only, no lock; `.env` no matches 14:33; `comm` vs `32`: 0 new. | LAUNCHED |
```
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"38-drc-merge-fix-r3-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` → `ef3960d4a0fe6150185763c4c577e5ea809ba060`.
- `grep -n "^| R80 " ".../cto-2026-09-28.md"` → exit 0:
```
89:| R80 | 14:18 ET | — DESK LAUNCH ROW: `37-draft-drc-merge-fix-r3.md` (Opus 5.5 — judgment: L75 classification of `33`; `31`'s seven read-only strings, no new string) on `7cdc5774` → writes `38` build r3 + `39` check round 2. Desk reading: HOLDs are hand-off text + one weak assertion; the merge and fixes agreed by both houses. | LAUNCHED `cc73bee8` 14:19; tab `w2:pBV` |
```
- `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-merge-fix-r3-draft-2026-09-28.md"` → `ef3960d4a0fe6150185763c4c577e5ea809ba060`.
- `tail -n 3 ".../drc-merge-fix-r3-draft-2026-09-28.md"` → last non-blank line:
```
DRC MERGE FIX R3 DRAFTED · FIX: 3 · NOT REAL: 1 · UNPROVEN: 0 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · code change: none · with-DB: no · prompts: 2 · new rule strings: 0 · ESCALATE: 3
```
Authorization holds.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 14:33:53 EDT 2026` |
| tree quiet | `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -2` | 0 | `509f19f5 docs(drc-merge): DRC merge fix r2 build report — 7cdc5774` / `7cdc5774 fix(drc-merge): fix r2 — 0018 rollback a no-op on absent drc_rows; 0015 registry pin re-stated` |
| code unmoved | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline 7cdc5774..HEAD -- src tests configs` | 0 | (empty) |
| merge parents | `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%p 5bb1f4b5` | 0 | `10163d51 daf36e01` |
| main at launch | `git -C /Users/cobalt/cobalt log -1 --format=%h main` | 0 | `ca7c6d78` |
| no `.env` anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| no `.env` here | `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |

`<preflight head>` = `509f19f5`. `<main at launch>` = `ca7c6d78` (the desk read `7bc0702b` at 14:33 ET).

## R0 RED
`<R2>` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-fix-r2-build-2026-09-28.md`. Each its own call, `grep -n -F "<cite>" <R2>`. A no-hit grep exits 1; the harness shows it as `(Bash completed with no output)`.
| # | pattern | exit | output |
|---|---|---|---|
| 1 | `test_assumed_store.py:245` | 1 | (none) — MISSING |
| 2 | `test_drc_k1_store.py:117` | 1 | (none) — MISSING |
| 3 | `test_drc_k1_store.py:123` | 1 | (none) — MISSING |
| 4 | `test_drc_store.py:65` | 1 | (none) — MISSING |
| 5 | `test_drc_store.py:67` | 1 | (none) — MISSING |
| 6 | `test_voice_store.py:57` | 1 | (none) — MISSING |
| 7 | `test_archiver_migrations.py:170` | 1 | (none) — MISSING |
| 8 | `test_archiver_migrations.py:495` | 1 | (none) — MISSING |
| 9 | `test_radar_score_migration.py:116` | 1 | (none) — MISSING |
| 10 | `every rollback on this tree is a no-op on absent objects` | 0 | see below — WRONG |
```
580:- THE ROLLBACK CONTRACT `08`–`11` inherit: every rollback on this tree is a no-op on absent objects (`IF EXISTS`, or `0013`'s / G2's `DO $migration$` + `to_regclass` guard). `08`'s `0019` rollback keeps it. The repeated `--down-to 0013` of W (f) step 2 is the proof shape.
```
RED as expected: nine cites absent from `32`'s `## FOR 08`, and the contract at `:580` is present as the parenthetical that omits `0015`'s shape.

## THE ROWS
R3-1 · ## FOR 08 · written whole · 10 <…> values filled

Values and where each was read (each its own call):
- `<preflight head>` (×2: TIP, RESTARTS range) = `509f19f5` — PREFLIGHT `log --oneline -2`.
- `<sha>` = `ca7c6d78` — PREFLIGHT `git -C /Users/cobalt/cobalt log -1 --format=%h main`.
- `<n>` = `71` — `git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log` (exit 0).
- `<m>` = `41` — `git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main` (exit 0).
- diff-stat quote = empty — `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` (exit 0, no output).
- `<the 40 lines>` — Read tool, `src/cobalt/db_migrations/__init__.py` lines 106–145 at the worktree (= `7cdc5774`: PREFLIGHT `log 7cdc5774..HEAD -- src tests configs` empty).
- `<p>` value — `## O OFFLINE`. `<l>` value — `## LIVE-NOTE`. `<as derived>` — `## RESTARTS`.

## PIN PROOF
Grepped 14:34–14:36 EDT at the tip (tests and src = `7cdc5774`). `<T>` = `/Users/cobalt/cobalt-wt/drc-d1/tests`; `<M>` = `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations`. Each its own call; outputs WHOLE, path prefix `/Users/cobalt/cobalt-wt/drc-d1/` kept as printed.

P1 `grep -r -n -F "FORWARD[" <T>` → exit 0, 12 hits (= expected):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:159:    assert FORWARD[-4] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:161:    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_migrate_proof.py:1510:    first_file_text = FORWARD[0].read_text()
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:65:    assert FORWARD[-3] == SQL and [p.name for p in FORWARD[-2:]] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:57:    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:245:    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:246:    assert FORWARD[-5].name == "0014_radar_handicap.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:249:    assert FORWARD[-4].name == "0015_shadow_agreement_stale.sql"  # the stale-score build (R40)
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:251:    assert FORWARD[-3].name == "0016_drc.sql"  # DRC D1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:253:    assert FORWARD[-2].name == "0017_voice_turns.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:255:    assert FORWARD[-1].name == "0018_drc_stated_books.sql"  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:84:    assert [p.name for p in FORWARD[-10:]] == [
```
P2 `grep -r -n -F "REVERSE[" <T>` → exit 0, 12 hits (= expected):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:67:    assert REVERSE[2] == ROLLBACK and [p.name for p in REVERSE[:2]] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:160:    assert REVERSE[3] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:162:    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:247:    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:248:    assert REVERSE[4].name == "0014_radar_handicap.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:250:    assert REVERSE[3].name == "0015_shadow_agreement_stale.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:252:    assert REVERSE[2].name == "0016_drc.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:254:    assert REVERSE[1].name == "0017_voice_turns.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:256:    assert REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:57:    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:101:    assert [p.name for p in REVERSE[:10]] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:117:    assert REVERSE[0] == ROLLBACK and [p.name for p in REVERSE[1:3]] == [
```
P3 `grep -r -n -F "_rollback_paths(" <T>` → exit 0, 26 hits (= expected):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:101:    assert [p.name for p in _rollback_paths("0007")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:114:    above_0009 = [p.name for p in _rollback_paths("0009")]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:127:    assert [p.name for p in _rollback_paths("0008")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_handicap_store.py:84:    assert [p.name for p in _rollback_paths("0013")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_handicap_store.py:187:        _apply(conn, _rollback_paths("0013"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_handicap_store.py:190:        _apply(conn, _rollback_paths("0013"))                     # repeated reverse is a no-op
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:142:    assert [p.name for p in _rollback_paths("0011")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_migrate_proof.py:1528:    reverse_text = cli._rollback_paths("0005")[0].read_text()
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:178:        _apply(conn, _rollback_paths("0013"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:180:        _apply(conn, _rollback_paths("0013"))  # a repeated reverse is a no-op
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:58:    assert [p.name for p in _rollback_paths("0015")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:188:        _apply(conn, _rollback_paths("0015"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:129:    assert [p.name for p in _rollback_paths("0009")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:139:    assert [p.name for p in _rollback_paths("0007")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:509:        _apply(conn, _rollback_paths("0009"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:523:        _apply(conn, _rollback_paths("0007"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:513:    selected = [path.name for path in _rollback_paths("0004")]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:33:    selected = _rollback_paths("0003")
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:61:        _rollback_paths(None)
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:121:    assert [p.name for p in _rollback_paths("0005")][:10] == newest_four
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:122:    assert [p.name for p in _rollback_paths("0005")][-2:] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:126:    assert [p.name for p in _rollback_paths("0006")][:10] == newest_four
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:127:    assert [p.name for p in _rollback_paths("0006")][-1:] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:132:        for p in _rollback_paths("0006")
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:494:        _apply(conn, _rollback_paths("0005"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:123:    assert [p.name for p in _rollback_paths("0016")] == [
```
P4 `grep -r -n -F "names[" <T>` → exit 0, 12 hits (= expected; `test_drc_k1_store.py:116` and `test_radar_score_migration.py:116` among them):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_runner.py:360:        assert store.names[0] == "run_lock"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:473:    assert names[names.index("0003_heartbeat_vault_outcome.sql"):][:3] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:532:    assert names[-1] == "0005_heartbeat_note_absent.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:126:    assert len(left_out) == 1 and left_out[0] == names[-1]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:127:    assert list(stats_log.REQUIRED) == names[:-1]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:230:    d = detect.detect_kind("t", _with_header(TRADING_LOG_E1, names[:-1] + ["New Column", ""]))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:243:    d = detect.detect_kind("dup", _with_header(TRADING_LOG_E1, [names[0]] + names))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:92:    assert names[start:][:2] == ["0006_radar_score.sql", "0007_radar_cards.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:116:    assert reverse_names[:10] == newest_four
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:116:    assert names[-3:] == ["0016_drc.sql", "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/taxonomy/test_catalyst.py:342:    assert names[:3] == ["range_duration", "range_height_vs_day_range", "break_bar_volume_vs_prior"]
/Users/cobalt/cobalt-wt/drc-d1/tests/taxonomy/test_catalyst.py:345:    assert factor_block(probe).names[1:3] == ["catalyst_grade", "catalyst_class"]
```
P5 `grep -n -F "numbers" <T>/cobalt/test_archiver_migrations.py` → exit 0, 10 hits (= expected; `:170`, `:171`, `:172` among them):
```
157:    its numbers run 1…11 contiguously with no duplicate, and REVERSE is
161:    numbers = [int(p.name.split("_", 1)[0]) for p in FORWARD]
162:    assert numbers == sorted(numbers), "FORWARD must be in numeric order"
163:    assert len(numbers) == len(set(numbers)), f"duplicate migration number in {numbers}"
170:    assert numbers == [*range(1, 12), 13, 14, 15, 16, 17, 18], f"1…11 then 13–18, got {numbers}"
171:    assert numbers[-8:-6] == [10, 11], "this branch's pair is still in place"
172:    assert numbers[-1] == 18, "DRC K1's 0018 is the tail"
173:    reverse_numbers = [int(p.name.split("_", 1)[0]) for p in REVERSE]
174:    assert reverse_numbers == sorted(reverse_numbers, reverse=True)
175:    assert reverse_numbers == [n for n in reversed(numbers) if n != 1], (
```
P6 `grep -r -n -F "0018_drc_stated_books" <T>` → exit 0, 24 hits (= expected):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:102:        "0018_drc_stated_books.rollback.sql",  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:117:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_p4_migrations.py:128:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_handicap_store.py:85:        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:66:        "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:68:        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:143:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:59:        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:255:    assert FORWARD[-1].name == "0018_drc_stated_books.sql"  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_assumed_store.py:256:    assert REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:35:        "0018_drc_stated_books.rollback.sql",  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:516:        "0018_drc_stated_books.rollback.sql",  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:94:        "0018_drc_stated_books.sql",  # DRC K1; 0017 is the voice branch's
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:102:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:130:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:140:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:104:        "0018_drc_stated_books.rollback.sql",  # DRC K1 (the name stays; the list is ten now)
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:3:Migration `0018_drc_stated_books`, `DrcStore.record_stated_book` /
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:45:SQL = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:46:ROLLBACK = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:116:    assert names[-3:] == ["0016_drc.sql", "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:124:        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_experiments.py:362:    forward = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_experiments.py:363:    rollback = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
```
`grep -r -n -F "len(FORWARD" <T>` → exit 1, no output. `grep -r -n -F "len(REVERSE" <T>` → exit 1, no output (= expected).

P7 `grep -n -F "survivors" <T>/cobalt/test_archiver_migrations.py` → exit 0:
```
494:        # by both rollbacks, never survivors.
495:        survivors = {
516:        for name in survivors:
528:        for name in survivors:
```
`grep -n -F "DRC_D1_TABLES =" …` → exit 0:
```
54:DRC_D1_TABLES = ("drc_imports", "drc_fills", "drc_rows", "drc_stated_books")
```
`grep -n -F "def test_rollback_down_to_0009_drops_this_branch_alone" …` → exit 0:
```
470:def test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4():
```
P8 `grep -n -F "pytestmark" <T>/cobalt/test_stale_score_db.py` → exit 0:
```
22:pytestmark = [sds.requires_db, pytest.mark.integration]
```
P9 `grep -n -F "0018_drc_stated_books" <M>/__init__.py` → exit 0:
```
62:`0018_drc_stated_books.sql` — DRC K1: `"user".drc_stated_books` (his
66:`0018_drc_stated_books.rollback.sql` — deletes the `seed` / `book_close`
72:(`0016_drc`); 0018 is DRC K1's (`0018_drc_stated_books`), 0019 the DRC
124:    MIGRATIONS_DIR / "0018_drc_stated_books.sql",
129:    MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql",
```
P10 THE CONTRACT, each exit 0:
```
$ grep -n -F "to_regclass" <M>/0013_tunables_slug_nullable.rollback.sql
6:    IF to_regclass('"user".tunables') IS NULL THEN
$ grep -n -F "DROP COLUMN IF EXISTS" <M>/0014_radar_handicap.rollback.sql
8:    DROP COLUMN IF EXISTS handicap,
9:    DROP COLUMN IF EXISTS handicap_factor,
10:    DROP COLUMN IF EXISTS raw_rank;
$ grep -n -F "CREATE OR REPLACE VIEW" <M>/0015_shadow_agreement_stale.rollback.sql
4:CREATE OR REPLACE VIEW "user".shadow_agreement_v AS
$ grep -n -F "card_dot_taps" <M>/0015_shadow_agreement_stale.rollback.sql
12:      FROM "user".card_dot_taps AS t
$ grep -n -F "DROP TABLE IF EXISTS" <M>/0016_drc.rollback.sql
6:DROP TABLE IF EXISTS "user".drc_rows;
7:DROP TABLE IF EXISTS "user".drc_fills;
8:DROP TABLE IF EXISTS "user".drc_imports;
$ grep -n -F "DROP TABLE IF EXISTS" <M>/0017_voice_turns.rollback.sql
5:DROP TABLE IF EXISTS "user".voice_turns;
$ grep -n -F "to_regclass" <M>/0018_drc_stated_books.rollback.sql
9:    IF to_regclass('"user".drc_rows') IS NULL THEN
$ grep -n -F "DROP TABLE IF EXISTS" <M>/0018_drc_stated_books.rollback.sql
18:DROP TABLE IF EXISTS "user".drc_stated_books;
```
P11 THE ANCHORS, each exit 0 (`grep -n -F` under `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/`; the routes by the Read tool):
```
$ grep -n -F "drc_stated_books" db_migrations/placement.py
98:    # db_migrations/0018_drc_stated_books.sql — DRC K1: his stated opening
100:    "drc_stated_books": Side.USER,
$ grep -n -F "def radar_card_release" aset/web.py
1512:async def radar_card_release(card_id: int):
$ grep -n -F "drc_cli.add_parser" cli.py
512:    drc_cli.add_parser(sub)
$ grep -n -F "MIN_N_FOR_AVERAGE = " replay/line.py
60:MIN_N_FOR_AVERAGE = 30
$ grep -n -F "STRATEGIES_DIR = " taxonomy/vault_loader.py
91:STRATEGIES_DIR = "1 - Trading/4 - Strategies"
Read aset/web.py:1152 → @app.post("/attest", response_class=HTMLResponse)
Read aset/web.py:1557 → @app.get("/drc", response_class=HTMLResponse)
```
Also read by the Read tool (list ranges R3-1 cites, not in P1–P11): `test_p4_migrations.py:100–137` (lists end `:112`, `:125`, `:137`; `above_0009 ==` at `:116`), `test_archiver_migrations.py:82–150` (ends `:95`, `:112`, `:138`, `:150`) and `:492–533` (`:503` `"voice_turns"`; asserts `:516–519`, `:528–531`), `test_radar_score_migration.py:100–129` (`newest_four` `:103–114`), `test_tenancy.py:511–527` (`:513–526`), `test_radar_migration.py:31–46` (`:33–45`). Each matches R3-1.

LINE MOVED: none. Every count and line equals the drafter's; no cited pin is absent.

## O OFFLINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `7cdc5774`'s code (`run_in_background`, exit 0; output 88 lines, `FAILED` and `ERROR` grep no hit), summary WHOLE (ANSI colour codes stripped):
```
3547 passed, 525 skipped, 1 xfailed, 20 warnings in 553.73s (0:09:13)
```
GATE green: 0 failed, 0 errors. **`<p>` = 3547** = expected 3547; 525 skipped = expected; 1 xfailed = expected. Status rule, 14:46:38 EDT: `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` →
```
## drc/d1-trading-log
?? "docs/40 - DevDocs/reports/drc-merge-fix-r3-build-2026-09-28.md"
```

## W WITH-DB
NOT RUN — no test or src row; the code is 7cdc5774, whose with-DB 4066/0 is 32's (R2:221, :299); the lock was never taken.

## LIVE-NOTE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (`run_in_background`, exit 0; output read whole, 57 lines), every `SKIPPED` line and the summary (ANSI codes stripped):
```
SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
146 passed, 1 skipped, 15 warnings in 24.99s
```
GATE green: 0 failed; the one skip is the known `COBALT_TEST_LIVE_DRC` skip; no skip names `COBALT_LIVE_VAULT_ROOT`. **`<l>` = 146** = `32`'s 146 (no extra skip without `.env`).

## RESTARTS
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `uv run cobalt jobs restarts 10163d51..509f19f5` (`run_in_background`) → **exit 1** (`RestartError`: one path unclassified). Output 752 lines, read whole from the task output file. The 524 `DOCS` rows (`grep -c -F "<TAB>DOCS<TAB>"` → 524) are output lines 5–7 (`AGENTS.md`, `CLAUDE.md`, `QWEN.md`) and 16–536 (every path under `docs/`), each `DOCS	-`, no restart; `32`'s 523 plus `docs/40 - DevDocs/reports/drc-merge-fix-r2-build-2026-09-28.md	A	DOCS	-` (line 416), `32`'s report commit. Every other line, verbatim (`grep -n -v -F "<TAB>DOCS<TAB>"` of the output file):
```
1:FAILED: RestartError: one or more changed paths were unclassified
2:path	change	rule	restart
3:.clinerules	M	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
4:ESCALATE: unclassified path .clinerules
8:configs/cobalt/agents/voice.yaml	A	resident reads	com.cobalt.aset
9:configs/cobalt/jobs.yaml	M	registry; register, no restart	-
10:configs/cobalt/modelaccess.yaml	A	resident reads	com.cobalt.aset
11:configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
12:configs/cobalt/rules.yaml	M	no resident reads (one-shot: com.cobalt.prefill-daily,com.cobalt.prefill-drc)	-
13:configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
14:configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
15:configs/cobalt/voice.yaml	A	resident reads	com.cobalt.aset
537:ops/start_aset.sh	M	resident reads	com.cobalt.aset
538:pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
539:src/cobalt/aset/card_stop.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
540:src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
541:src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
542:src/cobalt/cards/health.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
543:src/cobalt/cards/scoring.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
544:src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
545:src/cobalt/cli.py	M	static import reach	com.cobalt.radar
546:src/cobalt/db_migrations/0013_tunables_slug_nullable.rollback.sql	A	non-Python src asset	-
547:src/cobalt/db_migrations/0013_tunables_slug_nullable.sql	A	non-Python src asset	-
548:src/cobalt/db_migrations/0014_radar_handicap.rollback.sql	A	non-Python src asset	-
549:src/cobalt/db_migrations/0014_radar_handicap.sql	A	non-Python src asset	-
550:src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql	A	non-Python src asset	-
551:src/cobalt/db_migrations/0015_shadow_agreement_stale.sql	A	non-Python src asset	-
552:src/cobalt/db_migrations/0017_voice_turns.rollback.sql	A	non-Python src asset	-
553:src/cobalt/db_migrations/0017_voice_turns.sql	A	non-Python src asset	-
554:src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql	M	non-Python src asset	-
555:src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
556:src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
557:src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
558:src/cobalt/modelaccess/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
559:src/cobalt/modelaccess/adapters.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
560:src/cobalt/modelaccess/client.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
561:src/cobalt/modelaccess/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
562:src/cobalt/modelaccess/guard.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
563:src/cobalt/modelaccess/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
564:src/cobalt/radar/anatomy/extension.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
565:src/cobalt/radar/anatomy/frame.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
566:src/cobalt/radar/anatomy/in_play.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
567:src/cobalt/radar/anatomy/indicators.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
568:src/cobalt/radar/anatomy/leg_roles.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
569:src/cobalt/radar/anatomy/micro_range.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
570:src/cobalt/radar/anatomy/pivots.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
571:src/cobalt/radar/anatomy/range_break.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
572:src/cobalt/radar/anatomy/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
573:src/cobalt/radar/anatomy/session_levels.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
574:src/cobalt/radar/anatomy/slope.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
575:src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
576:src/cobalt/radar/cli.py	M	static import reach	com.cobalt.radar
577:src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
578:src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
579:src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
580:src/cobalt/radar/formation/__init__.py	A	static import reach	-
581:src/cobalt/radar/formation/anchors.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
582:src/cobalt/radar/formation/atoms.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
583:src/cobalt/radar/formation/stops.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
584:src/cobalt/radar/formation/triggers.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
585:src/cobalt/radar/handicap.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
586:src/cobalt/radar/handicap_dry_run.py	A	static import reach	com.cobalt.radar
587:src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
588:src/cobalt/radar/pool.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
589:src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
590:src/cobalt/radar/seam.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
591:src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
592:src/cobalt/replay/cli.py	M	static import reach	com.cobalt.radar
593:src/cobalt/replay/formations.py	M	static import reach	com.cobalt.radar
594:src/cobalt/replay/line.py	M	static import reach	com.cobalt.radar
595:src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
596:src/cobalt/replay/movers.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
597:src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
598:src/cobalt/smoke/checks.py	M	static import reach	com.cobalt.radar
599:src/cobalt/taxonomy/cli.py	M	static import reach	com.cobalt.radar
600:src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
601:src/cobalt/taxonomy/tunables.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
602:src/cobalt/taxonomy/vault_loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
603:src/cobalt/voice/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
604:src/cobalt/voice/agent.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
605:src/cobalt/voice/cli.py	A	static import reach	com.cobalt.radar
606:src/cobalt/voice/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
607:src/cobalt/voice/confirm.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
608:src/cobalt/voice/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
609:src/cobalt/voice/registry.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
610:src/cobalt/voice/resolve.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
611:src/cobalt/voice/scratch.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
612:src/cobalt/voice/store.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
613:src/cobalt/voice/tools.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
614:src/cobalt/voice/transcribe.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
615:src/cobalt/voice/turn.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
616:src/cobalt/voice/web.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
617:tests/cobalt/radar_migrated_support.py	A	test/documentation; no resident	-
618:tests/cobalt/radar_p2_support.py	M	test/documentation; no resident	-
619:tests/cobalt/setups_shapes.py	A	test/documentation; no resident	-
620:tests/cobalt/stale_db_support.py	A	test/documentation; no resident	-
621:tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
622:tests/cobalt/test_assumed_store.py	A	test/documentation; no resident	-
623:tests/cobalt/test_cards_picks.py	M	test/documentation; no resident	-
624:tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
625:tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
626:tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
627:tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
628:tests/cobalt/test_modelaccess_client.py	A	test/documentation; no resident	-
629:tests/cobalt/test_modelaccess_config.py	A	test/documentation; no resident	-
630:tests/cobalt/test_modelaccess_silence.py	A	test/documentation; no resident	-
631:tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
632:tests/cobalt/test_radar_anatomy.py	M	test/documentation; no resident	-
633:tests/cobalt/test_radar_audit_export.py	M	test/documentation; no resident	-
634:tests/cobalt/test_radar_cards_db.py	M	test/documentation; no resident	-
635:tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
636:tests/cobalt/test_radar_evaluate_cli.py	M	test/documentation; no resident	-
637:tests/cobalt/test_radar_handicap.py	A	test/documentation; no resident	-
638:tests/cobalt/test_radar_handicap_dead.py	A	test/documentation; no resident	-
639:tests/cobalt/test_radar_handicap_dry_run.py	A	test/documentation; no resident	-
640:tests/cobalt/test_radar_handicap_fix_r1_runs.py	A	test/documentation; no resident	-
641:tests/cobalt/test_radar_handicap_group.py	A	test/documentation; no resident	-
642:tests/cobalt/test_radar_handicap_panel.py	A	test/documentation; no resident	-
643:tests/cobalt/test_radar_handicap_runner.py	A	test/documentation; no resident	-
644:tests/cobalt/test_radar_handicap_shadow.py	A	test/documentation; no resident	-
645:tests/cobalt/test_radar_handicap_store.py	A	test/documentation; no resident	-
646:tests/cobalt/test_radar_migrated_harness.py	A	test/documentation; no resident	-
647:tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
648:tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
649:tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
650:tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
651:tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
652:tests/cobalt/test_radar_store.py	M	test/documentation; no resident	-
653:tests/cobalt/test_replay_formations.py	M	test/documentation; no resident	-
654:tests/cobalt/test_replay_line.py	M	test/documentation; no resident	-
655:tests/cobalt/test_replay_movers.py	M	test/documentation; no resident	-
656:tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
657:tests/cobalt/test_rubberband_forms.py	A	test/documentation; no resident	-
658:tests/cobalt/test_setups_d1.py	A	test/documentation; no resident	-
659:tests/cobalt/test_setups_d4.py	A	test/documentation; no resident	-
660:tests/cobalt/test_setups_fix_r2.py	A	test/documentation; no resident	-
661:tests/cobalt/test_setups_fix_r3.py	A	test/documentation; no resident	-
662:tests/cobalt/test_setups_fix_r4.py	A	test/documentation; no resident	-
663:tests/cobalt/test_setups_fixture_cut.py	A	test/documentation; no resident	-
664:tests/cobalt/test_setups_hitchhiker.py	A	test/documentation; no resident	-
665:tests/cobalt/test_setups_lego.py	A	test/documentation; no resident	-
666:tests/cobalt/test_setups_nine_ema.py	A	test/documentation; no resident	-
667:tests/cobalt/test_setups_registries.py	A	test/documentation; no resident	-
668:tests/cobalt/test_setups_second_chance.py	A	test/documentation; no resident	-
669:tests/cobalt/test_setups_vwap_cont.py	A	test/documentation; no resident	-
670:tests/cobalt/test_setups_x5.py	A	test/documentation; no resident	-
671:tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
672:tests/cobalt/test_smoke_k3_sql.py	M	test/documentation; no resident	-
673:tests/cobalt/test_stale_score.py	A	test/documentation; no resident	-
674:tests/cobalt/test_stale_score_db.py	A	test/documentation; no resident	-
675:tests/cobalt/test_taxonomy_store.py	M	test/documentation; no resident	-
676:tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
677:tests/cobalt/test_voice_card_stop.py	A	test/documentation; no resident	-
678:tests/cobalt/test_voice_cli.py	A	test/documentation; no resident	-
679:tests/cobalt/test_voice_config.py	A	test/documentation; no resident	-
680:tests/cobalt/test_voice_confirm.py	A	test/documentation; no resident	-
681:tests/cobalt/test_voice_fix_r1_runs.py	A	test/documentation; no resident	-
682:tests/cobalt/test_voice_lifecycle.py	A	test/documentation; no resident	-
683:tests/cobalt/test_voice_plan.py	A	test/documentation; no resident	-
684:tests/cobalt/test_voice_resolve.py	A	test/documentation; no resident	-
685:tests/cobalt/test_voice_scratch.py	A	test/documentation; no resident	-
686:tests/cobalt/test_voice_store.py	A	test/documentation; no resident	-
687:tests/cobalt/test_voice_tools.py	A	test/documentation; no resident	-
688:tests/cobalt/test_voice_transcribe.py	A	test/documentation; no resident	-
689:tests/cobalt/test_voice_turn.py	A	test/documentation; no resident	-
690:tests/cobalt/test_voice_web.py	A	test/documentation; no resident	-
691:tests/experiments/handicap_h1/conftest.py	A	test/documentation; no resident	-
692:tests/experiments/handicap_h1/h1_cache.py	A	test/documentation; no resident	-
693:tests/experiments/handicap_h1/h1_support.py	A	test/documentation; no resident	-
694:tests/experiments/handicap_h1/test_h1_x0_grouping.py	A	test/documentation; no resident	-
695:tests/experiments/handicap_h1/test_h1_x1_blanks.py	A	test/documentation; no resident	-
696:tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py	A	test/documentation; no resident	-
697:tests/experiments/handicap_h1/test_h1_x3_cell_format.py	A	test/documentation; no resident	-
698:tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py	A	test/documentation; no resident	-
699:tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py	A	test/documentation; no resident	-
700:tests/experiments/handicap_h1/test_h1_x8_x11_group.py	A	test/documentation; no resident	-
701:tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py	A	test/documentation; no resident	-
702:tests/experiments/handicap_h1/test_x12_identity.py	A	test/documentation; no resident	-
703:tests/experiments/handicap_h1/test_xl76_membership_harness.py	A	test/documentation; no resident	-
704:tests/experiments/setups_one/conftest.py	A	test/documentation; no resident	-
705:tests/experiments/setups_one/test_x13_x15_drive.py	A	test/documentation; no resident	-
706:tests/experiments/setups_one/test_x1_premarket_seed.py	A	test/documentation; no resident	-
707:tests/experiments/setups_one/test_x2_coverage.py	A	test/documentation; no resident	-
708:tests/experiments/setups_one/test_x7_x18_stored.py	A	test/documentation; no resident	-
709:tests/experiments/stale_score/conftest.py	A	test/documentation; no resident	-
710:tests/experiments/stale_score/stale_predicates.py	A	test/documentation; no resident	-
711:tests/experiments/stale_score/stale_support.py	A	test/documentation; no resident	-
712:tests/experiments/stale_score/test_x10_replay_as_of.py	A	test/documentation; no resident	-
713:tests/experiments/stale_score/test_x11_audit_replay_fallback.py	A	test/documentation; no resident	-
714:tests/experiments/stale_score/test_x12_published_null.py	A	test/documentation; no resident	-
715:tests/experiments/stale_score/test_x13_tap_keeps_sentence_db.py	A	test/documentation; no resident	-
716:tests/experiments/stale_score/test_x14_daily_missing_keeps_proximity.py	A	test/documentation; no resident	-
717:tests/experiments/stale_score/test_x15_two_clocks.py	A	test/documentation; no resident	-
718:tests/experiments/stale_score/test_x16_last_price_coalesce_db.py	A	test/documentation; no resident	-
719:tests/experiments/stale_score/test_x18_x19_callers.py	A	test/documentation; no resident	-
720:tests/experiments/stale_score/test_x20_x22_bindings.py	A	test/documentation; no resident	-
721:tests/experiments/stale_score/test_x21_htf_tap_no_pair_db.py	A	test/documentation; no resident	-
722:tests/experiments/stale_score/test_x23_next_day_card_db.py	A	test/documentation; no resident	-
723:tests/experiments/stale_score/test_x24_no_print_minutes_db.py	A	test/documentation; no resident	-
724:tests/experiments/stale_score/test_x25_stale_graded_taps_db.py	A	test/documentation; no resident	-
725:tests/experiments/stale_score/test_x26_slug_match_not_evaluable.py	A	test/documentation; no resident	-
726:tests/experiments/stale_score/test_x27_reason_bytes.py	A	test/documentation; no resident	-
727:tests/experiments/stale_score/test_x28_proximity_one_receipts_db.py	A	test/documentation; no resident	-
728:tests/experiments/stale_score/test_x29_ladder_render.py	A	test/documentation; no resident	-
729:tests/experiments/stale_score/test_x2_stale_sequence_db.py	A	test/documentation; no resident	-
730:tests/experiments/stale_score/test_x30_r40_discriminator_db.py	A	test/documentation; no resident	-
731:tests/experiments/stale_score/test_x3_taps_moved_null_db.py	A	test/documentation; no resident	-
732:tests/experiments/stale_score/test_x4_audit_stale_card.py	A	test/documentation; no resident	-
733:tests/experiments/stale_score/test_x5b_prior_session_bars.py	A	test/documentation; no resident	-
734:tests/experiments/stale_score/test_x6_htf_proximity_stale.py	A	test/documentation; no resident	-
735:tests/experiments/stale_score/test_x7_ladder_promoted_stale.py	A	test/documentation; no resident	-
736:tests/experiments/stale_score/test_x8_expiry_on_stale.py	A	test/documentation; no resident	-
737:tests/experiments/stale_score/test_x9_stale_scored_cards_db.py	A	test/documentation; no resident	-
738:tests/experiments/stale_score/test_xl76_devdb_absence.py	A	test/documentation; no resident	-
739:tests/fixtures/radar/_cut_setups_fixtures.py	A	test/documentation; no resident	-
740:tests/fixtures/radar/bars-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
741:tests/fixtures/radar/daily-bars-setups-rubberband.real-shape.csv	A	test/documentation; no resident	-
742:tests/fixtures/radar/membership-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
743:tests/fixtures/radar/screen-handicap.real-shape.csv	A	test/documentation; no resident	-
744:tests/fixtures/replay/_cut_p4_fixtures.py	M	test/documentation; no resident	-
745:tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv	A	test/documentation; no resident	-
746:tests/fixtures/voice/plan-replies.constructed.yaml	A	test/documentation; no resident	-
747:tests/fixtures/voice/plan-utterances.constructed.yaml	A	test/documentation; no resident	-
748:tests/taxonomy/test_predicate.py	M	test/documentation; no resident	-
749:uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
750:RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
751:
752:[exited with code 1]
```
`RESTARTS:` = `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar` — `32`'s set, widened to every resident by the UNCLASSIFIED `.clinerules` row (arrives through the merge from main). Non-`DOCS` rows are `32`'s rows exactly; the range differs from `32`'s only by `32`'s report (one `DOCS` row). → ESCALATE 1. Status rule, 14:47:42 EDT: `## drc/d1-trading-log` + this report's `??` line only.

## FOR 08
Re-issued WHOLE (r3); supersedes `32`'s `## FOR 08` and `17`'s. r3 changed no file but its own report: the code is `7cdc5774`.
- TIP: code `7cdc5774` (fix r2), parent `0e75e46d`, over `4fc270c7` (fix r1); the merge commit `5bb1f4b5` has parents `10163d51` and `daf36e01`. Branch head at r3 PREFLIGHT `509f19f5`; r3's report commit sits on it (`git -C /Users/cobalt/cobalt log -1 --format=%h drc/d1-trading-log`, read by the desk after CLOSE). `<main at launch>` = `ca7c6d78`. `71` ahead (`git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log`), `41` behind (`git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main`); `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` → empty (exit 0; empty = main moved docs-only since the merge).
- FORWARD and REVERSE as merged, `src/cobalt/db_migrations/__init__.py:106–145` at `7cdc5774` (Read tool, quoted whole below this line):
```
#: Applied in this order, every time, every file idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
    MIGRATIONS_DIR / "0004_radar_pool.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.sql",
    MIGRATIONS_DIR / "0006_radar_score.sql",
    MIGRATIONS_DIR / "0007_radar_cards.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.sql",
    MIGRATIONS_DIR / "0009_picks_missed.sql",
    MIGRATIONS_DIR / "0010_archive_progress.sql",
    MIGRATIONS_DIR / "0011_archive_incidents.sql",
    MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",
    MIGRATIONS_DIR / "0014_radar_handicap.sql",
    MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql",
    MIGRATIONS_DIR / "0016_drc.sql",
    MIGRATIONS_DIR / "0017_voice_turns.sql",
    MIGRATIONS_DIR / "0018_drc_stated_books.sql",
)

#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
REVERSE = (
    MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql",
    MIGRATIONS_DIR / "0017_voice_turns.rollback.sql",
    MIGRATIONS_DIR / "0016_drc.rollback.sql",
    MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql",
    MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql",
    MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",
    MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql",
    MIGRATIONS_DIR / "0010_archive_progress.rollback.sql",
    MIGRATIONS_DIR / "0009_picks_missed.rollback.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql",
    MIGRATIONS_DIR / "0007_radar_cards.rollback.sql",
    MIGRATIONS_DIR / "0006_radar_score.rollback.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.rollback.sql",
    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
)
```
  `0018` FORWARD `:124`, REVERSE `:129` (docstring `:62`, `:66`, `:72`). Next free: `0019` (`08`'s `drc_events`), `0020` (D3), `0021` (S3 exits C1, off main).
- THE ROLLBACK CONTRACT `08`–`11` inherit. Every rollback `--down-to 0013` selects (`0014`–`0018`), and `0013`'s own, is a no-op when its objects are absent, each by its own shape: `0013_tunables_slug_nullable.rollback.sql:4–14` a `DO $migration$` block that returns at `:6–7` when `to_regclass('"user".tunables')` is null · `0014_radar_handicap.rollback.sql:7–10` `DROP COLUMN IF EXISTS` ×3 on `system.radar_membership` (created by `0004`, below the bound) · `0015_shadow_agreement_stale.rollback.sql:4–16` `CREATE OR REPLACE VIEW "user".shadow_agreement_v` — NOT an absent-object guard: an idempotent re-create of `0007`'s view, reading `"user".card_dot_taps` (`:12`, created by `0007`, below the bound) · `0016_drc.rollback.sql:6–8` `DROP TABLE IF EXISTS` ×3 · `0017_voice_turns.rollback.sql:5` `DROP TABLE IF EXISTS` · `0018_drc_stated_books.rollback.sql:7–17` G2's `DO $migration$` block (returns at `:9–10` when `"user".drc_rows` is absent), then `:18` `DROP TABLE IF EXISTS`. Rollbacks at or below `0011` are OUTSIDE this contract (not walked for it; the round-1 check's read of them: `reports/drc-merge-fix-r2-check-2026-09-28.md:145`). `08`'s `0019` rollback keeps the contract: a table it creates → `DROP TABLE IF EXISTS`; a statement on a table another migration owns → the `to_regclass` guard. The proof shape is `32`'s repeated `--down-to 0013` (R2:366–420, `F3 = F2 = F0`).
- ANCHORS at `7cdc5774` (`## PIN PROOF` P11): `src/cobalt/db_migrations/placement.py:100` `"drc_stated_books": Side.USER,` · `src/cobalt/aset/web.py:1152` `@app.post("/attest", …` · `:1557` `@app.get("/drc", …` · `:1512` `async def radar_card_release(card_id: int):` · `src/cobalt/cli.py:512` `drc_cli.add_parser(sub)` · `src/cobalt/replay/line.py:60` `MIN_N_FOR_AVERAGE = 30` · `src/cobalt/taxonomy/vault_loader.py:91` `STRATEGIES_DIR = "1 - Trading/4 - Strategies"`.
- COUNTS: code `7cdc5774`: `15`'s `<p0>` 2588 on `10163d51` → r3 `<p>` 3547 offline (`32`: 3547); with-DB `32`'s `<d>` **4066** (4057 + 9; r3 ran no with-DB: no code changed); live-note r3 `<l>` 146 (`32`: 146, with `.env` present); `32`'s `<F0>` = `<F2>` = `<F3>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`; `<F1>` (at `0018`) = 796 · 40 · `5727e9dfb418376cc48722a3601ca7c3`.
- THE WITH-DB DESELECT SET: the eight arguments (nine tests) `32`'s W (c1) ran with (R2:211) are the merged tree's. `08`'s three arguments (four tests) no longer describe a green pass at `0013`.
- THE REGISTRY PINS `08` MUST RE-STATE when it adds `0019` — COMPLETE, from a sweep of every idiom (`## PIN PROOF` P1–P8), each `file:line` at `7cdc5774`. Kinds: S = slot pin (`FORWARD[-n]` / `REVERSE[n]`), N = number pin, L = list pin (exact, or a `[:10]` / `[-10:]` prefix), T = table-set pin. "→" = the same migration's slot or list once `0019` is `FORWARD[-1]` / `REVERSE[0]`. Offline unless marked WITH-DB (the offline suite skips those; only `08`'s with-DB pass shows them red).
  - `tests/cobalt/test_assumed_store.py:245–256` — S ×12 (`test_0013_is_registered_forward_and_reverse`): `:245` `FORWARD[-6]` 0013 → `[-7]` · `:246` `FORWARD[-5]` 0014 → `[-6]` · `:247` `REVERSE[5]` 0013 → `[6]` · `:248` `REVERSE[4]` 0014 → `[5]` · `:249` `FORWARD[-4]` 0015 → `[-5]` · `:250` `REVERSE[3]` 0015 → `[4]` · `:251` `FORWARD[-3]` 0016 → `[-4]` · `:252` `REVERSE[2]` 0016 → `[3]` · `:253` `FORWARD[-2]` 0017 → `[-3]` · `:254` `REVERSE[1]` 0017 → `[2]` · `:255` `FORWARD[-1]` 0018 → `[-2]` · `:256` `REVERSE[0]` 0018 → `[1]`. (`:242–243` are membership, unchanged.)
  - `tests/cobalt/test_drc_k1_store.py:116` — L `names[-3:]` = 0016, 0017, 0018 → `names[-4:-1]` · `:117–118` — S `REVERSE[0] == ROLLBACK` → `REVERSE[1]`, and L `REVERSE[1:3]` = 0017, 0016 → `REVERSE[2:4]` · `:123–124` — L `_rollback_paths("0016")` = 0018, 0017 → 0019 first.
  - `tests/cobalt/test_drc_store.py:65–66` — S `FORWARD[-3] == SQL` (0016) → `[-4]`, and L `FORWARD[-2:]` = 0017, 0018 → `FORWARD[-3:-1]` · `:67–68` — S `REVERSE[2] == ROLLBACK` → `[3]`, and L `REVERSE[:2]` = 0018, 0017 → `REVERSE[1:3]` · `:142–149` — L `_rollback_paths("0011")` six names → 0019 first, seven.
  - `tests/cobalt/test_voice_store.py:57` — S ×2 `FORWARD[-2] == SQL` (0017) → `[-3]`, `REVERSE[1] == ROLLBACK` → `[2]` · `:58–60` — L `_rollback_paths("0015")` = 0018, 0017, 0016 → 0019 first.
  - `tests/cobalt/test_radar_handicap_store.py:84–87` — L `_rollback_paths("0013")` five names → 0019 first, six.
  - `tests/cobalt/test_stale_score_db.py:159–162` — S ×4, WITH-DB (module `pytestmark` `:22` is `requires_db`): `:159` `FORWARD[-4]` 0015 → `[-5]` · `:160` `REVERSE[3]` → `[4]` · `:161` `FORWARD[-6]` 0013 → `[-7]` · `:162` `REVERSE[5]` → `[6]`.
  - `tests/cobalt/test_p4_migrations.py:101–112` — L `_rollback_paths("0007")` exact, ten → eleven · `:114–125` — L `above_0009` exact (`:116`), eight → nine · `:127–137` — L `_rollback_paths("0008")` exact, nine → ten; 0019 first in each.
  - `tests/cobalt/test_radar_migration.py:33–45` — L `[:10]` prefix of `_rollback_paths("0003")`, 0018…0008 → 0019…0009 (or the slice widened to eleven).
  - `tests/cobalt/test_radar_score_migration.py:103–114` — L `newest_four` (ten names, 0018…0008), read by three prefix asserts that break with it: `:116` `reverse_names[:10]`, `:121` `_rollback_paths("0005")[:10]`, `:126` `_rollback_paths("0006")[:10]`.
  - `tests/cobalt/test_tenancy.py:513–526` — L `selected[:10]` of `_rollback_paths("0004")`, 0018…0008.
  - `tests/cobalt/test_archiver_migrations.py:84–95` — L `FORWARD[-10:]` = 0008…0018 → 0009…0019 · `:101–112` — L `REVERSE[:10]` · `:129–138` — L `_rollback_paths("0009")` exact, eight → nine · `:139–150` — L `_rollback_paths("0007")` exact, ten → eleven · `:170` — N `numbers == [*range(1, 12), 13, 14, 15, 16, 17, 18]` → `…, 18, 19]` · `:171` — N `numbers[-8:-6] == [10, 11]` → `numbers[-9:-7]` · `:172` — N `numbers[-1] == 18` → `19`.
  - `tests/cobalt/test_archiver_migrations.py:54` + `:495–505`, asserted `:516–519` and `:528–531` — T, WITH-DB (`test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4`, `:470`): every `CREATED_TABLES` name outside `NEW_TABLES`, `P4_TABLES`, `DRC_D1_TABLES` (`:54`) and `"voice_turns"` (`:503`) must survive `--down-to 0009` and `--down-to 0007`. A table `0019` adds to `CREATED_TABLES` is numbered above both bounds, so both rollbacks drop it: it joins the exclusions, or `:517` goes red with-DB.
  - NOT PINS (read; `0019` moves none): `test_migrate_proof.py:1510` (`FORWARD[0]`), `:1528` (`_rollback_paths("0005")[0]`, value-free); by-name slices `test_radar_score_migration.py:92–93`, `test_tenancy.py:473`, `:479`; suffixes `test_tenancy.py:527–534`, `test_radar_score_migration.py:122`, `:127`; paths by name `test_drc_k1_experiments.py:362–363`, `test_drc_k1_store.py:45–46`.
- `08`'s own list (`prompts/2026-09-28/08-drc-d2-fix-r1-build.md:106`) is pre-merge and name-grep-based: re-pointed from THIS list.
- RESTARTS (`10163d51..509f19f5`, derived under `## RESTARTS`; r3's report commit adds one `docs/` path, no restart by L42): `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`.
- `CLAUDE.md` in the worktree is main's stub (R33 (4)).

## FOR THE CHECK
- R0: the ten greps with exit codes under `## R0 RED` (nine exit 1, `:580` exit 0).
- `## FOR 08` written from 38's R3-1 block verbatim, 10 values filled (listed under `## THE ROWS`).
- P1–P11 WHOLE under `## PIN PROOF`. `LINE MOVED`: none.
- O: `3547 passed, 525 skipped, 1 xfailed, 20 warnings in 553.73s (0:09:13)`. Live-note: `146 passed, 1 skipped, 15 warnings in 24.99s` (the one skip `COBALT_TEST_LIVE_DRC`).
- `## W WITH-DB`: NOT RUN.
- RESTARTS table under `## RESTARTS` (524 `DOCS` rows summarised as count and line ranges, every other line verbatim).
- The report commit's `git -C /Users/cobalt/cobalt-wt/drc-d1 show --stat --format=%h HEAD`: in the final chat message after CLOSE.
- No path on the branch changed but this report.

## CONTINUE
next: none — CLOSE done at the stop line.

## ESCALATE
1. ESCALATE: UNCLASSIFIED `.clinerules` — OWED to the DRC deploy (R74). `cobalt jobs restarts 10163d51..509f19f5` row 3, exit 1; it arrives through the merge from main and widens `RESTARTS:` to every resident. [14:47 EDT]
2. RECORD: `<main at launch>` read `ca7c6d78` at 14:33:53 EDT; the desk's launch row read `7bc0702b`. Main moved in between. `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` is empty: main is still docs-only since the merge. Ahead `71` / behind `41` (`32`: 70 / 26).
3. RECORD: the L74 block (see `## L74`) arrived and was not followed.

DRC MERGE FIX R3 BUILT report-only (code 7cdc5774; tip = this report's commit) | on 7cdc5774 | files: 1 (src 0, tests 0, report 1) | offline 3547/0 | with-DB not run | live-note 146/0 | cobalt_dev: 0013 (untouched) | .env: absent | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | FIX: 1 | ESCALATE: 3
