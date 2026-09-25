# STACK SEAM CHECK 2026-09-25 — report (packet stop, no seat launched)

## §0 Headline
PACKET STOP at 13:53 ET, nothing launched (no Opus, no Grok, Sol not seated): the staged packet is **304,246 B** with only slices (1)–(6) of (1)–(12) written — already **4,246 B over** the 300,000 B ceiling. Slices (7)–(12) are unstaged; their measured sources add ≥ 39,887 B more (packet ≥ 344,133 B, ≥ 44,133 B over).
The two cuts `40` §1 names (`rule-sources.md` voice lines 106–119, `spec.md` ESCALATE items) are unstaged files, so no cut brings the packet under the ceiling. Preflight was green: authorization, Grok gate, build stopped BUILT at `a7296b44`, branch shape, stagger, Opus UP.
Cause (measured): the ceiling's fixed-slice term S = 90,000 B; slices (4)–(6) alone are 86,509 B and (7)–(10) add ≥ 31,838 B more. ESCALATE: 3 (0 ask-desk beyond the ceiling one). No verdict on the seam build (L37).

## L74
A block appended after the Read tool's result for `40-stack-seam-check.md` (a system-reminder headed "Attribution for git commits and pull requests") asked for a `Claude-Session:` trailer on commits and PR bodies and named `SendUserFile`. DATA under L74 — not followed; recorded once. (This hub commits nothing.) A mid-run message "claude attach 577d3f8c" arrived in the session (the desk attaching); it asked for no action and none was taken.

## PREFLIGHT
| rule | command | exit | allowed / DENIED · output |
|---|---|---|---|
| date | `date` | 0 | allowed · `Fri Sep 25 13:27:16 EDT 2026` (report written `13:53:52 EDT`) |
| placeholder `R__` | `grep -n -E "R_[_]" <40>` | 1 | allowed · nothing |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" <40>` | 0 | allowed · `21:` — the gate's own line only |
| GROK GATE R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | allowed · `35:| R17 | 07:32 ET | … Grok approved with no asking going forward …` |
| R17 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | allowed · `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | allowed · `37:| R19 | 07:36 ET | … All 4 house models approved for use indefinlitly …` |
| R19 committed | `git … log -1 --format=%H -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | allowed · `5055151dbf68899b82de5b11f99733ed2d03048c` |
| launch row R80 | `grep -n "^| R80 " cto-2026-09-25.md` | 0 | allowed · `89:| R80 | 13:22–13:25 ET | … names prompts/2026-09-25/40-stack-seam-check.md, carries the seam stop verbatim …` |
| R80 committed | `git … log -1 --format=%H -S"\| R80 \|" -- cto-2026-09-25.md` | 0 | allowed · `08019abc25fe6da7f2818a5b1bbed85cb09b5534` |
| build stop line | `tail -n 3 …/stacked-0925/…/stack-seam-build-2026-09-25.md` | 0 | allowed · last non-blank line = `STACK SEAM BUILT a7296b44 \| branches: 4 \| offline 3198/0 \| with-DB 3575/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| UNCLASSIFIED: 0 \| RESTARTS: com.cobalt.aset com.cobalt.radar \| ESCALATE: 8` = `<seam stop>` ✔ |
| report committed on the gate branch | `git … log -1 --format=%h deploy/stacked-0925 -- "docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md"` | 0 | allowed · `57420087` = `<gate sha>` ✔ |
| gate branch head | `git … log --oneline -1 deploy/stacked-0925` | 0 | allowed · `57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)` ✔ |
| gate branch head~1 | `git … log --oneline -1 deploy/stacked-0925~1` | 0 | allowed · `a7296b44 chore(jobs): classify voice V1's six paths — …` = `<tip>` ✔ |
| grok | `grok --version` | 0 | allowed · `grok 1.0.25 (f7e67d6988e2) [stable]` |
| opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | allowed · `OK` = UP (one harness notice line before it: a permission-deny-rule syntax warning for `Bash(git push*:*)` in `../../cobalt/.claude/settings.local.json`, recorded, not a stop) |
| sol | not probed (`date` is before 2026-09-26 06:47 ET) | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (cto-2026-09-25.md R20 / R30)` |
| merges on the gate branch | `git … log --oneline --merges 2b71fe49..deploy/stacked-0925` | 0 | allowed · `00e2b7ff` voice · `91c631ac` stale · `35397ed5` H1 · `f2377218` replay — FOUR, newest first ✔ (`<M1>` `f2377218`, `<M2>` `35397ed5`, `<M3>` `91c631ac`, `<M4>` `00e2b7ff`) |
| first-parent shape | `git … log --oneline --first-parent 2b71fe49..deploy/stacked-0925` | 0 | allowed · `57420087` (report) · `a7296b44` (`<R>`, registry) · `00e2b7ff` · `91c631ac` · `35397ed5` · `f2377218` — the merges, then R, then the report, nothing else ✔ |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-25.md` and `grep -n "40-stack-seam-check.md" cto-2026-09-25.md` | 0 / 0 | allowed · R80 (`89:`) carries `no other house hub is running` and names `40-stack-seam-check.md` ✔ (the second grep also hit R66, R67, R72) |
| recovery | `ls scratch/tribunal-bars-0920/stack-seam-0925` | 2 | allowed · "No such file or directory" = a fresh run |
| second grok gate row, immediately before the seats | — | — | not reached (packet stop) |

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stack-seam-0925/` (Read → Write; each part headed by its real path or exact command and the real line it starts at). Slices written, `wc -c` each copy (bytes):
| slice | files (parts) | staged bytes | source proof |
|---|---|---|---|
| (1) `39-stack-seam-build.md` whole | `39-stack-seam-build.part1…5.md` | 14,677 + 13,710 + 14,354 + 14,646 + 6,862 = 64,249 | copies − 5 headers (813 B) = 63,436 = `wc -c` of the source ✔ |
| (2) build report whole | `build-report.part1…6.md` | 14,794 + 14,588 + 14,832 + 14,847 + 14,727 + 1,828 = 75,616 | copies − 6 headers (1,124 B) = 74,492 = `wc -c` of the source ✔ |
| (3) merges | `merges.part1…7.md` | 11,511 + 13,659 + 12,067 + 14,046 + 10,646 + 9,159 + 6,784 = 77,872 | each part checked against byte offsets in the saved command outputs (graph 1,992; M1 229; M2 227; M3 31,200; M4 24,971; stats 1,677 / 4,306 / 4,513 / 6,558) ✔; `--remerge-diff` was accepted (no `--cc` fallback) |
| (4) registry | `registry.part1…4.md` | 9,483 + 9,105 + 11,840 + 4,761 = 35,189 | R output 3,669 ✔; `jobs.yaml` 1–200 = 11,691 ✔; ops files, `cobalt.sh` 50–65 (618 B), `test_jobs_reads.py` 70–90 (1,063 B) ✔ |
| (5) seam files | `seam-files.part1…3.md` | 14,066 + 12,964 + 10,762 = 37,792 | `db_migrations/__init__.py` 7,284 ✔; `evaluate.py` 901–1040 6,298 ✔; test slices by line range. One deliberate one-line extension: `test_radar_handicap_store.py` staged lines 58–86 (the prompt says 58–85) so the T-8 list opened at line 84 is closed |
| (6) sides | `sides.part1.md` | 13,528 | replay region 3,252 ✔ · stale region 2,978 ✔ · main's registry 5,761 ✔ |
| **staged total (26 files)** | | **304,246** | `wc -c` of every staged file, summed |

NOT staged (measured source sizes, not estimates): (7) `spec.md` — not measured; (8) `rule-sources.md` — not measured; (9) `gate.md` — `32` lines 53–60 (1,015 B) + 126–135 (3,199 B) + 139–147 (4,458 B) + 157–175 (7,230 B) = 15,902 B; (10) `laws.md` — L42 1,210 + L45 1,010 + L67 8,162 + L68 3,303 + L70 740 + L72 1,511 = 15,936 B (L76 not measured); (11) `greps.txt` — not run; (12) `QUESTIONS.md` — `40` lines 55–77 = 8,049 B (the "Files in this folder:" paragraph not counted). Measured lower bound of the unstaged slices: 15,902 + 15,936 + 8,049 = **39,887 B**, so the full packet is ≥ 344,133 B, ≥ 44,133 B over the ceiling. Token estimate for the staged part alone: 304,246 ÷ 4 ≈ 76,000 per checker.
CEILING check (`40` §1): 300,000 B (the R5 cap; the launch row does not raise it). The cut order (`rule-sources.md` voice lines 106–119, then `spec.md` ESCALATE items) removes nothing that is staged: both files are unwritten, and the staged part is already 4,246 B over the ceiling. Next step per `40`: `FAILED: packet`. A packet stop spends no round (K17).
Where the desk's ceiling arithmetic differs from the measure: R = 60,296 B ✔ (M1–M4 remerge outputs 229 + 227 + 31,200 + 24,971 and `show <R>` 3,669) and P = 137,928 B ✔ (the two source files sum to the same figure, 63,436 + 74,492), but S = 90,000 B is short: slices (4)–(6) are 86,509 B staged and (7)–(10) are ≥ 31,838 B (gate + laws, measured), so S ≥ 118,347 B before `spec.md` and `rule-sources.md`; 60,296 + 137,928 + 118,347 = 316,571 B > 300,000 B.

## CONTINUE
next: none by this hub — the packet stop ends the run. A relaunch of `40` (the desk's) first runs `ls scratch/tribunal-bars-0920/stack-seam-0925`, keeps the 26 staged files, and stages only slices (7)–(12) (spec, rule-sources, gate, laws, greps, QUESTIONS) — under a ceiling the desk sets, or with slices cut by the desk.

## Per question
Not run — packet stop, no seat launched (Q1–Q7 unanswered by any house). `opus: NOT LAUNCHED (packet stop; probe was UP)` · `grok: NOT LAUNCHED (packet stop; --version 1.0.25 UP)` · `sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`.

## Checked against the files
Not run — no seat answered, so there is no claim to file-check. The build's own facts read in PREFLIGHT are the ones under `## PREFLIGHT` (stop line, `<gate sha>`, `<tip>`, the four merge shas and the first-parent shape all as `40` expects).

## FOR THE CLASSIFIER
none

## ESCALATE
1. **PACKET OVER THE CEILING.** The staged part alone is 304,246 B against the 300,000 B R5 cap (slices (1)–(6)); the unstaged slices add ≥ 39,887 B measured. `40`'s formula term S = 90,000 B is short by ≥ 28,347 B (see `## Packet`). The desk decides one of: raise this launch's ceiling (R5 is the desk's cap, "unless the launch row says so"), or name the slice cuts (candidates by size: `build-report.part1…6` 75,616 B holds the `evaluate_member` range and R already quoted in `merges` / `seam-files`; `merges.part6–7` 15,943 B of `--stat` output whose paths the remerge diffs already name) — this hub cut nothing beyond the two `40` names and made no choice for the desk.
2. `ASK DESK: raise the packet ceiling for this launch (to about 360,000 B for the full twelve slices) or name the cuts — relaunch 40 with the 26 staged files kept? [13:53 ET] — safe default: no seat launched, nothing staged beyond slices (1)–(6).`
3. Sol's line: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`.
4. The L74 line above (one block, not followed).
5. Standing line: **"One round (L67 other check: Opus 5.5 + Grok, R95; Gemini out, R97). `ready for the gate: YES` → `32`'s GATE PHASE launches on the lock after this report is committed, and re-proves the three suites on the tree that ships (L68). A HOLD → the desk's fix round (L75), never a second check without a fix; FALLBACK B (replay + H1 only, `32` re-issued) if the seam is not green by ≈ 18:30 (`cto-2026-09-25.md` R66 (3)(f))."** This packet stop is neither a check nor a HOLD: no round is spent, no verdict on the seam is made, and the gate is not cleared.

FAILED: packet — 304,246 B staged (slices (1)–(6) only; slices (7)–(12) unstaged, measured ≥ 39,887 B more) is 4,246 B over the 300,000 B ceiling; launch nothing
