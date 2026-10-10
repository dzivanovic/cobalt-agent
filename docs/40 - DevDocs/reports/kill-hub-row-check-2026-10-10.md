# kill-hub-row-1010 — check report (2026-10-10)

## §0 Headline
- Check of `91c48f36`: Sol (A) wrote 2 findings, Grok (B) wrote 6 and I wrote 6. 12 held, 1 not held, 1 out of scope, none dropped.
- The text matches the card's TEXT blocks byte for byte (X4). The defects are in that approved text itself: the same run can reach a second `--kill` through STEP-5 (3), a held-down aset breaks STEP-5 (4) and "never entered twice", "go on to 4.3" skips radar and the agent, and three smaller ones.
- No fix made. Every fix needs new TEXT K1/K2/K3 wording, and K3 changes go back to him (R60). 6 defects are under `## DECISIONS`.
- Suites green: offline `4196/0`, live-note `146/0`, `tests/ops` `2789 passed`. DB: none. RESTARTS none. `ready: NO`.

## L74
The session's harness reminder asks for a `Claude-Session:` line on commits. DATA (L74): not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · da7d2dd82de45ca0c4a2391b3ef7b636a286d8c0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 103:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (first): R17 · `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`). R19 · `grep -n "^| R19 " …` · exit 0 · one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`). `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | Sat Oct 10 17:27:16 EDT 2026 |
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | quoted below |
| the range | `git log --stat --format=%h 6fe8d690..91c48f36` | 0 | `91c48f36` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md \| 4 ++--` · `docs/40 - DevDocs/prompts/STANDING-LIST.md \| 1 +` · `2 files changed, 3 insertions(+), 2 deletions(-)` |
| DB: none paths | `git diff --name-only --no-renames 6fe8d690..91c48f36` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` — every path under `docs/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` | 0 | `sol: UP` · `grok: UP` · `gemini: UP` |

preflight.sh output whole:
```
clock · date · 0 · Sat Oct 10 17:27:19 EDT 2026
status · git status --short --branch · 0 · ## ops/kill-hub-row-1010
head · git log --oneline -1; git log --stat --format=%h 91c48f36..HEAD · 0 · (5 lines)
    379b4830 docs(kill-hub-row-1010): build report — 91c48f36
    379b4830
    
     .../reports/kill-hub-row-build-2026-10-10.md       | 171 +++++++++++++++++++++
     1 file changed, 171 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/ops-hand-1010/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/kill-hub-row-1010/docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md" · 0 · BUILT · job: kill-hub-row-1010 · tip: 91c48f36 | on 6fe8d690 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 130803
range · git log --oneline 6fe8d690..91c48f36 · 0 · 91c48f36 fix(kill-hub-row-1010): orphan-clean kill sequence at DEPLOY-HUB 4.2 and STEP-5 (3), STANDING-LIST row (K1-K3, L1 L28 L72)
PREFLIGHT OK
```
Path union for `## Scope`: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`. The docs-only commit above TIP: `379b4830` (the build report). A sibling `.env` in `ops-hand-1010`: another job holds the lock; this card is DB: none and takes none.
Seats (SEAT ORDER): **house A: Sol (OpenAI) · house B: Grok (xAI)**. HOUSE B: as needed. The card's RECORDS line "The check is house A Grok" is met by Grok in seat B: Grok reads the `--kill` text in this check.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
107 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/diff.md
13723 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/284-kill-hub-card.md
16606 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/kill-hub-row-build-2026-10-10.md
58628 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
40686 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
368 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/rulings.md
STAGED 6 files · 130118 bytes · commits 0
```
`commits 0` against PREFLIGHT's 1: the hub's diff is `-- . ":(exclude)docs"` and every path of this card is under `docs/`, so the code-only diff holds no commit; `diff.md` is its header alone (Read: one line). See `## DECISIONS` ASK DESK 1. So the houses see the change, I wrote `<S>/diff-docs.md` from `git log -p 6fe8d690..91c48f36` (the whole range, 1 commit, 9108 bytes) and named it in `HOUSE-INSTRUCTIONS.md`.
stage-copy, each exit 0 unless named:
- `COPIED 2080 …/files/standing-list-kill-row-2026-10-10.md`
- `COPIED 2061 …/files/kill-sequence-amend-2026-10-10.md`
- `COPIED 819 …/files/kill-label-fix-2026-10-10.md`
- `COPIED 4333 …/files/kill-row-preflight-2026-10-10.md`
- `/Users/cobalt/cobalt/ops/desk/orphan-clean.sh` · exit 1 · `REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/ops/desk/orphan-clean.sh` → copied from the worktree instead after `git diff --stat 91c48f36 main -- ops/desk/orphan-clean.sh` printed nothing (equal): `COPIED 12334 …/files/wt/ops/desk/orphan-clean.sh`
- `COPIED 10924 …/files/229-orphan-clean-card.md`
- `COPIED 17151 …/files/26-hub-text-card.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (16325 bytes): the HOUSE TEXT verbatim, the card's ROWS (with the TEXT blocks), NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
Launch: `date` 17:30:02 EDT; house gates R17, R19 one row each again; `cd <AGY>`; Sol (house A, task `bf5pm4ckb`) and Grok `grok-4.7` (house B, task `bpi50s9nc`) started one after the other, `run_in_background`, timeout 2700000; `cd <WT>`; `git status --short --branch` → `## ops/kill-hub-row-1010`.

## OWN FINDINGS
Written before either house's list was opened. Paths are at the tip, in `<WT>`.

FINDING O1
ROW: K2 (X2)
CLAIM: A 4.2 kill-sequence failure (a difference at (2), an orphan left at (4), or exit 1) ends in STEP-5, and STEP-5 (3) at `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:162` starts the sequence again on the bare condition "aset booted out", with no clause for an aset already through 4.2's sequence, so the same run can reach a second `--kill aset` (or a first one the 4.2 stop refused), which contradicts "no second kill" at `:137` and `STANDING-LIST.md:149`.
RUN: COMMAND `grep -n -F -e "aset booted out → the kill sequence" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one hit, `162:- (3) THE RESTORE: aset booted out → the kill sequence: …`, the trigger "aset booted out" alone, with no exception for a 4.2 that already ran or stopped the sequence.

FINDING O2
ROW: K2 (X5)
CLAIM: When STEP-5 (3) holds aset down, STEP-5 (4) at `DEPLOY-HUB.md:163` still re-runs 4.7 (a) ("`launchctl print` aset / radar → running", `:145`) and (b), and no line says how a held-down aset is read there, so the re-run reads a red the text did not foresee.
RUN: COMMAND `grep -c -F -e "held DOWN" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `1` (only `:162`); no line of STEP-5 (4) or 4.7 names the held-down aset.

FINDING O3
ROW: K2 / K3
CLAIM: The stop for a failed STEP-5 (3) sequence reads "residents stay down (aset no bootstrap)" and then "bootstrap each resident booted out and not held DOWN" at `DEPLOY-HUB.md:162`, while `STANDING-LIST.md:149` says "inside STEP-5 (3) residents stay down"; the two lines leave it open whether radar is bootstrapped.
RUN: COMMAND `grep -n -F -e "inside STEP-5 (3) residents stay down" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: `149:` one hit: the plural "residents stay down", with no "(aset no bootstrap)" restriction that `:162` carries.

FINDING O4
ROW: X3 / SCOPE
CLAIM: The deploy hub's own account of CLASS (a) at `DEPLOY-HUB.md:13` ("`authorize.sh`, `gate.sh` and the two lock scripts, at the repo path") and `STANDING-LIST.md:135` still name no `orphan-clean.sh`, so the deploy hub's CLASS (a) list and the new K3 row disagree.
RUN: COMMAND `grep -n -F -e "and the two lock scripts, at the repo path" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `13:` one hit, the CLASS (a) script list without `orphan-clean.sh`.

FINDING O5
ROW: X4
CLAIM: The tip's two files are not byte-identical to the staged label-fixed copies the card's RECORDS name as the source of the TEXT blocks.
RUN: COMMAND `git -C /Users/cobalt/cobalt diff --no-index "/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/DEPLOY-HUB.md" "/Users/cobalt/cobalt-wt/kill-hub-row-1010/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (and the same for `STANDING-LIST.md`)
EXPECT: any output (a hunk) if true; no output if the claim is false.

FINDING O6
ROW: K1 / K2 (X1)
CLAIM: `--kill aset` can exit 1 with stdout `FAILED: <pid> survived KILL` (`ops/desk/orphan-clean.sh:296-297`), a line neither `DEPLOY-HUB.md:137` ("Exit 1 (`REFUSED:` / `UNVERIFIED:`)") nor `:162` names, so the text's exit-1 list is narrower than the script's.
RUN: COMMAND `grep -c -F -e "survived KILL" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0`.

## Findings
House A Sol: notice 17:32:17 (`date`), final message written by me to `<S>/house-a.md` (lines 3449-3461 of its output), `FINDINGS: 2`. House B Grok `grok-4.7`: notice 17:42:11, wrote `<S>/house-b.md` itself (4279 bytes), stdout only its path, `FINDINGS: 6`. Every block has a `RUN:` line followed by one `grep` command: none dropped.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| A1 | Sol | X2 | A 4.2 orphan left at (4) goes to STEP-5, whose (3) starts the sequence again unconditionally: a second `--kill`. | COMMAND |
| A2 | Sol | X5 | A STEP-5 (3) hold-down meets STEP-5 (4)'s re-run of 4.7 (a) (aset running), red → STEP-5 again, against "never entered twice". | COMMAND |
| B1 | Grok | X2 | After 4.2's `--kill`, an orphan at (4) enters STEP-5 and (3) runs `--kill aset` again. | COMMAND |
| B2 | Grok | X2 | The hold-down does not stop the path: (4) re-runs 4.7 (a), a red row enters STEP-5 again. | COMMAND |
| B3 | Grok | X5 | Rule F (`:23`) still brings residents up; its exceptions write `aset: DOWN · radar: DOWN`; nothing maps the aset-only hold-down. | COMMAND |
| B4 | Grok | K1 | Both "go on to 4.3" jumps on line 137 come before the agent stop, so the agent stop never runs. | COMMAND |
| B5 | Grok | K1 | `--kill` also exits 1 as `FAILED: <pid> survived KILL`, which K1's `REFUSED:` / `UNVERIFIED:` list does not name. | COMMAND |
| B6 | Grok | X2 | 4.2 puts pids into `## DECISIONS` but not as `DECISION 0`; STEP-7 (3) keeps only `ASK DESK` and `DECISION 0` lines. | COMMAND |

## Dropped
none

## RUNS
Commands with a backtick in the pattern were run through the Grep tool (`-o`, the same fixed strings as alternation), as the UNATTENDED RULES require; the outputs are the lines they matched.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -n -F -e "aset booted out → the kill sequence" DEPLOY-HUB.md` | `162:- (3) THE RESTORE: aset booted out → the kill sequence: (1) … (3) … --kill aset once; …` — the trigger is "aset booted out" alone | HELD |
| A1 | Sol | `grep -n -F -e "any orphan at (4) → no second kill, STEP-5" -e "THE RESTORE: aset booted out → the kill sequence:" DEPLOY-HUB.md` | `137:` (… "(3) … `--kill aset` once; … any orphan at (4) → no second kill, STEP-5 (nothing merged) …") · `162:` (the sequence again, its (3) `--kill aset`) | HELD (same defect as O1) |
| B1 | Grok | `grep -n -F -e "no second kill, STEP-5" -e "orphan-clean.sh --kill aset" DEPLOY-HUB.md` | `137:` holds both strings; `162:` holds `orphan-clean.sh --kill aset` | HELD (same defect as O1) |
| O2 | own | `grep -c -F -e "held DOWN" DEPLOY-HUB.md` | `1` (only `:162`) | HELD |
| A2 | Sol | Grep tool, the four strings | `145:launchctl print\` aset / radar → running` · `162:residents stay down (aset no bootstrap)` · `163:Re-run 4.7 (a), (b), (c), (e), (f)` · `164:STEP-5 is never entered twice` | HELD (same defect as O2) |
| B2 | Grok | Grep tool, the five strings | `143:a red row → STEP-5` · `145:…aset / radar → running` · `162:residents stay down (aset no bootstrap)` (and `not held DOWN`) · `163:Re-run 4.7 (a), (b), (c), (e), (f)` · `164:STEP-5 is never entered twice`; no line says to skip (4) when aset is held down | HELD (same defect as O2) |
| O3 | own | `grep -n -F -e "inside STEP-5 (3) residents stay down" STANDING-LIST.md` | `149:` … "inside STEP-5 (3) residents stay down, FOR DEJAN" (plural, no aset restriction); `DEPLOY-HUB.md:162` reads "residents stay down (aset no bootstrap). Then `launchctl bootstrap` each resident booted out and not held DOWN" (O1's output) | HELD — whether radar comes up is left open |
| B3 | Grok | Grep tool, the three strings plus `held` | `23:aset: DOWN · radar: DOWN` (rule F: "Residents come up before any stop … EXCEPTION … revert did not restore … or … partial"); `162:not held DOWN`; `164:aset: <UP\|DOWN\|not in the set>`; neither `:23` nor `:164` carries `held` | HELD — the aset hold-down is a third "stay DOWN" ending rule F's EXCEPTION does not list |
| O4 | own | `grep -n -F -e "and the two lock scripts, at the repo path" DEPLOY-HUB.md` | `13:` … "(a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` — `authorize.sh`, `gate.sh` and the two lock scripts, at the repo path" | OUT OF SCOPE — `## NOT IN THIS JOB`: "Any other line of `DEPLOY-HUB.md` or `STANDING-LIST.md`" (and the launch-line text) |
| O5 | own | `git -C /Users/cobalt/cobalt diff --no-index <staged kill-row copy> <tip file>`, both files | no output, both | NOT HELD — X4: byte-identical to the staged label-fixed copies; `git diff --numstat 6fe8d690 91c48f36` → `2 2` DEPLOY-HUB, `1 0` STANDING-LIST |
| O6 | own | `grep -c -F -e "survived KILL" DEPLOY-HUB.md` | `0` | HELD (minor: the exit-1 list is narrower than the script) |
| B5 | Grok | `grep -n -A1 -F -e "survived KILL" orphan-clean.sh` (the hub half via Grep tool, O6) | `296:        printf 'FAILED: %s survived KILL\n' "$pid"` · `297-        exit 1`; hub `:137` names `REFUSED:` / `UNVERIFIED:` only | HELD (same as O6) |
| B4 | Grok | `grep -n -F -e "go on to 4.3" DEPLOY-HUB.md` | one hit `137:`; both "go on to 4.3" (at (1) clean and (5)) sit before "If `com.cobalt.agent` is in the set:" | HELD — and wider than claimed: line 137 is the body of "for each of `com.cobalt.aset`, `com.cobalt.radar`", aset first, so "go on to 4.3" after aset's sequence also skips radar's bootout; read literally, a clean aset dry run jumps past radar and the agent stop |
| B6 | Grok | Grep tool, the strings plus `DECISION 0` | `137:each pid into \`## DECISIONS\` FOR DEJAN` (no `DECISION 0` on `:137`); `162:DECISION 0`; `175:every \`DECISION 0\` line` | HELD — K1 and K2 word the same stop two ways; STEP-7 (3)'s list (`ASK DESK`, `DECISION 0`, else `none`) does not name 4.2's pids |

Verdict counts: HELD 12 (O1 O2 O3 O6 A1 A2 B1 B2 B3 B4 B5 B6), NOT HELD 1 (O5), OUT OF SCOPE 1 (O4). No test was written: every finding is a COMMAND, so no `wip(kill-hub-row-1010): check red` commit exists.
Distinct defects among the held: D1 second kill via STEP-5 (3) (O1 A1 B1) · D2 hold-down vs STEP-5 (4) and "never entered twice" (O2 A2 B2) · D3 radar up or down on a hold-down, and rule F (O3 B3) · D4 "go on to 4.3" skips radar's bootout and the agent stop (B4) · D5 `FAILED: <pid> survived KILL` not named (O6 B5) · D6 4.2 pids not a `DECISION 0` (B6).

## FIXES
None made. Every held defect lies in the text the rows pin byte for byte: K1 and K2 require NEW = the card's TEXT K1 NEW / K2 NEW ("each NEW is the label-fixed text", drafted and amended through brain R926-R930), K3 is a line of `STANDING-LIST.md`, whose changes return to him alone (R60: "a command string the close test or the DEPLOY-HUB read changes returns to him alone"), and D3's rule F (`:23`) is a fenced line. A fix here would make the tip differ from the card's TEXT blocks, which is the rows' own red. Each is `HELD, NOT FIXED — <file>` and goes to `## DECISIONS` for the builder's one fix round on new TEXT.

## Suites
DB: none card: RESTARTS, then W (a0), (a), (e) and `tests/ops`, on `91c48f36` (no commit of mine).
- RESTARTS: `uv run cobalt jobs restarts 6fe8d690..HEAD` → `DEPLOY-HUB.md M DOCS -` · `STANDING-LIST.md M DOCS -` · `kill-hub-row-build-2026-10-10.md A DOCS -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 6fe8d690` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md`; every path under `docs/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 offline` → exit 0 · `offline 4196/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-offline-20261010-174309.log` · log `:879` `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 670.21s (0:11:10)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 livenote` → exit 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-livenote-20261010-175434.log` · its one skip (log `:56`): `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0 · `2789 passed, 1 xfailed, 15 warnings in 517.54s (0:08:37)`.
- with-DB: not run (DB: none); `cobalt_dev: not taken`.
- `.env`: `ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env` → `No such file or directory` (never taken). `git status --short --branch` → `## ops/kill-hub-row-1010`.

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (rows K1, K2) and `docs/40 - DevDocs/prompts/STANDING-LIST.md` (row K3), both in the rows' `files`. Above `TIP`: the build report alone (`379b4830`, docs). My commits: none. Nothing outside the rows' files; no vendor or person name in an identifier (docs only).

## Checked against the branch
- (i) `git log --oneline 91c48f36..HEAD -- . ":(exclude)docs"` → no output: no commit of mine; `<tip now>` = `91c48f36`.
- (ii) `git log --stat --format=%h 91c48f36..HEAD` → `379b4830` · `.../reports/kill-hub-row-build-2026-10-10.md | 171 +++` (docs only).
- (iii) fence: `git log --oneline 6fe8d690..HEAD -- ops tests .claude` → no output; `git log --oneline 6fe8d690..HEAD -- <BUILD-HUB.md> <CHECK-HUB.md> <DEVFIX-HUB.md>` → no output. The fenced lines of the two hub files: the diff touches `DEPLOY-HUB.md:137`, `:162` and adds `STANDING-LIST.md:149` only (O5: byte-equal to the staged copies; numstat `2 2`, `1 0`).
- (iv) no HELD finding has a test (all COMMAND): no `def` line, no red commit.
- (v) `ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env` → `No such file or directory`; `git status --short --branch` → see `## Suites`.
- (vi) `git log --stat --format=%h 6fe8d690..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output: no migration, no with-DB test; gate lists not needed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -1` → `92c3fd5c docs(desk): ops-hand deploy card 293, fix round row S` (main has moved past `6fe8d690` since the drafter); `git -C /Users/cobalt/cobalt diff --stat 6fe8d690 HEAD -- <both files>` → no output (main's two files still equal `BASE`); `grep -c -F -e "orphan-clean.sh --kill aset"` on main's `DEPLOY-HUB.md` → `0`; `ls …/scratch/tribunal-bars-0920/kill-row` → `DEPLOY-HUB.md DIFF.md orphan-clean.sh STANDING-LIST.md`.
- (viii) L32: this report holds no ticker, price or date of his; the pids are `<pid>` placeholders.

## OPEN
none open (no REJECTED, no UNSETTLED). Six `HELD, NOT FIXED` defects, listed in full under `## DECISIONS` (D1–D6). OUT OF SCOPE: O4 (`DEPLOY-HUB.md:13` and `STANDING-LIST.md:135` list CLASS (a)'s scripts without `orphan-clean.sh`; fenced: "Any other line of `DEPLOY-HUB.md` or `STANDING-LIST.md`").

## CONTINUE
next: none (CLOSE done 17:55)

## DECISIONS
Six held defects, none fixed: each one's fix is new wording in a TEXT block that the rows pin byte for byte (`## FIXES`). Each goes to the builder's one fix round on this card. That round needs new TEXT K1 / K2 / K3 blocks from the drafter. The default I took: no edit, `ready: NO`.
- D1 — HELD, NOT FIXED — `DEPLOY-HUB.md:162` (K2) and `STANDING-LIST.md:149` (K3) — **FOR DEJAN** (K3 is his list, R60). The second kill (O1, A1, B1). When 4.2's sequence fails (an orphan left at (4), a difference at (2), or exit 1), the run goes to STEP-5. STEP-5 (3) then starts the sequence again on "aset booted out" alone. So one deploy run can reach a second `--kill aset`, or a first kill that 4.2 refused. That contradicts "no second kill". Needs: a STEP-5 (3) clause for an aset whose sequence already ran or stopped at 4.2 (for example: held DOWN, no sequence).
- D2 — HELD, NOT FIXED — `DEPLOY-HUB.md:162`-`:164` (K2). The hold-down meets the smoke re-run (O2, A2, B2). When STEP-5 (3) holds aset down, STEP-5 (4) still re-runs 4.7 (a), which needs aset running (`:145`). Under `:143` a red row means STEP-5, which `:164` forbids entering twice. No line says how (4) reads a held-down aset.
- D3 — HELD, NOT FIXED — `DEPLOY-HUB.md:162` (K2), `STANDING-LIST.md:149` (K3), rule F `DEPLOY-HUB.md:23` (fenced) — **FOR DEJAN**. Radar's state and rule F (O3, B3). K3 says "residents stay down". K2 says "(aset no bootstrap)", then bootstraps "each resident … not held DOWN". So it is open whether radar comes up. Rule F lists only two stay-DOWN endings, each `aset: DOWN · radar: DOWN`, and the aset-only hold-down is a third ending that rule F does not list.
- D4 — HELD, NOT FIXED — `DEPLOY-HUB.md:137` (K1). "go on to 4.3" (B4). Both "go on to 4.3" jumps sit inside the body of "for each of `com.cobalt.aset`, `com.cobalt.radar`", before the agent stop. Read literally, after aset's sequence (clean or done) the run skips radar's bootout and the agent stop. Needs: "go on" to the next label, then the agent stop, then 4.3.
- D5 — HELD, NOT FIXED — `DEPLOY-HUB.md:137`, `:162` (K1, K2). The exit-1 list (O6, B5). `--kill` can exit 1 with `FAILED: <pid> survived KILL` (`orphan-clean.sh:296-297`). K1 names only `REFUSED:` / `UNVERIFIED:`. Exit 1 still routes to STEP-5, so this is minor.
- D6 — HELD, NOT FIXED — `DEPLOY-HUB.md:137` (K1). The 4.2 pids are not a `DECISION 0` (B6). K1 writes "each pid into `## DECISIONS` FOR DEJAN", while K2 writes `DECISION 0: aset orphan …`. STEP-7 (3) fills `## DECISIONS` from `ASK DESK` and `DECISION 0` lines only, so it has no slot for K1's pids.
- ASK DESK 1 [17:28]: `stage-set.sh` printed `STAGED 6 files · 130118 bytes · commits 0`, but PREFLIGHT counted 1 commit. The hub's diff excludes `docs`, and every path of this card is under `docs/`, so the count is right for that diff and nothing is missing. Default taken: go on (no wider access, no second attempt of a house), and give the houses the whole range as `<S>/diff-docs.md` (`git log -p 6fe8d690..91c48f36`). The question for the desk: should a DB: none docs card's stage count compare against the docs-excluded range?

## RECORDS
- Dropped findings: none.
- Every house produced a list: Sol `FINDINGS: 2`, Grok `FINDINGS: 6`. No house sat a second time; Gemini was not seated.
- Sol's output shows `sed -n` reads of files in its read-only sandbox (for example `/bin/zsh -lc "sed -n '301,360p' …orphan-clean.sh"`). It was told to run no command but reading files, and these were reads only, with no write.
- REFUSED, not needed: `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh …` — `REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/ops/desk/orphan-clean.sh` (copied from the worktree, equal to main).
- No `CONTINUED` line. No lock taken (DB: none), so no extra lock take.
- L74: the session's harness reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on. I made no commit.
- Seats: the card's RECORDS expected Grok in seat A. The SEAT ORDER put Sol in A and Grok in B, because all three were UP. Grok's read of the `--kill` text (R932) happened in seat B.
- files opened: 20 — CHECK-HUB.md; the card 284; BUILD-HUB.md (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report; `areas/cobalt.md` (from `## What Cobalt is`, `## Build rules` down); DEPLOY-HUB.md (worktree); STANDING-LIST.md (worktree); `ops/desk/orphan-clean.sh`; my report; the probe output; `<S>/diff.md`; `<S>/rulings.md`; `<S>/diff-docs.md` (written); `<S>/HOUSE-INSTRUCTIONS.md` (written); Sol's output; `<S>/house-a.md` (written); Grok's output; `<S>/house-b.md`; the offline gate output; the live-note gate output.
- Check of `kill-hub-row-1010`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: kill-hub-row-1010 · pass: 1 · tip: 91c48f36 · house A: Sol FINDINGS: 2 · findings: 14 · dropped: 0 · held: 12 · fixed: 0 · held unfixed: 12 · open: 12 · house B: Grok FINDINGS: 6 · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 191529
