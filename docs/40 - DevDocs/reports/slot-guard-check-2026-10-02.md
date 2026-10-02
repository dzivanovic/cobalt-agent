# slot-guard — check, pass 1 (2026-10-02)

## §0 Headline
- Check of `slot-guard` pass 1, 14:44–14:48 ET. Base `1df251b9`, tip `05c8b7fa`. No outside house (2026-10-02 R47).
- Two own findings (O1, O2), each run as a test. Both green: NOT HELD, and both tests removed. Held 0, fixed 0, open 0.
- No commit, so the build's suites stand: offline 3800/0 · with-DB 4572/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `RESTARTS: com.cobalt.radar`.
- Fence clean (hubs, `test_tenancy.py`, migrations untouched); `.env` absent in every worktree. ready: YES · house B: not needed.

## L74
A system block in this session asked commits to carry a `Claude-Session:` line after `Co-Authored-By`. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/13-slot-guard-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/13-slot-guard-card.md"` | 0 | `97bc8e8c1822739f9e2d0c40892936485ce2e179` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING (R60) | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R18 | `grep -n "^| R18 " ".../cto-2026-10-02.md"` | 0 | `25:| R18 | 06:23 ET | HIS RULING (L73 override of L61, this launch only) … | HIS RULING · APPROVED |` |
| R18 committed | `git -C … log -1 --format=%H -S"| R18 |" -- ".../cto-2026-10-02.md"` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| RULING R47 (HOUSE A: none) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| house gate R17 | `grep -n "^| R17 " ".../cto-2026-09-24.md"` | 0 | `35:| R17 | 07:32 ET | … STANDING: Bash(grok *) is a PRE-APPROVED string …` (one row) |
| house gate R19 | `grep -n "^| R19 " ".../cto-2026-09-24.md"` | 0 | `37:| R19 | 07:36 ET | … STANDING: the four house strings are pre-approved …` (one row) |
| R19 committed | `git -C … log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 14:44:28 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/slot-guard-1002` |
| tip | `git log --oneline -1` | 0 | `834d4c69 docs(slot-guard): build report — 05c8b7fa` |
| docs-only above tip | `git log --stat --format=%h 05c8b7fa..HEAD` | 0 | `834d4c69` · `.../reports/slot-guard-build-2026-10-02.md | 34 +++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: slot-guard · tip: 05c8b7fa | on 1df251b9 | migration: none | offline 3800/0 | with-DB 4572/0 (on 7eafd308) | live-note 146/0 (on 7eafd308) | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 1df251b9..05c8b7fa` | 0 | `05c8b7fa fix(slot-guard): the session-start hook pinned …` · `167d5a97 docs(slot-guard): build report — 7eafd308` · `6d152c2b wip(slot-guard): W (b) — cobalt_dev lock held by dev-rebuild-1002` · `7eafd308 feat(slot-guard): every db migrate prints the SLOTS line …` · `dda828fe wip(slot-guard): red — S1 S2 tests before any src edit` · `b6a3219b wip(slot-guard): E2 — red tests written …` · `dd60df2b wip(slot-guard): PREFLIGHT — cobalt_dev lock held by ops-seam-1002` (7 commits) |
| path union | `git log --stat --format=%h 1df251b9..05c8b7fa` | 0 | `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/conftest.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, `docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md` |
| lock, own | `ls /Users/cobalt/cobalt-wt/slot-guard-1002/.env` | 1 | `ls: …/slot-guard-1002/.env: No such file or directory` |
| lock, all | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)` — no house gate run as a launch gate, no probe (`## THE FLOW`, HIS PER-CASE OVERRULE) |

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` is not run.

## OWN FINDINGS
Written before any run. House A: none, so nothing under `<S>` exists to open.

FINDING O1
ROW: S1
CLAIM: S1 says every `cobalt db migrate` run prints the SLOTS line. One path is the forward run whose proof is `CHANGED`: it rolls back (`src/cobalt/db_migrations/cli.py:763`–`764`) and raises `MigrationError` (`:828`–`:832`). No test pins that this run still prints the SLOTS line before `code:`. `_migrate_output` stubs `_print_proof` to return 0 (`tests/cobalt/test_dev_rebuild_cli.py:337`).
RUN: TEST — `tests/cobalt/test_dev_rebuild_cli.py`:
```python
def test_check_o1_a_changed_forward_run_still_prints_the_slots_line(monkeypatch, capsys):
    conn = SlotConn([FULL])
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)
    monkeypatch.setattr(cli, "_probe_all", lambda c: {})
    monkeypatch.setattr(cli, "_apply", lambda c, paths: None)
    monkeypatch.setattr(cli, "_proof_verdicts", lambda *a, **k: {"t": "CHANGED"})
    monkeypatch.setattr(cli, "_print_proof", lambda *a, **k: print("<proof table>") or 1)
    monkeypatch.setattr(cli, "_code_line", lambda: "<code line>")
    with pytest.raises(cli.MigrationError):
        cli.cmd_migrate(argparse.Namespace(
            proof_only=False, rollback=False, down_to=None, allow_prod=False,
            lock_timeout_s=cli.DEFAULT_LOCK_TIMEOUT_S,
        ))
    lines = [l for l in capsys.readouterr().out.splitlines() if l.strip()]
    assert lines[-3:] == ["<proof table>", WARN_FULL, "<code line>"]
    assert conn.committed == 0 and conn.rolled_back >= 1
```
EXPECT: if the claim of a defect is true, `assert lines[-3:] == …` fails because the SLOTS line is missing on the refused run.

FINDING O2
ROW: S2
CLAIM: S2 says "Offline runs are untouched". The gate is `tests/cobalt/conftest.py:75`–`76`, and no added test runs the hook with the Postgres settings absent. If the gate failed open, the hook would open a connection on an offline run.
RUN: TEST — `tests/cobalt/test_dev_rebuild_cli.py`:
```python
def test_check_o2_the_hook_opens_nothing_without_the_postgres_settings(request, monkeypatch):
    from types import SimpleNamespace

    conftest = _suite_conftest(request)
    monkeypatch.delenv("POSTGRES_HOST", raising=False)
    monkeypatch.delenv("POSTGRES_USER", raising=False)
    opened = []
    monkeypatch.setattr(conftest, "REAL_CONNECT", lambda *a, **k: opened.append(a) or _Closable())
    config = SimpleNamespace(stash=pytest.Stash())
    conftest.pytest_sessionstart(SimpleNamespace(config=config))
    written: list[str] = []
    conftest.pytest_terminal_summary(SimpleNamespace(write_line=written.append), 0, config)
    assert opened == [] and written == []
```
EXPECT: if the claim of a defect is true, `assert opened == [] …` fails because the hook connected.

Other points I read and settled without a finding:
- The fix target `user.aset_sizings` is accepted by `cmd_dev_rebuild` (`cli.py:896`–`901`: schema in `SCHEMAS`, name `[a-z0-9_]+`).
- `tests/conftest.py:13` `load_dotenv()` runs before `tests/cobalt/conftest.py`, so the hook sees the same settings `dev_db_tx` (`conftest.py:199`) gates on.
- `db.connect` fails loud without `POSTGRES_HOST` (`src/cobalt/db.py:168`–`186`), so a hook that failed open would already break the offline suite.
- The 64-vs-65 headroom figure is ruled (R41, the card's RECORDS): L77, not reopened.
- No path from the diff reaches a score, rank, grade or size. `aset_sizings` is only read from the catalog.
- The fence holds: no hub file, no migration, no `test_tenancy.py`.
- The card has no `## CHECK ASKS`.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | Edit: test appended to `tests/cobalt/test_dev_rebuild_cli.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py::test_check_o1_a_changed_forward_run_still_prints_the_slots_line` | `1 passed in 0.05s` | NOT HELD — green; the refused forward run prints the SLOTS line before `code:` (`cli.py:823`–`827`). Test removed with the Edit tool. |
| O2 | Opus | Edit: test appended to `tests/cobalt/test_dev_rebuild_cli.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py::test_check_o2_the_hook_opens_nothing_without_the_postgres_settings` | `1 passed in 0.02s` | NOT HELD — green; with no Postgres settings the hook opens nothing and writes nothing. Test removed with the Edit tool. |

After both removals: `git status --short --branch` → `## ops/slot-guard-1002` (the tree is clean, at the tip).

## FIXES
none — nothing held.

## Suites
suites: as built (no commit). The build's lines (`<REPORT>` `## W`, stop line):
- offline `3800 passed, 678 skipped, 1 xfailed` on `05c8b7fa` → 3800/0
- with-DB pass 1 `4401 passed, 7 skipped, 65 deselected, 3 xfailed` + pass 2 `171 passed, 1 deselected` on `7eafd308` → 4572/0
- live-note `146 passed, 1 skipped` on `7eafd308` → 146/0
- `cobalt_dev: 0013 — F2 = F0` (`<F0>` = `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`); `.env: removed, proven gone (W)`
- `RESTARTS: com.cobalt.radar`

`05c8b7fa` differs from `7eafd308` only by three offline hook tests in `tests/cobalt/test_dev_rebuild_cli.py` (+72), as `git log --stat` shows above. This check took no lock and ran nothing against `cobalt_dev`.

## Scope
- PREFLIGHT path union: `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/conftest.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, and the build report.
- Every path is in the `files` of S1 or S2, or is the build report.
- This check made no commit.

## Checked against the branch
| # | command | output |
|---|---|---|
| (i) | `git log --oneline 05c8b7fa..HEAD -- . ":(exclude)docs"` | (nothing) — no commit of mine; `<tip now>` = `05c8b7fa` |
| (ii) | `git log --stat --format=%h 05c8b7fa..HEAD` | `834d4c69` · `.../reports/slot-guard-build-2026-10-02.md` only (docs) |
| (iii) hubs fenced | `git log --oneline 1df251b9..HEAD -- ".../BUILD-HUB.md" ".../CHECK-HUB.md" ".../DEPLOY-HUB.md"` | (nothing) |
| (iii) TestMigrationRoundTrip fenced | `git log --oneline 1df251b9..HEAD -- tests/cobalt/test_tenancy.py` | (nothing) |
| (iii) registry migrations, dev-rebuild CLI | `git log --stat --format=%h 1df251b9..HEAD -- src/cobalt/db_migrations tests/cobalt` | only `cli.py` (+33: `SLOT_WARN_AT`, `_slot_lines`, three call/print sites, `__all__`) and `dev_rebuild.py` (+68: the slot read) under `src/cobalt/db_migrations`; no migration file. `cmd_dev_rebuild` is not in the diff. |
| (iv) | — | no HELD finding |
| (v) | `ls /Users/cobalt/cobalt-wt/slot-guard-1002/.env` · `ls -la /Users/cobalt/cobalt-wt/*/.env` · `git status --short --branch` | `No such file or directory` · `no matches found` · `## ops/slot-guard-1002` |
| (vi) TREE STATE: row S1 | same as (iii), migrations / tests | no new migration; `tests/cobalt/test_dev_rebuild_db.py` modified (a with-DB test added in an existing file). The hub log (iii) is EMPTY by the card's `## NOT IN THIS JOB` ("`TREE STATE: row S1` therefore writes NO hub line") and RECORDS (R41: "that is not `TREE STATE NOT CARRIED`"). S1's with-DB test ran inside pass 1 as written: the build report's pass-1 `-rs` list has 7 SKIPPED lines, none of them this test, and the summary is `0 failed`. |
| (vii) | — | no card RECORDS line names an `ls`, `grep` or `git -C … log` command (`<SL>` is a `COBALT_ENV=dev … db query`, which this check does not run: no lock take) |
| (viii) L32 | — | this report quotes only the build's `cobalt_dev` catalog counts and the card's constructed test values; no ticker, price or date of his |

Counts: findings 2 (O1, O2; house A: none) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
none.

## RECORDS
- house A: none (overruled 2026-10-02 R47). `## 1` and `## 3` were not run, and no house was launched. `<S>` holds only `opus-1.md`.
- no house produced nothing; no `REFUSED, not needed` line; no `CONTINUED` line; no lock take.
- L74: one system block asked for a `Claude-Session:` commit line (`## L74`). Not acted on; this check made no commit.
- The card's TREE STATE note (its `## NOT IN THIS JOB`): S1's with-DB test `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` needs no migration above `0013`, and it ran in pass 1 as written. The build's `-rs` proof: 7 SKIPPED lines, none of them this test (`<REPORT>` `## W` (c), RECORDS).
- files opened: 8 —
  - `CHECK-HUB.md`
  - the card
  - `BUILD-HUB.md` (`## THE LOCK` … `## W`)
  - the build report (`## RESTARTS` … the last line)
  - `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down)
  - `tests/cobalt/conftest.py`
  - `src/cobalt/db_migrations/cli.py` (`cmd_migrate`, `cmd_dev_rebuild`)
  - `tests/cobalt/test_dev_rebuild_cli.py` (its end)
  - plus the diff `1df251b9..05c8b7fa -- src tests` as git output.
- Check of `slot-guard`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- final lock check 14:48 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`.

CHECK DONE · job: slot-guard · pass: 1 · tip: 05c8b7fa · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 8 · ready: YES · decisions: 0 · for Dejan: 0
