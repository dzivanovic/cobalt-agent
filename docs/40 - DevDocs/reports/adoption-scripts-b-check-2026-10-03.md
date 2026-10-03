# adoption-scripts-b — check, pass 1 (2026-10-03)

## §0 Headline
- Check of `adoption-scripts-b` at `b7eeb80c`, pass 1, by this session alone (house A: none, overruled 2026-10-02 R47).
- 3 own findings, all run. Each reproduced as stated, and each is REJECTED by a card line or THE LOCK. None is fixed, so 3 stay open and go to `## DECISIONS`.
- No commit of mine. The suites stand as built: offline 3749/0, with-DB not run (DB: none), live-note 146/0, tests/ops 603 passed.
- Rows M1–M5 match the diff. M6's own grep proof reads `7`, not `0`. The builder raised this as their DECISION 2; it is O3 here.

## L74
The session's harness attribution reminder asked for a `Claude-Session:` line on commits. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" CHECK-HUB.md` | 0 output | nothing |
| card placeholders | `grep -n -E "«FIL[L]" <card>` | 0 output | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- <card>` | 0 | `4d56b0f67eab2934c82302cb35e0cb64d503b307` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | nothing |
| STANDING R60 (cto-2026-09-30) | grep / log -S | 0 | row 46 `HIS RULING` … `APPROVED`; `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (cto-2026-10-02; also HOUSE A overrule) | grep / log -S | 0 | row 54 `HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house …` `HIS RULING · APPROVED`; `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | grep / log -S | 0 | row 161 `HIS RULING · APPROVED`; `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | grep / log -S | 0 | row 164 `HIS RULING · APPROVED`; `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gates R17/R19 | not run | — | `HOUSE A: none — overruled 2026-10-02 R47`: PREFLIGHT runs no house gate and no probe |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Sat Oct  3 16:14:13 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-scripts-b2-1003` |
| tip | `git log --oneline -1` | 0 | `9694a679 docs(adoption-scripts-b): build report — b7eeb80c` (docs-only above TIP) |
| above tip | `git log --stat --format=%h b7eeb80c..HEAD` | 0 | `9694a679` — `.../adoption-scripts-b2-build-2026-10-03.md \| 226 +++` (docs only) |
| built | `tail -n 3 <REPORT>` | 0 | `BUILT · job: adoption-scripts-b · tip: b7eeb80c \| on 6251baeb \| migration: none \| offline 3749/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 6 of 6 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0` |
| range | `git log --oneline 6251baeb..b7eeb80c` | 0 | `b7eeb80c fix(adoption-scripts-b): M1-M4 ported …` · `289c7a0f wip(adoption-scripts-b): red — M1 M2 M3 M4 tests ported …` |
| range stat | `git log --stat --format=%h 6251baeb..b7eeb80c` | 0 | b7eeb80c: STANDING-LIST.md 2, desk-launch.sh 4, gate.sh 94, preflight.sh 30 · 289c7a0f: test_desk_launch_prechecks.py 40, test_gate.py 137, test_pass1_db_only.py 39, test_preflight.py 97 |
| lock (DB: none) | `ls <WT>/.env` | 1 | `No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames 6251baeb..b7eeb80c` | 0 | `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `ops/desk/gate.sh`, `ops/desk/preflight.sh`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_gate.py`, `tests/ops/test_pass1_db_only.py`, `tests/ops/test_preflight.py` — all under ops/, tests/ops/, docs/ |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47) |

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Read: the card; BUILD-HUB `## THE LOCK`, `## W`; the diff `6251baeb..b7eeb80c` (all 8 paths); `ops/desk/preflight.sh`, `ops/desk/gate.sh`, `ops/desk/take-devdb-lock.sh` and `ops/desk/desk-launch.sh` (the `field` / `tree_state` lines) at the tip; the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK`, `## DECISIONS` and its last line.

FINDING O1
ROW: M1 (X2)
CLAIM: `ops/desk/preflight.sh:114` strips `$REPO/` from a card path as well as `$dir/`, so for a check whose `CHECK REPORT` lives on the main checkout, an untracked worktree file at the same relative path is accepted, although it is not the card's report path (the script's own header, `:10`, says "inside this worktree").
RUN: TEST — `tests/ops/test_preflight.py`:
```python
def test_o1_a_worktree_file_at_the_check_reports_main_repo_path_is_not_the_report(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip, check_report=str(repo / CHECK_REL))
    untracked(job_wt, CHECK_REL)
    done = preflight(env, "check", card)
    assert last_line(done) == "FAILED PREFLIGHT: status"
```
EXPECT: on the tip it fails: `last_line(done)` is `PREFLIGHT OK`.

FINDING O2
ROW: M2 (X1)
CLAIM: M2 says "exit 4 only when that script exits 4"; `ops/desk/gate.sh:288` exits 4 after the take exited 0, when `$WT/*/.env` shows any other `.env`. A sibling `.env` without the mkdir lock (`take-devdb-lock.sh:47`) is not waited for: the take wins at once and the gate exits 4 at once.
RUN: COMMAND — `grep -n -F "not ours alone after the take" ops/desk/gate.sh`
EXPECT: `288:    [ "$held" = "$dir/.env" ] || { say "cobalt_dev lock not ours alone after the take — $held"; exit 4; }`

FINDING O3
ROW: M6
CLAIM: M6's red-first proof `grep -c -F ".claude/ops" docs/40 - DevDocs/prompts/STANDING-LIST.md → 0` is not met at the tip (build DECISION 2).
RUN: COMMAND — `grep -c -F ".claude/ops" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: `7`, not `0`.

Considered, no finding: X1 `--deploy` is set only by its own argument (`gate.sh:106`), refused outside `withdb`/`all` (`:112`), and `p1cmd=$PASS1` unchanged without it (`:428`). X1 uv-before-lock: `probe`/`withdb` call `take` first (`:414`, `:423`); `all` runs OFFLINE first (no `COBALT_ENV`), unchanged from BASE; no `cp` way is left (`:115-120`). X2 a second untracked line or a modified tracked one: the accept path needs exactly two lines (`preflight.sh:105`) and a `?? ` prefix (`:117`). M4: `grep -q '^TREE STATE:'` (`desk-launch.sh:508`) reads the whole card, as `field` (`:464`) does.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py::test_o1_a_worktree_file_at_the_check_reports_main_repo_path_is_not_the_report` | `1 failed, 15 warnings in 1.04s` · `E       AssertionError: assert 'PREFLIGHT OK' == 'FAILED PREFLIGHT: status'` | REJECTED — card M1 "(and, for a check, `CHECK REPORT`)". The check's report lives on the main checkout, so it can reach this worktree's status only at its relative path. The builder's `test_m1_a_check_with_its_untracked_check_report_alone_passes` pins exactly this case as intended. OPEN. The test was removed again so the suites stay green (it is quoted whole under `## OWN FINDINGS`). |
| O2 | own | `grep -n -F "not ours alone after the take" ops/desk/gate.sh` | `288:    [ "$held" = "$dir/.env" ] \|\| { say "cobalt_dev lock not ours alone after the take — $held"; exit 4; }` | REJECTED — BUILD-HUB THE LOCK (a)+(b): "Exit 0 → … `ls -la /Users/cobalt/cobalt-wt/*/.env` → EXACTLY one line, this worktree's". Card M5: "tests/ops/test_gate.py keeps both sides' changes", and `02`'s `test_a_sibling_env_is_a_held_lock_and_no_uv_runs` asserts `returncode == 4`. OPEN (the row's literal "exit 4 only when that script exits 4" is not met). |
| O3 | own | `grep -c -F ".claude/ops" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | `7` | REJECTED — NOT IN THIS JOB "any string on a launch line". The remaining hits include the `--add-dir /Users/cobalt/.claude/ops` roots on the launch lines (`:54`, `:109`, `:192`), and `02`'s A10 text at `:49` says that root "stays on each line". OPEN. |

## FIXES
none.

## Suites
suites: as built (no commit). From the build report: W (a) `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 570.29s (0:09:30)`; tests/ops `603 passed, 1 xfailed, 15 warnings in 205.38s (0:03:25)`; W (e) `146 passed, 1 skipped, 15 warnings in 25.83s`; with-DB not run (DB: none); `cobalt_dev: not taken (DB: none — 8 paths)`; RESTARTS: `RESTARTS: none`. `.env`: `ls /Users/cobalt/cobalt-wt/adoption-scripts-b2-1003/.env` → `No such file or directory` (16:17 ET).

## Scope
Path union `6251baeb..b7eeb80c`: `ops/desk/preflight.sh` (M1), `ops/desk/gate.sh` (M2, M3), `ops/desk/desk-launch.sh` (M4), `docs/40 - DevDocs/prompts/STANDING-LIST.md` (M6), and the tests `tests/ops/test_preflight.py`, `tests/ops/test_gate.py`, `tests/ops/test_pass1_db_only.py`, `tests/ops/test_desk_launch_prechecks.py` (the launcher's card test file, M4). All of these are in some row's `files`. My commits: none.

## Checked against the branch
- (i) `git log --oneline b7eeb80c..HEAD -- . ":(exclude)docs"` → nothing; `<tip now>` = `b7eeb80c`.
- (ii) `git log --stat --format=%h b7eeb80c..HEAD` → `9694a679`, the build report only (docs).
- (iii) `git log --oneline 6251baeb..HEAD -- CARD.md BUILD-HUB.md DEPLOY-HUB.md CHECK-HUB.md ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh ops/desk/gate-lists.md` → nothing.
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-scripts-b2-1003`.
- (vi) `git log --stat --format=%h 6251baeb..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing; `TREE STATE: unchanged` holds.
- (vii) no card record names an `ls`, `grep` or `git -C` command.
- (viii) L32: this report holds no ticker, price or date of his.
- No path reaches a score, rank, grade or size: the diff touches only operator scripts, their tests and one docs list.

## OPEN
- O1 (M1/X2) — REJECTED. A worktree file at the check report's main-repo relative path is accepted (`preflight.sh:114`). It would be settled by a desk word on whether M1's "for a check, `CHECK REPORT`" means this mapping. If not, drop the `"$REPO"/*` branch and flip `test_m1_a_check_with_its_untracked_check_report_alone_passes`.
- O2 (M2/X1) — REJECTED. `gate.sh:288` exits 4 after a take that exited 0, when a sibling `.env` sits beside it without the mkdir lock: the gate does not wait for it. It would be settled by a desk word on whether that should exit 4 (THE LOCK, `02`'s test) or something else. The behaviour itself (refuse, run no uv) is safe.
- O3 (M6) — REJECTED. The card's proof `grep -c -F ".claude/ops" … → 0` reads `7`. It would be settled by the desk rewording the proof (the builder used `grep -c -F "for the two lock scripts"` → `0`).

## CONTINUE
next: done

## DECISIONS
1. O1 (open, house B: none available): M1 accepts an untracked worktree file at the check report's main-repo relative path. Safe default taken: left as built, because the builder's test pins it as the card's "for a check, `CHECK REPORT`" clause. Ships to the follow-up list unless the judgment seat says otherwise. Not his.
2. O2 (open, house B: none available): `gate.sh:288` exits 4 after a successful take when another `.env` is present, against M2's literal "exit 4 only when that script exits 4". Safe default taken: left as built. THE LOCK's after-take proof and `02`'s test require this refusal, and it runs no uv. Not his.
3. O3 (open, house B: none available): M6's grep proof reads `7`, not `0`; this is the builder's DECISION 2. Safe default taken: left as built, because the remaining hits are launch-line roots the fence excludes. The desk words the proof. Not his.

## RECORDS
- No house: `HOUSE A: none — overruled 2026-10-02 R47` (proved under `## AUTHORIZATION`). `## 1` and `## 3` were not run, and `<S>` holds only `opus-1.md`.
- O1's test was added, run red, and removed with the Edit tool. `git status --short --branch` → `## ops/adoption-scripts-b2-1003`.
- L74: the harness's attribution reminder asking for a `Claude-Session:` line is recorded under `## L74`. I made no commit.
- No lock take (DB: none).
- files opened: 18 — CHECK-HUB.md, the card, BUILD-HUB.md (THE LOCK, W), the build report, areas/cobalt.md (What Cobalt is, Build rules down), ops/desk/preflight.sh, ops/desk/gate.sh, ops/desk/take-devdb-lock.sh, ops/desk/desk-launch.sh (grep), tests/ops/test_gate.py (diff, grep), tests/ops/test_preflight.py (diff, edit), tests/ops/test_desk_launch_prechecks.py (diff), tests/ops/test_pass1_db_only.py (diff), STANDING-LIST.md (diff, grep), DEPLOY-HUB.md (grep), cto-2026-09-30.md (grep), cto-2026-10-02.md (grep), tests/ops/test_desk_size_guard.py (grep hit).
- **Check of `adoption-scripts-b`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).**

CHECK DONE · job: adoption-scripts-b · pass: 1 · tip: b7eeb80c · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 18 · ready: YES · decisions: 3 · for Dejan: 0
