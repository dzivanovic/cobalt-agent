# `src/cobalt/classify/collector.py`

## What it does
The typed-classifier collector behind ONE interface (L9):
`Classifier` protocol (`discover() -> list[ModelEntry]`,
`classify(qset, item) -> CallRecord`), first class
`OpenRouterClassifier(cfg, transport=None, ledger=None)`. The local lane
plugs in later as a second class; nothing upstream notices.

`transport(method, url, headers, body, timeout) -> (status, body_bytes)`
is injectable — the default `urllib_transport` returns an HTTP error
status instead of raising, so it is recorded. The default transport
follows NO redirect (JEV fix r1 F2): it opens through `_OPENER =
build_opener(_NoRedirect)`, whose `redirect_request` returns `None`, so
a 3xx is returned as its status (a POST 3xx is recorded `http_error`; a
discovery 3xx is the existing loud `ClassifyError`). The stdlib default
would re-send every non-content header, `Authorization` included, to any
`Location` host; now the `Authorization` header can reach only the
configured `door_url`. Tests use an injected transport; the one
exception is F2's pair of LOOPBACK servers on `127.0.0.1`.

## The key (L4, L41)
`_key()` calls `cobalt.redact.secrets.read_secret("OPENROUTER_API_KEY")`
— the new core's one vault reader (L3) — INSIDE each keyed request
(`_send`). The value goes into that request's `Authorization: Bearer …`
header and nowhere else: never cached on the instance, never returned
upward, never logged. A missing key or a locked vault (`VaultAccessError`)
raises `ClassifyError` naming the KEY NAME only, before any transport
call.

## The guards (F19)
- `_guard_outbound(body, keyed=)` — `redact()` over the decoded body; a
  body the redactor would change is REFUSED (`outbound body carries
  secret-shaped text — refused, not sent`), never sent redacted. On a
  keyed call the F19 literal guard must be ACTIVE, else refused before
  sending.
- `_guard_stored(obj)` — the same over anything written to disk
  (`refused, not written`).
- Every error text passes `redact()` and is raised `from None`: a 401 body
  can echo the key back (tested with a constructed echo).
- `redact(…, record=False)` throughout: a refusal raises (louder than a
  counter row), and counting would open a database connection this trial
  never holds. Named in the build report's ESCALATE.

## Discovery — KEYLESS (`discover_detail()` / `discover()`)
Two public GETs, no `Authorization` header, `_key()` never called:
1. `endpoints_url()` = `<models_url>/<model_id>/endpoints` — his id's
   PER-MODEL record, THE AUTHORITY (desk `cto-2026-09-23.md` R46: the
   general list omits non-text-output models such as Jev, modality
   `text->decisions`). 404 → `does not list <model_id> — matching ids:
   <ids>` (or `lists no model matching <pattern> — <n> models listed` when
   the general list has none); any other non-200 → loud `HTTP <status>`;
   a record whose own `id` is not his → refused.
2. `models_url` — the general list, read only to RECORD other ids
   matching `match_pattern` (never an error when there are none, never
   substituted for his id).

`_entry_from_record` builds the `ModelEntry`: the record's model-level
fields, plus `pricing` / `context_length` / `supported_parameters` from
the endpoint when there is EXACTLY one; with several endpoints nothing is
merged and `pricing` stays `None` (L1: no cost picked for him).
`Discovery.raw_record` keeps the response body byte for byte (L45).

## `_send(payload, projected_usd=)`
Order: guard outbound → `ledger.check` (total demand, L53) → key → timed
POST to `door_url`. 401 / 403 → `ClassifyAuthError` (the run stops);
every other status is returned for recording — 429 / 5xx are NOT retried
(the trial measures raw behaviour).

## The door — OpenRouter System One (desk R47)
`POST https://openrouter.ai/api/v1/systemone` (`door: systemone`), built
field for field from OpenRouter's published OpenAPI schema
(`DecisionsRequest` / `DecisionsResponse`; the saved docs sit in the
worktree's gitignored `scratch/docs-openrouter/`).

- `render_systemone(model_id, qset, item)` → `{model, state, questions}`.
  Choice → `criteria` = its options map; Score → `criteria` = its levels
  list (index 0 = the first level); Noul → `criteria` `{"true", "false"}`
  when both are written, no `criteria` when neither, REFUSED when only
  one is (the schema requires both; one side is never invented). No other
  field is sent. The schema has no usage-accounting switch, so none is
  sent; the docs say `usage.cost` comes back on every response.
- `parse_answers(qset, resp)` → one `Answer` per asked question.
  `value` = the returned field of the question's own type: the choice key
  (must be one of the options), the score position (must sit in
  `0..levels-1`), the noul probability of yes (must sit in `0..1`).
  Never thresholded into a label (that would be a rule, and rules are
  his). `probabilities` / `confidence` only when returned; absent →
  `None`, `source: absent`. A missing, unasked or wrongly typed answer
  raises `ValueError`.
- `pricing()` — (prompt, completion) USD per token from the listed entry
  (`cfg.entry_pricing()`, R3's committed real capture), or an injected
  map. No numeric price → `ClassifyError`, before any call (L1). A listed
  price that is negative or not finite is refused the same way (`the
  entry's pricing is negative or not finite — no call`, JEV fix r2 F8):
  `project()` calls `pricing()` before `_send`, so no request is made and
  no ledger line is written.
- `project(body)` — the body's bytes ÷ 4 as input tokens (an ESTIMATE)
  × the prompt price. Output is not projected.
- `classify(qset, item)` / `_classify(…, overrun_check=True)`: render →
  project → `_send` → parse ONLY what came back → ledger `record` (when a
  cost is known — BEFORE the stored guard, so a refused body that was
  paid for still counts toward the total; the ledger line carries the
  response `id` only when that id passes the guard, else a
  `local-<uuid>` id — JEV fix r1 F3) → `_guard_stored` on the record
  and on the raw body → the 10× overrun check. `latency_ms` = render
  start → the validated record; `http_ms` = send → last byte.
  A non-200 → `status: http_error` with `http_status`, recorded, not
  retried. The FULL raw body is guarded on EVERY status path before it
  is returned or written (JEV fix r1 F1): `raw_response` keeps only
  `raw[:2000]` of a non-JSON body and `json.loads` keeps only the last
  of duplicate keys, so the record's guard alone never sees the whole
  body; `_guard_stored(raw…)` runs on the non-200 path as on the 200
  path, and `cli.py`'s probe therefore never writes an unguarded
  `.raw.json`. A 200 missing `model` or `usage`, or an answer
  `parse_answers` refuses → `status: invalid` plus a loud
  `logger.error` line (plan B3), never a default. A `usage` whose
  `input_tokens` / `output_tokens` are not two non-negative integers is
  treated as NO usage (JEV fix r2 F7): the call is `invalid`. A
  `usage.cost` the server returned (a finite number ≥ 0) is always what
  the ledger books, even when the token counts beside it are malformed
  (JEV fix r3 F9): `cost_source: returned`, the call stays `invalid`,
  and the 10× overrun check runs on it. Only a missing or unusable
  returned cost falls back to the computed cost (tokens × the listed
  price, `computed`) or, with no usable tokens, the projection. A negative returned cost is never taken (JEV fix r1 F5):
  one `logger.error` line ("returned cost is negative — computed from
  tokens instead", no response text) and the `computed` branch. A
  computed cost that is not finite (tokens × price overflowing to `inf`)
  is never recorded (JEV fix r2 F8): one `logger.error` line ("computed
  cost is not finite … — booked at its projection", ids only), the
  record's `cost_usd` / `cost_source` stay `None`, the call is `invalid`
  (an `ok` `CallRecord` must carry a cost), it is booked at its
  projection, and the overrun check is skipped. Every POST that came back is exactly ONE ledger line
  (JEV fix r1 F4): a call with no known cost — a non-200, a 200 without
  `usage`, or a 401 / 403 (booked in `_send` before `ClassifyAuthError`
  is raised) — is booked at its own projection, `cost_source:
  projected`, under a `local-<uuid>` id, before the stored guards. The
  `CallRecord`'s own `cost_usd` / `cost_source` stay `None` on those
  paths. A transport exception (nothing came back) writes no line. `model_returned` / `provider_returned` are copied as
  returned.

## What it never does
Holds a key between requests; talks to any host but `openrouter.ai`
(config-validated; no redirect is followed, so no answer can send a
request elsewhere); opens a database; writes the vault; imports LiteLLM,
a vendor SDK or the old tree (L15).

## 2026-10-15 — jev-shadow-1015
`_is_number` returns False for an int too large for a float (D2: a 400-digit `usage.cost` no longer raises `OverflowError`; the cost is computed from tokens). The default `Ledger` is the ONE host-wide `cfg.spend_ledger` with `cfg.carried_spend` (F2), never `results_path()/classify-spend.jsonl`. `_send` checks the cap on `OVERRUN_FACTOR × projected` before the call (F3).
