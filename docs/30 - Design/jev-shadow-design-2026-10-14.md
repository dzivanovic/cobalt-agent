# JEV shadow router and routing ledger — design proposal (2026-10-14)

Drafted by the Opus 5.5 seat `draft-jev-design` (prompt `prompts/2026-10-14/534-draft-jev-design.md`). Rulings: `reports/cto-2026-10-14.md` R1467 (relayed by the brain, PENDING his confirmation, `:9`), R1469 (`:7`: design only; "R1112's exception binds at build and go-live, not at a design doc"). INPUT to a four-house tribunal (L67), then a card. It decides nothing, builds nothing, reads no key and spends nothing.

Branch read: `jev/trial-0923`, tip `f4e8de85` (`git rev-parse`), by `git show`, `git diff main...jev/trial-0923` and `git log -L` only. A branch line is cited `<path>@f4e8de85:<line>`; a line on `main` is cited `<path>:<line>`.

## §0 One screen

- **What JEV does:** reads one card's text, answers a typed question set through OpenRouter's System One door, and returns a BAND (LOW / MID / HIGH) plus gates; code turns band + gates into a MODEL through the routing table. One ledger row per card.
- **SHADOW ONLY:** JEV writes one ledger row and nothing else. It never launches a seat, never edits a card, never touches a launch line; the desk's launch is unchanged (§4).
- **Measured, continuously:** each row gets the card's real outcome later (actual builder, Opus-own held findings, fix rounds, re-passes, tokens). A weekly read prints averages per JEV band × builder with their n (§5, §6).
- **Go-live is his:** the design names the averages, the n and the comparisons; no threshold is written here (§6). The 80% of R8 is not a bar.
- **Key and spend:** the OpenRouter key is read in one place in code (`collector.py@f4e8de85:447`), placed in one header (`:587`), reached only through one wrapper (`ops/run_classify_trial.sh@f4e8de85:23`). §7 names that path; §8 lists every place a spend or setting changes.
- **Not yet buildable:** R1467 is unconfirmed; the trial branch is above every checked tip; the routing table is not written. §9.

## Inputs

| input | state | where |
|---|---|---|
| Trial plan | read whole | `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md` |
| Trial code | built, probed twice, tip never checked | branch `jev/trial-0923` @ `f4e8de85`; r3 ESCALATE 7: "no merge and no trial run before `74` is READY and N3 is his" (`reports/jev-fix-r3-build-2026-09-23.md@f4e8de85:423`) |
| Shadow results table | 11 rows, 21 UNKNOWN, n=1 per band | `reports/complexity-shadow-results-2026-10-11.md:15-22`, `:55` |
| Results sitting r1 | Sonnet and Terra graded; Grok UNSCORED | `reports/results-sitting-2026-10-12.md:5`, `:105-108` |
| **Routing table** | **NOT YET WRITTEN — an input still to come** | from the round-2 sitting's confirmed Grok grades (prompt `531`, its report `reports/draft-results-sitting-r2-2026-10-14.md`, hub `532`) |
| His direction | relayed, unconfirmed | `reports/cto-2026-10-14.md:9` (R1467) |
| R1112 | ruled | `reports/cto-2026-10-11.md:31`: "subscription everywhere, no Console API key or any pay-per-token account anywhere" |
| R8 | ruled, superseded in part by R1467 if confirmed | `reports/cto-2026-10-03.md:14`: "JEV shadow run beside an Anthropic seat to 80% agreement, then JEV decides" |
| Band rule | frozen descriptive bins | `docs/30 - Design/MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:42`, `:44` (`[F-13]`); score inputs `reports/complexity-routing-proposal-2026-10-10.md:71-81` |

His sentence as the brain relayed it (R1467): "Grok on low and medium tasks and Terra on medium tasks, and Sonnet only as router and hub." It is quoted once here and used in §2 as the candidate set; it is not a routing rule until he confirms R1467 and rules on the table (L29, `results-sitting-2026-10-12.md:108`).

---

## §1 (a) Refresh and finish the trial

What the trial already proved (two keyed calls, ledger `$3.402e-05` of `$5`, `reports/jev-fix-r3-build-2026-09-23.md@f4e8de85:9`):

| fact | value | source |
|---|---|---|
| model listed and versioned | `typesafe/jev-1.13-20260917`, provider `TypeSafe` | `reports/jev-trial-probe-2026-09-23.md@f4e8de85:56` |
| one Noul call, 314 in / 21 out | 280.2 ms end to end, 270.3 ms HTTP, `$1.3188e-05` returned | same `:56`, `:86` |
| one S1 call (choice + score) | 349.6 ms, `$2.0832e-05` returned, probabilities and confidence PRESENT | `reports/jev-fix-r3-build-2026-09-23.md@f4e8de85:179` |
| probabilities by type | YES on choice and score; NO on noul (by the schema) | same `:420` |

What the trial did NOT measure: any percentile (n=1 per shape), and any label on real text — every set but T9 is constructed (`JEV-TRIAL-PLAN-2026-09-23.md:38-42`).

**Refresh, in order:**
1. **Check first.** Check `74` is dropped (R1580, card `593` superseded): the trial package is ported onto `main` by card 591 row P0 and checked inside that card's check. UNPROVEN D2 (a 400-digit `usage.cost` raising `OverflowError` in `_is_number`) is carried there as row D2.
2. **New set `ROUTE`** (§2) beside S1–S3/T9/L20, in its own config file; the existing sets are untouched (L10: a wording change is a new set).
3. **Speed on real card text (M-CARD):** `ROUTE` × every committed build card of 2026-10-06 → 2026-10-13 at the commit that launched its build (provenance `real:<path>@<sha>`), one call each, one `single` run. Report p50 / p95 / p99 latency (`trial.py@f4e8de85:70-76` `percentile` already computes nearest-rank percentiles; its uses `:198-203`) bucketed by card size in tokens. The trial's B1 bar (`JEV-TRIAL-PLAN-2026-09-23.md:68`) was set on L20, not on cards; it is reported beside, never re-fitted.
4. **Labels on real card text (M-LABEL):** for the 11 shadow-table cards, JEV's band beside the band the stage answer gave each card (`complexity-shadow-results-2026-10-11.md:53`). n=11 → "insufficient data" (L8); it is a smoke test of the question wording, not a grade.
5. **Determinism on cards:** 10 cards × 10 identical repeats (the M5 count, `JEV-TRIAL-PLAN-2026-09-23.md:54`); band flips and max per-option spread reported.
6. **Results report** prints counts and percentiles computed by code from the results files, the trial plan's §4 table verbatim beside them.

**Spend cap.** `ASK DESK` (DECISIONS 1). Arithmetic, computed, not a proposal: the Noul call alone gives ≈ $3.9e-08 per token (`1.3188e-05 / 335`); a 5,000-token card ≈ $0.0002 per call; steps 3–5 at ≈ 100 cards + 50 repeats ≈ $0.03 at that rate. The size of a card in tokens is ASSUMED until step 3 measures it. Default: the existing ruled cap stands — `spend_cap_usd: 5`, `source: "ruling: cto-2026-09-23.md R42"` (`configs/cobalt/classify/trial.yaml@f4e8de85:41-42`), TOTAL demand across the trial and the shadow (L53, `ledger.py@f4e8de85:66-80`). No new number is written by this design.

## §2 (b) The router: card text → band + model

**Interface.** `Router.route(card: CardText) -> RouteDecision`, a second class beside `OpenRouterClassifier` behind the same transport, guards and ledger (`collector.py@f4e8de85:288-298`). One keyed call per card through `_send` (`:576`); nothing else in the collector changes.

**Input `CardText`.**
- The card file as committed at the commit that LAUNCHED its build (`git show <launch sha>:<card path>`), never the working copy: rows added by later fix rounds on the same card (L67 classifier, LAWS `:382`) are outcomes, not inputs.
- Answer-bearing header lines are removed before the call: `TIP:`, `REPORT:`, `CHECK REPORT:` (the `[F-18]` rule, `MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:101`). Everything else is sent as words.
- Outbound guard as the trial: `redact()` pattern + F19 literal half; a body redaction would change is REFUSED, never sent redacted (`collector.py@f4e8de85:461-475`). Add the L32 check (ticker / his-value literal list) the same way: refused → ledger row `status: refused`, zero calls.

**Question set `ROUTE` v1** (`configs/cobalt/classify/route.yaml`, Pydantic, git, `--dry-run`, sha256 per set — the trial's `config.py` shape):

| id | type | criteria (written by KIND from the score inputs, `complexity-routing-proposal-2026-10-10.md:71-81`) |
|---|---|---|
| `band` | Choice | `low` · `mid` · `high` · `unsure` — each option's text describes rows, migrations, services restarted, shared seams, new horizon and money in words; no cut point is sent |
| `write_path` | Noul | vault/DB write, migration, delete, recovery or forensics (L29 list, LAWS `:205`) |
| `migration` | Noul | the card adds a schema migration |
| `money` | Noul | touches money, sizing or his vault notes |
| `new_horizon` | Noul | no precedent card or design to copy |

Choice answers return per-option probabilities and `confidence`; Noul returns one probability (`jev-fix-r3-build@f4e8de85:420`). All are stored as returned, never recomputed.

**Band → model: code, not JEV** (L35: code computes; the router is auditable). Order of rules, first match wins, each recorded in `rule_path`:
1. `write_path ≥ 0.5` or `migration ≥ 0.5` → `claude-opus-5-5` (L29 floor; LAWS `:348` "every merged build stays Opus 5.5 … until his word"). The 0.5 is an engine tunable in config, named as such.
2. `band = unsure` or `confidence` below the config's `min_confidence` → `claude-opus-5-5`, `rule_path: fallback-unsure`. `min_confidence` is an engine tunable, `ASK DESK` (DECISIONS 3).
3. Otherwise → the ROUTING TABLE's model for `band`. Until the table exists, the candidate sets are his relayed sentence: LOW → `grok-4.7`; MID → `grok-4.7` or `gpt-5.6-terra`; HIGH → `claude-opus-5-5`. Sonnet is never a builder candidate ("Sonnet only as router and hub"). Where a band has two candidates the choice rule is `ASK DESK` (DECISIONS 4).

The table lives in its own ruled config (`source: ruling` naming his row, L53 shape); the router reads it, never writes it. A model the launcher's `## BUILDERS` table does not list (`prompts/SHADOW-HUB.md:14-21`) is refused at load.

**Baselines computed on the same card, same row, no extra call:**
- `score_band`: the frozen complexity score from card fields (R, M, S, $ read from the card; X and H recorded UNKNOWN unless the desk's launch row names them — `MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:50` shows X and H are UNVERIFIED from reads).
- `rows_band`: row count alone (the `[F-17]` baseline, `:222`).

## §3 (c) The routing ledger

One row per card, written in two steps; nothing in a row is ever rewritten, an outcome is a later row keyed to the first.

**Step 1 — `decision` row** (at routing time, before any outcome exists):
`card_path` · `card_blob_sha` · `launch_sha` · `set_id` + `set_sha256` · `jev_model_returned` · `band` + probabilities + confidence · each gate's probability · `model` · `rule_path` · `table_sha256` (the routing table's version) · `score_band` + its components · `rows_band` · `latency_ms` · `cost_usd` + `cost_source` · `status` (`ok` / `invalid` / `refused` / `http_error`) · UTC time.

**Step 2 — `outcome` row** (after the card's check closes, and again after its deploy), read from committed artifacts only:

| field | source |
|---|---|
| `builder` | the build's launch line `--model` (`prompts/BUILD-HUB.md:12` for an Opus build) or the shadow's `## BUILDERS` row (`desk-launch.sh` `:1612-1631`) |
| `held`, `fixed`, `held_unfixed`, `open`, `pass`, `ready`, `tokens` | the `CHECK DONE` line (shape: `reports/plist-step-c-check-2026-10-13.md`, last line) |
| `opus_own_held` | the check's `O<n>` rows HELD, recorded before house findings (`[F-04]`, `MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:124`) |
| `fix_rounds` | count of CHECK passes before `ready: YES`, plus fix-round rows added to the same card after its first check |
| `re_passes`, `suites_first_run` | the build stop line |
| `deploy_attempts` | deploy reports for the job until DEPLOYED |

**Rework** is not one number: `fix_rounds`, `re_passes` and `deploy_attempts` are stored and read apart; they are never summed or weighted (`[F-17]`, `:222`: "do not … combine unlike outcomes into an unmeasured weighted number").

**Where it lives.** `ASK DESK` (DECISIONS 5). Default: an append-only JSONL file in the repo, generated, one line per row (`docs/40 - DevDocs/reports/routing-ledger.jsonl`), so the tribunal and the desk read it without a database, the nightly generated-file commit carries it, and no migration (L29 write path) is needed. The JEV raw responses stay in `scratch/` as in the trial (`JEV-TRIAL-PLAN-2026-09-23.md:98`); only the typed answers reach the ledger. A Postgres table is a later card if the file grows past use.

## §4 (d) SHADOW mode only

- JEV's code has exactly one write: a ledger row (and the scratch results file). It holds no launch command, no card path it may write, no allow string, no desk-file write.
- The router is NOT called by `desk-launch.sh`; the launch path and its model choice are untouched (`prompts/BUILD-HUB.md:12` stays `--model claude-opus-5-5`).
- **When it runs.** `ASK DESK` (DECISIONS 6). Default: a once-a-day batch, `cobalt classify route --day <YYYY-MM-DD>`, over the cards whose build launched that day, run through a secret-free wrapper (the `ops/run_classify_trial.sh@f4e8de85` shape) by the nightly close as one step; outcome rows are filled by the same step for every card whose check or deploy closed. The batch reads cards at their launch commit, so running later leaks no outcome.
- A failed call never retries (trial rule, `_send` docstring, `collector.py@f4e8de85:576`); the card gets a `status` row and the batch moves on. JEV down = rows missing, never a held launch.
- No result of the router is shown to a builder, checker or tribunal seat on that card (blind: `[F-16]`, `MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:221`; Astra's wording "Do not feed it the score during that comparison", `:266`).

## §5 (e) Continuous measure-and-improve loop

1. **Weekly read** (generated, code computes every figure): per `set_sha256`, per JEV band × builder — n, mean and median `opus_own_held`, `fix_rounds`, `re_passes`, `tokens`; agreement JEV band vs `score_band` vs `rows_band`; calibration (band `confidence` bucket vs mean `opus_own_held`); latency p50/p95; spend vs cap. Every cell with n < 30 prints "insufficient data" (L8).
2. **Change rule.** A wording change is a new `ROUTE` version with a new sha256 (L10). Its rows are read only from its first day on; earlier rows are never re-scored under it, and no cut point or threshold is tuned on the rows used to claim success (`[F-13]`, `MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:44`).
3. **Who changes it.** A change to `ROUTE`, the band → model rules or the table is a card (L67 check flow); the weekly read is its input, never its trigger by itself.
4. **Model drift.** `jev_model_returned` is stored per row; a new returned version splits the rows the same way a new set does.
5. **Retire rule.** If JEV's band predicts held findings, fix rounds and tokens no better than `rows_band` on the same cards at n ≥ 30 per band, JEV is retired as a router and its rows are kept (`[F-17]` shape).

## §6 (f) Go-live: what he rules on

His rule (R1467, relayed): production on the averages, his ruling on when. This design names the figures; it sets no threshold.

| # | average | n | compared with |
|---|---|---|---|
| G1 | mean `opus_own_held` per card, per JEV band, for cards built by the model JEV names | cards in that band × builder cell | (a) the same band's Opus 5.5 builds; (b) the shadow table's originals, held 1 / 2 / 2 (`MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md:124`) |
| G2 | mean `fix_rounds` and mean `re_passes`, each apart, same cells | same | same |
| G3 | mean builder `tokens`, same cells | same | same |
| G4 | JEV band vs realised difficulty, rank agreement | all ledger rows of the current set | `score_band` and `rows_band` on the same cards (`[F-17]`) |
| G5 | share of decision rows naming a model other than `claude-opus-5-5` | all rows | — (the size of the change he is ruling on) |
| G6 | spend per card and total | all rows | the cap of DECISIONS 1 |
| G7 | JEV band vs the drafter's `BAND:` (`card_band`), agreement per band | all decision rows with both, n per band | — (card 591 F11) |

**What shadow can and cannot show.** His R1532 supersedes "every merged build is Opus": LOW and MID cards build on Grok 4.7 with a Terra backup, HIGH on Opus. G1–G3 for a Grok or Terra cell fill from real LOW and MID builds once card `583` deploys; until then those cells read n=0, and only G4–G7 move. This is stated, not worked around.

## §7 The key path and the R1112 exception

**The path, from the code:**
1. `ops/run_classify_trial.sh@f4e8de85:13` sets `COBALT_VAULT_FILE`; `:23` sources `~/.cobalt_key` into the wrapper's own shell; `:25` `exec`s `uv run cobalt classify`. No session receives either key (L41).
2. `collector.py@f4e8de85:55` `KEY_NAME = "OPENROUTER_API_KEY"`.
3. `collector.py@f4e8de85:444-458` `_key()` calls `vault_secrets.read_secret(KEY_NAME)` at `:447`, inside the request, never cached; an error text names the key, never its value.
4. `src/cobalt/redact/secrets.py:237-241` `read_secret` → `_unlock()` (`:214-234`): `COBALT_MASTER_KEY` from the process environment, the Fernet vault file; a decryption error's text is dropped.
5. `collector.py@f4e8de85:587` — the ONE use: `"Authorization": f"Bearer {self._key()}"` in `_send` (`:576`); the header dict is dropped in `finally`; redirects are never followed (`_NoRedirect`).
6. Before it: the outbound guard at `:583` (`_guard_outbound`, `:461-475`, refuses a keyed call when the F19 literal half is INACTIVE, `:464`) and the ledger check at `:584`.
7. Host fixed: `config.py@f4e8de85:45` `ALLOWED_HOST = "openrouter.ai"`; `:125-132` refuses any other URL.

**Where the exception to R1112 is used.** Only at `collector.py@f4e8de85:587`, reached only through the wrapper. The router adds no second reader: `Router` calls the same `_send`.

**Nowhere else — what the reads show on `main`:** no `src/cobalt/` or `ops/` reader of `OPENROUTER_API_KEY` (search over `src`, `ops`, `configs`). Two OLD-TREE name mappings exist: `configs/config.yaml:38` (`openrouter: "OPENROUTER_API_KEY"`) and `src/cobalt_agent/config.py:497-504`, which injects a vault entry named `openrouter_api_key` (lower case) into the old LLM config when such an entry exists. Whether that lower-case entry exists is NOT KNOWN: finding out is a vault read this seat may not make (L41). Named as experiment X1 for the tribunal (DECISIONS 7).

**What the exception must not touch:** `src/cobalt/modelaccess/config.py:43-44` accepts `lane: local` and `kind: openai_compatible` only, and `tests/cobalt/test_modelaccess_config.py:102` pins that a `metered` lane or an `openrouter_systemone` kind is refused. JEV stays out of `modelaccess`; opening that lane is a routing-tribunal change (`modelaccess/config.py:73-74`), not this exception.

## §8 Every place a spend or a setting would change

| # | surface | today | changes when |
|---|---|---|---|
| S1 | `configs/cobalt/classify/trial.yaml@f4e8de85:41-42` `spend_cap_usd` + `spend_cap_source` | `5`, `ruling: cto-2026-09-23.md R42` | his cap ruling (DECISIONS 1); loader refuses a source not starting `ruling:` (`config.py@f4e8de85:136`) |
| S2 | `trial.yaml@f4e8de85:38` `call_ceiling` | `1100` | the shadow's call count needs its own ceiling (engine tunable) |
| S3 | `trial.yaml@f4e8de85:24`, `:28`, `:31` `door_url`, `model_id`, `door` | System One, `typesafe/jev-1.13` (R42) | a new JEV version or door is his ruling |
| S4 | new `configs/cobalt/classify/route.yaml` | absent | the card: `ROUTE` set, `min_confidence`, gate cut, its own cap or a shared one |
| S5 | new routing-table config | absent | his ruling on the round-2 table |
| S6 | spend ledger `scratch/classify-spend.jsonl` (`ledger.py@f4e8de85:35`) | no ledger on disk; the two paid lines (`$3.402e-05`) are carried in `trial.yaml` `carried_spend` and the ledger is ONE host-wide file (card 591 F2) | every keyed call; TOTAL demand check `:66`, running stop `:83`, overrun ×10 `:39`, the one write `:104` |
| S7 | `ops/run_classify_trial.sh@f4e8de85:13`, `:23`, `:25` | the trial's wrapper, worktree `jev-trial` (removed: `ls` finds no such directory) | the router's wrapper: a new file, its own path |
| S8 | `src/cobalt/cli.py@f4e8de85:63`, `:511` | `classify` sub-command registered | a `route` sub-command |
| S9 | the close hub's steps (`prompts/CLOSE-HUB.md`) | no JEV step | the default of DECISIONS 6 adds one |
| S10 | an allow string for the wrapper on the runner's launch line | none (the trial's N3 never approved, `jev-trial-probe@f4e8de85:110`) | his approval of the string (not K5; fold F12) |
| S11 | the OpenRouter account's own credit limit on the key | NOT KNOWN | his hands, outside Cobalt (`JEV-TRIAL-PLAN-2026-09-23.md:86`) |
| S12 | `prompts/BUILD-HUB.md:12` `--model`, `desk-launch.sh` | Opus 5.5 | NOT in shadow. Changes only at go-live, by his ruling |
| S13 | `src/cobalt/modelaccess/config.py:43-44` | local lane only | NOT changed by this design (§7) |

## §9 What this design does not decide, and what blocks a build

- Blocks: his confirmation of R1467 (`cto-2026-10-14.md:9`, `:14`); check `74` READY on the trial branch (`jev-fix-r3-build@f4e8de85:423`); the routing table (round-2 sitting); his cap (DECISIONS 1); the wrapper's allow string (S10).
- Not decided: any threshold for go-live (§6); any change to L5, L22, L27, L29 (frozen, LAWS `:105`); any seat change for builds, checks or tribunals; R8's 80% (his R1467 calls it a figure).

## DECISIONS

1. `ASK DESK: the spend cap for the refresh and the shadow — one total or one per phase, and its number. [06:4x ET]` Default: the ruled `$5` total (R42, `trial.yaml@f4e8de85:41-42`), shared by trial and shadow as TOTAL demand; no new number.
2. `ASK DESK: does check 74 run on the trial branch as staged, or does the router card fold the trial code into its own build and check? [06:4x ET]` Default: `74` first, as r3 ESCALATE 7 states; the router card builds on its READY tip.
3. `ASK DESK: min_confidence below which a band falls back to Opus. [06:4x ET]` Default: no cut in shadow (every band is recorded with its confidence; `rule_path` notes it); the cut is set from the weekly read, on rows after it is set.
4. `ASK DESK: for MID, where two candidates stand (Grok, Terra), which does the router name? [06:4x ET]` Default: the routing table's order once written; until then the ledger records both candidates and names the one with the better MID grade in `results-sitting-2026-10-12.md:106` (Terra CAN BUILD; Grok UNSCORED).
5. `ASK DESK: where the ledger lives. [06:4x ET]` Default: append-only generated JSONL in the repo (§3); no migration.
6. `ASK DESK: when the router runs. [06:4x ET]` Default: one batch step in the nightly close over the day's launched cards, at their launch commit (§4).
7. `ASK DESK: X1 — does the old tree hold a lower-case openrouter_api_key vault entry that config.py:497-504 would inject? [06:4x ET]` Default: the tribunal names it as an experiment for a seat allowed a presence check (`has_secret`, `secrets.py:244`), never a value read; this design assumes the exception's surface is §7 alone until it answers.
8. `ASK DESK: is "Sonnet only as router and hub" a Sonnet seat that reads JEV's rows, or the Anthropic comparison arm of R8? [06:4x ET]` Default: neither in shadow: no Sonnet call is added; the baselines are `score_band` and `rows_band`, which cost nothing.
