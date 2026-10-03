# adoption-scripts — CHECK, pass 1 (2026-10-03)

## §0 Headline
- I checked tip `0a4a7743` alone (house A overruled by R47), with 7 own findings. Each was run: 0 held, 5 not held, 2 rejected and left open.
- I made no commit. The build's suites stand: offline 3749/0, with-DB 847/0, live-note 146/0, `cobalt_dev: 0013`, `.env` removed.
- `ready: NO` on one form rule: the new with-DB test file `tests/cobalt/test_migrate_level.py` sits on a `TREE STATE: unchanged` card (`## 7` (vi)). The pass lists did not change. The judgment seat decides.
- Open: O1, `LEVEL 0013` is blind to `0013`'s DROP NOT NULL, which is the ruled design; O5, an allowed skip at a moved line is marked OUTSIDE, which is advisory and goes to card 02.

## L74
One `Claude-Session:` request (a system block at the start of this session) was recorded and not acted on (`## RECORDS`).

## AUTHORIZATION
Started `date` → `Sat Oct  3 13:44:46 EDT 2026`.
- INSTALLED: `grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md"` → no output.
- CARD: `grep -n -E "«FIL[L]" ".../2026-10-03/03-adoption-scripts-card.md"` → no output · `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03-adoption-scripts-card.md"` → `00870856fe35b4942210aa53891618d1915ed063` · `git -C … diff --stat -- <card>` → no output.
- STANDING LIST: `cto-2026-09-30.md:46` `| R60 | … **HIS RULING** … APPROVES STANDING-LIST.md … | APPROVED |` · log -S → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- RULINGS:
  - 2026-10-02 R47 — `cto-2026-10-02.md:54` `HIS RULING · APPROVED` · log -S → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
  - 2026-10-02 R157 — `cto-2026-10-02.md:164` `HIS RULING · APPROVED` · log -S → `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`.
  - 2026-10-03 R3 — `cto-2026-10-03.md:9` `HIS RULING · APPROVED — pending fold` · log -S → `3727a00454268f485f97fdeccb8f9cc428e86113`.
  - 2026-10-02 R39 — `cto-2026-10-02.md:46` `HIS RULING · APPROVED` · log -S → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
  - 2026-10-02 R42 — `cto-2026-10-02.md:49` `HIS RULING · APPROVED` · log -S → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
- HOUSE A overrule: the card header `HOUSE A: none — overruled 2026-10-02 R47` — R47 proved above ("no outside house").
- HOUSE GATES (standing): `cto-2026-09-24.md:35` R17 one row · `:37` R19 one row · log -S R19 → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 13:44:46 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-scripts-1003` |
| tip | `git log --oneline -1` | 0 | `58098cd3 docs(adoption-scripts): build report — 0a4a7743` |
| docs-only above tip | `git log --stat --format=%h 0a4a7743..HEAD` | 0 | `58098cd3` · `.../reports/adoption-scripts-build-2026-10-03.md | 43 +++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: adoption-scripts · tip: 0a4a7743 \| on a09f0862 \| migration: none \| offline 3749/0 \| with-DB 847/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.radar \| rows: 6 of 6 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline a09f0862..0a4a7743` | 0 | 8 commits: `0a4a7743` fix recut third arg · `8942b505` docs · `8aad8b2e` fix FINGERPRINT search_path · `1befca95` feat (L1 L2 L3 L4 L5 L7) · `bcf4c68f` feat desk-list.sh · `4e88fd64` wip red · `d00dea6d` wip PREFLIGHT · `5625c6c8` wip PREFLIGHT |
| range stat | `git log --stat --format=%h a09f0862..0a4a7743` | 0 | path union below (`## Scope`) |
| lock | `ls <WT>/.env` | 1 | `ls: …/adoption-scripts-1003/.env: No such file or directory` |
| lock, others | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47) — no house gate, no probe |

## Files copied
none (house A: none).

## OWN FINDINGS
Written before any run (house A: none, so there is no list to keep apart from). Read: the card; BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`; the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## DECISIONS`, `## RECORDS` and last line; `git diff a09f0862 0a4a7743 -- src` and `-- ops/desk/desk-launch.sh ops/desk/desk-context.sh ops/desk/desk-list.sh ops/desk/house-probe.sh ops/desk/authorize.sh`; at the tip `ops/desk/gate.sh`, `ops/desk/gate-lists.md`, `ops/desk/desk-context.sh`, `tests/cobalt/test_migrate_level.py`, `tests/ops/test_gate.py` (1–319), `tests/ops/test_locale.py`, `tests/ops/test_desk_context.py`, `tests/ops/test_desk_list.py`; `src/cobalt/db_migrations/0013_…sql`, `0014_…sql`, `0020_…sql`; `DEPLOY-HUB.md:107` and `:184–186`; `areas/cobalt.md` from `## What Cobalt is`.

FINDING O1
ROW: X1 (L1, L2)
CLAIM: `LEVEL 0013` prints on a `cobalt_dev` that lacks `0013`: `0013_tunables_slug_nullable.sql:21` only runs `ALTER COLUMN slug DROP NOT NULL`, and neither level line reads nullability — TABLES reads only `CREATED_TABLES` presence (`src/cobalt/db_migrations/cli.py:468`) and FINGERPRINT counts columns and relations and hashes view text (`cli.py:378-387`), so a database at `0011` + no `0013` prints the same `TABLES 0011` and `FINGERPRINT …` as one at `0013`, and `gate.sh:310-313` then prints `LEVEL 0013`. The same holds for any constraint, index or default a `0001`–`0013` migration sets.
RUN: COMMAND `grep -n -F "attnotnull" src/cobalt/db_migrations/cli.py`
EXPECT: no output (exit 1): the level lines never read a NOT NULL mark, so `0013` present or absent prints the same two lines.

FINDING O2
ROW: X1 (L1)
CLAIM: on the REAL creator map, `TABLES 0011` prints for a marks picture other than "every `0004`–`0011` table present, every `0016`+ table absent" (one table flipped either way) — `cli.py:427-449`.
RUN: TEST `tests/cobalt/test_migrate_level.py`
```python
def test_check_x1_the_real_map_prints_tables_0011_only_for_the_one_picture():
    creators = cli._table_creators()
    at_0013 = {t: m <= "0011" for t, m in creators.items()}
    assert cli._tables_line(creators, at_0013) == "TABLES 0011"
    for table, creator in creators.items():
        flipped = {**at_0013, table: not at_0013[table]}
        assert cli._tables_line(creators, flipped) != "TABLES 0011", (table, creator)
```
EXPECT: if the claim is true, `AssertionError: (<table>, <creator>)` for the flip that still prints `TABLES 0011`.

FINDING O3
ROW: X2 (L2)
CLAIM: the lists file is byte-equal to `BUILD-HUB.md` as this branch's BASE has it, but `main` has moved since `a09f0862`; if `main`'s BUILD-HUB W / THE LOCK commands changed, the combined tree's `gate-lists.md` differs from the hub by at least one byte (`ops/desk/gate-lists.md:23-42` against the hub of `main`).
RUN: COMMAND `git -C /Users/cobalt/cobalt log --oneline a09f0862..main -- "docs/40 - DevDocs/prompts/BUILD-HUB.md"`
EXPECT: one or more commits; then `git -C /Users/cobalt/cobalt diff a09f0862 main -- "docs/40 - DevDocs/prompts/BUILD-HUB.md"` shows a changed `(a)`/`(b)`/`(c)`/`(c2)`/`(c3)`/`(c3r)`/`(e)`/`(f)` or `<FP>` line.

FINDING O4
ROW: X2 (L2)
CLAIM: a string `gate.sh` executes differs from `BUILD-HUB.md` W at this tip by a byte (`tests/ops/test_gate.py:247-259` would fail; `:225-244` would show a call argv off the lists file).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py`
EXPECT: if the claim is true, a failure in `test_the_lists_file_and_the_hub_files_say_the_same_commands_byte_for_byte` or `test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order`.

FINDING O5
ROW: L2 (ALLOWED SKIPS)
CLAIM: `DEPLOY-HUB.md:107` says "the same test and reason at a moved line is inside the set", but `gate.sh:430-438` covers `tests/cobalt/test_cards_picks.py:388` only at line `388`: the same skip and reason at `:390` is printed `OUTSIDE the allowed set: …`.
RUN: TEST `tests/ops/test_gate.py`
```python
def test_check_o5_an_allowed_skip_at_a_moved_line_is_not_marked_outside(gate):
    wt, repo, job, env, calls, script = gate
    line = "SKIPPED [1] tests/cobalt/test_cards_picks.py:390: S2-P2's card_score column is present on cobalt_dev"
    set_script(script, pytest=[{"out": line + "\n4 passed, 1 skipped in 0.1s", "rc": 0}])
    done = run_gate(env, "withdb")
    assert done.returncode == 0, done.stdout + done.stderr
    assert line in done.stdout.splitlines()
```
EXPECT: if the claim is true, `AssertionError` — stdout holds `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_cards_picks.py:390: …` instead of the bare line.

FINDING O6
ROW: X5 (L5)
CLAIM: `recut` recuts a deploy whose rollback ran, or reuses an attempt name in use (`ops/desk/desk-launch.sh:860-895`).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_recut.py`
EXPECT: if the claim is true, a failure in `test_a_deploy_whose_rollback_ran_is_refused`, `test_an_attempt_name_already_present_is_never_reused` or `test_a_recut_of_a_recut_counts_from_the_cards_own_attempt`.

FINDING O7
ROW: X4 (L3)
CLAIM: with `LC_ALL=C` the output of a desk reader changes: `desk-watch.sh`, `card-fill.sh`, `deploy-card.sh` (its `sort -u` at `ops/desk/deploy-card.sh:172`, its `· before ` byte search at `:154`) or `desk-list.sh` (the `·` separator printed by `python3` at `ops/desk/desk-list.sh:16`, read by `desk-context.sh:44-49`).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py tests/ops/test_card_fill.py tests/ops/test_deploy_card.py tests/ops/test_desk_list.py tests/ops/test_desk_context.py tests/ops/test_desk_size_guard.py`
EXPECT: if the claim is true, a failure whose first line shows an order or a character that differs.

X3 (`dev-clean`): OUT OF SCOPE — the card's `## NOT IN THIS JOB` ("The devfix verbs (dev-clean, dev-level, the VERB key): card 03b"); no `dev-clean` file is in the diff (`## Scope`).
Read, no finding: L4's copy is the source byte for byte at `bcf4c68f` (`git diff a09f0862 bcf4c68f -- ops/desk/desk-list.sh` → blob `b27bdcab`; `git diff --no-index /Users/cobalt/.claude/ops/desk-list.sh ops/desk/desk-list.sh` → `index b27bdcab..9fc95c09`, the header, the export and the `id` skip only). L3's range scripts (job-clean, deploy-card, release/take-devdb-lock, gate-clean, stage-set, preflight, desk-launch, gate) each carry one `é`/capital refusal test (Grep `L3` over `tests/ops`).

## Findings
none (house A: none).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "attnotnull" src/cobalt/db_migrations/cli.py` | no output, exit 1 (the level lines read no NOT NULL mark; `0013_tunables_slug_nullable.sql:21` is `ALTER TABLE "user".tunables ALTER COLUMN slug DROP NOT NULL;`, its only DDL) | REJECTED — card L1: FINGERPRINT is "computed by the three reads of BUILD-HUB.md THE LOCK's `<FP>` query, byte for byte the same SQL", and card `## RECORDS`: "the level is TABLES (from CREATED_TABLES) plus the FINGERPRINT; LEVEL 0013 is the gate's comparison". The blind spot is the ruled design: OPEN |
| O2 | Opus | test added to `tests/cobalt/test_migrate_level.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_migrate_level.py::test_check_x1_the_real_map_prints_tables_0011_only_for_the_one_picture` | `1 passed in 0.04s` | NOT HELD — removed again with Edit |
| O3 | Opus | `git -C /Users/cobalt/cobalt log --oneline a09f0862..main -- "docs/40 - DevDocs/prompts/BUILD-HUB.md"` | no output: `main`'s BUILD-HUB.md is unchanged since BASE | NOT HELD |
| O4 | Opus | one run for O4, O6, O7 together (the three named commands' files in one call): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py tests/ops/test_desk_launch_recut.py tests/ops/test_desk_watch.py tests/ops/test_card_fill.py tests/ops/test_deploy_card.py tests/ops/test_desk_list.py tests/ops/test_desk_context.py tests/ops/test_desk_size_guard.py` (background) | `150 passed, 1 xfailed, 15 warnings in 49.09s`, exit 0 | NOT HELD |
| O5 | Opus | test added to `tests/ops/test_gate.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::test_check_o5_an_allowed_skip_at_a_moved_line_is_not_marked_outside` | `1 failed, 15 warnings in 1.57s`; first failing line `E       assert "SKIPPED [1] tests/cobalt/test_cards_picks.py:390: S2-P2's card_score column is present on cobalt_dev" in ['proof-only: on cobalt_dev, nothing CHANGED — …', 'LEVEL 0013', …, 'with-DB 9/0', ...]`; the gate's log (Grep tool) line 78: `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_cards_picks.py:390: S2-P2's card_score column is present on cobalt_dev` — red for the stated reason | REJECTED — card `## RECORDS` (R82): ASK DESK 9 KEEP ("the exit does not change … Card 02 decides whether a mark becomes a red"); and `gate-lists.md` names `:388` by line with no reason words to match a moved line by, as DEPLOY-HUB.md:107 lists it — matching by reason would be words the hub does not give (L1). OPEN. The test was removed again with Edit (a red left in `tests/ops` would hold the next gate) |
| O6 | Opus | the O4 run (`tests/ops/test_desk_launch_recut.py` inside it) | green | NOT HELD |
| O7 | Opus | the O4 run (the six reader test files inside it) | green | NOT HELD |

No HELD finding: no `wip(adoption-scripts): check red` commit.

## FIXES
none.

## Suites
`suites: as built (no commit)`. From the build report (W on `0a4a7743`): offline `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 636.35s` · with-DB pass 1 `674 passed, 7 skipped, 3813 deselected, 2 xfailed` + pass 2 `173 passed, 1 deselected` = 847 · live-note `146 passed, 1 skipped` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed, proven gone (W, third take)` · `RESTARTS: com.cobalt.radar`. No lock taken by this check; `ls <WT>/.env` → `No such file or directory` (13:50).

## Scope
Path union `a09f0862..0a4a7743` (PREFLIGHT): `src/cobalt/db_migrations/cli.py`; `ops/desk/` — `authorize.sh`, `card-fill.sh`, `deploy-card.sh`, `desk-commit.sh`, `desk-context.sh`, `desk-done.sh`, `desk-handover.sh`, `desk-launch.sh`, `desk-list.sh` (new), `desk-row.sh`, `desk-wake.sh`, `desk-watch.sh`, `gate-clean.sh`, `gate-lists.md` (new), `gate.sh`, `house-probe.sh`, `install-fixed.sh`, `job-clean.sh`, `order-open.sh`, `preflight.sh`, `release-devdb-lock.sh`, `stage-copy.sh`, `stage-set.sh`, `take-devdb-lock.sh`, `wait-desk-idle.sh`, `wait-stop-line.sh`; `tests/cobalt/test_migrate_level.py` (new), `tests/cobalt/test_migrate_proof.py`; `tests/ops/` — `test_deploy_card.py`, `test_desk_context.py` (new), `test_desk_launch_prechecks.py`, `test_desk_launch_recut.py` (new), `test_desk_list.py` (new), `test_devdb_lock.py`, `test_gate.py`, `test_gate_clean.py`, `test_house_probe.py`, `test_locale.py` (new), `test_preflight.py`, `test_stage_set.py`, `test_desk_launch_devfix.py`, `test_desk_size_guard.py`; docs: the build report and `docs/40 - DevDocs/cobalt/db_migrations/cli.md`. Every non-docs path is in a row's files (L3 covers every `ops/desk/*.sh` and each script's existing test file) except `authorize.sh`'s parse rewrite (ASK DESK 8) and `test_desk_launch_devfix.py` / `test_desk_size_guard.py` (ASK DESK 7) — both KEEP by the judge (card `## RECORDS`, R82). This check committed nothing.

## Checked against the branch
- (i) `git log --oneline 0a4a7743..HEAD -- . ":(exclude)docs"` → no output (no commit of this check); `<tip now>` = `0a4a7743`.
- (ii) no commit of this check: nothing to widen.
- (iii) the fence: `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/BRAIN-HUB.md" ops/desk/deploy-step0.sh ops/desk/deploy-outage.sh ops/desk/deploy-smoke.sh ops/desk/job-run.sh` → no output.
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-scripts-1003`.
- (vi) TREE STATE: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → `8aad8b2e` (`cli.py`, `test_migrate_level.py`), `1befca95` (`cli.py`, `test_migrate_proof.py`), `4e88fd64` (`tests/cobalt/test_migrate_level.py | 201 +++`, new). No new migration file. `tests/cobalt/test_migrate_level.py` is a NEW WITH-DB TEST FILE (`test_with_db_the_two_lines_match_the_hubs_fingerprint_query`, `@requires_db`, `test_migrate_level.py:188-189`) while the card says `TREE STATE: unchanged` → **TREE STATE NOT CARRIED — tests/cobalt/test_migrate_level.py** (`## DECISIONS`). Fact beside it: the build ran it inside the hub's unchanged pass-1 command at `0013` (build report W (c): no skip and no failure names it; run alone `1 passed`), so no pass command changed.
- (vii) card `## RECORDS`: `ls /Users/cobalt/.claude/ops/desk-list.sh` → `/Users/cobalt/.claude/ops/desk-list.sh` (present). The sha256 is not on this check's list; identity shown by blob instead: `git diff a09f0862 bcf4c68f -- ops/desk/desk-list.sh` → `index 00000000..b27bdcab`, and `git diff --no-index /Users/cobalt/.claude/ops/desk-list.sh ops/desk/desk-list.sh` → `index b27bdcab..9fc95c09` (the source is blob `b27bdcab`).
- (viii) L32: this report holds no ticker, price or date of his; the `F` values are `cobalt_dev` catalog counts quoted from the build report.

## OPEN
- O1 (X1) — REJECTED. `LEVEL 0013` cannot tell a `cobalt_dev` with `0013` from one without it: `0013` only drops a NOT NULL, which neither TABLES nor FINGERPRINT reads (`cli.py:378-387`, `:468`; grep `attnotnull` → nothing). The same goes for any constraint, index or default from `0001`–`0013`, and for a dropped column offset by an added one (FINGERPRINT counts). What would settle it: a ruling that the level must see constraints, then a with-DB test that drops `0013`'s effect inside a rolled-back transaction and expects the two lines to differ. That needs a FINGERPRINT that is no longer the hub's `<FP>` byte for byte, so it changes card L1. Otherwise the limit is accepted as it is.
- O5 (L2) — REJECTED. A pass-1 skip of an allowed test at a moved line is printed `OUTSIDE the allowed set: …` (`gate.sh:430-438`), where DEPLOY-HUB.md:107 calls it inside the set. The exit does not change. What would settle it: card 02, when it decides whether a mark becomes a red, gives each `gate-lists.md` `## ALLOWED SKIPS` item the reason words its line must hold, so `covered()` can match path + reason without the line. The test above is the red to start from.

## CONTINUE
next: none — CHECK DONE (pass 1).

## DECISIONS
- TREE STATE NOT CARRIED — `tests/cobalt/test_migrate_level.py` (a new with-DB test file, `CHECK-HUB.md` `## 7` (vi)) on a card that says `TREE STATE: unchanged`. Card L1 itself orders this test ("With-DB, marked, at `0013`"). It runs inside the hub's unchanged pass-1 command, and pass 1 and pass 2 needed no added deselect or id. So the pass lists are what `unchanged` claims, but the rule's letter is not met. Safe default taken: `ready: NO`, nothing changed. The judgment seat either confirms that `unchanged` holds for a with-DB test that runs at `0013`, which makes it `ready: YES` with nothing to build, or orders a TREE STATE row.
- OPEN O1 (X1, `house B: none available` — R47, no outside house for this program): `LEVEL 0013` is blind to `0013`'s own change and to every constraint, index or default up to `0013`. This is the design the judge ruled (TABLES + FINGERPRINT, the `<FP>` SQL byte for byte). Safe default taken: nothing changed; it goes to the follow-up list unless the judgment seat orders otherwise.
- OPEN O5 (L2, `house B: none available`): an allowed skip at a moved line is marked `OUTSIDE the allowed set`. The mark is advisory (ASK DESK 9 KEEP). Safe default taken: nothing changed; it is handed to card 02 with the test in `## RUNS`.

## RECORDS
- Dropped findings: none (house A: none).
- House: none launched — `HOUSE A: none — overruled 2026-10-02 R47` (proved in `## AUTHORIZATION`); `<S>` not created for a house; no staging, no probe.
- REFUSED, not needed: `grep -n -F "test_cards_picks.py:390" /private/var/folders/4b/…/test_check_o5_an_allowed_skip_0/wt/.gate-logs/x-job-withdb-20261003-135006.log` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Done with the Grep tool instead (line 78 quoted in `## RUNS`).
- A mistyped read, harmless: `git diff --no-index /Users/cobalt/.claude/ops/desk-list.sh /Users/cobalt/cobalt-wt/adoption-scripts-1003/.git` (meant the `bcf4c68f` blob; it diffed against the worktree's `.git` pointer file). It read only and changed nothing; the blob was then read with `git diff a09f0862 bcf4c68f -- ops/desk/desk-list.sh`.
- O4, O6 and O7 were run as one pytest call over their named files (`## RUNS`). The O5 test was added to `test_gate.py` while that run was in flight. Its result (`150 passed`, no failure) shows the run had collected the file before the edit.
- Lock takes: none. `.env` absent at every read.
- L74: a system block arrived at the start of this session asking that commits end with a `Claude-Session:` line. Recorded, not acted on: this check made no commit, and `CHECK-HUB.md` L74 says commits carry `Co-Authored-By` only.
- files opened: 19 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report (`## RESTARTS` on); `src/cobalt/db_migrations/cli.py`; `tests/cobalt/test_migrate_level.py`; `ops/desk/gate.sh`; `ops/desk/gate-lists.md`; `ops/desk/desk-context.sh`; `tests/ops/test_desk_context.py`; `tests/ops/test_desk_list.py`; `tests/ops/test_locale.py`; `tests/ops/test_gate.py`; `0013_tunables_slug_nullable.sql`; `0014_radar_handicap.sql`; `0020_drc_build_kinds.sql`; `DEPLOY-HUB.md` (`:107`, `:180-186`); `areas/cobalt.md` (from `## What Cobalt is`); the background run's output file.
- Check of `adoption-scripts`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-scripts · pass: 1 · tip: 0a4a7743 · house A: none (overruled 2026-10-02 R47) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: NO · decisions: 3 · for Dejan: 0
