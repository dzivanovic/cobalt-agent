# f4-refresh-1018 — check report (PORT and CR3, recut of card 304)

## §0 Headline
- The PORT is byte-equal to `edd5c076` in 24 files. `jobs.yaml` and `s2.yaml` carry exactly 304's hunks beside main's (cards 591 and 496). P1 to P4 hold.
- Grok (house A) and I each found the same fault: the build report claimed five strict xfails, but there are four, because X16's leg has been unmarked since `c1a5be02` (R998). It is fixed by a correction line in the build report, `7b291371`.
- One open item, O2: a stale `daily.py:239` citation in the `jobs.yaml` comment. The fence forbids changing it, so it goes to the follow-up list.
- The deploy gate on code tip `51b03e00` is green: offline 8538/0, with-DB 5552/0 and live-note 146/0. cobalt_dev is at 0013 with F2 = F0, and `.env` is removed. ready: YES.

## L74
One block arrived as a system reminder at the start of the run, not in a tool result. It asked that commits end with a `Claude-Session:` line. It is recorded here once and not acted on: CHECK-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 0 · ee844aa4d93016ab612061ebc7938e557a69e8ef
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R849 row · grep -n "^| R849 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 163:| R849 | 07:13 ET | HIS RULING · APPROVED: option A, S5 pulled forward: build as much as possible this weekend, F4 then F5; he asks the brain for the full not-MVP list. Words: `cto-2026-10-10-words.md` R849. | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R849 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R849 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2ef44c847a7c0c61e1f97f236fa50b9f8e991289
RULING 2026-10-10 R849 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 44:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R971 row · grep -n "^| R971 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 42:| R971 | 18:54 ET | HIS RULING · APPROVED: "Yes both" confirms R969 covered F4 FINAL and ops-hand D1-D5; words `cto-2026-10-10-words.md` R971. | APPLIED: R969 row (no new text) |
RULING 2026-10-10 R971 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R971 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · d78c66a274f2cd61cdab224c311024f1080db6a4
RULING 2026-10-10 R971 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 62:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`date` → `Sun Oct 18 07:56:11 EDT 2026`.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:

```
clock · date · 0 · Sun Oct 18 07:56:16 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-refresh-1018
head · git log --oneline -1; git log --stat --format=%h 51b03e00..HEAD · 0 · (6 lines)
    1ac63f5d docs(f4-refresh-1018): build report — 51b03e00
    1ac63f5d
    
     .../reports/f4-refresh-build-2026-10-18.md         | 228 +++++++++++++++++++++
     .../reports/f4-refresh-build-2026-10-18.result     |  15 ++
     2 files changed, 243 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f4-refresh-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f4-refresh-1018/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md" · 0 · BUILT · job: f4-refresh-1018 · tip: 51b03e00 | on 75dcdb5f | migration: none | offline 8538/0 | with-DB 5552/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 (PORT 26 PROOF of 26, CR3) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 317898
range · git log --oneline 75dcdb5f..51b03e00 · 0 · 51b03e00 feat(f4-refresh-1018): port card 304 F4 refresh from edd5c076 onto main (PORT, R1833, L3, L28, L42)
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| THE RANGE | `git log --stat --format=%h 75dcdb5f..51b03e00` | 0 | `51b03e00`, 26 files changed, 2690 insertions(+), 115 deletions(-): configs/cobalt/{jobs.yaml, prefill.yaml, smoke/s2.yaml, taxonomy/tunables.yaml, templates/daily.md.j2}; docs/40 - DevDocs/cobalt/{daymode/note.md, prefill/cli.md, prefill/config.md, prefill/daily.md, prefill/market.md, vaultwrite/README.md}; ops/com.cobalt.prefill-refresh.plist; src/cobalt/{daymode/note.py, prefill/cli.py, prefill/config.py, prefill/daily.py, prefill/market.py, vaultwrite/merge.py, vaultwrite/writer.py}; tests/cobalt/{test_daymode_note.py, test_finviz_consumers.py, test_prefill_daily.py, test_prefill_refresh.py, test_prefill_refresh_experiments.py, test_setups_d1.py, test_setups_registries.py} |
| DB | card carries no `DB: none` line | — | the full gate runs at `## 6` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, no `HOUSE A` header line; card `HOUSE B: as needed` | — | house A: Grok · house B: none (not needed) |
| self-check | build report last line | — | `self-check: 3 of 3` |

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, last line `STAGED 31 files · 646208 bytes · commits 1` (commits 1 = PREFLIGHT's range count). Per-file lines (bytes, dest under `<S>`): `STAGED-CARD` 25 · `diff.md` 152245 · `files/726-f4-304-recut-card.md` 15494 · `files/f4-refresh-build-2026-10-18.md` 27836 · `files/wt/configs/cobalt/jobs.yaml` 22136 · `prefill.yaml` 1480 · `smoke/s2.yaml` 28202 · `taxonomy/tunables.yaml` 37921 · `templates/daily.md.j2` 2521 · `docs/…/daymode/note.md` 2851 · `prefill/cli.md` 1998 · `prefill/config.md` 3266 · `prefill/daily.md` 10831 · `prefill/market.md` 1705 · `vaultwrite/README.md` 10200 · `ops/com.cobalt.prefill-refresh.plist` 16276 · `src/cobalt/daymode/note.py` 10287 · `prefill/cli.py` 4143 · `prefill/config.py` 8305 · `prefill/daily.py` 54690 · `prefill/market.py` 3642 · `vaultwrite/merge.py` 7352 · `vaultwrite/writer.py` 59962 · `tests/cobalt/test_daymode_note.py` 10603 · `test_finviz_consumers.py` 7998 · `test_prefill_daily.py` 18148 · `test_prefill_refresh.py` 56861 · `test_prefill_refresh_experiments.py` 7277 · `test_setups_d1.py` 30081 · `test_setups_registries.py` 30496 · `rulings.md` 1376.
`stage-copy.sh` (the card's `## READ` files): `COPIED 34139 <S>/files/304-f4-refresh-card.md` · `COPIED 78381 <S>/files/F4-FINAL-2026-10-10.md` · `COPIED 33600 <S>/files/f4-refresh-check-2026-10-10.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (14873 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
Launch: `date` → `Sun Oct 18 07:58:05 EDT 2026`; gates R17, R19 re-grepped, one row each; `cd <AGY>`; Grok started (`run_in_background`, timeout 2700000) with the GROK line as written; `cd <WT>`; `git status --short --branch` → `## ops/f4-refresh-1018`. House B: none (not needed, `HOUSE B: as needed`).

## OWN FINDINGS
Read before any house list: the card, the diff `75dcdb5f..51b03e00` (seams in full; `git diff --stat edd5c076 51b03e00 -- configs src tests ops` and `-- "docs/40 - DevDocs/cobalt"` list none of the 24 untouched files, and only `jobs.yaml | 17 +` and `s2.yaml | 3 +-` among the two touched ones, both main's own hunks), `git -C /Users/cobalt/cobalt diff -U0 d78c66a2 75dcdb5f` and `d78c66a2 edd5c076` over the two seam files (304's hunks and the port's are line-for-line the same), the build report whole, `tests/cobalt/test_prefill_refresh.py:960-1169`, `tests/cobalt/test_finviz_consumers.py:60-84`, `configs/cobalt/jobs.yaml:344-379`.

FINDING O1
ROW: PORT (P3)
CLAIM: The build report says "its five strict xfails stand unedited: T2b `:739`, O1 `:1062`, O2/B1 `:1078`, A3 `:1152`, and X16's hand-typed leg" (`docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md:199`), but the file carries four `strict=True` markers (`tests/cobalt/test_prefill_refresh.py:740`, `:1063`, `:1079`, `:1153`); X16's hand-typed leg (`:1008`) has no xfail marker at the ported tip.
RUN: COMMAND `grep -c -F "strict=True" tests/cobalt/test_prefill_refresh.py`
EXPECT: `4` (not 5).

FINDING O2
ROW: PORT (C2 seam)
CLAIM: The ported `daily.md.j2` readers entry still cites `prefill/daily.py:239` / `:238` for the loader (`configs/cobalt/jobs.yaml:349-350`, `:359`), but at the tip the loader sits at `src/cobalt/prefill/daily.py:273-274`, and the `because:` text names only `com.cobalt.prefill-daily` though the readers line now names both one-shots.
RUN: COMMAND `grep -n -F "get_template(\"daily.md.j2\")" src/cobalt/prefill/daily.py`
EXPECT: `274:    template = env.get_template("daily.md.j2")` (not `239:`).

## Findings
Grok finished at 08:09 (`ls -la <S>` at 08:10: `house-a.md` 857 bytes, written by Grok; stdout was only its path). Its list ends `FINDINGS: 1`.

| id | house | row | claim | run |
|---|---|---|---|---|
| H1 | Grok | P3 | Build report `:199` claims five strict xfails incl. X16's hand-typed leg; `test_prefill_refresh.py:1008` has no xfail marker, so four exist | COMMAND |

## Dropped
none (Grok's one block has a `RUN:` line followed by a `grep` command line).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -c -F "strict=True" tests/cobalt/test_prefill_refresh.py` | `4` | HELD — the report's "five" is false. The code is right: `git log --oneline d78c66a2..edd5c076 -- tests/cobalt/test_prefill_refresh.py` → `c1a5be02 wip(f4-refresh-1010): fix round red — X12 X16 unmarked, A4 test, B5 pin (R998)`, and `git diff --stat edd5c076 51b03e00 -- tests/cobalt/test_prefill_refresh.py` → empty. The defect is the build report's claim (CR3's file), and P3's own list carries X16 from before R998 |
| H1 | Grok | `grep -n -B8 "def test_x16_a_hand_typed_trading_table_in_a_stub_keeps_its_bytes" tests/cobalt/test_prefill_refresh.py` | `:1000-1007` = the previous test's body and a blank line, then `1008:    def test_x16_a_hand_typed_trading_table_in_a_stub_keeps_its_bytes(self, vault, finviz, db_store):`; no `@pytest.mark.xfail` | HELD — same cause as O1 |
| O2 | own | `grep -n -F "get_template(\"daily.md.j2\")" src/cobalt/prefill/daily.py` | `274:    template = env.get_template("daily.md.j2")` | REJECTED — card `## NOT IN THIS JOB`: "any change beyond `edd5c076`'s content and the two seams" (the `because:` text at `jobs.yaml:349-350`, `:359` is neither 304's hunk nor main's); OPEN |

No test was written (both held findings are COMMAND findings about a report claim), so no `wip(f4-refresh-1018): check red` commit.

## FIXES
- O1, H1: fixed — `7b291371 fix(f4-refresh-1018): build report P3 line names four strict xfails, X16 hand-typed leg unmarked since c1a5be02 (check O1 H1)`. It adds one correction line to the build report's `## W` (the original line stays), the CR3 row's file. Re-run: `grep -n -F "the file holds FOUR strict xfails" "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md"` → `200:- Check correction (f4-refresh-1018-check, O1 and Grok 1, 2026-10-18): the file holds FOUR strict xfails, not five: …`. No module changed, so no DevDocs module line. It is a docs-only commit, so the code tip stays `51b03e00`.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 75dcdb5f..HEAD` → the same 28 rows as the build's table, plus `docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.result	A	DOCS	-`; no `UNCLASSIFIED`; last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1018 all --deploy --deploy-gate` on HEAD `7b291371` (code tip `51b03e00`), exit 0, output whole:

```
tests/ops: run (deploy gate)
offline 8538/0
lock: waited 21 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5552/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1018-all-20261018-081100.log
```
- Log summaries (`grep -n -F " passed" <log>`): `:921` `4618 passed, 838 skipped, 4 xfailed` (offline) · `:993` `3920 passed, 1 xfailed` (tests/ops) · `:1228` `5347 passed, 7 skipped, 99 deselected, 7 xfailed` (pass 1) · `:2082` `205 passed, 1 deselected` (pass 2) · `:2273` `146 passed, 1 skipped` (live-note).
- `F0` (log `:1010`) `664 35 272c95bbb12241e3611e4b36326ccf87` = `F2` (log `:2150`) `664 35 272c95bbb12241e3611e4b36326ccf87`.
- No skip is marked `OUTSIDE the allowed set`.
- `.env`: `ls /Users/cobalt/cobalt-wt/f4-refresh-1018/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union (26 files, `51b03e00`) = the PORT row's 26 files. My commit `7b291371` touches only `docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md`, the CR3 row's file. Fenced paths: none touched (below).

## Checked against the branch
- (i) `git log --oneline 51b03e00..HEAD -- . ":(exclude)docs"` → empty. I made no code commit, so `<tip now>` = `51b03e00`.
- (ii) `git log --stat --format=%h 51b03e00..HEAD` → `7b291371` (`f4-refresh-build-2026-10-18.md | 1 +`) and `1ac63f5d` (the build report and `.result`). No non-docs path.
- (iii) `git log --oneline 75dcdb5f..HEAD -- src/cobalt/strike src/cobalt/radar src/cobalt/jobs/watchdog.py src/cobalt/smoke/checks.py data/deploy/bootstrap-owed.json src/cobalt/db_migrations tests/cobalt/test_smoke.py` → empty. `git log --oneline 75dcdb5f..HEAD -- "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md" tests/cobalt/test_jobs.py` → empty.
- (iv) Neither held finding is a test (both are COMMAND findings). Their fix is `7b291371`, and its re-run grep is quoted under `## FIXES`.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/f4-refresh-1018`.
- (vi) `git log --stat --format=%h 75dcdb5f..HEAD -- src/cobalt/db_migrations tests/cobalt` → `51b03e00`, 7 test files, no migration file. No with-DB test needs a level above `0013` (the gate ran with no `--deselect` and pass 2 printed `205 passed, 1 deselected`, the standing deselect), so the gate lists are not owed.
- (vii) Card records re-run: `git -C /Users/cobalt/cobalt diff --stat 279c99ce 75dcdb5f -- src configs tests ops pyproject.toml` → empty (as recorded). `git -C /Users/cobalt/cobalt diff main ops/f4-refresh-1010 -- "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` → empty (as recorded). `git -C /Users/cobalt/cobalt diff -U0 d78c66a2 75dcdb5f -- configs/cobalt/jobs.yaml configs/cobalt/smoke/s2.yaml` → main's hunks `@@ -344,0 +345,17 @@` (classify trial/route) and `@@ -636 +636,2 @@` (K18 owed clause), as recorded.
- P1: `git diff --stat edd5c076 51b03e00 -- configs src tests ops` and `-- "docs/40 - DevDocs/cobalt"` list none of the 24 files. Among the two seam files they list only `jobs.yaml | 17 +` and `s2.yaml | 3 +-`, which are main's own hunks. `git diff -U3 75dcdb5f 51b03e00` over the two seam files equals 304's `d78c66a2..edd5c076` hunks line for line.
- P2: `jobs.yaml:214` holds the `com.cobalt.prefill-refresh` row once. `:347` reads `readers: [com.cobalt.prefill-daily, com.cobalt.prefill-refresh]`, `:353` reads `readers: [com.cobalt.prefill-daily]` (drc.md.j2, unchanged), and `:361` and `:371` hold the classify entries. `s2.yaml` K12.3 was inserted once and K18's owed clause stands (diff above).
- P3: `git diff --stat edd5c076 51b03e00 -- tests/cobalt/test_prefill_refresh.py` → empty. The four strict xfails stand; X16's leg has been unmarked since `c1a5be02` (O1/H1).
- P4: `grep -n -F "BOOTSTRAP: deferred com.cobalt.prefill-refresh" <build report>` → `124:BOOTSTRAP: deferred com.cobalt.prefill-refresh` at column 0.
- (viii) L32: this report holds no ticker, price or date of his; the only values quoted are constructed test values.

## OPEN
- O2 (own): REJECTED by the fence. `configs/cobalt/jobs.yaml:349-350` and `:359` cite `prefill/daily.py:239`/`:238`, but the loader is at `:273-274`, and the `because:` text names only `com.cobalt.prefill-daily`. Settled by a later card that may change jobs.yaml beyond 304's hunks: re-cite `daily.py:273-274` and name both one-shots. It is a comment only: `test_jobs_reads.py` passes and RESTARTS derives the readers from the `readers:` line.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- O2 (open, follow-up list; no house B sat because the card is `HOUSE B: as needed`): the stale `daily.py:239`/`:238` citation in the `daily.md.j2` `because:` text, `configs/cobalt/jobs.yaml:349-350`, `:359`. Default taken: not fixed (fence: "any change beyond `edd5c076`'s content and the two seams"); it ships to the follow-up list. It does not touch his notes, money or sizing.

## RECORDS
- Grok produced a list: `house-a.md` (857 bytes, 08:09), `FINDINGS: 1`. It wrote the file itself; stdout was its path plus progress prose.
- House B: none. Gemini was UP at the probe and was not seated (`HOUSE B: as needed`). The stop line writes `none available`, the closest form the line allows.
- Dropped: none. Refused: none. CONTINUED: none. Extra lock takes: none (the gate took the lock once and waited 21 min for another holder).
- The L74 line is under `## L74`. My commit `7b291371` carries only the Co-Authored-By trailer.
- Ordering: `stage-set.sh` ran before the report's first Write, while the house probe was in flight. The probe result was in hand before Grok was started.
- I did not open `areas/cobalt.md` (WHAT YOU READ (5)): the job is a byte-equal port and the card carries the binding rules.
- RESULT FILE: `f4-refresh-check-2026-10-18.result` was written beside this report for the desk to commit with it. This session can commit only inside `<WT>`.
- files opened: 15. They are CHECK-HUB.md, the 726 card, BUILD-HUB.md (`## THE LOCK` to `## W`), the build report, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_prefill_refresh_experiments.py` (grep), `tests/cobalt/test_finviz_consumers.py`, `tests/cobalt/test_jobs.py` (grep), `configs/cobalt/jobs.yaml`, `src/cobalt/prefill/daily.py` (grep), `reports/f4-refresh-check-2026-10-10.md` (grep), `<S>/house-a.md`, and the three task output files (probe, Grok, gate).
- **Check of `f4-refresh-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).**

CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · house A: Grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8538/0 · with-DB 5552/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500
