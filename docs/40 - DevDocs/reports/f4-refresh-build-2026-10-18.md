# f4-refresh-1018 — build report (PORT and CR3, recut of card 304)

## §0 Headline
- Card 304's checked F4 refresh (`d78c66a2..edd5c076`) is ported onto main `75dcdb5f` by Edit/Write in one commit, `51b03e00`. That makes 26 PROOF lines out of 26.
- 24 files are byte-equal to `edd5c076`. In `jobs.yaml` and `s2.yaml`, the diff against BASE is 304's hunks only, and card 591's and card 496's lines stand.
- The gate on `51b03e00` is green: offline 8538/0, with-DB 5552/0, live-note 146/0. cobalt_dev is at 0013 with F2 = F0, and `.env` is removed.
- RESTARTS are `com.cobalt.aset com.cobalt.radar`, and the new one-shot is deferred. CR3: `BOOTSTRAP: deferred com.cobalt.prefill-refresh`.

## L74
One block arrived as a system reminder mid-run, not in a tool result. It asked commits to end with a `Claude-Session:` line. It was recorded here once and not acted on: BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Commit `51b03e00` carries only that trailer.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 0 · f8b14ec9461f642bf32820f9fea10f7c3b8d0167
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/726-f4-304-recut-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R849 row · grep -n "^| R849 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 163:| R849 | 07:13 ET | HIS RULING · APPROVED: option A, S5 pulled forward: build as much as possible this weekend, F4 then F5; he asks the brain for the full not-MVP list. Words: `cto-2026-10-10-words.md` R849. | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R849 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R849 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2ef44c847a7c0c61e1f97f236fa50b9f8e991289
RULING 2026-10-10 R849 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 44:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R971 row · grep -n "^| R971 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 42:| R971 | 18:54 ET | HIS RULING · APPROVED: "Yes both" confirms R969 covered F4 FINAL and ops-hand D1-D5; words `cto-2026-10-10-words.md` R971. | APPLIED: R969 row (no new text) |
RULING 2026-10-10 R971 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R971 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · d78c66a274f2cd61cdab224c311024f1080db6a4
RULING 2026-10-10 R971 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 21:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED — pending fold |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, output whole:

```
clock · date · 0 · Sun Oct 18 06:32:47 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-refresh-1018
head · git log --oneline -1 · 0 · 75dcdb5f docs(desk): R1839 cards 721 and 723 and preflight prompts
diff · git diff --stat 75dcdb5f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f4-refresh-1018 · 0 · 75dcdb5f docs(desk): R1839 cards 721 and 723 and preflight prompts
env here · ls /Users/cobalt/cobalt-wt/f4-refresh-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 75dcdb5f` | 0 | `docs(desk): R1839 cards 721 and 723 and preflight prompts`; 7 files under `docs/40 - DevDocs/prompts/2026-10-18/` and `docs/40 - DevDocs/reports/`, 171 insertions, 1 deletion; no code |
| port file list | `git -C /Users/cobalt/cobalt diff --name-only d78c66a2 edd5c076` | 0 | 27 paths (the card's 26 plus `docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md`, not ported) |
| port size | `git -C /Users/cobalt/cobalt diff --stat d78c66a2 edd5c076` | 0 | `27 files changed, 2916 insertions(+), 115 deletions(-)` |
| main's seam hunks | `git -C /Users/cobalt/cobalt diff -U0 d78c66a2 75dcdb5f -- configs/cobalt/jobs.yaml configs/cobalt/smoke/s2.yaml` | 0 | jobs.yaml `@@ -344,0 +345,17 @@ no_resident_reads:` (the `classify/trial.yaml` and `classify/route.yaml` entries, card 591); s2.yaml `@@ -636 +636,2 @@` (K18 `expect_text` extended with `data/deploy/bootstrap-owed.json`, card 496) |
| 304's seam hunks | `git -C /Users/cobalt/cobalt diff -U0 d78c66a2 edd5c076 -- configs/cobalt/jobs.yaml configs/cobalt/smoke/s2.yaml` | 0 | jobs.yaml `@@ -213,0 +214,16 @@ jobs:` (row `com.cobalt.prefill-refresh`) and `@@ -331 +347 @@` (`readers: [com.cobalt.prefill-daily, com.cobalt.prefill-refresh]`); s2.yaml `@@ -580,0 +581,11 @@` (K12.3 block) |
| jobs.yaml anchors | `grep -n -F "com.cobalt.prefill-daily" configs/cobalt/jobs.yaml` | 0 | `207:  - label: com.cobalt.prefill-daily` · `331:    readers: [com.cobalt.prefill-daily]` (daily.md.j2) · `337:    readers: [com.cobalt.prefill-daily]` (drc.md.j2) · `:79`, `:334`, `:342` comments |
| s2.yaml anchors | `grep -n -F "id: K1" configs/cobalt/smoke/s2.yaml` | 0 | `572:  - id: K12.1` · `581:  - id: K13` · `630:  - id: K18` |
| cli.py anchor | `grep -n -F "from cobalt.drc import cli as drc_cli" src/cobalt/cli.py` | 0 | `70:from cobalt.drc import cli as drc_cli  # noqa: E402` |
| pyproject anchor | `grep -n -F "prefill = " pyproject.toml` | 0 | `69:prefill = "cobalt.prefill.cli:main"` |
| wc -l | `wc -l` of the 17 existing files the port edits | 0 | daily.py 594 · cli.py 74 · config.py 163 · market.py 96 · merge.py 171 · writer.py 1394 · note.py 270 · jobs.yaml 369 · prefill.yaml 17 · s2.yaml 637 · tunables.yaml 1075 · daily.md.j2 99 · test_daymode_note.py 228 · test_finviz_consumers.py 174 · test_prefill_daily.py 428 · test_setups_d1.py 610 · test_setups_registries.py 611 |
| READ tail | `tail -n 3 ".../reports/f4-refresh-check-2026-10-10.md"` | 0 | last line: `CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · … · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185` |
| READ | card 304 read whole (Read tool) | — | rows A1-CR3, `## NOT IN THIS JOB`, RESTARTS paragraph, `## CHECK ASKS` |
| restarts empty range | `uv run cobalt jobs restarts 75dcdb5f..HEAD` | 0 | `docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md	A	DOCS	-` · `RESTARTS: none` (only this report, uncommitted-tree path) |
| DB | none taken at PREFLIGHT (L76 as amended); with-DB strings proven at W's gate | — | — |

Card `## RECORDS` copied: drafter `draft-304-recut` 2026-10-18 06:24 EDT, BASE `75dcdb5f`; `git diff --stat d78c66a2 main` over the 26 files → only `configs/cobalt/jobs.yaml | 17 +` and `configs/cobalt/smoke/s2.yaml | 3 +-` (re-read per file at PORT, PROOF lines); anchors `cli.py:70`, `pyproject.toml:69`, `jobs.yaml:207`, `:331`, `:337`, `s2.yaml:572`, `:630` re-read above; old job build `799b6040`, check tip `98174119`, fix `edd5c076`; the `## LAUNCHD` line is the deploy card's.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `75dcdb5f` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 772.11s (0:12:52)`; 0 failed, 0 errors. (One skip names `COBALT_LIVE_VAULT_ROOT`, `tests/taxonomy/test_predicate.py:262` — the offline run, expected; the live-note run below covers it.)
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.56s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
None written, by the card: `ORDER (… A1-DOC are built and checked on the old branch, no re-red of them)`; PORT's red column is `— (the port is the change)` and CR3's is `RUN — asserts nothing`. The old job's reds are its record (`reports/f4-refresh-build-2026-10-10.md`). No with-DB red, so no lock take at E2.

## E3 THE ROWS
### PORT (R1833) — commit `51b03e00` `feat(f4-refresh-1018): port card 304 F4 refresh from edd5c076 onto main (PORT, R1833, L3, L28, L42)` (26 files changed, 2690 insertions(+), 115 deletions(-))
Method: Edit/Write only. Source text read from `git -C /Users/cobalt/cobalt diff d78c66a2 edd5c076 -- <file>` and, for the three new files and the whole-page rewrite of `prefill/daily.md`, from the old worktree `/Users/cobalt/cobalt-wt/f4-refresh-1010` (read only), whose tree equals `edd5c076` except its report: `git -C /Users/cobalt/cobalt-wt/f4-refresh-1010 diff --stat edd5c076` → `.../reports/f4-refresh-build-2026-10-10.md | 116 +++++++++++++++++++--` only. No merge, cherry-pick, revert or rebase.

Untouched-by-main proof, one call over the 24 files: `git diff --stat d78c66a2 75dcdb5f -- <the 24>` → empty (exit 0, no output).
Byte-equal proof at the tip, one call over the 24 files: `git diff --stat edd5c076 -- <the 24>` → empty (exit 0, no output), run after `51b03e00`. (Before the commit the same call listed only the three then-untracked new files; each was then proved with `git diff --no-index --stat <old worktree file> <file>` → empty. `test_prefill_refresh.py` first showed `1 deletion` — a trailing blank line my Write dropped — fixed by Edit and re-proved empty.)

PROOF lines (one per ported file; each line's evidence is the two empty calls above, or the seam diff below):
PROOF: configs/cobalt/prefill.yaml — main untouched; equal to edd5c076
PROOF: configs/cobalt/taxonomy/tunables.yaml — main untouched; equal to edd5c076
PROOF: configs/cobalt/templates/daily.md.j2 — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/daymode/note.md — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/prefill/cli.md — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/prefill/config.md — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/prefill/daily.md — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/prefill/market.md — main untouched; equal to edd5c076
PROOF: docs/40 - DevDocs/cobalt/vaultwrite/README.md — main untouched; equal to edd5c076
PROOF: ops/com.cobalt.prefill-refresh.plist — main untouched (new); equal to edd5c076
PROOF: src/cobalt/daymode/note.py — main untouched; equal to edd5c076
PROOF: src/cobalt/prefill/cli.py — main untouched; equal to edd5c076
PROOF: src/cobalt/prefill/config.py — main untouched; equal to edd5c076
PROOF: src/cobalt/prefill/daily.py — main untouched; equal to edd5c076
PROOF: src/cobalt/prefill/market.py — main untouched; equal to edd5c076
PROOF: src/cobalt/vaultwrite/merge.py — main untouched; equal to edd5c076
PROOF: src/cobalt/vaultwrite/writer.py — main untouched; equal to edd5c076
PROOF: tests/cobalt/test_daymode_note.py — main untouched; equal to edd5c076
PROOF: tests/cobalt/test_finviz_consumers.py — main untouched; equal to edd5c076
PROOF: tests/cobalt/test_prefill_daily.py — main untouched; equal to edd5c076
PROOF: tests/cobalt/test_prefill_refresh.py — main untouched (new); equal to edd5c076
PROOF: tests/cobalt/test_prefill_refresh_experiments.py — main untouched (new); equal to edd5c076
PROOF: tests/cobalt/test_setups_d1.py — main untouched; equal to edd5c076
PROOF: tests/cobalt/test_setups_registries.py — main untouched; equal to edd5c076
PROOF: configs/cobalt/jobs.yaml — main touched (card 591); `git diff -U0 75dcdb5f -- configs/cobalt/jobs.yaml` = 304's two hunks only: `@@ -213,0 +214,16 @@ jobs:` (the `com.cobalt.prefill-refresh` row, the 16 lines of `git diff -U0 d78c66a2 edd5c076`'s `@@ -213,0 +214,16 @@`, identical) and `@@ -331 +347 @@` (`-    readers: [com.cobalt.prefill-daily]` / `+    readers: [com.cobalt.prefill-daily, com.cobalt.prefill-refresh]`, identical to 304's `@@ -331 +347 @@`). Card 591's lines stand: `grep -n -F "classify/" configs/cobalt/jobs.yaml` → `361:  - path: configs/cobalt/classify/trial.yaml`, `371:  - path: configs/cobalt/classify/route.yaml` (+ `:364`, `:365`, `:374` `because:` lines)
PROOF: configs/cobalt/smoke/s2.yaml — main touched (card 496); `git diff -U0 75dcdb5f -- configs/cobalt/smoke/s2.yaml` = 304's one hunk only: `@@ -580,0 +581,11 @@ checks:` (the K12.3 block, identical to 304's `@@ -580,0 +581,11 @@`). Card 496's line stands: `grep -n -F "bootstrap-owed.json" configs/cobalt/smoke/s2.yaml` → `648:      data/deploy/bootstrap-owed.json (OWED, deferred bootstrap)`

PROOF count: 26 of 26.

P2 seams: `grep -c -F "label: com.cobalt.prefill-refresh" configs/cobalt/jobs.yaml` → `1`; `grep -n -F "readers: [com.cobalt.prefill-daily" configs/cobalt/jobs.yaml` → `347:    readers: [com.cobalt.prefill-daily, com.cobalt.prefill-refresh]` (daily.md.j2) and `353:    readers: [com.cobalt.prefill-daily]` (drc.md.j2, unchanged); `grep -c -F "id: K12.3" configs/cobalt/smoke/s2.yaml` → `1`.

Rows' tests after the port (offline): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_prefill_refresh.py tests/cobalt/test_prefill_refresh_experiments.py tests/cobalt/test_prefill_daily.py tests/cobalt/test_daymode_note.py tests/cobalt/test_finviz_consumers.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_vaultwrite.py tests/cobalt/test_placement.py` → `233 passed, 97 skipped, 4 xfailed in 193.32s (0:03:13)` (skips: `Postgres env settings not available`, the with-DB half runs at W).

MUTATIONS: none run, by the card: the rows A1-DOC are "context, not rebuilt; their RED-on-BASE lines are the old job's (done and checked)" and "no re-red of them"; PORT's red column is `—`. The old job's reds and mutations are its record (`reports/f4-refresh-build-2026-10-10.md`).

DevDocs: the six pages' dated lines are the ported `## 2026-10-10 — f4-refresh-1010` sections (byte-equal to `edd5c076`); no new line is added — a new line would break P1's byte-equality.

### CR3 (R1379)
BOOTSTRAP: deferred com.cobalt.prefill-refresh

## RESTARTS
`uv run cobalt jobs restarts 75dcdb5f..HEAD` (HEAD `51b03e00`), table WHOLE:

```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/prefill.yaml	M	resident reads	com.cobalt.aset
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
configs/cobalt/templates/daily.md.j2	M	no resident reads (one-shot: com.cobalt.prefill-daily,com.cobalt.prefill-refresh)	-
docs/40 - DevDocs/cobalt/daymode/note.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/market.md	M	DOCS	-
docs/40 - DevDocs/cobalt/vaultwrite/README.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-refresh-build-2026-10-18.md	A	DOCS	-
ops/com.cobalt.prefill-refresh.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.prefill-refresh	-
src/cobalt/daymode/note.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/market.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/merge.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/writer.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_daymode_note.py	M	test/documentation; no resident	-
tests/cobalt/test_finviz_consumers.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_daily.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh.py	A	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. Matches the card's expected set (`com.cobalt.aset com.cobalt.radar`, plus the new one-shot `deferred`). (The report row is this uncommitted report.)

## W THE THREE SUITES
`<tip>` = `51b03e00`. The call was `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1018 all --deploy`, run in the background, exit 0. It had no `--deselect` (no migration, no with-DB test above `0013`), no `--tickers` (the port's with-DB tests write `vault_writes` rows only; the old job's gate calls carried none either) and no `--migration`. Verdict lines, whole:

```
tests/ops: run (ops/com.cobalt.prefill-refresh.plist)
offline 8538/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5552/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1018-all-20261018-070255.log
```
- The skips in pass 1 are not marked `OUTSIDE the allowed set`. The `COBALT_LIVE_VAULT_ROOT` skips belong to pass 1 at `.env`; the live-note pass (`146 passed, 1 skipped`, log `:2273`) runs those files and skips only `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`).
- Summaries in the log (`grep -n -F " passed" <log>`):
  - `:921` `4618 passed, 838 skipped, 4 xfailed, 36 warnings in 784.61s` (offline)
  - `:993` `3920 passed, 1 xfailed, 16 warnings in 970.25s` (tests/ops)
  - `:1228` `5347 passed, 7 skipped, 99 deselected, 7 xfailed, 43 warnings in 950.68s` (pass 1)
  - `:2082` `205 passed, 1 deselected, 5 warnings in 247.80s` (pass 2, the standing gate-list deselects)
  - `:2273` `146 passed, 1 skipped, 15 warnings in 29.61s` (live-note)
- Pass 1 executed command (log `:1066`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py`
- Fingerprints:
  - `<F0>` (log `:1010`): `664 35 272c95bbb12241e3611e4b36326ccf87`
  - `<F2>` (log `:2150`): `664 35 272c95bbb12241e3611e4b36326ccf87`, so F2 = F0
  - No forward was applied (no migration), so there is no F1.
- Lock: taken at log `:998-1002` (`lock taken: f4-refresh-1018`, `lock: waited 0 min`) and released at `:2203-2204` (`lock released`). `ls /Users/cobalt/cobalt-wt/f4-refresh-1018/.env` gives `No such file or directory`.
- Strict xfails (P3): `tests/cobalt/test_prefill_refresh.py` is byte-equal to `edd5c076` (PORT proof), so its five strict xfails stand unedited: T2b `:739`, O1 `:1062`, O2/B1 `:1078`, A3 `:1152`, and X16's hand-typed leg, carried as in the old tip. The xfail counts are 4 offline on the tip against 1 on BASE (E0), which is the 3 offline strict xfails of the file, and 7 in pass 1. With `-rs` the gate does not print XFAIL ids (`grep` of the log for `XFAIL … test_prefill_refresh` finds nothing), so the counts are the tool evidence. `reports/f4-refresh-build-2026-10-10.md` is unchanged: `git diff --stat 75dcdb5f HEAD -- "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` is empty.

## PRE-STOP SELF-CHECK
(1) Every added or changed test has been shown RED for its named reason. Each ported test is byte-equal to the checked tip `edd5c076`. Its RED on BASE and its mutation runs are the old job's record (`reports/f4-refresh-build-2026-10-10.md`, checked in `reports/f4-refresh-check-2026-10-10.md`). The card forbids re-reds here ("A1-DOC are built and checked on the old branch, no re-red of them"). This job adds no test of its own.
(2) Every entry path is pinned. The callers are those of card 304, pinned by the same tests, which are unchanged. The two seam assertions are pinned by `TestTheJobRow::test_the_template_names_both_one_shot_readers` and `test_the_smoke_row_watches_the_job`, both green in the offline run (`233 passed`) and in the gate (`offline 8538/0`).
(3) Every count and quote was re-read from tool output at the tip `51b03e00`: `git diff --stat edd5c076 -- <24>` was empty after the commit, along with the seam `grep -n -F`/`grep -c -F` calls, the RESTARTS table on `75dcdb5f..HEAD` and the gate log greps above.

## FOR THE CHECK
- Range `75dcdb5f..51b03e00` has one commit: `51b03e00 feat(f4-refresh-1018): port card 304 F4 refresh from edd5c076 onto main (PORT, R1833, L3, L28, L42)`.
- P1, P2 and P3 are under `## E3 THE ROWS` and `## W`. P4 is the CR3 line at column 0 under `### CR3`.
- Reds and mutations: none in this job (the card). Greens: the offline run of the rows' files (`233 passed, 97 skipped, 4 xfailed`) and the gate (`## W`).
- The RESTARTS table is under `## RESTARTS`. F0, F2 and the lock times are under `## W`.
- The records copied at PREFLIGHT are under `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- `REFUSED, not needed: git -C /Users/cobalt/cobalt diff --stat d78c66a2 75dcdb5f -- configs src/... docs/40\ -\ DevDocs/... — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (backslash-escaped paths; the same proof ran later as `git diff --stat d78c66a2 75dcdb5f -- <24 quoted paths>`, which was empty).
- `REFUSED, not needed: git -C /Users/cobalt/cobalt show edd5c076:ops/com.cobalt.prefill-refresh.plist — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (I read the file with the Read tool from the old worktree instead, which equals `edd5c076`.)
- No extra lock take: the gate took the lock once. `.env: removed, proven gone (W)`.
- Context: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh c294d27f` printed `context 317898 of 400000 — ok` at 07:54 EDT. That is above the desk's 250,000 line in UNATTENDED RULES (c). I recorded it for the desk and did not act on it.
- The L74 line is under `## L74`.
- The card's records, re-read at PREFLIGHT, are under `## PREFLIGHT`.
- **The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.**

BUILT · job: f4-refresh-1018 · tip: 51b03e00 | on 75dcdb5f | migration: none | offline 8538/0 | with-DB 5552/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 (PORT 26 PROOF of 26, CR3) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 317898
