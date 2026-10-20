# f21-vectors-1013 — check r2 (CHECK-HUB, one pass) — 2026-10-19

## §0 Headline
- Check r2 of `f21-vectors-1013` (tip `11eb0d24`, F1 fix round). House A Grok returned `FINDINGS: 0`; house B was not needed (`as needed`).
- One finding of my own, O1 (V4): `test_genesis_vectors_db.py:72` asserted `"8"`, which is a substring of `"768"`. HELD, and fixed in `c56817ec` (test only).
- Deploy gate on `c56817ec`: offline 8852/0 · with-DB 5751/0 · live-note 147/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`.
- X1–X4 answered (`## Checked against the branch`). There are 5 decisions, and one is FOR DEJAN: the `vector` extension stays on `cobalt_dev` after rollback.

## L74
- A system-reminder in this session asks commits to also carry a `Claude-Session:` line. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · 69687cc2a6241237ba5440d8995b5566290054b5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: R17 · `grep -n "^| R17 " …cto-2026-09-24.md` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row) · R19 · `grep -n "^| R19 " …` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row) · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`date` · 0 · `Mon Oct 19 21:32:35 EDT 2026`
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 19 21:32:40 EDT 2026
status · git status --short --branch · 0 · ## ops/f21-vectors-1013
head · git log --oneline -1; git log --stat --format=%h 11eb0d24..HEAD · 0 · (6 lines)
    42e20201 docs(f21-vectors-1013): build report — 11eb0d24 (F1 fix round)
    42e20201
    
     .../reports/f21-vectors-build-2026-10-13.md        | 50 +++++++++++++++++++++-
     .../reports/f21-vectors-build-2026-10-13.result    | 10 ++---
     2 files changed, 53 insertions(+), 7 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f21-vectors-1013/docs/40 - DevDocs/reports/f21-vectors-build-2026-10-13.md" · 0 · BUILT · job: f21-vectors-1013 · tip: 11eb0d24 | on 9436c975 | migration: 0028, rolled back | offline 8852/0 | with-DB 5751/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 104885
report: self-check 2 of 3 (recorded)
range · git log --oneline 9436c975..11eb0d24 · 0 · (6 lines)
    11eb0d24 fix(f21-vectors-1013): load_agent refuses a non-chat route; O1 xfail mark dropped (F1, L1 L75)
    c678dda0 wip(f21-vectors-1013): check — O1 held, not fixed: strict xfail until the fix round
    736beb73 wip(f21-vectors-1013): check red — O1
    236fc548 docs(f21-vectors-1013): build report — c772a516
    c772a516 feat(f21-vectors-1013): embeddings kind, local.embed route, 0028 vector column, genesis embed (V1-V5, L1 L3 L10 L32)
    931f9b8f wip(f21-vectors-1013): red
PREFLIGHT OK
```
- Self-check `2 of 3` recorded; it goes to the house as a fact.
- THE RANGE typed: `git log --stat --format=%h 9436c975..11eb0d24` · 0 · path union: `configs/cobalt/modelaccess.yaml`; `ops/desk/gate-lists.md`; `src/cobalt/db_migrations/{0028_genesis_vectors.sql,0028_genesis_vectors.rollback.sql,__init__.py}`; `src/cobalt/genesis/{cli.py,embed.py,store.py}`; `src/cobalt/modelaccess/{__init__.py,adapters.py,client.py,config.py,models.py}`; `src/cobalt/voice/registry.py`; tests `test_genesis_embed.py`, `test_genesis_vectors_db.py`, `test_modelaccess_config.py`, `test_modelaccess_embed.py`, `test_voice_config.py`, `test_genesis_db.py` and the 18 tail-pin files (`test_archiver_migrations.py` … `test_voice_store.py`); docs pages under `docs/40 - DevDocs/cobalt/{db_migrations,genesis,modelaccess}/`; the build report and `.result`.
- The card is not "DB: none": no `--name-only` row.
- `ls <S>` · 0 · `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md STAGED-CARD`. `ls -la <S>`: every file is dated `Oct 19 18:21`–`18:36`, before F1 (`11eb0d24`). This folder belongs to the first check of this job (same `<JOB>`, so the same `<S>`). This launch carries no `CONTINUE:` and `CHECK REPORT` (`…check-r2-2026-10-19.md`) did not exist (`ls` exit 1). So this run is a FRESH check, not RECOVERY: it stages over the folder, and house A's list is accepted only with an mtime later than this session's launch (ASK DESK 1).
- House probe (`house-probe.sh --card "<card>"`, background) · exit 0 · `grok: UP` · `gemini: UP`.
- Seats: no `HOUSE A:` header line → `house A: Grok · house B: none (not needed)` (card `HOUSE B: as needed`).
- PROVEN BY FIRST REAL USE: the with-DB strings, at the take inside `gate.sh` (`## 6`), or at a by-hand take for a with-DB finding.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0. Its first line is `cleared: <S> (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-vectors-check-2026-10-13.md)`, so the first check's files, its `house-a.md` among them, were removed (`ls -la <S>` 21:35: no `house-a.md`). It staged `diff.md` (101308), `rulings.md` (374), `STAGED-CARD` (24), `files/469-f21-vectors-card.md` (20063), `files/f21-vectors-build-2026-10-13.md` (37677), and 49 files under `files/wt/` (every path of the diff at `11eb0d24`, each proved against its blob id by the script; per-file byte lines are in the session's tool output). Last line: `STAGED 54 files · 626127 bytes · commits 5`.
- `commits 5` against PREFLIGHT's 6: the diff is `-- . ":(exclude)docs"`. `git log --oneline 9436c975..11eb0d24 -- . ":(exclude)docs"` → 5 commits (`11eb0d24`, `c678dda0`, `736beb73`, `c772a516`, `931f9b8f`). The sixth, `236fc548`, touches only `docs/` (PREFLIGHT range stat), so the diff is complete for its pathspec (ASK DESK 2).
- `stage-copy.sh`, each `COPIED <bytes> <dest>`: `F21-ADR-FINAL-2026-10-11.md` 30048 · `f21-host-probe-r2-2026-10-13.md` 10943 · `f21-x8-probe-2026-10-18.md` 3591 · `f21-genesis-fr1-build-2026-10-19.md` 21754 · `f21-vectors-check-2026-10-13.md` 20034 · `draft-469-fix-round-2026-10-19.md` 1740 · `files/wt/src/cobalt/voice/turn.py` 21265 · `files/wt/src/cobalt/voice/web.py` 15062 (the last two for X1).
- `HOUSE-INSTRUCTIONS.md` (21765 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.

## OWN FINDINGS
Written by 21:38 EDT (`date`), before either house list was opened. Read: the diff `9436c975..11eb0d24` and every `src/` file it touches at the tip; `test_modelaccess_embed.py`, `test_genesis_embed.py`, `test_genesis_vectors_db.py`, the `test_modelaccess_config.py` and `test_genesis_db.py` diffs; the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## F1 FIX ROUND`, `## DECISIONS` and its last line; `cobalt.md` from `## What Cobalt is` and from `## Build rules`; and `voice/turn.py:98-122` for X1.

FINDING O1
ROW: V4
CLAIM: `tests/cobalt/test_genesis_vectors_db.py:72` asserts `"768" in str(e.value) and "8" in str(e.value)`. The substring `"8"` is already inside `"768"`, so the test never shows that the error names the route's `dim` 8. A message naming only the column dimension would pass (HOUSE TEXT (5), an assertion too weak).
RUN: COMMAND `grep -n -F "and \"8\" in str(e.value)" tests/cobalt/test_genesis_vectors_db.py`
EXPECT: one line, `72:    assert "768" in str(e.value) and "8" in str(e.value)`.

What I read and found no finding in, so no RUN block:
- X1: `Route` (`config.py:43-69`) keeps every key, type and `Field` constraint. Its two validators now call module functions with the same bodies (`git diff` of `config.py`). `voice/turn.py:112,118` and `voice/web.py:176` index `routes[...]` only by `load_agent().route`, which F1 now guards (`registry.py:108`).
- X2: `embed_sync` (`client.py:217-225`) refuses another model, a wrong length, a non-finite value and a zero vector. `GenesisStore.set_embedding` (`store.py:103-111`) refuses an unchecked column, a dim or length other than the proven column, zero, non-finite and an empty model. The column type refuses a wrong length, and the CHECK refuses a half-stamped row. `replace` and `import_paths` write no vector column.
- X4: `git show 11eb0d24` touches only `src/cobalt/voice/registry.py` (+6) and `tests/cobalt/test_voice_config.py` (−1, the xfail line). The test body at `:358-360` is unchanged.
- Coverage note, no red: `store.py:105`'s `len(vector) != self._embed_dim` is never reached by `test_x10_…:104-106`, because each `bad` passes `dim=len(bad)` and the `dim` clause trips first. The database type check stands behind it. No defect reaches a write.

## Findings
House A Grok finished at 21:44 (`date` 21:45:03 at the notice). `ls -la <S>` shows `house-a.md` at 12 bytes, `Oct 19 21:44`, written by Grok after this launch. Its whole content is `FINDINGS: 0`. Grok's stdout was progress text, then the path. House B: none (not needed).

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | opus-own | V4 | `test_genesis_vectors_db.py:72` asserts `"8" in str(e.value)`, which `"768"` already satisfies, so the route's `dim` is never pinned | COMMAND |

## Dropped
none (Grok wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `grep -n -F "and \"8\" in str(e.value)" tests/cobalt/test_genesis_vectors_db.py` | `72:    assert "768" in str(e.value) and "8" in str(e.value)` | HELD (the output shown, for the stated reason) |
O1 is a COMMAND finding: no red test exists to commit, so there is no `wip(…): check red` commit. The defect is the test's own assertion, and the code it pins raises the strong message on the tip (`store.py:88`, `f"the route's dim {dim} is not genesis_chunk.embedding's declared dimension {column}: …"`).

## FIXES
- O1: `c56817ec fix(f21-vectors-1013): the V4 dim-mismatch test pins both numbers in place (check O1)`. `tests/cobalt/test_genesis_vectors_db.py:72-73` now asserts `"the route's dim 8 is not" in …` and `"declared dimension 768" in …`, and `docs/40 - DevDocs/cobalt/genesis/store.md` carries one dated line. The test file and its neighbours offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_genesis_vectors_db.py tests/cobalt/test_genesis_embed.py tests/cobalt/test_genesis_db.py` → `4 passed, 6 skipped in 0.53s` (the 6 skips are `Postgres env settings not available`; `0 failed`). The with-DB proof is the gate's pass 2 (`## Suites`). The strengthened assertion was not shown red under a mutation, because that needs a level above 0013 outside the gate (DECISIONS).

## Suites
RESTARTS (before the gate): `uv run cobalt jobs restarts 9436c975..HEAD` at `c56817ec` · 0 · no `UNCLASSIFIED` row, and the new row is `src/cobalt/voice/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`. Last line: `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f21-vectors-1013 all --deploy --deploy-gate --deselect tests/cobalt/test_genesis_vectors_db.py --migration` on `c56817ec` · exit 0 · verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8852/0
lock: waited 14 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5751/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-vectors-1013-all-20261019-214558.log
```
- Log greps: `:1040` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:1095` `pass 1: whole (deploy)` · `:1264` `dev forward: APPLIED 22:42:39` · `:2224` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_route_dim_not_column_dim_crashes_before_any_write` (O1's strengthened test) · `:2225` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_x10_a_wrong_length_vector_is_refused_loud` · `:2298` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0. `grep -n -F "OUTSIDE the allowed set" <log>` → nothing.
- `.env`: `ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env` → `No such file or directory` (22:48).

## Scope
The PREFLIGHT path union (`## PREFLIGHT`) is every file of rows V1–V5 and F1, the 18 tail-pin files plus `test_genesis_db.py`, and docs. `test_genesis_db.py` matches the card's re-find: `git grep -n -e "0026" 9436c975 -- tests/cobalt/test_genesis_db.py` → `:3`, `:46`. My one commit, `c56817ec`, changed `tests/cobalt/test_genesis_vectors_db.py` (a V4 file) and `docs/40 - DevDocs/cobalt/genesis/store.md` (a DevDocs line). Nothing changed outside the rows' files.

## Checked against the branch
(i) `git log --oneline 11eb0d24..HEAD -- . ":(exclude)docs"` → `c56817ec fix(f21-vectors-1013): the V4 dim-mismatch test pins both numbers in place (check O1)`, so `<tip now>` = `c56817ec`.
(ii) `git log --stat --format=%h 11eb0d24..HEAD` → `c56817ec`: `docs/40 - DevDocs/cobalt/genesis/store.md`, `tests/cobalt/test_genesis_vectors_db.py`; `42e20201`: the build report and `.result`. Every non-docs path is a row's test file. No WIDENED.
(iii) The fence: `git log --oneline 9436c975..HEAD -- src/cobalt_agent configs/cobalt/jobs.yaml` → EMPTY. The cloud-lane, fallback and production items have no path. A fallback key is refused by `config.py:166-171`, unchanged.
(iv) O1 is a COMMAND finding, so it has no red commit. `grep -n -F "def test_route_dim_not_column_dim_crashes_before_any_write" tests/cobalt/test_genesis_vectors_db.py` → `56:` (one line). Its fix `c56817ec` is in (i).
(v) `ls <WT>/.env` → No such file. `git status --short --branch` → `## ops/f21-vectors-1013` alone.
(vi) The gate lists: `git log --stat --format=%h 9436c975..HEAD -- src/cobalt/db_migrations tests/cobalt` shows the new migration `0028_genesis_vectors.sql` and the new with-DB file `test_genesis_vectors_db.py` (`931f9b8f`, `c772a516`). `grep -n -F "test_genesis_vectors_db.py" ops/desk/gate-lists.md` → `:33` (PASS 1, the last `--deselect`) and `:39` (PASS 2, the last id). Row V4's `files` names `ops/desk/gate-lists.md`. The gate ran those lines (`:1095`, `:2224-2225`). Carried.
(vii) Card records: `grep -n "^| R1055 " ".../cto-2026-10-11.md"` → `88:| R1055 | 09:04 ET | HIS RULING · APPROVED: … F5, F21, F20, F23 FINALs …`. `git -C /Users/cobalt/cobalt log --oneline -1 -S"| R1055 |" -- …` → `0a1951ef docs(desk): R1055 his approval, deploy card 348, check 324 launched`. The record "the build's `## RESTARTS` is the word": derived again at `c56817ec` as `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`## Suites`).
(viii) L32: this report holds constructed values and repo identifiers only.
CHECK ASKS:
- X1: yes. `Route` is unchanged key for key (`## OWN FINDINGS`). The voice callers have no code change, and the gate's offline 8852/0 includes the voice suites.
- X2: no path found (`## OWN FINDINGS`).
- X3: the derived table adds `com.cobalt.cos` to the card's two, on the five `modelaccess/*` files and `voice/registry.py` (DECISIONS 5).
- X4: yes. `git show 11eb0d24` touches only the two F1 files, and the mark is gone with the body unchanged. The test passes in the gate's offline suite, and `test_committed_agent_is_the_v1_allowlist` stays green (offline 8852/0, 0 failed).
- G1, G2: not opened here (DECISIONS 3).

## OPEN
none (open: 0).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- 1 · ASK DESK 2 [21:34]: `stage-set.sh` printed `commits 5`, and PREFLIGHT's range holds 6. The one missing commit, `236fc548`, is docs-only and sits outside the diff's `:(exclude)docs` pathspec. Default taken: the diff counts as complete, and the check goes on.
- 2 · O1's strengthened assertion was not shown red under a mutation: it is a with-DB test and needs a level above 0013 outside the gate. It PASSED in the gate's pass 2 (`:2224`), and the message it pins is `store.py:88` on the tip. The build's DECISION 2 also stands: V4's two with-DB tests have never been mutated. Default taken: no by-hand forward migration (never more access).
- 3 · G1 and G2 (card `## CHECK ASKS`): ASK DESK, per the drafter report `draft-469-fix-round-2026-10-19.md`. Default taken: not opened, and no SETTLED line written here.
- 4 · FOR DEJAN (schema rollback, carried from the build's DECISION 4): `0028_genesis_vectors.rollback.sql` does not drop `vector`. After this gate, `cobalt_dev` keeps the extension in `public`, where X6 found `plpgsql` only. The fingerprint (system and user schemas) reads F2 = F0 and does not see it. Default taken: as built.
- 5 · RESTARTS: derived as `com.cobalt.aset com.cobalt.cos com.cobalt.radar`, while the card header names `com.cobalt.aset com.cobalt.radar`. Default taken: the derived line (L42).

## RECORDS
- Dropped findings: none. Houses that produced nothing: none. Grok produced `FINDINGS: 0` (a valid list).
- ASK DESK 1 [21:33], settled: `<S>` held the first check's files (dated 18:21–18:36). There was no `CONTINUE:` and no r2 report, so this run is a fresh check. `stage-set.sh` cleared the folder (`cleared: … (prior check …f21-vectors-check-2026-10-13.md)`).
- No `REFUSED, not needed` line and no `CONTINUED` line. No lock take by hand: the only take was inside `gate.sh` (`lock: waited 14 min`). `.env: removed, proven gone (6)`.
- Desk message 22:35 ET (`cto-desk`, a check-in that grants nothing): answered in one line with the step and an ETA.
- L74: one system block asked for a `Claude-Session:` line in commits. Recorded under `## L74`, not acted on: `c56817ec` carries `Co-Authored-By` only.
- files opened: 19 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the build report (`## RESTARTS` to the end); `src/cobalt/modelaccess/config.py`, `client.py`, `adapters.py`; `src/cobalt/genesis/embed.py`, `store.py`, `cli.py`; `0028_genesis_vectors.sql`, `0028_genesis_vectors.rollback.sql`; `tests/cobalt/test_modelaccess_embed.py`, `test_genesis_embed.py`, `test_genesis_vectors_db.py`; `src/cobalt/voice/turn.py` (`:98-122`); `<S>/house-a.md`; `docs/40 - DevDocs/cobalt/genesis/store.md`.
- Check of `f21-vectors-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f21-vectors-1013 · pass: 1 · tip: c56817ec · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8852/0 · with-DB 5751/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 207817
