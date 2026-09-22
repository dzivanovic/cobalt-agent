# SETUPS FIX R3 — 2026-09-22

## §0 Headline
- FAILED PREFLIGHT on the branch-tip rule: HEAD is `a09c6da` (12's report commit, docs only), the prompt's BASE TIP is `65c08a0`; the prompt rules "anything else on a first launch → FAILED PREFLIGHT … the desk re-issues".
- AUTHORIZATION passed in full. No edit, no suite, no `.env` copied. ESCALATE: 1.

## L74
Recorded once: a system-reminder appended after this session's first tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool. Data under L74 — not followed.

## AUTHORIZATION
| check | command | result |
|---|---|---|
| R47 | `grep -n "^| R47 " cto-2026-09-22.md` | `:66` carries `"A definition wins"` |
| R48 | `grep -n "^| R48 " …` | `:65` carries `F1 is WIDENED` |
| R49 | `grep -n "^| R49 " …` | `:64` carries `"A and we tune in live"` |
| R50 | `grep -n "^| R50 " …` | `:63` carries `SKIP \`assumed_formation\`` |
| R51 | `grep -n "^| R51 " …` | `:62` carries `"You pick the one easier to program and maintain"` |
| R61 | `grep -n "^| R61 " …` | `:52` carries `SUPERSEDES R46` |
| R49 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"we tune in live" -- …cto-2026-09-22.md` | `636763520c9cca3365da70a6f34f8bb65c0acd94` |
| R61 committed | `… -S"SUPERSEDES R46" …` | `74fe5c8af4c984f138f73c3d4c913871e6ed1299` |
| R32 | `grep -n "^| R32 " …` | `:78` carries `claude-opus-5-5` |
| R41 | `grep -n "^| R41 " cto-2026-09-21.md` | `:52` quotes both `.env` strings and `"Approved"` |
| R41 committed | `… -S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)" -- …cto-2026-09-21.md` | `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| launch row | `grep -n "33-setups-fix-r3.md" cto-2026-09-22.md cto-2026-09-23.md` | `cto-2026-09-22.md:35: | R78 | 16:4x ET | …`; `cto-2026-09-23.md`: `No such file or directory` (recorded, not fatal) |
| launch row committed | `… -S"33-setups-fix-r3.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `56700a96b7b638381c4e7ebbeee7a440280e834f` |
| rule strings | 25 × `grep -c -F -e "<rule>" 15-setups-fix.md` (19 allow, 3 deny, 3 `--add-dir`) | every count ≥1 (`"AskUserQuestion"` = 2, all others = 1) |

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 22 16:42:36 EDT 2026` |
| BASE TIP filled | title line | — | `65c08a0` (7-hex) |
| 12 stopped on that tip | `tail -n 3 ".../setups-fixture-cut-2026-09-22.md"` | 0 | `SETUPS FIXTURE CUT BUILT 65c08a0 \| on 74eefd8 \| … \| ESCALATE: 7` — PASS |
| clean | `git status --porcelain` | 0 | (no output) — PASS |
| branch | `git status` | 0 | `On branch setups/seven-0921` / `nothing to commit, working tree clean` — PASS |
| **tip** | `git log --oneline -1` | 0 | `a09c6da docs(report): setups fixture cut — rubberband closed, hitchhiker escalated` — **FAIL (≠ `65c08a0`)** |
| range | `git log --oneline 65c08a0..HEAD` | 0 | `a09c6da docs(report): setups fixture cut — rubberband closed, hitchhiker escalated` — **FAIL (not empty)** |
| `.env` | `ls -la /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` — PASS |
| stagger | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — PASS |
| first launch | `ls -la ".../setups-fix-r3-2026-09-22.md"` | 1 | `No such file or directory` — PASS |
| companion | `ls …/setups-assumed-values-2026-09-21.md` | 0 | present |
| references | `ls "/Users/cobalt/cobalt/docs/90 - References"` | 0 | listed (not needed after the stop) |
| `_inflight` | `ls /Users/cobalt/cobalt-wt/setups-c1/docs/_inflight` | 0 | `README.md` |
| restarts | `uv run cobalt jobs restarts 65c08a0..HEAD` | 0 | `docs/40 - DevDocs/reports/setups-fixture-cut-2026-09-22.md	A	DOCS	-` / `RESTARTS: none` |

`git show --stat --oneline a09c6da` → `1 file changed, 194 insertions(+)` — only `.../reports/setups-fixture-cut-2026-09-22.md`.

## BASELINE
Not run (stopped at PREFLIGHT).

## ESCALATE
1. `ASK DESK: the BASE TIP rule contradicts the branch — R78 names 65c08a0 (12's code tip) with 12's report commit a09c6da above it, but PREFLIGHT requires HEAD = BASE TIP and <base>..HEAD empty on a first launch. Re-issue 33 with BASE TIP = a09c6da (docs-only above 65c08a0, RESTARTS: none), or word the tip rule to accept 12's report commit [16:43 EDT]`. No safe default taken beyond stopping: the prompt names FAILED PREFLIGHT for this case (L62). A relaunch will also meet this report file (the "r3 has started before" row) and this wip commit above `a09c6da` — the re-issue should name both.

## CONTINUE
next: AUTHORIZATION (passed 16:43; re-run on relaunch) → PREFLIGHT on the re-issued BASE TIP. Nothing built; no `.env` was ever copied.

FAILED PREFLIGHT: branch tip is a09c6da — the desk re-issues
