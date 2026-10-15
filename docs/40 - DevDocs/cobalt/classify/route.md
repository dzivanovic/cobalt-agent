# `src/cobalt/classify/route.py`

## What it does
The JEV shadow router and its routing ledger (card 591; design
`docs/30 - Design/jev-shadow-design-2026-10-14.md` §2-§6, his R1467).
SHADOW ONLY: it writes routing-ledger rows and nothing else. Nothing routes;
no launch line, hub or card is touched.

- `load_route_config(path=None, *, shadow_hub=None, trial_path=None)` —
  `configs/cobalt/classify/route.yaml` into `RouteConfig` (strict; a bad file
  crashes, no default). Set `ROUTE` v1: `band` (Choice `low` / `mid` / `high`
  / `unsure`) and four Noul gates (`write_path`, `migration`, `money`,
  `new_horizon`). The loader refuses: a `spend_ledger`, `spend_cap_usd` or
  `spend_cap_source` that differs from trial.yaml's (fold F2); a ledger path
  that is relative or under the checkout or `WORKTREES_ROOT` (F2, F8); a
  `routing_table` id that is no SHADOW-HUB `## BUILDERS` row and not
  `claude-opus-5-5`, and `claude-sonnet-5-5` as a builder (F6); a file
  without `retire`, or a `retire.set_sha256` that is not set ROUTE's sha256
  (F10). `carried_spend` is filled from trial.yaml, never written here.
- `RoutingTable` — his R1532 table (`source: "ruling: …"`); `sha256()` is the
  table's version on every decision row.
- `launch_sha(repo, path)` — the commit that launched a card's build (ASK
  DESK 9): the last commit of the card file whose `TIP:` header is empty.
- `load_card(repo, path, *, launch=None)` → `CardText` — the card at that
  commit, never the working copy; the header lines `TIP:`, `REPORT:`,
  `CHECK REPORT:`, `BAND:`, `MODEL:` are removed (fold F4); `BAND:` is kept
  apart as `card_band`, never sent. `rows` is the `## ROWS` row count.
- `score(card)` — the frozen complexity index (`[F-11]`): R from rows, S from
  `RESTARTS:`; M, X, H and $ are UNKNOWN (no card field states them), so
  `score_band` is UNKNOWN.
- `Router(cfg, transport=None, ledger=None, pricing=None)` — a subclass of
  `OpenRouterClassifier`: the same transport, guards, spend ledger and key
  path. `route(card)` makes ONE keyed call through `_send` (no retry) and
  writes ONE decision row (`RouteDecision`); a `ClassifyError` becomes the
  row's `status` (`status_of`). The model is code's: `unsure` → the `high`
  row (`rule_path: unsure-higher`), else the band's row (`rule_path:
  table`). The gates and the band's confidence are recorded and route
  nothing. `status_row(card, status, error)` writes a no-call row.
- `run_batch(router, cards, *, wall_clock_s)` — fold F9: every failure a
  row; after an `auth_error` no further call; at the wall clock the cards
  left get `timeout` rows.
- `closed_cards(repo, day)` — the cards whose `CHECK REPORT:` file ends in a
  `CHECK DONE` line, that file last committed on `day` (ASK DESK 16).
- `write_outcome(repo, path, ledger, *, stage="check")` — one outcome row
  from the `CHECK DONE` line (`held`, `fixed`, `held_unfixed`, `open`,
  `pass`, `ready`, `tokens`), `opus_own_held` from the check's `O<n>` rows
  HELD, `fix_rounds` = passes − 1; `builder` from the launch record
  (BUILD-HUB `--model`, or a shadow card's SHADOW-HUB row); `re_passes`,
  `suites_first_run`, `deploy_attempts` null (no committed reader yet).
  Nothing before the check closes; the decision row is never touched.
- `weekly_read(rows, cfg, *, week, spent=None)` / `write_read(text, out_dir,
  week)` — aggregates only (no card path, no launch sha): per set and JEV
  band × builder, `n=<int> insufficient data` under 30 (L8); G4, G5, G6, G7;
  the retire comparison counts only rows of `retire.set_sha256` dated on or
  after `retire.declared`. It retires nothing.
- `add_route_parsers(csub)` — `cobalt classify route (--card <path>… |
  --day <YYYY-MM-DD>) (--dry-run | --run) [--reps n] [--repo <dir>]` and
  `cobalt classify route-read --week <YYYY-MM-DD> [--out-dir <dir>]`.
  `--dry-run` prints one `ROUTE DRY card=…` line per card and a `ROUTE DRY
  TOTAL cards=<n> calls=<n>` line; zero network. `--run` is KEYED and
  METERED and waits for his yes on the wrapper (fold F12).

## Laws it carries
- **L10**: ROUTE's identity is its sha256; a wording change is a new set.
- **L35**: code computes the model, the counts and every figure.
- **L8**: no figure for a cell under n=30.
- **L32 / decision 5**: no row holds card text.

## What it never does
Holds a key, launches a seat, edits a card or a hub, opens a database or
the vault, or retries a call.

## 2026-10-15 — jev-shadow-1015
New module (card 591 rows J1, F4-F11, F1).

## 2026-10-15 — jev-shadow-1015 check
`cmd_route`: a card `load_card` cannot read is an `invalid` row (`Router.unloaded_row`), never a crash of the batch (O1). `weekly_read`: one check-stage outcome per decision (O3); the G4 `rows_band` median only at n ≥ 30 (H1). `write_outcome`: a shadow line's `held: <n> (opus-own … · house …)` parses as `<n>` (O6).
