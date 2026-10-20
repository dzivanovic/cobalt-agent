## §0
- Card 877 as port `cos-probe-fr1` is ready: every check holds; 0 fails, 3 notes.
- The five files are untouched by main since `07eb89a3`; `cli.md` is the one seam (+3 lines, f16-close-1018). Only the F5 deploy blocks the build.
- Read-only: git, the card, the hub launch line, `jobs.yaml`, `gate-lists.md`; nothing run, nothing written but this report.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --name-only 07eb89a3 8f47d85b` vs the card's PORT file list | `cli.md`, `cos/README.md`, `cos/cli.py`, `cos/probe.py`, `test_cos_probe.py`, `test_hitl_offline.py` = the card's 6, no report | OK |
| 2 | `git diff --shortstat 07eb89a3 8f47d85b` | `6 files changed, 919 insertions(+), 1 deletion(-)` = the drafter's 919 / 1 | OK |
| 3 | `git diff --numstat 07eb89a3 8f47d85b` vs PORT counts | probe.py 458, test_cos_probe.py 419, test_hitl_offline.py 18, cli.md 3, README 3, cos/cli.py 18/1 = the card's 458 / 419 / 18 | OK |
| 4 | `git diff --stat 07eb89a3 main -- <the six>` (PROOF lines) | only `cli.md`, 3 insertions; the other five empty (byte-equal to `8f47d85b` after the port) | OK |
| 5 | `git diff 07eb89a3 main -- cli.md` vs `git diff 07eb89a3 8f47d85b -- cli.md` | main: blank + `## 2026-10-19 — f16-close-1018` + the `cobalt validate` line, after f21-genesis; branch: blank + `## 2026-10-19 — cos-probe-1019` + the `cos_cli.add_parser(sub)` line, same anchor = the card's seam and resolution | OK |
| 6 | `git grep -n "^## 20"` on `main` / `8f47d85b`, `cli.md` | main ends f16-close-1018 `:144`; branch ends cos-probe-1019 `:144`; both after f21-genesis `:141` | OK |
| 7 | `git diff --name-only f1196d2b main` (BASE drift) | the card, prompt 898, `cto-2026-10-20.md`, the drafter report: docs only; main now `2fc9c55c`, BASE `f1196d2b` trails it | OK (NOTE 1) |
| 8 | header JOB / BRANCH / WORKTREE / REPORT / CHECK REPORT; `git branch --list "ops/cos-probe*"`, `git worktree list` | `cos-probe-fr1` · `ops/cos-probe-fr1` · `cos-probe-fr1` · `…cos-probe-fr1-build-2026-10-20.md` · `…cos-probe-fr1-check-2026-10-20.md` agree; only the old `ops/cos-probe-1019` and `cos-probe-1019` exist, no collision | OK |
| 9 | header BAND / TIP / CLASS | `BAND: HIGH`; `TIP:` empty; `CLASS: K2` | OK |
| 10 | `grep -n -F "«FILL"` over the card | no match | OK |
| 11 | `grep -n -F -e "--no-db"` over the card | one hit, `:73` (RECORDS: "no `--no-db` spelling in the card", prose); no smoke read | OK |
| 12 | PORT is ONE row | one `\| PORT \|` row; P1, P2, A1, X20, R1, D0 stated as content, not rebuilt | OK |
| 13 | deploy allow list: `prompts/DEPLOY-HUB.md:11` launch line | admits `uv run pytest *`, `COBALT_ENV=production uv run cobalt validate`, `grep *`, `ls *`; no `cobalt cos probe`, no `claude` | OK |
| 14 | marker 1 `ls …/cos/probe.py` | main: `No such file or directory` (before); `8f47d85b:src/cobalt/cos/probe.py` is 458 lines (after) | OK |
| 15 | marker 2 `grep -c -F "def test_x20_redact_keeps_the_card_fragment_key" …/test_hitl_offline.py` | main: `0`; `8f47d85b`: `1` | OK |
| 16 | marker 3 (mount) `grep -c -F 'csub.add_parser("probe"' …/cos/cli.py` | main: `0`; `8f47d85b`: `1` (`:37`, `probe = csub.add_parser("probe", …`); main has only the `run` parser `:20` | OK |
| 17 | smoke read `uv run pytest -q tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` | admitted by `Bash(uv run pytest *)`; no `--no-db`, no `cobalt cos probe --help` | OK |
| 18 | `ops/desk/gate-lists.md` `## OFFLINE` vs the card's PORT | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; the card says "as written, whole" without restating it | OK |
| 19 | K10 RESTARTS: `jobs.yaml` `:203` radar `imports: [cobalt.cli]`, `:226` cos `imports: [cobalt.cos.run]`; `main:src/cobalt/cli.py:87` `cos_cli` import, `:574` mount | `cos/cli.py` and `cos/probe.py` reach only radar; cos.run does not import `cos.cli`; header `RESTARTS: com.cobalt.radar` | OK (NOTE 2) |
| 20 | CHECK ASKS: old X1-X5 (`7bb031e4` card) vs now | X1-X5 identical, plus P1 (PORT PROOF), P2 (shared seam with F5 731 `cli.md`, re-read by content), P3 (merge-base) | OK |
| 21 | shared files with F5 card 731 (`731-f5-card.md` header BASE `bd5dd70a`, `ops/f5-checkpoints-fr1`) | 731 names `cobalt/cli.md` (row D0 and PORT (2): "F5's section goes after the last section on main at the build"); no `cos/cli.py`, `probe.py`, `cos/README.md`, test files of this card | OK |
| 22 | drafter decision 1 (BASE = main HEAD at drafting; builder takes HEAD at launch, desk updates header) | right: the prompt allows BASE trailing main; docs-only drift (check 7), the desk resets BASE after the F5 deploy | OK |
| 23 | drafter decision 2 (mount smoke is a `grep -c -F`, not `--help`) | right: `--help` is not on the hub line; the real mount is pinned by `test_the_probe_is_mounted_and_lists_the_seven_items` in the suite of check 17 | OK |
| 24 | `git diff HEAD --stat` over the card, prompt 898, the drafter report | empty (committed, unchanged) | OK |
| 25 | what blocks the card's own build | the F5 port (`f5-checkpoints-fr1`, 731) DEPLOYED, then the desk resets `BASE`; no branch or worktree collision, the five files are clean on main | OK |

## ISSUES
- NOTE 1: `BASE: f1196d2b` trails main (`2fc9c55c`) by docs commits only; the desk resets it to main HEAD after the F5 deploy (prompt 898, drafter decision 1).
- NOTE 2: the header names `com.cobalt.radar` only. `cos/cli.py` is reached only via `cobalt.cli`; the builder's `jobs restarts` line (row R1) is the record, and the check should expect radar alone (cos does not import `cos.cli`).
- NOTE 3: both cards append to `cli.md`'s end. Whichever lands second re-finds the last section by content (CHECK ASKS P2). F5's own section shifts the anchor, but the card's PORT keys on the f16-close-1018 line by content, not on a number.

PREFLIGHT DONE · card: cos-probe-fr1 · checks: 25 · fails: 0 · ready: YES
