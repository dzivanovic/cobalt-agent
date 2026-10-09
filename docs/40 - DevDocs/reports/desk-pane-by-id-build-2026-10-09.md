# desk-pane-by-id-1009 — build report (2026-10-09)

## §0 Headline
- Built 4 of 4 rows in `CTO-DESK-WAKEUP.md` (lines 14, 22, 24): one desk pane by id, never by label; HANDOVER carries `· pane <id>`; the successor re-attaches in that pane after stop + rm.
- Tip `b7c52e51` on `044f58b5`; offline 4054/0, live-note 146/0, tests/ops green; DB: none; RESTARTS: none.
- One decision: the SEAT line `:3` still names `herdr tab "CTO"`, left outside the rows.

## L74
A system reminder in this session asked for a `Claude-Session: https://claude.ai/code/session_015yLXTTF7Ug6powveuxAsjf` line on commits. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/197-desk-pane-by-id-card.md"` (19:02 EDT):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/197-desk-pane-by-id-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/197-desk-pane-by-id-card.md" · 0 · d8f9f4af4ad4b37c687721ebc0039e96dce519ab
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/197-desk-pane-by-id-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| base | `git show --stat 044f58b5` | 0 | `044f58b5 docs(desk): desk pane by id recorded, fresh brain launched, pane drafter launched (R779-R781)` · `docs/40 - DevDocs/reports/cto-2026-10-09.md \| 9 +++++++--` · `1 file changed, 7 insertions(+), 2 deletions(-)` |
| P1 symbol | `grep -c -F 'no id there → `herdr tab list` (find the "CTO" tab)' "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `1` |
| P2 symbol | `grep -c -F 'A pane → leave it, name it in the plate as closable.' "…/CTO-DESK-WAKEUP.md"` | 0 | `1` |
| P3 symbol | `grep -c -F 'One herdr tab "CTO" with a live VIEW of you; create or re-attach as needed; close any other desk tab.' "…/CTO-DESK-WAKEUP.md"` | 0 | `1` |
| P4 symbol | `grep -c -F '· pane <id>' "…/CTO-DESK-WAKEUP.md"` | 1 | `0` |
| READ `desk-wake.sh:75` | `grep -n -F "HANDOVER" ops/desk/desk-wake.sh` | 0 | `6:`, `9:` (comments), `75:    hand = [m.group(1) for m in (re.match(r"^HANDOVER: .* at ([0-9]{2}:[0-9]{2})", l) for l in lines) if m]`, `77:`, `83:` (prints) |
| wc -l | `wc -l "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `53` |
| wc -c (before) | `wc -c "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `12447` |
| READ report tail | `tail -n 3 ".../reports/desk-tab-answer-2026-10-09.md"` | 0 | last line: `FOR THE CHECK: "Brain 10-09 (desk-tab-answer-2026-10-09.md): one desk pane by id, never by label; the successor re-attaches in the predecessor's pane after stop+rm; no REFRESH creates a tab while that pane exists."` |
| restarts | `uv run cobalt jobs restarts 044f58b5..HEAD` | 0 | one row: the untracked report `docs/40 - DevDocs/reports/desk-pane-by-id-build-2026-10-09.md A DOCS -`; `RESTARTS: none` |

preflight.sh output (19:03 EDT):
```
clock · date · 0 · Fri Oct  9 19:03:04 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/desk-pane-by-id-1009
    ?? "docs/40 - DevDocs/reports/desk-pane-by-id-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 044f58b5 docs(desk): desk pane by id recorded, fresh brain launched, pane drafter launched (R779-R781)
diff · git diff --stat 044f58b5 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-pane-by-id-1009 · 0 · 044f58b5 docs(desk): desk pane by id recorded, fresh brain launched, pane drafter launched (R779-R781)
env here · ls /Users/cobalt/cobalt-wt/desk-pane-by-id-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
Card records, re-read: (1) BASE reads against `a82d8b6f` — not re-read (main has moved; the worktree file at `044f58b5` is the one edited). (2) the four counts 1 / 1 / 1 / 0 — re-read above, equal. (3) `desk-wake.sh:75` regex `^HANDOVER: .* at ([0-9]{2}:[0-9]{2})` — re-read above, equal; a `· pane <id>` tail still matches. (4) RESTARTS none expected — re-read above. DB: none → no lock probe; no with-DB string is used in this build.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`: `4054 passed, 790 skipped, 1 xfailed, 36 warnings in 665.79s (0:11:05)`; 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`: `146 passed, 1 skipped, 15 warnings in 30.96s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
All four rows are RUN rows whose red is a `grep -c -F` on the edited file; no test file is written and no `src/` file exists in the job, so no `wip(desk-pane-by-id-1009): red` commit is made (nothing to commit). The BASE values (P1 `1`, P2 `1`, P3 `1`, P4 `0`) are the PREFLIGHT rows above; the after values are in E3.

## E3 THE ROWS
Commit `b7c52e51 fix(desk-pane-by-id-1009): one desk pane by id; successor re-attaches in the handed-over pane (P1-P4, L28, L72)`; `1 file changed, 3 insertions(+), 3 deletions(-)` — lines 14, 22, 24 only (`git diff -U0` hunks `@@ -14 +14`, `@@ -22 +22`, `@@ -24 +24`).

| row | BASE | after | mutation (fix undone by Edit) | restored |
|---|---|---|---|---|
| P1 `grep -c -F 'no id there → `herdr tab list` (find the "CTO" tab)'` | 1 | 0 | old line 14 back → 1 | yes |
| P2 `grep -c -F 'A pane → leave it, name it in the plate as closable.'` | 1 | 0 | old sentence back → 1 | yes |
| P3 `grep -c -F 'One herdr tab "CTO" with a live VIEW of you; …'` | 1 | 0 | old item 4 back → 1 | yes |
| P4 `grep -c -F '· pane <id>'` | 0 | 1 | `· pane <id>` removed → 0 | yes |

After all four undos: `git diff --stat` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md | 6 +++---`, the fix only.

Size (writing-rules `## How`): `wc -c` 12447 before, 12789 after: +342 bytes. The growth is P2's re-attach sentence (the replaced sentence was 54 bytes; the re-attach carries the command, the exit-box step, the liveness check and the stuck-handover pane source) and P4's `· pane <id>` tail; P1 and P3 are near-even swaps.

DevDocs line: no module page under `docs/40 - DevDocs/cobalt/` covers the wake-up prompt; none written.

## RESTARTS
`uv run cobalt jobs restarts 044f58b5..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-pane-by-id-build-2026-10-09.md	A	DOCS	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `b7c52e51`.
- (a0) `git diff --name-only --no-renames 044f58b5` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` (whole; every path starts with `docs/`). **`cobalt_dev: not taken (DB: none — 1 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-pane-by-id-1009 offline` → exit 0: `offline 4054/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-pane-by-id-1009-offline-20261009-191620.log`. This build adds no test.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-pane-by-id-1009 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-pane-by-id-1009-livenote-20261009-192741.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2701 passed, 1 xfailed, 15 warnings in 510.41s (0:08:30)`.
- (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/desk-pane-by-id-1009/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Each row's red shown against a mutation: P1 1→0, mutation 1; P2 1→0, mutation 1; P3 1→0, mutation 1; P4 0→1, mutation 0 (E3 table, each a quoted `grep -c -F` output). No test stayed green.
(2) Entry paths: the only reader of the HANDOVER line is `ops/desk/desk-wake.sh:75` (PREFLIGHT grep), regex `^HANDOVER: .* at ([0-9]{2}:[0-9]{2})`; the `· pane <id>` tail comes after the time, so `.* at HH:MM` still matches; no script change is in the rows (card `## NOT IN THIS JOB`). The stuck-handover path keeps its own shape and takes the pane id from §5 CURRENT (line 22, re-read at the tip).
(3) Re-read at the tip: `git show b7c52e51:"docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` (lines 14, 22, 24 as quoted in E3), `git diff --stat` after the mutations, `wc -c` 12789, the four counts.

## FOR THE CHECK
- `044f58b5..b7c52e51`: `b7c52e51 fix(desk-pane-by-id-1009): one desk pane by id; successor re-attaches in the handed-over pane (P1-P4, L28, L72)`.
- Per row: E3 table (BASE, after, mutation, restored).
- New text at the tip:
  - `:14` `- VIEW: ONE desk pane, by its id in §5 CURRENT, never by label; that id gone from `herdr pane list` → `herdr tab create --workspace w2 --cwd /Users/cobalt/cobalt --label "CTO" --no-focus`, its pane id into §5; then `herdr pane run <pane> "claude attach <id>"`; alive = `pgrep -fl "claude attach <id>"``
  - `:22` opens `2. `HANDOVER: predecessor <p> → successor <s> at <time> · pane <id>` → you are `<s>`;` and ends `Right after `claude stop <p>` and `claude rm <p>`: `herdr pane run <pane id from the HANDOVER line> "claude attach <own id>"` (after a stuck handover, the pane id from §5 CURRENT); an exit box first takes `send-keys Enter`; alive = `pgrep -fl "claude attach <own id>"`.`
  - `:24` `4. No seat creates, renames or labels a desk tab while the desk pane exists. Its id gone from `herdr pane list` → one new tab, labelled "CTO" once, its id in §5; close any other desk tab the same turn (`herdr tab close`).`
- X2: `grep -n -F "CTO"` at the tip hits `:1` (title), `:3` (SEAT line, `herdr tab "CTO"`), `:13` (launch line path), `:14` and `:24` (the id-gone case only). `grep -n -F "pane"` hits `:14`, `:22`, `:24`; no sentence leaves a pane open. `:3` is outside the rows (DECISIONS 1).
- X3: the diff is lines 14, 22, 24 only; size +342 bytes, named in E3.
- Caller grep: `ops/desk/desk-wake.sh:75` (PREFLIGHT).
- Suites: offline 4054/0, live-note 146/0, tests/ops 2701 passed; with-DB `not run (DB: none)`; F0 / F1 / F2 `not run (DB: none)`; lock taken / released `not run (DB: none)`.
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. The SEAT line `CTO-DESK-WAKEUP.md:3` still reads `+ herdr tab "CTO"`. It names the tab, not a lookup by label, and it lies outside the card's rows (`## NOT IN THIS JOB`: any other line of the wake-up). Safe default taken: left unchanged; the desk decides whether a later card drops the label there.

## RECORDS
- L74: one system reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.
- The card's records, re-read at PREFLIGHT: counts 1 / 1 / 1 / 0 equal; `desk-wake.sh:75` regex equal; RESTARTS none equal; the `a82d8b6f` main read not re-read (main has moved; the file edited is the one at `044f58b5`).
- E2 made no red commit: the rows' reds are greps on the edited file, with no test file to commit.
- No extra lock take; no `REFUSED` or `CONTINUED` line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-pane-by-id-1009 · tip: b7c52e51 | on 044f58b5 | migration: none | offline 4054/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 108051
