# Preflight — card 994 x15-hitl-probe-port (read-only)

Run 2026-10-21 16:03 EDT (`date`). Reads only; nothing run, no git write. `git rev-parse --short=8 HEAD` → `7d15fbb5` (BASE `e88edfef` trails main by desk commits; the desk resets it at launch, not a fail).

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header read (card 994 `:1-14`) | JOB `x15-hitl-probe-port`, BRANCH `ops/x15-hitl-probe-port`, WORKTREE `x15-hitl-probe-port`, BAND HIGH, CLASS `K2 serving K4`, INSTALL none, RESTARTS `com.cobalt.aset com.cobalt.cos com.cobalt.radar`, RULINGS `2026-10-18 R1863`, TIP empty | OK |
| 2 | `ls /Users/cobalt/cobalt-wt/` | no `x15-hitl-probe-port` (fresh); `x15-hitl-probe` present | OK |
| 3 | no migration | no migration row, no plist, no database row in the card; INSTALL none | OK |
| 4 | RULINGS: `grep -n -F R1863 cto-2026-10-18.md` | `:90` `R1863 … HIS RULING · APPROVED`; card 977 header carries the same value | OK |
| 5 | brain RECORDS line: `grep` of card `:74` | `977 refused on a cli.md trial-merge conflict → fresh PORT (HIGH, PROOF vs c1b4b785) … brain 9b07db5a 2026-10-21`; desk rows R2321, R2322 at `cto-2026-10-21.md:15-16`, R2285 `:52` (LADDER) | OK |
| 6 | `git diff --stat 41804777 c1b4b785` | 9 files, 627+, 6−; seven spec files: `web.py 37`, `hitl/cli.py 34`, `test_hitl_x15.py 267`, `test_s3_c3_panel_offline.py 2`, `aset/web.md 4`, `hitl/README.md 3`, `cli.md 3` = card E1 (c) list; numstat 33/4, 33/1, 267/0, 1/1, 4/0, 3/0, 3/0 = 344+, 6− | OK |
| 7 | `git diff --stat 41804777..main --` the seven spec paths | `docs/40 - DevDocs/cobalt/cli.md | 3 +++` only; the other six unchanged | OK |
| 8 | `git diff 41804777..main -- cli.md` | `@@ -149,3 +149,6 @@`: a blank, `## 2026-10-21 — f5-probe`, the `checkpoints_cli.add_parser(sub)` line (3 `+`, no `-`); the spec's hunk is the same `@@ -149,3 +149,6 @@` with `## 2026-10-21 — x15-hitl-probe` / `hitl_cli.add_parser(sub)`; card D2 keeps both (main's first, spec's appended), E1 (b) allows only main's 3 lines | OK |
| 9 | `git grep -n -F '@app.get("/hitl' main -- web.py` | `:1436` `/hitl`, `:1451` `/hitl/{row_id}`; `grep -n hitl_list|def hitl_detail` → `:1437`, `:1452` (`hitl_detail(row_id: int)`): card's `:1436`, `:1451`, probe path → 422 hold | OK |
| 10 | `BASE_ROUTES` in `test_s3_c3_panel_offline.py` | `main:…:57 BASE_ROUTES = [`; spec hunk `@@ -58,7 +58,7 @@` changes line 61 (`"/hitl", "/hitl/{row_id}", …` → adds `"/hitl/x15-probe"`) = card T1's `:61`, found by content | OK |
| 11 | builder commands vs `BUILD-HUB.md:14`, `:16` | `:14` allows `Edit(//Users/cobalt/cobalt-wt/**)` (governs Write, `:16`), `git show*`, `git diff *`, `uv run pytest *`, `uv run cobalt jobs restarts *`, `git add/commit`; `:16` never types `git checkout`, `git merge`, `rm` but the .env string. Card rows use only Edit/Write, `git show`, `git diff`, `uv run pytest`, `uv run cobalt jobs restarts`; `git apply`, `cherry-pick`, `git mv`, `rm`, `mv` appear only in prohibitions (`grep -n -o`: card `:18`, `:38`, `:83`) | OK |
| 12 | DEPLOY PROOF before 1: `git grep -c -F "def _hitl_key_script" main -- web.py` | no match (0); after: `c1b4b785` → `1` | OK |
| 13 | DEPLOY PROOF before 2: `git grep -c -F '@app.get("/hitl/x15-probe"' main -- web.py` | no match (0); after: `c1b4b785` → `1` | OK |
| 14 | DEPLOY PROOF before 3: `git grep -c -F 'add_parser("x15-send"' main -- hitl/cli.py` | no match (0); after: `c1b4b785` → `1` | OK |
| 15 | smoke reads vs `DEPLOY-HUB.md:11` | admits `Bash(curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*)`; card's two reads are `…ts.net/hitl/x15-probe` and `…ts.net/`; `grep -n -o` of `127.0.0.1:5010` in the card → `:52`, `:69`, `:80` only (CHECK ASK X4, DECISION 3, RECORDS), none in `## DEPLOY PROOF`; no `uv run` line in that section | OK |
| 16 | `ops/desk/deploy-card.sh:567-577` | `## DEPLOY PROOF` non-blank lines: a line with `· before ` and `· after ` is a marker (the three greps match), any other a smoke read (the two `curl` lines; the probe line's `(before the deploy …` has no `· before `); nothing refused, no `«FILL` | OK |
| 17 | E1 rows, one per file: T1 `test_hitl_x15.py` 267, C1 `web.py` 33+/4−, C2 `hitl/cli.py` 33+/1−, D1 `aset/web.md` 4 and `hitl/README.md` 3, T1 `test_s3_c3_panel_offline.py` 1+/1−, D2 `cli.md` | card E1 (a) six paths print nothing (none changed on main, check 7); (b) `cli.md` prints only main's 3 f5-probe lines, named against `git diff 41804777 <BASE> -- cli.md`; (c) counts equal check 6; (d) names the four code/test paths (main's four f5-probe files are not spec paths, so a `<BASE>..<tip>` diff names only the four) | OK |
| 18 | RESTARTS homes: `git grep -n imports: main -- configs/cobalt/jobs.yaml` | `:99` aset `[cobalt.aset.__main__, cobalt.aset.web]`, `:203` radar `[cobalt.cli]`, `:226` cos `[cobalt.cos.run]`; check report `:186`, `:202`, `:264` last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` = card header (card 977 header held aset radar; cos added from the check's tool line, DECISION 2). `DEPLOY-HUB.md:93-94`: cos skipped when `launchctl print` finds it not loaded, FAIL if loaded | OK |
| 19 | RED test first (card T1) | Ported first, before C1/C2; RUN on BASE's `src/`, quoted whole; five reds named by reason (`_hitl_key_script` AttributeError, `/hitl/x15-probe` 422, `hitl-k-state` absent, `invalid choice: 'x15-send'`, the one-block route test); T1 lists `test_hitl_x15.py`, `test_s3_c3_panel_offline.py` | OK |
| 20 | card committed, empty diff: `git diff --stat -- <card>`; `git log --oneline -2 -- <card>` | diff empty; `b19d5560 docs(desk): X15 port card 994, drafter report, preflight prompt 995, R2325` | OK |
| 21 | `git diff --stat main --` `BUILD-HUB.md`, `DEPLOY-HUB.md`, `deploy-card.sh`, `jobs.yaml` | empty: the on-disk lines read above are main's | OK |
| 22 | what blocks the card's own build | nothing: the spec paths are unchanged on main but `cli.md`; no file outside the seven; no migration, no lock, no live send | OK |

## ISSUES
- NOTE 1: `RULINGS: 2026-10-18 R1863` is the card 977 value and its `cto-2026-10-18.md:90` row reads `HIS RULING · APPROVED` for the Gemini ask; the preflight does not re-decide it (copied, card DECISION 4).
- NOTE 2: HEAD is `7d15fbb5`, BASE `e88edfef`; the delta is desk commits, none on a spec path (check 7); the desk resets BASE at launch.
- NOTE 3: `git grep -c` prints nothing for a zero count; checks 12-14 read that as `0` (the card's `before 0`).
- NOTE 4: the cos restart depends on the hub's NOT LOADED read (`DEPLOY-HUB.md:94`): if card 929 loads cos before the deploy, STEP-R FAILS until the desk adds cos's strings via R60 (card DECISION 2, not a build blocker).
- NOTE 5: `deploy-smoke.sh` does not map the https reads (card DECISION 3); the same form ran on the 965 deploy.

PREFLIGHT DONE · card: x15-hitl-probe-port · checks: 22 · fails: 0 · ready: YES
