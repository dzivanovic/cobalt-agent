# note-daily-stop — check report 2026-10-01 (pass 1)

Started 16:26 EDT 2026-10-02 (`date`). Card: `docs/40 - DevDocs/prompts/2026-10-01/06-note-daily-stop-card.md`.

## §0 Headline
- House A was Grok (Sol is out of meter until Oct 4th, 2026 2:06 PM). There were 7 findings: 4 mine, 3 Grok's. Nothing was dropped.
- Fixed in `3d04d48d` (O4 and H3): when the attestation strike fails, `/attest` leaves the stop line alone and shows FAILED, so the box and the stop never disagree.
- O1 and H1 hold but are not fixed. Before the first attest, Cobalt's own morning line is taken for his hand edit when the stored stops have changed since 05:15. Choosing the fix is his call (L28 against L3); the tests are pinned `xfail(strict)`.
- Open for pass 2: O2 (a box he ticks in the note: unsettled), O3 (the CLI attest: outside the row) and H2 (rejected by the row).
- On `3d04d48d`: offline 3793/0, with-DB 4563/0, live-note 146/0. `cobalt_dev` is at 0013 (F2 = F0) and `.env` is removed. House B is needed (the card makes it mandatory, and items are open), so ready is NO.

## L74
- A system block in this session asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/CHECK-HUB.md` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" …/06-note-daily-stop-card.md` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/06-note-daily-stop-card.md"` | 0 | `d0b0350ac318fb0bcbc34b8d801bb179b8a92173` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/06-note-daily-stop-card.md"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- "docs/…/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R15 | `grep -n "^| R15 " cto-2026-10-01.md` | 0 | `23:| R15 | 08:40 ET | **HIS RULING** … after he attests a size it must show only that sheet's stop. Stored settings are swapped; card 06-note-daily-stop-card.md. | APPROVED |` |
| R15 committed | `git -C … log -1 --format=%H -S"| R15 |" -- "docs/…/cto-2026-10-01.md"` | 0 | `f5e01b382073e93a424eefbf183d40c4fb2c6182` |
| house gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | `35:| R17 | 07:32 ET | … STANDING: Bash(grok *) is a PRE-APPROVED string …` |
| house gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | `37:| R19 | 07:36 ET | … the four house strings are pre-approved … indefinitely …` |
| R19 committed | `git -C … log -1 --format=%H -S"| R19 |" -- "docs/…/cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 16:26:35 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/note-daily-stop-1001` |
| head | `git log --oneline -1` | 0 | `56c67dff docs(note-daily-stop): build report — 0b678bd0` |
| docs-only above TIP | `git log --stat --format=%h 0b678bd0..HEAD` | 0 | `56c67dff` and `96da11d2`, each only `.../reports/note-daily-stop-build-2026-10-01.md` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: note-daily-stop · tip: 0b678bd0 \| on 5ed7c3fd \| migration: none \| offline 3791/0 \| with-DB 4561/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 3 of 3 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 2` |
| range | `git log --oneline 5ed7c3fd..0b678bd0` | 0 | `0b678bd0 fix(note-daily-stop): after an attest …` · `4f65090d wip(note-daily-stop): red — D2 D3 tests` |
| range paths | `git log --stat --format=%h 5ed7c3fd..0b678bd0` | 0 | `0b678bd0`: `docs/40 - DevDocs/cobalt/aset/web.md`, `docs/40 - DevDocs/cobalt/prefill/daily.md`, `src/cobalt/aset/web.py`, `src/cobalt/prefill/daily.py`; `4f65090d`: `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_drc_settings.py` |
| no .env here | `ls <WT>/.env` | 1 | `No such file or directory` |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | `1.2.14` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. … try again at Oct 4th, 2026 2:06 PM.` → METER |

Path union for `## Scope`: `src/cobalt/aset/web.py`, `src/cobalt/prefill/daily.py`, `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_drc_settings.py`, two DevDocs pages.

house A: Grok · house B, if needed: Gemini. MANDATORY: `HOUSE B: mandatory — vault notes` → pass 2 runs; Gemini is the second house up.

## Files copied
Folder `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/note-daily-stop-check`.
- `diff.md` (Write): `git log -p 5ed7c3fd..0b678bd0 -- . ":(exclude)docs"` output under its header; `grep -c "^commit "` → `2` = PREFLIGHT's 2 commits; `wc -l` 451 = 450 lines of output + the header.
- `rulings.md` (Write): the R15 grep, its command line above it.
- By `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh` (cmp proves byte-identical; its printed bytes):
  - `COPIED 6587 …/files/06-note-daily-stop-card.md`
  - `COPIED 34476 …/files/note-daily-stop-build-2026-10-01.md`
  - `COPIED 10607 …/files/cto-2026-10-01-words.md`
  - `COPIED 102804 …/files/wt/src/cobalt/aset/web.py`
  - `COPIED 27668 …/files/wt/src/cobalt/prefill/daily.py`
  - `COPIED 10183 …/files/wt/src/cobalt/settings/drc.py`
  - `COPIED 17004 …/files/wt/src/cobalt/settings/models.py`
  - `COPIED 47459 …/files/wt/tests/cobalt/test_aset_web.py`
  - `COPIED 24518 …/files/wt/tests/cobalt/test_drc_settings.py`
  - `COPIED 29052 …/files/wt/docs/40 - DevDocs/cobalt/aset/web.md`
  - `COPIED 6882 …/files/wt/docs/40 - DevDocs/cobalt/prefill/daily.md`
  - `COPIED 59388 …/files/wt/src/cobalt/vaultwrite/writer.py`, `COPIED 8218 …/files/wt/src/cobalt/vaultwrite/markers.py`, `COPIED 9770 …/files/wt/src/cobalt/daymode/note.py` (the writer the D3 unit runs through, and `/attest`'s note path; context for the house).
- `HOUSE-INSTRUCTIONS.md` (Write): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` (the card has none: said so), `## RECORDS`, the Files paragraph.
- House A start: `date` 16:29:25 EDT; R17 and R19 gates re-run (one row each); `ls -la <S>` → `diff.md`, `files`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`; `cd <AGY>`; Grok launched `run_in_background` (task `b3lk92y78`); `cd <WT>`; `git status --short --branch` → `## s3/note-daily-stop-1001`.

## OWN FINDINGS
Read: the card, R15 (`cto-2026-10-01-words.md:30-31`), the diff, `aset/web.py` 490-610 and 1239-1290, `prefill/daily.py` 540-680, `settings/drc.py` 100-229, `daymode/cli.py` 80-209, `daymode/note.py` `read_attestation` / `reconcile` / `daily_note_path`, `vaultwrite/writer.py` `skip_if`, the build report, `areas/cobalt.md` (the two sections).

FINDING O1
ROW: D3
CLAIM: `src/cobalt/prefill/daily.py:174-182` decides "his hand edit" by comparing the note's line with the both-values text rendered from the settings NOW; when the stored stops change after 05:15 (the change line, which is how the swapped data gets fixed), Cobalt's own line no longer matches, the rewrite is skipped and the sheet says "your hand edit stands" (`aset/web.py:602-603`) although he never touched the line.
RUN: TEST `tests/cobalt/test_aset_web.py`, in `TestAttestRewritesTheDailyStop`:
```python
    def test_o1_a_settings_change_after_the_note_was_written_is_not_his_hand_edit(self, attest_world):
        attest_world.settings["account.daily_stop_full"] = "8484"
        banner = _attest("full.htk")
        assert "your hand edit stands" not in banner, banner
        assert _stop_lines(attest_world.note) == ["Daily HARD Stop: full $8484"]
```
EXPECT: red — `assert 'your hand edit stands' not in ...` fails; the line keeps `full $4242 · half $2121`.

FINDING O2
ROW: D3
CLAIM: an attestation he makes by ticking the box in the note is read back and recorded through `store.attest_sheet` (`src/cobalt/aset/web.py:517-519`), but the `Daily HARD Stop:` line is never rewritten on that path — only `/attest` (`aset/web.py:1280`) calls the rewrite.
RUN: TEST `tests/cobalt/test_aset_web.py`, in `TestAttestRewritesTheDailyStop`:
```python
    def test_o2_a_box_he_ticks_in_the_note_also_rewrites_the_stop(self, attest_world):
        note = attest_world.note
        note.write_text(
            note.read_text(encoding="utf-8").replace("- [ ] full.htk", "- [x] full.htk"), encoding="utf-8"
        )
        client.get("/")
        assert attest_world.day_store.calls == ["full.htk"], "the tick was read back as the attestation"
        assert _stop_lines(note) == [f"Daily HARD Stop: full ${_STOP_FULL}"]
```
EXPECT: red at the last assert — the line still holds both values.

FINDING O3
ROW: D3
CLAIM: `cobalt daymode attest` (`src/cobalt/daymode/cli.py:188-196`) records an attestation and strikes the box through `_sync_note`, but never rewrites the `Daily HARD Stop:` line.
RUN: COMMAND `grep -n -F "write_attested_daily_stop" src/cobalt/daymode/cli.py`
EXPECT: no output (exit 1).

FINDING O4
ROW: D3
CLAIM: the row says the rewrite happens "in the same call that strikes the attestation, so the two never disagree", but `/attest` (`src/cobalt/aset/web.py:1270`, `:1280`) rewrites the stop even when the strike itself failed (`_write_daymode_note` swallows the failure into a `⚠` suffix, `aset/web.py:587-589`), leaving a note that shows the full sheet's stop with no box ticked.
RUN: TEST `tests/cobalt/test_aset_web.py`, in `TestAttestRewritesTheDailyStop`:
```python
    def test_o4_a_failed_strike_does_not_leave_a_rewritten_stop_beside_an_unticked_box(self, attest_world, monkeypatch):
        def _boom(*a, **k):
            raise RuntimeError("constructed: strike failed")

        monkeypatch.setattr(web_module.daymode_note, "write", _boom)
        _attest("full.htk")
        text = attest_world.note.read_text(encoding="utf-8")
        assert "- [x] full.htk" not in text
        assert _stop_lines(attest_world.note) == [_BOTH], "the stop and the strike never disagree"
```
EXPECT: red at the last assert — the line reads `Daily HARD Stop: full $4242`.

## Findings
House A Grok: completion notice 16:41:06 EDT (`date`); `ls -la <S>` → `house-a.md` 2735 bytes, 16:40, written by Grok; stdout ended with its path. Last line `FINDINGS: 3`. Each block's `RUN:` line is followed by a `def test_` (THE DROP: none dropped).
- H1 · Grok · D3 · before the first wrap a line that is not a fresh both-sheets render is skipped as a hand edit, so an attest after the stops change does not write the current value · TEST
- H2 · Grok · D3 · a failed stop write leaves the note's attestation struck; the row says a failed vault write leaves the attestation unchanged · TEST
- H3 · Grok · D3 · a failed strike is swallowed and `/attest` still rewrites the stop, so the stop and the unticked box disagree · TEST

H1 is O1's claim; H3 is O4's claim. Each is run as written.

## Dropped
none

## RUNS
Each TEST pasted into `tests/cobalt/test_aset_web.py` with the Edit tool (mine inside `TestAttestRewritesTheDailyStop`; the house's at module level as written). First run, all six together: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_aset_web.py -k "…six names…"` → `6 failed, 57 deselected in 0.89s`.
| id | source | run | output (first failing line) | verdict |
|---|---|---|---|---|
| O1 | Opus | TEST `test_o1_a_settings_change_after_the_note_was_written_is_not_his_hand_edit` | `test_aset_web.py:1068: AssertionError: <div class="saved">Attested full.htk … Daily HARD Stop: your hand edit stands — not rewritten (L28: human text wins).` | HELD, NOT FIXED — `src/cobalt/prefill/daily.py`: the fix must choose, for a bare line in Cobalt's own shape whose values are not today's stored stops, between overwriting it (it may be his in-shape hand fix — L28) and keeping a stale Cobalt line (L3). His ruling (`## DECISIONS` 1) |
| O2 | Opus | TEST `test_o2_a_box_he_ticks_in_the_note_also_rewrites_the_stop` | run 1: `:1077: AssertionError: the tick was read back as the attestation · assert [] == ['full.htk']` — red for another reason (the fixture's note has no day-mode boxes until a first write). Form repaired once (an `_attest("half.htk")` first, the row cleared, the ticks swapped; the stop-line assertion unchanged): `:1079: … assert ['half.htk'] == ['half.htk', 'full.htk']` — the offline GET `/` does not reach the read-back | UNSETTLED — the test cannot reach the note read-back in this fixture without changing what it asserts; removed with the Edit tool. OPEN |
| O3 | Opus | COMMAND `grep -n -F "write_attested_daily_stop" src/cobalt/daymode/cli.py` | (no output, exit 1) | REJECTED — card D3: "AFTER HE ATTESTS a size (`POST /attest`, `src/cobalt/aset/web.py:1202`…)" names the one entry path; the CLI path is outside it. OPEN |
| O4 | Opus | TEST `test_o4_a_failed_strike_does_not_leave_a_rewritten_stop_beside_an_unticked_box` | `:1088: AssertionError: the stop and the strike never disagree · 'Daily HARD Stop: full $4242' != 'Daily HARD Stop: full $4242 · half $2121'` | HELD |
| H1 | Grok | TEST `test_stale_cobalt_stop_line_is_rewritten_to_the_attested_sheet` | `:1095: AssertionError: assert ['Daily HARD ...· half $2121'] == ['Daily HARD ...: full $4343']` | HELD, NOT FIXED — as O1 (same defect) |
| H2 | Grok | TEST `test_failed_stop_write_leaves_the_attestation_line_unchanged` | `:1112: AssertionError: attestation line changed · '- [x] full.htk' is contained here` | REJECTED — card D3: "a failed rewrite is a loud failure on the sheet (L1), never a silent skip, and the attestation itself still stands"; test (e) of the row is satisfied by the attestation standing. Removed with the Edit tool. OPEN |
| H3 | Grok | TEST `test_failed_attestation_strike_does_not_rewrite_the_stop` | `:1122: AssertionError: assert ['Daily HARD ...: full $4242'] == ['Daily HARD ...· half $2121']` | HELD |

After removing O2 and H2: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_aset_web.py` → `4 failed, 57 passed in 1.70s` (O1 `:1068`, O4 `:1079`, H1 `:1086`, H3 `:1095`). Commit `4b99561c wip(note-daily-stop): check red — O1 O4 H1 H3`.

## FIXES
| id | change | run | commit |
|---|---|---|---|
| O4 · H3 | `src/cobalt/aset/web.py`: `_write_daymode_note` returns `(suffix, failed)`; `/attest` with a failed strike renders `_failed("<attested>\nThe attestation stands. Daily HARD Stop NOT rewritten: the attestation was not struck in the note, and the two never disagree.")` and does not call `_write_attested_daily_stop`. DevDocs: `## 2026-10-02 — note-daily-stop (check)` in `docs/40 - DevDocs/cobalt/aset/web.md` | `uv run pytest … tests/cobalt/test_aset_web.py` → `2 failed, 59 passed` (only O1, H1 left); after O1/H1 marked `xfail(strict=True, reason="check O1|H1: HELD, NOT FIXED …")`: `… test_aset_web.py test_drc_settings.py test_drc_web_seam.py test_daymode_note.py test_prefill_daily.py test_radar_panel_cards.py` → `177 passed, 13 skipped, 2 xfailed in 2.92s` (skips: `Postgres env settings not available`) | `3d04d48d fix(note-daily-stop): a failed strike leaves the Daily HARD Stop unrewritten and the sheet FAILED (check O4 H3)` |
| O1 · H1 | not fixed (his ruling). The two tests stay in the file, `xfail(strict=True)`: they run red, and pass the suite only while red; the fix that lands turns them XPASS → a strict failure, so the marker must come off with it | — | same commit |

## Suites
RESTARTS (before the suites): `uv run cobalt jobs restarts 5ed7c3fd..HEAD` → same rows as the build's table (`src/cobalt/aset/web.py`, `src/cobalt/prefill/daily.py` → `static import reach com.cobalt.aset,com.cobalt.radar`; tests `no resident`; docs `DOCS`); no `UNCLASSIFIED`; last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.
W on `3d04d48d`:
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3793 passed, 673 skipped, 3 xfailed, 25 warnings in 566.86s (0:09:26)`. That is 3791 plus O4 and H3. The two new xfails are O1 and H1.
- (b) Lock take 16:53 EDT: `ls -la …/*/.env` → `no matches found`; `cp`; `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 16:53 /Users/cobalt/cobalt-wt/note-daily-stop-1001/.env` (one line). `<FP>` (typed as BUILD-HUB gives it) → `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables probed. Every table above 0013 reads `-`. `NOTHING WAS APPLIED`; `code: 3d04d48d (clean)`.
- (c) PASS 1: the pass-1 command byte for byte, nothing added (no with-DB test in this check) → `4392 passed, 7 skipped, 65 deselected, 5 xfailed, 31 warnings in 705.80s (0:11:45)`. The 7 SKIPPED lines are the build's 7: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) FORWARD → 0001 … 0011, 0013 … 0022 applied in order; 8 tables CREATED; `content UNCHANGED on every table`. **dev forward: APPLIED 17:06** EDT. `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2: the pass-2 command byte for byte → `171 passed, 1 deselected, 5 warnings in 220.45s (0:03:40)`.
- (c3r) This check writes no `aset_sizings` row (its tests are offline).
- (f) ROLLBACK `--down-to 0013` → 0022 … 0014 `.rollback.sql`; 8 DROPPED; `content UNCHANGED on every table`. `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>` → **`cobalt_dev: 0013 — F2 = F0`**. `rm …/.env`; `ls …/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found`, 17:10 EDT. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE (`.env` absent) → `146 passed, 1 skipped, 15 warnings in 25.10s`. The skip names `COBALT_TEST_LIVE_DRC`.
- Lines: offline 3793/0 · with-DB 4392 + 171 = 4563/0 · live-note 146/0.

## Scope
PREFLIGHT's path union plus my commits: `src/cobalt/aset/web.py` (D3's files), `tests/cobalt/test_aset_web.py` (D3's tests), `docs/40 - DevDocs/cobalt/aset/web.md` (the DevDocs line). Nothing else.

## Checked against the branch
- (i) `git log --oneline 0b678bd0..HEAD -- . ":(exclude)docs"` → `3d04d48d fix(note-daily-stop): a failed strike leaves the Daily HARD Stop unrewritten and the sheet FAILED (check O4 H3)`, `4b99561c wip(note-daily-stop): check red — O1 O4 H1 H3`. `<tip now>` = `3d04d48d`.
- (ii) `git log --stat --format=%h 0b678bd0..HEAD` → the non-docs paths are `src/cobalt/aset/web.py` (row D3) and `tests/cobalt/test_aset_web.py` (test). No `WIDENED`.
- (iii) Fence: `git log --oneline 5ed7c3fd..HEAD -- src/cobalt/settings` → empty (the stored settings and their code are untouched). `git log --oneline 5ed7c3fd..HEAD -- configs/cobalt/templates` → empty (no other note line, no template marker). The aset-interim-close rows: my diff touches only `_write_daymode_note` and `/attest`.
- (iv) `grep -n -F "def test_o4_a_failed_strike_does_not_leave_a_rewritten_stop_beside_an_unticked_box"` → `1072:` (one line). `grep -n -F "def test_failed_attestation_strike_does_not_rewrite_the_stop"` → `1091:` (one line). Both came in `4b99561c`, below `3d04d48d` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found`; `git status --short --branch` → `## s3/note-daily-stop-1001`.
- (vi) `git log --stat --format=%h 5ed7c3fd..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_aset_web.py` and `tests/cobalt/test_drc_settings.py`, both offline files. No migration and no with-DB test file, so TREE STATE `unchanged` holds.
- (vii) Card RECORDS: the RESTARTS record (`uv run cobalt jobs restarts`) was re-run above. `web.py` and `daily.py` → `com.cobalt.aset`, `com.cobalt.radar`, as the record says. The production-read record names no command on my list; it is not re-read.
- (viii) L32: this report holds only constructed test values (4242, 2121, 4343, 8484) and the card's own quoted record. It holds no new value of his.

COUNTING: findings 7 · dropped 0 · held 4 (O1, O4, H1, H3) · fixed 2 (O4, H3) · held unfixed 2 (O1, H1) · open 5 (O1, H1, O2, O3, H2).

## OPEN
- O1 · H1 — HELD, NOT FIXED (`src/cobalt/prefill/daily.py` `_his_edit`). Before the first attest, a bare `Daily HARD Stop:` line in Cobalt's shape whose values are not today's stored stops is skipped as his edit, and the sheet says "your hand edit stands". What would settle it: his ruling (`## DECISIONS` 1). Then the fix goes in and the `xfail` markers come off (strict: the fix turns them XPASS, which is a failure until they are removed).
- O2 — UNSETTLED. A box he ticks in the note is read back (`aset/web.py:517-519`) without the stop being rewritten. What would settle it: a test that calls `web_module._read_back_note_attestation(cfg, day, None, store)` on a note with a ticked unit, plus his scope word (`## DECISIONS` 2).
- O3 — REJECTED: card D3 names `POST /attest`. `cobalt daymode attest` (`daymode/cli.py:188-196`) does not rewrite the stop. What would settle it: his scope word (`## DECISIONS` 2).
- H2 — REJECTED: card D3 says "the attestation itself still stands". Grok's test asks a failed stop write to leave the box unstruck. What would settle it: house B, or a ruling on the reading of D3 (e).

## CONTINUE
next: none — pass 1 closed. PASS-2 (house B Gemini) is the desk's launch.

## DECISIONS
1. FOR DEJAN — the morning line once the stored stops change (O1, H1, held, not fixed). Before the first attest, the note's line still reads as the 05:15 run wrote it, for example `full $X · half $Y`. If the stored stops change after 05:15 (the change line is how the swapped values get fixed), an attest finds the line no longer matches and treats it as his hand edit. The line is not rewritten, and the sheet says "your hand edit stands". The code cannot tell that case apart from his own in-shape fix, such as swapping the two numbers by hand in the note. Overwriting would lose that fix (L28); keeping it leaves a stale Cobalt line (L3). His choice:
   - (a) A line in Cobalt's exact shape is Cobalt's, so it is rewritten.
   - (b) It is refused loud: FAILED, both texts shown, nothing written.
   - (c) As built: kept, with a truthful banner.

   Safe default taken: nothing changed; the tests are pinned `xfail(strict)`.
2. FOR DEJAN — scope: should the other attestation paths also rewrite the stop (O2, O3)? Those are a box he ticks in the note (read back at `aset/web.py:517-519`) and `cobalt daymode attest` (`daymode/cli.py:188-196`). D3 names only `POST /attest`; `daymode/cli.py` lies outside the rows' files. Safe default taken: only `/attest` rewrites the stop.

## RECORDS
- OpenAI (Sol) METER at PREFLIGHT: `You've hit your usage limit … try again at Oct 4th, 2026 2:06 PM.` House A = Grok, house B = Gemini.
- Grok wrote `house-a.md` itself (2735 bytes, 16:40 EDT); stdout ended with the path.
- Dropped: none. No `REFUSED, not needed`, no `CONTINUED`, no extra lock take (one take, at W).
- The L74 line: see `## L74`.
- I did not open `house-a.md` until `## OWN FINDINGS` was written. The house's completion notice arrived at 16:41 EDT, after that.
- O2's test was repaired once (its setup, not its assertion), then removed; H2's test was removed (REJECTED). Neither is committed.
- `opus-1.md` written in `<S>` for house B.
- files opened: 17 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (THE LOCK, REPORT, PREFLIGHT, E0–W), the build report, `ops/desk/stage-copy.sh`, `areas/cobalt.md` (the two sections), `cto-2026-10-01-words.md` (`## R15`, grep), `src/cobalt/aset/web.py`, `src/cobalt/prefill/daily.py`, `src/cobalt/settings/drc.py`, `src/cobalt/daymode/cli.py`, `src/cobalt/daymode/note.py` (grep), `src/cobalt/vaultwrite/writer.py` (grep), `tests/cobalt/test_aset_web.py`, `tests/cobalt/test_radar_panel_cards.py` (the `_write_daymode_note` sentinel), `docs/40 - DevDocs/cobalt/aset/web.md`, `house-a.md`.
- Check of `note-daily-stop`, pass 1: house A `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: note-daily-stop · pass: 1 · tip: 3d04d48d · house A: Grok FINDINGS: 3 · findings: 7 · dropped: 0 · held: 4 · fixed: 2 · held unfixed: 2 · open: 5 · house B: needed · suites: offline 3793/0 · with-DB 4563/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: NO · decisions: 2 · for Dejan: 2
