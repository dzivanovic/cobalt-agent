# `src/cobalt/classify/config.py`

## What it does
`configs/cobalt/classify/trial.yaml` → `TrialConfig` (L10: Pydantic
schema, in git, dry-run = `cobalt classify trial --dry-run`). A missing
file, a YAML that does not parse (the error carries its line), an unknown
key (`extra="forbid"`) or an invalid value crashes with
`ClassifyConfigError` — `notify/config.py`'s loader shape, no defaults.

The file sits under `configs/cobalt/`, outside the old loader's top-level
`configs/*.yaml` glob (CLAUDE.md config boundary).

## Validators
- `models_url`, `door_url`: `https://openrouter.ai/…` only — the one host
  this package talks to. `door_url` = `https://openrouter.ai/api/v1/systemone`
  and `door: systemone` (build step R4, desk R47); `door: ""` renders no
  request at all.
- `entry_record`: the repo path of R3's committed per-model endpoints
  capture; `entry_pricing()` reads its ONE endpoint's `pricing`, and
  anything else is FAILED (L1: no cost, no call).
- `model_id_source`, `spend_cap_source`: must start `ruling:` and name
  his row (L53). `model_id` = `typesafe/jev-1.13`, `spend_cap_usd` = 5,
  both `cto-2026-09-23.md` R42. Discovery verifies the id; it never
  replaces it.
- `results_dir`: must resolve inside the worktree's `scratch/` (never the
  vault, the DB or git).
- `sets`: exactly FLOOR, S1, S2, S3, T9, L20.

## Resolution — `cfg.resolve(name) -> (QuestionSet, [TrialItem])`
Deterministic. Questions: `questions_from` sets first, in order, then the
set's own (a duplicate id or a cycle crashes; `expect_questions` is
checked). Items: explicit items, or `items_from` another set, plus the
declared derivations — `padding` (FLOOR's ≈300 / ≈1,500-token constructed
states: base words repeated until chars ÷ 4 reaches the target),
`injection_twins` (S1: the first ten items with an instruction appended),
`shuffled_twin` (S3: the first twenty dict states with a seeded key
shuffle; a shuffle that moved nothing is rotated), `compose` (L20: S1
headline × S3 context words). `items_glob` (T9) reads Cobalt's committed
`docs/40 - DevDocs/reports/day-open-*.md` AT RUN TIME with provenance
`real:<path>`; an empty glob or an empty set crashes (L1).

Shapes as committed: FLOOR 1 question / 3 items · S1 4 / 50 · S2 3 / 40 ·
S3 3 / 60 · T9 5 / one per day-open report · L20 20 / 40.

## What it never does
Holds or names a credential, touches the network, a database or the vault.

## 2026-10-15 — jev-shadow-1015
New keys `spend_ledger` (validated by `host_ledger_path`: absolute, outside `REPO_ROOT` and `WORKTREES_ROOT`) and `carried_spend` (`CarriedSpend`: `cost_usd`, `source`), both required (F2). `host_ledger_path` is also the routing ledger's check (route.py, F8).

## 2026-10-15 — jev-shadow-1015 check
`host_ledger_path` also refuses a path under `MAIN_CHECKOUT` (`/Users/cobalt/cobalt`): from a worktree, `REPO_ROOT` is the worktree (O5).
