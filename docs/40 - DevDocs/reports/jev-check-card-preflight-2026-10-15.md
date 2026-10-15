# Preflight of card 603 `jev-shadow-1015` (CHECK) — 2026-10-15

Read only. No keyed call, no key read, no git write.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt ls-files --error-unmatch <603 card>` · `git status --short -- <card>` · `git diff HEAD --stat -- <card>` | tracked; status and diff both empty; last commit `687f3a78` | OK |
| 2 | `grep -n -F "FILL" <card>` | nothing (no placeholder token) | OK |
| 3 | header vs CARD.md check column | `JOB` `LADDER` `BRANCH` `WORKTREE` `BASE` `TIP` `REPORT` `CHECK REPORT` `HOUSE B` `RULINGS` all present (`DB` optional, left out). `HOUSE A: grok` is not a CARD.md key (see N2) | OK |
| 4 | `tail -n 2 <build report>` | last line `BUILT · job: jev-shadow-1015 · tip: d0fdd674 \| on d601b1f6 … self-check: 3 of 3 …`. It is the same text the card quotes in RECORDS | OK |
| 5 | `git -C … diff --stat d0fdd674 f298a7bf` | `jev-shadow-build-2026-10-15.md` +224 and `.result` +15 only; 2 files, 239 insertions | OK |
| 6 | `git -C … log --oneline -6 feat/jev-shadow-1015` | `f298a7bf` · `d0fdd674` · `06e016b2` · `1f71790c` · `d601b1f6` — as the card's RECORDS list them | OK |
| 7 | anchors at the tip, `collector.py` | `:182` `except OverflowError:` · `:304` `Path(cfg.spend_ledger)` · `:307` `carried=[c.cost_usd …]` · `:584` `def _send` · `:594` `self.ledger.check(OVERRUN_FACTOR * projected_usd, calls=1)` | OK |
| 8 | anchors, `ledger.py` | `:41` `OVERRUN_FACTOR = 10` · `:64` `spent` · `:67` `calls` · `:72` `check` · `:110` `record` · `:123` mkdir · `:130-131` open and write | OK |
| 9 | anchors, `config.py` (classify) | `:48` `WORKTREES_ROOT` · `:134-135` `spend_ledger`, `carried_spend` · `:139-142` validator · `:320` `host_ledger_path` | OK |
| 10 | anchors, `route.py` | `:77` `DROPPED_HEADERS` · `:354` `load_card` (`:363` filter) · `:394` `status_of` · `:703` `router.body(router.qset, router.item(card))` · `:710` `ROUTE DRY` · `:689-690` `write_read` · `:739-744` `cmd_route_read` · `:751`, `:762` the two parsers. The ledger append is `:473-475`, the card says `:474-476` (one line out, harmless) | OK |
| 11 | anchors, yaml and `src/cobalt_agent` | `route.yaml` `:22` `:26` `:28` `:31` `:46-47`; `trial.yaml` `:46` `:49` `:54`; `config.py:597` `if key_name.lower() == "openrouter_api_key":`; `llm.py:112` closed branch; `configs/config.yaml` `:57` `:61` `provider: "openrouter"`, `:78` `active_profile:` | OK |
| 12 | anchors, writers | `trial.py:170-172` · `cli.py:53-54`, `:104-105` · `route.py:689-690` — all as the card says | OK |
| 13 | test anchors, `grep -n -E "def test_" test_jev_shadow_1015.py` | 49 defs (the card's 49). Every test name the rows cite exists (D2, F13 ×5, F2 ×4, F3 ×2, J1 ×3, F4 ×3, F5 ×5, F6 ×3, J2 ×2, F7 ×3, F8 ×4, F9 ×5, F10 ×3, F11 ×3, F1 ×2, F12 ×1). `:420-423` (4.9999, `projected_usd=0.00002`, `stub.calls == []` at `:424`), `:734` `_batch`, `:763` `_spend_file(tmp_path, 4.99999)` match | OK |
| 14 | R1 recount, `-card.md` names of `prompts/2026-10-0[6-9]` and `2026-10-1[0-3]` by `ls` | 17 + 8 + 12 + 22 + 18 + 23 + 20 + 27 = 147, which `route.yaml:27` and `:29` name. `147 × 10 = 1470`, `2 × (147 + 11 + 100) + 2 = 518` | OK |
| 15 | 591 row coverage by id | 591 rows: Z0 P0 D2 F13 F2 F3 J1 F4 F5 F6 J2 F7 F8 F9 F10 F11 R1 F1 F12 R2 (20). 603 holds the same 20 ids. X0a-f are present as RUNs, each saying "quote the output" | OK |
| 16 | houses told to read 591 | `## READ` names 591 whole. No line says it is staged for the houses (see N3) | OK |
| 17 | keyed call or key read in the card | `## NOT IN THIS JOB` and the WHY forbid both. Every run is a stub or no transport. No `--run`, `probe`, `discover`, vault open or `.env` read among the RUN commands (F12) | OK |
| 18 | RESTARTS, from the tip's `jobs.yaml` and the `uv run cobalt jobs restarts d601b1f6..d0fdd674` table | Card line `com.cobalt.agent com.cobalt.aset com.cobalt.radar`. `config.py` maps to agent+aset+radar, `llm.py` to agent, `cli.py` to radar, `classify/*` to none. The tip's `jobs.yaml` classifies `trial.yaml` and `route.yaml` under `no_resident_reads` (reader `com.cobalt.generated`), as R2 says. My own run from `/Users/cobalt/cobalt` printed the three extra labels herdr, mainframe, obsidian, because `main` lacks those two classifications (see N4); that run does not contradict the card | OK |
| 19 | Z0 covers aset | Z0 names the three services, says "`com.cobalt.aset` is not in [the report's table]: read what `aset` imports from `cobalt_agent`", and wants the model and provider per role | OK |
| 20 | stop-line shape | The card holds none (CARD.md forbids it). The `BUILT ·` line it quotes matches CHECK-HUB `## PREFLIGHT` (`BUILT · job · tip … self-check: 3 of 3`). The card has no shadow marker, so the CHECK DONE shape is CHECK-HUB's | OK |
| 21 | allow line, `grep` rows | Z0, X0b read and P0 `git diff` are `grep *` and `git diff *`; X0a `uv run pytest *`; R2 `uv run cobalt jobs restarts *`; X0f `sh /Users/cobalt/cobalt/ops/desk/*`; X2 `ls` is marked `ASK DESK` | OK |
| 22 | X0c command, run as written: `grep -rn -c -E "write_text\|\.write\(\|\.open\(\|mkdir" src/cobalt/classify` | all 8 files `:0`. The same search for `-F "write_text"` finds `route.py:1`, `cli.py:2`. The `\|` is a literal pipe in this `grep`, so the command finds no writer. CHECK-HUB also bans `\|` and wants one fixed string per call | **FAIL** |
| 23 | X0d, "a small driver" for `Router.body` on a tmp git repo | Needs a Python process. `uv run python` is not on the allow line, no pytest-file shape is carded, and the row is not marked `ASK DESK` (R411, R412) | **FAIL** |
| 24 | X0e, `uv run cobalt classify route-read …` and the two-row driver | `uv run cobalt classify …` is not on the allow line (only `uv run pytest *`, `uv run cobalt jobs restarts *`, `COBALT_ENV=dev uv run cobalt db *`). The two-row driver is also a Python process. Neither is marked `ASK DESK` | **FAIL** |

## ISSUES

- F1 (check 22) X0c: `\|` finds nothing, so the writer list comes back empty. Replace it with fixed-string greps, one per call: `-F "write_text"`, `-F ".open("`, `-F "mkdir"`, `-F ".write("`. The listing in checks 8, 11 and 12 shows the expected writers.
- F2 (check 23) X0d: name a runnable shape inside the allow line, e.g. a throwaway pytest file under the worktree run with `uv run pytest -q -rA -p no:cacheprovider --color=no <file>`, or mark the row `ASK DESK`.
- F3 (check 24) X0e: `uv run cobalt classify route-read` is off the allow line. Mark it `ASK DESK` with the safe default (a pytest-file driver that calls the CLI's `cmd_route_read`), or the check records `REFUSED, not needed`. A pytest-file driver also covers the two-row ledger.
- N1 P0: the row's command `git diff f4e8de85 d0fdd674 -- <each ported path>` over `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` shows main's drift (132 and 36 lines), not the trial's hunk. For those two use `git diff d601b1f6 d0fdd674` (I read it: `cli.py` +2, `cli.md` +11, `test_classify_door.py` +389). For the classify tree, `f4e8de85..d0fdd674` is right (`ops/run_classify_trial.sh` shows as deleted vs `f4e8de85`, i.e. not ported, as carded).
- N2 Header: `HOUSE A: grok` is not a CARD.md or CHECK-HUB key (only `HOUSE A: OpenAI — …` and `HOUSE A: none — …` are). It is harmless. Per SEAT ORDER, house A is the first house UP (Grok first), so the line changes nothing.
- N3 X10 asks for both houses ("house B for the money, the $5 cap, R921"), but the header says `HOUSE B: as needed`, and CHECK-HUB makes house B needed only for `mandatory — vault notes|sizing`. As written, house B is none (money is not a listed reason). The desk should either accept that or change the header. Neither blocks the launch.
- N4 R2 must be run from the worktree (the check's cwd). `main`'s `jobs.yaml` lacks the two `no_resident_reads` rows, so a run from `/Users/cobalt/cobalt` prints `UNCLASSIFIED CONFIG` and a six-label RESTARTS line. I could not run it in the worktree (not on this seat's allow line), so the three-label result rests on the tip's `jobs.yaml` and the table's per-path rules.
- N5 R2 and the tip: head `f298a7bf` is docs-only past `d0fdd674` (check 5), so the code the houses read is the BUILT tip's.
- N6 The 9 `tests/test_llm.py` reds are carded as a RECORD, not a finding, and I did not run them (no test is run by this preflight).

**Blocks the check launch:** F1, F2 and F3. Each is a command the check cannot run as written (a search that matches nothing, two off-allow-line runs not marked `ASK DESK`). N1-N4 do not block.

PREFLIGHT DONE · card: jev-shadow-1015-check · checks: 24 · fails: 3 · ready: NO
