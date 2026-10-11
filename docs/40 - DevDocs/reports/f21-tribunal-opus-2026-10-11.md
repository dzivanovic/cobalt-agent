BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Sun Oct 11 07:12:29 EDT 2026

## DIGEST FOR THE DESK
TRIBUNAL R1: ADOPT AFTER user-side table, separate embed kind, aset restart coupling, preflight checks folded in
- D1 ADOPT WITH — two chunks: FTS floor, then `local.embed` as its own route KIND (not a disguised chat route).
- D2 ADOPT WITH — table on the `"user"` side, declared in `placement.py`; DDL dimension = config key, checked at load; dimension change = migration.
- D3 ADOPT WITH — preflight measures model listed, dimension, finite non-zero vector, p95; FTS-only if any fails.
- D4 ADOPT
- D5 ADOPT
- T1 ADOPT WITH — inside L5/L21/L23 as ruled: same posture as `local.plan` (loopback, no fallback, no new lane).
- T2 ADOPT WITH — acceptance = verbatim passage(s) with source path:line; X2 settles the ranking.
- T3 ADOPT WITH — the preflight list of D3, recorded in the card report; X3.
- T4 ADOPT WITH — "off the voice path" is not enough (same server): one-shot command, not overlapping voice use; X4 sets it.
- T5 ADOPT WITH — new table; code refuses a new `public` table and new-core roles hold no `public` grant.
- T6 ADOPT WITH — spike changes nothing in the embedder choice; F20 consumes F21's search function; gate not reopened.
- (a) ADOPT WITH — fact base holds; seven misses named (per-turn registry load, committed-registry test, pgvector extension, placement map, heartbeat probe, `[]` return, moved lines).
- (b) ADOPT — arithmetic OK; storage and cost decide nothing.
- (c) ADOPT WITH — L1 failure list with exits; L52/L53 not reached.
- (d) ADOPT WITH — names the route file, table, owner of the one-shot command, and the answer step.
- (e) ADOPT WITH · SELF: yes — two chunks, GUESS 6–10 h each, Opus 5.5 builds, Grok house A, no mandatory house B.
- (f) ADOPT WITH — chunk 2 restarts `com.cobalt.aset` in the same action as the merge; chunk 1 restarts what `cobalt jobs restarts` derives.
EXPERIMENTS: X1 pgvector extension in cobalt_dev · X2 FTS ranking of the question (synthetic + committed ledger) · X3 host embed model (dim, p95, not-loaded) · X4 plan-vs-batch contention · X5 dimension-mismatch insert · X6 aset restart cost.
OWNER: none.
SELF: yes lines: 1 · UNMEASURED: 1.
WITHDRAWN: 2.
ESCALATE: 0.

## Rulings

### D1 — default A staged on C
ADOPT WITH: "F21 ships in two chunks. Chunk 1 (the floor): a new-core memory module with one table carrying a `tsvector` column, an importer and a search command; it meets the acceptance test with no model call. Chunk 2: a `local.embed` route on the existing loopback lane through `cobalt.modelaccess`, declared as its own route KIND (an embeddings kind with its own Route variant, adapter method and result type), never as an `openai_compatible` chat route; no `fallback` key; never a cloud embedder in Phase 1."
SELF: no
- The current schema cannot carry an embed route as-is: `Route` requires `no_think`, `think_policy`, `max_output_tokens`, `response_format` (`config.py:47-55`), the only adapter calls `client.chat.completions.create` (`adapters.py:97`), and `call_sync` applies the think policy and fails `empty` on no text content (`client.py:142`, `:76-77`). An embed reply has no `content`.
- Failing scenario for a disguised route: `local.embed: {kind: openai_compatible, model: <embed model>, think_policy: forbid_nonempty, max_output_tokens: 1, …}` loads, a caller sends text, the adapter posts to `/chat/completions` with an embedding model → `http_status` or `empty` (`client.py:77`), never a vector.
- Price of the separate kind: `config.py` (a discriminated Route on `kind`), `models.py` (an embed request/result; `ModelResult.kind` is `Literal["openai_compatible"]` at `models.py:68`), `adapters.py` (one method), `client.py` (one `embed_sync`), plus tests. All inside chunk 2; one package, one registry (L3, `modelaccess/__init__.py:3-5`).

### D2 — a new table, dimension in config, model on every row
ADOPT WITH: "The F21 table is a new-core table on the `\"user\"` side (L32: the ledger and his vault history are user data), declared in `src/cobalt/db_migrations/placement.py` before it exists, with `user_id NOT NULL` and its FK, created by the module's own migration. The vector column arrives in chunk 2's migration with its dimension written in the DDL; the config key holding the dimension is checked against the column's declared dimension at load and a mismatch crashes (L1, L10). Every row records the embedding model as returned by the server and the dimension. A model swap that keeps the dimension is a re-embed job; a swap that changes it is a migration of this one table. The four 1536-dim tables are untouched."
SELF: no
- `placement.py:9-19`: a table in `user`/`system` not in the map fails the placement test, and "A NEW table landing in `public` fails the suite". The ADR names no side; L32 puts "the Memory folder" and "1 - Trading" on the user side (LAWS:216).
- Scenario: config says 768, migration wrote `vector(1024)`; without the load check the first insert fails mid-import (pgvector behaviour: X5). With the check, the command exits non-zero before any row.
- The ADR's "a model swap … is a job, not a migration" (ADR:50) holds only for an equal dimension; recorded here, not as a wrong fact (behaviour → X5).

### D3 — no model named; preflight proves one; else FTS-only
ADOPT WITH: "The F21 card's chunk-2 preflight, on the loopback lane, records: (1) the model id `/v1/models` lists for the configured alias; (2) one probe embed of a synthetic string returns a vector of exactly the configured dimension, every element finite, norm non-zero; (3) p50/p95 latency over a fixed synthetic batch. Any failure → chunk 2 does not build; F21 lands chunk 1 only and vectors go to a follow-up card on the same feature. Cloud is never the substitute."
SELF: no
- The zero-vector check exists because the old code returned `[0.0] * 1536` on failure (`postgres.py:264`); a server that answers with zeros must fail the preflight, not seed the table.

### D4 — cloud only by a routing-tribunal ruling
ADOPT
SELF: no
- `config.py:71-74` refuses a non-loopback host and names the routing tribunal; `config.py:122-127` refuses any `fallback`. L25 (LAWS:188): "by ruling, not by fallback". Nothing to add.

### D5 — do not port the old `OPENAI_API_KEY` path
ADOPT
SELF: no
- The old path's three silent outcomes — `None` (`postgres.py:259`), zero vector (`:264`), empty list (`:775`) — each break L1. KEEP-CONCEPT/REBUILD (`memory-system.md:8`). The old tree stays runnable (strangler rule); nothing is deleted.

### T1 — does a loopback-only `local.embed` touch the freeze
ADOPT WITH: "A loopback-only `local.embed` route is inside L5, L21 and L23 as ruled: it is a call through the routing layer (L5), local-first (L21, L23), adds no lane, no fallback and no metered kind, and holds the same posture `local.plan` holds today (`config.py:7-13`). The schema change is confined to `cobalt.modelaccess`, which the routing build later extends (`modelaccess.yaml:12-13`); it unfreezes nothing. F21 is therefore not C-only on freeze grounds."
SELF: no
- L5 (LAWS:120) names out-of-band embeddings as the defect; routing through `modelaccess` is the cure, not a bypass. L25's fallback chain is the frozen part, and `local.plan` already runs with none by the same docstring (`config.py:9-11`).
- I do not unfreeze anything; this is a reading of the ruled text.

### T2 — is FTS alone enough for the acceptance test
ADOPT WITH: "F21 passes its acceptance test when `cobalt memory search \"why is the stop buffer 0.02\"` (on the imported record) prints, among its top-k results, the passage that states the reason, verbatim, with its source path and line (L57; CLAUDE.md: extracted figures require verbatim source quotes). The value of k and the query form (`websearch_to_tsquery`/`plainto_tsquery`, the text-search config) are set from X2, never guessed."
SELF: no
- The question asks WHY; a hit that carries only "0.02" answers WHAT. Whether the ledger lines the ADR cites carry the reason is not readable by this seat (L32: the ledger text is not opened) → X2.
- The ADR leaves "answers" undefined; a composed model answer is not needed for the floor and would add a model call to chunk 1.
- Chunk boundaries can split "stop buffer" from "0.02": X2 measures it.

### T3 — host embed model: dimension, throughput, p95
ADOPT WITH: "The card's preflight measures exactly the three records of D3 and the behaviour of the server when the model is not loaded (refusal, error code, or a load on demand and its time). A not-loaded model must surface as one typed `ModelCallError` (`unreachable`, `http_status` or `timeout`), never a hang and never a partial batch committed as complete. The embed route's `timeout_s` is set from the measured p95 with the same written-source comment `local.plan` carries (`modelaccess.yaml:31-34`)."
SELF: no
- No measurement exists (ADR:45); `jobs.yaml:106-107` confirms LM Studio's config is outside the repo → X3.

### T4 — contention with `local.plan`
ADOPT WITH: "The genesis embed is a one-shot operator command, never a resident and never a timer in F21. It runs only when no voice turn is expected; whether it may overlap a voice turn at all, and its batch size and per-request timeout, are set from X4. Every batch is committed per chunk with its model and dimension, so an interrupted run resumes from the first chunk without a vector, and the command exits non-zero on the first failed batch."
SELF: no
- A separate process does not separate the server: both routes hit `127.0.0.1:1234` (`modelaccess.yaml:22`). X-E4 already showed chat calls queued 60–72 s behind a second client (`modelaccess.yaml:31-33`).
- Scenario: batch embed of ~760 chunks running when he speaks a voice turn; the Plan call queues behind it past `timeout_s: 15` (`modelaccess.yaml:34`) → `timeout`, the turn fails loud. Whether LM Studio queues embed and chat on one model slot or serves them in parallel is behaviour → X4.

### T5 — new table versus `public.memory_logs`
ADOPT WITH: "New table, as D2 words it. Reusing `public.memory_logs` is refused by the code: `public` is frozen and a new-core table landing there fails the suite (`placement.py:17-19`), `memory_logs` is on the old-tree list (`placement.py:161-162`), and the new-core roles hold no grant on `public.*` (`memory-history-2026-09-20.md:240`, U1). The F21 table is owned through the `\"user\"` schema, where `cobalt_user` holds USAGE, CREATE and ALL by default privileges (`0001_schemas.sql:119-121`, `:157`)."
SELF: no
- Scenario: a store running as `cobalt_user` issues `SELECT … FROM public.memory_logs` → permission denied (U1 observed it for both roles).

### T6 — does the SDK spike change anything
ADOPT WITH: "The spike changes nothing in the embedder decision. F20 (the chief of staff) consumes recall through F21's search function or command, never a second index (L3). F21's chunk 1 has no code dependency on the SDK chassis; the existing gate that no F20/F21 build starts before the spike's report stands as ruled (`s5-weekend-and-parked-answer-2026-10-10.md:21`) and this tribunal does not reopen it."
SELF: no
- L22 puts "memory machinery" on the fast wire and agents-with-tools on the chassis (LAWS:178): the chassis is a caller of recall, not its owner.

### (a) — the fact base
ADOPT WITH (add to `## Context`): "Also: (1) every voice Plan call re-reads the registry from disk (`client.py:83`, `agent.py:167`, `turn.py:294`), so any `modelaccess.yaml` change reaches the running sheet's voice path at once; (2) `tests/cobalt/test_modelaccess_config.py:49` asserts the committed registry holds exactly `local.plan`, and `:104` that V1 accepts one kind — chunk 2 edits both; (3) no new-core migration creates the `vector` extension (only the old tree does, `postgres.py:166`, `:715`, `schema.sql:7`); (4) every new table must be declared in `db_migrations/placement.py`; (5) the heartbeat probes the same port (`heartbeat/probes.py:252`); (6) the old `_generate_embedding` also returns `[]` on failure (`postgres.py:773-775`); (7) the ladder's F21 row is now at `SPRINT-LADDER-v0_1.md:965`."
SELF: no
- HOLDS (opened): `config.py:43-44`, `:48`, `:55`, `:73-74`, `:125-126`; `modelaccess.yaml:12-13`, `:18-22`, `:31-33`, `:34`; `postgres.py:196`, `:243`, `:259`, `:264`, `:725`, `:747`, `:754`, `:759`, `:762`; `schema.sql:87`, `:187`; `jobs.yaml:106-107`; `TRIAGE.md:43`; `memory-history:200`, `:201`, `:224`; `README.md:9-11` (text at :11); Charter `:200-203`; `memory-system.md:8`; LAWS lines cited.
- MOVED (text holds, number not): LADDER:935 → :965; LADDER:925-928 (F20) → :964.
- CANNOT SETTLE from reads allowed to me: `PROJECT-LEDGER.md:326/:370/:1791` text (L32; size now 528,184 B by `wc -c`, ADR said 515,281 — a live file).
- Greps agree: `src/cobalt` has no embed/pgvector code beyond `smoke/checks.py:253`; `modelaccess.yaml` is the only registry; no `tsvector`/`to_tsquery` anywhere in `src`/`configs`.

### (b) — cost and storage
ADOPT
SELF: no
- Corpus: 515,281 B + 984 KiB × 1,024 = 1,007,616 B → 1,522,897 B ≈ 1.5 MB. (`du -sk` counts disk blocks, so text is ≤ that.)
- Chunks: 1,522,897 ÷ 2,000 ≈ 761 (ADR "~750"). Row: 4·1536+8 = 6,152 B; 4·768+8 = 3,080 B. 761 × 6,152 = 4,681,672 B ≈ 4.7 MB; 750 × 6,152 = 4,614,000 ✓; 750 × 3,080 = 2,310,000 ✓. Tokens: 1,522,897 ÷ 4 ≈ 380,700 (ADR 375k) ✓. ARITHMETIC OK.
- "Vault history" size is UNKNOWN; even ×100 it is ~470 MB of vectors at 1536 — UNVERIFIED (measure `du` of the import set). Neither storage nor cost decides: B is blocked by law and code before price matters. Settling measurements: X3 (throughput), the cloud price only if a routing ruling ever adds a lane.

### (c) — the laws
ADOPT WITH: "L1 — each failure is loud and named: route missing → `route_unknown`; server down → `unreachable`; model not loaded → the typed error X3 records; slow → `timeout`; wrong length or non-finite or all-zero vector → `bad_response`; dimension ≠ the column → the load check crashes before any write; FTS import of an unreadable file → the command exits non-zero naming the file. The new code never returns `None`, `[]` or a zero vector (unlike `postgres.py:259`, `:264`, `:775`). L5/L21–L25 — inside as ruled (T1). L41 — A needs no secret (`key_name: null`); B would need a metered key held by the process in VaultManager (`config.py:12-13`), which is why B waits on the routing tribunal. L10 — config keys: the route fields, the embed dimension, batch size, chunk size, text-search config, top-k — each set from X2–X4 with its source comment. L52 — F21's recall ranks text passages to answer questions; it reaches no card, score or rank of trades; a later design that feeds recall into a grade is L52's. L53 — F21 has no cadence and no request ceiling (one-shot command); nothing is his under L53."
SELF: no
- Existing kinds cover the failures; no new error kind is needed (`models.py:15-26`: "A new kind is a seam change").

### (d) — the seam (L72)
ADOPT WITH: "Named seams: the route lives in `configs/cobalt/modelaccess.yaml` (the one registry); the table is `\"user\".<name the card fixes>` declared in `placement.py`; the search function and its CLI are F21-owned and are the only recall entry for F20, the dream job (R4, Charter:398) and the observation store (O3); the one-shot embed command is owned by F21's builder until a dream job design takes it over by its own card. The voice path is a neighbour, not a consumer: it shares the registry file and the server, so chunk 2 lands with the restart of (f) and the contention rule of T4."
SELF: no
- None of F20, dream or O3 exists in code (greps); each gets an F21-owned function to call, not a line to edit.

### (e) — chunks and seats
ADOPT WITH: "Two chunks. Chunk 1: table + migration + placement entry + importer + search CLI + tests (GUESS 6–10 h). Chunk 2: the embeddings kind in `cobalt.modelaccess`, `local.embed` route, vector-column migration, one-shot embed command, preflight + tests (GUESS 6–10 h). Builder: Opus 5.5 (L29, R919: every merged build stays Opus 5.5 until his word). Check: the fresh Opus session plus house A = Grok (R921); F21 writes none of his vault notes and touches no sizing, so no mandatory house B; Gemini sits only if Grok fails. Tests needing `cobalt_dev` (one lock, L76): the migration/placement tests, the FTS import-and-rank test, the vector insert/dimension test; the modelaccess tests run offline against a fake server."
SELF: yes
EVIDENCE: UNMEASURED — RULED L67 (LAWS:348, R919: "Every merged build stays Opus 5.5 (L29) until his word")
- The hours are guesses, marked so. No measurement in the files compares houses on this card's band; the model bake-off FINAL was set aside (LAWS:352).

### (f) — restarts (L42)
ADOPT WITH: "Chunk 2 changes `configs/cobalt/modelaccess.yaml` (in `com.cobalt.aset`'s `reads:`, `jobs.yaml:86`) and `src/cobalt/modelaccess/*` (imported by the sheet through voice, `voice/agent.py:27-29`): `com.cobalt.aset` restarts in the same action as the merge, with the resident down before the merge (L66). Chunk 1 restarts whatever `cobalt jobs restarts <range>` derives (none if no resident imports the new module). The embed command is one-shot and restarts nothing. Each deploy card carries `RESTARTS:` from that command."
SELF: no
- Failing scenario if the restart is not coupled: the merge lands a registry with `kind: <embeddings>`; the running sheet's in-memory `Route` still accepts only `openai_compatible` (`config.py:44`); the next voice turn's `call_sync` re-reads the file (`client.py:83`) → `ModelAccessConfigError` (`config.py:130-131`) → every voice turn fails until restart.
- Cost to him: the sheet he trades beside is down for the restart's duration — UNVERIFIED, X6. L43 permits any hour; the cost argues for a time he is not trading, which is the deploy's choice, not a rule here.

## Self-attack
Writers and readers found (grep, real files):
- `modelaccess`: package `src/cobalt/modelaccess/{__init__,client,config,models,adapters,guard}.py`; readers `voice/turn.py:103,118`, `voice/web.py:170,176`, `voice/registry.py:99-101`, `voice/agent.py:27-29,167`, `voice/config.py:57,112`; config `voice.yaml:41-42`, `agents/voice.yaml:3,26`, `jobs.yaml:86`; tests `test_modelaccess_config.py`, `test_modelaccess_client.py`, `test_modelaccess_silence.py`, `test_voice_plan.py`, `test_voice_turn.py`, `test_voice_lifecycle.py:184`, `test_voice_config.py`.
- `local.plan`: `modelaccess.yaml:18`, `voice.yaml:42`, `agents/voice.yaml:26`, tests above. `local.embed`: no committed file carries it.
- `lane`/`kind`: `config.py:43-44`, `models.py:67-68`, `client.py:48,131,147`, `adapters.py:71,123`, `modelaccess.yaml:19-20`; no other config sets `lane:`.
- `fallback`: `config.py:9-11,94-127`, `__init__.py:4`, `modelaccess.yaml:10-11`, test `:89-97`.
- `think_policy` / `max_output_tokens` / `response_format`: `modelaccess/{client,models,adapters,config}.py`, `voice/agent.py:79`, `modelaccess.yaml`.
- `127.0.0.1:1234`: `modelaccess.yaml:22` only as one string; `heartbeat/probes.py:252` holds host and port separately.
- `embedding` / `embed` / `pgvector` in `src/cobalt`: none (one false hit `smoke/checks.py:253`). `pgvector` elsewhere: `src/cobalt_agent/memory/postgres.py`, `src/cobalt_agent/skills/research/finviz_extractor.py`, `docker-compose.yml:4` (image `pgvector/pgvector:pg16`).
- `text-embedding-3-small`: `postgres.py:243,762`. `OPENAI_API_KEY`: `postgres.py:747,754`, `configs/config.yaml:35` (old loader key name), `configs/cobalt/redact.yaml:122` (a redaction pattern comment).
- `vector(1536)` / `VECTOR(1536)`: `postgres.py:196,725`, `schema.sql:87,187` — four, as the ADR says.
- `memory_logs`: `src/cobalt/db_migrations/placement.py:162` (old-tree list), `src/cobalt_agent/memory/postgres.py`, `tests/cobalt/test_env.py`.
- `tsvector` / `to_tsquery` / `websearch_to_tsquery` / `plainto_tsquery`: none in `src` or `configs`.
- `cobalt_brain`: the search was REFUSED by the bare guard (route: production) twice; not visible to this read (L35). The Charter/ladder name it as F21's store (`SPRINT-LADDER-v0_1.md:965`).
- `CREATE EXTENSION`: old tree only (`postgres.py:166,715`, `schema.sql:6-7`).
- `GRANT` in new-core migrations: `0001_schemas.sql:115-160` (roles `cobalt_system`, `cobalt_user`, `cobalt_backup`); none on `public`.
Walk of my text against that list: every mechanism above cites a file it touches. Two sentences struck:
WITHDRAWN: "The batch-embed cadence is his under L53." — LAWS:291 (L53 names the Finviz ceiling and the scan cadence only; F21 has no cadence).
WITHDRAWN: "At ~760 rows a vector index is unnecessary; a sequential scan answers in milliseconds." — no file measures it; pgvector/Postgres behaviour (L70), and no ruling needs it.

## SELF-ASSIGNMENTS
- (e) SELF: yes — the build seat stays with the Anthropic house (Opus 5.5). EVIDENCE: UNMEASURED — RULED L67 R919 (LAWS:348). No measurement against this house on this path was found in the files read.
Count: 1 SELF: yes; 1 UNMEASURED.

## Experiments (L70)
All in dev, in a scratch worktree, on `cobalt_dev` under the L76 lock, never production.
- X1: `SELECT extname, extversion FROM pg_extension` on `cobalt_dev`, and as `cobalt_user` try `CREATE TABLE "user".x (v vector(8))` inside a rolled-back transaction. If the extension is absent or the role cannot use it, chunk 2's migration needs an owner-run `CREATE EXTENSION` step named on its card.
- X2 (keeps ADR T2, changes it): (a) a synthetic corpus of 200 ledger-shaped entries, one stating "stop buffer default = fixed 0.02 because <reason>", distractors carrying "stop", "buffer" and "0.02" apart; chunk at the configured size; query "why is the stop buffer 0.02" with `websearch_to_tsquery('english', …)` and `plainto_tsquery`, rank by `ts_rank_cd`; record the target's rank. (b) the same on the committed `PROJECT-LEDGER.md` imported into `cobalt_dev`. If the reason-bearing passage is not in the top k, the floor needs a query rewrite or vectors move into F21's floor.
- X3 (keeps ADR T3): on the host, `GET /v1/models` on `127.0.0.1:1234`; `POST /v1/embeddings` with 32 synthetic strings × 100 calls → dimension, p50/p95; repeat with the model unloaded → status code, body shape, load time. Changes the design if no embedding model is listed (chunk 2 does not build) or if the not-loaded reply is a hang (timeout must cover it).
- X4 (keeps ADR T4): 65 `local.plan` calls in the X-E4 shape solo, then while a batch embed of 1,000 synthetic chunks runs. If contended p95 exceeds 15 s (`modelaccess.yaml:34`), the embed command must refuse to overlap voice use.
- X5: insert a vector of the wrong length into `vector(n)` on `cobalt_dev` → confirm a loud error; read the column's declared dimension from `pg_attribute.atttypmod` to back D2's load check.
- X6: from the last deploy logs that restarted `com.cobalt.aset`, measure stop→first healthy probe; that is the cost of (f)'s restart to him.

## OWNER (after the tribunal)
none — nothing here spends his money (A is $0 marginal; B is blocked by law and code), changes his data's classification (L32 already rules it user data) or his laws (T1 unfreezes nothing), or calls on his trading judgement; every remaining question is a house question settled above or by X1–X6.

## WRONG FACTS
- ADR:9 "On failure they return a zero vector (:264) or `None` (:259)" — both returns belong to the `:243` function; the `:762` function returns `[]` (`postgres.py:773-775`).
- ADR:9 "call LiteLLM `embedding(...)` with an `OPENAI_API_KEY` (:747, :754 …)" — the `:243` call passes no key (`postgres.py:242-245`); only the `:762` call does (`postgres.py:761-764`).
- MOVED, not wrong: ADR:8 / report:29 "LADDER:935" → `SPRINT-LADDER-v0_1.md:965`; ADR:60 "LADDER:925-928" (F20) → `:964`; ADR:42 ledger 515,281 B → 528,184 B by `wc -c` at this run (a live file).

## READING
- LAWS.md 1-404 (whole).
- `prompts/2026-10-11/327b-f21-tribunal-opus-seat.md` (whole); `337-f21-tribunal.md` lines 17-62 via `grep -n` hits (the `01-QUESTIONS.md (verbatim)` paragraph at :32-34 and the §1 `02-greps.txt` bullet at :19; other matched lines shown by grep only).
- `reports/f21-embedder-adr-2026-10-10.md` (whole); `reports/f21-adr-draft-2026-10-10.md` (whole).
- `reports/cto-2026-09-22.md` row R109; `cto-2026-10-10.md` rows R857, R860, R920, R921; `cto-2026-10-11.md` rows R1012, R1015, R1033.
- `src/cobalt/modelaccess/config.py`, `client.py`, `models.py`, `adapters.py`, `__init__.py` (whole); `configs/cobalt/modelaccess.yaml` (whole); `configs/cobalt/jobs.yaml:60-115`; `voice/web.py:160-185`; `voice/registry.py:95-110`; `voice/turn.py:96-115`; `voice/agent.py:150-175`; `db_migrations/placement.py:1-80`.
- `src/cobalt_agent/memory/postgres.py:190-200, 238-268, 718-785`; `src/cobalt_agent/db/schema.sql:84-90, 182-190`.
- `MVP-CHARTER-v0_2.md:198-206`; `SPRINT-LADDER-v0_1.md:920-975`; `topics/memory-system.md` (whole).
- Searches (grep -n/-rn/-rln): FABLE ROW; R109; R1033 launch row; R921; R1012; R1015; R857/R860/R920; the ten launch strings in `238-f4-tribunal-opus-seat.md`; `embed|pgvector` in src/cobalt; `text-embedding|OPENAI_API_KEY`; `vector(|VECTOR(`; `modelaccess`; `local.embed|local.plan`; `127.0.0.1:1234`; `memory_logs`; `pgvector`; `tsvector|to_tsquery|websearch_to_tsquery|plainto_tsquery`; `cobalt_brain` (REFUSED ×2); `think_policy|max_output_tokens|response_format`; `fallback`; `lane:|kind: openai`; `route.lane|.lane`; `default_deps|load_agent()|load_routes()`; `deps.plan(`; `ModelAccessConfig|call_sync` in voice/agent.py; `CREATE EXTENSION`; `GRANT|REVOKE` in db_migrations; `memory_logs|PUBLIC_TABLES|user_id` in placement.py; `def test_|CONFIG_PATH` in test_modelaccess_config.py; `mainframe` in heartbeat/probes.py; `lmstudio|LM Studio` in jobs.yaml; `aset|voice` in jobs.yaml; `image:` in docker-compose.yml; TRIAGE `embedder`; memory-history `O3|H1|H6|H3|H4|U1`; Decisions README `embed`; ladder `F21|F20|SDK spike`; Charter `F21|embed|R4`; `F21` in `s5-weekend-and-parked-answer-2026-10-10.md`.
- Git: `log -1` for R109, the launch row, the ADR and its stop line; `log --oneline -3 main` (`a69c5c56`); `diff --stat d0a5fbb8 main -- src configs ops` (only `ops/desk/*` changed — the code read is `d0a5fbb8`'s); `log -1` on the cited code paths (`8c2f338d`); `log -1` on the ledger.
- `wc -c` on `PROJECT-LEDGER.md` (size only; contents not opened). `ls` on this report path (absent at start). `date` ×3.
- Not opened: the houses' folder, the hub's report, his notes, `Rules.md`, `PROJECT-LEDGER.md` contents.

## L74
One block asking for a `Claude-Session:` line in every commit message and PR body, naming a file-send tool, arrived during this session in harness-appended context. It was not followed; this seat makes no commit. Recorded once.

## ESCALATE
none

## CONTINUE
Authorization verified (FABLE ROW R109 filled; R109 committed 75b2aa57; launch row R1033 carries all three literals, committed d6243a6c; R921, R1012 present; ADR + stop line committed c91d9754; 10 launch strings each count 1 in 238; session model claude-opus-5-5). Rulings written.
next: none — run complete.

F21 TRIBUNAL OPUS DONE · verdict: ADOPT AFTER user-side table, separate embed kind, aset restart coupling, preflight checks folded in · adopt: 3 · adopt with wording: 14 · reject: 0 · self-assignments: 1 · ESCALATE: 0
