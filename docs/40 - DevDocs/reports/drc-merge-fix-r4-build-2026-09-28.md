# DRC merge fix r4 build 2026-09-28 — seat `drc-merge-fix-r4-build`

## §0 Headline
- Report-only r4 on `7cdc5774` (branch head at PREFLIGHT `84827649`); no `src/`, `tests/`, `configs/` path; no `.env`, no lock, no migrate.
- `## FOR 08` re-issued whole: all four prefix-list entries state 0019…0009; the RESTARTS bullet carries the `.clinerules` caveat; counts named at head `84827649` against main `68862854` (72 ahead / 71 behind). P1–P12 hold at the tip, no LINE MOVED.
- O `3547 passed, 525 skipped, 1 xfailed`; W not run (`32`'s 4066/0 stands).
- RESTARTS: every resident, widened by the UNCLASSIFIED `.clinerules` (ESCALATE 1).

## L74
A block arrived as a system-reminder right after the Read tool result that printed `42-drc-merge-fix-r4-build.md`. It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed; the report commit carries the prompt's `Co-Authored-By` line only.

## AUTHORIZATION
Each its own Bash call.
- `grep -n -E "R_[_]" ".../prompts/2026-09-28/42-drc-merge-fix-r4-build.md"` → exit 1, no output.
- `grep -n -F "FILL AT LAUNCH" ".../42-drc-merge-fix-r4-build.md"` → exit 0, `21:` only (the gate's own line).
- `grep -n "^| R112 " ".../reports/cto-2026-09-28.md"` → exit 0 (names `42-drc-merge-fix-r4-build.md` and `7cdc5774`):
```
121:| R112 | 17:33 ET | — NO NEW WORDS; R103 chain: DESK LAUNCH ROW for `42-drc-merge-fix-r4-build.md` — report-only fix r4 on code `7cdc5774`, cwd `~/cobalt-wt/drc-d1` (head `84827649`, no `.env`, tree quiet); report `drc-merge-fix-r4-build-2026-09-28.md`, stop `^(DRC MERGE FIX R4 BUILT\|FAILED)` → fill `43` → launch. | APPROVED — LAUNCHED `c729fd72` 17:33; watch `boc6up7lm` (45 min); tab "F14 fix r4 build" `w2:pC4` |
```
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"42-drc-merge-fix-r4-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` → `688628547837bb4bedb9f2cf7d8423b9f61dde31`.
- `grep -n "^| R101 " ".../cto-2026-09-28.md"` → exit 0 (carries `41-draft-drc-merge-fix-r4.md`):
```
110:| R101 | 16:35 ET | — DESK LAUNCH ROW for `41-draft-drc-merge-fix-r4.md` — Opus 5.5 judgment drafter (L75 classification), auto, cwd `~/cobalt`, rc + name `drc-merge-fix-r4-draft-0928`; writes `42` build + `43` round 3 check. `S3-P3 · F14`. Report `reports/drc-merge-fix-r4-draft-2026-09-28.md`, stop `^(DRC MERGE FIX R4 DRAFTED\|FAILED)`. | LAUNCHED |
```
- `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-merge-fix-r4-draft-2026-09-28.md"` → `56782bf4cffd6cced348315038550cd9ac018342`.
- `tail -n 3 ".../drc-merge-fix-r4-draft-2026-09-28.md"` → last non-blank line:
```
DRC MERGE FIX R4 DRAFTED · FIX: 2 · NOT REAL: 0 · UNPROVEN: 0 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · code change: none · with-DB: no · prompts: 2 · new rule strings: 0 · ESCALATE: 3
```
Authorization holds.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 17:33:45 EDT 2026` |
| tree quiet | `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -3` | 0 | `84827649 docs(drc-merge): DRC merge fix r3 build report — FOR 08 re-issued whole (report only, code 7cdc5774)` / `509f19f5 docs(drc-merge): DRC merge fix r2 build report — 7cdc5774` / `7cdc5774 fix(drc-merge): fix r2 — 0018 rollback a no-op on absent drc_rows; 0015 registry pin re-stated` |
| code unmoved | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline 7cdc5774..HEAD -- src tests configs` | 0 | (empty) |
| merge parents | `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%p 5bb1f4b5` | 0 | `10163d51 daf36e01` |
| main at launch | `git -C /Users/cobalt/cobalt log -1 --format=%h main` | 0 | `68862854` |
| `.env` any worktree | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| no `.env` here | `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |

`<main at launch>` = `68862854` (the launch-row commit over the desk's `42be9c1a`).

## R0 RED
`<R3>` = `.../reports/drc-merge-fix-r3-build-2026-09-28.md`; `<R2>` = `.../reports/drc-merge-fix-r2-build-2026-09-28.md` (both under `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/`). Each its own call. A no-hit grep exits 1; the harness shows it as `(Bash completed with no output)`.
| # | grep | exit | output | expected |
|---|---|---|---|---|
| 1 | `grep -n -F "0019…0009" <R3>` | 0 | `581:` only (below) | = |
| 2 | `grep -n -F "widened to all residents by the UNCLASSIFIED" <R3>` | 1 | (none) | = |
| 3 | the same on `<R2>` | 0 | `603:` (below) | = |
| 4 | `grep -n -F "read at branch head" <R3>` | 1 | (none) | = |
```
581:  - `tests/cobalt/test_radar_migration.py:33–45` — L `[:10]` prefix of `_rollback_paths("0003")`, 0018…0008 → 0019…0009 (or the slice widened to eleven).
```
```
603:- RESTARTS (`10163d51..7cdc5774`, derived under `## RESTARTS`): `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. It is widened to all residents by the UNCLASSIFIED `.clinerules` (ESCALATE 1).
```
RED as expected: `38`'s `## FOR 08` states the target for `test_radar_migration.py` alone, drops r2's caveat, and names no head for the counts.

## THE ROWS
R4-1 · ## FOR 08 · written whole · 11 <…> values filled

Values and where each was read (each its own call):
- `<sha>` (×5) = `68862854` — PREFLIGHT `git -C /Users/cobalt/cobalt log -1 --format=%h main`.
- `<n>` = `72` — `git -C /Users/cobalt/cobalt rev-list --count 68862854..84827649` (exit 0).
- `<m>` = `71` — `git -C /Users/cobalt/cobalt rev-list --count 84827649..68862854` (exit 0).
- diff-stat quote = empty — `git -C /Users/cobalt/cobalt diff --stat daf36e01 68862854 -- . ':(exclude)docs'` (exit 0, no output).
- `<the 40 lines>` — Read tool, `src/cobalt/db_migrations/__init__.py` lines 106–145 at the worktree (= `7cdc5774`: PREFLIGHT `log 7cdc5774..HEAD -- src tests configs` empty).
- `<value>` — `## O OFFLINE`. `<as derived>` — `## RESTARTS`.

## PIN PROOF
Grepped between 17:33:45 (PREFLIGHT `date`) and 17:36:41 EDT (the next `date`) at the tip (tests and src = `7cdc5774`). `<T>` = `/Users/cobalt/cobalt-wt/drc-d1/tests`; `<M>` = `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations`. Each its own call; P1–P9 outputs WHOLE as printed; P10–P12 as `file · pattern → every printed line` (one call per row). A no-hit grep exits 1.

P1 `grep -r -n -F "FORWARD[" <T>` → exit 0, 12 hits (= expected):
```
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_migrate_proof.py:1510:    first_file_text = FORWARD[0].read_text()
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:65:    assert FORWARD[-3] == SQL and [p.name for p in FORWARD[-2:]] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:159:    assert FORWARD[-4] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:161:    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
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
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:160:    assert REVERSE[3] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:162:    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:67:    assert REVERSE[2] == ROLLBACK and [p.name for p in REVERSE[:2]] == [
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
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:178:        _apply(conn, _rollback_paths("0013"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_stale_score_db.py:180:        _apply(conn, _rollback_paths("0013"))  # a repeated reverse is a no-op
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_migrate_proof.py:1528:    reverse_text = cli._rollback_paths("0005")[0].read_text()
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_store.py:142:    assert [p.name for p in _rollback_paths("0011")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:58:    assert [p.name for p in _rollback_paths("0015")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_voice_store.py:188:        _apply(conn, _rollback_paths("0015"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:33:    selected = _rollback_paths("0003")
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:61:        _rollback_paths(None)
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:129:    assert [p.name for p in _rollback_paths("0009")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:139:    assert [p.name for p in _rollback_paths("0007")] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:509:        _apply(conn, _rollback_paths("0009"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:523:        _apply(conn, _rollback_paths("0007"))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:513:    selected = [path.name for path in _rollback_paths("0004")]
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
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:126:    assert len(left_out) == 1 and left_out[0] == names[-1]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:127:    assert list(stats_log.REQUIRED) == names[:-1]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:230:    d = detect.detect_kind("t", _with_header(TRADING_LOG_E1, names[:-1] + ["New Column", ""]))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_detect.py:243:    d = detect.detect_kind("dup", _with_header(TRADING_LOG_E1, [names[0]] + names))
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:473:    assert names[names.index("0003_heartbeat_vault_outcome.sql"):][:3] == [
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:532:    assert names[-1] == "0005_heartbeat_note_absent.rollback.sql"
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
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:94:        "0018_drc_stated_books.sql",  # DRC K1; 0017 is the voice branch's
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:102:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:130:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_archiver_migrations.py:140:        "0018_drc_stated_books.rollback.sql",
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_tenancy.py:516:        "0018_drc_stated_books.rollback.sql",  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_migration.py:35:        "0018_drc_stated_books.rollback.sql",  # DRC K1
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_radar_score_migration.py:104:        "0018_drc_stated_books.rollback.sql",  # DRC K1 (the name stays; the list is ten now)
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_experiments.py:362:    forward = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_experiments.py:363:    rollback = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:3:Migration `0018_drc_stated_books`, `DrcStore.record_stated_book` /
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:45:SQL = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:46:ROLLBACK = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:116:    assert names[-3:] == ["0016_drc.sql", "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_k1_store.py:124:        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
```
`grep -r -n -F "len(FORWARD" <T>` → exit 1, no hit. `grep -r -n -F "len(REVERSE" <T>` → exit 1, no hit.

P7 `grep -n -F "survivors" <T>/cobalt/test_archiver_migrations.py` → exit 0:
```
494:        # by both rollbacks, never survivors.
495:        survivors = {
516:        for name in survivors:
528:        for name in survivors:
```
`grep -n -F "DRC_D1_TABLES =" …/test_archiver_migrations.py` → exit 0:
```
54:DRC_D1_TABLES = ("drc_imports", "drc_fills", "drc_rows", "drc_stated_books")
```
`grep -n -F "def test_rollback_down_to_0009_drops_this_branch_alone" …/test_archiver_migrations.py` → exit 0:
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
`grep -n -F "0019" <M>/__init__.py` → exit 0 (docstring only):
```
72:(`0016_drc`); 0018 is DRC K1's (`0018_drc_stated_books`), 0019 the DRC
73:D2 fix round's (`0019_drc_events`) and 0020 DRC D3's
```
P10 THE CONTRACT, each exit 0:
```
0013_tunables_slug_nullable.rollback.sql  to_regclass           → 6:    IF to_regclass('"user".tunables') IS NULL THEN
0014_radar_handicap.rollback.sql          DROP COLUMN IF EXISTS → 8:    DROP COLUMN IF EXISTS handicap,
                                                                  9:    DROP COLUMN IF EXISTS handicap_factor,
                                                                  10:    DROP COLUMN IF EXISTS raw_rank;
0015_shadow_agreement_stale.rollback.sql  CREATE OR REPLACE VIEW → 4:CREATE OR REPLACE VIEW "user".shadow_agreement_v AS
0015_shadow_agreement_stale.rollback.sql  card_dot_taps         → 12:      FROM "user".card_dot_taps AS t
0016_drc.rollback.sql                     DROP TABLE IF EXISTS  → 6:DROP TABLE IF EXISTS "user".drc_rows;
                                                                  7:DROP TABLE IF EXISTS "user".drc_fills;
                                                                  8:DROP TABLE IF EXISTS "user".drc_imports;
0017_voice_turns.rollback.sql             DROP TABLE IF EXISTS  → 5:DROP TABLE IF EXISTS "user".voice_turns;
0018_drc_stated_books.rollback.sql        to_regclass           → 9:    IF to_regclass('"user".drc_rows') IS NULL THEN
0018_drc_stated_books.rollback.sql        DROP TABLE IF EXISTS  → 18:DROP TABLE IF EXISTS "user".drc_stated_books;
```
P11 THE ANCHORS, each exit 0:
```
db_migrations/placement.py  drc_stated_books       → 98:    # db_migrations/0018_drc_stated_books.sql — DRC K1: his stated opening
                                                     100:    "drc_stated_books": Side.USER,
aset/web.py                 def radar_card_release → 1512:async def radar_card_release(card_id: int):
cli.py                      drc_cli.add_parser     → 512:    drc_cli.add_parser(sub)
replay/line.py              MIN_N_FOR_AVERAGE =    → 60:MIN_N_FOR_AVERAGE = 30
taxonomy/vault_loader.py    STRATEGIES_DIR =       → 91:STRATEGIES_DIR = "1 - Trading/4 - Strategies"
Read aset/web.py:1152 → @app.post("/attest", response_class=HTMLResponse)
Read aset/web.py:1557 → @app.get("/drc", response_class=HTMLResponse)
```
P12 THE TARGETS, each exit 0:
```
test_radar_score_migration.py  newest_four                           → 103:    newest_four = [
                                                                       116:    assert reverse_names[:10] == newest_four
                                                                       121:    assert [p.name for p in _rollback_paths("0005")][:10] == newest_four
                                                                       126:    assert [p.name for p in _rollback_paths("0006")][:10] == newest_four
test_radar_score_migration.py  0008_radar_value_movers.rollback.sql  → 113:        "0008_radar_value_movers.rollback.sql",
test_tenancy.py                selected[:10]                         → 515:    assert selected[:10] == [
test_tenancy.py                0008_radar_value_movers.rollback.sql  → 525:        "0008_radar_value_movers.rollback.sql",
test_archiver_migrations.py    REVERSE[:10]                          → 101:    assert [p.name for p in REVERSE[:10]] == [
test_archiver_migrations.py    0008_radar_value_movers.rollback.sql  → 111:        "0008_radar_value_movers.rollback.sql",
                                                                       149:        "0008_radar_value_movers.rollback.sql",
```
Read tool on the three slices:
- `test_radar_score_migration.py:103–126` — `:104` `"0018_drc_stated_books.rollback.sql"` · `:105` 0017 · `:106` 0016 · `:107` 0015 · `:108` 0014 · `:109` 0013 · `:110` 0011 · `:111` 0010 · `:112` 0009 · `:113` `"0008_radar_value_movers.rollback.sql"` · `:114` `]`; `:116`, `:121`, `:126` compare `[:10]` to it.
- `test_tenancy.py:513–526` — `:513` `selected = [path.name for path in _rollback_paths("0004")]`, `:515` `assert selected[:10] == [`, `:516` 0018 … `:525` 0008 (the same ten), `:526` `]`.
- `test_archiver_migrations.py:101–112` — `:101` `assert [p.name for p in REVERSE[:10]] == [`, `:102` 0018 … `:111` 0008 (the same ten), `:112` `]`.
Each list is REVERSE's first ten (0018…0008, `__init__.py:129–138`); with `0019` at `REVERSE[0]` each prefix is 0019…0009.

LINE MOVED: none. Every count and line equals `38`'s P1–P11 and the drafter's P12; no cited pin is absent.

## O OFFLINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `7cdc5774`'s code (`run_in_background`, exit 0; output 88 lines, `grep -c -F "FAILED"` → 0, `grep -c -F "ERROR"` → 0), summary line 86 WHOLE (ANSI colour codes stripped):
```
3547 passed, 525 skipped, 1 xfailed, 20 warnings in 574.49s (0:09:34)
```
GATE green: 0 failed, 0 errors. **`<p>` = 3547** = `38`'s 3547; 525 skipped = `38`'s 525; 1 xfailed = expected. Status rule (right after the first `uv run` started, between 17:33:45 and 17:36:41 EDT, and again after O, `date` 17:44:22 EDT; same output both times): `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` →
```
## drc/d1-trading-log
?? "docs/40 - DevDocs/reports/drc-merge-fix-r4-build-2026-09-28.md"
```

## W WITH-DB
NOT RUN — no test or src row; the code is 7cdc5774, whose with-DB 4066/0 is 32's (R2:221, :299); the lock was never taken.

## RESTARTS
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `uv run cobalt jobs restarts 10163d51..84827649` (`run_in_background`, run while O ran) → **exit 1** (`RestartError`: one path unclassified). Output read whole from the task output file. The 525 `DOCS` rows (`grep -c -F "<TAB>DOCS<TAB>"` → 525) are output lines 5–7 (`AGENTS.md`, `CLAUDE.md`, `QWEN.md`) and 16–537 (every path under `docs/`), each `DOCS	-`, no restart: `38`'s 524 plus `docs/40 - DevDocs/reports/drc-merge-fix-r3-build-2026-09-28.md	A	DOCS	-` (line 417), `38`'s report commit. Every other line, verbatim (`grep -n -v -F "<TAB>DOCS<TAB>"` of the output file):
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
538:ops/start_aset.sh	M	resident reads	com.cobalt.aset
539:pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
540:src/cobalt/aset/card_stop.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
541:src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
542:src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
543:src/cobalt/cards/health.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
544:src/cobalt/cards/scoring.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
545:src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
546:src/cobalt/cli.py	M	static import reach	com.cobalt.radar
547:src/cobalt/db_migrations/0013_tunables_slug_nullable.rollback.sql	A	non-Python src asset	-
548:src/cobalt/db_migrations/0013_tunables_slug_nullable.sql	A	non-Python src asset	-
549:src/cobalt/db_migrations/0014_radar_handicap.rollback.sql	A	non-Python src asset	-
550:src/cobalt/db_migrations/0014_radar_handicap.sql	A	non-Python src asset	-
551:src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql	A	non-Python src asset	-
552:src/cobalt/db_migrations/0015_shadow_agreement_stale.sql	A	non-Python src asset	-
553:src/cobalt/db_migrations/0017_voice_turns.rollback.sql	A	non-Python src asset	-
554:src/cobalt/db_migrations/0017_voice_turns.sql	A	non-Python src asset	-
555:src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql	M	non-Python src asset	-
556:src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
557:src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
558:src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
559:src/cobalt/modelaccess/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
560:src/cobalt/modelaccess/adapters.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
561:src/cobalt/modelaccess/client.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
562:src/cobalt/modelaccess/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
563:src/cobalt/modelaccess/guard.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
564:src/cobalt/modelaccess/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
565:src/cobalt/radar/anatomy/extension.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
566:src/cobalt/radar/anatomy/frame.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
567:src/cobalt/radar/anatomy/in_play.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
568:src/cobalt/radar/anatomy/indicators.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
569:src/cobalt/radar/anatomy/leg_roles.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
570:src/cobalt/radar/anatomy/micro_range.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
571:src/cobalt/radar/anatomy/pivots.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
572:src/cobalt/radar/anatomy/range_break.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
573:src/cobalt/radar/anatomy/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
574:src/cobalt/radar/anatomy/session_levels.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
575:src/cobalt/radar/anatomy/slope.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
576:src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
577:src/cobalt/radar/cli.py	M	static import reach	com.cobalt.radar
578:src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
579:src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
580:src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
581:src/cobalt/radar/formation/__init__.py	A	static import reach	-
582:src/cobalt/radar/formation/anchors.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
583:src/cobalt/radar/formation/atoms.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
584:src/cobalt/radar/formation/stops.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
585:src/cobalt/radar/formation/triggers.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
586:src/cobalt/radar/handicap.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
587:src/cobalt/radar/handicap_dry_run.py	A	static import reach	com.cobalt.radar
588:src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
589:src/cobalt/radar/pool.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
590:src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
591:src/cobalt/radar/seam.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
592:src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
593:src/cobalt/replay/cli.py	M	static import reach	com.cobalt.radar
594:src/cobalt/replay/formations.py	M	static import reach	com.cobalt.radar
595:src/cobalt/replay/line.py	M	static import reach	com.cobalt.radar
596:src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
597:src/cobalt/replay/movers.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
598:src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
599:src/cobalt/smoke/checks.py	M	static import reach	com.cobalt.radar
600:src/cobalt/taxonomy/cli.py	M	static import reach	com.cobalt.radar
601:src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
602:src/cobalt/taxonomy/tunables.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
603:src/cobalt/taxonomy/vault_loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
604:src/cobalt/voice/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
605:src/cobalt/voice/agent.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
606:src/cobalt/voice/cli.py	A	static import reach	com.cobalt.radar
607:src/cobalt/voice/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
608:src/cobalt/voice/confirm.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
609:src/cobalt/voice/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
610:src/cobalt/voice/registry.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
611:src/cobalt/voice/resolve.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
612:src/cobalt/voice/scratch.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
613:src/cobalt/voice/store.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
614:src/cobalt/voice/tools.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
615:src/cobalt/voice/transcribe.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
616:src/cobalt/voice/turn.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
617:src/cobalt/voice/web.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
618:tests/cobalt/radar_migrated_support.py	A	test/documentation; no resident	-
619:tests/cobalt/radar_p2_support.py	M	test/documentation; no resident	-
620:tests/cobalt/setups_shapes.py	A	test/documentation; no resident	-
621:tests/cobalt/stale_db_support.py	A	test/documentation; no resident	-
622:tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
623:tests/cobalt/test_assumed_store.py	A	test/documentation; no resident	-
624:tests/cobalt/test_cards_picks.py	M	test/documentation; no resident	-
625:tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
626:tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
627:tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
628:tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
629:tests/cobalt/test_modelaccess_client.py	A	test/documentation; no resident	-
630:tests/cobalt/test_modelaccess_config.py	A	test/documentation; no resident	-
631:tests/cobalt/test_modelaccess_silence.py	A	test/documentation; no resident	-
632:tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
633:tests/cobalt/test_radar_anatomy.py	M	test/documentation; no resident	-
634:tests/cobalt/test_radar_audit_export.py	M	test/documentation; no resident	-
635:tests/cobalt/test_radar_cards_db.py	M	test/documentation; no resident	-
636:tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
637:tests/cobalt/test_radar_evaluate_cli.py	M	test/documentation; no resident	-
638:tests/cobalt/test_radar_handicap.py	A	test/documentation; no resident	-
639:tests/cobalt/test_radar_handicap_dead.py	A	test/documentation; no resident	-
640:tests/cobalt/test_radar_handicap_dry_run.py	A	test/documentation; no resident	-
641:tests/cobalt/test_radar_handicap_fix_r1_runs.py	A	test/documentation; no resident	-
642:tests/cobalt/test_radar_handicap_group.py	A	test/documentation; no resident	-
643:tests/cobalt/test_radar_handicap_panel.py	A	test/documentation; no resident	-
644:tests/cobalt/test_radar_handicap_runner.py	A	test/documentation; no resident	-
645:tests/cobalt/test_radar_handicap_shadow.py	A	test/documentation; no resident	-
646:tests/cobalt/test_radar_handicap_store.py	A	test/documentation; no resident	-
647:tests/cobalt/test_radar_migrated_harness.py	A	test/documentation; no resident	-
648:tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
649:tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
650:tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
651:tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
652:tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
653:tests/cobalt/test_radar_store.py	M	test/documentation; no resident	-
654:tests/cobalt/test_replay_formations.py	M	test/documentation; no resident	-
655:tests/cobalt/test_replay_line.py	M	test/documentation; no resident	-
656:tests/cobalt/test_replay_movers.py	M	test/documentation; no resident	-
657:tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
658:tests/cobalt/test_rubberband_forms.py	A	test/documentation; no resident	-
659:tests/cobalt/test_setups_d1.py	A	test/documentation; no resident	-
660:tests/cobalt/test_setups_d4.py	A	test/documentation; no resident	-
661:tests/cobalt/test_setups_fix_r2.py	A	test/documentation; no resident	-
662:tests/cobalt/test_setups_fix_r3.py	A	test/documentation; no resident	-
663:tests/cobalt/test_setups_fix_r4.py	A	test/documentation; no resident	-
664:tests/cobalt/test_setups_fixture_cut.py	A	test/documentation; no resident	-
665:tests/cobalt/test_setups_hitchhiker.py	A	test/documentation; no resident	-
666:tests/cobalt/test_setups_lego.py	A	test/documentation; no resident	-
667:tests/cobalt/test_setups_nine_ema.py	A	test/documentation; no resident	-
668:tests/cobalt/test_setups_registries.py	A	test/documentation; no resident	-
669:tests/cobalt/test_setups_second_chance.py	A	test/documentation; no resident	-
670:tests/cobalt/test_setups_vwap_cont.py	A	test/documentation; no resident	-
671:tests/cobalt/test_setups_x5.py	A	test/documentation; no resident	-
672:tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
673:tests/cobalt/test_smoke_k3_sql.py	M	test/documentation; no resident	-
674:tests/cobalt/test_stale_score.py	A	test/documentation; no resident	-
675:tests/cobalt/test_stale_score_db.py	A	test/documentation; no resident	-
676:tests/cobalt/test_taxonomy_store.py	M	test/documentation; no resident	-
677:tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
678:tests/cobalt/test_voice_card_stop.py	A	test/documentation; no resident	-
679:tests/cobalt/test_voice_cli.py	A	test/documentation; no resident	-
680:tests/cobalt/test_voice_config.py	A	test/documentation; no resident	-
681:tests/cobalt/test_voice_confirm.py	A	test/documentation; no resident	-
682:tests/cobalt/test_voice_fix_r1_runs.py	A	test/documentation; no resident	-
683:tests/cobalt/test_voice_lifecycle.py	A	test/documentation; no resident	-
684:tests/cobalt/test_voice_plan.py	A	test/documentation; no resident	-
685:tests/cobalt/test_voice_resolve.py	A	test/documentation; no resident	-
686:tests/cobalt/test_voice_scratch.py	A	test/documentation; no resident	-
687:tests/cobalt/test_voice_store.py	A	test/documentation; no resident	-
688:tests/cobalt/test_voice_tools.py	A	test/documentation; no resident	-
689:tests/cobalt/test_voice_transcribe.py	A	test/documentation; no resident	-
690:tests/cobalt/test_voice_turn.py	A	test/documentation; no resident	-
691:tests/cobalt/test_voice_web.py	A	test/documentation; no resident	-
692:tests/experiments/handicap_h1/conftest.py	A	test/documentation; no resident	-
693:tests/experiments/handicap_h1/h1_cache.py	A	test/documentation; no resident	-
694:tests/experiments/handicap_h1/h1_support.py	A	test/documentation; no resident	-
695:tests/experiments/handicap_h1/test_h1_x0_grouping.py	A	test/documentation; no resident	-
696:tests/experiments/handicap_h1/test_h1_x1_blanks.py	A	test/documentation; no resident	-
697:tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py	A	test/documentation; no resident	-
698:tests/experiments/handicap_h1/test_h1_x3_cell_format.py	A	test/documentation; no resident	-
699:tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py	A	test/documentation; no resident	-
700:tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py	A	test/documentation; no resident	-
701:tests/experiments/handicap_h1/test_h1_x8_x11_group.py	A	test/documentation; no resident	-
702:tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py	A	test/documentation; no resident	-
703:tests/experiments/handicap_h1/test_x12_identity.py	A	test/documentation; no resident	-
704:tests/experiments/handicap_h1/test_xl76_membership_harness.py	A	test/documentation; no resident	-
705:tests/experiments/setups_one/conftest.py	A	test/documentation; no resident	-
706:tests/experiments/setups_one/test_x13_x15_drive.py	A	test/documentation; no resident	-
707:tests/experiments/setups_one/test_x1_premarket_seed.py	A	test/documentation; no resident	-
708:tests/experiments/setups_one/test_x2_coverage.py	A	test/documentation; no resident	-
709:tests/experiments/setups_one/test_x7_x18_stored.py	A	test/documentation; no resident	-
710:tests/experiments/stale_score/conftest.py	A	test/documentation; no resident	-
711:tests/experiments/stale_score/stale_predicates.py	A	test/documentation; no resident	-
712:tests/experiments/stale_score/stale_support.py	A	test/documentation; no resident	-
713:tests/experiments/stale_score/test_x10_replay_as_of.py	A	test/documentation; no resident	-
714:tests/experiments/stale_score/test_x11_audit_replay_fallback.py	A	test/documentation; no resident	-
715:tests/experiments/stale_score/test_x12_published_null.py	A	test/documentation; no resident	-
716:tests/experiments/stale_score/test_x13_tap_keeps_sentence_db.py	A	test/documentation; no resident	-
717:tests/experiments/stale_score/test_x14_daily_missing_keeps_proximity.py	A	test/documentation; no resident	-
718:tests/experiments/stale_score/test_x15_two_clocks.py	A	test/documentation; no resident	-
719:tests/experiments/stale_score/test_x16_last_price_coalesce_db.py	A	test/documentation; no resident	-
720:tests/experiments/stale_score/test_x18_x19_callers.py	A	test/documentation; no resident	-
721:tests/experiments/stale_score/test_x20_x22_bindings.py	A	test/documentation; no resident	-
722:tests/experiments/stale_score/test_x21_htf_tap_no_pair_db.py	A	test/documentation; no resident	-
723:tests/experiments/stale_score/test_x23_next_day_card_db.py	A	test/documentation; no resident	-
724:tests/experiments/stale_score/test_x24_no_print_minutes_db.py	A	test/documentation; no resident	-
725:tests/experiments/stale_score/test_x25_stale_graded_taps_db.py	A	test/documentation; no resident	-
726:tests/experiments/stale_score/test_x26_slug_match_not_evaluable.py	A	test/documentation; no resident	-
727:tests/experiments/stale_score/test_x27_reason_bytes.py	A	test/documentation; no resident	-
728:tests/experiments/stale_score/test_x28_proximity_one_receipts_db.py	A	test/documentation; no resident	-
729:tests/experiments/stale_score/test_x29_ladder_render.py	A	test/documentation; no resident	-
730:tests/experiments/stale_score/test_x2_stale_sequence_db.py	A	test/documentation; no resident	-
731:tests/experiments/stale_score/test_x30_r40_discriminator_db.py	A	test/documentation; no resident	-
732:tests/experiments/stale_score/test_x3_taps_moved_null_db.py	A	test/documentation; no resident	-
733:tests/experiments/stale_score/test_x4_audit_stale_card.py	A	test/documentation; no resident	-
734:tests/experiments/stale_score/test_x5b_prior_session_bars.py	A	test/documentation; no resident	-
735:tests/experiments/stale_score/test_x6_htf_proximity_stale.py	A	test/documentation; no resident	-
736:tests/experiments/stale_score/test_x7_ladder_promoted_stale.py	A	test/documentation; no resident	-
737:tests/experiments/stale_score/test_x8_expiry_on_stale.py	A	test/documentation; no resident	-
738:tests/experiments/stale_score/test_x9_stale_scored_cards_db.py	A	test/documentation; no resident	-
739:tests/experiments/stale_score/test_xl76_devdb_absence.py	A	test/documentation; no resident	-
740:tests/fixtures/radar/_cut_setups_fixtures.py	A	test/documentation; no resident	-
741:tests/fixtures/radar/bars-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
742:tests/fixtures/radar/daily-bars-setups-rubberband.real-shape.csv	A	test/documentation; no resident	-
743:tests/fixtures/radar/membership-setups-rubberband.real-shape.json	A	test/documentation; no resident	-
744:tests/fixtures/radar/screen-handicap.real-shape.csv	A	test/documentation; no resident	-
745:tests/fixtures/replay/_cut_p4_fixtures.py	M	test/documentation; no resident	-
746:tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv	A	test/documentation; no resident	-
747:tests/fixtures/voice/plan-replies.constructed.yaml	A	test/documentation; no resident	-
748:tests/fixtures/voice/plan-utterances.constructed.yaml	A	test/documentation; no resident	-
749:tests/taxonomy/test_predicate.py	M	test/documentation; no resident	-
750:uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
751:RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
752:
753:[exited with code 1]
```
`RESTARTS:` = `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar` — `38`'s set, widened to every resident by the UNCLASSIFIED `.clinerules` row (arrives through the merge from main). Non-`DOCS` rows are `38`'s rows exactly (their line numbers +1 past line 417); the range differs from `38`'s only by `38`'s report (one `DOCS` row). → ESCALATE 1.

## FOR 08
Re-issued WHOLE (r4); supersedes `38`'s `## FOR 08`, `32`'s and `17`'s. r4 changed no file but its own report: the code is `7cdc5774`.
- TIP: code `7cdc5774` (fix r2), parent `0e75e46d`, over `4fc270c7` (fix r1); the merge commit `5bb1f4b5` has parents `10163d51` and `daf36e01`. Branch head at r4 PREFLIGHT `84827649` (`38`'s report commit); r4's report commit sits on it (`git -C /Users/cobalt/cobalt log -1 --format=%h drc/d1-trading-log`, read by the desk after CLOSE). `<main at launch>` = `68862854`. Counts read at branch head `84827649` against main `68862854`: `72` ahead (`git -C /Users/cobalt/cobalt rev-list --count 68862854..84827649`), `71` behind (`git -C /Users/cobalt/cobalt rev-list --count 84827649..68862854`); `git -C /Users/cobalt/cobalt diff --stat daf36e01 68862854 -- . ':(exclude)docs'` → empty (exit 0; empty = main moved docs-only since the merge).
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
- COUNTS: code `7cdc5774`: `15`'s `<p0>` 2588 on `10163d51` → r4 `<p>` 3547 offline (`38`: 3547; `32`: 3547); with-DB `32`'s `<d>` **4066** (4057 + 9; r3 and r4 ran no with-DB: no code changed); live-note `38`'s `<l>` 146 (`32`: 146; r4 ran no live-note leg: no code changed); `32`'s `<F0>` = `<F2>` = `<F3>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`; `<F1>` (at `0018`) = 796 · 40 · `5727e9dfb418376cc48722a3601ca7c3`.
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
  - `tests/cobalt/test_radar_score_migration.py:103–114` — L `newest_four` (ten names `:104–113`, 0018…0008) → 0019…0009 (or the list and its three slices widened to eleven), read by three prefix asserts that break with it: `:116` `reverse_names[:10]`, `:121` `_rollback_paths("0005")[:10]`, `:126` `_rollback_paths("0006")[:10]`.
  - `tests/cobalt/test_tenancy.py:513–526` — L `selected[:10]` (`:515`) of `_rollback_paths("0004")` (`:513`), ten names `:516–525`, 0018…0008 → 0019…0009 (or the slice widened to eleven).
  - `tests/cobalt/test_archiver_migrations.py:84–95` — L `FORWARD[-10:]` = 0008…0018 → 0009…0019 · `:101–112` — L `REVERSE[:10]` (ten names `:102–111`) = 0018…0008 → 0019…0009, the mirror of `:84–95` · `:129–138` — L `_rollback_paths("0009")` exact, eight → nine · `:139–150` — L `_rollback_paths("0007")` exact, ten → eleven · `:170` — N `numbers == [*range(1, 12), 13, 14, 15, 16, 17, 18]` → `…, 18, 19]` · `:171` — N `numbers[-8:-6] == [10, 11]` → `numbers[-9:-7]` · `:172` — N `numbers[-1] == 18` → `19`.
  - `tests/cobalt/test_archiver_migrations.py:54` + `:495–505`, asserted `:516–519` and `:528–531` — T, WITH-DB (`test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4`, `:470`): every `CREATED_TABLES` name outside `NEW_TABLES`, `P4_TABLES`, `DRC_D1_TABLES` (`:54`) and `"voice_turns"` (`:503`) must survive `--down-to 0009` and `--down-to 0007`. A table `0019` adds to `CREATED_TABLES` is numbered above both bounds, so both rollbacks drop it: it joins the exclusions, or `:517` goes red with-DB.
  - NOT PINS (read; `0019` moves none): `test_migrate_proof.py:1510` (`FORWARD[0]`), `:1528` (`_rollback_paths("0005")[0]`, value-free); by-name slices `test_radar_score_migration.py:92–93`, `test_tenancy.py:473`, `:479`; suffixes `test_tenancy.py:527–534`, `test_radar_score_migration.py:122`, `:127`; paths by name `test_drc_k1_experiments.py:362–363`, `test_drc_k1_store.py:45–46`.
- `08`'s own list (`prompts/2026-09-28/08-drc-d2-fix-r1-build.md:106`) is pre-merge and name-grep-based: re-pointed from THIS list.
- RESTARTS (`10163d51..84827649`, derived under `## RESTARTS`; r4's report commit adds one `docs/` path, no restart by L42): `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. It is widened to all residents by the UNCLASSIFIED `.clinerules` (ESCALATE 1), OWED to the DRC deploy (R74).
- `CLAUDE.md` in the worktree is main's stub (R33 (4)).

### FOR 08 proof (each its own call, `grep -n -F … <R4>`, re-run after §0 was written, 17:45 EDT; the R4-1 block spans lines 519–586)
| pattern | exit | hits in the R4-1 block | hits outside (named, not counted) |
|---|---|---|---|
| `0019…0009` | 0 | `:578` `test_radar_migration.py` · `:579` `test_radar_score_migration.py` · `:580` `test_tenancy.py` · `:581` `test_archiver_migrations.py` (`:101–112`) — exactly the four | `:5` (§0), `:50`, `:55` (R0), `:267` (P12 conclusion), this table and `## FOR THE CHECK` |
| `widened to all residents by the UNCLASSIFIED` | 0 | `:585` the RESTARTS bullet | `:51`, `:58` (R0), this table |
| `read at branch head` | 0 | `:521` the TIP bullet | `:53` (R0), this table, `## FOR THE CHECK` |

## FOR THE CHECK
- R0: four greps with exit codes under `## R0 RED` (`0019…0009` on R3 exit 0 `581:` only; caveat on R3 exit 1, on R2 exit 0 `603:`; `read at branch head` on R3 exit 1).
- `## FOR 08` written from 42's R4-1 block verbatim, 11 values filled (listed under `## THE ROWS`).
- P1–P12 under `## PIN PROOF`. `LINE MOVED`: none.
- The three `## FOR 08` proof greps: the table above.
- O: `3547 passed, 525 skipped, 1 xfailed, 20 warnings in 574.49s (0:09:34)`.
- `## W WITH-DB`: NOT RUN.
- RESTARTS table under `## RESTARTS` (525 `DOCS` rows summarised as count and line ranges, every other line verbatim).
- The report commit's `git -C /Users/cobalt/cobalt-wt/drc-d1 show --stat --format=%h HEAD`: in the final chat message after CLOSE.
- No path on the branch changed but this report.

## CONTINUE
next: none — CLOSE done at the stop line.

## ESCALATE
1. ESCALATE: UNCLASSIFIED .clinerules — OWED to the DRC deploy (R74). `cobalt jobs restarts 10163d51..84827649` row 3, exit 1; it arrives through the merge from main and widens `RESTARTS:` to every resident. [17:36 EDT]
2. RECORD: `<main at launch>` read `68862854` at 17:33:45 EDT (the desk's launch-row commit `688628547837…`, over the `42be9c1a` the desk read). `git -C /Users/cobalt/cobalt diff --stat daf36e01 68862854 -- . ':(exclude)docs'` is empty: main is still docs-only since the merge. Ahead `72` / behind `71` at branch head `84827649` (`38`: 71 / 41, symbolic refs).
3. RECORD: the L74 block (see `## L74`) arrived and was not followed.

DRC MERGE FIX R4 BUILT report-only (code 7cdc5774; tip = this report's commit) | on 7cdc5774 | files: 1 (src 0, tests 0, report 1) | offline 3547/0 | with-DB not run | cobalt_dev: 0013 | .env: none | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | FIX: 1 | ESCALATE: 3
