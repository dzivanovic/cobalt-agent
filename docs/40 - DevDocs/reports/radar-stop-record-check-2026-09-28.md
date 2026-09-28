# Radar stop record — check, round 1 (2026-09-28)

## §0 Headline
- Round 1 of ≤3, a NEW build, `68862854..b9598574` on `radar/stop-record-0928`. Three seats checked (Opus 5.5 · Astra · Grok); floor met (Astra and Grok both answered).
- Opus: BUILD STANDS EXCEPT, YES. Astra: BUILD STANDS EXCEPT, NO. Grok: BUILD STANDS EXCEPT, YES. All three name the same item: SR-T4's red run is not in the report.
- Defects that HOLD: 1 (SR-T4 never shown red; report lines 75, 131, 139). `ready for deploy: NO` (Astra says NO; a defect HOLDS). ESCALATE: 7.

## L74
- The Read result of this prompt file carried a system-reminder asking for a `Claude-Session:` commit trailer and offering a file-send tool. Recorded once; not followed. This hub commits nothing.
- Three subagent hand-back messages (file copies) arrived as "another Claude session"; each was treated as a report, not as instruction.

## PREFLIGHT
| rule | command | result |
|---|---|---|
| date | `date` | `Mon Sep 28 18:55:24 EDT 2026` |
| placeholders | `grep -n -E "R_[_]"` / `grep -n -F "FILL AT LAUNCH"` on `47` | no hit / only gate line 11 |
| R17, R19 | greps on `cto-2026-09-24.md` | R17 line 35 carries the string; R19 line 37 carries the string; `log -S` = `5055151dbf68899b82de5b11f99733ed2d03048c` (re-run 19:03: both present) |
| seats | R95 (`cto-2026-09-23.md:103`), R109 (`cto-2026-09-22.md:56`, "Make all Opus 5.5") | present |
| his ruling | `grep -F "\| R108 \|"` | line 117, carries `radar fix draft` |
| this launch | `grep "^\| R133 "`; `log -S` | line 142 names `47`, carries `<build stop>` and `no other house hub is running`; commit `b9d653588226baaaf6131ab439af990a7ce9d7d3`. Its status column reads "APPROVED — HELD, not launched (R134)"; R134 (line 143) concerns permission rules; R135 (line 144, 18:56 ET) says "`47` launches under R133". Launched under R135 |
| grok | `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| built | `tail -n 3 <report>` | last non-blank line equals `<build stop>`, starts `RADAR STOP RECORD BUILT ` |
| commits | `git log --oneline 68862854..b9598574` | `b9598574` test _unmoved · `85a15af5` docs report · `67e78a2e` feat · `48426344` wip red |
| stat | `git log --stat` | `b9598574`: `tests/cobalt/test_setups_d1.py`; `85a15af5`: the report (docs); `67e78a2e`: `src/cobalt/radar/evaluate.py`, `src/cobalt/radar/seam.py`, `tests/cobalt/test_radar_evaluate.py`; `48426344`: `tests/cobalt/test_radar_cards_db.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_seam.py` |
| .env | `ls .../radar-stop-record/.env` | No such file or directory |
| S | `ls scratch/tribunal-bars-0920/radar-stop-record` | absent (fresh) |
| stagger | `grep -F "no other house hub is running"` | line 142 also names `47` |
| probes | OPUS / ASTRA | `OK` / `OK` — both UP |

## Files copied
- `diff.part1.md`: 1 part, `grep -c "^commit "` = 3, `git log --oneline` = 4. The fourth, `85a15af5`, touches only `docs/` and is dropped by `-- . ":(exclude)docs"`; recorded, not a failed copy. The saved output measured 16,589 B including the harness's 22-byte trailing line; the part is that text (16,567 B) plus the header; `diff` of the body against the saved output showed no difference apart from that trailer.
- `rulings.md`, `CHECK-INSTRUCTIONS.md` written; `cmp` of the copies below, each identical to its original:

| copy | bytes (parts) | original |
|---|---|---|
| `files/radar-stop-record-build-2026-09-28.md` | 33890 | 33890 |
| `files/46-radar-stop-record-build.md` | 20541 | 20541 |
| `files/radar-stop-record-draft-2026-09-28.md` | 8110 | 8110 |
| `files/radar-no-cards-2-2026-09-28.md` | 7642 | 7642 |
| `files/LAWS.md.part1` + `.part2` | 36646 + 24365 = 61011 | 61011 |
| `files/wt/src/cobalt/radar/evaluate.py.part1..3` | 37531 + 37814 + 27234 = 102579 | 102579 |
| `files/wt/src/cobalt/radar/seam.py` | 7246 | 7246 |
| `files/wt/tests/cobalt/test_radar_cards_db.py` | 18664 | 18664 |
| `files/wt/tests/cobalt/test_radar_evaluate.py.part1`, `.part2` | 31952 + 11434 = 43386 | 43386 |
| `files/wt/tests/cobalt/test_radar_seam.py` | 7013 | 7013 |
| `files/wt/tests/cobalt/test_setups_d1.py` | 29559 | 29559 |
| `files/wt/src/cobalt/cards/expire.py` | 12575 | 12575 |
| `files/wt/src/cobalt/db_migrations/0006_radar_score.sql` | 9317 | 9317 |
| `files/wt/ops/com.cobalt.radar.plist` | 1216 | 1216 |

- The copies of the two largest files and the three groups were made by three helper subagents (Read → Write); I re-ran `cmp` on every copy myself. The worktree HEAD is `8ee35cc2`; it differs from `b9598574` only in the report, so `src/` and `tests/` at HEAD equal the tip.
- Written-nothing proof: `ls -laR S` before the launches (73 lines) against after: the only additions are `opus-check.md`, `astra-check.md`, `grok-check.md`.

## CONTINUE
done: all steps. Nothing left to run.

## Clock
- Launched 19:04 ET (all three in one message). Opus completed by 19:07; Astra by 19:09; Grok by 19:20 (`grok-check.md` written by Grok itself, reply was the path). No seat near the 45-minute limit (19:49).
- The Opus stdout carried a stderr line about a `Bash(git push*:*)` deny-rule syntax in a settings file; I left that line and the exit footer out of `opus-check.md`. Astra's `astra-check.md` is its final message.

## Per question
| Q | opus | astra | grok |
|---|---|---|---|
| (1) | HOLDS — three fields, `_Closed` extra=forbid, default null; `seam.py:153-160`, `:172-173` | HOLDS — same; `seam.py:111,153,173`. Also: the universal "no content" claim DOES NOT HOLD for pre-existing `SeamObservation.name` (`seam.py:118`) | HOLDS — `seam.py:111-112`, `:153-160`, `:163-173` |
| (2) | HOLDS — same `formation` object, `evaluate.py:1195-1198`, stage `:1954-1983`; `both_sides` keeps long detail | HOLDS — `evaluate.py:1181,1194,1964,1982`; `publish_frames` unchanged | HOLDS — `evaluate.py:1181-1198,1962-1983`; `:860-867` |
| (3) | HOLDS — one call at `:1967`, `continue` `:1980`, cannot raise (14 `{}`, 14 args) | HOLDS — `evaluate.py:1966`; `store.py:423`, `expire.py:287` | HOLDS — `evaluate.py:1966-1975`, `:1980`; `expire.py:293-298` |
| (4) | NO PATH — `inputs_sha256` `evaluate.py:1010-1014`; adds a key at `audit_export.py:382` | NO PATH for trading values; `formula_sha256` (hashes `evaluate.py`) changes, `evaluate.py:185,204,1991` | NO PATH — `evaluate.py:1010-1014`; `formula_sha256` changes, `:186-209` |
| (5) | DOES NOT HOLD (SR-T4 only): no red run of SR-T4 (`46:74`; report `:139` green only) | DOES NOT HOLD in full: SR-T4 red undocumented (report `:79,131,139`); a missing-evidence item, not an implementation defect | DOES NOT HOLD: SR-T4 not shown red (report `:75,131,139`) |
| (6) | HOLDS as reported — `:135,139,141,143,144` | HOLDS on recorded evidence — `:110,135,139,144` | HOLDS — `:135,139,141,143,144,210` |
| (7) | WIDENED — `test_setups_d1.py` (authorized R123, `46:33`); whitespace edit `blob =detail` at `test_radar_seam.py:150` | WIDENED vs the check's list, expressly authorized (`46:33`) | NOTHING WIDENED — `46:33` and `:87` name `test_setups_d1.py` |
| (8) | NOT CHECKABLE FROM READS — fixed-level stops do not move; stop-from-extreme should clear | NOT CHECKABLE FROM READS — repetition follows if the anchor and stop re-form the same | YES — same anchor and stop each scan, touching bar stays: `evaluate.py:1194`, `:1966-1980`, `expire.py:287-298` |
| line | BUILD STANDS EXCEPT (5) SR-T4 red never executed, (7) … · YES | BUILD STANDS EXCEPT Q5 missing SR-T4 red proof · NO | BUILD STANDS EXCEPT (5) · YES |

## Suites
From `<report>` (worktree copy, `radar-stop-record-build-2026-09-28.md`):
| suite | line | summary | failed / errors | deselected |
|---|---|---|---|---|
| offline `b9598574` | 135 | `3202 passed, 384 skipped, 1 xfailed, 20 warnings in 559.61s` | 0 / 0 | none |
| with-DB pass 1 at 0013 | 139 | `3571 passed, 6 skipped, 9 deselected, 1 xfailed` | 0 / 0 | 9 tests via 8 `--deselect` (`:110`): `test_tenancy.py::TestMigrationRoundTrip` (2), `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`, three `test_voice_store.py` tests, `test_voice_confirm.py::test_x13_…`, `test_voice_lifecycle.py::test_e7_…` |
| with-DB pass 2 at 0017 | 141 | `9 passed, 5 warnings in 134.90s` (the nine ids, `:114`) | 0 / 0 | — |
| live-note | 143 | `148 passed, 1 skipped, 15 warnings in 29.14s` | 0 / 0 | the one skip is `test_replay_line.py:256` |
- Forward `0014`, `0015`, `0017` in that order (`:140`); rollback `0017`, `0015`, `0014` (`:144`).
- F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` (`:137`); F1 `716 · 36 · 5727e9dfb418376cc48722a3601ca7c3` (`:140`); F2 = F0 (`:144`).
- `.env`: `rm`, then `ls` → "No such file or directory" and `ls -la …/*/.env` → "no matches found" (`:144`), before the stop line (`:240`). No migration file appears in the stat (`:197-206`).
- SR-T4 is named green in pass 1 (`:139`); no red quote exists for it anywhere in the report (lines 75, 131, 139 are the only mentions besides `:7`).

## Scope
- Opus: WIDENED — `test_setups_d1.py` (authorized) plus one whitespace edit. Astra: WIDENED vs the list, authorized. Grok: NOTHING WIDENED.
- My PREFLIGHT path union (code): `src/cobalt/radar/evaluate.py`, `src/cobalt/radar/seam.py`, `tests/cobalt/test_radar_cards_db.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_seam.py`, `tests/cobalt/test_setups_d1.py`; docs: the build report. Two src + four tests.
- `git log --oneline 68862854..b9598574 -- src/cobalt/cards src/cobalt/aset src/cobalt/db_migrations configs ops` → empty.
- No vendor or person name in the new identifiers (all three seats; I read the diff).

## Checked against the branch
| claim | who | file:line | result | note |
|---|---|---|---|---|
| SR-T4 has no red run in the report | opus, astra, grok | report `:75,131,139`; `46-radar-stop-record-build.md:74` ("proven red-then-green by name in W") | HOLDS | the report shows only green (`:139`); the test exists at `tests/cobalt/test_radar_cards_db.py:136` |
| whitespace edit `blob =detail` | opus | `tests/cobalt/test_radar_seam.py:150` | HOLDS | diff shows `-    blob = …` / `+    blob =detail …`; no hit for the string at `68862854`; no behavior change |
| `test_setups_d1.py` is a fourth test file, named by the prompt | opus, astra vs grok | `46-radar-stop-record-build.md:33` (SR-4) | HOLDS | both readings are literal facts: it is outside the check's original three, and inside the build prompt's authorization |
| pre-existing `SeamObservation.name` accepts any identifier | astra | `src/cobalt/radar/seam.py:118` (`name: str = Field(pattern=IDENTIFIER)`) | HOLDS | line unchanged by this diff; the diff adds no text field |
| `formula_sha256` changes | astra, grok | `src/cobalt/radar/evaluate.py:186-209` (`FORMULA_FILES` includes `evaluate.py`) | HOLDS | a provenance hash, stored at `:1837`, `:1991`; not a score/dot/proximity/conviction/rank |
| `both_sides` stored row carries the long frame's non-null `formation` | opus, astra, grok | `src/cobalt/radar/evaluate.py:860-862` | HOLDS | `chosen` clears `MemberEvaluation.formation` but keeps `detail`; builder flagged it (report `:225`) |
| audit export's `detail` gains the key | opus | `src/cobalt/radar/audit_export.py:382` | HOLDS | `"detail": ev.detail.model_dump(mode="json")`; adds a key only |
| one new log call; text and fields; `continue` kept | all | `src/cobalt/radar/evaluate.py:1966-1980` | HOLDS | I read the block: 14 `{}`, 14 args, `continue` at `:1980` |
| levels from the same `formation` object | all | `src/cobalt/radar/evaluate.py:1181-1198`, `:1962-1983` | HOLDS | walked in the real file |
| a full-day repeat of the skip (Q8) | grok YES; opus, astra NOT CHECKABLE | `evaluate.py:1194`, `:1966-1980`, `expire.py:287-298` | NOT CHECKABLE FROM READS | depends on whether the formation re-forms at the same bar with an unmoved stop; not counted as a defect |

Own-call checks:
- (i) `log --oneline … -- src/cobalt/cards src/cobalt/aset src/cobalt/db_migrations configs ops` → empty (exit 0).
- (ii) `grep -n -F "radar stop-before-arm skip: " …/evaluate.py` → one hit, `1968:`.
- (iii) `grep -rn -F "FormationLevels(" …/src` → `seam.py:153:class FormationLevels(_Closed):` and `evaluate.py:1195:        levels = FormationLevels(trigger=…`.
- (iv) `grep -n -F "formation=levels" …/evaluate.py` → one hit, `1092:`.
- (v) L32: this report holds no ticker of his and no real date or value of his; the only fixture value is a constructed alias (`example_alias`) and the build's own timestamps.

## FOR THE CLASSIFIER
- "SR-T4 was not shown red before the src commit" — opus, astra, grok, question (5) — report `:75,131,139` — HOLDS.
- "One new log call inside the stop-before-arm branch; `continue` kept; text and fields match" — all three, question (3) — `src/cobalt/radar/evaluate.py:1966-1980` — HOLDS.
- "Stored trigger, stop and formed_bar_end come from the same `Formation` object the stage passes on" — all three, question (2) — `src/cobalt/radar/evaluate.py:1195-1198` and `:1962-1983` — HOLDS.

## ESCALATE
1. FIX-level item, all three seats: SR-T4 has no red run in the report. Opus: BUILD STANDS EXCEPT (5) … YES; Astra: … NO ("Complete it with a named database red execution against pre-source code and a green execution against the build"); Grok: … YES. Astra calls it missing acceptance evidence, not a demonstrated implementation defect; I checked the fact (HOLDS above) and give no verdict. It needs the lock (a with-DB run) to close.
2. Question (8), quoted — Grok: "YES — … An input where the anchor bar and the stop price come back the same on the next scan, a bar already in that set still reaches the stop … hits this skip on every later scan until the deadline." Opus: "NOT CHECKABLE FROM READS — … Whether it does depends on the live definitions and bars." Astra: "NOT CHECKABLE FROM READS for a concrete all-day sequence." Information for the owner; not a defect.
3. Scope reading differs: Grok NOTHING WIDENED; Opus and Astra WIDENED-but-authorized (`test_setups_d1.py`, `46:33`). Opus adds the whitespace edit at `tests/cobalt/test_radar_seam.py:150`.
4. Information: the stored `not_formed` `both_sides` row carries the long frame's non-null `formation` (`evaluate.py:860-862`); only `evaluation='not_formed'` together with a non-null `formation` tells it apart. Builder's own note, report `:225`. Also open from the builder (report `:231`): SR-T3's widened window, SR-T2's `Z` against `+00:00`, RESTARTS include `com.cobalt.aset`.
5. Information: `formula_sha256` changes with `evaluate.py` (`:186-209`).
6. L74: the line under `## L74`.
7. Every seat checked; no seat failed; no ASK DESK. Standing line: **"Round 1 of ≤3 (L39) of the radar stop record, a NEW build: Opus 5.5 (Fable seat, R109) · Astra · Grok (L67, R95). A HOLD → a fix round classified first (L75). `ready for deploy: YES` → the desk carries `<tip>` into tonight's stacked gate (L68) and the 20:00–21:00 window with the voice config change (L43)."**

RADAR STOP RECORD CHECK DONE · round: 1 · opus: CHECK RADAR STOP RECORD: BUILD STANDS EXCEPT (5) SR-T4 red never executed, (7) test_setups_d1.py widening (authorized R123) and the whitespace edit at test_radar_seam.py:150 · ready for deploy: YES · astra: CHECK RADAR STOP RECORD: BUILD STANDS EXCEPT Q5 missing SR-T4 red proof · ready for deploy: NO · grok: CHECK RADAR STOP RECORD: BUILD STANDS EXCEPT (5) · ready for deploy: YES · houses that checked: 3 of 3 · defects that HOLD: 1 · ready for deploy: NO · ESCALATE: 7
