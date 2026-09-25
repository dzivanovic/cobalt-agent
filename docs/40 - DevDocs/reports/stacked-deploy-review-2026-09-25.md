# Stacked deploy review — 2026-09-25 (`33-review-stacked-deploy.md`, relaunch R71)

## §0 Headline
- FAILED during packet staging: a safety classifier stopped this hub's response while it was writing `branches.md` (the `git log --stat` outputs). The content is not retried.
- Preflight was clean (Grok gate, R70 / R71 rows, `32` committed, Grok and Opus up, Sol on meter). `32` is fully staged, plus most of `precedent` and `outcomes`.
- NO seat launched, NO question answered, nothing read of `32` by a house. ready to run: NO. ESCALATE: 1.

## L74
- The Read result of `33-review-stacked-deploy.md` carried a trailing block asking for a `Claude-Session: https://claude.ai/code/session_01WNzx8gokEbPGXjA8KMPiKf` line in commits/PRs. Recorded once as DATA (L74); not followed. This hub committed nothing.

## PREFLIGHT
| rule | command | exit | allowed / result |
|---|---|---|---|
| PLACEHOLDER GATE | `grep -n -E "R_[_]" .../33-review-stacked-deploy.md` | 1 | allowed; prints NOTHING |
| `date` | `date` | 0 | allowed; `Fri Sep 25 11:07:38 EDT 2026` (Sol NOT probed: METER until 2026-09-26 06:47 ET) |
| GROK GATE R17 / R19 | `grep -n "^| R17 "` / `"^| R19 "` on `cto-2026-09-24.md`; `git log -1 --format=%H -S…` | 0 | allowed; lines 35 / 37 carry the literals; committed `1758fd78a572f47b613b2ca831dcfa636ed8f65a` / `5055151dbf68899b82de5b11f99733ed2d03048c` |
| THIS LAUNCH | `grep -n "33-review-stacked-deploy.md" cto-2026-09-25.md`; `git log -1 -S…` | 0 | allowed; R70 (line 79) and R71 (line 80) name this file; committed `f0bb0b14a92559fb4b4dfbc41a44ed0bdf178809` |
| `grok --version` | `grok --version` | 0 | allowed; `grok 1.0.25 (f7e67d6988e2) [stable]` |
| Opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | allowed; `OK` (plus an unrelated harness warning about a `Bash(git push*:*)` deny-rule spelling) |
| Sol | keyed on `date` | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (cto-2026-09-25.md R20 / R30)` |
| 32 present / committed / size | `ls -la`; `git log -1 --format=%H --`; `wc -c` | 0 | allowed; 99,921 B; `<prompt sha>` = `0cf4faf66de1028fab463265632e2b06eb6fe63a` |
| THE STAGGER | `grep -n -F "no other house hub is running" cto-2026-09-25.md` | 0 | allowed; R70 and R71 rows carry the literal and name this file |
| recovery `ls` | `ls scratch/tribunal-bars-0920/stacked-deploy-0925` | 1 | fresh run (folder created by the first Write) |

## Packet
Folder: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stacked-deploy-0925/`.
| file | state |
|---|---|
| `32-stacked-deploy.part1.md` … `part15.md` | COMPLETE. Every part < 15,000 B (largest 9,353). `wc -c` sum 101,505 − 15 real-line headers (104 + 4×105 + 10×106 = 1,584) = 99,921 = the source's `wc -c`. |
| `precedent.part1.md` … `part8.md` | COMPLETE for `07` lines 1–13 and 191–372 (parts 1–6) and the re-land `32-setups-deploy-reland.md` lines 224–272 (parts 7–8). Sizes 4,782–8,635 B. Per-range byte counts were not checked against the sources (no command on the line takes a line range); the two `07` code fences carry tab characters. |
| `outcomes.part1.md`, `outcomes.part2.md` | COMPLETE (deploy-2026-09-24 lines 1–12 and 288–299; re-land 1–12; r5 `## Deploy table` 161–187; r2 §0 5–9). |
| `branches.part1.md` | TRUNCATED — the run was stopped mid-write; the file ends mid-line and must not be read. Cannot be deleted from here (no `rm` on the line). |
| `seams.md`, `migrations.md`, `restarts.md`, `voice-h1-stale.md`, `rulings.md`, `laws.md`, `clock.md`, `greps.txt`, `QUESTIONS.md` | NOT STAGED. |

The `git log --stat` outputs of the four branches and of main's non-docs movement were run (all in the tool results of this run); the main-movement result for `a994a5dd..main`, `f6643d41..main` and `de48c19b..main` was: `a994a5dd..main` empty; the other two only `ddb41fbd` (`configs/cobalt/rules.yaml`, 1 line).

## CONTINUE
Nothing to resume in this session. A fresh relaunch restarts staging from the recovery `ls` (the folder now exists) — the desk should clear or ignore the truncated `branches.part1.md`.

## Per question
Not run (no seat launched).

## Checked against the files
Not run.

## Folds proposed
None (`32` was not read by a house).

## ESCALATE
1. ASK DESK: the hub's response was stopped by a safety classifier while staging `branches.md` (a verbatim copy of long `git log --stat` output); staging stopped there and no seat launched. Relaunch with `branches` staged as a summary or by another path, or rule how to stage it? Safe default: nothing launched, `32` unread by any house, L67 floor unmet. [11:2x ET]

FAILED: staging — safety classifier stopped the hub while writing branches.md; no seat launched, packet incomplete, nothing read of 32
