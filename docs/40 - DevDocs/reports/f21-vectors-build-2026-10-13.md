# f21-vectors-1013 — build report (2026-10-19)

## §0 Headline
- V1–V5 built at tip `c772a516` on `9436c975`: the `openai_embeddings` route kind, `embed_sync`, `local.embed` (768, 30 s), migration `0028_genesis_vectors`, and `cobalt genesis embed`.
- Gate green: offline 8851/0, with-DB 5750/0 (both V4 tests PASSED in pass 2), live-note 147/0. Migration round trip `F = F0 twice`; `cobalt_dev: 0013 — F2 = F0`; `.env` removed.
- RESTARTS derived: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`. The card's header lists aset and radar only.
- Self-check 2 of 3: V4's two with-DB tests were never red for the row's own reason or under a mutation (E2 runs at 0013 with no forward). 8 decisions, 1 for Dejan (the rollback keeps the `vector` extension).
- F1 fix round (2026-10-19), tip `11eb0d24`: `load_agent` now refuses a non-chat route (O1). The deploy gate is green: offline 8852/0, with-DB 5751/0, live-note 147/0, `F2 = F0`. See `## F1 FIX ROUND`.

## L74
A system block in this session asks commit messages to end with a `Claude-Session:` line (session URL). Recorded once here as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md"` (12:24 ET):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · 133cad2e2708d7a0c733d94cda995963d952473b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/469-f21-vectors-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` (exit 0):
```
clock · date · 0 · Mon Oct 19 12:24:36 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f21-vectors-1013
    ?? "docs/40 - DevDocs/reports/f21-vectors-build-2026-10-13.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 9436c975 docs(desk): F16 seam2 preflight YES, 717 re-point prompt, R2042-R2044
diff · git diff --stat 9436c975 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f21-vectors-1013 · 0 · 9436c975 docs(desk): F16 seam2 preflight YES, 717 re-point prompt, R2042-R2044
env here · ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat 9436c975` · 0 · `docs(desk): F16 seam2 preflight YES, 717 re-point prompt, R2042-R2044` — 3 files under `docs/40 - DevDocs/` (854-draft-717-repoint.md, cto-2026-10-19.md, f16-seam2-preflight-2026-10-19.md), 47 insertions, 4 deletions.

THE CARD'S SYMBOLS (Read tool on each file at BASE, plus greps):
| symbol | where at BASE | matches card |
|---|---|---|
| `class Route` | `config.py:40`; `kind: Literal["openai_compatible"]` `:44`; chat keys `:43-56` | yes |
| loopback validator | `config.py:58-76` | yes |
| `_find_fallback` / fallback refusal | `config.py:94-103`, `:122-127` | yes |
| `ModelResult.kind` | `models.py:68` | yes |
| `_classify` · `OpenAICompatibleAdapter` · `ADAPTERS` | `adapters.py:55`, `:68-121`, `:123` | yes |
| `_record` · `_apply_think_policy` · `call_sync` | `client.py:38`, `:62-77`, `:81` | yes |
| `local.plan` | `modelaccess.yaml:17-42`, source comments `:31-39` | yes |
| `test_committed_registry_loads_with_exactly_the_local_plan_route` | `test_modelaccess_config.py:49-51` | yes |
| `FORWARD` tail / `REVERSE` head | `db_migrations/__init__.py:180` `0026_genesis_chunk.sql`; `:185` `0026_genesis_chunk.rollback.sql` | yes |
| `GenesisStore` · `replace` · `import_paths` | `genesis/store.py:26`, `:37`, `:55` | yes |
| genesis `add_parser` | `grep -n -F "add_parser" src/cobalt/genesis/cli.py` → `22:def add_parser(sub) -> None:` · `25: imp = gsub.add_parser("import", …)` · `28: find = gsub.add_parser("search", …)` | yes |
| gate-lists genesis ids | `ops/desk/gate-lists.md:33` (PASS 1 last two `--deselect`s `test_genesis_db.py`, `test_genesis_experiments_db.py`), `:39` (PASS 2, same two last) | yes |
| `connect_migration` | `src/cobalt/db.py:269-300`, `SET search_path TO public` `:292` | yes |

Callers:
- `grep -rn -F "call_sync(" src` → `src/cobalt/voice/agent.py:167: result = call_sync(req, config=config)` (plus the def `client.py:81` and docstrings `client.py:1,6`).
- `grep -rn -F "GenesisStore(" src` → `src/cobalt/genesis/cli.py:12`, `src/cobalt/genesis/search.py:38`.
- `load_routes` readers (Grep): `voice/web.py:170,176`, `voice/registry.py:99,101`, `voice/turn.py:103,118`, `client.py:83`; `Route(` constructed as a class in `tests/cobalt/test_voice_plan.py:106`, `tests/cobalt/test_modelaccess_client.py:98`.
- `git grep -n -e "0026" tests` → the 18 files of the card plus `test_genesis_db.py:3,46` and `test_genesis_experiments_db.py:9` (docstrings); `test_genesis_db.py:59` asserts `"embedding" not in cols` (see DECISIONS).

`wc -l`: config.py 134 · models.py 103 · adapters.py 125 · client.py 165 · modelaccess/__init__.py 23 · modelaccess.yaml 42 · test_modelaccess_config.py 131 · db_migrations/__init__.py 211 · genesis/store.py 66 · genesis/cli.py 31 · gate-lists.md 57 · test_genesis_db.py 153.

`tail -n 3 "docs/40 - DevDocs/reports/f21-genesis-fr1-build-2026-10-19.md"` → last line: `BUILT · job: f21-genesis-fr1 · tip: 2cd0219a | on 91490502 | migration: 0026, never applied (DECISION 1) | offline 4749/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 (PROOF 42: 38 byte-equal, 4 seam) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 271277`

`uv run cobalt jobs restarts 9436c975..HEAD` → `docs/40 - DevDocs/reports/f21-vectors-build-2026-10-13.md A DOCS -` · `RESTARTS: none` (only this untracked report; no code path).

Card `## RECORDS`, copied: R1055 at `cto-2026-10-11.md:88` — re-read by `authorize.sh` above (row 88, `HIS RULING · APPROVED`). RESTARTS record (`com.cobalt.aset` by `jobs.yaml:86`, `com.cobalt.radar` by import reach) — re-derived at RESTARTS. V3/V4/V5 cells from `f21-host-probe-r2-2026-10-13.md`: re-read by Grep — `X2 model_returned=['text-embedding-nomic-embed-text-v1.5'] dims=[768] zero_vectors=0` (:33), `X8 … dims=[768] vectors_per_call=[32] zero_vectors=0` (:41), `X8 unknown-alias status=200 … ` (:42: an unknown alias answers 200 with this model's vector), X6 `pg_extension: [('plpgsql', '1.0')]` (:91), `vector 0.8.1` available (:101). Round-3 and re-point line numbers: re-proved by the Reads above. The `pg_available_extensions` re-read is the desk's (not re-readable here before W).

PROVEN BY FIRST REAL USE: as the hub's table; `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT (exit 0).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `9436c975` → `4749 passed, 871 skipped, 4 xfailed, 36 warnings in 764.30s (0:12:44)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.42s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Commit `931f9b8f wip(f21-vectors-1013): red` (tests only).

Offline (`uv run pytest -q -rs -p no:cacheprovider --color=no <files>`):
- V2 `tests/cobalt/test_modelaccess_embed.py` → collection error `E ImportError: cannot import name 'embed_sync' from 'cobalt.modelaccess'` (the row's reason).
- V1 / V3, `tests/cobalt/test_modelaccess_config.py`, with V5 and the with-DB file (skipped offline) → `11 failed, 43 passed, 2 skipped`:
  - V3 `::test_committed_registry_loads_with_local_plan_and_local_embed` → `AssertionError: assert ['local.plan'] == ['local.plan', 'local.embed']` (the row's reason).
  - V1 `::test_an_embed_route_loads_without_chat_keys` → `ModelAccessConfigError: … routes.`local.embed`.kind Input should be 'openai_compatible' [type=literal_error …] … no_think Field required … dim Extra inputs are not permitted` (the row's `:44` reason).
  - V1 `::test_an_embed_route_with_a_chat_key_refuses[no_think|think_policy|max_output_tokens|response_format]` → 4 reds, each `assert ('<key>' in '…extra_forbidden')`: the BASE error is the `:44` literal error plus missing chat keys, not the chat key refused as extra.
  - V1 `::test_an_embed_route_with_a_fallback_key_refuses` → PASSED on BASE (the row says green on BASE and after).
  - extra (not named by the card): `::test_every_missing_embed_key_crashes[dim]` red (`assert 'dim' in …`), its other cases green on BASE; `::test_an_embed_route_refuses_a_bad_value` green on BASE (refused for `:44`); both are proven by their E3 mutations.
- V5 `tests/cobalt/test_genesis_embed.py` → `4 failed`; every first line holds `cobalt genesis: error: argument command: invalid choice: 'embed' (choose from import, search)` (the row's reason; the fourth test `::test_an_over_length_chunk_is_not_sent_and_fails_loud` is added by the build to pin the stated length rule).

With-DB, ONE lock take (taken 12:43:17, released 12:43:43):
- `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh f21-vectors-1013 90` → `lock taken: f21-vectors-1013`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's.
- `<FP>` (the hub's text, typed exactly) → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` (= `## LEVEL 0013` of gate-lists.md) · `NOTHING WAS APPLIED`. No forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_genesis_vectors_db.py` → `2 failed in 0.04s`; both `psycopg.errors.UndefinedTable: relation "genesis_chunk" does not exist` (LINE 1: `DELETE FROM genesis_chunk …`).
  The card's named reason (`column embedding does not exist`) needs `genesis_chunk` (0026), which is above 0013; E2 runs no forward, so the red at 0013 is the table's absence. See DECISIONS.
- `<FP>` again → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh f21-vectors-1013` → `lock released`; `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (E2)`.

## E3 THE ROWS
Commit `c772a516 feat(f21-vectors-1013): embeddings kind, local.embed route, 0028 vector column, genesis embed (V1-V5, L1 L3 L10 L32)`.

| row | built | greens (row tests and their neighbours) |
|---|---|---|
| V1 | `config.py`: `EmbedRoute` (`lane`, `kind: openai_embeddings`, `api_base`, `model`, `timeout_s`, `dim > 0`, `key_name`, `extra="forbid"`); `ModelAccessConfig.routes: dict[str, AnyRoute]`, `AnyRoute = Annotated[Union[Route, EmbedRoute], Field(discriminator="kind")]`. The chat class keeps its name `Route` and every key (so `Route(**…)` in `test_voice_plan.py:106`, `test_modelaccess_client.py:98` and the voice callers need no change); its two validators call module functions shared with `EmbedRoute`. Fallback refusal untouched. | `test_modelaccess_config.py` + `test_modelaccess_client.py` + `test_voice_plan.py` → `1 failed, 104 passed, 7 skipped` (the one red: V3's pin, not built yet) |
| V2 | `models.py` `EmbedResult`; `adapters.py` `OpenAIEmbeddingsAdapter.embed()` (`POST {api_base}/embeddings`, `encoding_format="float"`) in `ADAPTERS["openai_embeddings"]`, reusing `_classify`; `client.py` `embed_sync(route, text, *, caller, config=None)`: guard on the input, `_record` (now `getattr` for `usage` / `think_block`), no think policy; `bad_response` for a wrong model, a wrong length, non-finite or all-zero; `call_sync` refuses an embeddings route (`route_unknown`); `__init__.py` exports both | `test_modelaccess_embed.py` + `test_modelaccess_client.py` + `test_modelaccess_silence.py` + `test_voice_plan.py` → `69 passed, 7 skipped` |
| V3 | `modelaccess.yaml` `local.embed` after `local.plan`, each value with its `# source:` line | `test_modelaccess_config.py` + `test_voice_web.py` + `test_voice_turn.py` + `test_voice_lifecycle.py` + `test_voice_plan.py` → `151 passed, 7 skipped` |
| V4 | `0028_genesis_vectors.sql` (`CREATE EXTENSION IF NOT EXISTS vector` first; `embedding vector(768)`, `embed_model TEXT`, `embed_dim INTEGER`, `CHECK genesis_chunk_embedding_stamped`) + rollback (drops CHECK and columns, keeps the extension); `FORWARD`/`REVERSE` registered; `store.py` `GenesisEmbedError`, `column_embed_dim`, `check_embed_dim`, `null_chunks`, `set_embedding`; the 18 pin files moved one place out (`# F21 vectors (0028)`), `test_genesis_db.py:59` (see DECISIONS); `gate-lists.md` PASS 1 `--deselect tests/cobalt/test_genesis_vectors_db.py` (end), PASS 2 the id (end); `placement.py` no line | the 18 pin files + `test_genesis_db.py` → `225 passed, 170 skipped`. Before the pin edits the offline suite showed exactly the card's 18 files red (`27 failed, 4473 passed`: 23 pin tests + V5's 4 unbuilt) |
| V5 | `genesis/embed.py` `run_embed` (preflight → `check_embed_dim` → NULL chunks one per call → summary line; raises on DEGRADED / mismatch / any NULL left), `MAX_CHUNK_CHARS = 2046`; `genesis/cli.py` `embed` verb | `test_genesis_embed.py` + `test_genesis_offline.py` + the two with-DB files (skipped offline) → `23 passed, 6 skipped`; `uv run cobalt genesis embed --help` → `usage: cobalt genesis embed [-h]` |

All row tests at the fix: `test_genesis_embed.py test_genesis_offline.py test_modelaccess_config.py test_modelaccess_embed.py test_modelaccess_client.py` → `111 passed, 2 skipped in 20.60s`. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops` → `4069 passed, 1 xfailed, 16 warnings in 902.88s`.

THE CHUNK LENGTH, stated (V5): the chunker has no maximum (structure only, DECISION D3 of card 468). nomic-embed-text-v1.5's context is 2048 tokens; a WordPiece token covers ≥ 1 character and two special tokens are added, so ≤ 2046 characters always fits. A longer chunk is not sent, stays NULL, is named, and counts toward the non-zero exit.

THE MUTATIONS (Edit, run, undo):
| row | mutation | run | result |
|---|---|---|---|
| V1 | `EmbedRoute.kind` → `Literal["openai_embeddings_mutated"]` | `-k "embed and not committed"` | `10 failed, 7 passed`: first `ModelAccessConfigError … Input tag 'openai_embeddings' found using 'kind' does not match any of the expected tags` (`::test_an_embed_route_loads_without_chat_keys`, the 4 chat-key cases, 5 missing-key cases) |
| V1 | `dim: int = Field()` and the embed loopback validator returns `v` | same | `3 failed, 14 passed`: `::test_an_embed_route_refuses_a_bad_value[over0]`, `[over1]` (dim 0, −768), `[over3]` (10.0.0.5) |
| V1 (negative control) | `EmbedRoute` `extra="ignore"` | `-k chat_key` | `4 failed, 1 passed`: `Failed: DID NOT RAISE <class 'cobalt.modelaccess.config.ModelAccessConfigError'>` (all 4 chat keys) |
| V2 | model check and length check → `if False:` | `test_modelaccess_embed.py` | `3 failed, 9 passed`: `[short]`, `[long]` `DID NOT RAISE`; `::test_a_model_returned_other_than_the_route_model_raises` `DID NOT RAISE` (`[empty]` is still refused by the zero check) |
| V2 | zero check → `if False:`; adapter raises `AdapterFailure("bad_response", …)` instead of `_classify(e)` | same | `6 failed, 6 passed`: `[zero]`, `::test_a_timeout_raises`, the 4 `::test_a_non_2xx_any_body_raises` cases |
| V3 | `dim: 768` → `767` | `-k committed` | `1 failed`: `AssertionError: … At index 4 diff: 767 != 768` |
| V4 | — | — | NOT RUN: both V4 tests are with-DB and need 0026 + 0028 (above 0013); E3 holds no lock and no forward. Their proof is W's PASS 2. See DECISIONS. |
| V5 | preflight failure swallowed (probe with dim 8) | `test_genesis_embed.py` | `1 failed, 3 passed`: `AssertionError: vectors: embedded 2 · failed 0 · over-length 0 · of 2 NULL … assert 0 != 0` |
| V5 | end raise only on over-length; bound `>=` | same | `2 failed, 2 passed`: `::test_a_failed_chunk_leaves_it_null_and_exits_nonzero` `assert 0 != 0`; `::test_an_over_length_chunk_is_not_sent_and_fails_loud` `assert ('over-length 1' in 'over-length: chunk 2 … chunk 3 is 2046 characters …')` |
| V5 | `pending` = every chunk, not `null_chunks()` | `-k rerun` | `1 failed`: `assert ['chunk one',...'chunk three'] == ['chunk two', 'chunk three']` |
After each: undone with Edit; `git diff --stat` back at the fix (shown after V1 and V2; the final row-test run above is at the fix).

## RESTARTS
`uv run cobalt jobs restarts 9436c975..HEAD` (at `c772a516`): no `UNCLASSIFIED` row. Code rows:
```
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/db_migrations/0028_genesis_vectors.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0028_genesis_vectors.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/genesis/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/genesis/embed.py	A	static import reach	com.cobalt.radar
src/cobalt/genesis/store.py	M	static import reach	com.cobalt.radar
src/cobalt/modelaccess/__init__.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/adapters.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/client.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/modelaccess/models.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
(every `docs/` row `DOCS -`, every `tests/` row `test/documentation; no resident -`.) The card's header names `com.cobalt.aset com.cobalt.radar`; the derived table adds `com.cobalt.cos` (see DECISIONS).

## W THE THREE SUITES
`<tip>` = `c772a516`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh f21-vectors-1013 all --deploy --deselect tests/cobalt/test_genesis_vectors_db.py --migration` (exit 0). No `--tickers`: this build's with-DB tests write no `aset_sizings` row. Verdict lines, whole:
```
tests/ops: run (ops/desk/gate-lists.md)
offline 8851/0
lock: waited 27 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-vectors-1013-all-20261019-132001.log
```
None of the skips is marked `OUTSIDE the allowed set`. Each is in `## ALLOWED SKIPS`.
- (a) offline: log `:949` `4782 passed, 873 skipped, 4 xfailed` (tests/cobalt + tests/taxonomy) and `:1023` `4069 passed, 1 xfailed` (tests/ops) → 8851. This build adds the tests in `test_modelaccess_config.py` (V1/V3), `test_modelaccess_embed.py` (V2), `test_genesis_embed.py` (V5) and `test_genesis_vectors_db.py` (V4, with-DB).
- (b) lock taken (log `:1029`), `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1040`), LEVEL 0013.
- (c) pass 1, log `:1097`, the full command: the PASS 1 line of `gate-lists.md` without `--db-only`, ending `… --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_genesis_vectors_db.py`. The id appears twice: once from gate-lists, once from the flag. Result: `:1262` `5510 passed, 8 skipped, 134 deselected, 7 xfailed` → `<d1>` = 5510.
- (c2) `dev forward: APPLIED 14:30:48` (`:1264`); `F1: 929 46 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1346`).
- (c3) pass 2: `:2226` `240 passed, 1 deselected` → `<d2>` = 240. This build's ids: `:2224` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_route_dim_not_column_dim_crashes_before_any_write` and `:2225` `PASSED tests/cobalt/test_genesis_vectors_db.py::test_x10_a_wrong_length_vector_is_refused_loud`. `<d>` = 5510 + 240 = 5750 = `with-DB 5750/0`.
- (c3r) `stray rows: not read (no --tickers given)`.
- (c4) `forward, back, forward, back — F = F0 twice`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2298`) = F0 → `cobalt_dev: 0013 — F2 = F0`. `lock released` (`:2500`). `ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env` → `No such file or directory`.
- (e) live-note: `:2570` `147 passed, 1 skipped`. The one skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`). No skip names `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — **gap for V4.** V1, V2, V3 and V5 hold (reds quoted in E2; mutation reds in E3's table). `::test_an_embed_route_with_a_fallback_key_refuses` is the card's control: green on BASE and green after. The 18 pin files and `test_genesis_db.py` went red at the 0028 registration (`27 failed` run, E3 V4 row) and green after the edit. V4's two with-DB tests went red at E2, but because `relation "genesis_chunk" does not exist`, not because `column embedding does not exist`. Neither ran under a mutation: both need a level above 0013. Their only proof is PASSED in W's pass 2. → DECISION 2.
(2) "Every entry path of each rule pinned by a test." — `call_sync`'s one src caller `voice/agent.py:167` (PREFLIGHT grep): `call_sync` refusing an embeddings route is pinned by `test_modelaccess_embed.py::test_a_chat_route_is_not_an_embed_route_and_the_reverse`, and the chat path is unchanged under `test_voice_plan.py` / `test_modelaccess_client.py` (green). `load_routes` readers `voice/web.py:170`, `voice/turn.py:103`, `voice/registry.py:99`: covered by `test_voice_web.py`, `test_voice_turn.py`, `test_voice_lifecycle.py` on the committed registry (green, E3 V3). `GenesisStore(` callers `genesis/cli.py:12` (import; `embed` is new at cli `_cmd_embed`, pinned by `test_genesis_embed.py` through `cobalt.cli.main`) and `genesis/search.py:38` (unchanged; `test_genesis_db.py` G4 PASSED in pass 2). `embed_sync` has one caller, `genesis/embed.py` (`run_embed`), pinned by `test_genesis_embed.py` (offline) and `test_genesis_vectors_db.py` (with-DB).
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." — re-ran at `c772a516`: `grep -n -F "0028_genesis_vectors" src/cobalt/db_migrations/__init__.py` → `:115`, `:119`, `:193`, `:198`; `grep -n -F "class EmbedRoute" src/cobalt/modelaccess/config.py` → `:99`; `grep -n -F "def embed_sync" src/cobalt/modelaccess/client.py` → `:184`; `grep -n -F "test_genesis_vectors_db.py" ops/desk/gate-lists.md` → `:33` (PASS 1, last) and `:39` (PASS 2, last). Gate log lines are quoted from Grep and Read of the log above.

## FOR THE CHECK
- Range `9436c975..c772a516`: `931f9b8f wip(f21-vectors-1013): red` · `c772a516 feat(f21-vectors-1013): embeddings kind, local.embed route, 0028 vector column, genesis embed (V1-V5, L1 L3 L10 L32)`.
- Per row: reds are in E2, mutation runs and greens in E3.
- Caller greps: in PREFLIGHT.
- RUN rows: none on this card.
- Three suites: in W. The executed pass 1 command is at log `:1097`.
- Lock takes: E2 took the lock 12:43:17 and released it 12:43:43, F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87`. W took it after `lock: waited 27 min` (log `:1029`) and released it at log `:2500`, with F0 `664 35 272c95…`, F1 `929 46 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 = F0.
- RESTARTS table: in `## RESTARTS`.
- Records copied at PREFLIGHT: in `## PREFLIGHT`.
- CHECK ASKS: X1, X2, X3.
  - X1: the chat class `Route` keeps every key and its name. Its two validators now call module functions with the same bodies. The voice callers have no code change and are green.
  - X2: a zero vector, `[]` or a wrong length is refused in three places: `embed_sync` (bad_response), `GenesisStore.set_embedding` (GenesisEmbedError), and the column itself (`expected 768 dimensions`, pinned in `::test_x10_…`). A NULL vector comes only with NULL `embed_model` and `embed_dim` (the CHECK).
  - X3: the derived table is in `## RESTARTS`.

## F1 FIX ROUND (2026-10-19, CONTINUE: F1; the check's one held finding O1)
- Range `c678dda0..11eb0d24`: `11eb0d24 fix(f21-vectors-1013): load_agent refuses a non-chat route; O1 xfail mark dropped (F1, L1 L75)`. `git diff --name-only c678dda0 HEAD` → `src/cobalt/voice/registry.py`, `tests/cobalt/test_voice_config.py` (the two files of F1, X4).
- Symbols re-read before the edit (Read tool at `c678dda0`): `registry.py:85` `def load_agent`, `:99` `from cobalt.modelaccess import load_routes`, `:101` `routes = load_routes().routes`, `:102` `if spec.route not in routes:`; `test_voice_config.py:358` the strict xfail mark, `:359-361` the test. `grep -n -F "class " src/cobalt/modelaccess/config.py` → `43:class Route(BaseModel):`, `99:class EmbedRoute(BaseModel):`.
- (1) `registry.py`: `from cobalt.modelaccess.config import Route` beside the lazy `load_routes` import; after the unchanged `:102` block, `if not isinstance(routes[spec.route], Route): raise AgentConfigError(f"{path}: route {spec.route!r} is not a chat route — the voice agent needs a chat route (kind: openai_compatible), not an embeddings route")`.
- (2) `test_voice_config.py`: the one xfail line removed; the test body is unchanged.
- RED (mark gone, fix not yet in): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_voice_config.py::test_the_route_must_be_a_chat_route_not_the_embed_route` → `E   Failed: DID NOT RAISE <class 'cobalt.voice.registry.AgentConfigError'>` · `1 failed in 0.25s`. This is the row's reason, and the same as `736beb73`.
- GREEN (the row's RUN): `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_voice_config.py tests/cobalt/test_modelaccess_config.py` → `114 passed in 0.51s`. `::test_committed_agent_is_the_v1_allowlist` is among the passes, so the committed agent still loads on `local.plan` (X4).
- No DevDocs line: F1's `files` name only the two files, and X4 asks that they be the only ones changed.
- RESTARTS `uv run cobalt jobs restarts 9436c975..HEAD` → the new row `src/cobalt/voice/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`; last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (unchanged from the first build; no UNCLASSIFIED).

- THE DEPLOY GATE (L75) on `<tip>` = `11eb0d24`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f21-vectors-1013 all --deploy --deselect tests/cobalt/test_genesis_vectors_db.py --migration` (exit 0). Verdict lines, whole:
```
tests/ops: run (ops/desk/gate-lists.md)
offline 8852/0
lock: waited 0 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-vectors-1013-all-20261019-195124.log
```
  No skip is marked `OUTSIDE the allowed set`. Log lines (Grep): offline `:949` `4783 passed, 873 skipped, 4 xfailed` + `:1023` `4069 passed, 1 xfailed` = 8852. That is the first build's 8851 plus the O1 test, which was xfailed before and passes now. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1040`). Pass 1: `:1262` `5511 passed, 8 skipped, 134 deselected, 7 xfailed`. `dev forward: APPLIED 20:34:18` (`:1264`). `F1: 929 46 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1346`). Pass 2: `:2226` `240 passed, 1 deselected`, with `:2224-2225` both `test_genesis_vectors_db.py` ids PASSED. 5511 + 240 = 5751. `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2298`) = F0. Live-note `:2570` `147 passed, 1 skipped`. `ls /Users/cobalt/cobalt-wt/f21-vectors-1013/.env` → `No such file or directory` (20:40).

FIXED: O1 — tests/cobalt/test_voice_config.py::test_the_route_must_be_a_chat_route_not_the_embed_route

## CONTINUE
next: none (BUILT, F1 fix round)

## DECISIONS
- DECISION 1 · ASK DESK [13:00]: migration number. Default taken: the card's. 469 takes `0028_genesis_vectors`; `0027` is left to F5 card 731 (`0027_market_checkpoints`), which deploys first. `FORWARD` here goes `… 0026, 0028`, and `test_archiver_migrations.py` pins `[*range(1, 12), *range(13, 27), 28]`. Whichever card deploys second re-reads `FORWARD`'s tail and moves the pins, as the card states.
- DECISION 2 · self-check gap (V4): the two with-DB tests were red at E2 only because `relation "genesis_chunk" does not exist`. `cobalt_dev` sits at 0013 and E2 runs no forward, so the card's red (`column embedding does not exist`) cannot appear there. The tests had no E3 mutation run either, because that needs a forward outside the gate. Their only proof is `PASSED` in W pass 2 (log `:2224-2225`). Default taken: report the gap; the check (L67) may mutate them under its own lock take.
- DECISION 3: `tests/cobalt/test_genesis_db.py:59` asserted `"embedding" not in cols`, which is true only at 0026 alone. 0028 makes it false by design. The file is in the card's `git grep -n -e "0026" tests` re-find (`:3`, `:46`), so it was edited as a V4 pin. It now asserts only that no column name holds "vector"; the 0028 columns are pinned in `test_genesis_vectors_db.py`. Default taken: edit it (otherwise pass 2 is red).
- DECISION 4 · FOR DEJAN (schema rollback): `0028_genesis_vectors.rollback.sql` drops the CHECK and the three columns but does **not** `DROP EXTENSION vector`. On `cobalt_brain` the old tree's 1536-dim tables use the type, and dropping it would cascade into them. The FINAL says those tables are untouched. So after this gate, `cobalt_dev` keeps `vector` installed in `public`, where before it had `plpgsql` only (X6). The fingerprint (system/user schemas) does not see it: `F2 = F0`. Default taken: the extension stays.
- DECISION 5: RESTARTS derived `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; the card header lists `com.cobalt.aset com.cobalt.radar`. `com.cobalt.cos` comes from `static import reach` on the five `src/cobalt/modelaccess/*` files. Default taken: the derived line (L42), never trimmed.
- DECISION 6 · ASK DESK: `MAX_CHUNK_CHARS = 2046` (`genesis/embed.py`) is a code constant, with its source in the module docstring. The card fixes `EmbedRoute`'s keys, so the bound has no config home without a new key. Default taken: the constant. A config key would be a seam change of the route.
- DECISION 7: `embed_sync` runs the existing secret guard (`refuse_if_secret_shaped`) on the input, as `call_sync` does for every byte that leaves the process. A secret-shaped chunk is therefore `prompt_refused`, left NULL and counted in the non-zero exit. Default taken: guard on (L3 one path); the row did not name it.
- DECISION 8: reading of V1's "`Route` becomes a discriminated union". The union is `AnyRoute` (`ModelAccessConfig.routes`). The chat class keeps the name `Route`, so its keys and every constructor caller (`tests/cobalt/test_voice_plan.py:106`, `tests/cobalt/test_modelaccess_client.py:98`) stay unchanged (X1). Default taken: as built.

## RECORDS
- L74: one system block asked for a `Claude-Session:` line in commits; recorded under `## L74`, not acted on.
- Lock takes: E2 (one, with-DB red) and W (gate). `.env: removed, proven gone (E2)`; `.env: removed, proven gone (W)`.
- No `REFUSED, not needed` and no `CONTINUED` line.
- The card's records, as re-read at PREFLIGHT: R1055 row 88 (authorize.sh); probe r2 X2 `:33`, X8 `:41-42`, X6 `:91`, `:101`.
- Scratch: none in the worktree (`git status` at CLOSE).
- `tokens:` from `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh aa4b75c7` → `context 325446 of 400000 — ok` (above the desk's 250,000 line, read at the last step).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.
- First build's stop line (V1–V5, before the fix round), kept as a record: `BUILT · job: f21-vectors-1013 · tip: c772a516 | on 9436c975 | migration: 0028, rolled back | offline 8851/0 | with-DB 5750/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 5 of 5 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 325446`

- CONTINUED at F1 19:50 (the desk's `CONTINUE: F1`; the fact re-read: `git log --oneline -1` → `c678dda0`, the card's code tip; `.env` absent; `authorize.sh` → `AUTHORIZED` on card commit `0a513165`).
- F1: the system block asking for a `Claude-Session:` line came again this session (L74). Not acted on; `11eb0d24` carries `Co-Authored-By` only.
- F1: G1 and G2 were REJECTED, not held. They get no `FIXED` line, and no SETTLED line is written (card `## CHECK ASKS`). Decisions 1–8 above carry over unchanged; F1 adds none.
- F1 lock take: by the gate (`lock: waited 0 min`), released with `.env: removed`; proven gone 20:40.
- F1 `tokens:` from `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 9145873b` → `context 104885 of 400000 — ok`.

BUILT · job: f21-vectors-1013 · tip: 11eb0d24 | on 9436c975 | migration: 0028, rolled back | offline 8852/0 | with-DB 5751/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 104885
