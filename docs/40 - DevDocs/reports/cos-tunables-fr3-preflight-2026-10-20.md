# Card 933 FR-3 amend — preflight (read-only), 2026-10-20

Branch tip read: `ops/cos-tunables` = `af878860` (one docs-only commit past `ace7a92a`: it adds only `reports/cos-tunables-build-fr1-2026-10-20.md`). HEAD = `e701d3ee`. Nothing run, no GET made.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <933 card>`; `git ls-files --error-unmatch` | empty diff; file tracked | OK |
| 2 | `git log c98c28f5..ops/cos-tunables`; `git show --stat af878860` | 6 commits; tip `af878860` touches one report file, so FR-1/FR-2 files are unchanged by it | OK |
| 3 | `git show ops/cos-tunables:configs/cobalt/taxonomy/tunables.yaml` | row `key: hitl.page_base_url` `:1038`, `value: null` `:1039`, comment `:1035-1037` ("null until ruled; the card refuses to send while it is"), `unit: label`, `status: proposed`, `source: dwv`, `consumers` — all as the card says | OK |
| 4 | `git grep -c -F "DEFAULT (brain; his word may change it)"` on the tip | `2` (`:1009`, `:1027`); the new row carries none, so marker 2 stays 2 | OK |
| 5 | `git grep -c -F "cobalt.taild24291.ts.net"` in `tunables.yaml` on the tip | no match (0); the DEPLOY PROOF "before `0` · after `1`" holds if the value line is the only occurrence (the re-worded comment must not spell the host) | OK (NOTE 1) |
| 6 | value string in card | `"https://cobalt.taild24291.ts.net"`, no trailing slash, same in RECORDS D14 line | OK |
| 7 | `src/cobalt/taxonomy/tunables.py` on the tip | `value: Any = None` at `:96`; `unit: label` is a `TunableUnit`; a string loads with no code change | OK |
| 8 | `src/cobalt/hitl/card.py` on the tip | `BASE_URL_KEY` `:20`; `page_base_url()` reads `load_tunables().by_key`, refuses null and non-`https://`, `rstrip("/")`; the URL passes | OK |
| 9 | `tests/cobalt/test_cos_offline.py` on the tip | `test_the_shipped_cos_rows` `:287` (was `:287-294`); uses `load_tunables().by_key`; the new `test_the_shipped_hitl_page_base_url` (value equality, `not endswith("/")`, `status.value == "proposed"`) fits that style; RED on the tip because `row.value` is `None` | OK |
| 10 | GET proof placement: BUILD-HUB `:14` allow list (`docs/40 - DevDocs/prompts/BUILD-HUB.md`) | no `curl`, no other GET command; the card makes the builder write `GET proof deferred to the deploy smoke read` | OK |
| 11 | DEPLOY-HUB `:11` allow list | `"Bash(curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*)"` is admitted; `/hitl` matches the `/*`. The card's DEPLOY PROOF line is exactly that command. Holds | OK |
| 12 | every command given the builder vs BUILD-HUB `:14`/`:16` | pytest (`uv run pytest *`), `git add/commit/diff/show/log`, `grep`, `ls`, `uv run cobalt jobs restarts *`, Edit under `cobalt-wt/**`: all admitted | OK |
| 13 | `ops/desk/desk-launch.sh` step check (`:2631-2632`) | `*[!A-Za-z0-9.\ -]*` refuse; `FIX ROUND row FR-3` has letters, spaces, `-`, digits only → passes | OK |
| 14 | RECORDS lines | fix-round line (`:71`) and D14 line (`:72`) present verbatim, plus the FR-3 drafter line (`:73`) | OK |
| 15 | `hitl/README.md:22` on the tip | line 22 reads "`hitl.request_ttl_min` and `hitl.page_base_url`: null, no value set …"; the card's dated line `## 2026-10-20 — cos-tunables fr3` is named, with files list carrying the README | OK (NOTE 2) |
| 16 | header `RULINGS:` and `reports/cto-2026-10-18.md` | `2026-10-18 R1863` unchanged; the R1863 row exists | OK |
| 17 | `## CHECK ASKS` | one check, job `cos-tunables-fr1`, covers FR-1..FR-3 (FR1 bullet + separate FR-3 bullet) | OK (NOTE 3) |
| 18 | `ls /Users/cobalt/cobalt-wt/cos-tunables` | no `SHADOW-INSTRUCTIONS.md` | OK |

## ISSUES
- NOTE 1: the re-worded comment above the row must not contain the host string, or marker `grep -c -F https://cobalt.taild24291.ts.net` reads 2. The card does not say so; builder must keep the host in the value line only.
- NOTE 2: README `:22` also says `hitl.request_ttl_min` is null (stale since T1). The card's text supersedes only the base-URL null sentence; the drafter's decision 2 (reword the whole `:22` sentence) is not in the card. Builder will leave a stale ttl claim unless the card says so. Not a blocker.
- NOTE 3: the FR1 CHECK ASK still says "scoped to FR1 with the suites"; FR-3 is covered by the separate FR-3 ask in the same job. Fine.
- NOTE 4: `src/cobalt/hitl/card.py` docstring/comment ("No house set it … while it is null") goes stale; the card forbids a `src/` change, so it stays. Not a blocker.
- NOTE 5: the tip moved to `af878860`; FR-1's byte-equality PROOF names `ace7a92a` and the builder re-runs it on its own tip. Satisfied (the tip's commit does not touch `test_sheet_daymode_probe.py`).
- Blocks the build: nothing. Worktree is clean of `SHADOW-INSTRUCTIONS.md`.

PREFLIGHT DONE · card: cos-tunables-fr3 · checks: 18 · fails: 0 · ready: YES
