# f5-probe-x4-fix — card 989 preflight (prompt 991)

## §0
- Card 989 is ready to build. Nothing blocks it.
- Every `file:line` I checked holds on main `63354cf2`. The card is committed and `git diff HEAD` on it is empty.
- The cause (a) holds by the code: `_scratch` chdirs into `f5-probe-` (`:119`, `:357`) and the old tree resolves against the cwd.
- Four NOTEs below; none is a FAIL.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 HEAD` / `main` | `63354cf2` / `63354cf2`; card BASE `956167fa` is one desk commit behind | OK (NOTE 1) |
| 2 | `git diff --stat HEAD -- <card>`; `git log --oneline -2 -- <card>` | empty; `63354cf2 docs(desk): card 989 f5-probe-x4-fix drafted, preflight prompt 991` | OK |
| 3 | header read: JOB `f5-probe-x4-fix`, BRANCH `ops/f5-probe-x4-fix`, WORKTREE `f5-probe-x4-fix`, BAND HIGH, CLASS K2, RESTARTS `com.cobalt.radar`, RULINGS `2026-10-18 R1863`, MIGRATIONS none, CHECK REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-x4-fix-check-2026-10-21.md` | all present; same shape as card 973's header | OK (NOTE 3) |
| 4 | `git rev-parse --verify --quiet ops/f5-probe-x4-fix`; `ls /Users/cobalt/cobalt-wt/` | branch exit 1 (absent); no `f5-probe-x4-fix` dir (`f5-probe` exists) | OK |
| 5 | `grep -c -F "F5 gate pass 2 — X4 fix round (fresh job, HIGH, red test of the cause, no live screener) — brain 9b07db5a 2026-10-21" <card>` | `1` | OK |
| 6 | `git grep -n main -- checkpoint_probe.py` | `REPO_ROOT :58`, `KEEP_ROOT :60`, `_scratch :119`, `_real_figures :182`, `_prompts :215`, `_x4 :274` (`_real_figures` call `:276`), `_verdict :351`, `with _scratch() :357`; no `X4_` name, no `_at_repo` | OK |
| 7 | `git grep -n main -- checkpoints.py cli.py` | `GroupsShapeError :136`, `parse_groups :200-221`, `fetch_groups :224`, `fetch_figures :242`, `check_demand :582`, lazy import `checkpoint_probe :844`, `cli.py:91` | OK |
| 8 | `git grep -n main -- cobalt_agent/config.py` | `Path.cwd() / "configs" :543`, `Path(__file__).parent.parent / "configs" :544`, `Config directory 'configs/' not found :549` | OK |
| 9 | `git show main:src/cobalt_agent/security/vault.py` | `vault_path="data/.cobalt_vault" :19` (relative); `:30-34` a missing file unlocks an empty vault | OK |
| 10 | `git grep -n main -- finviz_api.py aset/prefill.py market.py` | `VaultManager(vault_path) :100`, default at `:93`, `Missing API token in vault :232`; `aset/prefill.py:37-38` `resolve_token` → `FinvizApiClient()`; `market.py:64` calls `resolve_token` | OK |
| 11 | `git grep -n main -- test_checkpoint_probe.py` | `world :62`, X4 tests `:326`, `:342`, `:368`, `:384`; SPY `500.00`/`0.10` at `:375`; `KEEP_ROOT` monkeypatch pattern at `:193`, `:243` | OK |
| 12 | `git grep -n main -- jobs.yaml` | radar `:193`, `imports: [cobalt.cli] :203`; checkpoint one-shots `:258-284`, not resident | OK (matches the header's RESTARTS) |
| 13 | `git ls-tree --name-only main tests/cobalt/fixtures/checkpoints/` | `groups_sector_v140.csv` only: row (b) fixture absent, so the `NOT RUN — no real Groups body` path is the real state | OK |
| 14 | `git grep -c -F "def _at_repo"` / `"X4_GROUPS_KEPT = "` / `"def test_fr3_x4_reaches_no_finviz"` on main, DEPLOY PROOF files | no match for any (count 0, `git grep -c` prints nothing, exit 1) = card's `before 0` ×3 | OK |
| 15 | `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist`; `ls …/checkpoint_probe.py` | both listed (exit 0) | OK |
| 16 | `deploy-smoke.sh` mapping (`:10-12`, `:118-136`) | maps `ls`, `grep -c -F`, `curl http://127.0.0.1:5010/` only. The card's smoke reads are `ls` forms, as card 973's, with no 127.0.0.1 read | OK |
| 17 | BUILD-HUB `:14`, `:16` vs the card's commands | ORDER uses `uv run pytest -q -p no:cacheprovider --color=no …` and `uv run cobalt jobs restarts <BASE>..HEAD`, both listed strings. No `git mv`, `rm`, `mv`, network or production command. FR-3's test patches `check_demand`, `fetch_figures`, `fetch_groups`, `fetch_market_table`, `resolve_token` to raise, so no live Finviz call | OK |
| 18 | FR-1 is first, K25 | FR-1 test is written before any `src/` edit and says which cause (a, the scratch cwd). Its RED message names `cobalt_agent/config.py:543` (verified). It falls back to UNPROVEN and still builds FR-3 if it cannot go red | OK |
| 19 | X4 without a live screener (FR-3 vs `_x4` `:274-276`, `parse_groups` `:200-221`) | `_x4` stops calling `_real_figures`; sectors come from `parse_groups` on a read-only file with `#` lines dropped; `parse_groups` raises `GroupsShapeError` on a non-11 body (message holds "not the 11 sector rows") | OK |
| 20 | `X4_INDICES` labelled constructed (L32) | the PROBE clause prefix is `groups: <source name> · indices: constructed · `, with names only and no figure or path; the tests' `\d\.\d` no-figure pin (`:390`) stays | OK |
| 21 | `files` vs RESTARTS classes (K10) | `checkpoint_probe.py` → radar at most (lazy import `:844`, `cli.py:91`); `test_checkpoint_probe.py` → test; `checkpoints.md` → DOCS. All three are in the card's `## RECORDS` | OK |
| 22 | old-tree files from drafter decision 2 | `cobalt_agent/*`, `aset/prefill.py`, `market.py`, `checkpoints.py` are not in any row's `files`; all four are in `## NOT IN THIS JOB` | OK |
| 23 | `## DEPLOY PROOF` form vs CARD.md and card 973 | three marker lines with `· before` / `· after`, two smoke lines; same shape as 973 | OK |
| 24 | D0 target `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` | exists; last section `## 2026-10-21 — f5-probe` at `:76`; `cli.md` correctly left alone | OK |
| 25 | other tests that run X4 through `world` | `test_checkpoint_probe.py:141` (X4 expected `OK`) and `:454-460` (`X4 OK 0`, `X4 FAIL 1 all_invalid`) are not among the four tests the card names | OK (NOTE 2) |

## ISSUES
- NOTE 1: BASE `956167fa` trails main `63354cf2` by one desk commit (the card's own). The desk resets BASE at launch.
- NOTE 2: after FR-3, X4 prints `NOT RUN` (exit 3) unless a Groups body is present. Two existing tests besides the four the card names expect X4 `OK`: `test_checkpoint_probe.py:141` (the all-items verdicts test) and the `X4 OK` / `X4 FAIL` rows of `test_each_item_prints_one_line_and_exits_by_verdict` (`:454-460`). The card's whole-suite `0 failed` gate catches both, and both sit in a file the rows may touch. The builder gives them the shared kept-file fixture. Not a blocker.
- NOTE 3: `MIGRATIONS: none` is a deploy key in CARD.md, not a build key. Card 973 omitted it. This is the drafter's decision 5 and is harmless.
- NOTE 4: FR-3 says to change "P2's live cost" text. In the module that text is only the docstring's X4 line (the live-cost sentence is in card 973's P2 row, not in the module or docs). The builder updates the docstring's X4 line and D0 says X4 now spends 20 model calls and no Finviz GET.
- Blocks the card's own build: nothing.

PREFLIGHT DONE · card: f5-probe-x4-fix · checks: 25 · fails: 0 · ready: YES
