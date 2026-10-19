§0 Card 869 `hub-cos-restart-1019` preflight, read-only against `main` b8b2a393. 25 checks, 0 fails, ready YES. Nothing blocks the launch. Three NOTES below.

## CHECKS

| # | command · output | OK/FAIL |
|---|---|---|
| 1a | `git merge-base --is-ancestor bcbf08f9 main` · exit 0 (no output) | OK |
| 1b | `git log --stat bcbf08f9..main` · 1 commit, b8b2a393: the card 869, prompt 870, `cto-2026-10-19.md`, `draft-hub-cos-restart-2026-10-19.md`. None under `prompts/DEPLOY-HUB.md`, `ops/desk/` or `tests/` | OK |
| 2 | `grep -c "«FILL" <card>` · `0` | OK |
| 3 | card header read · `JOB: hub-cos-restart-1019`, `BRANCH: ops/hub-cos-restart-1019`, `WORKTREE: hub-cos-restart-1019`, `REPORT: …/hub-cos-restart-1019-build-2026-10-19.md`, `BAND: HIGH`, `## RULINGS`-line `RULINGS:` present, `LADDER: OFF-LADDER` present | OK |
| 4 | rows R1-R3 vs the brain's four points · R1 = F16 shape passes, unknown label still refused; R2 = not loaded → `com.cobalt.cos: not loaded — skipped`, a deploy never bootstraps; R3 = loaded cos bootout, wait, bootstrap after radar. The rest are consequent text/pin edits (`:3`, `:78`, `:94`, `:149`, `:153`). `NOT IN THIS JOB` keeps `orphan-clean.sh`, `:53`, `:150` and the F-14 order out (X3, X5) | OK |
| 5.1 | `git show main:…/DEPLOY-HUB.md` line 93 · `- GATE: exit 0 … within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\` (one, two, all three, or none)`, with the `minus every label of \`<deferred set>\`` clause and the `Anything else (…)` sentence | OK |
| 5.2 | same, line 94 · `- THE SET DRIVES THE REST: …`; the new line goes between 93 and 94; `P8 and D1 print \`com.cobalt.aset\` and \`com.cobalt.radar\` by name;` present | OK |
| 5.3 | same, line 122 · D1: `launchctl print gui/501/com.cobalt.radar\` → \`state = running\`, \`<radar pid>\`;` present | OK |
| 5.4 | same, line 139 · 4.2 `for each of \`com.cobalt.aset\`, \`com.cobalt.radar\` in \`<restart set>\``, `(ORPHAN-CLEAN, aset only; radar: no call, the script REFUSES it)` | OK |
| 5.5 | same, line 143 · 4.6 bootstrap strings aset / radar / `kickstart gui/501/com.cobalt.agent`, in that order | OK |
| 5.6 | same, line 150 · smoke (b) reads aset's and radar's logs only | OK |
| 5.7 | same, lines 149, 153, 154 · (a) `launchctl print aset / radar → running`; (e) `…com.cobalt.radar\` \`running … heartbeat fresh\``; (f) `\`RESTARTS:\` minus \`<deferred set>\` (as \`## RESTARTS\` records it)` | OK |
| 5.8 | `grep -n -E "aset\)\|label table\|JOB=\|PORT=" ops/desk/orphan-clean.sh` · `76: aset)` … `80: PORT=5010`, `82: *) refuse "label '$label' is not in the label table (aset)"`; aset only | OK |
| 5.9 | `grep -n "loop stamping" src/cobalt/heartbeat/probes.py` · `164: return Probe("cos", True, f"loop stamping …")` | OK |
| 5.10 | `jobs.yaml` 204-214 read · `206 - label: com.cobalt.cos`, `211 … pidfile is alive (F-14)`, `214 enabled: false` | OK |
| 5.11 | `grep -n` on `ops/desk/desk-launch.sh` · `1865: agent\|aset\|radar) refuse …`, `1918: launchd="… launchctl bootout … bootstrap gui/501 /Users/cobalt/cobalt/ops/$lab.plist"`, `2614: n=$(grep -c '^claude --bg ' "$fixed")`; `ls -l ~/.claude/ops/desk-launch.sh` → link to `/Users/cobalt/cobalt/ops/desk/desk-launch.sh` | OK |
| 5.12 | `grep -n` on the tests · `test_hub_deferred_1018.py:17 THREE`, `:57`, `:69`, `:74`, `:75`, `:76`, `:96 == 5`, `:105 assert COS not in launch`; `test_desk_launch_launchd.py:143 TODAY_EIGHT = 8`, `:149`, `:166`, `:181`, `:160 …radar)" <launchd strings>`. Line 11 holds 8 `Bash(launchctl …)` strings (2 bootout, 2 bootstrap, 2 `kickstart -k`, `print gui/501/*`, agent kickstart); +3 = 11 | OK |
| 5.13 | `grep -c -F "com.cobalt.cos"` on the hub · `0` (so both DEPLOY PROOF "before" counts are 0). `grep -n -o "com\.cobalt\.[a-z0-9-]+"` → only agent, aset, radar, herdr, mainframe, obsidian; herdr / mainframe / obsidian only on `:93`, which holds no `launchctl ` (so C2 is green on BASE) | OK |
| 6a | precedent · `tests/ops/test_hub_deferred_1018.py` (read whole; its docstring names `test_hub_text_1013.py`) and `test_hub_text_1013.py` exist (`ls`). Helpers `one()`, `lines()`, `section()`, `GATE`, `admits()` are in the form the card names | OK |
| 6b | RED by main's text · `four()` of `:93` = the three labels, so `admits({aset,cos,radar})` is False; no `- NOT LOADED` line; `:139` lacks cos. R1, R2, R3 fail, so `3 failed` | OK |
| 6c | CONTROLs green on BASE · C1: `admits({aset,herdr})` False, `admits({obsidian})` False, `Anything else (…)` text is on `:93`. C2: every `launchctl` hub line names only agent / aset / radar. So `2 passed`. New test file does not exist yet (`ls` → No such file), as it should before the build | OK |
| 7 | card `Scope` paragraph · "The changed `DEPLOY-HUB.md` is read by one other house before its deploy (L9, L67), and its deploy runs the gate on the merged hub text first (L68)" | OK |
| 8 | `grep -n "com.cobalt.radar" /Users/cobalt/.claude/ops/desk-launch.sh` · no output (also none in the repo file): `desk-launch.sh` carries no resident `launchctl` strings. They are literal text of `DEPLOY-HUB.md:11`. The card changes `:11` and says `desk-launch.sh` does not change (`NOT IN THIS JOB`; its `:1865` refusal stays) | OK |
| 9a | `git log -1 -- <card>` · `b8b2a393 docs(desk): K5 card 869 drafted, preflight 870 R2070` | OK |
| 9b | `git diff HEAD --stat -- <card>` · no output (clean, committed) | OK |

## ISSUES
- NOTE: card fields `TIP`, `CHECK REPORT`, `HOUSE B` are blank. They are the build's and check's, and the desk fills `HOUSE B` for the L9 read before the deploy.
- NOTE: BASE `bcbf08f9` is one docs-only commit behind `main` (b8b2a393). Nothing it touched is in the card's files.
- NOTE: smoke (e)'s new "cos probe green, `loop stamping`" holds only once `jobs.yaml` `com.cobalt.cos` reads `enabled: true`; today it is `false` and the probe says `unknown — NOT PROBED` (`probes.py:143`). The read applies only when cos is in `<restart set>`, which needs cos loaded, so it is the K4 bootstrap deploy that flips it. A question for the check, not a block.

PREFLIGHT DONE · card: hub-cos-restart-1019 · checks: 25 · fails: 0 · ready: YES
