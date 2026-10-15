# `src/cobalt/classify/models.py`

## What it does
The neutral typed-question schema and the per-call record of the JEV
trial (plan `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md`).

- `Choice` (instructions, `options: {key: description}`), `Score`
  (instructions, `levels`, 2–10, lowest first, distinct), `Noul`
  (instructions, optional `true` / `false` descriptions) — the three
  primitives of the typed-classifier research (deep research §2 rows 1–3),
  written with no vendor field name so any door can render them (L9).
- `QuestionSet` — an ORDERED map of question id → question. `sha256` is
  computed (never stored) over the canonical JSON of the questions in
  order: exactly what is sent. A one-character wording change, or a
  reordering, is a new set (L10). `first(n)` (plan M2), `reversed()`
  (plan M6), `only(qid)` (parallel / sequential modes).
- `TrialItem` — one state (`str` or `dict[str, str]`) and its provenance
  (`constructed` or `real:<repo path>`).
- `Answer` (`value` = the door's own returned field, never thresholded:
  a Choice's option key, a Score's position, a Noul's probability of
  yes), `Usage`, `ModelEntry` (one entry of OpenRouter's public model
  list, extra fields KEPT), `CallRecord` (L57: set id + sha256, item id +
  provenance, request, raw response, answers, `latency_ms`, `http_ms`,
  `status` + `http_status`, usage, cost + `cost_source`, `projected_usd`,
  `model_returned`, `provider_returned`, `door = "openrouter"`, UTC time).

## Rules it keeps
- **`unsure` is required** in every `Choice`: abstaining is the question's
  answer, never the code's.
- **A state is WORDS.** A dict state refuses any numeric value — an int, a
  float, a bool, or a string that reads as a number (`"3"`, `"-0.25"`,
  `"1e3"`). Code buckets numbers into words before they get here (plan §2;
  bucket edges are his, L53).
- **Confidence only as returned.** `Answer.probabilities` / `confidence`
  default to `None`; `source: absent` says the response did not carry
  them. Nothing is computed or defaulted (L1).
- **An `ok` record carries usage and a cost** — "no cost, no call".

## What it never does
Holds a key, touches the network, a database or the vault. Pure data.
