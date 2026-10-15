# `src/cobalt/classify/cli.py`

## What it does
Registers `cobalt classify` (via `add_parser(sub)`, called from
`src/cobalt/cli.py`). Subcommands `discover`, `probe`, `trial`.

    cobalt classify discover --out scratch/openrouter-models-<YYYYMMDD>.json

KEYLESS: `OpenRouterClassifier.discover_detail()` — his id's per-model
endpoints record first (the authority, desk R46), the general list second
(only to record other matching ids). Writes, each through `_guard_stored`,
inside the configured `scratch/` results dir (`--out` elsewhere is
refused):
- `<out>` — `models_listed`, `ruled_id`, `ruled_id_listed: true`,
  `ruled_id_source`, `endpoints_record` and `other_matching` (the OTHER
  matching entries only — never the rest of the list);
- `<out stem>.endpoints.json` — the endpoints response body byte for
  byte: the source of `tests/fixtures/classify/openrouter-model-entry.real-shape.json`
  (L45).

Prints one `DISCOVER ruled=<id> ruled_listed=yes … models_listed=<n>
others=<ids|none> …` line. Any `ClassifyError` reaches `cobalt`'s
top-level handler as `FAILED: ClassifyError: <redacted text>`, exit 1.

## `probe` — KEYED, METERED, one call per set per branch

    cobalt classify probe [--set FLOOR|S1] --out scratch/probe-[s1-]<YYYYMMDDTHHMMSS>.json

ONE call of the set's first item through
`OpenRouterClassifier._classify` — so the outbound guard, `ledger.check`
before the POST and ledger `record` after it, exactly as every trial
call. `--set FLOOR` (the default; build `31`) asks FLOOR's one Noul,
which by the schema (`DecisionsNoulAnswer`: `noul` only) cannot show
probabilities or confidence. `--set S1` (JEV fix r3 P1, his R89) asks
S1's item `s1-01` with its choice (`relevance`), score (`urgency`) and
two Nouls — the answer types that carry `probabilities` / `confidence`.
Any other set is refused (argparse `choices`, and `cmd_probe` itself).
Refuses with zero calls when `--out` is not a `probe-*.json` (FLOOR) or
`probe-s1-*.json` (S1) inside `scratch/`, or when that set's file
already exists — FLOOR's glob `probe-*.json` also sees an S1 file,
S1's glob sees only `probe-s1-*.json` (one metered probe per set per
branch; the refusal names the file). Writes `<out>` =
the guarded `CallRecord` and `<out stem>.raw.json` = the raw body byte
for byte; a body the stored guard refuses writes neither, and the error
names the KIND of hit only. Prints exactly one line:

    PROBE status=<http> model=<returned> provider=<returned|none> latency_ms=<n> http_ms=<n> cost_usd=<x> cost_source=<returned|computed> probabilities=<present|absent> confidence=<present|absent> ledger_usd=<total> cap_usd=<cap> guard_literals=<active|INACTIVE>

The 10× overrun check runs AFTER the files are written (the capture is
kept; the command then exits non-zero). A non-`ok` status exits non-zero
after the line. It runs only through `ops/run_classify_trial.sh` (the
secret-free wrapper that unlocks the vault), and only after the
three-house check `29` reads READY (desk R42).

## `trial`

    cobalt classify trial --set <FLOOR|S1|S2|S3|T9|L20> [--reps n] [--mode single|parallel|sequential|gated] [--questions n] [--reverse] (--dry-run|--run) [--tag text]

`--dry-run` prints `trial.dry_run`'s one `DRY …` line, with ZERO network
calls. `--run` is KEYED and METERED. It prints `trial.run`'s one
`RUN …` line and is never run by build `28`; the trial-run hub runs it
through the wrapper, under the approved cap. See `trial.md`.

## What it never does
Reads the key on `discover` (discovery is public); calls any host but
`openrouter.ai`; writes outside `scratch/`; opens a database; writes the
vault; retries a call.

## Laws
L1 (no match / no id / bad record / no price → FAILED), L4 / L41 (the
key only in the one keyed request's header), L45 (the real record, byte
for byte), L9 (one collector class behind `Classifier`), L53 (the
ledger's total demand), L57 (the probe's record).
