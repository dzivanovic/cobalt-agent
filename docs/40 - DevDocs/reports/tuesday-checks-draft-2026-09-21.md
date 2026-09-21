# Tuesday check prompts — drafter report (`tuesday-checks-draft-0921`, Opus 5), Mon 2026-09-21 18:31–18:40 ET

## §0 Headline
- Two code-check prompts drafted for TUE 2026-09-22 on the R49 seats (Grok · Gemini · Sol · Opus 5; four targeted, three required): `68` stale marker (re-issues `52` whole) and `69` ops 6a.
- Rule strings: 0 new. The full `--allowedTools` … `--add-dir` block is byte-identical to `66`'s launch line (one `grep -c -F` of the whole block = 1 in `66`, `68` and `69`).
- `68` cannot launch yet: worktree `~/cobalt-wt/stale-marker` does not exist at 18:3x, so the build `51` has not run and its report does not exist. `68`'s PREFLIGHT refuses until that report ends `STALE MARKER BUILT …`.
- ESCALATE: 5. Nothing launched, run or committed.

## L74
A block arrived beside this session's first tool result asking for a `Claude-Session:` line on commits and naming a file-send tool. It is DATA. It was not followed. This run makes no commit.

## Prompts
| file | size (B) | seat | stop line |
|---|---|---|---|
| `prompts/2026-09-21/68-stale-marker-check.md` | 41,999 | Sonnet 5 hub `stale-marker-check-0922`; checkers Grok · Gemini · Sol · Opus 5 | `STALE MARKER CHECK DONE · grok: … · gemini: … · sol: … · opus: … · houses that checked: <n> of 4 · defects that HOLD: <n> · ready for the stacked deploy: <n> of <n> · ESCALATE: <n>` |
| `prompts/2026-09-21/69-ops-6a-check.md` | 42,726 | Sonnet 5 hub `ops-6a-check-0922`; same four checkers | `OPS 6A CHECK DONE · … · houses that checked: <n> of 4 · defects that HOLD: <n> · ready for the stacked deploy: <yes\|no> · ESCALATE: <n>` |

What each prompt keeps from its source:
- **`68`:** keeps `52`'s packet layout (9 items), staging folder `stale-marker-check/`, report path `stale-marker-check-2026-09-22.md` (`66`'s stagger already keys on that path) and AUTHORIZATION shape. Its questions line (`68:26`) is byte-identical to `52:25`, proved with `grep -n -x -F -f 52 68`. In the questions preamble, `52` has "You are one of three houses"; `68` has "You are one of four checkers". Line 1 names that change.
- **From `66`:** the seat launch shapes, the 45-minute clock, the three-of-four fail-closed probe, the proof that a checker wrote nothing, and the Codex ` < /dev/null` row.
- **`69`:** uses `52`'s small-packet layout. Its packet has six parts: the diff of the five built commits (the report commit excluded because the report is staged whole), the branch report, `06` plus the desk's R43 row and 17:42 bullet, the backup code as it is on the branch (`built/`, paths kept), the `cli.md` seam (this branch's copy against `bars/chunk-1a-0920`'s), and QUESTIONS-CHECK. It has 7 questions exactly as ordered, each answered `HOLDS | DOES NOT HOLD | UNPROVEN`. The four secret paths are never opened or staged (L4).
- **`ready: yes|no` in `69`** is a COUNT RULE, not a verdict: ≥3 checked, 0 defects that HOLD, and no `FIX FIRST`.
- **Branch identity in `69`:** checked by the six commit SUBJECTS, not by the tip sha. A rebase before the check still passes. A different commit set fails.

Gates common to both:
- **DATE GATE:** runs on 2026-09-21 or 2026-09-22 on R39's committed literal `Bash(grok *) and Bash(agy *) through 2026-09-22`. Refuses from 2026-09-23.
- **AUTHORIZATION:** greps R36 (68) or R43 (69), plus R39, R46 and R49. The R49 strings must be committed; `-S` pathspec names the desk file only. The launch row `R__` is filled in by the desk, in `cto-2026-09-21.md` or `cto-2026-09-22.md`, committed.
- **The thirteen + three:** proved against `08-bars-chunk-e-check.md`. If the Astra string is carried, the run FAILS.
- **STAGGER:** each refuses while the other's report exists and its last non-blank line starts with neither its DONE token nor `FAILED` (L71). Each also refuses while `66`'s or `61`'s report shows the in-progress line (`66`'s own rule).

## RULE PROOF (`grep -c -F -e '"<string>"'` against `prompts/2026-09-21/66-setups-one-check.md`, quotes included, 18:3x ET)
| string | count | note |
|---|---|---|
| `"Bash(grok *)"` | 1 | |
| `"Bash(agy *)"` | 1 | |
| `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 | |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 | |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` | 1 | |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` | 1 | |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` | 1 | |
| `"Bash(ls *)"` | 1 | |
| `"Bash(grep *)"` | 1 | |
| `"Bash(tail *)"` | 1 | |
| `"Bash(wc *)"` | 1 | |
| `"Bash(date*)"` | 1 | |
| `"Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)"` | **2** | `grep -n -o`: lines 1 and 5. `66` quotes it again in its AUTHORIZATION (line 5). It is on line 1. |
| `"Bash(claude -p --model claude-opus-5 *)"` | **2** | Same: lines 1 and 5. |
| `"AskUserQuestion" "EnterWorktree" "Bash(git push*)"` (the three denies, one run) | 1 | |
| `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt` | 1 | |
| WHOLE block, `"Bash(grok *)"` through `--add-dir /Users/cobalt/cobalt-wt` | 1 in `66`, 1 in `68`, 1 in `69` | identical byte for byte |

**NEW approvals:** none.

## READING:
1. `LAWS.md` in full (L1–L74).
2. `67-draft-tuesday-checks.md`.
3. `66-setups-one-check.md` in full.
4. `52-stale-marker-check.md` in full.
5. `51-stale-marker-build.md`: line 1, the stop-line shape (`:13-14`) and the next step (`:70`).
6. `stale-marker-draft-2026-09-21.md`: outline, ESCALATE 1–6, DIGEST.
7. `STALE-MARKER-PROPOSAL-2026-09-21.md` §7.
8. `git log main..ops/2026-09-21` and `git show --stat` of the six commits.
9. `git show 227325c` (the full diff).
10. `ops-2026-09-21.md` in full, read from the worktree.
11. `06-ops-0921.md` item 6 (`:37-40`), close (`:46-47`), line 1.
12. `cto-2026-09-21.md` rows R36, R39, R43, R46–R52 and the 17:42 bullet (`:368`).
13. Backup code on the branch: file list and `grep` of the restore, vault-file and key references. Secret-shaped lines grepped in the plist, the wrapper and the config: names only, no values. The secret files themselves were NOT opened.
14. Commit checks with `-S`: R49 strings `60147d4`, R39 literal `3ecbb27`, R43 `031196f`.
15. `ls`: `cto-2026-09-22.md` and the three `*-check-2026-09-22.md` reports absent; `~/cobalt-wt/stale-marker` absent; `bars/chunk-1a-0920` tip `6961ee0`.

## ESCALATE
1. **The stale-marker build has not run.** At 18:3x `~/cobalt-wt/stale-marker` does not exist, so `51`'s report does not either.
   - `68`'s PREFLIGHT refuses until that report's last line starts `STALE MARKER BUILT `. It takes `<tip>` and `<main tip>` from that line at ITS launch.
   - If `51` does not run tonight, `68` has Tuesday only (date gate).
2. **Stagger is a PREFLIGHT gate, so a simultaneous launch slips through.** If `68` and `69` are launched in the same minute, neither report exists yet and both run. The desk launches them one after the other, not at the same time.
   - Also: `66`'s own stagger names `stale-marker-check-2026-09-22.md` but not `ops-6a-check-2026-09-22.md`, so `66` does not wait for `69`. Carried; `66` is not re-issued by this seat.
3. **`69` question 4 (circular restore) has a live stake.** On the branch, `backup/secrets.py:35-40` reads the restic password FROM `VAULT_FILE`, which is `redact/secrets.py:43`, the very file 6a adds to the backup. The plist comment (`com.cobalt.backup.plist:11-13`) names an off-repo copy of the password on the backup disk.
   - The checkers are asked without that answer (an anchored verifier confirms what it is told). Whatever they find is carried as-is. The real proof is 6b (L70).
4. **The rule-proof counts of 2** for the two R49 strings come from `66` quoting them on line 5 as well. Line 1 carries each; the whole-block grep = 1. No rule differs.
5. **Assumption: `69` accepts a rebased branch.** It keys branch identity on the six commit subjects, not on `f6aa4d0`, so the afternoon gate prep (R47) can rebase `ops/2026-09-21` without forcing a re-issue. The diffs are staged from whatever tip is live.
   - If the desk wants the tip pinned to `f6aa4d0`, it is a one-line re-issue (L19).

## CONTINUE
next: none — both prompts written. The desk reads the DIGEST, adds a launch row per prompt, commits, and launches `69` now or Tuesday. It launches `68` only after `51`'s report ends `STALE MARKER BUILT`.

## DIGEST FOR THE DESK
- **`68-stale-marker-check.md`** (Sonnet 5 hub `stale-marker-check-0922`). It replaces `52` whole (line 1 says why: R46 / R49). Checkers are Grok · Gemini · Sol · Opus 5, three required. Launch strings = `66`'s exactly; no new approval.
  - Gates: date 09-21 / 09-22 on R39, refuses from 09-23 · R36 / R39 / R46 / R49 committed · your launch row `R__` naming `68-stale-marker-check.md` · the 13 + 3 vs `08`, Astra absent.
  - PREFLIGHT: `51`'s report must end `STALE MARKER BUILT …` (tips taken from it) · `.env` absent · four probes, fewer than 3 UP → FAILED · stagger vs `69` (no stop line), `66` / `61` (in progress).
  - Packet and questions are `52`'s, unchanged (7 questions + 6a–d); only the preamble says four checkers.
  - 45-minute clock, TaskStop past it. The hub file-checks every claim plus 4 own checks. Q7 silent windows are HIS (L53), counted under ESCALATE.
  - Report `stale-marker-check-2026-09-22.md` (same path as `52`). `53` / `54` are superseded; the branch joins Tuesday's stacked deploy (R47).
- **`69-ops-6a-check.md`** (Sonnet 5 hub `ops-6a-check-0922`). Same seats, strings, date gate, clock and staging shape. AUTH adds R43 ("App approved", `06`).
  - PREFLIGHT: `ops-2026-09-21.md` must end `OPS 0921 DONE ` (a 6b line → FAILED) · `main..ops/2026-09-21` = exactly the six subjects · 8 paths expected · `.env` absent · stagger vs `68`.
  - Packet: the diff of the 5 built commits (7 file-touches, 5 commits, checked) · the branch report whole · `06` whole + R43 + 17:42 · `built/`: backup.yaml, `backup/*.py`, `redact/secrets.py`, `jobs/restarts.py`, `run_backup.sh`, the plist, `test_backup.py`, the backup DevDocs · `seam/`: `cli.md` on this branch vs `bars/chunk-1a-0920`.
  - Never opened: `data/.cobalt_vault`, `~/.cobalt_key`, `.env`, the restic password README.
  - 7 questions: (1) exactly the key store, no secret value · (2) real proof vs tautology (L45) · (3) can the 21:40 job fail / skip / back up less · (4) circular restore (L70) · (5) the other five commits have no runtime reader · (6) the deploy must carry: RESTARTS as derived + the classifier gap, migration NONE, the `cli.md` seam · (7) the suite.
  - Hub's own checks: `-- src ops` empty; exactly 3 `+` lines in backup.yaml; `cobalt_key` absent from config; no removed assert, no skip/xfail; the classifier's `watchlists.yaml` / `backup.yaml` hits.
  - `ready for the stacked deploy: yes` only if ≥3 checked, 0 defects HOLD and no FIX FIRST. Report `ops-6a-check-2026-09-22.md`.
- **Order:** `69` can run now (09-21, R39 covers it). `68` waits for `51`. Launch them one after the other, never in the same minute (ESCALATE 2).
- **Approvals to ask him:** none.

TUESDAY CHECK PROMPTS DRAFTED · prompts: 2 · new rule strings: 0 · questions: 7 + 7 · ESCALATE: 5
