# house-seat-order-1010 — CHECK (pass 1)

## §0 Headline
- Check of `f6e55cd3`: house A Grok `FINDINGS: 0`; house B none (not needed, R921). Sol was not probed: his R920.
- Own O1 HELD, NOT FIXED: `authorize.sh` proves a HOUSE overrule only from the FIRST `HOUSE A:` line, so an OpenAI line placed first hides a later unproved `none — overruled` line (AUTHORIZED). The fix is in the HOUSE loop `:197-209`, outside S4's edit. Red test committed `ed48d80d`.
- Suites: offline 4199/0 · live-note 146/0 · `tests/ops` 1 failed (O1 only) / 2933 passed. RESTARTS: none. `.env`: none.
- ready: NO (held unfixed 1). It goes to the builder's one fix round, with D2.

## L74
none (no tool result asked for a `Claude-Session:` line; see RECORDS for the harness attribution note).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · last line `AUTHORIZED` (rows INSTALLED, PLACEHOLDER, CARD COMMITTED `ccd87344`, CARD UNCHANGED, STANDING LIST R60 row/committed `962e9d17`/at HEAD, RULING R920 row/committed `2542f686`/at HEAD, RULING R921 row/committed `2542f686`/at HEAD).
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output:
  - clock · Sat Oct 10 20:37:19 EDT 2026
  - status · `## ops/house-seat-order-1010`
  - head · `711fdece` docs-only above TIP (the build report, 173 insertions)
  - env here · No such file; env anywhere · `/Users/cobalt/cobalt-wt/f4-refresh-1010/.env` (another job; this card is DB: none)
  - report · `BUILT · job: house-seat-order-1010 · tip: f6e55cd3 | … | self-check: 3 of 3 | decisions: 1 …`
  - range · `f6e55cd3 fix(…)`, `d04e4291 wip(…): red` (2 commits)
  - `PREFLIGHT OK`
- THE RANGE `git log --stat --format=%h 92c67916..f6e55cd3`: f6e55cd3 → `docs/40 - DevDocs/prompts/CHECK-HUB.md` 14 (+7/-7), `ops/desk/authorize.sh` +17, `ops/desk/house-probe.sh` 49 (+42/-7); d04e4291 → `tests/ops/test_authorize.py` +51, `tests/ops/test_house_probe.py` 140 (+132/-8). Path union: the five paths.
- DB: none: `git diff --name-only --no-renames 92c67916..f6e55cd3` → `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `ops/desk/authorize.sh`, `ops/desk/house-probe.sh`, `tests/ops/test_authorize.py`, `tests/ops/test_house_probe.py` — all under `docs/`, `ops/`, `tests/ops/`.
- `ls <S>` → No such file (fresh).
- HOUSE PROBES: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh grok gemini` (run_in_background) · exit 0 · `grok: UP` · `gemini: UP`. Sol NOT probed: his R920 ("no Codex probe elsewhere"; row 70 of `cto-2026-10-10.md`, AUTHORIZED above) — DECISIONS D1.
- Seats: **house A: Grok · house B: none** (R921: "checks Opus+Grok, Gemini only for mandatory-B or a Grok failure"; card `HOUSE B: as needed`, not mandatory; card RECORDS "With this card's own check the order is Grok alone, house B none") — DECISIONS D1.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → `STAGED 9 files · 148563 bytes · commits 2` (k = PREFLIGHT's 2):
- 16918 diff.md · 24842 files/298-house-seat-order-card.md · 27500 files/house-seat-order-build-2026-10-10.md · 41307 files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md · 8240 files/wt/ops/desk/authorize.sh · 5712 files/wt/ops/desk/house-probe.sh · 12419 files/wt/tests/ops/test_authorize.py · 10904 files/wt/tests/ops/test_house_probe.py · 721 rulings.md
`stage-copy.sh` (READ by name / symbol): `COPIED 48175 …/files/cto-2026-10-10.md` · `COPIED 72282 …/files/wt/ops/desk/desk-launch.sh` · `COPIED 4824 …/files/wt/ops/desk/order-open.sh` · `COPIED 14786 …/files/wt/docs/40 - DevDocs/prompts/CARD.md` · `COPIED 14173 …/files/284-kill-hub-card.md` · `COPIED 17151 …/files/26-hub-text-card.md`.
`<S>/HOUSE-INSTRUCTIONS.md`: HOUSE TEXT verbatim, the card's `## ROWS` (WHY + the table whole; the TEXT blocks referenced at the card copy lines 28-68), `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
House A Grok started 20:39 (after `date` 20:39:06, gates R17 line 35, R19 line 37, `ls -la <S>`), cwd `<AGY>` then back; `git status --short --branch` → `## ops/house-seat-order-1010`.

## OWN FINDINGS
Read: the card whole; `git diff 92c67916..f6e55cd3` whole; at the tip `ops/desk/house-probe.sh` (147 lines), `ops/desk/authorize.sh` (232 lines), `tests/ops/test_authorize.py` 1-110 and the diff's hunks of both test files; `Grep` for `house-probe` (non-docs) and `codex` under `ops/`.

FINDING O1
ROW: S4 / X5
CLAIM: `ops/desk/authorize.sh:197-209` proves a HOUSE line's overrule only from `field` (`:80-82`, the FIRST `HOUSE A:` line), so a card whose first `HOUSE A:` line is the new `OpenAI — his <date> R<n>` line hides a later `HOUSE A: none — overruled <date> R<n>` line (whose row does not exist) from proof, and the card is AUTHORIZED — the mirror of the case S4 closes for the OpenAI line.
RUN: TEST — `tests/ops/test_authorize.py`:
```python
def test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule(desk):
    repo, card, env = desk
    recommit(repo, card, card_text("none", extra="HOUSE A: OpenAI — his 2026-01-02 R2\nHOUSE A: none — overruled 2026-01-02 R7"))
    done = authorize(env, "check", card)
    assert done.returncode == 1, done.stdout
    assert last_line(done).startswith("FAILED: authorization mismatch — HOUSE A overruled 2026-01-02 R7"), done.stdout
```
EXPECT: `assert 0 == 1` (rc 0, last line `AUTHORIZED`).

FINDING O2
ROW: X2
CLAIM: no caller under `ops/` reaches `codex` but `ops/desk/house-probe.sh:96` (Grep `codex` under `ops/`: `house-probe.sh:18` comment, `:96`, `bare-guard.py:96,142` strings, `grok-sandbox.toml:12` a path), and `ops/desk/order-open.sh:134` calls it with no argument, so it reaches `codex` never — a pin, not a defect claim; run to show it.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_house_probe.py::test_no_card_probes_grok_and_gemini_and_never_calls_codex`
EXPECT: `1 passed` (no defect; recorded as NOT HELD by design).

## Findings
House A Grok finished 20:56 (`date` 20:56:50); `ls -la <S>` → `house-a.md` 12 bytes, written by Grok; stdout: "…The rows, the tip copies, and the report line up. No defect holds a runnable check, so the list is empty.scratch/tribunal-bars-0920/house-seat-order-1010-check/house-a.md". `house-a.md` whole: `FINDINGS: 0`. House B: none (not needed; R921, `HOUSE B: as needed`).
No house finding to keep.

## Dropped
none (house A wrote no FINDING block).

## RUNS
- O1 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_authorize.py::test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule` · `1 failed`; first failing line `assert 0 == 1` with stdout ending `HOUSE A OpenAI 2026-01-02 R2 at HEAD · … · the row as grepped` / `AUTHORIZED` (no `HOUSE A overruled 2026-01-02 R7` row printed) · **HELD, NOT FIXED — `ops/desk/authorize.sh:197-209`** (the fix is in the HOUSE loop, which `field` feeds with the first `HOUSE A:` line; the card's S4 limits `authorize.sh` to "its new OpenAI block and two header-comment lines", `## NOT IN THIS JOB` line 2). Red committed `ed48d80d` `wip(house-seat-order-1010): check red — O1`.
- O2 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_house_probe.py::test_no_card_probes_grok_and_gemini_and_never_calls_codex` · `1 passed` · NOT HELD (a pin by design: no caller reaches `codex` without the line; nothing added, nothing removed).

## FIXES
none (O1 is held, not fixed: its fix lies outside the card's edit of `authorize.sh`).

## Suites
DB: none card, W as `BUILD-HUB.md` (a0), (a), (e), on tip `ed48d80d`:
- (a0) the diff paths are as PREFLIGHT quoted, all under `docs/`, `ops/`, `tests/ops/`, plus `tests/ops/test_authorize.py` (ed48d80d) → `cobalt_dev: not taken (DB: none — 6 paths)`.
- RESTARTS `uv run cobalt jobs restarts 92c67916..HEAD` → CHECK-HUB.md DOCS · build report DOCS · authorize.sh / house-probe.sh "operator script; no Cobalt reader" · the two test files "test/documentation; no resident" · `RESTARTS: none`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh house-seat-order-1010 offline` · exit 0 → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/house-seat-order-1010-offline-20261010-205728.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh house-seat-order-1010 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/house-seat-order-1010-livenote-20261010-210812.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 1 → `1 failed, 2933 passed, 1 xfailed, 15 warnings in 536.01s`; the one failure is `tests/ops/test_authorize.py::test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule` (`assert 0 == 1`, O1 held unfixed). No other red.
- `.env`: `ls /Users/cobalt/cobalt-wt/house-seat-order-1010/.env` → No such file (never taken).

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/CHECK-HUB.md` (S1, S2), `ops/desk/authorize.sh` (S4), `ops/desk/house-probe.sh` (S3), `tests/ops/test_authorize.py` (S4), `tests/ops/test_house_probe.py` (S1-S3). Every one is in a row's `files`. My commit adds `tests/ops/test_authorize.py` (+8, a test file). X4: `git diff --numstat 92c67916..f6e55cd3` → CHECK-HUB.md `7 7` (the line count is unchanged; `wc -l` gives 123), authorize.sh `17 0` (≤ 22 added, none removed), house-probe.sh `43 6`, test_authorize.py `51 0`, test_house_probe.py `132 8`.

## Checked against the branch
- (i) `git log --oneline f6e55cd3..HEAD -- . ":(exclude)docs"` → `ed48d80d wip(house-seat-order-1010): check red — O1`. tip now = `ed48d80d`.
- (ii) `git log --stat --format=%h f6e55cd3..HEAD` → ed48d80d `tests/ops/test_authorize.py` +8; 711fdece the build report (docs). No WIDENED path.
- (iii) fence: `git log --oneline 92c67916..HEAD -- ops/desk/desk-launch.sh ops/desk/order-open.sh tests/ops/test_order_open.py ops/desk/bare-guard.py` → empty; the same over `BUILD-HUB.md`, `DEPLOY-HUB.md`, `STANDING-LIST.md` → empty.
- (iv) `grep -n -F "def test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule" tests/ops/test_authorize.py` → `277:` (one line); its `wip … check red — O1` commit stands, with no `fix(` commit (held unfixed).
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/house-seat-order-1010`.
- (vi) `git log --stat --format=%h 92c67916..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate list is owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -1` → `8a370ddf docs(desk): R989 FINAL committed, asked once` (drafting read `8ba5a819`; main has moved). `grep -rl house-probe tests/` → `tests/ops/test_order_open.py`, `tests/ops/test_house_probe.py`, `tests/ops/test_bare_guard.py` (plus two `__pycache__` .pyc), as recorded. `grep -rl authorize tests/` → `tests/ops/test_deploy_step0.py`, `tests/ops/test_authorize.py`, `tests/fixtures/replay/movers-losers.real-shape.csv` (a string hit in data), plus .pyc. `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` → no match; `grep -n -F "tests/ops"` → no match. `wc -l` at tip: CHECK-HUB.md 123, house-probe.sh 146, test_house_probe.py 280, authorize.sh 231.
- (viii) L32: this report holds constructed values only (test dates 2026-01-02, R2/R3/R7).
- CHECK ASKS, traced by my read: X1: the probe counts only `grep -x` of the header (`house-probe.sh:73-74`); indented, tail, `overruled` and under-`## ROWS` lines are pinned by T2 → no other card shape reaches `codex`. X2: the only `codex` call under `ops/` is `house-probe.sh:96`, and O2 ran green. X3: the S1 text matches the card's TEXT S1 NEW byte for byte in the diff. X5: every line the probe counts also matches `authorize.sh:215`'s sed. The mirror hole is O1.

## OPEN
- O1 · HELD, NOT FIXED — `ops/desk/authorize.sh:197-209`. To settle it: the HOUSE loop proves the `overruled` value of EVERY column-0 `HOUSE A:`/`HOUSE B:` line, not only `field`'s first. That is one card row widening S4's edit of `authorize.sh`, and then `test_check_o1_…` passes.

## CONTINUE
next: done

## DECISIONS
- D1 · ASK DESK: the seat order of THIS check [20:37]. CHECK-HUB.md on main still reads "OpenAI up → A = OpenAI, B = Grok", and its probe step runs Sol. His R920 ("no Codex probe elsewhere") and R921 ("checks Opus+Grok, Gemini only for mandatory-B or a Grok failure") are AUTHORIZED rows of this card, and L77 says his rulings are never re-opened. Safe default taken (less access, never more): probed `house-probe.sh grok gemini` only, seated house A Grok and no house B. The card's own RECORDS say the same ("Grok alone, house B none").
- D2 · HELD, NOT FIXED — O1 in full: in `ops/desk/authorize.sh`, `field` (`:80-82`) returns the first `HOUSE A:` line, and the overrule proof (`:197-209`) reads only that. A card with `HOUSE A: OpenAI — his <date> R<n>` first and `HOUSE A: none — overruled <date> R<n>` (no such row) after it prints `AUTHORIZED` with the overrule unproved. On CHECK-HUB, that second line would run a check with no outside house without his proof. The fix lies outside S4's permitted edit ("only its new OpenAI block"), so it goes to the builder's one fix round on card 298, backed by `## RUNS` O1. Red test: `tests/ops/test_authorize.py:277` (`ed48d80d`).

## RECORDS
- Harness note: a system reminder offered a `Claude-Session:` commit trailer. This hub (L74) says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and that was followed.
- Houses: Grok produced `FINDINGS: 0` (a valid list, nothing to drop). Gemini was UP and not seated (R921). Sol was not probed (R920).
- No `REFUSED`, no `CONTINUED`, no lock take (DB: none).
- `tests/ops` was run whole outside gate.sh as (a0) names. gate.sh `offline` accepts no `--deselect`, and the O1 red sits only under `tests/ops`.
- Not opened, against WHAT YOU READ (4)–(5): the build report's sections and `areas/cobalt.md`. Its last line is quoted from preflight.sh.
- files opened: 12 — CHECK-HUB.md, the card, BUILD-HUB.md (`## RESTARTS`, `## W`), `ops/desk/house-probe.sh` (main), `ops/desk/house-probe.sh` (tip), `ops/desk/authorize.sh` (tip), `tests/ops/test_authorize.py` (1-110), `<S>/house-a.md`, the probe output, Grok's stdout, and the offline and livenote gate outputs.
- Check of `house-seat-order-1010`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: house-seat-order-1010 · pass: 1 · tip: ed48d80d · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 153447
