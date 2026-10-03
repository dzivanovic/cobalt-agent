# deploy-steps — CHECK, pass 1 — 2026-10-03

## §0 Headline
Pass 1 of `deploy-steps` (card 20), house A Grok (`FINDINGS: 3`) plus 4 of my own: 7 findings, 7 held, 7 fixed at `bb59ba34` inside the rows' files.
Fixed: `deploy-outage.sh` now traps QUIT (it left both residents down), kickstarts an agent that drops at the final status, reads a relative card; `deploy-step0.sh` P7 now catches an edited migration, (iv) needs the whole JOB name, the dry run names the real reads; one weak test assertion strengthened.
Suites green: tests/ops 556/0, offline 3737/0, live-note 146/0; RESTARTS: none; DB: none (no lock, no `.env`).
OPEN 1: Grok's own G1 test cannot pass under any fix (its stub kills the agent on every read); the defect is fixed and pinned by the check's test → house B: needed (Sol is up), ready: NO.

## L74
The session's attribution reminder asked for a `Claude-Session:` line on commits. Recorded once here as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/20-deploy-steps-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../20-deploy-steps-card.md"` | 0 | `65965076c4eeb2190260abd0c23c11f7dd5b450f` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- ".../20-deploy-steps-card.md"` | 0 | (nothing) |
| STANDING (09-30 R60) | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 commit | `git -C … log -1 --format=%H -S"\| R60 \|" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10 …) … card 20 (deploy-outage.sh) keeps a Grok check … \| HIS RULING · APPROVED \|` |
| R47 commit | `git -C … log -1 --format=%H -S"\| R47 \|" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` |
| R157 commit | `git -C … log -1 --format=%H -S"\| R157 \|" -- cto-2026-10-02.md` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| gate R17 | `grep -n "^\| R17 " cto-2026-09-24.md` | 0 | `35:\| R17 \| 07:32 ET \| … STANDING: Bash(grok *) is a PRE-APPROVED string …` (one row) |
| gate R19 | `grep -n "^\| R19 " cto-2026-09-24.md` | 0 | `37:\| R19 \| 07:36 ET \| … STANDING: the four house strings are pre-approved …` (one row) |
| R19 commit | `git -C … log -1 --format=%H -S"\| R19 \|" -- cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 12:39:46 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/deploy-steps-1003` |
| tip | `git log --oneline -1` | 0 | `b4f1c2f0 docs(deploy-steps): build report — 735f5ed8` |
| above tip docs-only | `git log --stat --format=%h 735f5ed8..HEAD` | 0 | `b4f1c2f0` · `.../reports/deploy-steps-build-2026-10-03.md \| 53 +++…` (docs only) |
| BUILT | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: deploy-steps · tip: 735f5ed8 \| on a09f0862 \| migration: none \| offline 3737/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline a09f0862..735f5ed8` | 0 | `735f5ed8 feat … PATH guard (D5, D2 amended)` · `668344ac wip red — D5 guard, D2 amended` · `dfddc1be docs build report` · `775aedfd feat … three scripts (D1-D4)` · `7a9db92b wip red — D1-D4` (5 commits) |
| range stat | `git log --stat --format=%h a09f0862..735f5ed8` | 0 | 735f5ed8: tests/ops/conftest.py +31 · 668344ac: tests/ops/test_conftest_guard.py +58, tests/ops/test_deploy_outage.py +45 · dfddc1be: build report +261 · 775aedfd: ops/desk/deploy-outage.sh +404, ops/desk/deploy-smoke.sh +358, ops/desk/deploy-step0.sh +470, three test files ±12 · 7a9db92b: test_deploy_outage.py +359, test_deploy_smoke.py +250, test_deploy_step0.py +406 |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/deploy-steps-1003/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..735f5ed8` | 0 | `docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md` · `ops/desk/deploy-outage.sh` · `ops/desk/deploy-smoke.sh` · `ops/desk/deploy-step0.sh` · `tests/ops/conftest.py` · `tests/ops/test_conftest_guard.py` · `tests/ops/test_deploy_outage.py` · `tests/ops/test_deploy_smoke.py` · `tests/ops/test_deploy_step0.py` — every path under ops/, tests/ops/ or docs/ |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house gates | R17, R19 (AUTHORIZATION) | 0 | one row each, R19 commit non-empty |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | `1.2.16` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` | 0 | `OK` = UP |
| seats | card `HOUSE A: Grok` (10-02 R47) | — | house A: Grok · house B, if needed: Sol (first UP that is not A) · card `HOUSE B: as needed` |
| first real use | `uv run pytest *`, `git add *`, `git commit *` | — | proven at first use (## 4) |

## Files copied
- diff: `git log -p a09f0862..735f5ed8 -- . ":(exclude)docs"` (background) → Write `<S>/diff.md` with its header; `grep -c "^commit "` → `4` in the copy and `4` in the source output (the range has 5 commits; `dfddc1be` touches docs only: `git log --oneline a09f0862..735f5ed8 -- . ":(exclude)docs"` → 4 lines). `wc -l`: copy 2529 = source 2530 − the harness `[exited with code 0]` line and its blank + the header line. Size 99924 bytes.
- `<S>/rulings.md`: R47, R157 rows under their grep lines (Write).
- Every other copy by `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <src> <dst>` (cmp-proved byte-identical, `COPIED <bytes>`):

| file | bytes |
|---|---|
| card `20-deploy-steps-card.md` | 9215 |
| build report `deploy-steps-build-2026-10-03.md` (worktree) | 42015 |
| `brain-unattended-2026-10-02.md` | 37859 |
| `deploy-2026-09-30-1-attempt1.md` | 13944 |
| `deploy-2026-09-30-1-attempt2.md` | 15400 |
| `deploy-2026-09-30-1-attempt3.md` | 21429 |
| `deploy-2026-10-01-1.md` | 17967 |
| wt `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` | 57453 |
| wt `docs/40 - DevDocs/prompts/2026-10-02/25-deploy-scripts-card.md` | 15213 |
| wt `ops/desk/deploy-outage.sh` | 13704 |
| wt `ops/desk/deploy-smoke.sh` | 12094 |
| wt `ops/desk/deploy-step0.sh` | 19169 |
| wt `ops/desk/authorize.sh` | 7074 |
| wt `ops/desk/gate-clean.sh` | 5083 |
| wt `ops/desk/deploy-card.sh` | 11441 |
| wt `tests/ops/conftest.py` | 1039 |
| wt `tests/ops/test_conftest_guard.py` | 2148 |
| wt `tests/ops/test_deploy_outage.py` | 16413 |
| wt `tests/ops/test_deploy_smoke.py` | 10166 |
| wt `tests/ops/test_deploy_step0.py` | 17371 |

- `<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS whole, the Files paragraph.
- House A launch: `date` → `Sat Oct  3 12:47:56 EDT 2026`; R17, R19 one row each; `ls -la <S>` → diff.md 99924, files/, HOUSE-INSTRUCTIONS.md 11921, rulings.md 735; `cd <AGY>`; GROK spelling of `## 1` (5), background, timeout 2700000; `cd <WT>`; `git status --short --branch` → `## ops/deploy-steps-1003`.

## OWN FINDINGS
Written before house A's list was opened. Read: the card, rulings, the diff `a09f0862..735f5ed8`, the three scripts and five test files at the tip, `DEPLOY-HUB.md` (worktree) STEP-0 / P1 / STEP-D0–D2 / STEP-4 / 4.7 / STEP-5, the build report's RESTARTS, W, FOR THE CHECK, DECISIONS and last line, `areas/cobalt.md` (What Cobalt is; Build rules down). Build DECISION 2 (the holiday form) and 3, 5, 6 were answered by the judge (card `## RECORDS`): not re-opened (L77).

FINDING O1
ROW: D2 / X1
CLAIM: `ops/desk/deploy-outage.sh:355-358` traps only EXIT, INT, TERM and HUP; any other signal whose default action ends the shell (QUIT, USR1, USR2, ALRM) between the first bootout and the bootstrap ends the script with the residents down and no `RESIDENTS UP (trap)`.
RUN: TEST `tests/ops/test_deploy_outage.py`
```python
@pytest.mark.parametrize("sig", [signal.SIGQUIT, signal.SIGUSR1, signal.SIGUSR2, signal.SIGALRM])
def test_o1_any_ending_signal_between_bootout_and_bootstrap_brings_every_label_up(box, sig):
    proc = subprocess.Popen(
        box.args(f"{ASET},{RADAR}"), env=dict(box.env, STUB_MARK_ON=RADAR, STUB_HOLD="2"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace",
    )
    deadline = time.monotonic() + 30
    while not box.mark.exists():
        assert time.monotonic() < deadline, "the bootout never ran"
        time.sleep(0.05)
    proc.send_signal(sig)
    out, err = proc.communicate(timeout=60)
    assert proc.returncode != 0, out + err
    st = box.launchd()["labels"]
    assert ASET in st and RADAR in st, (out, err)
    assert "RESIDENTS UP (trap)" in out, out + err
```
EXPECT: on the tip `AssertionError` at `assert ASET in st and RADAR in st` (both labels booted out, none bootstrapped).

FINDING O2
ROW: D1 / X3
CLAIM: `ops/desk/deploy-step0.sh:413-418` compares only the NAMES in `git show <head>:src/cobalt/db_migrations/` against main's, so a head that EDITS an existing migration file passes `P7 migrations` on a `MIGRATIONS: none` card, while the hub's P7 (`DEPLOY-HUB.md:65`, `git diff --stat main <head> -- src/cobalt/db_migrations` → NOTHING when `none`) fails it.
RUN: TEST `tests/ops/test_deploy_step0.py`
```python
def test_o2_a_head_that_edits_an_existing_migration_fails_p7_on_a_none_card(desk):
    mig = desk.repo / "src" / "cobalt" / "db_migrations"
    git(desk.repo, "checkout", "-q", "-B", "ops/beta", "main")
    (desk.repo / "src" / "beta.py").write_text("beta = 2\n")
    (mig / "0001_base.sql").write_text("-- base, edited by beta\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "beta code edits a migration")
    desk.tip["beta"] = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    desk.head["beta"] = desk.tip["beta"]
    git(desk.repo, "checkout", "-q", "main")
    desk.check["beta"].write_text(f"# check beta\n\n{check_line(desk.tip['beta'])}\n")
    desk.recard()
    done = desk.run()
    assert done.returncode == 1, done.stdout
    assert last_line(done).startswith("FAILED STEP-0: P7 migrations — "), done.stdout
```
EXPECT: on the tip `AssertionError` at `assert done.returncode == 1` (the run ends `STEP-0 OK — window: (iii)`).

FINDING O3
ROW: D1 / X4
CLAIM: `ops/desk/deploy-step0.sh:177` matches the card's JOB as a substring of the ruling row, so an override naming another job whose name merely contains this JOB (`x-set-2` for `x-set`) opens window (iv), while the hub's (iv) (`DEPLOY-HUB.md:59`) needs a row that "names this card's `JOB`".
RUN: TEST `tests/ops/test_deploy_step0.py`
```python
def test_o3_an_override_for_a_job_that_only_contains_this_job_does_not_open_the_window(desk):
    desk.write_rulings(
        "| R2 | 09:05 ET | HIS RULING: the set ships. | HIS RULING · APPROVED |\n"
        "| R3 | 09:10 ET | HIS RULING: overrules L66 for deploy x-set-2 at 14:00. | HIS RULING · APPROVED |\n"
    )
    desk.commit("override for x-set-2")
    desk.recard(rulings="2026-01-02 R2, R3")
    done = desk.run("--window", now=THURSDAY_1400)
    assert done.returncode == 1, done.stdout
```
EXPECT: on the tip `AssertionError` at `assert done.returncode == 1` (stdout `WINDOW (iv)`).

FINDING O4
ROW: D2
CLAIM: `ops/desk/deploy-outage.sh:141` enters `$REPO` before `:162` hands `"$card"` to `deploy-step0.sh --window`, so a card given by a path relative to the caller's directory (checked present at `:68`) is refused as `REFUSED: window — REFUSED: no such card …` although the window is open: the outage cannot run on a relative card path (nothing goes down).
RUN: TEST `tests/ops/test_deploy_outage.py`
```python
def test_o4_a_card_given_by_a_relative_path_runs_the_outage(box):
    done = subprocess.run(
        ["sh", str(SCRIPT), box.card.name, f"{ASET},{RADAR}", "MERGED"], cwd=box.root,
        env=box.env, capture_output=True, text=True, errors="replace", timeout=120,
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "OUTAGE DONE 0s"
```
EXPECT: on the tip `AssertionError` at `assert done.returncode == 0` with stderr `REFUSED: window — REFUSED: no such card: deploy-x-set-card.md; nothing is down`.

## Findings
House A `Grok` completed 13:11 (`date` at the notice: `Sat Oct  3 13:12:06 EDT 2026`); `<S>/house-a.md` 3463 bytes, written by Grok; its stdout: the path, then `[exited with code 0]`; closing line `FINDINGS: 3`. THE DROP: `grep` of each `RUN:` — all three blocks carry a test function or an allowed command; none dropped.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| G1 | Grok | X1 | After every label leaves `down`, the final `cobalt.sh status` can fail; the trap restores nothing, so the agent stays down and is reported `up:`. | TEST |
| G2 | Grok | D4 | `--dry-run` of `deploy-step0.sh` names `tail -n 3` and `rev-parse --short=8`, while the run executes `grep -v … \| tail -n 1` and `rev-parse --verify --quiet`. | TEST |
| G3 | Grok | D2 | `test_deploy_outage.py:302` `("bootstrap", RADAR) not in acts(box) or RADAR in st` is true whenever no RADAR bootstrap is recorded: too weak. | COMMAND |

## Dropped
none

## RUNS
Each test placed in the file it names with the Edit tool (no form repair needed), run on the tip `735f5ed8` code: `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>` (the seven together; O2 and O3 again with `--tb=line`). Summary of the joint run: `6 failed, 3 passed, 15 warnings in 13.33s` (O1 has four parameters).

| id | source | run | output (first failing line) | verdict |
|---|---|---|---|---|
| O1 | Opus | TEST `test_deploy_outage.py::test_o1_any_ending_signal_between_bootout_and_bootstrap_brings_every_label_up` ×4 | `[3]` (SIGQUIT): `AssertionError: ('', '')` · `assert ('com.cobalt.aset' in {})` at `:429` — both labels booted out, nothing bootstrapped, no output. `[30]`, `[31]`, `[14]` (USR1, USR2, ALRM): passed | HELD for SIGQUIT (the shell dies without its EXIT trap); NOT HELD for USR1, USR2, ALRM (the shell's EXIT trap ran). The test is kept whole: the three green parameters pin the fix's added traps |
| O2 | Opus | TEST `test_deploy_step0.py::test_o2_a_head_that_edits_an_existing_migration_fails_p7_on_a_none_card` | `assert 0 == 1` at `:426`; the run's rows `P7 listing 2 · … · new against main: none`, `P7 migrations · … · heads add: none; MIGRATIONS names: none`, last line `STEP-0 OK — window: (iii)` | HELD |
| O3 | Opus | TEST `test_deploy_step0.py::test_o3_an_override_for_a_job_that_only_contains_this_job_does_not_open_the_window` | `assert 0 == 1` at `:438`; stdout `P1 window · … · Thu 2026-01-08 14:00 ET — holds: (iv) his per-case override 2026-01-02 R3` / `WINDOW (iv)` | HELD |
| O4 | Opus | TEST `test_deploy_outage.py::test_o4_a_card_given_by_a_relative_path_runs_the_outage` | `AssertionError: REFUSED: window — REFUSED: no such card: deploy-x-set-card.md; nothing is down` at `:438` | HELD |
| G1 | Grok | TEST `test_deploy_outage.py::test_final_agent_status_failure_after_up_does_not_kickstart_again` | `assert 1 >= 2` at `:475`; `starts` = `[['kickstart', 'gui/501/com.cobalt.agent']]`; stdout `FAILED OUTAGE: com.cobalt.agent — cobalt.sh status is not ONLINE:   Cobalt is OFFLINE. · residents: up: com.cobalt.agent · down: none` | HELD — red for its stated reason. Its test cannot pass under ANY fix: its stub sets the agent OFFLINE on every `status` from the third on (`if n >= 3: st['agent'] = None`), so its second assertion `box.launchd().get("agent") not in (None, 503)` is false after every kickstart the script can make. Run once against the fix (appended, then removed, never committed): `assert None not in (None, 503)` at `:512`, the first assertion now passing (`'next': 902`: two kickstarts). The claim is pinned instead by the check's own `test_g1_an_agent_offline_at_the_final_status_is_kickstarted_by_the_trap` (the agent drops once, at step 3's read): red on the tip `assert [['kickstart'...obalt.agent']] == [['kickstart'...obalt.agent']]` — `Right contains one more item` at `:470`. The house test itself stays OPEN (UNSETTLED) |
| G2 | Grok | TEST `test_deploy_step0.py::test_dry_run_names_the_p2_and_p3_commands_the_script_runs` | `assert 'grep -v' in 'WOULD RUN: sh …authorize.sh deploy …'` at `:446`; the would-run lines show `tail -n 3 "…/alpha-check.md"` and `rev-parse --short=8 e8bac31f ops/alpha` | HELD |
| G3 | Grok | COMMAND `grep -n 'bootstrap", RADAR) not in acts' tests/ops/test_deploy_outage.py` | `302:    assert ("bootstrap", RADAR) not in acts(box) or RADAR in st` | HELD (the output shown; the disjunction is true whenever no RADAR bootstrap is recorded) |

Red commit before any fix: `27555266 wip(deploy-steps): check red — O1 O2 O3 O4 G1 G2` (test files only; the G1 house test kept out of the tree, the check's G1 test in).

## FIXES
One commit, `bb59ba34 fix(deploy-steps): outage traps every ending signal, re-downs a dropped agent, reads a relative card; step0 P7 diff and whole-JOB override, dry-run names the real reads (check O1 O2 O3 O4 G1 G2 G3)`, inside the rows' files (`ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`):

| id | fix |
|---|---|
| O1 | `deploy-outage.sh`: `trap 'on_signal QUIT' QUIT` (and USR1, USR2, ALRM explicitly) beside INT / TERM / HUP; `on_exit` ignores all seven while it restores; header updated. |
| O4 | `deploy-outage.sh`: a relative card is made absolute (`$(pwd)/$card`) before the script enters `$REPO`. |
| G1 | `deploy-outage.sh` step 3: the agent of the set not ONLINE at the final `cobalt.sh status` is put back in `down` before `fail`, so the trap kickstarts it and the residents line names it truly; header updated. |
| O2 | `deploy-step0.sh` P7: per head `git -C $REPO diff --name-status --no-renames main <head> -- src/cobalt/db_migrations` (the hub's P7 read): on a `none` card any line fails; otherwise only added `NNNN_` files and `__init__.py` pass; the `P7 migrations` row carries `other migration changes:`; the dry run names the command; header updated. |
| O3 | `deploy-step0.sh` (iv): the JOB must stand as a whole name in the ruling row (every character outside `[a-z0-9-]` read as a blank). |
| G2 | `deploy-step0.sh`: the P2 / P3 command strings (table column and `--dry-run`) are the reads that run: `grep -v '^[[:space:]]*$' "<report>" \| tail -n 1` and the two `rev-parse --verify --quiet --short=8 …^{commit}`. |
| G3 | `test_deploy_outage.py:302` → `assert ("bootout", RADAR) not in acts(box)` and `assert RADAR in st and st[RADAR]["pid"] == 502`. |

After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/ops/test_deploy_step0.py tests/ops/test_deploy_outage.py tests/ops/test_deploy_smoke.py tests/ops/test_conftest_guard.py` → `84 passed, 15 warnings in 46.40s` (the 75 the build added + 9 check tests). G3 alone → `1 passed, 15 warnings in 1.29s`.
DevDocs line: no page under `docs/40 - DevDocs/cobalt/` documents `ops/desk/` scripts (Grep of the three names there → no files; the build wrote none); none created (a new file is outside the rows' files). Each script's header comment carries the change.

## Suites
On `<tip now>` = `bb59ba34` (DB: none card: RESTARTS, then W (a0), (a), (e) and tests/ops):
- RESTARTS: `uv run cobalt jobs restarts a09f0862..HEAD` → exit 0; nine rows (`docs/…/deploy-steps-build-2026-10-03.md A DOCS -`, the three `ops/desk/deploy-*.sh A operator script; no Cobalt reader -`, the five `tests/ops/*.py A test/documentation; no resident -`), last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a09f0862` → the nine paths above, every one under `docs/`, `ops/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 9 paths)`.
- tests/ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `556 passed, 1 xfailed, 15 warnings in 232.97s (0:03:52)` (the build's 547 + 9 check tests).
- (a) offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 571.34s (0:09:31)`, 0 failed, 0 errors.
- (e) live-note: `ls <WT>/.env` → `No such file or directory`; `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.02s`; the skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).
- cobalt_dev: not taken (DB: none); no lock, no `.env` at any step.

## Scope
PREFLIGHT path union (build): `docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/conftest.py`, `tests/ops/test_conftest_guard.py`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_smoke.py`, `tests/ops/test_deploy_step0.py` — each a row's file (D1–D5) or the build report. The check's commits touch `ops/desk/deploy-outage.sh` (D2), `ops/desk/deploy-step0.sh` (D1), `tests/ops/test_deploy_outage.py` (D2), `tests/ops/test_deploy_step0.py` (D1): all inside the rows' files.

## Checked against the branch
- (i) `git log --oneline 735f5ed8..HEAD -- . ":(exclude)docs"` → `bb59ba34 fix(deploy-steps): … (check O1 O2 O3 O4 G1 G2 G3)` · `27555266 wip(deploy-steps): check red — O1 O2 O3 O4 G1 G2`. `<tip now>` = `bb59ba34`.
- (ii) `git log --stat --format=%h 735f5ed8..HEAD` → `bb59ba34`: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py` · `27555266`: `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py` · `b4f1c2f0`: the build report (docs). Every non-docs path in a row's files. No WIDENED.
- (iii) fence: `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → empty; `git log --oneline a09f0862..HEAD -- ops/desk/deploy-card.sh` → empty.
- (iv) `grep -n -F "def <test>"`: O1 `tests/ops/test_deploy_outage.py:418`, O4 `:435`, G1 (check's test) `:444`; O2 `tests/ops/test_deploy_step0.py:413`, O3 `:430`, G2 `:441`; G3 is the strengthened assertion in `test_a_bootout_that_leaves_the_label_loaded_fails_and_residents_stay_up` (a COMMAND finding, no red test of its own). `27555266` (red) sits below `bb59ba34` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/deploy-steps-1003`.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. Carried.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: nothing to run.
- (viii) L32: the values in this report are constructed test values (pids 501–503, 900–902, the 2026-01 test dates, `x-set`) or repo facts (commits, paths, counts); none of his.

COUNTING: findings 7 (O1–O4, G1–G3) · dropped 0 · held 7 · fixed 7 · held unfixed 0 · open 1.

## OPEN
- G1 (Grok) — UNSETTLED: the house's own test `test_final_agent_status_failure_after_up_does_not_kickstart_again` was red for its stated reason and the defect is fixed (`bb59ba34`, pinned by `test_g1_an_agent_offline_at_the_final_status_is_kickstarted_by_the_trap`), but the house test cannot pass under any fix: its stub sets the agent OFFLINE on every `status` from the third read on, so `box.launchd().get("agent") not in (None, 503)` is false after every kickstart (run against the fix: `assert None not in (None, 503)`, first assertion passing). It is not in the tree. WHAT WOULD SETTLE IT: house B reads the test against the fix and either accepts the check's companion test as the pin, or writes a test whose stub can come back up.

## CONTINUE
next: none — closed (the desk verifies and launches PASS-2)

## DECISIONS
none

## RECORDS
- Check of `deploy-steps`, pass 1: house A `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- House A Grok produced its list (`FINDINGS: 3`); no house produced nothing; Sol probe `OK` (UP) at PREFLIGHT — house B, when needed: Sol (the first house UP that is not house A).
- Dropped findings: none.
- REFUSED, not needed: `ls -la /bin/sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (it would have named the shell; the O1 run settled the question directly).
- The G1 house test was run once more against the fix, appended to `tests/ops/test_deploy_outage.py` and removed again with the Edit tool, never committed.
- The `cd`, the house launch and the return: `## Files copied` last line.
- No lock taken, no `.env` written, no extra lock take (DB: none).
- L74: one attribution reminder asking for a `Claude-Session:` line arrived (system reminder); recorded under `## L74`, not acted on.
- `<S>/opus-1.md` = this report as it stands at close, copied by `stage-copy.sh` (it holds `## OWN FINDINGS`, `## RUNS`, `## FIXES`, `## OPEN` whole).
- files opened: 15 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (THE LOCK, E2, RESTARTS, W), `DEPLOY-HUB.md` (worktree), the build report, `areas/cobalt.md` (two sections), `ops/desk/stage-copy.sh`, the diff output, the Sol probe output, Grok's stdout, `house-a.md`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`.

CHECK DONE · job: deploy-steps · pass: 1 · tip: bb59ba34 · house A: Grok FINDINGS: 3 · findings: 7 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: needed · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 15 · ready: NO · decisions: 0 · for Dejan: 0

# PASS 2

## §0 Headline
Pass 2 of `deploy-steps`, house B Sol (`FINDINGS: 11`): 9 held and fixed at `f04a1d56` inside the rows' files, 1 not held (SIGPIPE), 1 the run that settled pass 1's OPEN G1.
Fixed: step0 `LC_ALL=C` first; window (iv) needs a row that overrules and stands at HEAD; P2 always needs `held unfixed: 0` and `ready: YES`; P7 counts only `NNNN_*.sql`; the dry run prints one command per line in run order. The outage re-reads each label at the end. Smoke rows out of form are RED.
Suites green: tests/ops 564/0, offline 3737/0, live-note 146/0; RESTARTS: none; DB: none (no lock, no `.env`). Open 0 · ready: YES · decisions 0.

## L74
The session's attribution reminder again asked for a `Claude-Session:` line on commits (system reminder). Recorded once here as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Every gate re-run in this session, same answers as pass 1:

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../20-deploy-steps-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../20-deploy-steps-card.md"` | 0 | `65965076c4eeb2190260abd0c23c11f7dd5b450f` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- ".../20-deploy-steps-card.md"` | 0 | (nothing) |
| STANDING (09-30 R60) | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 commit | `git -C … log -1 --format=%H -S"\| R60 \|"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10 …) … card 20 (deploy-outage.sh) keeps a Grok check … \| HIS RULING · APPROVED \|` |
| R47 commit | `git -C … log -1 --format=%H -S"\| R47 \|"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): … \| HIS RULING · APPROVED \|` |
| R157 commit | `git -C … log -1 --format=%H -S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| gate R17 | `grep -n "^\| R17 " cto-2026-09-24.md` | 0 | `35:\| R17 \| 07:32 ET \| … STANDING: Bash(grok *) is a PRE-APPROVED string …` (one row) |
| gate R19 | `grep -n "^\| R19 " cto-2026-09-24.md` | 0 | `37:\| R19 \| 07:36 ET \| … STANDING: the four house strings are pre-approved …` (one row) |
| R19 commit | `git -C … log -1 --format=%H -S"\| R19 \|"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 13:28:35 EDT 2026` |
| pass 1 closed | `tail -n 3 "<CHECK REPORT>"` | 0 | last line `CHECK DONE · job: deploy-steps · pass: 1 · tip: bb59ba34 · house A: Grok FINDINGS: 3 · … · house B: needed · … · ready: NO …` → `<tip now>` = `bb59ba34` |
| branch | `git status --short --branch` | 0 | `## ops/deploy-steps-1003` |
| tip | `git log --oneline -1` | 0 | `bb59ba34 fix(deploy-steps): outage traps every ending signal, …` = pass 1's `tip:` |
| above TIP | `git log --stat --format=%h 735f5ed8..HEAD` | 0 | `bb59ba34`: deploy-outage.sh, deploy-step0.sh, test_deploy_outage.py · `27555266`: test_deploy_outage.py, test_deploy_step0.py · `b4f1c2f0`: the build report |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/deploy-steps-1003/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..bb59ba34` | 0 | the nine paths of pass 1 (build report, three `ops/desk/deploy-*.sh`, five `tests/ops/*.py`) — every one under ops/, tests/ops/ or docs/ |
| scratch | `ls <S>` | 0 | `diff.md files house-a.md HOUSE-INSTRUCTIONS.md opus-1.md rulings.md` (pass 1's; house A is never launched again) |
| house gates | R17, R19 (AUTHORIZATION) | 0 | one row each, R19 commit non-empty |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | `1.2.16` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` (background) | 0 | `OK` = UP (`tokens used 2,196`) |
| seats | pass 1's house A = Grok | — | house B = Sol (OpenAI): the first house UP in the seat order that is not Grok |

## Files copied
- `<S>/diff-b.md`: `git log -p a09f0862..bb59ba34 -- . ":(exclude)docs"` (background), Read whole, Write with its header. `grep -c "^commit "` → `6`; `git log --oneline a09f0862..bb59ba34 -- . ":(exclude)docs"` → 6 commits. `wc -l`: copy 2847 = source 2848 − the harness blank and `[exited with code 0]` line + the header. `wc -c`: copy 115183 = source 115098 − 22 (the harness tail) + 107 (the header line): byte count exact.
- Sol reads the originals by absolute path: no `files/` copy is made in this pass (copies are for Grok and Gemini only). `HOUSE-B-INSTRUCTIONS.md` says the `files/` copies are pass 1's at `735f5ed8` and points the four files pass 1 changed to the worktree.
- `<S>/HOUSE-B-INSTRUCTIONS.md`: the HOUSE TEXT verbatim with the HOUSE B paragraph before "EVERY FINDING", the card's ROWS, NOT IN THIS JOB, CHECK ASKS and RECORDS whole, the Files paragraph naming `diff-b.md`, `house-a.md`, `opus-1.md`.

- House B launch: `date` → `Sat Oct  3 13:36:57 EDT 2026`; R17, R19 one row each, R19 commit `5055151d…`; `ls -la <S>` → diff-b.md 115183, diff.md 99924, files/, house-a.md 3463, HOUSE-B-INSTRUCTIONS.md 12347, HOUSE-INSTRUCTIONS.md 11921, opus-1.md 26646, rulings.md 735; `cd <AGY>`; the SOL spelling of `## 1` (5) with `HOUSE-B-INSTRUCTIONS.md`, background, timeout 2700000; `cd <WT>`; `git status --short --branch` → `## ops/deploy-steps-1003`.

## Findings
House B `Sol` completed (`date` at the notice: `Sat Oct  3 13:48:45 EDT 2026`); output 10731 lines; its final message (after `tokens used 261,619`) written by me, byte for byte, to `<S>/house-b.md`; closing line `FINDINGS: 11`. THE DROP: every block carries `RUN:` with a test function or a command beginning `grep` / `uv run pytest`; none dropped. Ids S1–S11 (Sol's FINDING 1–11).

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| S1 | Sol | D1 | `deploy-step0.sh:55-57` sets `CALLER_LC_ALL` / `CALLER_LC_SET` before `export LC_ALL=C`: the card's "`export LC_ALL=C` first" is not met. | COMMAND |
| S2 | Sol | D3 | `deploy-smoke.sh` skips a `- ` SMOKE READS row not in its backtick form, silently: the run can say `SMOKE GREEN` without that row's line. | TEST |
| S3 | Sol | X1 | Step 2 drops each label from `down` after its own bootstrap and step 3 re-reads only the agent: a later bootstrap can leave an earlier label down under `OUTAGE DONE`. | TEST |
| S4 | Sol | D1 | P7 accepts any added `NNNN_` file, so `0002_beta.txt` satisfies `MIGRATIONS: 0002`. | TEST |
| S5 | Sol | X4 | (iv) takes any approved row holding `L66`/`L43` and the JOB, even one that affirms the window; the hub needs a row that overrules it. | TEST |
| S6 | Sol | X4 | (iv) reads the row from the working tree and proves only some commit with `-S"\| R<n> \|"`: an uncommitted rewrite opens the window under `--window`. | TEST |
| S7 | Sol | X1 / OPEN G1 | The OPEN G1 is settled by `test_g1_an_agent_offline_at_the_final_status_is_kickstarted_by_the_trap`. | COMMAND |
| S8 | Sol | D1 | P2 reads the needed statuses only from the row's backticked literals: a SHIPS row naming none lets a `ready: NO` report pass. | TEST |
| S9 | Sol | X1 | No `PIPE` trap: a SIGPIPE between bootout and bootstrap ends the shell without the restore. | TEST |
| S10 | Sol | D4 | The dry run prints the two `rev-parse` reads as one `;`-joined line and counts it once. | TEST |
| S11 | Sol | D4 | The dry run prints `git show main:src/cobalt/db_migrations/` after every ship; a run reads it first. | TEST |

## Dropped
none

## RUNS
Each test placed in the file it names with the Edit tool (no form repair), run on `bb59ba34`: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <the nine>` → `8 failed, 1 passed, 15 warnings in 7.49s`; S5 and S6 again alone → `2 failed`.

| id | source | run | output (first failing line) | verdict |
|---|---|---|---|---|
| S1 | Sol | COMMAND `grep -n -B2 -A1 '^export LC_ALL=C$' ops/desk/deploy-step0.sh` | `55-CALLER_LC_ALL=${LC_ALL-}` · `56-CALLER_LC_SET=${LC_ALL+set}` · `57:export LC_ALL=C` · `58-set -u` | HELD (the output shown; the build report's `## RECORDS` disclosed the two lines, no card line or ruling allows them) |
| S2 | Sol | TEST `test_deploy_smoke.py::test_a_malformed_smoke_row_is_red_instead_of_silently_ignored` | `assert 0 == 1` at `:261`; stdout ends `SMOKE GREEN`, no `malformed ·` line | HELD |
| S3 | Sol | TEST `test_deploy_outage.py::test_a_later_bootstrap_cannot_leave_an_earlier_label_down_on_success` | `assert ('com.cobalt.aset' in {'com.cobalt.radar': {… 'pid': 901}})` at `:491`; stdout `com.cobalt.aset · pid before 501 · pid after 900` · `OUTAGE DONE 0s` | HELD |
| S4 | Sol | TEST `test_deploy_step0.py::test_p7_rejects_a_number_prefixed_file_that_is_not_a_migration` | `assert 0 == 1`; the run ends `STEP-0 OK — window: (iii)` | HELD |
| S5 | Sol | TEST `test_deploy_step0.py::test_a_ruling_that_affirms_l66_does_not_open_the_window` | `assert 0 == 1` at `:481`; stdout `… holds: (iv) his per-case override 2026-01-02 R3` / `WINDOW (iv)` | HELD (`DEPLOY-HUB.md:59` (iv): "a row of `RULINGS` that overrules L66 / L43 for THIS deploy") |
| S6 | Sol | TEST `test_deploy_step0.py::test_an_uncommitted_override_rewrite_does_not_open_the_window` | `assert 0 == 1` at `:497`; stdout `WINDOW (iv)` | HELD (under `--window`, the path `deploy-outage.sh` takes; a full run's P0 `authorize.sh` proves each row at HEAD, `authorize.sh:110`) |
| S7 | Sol | COMMAND `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_outage.py::test_g1_…_kickstarted_by_the_trap` | `1 passed, 15 warnings in 1.63s` | the run house B wrote for OPEN G1: SETTLED (the defect fixed at `bb59ba34` is pinned by a passing test whose stub can come back; Grok's own test, whose stub stays OFFLINE on every read, cannot pass under any fix and is not kept) |
| S8 | Sol | TEST `test_deploy_step0.py::test_a_ships_row_cannot_erase_the_mandatory_clean_check_statuses` | `assert 0 == 1` at `:512`; the run ends `STEP-0 OK — window: (iii)` | HELD (the card's D1: "each head's check report stop line (`held unfixed: 0`, `ready: YES`, the code tip)") |
| S9 | Sol | TEST `test_deploy_outage.py::test_sigpipe_between_bootout_and_bootstrap_brings_every_label_up` | passed | NOT HELD (the shell's EXIT trap ran on SIGPIPE); removed again with the Edit tool before the red commit |
| S10 | Sol | TEST `test_deploy_step0.py::test_dry_run_prints_each_rev_parse_as_its_own_command` | `assert 2 == 4` at `:526`; two `…rev-parse … $ctip^{commit}; git … refs/heads/ops/<b>^{commit}` lines | HELD |
| S11 | Sol | TEST `test_deploy_step0.py::test_dry_run_prints_the_main_migration_listing_in_real_execution_order` | `assert 18 < 8` at `:543` (main's listing at index 18, alpha's at 8) | HELD |

Red commit before any fix: `973ea772 wip(deploy-steps): check red — S2 S3 S4 S5 S6 S8 S10 S11` (test files only; S9's test not in it).

## FIXES
One commit, `f04a1d56 fix(deploy-steps): step0 LC_ALL=C first, override must overrule and stand at HEAD, P2 always needs a clean check, P7 only NNNN_*.sql, dry run one command per line in run order; outage re-reads each label at the end; smoke rows out of form are RED (check S1 S2 S3 S4 S5 S6 S8 S10 S11)`, inside the rows' files (`ops/desk/deploy-step0.sh`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh`):

| id | fix |
|---|---|
| S1 | `deploy-step0.sh`: `export LC_ALL=C` is the first command; the two `CALLER_LC_*` lines are gone; P0 runs `LC_ALL=en_US.UTF-8 sh authorize.sh deploy "<card>"` (the table and the dry run name that command); header updated. After: `grep -n -B2 -A1 '^export LC_ALL=C$' ops/desk/deploy-step0.sh` → `58-# in tests/ops/test_deploy_step0.py only.` · `59-` · `60:export LC_ALL=C` · `61-set -u`. |
| S2 | `deploy-smoke.sh`: a `- ` line of `## MARKERS` or `## SMOKE READS` not in its row form is RED (`not a marker row` / `not a smoke read row`), labelled, never run; `--dry-run` prints `WOULD REFUSE`; header updated. Card 25's 10 markers and 13 smoke reads are all in form (Grep). |
| S3 | `deploy-outage.sh` step 3: each aset / radar of the set is re-read by `launchctl print`; one not running is put back in `down`, said (`<label> · not running at the final read (<state>): brought up again`) and brought up by step 2's calls, a failure there going to the trap; the dry run names the reads; header updated. |
| S4 | `deploy-step0.sh` P7: only `NNNN_*.sql` counts as an added migration (the listing's numbers and the diff's allowed lines); any other file under `db_migrations` is a stray change. |
| S5 | `deploy-step0.sh` (iv): the row must also hold `overrules` / `overruled` (`*[Oo]verrul*`). |
| S6 | `deploy-step0.sh` (iv): the row as read must stand in `git show HEAD:<cto report>` (authorize.sh's at-HEAD proof). |
| S8 | `deploy-step0.sh` P2: `held unfixed: 0` and `ready: YES` are always required, with the row's literals added. |
| S10 | `deploy-step0.sh` dry run: the two `rev-parse` reads are two `WOULD RUN` lines (the table column keeps them joined). |
| S11 | `deploy-step0.sh` dry run: `git -C <repo> show main:src/cobalt/db_migrations/` is printed before the ships, where a run reads it. |

After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/ops/test_deploy_step0.py tests/ops/test_deploy_outage.py tests/ops/test_deploy_smoke.py tests/ops/test_conftest_guard.py` → `92 passed, 15 warnings in 52.81s` (pass 1's 84 + the 8 held tests).
DevDocs line: as pass 1 found, no page under `docs/40 - DevDocs/cobalt/` documents `ops/desk/` scripts; none created. Each script's header carries the change.

## Suites
On `<tip now>` = `f04a1d56` (DB: none card: RESTARTS, then W (a0), (a), (e) and tests/ops):
- RESTARTS: `uv run cobalt jobs restarts a09f0862..HEAD` → exit 0; nine rows (`docs/…/deploy-steps-build-2026-10-03.md A DOCS -`, the three `ops/desk/deploy-*.sh A operator script; no Cobalt reader -`, the five `tests/ops/*.py A test/documentation; no resident -`), last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a09f0862` → the same nine paths, every one under `docs/`, `ops/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 9 paths)`.
- tests/ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `564 passed, 1 xfailed, 15 warnings in 250.33s (0:04:10)` (pass 1's 556 + the 8 pass-2 tests).
- (a) offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 619.57s (0:10:19)`, 0 failed, 0 errors (this pass adds no test there).
- (e) live-note: `ls <WT>/.env` → `No such file or directory`; `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.48s`; the skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`.
- cobalt_dev: not taken (DB: none); no lock, no `.env` at any step: `ls <WT>/.env` at 14:05 → `No such file or directory`.

## Scope
PREFLIGHT path union: the nine paths of pass 1 (`docs/…/deploy-steps-build-2026-10-03.md`, `ops/desk/deploy-{outage,smoke,step0}.sh`, `tests/ops/{conftest,test_conftest_guard,test_deploy_outage,test_deploy_smoke,test_deploy_step0}.py`). Pass 2's commits touch `ops/desk/deploy-step0.sh` (D1), `ops/desk/deploy-outage.sh` (D2), `ops/desk/deploy-smoke.sh` (D3) and their three test files: all inside the rows' files.

## Checked against the branch
- (i) `git log --oneline bb59ba34..HEAD -- . ":(exclude)docs"` → `f04a1d56 fix(deploy-steps): … (check S1 S2 S3 S4 S5 S6 S8 S10 S11)` · `973ea772 wip(deploy-steps): check red — S2 S3 S4 S5 S6 S8 S10 S11`. `<tip now>` = `f04a1d56`.
- (ii) `git log --stat --format=%h bb59ba34..HEAD` → `f04a1d56`: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh`, `ops/desk/deploy-step0.sh` · `973ea772`: `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_smoke.py`, `tests/ops/test_deploy_step0.py`. Every path in a row's files. No WIDENED.
- (iii) fence: `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" ops/desk/deploy-card.sh` → empty.
- (iv) Grep `def <test>`: S2 `tests/ops/test_deploy_smoke.py:256`; S3 `tests/ops/test_deploy_outage.py:481`; S4 `tests/ops/test_deploy_step0.py:454`, S5 `:473`, S6 `:485`, S8 `:501`, S10 `:516`, S11 `:530`; G1's pin `tests/ops/test_deploy_outage.py:444`. S1 is a COMMAND finding (its output re-run after the fix, `## FIXES`). `973ea772` (red) sits below `f04a1d56` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/deploy-steps-1003`.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. Carried.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: nothing to run.
- (viii) L32: the values here are constructed test values (pids 501–503 / 900–902, the 2026-01 test dates, `x-set`, `0002_beta.txt`) or repo facts (commits, paths, counts); none of his.

COUNTING (pass 2): findings 11 (S1–S11) · dropped 0 · held 9 (S1 S2 S3 S4 S5 S6 S8 S10 S11) · fixed 9 · held unfixed 0 (both passes) · S9 NOT HELD · S7 the run that settled pass 1's OPEN G1 · open 0.

## OPEN
none. Pass 1's one OPEN item, G1 (UNSETTLED), is settled by S7: `test_g1_an_agent_offline_at_the_final_status_is_kickstarted_by_the_trap` → `1 passed` on `bb59ba34` and inside the `92 passed` / `564 passed` runs on `f04a1d56`. Nothing goes to the follow-up list.

## CONTINUE
next: none — closed (the desk verifies and commits; no further pass)

## DECISIONS
none

## RECORDS
- Check of `deploy-steps`, pass 2: house B `Sol` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- House B Sol produced its list (`FINDINGS: 11`, its run `tokens used 261,619`); no house produced nothing; Grok was not launched in this pass (pass 1's house A).
- Dropped findings: none.
- S9's test (SIGPIPE) ran green on the tip and was removed with the Edit tool, never committed.
- Behaviour each fix chose, for the desk's reading: S1 — `authorize.sh` now runs in `en_US.UTF-8` whatever the caller's locale (before: the caller's); S3 — a label that dropped after its own bootstrap is brought up once more and the run can still end `OUTAGE DONE`, with a `brought up again` line (the house test asserts exit 0); S5 — an override row must say `overrules` / `overruled`.
- The `cd`, the house launch and the return: `## Files copied` last line (pass 2).
- No lock taken, no `.env` written, no extra lock take (DB: none).
- L74: the attribution reminder asking for a `Claude-Session:` line arrived again; recorded under `## L74` (pass 2), not acted on.
- No `REFUSED` command and no `CONTINUE` message in this pass.
- files opened: 21 — `CHECK-HUB.md`, the card, this report (pass 1), `ops/desk/stage-copy.sh`, the `git log -p` output, the Sol probe output, `HOUSE-INSTRUCTIONS.md` (pass 1's, for the house text), Sol's output, the build report (two sections), `DEPLOY-HUB.md` (worktree, P1–P7), `ops/desk/authorize.sh` (Grep), `prompts/2026-10-02/25-deploy-scripts-card.md` (Grep), `tests/ops/test_deploy_smoke.py`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, `ops/desk/deploy-step0.sh`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-smoke.sh`, `BUILD-HUB.md` (RESTARTS, W), the tests/ops output, the offline output.

CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · house B: Sol FINDINGS: 11 · findings: 11 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0
