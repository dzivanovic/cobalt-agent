# f21-vectors-1013 — CHECK (pass 1)

## §0 Headline
- House A Grok gave 2 findings (`FINDINGS: 2`). House B was not needed. Opus read the build first and wrote 1 finding. Total 3, dropped 0.
- HELD 1, fixed 0: O1. `voice/registry.py` accepts the new `local.embed` route as the voice agent's route. Such an agent file loads clean and fails at every turn. The fix is outside the rows' files, so it goes to the fix round. Its test is committed red (`736beb73`), then marked strict-xfail (`c678dda0`).
- REJECTED 2 (G1, G2): the output matches what Grok claimed, and the card's V4 lines say the build is right.
- Gate at `c678dda0`: offline 8851/0 · with-DB 5750/0 · live-note 147/0 · cobalt_dev 0013, F2 = F0 · .env removed. ready: NO, because 1 held finding is not fixed.

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded as DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · 021100c71ad52d50d90d12460d5a9e0c1394b54f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35 (one row, STANDING `Bash(grok *)`); `grep -n "^| R19 "` → line 37 (one row, STANDING four house strings); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 19 18:21:07 EDT 2026
status · git status --short --branch · 0 · ## ops/f21-vectors-1013
head · git log --oneline -1; git log --stat --format=%h c772a516..HEAD · 0 · (6 lines)
    236fc548 docs(f21-vectors-1013): build report — c772a516
    236fc548
    
     .../reports/f21-vectors-build-2026-10-13.md        | 231 +++++++++++++++++++++
     .../reports/f21-vectors-build-2026-10-13.result    |  15 ++
     2 files changed, 246 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f21-vectors-1013/docs/40 - DevDocs/reports/f21-vectors-build-2026-10-13.md" · 0 · BUILT · job: f21-vectors-1013 · tip: c772a516 | on 9436c975 | migration: 0028, rolled back | offline 8851/0 | with-DB 5750/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 5 of 5 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 325446
report: self-check 2 of 3 (recorded)
range · git log --oneline 9436c975..c772a516 · 0 · (2 lines)
    c772a516 feat(f21-vectors-1013): embeddings kind, local.embed route, 0028 vector column, genesis embed (V1-V5, L1 L3 L10 L32)
    931f9b8f wip(f21-vectors-1013): red
PREFLIGHT OK
```
- Self-check 2 of 3: recorded; goes to the house as a fact.
- Range `git log --stat --format=%h 9436c975..c772a516`: 2 commits; path union = 41 paths of `c772a516` (configs/cobalt/modelaccess.yaml; 9 docs pages under `docs/40 - DevDocs/cobalt/`; ops/desk/gate-lists.md; src/cobalt/db_migrations/{0028_genesis_vectors.sql, 0028_genesis_vectors.rollback.sql, __init__.py}; src/cobalt/genesis/{cli,embed,store}.py; src/cobalt/modelaccess/{__init__,adapters,client,config,models}.py; 19 tests/cobalt files of the tail pins plus test_genesis_db.py) + 4 test files of `931f9b8f` (test_genesis_embed.py, test_genesis_vectors_db.py, test_modelaccess_config.py, test_modelaccess_embed.py).
- `ls <S>` → No such file or directory (fresh).
- House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
- No `HOUSE A:` header line on the card. `HOUSE B: as needed` → house A: Grok · house B: none (not needed).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → 50 per-file lines (each `<bytes> <dest>`, from git, proved against the blob id), last line `STAGED 50 files · 559702 bytes · commits 2` (= PREFLIGHT's 2). Among them: `diff.md` 97343, `rulings.md` 374, `files/469-f21-vectors-card.md` 15711, `files/f21-vectors-build-2026-10-13.md` 31486, and every touched file at `c772a516` under `files/wt/`.
`stage-copy.sh`, each `COPIED`: `files/F21-ADR-FINAL-2026-10-11.md` 30048 · `files/f21-host-probe-r2-2026-10-13.md` 10943 · `files/f21-x8-probe-2026-10-18.md` 3591 · `files/f21-genesis-fr1-build-2026-10-19.md` 21754 · `files/731-f5-card.md` 40101 · `files/wt/src/cobalt/voice/web.py` 15062 · `voice/turn.py` 21265 · `voice/registry.py` 3924 · `voice/agent.py` 8046 · `voice/cli.py` 4976 · `src/cobalt/cli.py` 26377 · `configs/cobalt/jobs.yaml` 25642 · `src/cobalt/db.py` 14043 · `src/cobalt/jobs/restarts.py` 12118 · `src/cobalt/db_migrations/placement.py` 9122.
`<S>/HOUSE-INSTRUCTIONS.md` 17572 bytes (HOUSE TEXT verbatim, the self-check fact, the card's ROWS / NOT IN THIS JOB / CHECK ASKS / RECORDS whole, Files paragraph).
House A start: `date` 18:23:02; gates R17 `:35`, R19 `:37`, `5055151d…` again; `cd <AGY>`; the GROK line; `cd <WT>`; `git status --short --branch` → `## ops/f21-vectors-1013`.

## OWN FINDINGS
Read: the card, the diff `9436c975..c772a516` (`<S>/diff.md`), the touched files at the tip, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK`, last line; `src/cobalt/modelaccess/client.py:38-137`; the `load_routes` readers `src/cobalt/voice/registry.py:85-107`, `voice/turn.py:98-119`, `voice/web.py:165-179`; `tests/cobalt/test_voice_config.py:320-359`.

FINDING O1
ROW: X1 (V1)
CLAIM: `src/cobalt/voice/registry.py:101-102` accepts any registry key as the agent's route, so with `local.embed` now in the registry (`configs/cobalt/modelaccess.yaml:21`) an agent file naming the embeddings route loads clean and fails only at every turn (`client.py:97-98` route_unknown), where before every registry route was a chat route (L1: crash at load).
RUN: TEST — `tests/cobalt/test_voice_config.py`
```python
def test_the_route_must_be_a_chat_route_not_the_embed_route(tmp_path):
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, route="local.embed"))
```
EXPECT: `Failed: DID NOT RAISE <class 'cobalt.voice.registry.AgentConfigError'>`.

Other reads, no finding: X2 — a zero, empty, wrong-length or non-finite vector is refused in `embed_sync` (`client.py` the four `bad_response` checks), again in `GenesisStore.set_embedding` (`store.py` the `GenesisEmbedError` guards, and only after `check_embed_dim`), and the column refuses a wrong length; the CHECK keeps the three columns NULL together. V5 DEGRADED / failed-chunk / re-run paths are as the row states (`genesis/embed.py:61-91` at the tip). X3 is re-derived at `## 6` (RESTARTS).

## Findings
House A Grok finished (notice 18:36:14; `<S>/house-a.md` 1102 bytes, written by Grok, last line `FINDINGS: 2`; stdout recorded the path). House B: none (not needed).
- O1 · Opus · X1 (V1) · `voice/registry.py:101-102` accepts the embeddings route `local.embed` as the voice agent's route; it loads clean and fails at every turn, not at load (L1) · TEST
- G1 · Grok · V4 · `tests/cobalt/test_genesis_db.py` is not among V4's 18 pin files; its `"embedding" not in cols` pin is replaced by a weaker "no column named for a vector" · COMMAND
- G2 · Grok · SCOPE · `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` is in no row's files but the diff touches it · COMMAND

## Dropped
none (both house blocks carry a `RUN:` line with an allowed command; O1 carries a test).

## RUNS
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_voice_config.py::test_the_route_must_be_a_chat_route_not_the_embed_route` · `E       Failed: DID NOT RAISE <class 'cobalt.voice.registry.AgentConfigError'>` · `tests/cobalt/test_voice_config.py:359: Failed` · `1 failed in 0.30s` · HELD, NOT FIXED — src/cobalt/voice/registry.py (no row names it; NOT IN THIS JOB does not fence it either). Committed red `736beb73 wip(f21-vectors-1013): check red — O1`.
- G1 · Grok · `git diff 9436c975..c772a516 -- tests/cobalt/test_genesis_db.py` · shows `-        assert "embedding" not in cols and not [c for c in cols if "vector" in c], "no vector column (chunk 2)"` and `+        assert not [c for c in cols if "vector" in c], "no column named for a vector"` · REJECTED — V4: "The head pins move one place from the tail `0026` … re-found at BASE by `git grep -n -e "0026" tests`": `grep -n -F "0026" tests/cobalt/test_genesis_db.py` → `:3`, `:46`, `:60`, so the file is in the card's re-find set; 0028 makes `embedding` exist by design, and the three new columns are pinned in `test_genesis_vectors_db.py::test_x10_a_wrong_length_vector_is_refused_loud` (build DECISION 3).
- G2 · Grok · `git diff --stat 9436c975..c772a516 -- "docs/40 - DevDocs/cobalt/db_migrations/__init__.md"` · ` docs/40 - DevDocs/cobalt/db_migrations/__init__.md | 3 +++` · `1 file changed, 3 insertions(+)` · REJECTED — V4 files name `src/cobalt/db_migrations/__init__.py`; the touched page is that module's DevDocs page (the one dated DevDocs line per changed module), and `## Checked against the branch` (ii) holds docs paths outside the scope test.

## FIXES
- O1: HELD, NOT FIXED — src/cobalt/voice/registry.py. The fix (refuse an agent route that is not a chat `Route`, e.g. `isinstance(routes[spec.route], Route)`) lies outside every row's files; it goes to the builder's one fix round. The red test is deselected at W (`--deselect`), named there.

## Suites
RESTARTS: `uv run cobalt jobs restarts 9436c975..HEAD` → no `UNCLASSIFIED` row. Code rows are as the build's table, plus `tests/cobalt/test_voice_config.py	M	test/documentation; no resident	-`. Last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`. X3: `com.cobalt.aset` comes from `configs/cobalt/modelaccess.yaml	M	resident reads`, and `com.cobalt.radar` from static import reach. The derived table also adds `com.cobalt.cos` on the five `modelaccess/*` files, which the card header does not name (build DECISION 5). The derived line stands (L42).
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f21-vectors-1013 all --deploy --deploy-gate --deselect tests/cobalt/test_genesis_vectors_db.py --migration` at `c678dda0` (exit 0), verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8851/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5750/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-vectors-1013-all-20261019-183726.log
```
No skip is marked `OUTSIDE the allowed set`. Log `:949` `4782 passed, 873 skipped, 5 xfailed` (the build had 4; +1 is O1's strict xfail) · `:1023` `4069 passed, 1 xfailed` (tests/ops) · `:1262` pass 1 `5510 passed, 8 skipped, 134 deselected, 8 xfailed` · `:2224` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_route_dim_not_column_dim_crashes_before_any_write` · `:2225` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_x10_a_wrong_length_vector_is_refused_loud`. `ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union, 45 paths. The non-docs paths are each in a row's `files`, or are a V4 pin test re-found by `0026` (`test_genesis_db.py`), or `ops/desk/gate-lists.md` (V4). My commits touch only `tests/cobalt/test_voice_config.py`, a test file for held finding O1.

## Checked against the branch
- (i) `git log --oneline c772a516..HEAD -- . ":(exclude)docs"` → `c678dda0 wip(f21-vectors-1013): check — O1 held, not fixed: strict xfail until the fix round` · `736beb73 wip(f21-vectors-1013): check red — O1`. `<tip now>` = `c678dda0`.
- (ii) `git log --stat --format=%h c772a516..HEAD` → `c678dda0` and `736beb73` each touch `tests/cobalt/test_voice_config.py` only. `236fc548` touches the build report and its `.result` (docs). No WIDENED.
- (iii) `git log --oneline 9436c975..HEAD -- configs/cobalt/jobs.yaml` → empty; `-- src/cobalt_agent` → empty.
- (iv) `grep -n -F "def test_the_route_must_be_a_chat_route_not_the_embed_route" tests/cobalt/test_voice_config.py` → `359:` (one line). Red commit `736beb73`; no `fix(` commit, because O1 is held and not fixed.
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/f21-vectors-1013`.
- (vi) `git log --stat --format=%h 9436c975..HEAD -- src/cobalt/db_migrations tests/cobalt` → new `0028_genesis_vectors.sql` and new with-DB `tests/cobalt/test_genesis_vectors_db.py`. `git diff 9436c975..HEAD -- ops/desk/gate-lists.md` → PASS 1 ends `--deselect tests/cobalt/test_genesis_vectors_db.py` and PASS 2 ends `tests/cobalt/test_genesis_vectors_db.py`. V4's `files` names `ops/desk/gate-lists.md`. Gate lists carried.
- (vii) Card RECORDS: R1055 → `authorize.sh` row 88 (quoted under AUTHORIZATION). The `jobs.yaml:86` and RESTARTS records are borne out by the RESTARTS table above.
- (viii) L32: this report holds only constructed values and the card's own config values; no ticker, price or date of his.

## OPEN
- O1 · HELD, NOT FIXED — `src/cobalt/voice/registry.py`. Settles when `load_agent` refuses a non-chat route (e.g. `isinstance(load_routes().routes[spec.route], Route)`). Then `test_voice_config.py::test_the_route_must_be_a_chat_route_not_the_embed_route` passes with its xfail mark removed (strict xfail goes red once the fix lands).
- G1 · REJECTED — V4 re-find line. Settles by a desk SETTLED row confirming that `test_genesis_db.py` sits in V4's `0026` re-find set and that the weaker pin is right at 0028.
- G2 · REJECTED — V4 files plus the DevDocs-line rule. Settles by a desk SETTLED row.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- O1 · HELD, NOT FIXED — `src/cobalt/voice/registry.py`. `load_agent` checks only that `spec.route in routes` (`registry.py:101-102`). Now that `local.embed` is in the registry, a voice agent file naming it loads clean, and every turn then fails `route_unknown` (`client.py:97-98`). L1 wants that crash at load. Proof: `Failed: DID NOT RAISE <class 'cobalt.voice.registry.AgentConfigError'>` (`736beb73`). The fix lies outside every row's files. Default taken: none made here; it goes to the builder's one fix round on this card. That fix round may need a row naming `src/cobalt/voice/registry.py`.
- ASK DESK [19:27]: the O1 test is committed red, so the deploy-gate pass would be red, and `gate.sh --deselect` only moves an id from pass 1 to pass 2 (`gate.sh:641-644`); it does not keep it out of offline. Default taken: `@pytest.mark.xfail(strict=True, reason="check O1 HELD, NOT FIXED …")` in `c678dda0`. The assertion is unchanged; the mark goes red the moment the fix lands, so the fix round must drop it.

## RECORDS
- L74: one system reminder asked for a `Claude-Session:` line in commits. Recorded under `## L74`, not acted on.
- No dropped finding. No house that produced nothing. House B was not seated (`HOUSE B: as needed`).
- Lock: no take by hand; one gate take (`lock: waited 0 min`), released by the gate (`.env: removed`).
- No `REFUSED, not needed` line. No `CONTINUED` line.
- Grok's stdout held prose plus the path. `house-a.md` was written by Grok itself (1102 bytes, closing `FINDINGS: 2`).
- `areas/cobalt.md` (WHAT YOU READ (5)) was not opened in this session. `ops/desk/gate.sh:630-659` was read (outside the list) to learn how `--deselect` is applied.
- files opened: 15 — CHECK-HUB.md · 469-f21-vectors-card.md · BUILD-HUB.md (`## THE LOCK` to `## W`) · `<S>/diff.md` · `src/cobalt/modelaccess/client.py` · `src/cobalt/voice/registry.py` · `src/cobalt/voice/turn.py` · `src/cobalt/voice/web.py` · `tests/cobalt/test_voice_config.py` · f21-vectors-build-2026-10-13.md (`## RESTARTS` to the end) · `ops/desk/gate.sh` · `<S>/house-a.md` · the house-probe output · the Grok stdout · the gate output.
- Check of `f21-vectors-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f21-vectors-1013 · pass: 1 · tip: c678dda0 · house A: Grok FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 3 · house B: none available · suites: offline 8851/0 · with-DB 5750/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 15 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 207262
