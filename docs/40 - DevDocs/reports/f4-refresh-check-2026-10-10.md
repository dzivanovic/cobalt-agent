# f4-refresh-1010 — check report (one pass)

## §0 Headline
Check of F4-1 `prefill refresh`. Houses: Sol (7) and Grok (5); my own read: 4. Findings 16, none dropped; 7 held, of which 5 are fixed in `98174119` (A1 manual tickers, A2 create race, A5 his added field row, A6 dead source under his units, A7 stale DevDocs).
Held, not fixed: O1/A3, the degraded age once his stamp owns the line. Keeping that age needs a store field, so a migration, which is fenced. It goes to the builder's fix round, so `ready: NO`.
Gate on `98174119` green: offline 4244/0, with-DB 5169/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: `com.cobalt.aset com.cobalt.radar`.
X16, X12 and T2b are red at the tip. They stay open, per the desk's R988 direction. Two items are for Dejan: `FAILED` cells in a note refresh creates on a dead source, and the sizing text in that create render.

## L74
A system notice in this session asked for a `Claude-Session:` line on commits. Recorded here once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md"` (after `date` 20:49:13 EDT), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 0 · f2328b1050e8e36db4211539b16a33ac82acb8a8
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R849 row · grep -n "^| R849 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 143:| R849 | 07:13 ET | HIS RULING · APPROVED: option A, S5 pulled forward: build as much as possible this weekend, F4 then F5; he asks the brain for the full not-MVP list. Words: `cto-2026-10-10-words.md` R849. | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R849 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R849 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2ef44c847a7c0c61e1f97f236fa50b9f8e991289
RULING 2026-10-10 R849 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 24:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …/cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …/cto-2026-09-24.md` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | block below |
| range, typed | `git log --stat --format=%h d78c66a2..799b6040` | 0 | 3 commits; path union below |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` (background) | 0 | `sol: UP` · `grok: UP` · `gemini: UP` |

```
clock · date · 0 · Sat Oct 10 20:49:20 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-refresh-1010
head · git log --oneline -1; git log --stat --format=%h 799b6040..HEAD · 0 · (5 lines)
    d896de05 docs(f4-refresh-1010): build report — 799b6040
    d896de05

     .../reports/f4-refresh-build-2026-10-10.md         | 226 +++++++++++++++++++++
     1 file changed, 226 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f4-refresh-1010/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md" · 0 · BUILT · job: f4-refresh-1010 · tip: 799b6040 | on d78c66a2 | migration: none | offline 4243/0 | with-DB 5165/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 15 of 15 | self-check: 3 of 3 | decisions: 11 · for Dejan: 3 · tokens: 536583
range · git log --oneline d78c66a2..799b6040 · 0 · (3 lines)
    799b6040 fix(f4-refresh-1010): one sheet-loader call in daily.py; the two refresh tunables rows join ADDED_KEYS (W reds; C2, S1, E1; L3)
    fea889b5 feat(f4-refresh-1010): prefill refresh — the trading and calendar units all day, ownership on every write attempt, form-B shared gate (C1 C2 M1 W1 O1 O2 S1 D1 G1 E1 U1 K1 DOC; L1 L3 L28 L53)
    e7ba534f wip(f4-refresh-1010): red — F4 refresh tests and the A1 experiments, no src edit
PREFLIGHT OK
```
Path union `d78c66a2..799b6040` (for `## Scope`): `configs/cobalt/jobs.yaml`, `configs/cobalt/prefill.yaml`, `configs/cobalt/smoke/s2.yaml`, `configs/cobalt/taxonomy/tunables.yaml`, `configs/cobalt/templates/daily.md.j2`, `docs/40 - DevDocs/cobalt/daymode/note.md`, `docs/40 - DevDocs/cobalt/prefill/{cli,config,daily,market}.md`, `docs/40 - DevDocs/cobalt/vaultwrite/README.md`, `ops/com.cobalt.prefill-refresh.plist`, `src/cobalt/daymode/note.py`, `src/cobalt/prefill/{cli,config,daily,market}.py`, `src/cobalt/vaultwrite/{merge,writer}.py`, `tests/cobalt/test_finviz_consumers.py`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_prefill_refresh_experiments.py`, `tests/cobalt/test_daymode_note.py`, `tests/cobalt/test_prefill_daily.py`, `tests/cobalt/test_setups_d1.py`, `tests/cobalt/test_setups_registries.py`.
Seats (SEAT ORDER): **house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`)**. HOUSE B is `mandatory — vault notes`; a second house is up, so the rule holds.
Self-check count in the build's last line: `3 of 3`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → `STAGED 30 files · 646603 bytes · commits 3` (= PREFLIGHT's 3; `grep -c "^commit " <S>/diff.md` → `3`). Per-file lines (bytes, dest under `<S>`): `diff.md` 141540 · `files/304-f4-refresh-card.md` 32048 · `files/f4-refresh-build-2026-10-10.md` 38469 · `files/wt/configs/cobalt/jobs.yaml` 21175 · `…/prefill.yaml` 1480 · `…/smoke/s2.yaml` 28111 · `…/taxonomy/tunables.yaml` 37921 · `…/templates/daily.md.j2` 2521 · `files/wt/docs/…/daymode/note.md` 2851 · `…/prefill/cli.md` 1998 · `…/prefill/config.md` 3266 · `…/prefill/daily.md` 10119 · `…/prefill/market.md` 1705 · `…/vaultwrite/README.md` 10200 · `files/wt/ops/com.cobalt.prefill-refresh.plist` 16276 · `files/wt/src/cobalt/daymode/note.py` 10287 · `…/prefill/cli.py` 4143 · `…/prefill/config.py` 8305 · `…/prefill/daily.py` 49634 · `…/prefill/market.py` 3642 · `…/vaultwrite/merge.py` 7352 · `…/vaultwrite/writer.py` 59962 · `files/wt/tests/cobalt/test_daymode_note.py` 10603 · `…/test_finviz_consumers.py` 7998 · `…/test_prefill_daily.py` 18148 · `…/test_prefill_refresh.py` 48269 · `…/test_prefill_refresh_experiments.py` 7277 · `…/test_setups_d1.py` 30081 · `…/test_setups_registries.py` 30496 · `rulings.md` 726.
`stage-copy.sh`, each `COPIED`: `files/F4-FINAL-2026-10-10.md` 78381 · `files/wt/src/cobalt/prefill/rules_gen.py` 6381 · `…/prefill/calendar.py` 3611 · `…/vaultwrite/store.py` 10932 · `…/session/clock.py` 12394 · `…/aset/daily_note.py` 9591 · `…/radar/notes.py` 30852 · `…/strike/detector.py` 15532 · `…/jobs/config.py` 20969 · `…/jobs/wrapper.py` 8047 · `…/jobs/restarts.py` 12098 · `files/wt/tests/cobalt/test_vaultwrite.py` 19952 · `…/test_jobs.py` 36803 · `…/test_jobs_reads.py` 10648 · `files/wt/ops/com.cobalt.prefill-daily.plist` 4199.
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph). `date` 20:52:13; house gates R17, R19 again → one row each; `cd <AGY>`; Sol (house A, writes nothing; its final message → `house-a.md`) and Grok (house B → `house-b.md`) started in two background calls; `cd <WT>`; `git status --short --branch` → `## ops/f4-refresh-1010`; `date` 20:52:26.

## OWN FINDINGS
Written before either house's list was opened. Read: card, CHECK-HUB, BUILD-HUB `## THE LOCK` `## E2` `## RESTARTS` `## W`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), the build report, the src diff `d78c66a2..799b6040`, `merge.py` whole, `writer.py:540-930`, `daily.py` whole, `store.py:85-145`, `test_prefill_refresh.py` whole, `F4-FINAL` grep `FAILED`.

FINDING O1
ROW: D1
CLAIM: When his edit owns the trading stamp line, `_last_success` (`src/cobalt/prefill/daily.py:863-878`) reads only stamp lines of `last_after`/`recent_afters`; his stamp carries no `SPY cobalt` part, so a dead source after a good 07:45 refresh reports the age of the last Cobalt stamp before his edit (05:15), not the last success.
RUN: TEST — `tests/cobalt/test_prefill_refresh.py`, class `TestDegraded`:
```python
    def test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line(self, vault, finviz):
        store = MemoryStore()
        refresh(at(5, 15), store)
        edit(vault, table(vault)[0], "as of 06:00 ET · his own words on the stamp")
        finviz.set(SPY=("501.00", "0.20"))
        assert refresh(at(7, 45), store).exit_code == 0
        assert line_of(vault, "| SPY") == row("SPY", "501.00", "0.20")
        finviz.dead = True
        result = refresh(at(8, 15), store)
        assert "SPY cobalt-degraded (finviz fetch failed; values as of 07:45)" in result.status_line
```
EXPECT: AssertionError — the status line reads `values as of 05:15`.

FINDING O2
ROW: D1 / X5
CLAIM: A note that refresh itself creates on a dead source gets the create render's `FAILED` cells (`daily.py:134-143` via `_ensure_note` `:807-820`), so the trading unit carries the uppercase `FAILED` token D1 forbids, and later dead refreshes keep it (`trading_proposal` keeps the line, `:1024-1026`).
RUN: TEST — `tests/cobalt/test_prefill_refresh.py`, class `TestDegraded`:
```python
    def test_check_o2_a_refresh_created_note_on_a_dead_source_carries_no_failed_token(self, vault, finviz):
        store = MemoryStore()
        finviz.dead = True
        first = refresh(at(5, 45), store)
        assert first.action == "created" and first.exit_code == 1
        assert "FAILED" not in unit_body(vault, "trading", "market_table")
```
EXPECT: AssertionError — `'FAILED' in '… | SPY | FAILED |  | …'`.

FINDING O3
ROW: E1 (X16; X7)
CLAIM: The hand-typed stub table leg is red at the tip: `upsert_unit`'s absent-section arm wraps his table as seed and Cobalt's body replaces it (`src/cobalt/vaultwrite/writer.py:731-748`).
RUN: COMMAND — `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no --runxfail "tests/cobalt/test_prefill_refresh.py::TestCreateStubDryRun::test_x16_a_hand_typed_trading_table_in_a_stub_keeps_its_bytes"` (with-DB, one lock take)
EXPECT: `1 failed` — `assert hand in vault.read_text()`.

FINDING O4
ROW: W1 (X12; X1)
CLAIM: The commit-window race leg is red at the tip: refresh B, inside A's commit window, classes A's fresh rows as his and records an override naming A's values (`daily.py:989-997` rule (b) then freezes them).
RUN: COMMAND — `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no --runxfail "tests/cobalt/test_prefill_refresh.py::TestConcurrency::test_x12_commit_window_race_no_override_names_a_values"` (with-DB, one lock take)
EXPECT: `1 failed` — `an override names A's values`.

## Findings
Both houses finished: Sol at 21:01:28 (`date`; exit 0; its final message written by me to `<S>/house-a.md`, `FINDINGS: 7`), Grok at 21:04:27 (exit 0; wrote `<S>/house-b.md` itself and replied with its path, `FINDINGS: 5`). Every block has a `RUN:` line followed by a `def test_` or an allowed command: nothing dropped.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| A1 | Sol | O1 | Absent-note create ignores `fields: SPY: manual`: create flags hard-coded (`daily.py:710-725`), so SPY is fetched and flagged `cobalt`. | TEST |
| A2 | Sol | E1 | A competing creator between check and create raises `NoteChangedOnDisk` instead of the refresh re-reading the winner (`writer.py:597-640`, `daily.py:1064-1071`). | TEST |
| A3 | Sol | D1 | With his stamp, after ten writes the last-success age is lost: `values as of unknown` (`daily.py:863-878`, `:934-939`). | TEST |
| A4 | Sol | S1 | The create render's daymode stamp reads the wall clock, not the caller's aware `when` (`daily.py:405-436`, `:500-526`). | TEST |
| A5 | Sol | O1 | A human duplicate SPY row survives but the flag says `SPY cobalt` (`daily.py:834-842`, `:993-1029`). | TEST |
| A6 | Sol | D1 | A calendar fetch failure with his calendar unit exits 0, `summary()` `ok` (`daily.py:1106-1108`, `:904-907`). | TEST |
| A7 | Sol | DOC | `prefill/daily.md` still describes three slots, blank VIX/BTC, `SlotAnchorNotFound`, `_fill_rules_slot` as current. | COMMAND |
| B1 | Grok | D1 | An absent-note refresh on a dead source writes `FAILED` into the trading cells and calendar (`daily.py:139`, `:152`, `:819`). | TEST |
| B2 | Grok | O1 | T2b: first refresh after his SPY edit leaves QQQ/IWM at base while the stamp says `cobalt` (strict xfail). | TEST |
| B3 | Grok | W1 | X12: the commit-window race records an override naming A's values (strict xfail). | TEST |
| B4 | Grok | SCOPE | `test_setups_d1.py` and `test_setups_registries.py` are edited and are no row's files. | COMMAND |
| B5 | Grok | E1 | Absent-note refresh writes grade dollars (`half /`) and the daily stop (`full $`) into the note. | TEST |

## Dropped
none

## RUNS
Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <the offline findings>` → `7 failed in 2.00s`. With-DB, ONE lock take (21:07; `lock taken: f4-refresh-1010`; `.env` listed; `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line --runxfail <O3, O4 and the with-DB findings>` → `7 failed in 2.00s`; `<FP>` again identical; `lock released`; `.env` "No such file". Form repairs (no assertion changed): Sol's `self` functions placed in classes `TestCheckFindings` / `TestCheckFindingsDb`.

| id | source | run | output (first failing line) | verdict |
|---|---|---|---|---|
| O1 | own | TEST, offline | `assert 'SPY cobalt-degraded (finviz fetch failed; values as of 07:45)' in 'as of 08:15 ET · SPY cobalt-degraded (finviz fetch failed; values as of 05:15) · …'` | HELD, NOT FIXED — the last success is recorded nowhere while his stamp owns the line; keeping it needs a store field (a migration, fenced) |
| O2 | own | TEST, offline | `AssertionError: assert 'FAILED' not in …` — `| SPY | FAILED |  |` | REJECTED — E1 "the shared create-if-absent render", [F-01] (both entrypoints share creation/rendering) and FINAL `:100` ("05:15 create with a dead source: `FAILED` text, as today"); OPEN, strict xfail |
| O3 | own | COMMAND, with-DB `--runxfail` X16 leg | `assert '| VIX | 17.5 | his |…' in '# 2026-09-03…'` | REJECTED — card E1 "A red here is not fixed (drafter report D4; FINAL X16 stays as it is)"; OPEN (desk R988: the fix round) |
| O4 | own | COMMAND, with-DB `--runxfail` X12 leg | `AssertionError: an override names A's values: [{… 'human_text': '| SPY | $570.00 | +0.10% |…', 'conflict': True …}]` | REJECTED — NOT IN THIS JOB "A per-note lock"; OPEN (desk R988: the fix round) |
| A1 | Sol | TEST, offline | `AssertionError: assert 'cobalt' == 'n/a (manual)'` | HELD — fixed |
| A2 | Sol | TEST, with-DB | `cobalt.vaultwrite.writer.NoteChangedOnDisk: ABORT: … changed on disk between this run's read and its write (sha None -> ac25f72b…)` | HELD — fixed |
| A3 | Sol | TEST, offline | `assert 'SPY cobalt-degraded (finviz fetch failed; values as of 11:15)' in '… values as of unknown) …'` | HELD, NOT FIXED — same cause as O1 |
| A4 | Sol | TEST, offline | `AssertionError: assert '- FAILED: da... to prevent.)' == 'as of 23:30 ET'` — `- FAILED: day mode unresolved (DbConfigError: Missing Postgres settings for the APP credential …)` | UNSETTLED — red for another reason (the day-mode block's own DB read fails before the stamp); runs only with more setup than a form repair; removed again; OPEN |
| A5 | Sol | TEST, with-DB | `AssertionError: assert 'cobalt' == 'human'` | HELD — fixed |
| A6 | Sol | TEST, with-DB | `AssertionError: assert 0 == 1` (`… notes=['market_calendar: his text (the unit is not a Cobalt body) — not written']).exit_code`) | HELD — fixed |
| A7 | Sol | COMMAND (as four `grep -n -F` calls) | `9:existing file's three Cobalt slots independently:` · `15:  never touched by this module at all (always Dejan's, always blank in` · `26:… raises \`SlotAnchorNotFound\` for the WHOLE run` / `61:- \`SlotAnchorNotFound(RuntimeError)\`` / `77:…` · `57:- \`_fill_rules_slot\` / …` | HELD — fixed |
| B1 | Grok | TEST, offline | `AssertionError: assert 'FAILED' not in '---\ntags:…'` — `| SPY | FAILED |  |` | REJECTED — as O2 (same defect); removed again (O2 carries it) |
| B2 | Grok | TEST, with-DB | `AssertionError: assert ('| QQQ | $411.11 | +0.21% |' in [… '| QQQ | $400.00 | +0.20% |' …])` | REJECTED — `cto-2026-10-10.md` R988 (DESK RECORD, DIRECTION: "T2b kept"), the build's strict xfail T2b; OPEN; removed again (duplicate of T2b) |
| B3 | Grok | TEST, with-DB | `AssertionError: an override names A's values: [{… 'human_text': '| SPY | $570.00 | +0.10% |…'}]` | REJECTED — as O4; removed again (duplicate of X12) |
| B4 | Grok | COMMAND | both diffs shown: `+              "prefill.refresh_window", "prefill.refresh_interval_min")` in `test_setups_d1.py` and `test_setups_registries.py` | REJECTED — CHECK-HUB `## 7` (ii) admits a test file; C2 (a) adds the two tunables rows these digest pins name; build DECISION W-1; OPEN |
| B5 | Grok | TEST, offline | `AssertionError: assert 'half /' not in '---\ntags:…'` — `B = $30 half / $30 full, A = $30 half / $30 full. #sizing` | REJECTED — E1 "the shared create-if-absent render" ([F-01]); the dollars are the rules unit's configured text, rendered, not computed; OPEN; removed again |

`wip(f4-refresh-1010): check red — O1 A1 A2 A3 A5 A6 (O2 strict xfail, open)` = `74085dbe` (the held tests, before any fix).

## FIXES
One commit, `98174119` `fix(f4-refresh-1010): manual tickers on create and stub, the create race, his added field row, a dead source under his units exits 1; daily.md current (check A1 A2 A5 A6 A7; O1 A3 strict xfail, held unfixed)`, files `src/cobalt/prefill/daily.py`, `tests/cobalt/test_prefill_refresh.py`, `docs/40 - DevDocs/cobalt/prefill/daily.md`.

| id | fix (`daily.py`) | after |
|---|---|---|
| A1 | `_manual_tickers(cfg)`; `_create_flags(…, cfg)` and `stamp_context(…, cfg)`; `_ensure_note` renders `n/a (manual)` cells and flags for a `manual` ticker; `fresh_trading_body` writes `n/a (manual)` for one | offline `70 passed, 41 skipped, 1 xfailed` (+ O1/A3 then still red, before their xfail marks) |
| A2 | `run_daily_refresh`: `NoteChangedOnDisk` from the create with the note now on disk → note, then the ownership path; absent still → raise | with-DB green |
| A5 | `trading_proposal`: a field row on disk aligned to no `last_after` line flags its field `human` | with-DB green |
| A6 | `_finish`: a market or calendar error with no degraded flag to carry it adds `market source: …` / `calendar source: …` to `degraded` (exit 1) | with-DB green |
| A7 | `docs/…/prefill/daily.md` `## What it does`, `## Key functions`, `## Data flow` describe the four-unit L28 writer; dated line `## 2026-10-10 — f4-refresh-1010 check` | the four greps print nothing but `51: … SlotAnchorNotFound is kept as a type only; it is never raised.` |
| O1, A3 | not fixed: `@pytest.mark.xfail(strict=True, reason="check O1 (HELD, NOT FIXED) …")` / `"check A3 …"` so the gate holds | `XFAIL` both |

The held tests and their neighbours, with-DB, a second lock take (21:10; `.env` listed; `<FP>` before = after = `664 · 35 · 272c95bb…`): `COBALT_ENV=dev uv run pytest -q -rxs -p no:cacheprovider --color=no --tb=short tests/cobalt/test_prefill_refresh.py tests/cobalt/test_prefill_refresh_experiments.py tests/cobalt/test_prefill_daily.py tests/cobalt/test_daymode_note.py tests/cobalt/test_vaultwrite.py tests/cobalt/test_aset_daily_note.py tests/cobalt/test_finviz_consumers.py` → `164 passed, 7 xfailed in 17.81s` (xfails: T2b, X12, X16, O1, O2, A3, the existing finviz gate xfail). `lock released`; `.env` "No such file".

## Suites
RESTARTS first: `uv run cobalt jobs restarts d78c66a2..HEAD` → the build's table plus `tests/cobalt/test_setups_d1.py` / `test_setups_registries.py` (`test/documentation; no resident`), no `UNCLASSIFIED` row, last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1010 all --deploy` on `98174119` (background), exit 0, verdict lines WHOLE:
```
offline 4244/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5169/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1010-all-20261010-211127.log
```
None of the skips is marked `OUTSIDE the allowed set`. `.env`: `ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env` → "No such file or directory" (21:41:41 EDT). Every held finding's kept test passes or is a strict xfail named HELD, NOT FIXED; each was shown red first (`## RUNS`).

## Scope
The build's path union (PREFLIGHT) against the rows' `files`: every `src/`, `configs/`, `ops/` and `docs/` path is a row's file; tests are the rows' tests plus `tests/cobalt/test_setups_d1.py` and `tests/cobalt/test_setups_registries.py` (the tunables digest pins of C2's two rows; B4, REJECTED; build DECISION W-1). My commits: `src/cobalt/prefill/daily.py` (rows O1, D1, E1), `tests/cobalt/test_prefill_refresh.py` (rows' test file), `docs/40 - DevDocs/cobalt/prefill/daily.md` (row DOC). No fenced path.

## Checked against the branch
(i) `git log --oneline 799b6040..HEAD -- . ":(exclude)docs"` → `98174119 fix(f4-refresh-1010): manual tickers on create and stub, the create race, his added field row, a dead source under his units exits 1; daily.md current (check A1 A2 A5 A6 A7; O1 A3 strict xfail, held unfixed)` · `74085dbe wip(f4-refresh-1010): check red — O1 A1 A2 A3 A5 A6 (O2 strict xfail, open)`. `<tip now>` = `98174119`.
(ii) `git log --stat --format=%h 799b6040..HEAD` → `98174119`: `docs/…/prefill/daily.md`, `src/cobalt/prefill/daily.py`, `tests/cobalt/test_prefill_refresh.py`; `74085dbe`: `tests/cobalt/test_prefill_refresh.py`; `d896de05`: the build report. Every non-docs path is a row's file or a test file: no WIDENED.
(iii) `git log --oneline d78c66a2..HEAD -- src/cobalt/strike src/cobalt/radar ops/desk/gate-lists.md configs/cobalt/generated.yaml src/cobalt/prefill/checkpoints.py` → empty.
(iv) `grep -n -F "def <test>" tests/cobalt/test_prefill_refresh.py` → A1 `1093:`, A2 `1146:`, A5 `1173:`, A6 `1186:` (one line each); O1 and A3 sit in the same file as strict xfails. `74085dbe` (check red) sits below `98174119` (fix) in (i). A7 is a COMMAND finding (the greps above).
(v) after the gate, below.
(vi) `git log --stat --format=%h d78c66a2..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file; the with-DB tests added (this build's and mine) need `vault_writes` / `vault_overrides` at `0013` only (card WHY), so no gate-list line is owed.
(vii) Card RECORDS re-run: `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 d78c66a2 -- src configs ops tests` → 14 files, only `ops/desk/*`, `tests/ops/*`, `tests/experiments/*`, `tests/cobalt/test_experiment_conftests.py` (as recorded); `ls` of `prompts/2026-10-04/01-drc-k3-card.md` and `prompts/2026-10-06/72-s4-p1-card.md` → both exist. The LADDER `grep` is over a vault note and the `git -C … show` lines are not on my list: not re-run.
(viii) L32: this report holds constructed values only (test prices, fixture tickers ZZZQ/SPX, constructed dates).
(v) `ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env` → "No such file or directory"; `git status --short --branch` → `## ops/f4-refresh-1010`.

COUNTING: findings 16 (own 4, Sol 7, Grok 5) · dropped 0 · held 7 (O1, A1, A2, A3, A5, A6, A7) · fixed 5 (A1, A2, A5, A6, A7) · held unfixed 2 (O1, A3) · open 11.

## OPEN
- O1, A3 — HELD, NOT FIXED. Settles: a place to keep each field's last-success time while his stamp owns the line (a store column; a migration is fenced).
- O2, B1 — REJECTED (E1 shared render, [F-01], FINAL `:100`). Settles: his word on whether a refresh-created note on a dead source may carry `FAILED` cells; the strict xfail `test_check_o2_…` goes green when it may not.
- O3 (X16), O4 and B3 (X12) — REJECTED (card E1 line; fence "A per-note lock"). Settles: the fix round R988 names (compare-and-swap before the write for X12; X16's stub table), then `--runxfail` on both legs.
- B2 (T2b) — REJECTED (R988 desk direction "T2b kept"). Settles: the per-row ownership follow-up row.
- A4 — UNSETTLED. Settles: the test with the day-mode block's store and config faked, so `build_sheet_mode_block` reaches `render_body`; by reading, `render_body` gets no `when` (`daily.py:434`), so the stamp is the wall clock's.
- B4 — REJECTED (CHECK-HUB `## 7` (ii); C2 (a); W-1). Settles: nothing more; recorded.
- B5 — REJECTED (E1 shared render). Settles: his word on whether a refresh-created note carries the rules unit's dollar text (it is the same render as `prefill daily`).

## CONTINUE
next: done (CLOSE)

## DECISIONS
1. **HELD, NOT FIXED — O1 / A3 (D1): the degraded age when his stamp owns the line.** After his edit of the trading stamp, a later dead source reports `values as of 05:15` (O1) or `unknown` after ten writes (A3), not the last success (`07:45` / `11:15`). `_last_success` (`src/cobalt/prefill/daily.py`) reads only Cobalt stamp lines, and with his stamp no write records a later success. Fixing it needs somewhere to store that time (a store column, so a migration — fenced). Default taken: not fixed; both tests are strict xfails; this goes to the builder's one fix round on card 304 (R438).
2. **FOR DEJAN — O2 / B1: `FAILED` cells in a note that refresh creates on a dead source.** The shared create render writes `| SPY | FAILED |  |` and `- FAILED: …`, and later dead refreshes keep them. That follows E1, [F-01] and FINAL `:100`, but it clashes with D1 ("no uppercase FAILED in the managed text"). Default taken: REJECTED as built; a strict xfail (`test_check_o2_…`) holds the red.
3. **X16 and X12 (O3, O4, B3): fix round.** Both legs are red at the tip when run with `--runxfail`. The card leaves them unfixed (E1 line; the per-note lock is fenced). The desk's R988 direction sends both to the one fix round on this card. Default taken: not fixed here; they stay OPEN.
4. **T2b (B2): kept.** Red for its stated reason. It is REJECTED on R988 ("T2b kept"), which is a DESK RECORD (DIRECTION), not a ruling of his. Default taken: kept as the build's strict xfail. Per-row ownership is a follow-up row.
5. **UNSETTLED — A4 (S1):** the create render's day-mode stamp comes from the wall clock, not the caller's `when`. The test went red for another reason (`DbConfigError` inside the day-mode block). Default taken: test removed; OPEN.
6. **FOR DEJAN — B5 (E1, sizing text):** a note that refresh creates carries the rules unit's dollar text (`B = $… half / $… full`) and the daily stop, the same render as `prefill daily`. Default taken: REJECTED (shared render); OPEN.
7. **B4 (SCOPE):** `test_setups_d1.py` and `test_setups_registries.py` were edited outside the rows' files. These are the tunables digest pins for C2's two rows (build W-1). Default taken: REJECTED; recorded.

## RECORDS
- A cross-session message from `cto-desk` arrived during `## 2` (not a `CONTINUE:`): "brain direction, L79, recorded R988 … A1-3/X16 … and X12 … are to be FIXED in the one fix round on this same card (L75), not left as strict xfail; treat them as the check's findings if they hold (run the xfail tests, L70/K24). T2b … is KEPT as the default; per-row ownership is a follow-up row, a record not a finding." Recorded. Acted on only inside this file's steps: X16 and X12 are run as findings O3/O4 (`--runxfail`); their fixes are not made here (the card fences X16's fix and a per-note lock; CHECK-HUB `## 5` sends a held item outside the rows to the builder's one fix round). T2b is not an own finding; Grok's B2 is judged by its run. `grep -n "^| R988 " …/cto-2026-10-10.md` → `8:| R988 | 21:00 ET | DESK RECORD (brain, L79): … F4 304: X16, X12 fixed in the one fix round (L75), T2b kept; Charter :82-87. | DIRECTION |`.
- Dropped findings: none. Every house produced a list: Sol `FINDINGS: 7`, Grok `FINDINGS: 5`.
- Removed again after their run (not kept in the tree): A4 (UNSETTLED), B1 (duplicate of O2), B2 (duplicate of T2b), B3 (duplicate of X12), B5 (REJECTED).
- Lock takes by hand: two (21:07 runs; 21:10 greens), each with F before = after = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, `lock released`, `.env: removed, proven gone`. The gate took its own.
- A6's fix: a dead or refused source now exits 1 even on a note where every field it serves is his (also a legacy-marker note). This is a behaviour change from the build.
- No `REFUSED, not needed` line; no `CONTINUE:` message.
- The L74 line (above).
- files opened: 21 — CHECK-HUB.md, the card, BUILD-HUB.md (§ THE LOCK–W), the build report, areas/cobalt.md, merge.py, writer.py, daily.py, store.py, test_prefill_refresh.py, test_prefill_daily.py, daily.md.j2, prefill/daily.md, `<S>/rulings.md`, `<S>/house-b.md`, Sol's output, Grok's output, the probe output, the two lock outputs, the gate output.
- **Check of `f4-refresh-1010`: house A `Sol`, house B `Grok`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).**

CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · house A: Sol FINDINGS: 7 · findings: 16 · dropped: 0 · held: 7 · fixed: 5 · held unfixed: 2 · open: 11 · house B: Grok FINDINGS: 5 · suites: offline 4244/0 · with-DB 5169/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185
